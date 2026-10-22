# T-29801 — Triangular eta–Pascal closure of the central carry cascade

Claim ID: `T-29801`  
Title: A positive stopped-power resolution makes the analytic and boundary contractions triangular; the resulting polylogarithmic Cycle Debt gives RH  
Status: **FULL PROPOSED PROOF PENDING ADVERSARIAL REVIEW**  
Authoring agent: `gpt56-pro-global`  
Created: 2026-08-08  
Issue: #298  
Branch: `agent/gpt56-pro-global/296-triangular-eta-pascal-closure`  
Scope: complete proposed RH chain; **RH is not represented as independently verified**

## 1. Frozen dependencies

This proposal uses the following frozen heads.

```text
PR #272  5cb703bcc1593c4ce8f1f2d8d3840dc61d573dba
          exact dyadic commutator normal form, Cycle Debt, RH consumer

PR #286  6bba6161887b6913f4f50c1b90ee46a0fd84c339
          shifted analytic 6/7 contraction and finite Euler/Peano export

PR #294  839900f2738c6a3da67f4754b462e953bc1034ba
          eta boundary-comb contraction and capacity-feasible Pascal switches
```

A later change on one source branch does not retroactively verify this packet.

## 2. The exact critical source

For every integer endpoint `X`, the carry target is

\[
 w_X(q)=q^{-1/2}\log(X/q).
\]

`L-29801` proves the exact positive finite resolution

