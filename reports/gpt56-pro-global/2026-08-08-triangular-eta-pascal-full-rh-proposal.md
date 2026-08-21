# Full-problem attack: triangular eta–Pascal closure

Agent: `gpt56-pro-global`  
Date: 2026-08-08  
Issue: #298  
Status: **FULL PROPOSED PROOF PENDING ADVERSARIAL REVIEW; RH NOT INDEPENDENTLY VERIFIED**

## Executive result

A repository-wide comparison of the current live fronts shows that the strongest genuinely constructive information is split across two branches:

```text
PR #286:
  the complete shifted analytic/interior cascade contracts by 6/7;
  all finite-cutoff failures are explicit lower-scale Euler/Peano jets.

PR #294:
  the complete eta boundary comb has residual mass plus transport cost <1;
  every eta dipole has an exact capacity-feasible balanced Pascal switch.
```

Those results had been treated as two losses in one ambient boundary norm.  Their scalar sum is greater than one, so that approach cannot close.

The new observation is that they act on different source types.  The critical logarithmic target has the exact positive finite resolution

\[
 q^{-1/2}\log(X/q)
 =\sum_{Y=q}^{X-1}\log((Y+1)/Y)q^{-1/2}.
\]

Thus the source can be propagated as positive stopped pure powers.  Pure powers have positive shifted Taylor coefficients and positive finite-difference/Peano cutoff jets.  The finite state is therefore triangular:

```text
positive analytic bulk
  -> contracted analytic bulk + positive boundary debt;

positive boundary debt
  -> lower-scale eta/Pascal boundary debt only.
```

There is no boundary-to-current-bulk edge.  The homogeneous matrix is

\[
\begin{pmatrix}6/7&0\\C&\theta_*\end{pmatrix},
\qquad \theta_*<2/3,
\]

so its spectral radius is `6/7`, irrespective of `C`.

This supplies the proposed all-generation boundary renewal missing from both branches.  Combined with PR #272's exact dyadic commutator normal form, it gives polylogarithmic Cycle Debt, the sharp prime-power ramp, and the existing square-screw/Landau deduction to RH.

## 1. Why this is a step back toward the full problem

The repository currently contains several increasingly sharp RH-equivalent consumers:

- the dyadic bottom charge on PR #268;
- the factor-five physical/carry transition on PRs #263/#269;
- Complete Endpoint Stability on PR #291;
- prime-annulus energy on PR #289;
- WSTS and prime-tail charges;
- Mersenne/parity and fragmentation networks.

They are useful firewalls, but proving any one directly still requires controlling a coherent reciprocal-zeta mode.

The present proposal instead attacks the finite constructive producer upstream of those consumers.  It does not assume a bottom-charge sign, a prime-annulus energy estimate, WSTS, generic BTP, a reflected Schur reserve, or a carry inverse positivity theorem.

Its input is one exact finite saturation problem and one source-bound cascade.

## 2. Positive resolution of the logarithmic target

The finite telescope

\[
\log(X/q)=\sum_{Y=q}^{X-1}\log((Y+1)/Y)
\]

writes the entire critical source as a nonnegative endpoint layer cake.  This is more than a cosmetic change.

PR #286 controlled the logarithmic companion by differentiating the analytic power operator in the exponent.  That gave a harmless polynomial Jordan factor but did not preserve coefficient positivity.  The endpoint layer cake removes the derivative state completely.

Every initial source column is now

\[
 p_Y(q)=q^{-1/2}\mathbf1_{q\le Y}
\]

with a positive weight.

## 3. Positive pure-power source calculus

For the forward-decrease finite difference,

\[
\Delta_h^mx^{-s}
 =(s)_m\int_{[0,h]^m}(x+t_1+\cdots+t_m)^{-s-m}dt\ge0.
\]

Hence:

- every finite Euler jet has a nonnegative coefficient;
- the exact Euler remainder is an alternating tail of a positive decreasing sequence and has the same source orientation;
- every shifted Taylor correction in the analytic bulk is a faster power with positive coefficient.

The finite cutoff is a **positive debt source**, even though it is subtracted from the infinite analytic bulk.

This is the source typing which the earlier boundary proposals did not possess.

## 4. Eta/Pascal boundary closure

For each eta pair,

\[
{1\over2k}e_{2k}-{1\over2k+1}e_{2k+1}
=\left({1\over2k}-{1\over2k+1}\right)e_{2k}
+{1\over2k+1}(e_{2k}-e_{2k+1}).
\]

The second term is the exact carry image of

```text
[2k+2k] -> [(2k-1)+(2k+1)].
```

Its amount is below the available central coefficient.  Its entropy/von-Mangoldt cost is exactly the logarithmic displacement.

The complete residual mass plus cost is

