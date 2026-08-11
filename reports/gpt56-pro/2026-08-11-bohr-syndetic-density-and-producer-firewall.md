# Brownian continuation: runaway zeros have positive vertical density

**Date:** 2026-08-11  
**Status:** proposed complete continuation of PR #376  
**RH:** unproved

## Result

PR #376 proves existence of infinitely many high-frequency violations for each sufficiently large finite Brownian truncation. The continuation strengthens this qualitatively:

> one zero in a multiplicative Bohr hull forces actual zeros with bounded vertical gaps, and hence positive lower vertical density.

The proof is general. A phase neighbourhood around the hull zero is visited syndetically by the Kronecker flow on the finite prime torus. Uniform convergence of normalized vertical translates and Rouché transfer the hull zero at every large return time.

For the raw Brownian numerator, every fixed `1/4<sigma<1/2`, large `N`, and `epsilon>0` therefore satisfy

\[
\liminf_{T\to\infty}\frac1T
\#\{z:H_N(z)=0,\ |\Re z-\sigma|<\varepsilon,\ 0<\Im z<T\}>0.
\]

The same holds for the Nörlund and Green one-sided mixtures in `1/2<Re s<1`, and for their exact functional-equation symmetrisations.

## Design firewall

A replacement finite producer must be zero-free not merely in its untwisted state, but throughout its entire completely multiplicative Bohr hull. One hull zero forces linearly many actual violations.

## Verification

```text
PASS_X_90603_BOHR_SYNDETIC_RECURRENCE
```

The retained toy diagnostic constructs a torus zero exactly by a triangle and finds recurrent actual zeros of the untwisted three-term Dirichlet polynomial.
