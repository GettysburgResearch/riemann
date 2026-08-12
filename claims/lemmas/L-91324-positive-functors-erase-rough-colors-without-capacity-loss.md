# L-91324 — Positive affine Pascal functors erase rough colors in ordinary-column Schur ports

Claim ID: `L-91324`  
Status: **PROPOSED COMPLETE EXACT ORDINARY-PROJECTION THEOREM — DETAIL/CAPACITY ASSEMBLY SEPARATE**  
Created: 2026-08-12  
Corrected: 2026-08-12 after hostile audit of the signed radix-four difference  
Depends on: `L-91110`, `L-91316`, `L-91318`–`L-91320`  
RH status: **unproved**

## 1. The alleged leakage problem

For an integer dilation `m>=1`, the affine Pascal lift is

\[
 \Phi_m(n)=m(n+1)-1.
\]

`L-91318` proves, for every real column `q>0`,

\[
 \overline\beta_{\Phi_m(n)}(mq)=\overline\beta_n(q).
\tag{L-91324.1}
\]

At an ordinary physical integer column `Q`, this reads

\[
 \boxed{
 \overline\beta_{\Phi_m(n)}(Q)
 =\overline\beta_n(Q/m).
 }
\tag{L-91324.2}
\]

Thus a colored child `(m,q)` produces a nonnegative value also when `Q` is not
divisible by `m`. Previous route summaries called this value *leakage* and left
open whether a branchwise matrix port remained valid after colors were forgotten.

The exact statement proved here is:

> physical evaluation of an affine lift is a positive linear functor, so every
> positive-semidefinite ordinary-column port domination survives at all physical
> columns, including nonmultiples.

This does **not** say that arbitrary integer-column child feasibility extends to
all real columns, and it does not infer a radix-four inequality by subtracting
two ordinary inequalities.

## 2. Positive endpoint-to-row maps

Let `mathcal E` be any positive linear map from scalar endpoint densities to
nonnegative finite row vectors:

\[
 f\ge0\Longrightarrow (\mathcal Ef)(n)\ge0.
\tag{L-91324.3}
\]

The nearest-neighbour martingale/B-spline quantization of `L-91110` is the
canonical example. The identity map on an already finite row vector is another.

For a row vector `d`, define the affine lift

