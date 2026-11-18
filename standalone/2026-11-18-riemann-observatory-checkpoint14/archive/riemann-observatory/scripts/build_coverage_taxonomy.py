#!/usr/bin/env python3
"""Export family and historical coverage without changing canonical evidence."""

import argparse
from collections import Counter, defaultdict
import csv
from datetime import date
from hashlib import sha256
import json
from pathlib import Path
import re
import unicodedata


ROOT = Path(__file__).resolve().parents[1]
FAMILIES = {
    "A": "Classical analysis", "B": "Zeros and statistics", "C": "Equivalent criteria",
    "D": "Spectral and operator approaches", "E": "Geometry, arithmetic and L-functions",
    "F": "Dynamics and alternative analysis", "G": "Documented failed or disputed approaches",
    "H": "Adjacent methods",
}
STRATA = (
    ("before_1859", 1859), ("1859–1900", 1901), ("1901–1950", 1951), ("1951–1980", 1981),
    ("1981–2000", 2001), ("2001–2015", 2016), ("2016–2023", 2024),
)
TOPICS = {
    "A": ("exponential sums", "resonance", "mollifiers", "universality", "zero-free", "moments",
          "derivative moments", "zero-density methods", "exponent pairs", "large sieve", "zero-density",
          "large values", "prime intervals", "multiplicative uniformity", "critical proportions"),
    "B": ("spacings", "correlations", "zero statistics", "value statistics", "weighted value law", "random matrices",
          "numerical statistics", "Turing method", "validated zero isolation", "critical line",
          "critical proportions", "derivative moments", "zero-density", "zero-density methods",
          "zero-free", "operator and zeros", "probability and zeros"),
    "C": ("Weil", "Li", "Turán", "L-function criteria", "completeness criterion", "spectral criteria"),
    "D": ("operator", "canonical systems", "inverse spectral ambiguity", "de Branges–Sonine",
          "operator and zeros", "probability and operator", "spectral criteria"),
    "E": ("L-function criteria",),
    "F": ("Jensen", "Jensen and real zeros", "probability", "heat flow", "Newman lower bound",
          "Newman upper bound", "probabilistic positivity", "probability and positivity",
          "probability and operator", "probability and zeros", "chaos"),
    "H": ("canonical systems", "inverse spectral ambiguity", "positive superresolution",
          "full moments and determinacy", "lattice feasibility and bounds", "flat extension and finite reconstruction",
          "quadrature", "interval arithmetic", "evaluation complexity", "finite verification",
          "rigorous tail summation", "validated Dirichlet computation", "decoupling", "restriction", "incidence"),
}
TITLE_RULES = {
    "A": (
        ("prime-number or explicit-formula method", r"prime[- ]number theorem|distribution des nombres premiers|theoreme des nombres premiers|explicit formulas?|formules? explicites?|perron"),
        ("analytic zeta estimates", r"zero[- ]free|zero[- ]density|large value|exponential sums?|dirichlet polynomial|mollif|universali|mean[- ](square|value)|moments? of .{0,35}(zeta|l[- ]functions?)|zeta.{0,28}moments?|theory of the riemann zeta.function"),
        ("arithmetic summation or continuation", r"fonctionnelle de la fonction zeta|dirichlet series|dirichletsche[nr]? reihen|series de dirichlet|chebyshev|tauberian|ikehara|prime gaps?|dirichlet convolution|euler products?|large sieve|van der corput|approximate functional equation|extent of asymptotic|upper bounds?.{0,25}mertens"),
    ),
    "B": (
        ("zero location, count or statistics", r"\b(?:zeroe?s?|roots?) of\b|nulos? (de|da)|zeros? de la fonction zeta|nullstellen|нулях|critical line|ligne critique|riemann zeros|zeta zeros|zero[- ](count|density|free|spacing|statistics|distribution|correlation|repulsion)|pair correlation|nearest neighbou?r|zeros? on the"),
        ("zero/value statistical models", r"random matri(?:x|ces)|sine kernel|value distribution of|distribution of (the )?values|distribution of zeroe?s|gram points|turing.s method|fyodorov[–— -]*hiary[–— -]*keating"),
    ),
    "C": (
        ("named RH criterion or explicit equivalence", r"nyman[–— -]*beurling|beurling.*(criterion|hypoth|reformul)|baez[–— -]*duarte|riemann hypothesis.{0,35}(criterion|criteria|inequality|equivalen)|(?:criterion|criteria|equivalen|implies).{0,45}riemann hypothesis|riemann.s hypothesis.{0,20}reformul|keiper[ /–-]*li|orthogonality.{0,40}hardy space|approche (hilbertienne|sequentielle).{0,45}hypothese de riemann"),
        ("standard named positivity criterion", r"\bli.s criterion|li coefficients|weil positivity|weil distribution|weil quadratic form|lagarias (inequality|criterion)|robin.s criterion"),
    ),
    "D": (
        ("operator or spectral construction", r"\boperators?\b|operatoren|operateurs?|\bspectral\b|canon(ical|ique) system|canonical differential|hilbert[–— -]*polya|berry[–— -]*keating|de branges|hilbert space|schrodinger|quantum graphs?|self[–— -]*adjoint|weyl coefficient|sonine|hamiltonian|weighted composition semigroup|one.dimensional translation group|landau levels"),
    ),
    "E": (
        ("function-field, arithmetic or geometric object", r"automorphic|langlands|finite fields?|function fields?|algebraic geometr|algebraic curves?|arithmetic geometr|algebraic number fields|number fields?|arithmetical progression|progression arithmetique|arithmetische progression|motivic|motives|l[- ]functions?|dirichlet characters?|hecke|selberg class|modular forms?|trace formula|noncommutative geometr|p.adic|algebraic cycles|frobenius|monodromy|artin.{0,18}(factor|conjectur|l.function)|crystalline companions|arithmetic site|orbifold|functoriality|chebotarev"),
    ),
    "F": (
        ("dynamical, probabilistic or alternative mechanism", r"heat flow|de bruijn[–— -]*newman|\bdynamical\b|\bdynamics\b|\bstochastic\b|\bprobabilistic\b|probability|infinite divisib|infinitely divisible|levy process|\bchaos\b|jensen[–— -]*polynomial|jensen[–— -]*polya|tur[aá]n inequalit|screw functions?"),
    ),
    "H": (
        ("portable adjacent mathematical or computational tool", r"canonical systems?|inverse spectral|weyl coefficient|moment problem|superresolution|decoupling|interval arithmetic|certified numerics|evaluation complexity|quadrature|dispersion method|restriction estimate|exponential sum estimate|finite reconstruction|flat extension|symbolic computation"),
    ),
}
PRIMARY = {
    "PAPER-A004": ("ABD", "Complete v2 reading covers the explicit-formula Gram matrix, trace and inertia bounds, and zero proportions."),
    "PAPER-A006": ("AB", "Whole preprint reading covers the pair-correlation formulation and zero-density tail."),
    "PAPER-H401": ("AB", "The source reading records the boundary zero-free argument and distribution-of-zeros setting."),
    "PAPER-H402": ("A", "Original pp. 52–59 record the explicit-formula and inverse-transform normalization."),
    "PAPER-H405": ("AB", "Original/translation scope records grouped residues and local zero-count inputs."),
    "PAPER-H406": ("AB", "Read pp. 285–292 document the grouped zero-sum bounds in the explicit formula."),
    "PAPER-MN2026-VERTICAL": ("CDF", "Full v1 scope covers a bounded Hardy-space vertical group and an RH membership equivalence."),
    "PAPER-HIST64-EULER1744": ("AH", "The targeted primary reading of Theorems 7–8 documents the prime-product antecedent."),
    "PAPER-HIST64-DIRICHLET1837": ("AE", "The recorded primary argument in pp. 45–46 and 69–71 concerns primes in arithmetic progressions."),
    "PAPER-HIST64-CHEB1852A": ("A", "The targeted reading records prime-counting comparisons."),
    "PAPER-HIST64-CHEB1852B": ("A", "The targeted reading pp. 382–390 records prime-count bounds and Bertrand's postulate."),
    "PAPER-HIST64-SPEISER1935": ("BC", "The primary note checks the geometric link between zeta derivative zeros and RH."),
    "PAPER-HIST64-LEVINSONMONTGOMERY1974": ("ABC", "The read theorem and corollary give a derivative-zero count and RH connection."),
    "PAPER-HIST64-STECHKIN1970": ("AB", "The read theorem gives a classical zeta zero-free-region bound."),
    "PAPER-HIST64-HADAMARD1893": ("AH", "Targeted Part III §§34–38 are the entire-function factorization source used by the analytic history."),
    "PAPER-HIST64-BOREL1978": ("AB", "Read Theorems 1–3 combine generalized-prime estimates with a distribution-modulo-one criterion."),
    "PAPER-HIST64-CAHEN1894": ("A", "Read Part I §§5–8 records half-planes of convergence and coefficient-sum formulas for generalized Dirichlet series."),
    "PAPER-HIST64-DELANGE1956D": ("A", "Read Theorem a and the arithmetic applications track an Ikehara-type singularity-to-asymptotic step."),
    "PAPER-HIST64-DELANGE1961": ("A", "Read source sections concern analytic estimates for multiplicative functions."),
    "PAPER-HIST64-FANTAPPIE1925": ("A", "Read source passages concern a zeta-derived asymptotic for the nth prime."),
    "PAPER-HIST64-GRISO1978": ("AB", "Primary pp. 1–3 link weighted Landau zero sums and distribution modulo one of transformed ordinates."),
    "PAPER-HIST64-LANDAU1905": ("A", "The historical source notes identify the printed zeta inequalities and their growth assumptions."),
    "PAPER-HIST64-LANDAU1908": ("ABE", "Read prime-power explicit formula and its extension to a reduced arithmetic progression via Dirichlet L-series."),
    "PAPER-HIST64-MOSER1976": ("AB", "Read theorem and pp. 45–46 connect a trigonometric-sum bound to odd-order critical-line zeros."),
    "PAPER-HIST64-MOSER1977": ("AB", "Read Theorems 1–2 concern real/imaginary level-set distribution subject to a trigonometric-sum bound."),
    "PAPER-HIST64-MOSER1979": ("AB", "Read addendum pp. 403–404 records a conditional critical-line finding and a modified remainder."),
    "PAPER-HIST64-PERRON1908": ("A", "Read pp. 103–104 give coefficient-summation inversion for Dirichlet series."),
    "PAPER-HIST64-RYAVEC1977": ("AB", "Read Theorems 2–3 use a Mellin decomposition and Bessel inequality for zero-free regions."),
    "PAPER-HIST64-VINOGRADOV1958N": ("AB", "The targeted source reading records Vinogradov's analytical zeta estimate and zero-free behavior."),
    "PAPER-A002": ("BH", "The source scope concerns validated finite-height verification of the zeta zero line and the count."),
    "PAPER-OP62-WEIL72": ("ACE", "The archive records Weil's explicit formula and the positivity formulation for zeta and L-functions."),

    "PAPER-POS64-OPPROB-016": ("CEF", "The recorded complete §§1–3 concern a Selberg-class GRH formulation via infinite divisibility."),
    "PAPER-POS64-OPPROB-024": ("DH", "The entered whole note and Theorems 2.1 and 3.1 concern Dirac/Schrödinger operator tools for the Fourier transform."),
}
SUBSTANTIVE_G = {
    "PAPER-S003": ("primary_reading_scope", "Theorem 15.6 proves a no-go for the fixed compact Berry–Keating spectral realization; the G tag concerns that failed route."),
    "PAPER-S006": ("primary_reading_scope", "Read pp. 4–5 explicitly exclude equality with the zeta spectral measure in the proposed infinite graph construction."),
    "PAPER-AS64-BOURGAIN-WATT": ("source_explicit_status", "The provider record explicitly documents the author withdrawal in arXiv v2, with v1 retained for the history."),
}


