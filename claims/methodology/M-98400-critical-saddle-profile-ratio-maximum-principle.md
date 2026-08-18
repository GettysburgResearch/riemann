# M-98400 — Critical-saddle profile-ratio maximum-principle programme

## Exact target

Where the denominator is positive, define

\[
Q(Y,p)=
\frac{U(Y/p,p^+)}{U(Y,p^+)}.
\]

The exact Bellman inequality is

\[
\boxed{Q(Y,p)\le p.}
\]

`L-98402` proves this throughout the hereditary mesoscopic corridor.  The only
remaining regime is the critical saddle where the least future prime is too
small for the Vinogradov--Korobov discrepancy to be dominated directly by the
Dickman margin.

## Required invariant

A valid maximum principle must exploit all of the following:

1. numerator and denominator use the same future-prime state;
2. both are Stieltjes transforms of the same signed base measure `dh`;
3. source activations are nested under `Y -> Y/p`;
4. the complete quotient profile, not one boundary coordinate, is retained;
5. division is forbidden at a zero or sign-indefinite denominator;
6. the mesoscopic corridor supplies the terminal boundary condition.

A candidate local inequality should be stress-tested against the exact finite
overshoot from PR #582 and against the \(\Omega(\sqrt N)\) state-minimality
separator.  Any proof using only PSD, parity covariance, logarithmic energy, or
a fixed moment list is invalid at the stated scope.
