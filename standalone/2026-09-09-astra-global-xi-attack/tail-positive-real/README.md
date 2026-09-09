# TPR26 — positive-real control of the exact omitted theta source

**Proposed complete component proofs; independent review required. RH and the
full complex Laguerre inequality remain unproved.** This is an add-only
continuation of #835 at `815ccae329a17327b873d21f05bc30c24db13e7e`.

Read [PROOF.md](PROOF.md), then [VALIDATION.md](VALIDATION.md). The source and
parent executable are fixed by [SOURCE_LOCK.json](SOURCE_LOCK.json).

Let `F=Xi`, let `F_N` be the cosine transform of the first N literal positive
half-line theta summands, and let `T_N=F-F_N`, `q=pi(N+1)^2`. The complete tail
is NOT replaced by its first summand or by a different model.

The manuscript proves, for every N>=1:

1. `Re T_N(x+iy)>0` for all real x and `|y|<=q`. The tail is zero-free there.
   In particular `F_N(x)<F_(N+1)(x)<F(x)` on the real line.
2. On the entire critical band, with unbounded real frequency,
   `q^3 exp(-q)/(18(4q^2+x^2)) <= Re T_N <= |T_N| <=256q^3 exp(-q)/(4q^2+x^2)`.
   The rational reference `L_q(z)=16q^3 exp(-q)/(4q^2+z^2)` also satisfies
   `|T_N/L_q-1|<=256/q`. The error is not asserted less than one at small N.
3. Every critical-band zero of the CHANGED raw truncation F_N has
   `|Re z|<=4(N+1)^2+(16/pi)log(N+1)+C`, for an absolute, unevaluated C.
   This is a truncation horizon, not a new zero-free region for zeta.
4. The parent's three-term candidate is separated from the full function:
   its exact center has a simple F_3 zero in radius `10^-35`, while
   `Re Xi>7*10^-32` on that same whole disk. This small source-level
   certificate uses the parent's defining-integral replay and the new
   analytic complete-tail lower bound. It is not a new zero census.

The sign proof uses convexity of each tilted omitted summand, not positivity
of an arbitrary Fourier kernel. The uniform relative estimate uses both an
L1 error and two integration-by-parts errors; a fixed-frequency expansion
alone would not cover the whole line. Neither theorem proves that adding a
positive-real tail to F_N preserves real zeros. Section 8 displays the exact
remaining mixed Laguerre terms and the failed closing inference.

## Reproduction

At the intended repository location this directory is a child of the original
#835 packet. All seven parent files remain unchanged. The three consumed parent
files are authenticated by length, Git blob and SHA256 before use.

```
python -I -S -B check.py --check verification.json
python -I -S -B -O check.py --check verification.json
python -I -S -B check.py --full --check verification.json
python -I -S -B -O check.py --full --check verification.json
python -I -S -B test_check.py
python -I -S -B -O test_check.py
```

The two `--full` commands rerun the original 152-cell, 384-bit defining-integral
certificate and require byte-for-byte agreement with its frozen receipt.
The default command checks exact finite algebra and transfers its authenticated
bounds; it does not rerun those integrals. `--emit` is a producer mode, not an
accepting interface. Use `--parent PATH` when the frozen original packet is in
another directory. The tests likewise accept `--parent PATH`.

The checker does not machine-prove the all-scale analytic theorems. Normal and
optimized runs of the same implementation are not independent implementations
or additional mathematical referees. No predecessor claim is silently promoted.
