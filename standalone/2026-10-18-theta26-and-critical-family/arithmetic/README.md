# Quadratic residual upper estimates and a native frequency-sector bound

**Status: PROPOSED component results; independent review required.** There is
no new ordinary-zeta zero-free boundary or RH proof in this packet.

The work pushes the preceding exact shared-factor calculation into genuine
upper estimates. It also pays a complete frequency sector of the rational
Newton source. No file in the frozen PR #1001 packet is changed.

## Results

In [PROOF.md](PROOF.md), Heath-Brown's quadratic large sieve and an exact
flat-cutoff functional equation prove, for the actual discriminants `-8u`,

\[
\mathbb E_Q\left|L(s,\chi_{-8u})-
           \sum_{n\le K}\chi_{-8u}(n)n^{-s}\right|^2
\ll_\varepsilon Q^\varepsilon K^{1-2\Re s},\qquad 1\le K\le Q.
\]

This holds on every fixed compact set in `1/2<Re s<1`, including after
conditioning on finitely many local sign/ramification states. All square
parts, their row masks, and the full functional-equation dual are retained.

The result transfers the complete `zeta L M-1` residual to the explicit
Euler model with growing triangular inverse-Dedekind mollifiers. The allowed
growth powers are:

| Fixed real part | Root residual error tends to zero for | Absolute squared residual error tends to zero for |
|---|---:|---:|
| `3/4` | `X<=Q^eta`, `eta<1/4` | `X<=Q^eta`, `eta<1/6` |
| `5/6` | `X<=Q^eta`, `eta<2/5` | `X<=Q^eta`, `eta<3/10` |

The proof gives the error exponents throughout the general range, not just
these samples. For fixed mollifier length this extends the previous actual
full-L adapter from `Re s>3/4` to `Re s>1/2`.

The same proof optimizes over **every** function of finitely many local
quadratic states with a prescribed principal mean. An explicit finite Euler
inverse, normalized by an absolutely convergent auxiliary mean, attains the
minimum. Its extra variance is `O(y^(1-2 Re s))`; this estimate transfers to
actual fields even with `y=(log Q)^nu` growing, because the exact coefficient
masses pay the primorial support. This is constructive removal of an
auxiliary fluctuation. The minimum retains the ordinary rational bias
`|zeta(s) M_Z(s)-1|^2`, and the multiplier contains no `1/zeta(s)`.

In [NATIVE_FREQUENCY_TAIL.md](NATIVE_FREQUENCY_TAIL.md), the exact rational
Mellin input satisfies

\[
\int_{|t|>T}\left|
 \frac{\zeta(1/2+it)G_Y(1/2+it)^2}{-1/2+it}
\right|^2dt
\ll_\varepsilon (YT)^\varepsilon T^{-71/42}(T+Y^2).
\]

Thus frequencies above `Y^(84/71)` have subpower squared norm. The proof
uses Bourgain's published pointwise exponent and finite polynomial mean
values. An exact Plancherel and physical-restriction argument transfers this
to the original strict native square step, with its mixed terms paid by a
root-norm inequality. The classical twelfth-moment cutoff `Y^(6/5)` is also
proved; a recent source-qualified refinement is recorded separately.

## Remaining arithmetic estimate

Neither the quadratic family nor the high-frequency removal bounds the
retained rational low-frequency amplitude with a power of the old Möbius
energy strictly below two. The attempted direct positive-moment estimate
still pays a quadratic power on fixed compact frequency intervals. This is
the unresolved step toward an improved ordinary-zeta boundary; the proved
upper estimates above are not presented as its solution.

## Replay

From this directory:

```bash
python check_arithmetic.py --report check_report.json
python -O check_arithmetic.py
```

The checker uses only the Python standard library. It checks Gaussian-rational
local means and variances, the full finite-state least-squares identity,
shared-prime ramification masks, exact exponent balances, and the literal
strict Newton endpoint. It remains active under `python -O`. Its finite
calculations do not certify the analytic estimates or any zero-free theorem.
