# L-25806 — Dyadic bit-layer depletion

Claim ID: `L-25806`  
Title: A scale-adapted radix `2^L` is a positive finite stack of odd-part depletion layers and interfaces exactly with the parity-comb source  
Status: **PROPOSED EXACT LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-07  
Issue: #258  
Dependencies: `L-25802`; PR #236 `L-23012`  
Scope: dyadic specialization of the nonmultiple-count kernel

## 1. Arithmetic bit-layer factorization

Let

\[
a_{2^L}(n)=1-\mathbf1_{2^L\mid n}
\]

and

\[
a_2(n)=1-\mathbf1_{2\mid n}.
\]

Put

\[
h_L=\sum_{j=0}^{L-1}\delta_{2^j}.
\tag{L-25806.1}
\]

At the Dirichlet-series level,

\[
(1-2^{-Ls})\zeta(s)
=(1-2^{-s})\zeta(s)
 \sum_{j=0}^{L-1}2^{-js}.
\]

Therefore, coefficientwise,

\[
\boxed{
a_{2^L}=a_2*h_L.}
\tag{L-25806.2}
\]

Equivalently, every integer not divisible by `2^L` is represented uniquely as
an odd integer times `2^j` with `0<=j<L`.

For every arithmetic source `T`,

\[
\boxed{
a_{2^L}*T
=\sum_{j=0}^{L-1}\delta_{2^j}*(a_2*T).}
\tag{L-25806.3}
\]

Thus the fixed-fraction dyadic depletion is a finite positive stack of ordinary
odd-part depleted sources.

## 2. Positive physical bit layers

Let `C_Q` be the positive nonmultiple-count kernel of `L-25802`. Then

\[
\boxed{
\mathcal C_{2^L}(t)
=\sum_{j=0}^{L-1}2^{-j/2}
 \mathcal C_2(t-j\log2).}
\tag{L-25806.4}
\]

Indeed, writing `N=floor(e^t)`,

\[
N-\left\lfloor{N\over2^L}\right\rfloor
=
\sum_{j=0}^{L-1}
\left(
 \left\lfloor{N\over2^j}\right\rfloor
 -\left\lfloor{N\over2^{j+1}}\right\rfloor
\right),
\]

and the `j`-th bracket counts integers of exact 2-adic valuation `j`.

The normalized coefficient `2^-j/2` in (L-25806.4) is exactly what converts
the shifted factor `exp(-(t-j log 2)/2)` back to `exp(-t/2)`.

## 3. Relation to the parity comb

Let

\[
\lambda_2(n)=(-1)^{n+1}.
\]

Then pointwise

\[
\boxed{2a_2=\mathbf1+\lambda_2.}
\tag{L-25806.5}
\]

The causal primitive of the normalized `lambda_2` atoms is the positive parity
comb

\[
P_2(t)=e^{-t/2}
\mathbf1_{\{\lfloor e^t\rfloor\text{ odd}\}}
\]

from `L-23012`, while the causal primitive of the normalized constant-one atoms
is

\[
C_{\rm all}(t)=e^{-t/2}\lfloor e^t\rfloor.
\]

Hence

\[
\boxed{
\mathcal C_2
={1\over2}(C_{\rm all}+P_2).}
\tag{L-25806.6}
\]

At transform level this is

\[
(1-2^{-s})\zeta(s)
={1\over2}
\left[
\zeta(s)+(1-2^{1-s})\zeta(s)
\right].
\]

Thus the PADT depletion contains the parity-comb source as one exact channel,
not merely as an analogy.

## 4. Scale-adapted dyadic choice

For one fixed

\[
0<\delta_0<\frac13,
\]

choose

\[
L(J)=\left\lfloor{\delta_0J\over\log2}\right\rfloor,
\qquad
Q_J=2^{L(J)}.
\tag{L-25806.7}
\]

Then

\[
\log Q_J=\delta_0J+O(1)
\tag{L-25806.8}
\]

and

\[
\|H_{Q_J}^\#\|_{\rm TV}
={1\over1-Q_J^{-1/2}}=1+O(e^{-\delta_0J/2}).
\tag{L-25806.9}
\]

The depletion therefore has a fixed scale gap and an asymptotically isometric
radix recovery.

The number of bit layers is `L(J)=O(J)`. This is polynomial in the output
parameter and does not affect an exponential block rate, provided the layers
are transported before total variation.

## 5. Mandatory dyadic mutation

A production `PADT` certificate using `Q_J=2^L` must export:

1. the factorization (L-25806.3);
2. the physical bit-layer identity (L-25806.4);
3. the parity channel (L-25806.6);
4. the three-tap parity-comb mutation from PR #236 after projecting to the
   dyadic fixed-ratio shell.

Failure of this mutation means that the transport has discarded the exact
Euler-aligned Möbius mode.

## 6. Proof boundary

Closed exactly:

- finite dyadic bit-layer factorization;
- positive physical layer decomposition;
- exact parity-comb channel;
- fixed-fraction dyadic radix choice.

Not closed:

- a contraction for any individual parity-depleted layer;
- a signed bit-layer transport estimate;
- `PADT(K)` or RH.
