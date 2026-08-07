# L-24502 — Exact discrete carry kernel and finite greedy minorant

Claim ID: `L-24502`  
Title: The finite carry matrix lies below the continuum kernel by an explicit positive discretization error, and backward minimum-ratio elimination gives a canonical nonnegative prime-ramp minorant  
Status: **PROPOSED EXACT FINITE LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-08`  
Created: 2026-08-07  
Dependencies: elementary floor algebra, Legendre's formula; comparison with PR #244 frozen at `a1582d6167cc777edf3e21292702beb268bec69b`  
Scope: finite rational algebra; no asymptotic mass estimate

## 1. Carry matrix

For integers `2<=q<=n`, write

\[
 n=qk+r,\qquad 0\le r<q,
 \tag{L-24502.1}
\]

and define

\[
\boxed{
 \beta_{nq}
 =\frac{k(q-1-r)}{n+1}.}
 \tag{L-24502.2}
\]

Equivalently,

\[
\boxed{
 \beta_{nq}
 =\frac1{n+1}\sum_{j=0}^{n}
 \left(
  \left\lfloor\frac nq\right\rfloor
 -\left\lfloor\frac jq\right\rfloor
 -\left\lfloor\frac{n-j}{q}\right\rfloor
 \right).}
 \tag{L-24502.3}
\]

The summand is the carry indicator at the `q`-adic place in `j+(n-j)=n`.
Direct block counting proves (L-24502.2). In particular,

\[
 \beta_{nn}=\frac{n-1}{n+1}>0.
 \tag{L-24502.4}
\]

## 2. Exact comparison with the continuum kernel

Let `b` be the continuum function of `L-24501`. Since

\[
 \left\lfloor\frac nq\right\rfloor=k,
 \qquad
 \frac nq=k+\frac rq,
\]

one has

\[
 b(n/q)=\frac{k(q-r)}n.
 \tag{L-24502.5}
\]

Subtracting (L-24502.2) gives the exact positive error

\[
\boxed{
 b(n/q)-\beta_{nq}
 =\frac{k(n+q-r)}{n(n+1)}.}
 \tag{L-24502.6}
\]

Therefore

\[
\boxed{
 0\le\beta_{nq}\le b(n/q),}
 \tag{L-24502.7}
\]

and, because `k<=n/q` and `n+q-r<=2n`,

\[
\boxed{
 0\le b(n/q)-\beta_{nq}\le\frac2q.}
 \tag{L-24502.8}
\]

The error is one-sided. This orientation is load bearing for any continuum-to-
discrete minorant argument.

## 3. Prime-ramp target

For an integer endpoint `X>=2`, define

\[
 w_X(q)=q^{-1/2}\log(X/q),
 \qquad2\le q\le X.
 \tag{L-24502.9}
\]

Let `B_X` be the upper-triangular matrix with entries `beta_(nq)`, rows indexed
by `2<=n<=X`, and columns by `2<=q<=X`.

The prime-power ramp is

\[
 P(X)=\sum_{q=p^a\le X}\Lambda(q)w_X(q).
 \tag{L-24502.10}
\]

For

\[
 G_n=\frac1{n+1}\sum_{j=0}^{n}\log\binom nj,
 \tag{L-24502.11}
\]

Legendre's formula and (L-24502.3) give exactly

\[
\boxed{
 G_n=\sum_{q=p^a\le n}\Lambda(q)\beta_{nq}.}
 \tag{L-24502.12}
\]

Hence every nonnegative vector `d=(d_2,...,d_X)` satisfying

\[
 B_X^Td\le w_X
 \tag{L-24502.13}
\]

produces the rigorous lower bound

\[
\boxed{
 P(X)\ge\sum_{n=2}^{X}d_nG_n.}
 \tag{L-24502.14}
\]

## 4. Canonical greedy minorant

Initialize

\[
 \rho^{(X)}(q)=w_X(q).
 \tag{L-24502.15}
\]

For `n=X,X-1,...,2`, define

\[
\boxed{
 d_X(n)=
 \min_{\substack{2\le q\le n\\\beta_{nq}>0}}
 \frac{\rho^{(n)}(q)}{\beta_{nq}},}
 \tag{L-24502.16}
\]

and update

\[
 \rho^{(n-1)}(q)
 =\rho^{(n)}(q)-d_X(n)\beta_{nq}
 \qquad(q\le n),
 \tag{L-24502.17}
\]

leaving the larger coordinates unchanged.

Because the diagonal coefficient in (L-24502.4) is positive, the minimum is
nonempty. Induction proves

\[
\boxed{
 d_X(n)\ge0,
 \qquad
 \rho^{(n)}(q)\ge0,
 \qquad
 B_X^Td_X\le w_X.}
 \tag{L-24502.18}
\]

The algorithm is rational after the target values have been supplied by directed
intervals. It uses no LP optimizer and has a deterministic blocker/tie ledger.

## 5. Mass and entropy debt

Define

\[
\boxed{
 M_X=\sum_{n=2}^{X}n\,d_X(n),}
 \tag{L-24502.19}
\]

and

\[
\boxed{
 L_X=\sum_{n=2}^{X}d_X(n)\,[\log(n+1)+3].}
 \tag{L-24502.20}
\]

The elementary entropy bound

\[
 G_n\ge\frac n2-\log(n+1)-3
 \tag{L-24502.21}
\]

then gives

\[
\boxed{
 P(X)\ge\frac12M_X-L_X.}
 \tag{L-24502.22}
\]

Thus the finite theorem needed by the carry route is an aggregate statement
about `M_X` and `L_X`, not entrywise positivity of the exact triangular inverse.

## 6. Continuum scaling dictionary

Write

\[
 n=Xe^{-v},\qquad q=Xe^{-u},\qquad0\le v\le u.
 \tag{L-24502.23}
\]

A profile of the form

\[
 d_X(n)\approx n^{-3/2}g(v)
 \tag{L-24502.24}
\]

turns the constraint, at Riemann-sum level, into

\[
 (k*g)(u)\le u,
 \tag{L-24502.25}
\]

where `k` is the exact continuum kernel of `L-24501`. Its mass becomes

\[
 M_X\approx\sqrt X
 \int_0^{\log(X/2)}e^{-v/2}g(v)\,dv.
 \tag{L-24502.26}
\]

Since the exact continuum inverse has critical Abel mass eight, the sharp finite
target is

\[
 M_X=8\sqrt X+\text{small error}.
 \tag{L-24502.27}
\]

Equations (L-24502.25)--(L-24502.27) are a scaling dictionary, not an estimate.
The required fail-closed discrete stability is stated separately in `L-24503`.

## 7. Review firewall

A reviewer should verify independently:

1. the carry count (L-24502.3);
2. the exact error identity (L-24502.6);
3. the one-sided bound (L-24502.8);
4. every residual update in the greedy algorithm;
5. the Legendre/Kummer assembly (L-24502.12);
6. the entropy orientation in (L-24502.22).

Mandatory mutations reverse the sign in (L-24502.6), omit the diagonal blocker,
change one carry residue, and replace a prime-power row by a prime-only row.
All must fail.

## 8. Proof boundary

Closed exactly:

- the finite carry matrix;
- its positive continuum comparison;
- the canonical nonnegative greedy minorant;
- the prime-ramp factorization;
- the mass/debt lower bound.

Open:

- the sharp aggregate mass;
- the entropy-debt bound;
- discrete-to-continuum resolvent stability;
- RH.
