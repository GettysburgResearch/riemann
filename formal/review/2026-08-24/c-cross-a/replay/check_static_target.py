#!/usr/bin/env python3
from __future__ import annotations
import subprocess, sys
from pathlib import Path

TARGET = "92f70a3b49b9295b5efb88491107670065b03317"
BOOTSTRAP = "573eb6aa42c3d9469462c91c6b3ddfb8ab36d77f"
REQUIRED = [
    "formal/registry/deltas/A_UPSTREAM_REUSE.tsv",
    "formal/registry/deltas/A.tsv",
    "formal/RiemannFormal/Analysis/LandauConsumer.lean",
    "formal/RiemannFormal/Analysis/MellinAPI.lean",
    "formal/RiemannFormal/Analysis/SingularityTransfer.lean",
    "formal/RiemannFormal/Analysis/Reflection.lean",
    "formal/comparator/Challenge/MellinAPI.lean",
    "formal/comparator/Solution/MellinAPI.lean",
]

def show(repo: Path, path: str) -> str:
    return subprocess.check_output(
        ["git", "-C", str(repo), "show", f"{TARGET}:{path}"], text=True
    )

def main() -> None:
    repo = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    for path in REQUIRED:
        show(repo, path)

    bridge = show(repo, "formal/RiemannFormal/Upstream/Zeta23Bridge.lean")
    audit = show(repo, "formal/RiemannFormal/AxiomAudit.lean")
    landau = show(repo, "formal/RiemannFormal/Analysis/LandauConsumer.lean")
    solution = show(repo, "formal/comparator/Solution/MellinAPI.lean")
    diff = subprocess.check_output(
        ["git", "-C", str(repo), "diff", BOOTSTRAP, TARGET, "--", "formal"],
        text=True,
    )

    assert "zeta23_bridge_preserves_RH" in audit
    assert "theorem zeta23_bridge_preserves_RH" not in bridge
    assert "def MellinLandauBoundarySingularity" in landau
    assert "mellin (fun x : ℝ => (f x : ℂ)) s" in landau
    landau_stmt = landau.split("def MellinLandauBoundarySingularity", 1)[1].split("/-- Data", 1)[0]
    assert "Set.Ici 1" not in landau_stmt
    assert "def SubpowerNegativeMassHolomorphy" in landau
    assert "import Challenge.MellinAPI" not in solution
    for forbidden in ("\naxiom ", "\nopaque ", "\nunsafe "):
        assert forbidden not in diff

    print("PASS_C_CROSS_A_STATIC_AUDIT")
    print("BUILD_BLOCKER_MISSING_ZETA23_BRIDGE=true")
    print("LANDAU_TAIL_ADAPTER_PRESENT=false")
    print("SUBPOWER_TAIL_ADAPTER_PRESENT=false")
    print("FINAL_CONDITIONAL_CONSUMER_PRESENT=false")
    print("CUSTOM_AXIOM_OR_OPAQUE_IN_DIFF=false")
    print("RH_PROVED=false")

if __name__ == "__main__":
    main()