\[
 (\mathcal A_m d)(\Phi_m(n))=m^{-1/2}d(n),
 \qquad
 (\mathcal A_m d)(N)=0
 \quad(N\notin\Phi_m(\mathbb Z_{\ge0})).
\tag{L-91324.4}

For a physical column `Q>0`, define

\[
 \boxed{
 \mathfrak P_{m,Q}(f)
 =\sum_N(\mathcal A_m\mathcal Ef)(N)
  \overline\beta_N(Q).
 }
\tag{L-91324.5}

Every coefficient in this definition is nonnegative, so `mathfrak P_(m,Q)` is a
positive linear functional.

Using (L-91324.2),

\[
 \boxed{
 \mathfrak P_{m,Q}(f)
 =m^{-1/2}
  \sum_n(\mathcal Ef)(n)
  \overline\beta_n(Q/m).
 }
\tag{L-91324.6}

This identity is valid for every physical integer `Q`; no divisibility
assumption occurs. It is the exact ordinary-column color-forgetting formula.

The same positive-functor argument applies to row score and to every finite
**nonnegative** combination of ordinary physical columns.

## 3. Matrix ports survive every positive functor

Let

\[
 \mathbf K(x)=
 \begin{pmatrix}
  V(x)&B(x)\\
  B(x)&V(x)
 \end{pmatrix}
\]

be a matrix-valued endpoint density satisfying

\[
 \boxed{
 \mathbf K(x)\succeq c\,V(x)I_2
 \qquad\text{pointwise},
 }
\tag{L-91324.7
}

with `V>=0` and `c>0`. Apply `mathfrak P_(m,Q)` entrywise. Since a positive
weighted sum of positive-semidefinite matrices is positive semidefinite,

\[
 \boxed{
 \mathfrak P_{m,Q}(\mathbf K)
 \succeq
 c\,\mathfrak P_{m,Q}(V)I_2
 }
\tag{L-91324.8}

for every real or physical integer column `Q`.

More generally, for any family of already assigned branch ports `b`, possibly
with different dilations and positive quantizers,

\[
 \boxed{
 \sum_b\mathfrak P_{m_b,Q}(\mathbf K_b)
 \succeq
 c\sum_b\mathfrak P_{m_b,Q}(V_b)I_2.
 }
\tag{L-91324.9}

Thus overlapping uncolored supports cannot invalidate a branchwise Schur
inequality. This theorem does not decide whether the same parent port has been
assigned to more than one branch; conservative port assignment is a separate
ledger, treated by `L-91325` and the final reset assembly.

## 4. Application to the rough-prime Schur reserve

For the finite block through `61`, `L-91320` supplies

\[
 \mathbf K_{61}(x)
 =\begin{pmatrix}
  \mathcal V_{61}(x)&\mathcal B_{61}(x)\\
  \mathcal B_{61}(x)&\mathcal V_{61}(x)
 \end{pmatrix}
 \succeq\frac19\mathcal V_{61}(x)I_2.
\tag{L-91324.10}

For every remaining rough prime `p>=67`, the minimal projective correction of
`L-91319` has coefficient

\[
 \tau_p=p^{-1/2}(1-p^{-1/2})<\frac19.
\tag{L-91324.11}

Apply (L-91324.8) to one assigned branch port, its exact endpoint quantization,
and its affine Pascal lift. At every physical column `Q`, including `p\nmid Q`,

\[
 \boxed{
 \tau_p\,\mathfrak P_{p,Q}(\mathcal V_{61})I_2
 \prec
 \mathfrak P_{p,Q}(\mathbf K_{61}).
 }
\tag{L-91324.12}

The nonmultiple contribution of the branch correction is therefore paid by the
nonmultiple contribution of the **same assigned branch port**. There is no extra
ordinary-column leakage term.

## 5. Main rough transition and ordinary physical placement

The paired-interior and activation-frontier terms of `L-91317` have
coefficientwise nonnegative source formulas and a direct ordinary-row/carry
realization. They may be placed in the physical column space before any affine
bookkeeping is introduced.

Equivalently, one may keep the affine description: equation (L-91324.6) says
that physical evaluation is exact at every real rescaled column. In either
coordinate, no cancellation or norm estimate is used.

Combining `L-91317`, `L-91319`, `L-91320`, and the present theorem gives, at the
ordinary branch-port scope:

```text
positive main rough source routing                 physical / exact;
projective state correction                        inside assigned branch port;
affine carry and score lift                         positive / exact;
ordinary physical color erasure                     positive functor;
nonmultiple ordinary-column load                    paid by same branch port.
```

## 6. Radix-four scope firewall

The radix-four operator is

\[
 \mathcal D_4C(q)=C(q)-2C(4q).
\]

It is not a positive linear functional. Therefore

\[
 C_1(q)\ge C_2(q),\qquad C_1(4q)\ge C_2(4q)
\]

does **not** by itself imply

\[
 \mathcal D_4C_1(q)\ge\mathcal D_4C_2(q).
\]

The present theorem must not be used for that invalid subtraction.

There are two legitimate ways to return to detail coordinates:

1. apply the exact affine covariance directly to a child statement already
   established for the real-column detail kernel;
2. prove ordinary slack and reconstruct it from nonnegative detail slack by the
   positive radix-four renewal of `L-90029`.

The factor-54 route uses ordinary-column Schur domination only for the auxiliary
projective port; the outer detail capacities remain governed by
`L-91114/L-91115` and the final source-faithful recursion.

## 7. Atomized interpretation

A parent split has the unique form

\[
 J=mj+r,
 \qquad0\le r<m.
\]

At matched columns every residue phase reproduces the child carry. At unmatched
columns all atomized carries remain nonnegative. Uniform averaging gives exactly
(L-91324.2). A branch port and its correction use the same residue phases and
the same positive weights; therefore phase averaging cannot reverse their
ordinary-column matrix order.

## 8. What remains

This theorem closes ordinary physical color projection for an already assigned
branch port. It does not prove:

```text
real-column feasibility of an arbitrary child packing;
radix-four domination by subtraction;
conservative assignment of the parent port to the complete rough tree;
or the all-generation endpoint-vector ledger.
```

`L-91325` supplies the positive one-scale endpoint renewal needed for the port
assignment. Their combination leaves the explicit recursive assembly as the
next theorem.

## 9. Verification boundary

The companion replay checks:

```text
146,026 exact real-column affine covariance identities;
matched and nonmatched physical columns;
positive 2x2 ordinary-port preservation under branch sums;
the exact p>=67 threshold tau_p<1/9;
synthetic assigned-branch superpositions.
```

Retained verdict:

```text
PASS_POSITIVE_FUNCTOR_COLOR_ERASURE
```

## 10. Proof boundary

```text
ordinary physical evaluation after affine lift       POSITIVE LINEAR
exact nonmultiple real-column covariance              EXACT
PSD Schur domination after ordinary projection        EXACT
assigned-branch color erasure                          EXACT
radix-four subtraction from ordinary domination       NOT VALID
conservative branch-port assignment                    SEPARATE
recursive endpoint-state assembly                      OPEN
coefficient-one all-generation ledger                  OPEN / RH-BEARING
Riemann Hypothesis                                     UNPROVEN
```
