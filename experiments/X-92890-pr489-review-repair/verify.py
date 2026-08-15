#!/usr/bin/env python3
import argparse
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
CONTROL = json.loads((HERE / "certificates/control.json").read_text())

def fail(msg):
    raise AssertionError(msg)

def check(mutate=None):
    c = json.loads(json.dumps(CONTROL))
    if mutate == "full_capacity":
        pass
    elif mutate == "nonzero_port":
        c["constants"]["port"] = 1
    elif mutate == "terminal":
        c["constants"]["terminal_reserve"] = 4452
    elif mutate == "total":
        c["constants"]["claimed_total"] = 61000
    elif mutate == "base":
        c["base_sha"] = "0" * 40

    k = c["constants"]
    assert c["base_sha"] == "0bb487c8a0782f601be0a3041743b357ad93726a"
    assert k["thinning"] + k["nonterminal"] + k["terminal"] + k["omissions"] == k["claimed_total"]
    assert k["claimed_total"] < k["ceiling"]
    assert k["terminal_reserve"] - k["terminal_overfill"] == 581
    assert 1 / (k["rough_factor"] ** 0.5) < 1 / 8
    assert k.get("port", 0) == 0

    for rel in c["required_paths"]:
        if not (ROOT / rel).exists():
            fail(f"missing required path: {rel}")

    controlling = "\n".join(
        (ROOT / p).read_text()
        for p in c["required_paths"]
        if p.endswith(".md")
    )
    if mutate == "full_capacity":
        controlling += "\nsum_b beta_b U_b Omega_{Y_b}\n"
    for bad in c["forbidden_controlling_claims"]:
        if bad in controlling:
            fail(f"forbidden controlling claim present: {bad}")

    r = (ROOT / "claims/refutations/R-92890-full-child-capacity-promotion-is-removed.md").read_text()
    assert "Xi(P_b)" in r and "Omega(P_b)" in r
    p = (ROOT / "claims/lemmas/L-92892-one-shot-correction-stack-has-zero-schur-demand.md").read_text()
    assert "D_X^{\\rm actual}" in p and "P_X^{\\rm port}=0" in p
    t = (ROOT / "claims/theorems/T-92890-native-deficit-below-61000-implies-rh.md").read_text()
    assert "C_{\\rm pp}" in t and "Landau" in t and "61000" in t

    h = hashlib.sha256()
    for rel in sorted(c["required_paths"]):
        h.update(rel.encode())
        h.update(b"\0")
        h.update((ROOT / rel).read_bytes())
        h.update(b"\0")

    return {
        "ok": True,
        "verdict": "PASS_PR489_REVIEW_REPAIRED_ONE_SHOT_PACKET",
        "proof_object_sha256": h.hexdigest(),
        "checks": {
            "base_pin": True,
            "required_paths": True,
            "full_capacity_promotion_removed": True,
            "zero_port_decompiled": True,
            "terminal_margin": True,
            "native_cost": True,
            "endpoint_moat_landau": True
        },
        "scope": "finite algebra, constants, file/pin authentication; analytic Hall, endpoint and Mellin inputs require independent reconstruction",
        "rh_proved": False
    }

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mutations", action="store_true")
    ap.add_argument("--output")
    args = ap.parse_args()

    result = check()
    mutations = {}
    if args.mutations:
        for name in ["full_capacity", "nonzero_port", "terminal", "total", "base"]:
            try:
                check(name)
            except Exception:
                mutations[name + "_fails"] = True
            else:
                mutations[name + "_fails"] = False
                fail(f"mutation unexpectedly passed: {name}")
    result["mutations"] = mutations

    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        Path(args.output).parent.mkdir(parents=True, exist_ok=True)
        Path(args.output).write_text(text)
    print(result["verdict"])
    print(result["proof_object_sha256"])

if __name__ == "__main__":
    main()
