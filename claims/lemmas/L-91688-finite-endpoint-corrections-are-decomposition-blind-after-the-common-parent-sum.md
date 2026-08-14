# L-91688 — The finite endpoint corrections are decomposition-blind after the common-parent sum

Claim ID: `L-91688`  
Status: **PROVED FORMAL COMPOSITION THEOREM ON EXPLICIT FROZEN ANALYTIC HYPOTHESES**  
Created: 2026-08-14  
Depends on: positive endpoint integration, `L-91110`, `L-91114`, `L-91115`, same-index functor  
RH status: **unproved**

## 1. Total endpoint measure

Let positive labelled endpoint measures be pushed to one common parent coordinate by positive linear maps:
\[
 \Lambda=\Lambda_0+\sum_b\Phi_b\Lambda_b.
\tag{L-91688.1}
\]
The labels retain provenance, but all physical response maps are evaluated on the single total measure `Lambda`.

Let `Q` be the positive martingale B-spline quantizer. Then
\[
 \boxed{
 Q\Lambda=Q\Lambda_0+\sum_bQ\Phi_b\Lambda_b.
 }
\tag{L-91688.2}
\]
The ordinary response at `q` and `4q`, every component row, target, and score commute with this sum. Radix-four equality is obtained only after the two ordinary equalities are formed.

## 2. Decomposition-blind correction operator

Let the finite realization of one total parent measure be
\[
 \boxed{
 \mathfrak F_X(\Lambda)
 =\sigma_{K_X}
 Q\!\bigl(\Lambda|_{[K_X+2,X-W-2]}\bigr)
 +\mathcal C_X(\Lambda),
 }
\tag{L-91688.3}
\]
where

```text
K_X=ceil(c0 X)+O(1);
W=10000;
sigma_K=(1+175/K)^(-1);
C_X is the single finite base/collar correction attached to the total row.
```

Restriction, pushforward, quantization, and the finite correction are applied to `Lambda` itself. They are not applied independently to its colors or recursive pieces.

Consequently the finite/continuum mismatch, safety loss, top omission, terminal taper, and common endpoint port each have one owner. Changing the positive decomposition of `Lambda` leaves the physical row `mathfrak F_X(Lambda)` unchanged.

## 3. Imported analytic bounds apply to the total row

Assume the total density lies in the exact positive corridor for which the frozen endpoint theorems prove:

\[
 \left|\mathcal D_4v_q(C_X-E_X)\right|
 <32q^{-3/2}+\frac{200}{q\sqrt K}
 \qquad(K\le q\le X/4),
\tag{L-91688.4}
\]

and the top omission removes more than the complete possible overfill on
\[
 X/4<q<X.
\tag{L-91688.5}
\]
Then the one total row (L-91688.3) satisfies
\[
 \boxed{
 \Xi_{\mathfrak F_X(\Lambda)}(q)\le\Omega_X(q)
 \quad(K\le q<X).
 }
\tag{L-91688.6}
\]
The positive radix-four renewal gives the corresponding ordinary inequalities.

The score orientation is also total-row based: positive martingale quantization is score-favorable, while the safety factor and fixed omission have one bounded charge. Thus there is one `C_fin`, not one charge per leaf or color.

## 4. Exact consequence for the three live routes

For a root Hall, target-Lorenz, or Hall-free raw-residual decomposition, it is enough to prove that the source pieces sum to the same positive total endpoint measure in the frozen corridor. No additional colored-to-physical theorem is needed for the analytic/discrete correction layer.

This closes a formal compatibility question but does not prove the frozen analytic hypotheses themselves. In particular, a reviewer must still reconstruct:

1. positivity and exact target/score normalization of the total endpoint density;
2. the bounds in (L-91688.4)--(L-91688.5) with the declared constants;
3. the finite base and shared-port placement in the native, not canonical, capacity.

```text
sum before quantization                          EXACT
one total finite correction                      EXACT
correction independent of color decomposition    EXACT
interior/terminal capacity implication           CONDITIONAL ON EXPLICIT BOUNDS
one bounded score charge                         CONDITIONAL ON EXPLICIT BOUNDS
analytic endpoint estimates                      FROZEN / REVIEW
Riemann Hypothesis                               UNPROVEN
```
