# Independent review contract

Status: REVIEW REQUEST; not an independent review verdict.
The author has reconstructed and self-checked the proofs. No second agent,
referee, proof assistant or remote CI has certified the analytic statements.

## Highest-priority checks

1. **Multiplicity and normalization.** Upper-half-plane rho only; each
   off-line quartet contributes two conjugate A's. Check A=w^2+1/4,
   U_0=e^(t/4)S, the binomial transport to D_m, and the v^(a+1)/(a+b)!
   factor in the mixed integral.
2. **The explicit count.** Check the classical argument-principle identity
   with its argument path, the f_T Jensen bound, the entire horizontal
   segment, the Euler--Maclaurin remainder and the Gamma remainder. The
   Gamma bound includes BOTH 1/(12z) and the periodic-Bernoulli integral;
   omitting the former is not authorized. Check right-limit conventions.
3. **The saddle proof's uniformity.** Check complex log-concavity only on
   x>=|eta|, the shifted saddle r_eta, the Gaussian envelope factor 2,
   the j<=100 and j>=100 phase cases, and the cancellation in (18).
4. **The complete complement.** Check interval counts and all exterior
   bands k>=5, not a finite list of bands. The geometric tail has its
   factor 8, and the core lower mass uses a separate factor 1/16.
5. **Finite height versus unbounded order.** The small-time theorem uses
   V100 only; the global 10^15-depth application additionally uses the
   full published V_(3*10^12). No simplicity is needed. Verify both
   overlap inequalities; do not interpret the corollary as unbounded b.
6. **Late time.** The factor (1+H^-2)^m stays in the estimate for arbitrary
   m. It is bounded by 2 ONLY in the separate m<=27 theorem.
7. **Growth theorem.** Check coefficient-column stochasticity in degree
   elevation; absolute convergence; attainment of R>1; finiteness and
   distinctness of the maximal mu's; the uniform smaller-rate remainder;
   and why monotonic V_n upgrades a block maximum to a full root limit.
8. **Source endpoint.** Check the Laguerre convention and Mobius factors.
   The L2 source estimate exp(o(n)) is NOT claimed. A spectral identity
   or a generating function does not prove its unit-disk analyticity.

## Proof-level versus executable evidence

The new checker uses only Fraction and an explicit exact Q(i) class. Its
checks remain active under -O. It verifies constants and finite algebra,
not integrals, Jensen, Riemann--von Mangoldt, an infinite tail theorem,
external zero verification, or RH. Its Gaussian-band and incomplete-gamma
fixtures corroborate the general inequalities proved in the text; they do
not establish the unbounded quantifiers by finite sampling.

The parent's interval Gamma computation is an explicit software dependency.
The new checker itself has no interval or special-function dependency.
The published large zero verification is imported and was not rerun.

## Falsifiers and scope boundaries

A flaw in the count remainder, a missing complex saddle phase, or an unpaid
exterior band would invalidate the new all-order small-time theorem and its
10^15-depth corollary. The separate 27-layer proof would not automatically
fall with that theorem, because it uses only the parent's N(T)<=T^2 bound.
A flaw in the Vandermonde/gap argument would invalidate the exact growth
claim without changing the heat-sign proofs.

The old positive-Bernstein-log polynomial control still has H_(0,14)<0.
It is not a zeta counterexample: it lacks the required zeta count and verified
prefix. A passing finite fixture may not be used to infer the final target.

No external novelty assessment has been completed. Classical ingredients
are credited; do not promote a new arrangement of those ingredients to a
priority claim without specialist literature review.
