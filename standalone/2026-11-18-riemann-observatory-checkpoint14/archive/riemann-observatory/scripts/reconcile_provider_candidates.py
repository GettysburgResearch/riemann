#!/usr/bin/env python3
"""Reconcile provider identities without modifying candidate or canonical masters."""
import argparse
from collections import Counter, defaultdict
from hashlib import sha256
import json
from pathlib import Path
import re
import unicodedata
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
ARXIV = r"(?:\d{4}\.\d{4,5}|[a-z][a-z0-9.-]*/\d{7})"
MANIFEST_FIELDS = (
    "manifestations", "manifestation_records", "additional_manifestations", "source_manifestation_overlays",
)
REGISTRY_EVIDENCE = "provider_duplicate_registry_evidence_round10.jsonl"
DOI_FIELDS = ("doi", "arxiv_doi", "journal_doi", "alternate_doi")
URL_FIELDS = ("canonical_url", "canonical_urls", "source_url", "source_urls", "arxiv_url", "journal_url", "journal_source_url")
DISTINCT_FLAGS = {
    "CAND-222B3D9BEA97": "Seelhoff citations have different volume/issue/page locators (8/1/26 and 7/3/264); retained as separate publications at metadata level.",
    "CAND-8C6F9F293ABE": "Carlitz/Chowla and Mordell have different bylines and journals; same title is insufficient.",
    "CAND-04816C4BC49E": "Two Lubkin DOI records have disjoint starting pages 105 and 195 in the same issue; retained as separate publication units.",
    "CAND-7BEBB9D40772": "Two Physical Review Letters locators have separate issue/pages and the Journal of Mathematical Physics item is a separately published article. Their relationships require a source comparison.",
    "CAND-9E12BE48B636": "The conference chapter and monograph differ in coauthor, publication type and DOI.",
    "CAND-1577E014E2E9": "Separate Cambridge book identifiers identify different volumes; a shared title is insufficient.",
    "CAND-C97C8B8CB3BF": "Separate Cambridge book identifiers identify Broughan volumes I and II; a shared title is insufficient.",
}


