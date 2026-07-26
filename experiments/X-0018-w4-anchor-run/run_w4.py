#!/usr/bin/env python3
"""
X-0018 -- Execute the PR #128 / X-9312 one-point production handoff at w = 4.

Agent: claude-02 (this repository's second agent; branch
claude/riemann-repo-development-h4vg4v).  This is the directed run that the
gpt56-04-e handoff (CANDIDATE_HANDOFF.md on branch
agent/gpt56-04-e/93-positive-anchor-geronimus) requested and that no agent had
performed: evaluate the completed-xi point

    s = 5/2 + i T,   T = 20225875608343133989267 / 2^32,

at 512 and 640 Arb bits, enclose the one new moment b0 both by the direct
seventeen-node response-1 contraction and by the L-9315 reduced one-new-point
replay, require overlap, and feed the directed rational interval to the
committed fail-closed checker verify_b0_interval.py.

REUSED REVIEWED CODE (imported from the PR #128 head worktree, never copied):
  * X-9309 verify_zero_anchor: RationalInterval, ExactLogEncloser,
    modulus_square, deflation_shells, residual_interval, basis_vector,
    load_json, file_sha256, fraction
  * X-9312 positive_anchor: load_basis, reduced_replay
  * X-9312 verify_b0_interval.py: the final verdict (run as a subprocess)

BINDING DIVERGENCE, DOCUMENTED: the gpt56-03-i PA1 verifier binds the basis to
its source certificate by requiring basis.source_certificate_sha256 to equal
the certificate's file-sha256 or internal digest.  On every branch carrying
these files the declared value (44a0101c...) matches NEITHER -- nor any file in
the results trees -- so that check can never pass and PR #135's workflow is
wedged.  The basis ALSO declares source_certificate_git_blob_sha1 =
a02e20c0..., and that DOES match the certificate byte-exactly.  This run
binds by the git-blob convention (strictly pinning the same bytes) and by
primitive_sha256, and records all digests.

Usage: python3 run_w4.py --w4-tree /home/user/w4 \
                         --anchor-low results/w4-p512.json \
                         --anchor-high results/w4-p640.json
"""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
import time
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent


