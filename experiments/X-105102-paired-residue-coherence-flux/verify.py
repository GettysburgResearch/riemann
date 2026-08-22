#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from fractions import Fraction as F
from pathlib import Path
from typing import Iterable

VERDICT = "PASS_T105102_PAIRED_RESIDUE_COHERENCE_FLUX"
REPO_ROOT = Path(__file__).resolve().parents[2]
BASE_PATH = (
    REPO_ROOT
    / "experiments"
    / "X-105101-entire-window-residue-flux"
    / "verify.py"
)
BASE_RESULT = BASE_PATH.parent / "results" / "verification.json"
BASE_DIGEST = "3e54ec6406ae1c37ceb43049ec433a29f7e2b269b293d84d9663b3480774a196"
BASE_COMMIT = "fd3ef43a6964e502f00ad906482eae5b3c544fba"

SPEC = importlib.util.spec_from_file_location("l105101_dependency", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load frozen L-105101 dependency")
BASE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = BASE
SPEC.loader.exec_module(BASE)

G = BASE.G
ZERO = BASE.ZERO
CONTENT_FILES = (
    "PACKET_METADATA_105102.json",
    "claims/lemmas/L-105102-paired-residue-coherence-window-flux.md",
    "claims/methodology/M-105102-paired-flux-review-contract.md",
    "claims/refutations/R-105102-nonreal-first-residue-correction-is-load-bearing.md",
    "claims/theorems/T-105102-boundary-coherence-frontier.md",
    "experiments/X-105102-paired-residue-coherence-flux/verify.py",
    "experiments/X-105102-paired-residue-coherence-flux/tests/test_verify.py",
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def dependency_checkpoint() -> dict[str, object]:
    artifact = json.loads(BASE_RESULT.read_text(encoding="utf-8"))
    live = BASE.build_payload()
    require(artifact == live, "L-105101 dependency artifact is stale")
    require(
        artifact["proof_object_sha256"] == BASE_DIGEST,
        "L-105101 dependency digest changed",
    )
    return {
        "commit": BASE_COMMIT,
        "proof_object_sha256": BASE_DIGEST,
        "artifact_matches_live_producer": True,
    }


def first_root_variance_ledger(coefficients: list[F]) -> F:
    degree = len(coefficients) - 1
    if degree < 2:
        raise ValueError("first root ledger requires degree at least two")
    sums = BASE.root_power_sums(coefficients)
    mean = sums[1] / degree
    v2 = sums[2] - 2 * mean * sums[1] + degree * mean**2
    return -v2 / degree**2


def first_residue_ladder(
    coefficients: list[F],
    critical_roots: Iterable[G],
) -> list[tuple[G, G]]:
    roots = list(critical_roots)
    degree = len(coefficients) - 1
    if len(roots) != degree - 1:
        raise ValueError("critical-root fixture does not have complete coverage")
    if len(set(roots)) != len(roots):
        raise ValueError("critical-root fixture is not simple")
    first = BASE.derivative(coefficients)
    second = BASE.derivative(first)
    rows: list[tuple[G, G]] = []
    for root in roots:
        require(
            BASE.evaluate(first, root) == ZERO,
            f"{root.render()} is not a zero of p'",
        )
        require(
            BASE.evaluate(second, root) != ZERO,
            f"{root.render()} is not a simple zero of p'",
        )
        rho = BASE.evaluate(coefficients, root) / BASE.evaluate(second, root)
        rows.append((root, rho))
    return rows


def first_local_ledger(
    name: str,
    coefficients: list[F],
    critical_roots: list[G],
    t: F,
    eta: F,
) -> dict[str, object]:
    if t <= 0 or eta <= 0:
        raise ValueError("rectangle dimensions must be positive")
    critical = first_residue_ladder(coefficients, critical_roots)
    if any(BASE.on_rectangle_boundary(root, t, eta) for root, _ in critical):
        raise ValueError("an F' zero lies on the rectangle boundary")
    inside = [
        (root, rho)
        for root, rho in critical
        if BASE.inside_rectangle(root, t, eta)
    ]
    real_sum = F(0)
    nonreal_correction = ZERO
    real_count = 0
    for root, rho in inside:
        if root.im == 0:
            require(rho.im == 0, "real critical point has nonreal residue")
            real_sum += rho.re
            real_count += 1
        else:
            nonreal_correction += rho
    first_moment = -real_sum
    boundary_charge = BASE.gsum(rho for _, rho in inside)
    global_charge = BASE.gsum(rho for _, rho in critical)
    exterior_charge = BASE.gsum(
        rho
        for root, rho in critical
        if not BASE.inside_rectangle(root, t, eta)
    )
    root_ledger = G(first_root_variance_ledger(coefficients))

    require(
        G(first_moment) == -boundary_charge + nonreal_correction,
        f"first-moment split failed for {name}",
    )
    require(
        global_charge == boundary_charge + exterior_charge,
        f"first global/exterior split failed for {name}",
    )
    require(
        global_charge == root_ledger,
        f"first V2 root ledger failed for {name}",
    )
    require(boundary_charge.im == 0, f"first boundary charge is nonreal for {name}")
    require(
        nonreal_correction.im == 0,
        f"first nonreal correction is nonreal for {name}",
    )
    return {
        "name": name,
        "T": str(t),
        "eta": str(eta),
        "inside_critical_roots": [root.render() for root, _ in inside],
        "real_critical_count": real_count,
        "first_moment": str(first_moment),
        "nonreal_first_correction": nonreal_correction.render(),
        "boundary_first_charge": boundary_charge.render(),
        "exterior_first_charge": exterior_charge.render(),
        "global_first_charge": global_charge.render(),
        "root_v2_ledger": root_ledger.render(),
        "first_split_verified": True,
        "first_global_exterior_split_verified": True,
        "independent_v2_ledger_verified": True,
    }


def paired_local_ledger(
    name: str,
    coefficients: list[F],
    critical_roots: list[G],
    second_critical_roots: list[G],
    t: F,
    eta: F,
) -> dict[str, object]:
    first = first_local_ledger(name, coefficients, critical_roots, t, eta)
    second = BASE.local_ledger(
        name,
        coefficients,
        critical_roots,
        second_critical_roots,
        t,
        eta,
    )
    count = int(first["real_critical_count"])
    m1 = F(str(first["first_moment"]))
    m2 = F(str(second["real_m2"]))
    phi1 = F(str(first["boundary_first_charge"]))
    c1 = F(str(first["nonreal_first_correction"]))
    b2 = F(str(second["boundary_residue_sum"]))
    c2 = F(str(second["nonreal_correction"]))
    d2 = F(str(second["adjacent_derivative_debt"]))
    reconstructed_m1 = -phi1 + c1
    reconstructed_m2 = b2 - c2 - d2
    require(reconstructed_m1 == m1, f"paired first reconstruction failed for {name}")
    require(reconstructed_m2 == m2, f"paired second reconstruction failed for {name}")
    endpoint_nonvanishing = (
        BASE.evaluate(coefficients, G(-t)) != ZERO
        and BASE.evaluate(coefficients, G(t)) != ZERO
    )
    critical = first_residue_ladder(coefficients, critical_roots)
    common_zero_free = all(
        BASE.evaluate(coefficients, root) != ZERO
        for root, _ in critical
        if root.im == 0 and BASE.inside_rectangle(root, t, eta)
    )
    transfer_hypotheses = endpoint_nonvanishing and common_zero_free
    coherence: F | None = None
    reconstructed_coherence: F | None = None
    formal_excess: F | None = None
    certified_transfer_constant: F | None = None
    if count * m2 > 0:
        carrier = max(m1, F(0))
        coherence = carrier**2 / (count * m2)
        reconstructed_carrier = max(reconstructed_m1, F(0))
        reconstructed_coherence = (
            reconstructed_carrier**2 / (count * reconstructed_m2)
        )
        require(
            reconstructed_coherence == coherence,
            f"displayed boundary quotient failed for {name}",
        )
        require(0 <= coherence <= 1, f"coherence range failed for {name}")
        if coherence > F(1, 2):
            formal_excess = 2 * coherence - 1
            if transfer_hypotheses:
                certified_transfer_constant = formal_excess
    return {
        "name": name,
        "first": first,
        "second": second,
        "coherence": None if coherence is None else str(coherence),
        "formal_coherence_excess": (
            None if formal_excess is None else str(formal_excess)
        ),
        "certified_transfer_constant": (
            None
            if certified_transfer_constant is None
            else str(certified_transfer_constant)
        ),
        "l104522_endpoint_nonvanishing": endpoint_nonvanishing,
        "l104522_common_zero_free": common_zero_free,
        "l104522_transfer_hypotheses_verified": transfer_hypotheses,
        "boundary_reconstructed_coherence": (
            None
            if reconstructed_coherence is None
            else str(reconstructed_coherence)
        ),
        "displayed_quotient_verified": True,
        "paired_identity_verified": True,
    }


def integrated_paired_edge_check() -> dict[str, object]:
    # On the unit square for p=z^2+1:
    # P=(z+1/z)/2 and Q=(z^3+2z+1/z)/4.
    # Represent each normalized edge contribution as a/pi+b.
    first_horizontal = (F(-1), F(1, 4))
    first_vertical = (F(1), F(1, 4))
    first_combined = (
        first_horizontal[0] + first_vertical[0],
        first_horizontal[1] + first_vertical[1],
    )
    second = BASE.integrated_edge_formula_check()
    first_residue = first_root_variance_ledger([F(1), F(0), F(1)])
    require(
        first_combined == (F(0), first_residue),
        "integrated first-edge formula failed",
    )
    horizontal_mutation = (
        -first_horizontal[0] + first_vertical[0],
        -first_horizontal[1] + first_vertical[1],
    )
    vertical_mutation = (
        first_horizontal[0] - first_vertical[0],
        first_horizontal[1] - first_vertical[1],
    )
    require(horizontal_mutation != first_combined, "first horizontal mutation survived")
    require(vertical_mutation != first_combined, "first vertical mutation survived")
    require(second["residue"] == "1/4", "frozen second-edge oracle changed")
    return {
        "fixture": "p(z)=z^2+1, T=eta=1",
        "first_top_imaginary_integral": "1-pi/4",
        "first_right_integral": "1+pi/4",
        "first_combined_a_over_pi_plus_b": [
            str(value) for value in first_combined
        ],
        "first_residue": str(first_residue),
        "second_residue": second["residue"],
        "both_first_sign_mutations_rejected": True,
        "frozen_second_sign_oracle_reused": True,
    }


def first_schwarz_parity_checks() -> dict[str, object]:
    z = G(F(2), F(1, 3))
    fixtures = {
        "even": [F(1), F(0), F(1)],
        "odd": [F(0), F(3), F(0), F(1)],
    }
    rows: dict[str, object] = {}
    for name, coefficients in fixtures.items():
        first = BASE.derivative(coefficients)
        value = BASE.evaluate(coefficients, z) / BASE.evaluate(first, z)
        conjugate_value = (
            BASE.evaluate(coefficients, z.conjugate())
            / BASE.evaluate(first, z.conjugate())
        )
        negative_value = (
            BASE.evaluate(coefficients, -z) / BASE.evaluate(first, -z)
        )
        require(
            conjugate_value == value.conjugate(),
            f"first Schwarz reflection failed for {name}",
        )
        require(negative_value == -value, f"first odd parity failed for {name}")
        rows[name] = {
            "P(z)": value.render(),
            "schwarz": True,
            "P_is_odd": True,
        }
    generic = [F(1), F(-3), F(0), F(1)]
    first = BASE.derivative(generic)
    value = BASE.evaluate(generic, z) / BASE.evaluate(first, z)
    conjugate_value = (
        BASE.evaluate(generic, z.conjugate())
        / BASE.evaluate(first, z.conjugate())
    )
    negative_value = BASE.evaluate(generic, -z) / BASE.evaluate(first, -z)
    require(conjugate_value == value.conjugate(), "generic first Schwarz failed")
    require(negative_value != -value, "generic first ratio accidentally odd")
    rows["generic_real"] = {
        "P(z)": value.render(),
        "schwarz": True,
        "P_is_odd": False,
    }
    return rows


def nonreal_carrier_firewall() -> dict[str, object]:
    coefficients = [F(0), F(1), F(0), F(-1), F(0), F(1)]
    first = BASE.derivative(coefficients)
    q0, q1, q2 = first[0], first[2], first[4]
    vertex = -q1 / (2 * q2)
    minimum = q2 * vertex**2 + q1 * vertex + q0
    critical_y_discriminant = q1**2 - 4 * q2 * q0
    parent_y = [coefficients[1], coefficients[3], coefficients[5]]
    scale = q2 / parent_y[2]
    difference_linear = q1 - scale * parent_y[1]
    difference_constant = q0 - scale * parent_y[0]
    common_root_candidate = -difference_constant / difference_linear
    common_root_residual = (
        parent_y[2] * common_root_candidate**2
        + parent_y[1] * common_root_candidate
        + parent_y[0]
    )
    charge = first_root_variance_ledger(coefficients)
    require(minimum > 0, "quintic derivative positivity failed")
    require(critical_y_discriminant != 0, "quintic critical roots are not simple")
    require(common_root_residual != 0, "quintic has a common p/p' root")
    require(charge == F(-2, 25), "quintic first charge changed")
    correction = charge
    corrected_m1 = -charge + correction
    naive_m1 = -charge
    require(corrected_m1 == 0, "nonreal carrier cancellation failed")
    require(naive_m1 > 0, "dropped-correction mutation did not create carrier")
    return {
        "polynomial": "x^5-x^3+x",
        "derivative_square_completion": "5(y-3/10)^2+11/20",
        "derived_vertex": str(vertex),
        "derivative_minimum": str(minimum),
        "critical_y_discriminant": str(critical_y_discriminant),
        "common_root_candidate_residual": str(common_root_residual),
        "critical_roots_simple_and_not_parent_roots": True,
        "firewall_constants_derived_from_coefficients": True,
        "real_critical_count": 0,
        "global_first_charge": str(charge),
        "nonreal_first_correction": str(correction),
        "corrected_first_moment": str(corrected_m1),
        "dropped_correction_false_carrier": str(naive_m1),
        "firewall_verified": True,
    }


def coherence_threshold_firewall() -> dict[str, object]:
    coefficients = [F(2), F(0), F(-2), F(0), F(1)]
    critical = first_residue_ladder(
        coefficients,
        [G(F(-1)), ZERO, G(F(1))],
    )
    residues = [rho.re for _, rho in critical]
    m1 = -sum(residues, F(0))
    m2 = sum((rho * rho for rho in residues), F(0))
    coherence = max(m1, F(0)) ** 2 / (F(3) * m2)
    require(residues == [F(1, 8), F(-1, 2), F(1, 8)], "quartic residues changed")
    require(m1 == F(1, 4), "quartic first moment changed")
    require(m2 == F(9, 32), "quartic second moment changed")
    require(coherence == F(2, 27), "quartic coherence changed")
    require(coherence < F(1, 2), "quartic firewall crossed threshold")
    return {
        "polynomial": "x^4-2x^2+2",
        "residues": [str(value) for value in residues],
        "first_moment": str(m1),
        "second_moment": str(m2),
        "real_critical_count": 3,
        "coherence": str(coherence),
        "positive_transfer_available": False,
    }


def content_hashes() -> dict[str, str]:
    hashes: dict[str, str] = {}
    for relative_path in CONTENT_FILES:
        path = REPO_ROOT / relative_path
        if not path.is_file():
            raise FileNotFoundError(f"missing load-bearing file: {relative_path}")
        normalized = path.read_bytes().replace(b"\r\n", b"\n")
        hashes[relative_path] = hashlib.sha256(normalized).hexdigest()
    return hashes


def build_payload() -> dict[str, object]:
    real_cubic = [F(1), F(-3), F(0), F(1)]
    asymmetric_quartic = [F(1), F(64), F(-32), F(-4, 3), F(1)]
    complex_cubic = [F(1), F(3), F(0), F(1)]
    common_removable = [F(1), F(-2), F(1)]
    fixtures = [
        paired_local_ledger(
            "real_cubic_narrow_window",
            real_cubic,
            [G(F(-1)), G(F(1))],
            [ZERO],
            F(1, 2),
            F(1),
        ),
        paired_local_ledger(
            "real_cubic_full_window",
            real_cubic,
            [G(F(-1)), G(F(1))],
            [ZERO],
            F(3, 2),
            F(1),
        ),
        paired_local_ledger(
            "asymmetric_quartic_partial_window",
            asymmetric_quartic,
            [G(F(-4)), G(F(1)), G(F(4))],
            [G(F(-2)), G(F(8, 3))],
            F(3),
            F(1),
        ),
        paired_local_ledger(
            "complex_cubic_narrow_strip",
            complex_cubic,
            [G(F(0), F(-1)), G(F(0), F(1))],
            [ZERO],
            F(1),
            F(1, 2),
        ),
        paired_local_ledger(
            "complex_cubic_wide_strip",
            complex_cubic,
            [G(F(0), F(-1)), G(F(0), F(1))],
            [ZERO],
            F(1),
            F(2),
        ),
        paired_local_ledger(
            "negative_carrier_positive_part_firewall",
            [F(1), F(0), F(1)],
            [ZERO],
            [],
            F(1),
            F(1),
        ),
        paired_local_ledger(
            "endpoint_nonvanishing_firewall",
            [F(-1), F(0), F(1)],
            [ZERO],
            [],
            F(1),
            F(1),
        ),
        paired_local_ledger(
            "common_zero_transfer_firewall",
            [F(-95, 3), F(64), F(-32), F(-4, 3), F(1)],
            [G(F(-4)), G(F(1)), G(F(4))],
            [G(F(-2)), G(F(8, 3))],
            F(5),
            F(1),
        ),
        paired_local_ledger(
            "common_p_pprime_removable",
            common_removable,
            [G(F(1))],
            [],
            F(2),
            F(1),
        ),
    ]
    payload: dict[str, object] = {
        "schema": "riemann.t105102.paired-residue-coherence-flux.v1",
        "classification": VERDICT,
        "arithmetic_class": "EXACT_RATIONAL_AND_GAUSSIAN_RATIONAL",
        "source": {
            "checkpoint_base": BASE_COMMIT,
            "post_freeze_context_pr": 720,
            "post_freeze_context_head": (
                "10bba584c01277e880aaa21e1fea09f396ca7246"
            ),
        },
        "dependency_checkpoint": dependency_checkpoint(),
        "checks": {
            "paired_local_ledgers": fixtures,
            "integrated_paired_edge_formula": integrated_paired_edge_check(),
            "first_schwarz_and_parity": first_schwarz_parity_checks(),
            "nonreal_carrier_firewall": nonreal_carrier_firewall(),
            "coherence_threshold_firewall": coherence_threshold_firewall(),
        },
        "content_sha256": content_hashes(),
        "content_hash_mode": "LF_NORMALIZED_TEXT",
        "scope": {
            "fixed_window_first_identity_proof_supplied": True,
            "paired_coherence_identity_proof_supplied": True,
            "pointwise_thin_strip_corrections_eliminated": True,
            "multiple_zero_confluent_ledger_proved": False,
            "xi_window_hypotheses_proved": False,
            "admissible_height_strip_sequence_controlled": False,
            "first_boundary_charge_estimated": False,
            "nonreal_first_correction_estimated": False,
            "second_boundary_and_corrections_estimated": False,
            "strict_coherence_margin_proved": False,
            "rcmv104530_proved": False,
            "rh_established": False,
        },
        "heavy_computation_run": False,
        "verdict": VERDICT,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    print(payload["verdict"])
    print(payload["proof_object_sha256"])


if __name__ == "__main__":
    main()
