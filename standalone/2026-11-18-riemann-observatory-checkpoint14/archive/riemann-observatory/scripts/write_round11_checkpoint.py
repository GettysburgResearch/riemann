#!/usr/bin/env python3
"""Generate current checkpoint prose from canonical metrics and numbered syntheses."""

import json
import re
from datetime import datetime, timezone
from pathlib import Path


SOURCE_SCOPE = (
    "The 1,000-work research program remains unfinished. The archive distinguishes source "
    "access, complete readings, scoped proof verification, and whole-work audits. This "
    "checkpoint contains no proof or disproof of RH, new zero-free or zero-density exponent, "
    "or established publication novelty."
)
C2_INTERVAL = "0.61649875288731141829 < C₂ < 1.075561"
REVIEWED_WORKS = {
    "PAPER-S001": "Riemann’s 1859 memoir",
    "PAPER-E008": "Li’s original criterion",
    "PAPER-E014": "Báez-Duarte’s original strengthening",
    "PAPER-DM63-HLZ2022": "Heap–Li–Zhao’s negative moments",
}


def evidence_table(metrics):
    levels = metrics["whole_work_audit_levels"]
    rows = [
        ("Provider metadata records", metrics["metadata_candidates"]),
        ("Selected source records", metrics["selected_checkpoint_works"]),
        ("Selected full texts accessed", metrics["fulltexts_accessed_selected"]),
        ("Selected primary-source excerpts only", metrics["selected_primary_excerpt_accessed"]),
        ("Complete substantive readings", metrics["whole_work_or_translation_read"]),
        ("Complete paper-wide Level2/3 audits", f"{levels.get('2', 0)} / {levels.get('3', 0)}"),
        ("Scoped independently adjudicated claim groups", metrics["scoped_level3_claim_groups"]),
        ("Theorem/conjecture/exercise records", metrics["theorem_or_exercise_records"]),
        ("Connection records", metrics["connection_records"]),
        ("Graph nodes / edges", f"{metrics['graph_nodes']:,} / {metrics['graph_edges']:,}"),
    ]
    values = (f"| {label} | {value:,} |" if isinstance(value, int)
              else f"| {label} | {value} |" for label, value in rows)
    return "| Evidence state | Actual |\n|---|---:|\n" + "\n".join(values)


