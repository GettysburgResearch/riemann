# Repository-wide RH proof attempt — consolidated result

Date: 2026-08-07  
Agent: `gpt56-08`

## Executive verdict

The repository has converged to a single global arithmetic obstruction, but the
current pass did not prove it. I therefore do **not** claim a full proposed
resolution of RH.

The shortest complete chain is:

```text
critical Möbius/prime signed-correlation estimate
    -> analytic-totient local second moment
    -> Mellin holomorphy in Re(s)>1/2
    -> RH.
```

The exact remaining theorem is
\[
\int_X^{2X}|E^{\rm AN}(t)|^2dt
\ll_\varepsilon X^{2+\varepsilon},
\]
or equivalently the critical Farey correlation `L-9515` / common gate
`L-23002`.

## What the repository has genuinely completed

1. Multiple exact RH-equivalent scalar criteria:
   square screw, finite totient Riesz errors, and analytic-totient energy.
2. Exact rightmost-zero exponents for those criteria.
3. A positive phase-free energy whose excess exponent is twice the horizontal
   displacement of the rightmost zero.
4. Exact full-period resonant covariance and positive Jordan-totient
   factorization.
5. Exact finite dyadic transport, semiprime, Schur and pole-exposure
   dictionaries.
6. Refutations of the main false shortcuts:
   finite ladders, coefficient-blind large sieve, prime-by-prime contraction,
   compact positive-Hankel stop-loss inversion, and local-zero-to-global
   extrapolation.

## What remains

The unresolved cluster consists of Möbius-weighted rational frequencies at
spacing \(D^{-2}\) observed on a physical interval of length \(D\).
A generic large sieve loses one power. The required gain must come from the
joint arithmetic signs before absolute values are taken.

The most plausible proof program remains:

1. determinant parameterization \(kb-\ell a=h\);
2. two-dimensional Möbius/Heath–Brown dispersion;
3. exact extraction of the \(h=0\) Jordan square;
4. a uniform critical estimate for the nonzero dual modes;
5. recombination with the complete Bernoulli and tail packet.

The fourth item is not presently justified.

## New durable files

- `claims/lemmas/L-9515-critical-farey-dispersion-candidate.md`
- `claims/refutations/R-9506-coefficient-blind-local-to-bohr-fails.md`
- `claims/theorems/T-9508-repository-wide-rh-proof-spine.md`

This packet is designed for immediate adversarial review. The reviewer should
attack `L-9515` first; accepting the surrounding exact reductions while leaving
that lemma open does not prove RH.
