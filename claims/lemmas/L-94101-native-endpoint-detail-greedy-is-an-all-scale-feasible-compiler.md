# L-94101 — The native endpoint-detail greedy is an unconditional all-scale feasible physical compiler

Claim ID: `L-94101`  
Status: **PROVED EXACT FINITE CONSTRUCTION FOR EVERY ENDPOINT**  
Created: 2026-08-16  
Primary inputs: `L-94100`; the exact positive radix-four dual `L-91378`  
RH status: **unproved**

## 1. Native target and generator dictionary

For integer `X>=3`, let

\[
 w_X(q)=\frac1{\sqrt q}\log\frac Xq\,\mathbf1_{q\le X},
\]

\[
 \Omega_X(q)=w_X(q)-2w_X(4q).
 \tag{L-94101.1}
\]

The native detail target is nonnegative. More explicitly,

\[
 \Omega_X(q)=\frac{\log4}{\sqrt q}
 \quad(2\le q\le X/4),
\]

and `Omega_X(q)=w_X(q)` on the terminal range `X/4<q<=X`.

For each `3<=T<=X`, take the positive endpoint atom `a_T` and its responses
from `L-94100`:

\[
 a_T(n)\ge0,
 \qquad
 \Gamma_T(q)=C_{a_T}(q),
 \qquad
 \Delta_T(q)=\Gamma_T(q)-2\Gamma_T(4q).
 \tag{L-94101.2}
\]

They obey

\[
 \Delta_T(q)>0\quad(2\le q<T),
 \qquad
 \Delta_T(q)=0\quad(q\ge T).
 \tag{L-94101.3}
\]

Define the exact score of one generator by

\[
 H_T=\mathcal H(a_T)
 =\sum_qY_4(q)\Delta_T(q).
 \tag{L-94101.4}
\]

Thus one generator record

\[
 \mathcal G_T=(T,a_T,\Gamma_T,\Delta_T,H_T)
 \tag{L-94101.5}
\]

contains one endpoint owner, every component row, ordinary `q`, ordinary `4q`,
radix-four detail and native-dual score. No coordinate chooses its own
coefficient.

## 2. Backward native-detail greedy

Initialize the residual detail target by

\[
 \rho^{(X+1)}(q)=\Omega_X(q)
 \qquad(2\le q\le X).
 \tag{L-94101.6}
\]

For `T=X,X-1,...,3`, set

\[
 \boxed{
 \lambda_T
 =\min_{2\le q<T}
 \frac{\rho^{(T+1)}(q)}{\Delta_T(q)}.
 }
 \tag{L-94101.7}
\]

Every denominator is strictly positive. Update

\[
 \rho^{(T)}(q)
 =\rho^{(T+1)}(q)-\lambda_T\Delta_T(q)
 \qquad(2\le q<T),
 \tag{L-94101.8}
\]

and leave all other coordinates unchanged.

By construction,

\[
 \lambda_T\ge0,
 \qquad
 \rho^{(T)}(q)\ge0.
 \tag{L-94101.9}
\]

Define the physical row

\[
 \boxed{
 d_X^{\rm ned}(n)=\sum_{T=3}^X\lambda_Ta_T(n).
 }
 \tag{L-94101.10}
\]

Then

\[
 \boxed{d_X^{\rm ned}(n)\ge0.}
 \tag{L-94101.11}
\]

The same coefficient `lambda_T` multiplies every coordinate of
`mathcal G_T`; there is no source/row/score/response coefficient mismatch.

## 3. Exact all-column native feasibility

Linearity gives

\[
 \Xi_{d_X^{\rm ned}}(q)
 =\sum_{T=3}^X\lambda_T\Delta_T(q).
\]

The residual definition therefore gives

\[
 \boxed{
 s_X(q):=\Omega_X(q)-\Xi_{d_X^{\rm ned}}(q)
 =\rho^{(3)}(q)\ge0
 \qquad(q\ge2).
 }
 \tag{L-94101.12}
\]

Every physical detail column is feasible, without a compact root window,
activation-cell interpolation, terminal annulus patch, rough child, or matrix
port.

For any finitely supported ordinary vector `C`, the positive radix-four inverse
is

\[
 C(q)=\sum_{h\ge0}2^h(\mathcal D_4C)(4^hq).
 \tag{L-94101.13}
\]

Applying it to the nonnegative detail slack in (L-94101.12) yields

\[
 \boxed{
 C_{d_X^{\rm ned}}(q)\le w_X(q)
 \qquad(q\ge2).
 }
 \tag{L-94101.14}
\]

Thus `d_X^ned` is an unconditional native-feasible nonnegative row at every
finite endpoint.

## 4. Exact blocker and slack identities

At stage `T`, define the diagonal candidate

\[
 \widehat\lambda_T
 =\frac{\rho^{(T+1)}(T-1)}{\Delta_T(T-1)},
 \tag{L-94101.15}
\]

and the blocker loss

\[
 \ell_T=\widehat\lambda_T-\lambda_T\ge0.
 \tag{L-94101.16}
\]

No later atom `a_U`, `U<T`, reaches column `T-1`. Hence the final slack in that
column is exactly

\[
 \boxed{
 s_X(T-1)=\Delta_T(T-1)\ell_T.
 }
 \tag{L-94101.17}
\]

Equivalently,

\[
 \boxed{
 s_X(q)=\Delta_{q+1}(q)\ell_{q+1}
 \qquad(2\le q<X).
 }
 \tag{L-94101.18}
\]

If the minimizing column at stage `T` is `q_T<T-1`, then that column is
saturated. Since `Delta_U(q_T)>0` for every `q_T<U<T`, all intermediate
endpoint weights vanish:

\[
 \boxed{
 q_T<U<T\Longrightarrow\lambda_U=0.
 }
 \tag{L-94101.19}
\]

One off-diagonal blocker freezes one contiguous interval of endpoint scales.

## 5. Exact native score and deficit

The positive dual identity gives

\[
 \mathcal H(d_X^{\rm ned})
 =\sum_T\lambda_TH_T
 =\sum_qY_4(q)\Xi_{d_X^{\rm ned}}(q).
 \tag{L-94101.20}
\]

Therefore

\[
 \boxed{
 \mathfrak D_X^{\rm ned}
 :=J_\Lambda(X)-\mathcal H(d_X^{\rm ned})
 =\sum_qY_4(q)s_X(q)
 =\sum_{T=3}^XY_4(T-1)\Delta_T(T-1)\ell_T.
 }
 \tag{L-94101.21}
\]

This is an exact finite scalar. It is not a continuum benchmark difference and
contains no hidden source, child, collar, or port term.

## 6. Architectural disposition

The construction deliberately replaces the impossible branchwise Möbius
compiler by a direct positive endpoint dictionary:

```text
positive source atom             endpoint scale T
owner                            T, exactly once
physical row                     a_T>=0
ordinary observations            Gamma_T(q)
radix-four observation           Delta_T(q)>0
score                            H_T=<Y4,Delta_T>
coefficient                      one lambda_T in every coordinate
native target                    Omega_X
output                           d_X^ned
```

It does not claim exact equality with the signed native component row `c_X`.
`R-94100` proves that such an exact positive equality would already be the full
SHARP theorem.

```text
all-scale finite compiler                         UNCONDITIONAL
component-row positivity                          BUILT IN
ordinary/detail feasibility                       EXACT
one coefficient across all physical coordinates   EXACT
Möbius child positivity                            NOT NEEDED
activation-aware endpoint source                   NOT NEEDED
native weighted deficit                            EXACT SCALAR / NEXT LEMMA
Riemann Hypothesis                                 UNPROVED
```
