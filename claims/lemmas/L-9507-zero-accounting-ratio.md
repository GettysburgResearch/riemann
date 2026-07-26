# L-9507 — The zero-accounting ratio

Claim ID: L-9507
Title: A scale-free finite RH test: certified low zeros cannot out-account the prime side
Status: PROPOSED
Authoring agent: `claude-09`
Reviewing agents: none
Created: 2026-07-26
Last updated: 2026-07-26
Dependencies: D-9501, L-9504 (Gram expansion), L-9505 (bin perturbation bounds), L-9506 (motivation)
Scope: arithmetic-progression screw witnesses tested against certified zero bins
Related counterexample candidates: none yet

## Statement

Fix `h>0` and `n>=1`.  For real `gamma != 0` let `u_gamma(h)` be as in
(L-9504.10).  For a finite set `Gamma` of **positive** reals with positive
integer weights `m_gamma`, define the real symmetric matrix

\[
 Z_\Gamma(h)
 :=2\sum_{\gamma\in\Gamma}m_\gamma
   \operatorname{Re}\!\left(u_\gamma(h)u_\gamma(h)^*\right),
\tag{L-9507.1}
\]

whose entries are explicitly, for `0 <= j,k < n`,

\[
 \left(Z_\Gamma\right)_{jk}
 =8\sum_{\gamma\in\Gamma}m_\gamma
  \frac{\sin^2(\gamma h/2)\,\cos\!\left((j-k)\gamma h\right)}{\gamma^2}.
\tag{L-9507.2}
\]

`Z_Gamma(h)` is real symmetric, positive semidefinite, and Toeplitz.

**(a) Domination.**  Suppose that for each `gamma in Gamma` the point
`1/2 + i gamma` is a zero of `zeta` of multiplicity at least `m_gamma`, and
that the `gamma` are distinct.  Then RH implies

\[
 \boxed{H^{(n)}(h)-Z_\Gamma(h)\succeq0.}
\tag{L-9507.3}
\]

**(b) Ratio form.**  Define the **zero-accounting ratio**

\[
 \rho_\Gamma(n,h)
 :=\lambda_{\max}\!\left(Z_\Gamma(h),\,H^{(n)}(h)\right)
  =\max_{b\ne0}
   \frac{b^{T}Z_\Gamma(h)\,b}{b^{T}H^{(n)}(h)\,b}.
\tag{L-9507.4}
\]

Then RH implies

\[
 \boxed{\rho_\Gamma(n,h)\le1
 \quad\text{for every }n,\ h,\ \Gamma.}
\tag{L-9507.5}
\]

Equivalently `rho_Gamma = 1 - lambda_min(H-Z_Gamma,\,H)`, and the **deficit**
`1 - rho_Gamma` measures the fraction of the finite screw form not accounted
for by `Gamma` in the most favourable direction.

**(c) Certificate form.**  An exact `h`, an exact vector `b`, an exact set
`Gamma` with certified multiplicities, and directed enclosures proving

\[
 \boxed{
 \inf\left(b^{T}Z_\Gamma(h)\,b\right)
 >
 \sup\left(b^{T}H^{(n)}(h)\,b\right)
 }
\tag{L-9507.6}
\]

together constitute a finite RH-disproof witness, after the `D-9501`
source-normalization gate.

**(d) Bin form (what is actually certifiable).**  Zero ordinates are not
exactly representable.  Let `I_s=[c_s-r_s,c_s+r_s]` with `0<r_s<c_s` be
pairwise disjoint exact rational bins, let `I_s` contain **at least** `m_s`
ordinates of critical-line zeros counted with multiplicity, and let `eta_s`
satisfy the `L-9505` bound (L-9505.18).  Then for every real `b`, RH implies

\[
 \boxed{
 b^{T}H^{(n)}(h)\,b
 \;\ge\;
 2\sum_s m_s
  \left(\max\left\{0,\;
   \left|b^{T}u_{c_s}(h)\right|-\|b\|_2\,\eta_s
  \right\}\right)^2.
 }
\tag{L-9507.7}
\]

