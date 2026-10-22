# L-23806 — A global coarse pivot-potential row bound

Claim ID: `L-23806`  
Title: One explicit sharp-leading carry potential costs at most the row index on every finite carry row  
Status: **PROPOSED EXACT ELEMENTARY LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-07  
Issue: #238  
Dependencies: the carry matrix of `D-23801` or `L-23801`  
Scope: source-free floor geometry; no residual theorem

## 1. Statement

For integers `q>=2`, put

\[
\boxed{
 a(q)=2-{64\over\sqrt q}.}
\tag{L-23806.1}
\]

The weights may be negative for finitely many small columns; no positivity of
`a` is asserted or needed. For every integer `n>=2`,

\[
\boxed{
 \sum_{q=2}^n a(q)\beta_{nq}\le n.}
\tag{L-23806.2}
\]

Moreover, for the carry target

\[
w_X(q)=q^{-1/2}\log(X/q),
\]

the initial potential has the sharp leading term

\[
\boxed{
 \sum_{q=2}^Xa(q)w_X(q)
 =8\sqrt X+O(\log^2X).}
\tag{L-23806.3}
\]

Thus the constant `64` spends only a polylogarithmic correction and does not
alter the mass-eight main term.

## 2. Comparison with the continuum carry kernel

Define, for `x>=1`,

\[
K(x)={\lfloor x\rfloor
 [\lfloor x\rfloor+1-x]\over x},
\]

and put

\[
f(t)=K(1/t),
\qquad0<t\le1.
\tag{L-23806.4}
\]

If

\[
A=\left\lfloor{n\over q}\right\rfloor,
\qquad
L=(A+1)q-n,
\]

then `1<=L<=q` and

\[
K(n/q)={AL\over n},
\qquad
\beta_{nq}={A(L-1)\over n+1}.
\]

Consequently

\[
\boxed{
0\le\beta_{nq}\le f(q/n).}
\tag{L-23806.5}
\]

On each interval

\[
I_A=\left({1\over A+1},{1\over A}\right],
\]

the function is the increasing affine ramp

\[
f(t)=A[(A+1)t-1],
\tag{L-23806.6}
\]

with values from `0` to `1`. Its integral is

\[
\int_0^1f(t)dt
=\int_1^\infty K(x)x^{-2}dx
={1\over2}.
\tag{L-23806.7}
\]

## 3. Upper bound for the unweighted row sum

Let

\[
S_0(n)=\sum_{q=2}^n\beta_{nq}
\]

and put `M=floor(sqrt(n))`. For `q<=M`, use `f(q/n)<=1`, giving total at most
`M`.

For `q>M`, the quotient `floor(n/q)` takes at most `M` values. On each ramp
`I_A`, the right grid sum of an increasing function of height at most one is at
most its integral times `n`, plus one endpoint unit. Therefore

\[
\sum_{q>M}f(q/n)
\le n\int_0^1f(t)dt+M.
\]

Together with (L-23806.5)--(L-23806.7),

\[
\boxed{
S_0(n)\le {n\over2}+2\sqrt n.}
\tag{L-23806.8}
\]

Hence

\[
2S_0(n)-n\le4\sqrt n.
\tag{L-23806.9}
\]

## 4. Lower bound for the square-root weighted row sum

Put

\[
S_{1/2}(n)
=\sum_{q=2}^n{\beta_{nq}\over\sqrt q}.
\]

For `n>=8`, restrict to

\[
\left\lceil{3(n+1)\over4}\right\rceil\le q\le n.
\]

There are at least `n/8` integers in this range. Since `q>n/2`,

\[
\beta_{nq}={2q-n-1\over n+1}\ge{1\over2},
\]

and `q^(-1/2)>=n^(-1/2)`. Therefore

\[
\boxed{
S_{1/2}(n)\ge{\sqrt n\over16}.}
\tag{L-23806.10}
\]

The finitely many cases `2<=n<8` are checked directly.

Combining (L-23806.9) and (L-23806.10),

\[
2S_0(n)-64S_{1/2}(n)\le n,
\]

which is exactly (L-23806.2).

## 5. Sharp initial potential

Elementary integral comparison gives

\[
2\sum_{q=2}^Xq^{-1/2}\log(X/q)
=8\sqrt X+O(\log X),
\]

while

\[
64\sum_{q=2}^Xq^{-1}\log(X/q)
=O(\log^2X).
\]

This proves (L-23806.3).

## 6. Application to a carry packing

For any feasible packing `d` with final residual

\[
\rho=w_X-B_X^Td\ge0,
\]

multiply the row inequality (L-23806.2) by `d(n)` and sum. One obtains

\[
\boxed{
\sum_{n=2}^Xn d(n)
\ge
8\sqrt X-O(\log^2X)
-
\sum_{q=2}^Xa(q)\rho(q).}
\tag{L-23806.11}
\]

Because `a(q)<0` only for finitely many `q`, it is enough to control the
positive residual potential

\[
\boxed{
\mathcal R_X^+
=\sum_{q=2}^X(a(q))_+\rho(q).}
\tag{L-23806.12}
\]

A bound

\[
\mathcal R_X^+=X^{o(1)}
\tag{L-23806.13}
\]

for the canonical greedy packing implies the Greedy Carry Mass theorem and
therefore RH through `L-23804/T-23802`.

## 7. Proof boundary

Closed here:

- an explicit global row-potential inequality;
- its sharp initial mass-eight asymptotic;
- reduction of GCM to one positive final-residual potential.

Open:

- the subpolynomial residual bound (L-23806.13);
- RH.