def read_jsonl(path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def write_jsonl(path, rows):
    path.write_text("".join(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n" for row in rows),
                    encoding="utf-8")


def strings(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, list):
        for member in value:
            yield from strings(member)


def doi(value):
    value = unquote(value).strip().lower()
    value = re.sub(r"^(?:https?://(?:dx\.)?doi\.org/|doi:\s*)", "", value)
    return value if re.fullmatch(r"10\.\d{4,9}/[^\s?#]+", value) else None


def arxiv(value):
    value = unquote(value).strip().lower()
    value = re.sub(r"^(?:https?://(?:www\.)?arxiv\.org/(?:abs|pdf)/|arxiv\s*:?\s*|(?:10\.48550/)?arxiv\.)", "", value)
    value = value.removesuffix(".pdf")
    result = re.fullmatch(rf"({ARXIV})(v\d+)?", value)
    return result.groups() if result else (None, None)


def norm(text):
    decomposed = unicodedata.normalize("NFKD", (text or "").casefold())
    return " ".join(re.findall(r"[^\W_]+", "".join(c for c in decomposed if not unicodedata.combining(c))))


def title_authors(row):
    authors = tuple(sorted(norm(name) for name in row.get("authors", []) if norm(name)))
    return norm(row.get("title")), authors


def version_family(identifier):
    rules = (
        r"(10\.33774/coe-[0-9]+-[a-z0-9]+)(?:-v\d+)?",
        r"(10\.21203/rs\.3\.rs-\d+)/v\d+",
        r"(10\.20944/preprints\d+\.\d+)\.v\d+",
        r"(10\.26434/chemrxiv\.\d+)/v\d+",
        r"(10\.31219/osf\.io/[a-z0-9]+)(?:_v\d+)?",
        r"(10\.13140/rg\.2\.2\.\d+\.\d+)(?:/\d+)?",
    )
    for rule in rules:
        match = re.fullmatch(rule, identifier)
        if match:
            return match[1]
    return None


def identity_keys(obj):
    result = set()
    for field in (*DOI_FIELDS, *URL_FIELDS, "arxiv", "arxiv_id", "openalex_id"):
        for value in strings(obj.get(field)):
            identifier = doi(value)
            base, _ = arxiv(identifier if identifier else value)
            if identifier:
                result.add("doi:" + identifier)
            if base:
                result.add("arxiv:" + base)
            parts = urlsplit(value)
            host = parts.hostname
            if host in {"openalex.org", "api.openalex.org"} and re.fullmatch(r"/(?:works/)?w\d+", parts.path, re.I):
                result.add("openalex:" + parts.path.split("/")[-1].upper())
            elif host and parts.path.strip("/") and not identifier and not base:
                result.add("url:" + host.removeprefix("www.") + parts.path.rstrip("/") + ("?" + parts.query if parts.query else ""))
    return result


def read_provider_details(corpus, candidates):
    """Get primary publication coordinates from the original provider caches."""
    locations = defaultdict(set)
    for row in candidates:
        for evidence in row.get("metadata_evidence", []):
            locations[evidence["file"]].add(row["openalex_id"])
    details = {}
    pinned = {row["raw_file"]: row["sha256"] for row in read_jsonl(corpus / "raw_discovery_index.jsonl")}
    for name, wanted in sorted(locations.items()):
        path = corpus.parent / name
        if not path.is_file():
            raise ValueError(f"Provider snapshot required for the journal-coordinate check: {name}")
        raw = path.read_bytes()
        if sha256(raw).hexdigest() != pinned.get(name):
            raise ValueError(f"Provider snapshot does not match its pinned hash: {name}")
        snapshot = json.loads(raw)
        for row in snapshot["result"]["results"]:
            if row["id"] in wanted:
                details.setdefault(row["id"], row)
    return details


def journal_anchor(row, raw):
    location = raw.get("primary_location") or {}
    source = location.get("source") or {}
    biblio = raw.get("biblio") or {}
    title, authors = title_authors(row)
    positions = tuple(biblio.get(key) for key in ("volume", "first_page", "last_page"))
    serial = source.get("issn_l") or source.get("id")
    if serial and title and authors and all(positions) and source.get("type") == "journal":
        return "journal:" + "|".join((serial, *positions, title, *authors))
    return None


def exact_keys(row, raw):
    keys = identity_keys(row)
    identifier = doi(row.get("doi") or "")
    if identifier:
        family = version_family(identifier)
        if family:
            keys.add("version-series:" + family)
    signature = journal_anchor(row, raw)
    if signature:
        keys.add(signature)
    # An explicit arXiv location supplied for the same OpenAlex work is a
    # manifestation link. Its exact arXiv base can bridge a publisher DOI.
    for location in raw.get("locations") or []:
        for field in ("doi", "landing_page_url", "pdf_url"):
            value = location.get(field)
            if value:
                base, _ = arxiv(doi(value) or value)
                if base:
                    keys.add("arxiv:" + base)
    return keys


def recorded_registry_keys(corpus):
    path = corpus / REGISTRY_EVIDENCE
    keys = defaultdict(set)
    if not path.is_file():
        return keys
    for entry in read_jsonl(path):
        identifier = entry["doi"]
        if entry.get("status") != "retrieved" or entry.get("returned_doi") != identifier:
            continue
        relations = entry.get("relations", {})
        if isinstance(relations, list):
            relations = [(row["relationType"], row["relatedIdentifier"], row["relatedIdentifierType"])
                         for row in relations]
        else:
            relations = [(kind, row["id"], row["id-type"]) for kind, rows in relations.items() for row in rows]
        subject = "doi:" + identifier
        for kind, value, kind_id in relations:
            name = re.sub("[^a-z]", "", kind.casefold())
            if name not in {"isversionof", "hasversion", "isidenticalto", "ispreprintof", "haspreprint"}:
                continue
            if kind_id.lower() == "doi" and doi(value):
                target = "doi:" + doi(value)
            elif kind_id.lower() == "arxiv" and arxiv(value)[0]:
                target = "arxiv:" + arxiv(value)[0]
            else:
                continue
            if name in {"hasversion", "haspreprint"}:
                anchor = "registry-work:" + subject
            elif name in {"isversionof", "ispreprintof"}:
                anchor = "registry-work:" + target
            else:
                anchor = "registry-identity:" + "|".join(sorted((subject, target)))
            keys[subject].add(anchor)
            keys[target].add(anchor)
    return keys


def canonical_anchors(papers):
    indexed = defaultdict(dict)
    titles = defaultdict(set)
    for paper in papers:
        ident = paper["id"]
        titles[title_authors(paper)].add(ident)
        contexts = [("canonical", paper)]
        for field in MANIFEST_FIELDS:
            values = paper.get(field, [])
            if isinstance(values, list):
                contexts.extend((field, item) for item in values if isinstance(item, dict))
        for field, item in contexts:
            for key in identity_keys(item):
                indexed[key].setdefault(ident, set()).add(field)
        direct = paper.get("candidate_id") or (paper.get("other_identifiers") or {}).get("candidate")
        if direct:
            indexed["candidate:" + direct][ident] = {"explicit_canonical_candidate_id"}
    return indexed, titles


def reconcile(candidates, papers, details, registry):
    rows = {row["candidate_id"]: row for row in candidates}
    by_paper = {row["id"]: row for row in papers}
    known, titles = canonical_anchors(papers)
    keys_by_id = {ident: exact_keys(row, details.get(row["openalex_id"], {})) for ident, row in rows.items()}
    matches = {}
    for ident, keys in keys_by_id.items():
        found = defaultdict(dict)
        for key in sorted(keys | {"candidate:" + ident}):
            for paper_id, field in known.get(key, {}).items():
                found[paper_id][key] = sorted(field)
        matches[ident] = dict(found)

    parent = {ident: ident for ident in rows}

    def find(ident):
        while parent[ident] != ident:
            ident, parent[ident] = parent[ident], parent[parent[ident]]
        return ident

    def join(left, right):
        a, b = find(left), find(right)
        if a != b:
            parent[max(a, b)] = min(a, b)

    evidence_groups = defaultdict(list)
    for ident, keys in keys_by_id.items():
        merged = keys | set().union(*(registry.get(key, set()) for key in keys if key.startswith(("doi:", "arxiv:"))))
        for key in merged:
            if not key.startswith("url:"):
                evidence_groups[key].append(ident)
        if len(matches[ident]) == 1:
            evidence_groups["canonical-work:" + next(iter(matches[ident]))].append(ident)
    accepted_groups = defaultdict(set)
    for key, ids in evidence_groups.items():
        if len(ids) < 2:
            continue
        if key.startswith("version-series:") and len({norm(rows[ident]["authors"][0]) for ident in ids
                                                      if rows[ident]["authors"]}) != 1:
            continue
        if key.startswith("arxiv:") and len({title_authors(rows[ident])[0] for ident in ids}) != 1:
            primary = [ident for ident in ids if key in identity_keys(rows[ident])]
            if len(primary) < 2:
                continue
            ids = primary
        for ident in ids:
            accepted_groups[ident].add(key)
        for ident in ids[1:]:
            join(ids[0], ident)

    grouped = defaultdict(list)
    for ident in rows:
        grouped[find(ident)].append(ident)
    group_of = {ident: tuple(sorted(ids)) for ids in grouped.values() for ident in ids}
    crosswalk = []
    for ident, row in rows.items():
        peers = group_of[ident]
        canonical = set().union(*(matches[peer].keys() for peer in peers))
        target = next(iter(canonical)) if len(canonical) == 1 else None
        exact = sorted(set().union(*(accepted_groups[peer] for peer in peers)))
        if target:
            work_id = target
            qualification = "exact_canonical_record_link" if target in matches[ident] else "inherited_exact_metadata_link"
        elif len(peers) > 1:
            work_id = "WORK-OA-" + rows[peers[0]]["openalex_id"].rsplit("/", 1)[-1]
            qualification = "exact_metadata_cluster_with_canonical_conflict" if canonical else "exact_provider_metadata_cluster"
        else:
            work_id = "WORK-OA-" + row["openalex_id"].rsplit("/", 1)[-1]
            qualification = "ambiguous_canonical_identifiers" if canonical else "provider_identity_only"
        keys = keys_by_id[ident]
        crosswalk.append({
            "candidate_id": ident,
            "openalex_id": row["openalex_id"],
            "work_id": work_id,
            "identity_status": qualification,
            "canonical_paper_id": target,
            "canonical_selection_status": by_paper[target]["selection_status"] if target else None,
            "canonical_record_path": by_paper[target]["record_path"] if target else None,
            "canonical_access_status": by_paper[target]["access_status"] if target else None,
            "direct_canonical_identifier_evidence": matches[ident],
            "canonical_identifier_conflicts": sorted(canonical) if len(canonical) > 1 else [],
            "metadata_cluster_members": list(peers) if len(peers) > 1 else [],
            "metadata_cluster_evidence": exact,
            "title_author_review_only": sorted(titles.get(title_authors(row), set()) - canonical),
            "doi": doi(row.get("doi") or ""),
            "arxiv_ids": sorted(key[6:] for key in keys if key.startswith("arxiv:")),
            "provider_evidence": row.get("metadata_evidence", []),
        })
    return crosswalk


def review_flags(candidates, crosswalk, details):
    rows = {row["candidate_id"]: row for row in candidates}
    links = {row["candidate_id"]: row for row in crosswalk}
    seen = set()
    reviews = []
    for row in rows.values():
        if not row.get("possible_duplicate_ids"):
            continue
        ids = tuple(sorted([row["candidate_id"], *row["possible_duplicate_ids"]]))
        if ids in seen:
            continue
        seen.add(ids)
        if not all(set(rows[ident]["possible_duplicate_ids"]) == set(ids) - {ident} for ident in ids):
            raise ValueError(f"Original flags no longer form a symmetric title cluster: {ids}")
        mapped = {links[ident]["work_id"] for ident in ids}
        distinction = next((DISTINCT_FLAGS[ident] for ident in ids if ident in DISTINCT_FLAGS), None)
        if len(mapped) == 1:
            status, reason = "exact_metadata_work_group", "Shared identifier, explicit version series or exact article coordinates."
        elif distinction:
            status, reason = "retained_distinct_publication_units", distinction
        elif len(mapped) < len(ids):
            status, reason = "partly_resolved", "At least one exact provider identity was resolved. Remaining rows need a version or publisher cross-link."
        else:
            status, reason = "unresolved_version_or_duplicate", "Title/authors support a comparison, but no shared identifier or exact journal locator proves identity."
        members = []
        for ident in ids:
            candidate = rows[ident]
            raw = details.get(candidate["openalex_id"], {})
            members.append({
                "candidate_id": ident, "work_id": links[ident]["work_id"], "title": candidate["title"],
                "authors": candidate["authors"], "year": candidate["year"], "doi": links[ident]["doi"],
                "venue": candidate.get("venue"), "biblio": raw.get("biblio"),
                "provider_evidence": candidate.get("metadata_evidence", []),
            })
        reviews.append({"flag_cluster_id": "FLAG-" + ids[0].removeprefix("CAND-"),
                        "status": status, "reason": reason, "members": members})
    return reviews


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    corpus = args.root / "corpus"
    candidates = read_jsonl(corpus / "candidates.jsonl")
    papers = read_jsonl(corpus / "bibliography.jsonl")
    if len({row["candidate_id"] for row in candidates}) != len(candidates):
        raise ValueError("Duplicate provider candidate IDs")
    details = read_provider_details(corpus, candidates)
    crosswalk = reconcile(candidates, papers, details, recorded_registry_keys(corpus))
    review = review_flags(candidates, crosswalk, details)
    summary = {
        "provider_rows": len(crosswalk),
        "provider_cache_matches": sum(row["openalex_id"] in details for row in candidates),
        "work_groups_including_unresolved_singletons": len({row["work_id"] for row in crosswalk}),
        "crosswalk_statuses": dict(Counter(row["identity_status"] for row in crosswalk)),
        "linked_to_selected_canonical_rows": sum(row["canonical_selection_status"] == "selected_checkpoint_priority_work"
                                                 for row in crosswalk),
        "linked_selected_canonical_works": len({row["canonical_paper_id"] for row in crosswalk
                                                if row["canonical_selection_status"] == "selected_checkpoint_priority_work"}),
        "flagged_clusters": len(review),
        "flagged_rows": sum(len(row["members"]) for row in review),
        "flag_cluster_outcomes": dict(Counter(row["status"] for row in review)),
        "flag_row_outcomes": dict(sum((Counter({row["status"]: len(row["members"])}) for row in review), Counter())),
        "input_sha256": {name: sha256((corpus / name).read_bytes()).hexdigest()
                         for name in ("candidates.jsonl", "bibliography.jsonl", "raw_discovery_index.jsonl", REGISTRY_EVIDENCE)
                         if (corpus / name).is_file()},
    }
    write_jsonl(corpus / "provider_candidate_work_crosswalk_round10.jsonl", crosswalk)
    write_jsonl(corpus / "provider_duplicate_flag_reviews_round10.jsonl", review)
    (corpus / "provider_candidate_reconciliation_round10.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
