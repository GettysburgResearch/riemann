from __future__ import annotations

import hashlib
import importlib.util
import json
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "quadratic_family_closed_place_weight_notch.py"
)
FIXTURE = SCRIPT.with_suffix(".json")


def _load_module():
    spec = importlib.util.spec_from_file_location("closed_place_weight_notch", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load closed-place weight-notch producer")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def test_source_lock_and_rational_profile_recovery() -> None:
    module = _load_module()
    source = module.load_locked_source()
    _require(
        source["payload_sha256"] == module.SOURCE_PAYLOAD_SHA256,
        "source payload lock drifted",
    )
    _require(
        module._git_blob(module.SOURCE, module.SOURCE_COMMIT) == module.SOURCE_BLOB,
        "source git-blob lock drifted",
    )
    for factor_count in range(1, 11):
        profile = (1,) * factor_count
        expected = tuple(comb(factor_count + k - 1, k) for k in range(7))
        _require(
            module.profile_coefficients(profile, 6) == expected,
            f"rational denominator drifted at r={factor_count}",
        )


def test_mixed_profile_coefficients_and_kernel() -> None:
    module = _load_module()
    _require(
        module.profile_coefficients((1, 2), 6) == (1, 1, 2, 2, 3, 3, 4),
        "profile (1,2) coefficients drifted",
    )
    _require(
        module.profile_coefficients((2, 3), 6) == (1, 0, 1, 1, 1, 1, 2),
        "profile (2,3) coefficients drifted",
    )
    _require(
        module.profile_kernel_coefficients((2, 3), 4)
        == (
            {0: 1},
            {1: -1},
            {0: 1},
            {0: 1, 1: -1},
            {0: 1, 1: -1},
        ),
        "mixed-profile kernel drifted",
    )


def test_reciprocity_adapter_sign_is_exact_in_both_q_mod_4_classes() -> None:
    module = _load_module()
    checks = 0
    for q in (3, 5, 7, 9):
        for conductor_degree in range(1, 11):
            for prime_degree in range(1, 6):
                _require(
                    module.reciprocity_adapter_signs_agree(
                        q, conductor_degree, prime_degree
                    ),
                    f"reciprocity sign drifted at q={q}, M={conductor_degree}, d={prime_degree}",
                )
                checks += 1
    _require(checks == 200, "reciprocity parity-check count drifted")


def test_original_and_regrouped_coefficients_agree_on_bounded_profiles() -> None:
    module = _load_module()
    profiles = module._all_replay_profiles()
    _require(len(profiles) == 138, "bounded profile count drifted")
    for n in range(2, 8):
        for profile in profiles:
            _require(
                module.original_p_coefficient_expansion(n, profile)
                == module.regrouped_p_coefficient_expansion(n, profile),
                f"closed-place regrouping drifted at n={n}, profile={profile}",
            )


def test_n5_rational_mixed_and_irreducible_signs() -> None:
    module = _load_module()
    expected = {
        (1,) * 9: {(3, 3): -9, (1, 1): -45},
        (9,): {},
        (2, 7): {(1, 1): -1},
        (1,) * 10: {
            (4, 4): -1,
            (3, 3): -10,
            (2, 2): -10,
            (1, 1): -55,
            (0, 0): -55,
        },
        (10,): {(4, 4): -1},
        (2, 8): {(4, 4): -1, (1, 1): -1, (0, 0): -1},
    }
    for profile, character_row in expected.items():
        _require(
            module.weighted_character_expansion(5, profile) == character_row,
            f"n=5 character row drifted for profile={profile}",
        )


def test_difference_channel_survives_just_beyond_numerator_degree() -> None:
    module = _load_module()
    _require(
        module.delta_character_expression(2, 0) == {0: -1},
        "D_2 must retain -q*p_0 when the genus-zero numerator has no p_2",
    )
    _require(
        module.weighted_character_expansion(2, (1,)) == {(2, 0): -1, (0, 0): 1},
        "degree-one conductor control must give 1-q",
    )


def test_odd_notch_exact_zero_support_condition() -> None:
    module = _load_module()
    for n in range(2, 6):
        for profile in module._integer_partitions(2 * n - 1):
            condition = min(profile) > n // 2
            _require(
                module.odd_notch_zero_condition(n, profile) == condition,
                f"odd-notch support predicate drifted at n={n}, profile={profile}",
            )
            if condition:
                _require(
                    module.weighted_character_expansion(n, profile) == {},
                    f"odd-notch exact zero failed at n={n}, profile={profile}",
                )
        irreducible_profile = (2 * n - 1,)
        _require(
            module.weighted_character_expansion(n, irreducible_profile) == {},
            f"irreducible odd-notch zero failed at n={n}",
        )


def test_even_notch_half_weight_channel_is_profile_independent() -> None:
    module = _load_module()
    for n in range(2, 6):
        for profile in module._integer_partitions(2 * n):
            expansion = module.weighted_character_expansion(n, profile)
            _require(
                expansion.get((n - 1, n - 1)) == (-1) ** n,
                f"even-notch leader drifted at n={n}, profile={profile}",
            )
            _require(
                all(exponent <= n - 1 for exponent, _ in expansion),
                f"higher channel survived at n={n}, profile={profile}",
            )


def test_primitive_metadata_accepts_distinct_factors_and_refuses_imprimitive_data() -> (
    None
):
    module = _load_module()
    _require(
        module.primitive_squarefree_profile((("P1", 3, 1), ("P2", 1, 1), ("P3", 3, 1)))
        == (1, 3, 3),
        "primitive factor metadata normalization drifted",
    )
    refusals = (
        ((("P", 3, 2),), "imprimitive"),
        ((("P", 3, 1), ("P", 5, 1)), "distinct"),
        ((("P", 0, 1),), "positive"),
    )
    for records, fragment in refusals:
        try:
            module.primitive_squarefree_profile(records)
        except ValueError as error:
            _require(fragment in str(error), f"wrong metadata refusal for {fragment}")
        else:
            raise AssertionError(f"metadata should be refused: {records}")


def test_fixed_q_feasibility_uses_irreducible_counts_without_enumeration() -> None:
    module = _load_module()
    _require(module.irreducible_count(3, 1) == 3, "I_3(1) drifted")
    _require(module.irreducible_count(3, 2) == 3, "I_3(2) drifted")
    _require(module.irreducible_count(3, 3) == 8, "I_3(3) drifted")
    _require(module.irreducible_count(5, 2) == 10, "I_5(2) drifted")
    _require(
        module.profile_feasibility(3, (1, 1, 1))["feasible"] is True,
        "three rational places should be feasible",
    )
    _require(
        module.profile_feasibility(3, (1, 1, 1, 1))["feasible"] is False,
        "four rational places should be infeasible",
    )
    _require(
        module.profile_feasibility(3, (2, 2, 2))["feasible"] is True,
        "three quadratic places should be feasible",
    )
    _require(
        module.profile_feasibility(3, (2, 2, 2, 2))["feasible"] is False,
        "four quadratic places should be infeasible",
    )


def test_symbolic_profiles_fail_closed_outside_declared_caps() -> None:
    module = _load_module()
    refusals = (
        (lambda: module.normalize_profile(()), "positive factor degrees"),
        (lambda: module.normalize_profile((21,)), "degree cap"),
        (lambda: module.profile_coefficients((1,), 9), "series cap"),
        (lambda: module.original_p_coefficient_expansion(11, (1,)), "2<=n<=10"),
        (lambda: module._integer_partitions(11), "total-degree cap"),
        (lambda: module.odd_notch_zero_condition(5, (8,)), "2*n-1"),
    )
    for call, fragment in refusals:
        try:
            call()
        except ValueError as error:
            _require(fragment in str(error), f"wrong cap refusal for {fragment}")
        else:
            raise AssertionError(f"symbolic replay should refuse outside {fragment}")


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
            digest == stored["packet_files_lf_sha256"][label], f"{label} hash drifted"
        )


