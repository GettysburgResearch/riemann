# L-90014 — The prime-power moat is globally negative and decreasing

Claim ID: `L-90014` (provisional range; branch-qualified)  
Title: A finite directed base certificate plus the analytic tail theorem closes the zero-insensitive moat for every real endpoint  
Status: **PROPOSED COMPLETE GLOBAL THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Date: 2026-08-09  
Depends on: `L-90012`; the exact prefix identities of `T-90009`  
Scope: the moat `M` only; no sign theorem for the RH-sensitive complete deficit

## 1. Statement

Retain the prime-power moat

\[
 \mathfrak M(X)=A(X)-\Delta_\Lambda(X)
\]

from `L-90009`. Then:

\[
\boxed{
 X\mathfrak M'(X)<-0.30
}
\tag{L-90014.1}
\]

for every noninteger real `X>=2`, and

\[
\boxed{
 \mathfrak M(X)<-4\sqrt2-0.30\log(X/2)<0
 \qquad(X\ge2).
}
\tag{L-90014.2}
\]

In particular `M` is continuous, strictly decreasing, and strictly negative on
the entire natural domain `[2,infinity)`.

`L-90012` already proves (L-90014.1) for `X>=2000`. The purpose of this lemma
is to close the finite base exactly and to identify the particularly simple
interval maximization used by the certificate.

## 2. Exact interval derivative

Let

\[
 d(m)=\log\operatorname{rad}(m)-\log\operatorname{rad}(m-1),
\]

\[
 S_{1/2}(N)=\sum_{m\le N}\sqrt m\,d(m),
 \qquad
 S_1(N)=\sum_{m\le N}m\,d(m),
\]

and

\[
 \vartheta_{1/2}(N)=\sum_{p\le N}{\log p\over\sqrt p},
 \qquad
 \psi_{1/2}(N)=\sum_{n\le N}{\Lambda(n)\over\sqrt n}.
\]

`T-90009` gives, for `X in (N,N+1)`,

\[
 \mathcal D_XA(X)
 =2S_{1/2}(N)-{2S_1(N)\over\sqrt X}
 -\vartheta_{1/2}(N),
\]

while

\[
 \mathcal D_X\Delta_\Lambda(X)
 =2\sqrt X-\psi_{1/2}(N).
\]

Therefore

\[
\boxed{
 \mathcal D_X\mathfrak M(X)
 =C_N-{2S_1(N)\over\sqrt X}-2\sqrt X,
}
\tag{L-90014.3}
\]

where

\[
\boxed{
 C_N=2S_{1/2}(N)-\vartheta_{1/2}(N)+\psi_{1/2}(N).
}
\tag{L-90014.4}
\]

Every quantity except `X` is a finite endpoint prefix.

## 3. Exact maximization on one interval

Put `y=sqrt(X)`. The variable part of (L-90014.3) is

\[
 -{2S_1(N)\over y}-2y.
\]

Its derivative in `y` is

\[
 {2S_1(N)\over y^2}-2.
\]

Consequently the maximum on the closed interval

\[
 \sqrt N\le y\le\sqrt{N+1}
\]

is attained at exactly one of the following:

\[
\boxed{
 y_N^*=\begin{cases}
 \sqrt N,&S_1(N)\le N,\\
 \sqrt{S_1(N)},&N<S_1(N)<N+1,\\
 \sqrt{N+1},&S_1(N)\ge N+1.
 \end{cases}}
\tag{L-90014.5}
\]

Thus no mesh or calculus approximation is needed. A finite interval is closed
by evaluating one explicitly selected radical expression.

## 4. Directed finite base

`X-90014` constructs directed interval enclosures for:

```text
log rad(m),
S_1/2(N), S_1(N),
theta_1/2(N), psi_1/2(N),
C_N,
and the value of (L-90014.3) at y_N^*.
```

Every interval

\[
 (N,N+1),\qquad2\le N<2000,
\]

is certified strictly negative. More precisely,

\[
\boxed{
 \sup_{2<X<2000,\ X\notin\mathbb Z}
 \mathcal D_X\mathfrak M(X)
 \le-2.82842712474619<-2.82.
}
\tag{L-90014.6}
\]

The least-negative interval is the first one, `(2,3)`. At its left limit the
value is exactly

\[
 -2\sqrt2.
\]

The branch inventory of the maximizer is also retained:

```text
left endpoint:   657 intervals;
right endpoint: 1337 intervals;
interior critical point: 4 intervals.
```

These counts are diagnostic only; the directed upper bounds are the proof
object.

## 5. Initial value

At `X=2`, every endpoint seed and ramp term vanishes at its own support point,
so

\[
 A(2)=0.
\]

The complete prime-power ramp also vanishes at `X=2`, hence

\[
 \Delta_\Lambda(2)=4\sqrt2.
\]

Therefore

\[
\boxed{
 \mathfrak M(2)=-4\sqrt2.
}
\tag{L-90014.7}
\]

## 6. Global completion

The directed finite base gives

\[
 \mathcal D_X\mathfrak M(X)<-2.82<-0.30
 \qquad(2<X<2000),
\]

while `L-90012` gives

\[
 \mathcal D_X\mathfrak M(X)<-0.30
 \qquad(X\ge2000).
\]

The moat is continuous at integer endpoints because every newly entering seed
or ramp summand vanishes at its own endpoint. Hence (L-90014.1) holds on every
open interval and integrates globally against `dX/X`:

\[
 \mathfrak M(X)-\mathfrak M(2)
 < -0.30\log(X/2).
\]

Using (L-90014.7) proves (L-90014.2).

## 7. Meaning for the RH-facing gate

The decomposition

\[
 A(X)=\Delta_\Lambda(X)+\mathfrak M(X)
\]

now has a completely closed correction term on its full domain:

```text
M is explicit;
M carries no original zeta-zero pole;
M<0 for every X>=2;
M is strictly decreasing for every X>=2.
```

Accordingly, every unresolved sign of `A`, every possible upward endpoint
movement, and every RH-sensitive oscillation belongs to the complete
prime-power coordinate `Delta_Lambda`.

This global moat theorem does **not** imply

\[
 \Delta_\Lambda(X)<-\mathfrak M(X),
\]

which remains the one-scalar RH-equivalent upper wall.

## 8. Proof boundary

Closed globally, subject to review:

1. the exact interval derivative;
2. the exact one-candidate maximization rule;
3. all directed intervals below 2000;
4. the exact initial value `M(2)=-4sqrt(2)`;
5. global strict negativity;
6. global strict decrease;
7. the quantitative bound (L-90014.2).

Imported tail theorem:

- `L-90012` for `X>=2000`.

Still open:

1. the weighted-Chebyshev upper wall;
2. endpoint negativity or monotonicity of `A`;
3. RH.

Replay: `experiments/X-90014-global-moat-base/certify.py`.
