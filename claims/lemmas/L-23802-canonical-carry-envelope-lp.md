# L-23802 — Canonical carry-envelope LP and exact deficit coordinates

Claim ID: `L-23802`  
Title: The weakest finite carry certificate is a canonical convex-obstacle packing, not exact triangular positivity  
Status: **PROPOSED COMPLETE FINITE OPTIMIZATION THEOREM**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-07  
Issue: #238  
Dependencies: `D-23801`, `L-23801`  
Scope: exact finite reduction; the asymptotic packing bound is separate

## 1. Entropy packing LP

Put

\[
 h_n=\frac n2-\log(n+1)-3.
 \tag{L-23802.1}
\]

Define

\[
 \boxed{
 \mathsf C_X
 =\max\left\{
 \sum_{n=2}^Xd(n)h_n:
 d\ge0,\ B_X^Td\le w_X
 \right\}.}
 \tag{L-23802.2}
\]

The objective is a certified lower bound for
`sum d(n)G_n`. The feasible polytope is nonempty. Because
`beta_(nn)>0`, every coordinate is bounded above by a finite backward
triangular bound, so an optimizer exists.

Choose the **canonical optimizer** by lexicographic tie breaking from
`n=X` down to `n=2`. This makes the finite certificate deterministic without
asserting that the exact inverse is positive.

## 2. Exact LP dual

Finite LP duality gives

\[
 \boxed{
 \mathsf C_X
 =\min\left\{
 \sum_{q=2}^Xw_X(q)y(q):
 y(q)\ge0,
 \quad
 \sum_{q=2}^n\beta_{nq}y(q)\ge h_n
 \ (2\le n\le X)
 \right\}.}
 \tag{L-23802.3}
\]

Thus the carry theorem admits two exactly equivalent proof languages:

```text
primal: pack nonnegative binomial-entropy rows beneath the prime ramp;
dual: every nonnegative carry super-solution has cost at least 4 sqrt(X)-small.
```

A numerical LP solver may nominate either side, but a proof object consists only
of outward rational/logarithmic enclosures and exact finite inequalities.

## 3. Convex-obstacle form

Let `F_X=F_(w_X)` be the Möbius-tail profile of `D-23801`. For a candidate
profile `P`, put

\[
 d_P(n)=(n+1)\Delta^2P(n)
 \tag{L-23802.4}
\]

and reconstruct the unused ramp by

\[
 \rho_P(q)
 =\sum_{k\le X/q}
 \Bigl[
 (qk-1)(F_X(qk)-P(qk))
 -qk(F_X(qk+1)-P(qk+1))
 \Bigr].
 \tag{L-23802.5}
\]

Then the primal is exactly

\[
 \boxed{
 \begin{aligned}
 \mathsf C_X=\max_P\quad&
 \sum_{n=2}^X(n+1)\Delta^2P(n)h_n\\
 \text{subject to}\quad&
 P(X+1)=P(X+2)=0,\\
 &\Delta^2P(n)\ge0,\\
 &\rho_P(q)\ge0.
 \end{aligned}}
 \tag{L-23802.6}
\]

This is a one-dimensional discrete convex obstacle with finitely many
Möbius-divisor inequalities.

Exact Carry Saturation is the special assertion that `P=F_X` is feasible,
i.e. that `F_X` itself is convex. The present route permits a strict convex
sub-profile.

## 4. Exact area and curvature budgets

For every feasible profile,

\[
 \mathcal M_X(P)
 :=\sum_{n=2}^Xn d_P(n)
 =6P(2)+2\sum_{j=4}^XP(j).
 \tag{L-23802.7}
\]

The entropy correction is

\[
 \mathcal L_X(P)
 =\sum_{n=2}^Xd_P(n)(\log(n+1)+3).
 \tag{L-23802.8}
\]

Hence

\[
 \boxed{
 \mathsf C_X
 \ge\frac12\mathcal M_X(P)-\mathcal L_X(P).}
 \tag{L-23802.9}
\]

The logarithmic correction may also be written by two summations by parts as a
positive boundary term plus

\[
 \sum_{j=4}^X P(j)
 \Delta^2\bigl[(j-1)(\log(j-1)+3)\bigr],
 \tag{L-23802.10}
\]

whose coefficient is `O(1/j)`. Thus a sufficient profile budget is

\[
 P(2)+\sum_{j=4}^X\frac{P(j)}j\le X^{o(1)}.
 \tag{L-23802.11}
\]

## 5. Canonical descending producer

A simple fail-closed producer starts from `rho=w_X` and descends
`n=X,X-1,...,2`. At level `n`, set

\[
 \boxed{
 d^{\rm gr}_X(n)
 =\min_{\substack{2\le q\le n\\\beta_{nq}>0}}
 \frac{\rho(q)}{\beta_{nq}},}
 \tag{L-23802.12}
\]

and replace

\[
 \rho(q)\leftarrow\rho(q)-d_X^{\rm gr}(n)\beta_{nq}.
 \tag{L-23802.13}
\]

This produces an exact feasible packing and saturates at least one carry
constraint at every nonzero step. It need not be the entropy-optimal LP point;
it is a canonical discovery and certificate generator.

If the diagonal `q=n` is always the minimizer, then the greedy vector equals
the exact triangular inverse and Carry Saturation holds. The new proposal does
not require this stronger invariant.

## 6. Carry deficit

Define the nonnegative finite deficit

\[
 \boxed{
 \mathfrak D_X
 =\bigl(4\sqrt X-\mathsf C_X\bigr)_+.}
 \tag{L-23802.14}
\]

The complete carry-envelope theorem needed for RH is simply

\[
 \boxed{
 \mathfrak D_X=X^{o(1)}.}
 \tag{L-23802.15}
\]

Equivalently, for every `epsilon>0`,

\[
 \mathsf C_X\ge4\sqrt X-C_\varepsilon X^\varepsilon.
 \tag{L-23802.16}
\]

By `L-23801`, (L-23802.15) implies RH.

## 7. Outer-layer theorem and proof firewall

The existing carry analysis proves positivity of the exact inverse whenever

\[
 5n>X.
 \tag{L-23802.17}
\]

In the curvature language, `F_X` is convex on the outer four-fifths. Therefore
all nontrivial obstacle corrections occur in quotient layers where
`floor(X/n)>=5`.

The exact Möbius-curvature formula shows why this is the correct firewall: the
fifth layer is the first place where `mu(5)=-1` enters. Any proposed proof that
replaces the signed transform by an unsigned norm before this layer cannot
prove (L-23802.15).

## 8. Proof boundary

Closed exactly:

- primal/dual LP;
- convex-obstacle representation;
- canonical greedy feasible producer;
- exact area and logarithmic budgets;
- reduction of RH to `mathfrak D_X=X^o(1)`.

Open:

- a subpolynomial bound for the optimal carry deficit.
