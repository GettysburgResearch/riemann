# R-25301 — Monotone Divisibility Cover has unavoidable square-root cost

Claim ID: `R-25301`  
Title: The nonnegative tail-cover repair of the parabolic carry seed must lose a fixed multiple of `sqrt(X)` and cannot preserve the sharp entropy constant  
Status: **EXACT REFUTATION OF ROUTE A IN PR #248**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-07  
Issue: #253  
Base: PR #248 at `c2a34e282f65ca0d890dc55e5e2fba08bed140c9`  
Dependencies: PR #248 `L-24501`, `L-24502`, `L-24504`, `L-24505`; the prime number theorem  
Scope: refutes the monotone nonnegative `alpha_m` Divisibility Cover; does not refute signed adjacent-flow or primitive-neighbor transport

## 1. Parabolic seed and constraint defect

Retain the divisor-gradient coordinates of `L-24501`. For

\[
b_X^{(0)}(m)
=
2\sqrt m
\left[
 \log\frac Xm
 -2\left(1-\sqrt{\frac mX}\right)
\right],
\qquad 2\le m\le X,
\tag{R-25301.1}
\]

put

\[
v_q(b)
=
\sum_{kq\le X}\bigl(b_{kq}-b_{kq+1}\bigr),
\qquad
w_X(q)=q^{-1/2}\log\frac Xq,
\tag{R-25301.2}
\]

with `b_(X+1)=0`, and define the positive seed excess

\[
e_X(q)=\bigl(v_q(b_X^{(0)})-w_X(q)\bigr)_+.
\tag{R-25301.3}
\]

The monotone Divisibility Cover proposed in `L-24502` asks for
nonnegative numbers `alpha_m` such that

\[
\sum_{kq\le X}\alpha_{kq}\ge e_X(q)
\qquad(q=p^a\le X),
\tag{R-25301.4}
\]

while the objective loss

\[
\mathcal C_X(\alpha)
=
\sum_{m=2}^{X}\alpha_m\log m
\tag{R-25301.5}
\]

is only polylogarithmic.

The tail-capacity condition of `L-24502` is irrelevant to the obstruction below:
already (R-25301.4) forces square-root cost.

## 2. Exact von-Mangoldt dual charge

For every nonnegative `alpha`,

\[
\begin{aligned}
\mathcal C_X(\alpha)
&=
\sum_{m\le X}\alpha_m
 \sum_{\substack{q=p^a\\q\mid m}}\Lambda(q)\\
&=
\sum_{q=p^a\le X}\Lambda(q)
 \sum_{kq\le X}\alpha_{kq}.
\end{aligned}
\tag{R-25301.6}
\]

The first equality is exact because

\[
\sum_{\substack{q=p^a\\q\mid m}}\Lambda(q)
=
\sum_{p}v_p(m)\log p
=
\log m.
\tag{R-25301.7}
\]

Consequently every cover satisfying (R-25301.4) obeys

\[
\boxed{
\mathcal C_X(\alpha)
\ge
\sum_{q=p^a\le X}\Lambda(q)e_X(q).
}
\tag{R-25301.8}
\]

This is a weak-dual certificate, not an estimate produced by a numerical LP.

## 3. Uniform positive continuum band

Write

\[
b_X^{(0)}(m)=\sqrt X\,B(m/X),
\]

where

\[
B(t)=
2\sqrt t\left[\log(1/t)-2(1-\sqrt t)\right]
\qquad(0<t\le1)
\tag{R-25301.9}
\]

and extend `B(t)=0` for `t>=1`. Then `B` is `C^1` at `1`,
`B'(1)=0`, and `B'` is Lipschitz on every interval bounded away from zero.

For

\[
\theta=\frac qX\in\left[\frac1{40},\frac1{37}\right],
\]

the number of multiples `kq<=X` is at most forty. Uniformly on this
fixed interval,

\[
\begin{aligned}
\sqrt X\,v_q(b_X^{(0)})
&=
X\sum_{kq\le X}
 \left[
  B(k\theta)-B\left(k\theta+\frac1X\right)
 \right]\\
&=
-\sum_{k\le1/\theta}B'(k\theta)+O(X^{-1}),
\end{aligned}
\tag{R-25301.10}
\]

while

\[
\sqrt X\,w_X(q)
=
\theta^{-1/2}\log(1/\theta)
\tag{R-25301.11}
\]

exactly. Hence

\[
\sqrt X\,[v_q(b_X^{(0)})-w_X(q)]
=
E(\theta)+O(X^{-1})
\tag{R-25301.12}
\]

uniformly, where

\[
E(\theta)=
-\sum_{1\le k\le1/\theta}B'(k\theta)
-\theta^{-1/2}\log(1/\theta).
\tag{R-25301.13}
\]

