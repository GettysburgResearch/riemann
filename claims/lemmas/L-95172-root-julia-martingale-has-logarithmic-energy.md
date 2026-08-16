# L-95172 — The dyadic root Julia state has an exact alternating martingale and logarithmic energy

Claim ID: `L-95172`  
Status: **PROPOSED COMPLETE EXACT ENERGY THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-17  
Depends on: `L-95171`  
Scope: multiplicative divisor dynamics and weighted source energy; no additive trace-free extraction

## 1. Positive divisor transition

For `n>1`, define

\[
P_n(d)
={\Lambda_2(d)g_2(n/d)\over g_2(n)\log n},
\qquad d\mid n,\ d>1.
\tag{L-95172.1}
\]

By (L-95171.6), `P_n(d)>=0` and

\[
\sum_{d\mid n,d>1}P_n(d)=1.
\tag{L-95172.2}
\]

Put

\[
f_2(n)={b_2(n)\over g_2(n)}\in[-1,1].
\tag{L-95172.3}
\]

Equation (L-95171.7) gives

\[
\boxed{
f_2(n)=-\sum_{d\mid n,d>1}P_n(d)f_2(n/d).
}
\tag{L-95172.4}
\]

Thus if `N_{t+1}=N_t/d` is chosen using `P_{N_t}`, then

\[
\boxed{(-1)^t f_2(N_t)\text{ is a bounded martingale.}}
\tag{L-95172.5}
\]

The channel flip is exact, not an inequality.

## 2. Exact support and Hilbert energy

For odd squarefree `m`, the only nonzero dyadic fibres are

\[
\begin{array}{c|c|c|c}
 n&b_2(n)&g_2(n)&b_2(n)^2/[g_2(n)n]\\ \hline
 m&\mu(m)&1&1/m\\
 2m&-2\mu(m)&2&1/m\\
 4m&\mu(m)&3&1/(12m).
\end{array}
\]

All other fibres contribute zero. Therefore, with `H_X=sum_(m<=X)1/m`,

\[
\begin{aligned}
\sum_{n\le X}{b_2(n)^2\over g_2(n)n}
&\le H_X+H_{X/2}+{1\over12}H_{X/4}\\
&\le {25\over12}(1+\log X).
\end{aligned}
\]

Hence

\[
\boxed{
\sum_{n\le X}{b_2(n)^2\over g_2(n)n}
\le {25\over12}(1+\log X).
}
\tag{L-95172.6}
\]

This is the natural Hilbert energy of the signed channel relative to its positive trace.

## 3. Positive mass is also logarithmic

Writing `n=2^e m` with `m` odd,

\[
{g_2(n)\over n}={e+1\over2^e m}.
\]

Since

\[
\sum_{e\ge0}{e+1\over2^e}=4,
\]

one obtains the safe bound

\[
\boxed{
\sum_{n\le X}{g_2(n)\over n}
\le4(1+\log X).
}
\tag{L-95172.7}
\]

Thus both the positive source mass and the signed square function are logarithmic.

## 4. What the energy does and does not buy

The energy theorem rules out the idea that the dyadic root channel is intrinsically macroscopic after the correct positive normalization. It does not by itself construct a scalar positive carry flow. A scalar absolute-value projection replaces `b_2` by `g_2`, destroys the alternating martingale, and reintroduces the Farkas obstruction identified by `R-95040`.

The remaining map must therefore preserve the channel covariance and charge the off-diagonal energy, not the trace.

## 5. Boundary

```text
positive divisor Markov kernel          EXACT
alternating root martingale              EXACT
root Hilbert energy O(log X)             EXACT
positive trace mass O(log X)             EXACT
matrix-to-scalar trace-free extraction   OPEN
Cycle Debt / RH                          UNPROVED
```
