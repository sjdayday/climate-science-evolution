"""Shared OpenAlex helpers for the climate-science-evolution scripts.

The API key is read from the environment variable OPENALEX_API_KEY and is
never written to any file.  Without a key OpenAlex serves a small per-IP
daily budget (~50 requests); with a key each request costs about
0.0001 USD (see https://docs.openalex.org).

    export OPENALEX_API_KEY=...        # your key
    python3 scripts/openalex_traces.py # etc.

Only the standard library is required (urllib); `requests` is not needed.
"""
import json, os, sys, time, urllib.parse, urllib.request

BASE = "https://api.openalex.org/"


def _key():
    k = os.environ.get("OPENALEX_API_KEY", "").strip()
    if not k:
        sys.stderr.write("warning: OPENALEX_API_KEY not set; running keyless (small daily budget)\n")
    return k


def get(path, params=None, retries=6, sleep=0.15):
    """GET an OpenAlex endpoint and return parsed JSON.

    `path` is e.g. 'works/W2174335611' or 'works'; `params` a dict of query
    parameters.  Retries on 429/5xx with exponential backoff.  Returns
    {'__404': True} for a 404 so callers can skip missing records.
    """
    params = dict(params or {})
    k = _key()
    if k:
        params["api_key"] = k
    url = BASE + path + ("?" + urllib.parse.urlencode(params) if params else "")
    delay = 1.0
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "climate-science-evolution/0.2"}), timeout=60) as r:
                data = json.loads(r.read().decode("utf-8"))
                time.sleep(sleep)
                return data
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return {"__404": True}
            if e.code in (429, 500, 502, 503, 504):
                time.sleep(delay); delay = min(delay * 2, 30); continue
            raise
        except (urllib.error.URLError, TimeoutError):
            time.sleep(delay); delay = min(delay * 2, 30)
    return {"__fail": True, "url": url.replace(k, "REDACTED") if k else url}


def short_id(x):
    """'https://openalex.org/W123' -> 'W123'"""
    return x.replace("https://openalex.org/", "") if isinstance(x, str) else x


def resolve_doi(doi, select="id,doi,title,publication_year,cited_by_count,referenced_works_count"):
    """Resolve a DOI to an OpenAlex work (or None)."""
    j = get("works/https://doi.org/" + doi, {"select": select})
    return None if j.get("__404") or j.get("__fail") else j


def title_search(title, year=None, per_page=8, select="id,doi,title,publication_year,cited_by_count,referenced_works_count,biblio,primary_location,authorships"):
    """Search works by title (optionally within year±1), best-cited first."""
    q = " ".join(ch if ch.isalnum() or ch == " " else " " for ch in title).split()
    filt = "title.search:" + " ".join(q)[:200]
    if year:
        filt += f",publication_year:{int(year)-1}-{int(year)+1}"
    j = get("works", {"filter": filt, "sort": "cited_by_count:desc", "per-page": per_page, "select": select})
    return j.get("results", [])


def citation_curve(work_id):
    """Citations per publication year: {year: count}. One request."""
    j = get("works", {"filter": "cites:" + short_id(work_id), "group_by": "publication_year"})
    return {int(g["key"]): g["count"] for g in j.get("group_by", []) if str(g["key"]).isdigit()}


def early_adopters(work_id, year, window=8, per_page=20):
    """Most-cited works citing `work_id` within `window` years of `year`."""
    j = get("works", {"filter": f"cites:{short_id(work_id)},publication_year:{year}-{year+window}",
                      "sort": "cited_by_count:desc", "per-page": per_page,
                      "select": "id,title,publication_year,cited_by_count,authorships,primary_location"})
    out = []
    for w in j.get("results", []):
        src = ((w.get("primary_location") or {}).get("source") or {}).get("display_name", "")
        auth = "; ".join((a.get("author") or {}).get("display_name", "") for a in (w.get("authorships") or [])[:2])
        out.append({"year": w.get("publication_year"), "cited_by": w.get("cited_by_count"), "authors": auth,
                    "title": w.get("title"), "venue": src, "id": short_id(w["id"])})
    return out, (j.get("meta") or {}).get("count")


def referenced_works(work_id):
    j = get("works/" + short_id(work_id), {"select": "referenced_works"})
    return [short_id(x) for x in j.get("referenced_works", [])]
