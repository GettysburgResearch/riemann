# L-32709 — The bare Q=4 inverse-source carry field is deterministic and polylogarithmic

Claim ID: `L-32709`  
Title: Convolving the atomized carry window by the unweighted Q=4 inverse source cancels zeta exactly and leaves one explicit base-four staircase field with `O(log^2 X)` carry-position energy  
Status: **PROPOSED COMPLETE EXACT THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-09  
Dependencies: PR #325 `L-32404`; `L-32706`; atomized carry transform `zeta(s)N_theta(s)`  
Scope: bare source leg in the reflected identity; no estimate for the source-convolved Selberg leg and no RH conclusion

## 1. Bare source field

For the Q=4 inverse source

\[
 B_4(s)=\frac{E_4(s)}{\zeta(s)},
 \qquad
 b_4=\mu*e_4,
\]

with

\[
 e_4(1)=1,
 \qquad e_4(4^r)=-3\quad(r\ge1),
\]

define for real `X>=1` and `0<=theta<=1`

\[
 \boxed{
 \mathcal B_4(X,\theta)
 =\sum_{d\le X}b_4(d)
 C\!\left(\frac Xd,\theta\right),
 }
\tag{L-32709.1}
\]

where

\[
 C(x,\theta)
 =\lfloor x\rfloor
 -\lfloor\theta x\rfloor
 -\lfloor(1-\theta)x\rfloor.
\]

This is the physical carry field of the **bare inverse source**, before any logarithmic/generalized-prime factor is inserted.

## 2. Exact zeta cancellation

The logarithmic carry window has transform

\[
 \widehat H_\theta(z)=\zeta(s)N_\theta(s),
 \qquad s=z+\frac12.
\]

Therefore the transform of (L-32709.1) is exactly

\[
 \boxed{
 B_4(s)\zeta(s)N_\theta(s)
 =E_4(s)N_\theta(s).
 }
\tag{L-32709.2}
\]

Every zeta factor has disappeared. In particular the bare source field has no nontrivial-zeta-zero pole and is not an RH-bearing principal state.

## 3. Exact staircase formula

Put

\[
 D_4(x)
 =\sum_{d\le x}b_4(d)\left\lfloor\frac xd\right\rfloor
\tag{L-32709.3}
\]

for real `x>=0`. Divisor switching gives

\[
 D_4(x)=\sum_{m\le x}e_4(m).
\]

Hence

\[
 \boxed{
 D_4(x)=0\quad(0\le x<1),
 }
\tag{L-32709.4}
\]

and

\[
 \boxed{
 D_4(x)=1-3\lfloor\log_4x\rfloor
 \quad(x\ge1).
 }
\tag{L-32709.5}
\]

Substitution into the three floor sums in (L-32709.1) gives

\[
 \boxed{
 \mathcal B_4(X,\theta)
 =D_4(X)-D_4(\theta X)-D_4((1-\theta)X).
 }
\tag{L-32709.6}
\]

At integer `X=n`, `theta=j/n`, this is precisely the source charge `Y_4(n,j)` of `L-32706`.

## 4. Uniform pointwise polylog bound

For every `0<=x<=X`,

\[
 |D_4(x)|
 \le1+3\lfloor\log_4X\rfloor
\]

when `x>=1`, and `D_4(x)=0` otherwise. Therefore

\[
 \boxed{
 |\mathcal B_4(X,\theta)|
 \le3+9\lfloor\log_4X\rfloor
 \qquad(0\le\theta\le1).
 }
\tag{L-32709.7}
\]

No arithmetic estimate enters this inequality.

## 5. Carry-position energy

Integrating (L-32709.7) gives

\[
 \boxed{
 \int_0^1
 |\mathcal B_4(X,\theta)|^2d\theta
 \le
 \left(3+9\lfloor\log_4X\rfloor\right)^2.
 }
\tag{L-32709.8}
\]

Thus the complete bare-source physical energy is

\[
 \boxed{O((1+\log X)^2).}
\tag{L-32709.9}
\]

The same estimate holds on every subinterval of carry positions and after integration over one bounded logarithmic X-block, with one additional absolute constant.

## 6. Source-scale version

For an integer source scale `m<=X`, define

\[
 \mathcal B_{4;m}(X,\theta)
 =\sum_{d\le X/m}b_4(d)
 C\!\left(\frac X{md},\theta\right).
\]

Exactly the same calculation gives

\[
 \boxed{
 \mathcal B_{4;m}(X,\theta)
 =D_4(X/m)-D_4(\theta X/m)-D_4((1-\theta)X/m),
 }
\tag{L-32709.10}
\]

and therefore

\[
 \boxed{
 \|\mathcal B_{4;m}(X,\cdot)\|_2
 \le3+9\log_4(X/m)
 }
\tag{L-32709.11}
\]

with the right side interpreted as `3` when `X/m<1`.

## 7. Consequence for reflected reserve accounting

PR #302 `L-28013` shows that, after source convolution of the independent-frequency Selberg identity, the individual source terms contain a **bare inverse-source leg** and a logarithmic/Selberg leg. Equation (L-32709.2) proves the bare leg is deterministic after the carry window; (L-32709.8) gives a polynomial block budget for it.

Therefore that leg does not need a new reciprocal-zeta recurrence. Any remaining difficulty in the individual reflected terms is confined to the other Selberg/current leg and their exact no-double-spend coupling.

In particular, a future factorization of an individual boundary term as an `L2` inner product

\[
 \langle \mathcal B_4,\mathcal F\rangle
\]

immediately gives by Cauchy

\[
 |\langle \mathcal B_4,\mathcal F\rangle|
 \le O(1+\log X)\,\|\mathcal F\|_2,
\]

without spending any principal inverse-zeta energy on the bare leg.

The present theorem does not assert that every source-convolved product/individual term has already been placed in this factorized form; that localization remains a separate algebraic step.

## 8. Proof boundary

Closed exactly:

- cancellation of zeta on the bare inverse-source leg;
- explicit base-four staircase formula;
- exact physical carry field;
- uniform pointwise `O(log X)` size;
- complete carry-position `O(log^2 X)` energy;
- source-scale version.

Open:

- exact independent-frequency factorization of each remaining reflected boundary term against this bare leg;
- the corresponding reserve accounting / scattering recurrence;
- RH.
