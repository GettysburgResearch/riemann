# L-90423 — The unique critically phase-locked factor-16 annular filter

Claim ID: `L-90423`  
Title: Exact factor-16 support and nonnegative critical-line phase lock force one quartic filter, whose prime scalar is zero-safe and directly RH-equivalent  
Status: **PROPOSED COMPLETE EXACT THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-11  
Dependencies: elementary Mellin transformation and the classical von Koch consequence of RH  
Scope: one complete-prime-power scalar and its critical-scale filter; no unconditional critical-growth estimate or proof of RH

## 1. Endpoint primitive

Put

\[
\mathcal H(X)
 =\sum_{n\le X}\Lambda(n)\left(\frac{2n}{X}-1\right),
\qquad X\ge1,
\tag{L-90423.1}
\]

with the sum empty below two. For `Re z>1`, finite switching gives

\[
\boxed{
\int_1^\infty \mathcal H(X)X^{-z-1}\,dX
 =\frac{z-1}{z(z+1)}
  \left(-\frac{\zeta'}{\zeta}(z)\right).
}
\tag{L-90423.2}
\]

The factor `z-1` cancels the pole of `-zeta'/zeta` at one.

Let

\[
Q_*(y)
 =(1-y)(1-2y)(2-y)(1-4y)
 =2-15y+35y^2-30y^3+8y^4.
\tag{L-90423.3}
\]

Define the filtered scalar

\[
\boxed{
\begin{aligned}
\mathcal S_*(X)
={}&2\mathcal H(X)-15\mathcal H(X/2)
 +35\mathcal H(X/4)\\
&-30\mathcal H(X/8)+8\mathcal H(X/16).
\end{aligned}}
\tag{L-90423.4}
\]

Then

\[
\boxed{
\int_1^\infty \mathcal S_*(X)X^{-z-1}\,dX
 =Q_*(2^{-z})\frac{z-1}{z(z+1)}
  \left(-\frac{\zeta'}{\zeta}(z)\right).
}
\tag{L-90423.5}
\]

## 2. Exact factor-16 annular support

For a finite filter `P(y)=sum_(r=0)^4 p_r y^r`, the coefficient of one prime power `n=uX` in

\[
\sum_{r=0}^4p_r\mathcal H(X/2^r)
\]

is, whenever all five scales are active,

\[
2uP(2)-P(1).
\tag{L-90423.6}
\]

Hence exact disappearance below `X/16` is equivalent to

\[
P(1)=P(2)=0.
\tag{L-90423.7}
\]

For `Q_*` this holds. The remaining piecewise-linear annular kernel is

\[
\boxed{
W_*(u)=
\begin{cases}
8-256u,&1/16<u\le1/8,\\
224u-22,&1/8<u\le1/4,\\
13-56u,&1/4<u\le1/2,\\
4u-2,&1/2<u\le1,\\
0,&\text{otherwise}.
\end{cases}}
\tag{L-90423.8}
\]

Thus

\[
\mathcal S_*(X)
 =\sum_{X/16<n\le X}\Lambda(n)W_*(n/X)
\tag{L-90423.9}
\]

up to the harmless convention at the four band endpoints.

## 3. Critical-line phase lock

Let `Re z=1/2` and put `y=2^-z`. Then

\[
y\overline y=\frac12,
\qquad
\frac1{2y}=\overline y.
\]

The paired factors satisfy

\[
(1-y)(1-2y)=-2y|1-y|^2,
\tag{L-90423.10}
\]

and

\[
(2-y)(1-4y)=-8y|1-y/2|^2.
\tag{L-90423.11}
\]

Therefore

\[
\boxed{
2^{2z}Q_*(2^{-z})
 =16|1-2^{-z}|^2|1-2^{-z-1}|^2
 \in\mathbf R_{>0}.
}
\tag{L-90423.12}
\]

In fact, uniformly on the critical line,

\[
\boxed{
43-30\sqrt2
 \le 2^{2z}Q_*(2^{-z})
 \le43+30\sqrt2.
}
\tag{L-90423.13}
\]

The lower constant is positive because `43^2>2*30^2`.

Thus the finite dyadic multiplier has no phase loss and no spectral zero on the critical line.

## 4. Uniqueness at quartic order

Consider a real quartic `P` with exact factor-16 support, so `P(1)=P(2)=0`, and suppose its centered critical-line symbol has constant real phase: `y^-2 P(y)` is real on `|y|=1/sqrt(2)`.

The latter is the self-inversive root symmetry

\[
\alpha\longmapsto\frac1{2\overline\alpha}.
\tag{L-90423.14}
\]

Hence the root `1` forces `1/2`, and the root `2` forces `1/4`. A quartic has no room for another root. Therefore

\[
P(y)=c(1-y)(1-2y)(2-y)(1-4y).
\tag{L-90423.15}
\]

The requirement of nonnegative rather than nonpositive critical phase fixes `c>0`.

Consequently `Q_*` is, up to positive scale, the unique minimal-degree filter simultaneously having

```text
exact factor-16 support;
critical-line phase lock;
no critical-line zero.
```

The main-pole root `y=1/2` is not separately imposed: it is forced by phase locking of the annular root `y=1`.

## 5. Zero safety and RH equivalence

The zeros of `Q_*(2^-z)` lie on the vertical lines

\[
\operatorname{Re}z\in\{-1,0,1,2\}.
\tag{L-90423.16}
\]

Therefore no nontrivial zeta zero with

\[
\frac12<\operatorname{Re}\rho<1
\]

is cancelled in (L-90423.5).

Under RH, von Koch gives

\[
\psi(X)-X=O(\sqrt X\log^2(2X)),
\]

and hence

\[
\mathcal S_*(X)=O(\sqrt X\log^2(2X)).
\tag{L-90423.17}
\]

Conversely, if for every `epsilon>0`

\[
\mathcal S_*(X)=O_\epsilon(X^{1/2+\epsilon}),
\tag{L-90423.18}
\]

then (L-90423.5) is holomorphic in every half-plane `Re z>1/2+epsilon`. Its zero-safe multiplier excludes a pole from any zeta zero there. Letting `epsilon` tend to zero and using the functional equation gives RH.

Thus

\[
\boxed{
\mathrm{RH}
\Longleftrightarrow
\mathcal S_*(X)=O_\epsilon(X^{1/2+\epsilon})
\quad\text{for every }\epsilon>0.
}
\tag{L-90423.19}
\]

## 6. Significance and boundary

Unlike the earlier factor-16 mean filter, `Q_*` is not merely zero-safe. It is critically phase locked, uniformly invertible on the critical line, exactly annular, and uniquely forced by those requirements.

This theorem does **not** prove the growth estimate (L-90423.18). It nominates a better-conditioned arithmetic scalar and supplies the exact finite filter through which a future source, reflected, or scale-energy proof must operate.

Closed exactly here:

1. Mellin transform;
2. factor-16 support;
3. explicit annular kernel;
4. critical Fejer phase lock and uniform bounds;
5. quartic uniqueness;
6. open-strip zero safety;
7. direct RH equivalence.

Open:

1. unconditional critical growth of `S_*`;
2. any prime-side positive decomposition proving that growth;
3. RH.