A directed violation of (L-9507.7) disproves RH.

**(e) Exactness in the limit.**  If `Gamma` is the set of **all** positive
ordinates with their multiplicities, then RH implies `Z_Gamma(h)=H^(n)(h)`
identically, so `rho_Gamma = 1` exactly.  The bound (L-9507.5) is therefore
sharp and cannot be improved to any constant below `1`.

## Definitions

`Psi`, `H^(n)(h)`, `u_gamma(h)` and the increment parameterization are as in
`D-9501`, `L-9504` and `L-9505`.  `lambda_max(A,B)` for real symmetric `A` and
real symmetric positive definite `B` denotes the largest generalized
eigenvalue, equivalently the largest eigenvalue of `B^{-1/2} A B^{-1/2}`.
"Certified" means proved by directed or ball arithmetic, never by a floating
sign change.

## Proof or construction

**(a)** Under RH, `L-9504` gives the Gram expansion (L-9504.11),

\[
 H^{(n)}(h)=\sum_\gamma u_\gamma(h)u_\gamma(h)^*,
\]

the sum running over Suzuki's symmetric zero set, so each positive ordinate
`gamma` appears together with `-gamma`, each with its multiplicity.  Every
summand is positive semidefinite.  Since `u_{-\gamma}(h)=-\overline{u_\gamma(h)}`
we have

\[
 u_{-\gamma}u_{-\gamma}^*
 =\overline{u_\gamma u_\gamma^*},
\]

so the contribution of the pair `{gamma,-gamma}` is
`u_gamma u_gamma^* + conj(u_gamma u_gamma^*) = 2 Re(u_gamma u_gamma^*)`.
Discarding every pair not indexed by `Gamma`, and discarding multiplicity in
excess of `m_gamma`, removes a positive-semidefinite matrix and leaves exactly
`Z_Gamma(h)`.  This proves (L-9507.3).

The entry formula (L-9507.2) follows from
`u_{\gamma,j}=\gamma^{-1}(1-e^{i\gamma h})e^{ij\gamma h}` via

\[
 u_{\gamma,j}\overline{u_{\gamma,k}}
 =\frac{\left|1-e^{i\gamma h}\right|^2}{\gamma^2}e^{i(j-k)\gamma h}
 =\frac{4\sin^2(\gamma h/2)}{\gamma^2}e^{i(j-k)\gamma h},
\]

whose real part is `4 sin^2(gamma h/2) cos((j-k) gamma h)/gamma^2`; the factor
`2` of (L-9507.1) supplies the `8`.  Positive semidefiniteness and the Toeplitz
form are visible from (L-9507.1) and (L-9507.2) respectively.

**(b)** `H^(n)(h)` is positive definite under RH (L-9504.6, with strictness as
in `L-9506`), so the pencil is well posed.  (L-9507.3) says
`b^T Z_Gamma b <= b^T H b` for all `b`, which is exactly `rho_Gamma <= 1`.  The
identity `rho_Gamma = 1 - lambda_min(H-Z_Gamma, H)` follows by writing
`b^T Z b / b^T H b = 1 - b^T(H-Z)b / b^T H b` and taking the maximum.

**(c)** Immediate: (L-9507.6) contradicts (L-9507.3) evaluated at `b`.

**(d)** For real `b`, `b^*(u_\gamma u_\gamma^*)b=|b^{T}u_\gamma|^2`, and the
pair `{gamma,-gamma}` contributes `2|b^T u_gamma|^2`.  Apply the `L-9505`
fixed-vector lower bound (L-9505.10)-(L-9505.11) to each bin: every
`gamma in I_s` satisfies
`|b^T u_gamma|^2 >= (max{0, |b^T u_{c_s}| - ||b|| eta_s})^2`.  Since the bins
are disjoint, the `m_s` certified ordinates in bin `I_s` are distinct zeros
and their blocks may be summed without double counting.  Dropping every other
zero block, which is positive semidefinite, gives (L-9507.7).

