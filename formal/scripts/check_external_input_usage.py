#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FORMAL = ROOT / "formal"
XI = FORMAL / "RiemannFormal" / "Operator" / "XiOrderThree.lean"
SHARED = FORMAL / "comparator" / "ChallengeDeps" / "XiPickOrderThreeConditional.lean"
SOURCE = FORMAL / "RiemannFormal" / "Operator" / "XiSourceSpecific.lean"

THEOREM = re.compile(
    r"\btheorem\s+([A-Za-z0-9_]+)\b(?P<body>.*?)(?=\n(?:private\s+)?theorem\s+|\nend\s)",
    re.S,
)


def strip_comments(text: str) -> str:
    text = re.sub(r"/--.*?-/", "", text, flags=re.S)
    text = re.sub(r"/-.*?-/", "", text, flags=re.S)
    text = re.sub(r"--.*", "", text)
    return text


def theorem_bodies(text: str) -> dict[str, str]:
    clean = strip_comments(text)
    return {m.group(1): m.group("body") for m in THEOREM.finditer(clean)}


def dependency_closure(bodies: dict[str, str], root: str) -> str:
    todo = [root]
    seen: set[str] = set()
    chunks: list[str] = []
    while todo:
        name = todo.pop()
        if name in seen:
            continue
        seen.add(name)
        body = bodies.get(name)
        if body is None:
            continue
        chunks.append(body)
        for candidate in bodies:
            if candidate != name and re.search(rf"\b{re.escape(candidate)}\b", body):
                todo.append(candidate)
    return "\n".join(chunks)


def main() -> None:
    xi_text = XI.read_text(encoding="utf-8")
    shared_text = SHARED.read_text(encoding="utf-8")
    source_text = SOURCE.read_text(encoding="utf-8")

    forbidden = [
        "HighZeroVerified",
        "CorrectedSourceLock",
        "GroupedC2Convergence",
        "OrbitConventionLocked",
        "MultiplicityResidualRetained",
        "ReciprocalSquareTailControlled",
        "hrepeated",
        "PaymentWorks",
    ]
    combined = strip_comments(xi_text + shared_text + source_text)
    present = [token for token in forbidden if re.search(rf"\b{re.escape(token)}\b", combined)]
    if present:
        raise SystemExit(f"forbidden inert/generic input labels remain: {present}")

    required_shared = [
        "PublishedVerifiedHeightTheorem",
        "ExternalSourceLock",
        "GroupedActualXiC2Expansion",
        "CriticalMultiplicityResidual",
        "ActualXiReserveAllocation",
        "criticalLineBelowHeight",
        "valueConverges",
        "firstConverges",
        "secondConverges",
        "multiplicity_eq_analyticOrder",
        "reflected_multiplicity_eq_analyticOrder",
        "offLineRepresentativeUnique",
        "reciprocalSquareTail",
        "RegroupedActualXiC2Approximation",
        "regroupedActualXiPrefix",
        "prefixEnergyNonnegative",
        "leftover_nonnegative",
        "oneUse",
    ]
    missing_shared = [token for token in required_shared if token not in shared_text]
    if missing_shared:
        raise SystemExit(f"missing concrete external-input fields: {missing_shared}")

    bodies = theorem_bodies(xi_text)
    closure = dependency_closure(bodies, "actualXiPickOrderThreeConditional")
    required_usage = [
        "verified.sourceLockExact",
        "verified.criticalLineBelowHeight",
        "inputs.grouped",
        "inputs.residual",
        "inputs.reserve",
        "inputs.paidC2Approximation",
        "repeated12_pick_psd",
        "repeated13_pick_psd",
        "repeated23_pick_psd",
        "actualXiReciprocalConcavity_of_inputs",
        "regroupedActualXi_energy_tendsto",
        "actualXiReciprocalCurvature_of_inputs",
        "actualXiCompanionCurvature_of_inputs",
    ]
    missing_usage = [token for token in required_usage if token not in closure]
    if missing_usage:
        raise SystemExit(f"headline dependency closure omits concrete inputs: {missing_usage}")

    required_source = [
        "reflectedOffLine_cross_curvature_exact",
        "orbitEpsilon_le_nine_mul_tail",
        "reflectedOffLineOrbit_absorbed",
        "buildActualXiReserveAllocation",
        "share_nonnegative",
        "everyOrbitPaid",
        "totalShare_le_one",
        "leftover_nonnegative",
        "oneUse",
    ]
    missing_source = [token for token in required_source if token not in source_text]
    if missing_source:
        raise SystemExit(f"source-specific reserve layer incomplete: {missing_source}")

    print(
        "PASS_REVIEWER_C_EXTERNAL_INPUT_USAGE "
        f"headline_theorems={len(bodies)} concrete_fields={len(required_shared)}"
    )


if __name__ == "__main__":
    main()
