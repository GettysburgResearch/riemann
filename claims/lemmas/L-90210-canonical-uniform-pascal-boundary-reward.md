# L-90210 — The two-low-row scalar is the unique zero-safe positive boundary reward of the uniform Pascal chain

Claim ID: `L-90210`  
Status: **PROPOSED COMPLETE EXACT MARKOV / SYMBOL LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-10  
Depends on: `L-33107/L-33108/L-33109`; `L-90208/L-90209`  
Scope: exact martingale representation and uniqueness of the low-row combination; no sign theorem and no RH conclusion

## 1. Uniform Pascal chain

Retain the size-biased uniform internal Pascal kernel

\[
 P_m(k)=\frac{2k}{m(m-1)},
 \qquad1\le k<m.
 \tag{L-90210.1}
\]

For a target state `j`, its hitting probability is

\[
 h_j(j)=1,
 \qquad
 h_j(m)=\frac2{j+1}\quad(m>j),
 \qquad
 h_j(m)=0\quad(m<j).
 \tag{L-90210.2}
\]

## 2. Boundary reward and harmonic potential

Put

\[
 \boxed{
 d(2)=15,
 \qquad d(3)=4,
 \qquad d(m)=0\quad(m\ne2,3).
 }
 \tag{L-90210.3}
\]

Define its stopped reward potential

\[
 f(m)=\mathbb E_m\sum_{0\le t<\tau_1}d(N_t).
 \tag{L-90210.4}
\]

The hitting law gives exactly

\[
 \boxed{
 f(1)=0,
 \qquad f(2)=15,
 \qquad f(3)=14,
 \qquad f(m)=12\quad(m\ge4).
 }
 \tag{L-90210.5}
\]

Indeed, from state three the chain collects `4` immediately and then reaches state two with probability `2/3`, while from every state `m>=4` it reaches states two and three with probabilities `2/3` and `1/2`, respectively.

Equivalently,

\[
 \boxed{
 f-Pf=d.
 }
 \tag{L-90210.6}
\]

Thus the normalized dual potential is exactly harmonic above state three. Put

\[
 F(m)=mf(m).
 \tag{L-90210.7}
\]

Then

\[
 \boxed{
 F(1)=0,
 \quad F(2)=30,
 \quad F(3)=42,
 \quad F(m)=12m\ (m\ge4).
 }
 \tag{L-90210.8}
\]

This is precisely the row potential `5F_2+F_3` of `T-32403`.

## 3. Exact source pairing

Let `r_X` be any size-conserving node divergence and put

\[
 s_X(m)=mr_X(m).
 \tag{L-90210.9}
\]

Let

\[
 M-MP=s_X
 \tag{L-90210.10}
\]

be its signed uniform-Pascal Green occupation. The Markov pairing identity gives

\[
 \boxed{
 \sum_m r_X(m)F(m)
 =\sum_mM(m)d(m)
 =15M(2)+4M(3).
 }
 \tag{L-90210.11}
\]

For the critical carry target, `L-33109` gives

\[
 M(n)=\frac{n(n-1)}{n+1}c_X(n).
 \tag{L-90210.12}
\]

Hence

\[
 \boxed{
 15M(2)+4M(3)
 =10c_X(2)+6c_X(3)
 =2[5c_X(2)+3c_X(3)].
 }
 \tag{L-90210.13}
\]

The RH-facing two-low-row scalar is therefore one half of the expected total reward delivered by the signed critical source to the two-state boundary reward (L-90210.3).

No coordinatewise positivity of the complete occupation is required for this identity.

## 4. Deterministic transfer of a general two-state reward

For arbitrary real rewards `A=d(2)` and `B=d(3)`, the stopped potential is

\[
 f_{A,B}(m)=A h_2(m)+B h_3(m).
 \tag{L-90210.14}
\]

Its deterministic Dirichlet transfer is

\[
 \boxed{
 \mathcal A_{A,B}(u)=A\mathcal A_2(u)+B\mathcal A_3(u),
 }
 \tag{L-90210.15}
\]

where

\[
 \mathcal A_2(u)
 =\frac23\zeta(u)-\frac23
  +\frac43\,2^{-u}-\frac23\,3^{-u},
 \tag{L-90210.16}
\]

\[
 \mathcal A_3(u)
 =\frac12\zeta(u)-\frac12
  -\frac12\,2^{-u}+\frac52\,3^{-u}
  -\frac32\,4^{-u}.
 \tag{L-90210.17}
\]

The coefficient of the independent `3^{-u}` channel is

\[
 -\frac23A+\frac52B.
 \tag{L-90210.18}
\]

It vanishes if and only if

\[
 \boxed{4A=15B.}
 \tag{L-90210.19}
\]

Thus, up to an overall scalar, the positive reward vector

\[
 \boxed{(A,B)=(15,4)}
 \tag{L-90210.20}
\]

is the **unique** two-state boundary reward whose deterministic transfer contains no 3-adic exponential channel.

For this vector,

\[
 \boxed{
 15\mathcal A_2(u)+4\mathcal A_3(u)
 =12\zeta(u)-6(1-2^{-u})(2-2^{-u}).
 }
 \tag{L-90210.21}
\]

After pairing with the Möbius Euler factor `1/zeta(u)`, the only nonconstant finite numerator is the zero-safe dyadic polynomial

\[
 (1-2^{-u})(2-2^{-u}).
 \]

Its zeros lie strictly outside the open RH counterexample half-plane.

## 5. Canonicality

The ratio `15:4` is therefore selected simultaneously by three independent exact structures:

1. the carry-inverse row identity `5c_X(2)+3c_X(3)`;
2. a positive stopped reward supported only at states two and three;
3. elimination of the independent 3-adic deterministic channel.

This is not an arbitrary low-row numerical optimization. It is the unique positive two-boundary reward whose uniform-Pascal transfer is purely zeta plus a zero-safe dyadic correction.

## 6. Martingale attack interface

A future proof may now target the single scalar

\[
 \boxed{15M_X(2)+4M_X(3)\ge0}
 \tag{L-90210.22}
\]

rather than full SHARP or coordinatewise nonnegative occupation.

Equivalently, it may seek a coupling or optional-stopping theorem showing that the signed critical source delivers nonnegative expected reward to (L-90210.3). Any such theorem must use arithmetic information beyond the deterministic Pascal chain, because the chain factor itself is already explicit and resonance-free.

The strict Gamma–carry square-root moment gap of `L-33106` is compatible with this formulation, but no theorem identifying the complete source with that single asymptotic mode is asserted here.

## 7. Proof boundary

Proved exactly:

- the positive two-state reward and its stopped potential;
- localization of the policy drift to states two and three;
- exact Green-occupation pairing with the two-low-row scalar;
- the general two-reward deterministic transfer;
- uniqueness of the ratio `15:4` under 3-channel elimination;
- the zero-safe dyadic numerator.

Open:

- sign of the expected reward for the critical Möbius source;
- a rigidity/coupling theorem using the Gamma–carry margin;
- SHARP or RH.
