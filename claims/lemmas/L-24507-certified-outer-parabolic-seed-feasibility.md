# L-24507 — Certified outer feasibility of the parabolic seed

Claim ID: `L-24507`  
Status: `PROPOSED COMPLETE — elementary proof plus exact rational finite certificate`  
Scope: all integer constraints in the fixed outer ratio  
Issue: #245  
Depends on: `L-24504`, `L-24505`, `X-24501`

Let

\[
b_X^{(0)}(m)=\sqrt X\,B(m/X),
\qquad
B(t)=2\sqrt t\left[\log(1/t)-2(1-\sqrt t)\right].
\]

For an integer `q<=X`, put

\[
v_q(b_X^{(0)})=\sum_{kq\le X}
\left(b_X^{(0)}(kq)-b_X^{(0)}(kq+1)\right),
\]

with `b_X^(0)(X+1)=0`, and

\[
w_X(q)=q^{-1/2}\log(X/q).
\]

Then the seed is already feasible in the full outer region.

## Theorem

For every integer

\[
X\ge104301
\]

and every integer `q` satisfying

\[
\frac X{28}\le q\le X,
\]

one has

\[
\boxed{v_q(b_X^{(0)})\le w_X(q).}
\tag{L-24507.1}
\]

This is stronger than needed: `q` need not be a prime power.

## 1. Continuum profile and its certified margin

Differentiate `B` and put `g=-B'`. Then

\[
B'(t)=\frac{4\sqrt t-\log t-4}{\sqrt t},
\qquad
\boxed{g(t)=\frac{\log t+4}{\sqrt t}-4.}
\tag{L-24507.2}
\]

For

\[
\frac1{N+1}<\theta\le\frac1N,
\]

the continuum residual of `L-24504/L-24505` is

\[
E_N(\theta)
=\theta^{-1/2}
\left[A_N+(H_N+1)\log\theta+4H_N\right]-4N,
\tag{L-24507.3}
\]

where

\[
H_N=\sum_{k=1}^Nk^{-1/2},
\qquad
A_N=\sum_{k=1}^Nk^{-1/2}\log k.
\]

Its derivative changes sign at most once. The global maximum of the same formula over all `theta>0` is

\[
\boxed{
M_N=
2(H_N+1)
\exp\left(\frac{A_N+2H_N-2}{2(H_N+1)}\right)-4N.}
\tag{L-24507.4}
\]

`X-24501` uses only integers and `fractions.Fraction`, with rigorous atanh-series bounds for logarithms, Taylor bounds for exponentials, and dyadic square-root intervals. It certifies exactly

\[
\boxed{M_N<-\frac1{50}\qquad(2\le N\le27).}
\tag{L-24507.5}
\]

The weakest cell is `N=27`, whose non-authoritative decimal upper endpoint is approximately

```text
-0.0230503319867433.
```

For `N=1`, direct substitution gives

\[
E_1(\theta)=4\left(\frac{1+\log\sqrt\theta}{\sqrt\theta}-1\right)\le0
\qquad(0<\theta\le1),
\]

by `log r<=r-1`, with equality only at `theta=1`.

At `theta=1/28`, the additional `k=28` term equals `g(1)=0`, so the value agrees with the adjacent `N=27` boundary. Consequently

\[
\boxed{E(\theta)\le-\frac1{50}
\qquad\left(\frac1{28}\le\theta\le\frac12\right).}
\tag{L-24507.6}
\]

## 2. Uniform finite-difference remainder

Put

\[
\theta=\frac qX,
\qquad h=\frac1X.
\]

For every term with `kq<X`, the fundamental theorem of calculus gives

\[
\sqrt X\left(b_X^{(0)}(kq)-b_X^{(0)}(kq+1)\right)
=
\frac1h\int_{k\theta}^{k\theta+h}g(u)\,du.
\tag{L-24507.7}
\]

If `kq=X`, both the discrete term and the continuum comparison term `g(1)` are zero.

Now

\[
g'(t)=-t^{-3/2}\left(1+\frac12\log t\right).
\tag{L-24507.8}
\]

On `1/28<=t<=1`, one has

\[
\left|1+\frac12\log t\right|\le1.
\]

Indeed `log 28<4`, while `log t<=0`. Also

\[
28^{3}<149^2.
\]

Therefore

\[
\boxed{|g'(t)|<149
\qquad(1/28\le t\le1).}
\tag{L-24507.9}
\]

An interval average over length `h` differs from its left endpoint by at most `149h/2`. There are at most `28` summands, hence

\[
\boxed{
\left|
\sqrt X\,v_q(b_X^{(0)})
-\sum_{kq\le X}g(k\theta)
\right|
\le\frac{2086}{X}.}
\tag{L-24507.10}
\]

Since

\[
\sqrt X\,w_X(q)=\theta^{-1/2}\log(1/\theta),
\]

(L-24507.6) and (L-24507.10) give, for `1/28<=theta<=1/2`,

\[
\sqrt X\left(v_q(b_X^{(0)})-w_X(q)\right)
\le-\frac1{50}+\frac{2086}{X}<0
\]

whenever `X>=104301`.

## 3. The one-term region

Suppose `1/2<=theta<1`. Then only `k=1` occurs. On `[1/2,1]`, `g` is decreasing because `B''(t)>0`. Thus

\[
\sqrt X\,v_q(b_X^{(0)})
\le g(\theta).
\]

Furthermore

\[
\theta^{-1/2}\log(1/\theta)-g(\theta)
=
\frac{2}{\sqrt\theta}
\left[
\log(1/\theta)-2(1-\sqrt\theta)
\right]\ge0,
\]

because, with `r=sqrt(theta)`,

\[
-\log r\ge1-r.
\]

Hence (L-24507.1) also holds throughout the one-term region. At `q=X`, both sides are zero.

## Consequence

Every positive seed excess for sufficiently large `X` lies in

\[
\boxed{q<X/28.}
\tag{L-24507.11}
\]

The outer-sign step of the two-stage PNC program is therefore closed. The remaining correction theorem may assume a fixed multiplicative reserve of at least `28`.

## Exact replay

```bash
python experiments/X-24501-outer-parabolic-seed/verify.py
```

Expected verdict:

```text
PASS_EXACT_OUTER_PARABOLIC_SEED_MARGIN
```

## Status boundary

The theorem closes only the uncorrected outer region. It does not prove the low-ratio primitive-neighbor correction or RH.
