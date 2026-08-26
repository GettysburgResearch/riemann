from __future__ import annotations

import hashlib
import importlib.util
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "quadratic_family_fixed_degree_weight_notch.py"
)
FIXTURE = SCRIPT.with_suffix(".json")


def _load_module():
    spec = importlib.util.spec_from_file_location("fixed_degree_weight_notch", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load fixed-degree weight-notch producer")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def test_source_lock_and_kernel_regrouping() -> None:
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
    for m in range(1, 15):
        _require(module.kernel_coefficient(m, 0) == {0: 1}, f"B_0 drifted at m={m}")
        for k in range(1, 5):
            _require(
                module.kernel_coefficient(m, k)
                == {
                    0: module.comb(m + k - 1, k),
                    1: -module.comb(m + k - 2, k - 1),
                },
                f"kernel coefficient drifted at m={m}, k={k}",
            )
    for n in range(2, 10):
        for m in range(1, 15):
            _require(
                module.original_p_coefficient_expansion(n, m)
                == module.regrouped_p_coefficient_expansion(n, m),
                f"exact regrouping drifted at n={n}, m={m}",
            )


def test_low_degree_regrouped_d_expansions_and_parity() -> None:
    module = _load_module()
    _require(
        module.d_coefficient_expansion(2, 1) == {2: 1, 0: 1},
        "n=2,m=1 expansion drifted",
    )
    _require(
        module.d_coefficient_expansion(2, 2) == {2: 1, 1: -1, 0: 2},
        "n=2,m=2 split-infinity expansion drifted",
    )
    _require(
        module.d_coefficient_expansion(5, 9) == {5: 1, 3: 9, 1: 45},
        "n=5,m=9 expansion drifted",
    )
    _require(
        module.d_coefficient_expansion(5, 10)
        == {5: 1, 4: -1, 3: 10, 2: -10, 1: 55, 0: -55},
        "n=5,m=10 split-infinity expansion drifted",
    )


def test_usp_top_channel_classification_including_omega_zero() -> None:
    module = _load_module()
    for n in range(2, 9):
        for genus in range(n + 2):
            actual = module.delta_character_expression(n, genus)
            expected = module.expected_top_delta(n, genus)
            _require(
                actual == expected, f"USp classification drifted at n={n}, g={genus}"
            )
            if 2 * genus < n - 2:
                _require(
                    actual == {}, f"below-range channel survived at n={n}, g={genus}"
                )
            elif genus <= n - 2:
                index = 2 * genus - n + 2
                _require(
                    actual == {index: -1},
                    f"pre-notch sign/index drifted at n={n}, g={genus}",
                )
            elif genus == n - 1:
                _require(actual == {}, f"notch failed at n={n}")
            else:
                _require(
                    actual == {n: 1}, f"post-notch channel drifted at n={n}, g={genus}"
                )
    _require(
        module.delta_character_expression(2, 0) == {0: -1},
        "chi_omega0 boundary drifted",
    )


def test_top_channel_signs_and_notch_leading_rows() -> None:
    module = _load_module()
    for n in range(2, 9):
        odd = module.notch_leading_row(n, False)
        even = module.notch_leading_row(n, True)
        _require(odd["marked_places"] == 2 * n - 1, f"odd notch count drifted at n={n}")
        _require(
            odd["coefficient"] == (2 * n - 1) * (-1) ** n,
            f"odd notch sign drifted at n={n}",
        )
        _require(
            odd["fundamental_character_index"] == n - 2,
            f"odd residual character drifted at n={n}",
        )
        _require(even["marked_places"] == 2 * n, f"even notch count drifted at n={n}")
        _require(even["coefficient"] == (-1) ** n, f"even notch sign drifted at n={n}")
        _require(
            even["fundamental_character_index"] == n - 1,
            f"even residual character drifted at n={n}",
        )


def test_complete_notch_character_expansions() -> None:
    module = _load_module()
    for n in range(2, 9):
        sign = (-1) ** n
        odd_m = 2 * n - 1
        expected_odd = {
            (n - 2 * k, n - 2 * k): sign * module.comb(2 * n + k - 2, k)
            for k in range(1, n // 2 + 1)
        }
        _require(
            module.weighted_character_expansion(n, odd_m, n - 1) == expected_odd,
            f"complete odd-notch expansion drifted at n={n}",
        )

        even_m = 2 * n
        expected_even = {(n - 1, n - 1): sign}
        for k in range(1, n // 2 + 1):
            index = n - 2 * k
            expected_even[(index, index)] = sign * module.comb(2 * n + k - 1, k)
        for k in range(1, (n - 1) // 2 + 1):
            index = n - 2 * k - 1
            expected_even[(index, index)] = sign * module.comb(2 * n + k - 1, k)
        _require(
            module.weighted_character_expansion(n, even_m, n - 1) == expected_even,
            f"complete even-notch expansion drifted at n={n}",
        )


def test_exact_n2_and_n5_character_replays() -> None:
    module = _load_module()
    _require(
        module.weighted_character_expansion(2, 3, 1) == {(0, 0): 3},
        "n=2 odd-notch character row drifted",
    )
    _require(
        module.weighted_character_expansion(2, 4, 1) == {(1, 1): 1, (0, 0): 4},
        "n=2 even-notch character row drifted",
    )
    _require(
        module.weighted_character_expansion(5, 9, 4) == {(3, 3): -9, (1, 1): -45},
        "n=5 odd-notch character row drifted",
    )
    _require(
        module.weighted_character_expansion(5, 10, 4)
        == {
            (4, 4): -1,
            (3, 3): -10,
            (2, 2): -10,
            (1, 1): -55,
            (0, 0): -55,
        },
        "n=5 even-notch character row drifted",
    )


def test_one_place_mean_has_family_degree_parity() -> None:
    module = _load_module()
    for q in (3, 5, 9):
        for n in range(2, 10):
            expected = Fraction(0) if n % 2 else Fraction(-1, q ** (n - 1))
            _require(
                module.one_place_mean(n, q) == expected,
                f"one-place mean drifted at n={n}, q={q}",
            )


def test_n2_third_connected_caveat_is_exact() -> None:
    module = _load_module()
    _require(len(module._set_partitions((0, 1, 2))) == 5, "Bell(3) drifted")
    for q in (3, 5, 7, 9):
        family_size = q * (q - 1)
        moments = {
            1: Fraction(-1, q),
            2: Fraction(2 - q, family_size),
            3: Fraction(3, family_size),
        }
        direct = module.cumulant_from_block_size_moments(3, moments)
        closed = Fraction(2 * (2 * q + 1), q**3 * (q - 1))
        _require(direct == closed, f"n=2 third cumulant drifted at q={q}")
        _require(module.n2_third_cumulant(q) == closed, f"n=2 wrapper drifted at q={q}")
        _require(
            Fraction(3, family_size) != closed,
            f"raw and connected rows collapsed at q={q}",
        )


def test_symbolic_replay_fails_closed_outside_caps() -> None:
    module = _load_module()
    refusals = (
        (lambda: module.original_p_coefficient_expansion(1, 1), "n>=2"),
        (lambda: module.expected_top_delta(1, 0), "n>=2"),
        (lambda: module._set_partitions((0, 1, 2, 3)), "order three"),
        (lambda: module.n2_third_cumulant(2), "odd q>=3"),
    )
    for call, fragment in refusals:
        try:
            call()
        except ValueError as error:
            _require(
                fragment in str(error), f"wrong fail-closed message for {fragment}"
            )
        else:
            raise AssertionError(f"replay should refuse outside {fragment}")


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
    _require("fixed (n,m)" in stored["scope"], "fixed-parameter scope missing")
    conventions = stored["notation"]["coefficient_conventions"]
    _require("outside 0<=j<=2*g" in conventions, "out-of-range convention missing")
    _require("chi_(omega_0)=1" in conventions, "omega-zero convention missing")
    warning = stored["notch_leading_residual_channels"]["warning"]
    _require("not complete equalities" in warning, "leading-residual warning missing")
    caveat = stored["connected_correction"]["n_2_caveat"]
    _require("cancel" in caveat["warning"], "n=2 cancellation caveat missing")
    _require("O(q^-3)" in caveat["connected_formula"], "n=2 connected scale missing")
    twist = stored["twist_infinity_and_weight_conventions"]
    _require("quadratic twist" in twist["odd_m_twist"], "odd-m twist firewall missing")
    _require("split infinity" in twist["even_m_infinity"], "infinity firewall missing")
    boundary = " ".join(stored["claim_boundary"])
    for phrase in (
        "fixed (n,m)",
        "upper envelope",
        "motive",
        "external novelty",
        "RH",
        "GRH",
    ):
        _require(phrase in boundary, f"claim firewall missing: {phrase}")
    resources = stored["resource_contract"]
    _require(resources["distinct_source_files_read"] == 1, "source-file ledger drifted")
    _require(resources["source_content_reads"] == 1, "source-content ledger drifted")
    _require(resources["source_git_commands"] == 2, "source-command ledger drifted")
    _require(resources["coefficient_pairs_replayed"] == 112, "replay count drifted")
    _require(resources["set_partitions_visited"] == 5, "partition count drifted")
    for gate in (
        "finite_field_enumeration",
        "extension_field_enumeration",
        "polynomial_family_enumeration",
        "curve_enumeration",
        "root_enumeration",
        "zero_enumeration",
        "sampling",
        "floating_point_arithmetic",
    ):
        _require(resources[gate] is False, f"resource gate drifted: {gate}")
