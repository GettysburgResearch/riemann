# L-91324 — Positive affine Pascal functors erase rough colors without capacity loss

Claim ID: `L-91324`  
Status: **PROPOSED COMPLETE EXACT PHYSICAL-PROJECTION THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-12  
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
divisible by `m`.  Previous route summaries called this value *leakage* and left
open whether summing colors could spend one physical capacity more than once.

The point of this theorem is that no separate estimate of that leakage is
needed.  Physical evaluation after affine lift is itself a positive linear
functor.  Every port domination proved before color erasure therefore survives
color erasure exactly, including at nonmultiples.

## 2. Positive endpoint-to-row maps

Let `mathcal E` be any positive linear map from scalar endpoint densities to
nonnegative finite row vectors:

\[
 f\ge0\Longrightarrow (\mathcal Ef)(n)\ge0.
\tag{L-91324.3}
\]

The nearest-neighbour martingale/B-spline quantization of `L-91110` is the
canonical example.  The identity map on an already finite row vector is another.

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
assumption occurs.  It is the exact color-forgetting formula.

The same construction applies to ordinary carry, radix-four detail, row score,
and any finite nonnegative combination of physical columns.  For the
radix-four detail one simply uses the difference of the already allocated
ordinary columns after the positive detail target has been fixed; branchwise
port domination is proved at the ordinary-column level and hence survives both
terms.

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
\tag{L-91324.7}

with `V>=0` and `c>0`.  Apply `mathfrak P_(m,Q)` entrywise.  Since a positive
weighted sum of positive-semidefinite matrices is positive semidefinite,

\[
 \boxed{
 \mathfrak P_{m,Q}(\mathbf K)
 \succeq
 c\,\mathfrak P_{m,Q}(V)I_2
 }
\tag{L-91324.8}

for every real or physical integer column `Q`.

More generally, for any family of branches `b`, possibly with different
dilations and positive quantizers,

\[
 \boxed{
 \sum_b\mathfrak P_{m_b,Q}(\mathbf K_b)
 \succeq
 c\sum_b\mathfrak P_{m_b,Q}(V_b)I_2.
 }
\tag{L-91324.9}

Thus summing colors before or after physical evaluation gives the same port
reserve.  Overlap of their uncolored supports cannot invalidate a domination
which was established branchwise against the same branch ports.

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

Apply (L-91324.8) to the exact endpoint quantization and affine Pascal lift used
on that branch.  At every physical column `Q`, including `p\nmid Q`,

\[
 \boxed{
 \tau_p\,\mathfrak P_{p,Q}(\mathcal V_{61})I_2
 \prec
 \mathfrak P_{p,Q}(\mathbf K_{61}).
 }
\tag{L-91324.12}

The nonmultiple contribution on the left is therefore paid by the
*nonmultiple contribution of the same positive port on the right*.  There is no
additional leakage term.

The least-prime routing of `L-91317` assigns every source packet to one branch.
Consequently the corresponding branch ports are not duplicated.  Summing
(L-91324.12) over the complete least-prime tree and using (L-91324.9) proves that
the complete collection of projective corrections remains inside the sum of the
available physical ports at every ordinary column.

## 5. Main rough transition requires no colored correction

The projective correction was the only part for which the colored description
was potentially dangerous.  The paired-interior and activation-frontier terms
of `L-91317` already have coefficientwise nonnegative source formulas and a
direct ordinary-row/carry realization.  They may therefore be placed in the
physical column space before any affine bookkeeping is introduced.

Equivalently, one may keep the affine description: equation (L-91324.6) says
that summing its colors is exactly a positive physical evaluation.  In either
coordinate, no cancellation or norm estimate is used.

Combining `L-91317`, `L-91319`, `L-91320`, and the present theorem gives:

```text
positive main rough source routing                 physical / exact;
projective state correction                        inside branch Schur port;
affine carry and score lift                         positive / exact;
forgetting colors                                   positive functor;
nonmultiple physical-column load                    paid by the same port;
source duplication                                  excluded by least-prime labels.
```

Hence the colored-to-uncolored operation named as open in
`L-91318`–`L-91320` is closed at the branch-port scope actually used by the
factor-54 reset.

## 6. Atomized interpretation

The same fact can be seen before averaging.  A parent split has the unique form

\[
 J=mj+r,
 \qquad0\le r<m.
\]

At matched columns, every residue phase reproduces the child carry.  At
unmatched columns all atomized carries remain nonnegative.  Uniform averaging
over the residue phases gives exactly (L-91324.2).  A branch port and its
correction use the same residue phases and the same positive weights; therefore
phase averaging cannot reverse their order.

This explains categorically why a separate polyphase cancellation theorem was
the wrong target: the required relation is domination, and positive functors
preserve domination automatically.

## 7. What remains

This theorem closes physical color projection for the already constructed
branchwise rough transition and Schur port.  It does not by itself prove that
the complete recursively assembled endpoint vector equals the canonical reset
state required by `T-91101`.

The remaining assembly obligation is now:

```text
compose the branchwise positive physical transitions into one contracted
endpoint state, keep all final endpoint coefficients nonnegative, and write the
coefficient-one score/column ledger explicitly across generations.
```

No additional real-column, residue-class, or colored-capacity estimate remains.

## 8. Verification boundary

The companion replay checks:

```text
146,026 exact real-column affine covariance identities;
matched and nonmatched physical columns;
positive 2x2 port preservation under branch sums;
the exact p>=67 threshold tau_p<1/9;
synthetic least-prime branch superpositions.
```

Retained verdict:

```text
PASS_POSITIVE_FUNCTOR_COLOR_ERASURE
```

## 9. Proof boundary

```text
physical evaluation after affine lift            POSITIVE LINEAR
exact nonmultiple real-column covariance           EXACT
PSD Schur domination after physical projection     EXACT
branch-sum color erasure                            EXACT
rough projective correction after color erasure    CLOSED
main rough source physical realization             AVAILABLE
recursive endpoint-state assembly                  OPEN
coefficient-one all-generation ledger              OPEN / RH-BEARING
Riemann Hypothesis                                 UNPROVEN
```