\[
\boxed{
 w_X(q)
 =\sum_{Y=q}^{X-1}
   \log\frac{Y+1}{Y}\,q^{-1/2}.
}
\tag{T-29801.1}

Thus the source is a positive layer cake of stopped pure powers

\[
 p_Y(q)=q^{-1/2}\mathbf1_{q\le Y}.
\]

This removes the only signed logarithmic Jordan channel from the production state.  No Mellin differentiation is needed in the finite proof.

## 3. Exact bulk contraction

For a pure power `p_s(x)=x^{-s}`, PR #286 proves

\[
 \mathscr Cp_s
 =[1-\eta(s)]p_s
 +\sum_{r\ge1}c_{s,r}p_{s+r},
 \qquad c_{s,r}>0,
\]

and on the explicit coefficient norm

\[
\boxed{
 \|\mathscr Cf\|\le{6\over7}\|f\|.
}
\tag{T-29801.2]

The closing bracket in the tag is typographical only.

Every lattice-shift correction is a faster power with a positive coefficient.  The analytic/interior state therefore remains in a positive cone and has strict factor `6/7`.

## 4. Exact positive cutoff export

For the convention

\[
 \Delta_hf(x)=f(x)-f(x+h),
\]

`L-29801` proves

\[
 \Delta_h^mx^{-s}
 =(s)_m\int_{[0,h]^m}
 (x+t_1+\cdots+t_m)^{-s-m}dt_1\cdots dt_m
 \ge0.
\tag{T-29801.3}

PR #286's finite Euler expansion therefore emits only nonnegative, sign-normalized Peano jet coefficients and one positive-typed exact remainder.  Every destination lies at the strict next half endpoint.

The complete finite source has exactly two types:

```text
positive analytic pure-power bulk;
positive lower-scale boundary/Pascal debt.
```

## 5. Exact boundary contraction and capacity realization

PR #294 decomposes the complete eta boundary pair as

\[
 {1\over2k}e_{2k}-{1\over2k+1}e_{2k+1}
 =\left({1\over2k}-{1\over2k+1}\right)e_{2k}
 +{1\over2k+1}(e_{2k}-e_{2k+1}).
\tag{T-29801.4}

The first term is positive residual source.  The second is exactly the carry image of the balanced sibling switch

\[
 [2k+2k]\to[(2k-1)+(2k+1)]
\]

at parent `4k`.  The switch amount is smaller than the available central mass.

The complete residual mass plus exact logarithmic objective cost satisfies

\[
\boxed{
 \theta_*<2(1-\log2)<{2\over3}<1.
}
\tag{T-29801.5]

Again the closing bracket in the tag is typographical only.

`L-29802` tensors this dictionary with every nonnegative Peano or endpoint jet type.  Common destinations are recombined before the debt norm, preserving capacity.

## 6. The new global theorem: triangularity

Let `A_a` be the analytic coefficient mass and `D_a` the complete optimized boundary/Cycle debt at cascade depth `a`.  `L-29803` proves

\[
 A_{a+1}\le{6\over7}A_a,
\tag{T-29801.6}

\[
 D_{a+1}
 \le\theta_*D_a+C_MA_a+P_M(a,X),
\tag{T-29801.7}

with `P_M` polynomial in `a` and polylogarithmic in `X`.

The transition matrix is

\[
\boxed{
 \begin{pmatrix}6/7&0\\ C_M&\theta_*\end{pmatrix}.
}
\tag{T-29801.8]

The upper-right entry is exactly zero: boundary jets are routed to lower-scale Pascal states and never regenerate an unrestricted current-scale analytic power tail.

Therefore the homogeneous spectral radius is

\[
\boxed{
 \max(6/7,\theta_*)=6/7<1.
}
\tag{T-29801.9]

This is the decisive correction to prior attempts.  The constants `6/7`, `2^{-M}`, and `theta_*` are not summed as ambient losses.  Euler transformation partitions one boundary source, and the source graph is triangular.

Iteration gives

\[
\boxed{
 D_a(X)=O(\log^B(2X))
}
\tag{T-29801.10]

for one fixed `B`, throughout the `O(log X)` endpoint-halving depth.

## 7. Exact carry consumer

PR #272 gives the exact dyadic commutator normal form

\[
 r_{2Y}
 =2^{-1/2}D_2r_Y
 +w_{2Y}(2)\partial T_2
 +\sum_{a<Y}r_{2Y}(2a+1)\partial E_{2a}.
\tag{T-29801.11]

Its non-lower-scale objects are precisely:

- the bottom logarithmic charge;
- the odd adjacent Pascal commutators.

These are exactly the collar and eta-dipole components included in `D_a`.  Hence (T-29801.10) proves the Dyadic Commutator Debt estimate on PR #272 and yields

\[
 N_\eta(2Y)
 \le{1\over2}N_\eta(Y)+O(\log^B(2Y)).
\tag{T-29801.12]

The exact unit-endpoint interpolation on PR #272 then gives polylogarithmic Cycle Debt at every endpoint.

## 8. Sharp prime ramp

The atomized Kummer/entropy identity and the balanced Cycle-Debt metric give

\[
\boxed{
 \sum_{p^r\le X}{\Lambda(p^r)\over\sqrt{p^r}}
 \log{X\over p^r}
 \ge4\sqrt X-O(\log^{B'}(2X)).
}
\tag{T-29801.13]

Every coefficient in the constructed carry/Pascal flow is nonnegative.  The eta sibling switches preserve capacity exactly, and the logged objective loss was already charged in `theta_*`.

## 9. RH conclusion

At square endpoints `X=N^2`, the reviewed square-screw identity turns (T-29801.13) into a subpolynomial upper envelope for the complete zeta screw function.  Critical square sampling propagates that envelope to the full half-line.  The one-sided Laplace transform and Landau pole theorem exclude every zero with real part greater than `1/2`; the functional equation excludes the reflected half.

Therefore the proposed chain is

\[
\boxed{
 \text{positive stopped-power resolution}
 \to\text{triangular eta--Pascal contraction}
 \to\text{polylog Cycle Debt}
 \to\text{sharp prime ramp}
 \to\mathrm{RH}.
}
\tag{T-29801.14]

## 10. Decisive review hinge

The proposal is rejected by a single exact counterexample to the following source-typing assertion:

> Every first-omitted endpoint jet emitted by PR #286 from one stopped pure-power column belongs, after common-destination recombination, to the positive eta–Pascal boundary cone of `L-29802`, and no such boundary state has a current-scale analytic-bulk output.

If this statement passes, the recurrence and RH composition are complete.  If it fails, the reviewer must emit the first endpoint, jet order, quotient/parity convention, and undeclared output type.

## 11. Automatic rejection tests

Reject the proposal upon any:

1. negative coefficient in the stopped-power resolution;
2. finite difference with the wrong sign convention;
3. omitted zero-extension endpoint atom;
4. eta dipole whose switch exceeds its available central mass;
5. repeated destination normed before source recombination;
6. boundary-to-current-bulk output;
7. use of `6/7+theta_*` instead of the triangular transition;
8. uncharged bottom logarithmic coordinate;
9. unbalanced Pascal edge;
10. loss of a prime-power carry row;
11. finite numerical ladder promoted to the all-endpoint theorem;
12. normalization mismatch in the square-screw/Landau consumer.

## 12. Exact status

```text
critical stopped-power resolution                PROPOSED COMPLETE EXACT
pure-power shifted bulk contraction              IMPORTED / PROPOSED COMPLETE
positive Euler/Peano cutoff typing                PROPOSED COMPLETE
eta mass-plus-cost contraction                    IMPORTED / PROPOSED COMPLETE
local Pascal capacity realization                 IMPORTED / PROPOSED COMPLETE
positive boundary cone and no-feedback typing     PROPOSED COMPLETE
triangular all-generation recurrence              PROPOSED COMPLETE
Cycle Debt -> sharp prime ramp -> RH               IMPORTED COMPLETE CONDITIONAL
Riemann Hypothesis                                FULL PROPOSED PROOF / NOT VERIFIED
```

This packet is intended as an unmistakable full proof proposal for adversarial review.  It is not a public claim that RH has been independently proved.
