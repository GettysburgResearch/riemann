# L-28303 — Critical boundary Peano jets are positive above order zero

Claim ID: `L-28303`  
Title: Every first-omitted finite-difference jet of the critical power-log source has the correct Peano sign from order one onward; only the zeroth endpoint value is adverse  
Status: **PROPOSED COMPLETE EXACT CALCULUS LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-09-x`  
Created: 2026-08-08  
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

In particular,

\[
 H_m^{(1/2)}\ge2
 \qquad(m\ge1).
 \tag{L-28303.4}
\]

## 2. First-omitted range

For an output coordinate of the finite central cascade one has

\[
 q\le{X+1\over2}.
\]

The first omitted shifted or unshifted quotient argument differs from `X` by
less than one complete even/odd step.  Hence every point in the associated
Peano interval obeys the review-safe bound

\[
 x\le3X.
 \tag{L-28303.5}
\]

Therefore

\[
 \log(X/x)\ge-\log3>-2.
 \tag{L-28303.6}
\]

Combining (L-28303.2)--(L-28303.6),

\[
 \boxed{
 (-1)^m f_X^{(m)}(x)>0
 \quad
 (m\ge1,\ X<x\le3X).
 }
 \tag{L-28303.7}
\]

The zeroth profile has the opposite sign beyond the cutoff:

\[
 f_X(x)<0
 \qquad(x>X).
 \tag{L-28303.8}
\]

Thus order zero is the unique adverse derivative channel on the complete
first-omitted range.

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
 \tag{L-28303.9}
\]

Whenever the complete integration box lies in the first-omitted range
`(X,3X]`, equations (L-28303.7) and (L-28303.9) give

\[
 \boxed{
 \Delta_h^m f_X(x)\ge0
 \qquad(m\ge1).
 }
 \tag{L-28303.10}
\]

Accordingly, every Euler boundary jet of orders `1,...,M-1` in `L-28402` has a
nonnegative one-variable Peano source. No signed conversion is needed for those
channels.

## 4. Zeroth collar

The only adverse finite jet is the first omitted zeroth value. It is explicit:

\[
 -f_X(x)=x^{-1/2}\log(x/X),
 \qquad X<x\le3X.
 \tag{L-28303.11}
\]

It has bounded normalized size

\[
 0<-f_X(x)\le X^{-1/2}\log3.
 \tag{L-28303.12}
\]

After the capacity normalization used in the carry cascade, the complete
first-generation zeroth collar is at most polylogarithmic by the same divisor
switch as `L-28402`.  Unlike the higher jets, this scalar collar must remain in
the BJPR state and be recombined with the eta residual before a sign is taken.

## 5. Consequence for BJPR

The boundary state is not an arbitrary signed jet bank.  For the exact critical
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
- strict sign on the complete first-omitted range for every order `m>=1`;
- positive Peano representation of every positive-order boundary jet;
- isolation and size of the unique adverse zeroth collar.

Open:

- all-generation recombination of the zeroth collar;
- preservation of the positive source cone after later finite cascades;
- BJPR, Cycle Debt, and RH.