def json_lines(path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def normalized(text):
    spaced = unicodedata.normalize("NFKD", text.casefold().replace("ζ", "zeta"))
    return "".join(letter for letter in spaced if not unicodedata.combining(letter))


def read_inputs(root, preview):
    canonical_path = root / "corpus/bibliography.jsonl"
    canonical_bytes = canonical_path.read_bytes()
    current = {}
    for line, payload in enumerate(canonical_bytes.splitlines(), 1):
        if payload.strip():
            row = json.loads(payload)
            ident = row["id"]
            if ident in current:
                raise ValueError(f"Duplicate canonical paper {ident}")
            current[ident] = (row, "canonical", str(canonical_path.relative_to(root)), line)
    pins = {str(canonical_path.relative_to(root)): sha256(canonical_bytes).hexdigest()}
    pending = defaultdict(list)
    if preview:
        aliases_path = root / "quality/paper_aliases.jsonl"
        aliases = {row["alias"]: row["canonical"] for row in json_lines(aliases_path)} if aliases_path.exists() else {}
        if aliases_path.exists():
            pins[str(aliases_path.relative_to(root))] = sha256(aliases_path.read_bytes()).hexdigest()
        for path in sorted((root / "papers").glob("*records.jsonl")):
            raw_path = str(path.relative_to(root))
            blob = path.read_bytes()
            added = False
            for line, payload in enumerate(blob.splitlines(), 1):
                if not payload.strip():
                    continue
                row = json.loads(payload)
                ident = row.get("id") or row.get("paper_id")
                seen = set()
                while ident in aliases:
                    if ident in seen:
                        raise ValueError(f"Alias cycle {ident}")
                    seen.add(ident)
                    ident = aliases[ident]
                if ident and ident not in current:
                    row["id"] = ident
                    pending[ident].append((row, "pending_canonical", raw_path, line))
                    added = True
            if added:
                pins[raw_path] = sha256(blob).hexdigest()
    held = {ident: [f"{row[2]}:{row[3]}" for row in candidates] for ident, candidates in pending.items()
            if len(candidates) > 1}
    for ident, candidates in pending.items():
        if ident not in held:
            current[ident] = candidates[0]
    return current, pins, held


def year_and_stratum(row, cutoff):
    year = row.get("year")
    cutoff_year = int(cutoff[:4])
    if isinstance(year, str) and re.fullmatch(r"\d{4}", year):
        year = int(year)
    if type(year) is not int or not 1 <= year <= 9999:
        return None, "undated"
    for label, upper in STRATA:
        if year < upper:
            return year, label
    return year, f"2024–{cutoff}" if year <= cutoff_year else "after_cutoff_year"


def evidence_record(kind, field, value, reason, path):
    return {"basis": kind, "field": field, "value": value, "reason": reason, "source": path}


def read_taxonomy_rules(root, pins):
    area_path = "quality/coverage_taxonomy_rules_round10.json"
    override_path = "quality/coverage_taxonomy_scope_overrides_round10.jsonl"
    payloads = {}
    for path in (area_path, override_path):
        blob = (root / path).read_bytes()
        pins[path] = sha256(blob).hexdigest()
        payloads[path] = blob.decode("utf-8")
    area_rules = {key.casefold(): value for key, value in json.loads(payloads[area_path]).items()}
    scope_overrides = {}
    for line in payloads[override_path].splitlines():
        entry = json.loads(line)
        if entry["id"] in scope_overrides or not (root / entry["source"]).is_file():
            raise ValueError(f"Duplicate override or missing review source for {entry['id']}")
        scope_overrides[entry["id"]] = entry
    for rule in (*area_rules.values(), *scope_overrides.values()):
        if not rule["families"] or set(rule["families"]) - (FAMILIES.keys() - {"G"}):
            raise ValueError(f"Invalid new taxonomy rule: {rule}")
    return area_rules, scope_overrides


def classify(row, state, source, line, cutoff, area_rules, scope_overrides):
    record = row.get("record_path") or row.get("record_file")
    original = row.get("family")
    recorded = list(original) if isinstance(original, list) else [original] if original else []
    track = row.get("track_file") or source
    tags = defaultdict(list)
    withheld = []
    for family in recorded:
        if family not in FAMILIES:
            withheld.append({"tag": family, "reason": "Original explicit field falls outside the A–H codes."})
        elif family == "G" and row["id"] not in SUBSTANTIVE_G:
            withheld.append({
                "tag": family, "reason": "Original G preserved. A substantial failed/disputed route or withdrawal requires specific review for G coverage.",
            })
        else:
            tags[family].append(evidence_record("existing_explicit_family", "family", family,
                                                "Family explicitly present in the archive record.", track))
    scope = row.get("read_scope") or row.get("audit_scope") or row.get("technical_audit_scope")
    access = row.get("access_status")
    if not access and row.get("full_text_accessed"):
        access = "full_text_accessed"
    if access and access.startswith(("full_text_accessed", "full_primary_", "full_scanned_primary_")):
        access = "full_text_accessed"
    if access == "primary_excerpt_accessed":
        access = "primary_source_excerpt_accessed"
    if row["id"] in PRIMARY and scope and access in {"full_text_accessed", "primary_source_excerpt_accessed"}:
        families, reason = PRIMARY[row["id"]]
        for family in families:
            tags[family].append(evidence_record("primary_reading_scope", "read_scope", scope, reason, record or track))
    override = scope_overrides.get(row["id"])
    if override and scope and access in {"full_text_accessed", "primary_source_excerpt_accessed"}:
        for family in override["families"]:
            evidence = evidence_record(
                "primary_reading_scope", "read_scope", scope, override["reason"], override["source"]
            )
            evidence["locator"] = override["locator"]
            tags[family].append(evidence)
    if row["id"] in SUBSTANTIVE_G:
        basis, reason = SUBSTANTIVE_G[row["id"]]
        field = "read_scope" if basis == "primary_reading_scope" else "publication_status"
        value = scope if field == "read_scope" else row.get(field)
        if value:
            tags["G"].append(evidence_record(basis, field, value, reason, record or track))
    mapped_areas = set()
    for field in ("area", "topic"):
        value = row.get(field)
        if not isinstance(value, str):
            continue
        for family, topics in TOPICS.items():
            if value.casefold() in {topic.casefold() for topic in topics}:
                tags[family].append(evidence_record("metadata_inferred", field, value, "Exact topic/area mapping.", track))
        key = value.casefold()
        if key in area_rules and key not in mapped_areas:
            rule = area_rules[key]
            for family in rule["families"]:
                tags[family].append(evidence_record("metadata_inferred", field, value, rule["reason"], track))
            mapped_areas.add(key)
    title = row.get("title") or ""
    folded = normalized(title)
    for family, patterns in TITLE_RULES.items():
        for description, pattern in patterns:
            matched = re.search(pattern, folded)
            if matched:
                tags[family].append(evidence_record("metadata_inferred", "title", title,
                                                    f"Title cue for {description} ({matched.group()!r}).", track))
                break
    year, stratum = year_and_stratum(row, cutoff)
    selected = row.get("selection_status")
    if state == "pending_canonical":
        selected = "deferred_supporting_bibliographic_record" if row.get("selected") is False else "selected_checkpoint_priority_work"
    whole = row.get("whole_work_read", row.get("substantive_whole_work_read"))
    return {
        "id": row["id"], "title": title, "input_state": state, "input_path": source, "input_line": line,
        "original_track": track, "record_path": record, "source_url": row.get("source_url") or row.get("canonical_url"),
        "recorded_family": original, "recorded_area": row.get("area"), "recorded_topic": row.get("topic"),
        "families": sorted(tags), "family_evidence": dict(sorted(tags.items())),
        "withheld_recorded_tags": withheld,
        "taxonomy_status": "classified" if tags else "unclassified_insufficient_subject_evidence",
        "year": year, "year_field": "year", "year_as_recorded": row.get("year"),
        "recorded_historical_stratum": row.get("historical_stratum"), "historical_stratum": stratum,
        "selection_status": selected, "access_status": access, "whole_work_read": whole, "audit_level": row.get("audit_level"),
    }


def count(rows):
    levels = Counter(row["audit_level"] for row in rows)
    return {
        "selected_works": len(rows),
        "full_text_accessed": sum(row["access_status"] == "full_text_accessed" for row in rows),
        "primary_excerpt_accessed": sum(row["access_status"] == "primary_source_excerpt_accessed" for row in rows),
        "whole_work_read": sum(row["whole_work_read"] is True for row in rows),
        **{f"whole_audit_level_{level}": levels[level] for level in range(4)},
        "whole_audit_unknown": sum(levels[n] for n in levels.keys() - set(range(4))),
    }


def make_tables(rows, cutoff, preview):
    selected = [row for row in rows if row["selection_status"] == "selected_checkpoint_priority_work"]
    universes = {"canonical": [row for row in selected if row["input_state"] == "canonical"]}
    if preview and any(row["input_state"] == "pending_canonical" for row in rows):
        universes["preview_including_pending"] = selected
    strata = [label for label, _ in STRATA] + [f"2024–{cutoff}", "after_cutoff_year", "undated"]
    cells = []
    for universe, eligible in universes.items():
        member = {family: [row for row in eligible if family in row["families"]]
                  for family in FAMILIES}
        member["unclassified"] = [row for row in eligible if not row["families"]]
        cells.append(dict(universe=universe, view="overall", family="", stratum="", **count(eligible)))
        for family, group in member.items():
            cells.append(dict(universe=universe, view="family", family=family, stratum="", **count(group)))
            for stratum in strata:
                cells.append(dict(universe=universe, view="family_by_stratum", family=family, stratum=stratum,
                                  **count([row for row in group if row["historical_stratum"] == stratum])))
        for stratum in strata:
            cells.append(dict(universe=universe, view="stratum", family="", stratum=stratum,
                              **count([row for row in eligible if row["historical_stratum"] == stratum])))
    return cells


def md_table(cells, field):
    text = [
        f"| {field} | Selected | Full text | Primary excerpt | Whole read | Level 0 | Level 1 | Level 2 | Level 3 | Unknown level |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for cell in cells:
        key = cell[field]
        label = f"{key} · {FAMILIES[key]}" if key in FAMILIES else key
        numbers = list(cell.values())[4:]
        text.append("| " + " | ".join([label, *map(str, numbers)]) + " |")
    return "\n".join(text)


def report(rows, cells, summary, cutoff):
    canonical = [row for row in rows if row["input_state"] == "canonical"]
    strength = Counter(item["basis"] for row in rows for group in row["family_evidence"].values() for item in group)
    provisional = len(rows) - len(canonical)
    lines = [
        "# Coverage taxonomy and reading depth", "",
        f"Historical cutoff {cutoff}. The export covers {len(canonical)} canonical paper IDs and "
        f"{provisional} separately marked pending contributor IDs. The taxonomy summarizes evidence already "
        "recorded in the archive. The family assignments carry their actual field, reason and provenance.", "",
        "Existing family tags are preserved in the original field. Title and topic mappings are metadata inferences, "
        "including when the record also reports a complete reading. A separate primary-scope label uses a documented "
        "passage or read scope specific to that family. The G table admits substantial failed research routes and "
        "documented withdrawals. Original G tags without that evidence are shown in the per-paper ledger as preserved, "
        "withheld from the G count. Local typos and theorem qualifications do not trigger G.", "",
        "The historical bucket uses the exact archive year field, with separate before-1859, post-cutoff-year and undated categories. "
        "The year follows the record's work/version identity. Readings and accesses count from their independent fields. Family rows "
        "overlap. Historical rows are disjoint. Both tables use selected works.", "",
        "[Per-paper taxonomy](coverage_taxonomy_round10.jsonl) · [Full cross-tabs](coverage_taxonomy_crosstabs_round10.csv) · "
        "[Input pins and summary](coverage_taxonomy_summary_round10.json) · "
        "[Exact area rules](coverage_taxonomy_rules_round10.json) · "
        "[Reviewed scope overrides](coverage_taxonomy_scope_overrides_round10.jsonl)", "",
    ]
    for universe in dict.fromkeys(cell["universe"] for cell in cells):
        label = "Canonical input" if universe == "canonical" else "Preview including pending contributor records"
        subset = [cell for cell in cells if cell["universe"] == universe]
        lines.extend((f"## {label}", "", md_table([cell for cell in subset if cell["view"] == "family"], "family"), "",
                      md_table([cell for cell in subset if cell["view"] == "stratum"], "stratum"), ""))
    active = [cell for cell in cells if cell["universe"] == "canonical"]
    early = {cell["stratum"]: cell for cell in active if cell["view"] == "stratum"}
    first = early["1859–1900"]
    second = early["1901–1950"]
    family_gaps = sorted((cell for cell in active if cell["view"] == "family" and cell["family"] in FAMILIES),
                         key=lambda cell: cell["full_text_accessed"] - cell["whole_work_read"], reverse=True)
    widest = ", ".join(f"{cell['family']} ({cell['full_text_accessed']} full texts, {cell['whole_work_read']} whole readings)"
                       for cell in family_gaps[:3])
    lines.extend((
        "## Gaps and next priorities", "",
        f"- In 1859–1900 the archive has {first['full_text_accessed']} full texts and {first['whole_work_read']} complete readings "
        f"among {first['selected_works']} selected works. In 1901–1950 it has {second['full_text_accessed']} full texts and "
        f"{second['whole_work_read']} complete readings among {second['selected_works']}. "
        "Prioritize full original-language readings alongside missing source retrieval. The historical review identifies specific original locators, and the "
        "provider triage separates original contributions from compendia and translations. "
        "[Historical source notes](../papers/geometry64_historical_sources_notes.md) · [Source triage](../corpus/curated_candidate_decisions_round10.jsonl)",
        f"- The largest absolute gaps between full text and whole reading are {widest}. Use the family-by-stratum "
        "cross-tabs and recorded source locators to choose new technical reconstructions. Keep scoped proof reviews and complete-work "
        "audit levels separate.", "",
        "- Review unclassified and metadata-only assignments from the source title and indicated mathematical sections "
        "during the next reading pass. The G cases withheld from coverage need source-level justification for the failure "
        "or controversy. Previously documented local issues keep their findings scope.",
        "", f"The ledger contains {strength['existing_explicit_family']} explicit-family evidence entries, "
        f"{strength['metadata_inferred']} metadata inferences, {strength['primary_reading_scope']} primary-scope entries "
        f"and {strength['source_explicit_status']} explicit publication-status entries. "
        f"Pending multi-track identities held for the canonical builder: {len(summary['held_pending_ids'])}.", "",
        "Rebuild after canonical integration with `python scripts/build_coverage_taxonomy.py`. "
        "Add `--preview-tracks` to include noncanonical contributor rows separately. The command writes only this taxonomy "
        "and its report and tabulation.", "",
    ))
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--cutoff", default="2026-11-18")
    parser.add_argument("--preview-tracks", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    try:
        if date.fromisoformat(args.cutoff).isoformat() != args.cutoff:
            raise ValueError
    except ValueError:
        parser.error("--cutoff expects YYYY-MM-DD")
    sources, pins, held = read_inputs(root, args.preview_tracks)
    area_rules, scope_overrides = read_taxonomy_rules(root, pins)
    rows = [classify(*entry, args.cutoff, area_rules, scope_overrides) for _, entry in sorted(sources.items())]
    cells = make_tables(rows, args.cutoff, args.preview_tracks)
    summary = {
        "cutoff": args.cutoff, "input_sha256": pins, "input_state_counts": dict(Counter(row["input_state"] for row in rows)),
        "taxonomy_status_counts": dict(Counter(row["taxonomy_status"] for row in rows)),
        "eligible_G_ids": [row["id"] for row in rows if "G" in row["families"]],
        "withheld_recorded_G_ids": [row["id"] for row in rows if any(tag["tag"] == "G" for tag in row["withheld_recorded_tags"])],
        "held_pending_ids": held,
        "overall_tables": [cell for cell in cells if cell["view"] == "overall"],
    }
    for name, digest in pins.items():
        if sha256((root / name).read_bytes()).hexdigest() != digest:
            raise ValueError(f"Input changed during taxonomy generation: {name}")
    output = root / "quality"
    (output / "coverage_taxonomy_round10.jsonl").write_text(
        "".join(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n" for row in rows), encoding="utf-8")
    with (output / "coverage_taxonomy_crosstabs_round10.csv").open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=list(cells[0]))
        writer.writeheader()
        writer.writerows(cells)
    (output / "coverage_taxonomy_summary_round10.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
                                                                 encoding="utf-8")
    (output / "coverage_taxonomy_report_round10.md").write_text(report(rows, cells, summary, args.cutoff), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
