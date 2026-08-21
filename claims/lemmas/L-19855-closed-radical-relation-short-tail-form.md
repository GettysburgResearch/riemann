# L-19855 — A closed radical relation has a canonical closed minimum-tail form

Claim ID: `L-19855`  
Status: **PROVED ABSTRACT HILBERT-SPACE THEOREM**  
Authoring agent: `gpt56-pro-09-q`  
Created: 2026-08-07  
Dependencies: closed linear relations; orthogonal projection in Hilbert space  
Scope: closes the quotient-form closability and linear-minimal-lift gate in `L-19852/T-19811`

## 1. Interior/exterior splitting

Let

\[
 \mathcal H_{\rm full}
 =\mathcal H_{\rm in}\oplus\mathcal H_{\rm out}
\]

be a Hilbert space and let

\[
 \mathcal R\subset\mathcal H_{\rm full}
\]

be a closed linear subspace. In the localized-Weil application, `mathcal R` is the `L2` closure of the global arithmetic-radical range, `mathcal H_in` is the interval `[lambda^-1,lambda]`, and `mathcal H_out` is its complement.

Let

\[
 \mathcal M
 :=\{t\in\mathcal H_{\rm out}:(0,t)\in\mathcal R\}
\tag{L-19855.1}
\]

be the vertical multivalued part. It is closed.

Define

\[
 \operatorname{Dom}\mathcal T
 :=P_{\rm in}\mathcal R.
\tag{L-19855.2}
\]

## 2. Canonical minimum-tail lift

For `v in Dom mathcal T`, choose any `t` with `(v,t) in mathcal R` and put

\[
 \boxed{
 \mathcal T v=P_{\mathcal M^\perp}t.}
\tag{L-19855.3}
\]

This is independent of the chosen `t`: if `(v,t_1),(v,t_2) in mathcal R`, then

\[
 (0,t_1-t_2)\in\mathcal R,
\]

so `t_1-t_2 in mathcal M` and their `mathcal M^perp` projections agree.

Moreover, since `(0,P_mathcal M t) in mathcal R`, subtraction gives

\[
 (v,\mathcal T v)\in\mathcal R.
\tag{L-19855.4}
\]

Thus `mathcal T` is the unique exterior component orthogonal to every zero-interior radical tail.

## 3. Exact minimization

Every exterior component representing `v` is of the form

\[
 \mathcal T v+m,
 \qquad m\in\mathcal M.
\]

Orthogonality gives

\[
 \|\mathcal T v+m\|^2
 =\|\mathcal T v\|^2+\|m\|^2.
\]

Therefore

\[
 \boxed{
 \|\mathcal T v\|^2
 =\min\{\|t\|^2:(v,t)\in\mathcal R\}.}
\tag{L-19855.5}
\]

The minimizer is linear in `v`.

## 4. Closedness

Suppose

\[
 v_n\to v\quad\text{in }\mathcal H_{\rm in},
\qquad
 \mathcal T v_n\to t\quad\text{in }\mathcal H_{\rm out}.
\]

By (L-19855.4), `(v_n,mathcal T v_n) in mathcal R`. Since `mathcal R` is closed,

\[
 (v,t)\in\mathcal R.
\]

Also `t in mathcal M^perp`, so by uniqueness `t=mathcal T v`. Hence

\[
 \boxed{\mathcal T\text{ is a closed densely defined operator whenever }P_{\rm in}\mathcal R\text{ is dense}.}
\tag{L-19855.6}
\]

## 5. Closed quotient form

Define

\[
 \boxed{
 \mathfrak D(v)=\|\mathcal T v\|^2,
 \qquad
 \operatorname{Dom}\mathfrak D=\operatorname{Dom}\mathcal T.}
\tag{L-19855.7}
\]

The graph norm

\[
 \|v\|_{\mathfrak D}^2
 =\|v\|_{\rm in}^2+\|\mathcal T v\|_{\rm out}^2
\]

is complete because `mathcal T` is closed. Thus `mathfrak D` is a closed nonnegative quadratic form.

Equations (L-19855.3)--(L-19855.5) supply exactly the linear `D`-minimal lift required in `L-19852`.

## 6. Radical application

Let `mathcal R_lambda` be the `L2` closure of the global exact-radical image under the decomposition

\[
 J=P_\lambda J+(I-P_\lambda)J.
\]

Then

\[
 \mathfrak D_\lambda(g)
 =\min\left\{
 \|(I-P_\lambda)J\|_2^2:
 J\in\mathcal R_\lambda,
 P_\lambda J=g
 \right\}.
\tag{L-19855.8}
\]

At a non-zeta-cycle support, the projected radical range is dense, so `mathfrak D_lambda` is densely defined. No finite Fourier projection is involved.

## 7. Proof boundary

- The theorem proves closability, closedness, linearity, and exact minimization from one condition: the chosen global radical range is closed in the full `L2` space.
- Replacing the exact radical range by its `L2` closure is harmless for ordinary tail energy, but extending the zero-side radical identity to every closure vector requires a separate form-continuity argument.
- The theorem does not prove the signed low-index hierarchy or the local-Weyl comparison.
- No RH conclusion is claimed here.
