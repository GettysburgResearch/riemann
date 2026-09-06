# Explicit critical Xi source map: construction, norm, and domain

Status: **PROPOSED COMPONENT THEOREMS; INDEPENDENT REVIEW PENDING. RH NOT PROVED.**
Scope: actual xi quotient for every 0<a<1/2, original L2(0,infinity) norm.
Exact base: PR804 at `967b2c65bdd37dadf72e1d2e6d27a295707bcb60`.

The new positive source is

    d_b(t)=exp(-bt)[N(1-t)+log(N!)], N=floor(exp(t)), b=1/2+a.

Its exact transform is `(z+b-1)zeta(z+b)/(z+b)^2`. A causal beta/gamma-filtered
output has transform `Theta_a(z)D_b(z)`. The functional equation proves all
polarized input/output Gram identities and an isometry on the cyclic source
subspace. Its norm is exactly one. Its domain need NOT be the whole ambient
space; proving completeness is the remaining RH-equivalent obligation.

This is not a relabeling of the parent's positive safe Gram as a critical
Pick Gram. A local differential/convolution formula connects the parent
Jordan measure to the actual causal impulse, with the centering term retained.
That formula is not claimed bounded globally in L2(mu_a).

## Read

- CONSTRUCTION.md: explicit sources; equal norms; causal realization and
  maximal domain; local Jordan recovery; strict short-time contraction.
- DOMAIN_AND_APPROXIMATION.md: prescribed finite Toeplitz hierarchy, exact
  projection defect, all-rank source-cutoff error, and literal Mobius inverse.
- ATTEMPT.md: three attempted completions and the exact missing step.
- VALIDATION.md: commands, executed bounds, trust boundaries and corrections.

A strict contraction `<(2/3)^a` is proved on every L2(0,T) with T<=1/32.
The finite Gram truncation error is O_b(log(N+2)/(N+2)) at integer source
cutoff at most (N+2)^(2/b). Neither assertion proves global contractivity or
convergence of the inverse-Gram projection error.

The exact positive-source synthetic pair has uniformly coercive Toeplitz
Grams yet leaves a domain defect 3/4. It is not an L-function. For the actual
source b=3/4, a directed integer computation bounds the first projection
error by 11/50, including the complete tail. No high-rank scan or extrapolation.

Publication adds this sibling directory only. The original PR804 packet and
its inventory validator are preserved, as are main and all review records.
Claim/edge ledgers are exploratory documentation, not a canonical graph update.
Classical Hardy/Nyman--Beurling/Suzuki mechanisms are credited; no literature
novelty or priority claim is made.