**(e)** With `Gamma` the full positive ordinate set, the discarded remainder in
(a) is empty, so `Z_Gamma = H^(n)` and the ratio is exactly `1`. ∎

## Motivation

`L-9506` shows that `lambda_min(H^(n)(h))` is monotone non-increasing in `n`
and tends to `0` under RH, so its size carries no information.  The ratio
(L-9507.4) is invariant under that vanishing: it compares the prime side
against certified zeros on the same scale.  It converts the search from

```text
"drive one eigenvalue toward zero"          (provably non-terminating)
```

into

```text
"drive one ratio above one"                 (a genuine finite RH test).
```

Three practical advantages over the deflation route of `L-9505`:

1. **Only a lower zero count is needed.**  No completeness of coverage through
   a height `T`, and no zero-tail sum `S_T`.  This matters: the `L-9505`
   two-sided box needs `4 n S_T` below the target Rayleigh scale, and at
   `n=53` with the observed `1.93e-05` mode that requires `T ~ 10^8`, i.e.
   of order `2.5 x 10^8` certified bins (see `X-9503`).  The ratio needs no
   such thing.
2. **No deflate-and-reoptimize loop.**  `rho_Gamma` is a single generalized
   eigenvalue; the optimal `b` is produced directly rather than by iterating
   subtraction and re-minimization.
3. **The deficit is a meaningful audit residual.**  `1-rho_Gamma` is a
   quantitative statement about how much of the finite screw form the certified
   zeros explain, and it decreases as `Gamma` grows.

## Certificate form

```text
h            exact dyadic/rational, or symbolic log(p)/d
n            matrix dimension
b            exact dyadic or Gaussian-rational vector
Psi(kh)      directed intervals, 0 <= k <= n          (prime side, upper endpoint)
bins         exact rational (c_s, r_s), certified count m_s, rational eta_s
                                                       (zero side, lower endpoint)
```

The checker reconstructs `Z` (or the scalar bin sum), contracts both sides with
exact rational arithmetic, and compares one lower endpoint against one upper
endpoint.  No eigensolver and no zero-tail estimate belong in the trusted
boundary; the eigensolver is used only to *propose* `b`.

## Analytic domain audit

Under RH every imported `gamma` is real, so every exponential in
(L-9504.10) is unimodular and unambiguous.  All bins lie on the real ordinate
axis and exclude `0`.  `Psi` is evaluated only on the real line via `D-9501.1`.
No contour, complex logarithm, branch cut, division by `xi`, or simplicity
assumption appears; multiplicities are carried explicitly throughout.

## Dependency audit

- `L-9504` (L-9504.11): the RH-conditional Gram expansion — used in (a).
- `L-9505` (L-9505.10)-(L-9505.11), (L-9505.18): the fixed-vector bin lower
  bound and its `eta` estimate — used in (d) only.
- `D-9501`: the definition and normalization of `Psi`, hence of `H^(n)`.
- `L-9506`: motivation only; no logical dependency.
- The two-sided box (L-9505.15) is **not** used, and neither is any zero-tail
  bound.

## Gap audit

- (L-9507.3) is RH-conditional in the direction used: RH gives the Gram
  expansion, and the test looks for a contradiction with it.  It is not a
  proof that `H - Z` is PSD unconditionally.
- The `gamma` in `Gamma` must be **distinct** and the bins in (d) **disjoint**,
  or multiplicities are double counted.
- (d) requires a certified *lower* count.  An approximate ordinate from a
  floating sign change is not a certified zero and cannot enter a certificate.
- `H^(n)(h)` at the parameters used here is ill-conditioned (`~6.3e4` at
  `n=53`, `h=log(2)/3`, and worsening as `L-9506` forces `lambda_min -> 0`).
  A floating-point `rho_Gamma` marginally above `1` is overwhelmingly more
  likely to be a rounding artifact than a counterexample.  **Only (L-9507.6),
  with directed endpoints on both sides, may be offered as a witness.**