def test_scope_resource_and_claim_firewalls() -> None:
    stored = json.loads(FIXTURE.read_text(encoding="utf-8"))
    _require("primitive squarefree" in stored["scope"], "primitive scope missing")
    adapter = stored["closed_place_character"]
    _require(
        "G=(-1)^M*Q" in adapter["curve_adapter"], "reciprocity sign adapter missing"
    )
    _require("split infinity" in adapter["infinity"], "infinity adapter missing")
    notch = stored["primitive_conductor_weight_notch"]
    difference = stored["exact_regrouped_identity"]["difference_channel"]
    _require(
        "p_j=0 outside" in difference
        and "retain D_r=p_r-q*p_(r-2)" in difference
        and "set D_r=0 by convention for r<0" in difference,
        "difference-channel support convention drifted",
    )
    _require(
        "S_(n,Q)=0 exactly" in notch["odd_M_2n_minus_1"]["exact_zero"],
        "odd exact-zero theorem missing",
    )
    _require(
        "profile-independent" in notch["even_M_2n"]["profile_independent_leader"],
        "even universal leader missing",
    )
    connected = stored["normalization_and_connected_correction"]
    _require(
        "need not vanish" in connected["proper_partition_bound"],
        "singleton warning missing",
    )
    _require(
        "does not force" in connected["odd_zero_firewall"],
        "raw/connected firewall missing",
    )
    primitive = stored["primitive_and_feasibility_firewalls"]
    _require(
        "primitive squarefree conductor" in primitive["primitive_only"],
        "imprimitive firewall missing",
    )
    _require(
        "no automatic reduction" in primitive["primitive_only"],
        "imprimitive Euler-deletion firewall missing",
    )
    _require("I_q(d)" in primitive["fixed_q_feasibility"], "fixed-q count missing")
    claims = " ".join(stored["claim_boundary"])
    for phrase in (
        "fixed-(n,profile)",
        "growing-rank",
        "motive",
        "external novelty",
        "RH",
        "GRH",
    ):
        _require(phrase in claims, f"claim firewall missing: {phrase}")
    resources = stored["resource_contract"]
    _require(resources["profiles_replayed"] == 138, "profile replay count drifted")
    _require(
        resources["coefficient_pairs_replayed"] == 828,
        "coefficient replay count drifted",
    )
    _require(
        resources["reciprocity_parity_checks"] == 200,
        "reciprocity replay count drifted",
    )
    _require(resources["source_git_commands"] == 2, "source-command ledger drifted")
    for gate in (
        "finite_field_enumeration",
        "irreducible_enumeration",
        "polynomial_family_enumeration",
        "curve_enumeration",
        "root_enumeration",
        "zero_enumeration",
        "sampling",
        "floating_point_arithmetic",
    ):
        _require(resources[gate] is False, f"resource gate drifted: {gate}")
