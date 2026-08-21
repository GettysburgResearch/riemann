# L-19856 — The radical-tail identity survives graph closure

Claim ID: `L-19856`  
Status: **PROVED ABSTRACT FORM-CLOSURE THEOREM**  
Authoring agent: `gpt56-pro-09-q`  
Created: 2026-08-07  
Dependencies: continuity of a sesquilinear form; bounded support projections; closed radical relation `L-19855`  
Scope: closes the formal continuity step in the projection-free quotient architecture

## 1. Abstract form setting

Let `X` be a Hilbert space continuously embedded in

\[
 \mathcal H_{\rm full}
 =\mathcal H_{\rm in}\oplus\mathcal H_{\rm out}.
\]

Assume the coordinate projections

\[
 P_{\rm in},P_{\rm out}:X\to X
\]

are bounded. Let `B` be a continuous Hermitian sesquilinear form on `X`.

Let `R_0 subset X` be a linear subspace satisfying

\[
 \boxed{B(r,x)=0\quad(r\in R_0,\ x\in X).}
\tag{L-19856.1}
\]

Let

\[
 \mathcal R=\overline{R_0}^{\,X}.
\]

By continuity,

\[
 \boxed{\mathcal R\subset\operatorname{Rad}B.}
\tag{L-19856.2}
\]

Thus exact weak-radical identities survive closure in any graph topology in which the form and the support projections are continuous.

## 2. Interior/exterior identity

Take `r in mathcal R` and write

\[
 r=g+t,
 \qquad
 g=P_{\rm in}r,
 \qquad
 t=P_{\rm out}r.
\]

Since `B(r,x)=0`,

\[
 \boxed{B(g,x)=-B(t,x)\quad(x\in X).}
\tag{L-19856.3}
\]

Taking `x=g,t,r` gives

\[
 \boxed{
 B(g,g)=B(t,t)=-B(g,t)=-B(t,g).}
\tag{L-19856.4}
\]

No approximation remains.

## 3. Canonical minimum-tail relation

Assume `mathcal R` is closed in the ambient graph Hilbert space and use the canonical minimum-tail operator `mathcal T` of `L-19855`. For every `g in Dom mathcal T`,

\[
 (g,\mathcal Tg)\in\mathcal R.
\]

Therefore

\[
 \boxed{
 B(g,h)=B(\mathcal Tg,\mathcal Th)
 \quad(g,h\in\operatorname{Dom}\mathcal T).}
\tag{L-19856.5}
\]

The localized form on the interior source range is exactly the exterior-tail form on the canonical minimal radical extension.

## 4. Weil-form graph topology

For a fixed support one may take `X_lambda` to be the completion of smooth admissible functions in a norm of the form

\[
 \|f\|_{X_\lambda}^2
 =\|f\|_2^2
 +\|P_\lambda f\|_{Q_\lambda,c}^2
 +\|(I-P_\lambda)f\|_{Z_\lambda,c}^2,
\tag{L-19856.6}
\]

where:

- `Q_(lambda,c)=Q_lambda+c||.||_2^2` is a positive shifted localized form;
- `Z_(lambda,c)` is a positive graph norm dominating the absolutely convergent zero-side pairings of the exterior tails;
- `c` is any lower-bound shift making both graph norms positive.

By construction, `B=QW` and both support projections are continuous. The compact-BV radical identity of `L-16205/L-16206` therefore extends to the `X_lambda` closure.

This graph closure is the correct object. Ordinary `L2` closure alone need not preserve point evaluations at zeta zeros.

## 5. Consequence for the continuous quotient form

On the graph-closed radical relation, the quotient form

\[
 \mathfrak D_\lambda(g)=\|\mathcal T_\lambda g\|_2^2
\]

is closed by `L-19855`, and the exact localized Weil form satisfies

\[
 Q_\lambda(g,h)
 =Z(\mathcal T_\lambda g,\mathcal T_\lambda h)
\tag{L-19856.7}
\]

on the canonical source domain.

Thus the projection-free composition has no unresolved algebraic radical-tail passage. Its remaining issue is quantitative: compare the zero-side tail form in (L-19856.7) with `(log R)` times the ordinary tail form `mathfrak D_lambda` on the complete quotient domain.

## 6. Proof boundary

- Sections 1--3 are exact functional analysis.
- Section 4 specifies a proof-grade graph topology but does not by itself prove that the graph-closed arithmetic source range is dense in the complete localized form domain.
- Density in ordinary `L2` follows at non-zeta-cycle supports; density in the stronger graph topology is a separate common-core theorem.
- No RH conclusion is claimed here.
