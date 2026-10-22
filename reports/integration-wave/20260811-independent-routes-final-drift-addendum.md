# Final live-head drift addendum: independent routes

**Applies after:** `reports/integration-wave/20260811-independent-routes-review.md`  
**Final drift check:** performed after publishing the first review commit  
**Base/main:** unchanged at `d6409319b4041cd09bee85f55a344631508f2501`

## PR #368 moved during publication

The initial #368 review was frozen at

`0de8f97f37617c050534c242ee3761af15b87a97`.

The final live-head check observed

`f6951a6bdb78a0778ca4b62e816c4c0a715ade0f`.

The newer head was re-reviewed. This addendum supersedes the #368 rows and conclusions in the original status table wherever they differ.

## What changed

The newer head retains the corrupted `T-90502` blob but adds a load-bearing pole-sign correction and two cleaner Fredholm completions:

1. `R-90501` proves that the explicit-formula pole contribution is the hyperbolic cross block `[[0,1],[1,0]]`, not two positive diagonal squares.
2. Corrected `L-90506` gives one forced negative pole direction, `n_-(Q)=q+1`, and pole-null index `q`, where `q` is the number of distinct reflected off-line pairs.
3. `L-90508/T-90503` construct an intrinsic pole-null Darboux-Sobolev completion using the multiplier `z^2+1/4=s(1-s)`.
4. `L-90509/T-90504` add the unique trace-minimal rank-one positive completion of the hyperbolic pole block and obtain an unconstrained Fredholm criterion.

## Review verdicts at the newer head

### R-90501 — hyperbolic pole correction

**VERIFIED**, `REFUTATION`.

With the repository's Hermitian Fourier convention,

`P(f,g)=fhat(i/2) overline(ghat(-i/2)) + fhat(-i/2) overline(ghat(i/2))`.

Thus the pole matrix is hyperbolic. The exact mutation `(a,b)=(1,-1)` gives pole value `-2`, whereas the rejected diagonal-square model gives `+2`.

This correction is load-bearing for the local pole-index programme. It does not refute the upstream Zeta23 headline theorem, whose main argument estimates the pole-density terms rather than using pole-block positivity.

### Corrected L-90506 — index-one pole shift

**VERIFIED WITH FIXES**, `UNCONDITIONAL THEOREM`.

The pole cardinals, hyperbolic plane, pole-null correction of off-line Xi cardinals, and index formulas are coherent. Required wording fix: the Fredholm determinant has `q` positive zeros **counted with multiplicity**; coincident negative eigenvalues need not give `q` distinct locations.

### L-90508 / T-90503 — intrinsic Darboux completion

**VERIFIED WITH FIXES**. The completion lemma is an `UNCONDITIONAL THEOREM`; the positivity/Fredholm/heat/Hankel closure is an `RH-EQUIVALENT CRITERION`.

The Green kernel for `D=partial_u^2-1/4`, the pole-null range condition, evaluation kernel, diagonal decay, prime-shift trace-norm summability, and capture of super-Gaussian Xi cardinals check out. The all-order word language must include the archimedean continuum operator, not only discrete prime words.

The equivalences

- `A>=0`;
- `det(I+tA)>0` for every `t>0`;
- `tr(e^{-beta A}-I)<=0` for every `beta>0`;
- `tr(A e^{-beta A})>=0` for every `beta>0`;
- positivity of every shifted moment Hankel matrix

are valid for the self-adjoint trace-class operator. No closing sign is proved.

### L-90509 / T-90504 — rank-one positive completion

**VERIFIED WITH FIXES**. The completion lemma is an `UNCONDITIONAL THEOREM`; the Fredholm closure is an `RH-EQUIVALENT CRITERION`.

In the diagonal pole basis, adding the negative-line square is the unique PSD completion of minimum trace. Corrected off-line cardinals can be placed in the kernel of that square, so the completed form retains exactly one negative direction per distinct reflected off-line pair. The same spectral-calculus wording fix about determinant zeros counted with multiplicity applies.

This is the cleanest unconstrained local operator criterion at the final reviewed head, but the prime-side positivity/heat-pressure theorem remains open.

### L-90507 — Levy/heat formulation

**VERIFIED WITH FIXES**, `RH-EQUIVALENT CRITERION`.

The digamma Levy representation, physical jump form, heat-trace amplification, and spectral equivalences are sound. The modulus inequality applies to the pole-free form on its natural form domain, but absolute value does not preserve the pole-null constraints. The global expansion must retain both the archimedean continuum contribution and the discrete prime adjacencies.

### T-90502 — corrupted original theorem artifact

**SUPERSEDED** by `T-90503` and `T-90504`; do not integrate.

The blob remains `f5bbc2392327b965a278917076c470f7eb15f359` and remains binary-corrupted/invalid UTF-8. The newer clean theorem files remove the need to reconstruct this artifact as the canonical front door.

## Revised operator-route frontier

The final #368 head strengthens the analytic infrastructure but does not change the RH verdict. The live first theorem is one of the equivalent prime-side signs for either the intrinsic Darboux operator or the rank-one completed operator. In particular, prove for every positive heat parameter that the corresponding relative heat trace is nonpositive, or prove the equivalent Fredholm positivity.

## Final movement record

- #364: first `219330bd0441a284fd16ff728dd843a7ee4503ee`; final/re-reviewed `46caa771ad2ab7875c3ccd079d3ba327249fd9a4`.
- #368: first `0de8f97f37617c050534c242ee3761af15b87a97`; final/re-reviewed `f6951a6bdb78a0778ca4b62e816c4c0a715ade0f`.
- #367 remained `2a725fb71794dfca11e76c1af2a49e6b3ea8bc9c`.
- `main` remained `d6409319b4041cd09bee85f55a344631508f2501`.

No heavy computation or Lean build was rerun during this drift reconciliation.