def git_blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob %d\x00" % len(raw) + raw).hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--w4-tree", type=Path, required=True)
    ap.add_argument("--anchor-low", type=Path, required=True)
    ap.add_argument("--anchor-high", type=Path, required=True)
    ap.add_argument("--log-terms", type=int, default=240)
    ap.add_argument("--output", type=Path, default=HERE / "results" / "w4-run.json")
    args = ap.parse_args()

    x9309 = args.w4_tree / "experiments" / "X-9309-zero-anchor-degree15"
    x9312 = args.w4_tree / "experiments" / "X-9312-positive-anchor-geronimus"
    x9302 = (args.w4_tree / "experiments" / "X-9302-total-count-zero-deflation"
             / "results" / "pr71-shift-fine" / "atomized-min-certificate-p512.json")
    x9306 = (args.w4_tree / "experiments" / "X-9306-real-log-portfolio-search"
             / "results" / "basis.json")
    sys.path.insert(0, str(x9309))
    sys.path.insert(0, str(x9312))
    import verify_zero_anchor as parent  # noqa: E402
    import positive_anchor as pa  # noqa: E402

    W = Fraction(4)
    t0 = time.time()
    prov = {
        "w4_branch_head": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=args.w4_tree, text=True).strip(),
        "verify_zero_anchor_sha256": parent.file_sha256(x9309 / "verify_zero_anchor.py"),
        "positive_anchor_sha256": parent.file_sha256(x9312 / "positive_anchor.py"),
        "verify_b0_interval_sha256": parent.file_sha256(x9312 / "verify_b0_interval.py"),
        "old_certificate_sha256": parent.file_sha256(x9302),
        "old_certificate_git_blob_sha1": git_blob_sha1(x9302),
        "old_basis_sha256": parent.file_sha256(x9306),
        "anchor_low_sha256": parent.file_sha256(args.anchor_low),
        "anchor_high_sha256": parent.file_sha256(args.anchor_high),
    }

    old_certificate = parent.load_json(x9302)
    old_basis, old_moments = pa.load_basis(x9306)
    low = parent.load_json(args.anchor_low)
    high = parent.load_json(args.anchor_high)

    # ---- bindings that must hold ------------------------------------------
    if old_certificate.get("classification") != "RIEMANN_XI_DIRECTED":
        raise SystemExit("old certificate classification mismatch")
    norm = old_certificate.get("normalization_id")
    for name, doc in (("anchor-low", low), ("anchor-high", high)):
        if doc.get("normalization_id") != norm:
            raise SystemExit(f"{name} normalization mismatch")
        for field in ("ordinate", "common_xi_scale_power_of_two"):
            if doc.get(field) != old_certificate.get(field):
                raise SystemExit(f"{name} {field} mismatch")
    if old_basis.get("ordinate") != old_certificate.get("ordinate"):
        raise SystemExit("basis ordinate mismatch")
    declared_blob = old_basis.get("source_certificate_git_blob_sha1")
    if declared_blob != prov["old_certificate_git_blob_sha1"]:
        raise SystemExit("basis -> certificate git-blob binding failed")
    src = old_certificate.get("source")
    if (not isinstance(src, dict)
            or old_basis.get("primitive_sha256") != src.get("primitive_sha256")):
        raise SystemExit("basis primitive digest mismatch")
    prov["binding_note"] = (
        "bound via source_certificate_git_blob_sha1 (byte-exact) and "
        "primitive_sha256; the declared source_certificate_sha256 "
        f"{old_basis.get('source_certificate_sha256')!r} matches no file or "
        "internal digest on any branch carrying these files (defect reported "
        "on PR #135)")

    # ---- anchor point: x = 2, nesting, positive modulus -------------------
    if low.get("precision_bits") >= high.get("precision_bits"):
        raise SystemExit("precision order invalid")
    pts_low, pts_high = low.get("points"), high.get("points")
    if len(pts_low) != 1 or len(pts_high) != 1:
        raise SystemExit("expected exactly one emitted point")
    pl, ph = pts_low[0], pts_high[0]
    for name, p in (("low", pl), ("high", ph)):
        x = p.get("x", {})
        if (x.get("numerator"), x.get("denominator")) != (2, 1):
            raise SystemExit(f"{name} point is not x = 2")
        if not p.get("functional_equation_residual_contains_zero"):
            raise SystemExit(f"{name} functional-equation flag missing")
    for comp in ("real", "imag"):
        rl = parent.parse_interval(pl["xi_rectangle"][comp], f"low.{comp}")
        rh = parent.parse_interval(ph["xi_rectangle"][comp], f"high.{comp}")
        if not (rl.lower <= rh.lower and rh.upper <= rl.upper):
            raise SystemExit(f"640-bit {comp} rectangle not nested in 512-bit")
    hsq = parent.modulus_square(ph)
    if hsq.lower <= 0:
        raise SystemExit("modulus-square lower endpoint not positive")

    # ---- residuals --------------------------------------------------------
    raw_points = old_certificate["points"]
    if len(raw_points) != 16:
        raise SystemExit("expected the sixteen-node old certificate")
    old_points = sorted(raw_points, key=lambda p: parent.fraction(p["u"], "u"))
    old_nodes = [parent.fraction(p["u"], "u") for p in old_points]
    if W in set(old_nodes):
        raise SystemExit("anchor duplicates an old node")
    shells = parent.deflation_shells(old_certificate)
    log = parent.ExactLogEncloser(args.log_terms)
    old_residuals = [parent.residual_interval(p, u, shells, log)
                     for p, u in zip(old_points, old_nodes)]
    anchor_residual = parent.residual_interval(ph, W, shells, log)

    # ---- direct seventeen-node response-1 contraction ---------------------
    full_nodes = old_nodes + [W]
    full_coeffs = parent.basis_vector(full_nodes, 0)
    if sum(full_coeffs) != 0:
        raise SystemExit("full response vector is not zero-sum")
    full_b0 = parent.RationalInterval(Fraction(0), Fraction(0))
    acc_lo = Fraction(0)
    acc_hi = Fraction(0)
    for c, r in zip(full_coeffs, old_residuals + [anchor_residual]):
        lo, hi = (c * r.lower, c * r.upper) if c >= 0 else (c * r.upper, c * r.lower)
        acc_lo += lo
        acc_hi += hi
    full_b0 = parent.RationalInterval(acc_lo, acc_hi)

    # ---- reduced one-new-point replay (L-9315) ----------------------------
    red = pa.reduced_replay(old_nodes, W, reference_index=0)
    beta = red["beta_anchor"]
    poly = red["old_response_coefficients"]
    if len(poly) != len(old_moments):
        raise SystemExit("reduced polynomial degree does not match moment rows")
    diff = anchor_residual.sub(old_residuals[0])
    dl, dh = (beta * diff.lower, beta * diff.upper) if beta >= 0 else \
             (beta * diff.upper, beta * diff.lower)
    acc_lo, acc_hi = dl, dh
    for c, m in zip(poly, old_moments):
        lo, hi = (c * m.lower, c * m.upper) if c >= 0 else (c * m.upper, c * m.lower)
        acc_lo += lo
        acc_hi += hi
    reduced_b0 = parent.RationalInterval(acc_lo, acc_hi)

    # ---- overlap and intersection -----------------------------------------
    lo = max(full_b0.lower, reduced_b0.lower)
    hi = min(full_b0.upper, reduced_b0.upper)
    if lo > hi:
        raise SystemExit("direct and reduced b0 enclosures do not overlap")
    b0 = parent.RationalInterval(lo, hi)

    dec = pa.decimal_string
    print(f"full    b0 in [{dec(full_b0.lower)}, {dec(full_b0.upper)}]")
    print(f"reduced b0 in [{dec(reduced_b0.lower)}, {dec(reduced_b0.upper)}]")
    print(f"intersection  [{dec(b0.lower)}, {dec(b0.upper)}]")
    print(f"width: {dec(b0.upper - b0.lower, 8)}")

    # ---- candidate file and the committed checker -------------------------
    candidate_path = HERE / "results" / "w4-candidate.json"
    candidate_path.write_text(json.dumps({
        "schema": "riemann.x9312-positive-anchor-b0.v1",
        "anchor": {"numerator": 4, "denominator": 1},
        "b0_interval": {
            "lower": {"numerator": b0.lower.numerator,
                      "denominator": b0.lower.denominator},
            "upper": {"numerator": b0.upper.numerator,
                      "denominator": b0.upper.denominator},
        },
    }, indent=1) + "\n")

    verdict_path = HERE / "results" / "w4-verdict.json"
    proc = subprocess.run(
        [sys.executable, str(x9312 / "verify_b0_interval.py"),
         str(x9306), str(candidate_path), "--output", str(verdict_path)],
        capture_output=True, text=True, cwd=x9312)
    print("checker stdout:", proc.stdout.strip()[:2000])
    if proc.stderr.strip():
        print("checker stderr:", proc.stderr.strip()[:800])

    verdict = json.loads(verdict_path.read_text()) if verdict_path.exists() else {}
    out = {
        "schema": "riemann.x0018-w4-anchor-run.v1",
        "agent": "claude-02",
        "anchor": {"numerator": 4, "denominator": 1},
        "point": {"re": "5/2", "ordinate": old_certificate.get("ordinate")},
        "provenance": prov,
        "log_terms": args.log_terms,
        "full_b0": [dec(full_b0.lower), dec(full_b0.upper)],
        "reduced_b0": [dec(reduced_b0.lower), dec(reduced_b0.upper)],
        "b0_intersection": [dec(b0.lower), dec(b0.upper)],
        "b0_width": dec(b0.upper - b0.lower, 8),
        "full_reduced_overlap": True,
        "checker_exit_code": proc.returncode,
        "checker_verdict": verdict.get("verdict"),
        "seconds": round(time.time() - t0, 1),
    }
    args.output.write_text(json.dumps(out, indent=1) + "\n")
    print(f"\nchecker exit code: {proc.returncode}")
    print(f"checker verdict:   {verdict.get('verdict')}")
    print("wrote", args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
