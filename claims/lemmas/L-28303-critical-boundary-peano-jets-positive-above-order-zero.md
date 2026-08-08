# L-28303 — Critical boundary Peano jets are positive above order zero

Claim ID: `L-28303`  
Title: Every first-omitted finite-difference jet of the critical power-log source has the correct Peano sign from order one onward; only the zeroth endpoint value is adverse  
Status: **PROPOSED COMPLETE EXACT CALCULUS LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-09-x`  
Created: 2026-08-08  
Corrected: 2026-08-08 to retain the order-dependent Peano range  
Dependencies: PR #286 `L-28402`  
Scope: critical-source boundary sign; no all-generation recurrence

## 1. Exact derivatives

Fix `X>=2` and put

\[
 f_X(x)=x^{-1/2}\log(X/x),
 \qquad x>0.
 \tag{L-28303.1}
\]

For every integer `m>=0`, differentiation with respect to the exponent gives

\[
 \boxed{
 (-1)^m f_X^{(m)}(x)
 =(1/2)_m x^{-m-1/2}
 \left[
 \log(X/x)+H_m^{(1/2)}
 \right],
 }
 \tag{L-28303.2}
\]

where

\[
 H_0^{(1/2)}=0,
 \qquad
 H_m^{(1/2)}
 =\sum_{r=0}^{m-1}{1\over r+1/2}
 =2H_{2m}-H_m.
 \tag{L-28303.3}
\]

For `m>=1`, decreasing-integrand comparison gives the strict lower bound

\[
 \boxed{
 H_m^{(1/2)}
 >\int_0^m{du\over u+1/2}
 =\log(2m+1)
 \ge\log(m+2).
 }
 \tag{L-28303.4}
\]

## 2. Order-dependent first-omitted range

Use the exact convention of `L-28402`: a boundary jet of order `m` is

\[
 \Delta_k^m f_X(kq+a),
 \qquad a\in\{-1,0\},
 \tag{L-28303.5}
\]

where the first omitted argument `x=kq+a` satisfies

\[
 X<x\le X+q,
 \tag{L-28303.6}
\]

and the finite-difference step in the argument is `q`.  Every output coordinate
satisfies

\[
 q\le{X+1\over2}.
 \tag{L-28303.7}
\]

Hence every point in the order-`m` Peano box obeys

\[
\begin{aligned}
 x+t_1+\cdots+t_m
 &\le X+(m+1)q\\
 &\le X+{m+1\over2}(X+1)\\
 &\le(m+2)X,
\end{aligned}
\tag{L-28303.8}
\]

where the last inequality uses `X>=2`.

Therefore, throughout the complete box,

\[
 \log{X\over x+t_1+\cdots+t_m}
 \ge-\log(m+2).
 \tag{L-28303.9}
\]

Combining (L-28303.2), (L-28303.4), and (L-28303.9),

\[
 \boxed{
 (-1)^m f_X^{(m)}(y)>0
 }
 \tag{L-28303.10}
\]

for every `m>=1` and every point `y` in its complete first-omitted Peano box.
The order-dependent growth of the box is thus paid exactly by the increasing
half-harmonic constant `H_m^(1/2)`.

The zeroth profile has the opposite sign beyond the cutoff:

\[
 f_X(x)<0
 \qquad(x>X).
 \tag{L-28303.11}
\]

Thus order zero is the unique adverse derivative channel.

## 3. Positive Peano finite differences

Use the forward-difference convention

\[
 \Delta_hf(x)=f(x)-f(x+h).
\]

The exact Peano formula is

\[
 \Delta_h^mf(x)
 =(-1)^m
 \int_{[0,h]^m}
 f^{(m)}(x+t_1+\cdots+t_m)
 \,dt_1\cdots dt_m.
 \tag{L-28303.12}
\]

Equations (L-28303.10) and (L-28303.12) give

\[
 \boxed{
 \Delta_q^m f_X(kq+a)>0
 \qquad(m\ge1)
 }
 \tag{L-28303.13}
\]

at every first-omitted boundary jet of `L-28402`.

Accordingly, every Euler boundary jet of orders `1,...,M-1` has a nonnegative
one-variable Peano source.  No signed conversion is needed for those channels.

## 4. Zeroth collar

For `m=0`, the first omitted argument satisfies

\[
 X<x\le X+q\le2X.
 \tag{L-28303.14}
\]

The unique adverse value is therefore explicit and uniformly bounded:

\[
 \boxed{
 0<-f_X(x)
 =x^{-1/2}\log(x/X)
 \le X^{-1/2}\log2.
 }
 \tag{L-28303.15}
\]

After the capacity normalization used in the carry cascade, the complete
first-generation zeroth collar is at most polylogarithmic by the same divisor
switch as `L-28402`. Unlike the higher jets, this scalar collar must remain in
the BJPR state and be recombined with the eta residual before a sign is taken.

## 5. Consequence for BJPR

The boundary state is not an arbitrary signed jet bank. For the exact critical
source it has the typed form

```text
one explicit adverse zeroth collar
+
nonnegative Peano jets of every order m>=1
+
geometrically damped top remainder.
```

Combining this with `L-28302` shows that the first-generation eta dipoles and all
positive-order Peano channels already lie in a nonnegative source/Pascal cone.
The genuinely open propagation question is reduced to the zeroth collar and
common-destination recombination.

## 6. Proof boundary

Closed exactly:

- all ordinary derivatives of the critical power-log source;
- strict sign on the complete order-dependent first-omitted Peano box;
- positive Peano representation of every positive-order boundary jet;
- isolation and size of the unique adverse zeroth collar.

Open:

- all-generation recombination of the zeroth collar;
- preservation of the positive source cone after later finite cascades;
- BJPR, Cycle Debt, and RH.
