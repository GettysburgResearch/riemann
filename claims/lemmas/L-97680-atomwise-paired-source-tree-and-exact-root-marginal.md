# L-97680 — The completed rough source has an exact atomwise paired-source tree and the correct annular root marginal

Claim ID: `L-97680`  
Status: **PROVED EXACT SOURCE-FAITHFULNESS THEOREM**  
Created: 2026-08-18  
Builds on: PR #581 `L-97500/L-97501`, PR #584 `L-97601`, PR #587 source audit  
RH status: **not assumed**

## 1. Literal native occurrences

Fix a real endpoint `X`. Every native squarefree occurrence has a unique
factorization
\[
k=d\,p_1\cdots p_t,
\qquad d\mid P_{61},
\qquad 67\le p_1<\cdots<p_t.
\]
Its immutable label is
\[
\omega=(d;p_1,\ldots,p_t;m,\eta),
\]
where `m` is the physical dictionary index and `eta` is the one-sided
activation flag. Its physical quotient, coefficient magnitude, and sign are
\[
\frac{X}{km},\qquad \frac{q_*(m)}{\sqrt{km}},
\qquad \mu(d)(-1)^t=\mu(k).
\tag{L-97680.1}
\]

Moving a rough prime from `k` into the history preserves both activation and
coefficient magnitude:
\[
\frac{X/p}{(k/p)m}=\frac{X}{km},
\qquad
p^{-1/2}(k/p)^{-1/2}=k^{-1/2}.
\tag{L-97680.2}
\]
It swaps the two parity channels once.

## 2. Unique first ownership and the atomwise bijection

A state is `v=(X_v,p_0,h)`, where `p_0` is the least rough prime still
allowed and `h` is the already extracted ordered history. Let `B_v` consist of
those occurrences with no remaining rough prime. For each active prime
`p>=p_0`, define

\[
 w=(X_v/p,\,p^+,\,h\mathbin{\|}p).
\]

Every occurrence outside `B_v` has one and only one least remaining prime
`p`. The map

\[
(d;h,p,p_2,\ldots,p_t;m,\eta)
\longmapsto
(d;h\mathbin{\|}p,p_2,\ldots,p_t;m,\eta)
\tag{L-97680.3}
\]

is a bijection from the `p`-owned parent occurrences to the occurrences of
`P_w`. Its coefficient and activation identities are exactly

\[
\frac{q_*(m)}{\sqrt{dpp_2\cdots p_tm}}
=p^{-1/2}
\frac{q_*(m)}{\sqrt{dp_2\cdots p_tm}},
\qquad
\frac{X_v}{dpp_2\cdots p_tm}
=\frac{X_v/p}{dp_2\cdots p_tm}.
\tag{L-97680.4}
\]

The extracted prime flips parity once, so the image lies in `S P_w`. Therefore

\[
\boxed{
P_v=B_v\oplus\bigoplus_{p\ge p_0}p^{-1/2}S P_{v/p,p^+}.
}
\tag{L-97680.5}
\]

The direct sum is literal: source labels are disjoint and exhaustive. At fixed
`X` the depth is at most `floor(log X/log 67)`, hence the tree is finite.

## 3. Arbitrary contracted recursion without coefficient loss

For any `0<=t_(v,w)<=r_(v,w)`, define
\[
C_v(t)=B_v\oplus\bigoplus_w(r_{v,w}-t_{v,w})S P_w.
\]
Then
\[
\boxed{
P_v=C_v(t)\oplus\bigoplus_wt_{v,w}S P_w
}
\tag{L-97680.6}
\]
in the positive paired-source cone, and
\[
(r_{v,w}-t_{v,w})+t_{v,w}=r_{v,w}.
\]
Thus current and children are disjoint, first-owned, activation-exact, and
coefficient-exact.

## 4. Exact signed root marginal

Let `ell(P)=ell_+(P^+)-ell_+(P^-)` be the `5:3` annular scalar observation.
Then
\[
f_v=b_v-\sum_wr_{v,w}f_w,
\qquad
c_v=b_v-\sum_w(r_{v,w}-t_{v,w})f_w,
\]
\[
\boxed{
f_v=c_v-\sum_wt_{v,w}f_w.
}
\tag{L-97680.7}
\]
At the root,
\[
\boxed{
f_{\rm root}
=
5[c_X(2)-c_{X/4}(2)]
+3[c_X(3)-c_{X/4}(3)]
=:\mathcal A_X.
}
\tag{L-97680.8}
\]

Equations (L-97680.1)--(L-97680.8) close the source-faithfulness gate:
one owner per native occurrence, literal coefficients and activations, no
reserve reuse, and the correct annular root marginal.

They do **not** prove that the signed current `c_v` is nonnegative. Two positive
parity channels are the minimal source-faithful state; the remaining sign is
nonlocal.
