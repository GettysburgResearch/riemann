# L-15134 — Order-four contact polynomial and the all-orders finite-jet Ward hierarchy

Claim ID: `L-15134`  
Status: **PROVED FINITE RENORMALIZATION LEMMA; RIEMANN WARD IDENTITIES OPEN**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-01  
Dependencies: `L-15132`, `L-15133`; finite-dimensional trace algebra  
Scope: exact collision/contact accounting for the one-contour versus product-contour comparison  
Related counterexample candidates: none

## 1. Setup

Fix a finite window/readout pair `(M,N)`. Work intrinsically on the support of
its Gram matrix, so every Moore--Penrose contraction is represented by an
ordinary operator.

Let

\[
 \widetilde B
\]

be the seam tensor before the common finite-jet subtraction, and let

\[
 B^{\rm ct}
\]

be the seam tensor induced by the finite-jet counterterm

\[
 \iota_M^{\rm cen}P_M^{\rm cen}J_M^{\rm cen}.
\]

The renormalized tensor is

\[
 B=\widetilde B-B^{\rm ct}.
 \tag{L-15134.1}
\]

Let `G` be the readout Gram and put

\[
 A=G^\dagger\widetilde B,
 \qquad
 D=G^\dagger B^{\rm ct},
 \qquad
 K=A-D.
 \tag{L-15134.2}
\]

Thus the connected product-contour coefficient is

\[
 A_{\ell}^{\rm cyc}=\operatorname{Tr}(K^\ell).
 \tag{L-15134.3}
\]

Write the displayed one-contour coefficient as

\[
 A_{\ell}^{\rm scalar}
 =\widetilde a_\ell-q_\ell,
 \tag{L-15134.4}
\]

where `q_ell` is the contribution of the common finite-jet counterterm to the
single contour pairing.  Because the contour biform and finite-jet subtraction
are linear, `q_ell` is a one-leg linear counterterm coefficient.  No nonlinear
cyclic contraction is implicit in the notation.

## 2. Exact order-four cyclic expansion

For arbitrary, not necessarily commuting, finite operators `A,D`, cyclicity of
the trace gives

\[
\boxed{
\begin{aligned}
 \operatorname{Tr}(A-D)^4
 ={}&\operatorname{Tr}A^4
 -4\operatorname{Tr}(A^3D)\\
 &+4\operatorname{Tr}(A^2D^2)
 +2\operatorname{Tr}(ADAD)\\
 &-4\operatorname{Tr}(AD^3)
 +\operatorname{Tr}D^4.
\end{aligned}}
 \tag{L-15134.5}
\]

### Proof

Expand the sixteen words in `(A-D)^4` and group them by cyclic trace class.
There are four one-`D` words, four adjacent-two-`D` words, two alternating
words, four three-`D` words, and one four-`D` word.  Their signs and
multiplicities are exactly those in (L-15134.5). QED.

If `A` and `D` commute, the middle two classes combine and

\[
 \operatorname{Tr}(A-D)^4
 =\operatorname{Tr}A^4
 -4\operatorname{Tr}(A^3D)
 +6\operatorname{Tr}(A^2D^2)
 -4\operatorname{Tr}(AD^3)
 +\operatorname{Tr}D^4.
 \tag{L-15134.6}
\]

## 3. Complete order-four defect

Define the raw diagonal defect

\[
 \delta_4^{\rm raw}
 =\widetilde a_4-\operatorname{Tr}A^4.
 \tag{L-15134.7}
\]

Then the exact scalar/cyclic defect is

\[
\boxed{
\begin{aligned}
 \Delta_4^{\rm CL}
 :={}&A_4^{\rm scalar}-A_4^{\rm cyc}\\
 ={}&\delta_4^{\rm raw}-q_4
 +4\operatorname{Tr}(A^3D)\\
 &-4\operatorname{Tr}(A^2D^2)
 -2\operatorname{Tr}(ADAD)\\
 &+4\operatorname{Tr}(AD^3)
 -\operatorname{Tr}D^4.
\end{aligned}}
 \tag{L-15134.8}
\]

Consequently, even after the raw one-contour/product-contour diagonal identity
has been proved, contact-free renormalization at order four requires the
nonlinear Ward identity

