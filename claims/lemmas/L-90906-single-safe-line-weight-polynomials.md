# L-90906 — The one-safe-line Euler weights have one sign change and a sharp root window

Claim ID: `L-90906`  
Status: **PROPOSED COMPLETE EXACT POLYNOMIAL THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: `L-90905`, especially the one-line prime polynomial `P_k`  
RH status: **unproved**

## 1. Purpose

The order-`k` single-safe-line criterion of `T-90903` has prime part

\[
 \sum_{n\ge2}\Lambda(n)n^{-3/2-ix}P_k(\log n).
\]

This note identifies an exact raising recurrence for `P_k`, proves that it has
exactly one positive zero, and locates that zero in a unit-width window for its
square.  The sign transition occurs at logarithmic scale

\[
 \log n\sim\sqrt{2k}.
\]

This is the discrete counterpart of the first-Hermite heat saddle.

## 2. Exact polynomial recurrence

Let `P_k` be defined by (L-90905.14), and put

\[
 Q_k(t)=2^{k+1}P_k(t).
\tag{L-90906.1}
\]

For a single Euler exponential `mathscr X(s+r)=e^{-t(s+r)}`, the differential
operator (L-90905.5) has the homogeneous form

\[
 \left(-\frac1{2r}\frac d{dr}\right)^k
 \frac{e^{-tr}}{2r^3}(1+tr-t^2r^2)
 =\frac{e^{-tr}}{2^{k+1}r^{2k+3}}Q_k(tr).
\tag{L-90906.2}
\]

Therefore

\[
 \boxed{
 Q_0(t)=1+t-t^2,
 \qquad
 Q_{k+1}(t)=(t+2k+3)Q_k(t)-tQ_k'(t).
 }
\tag{L-90906.3}
\]

If

\[
 Q_k(t)=\sum_{j=0}^{k+2}q_{k,j}t^j,
\]

then

\[
 \boxed{
 q_{k+1,j}=q_{k,j-1}+(2k+3-j)q_{k,j},
 }
\tag{L-90906.4}
\]

with out-of-range coefficients zero.  In particular

\[
 q_{k,0}=(2k+1)!!,
 \qquad
 q_{k,k+2}=-1.
\tag{L-90906.5}
\]

## 3. Exactly one positive zero

The coefficient row of `Q_0` is

\[
 (1,1,-1),
\]

with exactly one sign variation.  Suppose a row has at most one sign variation.
The update (L-90906.4) is a positive combination of adjacent entries, because

\[
 2k+3-j>0
 \qquad(0\le j\le k+2).
\]

Before the old sign boundary both summands are nonnegative; two positions after
it both are nonpositive; only the new boundary entry is undetermined.  Hence the
number of sign variations cannot increase.

The new constant coefficient is positive and the new leading coefficient is
negative, so the new row has at least one variation.  Inductively every row has
exactly one.

By Descartes' rule of signs and the opposite signs at zero and infinity,

\[
 \boxed{
 Q_k\text{ has exactly one positive zero }\tau_k,
 }
\tag{L-90906.6}
\]

counted with multiplicity.  It is therefore simple, with

\[
 Q_k(t)>0\quad(0\le t<\tau_k),
 \qquad
 Q_k(t)<0\quad(t>\tau_k).
\tag{L-90906.7}
\]

## 4. Monotonicity of the sign boundary

At the positive zero of `Q_k`, (L-90906.3) gives

\[
 Q_{k+1}(\tau_k)=-\tau_kQ_k'(\tau_k)>0.
\]

Since `Q_(k+1)` has one positive zero and is eventually negative,

\[
 \boxed{\tau_{k+1}>\tau_k.}
\tag{L-90906.8}
\]

## 5. Gamma--Bessel representation

For `t>0`,

\[
 \boxed{
 e^{-t}P_k(t)
 =\frac1{\sqrt\pi}
 \int_0^\infty
 q^{k+1/2}e^{-q-t^2/(4q)}
 \left(1-\frac{t^2}{2q}\right)dq.
 }
\tag{L-90906.9}
\]

Equivalently,

\[
 e^{-t}P_k(t)
 =\frac2{\sqrt\pi}\left[
 (t/2)^{k+3/2}K_{k+3/2}(t)
 -\frac{t^2}{2}(t/2)^{k+1/2}K_{k+1/2}(t)
 \right].
\tag{L-90906.10}
\]

This is the exact Gamma average of the first-Hermite prime weight.

## 6. Sharp root window

Put

\[
 J_\nu(t)=\int_0^\infty q^{\nu-1}e^{-q-t^2/(4q)}dq,
 \qquad
 R_\nu(t)=\frac{J_\nu(t)}{J_{\nu-1}(t)}.
\]

Integration by parts gives

\[
 J_{\nu+1}=\nu J_\nu+\frac{t^2}{4}J_{\nu-1},
 \qquad
 R_\nu=(\nu-1)+\frac{t^2}{4R_{\nu-1}}.
\tag{L-90906.11}
\]

Equation (L-90906.9) shows that the sign of `P_k(t)` is the sign of

\[
 R_{k+3/2}(t)-\frac{t^2}{2}.
\tag{L-90906.12}
\]

For `nu>2`, (L-90906.11) implies

\[
 \nu-1<R_\nu(t)
 <\nu-1+\frac{t^2}{4(\nu-2)}.
\tag{L-90906.13}
\]

For `k>=3`, apply these bounds once at `nu=k+1/2` and once at
`nu=k+3/2`.  At `t^2=2k+2` they give

\[
 R_{k+3/2}(t)>k+1=t^2/2,
\]

whereas at `t^2=2k+3` they give

\[
 R_{k+3/2}(t)<k+3/2=t^2/2.
\]

The cases `k=0,1,2` follow directly from

\[
\begin{aligned}
 Q_0(t)&=1+t-t^2,\\
 Q_1(t)&=3+3t-t^3,\\
 Q_2(t)&=15+15t+3t^2-2t^3-t^4.
\end{aligned}
\]

Hence for every `k>=0`,

\[
 \boxed{
 \sqrt{2k+2}<\tau_k<\sqrt{2k+3}.
 }
\tag{L-90906.14}
\]

In particular

\[
 \tau_k^2=2k+2+\theta_k,
 \qquad 0<\theta_k<1,
\tag{L-90906.15}
\]

and

\[
 \tau_k=\sqrt{2k+2}+O(k^{-1/2}).
\tag{L-90906.16}
\]

## 7. Arithmetic interpretation

The order-`k` Euler weight changes sign exactly once:

```text
P_k(log n)>0  for n<exp(tau_k),
P_k(log n)<0  for n>exp(tau_k),
tau_k^2 in (2k+2,2k+3).
```

Thus the integer derivative order selects the same parabolic logarithmic scale
as heat time `q approximately k`.  This gives a precise target for any future
summation-by-parts, total-positivity, or prime-cancellation attack.

It does not prove the RH-equivalent sign of `T-90903`.
