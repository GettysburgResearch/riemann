# Final vertical prime-energy attack

Agent: `gpt56-pro-19`  
Date: 2026-08-07  
Stack: PR #224 on PRs #222 and #216  
Status: **RH not proved**

## Requested statement

The target was

\[
 \int_{\mathbb R}
 |\widehat H(\sigma+it)|^2
 \left|P_1\!\left(\frac12+\sigma+it\right)\right|^2dt
 <\infty
 \qquad(\sigma>0).
\]

The attack treated the displayed integral itself rather than replacing it by another finite ladder.

## Main new theorem

`T-22302` proves that the vertical energy is a literal pole tomograph.

If

\[
 \rho=\frac12+\delta+i\gamma
\]

is an off-critical zeta zero of multiplicity `m`, then the prime logarithmic derivative has local principal part

\[
 P_1(1/2+z)=-{m\over z-(\delta+i\gamma)}+\text{analytic},
\]

and the fixed safe multiplier is nonzero at that point. Therefore

\[
 I_H(\delta)=\infty.
\]

More precisely, on one isolated ordinate neighborhood,

\[
 I_{\rho,r}(\sigma)
 ={\pi m^2|\widehat H(\delta+i\gamma)|^2
   \over|\sigma-\delta|}
 +O\!\left(\log{1\over|\sigma-\delta|}\right).
\]

Under RH, every zero remains a fixed horizontal distance `sigma` from the line, the logarithmic derivative has polylogarithmic vertical growth, and the `t^-2` decay of `widehat H` makes the requested integral finite.

Hence the target is exactly equivalent to RH, directly at the vertical-line level.

## Exact corrected positive interface

For every compact interval

\[
 0<a<b<1/2,
\]

a proof-producing positive result must establish

\[
 \sup_{a\le\sigma\le b}I_H(\sigma)<\infty.
\]

One such bound excludes every zero in the corresponding closed vertical strip. Overlapping compact strips covering `(0,1/2)` prove RH.

`R-22302` explains why almost-everywhere estimates, rational-line estimates, Bohr means, or linewise bounds with uncontrolled constants do not suffice: they can omit the countable set of pole lines, and the exact blow-up is finite on every punctured line while unbounded in the compact-strip supremum.

## Routes attempted

### Standard Dirichlet-Hardy and weak product

Already refuted by `R-22301`. The standard embedding lands one half-plane too far right, and the identity orbit has unbounded local mass even for coefficient-normalized polynomials.

### Prime-supported improvement

Restricting the no-go polynomial to primes still produces coherent local mass of order `N/log N`; prime support alone does not give the missing trace theorem.

### Semiprime grouping

Squaring reduces the arithmetic to one product-scale semiprime signal, but coefficient `ell^2` convergence does not control densely clustered logarithmic translates. The missing cancellation is exactly the semiprime discrepancy.

### Selberg Riccati identity

The equation

\[
 -H'+{2\over z-1/2}H+H^2=\mathcal R
\]

is exact, but at a simple zero the leading double poles of `-H'` and `H^2` cancel. The nonlinear identity is compatible with an isolated off-line simple zero and does not by itself give a dissipative sign.

### Positivity of generalized von Mangoldt coefficients

`Lambda_2>=0` retains the dominant real pole at `s=1`. Every finite pole-annihilating filter necessarily introduces signed coefficients or a signed physical window. Landau positivity cannot be applied after the RH-sensitive main cancellation.

### Conventional PNT, zero density, and large sieve

They bound phase-blind magnitudes and leave a positive exponential factor. One off-line zero is enough to violate the compact-strip bound, so density estimates cannot close the universal statement.

### Adaptive narrowing or additional differences

The resolution barrier from `R-22102` persists. Fine enough localization creates a diagonal with critical exponent `1/2`; repeated safe differences attenuate a fixed small horizontal displacement unless their support cost grows comparably.

## Exact regression

`X-22302` verifies the finite inverse-distance and punctured-line lower-bound algebra with integers and `fractions.Fraction`.

Retained values:

```text
residue modulus squared          9
principal-part dominance        1/2
scaled inverse-distance constant 9/4
local lower bounds               9/2, 9, 18, 36
punctured-line lower bounds      9/2, 9, 18, 36
proof-object SHA-256
6a16cbe701ab9a7a2641b82b72c2294daa08174b9cd6a3b0bb96cd5ae984584f
```

Eight central and mutation tests are committed. The result is synthetic local meromorphic algebra only.

## Exact smallest blocker

The smallest noncircular theorem is now

\[
 \boxed{
 \sup_{a\le\sigma\le b}
 \int_{\mathbb R}
 |\widehat H(\sigma+it)|^2
 \left|P_1\!\left(\frac12+\sigma+it\right)\right|^2dt
 <\infty
 }
\]

for every fixed `0<a<b<1/2`.

Equivalently, prove a locally uniform critical Carleson embedding for this one prime-supported analytic ray. Universal Dirichlet-Hardy or weak-product embeddings are false; the proof must use the exact prime/semiprime arithmetic.

## Conclusion

The requested integral was not proved. The attack established its exact local singularity law and showed that no almost-everywhere or line-by-line soft estimate can be promoted to RH. The global proof still requires a genuinely arithmetic compact-strip embedding.