def read_jsonl(path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def write_text(root, path, content):
    (root / path).write_text(content.strip() + "\n", encoding="utf-8")


def work_list(names):
    if len(names) > 2:
        return ", ".join(names[:-1]) + f", and {names[-1]}"
    return " and ".join(names)


def review_status(promotions, bibliography):
    pending = {paper_id: name for paper_id, name in REVIEWED_WORKS.items()
               if promotions.get(paper_id, 0) < 3}
    complete = [name for paper_id, name in pending.items()
                if bibliography[paper_id]["audit_level"] == 1 and bibliography[paper_id]["whole_work_read"]]
    sentences = []
    if complete:
        sentences.append(f"Complete readings of {work_list(complete)} are recorded at Level 1.")
    if pending:
        sentences.append(f"Level 3 whole-work adjudication remains pending for {work_list(list(pending.values()))}.")
    return " ".join(sentences) or "The registry records the editions and adjudications for the recent whole-work reviews."


def numbered(entries):
    return "\n\n".join(f"{number}. {entry}" for number, entry in enumerate(entries, 1))


def write_current(root, metrics):
    reports = [(11, root / "final_synthesis/round11_report.md")]
    for number in (12, 13, 14, 15, 16, 17):
        path = root / f"final_synthesis/round{number}_report.md"
        if path.is_file():
            reports.append((number, path))
    current_round, current_path = reports[-1]
    current_report = current_path.relative_to(root).as_posix()
    sections = [current_path.read_text(encoding="utf-8").strip()]
    for number, path in reversed(reports[:-1]):
        sections.append(f"# Previous Round {number} synthesis — historical snapshot\n\n"
                        f"This report records Round {number}. Use Round {current_round} and the current ledgers "
                        "for the latest claims, source decisions, and corpus counts.\n\n"
                        + path.read_text(encoding="utf-8").strip())
    synthesis = "\n\n".join(sections)
    table = evidence_table(metrics)
    levels = metrics["whole_work_audit_levels"]
    count = (
        f"{metrics['selected_checkpoint_works']:,} selected works, "
        f"{metrics['fulltexts_accessed_selected']:,} full texts accessed, "
        f"{metrics['whole_work_or_translation_read']:,} complete substantive readings, "
        f"{levels.get('3', 0):,} whole-work Level 3 audits, and "
        f"{metrics['scoped_level3_claim_groups']:,} scoped adjudicated groups."
    )
    promotions = {row["id"]: row["level"] for row in read_jsonl(root / "quality/whole_work_audit_promotions.jsonl")}
    bibliography = {row["id"]: row for row in read_jsonl(root / "corpus/bibliography.jsonl")}
    pending = review_status(promotions, bibliography)
    errors = sum(bool(row.get("verified_author_error")) for row in read_jsonl(root / "audits/findings.jsonl"))
    promotion_summary = ""
    if promotions.get("PAPER-E008") == 3:
        promotion_summary = (" Li’s original criterion has a version-pinned Level 3 audit of the journal-typeset mirror. "
                      "Two local repairs preserve both main criteria.")
    if promotions.get("PAPER-E014") == 3:
        promotion_summary += " Báez-Duarte’s original strengthening has a version-pinned Level 3 audit."
    round12_summary = ""
    executive_update = ""
    continuation_update = ""
    round12_evidence = ""
    round13_summary = ""
    round13_evidence = ""
    round14_summary = ""
    round14_evidence = ""
    round15_summary = ""
    round15_evidence = ""
    round17_summary = ""
    round17_evidence = ""
    bounded_phase = ""
    stopping_point = ""
    first_integration = "python scripts/integrate_round11.py"
    next_integration = ""
    checkpoint_number = 9
    receipt_number = 8
    continuation_priorities = (
        "The highest-priority open work is the fixed polynomial-band law, practical Q₂ error constants, "
        "the finite-length array remainder, and the arithmetic weighted-tail interface."
    )
    phase_proof = ("Work through the [joint array and Brownian proofs](audits/adversarial_reviews/director_joint_brownian_round11.md). "
                   r"Verify the uniform fourth-moment bound for every subset of primes \(p\le\log Y\) and the interpolation in the reciprocal prime sum.")
    if current_round >= 12:
        round12_summary = (
            "\n\nThe full intrinsic rooted CUE band law has a compensated determinantal description. "
            "In the cubic support range, the arithmetic and CUE models match the full centered third tensor. "
            "A nonzero mixed cosine–sine cumulant excludes independence despite zero covariance. Under RH, "
            "shrinking exponent bands have a time-changed Brownian limit and the corresponding scalar Gaussian "
            "moments converge. The formal all-order extension of the fixed-band "
            "arithmetic moment formula is not a probability moment sequence. The finite proved moment range remains valid."
        )
        executive_update = (" Shrinking exponent bands have a conditional Brownian limit. Rooted CUE has a full "
                            "intrinsic law and matches the arithmetic third tensor in range. Formal all-order "
                            "extrapolation fails.")
        continuation_update = (" Use the proved intrinsic CUE law, signed third tensor, and shrinking-band "
                               "Brownian limit as inputs. Seek the first arithmetic frequency-chamber correction "
                               "beyond the finite moment window.")
        round12_evidence = ("\n\nRound 12 independently reconstructs the compensated determinantal law for rooted CUE "
                            "and verifies a shrinking-band Brownian limit and scalar Gaussian moments under RH. "
                            "The full centered third tensor matches in its support range. Zero cosine–sine covariance "
                            "coexists with nonzero mixed cumulants and dependence for the specified weights. The signed inverse "
                            "and real zero of the formal moment-generating function obstruct extending the finite "
                            "arithmetic moment formula as a probability moment sequence at every order.")
        next_integration = "\npython scripts/integrate_round12.py\npython scripts/integrate_band_laws_round12.py"
        phase_proof = ("Work through the [Round 12 joint and process proofs](audits/adversarial_reviews/director_joint_process_round12.md). "
                       "Reproduce the mixed cosine–sine cumulant and the two-scale reciprocal-mass bound for Brownian tightness.")
    if current_round >= 13:
        checkpoint_number = 10
        receipt_number = 9
        round13_summary = (
            "\n\nIn Round 13 the rooted CUE moment formula is proved through the inclusive window "
            "rb≤1. The RH-conditional arithmetic comparison has its separate window rb<1/2. The first CUE "
            "correction beyond its window is explicit, and the formal continuation fails a finite positivity test at every fixed integer tilt rank. "
            "For the arithmetic fourth cosine moment with 1/8<b<1/6, a smooth contour argument reduces the missing pure arm to a signed estimate "
            "for the fixed coefficient sequence C_* = d₂ * (Λ log²). This estimate remains open."
        )
        executive_update = (
            " Shrinking bands have a conditional Brownian limit with a sharp universal two-scale tightness threshold. "
            "Rooted CUE has the inclusive moment window rb≤1, a first-crossing correction and an all-rank extrapolation obstruction. "
            "The arithmetic rb<1/2 window is unchanged. The longer-band fourth moment is reduced to the fixed signed C_* estimate."
        )
        continuation_priorities = (
            "The first arithmetic target is the signed C_* estimate for the pure fourth arm. The fixed-band law, "
            "practical Q₂ error constants and the finite-length arithmetic array remainder also remain open."
        )
        continuation_update = (
            " The [Round 13 synthesis](final_synthesis/round13_report.md) gives the exact CUE window, first-crossing and positivity results, "
            "the universal grid tightness criterion, and the version-specific source decisions."
        )
        round13_evidence = (
            "\n\nRound 13 verifies the inclusive intrinsic CUE window rb≤1, first-crossing corrections and an all-rank "
            "positivity obstruction for the extrapolated cosine moments. The arithmetic fourth-moment reduction leaves the "
            "fixed signed C_* estimate open. The sharp two-scale threshold is a universal guarantee over grids and laws with "
            "tight initial values. Lean checks one scalar implication with the envelopes as premises. The pinned Hughes–Rudnick "
            "whole-note audit gives the exact logarithmic weight repair. The Báez-Duarte work alias retains both preprint IDs "
            "and the journal manifestation under one canonical identity."
        )
        next_integration += "\npython scripts/integrate_round13.py\npython scripts/integrate_research_round13.py"
        if promotions.get("PAPER-AN79-HR-ZETA") == 3:
            promotion_summary += (
                " The pinned Hughes–Rudnick journal note has a whole-work Level 3 audit with an exact averaging-weight repair."
            )
        promotion_summary += (
            " The Báez-Duarte preprints remain separately citable manifestations of one canonical journal work."
        )

    if current_round >= 14:
        checkpoint_number = 11
        receipt_number = 10
        round14_summary = (
            "\n\nRound 14 gives an explicit finite Hankel witness bound at every fixed tilt rank and the exact "
            "least-order Hermite criterion at rank one. The real Petrov tail quotient has a positive finite "
            "Schur representation and admits factorial Hankel truncation. For the signed C_* sum, the entire "
            "prime-square stratum saves a power for 1/2<θ=4b<9/17. The Baker and Fouvry–Shparlinski windows save "
            "a power on two explicit regions in modulus and prime exponents, including nonunit dual indices "
            "by gcd grouping. The remaining long-prime estimate and full fourth moment are open."
        )
        executive_update += (
            " Round 14 quantifies the finite Hankel witness and exact positive Petrov factors. It removes "
            "the square stratum for θ<9/17 in the stated range and covers two inverse-prime regions. "
            "Long primes are the first remaining arithmetic target."
        )
        continuation_priorities = (
            "The first arithmetic target is the remaining long-prime part of the signed C_* sum. "
            "For 9/17≤θ<2/3, a middle square range also needs an estimate. The full fourth moment, fixed-band "
            "law, practical Q₂ error constants and finite-length arithmetic array remainder remain open."
        )
        continuation_update = (
            f" The [Round 14 synthesis]({current_report}) records the square-stratum threshold, the "
            "two-dimensional averaged inverse-prime windows with gcd grouping, and the quantitative "
            "Hankel and Petrov certificates."
        )
        round14_evidence = (
            "\n\nRound 14 verifies the quantitative all-rank finite Hankel bound, the exact rank-one Hermite "
            "criterion with rational fixtures, and the positive Petrov quotient with factorial truncation. "
            "It proves the square removal for 1/2<θ<9/17 and the Baker and Fouvry–Shparlinski partial prime "
            "estimates on their strict two-dimensional regions. Six new dependencies have targeted "
            "Level 0 scope. Round 14 adds no complete whole-work promotion."
        )
        next_integration += "\npython scripts/integrate_round14.py"

    if current_round >= 15:
        checkpoint_number = 12
        receipt_number = 11
        round15_summary = (
            "\n\nRound 15 adds 12 research records, including the open sufficient moving-phase square target, "
            "and nine scoped adjudication groups. Absolute sampling at the zeta zeros is guaranteed for "
            "p>3 in the critical logarithmic Mellin class. A smooth p=3 example disproves a universal "
            "absolute guarantee. Signed symmetric height convergence at p=3 remains open. The long-prime "
            "countermodel rules out deriving the required Fourier projection from the two phase-blind "
            "norms and row conditions alone. The full four-prime coefficient is triply well-factorable at "
            "the padded level, but fixed-residue distribution does not control the moving phase."
        )
        executive_update += (
            " Round 15 proves the sharp p>3 universal threshold for absolute sampling in the stated "
            "logarithmic scale, with signed convergence at p=3 open. It pins the exact padded factorability "
            "level and gives an explicit Abel substitution bound for one step of Gonek’s proof."
        )
        if promotions.get("PAPER-LF63-GONEK1984") == 3:
            promotion_summary += (
                " Gonek’s 1984 journal scan has the eighth whole-work Level 3 audit. "
                "The main theorem and corollaries survive three local display repairs."
            )
        pending += (
            " The pinned Morse v6 and Bombieri–Lagarias author manuscript retain Level 1 complete-reading "
            "scope alongside scoped findings. The independent audit of Riemann’s original text is ongoing."
        )
        continuation_priorities = (
            "The first arithmetic target is the moving-phase long-prime square estimate for C_*. "
            "A separate priority is signed symmetric height convergence in the critical Mellin class at p=3. "
            "The next effective derivative-tail step is to propagate the explicit Abel bound through the "
            "remaining contour, saddle and endpoint estimates."
        )
        continuation_update = (
            f" The [Round 15 synthesis]({current_report}) gives the exact source dispositions, "
            "the phase-sensitive sufficient estimate and the absolute Mellin threshold."
        )
        round15_evidence = (
            "\n\nRound 15 separates the absolute p>3 zero-sampling theorem and the absolute p=3 "
            "counterexample from the open signed p=3 problem. The pinned Bombieri–Lagarias author manuscript "
            "has two scoped findings on the broad height-limit class and the finite compensation in (3.5). "
            "The pinned Morse v6 has two auxiliary findings on the shifted structure function and quotient sign. "
            "Both readings remain Level 1. The phase-blind residue-array model lacks common-sequence "
            "compatibility. The exact padded factorability theorem meets the coefficient hypothesis at the "
            "longest scale, with the moving-residue and phase estimate still open. The real-shift bound "
            "31L^m+20mL^(m−1), with the second term omitted at m=0, makes one Gonek Abel substitution "
            "explicit. A full numerical derivative-tail budget is still needed."
        )
        next_integration += "\npython scripts/integrate_round15_sources.py\npython scripts/integrate_research_round15.py"

    if current_round >= 16:
        checkpoint_number = 13
        receipt_number = 12
        round15_summary = round15_summary.replace(" Signed symmetric height convergence at p=3 remains open.", "")
        round15_summary += (
            "\n\nRound 16 proves the ordinary symmetric height formula at the critical strip H¹⁄² norm "
            "with local H¹ near x=1 and the stated value decay. The independent Selberg proof gives "
            "separate half-axis convergence for p>1. The smooth p=3 absolute-divergence example "
            "therefore has a signed symmetric limit. A continuous cusp outside the literal manuscript "
            "class shows why the local hypothesis matters. The ninth whole-work audit reconstructs "
            "Riemann’s 1859 argument with explicitly identified later inputs."
        )
        executive_update = executive_update.replace(", with signed convergence at p=3 open", "")
        executive_update += (
            " Round 16 proves the signed symmetric formula at the critical strip weight with local "
            "H¹, separates the p>1 half-axis result, and quantifies the finite convolution and Abel "
            "steps of the (1,1) Gonek application."
        )
        round15_evidence = round15_evidence.replace(
            "Round 15 separates the absolute p>3 zero-sampling theorem and the absolute p=3 "
            "counterexample from the open signed p=3 problem.",
            "Round 15 proves the p>3 absolute zero-sampling theorem and gives the smooth "
            "p=3 absolute-divergence counterexample.",
        )
        round15_evidence += (
            "\n\nRound 16 proves symmetric signed convergence for p=0 with local H¹, including all "
            "inclusive cutoffs. The literal Bombieri–Lagarias condition (A) and the critical norm imply "
            "local H¹ because the norm excludes finite value jumps. The separate p>1 Selberg proof "
            "controls each half-axis. The p=3 continuous cusp with divergent signed sum and archimedean "
            "term falls outside literal (A). Luecking’s complete Level 1 reading gives context for "
            "ambient absolute sampling. The Riemann memoir audit distinguishes the modern genus-zero "
            "factorization, von Mangoldt’s ordered midpoint input, and Genocchi’s known −log 2 correction. "
            "Explicit constants for the positive-order convolution and the finite (1,1) application "
            "leave the full numerical derivative-tail onset open."
        )
        pending = pending.replace(" The independent audit of Riemann’s original text is ongoing.", "")
        pending += " Luecking’s pinned 1986 Bergman paper has a complete Level 1 reading in family H."
        if promotions.get("PAPER-S001") == 3:
            promotion_summary += (
                " Riemann’s pinned 1859 memoir has the ninth whole-work Level 3 audit. "
                "The modern reconstruction uses Genocchi’s known correction and explicitly identifies "
                "the later pointwise ordered-limit input."
            )
        continuation_priorities = (
            "The first arithmetic target is the moving-phase long-prime square estimate for C_*. "
            "Test weaker strip or local conditions for signed Mellin sampling and distinguish the "
            "symmetric and half-axis modes. Propagate the finite Gonek constants through the remaining "
            "contour, saddle and endpoint estimates."
        )
        continuation_update = (
            f" The [Round 16 synthesis]({current_report}) gives the signed critical formula, "
            "the finite Gonek constants and the scope of the Riemann audit."
        )
        next_integration += "\npython scripts/integrate_round16_sources.py\npython scripts/integrate_research_round16.py"

    if current_round >= 17:
        checkpoint_number = 14
        receipt_number = 13
        round17_summary = (
            "\n\nRound 17 gives the exact universal signed symmetric height threshold p≥0 in the stated "
            "logarithmic Mellin scale with the stated value bounds and local H¹ of F near the logarithmic "
            "origin, or literal (A) with midpoint values. "
            "The universal absolute threshold is p>3. One smooth test belongs to every strictly weaker "
            "logarithmic space and has zero prime-power samples and incompatible symmetric subsequences. "
            "The two phase-blind discrepancy bounds allow a large moving Fourier projection even for a "
            "common nonnegative integer sequence, when centered at P/k or the induced unit means. "
            "Simultaneous unit support, prime-model centering at P/φ(k) and the actual moving-prime estimate "
            "remain open."
        )
        executive_update = (
            " The universal signed symmetric Mellin threshold is p≥0 under the stated local and value "
            "hypotheses. One smooth witness defeats every strict logarithmic weakening. The separate "
            "absolute threshold is p>3. The common-sequence phase countermodels use integer-interval "
            "centering. The genuine unit-baseline estimate remains open."
        )
        round17_evidence = (
            "\n\nRound 17 closes the universal symmetric threshold question in the specified logarithmic "
            "scale. The escaped-prime construction gives one smooth witness for all p<0. Its signed zero "
            "sums have a subsequence tending to −∞ and a bounded subsequence. The pole and archimedean "
            "terms are finite, and each fixed prime-power argument has correct pointwise inversion. "
            "The common-sequence models use the full fourth-power support and respect whole-row "
            "common-divisor marginals. Their discrepancy estimates concern P/k or induced unit means. "
            "They leave all-unit support and P/φ(k) centering unresolved. Round 17 adds no verified "
            "author-error flags."
        )
        if bibliography["PAPER-H406"]["whole_work_read"] and bibliography["PAPER-H406"]["audit_level"] == 1:
            pending += (
                " Two independent complete readings of von Mangoldt’s pinned 1895 original journal "
                "article (PAPER-H406, 51 pages) are recorded at Level 1. The p. 293 uniformity wording has "
                "a compact-domain qualification in the reading record."
            )
        first_integration = "python scripts/integrate_round17_sources.py --apply"
        next_integration = "\npython scripts/integrate_research_round17.py"
        bounded_script = "scripts/integrate_checkpoint14_bounded.py"
        claims = read_jsonl(root / "theorems/theorems.jsonl")
        bounded_ids = {
            "OBS-CSTAR-BOUNDED-COMMON-REAL-SEQUENCE-NORM-COUNTERMODEL",
            "OBS-CSTAR-BOUNDED-COMMON-INTEGER-SEQUENCE-NORM-COUNTERMODEL",
        }
        if bounded_ids <= {row.get("id") for row in claims}:
            bounded_phase = (
                " The [1/2,3/2]-valued real and {0,1,2}-valued integer sequences retain a large positive projection "
                "under those same discrepancy baselines."
            )
            if (root / bounded_script).is_file():
                next_integration += f"\npython {bounded_script}"
            round17_summary += bounded_phase
            round17_evidence += bounded_phase
            executive_update += bounded_phase
        continuation_priorities = (
            "First, test the long-prime moving phase with simultaneous unit or explicit rough support "
            "and P/φ(k) centering. Check the baseline variance before seeking a large phase projection or "
            "applying the sufficient block square estimate. Next, propagate the finite Gonek constants "
            "through the contour, saddle, good-height and endpoint terms for one fixed (1,1) tail budget. "
            "Use the critical signed theorem for symmetric truncation and the proved p>1 estimate "
            "when a separate half-axis bound is needed."
        )
        continuation_update = (
            f" The [Round 17 synthesis]({current_report}) gives the exact thresholds, the common-sequence "
            "baseline distinction and the source disposition."
        )
        stopping_point = (
            "\n\nAfter checkpoint 14 is sealed, independently validated and delivered, pause research and "
            "await the next user prompt. The queue below is ready for that handoff."
        )

    write_text(root, "README.md", rf"""# Riemann Observatory — active research archive

Literature cutoff {metrics['cutoff']} UTC. {SOURCE_SCOPE}

{table}

Begin with [START HERE](START_HERE.md), the [current synthesis]({current_report}), and the [ranked research problems](final_synthesis/top_25_research_opportunities.md).{round17_summary}

Under RH the derivative-weighted cumulative cosine statistic has a weak Gaussian limit at cutoffs \(P=Y^\theta\) for each fixed \(0<\theta<1/2\), and all fixed Gaussian moments at subpower cutoffs tending to infinity. At fixed polynomial bands the covariance changes and the centered cosine third moment excludes Gaussian subsequences for \(0<a<b<1/6\). The globally tilted rooted CUE model matches the limiting cosine and sine means and covariance and the centered cosine third moment in their respective ranges. The full arithmetic band law remains open.{round12_summary}{round13_summary}{round14_summary}{round15_summary}

An unconditional global Hardy estimate improves the critical-line enclosure to {C2_INTERVAL}, using the existing finite zero census. The joint conditional Gaussian criterion and Brownian limit, the finite integer trace algorithm, the Deninger obstruction, and the version-specific Suzuki drift correction have separate evidence records.

The [whole-work registry](quality/whole_work_audit_promotions.jsonl) pins editions, source hashes, and review scopes.{promotion_summary} {pending}

Query the [read-only SQLite index](graphs/archive_index.md), its portable SQL dump, or the per-paper views in `paper_views/`. The [evidence audit](quality/evidence_audit.md) explains review levels, and the [continuation guide](CONTINUATION.md) gives rebuild commands. Provider metadata overlap the selected bibliography. Check [reconciliation](quality/provider_candidate_reconciliation_round10.md) before reusing those identities.

The distribution includes original analysis, code, permissible numerical inputs, and exact provenance. Full source texts and private build caches are omitted. Earlier numbered reports preserve the state at their own checkpoints.
""")

    write_text(root, "executive_report.md", rf"""# Research checkpoint — execution continues

{SOURCE_SCOPE}

{table}

Under RH, cumulative derivative-weighted prime phases are weakly Gaussian at each fixed cutoff \(Y^\theta\) with \(0<\theta<1/2\). The centered cosine cubic excludes Gaussian limits for fixed bands below exponent \(1/6\).{executive_update} The full arithmetic band law remains open.

The unconditional enclosure is {C2_INTERVAL}, with the existing height-10,000 census.{promotion_summary}
""")

    research_guide = rf"""
1. Read the [current synthesis](final_synthesis/comprehensive_report.md) and distinguish the derivative-weighted sampling law from the multiplicity-weighted real-line law.
2. Reconstruct the [cumulative and fixed-band comparison](audits/adversarial_reviews/director_polynomial_bands_round11.md). Check the polynomial length condition and the repeated-prime terms before reading the rooted CUE moment match.
3. {phase_proof}
4. Inspect the [global Hardy certificate](audits/adversarial_reviews/director_global_hardy_round11.md). Reuse its rigorous tail beyond height 10,000 and separate the quartic splice from the enclosure.
5. Compare the [finite integer trace test](audits/adversarial_reviews/director_integer_trace_round11.md) with the [Deninger audit](audits/adversarial_reviews/director_deninger_whole_round11.md). Identify the hypotheses a proposed arithmetic trace would still need.
6. Query a stable claim ID in the [archive index](graphs/archive_index.md). Select a [ranked problem](final_synthesis/top_25_research_opportunities.md) and read [CONTINUATION](CONTINUATION.md) before starting work.
"""
    if current_round >= 13:
        research_guide = """
1. Read the [Round 13 synthesis](final_synthesis/round13_report.md) and the [ranked problems](final_synthesis/top_25_research_opportunities.md). Distinguish the RH-conditional arithmetic window rb<1/2 from the inclusive intrinsic rooted CUE window rb≤1.
2. Start with the [pure fourth-arm reduction](audits/adversarial_reviews/director_pure_fourth_round13.md). The mixed arms are covered. The sufficient missing estimate is the real signed C_* sum after smoothing, principal subtraction and divisor cancellation.
3. Reproduce the [finite CUE compression and first crossing](audits/adversarial_reviews/director_cue_windows_round13.md). Check the cosine crossing sign by rank, the finite negative square and the [quadratic mismatch with the exact Petrov Gram](audits/adversarial_reviews/director_petrov_round13.md).
4. Read the [two-scale modulus proof](audits/adversarial_reviews/director_two_scale_round13.md). Check the universal quantifiers and distinguish the compiled scalar step from the probability and arithmetic proofs.
5. Compare the [Hughes–Rudnick weight repair](audits/adversarial_reviews/director_hughes_rudnick_whole_round13.md) and the [Báez-Duarte edition and alias decision](audits/adversarial_reviews/director_baez_whole_round13.md). Inspect the exact version pins before reusing a source claim.
6. For the unconditional enclosure, begin with the [global Hardy certificate](audits/adversarial_reviews/director_global_hardy_round11.md). Query stable claim IDs in the [archive index](graphs/archive_index.md) and use [CONTINUATION](CONTINUATION.md) for the rebuild sequence.
"""
    if current_round >= 14:
        research_guide = """
1. Read the [Round 14 synthesis](final_synthesis/round14_report.md) and select a [ranked problem](final_synthesis/top_25_research_opportunities.md). The intrinsic CUE window is rb≤1. The RH-conditional arithmetic moment window remains rb<1/2.
2. Start with the [signed C_* strata](audits/adversarial_reviews/director_arithmetic_strata_round14.md). Check the all-square range θ<9/17, the two Baker and Fouvry–Shparlinski prime regions, and the remaining long-prime problem before attempting the [pure fourth arm](audits/adversarial_reviews/director_pure_fourth_round13.md).
3. Read the [quantitative rooted CUE results](audits/adversarial_reviews/director_quantitative_rmt_round14.md). Reproduce the [rational Hermite certificates](experiments/code/geometry111_rankone_hankel_certificate.py) and distinguish the formal negative squares from the positive exact Petrov factors.
4. Read the [two-scale modulus proof](audits/adversarial_reviews/director_two_scale_round13.md). Check the universal quantifiers and the scope of the compiled scalar implication.
5. Check the version pins in the [Hughes–Rudnick repair](audits/adversarial_reviews/director_hughes_rudnick_whole_round13.md) and the [Báez-Duarte audit](audits/adversarial_reviews/director_baez_whole_round13.md). The six new Round 14 dependencies have targeted Level 0 coverage.
6. For the unconditional enclosure, start with the [global Hardy certificate](audits/adversarial_reviews/director_global_hardy_round11.md). Query stable claims in the [archive index](graphs/archive_index.md) and use [CONTINUATION](CONTINUATION.md) for the rebuild sequence.
"""
    if current_round >= 15:
        research_guide = """
1. Read the [Round 15 synthesis](final_synthesis/round15_report.md) and select a [ranked problem](final_synthesis/top_25_research_opportunities.md). Check the pinned edition and the hypotheses before reusing a result.
2. Start with the [long-prime moving-phase estimate](audits/adversarial_reviews/director_long_prime_round15.md). Reproduce the residue-array obstruction and the exact padded level, then identify which estimates use a common arithmetic sequence.
3. Compare the [absolute Mellin endpoint witness](audits/adversarial_reviews/director_critical_endpoint_round15.md) with the [sufficient trace conditions](audits/adversarial_reviews/director_mellin_explicit_formula_round15.md). The signed p=3 height limit remains open.
4. Trace the [explicit Abel constant](audits/adversarial_reviews/director_explicit_abel_round15.md) through the [Gonek proof](audits/adversarial_reviews/director_gonek_whole_round15.md). Allocate the remaining saddle, good-height and tail errors before claiming a numerical onset.
5. Compare the scoped [Morse formula repairs](audits/adversarial_reviews/director_morse_scoped_round15.md) and [Bombieri–Lagarias manuscript findings](audits/adversarial_reviews/director_mellin_explicit_formula_round15.md) with the source statements. Both works retain complete-reading Level 1.
6. Query stable IDs in the [archive index](graphs/archive_index.md) and use [CONTINUATION](CONTINUATION.md) for the rebuild sequence. The [global Hardy certificate](audits/adversarial_reviews/director_global_hardy_round11.md) gives the current unconditional C₂ interval.
"""
    if current_round >= 16:
        research_guide = """
1. Read the [Round 16 synthesis](final_synthesis/round16_report.md) and select a [ranked problem](final_synthesis/top_25_research_opportunities.md).
2. Start with the [long-prime moving-phase estimate](audits/adversarial_reviews/director_long_prime_round15.md). Check which bounds use common-sequence compatibility and which use fixed-residue factorability.
3. Compare the [critical signed contour proof](audits/adversarial_reviews/director_signed_mellin_round16.md) with the [absolute endpoint witness](audits/adversarial_reviews/director_critical_endpoint_round15.md). Check the local H¹ hypothesis and distinguish symmetric p=0 convergence, separate half-axis convergence for p>1, and the p>3 absolute theorem. The continuous cusp lies outside literal (A).
4. Trace the [finite convolution and Abel constants](audits/adversarial_reviews/director_gonek_constants_round16.md) through Gonek’s Lemmas 7 and 8. Identify the remaining estimates needed for a numerical derivative-tail onset.
5. Read the [Riemann memoir audit](audits/adversarial_reviews/director_riemann1859_whole_round16.md). Track the paired normalization, Genocchi’s known correction, the later ordered midpoint theorem, and the effect of changing the zero order.
6. Consult the [archive index](graphs/archive_index.md) for claim IDs, including the Level 1 Luecking context for ambient absolute sampling. Use [CONTINUATION](CONTINUATION.md) for the rebuild sequence.
"""
    if current_round >= 17:
        research_guide = f"""
1. Read the [Round 17 synthesis]({current_report}). In the stated logarithmic Mellin scale the universal symmetric signed threshold is p≥0 and the absolute threshold is p>3. The p>1 half-axis convergence result is a separate sufficiency statement.
2. Reproduce the fixed-prime sharp-inversion estimate and the two protected subsequences of the smooth all-weaker-log witness. Check that every prime-power sample vanishes and that the infinite prime sum is where the cutoff limit fails. [Signed obstruction](audits/adversarial_reviews/director_negative_mellin_round17.md) · [Absolute endpoint](audits/adversarial_reviews/director_critical_endpoint_round15.md)
3. Trace the two discrepancy budgets for the common sequence. Use P/k and the induced unit means in the model. Test simultaneous unit support and P/φ(k) centering for the actual moving-phase problem.{bounded_phase} [Common-sequence obstruction](audits/adversarial_reviews/director_common_sequence_round17.md) · [Rough-support boundary](frontiers/round17_program_update.md)
4. Compare the two complete 51-page readings of PAPER-H406. Check the p. 293 compact-domain qualification and reconstruct the ordered midpoint convention. [First reading](audits/adversarial_reviews/analytic167_mangoldt1895_whole_advocate.md) · [Second reading](audits/adversarial_reviews/geometry167_mangoldt1895_whole_skeptic.md)
5. Choose either the unit-baseline diagnostic or one finite (1,1) derivative-tail budget from the ranked list. The budget starts with the finite convolution and Abel constants. [Ranked problems](final_synthesis/top_25_research_opportunities.md) · [Finite constants](audits/adversarial_reviews/director_gonek_constants_round16.md)
6. Look up the relevant claim IDs, run the integration sequence, and check the predecessor receipt before sealing. [Archive index](graphs/archive_index.md) · [Continuation](CONTINUATION.md)
"""
    write_text(root, "START_HERE.md", f"""# START HERE — one research day

{count} {SOURCE_SCOPE}

{research_guide.strip()}

Every record retains its source version and reading or proof scope. A targeted inspection can carry substantial mathematical context at Level 0.
""")

    write_text(root, "final_synthesis/comprehensive_report.md", f"""# Current mathematical synthesis

{SOURCE_SCOPE}

{table}

{synthesis.strip()}

Earlier numbered reports preserve historical checkpoints. Use the current masters and registry for current counts, promotion scope, and proof status.
""")

    write_text(root, "quality/coverage_report.md", f"""# Coverage at this checkpoint

{table}

{SOURCE_SCOPE}

The catalogue contains {metrics['catalogued_works']:,} canonical identities, including {metrics['deferred_supporting_works']:,} deferred supporting records. The access and audit manifest gives exact source versions, reading scope, and access status. Selected records with targeted or excerpt-only coverage remain distinguishable from complete readings.

The [family and historical cross-tabs](coverage_taxonomy_report_round10.md) use overlapping labels with recorded evidence. A metadata-inferred label only supports selection or coverage analysis. The [provider reconciliation](provider_candidate_reconciliation_round10.md) documents unresolved duplicate and version groups against its pinned input. Provider rows and selected works overlap.

{pending}
""")

    write_text(root, "quality/limitations.md", rf"""# Evidence and resource limits

{count} {SOURCE_SCOPE}

The cumulative and fixed-band arithmetic limits use RH and the symmetric strict derivative-weighted tail. Weak Gaussian convergence at a fixed power cutoff holds below exponent 1/2. Moments through order \(2k\) there require \(k\theta<1/2\). Arbitrary growing-dimensional vectors need their own coefficient and covariance control. The rooted CUE comparison covers the limiting cosine and sine means and covariance and the centered cosine third moment. A complete arithmetic polynomial-band law and practical numerical onsets are open.{round12_evidence}{round13_evidence}{round14_evidence}{round15_evidence}{round17_evidence}

The C₂ enclosure {C2_INTERVAL} is unconditional for the critical-line series. Its identification with the tapered array limit uses RH. The upper endpoint comes from a global Hardy bound beyond the existing height-10,000 census. The conditional quartic splice near 0.65339 has unallocated constants, and the finite-length prime-array remainder requires a separate estimate.

The finite trace test assumes reciprocal symmetry in one compatible finite spectrum with positive multiplicities. Deninger’s obstruction uses an odd quaternionic Artin sector in the proposed universal real theory. The Suzuki finding concerns the deterministic compensated translation in the pinned preprint. The source’s screw kernel and real-part criterion are independent of that translation.

{pending} The whole-work registry names classical inputs accepted in each version-specific audit. Other technical reviews retain their scoped classification. Priority and correction-history searches are bounded.

Formal compilation, declaration checks, continuum search replay, and interval arithmetic have distinct trust boundaries. Structural validation checks record consistency and exact package bytes. Runtime usage balance is unavailable. Durable receipts record completed work and actual process state.
""")

    write_text(root, "quality/evidence_audit.md", f"""# Evidence audit

{count}

The [whole-work registry](whole_work_audit_promotions.jsonl) records exact editions and SHA-256 values, independent reviews, the director adjudication, and a coverage checklist. Deninger’s arXiv v2 audit includes a separate published-edition comparison and two primary routes to the odd Artin multiplicity. {pending}

The findings ledger contains {errors:,} groups flagged as independently witnessed version-specific false assertions. The group count is distinct from the number of papers or authors. The Suzuki sign finding identifies a precise auxiliary display and a class-valid witness, with the publisher version outside the verified scope.

Round 11's scoped evidence includes the sharp continuous moment interface, fixed-band second and third moments, the rooted CUE match, the low-influence and Brownian limits, the finite integer trace algorithm, and the global Hardy certificate. The latter uses the same height-10,000 complete finite census as the prior checkpoint, with a new rigorous analytic tail. Two precision replays check the global bound. The scoped records and director notes carry the exact hypotheses.{round12_evidence}{round13_evidence}{round14_evidence}{round15_evidence}{round17_evidence}

Earlier compilation and numerical receipts remain available. The distribution validator derives counts from sealed masters, checks promotion alignment and code pins, and compares exact payload hashes and the separate PDF and HTML.
""")

    tasks = [
        ("Identify the fixed-band law", "Control characteristic functions or a determining family of higher moments for arithmetic bands. Compare the globally tilted rooted CUE candidate beyond the proved means, covariance, and centered cosine third moment."),
        ("Quantify the arithmetic-to-CUE comparison", "Bound the finite-size error in the band means, covariance, and centered cosine third moment and determine where higher Fourier words exceed the shifted-moment support."),
        ("Study the small-exponent crossover", "Let both fixed polynomial-band exponents shrink with Y and specify the centering, variance, and scale at which the Gaussian limit returns."),
        ("Allocate the quartic error constants", "Make the fixed Q₂ product approximation and shifted-moment error numerical. Combine it with the exact quartic to certify the splice rather than treating it as an observation."),
        ("Reach a one-percent C₂ enclosure", "Use the analytic tail below 0.00591413 at height 2.8 million and determine the finite interval computation needed to meet the target. The larger census is still uncomputed."),
        ("Improve the finite-length arithmetic error", "Close the near-zero and infinite-height pieces of the tapered prime-array remainder with explicit constants. Its norm is separate from the C₂ series tail."),
        ("Bound the exceptional-coordinate contribution", "Derive a usable estimate for a prescribed prime that divides the possible exceptional conductor, keeping the case of macroscopic influence."),
        ("Compute a conditional onset height", "Allocate the contour, moment comparison, and approximation constants for a fixed scalar test and tolerance. Report the dominant loss."),
        ("Extend the functional bandwidth", "Prove a suitable subset increment bound at larger prime cutoffs before transferring tightness beyond the established reciprocal clock."),
        ("Quantify the Brownian approximation", "Give a numerical path-metric error using explicit time-change and all-time interpolation bounds."),
        ("Test growing-dimensional prime arrays", "Preserve the actual Dirichlet coefficient envelope and specify a metric that accommodates singular limiting covariance."),
        ("Establish derivative-weighted tightness", "Identify a zeta-specific positive or signed estimate preventing far-tail mass escape. Retain both shifts and the stated finite support."),
        ("Bound signed correlations", "Prove an arithmetic signed pair or shifted-moment estimate strong enough to improve the weighted tail."),
        ("Control factorial prefix endpoints", "Find cancellation in the residual at cell endpoints and compare it with the explicit hard-cutoff counterexample."),
        ("Accelerate exact finite trace certification", "Compare rational Toeplitz pivoting, Bezoutian structure, and coefficient bit growth with repeated and reducible roots."),
        ("Characterize sparse power tests", "Determine which exponent sets force purity for fixed integral reciprocal degree. Keep the known prime-degree counterexample in the test set."),
        ("Construct a compatible number-field trace", "Specify the trace power identities, summability, and positivity needed for a genuine arithmetic realization."),
        ("Evaluate complex and quaternionic descent", "Test which replacement categories preserve the Artin multiplicity axiom and what positive form remains to be constructed."),
        ("Control height-normalized central laws", "Quantify convergence at a moving zero and retain the regular logarithmic derivative and the signed compensated translation."),
        ("Sharpen the multiplicity-law tail", "Use cancellation without relying on an ordinary first moment. Separate the tail asymptotic from an atom-mass estimate."),
        ("Refine finite inverse stability", "Quantify what finitely many noisy Cₖ recover about an atomic measure, allowing the specified diffuse competitors."),
        ("Find an arithmetic all-grid obstruction", "Seek a condition from the prime-side formula that excludes the bounded-grid entire-function countermodel."),
        ("Adjudicate recent whole-work reviews", "Resolve the remaining edition and proof issues against the original sources, then register only the versions accepted by the director."),
        ("Increase substantive historical coverage", "Prioritize dependency-central full readings across underrepresented language and historical strata. Verify identity before counting a newly accessed manifestation."),
        ("Check priority for the strongest deductions", "Search the exact weights, quantifiers, ranges, and adjacent random-matrix formulas before assigning novelty."),
    ]
    if current_round >= 12:
        tasks[:3] = [
            ("Identify the fixed arithmetic band law", "Control the arithmetic characteristic function and test convergence to the established compensated rooted CUE law. The proved third tensor leaves the law undetermined."),
            ("Cross the finite moment window", "Derive the first arithmetic frequency-chamber correction beyond the shifted-moment support. The formal all-order extrapolation is obstructed."),
            ("Extend the shrinking-band functional limit", "Use the proved time-changed Brownian limit as a baseline. Determine which smaller lower endpoints or more general endpoint families admit a uniform modulus."),
        ]
    if current_round >= 13:
        tasks[:3] = [
            ("Estimate the fixed signed C_* sum", "Prove a real o(T log⁴T) estimate after the smooth cutoff and principal subtraction in the pure fourth arm. Keep the primitive Gauss phases, common-divisor blocks and the coefficient sequence d₂ * (Λ log²). Under RH this would extend the arithmetic fourth cosine moment for 1/8<b<1/6."),
            ("Identify the fixed arithmetic band law", "Test characteristic functions against the compensated rooted CUE candidate. Use the proved moments only in the RH arithmetic window rb<1/2 and account for the obstruction to all-order extrapolation."),
            ("Analyze later intrinsic CUE frequency chambers", "Use the first-crossing formula and finite matrix checks as controls. Determine how paths that can visit both forbidden regions change the actual moments beyond rb≤1."),
        ]
        tasks[8] = (
            "Extend the shrinking-band functional limit",
            "Use the universal two-scale threshold to identify the smallest usable lower endpoint and the bounds needed for new endpoint families. Derive arithmetic envelopes before invoking the grid theorem.",
        )
    if current_round >= 14:
        tasks[0] = (
            "Estimate the remaining long-prime part of the fixed signed C_* sum",
            "Prove the real o(T log⁴T) estimate after the smooth cutoff and principal subtraction. "
            "Use the proved all-square range θ<9/17 and the two inverse-prime regions with gcd grouping. "
            "Control longer primes and, where necessary, the remaining middle square range. "
            "[Current reduction](../audits/adversarial_reviews/director_arithmetic_strata_round14.md)",
        )
        tasks[2] = (
            "Quantify higher-rank rooted CUE positivity witnesses",
            "Use the explicit all-rank bound and the exact rank-one Hermite criterion as controls. "
            "Determine the least failure order at larger ranks and relate it to the true-cutoff Petrov factors "
            "and later intrinsic frequency chambers. "
            "[Quantitative results](../audits/adversarial_reviews/director_quantitative_rmt_round14.md)",
        )
    if current_round >= 15:
        tasks[0] = (
            "Estimate the remaining long-prime moving phase",
            "Prove the sufficient block square bound with the true centered phase R_k(h,p), or bound the "
            "signed aggregate directly. Preserve cross-modulus compatibility and use the exact padded "
            "factorability level when comparing fixed-residue inputs. "
            "[Open estimate](../audits/adversarial_reviews/director_long_prime_round15.md)",
        )
        tasks[4:4] = [
            (
                "Resolve the signed Mellin endpoint at p=3",
                "Determine whether the original value bounds and the critical logarithmic norm imply "
                "signed symmetric height convergence, or construct a sign-coherent counterexample. "
                "The proved absolute divergence does not decide this. "
                "[Endpoint proof](../audits/adversarial_reviews/director_critical_endpoint_round15.md)",
            ),
            (
                "Propagate the explicit Abel constant through the derivative tail",
                "Starting with the uniform prime-to-integral substitution, bound the remaining divisor "
                "convolution, contour, saddle and good-height errors through the strict weighted-zero tail. "
                "[Abel estimate](../audits/adversarial_reviews/director_explicit_abel_round15.md)",
            ),
            (
                "Carry the corrected Morse normalization into a canonical-system comparison",
                "Check the shifted Hermite–Biehler hypotheses and keep the first-order parameter z "
                "separate from Schrödinger energy z². Compare the resulting norming data rather than "
                "only the smooth counting function. "
                "[Scoped repairs](../audits/adversarial_reviews/director_morse_scoped_round15.md)",
            ),
        ]
        for index in (22, 18, 13):
            del tasks[index]
        tasks[22] = (
            "Adjudicate recent complete readings",
            "Complete the independent Riemann source audit and distinguish the pinned Morse v6 and "
            "Bombieri–Lagarias author manuscript from their separate journal editions. Carry the scoped "
            "findings and exact source hypotheses into any later whole-work decision.",
        )
    if current_round >= 16:
        tasks[4] = (
            "Test weaker assumptions for signed Mellin sampling",
            "Use the critical symmetric contour theorem and the p>1 half-axis proof as benchmarks. "
            "Determine which weaker strip or local hypotheses still give an ordinary height limit. "
            "Keep the continuous cusp outside literal (A) and the smooth absolute-divergence witness separate. "
            "[Signed critical formula](../audits/adversarial_reviews/director_signed_mellin_round16.md)",
        )
        tasks[5] = (
            "Propagate explicit finite constants through the derivative tail",
            "Start from the positive-order divisor-convolution and finite (1,1) Lemma 8 estimates. "
            "Allocate the remaining contour, saddle, good-height and zero-tail errors. "
            "[Finite constants](../audits/adversarial_reviews/director_gonek_constants_round16.md)",
        )
        tasks[22] = (
            "Reconstruct von Mangoldt’s ordered midpoint argument",
            "Compare the later ordered midpoint ψ₀ formula with the J₀ reconstruction in the Riemann "
            "audit. Track the height ordering, summable kernel remainder and midpoint convention. "
            "[Historical reconstruction](../audits/adversarial_reviews/director_riemann1859_whole_round16.md)",
        )
    if current_round >= 17:
        tasks[0] = (
            "Test the long-prime moving phase with the actual unit baseline",
            "Impose simultaneous unit support or explicit rough support and center unit rows at P/φ(k). "
            "Compute the pooled variance and sum of row maxima before testing the exact c_k/k phase "
            "or the sufficient block square bound. The common-sequence examples establish the ordinary "
            "integer and induced-unit baselines." + bounded_phase + " "
            "[Baseline and phase](../audits/adversarial_reviews/director_common_sequence_round17.md)",
        )
        tasks[1], tasks[5] = tasks[5], tasks[1]
        tasks[4] = (
            "Check the truncation mode in signed Mellin applications",
            "For one existing trace test, certify its strip norm and local H¹ or literal (A) hypotheses. "
            "Apply p≥0 for symmetric truncation, p>1 when using the separate half-axis theorem, or "
            "p>3 when the application needs absolute convergence. "
            "[Symmetric boundary](../audits/adversarial_reviews/director_negative_mellin_round17.md) · "
            "[Half-axis sufficiency](../audits/adversarial_reviews/director_signed_mellin_round16.md)",
        )
        tasks[22] = (
            "Reconstruct the ordered midpoint proof on compact x-domains",
            "Check the p. 293 uniformity wording in the pinned 1895 print, keeping the ordered zero limit, "
            "grouped remainder and midpoint convention explicit. Compare the two complete Level 1 readings. "
            "[Pinned reading](../audits/adversarial_reviews/analytic167_mangoldt1895_whole_advocate.md)",
        )
    if len(tasks) != 25:
        raise ValueError("The research problem list must contain exactly 25 entries.")
    task_text = numbered([f"**{title}.** {body}" for title, body in tasks])
    write_text(root, "final_synthesis/top_25_research_opportunities.md",
               "# Twenty-five actionable research problems\n\n" + task_text)
    write_text(root, "final_synthesis/open_problems_for_future_agents.md",
               "# Open problems for future agents\n\nRead CONTINUATION.md for the build and evidence sequence.\n\n" + task_text)
    write_text(root, "proposals/ranked_research_directions.md", "# Ranked research directions\n\n" + task_text)

    strongest_connections = r"""# Strongest currently adjudicated interactions

1. **A cumulative Gaussian limit coexists with non-Gaussian bands.** The bounded-coefficient aggregate moment calculation controls a cumulative scalar cutoff through fixed powers below 1/2. Below band exponent 1/6 the centered cosine third moment is negative, with uniform integrability from fourth moments. [Adjudication](../audits/adversarial_reviews/director_polynomial_bands_round11.md)
2. **Rooting and derivative-square tilting change CUE moments.** The rooted projection removes the constant and centered linear coefficient directions. Its cosine and sine means, covariance, and centered cosine third moment match the conditional arithmetic formulas in their respective ranges. [Adjudication](../audits/adversarial_reviews/director_polynomial_bands_round11.md)
3. **Low influence and subset moments lead to Brownian motion.** The fixed-dimensional Gaussian criterion handles finite-dimensional convergence. Uniform fourth moments of all subsets of primes \(p\le\log Y\) give tightness after interpolation in the reciprocal-prime clock. [Adjudication](../audits/adversarial_reviews/director_joint_brownian_round11.md)
4. **The global weighted Hardy bound controls the full C₂ series.** Applying variation to the two components of a single cutoff times Q₂Z/t retains arithmetic cancellation and treats the infinite endpoint. [Adjudication](../audits/adversarial_reviews/director_global_hardy_round11.md)
5. **A short joint trace matrix tests purity.** A classical power-sum criterion becomes an exact integer matrix test whose inertia counts distinct circle roots and distinct off-circle reciprocal-conjugate pairs, with a rational elimination algorithm. [Adjudication](../audits/adversarial_reviews/director_integer_trace_round11.md)
6. **Artin multiplicity can obstruct real descent.** The even multiplicity forced by real complexification contradicts an odd central Artin sector for an explicit quaternionic example. [Whole-work adjudication](../audits/adversarial_reviews/director_deninger_whole_round11.md)
7. **A drift correction leaves the screw kernel invariant.** The extended-class example changes the compensating deterministic translation and preserves the source’s jump and real-part quantities. [Adjudication](../audits/adversarial_reviews/director_suzuki_drift_round11.md)
8. **The two zero-weighted probability laws have different asymptotics.** The multiplicity-weighted law has dense atoms and Cauchy scaling, while the conditional derivative-weighted cumulative phase law is Gaussian. [Multiplicity law](../audits/adversarial_reviews/director_probability_tail_round10.md) · [Phase law](../audits/adversarial_reviews/director_polynomial_bands_round11.md)
9. **Finite-grid positivity leaves an arithmetic gap.** A countermodel can preserve bounded-grid positivity, smooth counting and the quadratic cusp while retaining off-line zeros. [Adjudication](../audits/adversarial_reviews/director_bounded_positivity_round10.md)
"""
    if current_round >= 13:
        strongest_connections = r"""# Strongest currently adjudicated interactions

1. **The long arithmetic fourth moment reduces to a fixed signed sum.** Under RH, for 1/8<b<1/6 the mixed arms are covered. Asymmetric continuous estimates, smooth saddle replacement and divisor cancellation leave the signed sum with C_*=d₂*(Λ log²) in the pure arm. The estimate remains open. [Adjudication](../audits/adversarial_reviews/director_pure_fourth_round13.md)
2. **The rooted CUE window includes its endpoint.** The finite inverse compression uses the two signed frequency totals and proves the intrinsic window rb≤1. The conditional arithmetic range is rb<1/2. [Adjudication](../audits/adversarial_reviews/director_cue_windows_round13.md)
3. **The first crossing detects terms outside the CUE window.** The cosine discrepancy has rank-dependent sign. The formal cosine extrapolation at every fixed integer tilt rank has a positive real zero and a finite negative square witness. [Adjudication](../audits/adversarial_reviews/director_cue_windows_round13.md)
4. **Two node-increment estimates give a sharp universal threshold.** Interpolation and the grid modulus yield tightness when A_n ε_n^(b−1)→0 and the initial values are tight; a random spike proves sharpness over grids and laws. Lean checks only a scalar implication with both bounds as premises. [Adjudication](../audits/adversarial_reviews/director_two_scale_round13.md)
5. **The smooth explicit formula exposes the exact averaging condition.** The Hughes–Rudnick whole-note audit repairs the finite moment window with a logarithmic weight moment or a mean-zero test. The isolated prime statistic retains the printed weight class. [Adjudication](../audits/adversarial_reviews/director_hughes_rudnick_whole_round13.md)
6. **Work identity and proof scope are separate.** Báez-Duarte’s two preprint deposits belong to one canonical work; the journal audit and version-specific theorem locators preserve the ordered limits and quantitative scope. [Adjudication](../audits/adversarial_reviews/director_baez_whole_round13.md)
7. **A cumulative Gaussian limit coexists with non-Gaussian bands.** The RH-conditional cumulative limit holds through fixed powers below one half. The fixed-band centered cosine cubic and uniform fourth moments exclude Gaussian subsequences below exponent one sixth. [Adjudication](../audits/adversarial_reviews/director_polynomial_bands_round11.md)
8. **The global Hardy cutoff controls the full C₂ series.** The unconditional bound uses the existing height-10,000 census and a rigorous infinite-height estimate. [Adjudication](../audits/adversarial_reviews/director_global_hardy_round11.md)
9. **Artin multiplicity obstructs universal real descent.** An odd central Artin multiplicity in an explicit quaternionic example conflicts with real complexification. [Whole-work adjudication](../audits/adversarial_reviews/director_deninger_whole_round11.md)
10. **The exact tilted Toeplitz factors explain a quadratic mismatch.** Petrov’s tilted tail contributes inside the moment window. The exact real factors stay positive while the formal determinant extrapolation has a positive real zero. [Adjudication](../audits/adversarial_reviews/director_petrov_round13.md)
"""
    if current_round >= 14:
        strongest_connections += """
11. **Averaged inverse-prime sums cover additional arithmetic scales.** Divisor Voronoi and gcd grouping permit Baker and Fouvry–Shparlinski bounds on two strict regions. All squares are removed for 1/2<θ<9/17. The long-prime estimate remains open. [Adjudication](../audits/adversarial_reviews/director_arithmetic_strata_round14.md)
12. **Hermite zeros locate the first rank-one negative square.** Explicit finite witnesses for all ranks and factorial approximation of the positive Petrov quotient quantify the difference between extrapolated and exact factors. [Adjudication](../audits/adversarial_reviews/director_quantitative_rmt_round14.md)
"""
    if current_round >= 15:
        strongest_connections += """
13. **Absolute and signed zero sampling have distinct endpoint questions.** The critical logarithmic Mellin norm with p>3 controls absolute sampling. At p=3 a smooth admissible example has divergent absolute mass, while the signed height limit remains open. [Endpoint adjudication](../audits/adversarial_reviews/director_critical_endpoint_round15.md)
14. **Padded factorability and the moving phase are separate inputs.** The four-prime coefficient satisfies the fixed-residue theorem's factorability hypothesis at the padded level. A row countermodel defeats the two phase-blind norm implications outside the common-sequence setting. [Phase and level](../audits/adversarial_reviews/director_long_prime_round15.md)
15. **An explicit PNT bound gives one numerical Gonek input.** The resulting Abel constant is uniform in the stated shift range. Computing a derivative-tail onset still requires the remaining estimates. [Abel substitution](../audits/adversarial_reviews/director_explicit_abel_round15.md)
"""
    if current_round >= 16:
        strongest_connections = strongest_connections.replace(
            "while the signed height limit remains open.",
            "and has signed symmetric convergence by the Round 16 critical contour theorem.",
        )
        strongest_connections += """
16. **Critical strip regularity suffices for the symmetric explicit formula.** The p=0 signed limit uses local H¹ at one. The p>1 Selberg proof additionally gives half-axis convergence. A p=3 cusp outside literal (A) diverges without the local condition. [Critical contour](../audits/adversarial_reviews/director_signed_mellin_round16.md)
17. **Paired normalization fixes the real constant in the ordered prime-power formula.** The modern Riemann reconstruction uses Genocchi’s −log 2 correction and von Mangoldt’s later midpoint input. [Whole-work audit](../audits/adversarial_reviews/director_riemann1859_whole_round16.md)
"""
    if current_round >= 17:
        strongest_connections += f"""
18. **Uniform inversion controls the infinite arithmetic trace.** The universal signed symmetric threshold is p≥0 with the value and local hypotheses. One smooth witness with zero prime-power samples fails at every strictly weaker logarithmic weight. The absolute threshold is p>3. [Boundary proof](../audits/adversarial_reviews/director_negative_mellin_round17.md)
19. **Common-sequence compatibility allows a large moving phase under integer centering.** The two discrepancy budgets hold about P/k or induced unit means. The prime-model unit support and P/φ(k) baseline remain open.{bounded_phase} [Common-sequence proof](../audits/adversarial_reviews/director_common_sequence_round17.md)
"""
    write_text(root, "connections/strongest_connections.md", strongest_connections)

    old = (root / "final_synthesis/round10_top_100_insights.md").read_text(encoding="utf-8")
    previous = re.findall(r"^\d+\. (.+)$", old, re.MULTILINE)
    updates = [
        r"**The cumulative cutoff reaches fixed powers below one half.** Under RH the standardized cosine sum is weakly Gaussian at \(P=Y^\theta\) for fixed \(0<\theta<1/2\). Subpower cutoffs tending to infinity give all fixed Gaussian moments. THM-SCALAR-PRIME-SUBPOWER-POLYNOMIAL.",
        r"**A fixed polynomial band has altered covariance.** Under RH its cosine and sine variances carry different finite-rank corrections when the upper exponent is below \(1/4\). THM-POLYNOMIAL-PRIME-BAND-COVARIANCE.",
        r"**The fixed-band cubic excludes Gaussian subsequences.** For an upper exponent below \(1/6\), the negative centered cosine third moment and uniform fourth moments work together. THM-POLYNOMIAL-PRIME-BAND-NONGAUSSIAN.",
        "**Rooted CUE matches selected limiting moments.** The global derivative-square tilt matches the cosine and sine means and covariance, plus the centered cosine third moment. THM-ROOTED-CUE-PRIME-BAND-MOMENT-MATCH.",
        "**The sharp continuous moment can be checked below half length.** Group integer frequencies before summing reciprocal distance bounds in the product approximation. THM-SHARP-AGGREGATE-CONTINUOUS-J.",
        "**Low influence characterizes the fixed-dimensional Gaussian limit.** With convergent finite covariance and logarithmic support, the largest coefficient column must vanish. THM-JOINT-PRIME-GAUSSIAN-ARRAY.",
        "**Disjoint logarithmic annuli can have finite Gaussian variances.** Their prime contributions vanish individually even though the total variance does not grow. THM-FINITE-VARIANCE-PRIME-ANNULI.",
        "**The reciprocal-prime clock yields a functional limit.** Uniform fourth moments over subsets of primes up to log Y establish tightness for the conditional Brownian process. THM-PRIME-BROWNIAN-PROCESS.",
        f"**A global Hardy cutoff improves the unconditional interval.** The critical-line series satisfies {C2_INTERVAL} using the existing finite census. CERT-GLOBAL-HARDY-C2.",
        "**Purity of a finite reciprocal spectrum has a low-index integer test.** The exact Toeplitz form determines inertia through Newton traces of index below the degree, counting distinct circle roots and distinct off-circle reciprocal-conjugate pairs. THM-INTEGER-TOEPLITZ-PURITY.",
        "**An odd quaternionic Artin multiplicity obstructs universal real descent.** Deninger’s exact scope leaves isolated zeta realizations open. THM-DENINGER-REAL-DESCENT-OBSTRUCTION.",
        "**The compensated drift changes by a deterministic translation.** The pinned Suzuki display has an exact sign witness with unchanged screw kernel. OBS-SUZUKI-COMPENSATED-DRIFT-SIGN.",
    ]
    replaced = {4, 9, 12, 16, 34, 35, 38, 46, 52, 60, 61, 88}
    if current_round >= 13:
        updates = [
            "**The arithmetic fourth moment has a fixed remaining coefficient sequence.** For 1/8<b<1/6 the mixed arms, smooth saddle and divisor terms are controlled. The real signed estimate for C_* = d₂ * (Λ log²) is open. OPEN-HLZ-PURE-FOURTH-CSTAR-CANCELLATION.",
            "**The intrinsic rooted CUE moment window includes rb=1.** The finite compression tracks separate signed frequency totals. The RH arithmetic window remains rb<1/2. THM-ROOTED-CUE-JOINT-CLOSED-MOMENT-WINDOW.",
            "**The first intrinsic cosine correction changes sign with tilt rank.** At the first crossing its sign is (−1)^(J+1); mixed cosine–sine rays can have a different sign. THM-ROOTED-CUE-RANK-CORRECTION-PARITY.",
            "**Every fixed integer rank has an extrapolation barrier.** The formal cosine moment series has a positive real zero and a finite negative square witness. The proved moment window remains valid. OBS-ROOTED-CUE-ALL-RANK-FINITE-SQUARE-BARRIER.",
            "**The two-scale tightness threshold is sharp over grids and laws.** The universal condition is A_n ε_n^(b−1)→0 with tight initial values. The Lean certificate proves only the scalar M=6 envelope step. THM-GRID-TWO-SCALE-UNIVERSAL-TIGHTNESS; CERT-LEAN-TWO-SCALE-SCALAR.",
            "**The Hughes–Rudnick averaging weight needs a logarithmic qualification.** The whole-note audit recovers the first m Gaussian moments with a zero-mean test or a finite mth log moment. THM-HR-REPAIRED-FINITE-GAUSSIAN-MOMENTS.",
            "**Two preprint identifiers can designate one journal work.** The February and May Báez-Duarte deposits retain their own locators under canonical PAPER-E014, with PAPER-E001 retained as an alias.",
        ] + updates
        replaced |= {5, 8, 10, 14, 20, 27, 31}
    if current_round >= 14:
        updates = [
            "**The long-prime part is the first remaining C_* target.** The Baker and Fouvry–Shparlinski windows cover two strict regions in the prime and modulus exponents. Gcd grouping treats nonunit dual indices; the longer primes and full fourth moment remain open. [Adjudication](../audits/adversarial_reviews/director_arithmetic_strata_round14.md)",
            "**A quadratic prime estimate removes every square for 1/2<θ<9/17.** The direct phase after opening the free divisor variable and the exact reduced conductor give a power saving across the whole square stratum. [Adjudication](../audits/adversarial_reviews/director_arithmetic_strata_round14.md)",
            "**The first rank-one negative Hankel square has an exact Hermite threshold.** A strict inequality for the largest Hermite zero determines the least order; rational fixtures check equality and failure. The all-rank circle estimate gives an explicit finite upper bound. [Adjudication](../audits/adversarial_reviews/director_quantitative_rmt_round14.md)",
            "**Exact Petrov tails admit factorial approximation.** A positive finite Schur complement gives the quotient, and the continuum Gram uses the true cutoff. The real factors stay separated from the formal determinant zero. [Adjudication](../audits/adversarial_reviews/director_quantitative_rmt_round14.md)",
        ] + updates
        replaced |= {15, 18, 67, 79}
    if current_round >= 15:
        updates = [
            "**The critical Mellin threshold is sharp for universal absolute zero sampling.** The p>3 trace bound and the smooth p=3 witness leave signed symmetric height convergence at the endpoint open. [Endpoint adjudication](../audits/adversarial_reviews/director_critical_endpoint_round15.md)",
            "**The full prime-product coefficient has an exact padded level.** The least r-way level for D^m/m! is p_*^(m+r−1). The four-prime triple weight therefore meets the padded fixed-residue hypothesis; the modulus-dependent Fourier mode remains open. [Exact level](../audits/adversarial_reviews/director_long_prime_round15.md)",
            "**Phase-blind progression norms leave room for a large target mode.** The positive fictitious rows satisfy both norms but have incompatible common-divisor marginals. This rules out a norm-only implication and leaves arithmetic compatibility available. [Countermodel](../audits/adversarial_reviews/director_long_prime_round15.md)",
            "**An explicit Abel substitution quantifies one derivative-moment step.** The real-shift error is bounded by 31L^m+20mL^(m−1), omitting the second term at m=0. A full derivative-tail constant needs separate estimates. [Abel proof](../audits/adversarial_reviews/director_explicit_abel_round15.md)",
            "**Gonek's derivative-prefix theorem survives three local display repairs.** The eighth whole-work Level 3 audit pins the 1984 journal scan and separates the unconditional shifted identity from its RH corollaries. [Whole-work adjudication](../audits/adversarial_reviews/director_gonek_whole_round15.md)",
            "**A broad explicit-formula class and its compact tests have different scopes.** The pinned Bombieri–Lagarias manuscript has a divergent height-limit witness and a finite correction to (3.5). The compact proof and main limiting result survive. [Scoped adjudication](../audits/adversarial_reviews/director_mellin_explicit_formula_round15.md)",
            "**The Morse first-order quotient has a sign distinct from the energy Weyl function.** The pinned v6 auxiliary shifted function and quotient need separate repairs; the half-line spectral theorem survives. [Scoped Morse findings](../audits/adversarial_reviews/director_morse_scoped_round15.md)",
        ] + updates
        replaced |= {13, 17, 19, 24, 28, 41, 44}
    if current_round >= 16:
        updates[0] = (
            "**Absolute sampling and signed convergence have distinct conclusions.** The p>3 absolute "
            "trace is sharp in its scale. The smooth p=3 absolute-divergence witness has a signed symmetric "
            "limit under the critical H¹⁄² strip theorem with local H¹. "
            "[Critical formula](../audits/adversarial_reviews/director_signed_mellin_round16.md)"
        )
        updates[3] = (
            "**The coefficient and Abel steps in Gonek’s (1,1) calculation have explicit constants.** "
            "The two-positive-order convolution estimate and a finite combined Lemma 8 bound leave a "
            "separate contour and zero-tail budget. "
            "[Finite constants](../audits/adversarial_reviews/director_gonek_constants_round16.md)"
        )
        updates = [
            "**The signed critical contour requires local regularity at one.** A continuous p=3 cusp outside literal (A) gives divergence, while literal (A) and the critical norm imply local H¹. The p>1 proof also gives separate half-axis convergence. [Signed theorem](../audits/adversarial_reviews/director_signed_mellin_round16.md)",
            "**The 1859 product and ordered prime-power formula have different proof dependencies.** The genus-zero reconstruction carries the paired normalization. The pointwise ordered identity uses von Mangoldt’s later midpoint formula and Genocchi’s known −log 2 correction. [Whole-work audit](../audits/adversarial_reviews/director_riemann1859_whole_round16.md)",
        ] + updates
        replaced |= {63, 82}
    if current_round >= 17:
        updates = [
            "**The universal signed symmetric logarithmic threshold is p≥0.** The original value bounds "
            "and local H¹, or literal (A) with midpoint values, give the signed formula in the fixed strip. "
            "The universal absolute threshold is p>3. "
            "[Exact signed boundary](../audits/adversarial_reviews/director_negative_mellin_round17.md)",
            "**One smooth test defeats every strict logarithmic weakening.** Its prime-power samples vanish, "
            "its pole and archimedean terms are finite, and its raw zero sums have both a bounded subsequence "
            "and one tending to −∞. [Escaped-prime construction](../audits/adversarial_reviews/director_negative_mellin_round17.md)",
            "**Integer weights can respect common-sequence compatibility and still give a large moving phase.** "
            "The two discrepancy bounds use P/k or induced unit means. A sieve or prime-supported estimate "
            "must address P/φ(k) and the simultaneous unit support." + bounded_phase + " "
            "[Common-sequence scope](../audits/adversarial_reviews/director_common_sequence_round17.md)",
            "**The ordered midpoint source has two complete readings.** The pinned 1895 von Mangoldt journal "
            "article has 51 pages and Level 1 reading scope. The p. 293 wording carries the compact-domain "
            "qualification. [Pinned reading](../audits/adversarial_reviews/geometry167_mangoldt1895_whole_skeptic.md)",
        ] + updates
        replaced |= {1, 2, 3, 6}
    insights = updates + [entry for index, entry in enumerate(previous, 1) if index not in replaced]
    if len(previous) != 100 or len(insights) != 100:
        raise ValueError("The archived and current insight lists must each contain 100 entries.")
    write_text(root, "final_synthesis/top_100_insights.md",
               "# 100 supported synthesis insights\n\n"
               "The entries include established results, reconstructions, countermodels, and scoped deductions. "
               "The earlier list is preserved in round10_top_100_insights.md.\n\n" + numbered(insights))

    write_text(root, "CONTINUATION.md", f"""# Continuous execution and next checkpoint

{count}

Continue source-grounded research with GPT-6.2 Sol on resumption. Check actual job status and durable receipts before resuming interrupted work. Runtime usage balance is unavailable.{stopping_point}

{continuation_priorities} The [ranked problems](final_synthesis/top_25_research_opportunities.md) give exact next statements. The global Hardy bound and joint Brownian limit have director adjudications.{continuation_update} {pending}

After approved mathematical or corpus changes, run from the archive root:

```bash
{first_integration}{next_integration}
python scripts/build_archive.py
python scripts/merge_findings.py
python scripts/write_live_checkpoint.py
python scripts/build_coverage_taxonomy.py
python scripts/export_archive_index.py build
python scripts/validate_archive.py
```

Freeze checkpoint {checkpoint_number} as an immutable snapshot under the existing distribution policy. Render from that snapshot using `scripts/render_and_package.py`, validate the exact ZIP and separate PDF/HTML using `scripts/validate_sealed_checkpoint.py`, and obtain independent sealed QA. Run the first-release generators only when recreating their dated outputs.

Reuse the distribution targets recorded in [the checkpoint receipt](quality/checkpoints/checkpoint{receipt_number}_drive_receipt.json). Verify metadata after authorized upload. Record that receipt after sealing so it does not create a self-reference in the current ZIP.
""")

    state_path = root / "quality/execution_state.json"
    state = json.loads(state_path.read_text(encoding="utf-8"))
    state.update(
        date=metrics["cutoff"],
        updated_at_utc=datetime.now(timezone.utc).isoformat(),
        last_prepared_checkpoint=f"checkpoint{checkpoint_number}_preparing",
        current_prose_round=current_round,
        current_mathematical_work=[title for title, _ in tasks[:9]],
        background_work="GPT-6.2 Sol research and review continue. Use actual process receipts for status.",
    )
    if current_round == 15:
        state["continuation"] = continuation_priorities
        state["current_work"] = (
            "Round 15 ledger and reports prepared. Long-prime phase, signed Mellin endpoint "
            "and the remaining explicit derivative-tail constants are open."
        )
        if state.get("last_delivered_checkpoint") in (None, "checkpoint11"):
            receipt_path = f"quality/checkpoints/checkpoint{receipt_number}_drive_receipt.json"
            receipt = json.loads((root / receipt_path).read_text(encoding="utf-8"))
            zip_entry, = [file for file in receipt["files"] if file["kind"] == "zip"]
            if receipt["checkpoint"] != "checkpoint11" or receipt["status"] != "delivered_verified_metadata":
                raise ValueError("Checkpoint 11 receipt lacks verified delivery metadata.")
            state.update(status="active_after_checkpoint11", last_delivered_checkpoint=receipt["checkpoint"],
                         last_delivered_sha256=zip_entry["sha256"], delivery_receipt=receipt_path)
    if current_round >= 16:
        state["continuation"] = continuation_priorities
        state["current_work"] = (
            "Round 16 ledger and reports prepared. The critical symmetric Mellin formula is proved "
            "under its stated local hypotheses. The long-prime phase and remaining derivative-tail constants are open."
        )
        receipt_path = f"quality/checkpoints/checkpoint{receipt_number}_drive_receipt.json"
        receipt = json.loads((root / receipt_path).read_text(encoding="utf-8"))
        expected = f"checkpoint{receipt_number}"
        if receipt["checkpoint"] != expected or receipt["status"] != "delivered_verified_metadata":
            raise ValueError(f"{expected} receipt lacks verified delivery metadata.")
        zip_entry, = [file for file in receipt["files"] if file["kind"] == "zip"]
        last_delivered = state.get("last_delivered_checkpoint")
        if not last_delivered or int(last_delivered.removeprefix("checkpoint")) <= receipt_number:
            state.update(status=f"active_after_{expected}", last_delivered_checkpoint=expected,
                         last_delivered_sha256=zip_entry["sha256"], delivery_receipt=receipt_path)
    if current_round >= 17:
        state["current_work"] = (
            "Round 17 ledger and reports prepared. The signed Mellin threshold is sharp in the stated "
            "logarithmic scale. The prime-model unit-baseline phase and the remaining explicit "
            "derivative-tail estimates are open."
        )
        state["background_work"] = (
            "Complete checkpoint 14 delivery, then pause research pending the next user prompt. "
            "Use actual process receipts for status."
        )
    write_text(root, "quality/execution_state.json", json.dumps(state, ensure_ascii=False, indent=2))
    print(json.dumps({
        "current_prose_round": current_round,
        "selected": metrics["selected_checkpoint_works"],
        "complete_readings": metrics["whole_work_or_translation_read"],
        "whole_Level3": levels.get("3", 0),
        "scoped_groups": metrics["scoped_level3_claim_groups"],
    }))


if __name__ == "__main__":
    archive_root = Path(__file__).resolve().parents[1]
    write_current(archive_root, json.loads((archive_root / "quality/metrics.json").read_text()))
