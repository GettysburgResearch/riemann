from __future__ import annotations

import hashlib
import importlib.util
import json
from collections import Counter
from fractions import Fraction
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "quadratic_family_closed_place_notch_density.py"
)
FIXTURE = SCRIPT.with_suffix(".json")


def _load_module():
    spec = importlib.util.spec_from_file_location("closed_place_notch_density", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load closed-place notch-density producer")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def _inclusive_cutoff_count(module, q: int, n: int) -> int:
    """Small hostile control using d>=h instead of the required d>h."""
    conductor_degree = 2 * n - 1
    threshold = n // 2
    coefficients = [0] * (conductor_degree + 1)
    coefficients[0] = 1
    for degree in range(threshold, conductor_degree + 1):
        available = module.irreducible_count(q, degree)
        updated = [0] * (conductor_degree + 1)
        for subtotal, coefficient in enumerate(coefficients):
            if coefficient == 0:
                continue
            for multiplicity in range((conductor_degree - subtotal) // degree + 1):
                updated[subtotal + multiplicity * degree] += coefficient * comb(
                    available, multiplicity
                )
        coefficients = updated
    return coefficients[conductor_degree]


def _independent_irreducible_table(q: int, maximum_degree: int) -> list[int]:
    """Recover I_q(d) from q^m=sum_(d|m) d*I_q(d), independently of the producer."""
    counts = [0] * (maximum_degree + 1)
    for degree in range(1, maximum_degree + 1):
        residual = q**degree - sum(
            divisor * counts[divisor]
            for divisor in range(1, degree)
            if degree % divisor == 0
        )
        _require(residual % degree == 0, "irreducible recurrence lost integrality")
        counts[degree] = residual // degree
    return counts


def _independent_profile_count(counts: list[int], degrees: tuple[int, ...]) -> int:
    value = 1
    for degree, multiplicity in Counter(degrees).items():
        value *= comb(counts[degree], multiplicity)
    return value


def _independent_one_two_three_count(q: int, n: int) -> int:
    conductor_degree = 2 * n - 1
    first_allowed = n // 2 + 1
    counts = _independent_irreducible_table(q, conductor_degree)
    total = counts[conductor_degree]
    for first in range(first_allowed, conductor_degree // 2 + 1):
        second = conductor_degree - first
        total += _independent_profile_count(counts, (first, second))
    for first in range(first_allowed, conductor_degree // 3 + 1):
        for second in range(first, (conductor_degree - first) // 2 + 1):
            third = conductor_degree - first - second
            total += _independent_profile_count(counts, (first, second, third))
    return total


def _independent_digest(rows: list[list[int]]) -> str:
    encoded = json.dumps(rows, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def test_source_lock_imports_the_exact_strict_support_theorem() -> None:
    module = _load_module()
    source = module.load_locked_source()
    _require(source["schema"] == module.SOURCE_SCHEMA, "source schema drifted")
    _require(
        source["payload_sha256"] == module.SOURCE_PAYLOAD_SHA256,
        "source payload lock drifted",
    )
    _require(
        module._git_blob(module.SOURCE, module.SOURCE_COMMIT) == module.SOURCE_BLOB,
        "source git-blob lock drifted",
    )
    odd = source["primitive_conductor_weight_notch"]["odd_M_2n_minus_1"]
    _require("min_i d_i>floor(n/2)" in odd["exact_zero"], "strict cutoff missing")
    _require("S_(n,Q)=0 exactly" in odd["exact_zero"], "exact raw zero missing")


def test_irreducible_counts_are_exact_formula_values() -> None:
    module = _load_module()
    expected = {
        (3, 1): 3,
        (3, 2): 3,
        (3, 3): 8,
        (3, 4): 18,
        (5, 2): 10,
        (5, 3): 40,
        (7, 2): 21,
    }
    for (q, degree), count in expected.items():
        _require(
            module.irreducible_count(q, degree) == count,
            f"I_{q}({degree}) drifted",
        )


def test_low_n_counts_match_independent_factor_degree_formulas() -> None:
    module = _load_module()
    for q in module.REPLAY_QS:
        count = module.irreducible_count
        expected = {
            2: count(q, 3),
            3: count(q, 5) + count(q, 2) * count(q, 3),
            4: count(q, 7) + count(q, 3) * count(q, 4),
            5: (
                count(q, 9)
                + count(q, 3) * count(q, 6)
                + count(q, 4) * count(q, 5)
                + comb(count(q, 3), 3)
            ),
            6: count(q, 11) + count(q, 4) * count(q, 7) + count(q, 5) * count(q, 6),
        }
        for n, value in expected.items():
            _require(
                module.support_forced_zero_count(q, n) == value,
                f"closed factor-degree formula drifted at q={q}, n={n}",
            )


def test_strict_cutoff_is_not_replaced_by_a_weak_inequality() -> None:
    module = _load_module()
    for q in module.REPLAY_QS:
        for n in (3, 5, 7):
            conductor_degree, threshold, first_allowed = module.notch_parameters(n)
            _require(first_allowed == threshold + 1, "strict first degree drifted")
            _require(4 * first_allowed > conductor_degree, "three-factor bound drifted")
            strict = module.support_forced_zero_count(q, n)
            inclusive = _inclusive_cutoff_count(module, q, n)
            _require(
                inclusive > strict,
                f"hostile inclusive cutoff was not detected at q={q}, n={n}",
            )


def test_density_denominator_and_reduction_are_exact() -> None:
    module = _load_module()
    for q in module.REPLAY_QS:
        for n in (2, 3, 5, 20, 80):
            conductor_degree = 2 * n - 1
            total = q**conductor_degree - q ** (conductor_degree - 1)
            count = module.support_forced_zero_count(q, n)
            density = module.support_forced_zero_density(q, n)
            _require(
                module.primitive_squarefree_conductor_count(q, n) == total,
                f"ambient squarefree count drifted at q={q}, n={n}",
            )
            _require(density == Fraction(count, total), "density reduction drifted")
            _require(0 < density < 1, "certified density must be a proper fraction")


def test_bounded_dp_statistics_and_three_factor_cap() -> None:
    module = _load_module()
    for q in module.REPLAY_QS:
        count, statistics = module._support_forced_zero_dp(q, module.MAX_N)
        _require(count > 0, "maximum-n count vanished")
        _require(
            statistics["transitions"] <= module.MAX_DP_TRANSITIONS_PER_ROW,
            "per-row transition cap exceeded",
        )
        _require(
            statistics["peak_nonzero_states"] <= module.MAX_M + 1,
            "DP state cap exceeded",
        )
        _require(
            statistics["maximum_local_multiplicity"] == 3,
            "strict cutoff must allow at most three factors",
        )


def test_public_entrypoints_fail_closed_outside_declared_bounds() -> None:
    module = _load_module()
    refusals = (
        (lambda: module.support_forced_zero_count(9, 5), "q in"),
        (lambda: module.support_forced_zero_count(3, 1), "2<=n<=80"),
        (lambda: module.support_forced_zero_count(3, 81), "2<=n<=80"),
        (lambda: module.irreducible_count(3, 0), "1<=degree"),
        (lambda: module.irreducible_count(3, 160), "1<=degree"),
        (lambda: module.notch_parameters(True), "2<=n<=80"),
        (lambda: module.notch_parameters(2.5), "2<=n<=80"),
        (lambda: module.primitive_squarefree_conductor_count(3, 2.5), "2<=n<=80"),
        (lambda: module.irreducible_count(3.0, 3), "q in"),
        (lambda: module.irreducible_count(3, 3.0), "1<=degree"),
    )
    for call, fragment in refusals:
        try:
            call()
        except ValueError as error:
            _require(fragment in str(error), f"wrong bound refusal for {fragment}")
        else:
            raise AssertionError(f"bounded replay should refuse outside {fragment}")


def test_payload_is_canonical_self_hashed_and_file_locked() -> None:
    module = _load_module()
    payload = module.build_payload()
    stored = json.loads(FIXTURE.read_text(encoding="utf-8"))
    _require(payload == stored, "stored payload drifted")
    unhashed = dict(stored)
    claimed = unhashed.pop("payload_sha256")
    _require(module._canonical_sha256(unhashed) == claimed, "self-hash failed")
    for label, path in {
        "note": module.NOTE,
        "producer": module.Path(module.__file__).resolve(),
        "test": module.TEST,
    }.items():
        digest = hashlib.sha256(path.read_bytes().replace(b"\r\n", b"\n")).hexdigest()
        _require(
            digest == stored["packet_files_lf_sha256"][label],
            f"{label} hash drifted",
        )


def test_fixture_has_complete_serialized_table_coverage() -> None:
    module = _load_module()
    stored = json.loads(FIXTURE.read_text(encoding="utf-8"))
    rows = stored["exact_finite_count"]["rows"]
    _require(
        stored["exact_finite_count"]["serialized_n_values"]
        == list(module.SERIALIZED_NS),
        "serialized n-grid metadata drifted",
    )
    expected_pairs = [(q, n) for q in module.REPLAY_QS for n in module.SERIALIZED_NS]
    _require(
        len(rows) == module.MAX_SERIALIZED_ROWS == 45,
        "serialized density row count drifted",
    )
    _require(
        [(row["q"], row["n"]) for row in rows] == expected_pairs,
        "bounded q,n coverage drifted",
    )
    for row in rows:
        density = Fraction(*row["certified_density"])
        scaled = Fraction(*row["M_times_certified_density"])
        _require(
            density
            == Fraction(
                row["certified_zero_count"],
                row["primitive_squarefree_conductor_count"],
            ),
            "stored exact density drifted",
        )
        _require(
            scaled == row["conductor_degree_M"] * density,
            "stored scaled density drifted",
        )


def test_all_replayed_rows_match_independent_factor_sums_and_digest() -> None:
    module = _load_module()
    stored = json.loads(FIXTURE.read_text(encoding="utf-8"))
    digest_rows: list[list[int]] = []
    for q in module.REPLAY_QS:
        for n in range(module.MIN_N, module.MAX_N + 1):
            conductor_degree = 2 * n - 1
            first_allowed = n // 2 + 1
            independent = _independent_one_two_three_count(q, n)
            produced = module.support_forced_zero_count(q, n)
            _require(
                produced == independent,
                f"independent all-row count drifted at q={q}, n={n}",
            )
            total = q**conductor_degree - q ** (conductor_degree - 1)
            digest_rows.append(
                [q, n, conductor_degree, first_allowed, independent, total]
            )
    recorded = stored["exact_finite_count"]["all_replayed_rows_digest"]
    _require(
        recorded["row_count"] == len(digest_rows) == 237, "digest coverage drifted"
    )
    digest = _independent_digest(digest_rows)
    _require(recorded["sha256"] == digest, "all-row replay digest drifted")
    hostile_rows = [row.copy() for row in digest_rows]
    hostile_rows[10][4] += 1
    _require(
        _independent_digest(hostile_rows) != digest,
        "all-row digest failed to detect numerator corruption",
    )


def test_asymptotic_and_claim_firewalls_are_separate_from_finite_counts() -> None:
    stored = json.loads(FIXTURE.read_text(encoding="utf-8"))
    finite = stored["exact_finite_count"]
    asymptotic = stored["rigorous_fixed_q_asymptotic"]
    _require("[x^M]" in finite["coefficient_formula"], "coefficient formula missing")
    _require(
        "binom(I_q(d),m_d)" in finite["multiset_formula"], "multiset formula missing"
    )
    _require("not asserted" in finite["semantics"], "zero-subset firewall missing")
    _require("O_q(M^(-2))" in asymptotic["theorem"], "rigorous error missing")
    _require(
        "4*omega(4)" in asymptotic["buchstab_identification"], "Buchstab link missing"
    )
    correction = asymptotic["first_parity_correction"]
    _require("O_q(M^-3)" in correction["theorem"], "parity remainder missing")
    _require("-4*(1+log(2))" in correction["n_even"], "even correction drifted")
    _require("-(4/3)*(1+log(2))" in correction["n_odd"], "odd correction drifted")
    _require(
        asymptotic["conjectural_extrapolation"] is None,
        "conjectural extrapolation must be absent",
    )
    _require("not a fit" in asymptotic["finite_table_role"], "fit firewall missing")
    claims = " ".join(stored["claim_boundary"])
    for phrase in (
        "no converse",
        "connected-cumulant",
        "individual L-function",
        "not inferred",
        "affine-isomorphism",
        "RH",
        "GRH",
    ):
        _require(phrase in claims, f"claim firewall missing: {phrase}")


def test_exact_tail_rows_control_first_parity_correction() -> None:
    stored = json.loads(FIXTURE.read_text(encoding="utf-8"))
    rows = stored["exact_finite_count"]["rows"]
    c0_control = Fraction(224_583_296_562_735, 100_000_000_000_000)
    targets = {
        79: Fraction(-2_257_529_574, 1_000_000_000),
        80: Fraction(-6_772_588_722, 1_000_000_000),
    }
    for n, target in targets.items():
        conductor_degree = 2 * n - 1
        for q in (3, 5, 7):
            row = next(row for row in rows if row["q"] == q and row["n"] == n)
            exact_control = conductor_degree**2 * (
                Fraction(row["certified_zero_count"], q**conductor_degree)
                - c0_control / conductor_degree
            )
            _require(
                abs(exact_control - target) < Fraction(1, 8),
                f"first parity residual control drifted at q={q}, n={n}",
            )


def test_resource_contract_records_the_bounded_code_path() -> None:
    module = _load_module()
    stored = json.loads(FIXTURE.read_text(encoding="utf-8"))
    resources = stored["resource_contract"]
    _require(
        resources["replayed_rows"] == module.MAX_REPLAY_ROWS == 237,
        "resource replay-row ledger drifted",
    )
    _require(
        resources["serialized_rows"] == module.MAX_SERIALIZED_ROWS == 45,
        "resource serialized-row ledger drifted",
    )
    _require(
        resources["dp_transitions"] <= resources["maximum_total_dp_transitions"],
        "aggregate DP cap drifted",
    )
    _require(
        resources["maximum_row_dp_transitions_observed"]
        <= resources["maximum_row_dp_transitions"],
        "row DP cap drifted",
    )
    _require(
        resources["maximum_local_multiplicity_observed"] == 3,
        "factor multiplicity ledger drifted",
    )
    _require(FIXTURE.stat().st_size <= module.MAX_OUTPUT_BYTES, "output cap exceeded")
    _require(
        "recorded code-path ledger" in resources["enumeration_flag_semantics"],
        "enumeration-ledger scope drifted",
    )
    _require(
        "post-build acceptance ceiling" in resources["wall_clock_semantics"],
        "wall-clock acceptance semantics drifted",
    )
    for gate in (
        "finite_field_element_enumeration",
        "polynomial_enumeration",
        "irreducible_enumeration",
        "factorization",
        "curve_enumeration",
        "root_enumeration",
        "zero_enumeration",
        "sampling",
        "floating_point_arithmetic_in_exact_counts",
    ):
        _require(resources[gate] is False, f"resource gate drifted: {gate}")
