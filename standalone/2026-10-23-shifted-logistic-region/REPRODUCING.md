# Reconstructing the finite obligations

From this directory, with Python3 and its standard library:

```sh
python -I -S -B replay_exact.py
```

The launcher authenticates every component listed in COMPONENT_HASHES.json,
copies the packet to a temporary directory, and executes ten checkers in
ordinary and optimized mode. It requires byte-identical stdout between
those modes. The input files in this packet are not changed.

The checks reconstruct the kernel constants, curvature, polynomial,
signed archimedean bound, low prime gain, combined high prime gain,
complete R=4.72 low rectangle, earlier general Ford engine, new Euler
constants, and shifted high endpoint. They use integer/Fraction arithmetic
and explicit elementary-function remainders. Decimal renderings are only
for reading; they do not decide acceptance.

The low checker covers 0<=A<=25/118 and28.7<=log(t)<=52 by28 disjoint
rectangles, with exact area1165/236. Its smallest lower endpoint exceeds
.00009525971317. The high endpoint at25/118,52 exceeds.0002948890299043;
the analytic monotonicity proof extends it to every larger height.

The 1280 retained prime powers in the Euler check are followed by explicit
infinite tails. The finite prime covers include every phase and negative
controls. Stored JSON is a receipt, never the acceptance input.

These are finite arithmetic and integrity checks. The imported analytic
theorems, finite RH computation, and the analytic detector proofs require
their separate mathematical review. No repository-wide tests or remote
CI are asserted by this launcher.
