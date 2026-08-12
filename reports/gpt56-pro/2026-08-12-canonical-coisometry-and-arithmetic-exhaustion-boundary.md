# Canonical coisometry and the exact arithmetic-exhaustion boundary

## Status

```text
branch: research/gpt56-pro/91008-cauchy-square-clark-jordan
RH:     UNPROVED
```

## Result of the requested attack

The model-space part of the requested theorem is now completely explicit.
If the crossed Blaschke factor `B_a` is constant, then

\[
 I_a=\Delta_a\Theta_a
\]

is a product of two inner functions and

\[
 \mathscr K_{I_a}
 =\mathscr K_{\Delta_a}\oplus\Delta_a\mathscr K_{\Theta_a}.
\]

After the common congruence by `1/Delta_a`, this gives the unitary

\[
 \mathcal C_a(h/\Delta_a)
 =(h_{\Theta},h_{\Delta}/\Delta_a),
\]

where `h=h_Delta+Delta_a h_Theta`.  Therefore

\[
 \mathcal K_a^{\rm src}
 =\mathcal K_a^{\rm crit}+\mathcal K_a^{\rm st}.
\]

Conversely, any exact Hilbert-space norm exhaustion with those source,
critical and stable kernels forces the positive hyperbolic kernel in `L-91034`
to vanish.  Its diagonal is

\[
 \frac{1-|B_a(z)|^2}{2\Re z\,|B_a(z)|^2},
\]

so vanishing makes `B_a` a unimodular constant.  Hence

```text
norm exhaustion at scale a
<=> no crossed zero of depth greater than a.
```

All-scale exhaustion is exactly RH.

## What is genuinely still missing

The explicit arithmetic safe source and the pole-removed model-space source
are not the same object by notation:

```text
arithmetic source:
  Hankel/Laplace or first-chaos feature space;

model source:
  de Branges--Rovnyak feature space of Delta_a B_a Theta_a.
```

The required arithmetic theorem is an explicit tangent-level identification
between these two spaces.  Suzuki's multiplicative Hankel operator supplies the
completed amplitude isometry, but amplitude unitarity does not imply positivity
of the normalized radial Wigner--Smith curvature.  The exact control
`Theta_a(z)=exp(i a^2 z)` already disproves that implication.

Thus the surviving construction target is:

\[
 \mathcal J_a:
 \mathfrak g_a^{\Gamma,\mathrm{pole}}
 \oplus\mathfrak h_a^{\rm Jordan,1}
 \longrightarrow
 \mathscr S_a,
\]

with the following mandatory properties:

1. `J_a` is source ordered and preserves every carrier polarization;
2. its source kernel is the completed normalized first-chaos kernel, not merely
   one diagonal or one Green slice;
3. it intertwines the delayed causal/anti-causal Cauchy filter on a common
   model-space domain;
4. it is unitary on the source feature span, with no unused arithmetic kernel;
5. after the canonical `C_a` of `L-91038`, no auxiliary output remains.

By `L-91038`, satisfying these five items proves the zero-free strip at scale
`a`; satisfying them cofinally as `a downarrow0` proves RH.

## Exact finite replay

`X-91026` verifies the kernel algebra with exact rational arithmetic:

```text
PASS_CANONICAL_COISOMETRY_EXHAUSTION_EQUIVALENCE
checks: 56
minimum nonzero omitted-port diagonal defect: 108/49
```

The replay certifies neither the arithmetic tangent identification nor RH.

## Strategic conclusion

The phrase "prove norm exhaustion" is not a soft final Hilbert-space lemma.
The canonical model-space coisometry is available explicitly once the zero port
is absent, and exact exhaustion conversely forces that absence.  The only
noncircular remaining route is to construct the arithmetic first-chaos tangent
map itself and prove its Douglas kernel equality from primes and the completed
gamma/pole channel.