On the reciprocal cell

\[
\frac1{N+1}<\theta\le\frac1N,
\]

put

\[
H_N=\sum_{k=1}^N k^{-1/2},
\qquad
A_N=\sum_{k=1}^N k^{-1/2}\log k.
\]

The exact formula of `L-24505` is

\[
E(\theta)
=
\theta^{-1/2}
\left[
 A_N+(H_N+1)\log\theta+4H_N
\right]
-4N.
\tag{R-25301.14}
\]

Its derivative has the sign of

\[
D_N(\theta)
=
(H_N+1)
-\frac12
\left[
 A_N+(H_N+1)\log\theta+4H_N
\right].
\tag{R-25301.15}
\]

The function `D_N` decreases with `theta`. Exact rational interval
arithmetic in `X-25301` proves

\[
D_N\left(\frac1{N+1}\right)<0
\qquad(N=37,38,39)
\tag{R-25301.16}
\]

and

\[
\boxed{
E(1/37)>2/5.
}
\tag{R-25301.17}
\]

The numerical diagnostics, not used as proof, are

\[
\begin{array}{c|c}
N&D_N(1/(N+1))\\ \hline
37&-0.25714744\ldots\\
38&-0.26417304\ldots\\
39&-0.27100776\ldots
\end{array}
\]

and

\[
E(1/37)=0.43770440\ldots.
\]

At reciprocal-cell boundaries the entering summand equals `-B'(1)=0`,
so `E` is continuous. Therefore (R-25301.16)--(R-25301.17) give

\[
\boxed{
E(\theta)>2/5
\qquad
\left(\frac1{40}\le\theta\le\frac1{37}\right).
}
\tag{R-25301.18}
\]

By uniformity in (R-25301.12), for all sufficiently large `X` and every
prime `p` in this interval,

\[
\boxed{
e_X(p)\ge\frac1{4\sqrt X}.
}
\tag{R-25301.19}
\]

## 4. Square-root lower bound

Let

\[
\vartheta(y)=\sum_{p\le y}\log p.
\]

The prime number theorem gives

\[
\vartheta(X/37)-\vartheta(X/40)
=
\left(\frac1{37}-\frac1{40}+o(1)\right)X
=
\left(\frac3{1480}+o(1)\right)X.
\tag{R-25301.20}
\]

In particular, for all sufficiently large `X`,

\[
\vartheta(X/37)-\vartheta(X/40)\ge\frac X{1000}.
\tag{R-25301.21}
\]

Using only prime rows in (R-25301.8) and (R-25301.19),

\[
\boxed{
\mathcal C_X(\alpha)
\ge
\frac1{4\sqrt X}
\sum_{X/40\le p\le X/37}\log p
\ge
\frac{\sqrt X}{4000}.
}
\tag{R-25301.22}
\]

Thus no monotone Divisibility Cover can satisfy

\[
\mathcal C_X(\alpha)=X^{o(1)}
\]

and in particular none can have cost `O(log^A X)` for any fixed `A`.

## 5. Consequence for PR #248

The seed itself has

\[
J_X(b_X^{(0)})=4\sqrt X+O(\log X).
\]

A monotone cover subtracts precisely the cost (R-25301.5). Equation
(R-25301.22) therefore destroys a fixed square-root amount of the sharp
constant. The finite LP costs reported in `O-24501` were not trending toward
polylogarithmic size; they were beginning to resolve this square-root law.

Accordingly,

```text
Divisibility Cover D1 + D3             INCOMPATIBLE
route A of PR #248                      REFUTED
parabolic seed                          RETAINED
divisor-gradient coordinate             RETAINED
signed adjacent-flow calculus           RETAINED
primitive-neighbor ledger               RETAINED
RH                                      UNPROVED
```

## 6. What the refutation does not show

The proof does not refute a signed repair. It uses positivity of `alpha_m`
at the exact step (R-25301.8). A signed adjacent flow may move positive
constraint defect into already available negative slack and pay only the
transport cost

\[
\sum_j F_j\log\frac{j^2}{j^2-1},
\]

rather than the full positive dual mass.

That cancellation is now the only viable parabolic-seed mechanism. It is
formalized in `L-25301` and `T-25301`.

## 7. Proof boundary

Exact in this claim:

- the von-Mangoldt dual identity;
- the uniform finite-difference limit;
- the reciprocal-cell reduction;
- the rational sign certificate on `[1/40,1/37]`;
- the square-root cost lower bound.

Imported classical input:

- the prime number theorem in the form (R-25301.20).

Not proved:

- a signed constraint-dipole transport;
- the sharp prime-ramp lower bound;
- RH.