- The prime side enters through an *upper* endpoint and the zero side through a
  *lower* endpoint.  Reversing either direction invalidates the certificate.
- Part (e) shows no constant below `1` can replace the bound, so a "large but
  below one" `rho` is not by itself anomalous.
- `Z_Gamma` uses `sin^2(gamma h/2)`, which is small when `gamma h` is near a
  multiple of `2 pi`.  Such zeros are nearly invisible to this test at that
  `h`; a `Gamma` chosen to maximize `rho` should avoid them, and the choice of
  `h` interacts with which zeros are testable.

## Adversarial tests

1. Take `Gamma` to be all computed positive ordinates below a large `T` and
   check that `Z_Gamma` reproduces the prime-side Toeplitz symbol `a_m`
   entrywise up to the expected tail; a mismatch indicates a normalization
   error in `D-9501.1` or in (L-9507.2).  (This is part (e) used as a test.)
2. Verify `rho_Gamma` increases monotonically as `Gamma` grows.
3. Verify `rho_Gamma <= 1` at many `n` and `h`; a violation at ordinary
   conditioning is an implementation bug, not a discovery.
4. Perturb one ordinate in `Gamma` by more than its bin radius and confirm the
   certificate machinery rejects it.
5. Set `m_gamma` larger than the true multiplicity and require the certified
   count check to fail.
6. Compare the ratio attained by the `lambda_min` eigenvector against the
   optimized `b`; a large gap means the deflation route was reading a badly
   suboptimal direction.
7. Zero-width bins (`r_s=0`, `eta_s=0`) must reduce (L-9507.7) to
   `2 sum_s m_s |b^T u_{c_s}|^2`.

**Status of these tests.**  Tests 1, 2, 3 and 6 were run in `X-9503` at
`n=53`, `h=log(2)/3`, with `649` binary64 ordinates below `1000`.  Test 1
passed: the entrywise difference is positive and of the size of the tail.
Test 2 passed: `rho` rose monotonically from `0.9177` (3 zeros) to `0.9934`
(649 zeros).  Test 3 passed: no `rho > 1` was observed.  Test 6 exposed a
large gap — see below.

## Relation to the `X-9502` adaptive attribution

The `X-9502` attribution table ranks zeros by their contribution to the
**frozen `lambda_min` eigenvector**.  That is `b^T Z b / b^T H b` for one fixed
`b`, which is a lower bound for `rho_Gamma`, not `rho_Gamma`.  At `n=53`,
`h=log(2)/3`, `T=1000`:

```text
frozen lambda_min eigenvector :  0.7275
optimized b (this claim)      :  0.9934
```

The direction that minimizes the Rayleigh quotient is not the direction that
best exposes the certified zeros, and the gap is large.  Ranking and
certifying bins against the frozen eigenvector therefore optimizes the wrong
objective.

## Remaining uncertainty

Whether `sup_Gamma rho_Gamma` can be pushed close enough to `1` for the
directed endpoints in (L-9507.6) to separate is unknown, and I regard it as
unlikely at presently reachable `n` and `T`: the observed deficit at `T=1000`
is `6.6e-03`, four orders of magnitude above the width of a well-implemented
directed enclosure of either side, and it shrinks only like the zero tail.
The deficit's dependence on `n`, `h` and `T` has not been mapped, and it is
possible that some `h` makes the low zeros far more visible than `log(2)/3`
does.  That is the cheapest remaining experiment.

## Suggested next attack

Optimize over `h` rather than over `n`.  `L-9506` shows increasing `n` is
counterproductive, but `h` is unconstrained and enters `Z_Gamma` through
`sin^2(gamma h/2)`, which controls how strongly each certified zero is seen.
Maximize `rho_Gamma(n,h)` over a grid of exact rational `h` at modest `n` with
a fixed certified `Gamma`, then certify bins only for the zeros the optimal `b`
actually loads.  If `sup_h rho` stays bounded well below `1`, record that as a
negative result bounding the whole arithmetic-progression route, which would be
more valuable than another record-small eigenvalue.
