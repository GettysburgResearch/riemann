# R-24501 — The polylogarithmic monotone Divisibility Cover is impossible

Claim ID: `R-24501`  
Status: `PROPOSED COMPLETE REFUTATION`  
Scope: the sufficient theorem `(D1)–(D3)` in `L-24502`  
Issue: #245  
Depends on: `L-24504`, `L-24505`, `X-24502`, the prime number theorem

The monotone cover proposed in `L-24502` cannot have polylogarithmic weighted cost. The obstruction is a fixed positive-excess band of large primes whose sets of multiples below `X` are disjoint.

## 1. A positive continuum band

On a reciprocal cell

\[
\frac1{N+1}<\theta\le\frac1N,
\]

the continuum seed excess is

\[
E_N(\theta)
=\theta^{-1/2}
\left[A_N+(H_N+1)\log\theta+4H_N\right]-4N.
\]

Its derivative has at most one zero, and that zero is a maximum because the derivative bracket is strictly decreasing in `log theta`. Hence the minimum on each closed reciprocal cell occurs at an endpoint.

`X-24502` certifies with exact rational intervals that

\[
E(1/N)>\frac1{10}
\qquad(32\le N\le40).
\tag{R-24501.1}
\]

The reciprocal endpoints are shared by adjacent cells. Therefore

\[
\boxed{
E(\theta)>\frac1{10}
\qquad\left(\frac1{40}\le\theta\le\frac1{32}\right).}
\tag{R-24501.2}
\]

## 2. Uniform discrete lower bound

Use the notation and exact averaging identity of `L-24507`. On `[1/40,1]`,

\[
|g'(t)|<253,
\]

because

\[
40^3<253^2
\]

and `|1+(1/2)log t|<=1` on this interval. There are at most `40` summands, so

\[
\left|
\sqrt X\,v_q(b_X^{(0)})-
\sum_{kq\le X}g(kq/X)
\right|
\le\frac{5060}{X}.
\tag{R-24501.3}
\]

Combining (R-24501.2) and (R-24501.3), for every integer

\[
X\ge101201
\]

and every integer `q` with

\[
\frac X{40}\le q\le\frac X{32},
\]

one has

\[
\boxed{
e_X(q):=v_q(b_X^{(0)})-w_X(q)
\ge\frac1{20\sqrt X}.}
\tag{R-24501.4}
\]

In particular this holds for every prime in the band.

## 3. Distinct large primes cannot share a cover atom

Suppose nonnegative atoms `alpha_m` satisfy the covering inequalities

\[
\sum_{kq\le X}\alpha_{kq}\ge e_X(q)
\tag{D1}
\]

for all prime powers `q<=X`.

Let

\[
\mathcal P_X=\left\{p\text{ prime}:\frac X{40}\le p\le\frac X{32}\right\}.
\]

For sufficiently large `X`, no integer `m<=X` can be divisible by two distinct primes in `P_X`, since

\[
p_1p_2\ge\frac{X^2}{1600}>X.
\]

Therefore the multiple sets

\[
\{m\le X:p\mid m\},\qquad p\in\mathcal P_X,
\]

are pairwise disjoint. Summing (D1) over `p in P_X` and using (R-24501.4) gives

\[
\sum_{m\le X}\alpha_m
\ge
\frac{\#\mathcal P_X}{20\sqrt X}.
\tag{R-24501.5}
\]

Every atom counted on the left lies at `m>=X/40`, so its weighted cost obeys

\[
\sum_{m\le X}\alpha_m\log m
\ge
\log(X/40)\frac{\#\mathcal P_X}{20\sqrt X}.
\tag{R-24501.6}
\]

The prime number theorem gives

\[
\#\mathcal P_X
=\pi(X/32)-\pi(X/40)
\sim\frac{X}{160\log X}.
\]

Consequently, for all sufficiently large `X`,

\[
\boxed{
\sum_{m\le X}\alpha_m\log m
\gg\sqrt X.}
\tag{R-24501.7}
\]

For example, after enlarging the threshold if needed, the right side may be taken as `sqrt(X)/16000`.

This contradicts the proposed condition

\[
\sum_m\alpha_m\log m=O(\log^2X).
\tag{D3}
\]

The tail-capacity condition `(D2)` is irrelevant to the contradiction; `(D1)` and `(D3)` are already incompatible.

## 4. Meaning of the refutation

The finite LP reconnaissance in `O-24501` was pre-asymptotic. Its apparent cheapness cannot persist: the large-prime band eventually forces square-root cost for every monotone subtraction cover.

This does **not** refute adjacent transport. A local flow at an index `j` pays the much smaller exact weight

\[
\log\frac{j^2}{j^2-1}\asymp j^{-2},
\]

and can repair the same large-prime constraint at negligible objective cost. The surviving route must therefore use signed adjacent transport and its primitive-neighbor cancellation; a monotone tail subtraction is too rigid.

## Review boundary

- `X-24502` certifies only the finite continuum inequalities.
- The discrete passage is elementary and explicit.
- The final counting step imports only the ordinary prime number theorem, not RH.
- The refutation applies precisely to the nonnegative cover `(D1)–(D3)` and not to PNC.