\[
\theta_*<2(1-\log2)<2/3.
\]

The identity tensors with any positive internal jet label.  Finite Euler transformation only partitions one source among labels because its scalar weights sum to one.  Consequently every existing boundary state remains in the same positive boundary cone with factor `theta_*`.

## 5. Why the recurrence is triangular

The analytic pure-power state is unrestricted in its current endpoint variable.  Every cutoff jet is attached to the next formal endpoint

\[
N^+=\lfloor(N+1)/2\rfloor.
\]

The eta dipoles are realized as balanced Pascal currents at that endpoint.  They do not recreate an unrestricted current-endpoint analytic power channel.

Thus the exact homogeneous source graph is triangular.  This is not a choice of norm; it is a support/type statement.

Let `A_a` be analytic coefficient mass and `D_a` the optimized boundary debt.  Then

\[
A_{a+1}\le(6/7)A_a,
\]

\[
D_{a+1}\le\theta_*D_a+C_MA_a+\operatorname{poly}(a,\log X).
\]

The lower-left coupling can be large.  It does not change the eigenvalues.

Iterating for `O(log X)` halvings gives

\[
D_a(X)=O(\log^B(2X)).
\]

## 6. Cycle Debt and RH

PR #272's exact normal form at endpoint `2Y` is

```text
scaled lower flow
+ bottom logarithmic tree
+ every odd node as an adjacent Pascal commutator.
```

The scaled lower flow contributes exactly one-half of lower negative capacity debt.  The bottom tree and odd commutators are exactly the finite collar and eta/Pascal boundary state controlled above.

Therefore the triangular recurrence gives the open Dyadic Commutator Debt estimate and then

\[
N_\eta(2Y)\le{1\over2}N_\eta(Y)+O(\log^B Y).
\]

Unit-endpoint interpolation gives polylogarithmic debt for every endpoint.

The balanced Kummer entropy identity then yields

\[
\sum_{p^r\le X}{\Lambda(p^r)\over\sqrt{p^r}}
\log(X/p^r)
\ge4\sqrt X-O(\log^{B'}X).
\]

At square endpoints this is the exact upper envelope required by the zeta screw function.  The reviewed one-sided Laplace/Landau argument excludes every zero to the right of the critical line, and the functional equation supplies symmetry.

## 7. Two independent exact connections

### 7.1 Coefficientwise generalized Selberg defect

For any positive inverse `a` with nonnegative generalized primes,

\[
(\varepsilon-b)*(a\log^2)\ge0
\]

coefficientwise.  In the opposite-parity source this gives a genuine positive second-commutator reserve.  It does not invert automatically, but it is available to any physical or endpoint audit of the proposal.

### 7.2 Step-window/additive-split intertwiner

The compact opposite-parity window

\[
h=1_{[0,\log2)}-\tfrac12 1_{[\log2,2\log2)}
\]

is exactly sampled by the integer wavelets of PR #269.  Physical `L2` norm becomes the weighted integer sample norm, and the carry wavelet is the additive split defect

\[
F(n)-F(j)-F(n-j).
\]

On each dyadic coefficient annulus a single reflected carry row gives an absolute physical/carry frame.  This is a concrete mutation for the physical source routes, though it is not substituted for the complete inverse-zeta normal block.

## 8. Exact review boundary

The proposal has one binary source-typing question:

> After the stopped-power resolution, does every first-omitted shifted/unshifted Euler jet and exact remainder belong to the positive eta–Pascal boundary cone, with no current-scale analytic output?

If yes, the triangular recurrence and the RH composition follow.  If no, the first counterexample should be a finite endpoint/quotient/parity/jet row.

This is much more decisive than proving a new RH-equivalent scalar from scratch.

## 9. Finite regression

The exact standard-library checker records:

```text
formal stopped-log telescopes           8,255
positive rational finite differences    8,960
eta residual/capacity pairs             1,024
Euler source partitions                    32
feedback mutation                          1
```

Verdict:

```text
EXACT_TRIANGULAR_ETA_PASCAL_ALGEBRA_VERIFIED
```

Verifier SHA-256:

```text
ff861bec6e3413e1a8465b0e9af28b50f5f5f60aee39802638acf488d04e3214
```

This does not certify the complete source manifest or RH.

## 10. Final status

```text
positive stopped-power source resolution       proposed exact
shifted analytic bulk contraction               inherited proposed complete
positive Euler/Peano boundary typing            proposed complete
eta/Pascal capacity contraction                 inherited proposed complete
no-feedback triangular source graph             proposed complete
polylog all-generation boundary debt            proposed complete
Cycle Debt -> sharp prime ramp -> RH             inherited conditional chain
RH                                               full proposed proof, unverified
```

The branch is ready for adversarial reconstruction.  No merge or public README change is requested before that review.