\[
\boxed{
\begin{aligned}
 q_4={}&4\operatorname{Tr}(A^3D)
 -4\operatorname{Tr}(A^2D^2)\\
 &-2\operatorname{Tr}(ADAD)
 +4\operatorname{Tr}(AD^3)
 -\operatorname{Tr}D^4.
\end{aligned}}
 \tag{L-15134.9}
\]

The right side contains mixed collision terms of degrees two, three, and four
in the seam/counterterm data.  It is not produced by the mere statement that
the same linear finite-jet subtraction is used in every ledger.

## 4. All-orders contact polynomial

For `ell>=2` and a subset `S subset {1,...,ell}`, let `W_S(A,D)` be the ordered
word whose `j`-th letter is `D` when `j in S` and `A` otherwise.  Then

\[
\boxed{
 \operatorname{Tr}(A-D)^\ell
 =\sum_{S\subseteq[\ell]}
   (-1)^{|S|}\operatorname{Tr}W_S(A,D).}
 \tag{L-15134.10}
\]

Define the nonempty-contact polynomial

\[
 \mathcal P_\ell(A,D)
 =\sum_{\varnothing\ne S\subseteq[\ell]}
   (-1)^{|S|}\operatorname{Tr}W_S(A,D).
 \tag{L-15134.11}
\]

Thus

\[
 \operatorname{Tr}(A-D)^\ell
 =\operatorname{Tr}A^\ell+\mathcal P_\ell(A,D).
 \tag{L-15134.12}
\]

Grouping the summands by cyclic necklaces gives the collision multiplicities at
any order.  No commutativity assumption is used.

Let

\[
 \delta_\ell^{\rm raw}
 =\widetilde a_\ell-\operatorname{Tr}A^\ell.
\]

Then

\[
\boxed{
 \Delta_\ell^{\rm CL}
 =\delta_\ell^{\rm raw}-q_\ell-\mathcal P_\ell(A,D).}
 \tag{L-15134.13}
\]

## 5. Necessary-and-sufficient Ward hierarchy

The contact-free cyclic diagonal identity

\[
 A_\ell^{\rm scalar}
 =A_\ell^{\rm cyc}
 \qquad(\ell\ge2)
 \tag{L-15134.14}
\]

holds if and only if

\[
\boxed{
 q_\ell
 =\delta_\ell^{\rm raw}-\mathcal P_\ell(A,D)
 \qquad(\ell\ge2).}
 \tag{L-15134.15}
\]

If the raw diagonal pullback is already contact free, so
`delta_ell^raw=0`, this reduces to

\[
\boxed{
 q_\ell=-\mathcal P_\ell(A,D)
 \qquad(\ell\ge2).}
 \tag{L-15134.16}
\]

Equation (L-15134.16) is the complete finite-jet Ward hierarchy.  It is the
precise meaning of “all contact terms cancel.”

## 6. Structural sufficient conditions

A strong sufficient condition is that the finite-jet range be a two-sided
radical of the realized contour seam biform.  In coordinates this means

\[
 D=0
 \tag{L-15134.17}
\]

and that the fixed one-contour probe annihilate the same counterterm, so

\[
 q_\ell=0.
 \tag{L-15134.18}
\]

Then every mixed cyclic word vanishes and no contact term is present.

More generally, it suffices that every cyclic word containing at least one `D`
have zero trace and that all `q_ell` vanish.  This is a trace-ideal condition,
not a consequence of finite-jet subtraction alone.

## 7. Application to the Shimizu interface

The manuscript fixes the common linear subtraction

\[
 \Psi_{w,M}^{\rm fw}
 =\widetilde\Psi_{w,M}^{\rm fw}
 -\iota_M^{\rm cen}P_M^{\rm cen}J_M^{\rm cen}(h_{w,M}^{\rm fw}).
\]

The accessible definitions establish neither (L-15134.17) nor the nonlinear
hierarchy (L-15134.16).  In particular, the fact that the subtraction is common
to the Archimedean, arithmetic, and singular-boundary ledgers guarantees
one-leg consistency, but does not remove the mixed cyclic words generated by a
connected product-contour contraction.

## 8. Proof boundary

This lemma completely tracks every finite algebraic contact term.  It does not
assert that the Riemann finite-jet tensors violate the Ward hierarchy; that
requires evaluating the actual source maps.  `R-15111` proves that grading,
quadratic matching, cubic parity, and a one-leg invisible counterterm still do
not force the quartic Ward identity.