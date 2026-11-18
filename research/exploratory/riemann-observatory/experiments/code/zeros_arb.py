#!/usr/bin/env python3
"""Rigorous ordinates of nontrivial zeta zeros via Arb (python-flint acb.zeta_zeros).
Arb isolates zeros on the critical line and certifies counts with Turing's method; each output is a ball
(midpoint, radius). Usage: python3 zeros_arb.py START COUNT OUT.tsv [PREC_BITS]
Output columns: n, midpoint (25 sig. digits), radius (upper bound)."""
import sys, time, flint
start, count, out = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
flint.ctx.prec = int(sys.argv[4]) if len(sys.argv) > 4 else 96
t0 = time.time()
with open(out, "w") as f:
    n, chunk = start, 2000
    while n < start + count:
        k = min(chunk, start + count - n)
        for i, z in enumerate(flint.acb.zeta_zeros(n, k)):
            im = z.imag
            f.write(f"{n+i}\t{im.mid().str(25, radius=False)}\t{float(im.rad()):.3e}\n")
        n += k
        f.flush()
print("done", start, count, round(time.time() - t0, 1), "s", flush=True)
