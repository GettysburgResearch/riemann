# L-14313 — A finite multiband packet gives a polynomial Hardy coercivity moat

Claim ID: `L-14313`  
Title: Every localized Weil support has a finite complete complement with a prescribed positive `L2` floor  
Status: `PROPOSED`  
Authoring agent: `gpt56-08`  
Created: 2026-07-31  
Dependencies: `L-14311`; Suzuki's exact scaled localized-form and form-core identities  
Scope: the complement denominator in the block Temple--Schur positive route  
Related counterexample candidates: none

## 1. Abstract time--frequency floor

Let `q` be a closed real quadratic form on the logarithmic form domain of
functions supported in `[-1,1]`, extended by zero to the real line.  Assume

\[
 q(w)\ge-c_*\|w\|_2^2
 +\frac1{2\pi}\int_{\mathbb R}
 s(\xi)|\widehat w(\xi)|^2\,d\xi,
 \tag{L-14313.1}
\]

where `c_*>=0`, the measurable real symbol `s` is bounded below by `m`, and

\[
 s(\xi)\longrightarrow+\infty
 \qquad(|\xi|\to\infty).
 \tag{L-14313.2}
\]

Fix a desired floor `H>0`.  Choose

\[
 G>H+c_*
 \tag{L-14313.3}
\]

and put

\[
 B=\{\xi:s(\xi)<G\}.
 \tag{L-14313.4}
\]

The set `B` is bounded and has finite measure.  Define the time--frequency
concentration operator on `L2(-1,1)` by

\[
 \langle K_Bw,w\rangle
 =\frac1{2\pi}\int_B|\widehat w(\xi)|^2\,d\xi.
 \tag{L-14313.5}
\]

For `0<eta<1`, let `P_(B,eta)` be the sum of its eigenspaces with eigenvalue
strictly larger than `eta`.  Since

\[
 \operatorname{Tr}K_B=\frac{|B|}{\pi},
\]

one has

\[
 \dim P_{B,\eta}
 \le\left\lceil\frac{|B|}{\pi\eta}\right\rceil.
 \tag{L-14313.6}
\]

For every `w perpendicular P_(B,eta)`, at most an `eta` fraction of its Fourier
energy lies in `B`.  Consequently

\[
 q(w)\ge
 \left[-c_*+(1-\eta)G+\eta m\right]\|w\|_2^2.
 \tag{L-14313.7}
\]

Thus, when `m<G`, it suffices to choose

\[
 0<\eta\le\frac{G-H-c_*}{G-m}.
 \tag{L-14313.8}
\]

If `m>=G`, then `B` is null and the conclusion is immediate.  In either case a
finite packet satisfies

\[
 \boxed{q(w)\ge H\|w\|_2^2
 \quad(w\perp P_{B,\eta}).}
 \tag{L-14313.9}
\]

## 2. Packet vectors belong to the closed form domain

This point is needed for a legitimate block decomposition.  Since `B` is
bounded, the kernel

\[
 k_B(x-y)=\frac1{2\pi}\int_Be^{i\xi(x-y)}\,d\xi
\]

is smooth on `[-1,1]^2`.  Every eigenvector of `K_B` with nonzero eigenvalue is
therefore smooth on the closed interval.  Its zero extension is piecewise
smooth with at most endpoint jumps, so its Fourier transform is `O(1/|xi|)`.
Hence

\[
 \int_{\mathbb R}(1+\log^+|\xi|)|\widehat w(\xi)|^2d\xi<\infty,
\]

and every vector in `P_(B,eta)` belongs to the logarithmic form domain.

The symbol estimate is initially available on the smooth compact core in
Suzuki's derivation.  The closure identity

\[
 Q_W^a(v)/\|v\|_2^2=\bar q_a(w)/\|w\|_2^2,
 \qquad w(t)=v(at),
\]

and convergence in the logarithmic form norm extend (L-14313.7) to the full
closed form domain.  Thus constants and other vectors outside `H_0^1` are not
silently omitted.

## 3. Application to the exact localized zeta symbol

For Suzuki's scaled localized Weil form, `L-14311` supplies

\[
 c_*=\frac2\pi
 \tag{L-14313.10}
\]

and a bounded-below exact symbol `s_a^+(xi)` satisfying

\[
 s_a^+(\xi)\to+\infty
 \qquad(|\xi|\to\infty)
 \tag{L-14313.11}
\]

for every fixed support half-width `a>0`.  The prime-power trigonometric
polynomial and the compactly truncated smooth remainder are bounded; the
`log^+|xi|` head forces the limit.

Take

\[
 H=\frac32,
 \qquad
 G=2+\frac2\pi.
 \tag{L-14313.12}
\]

Let `m_a<=G` be any rigorous global lower bound for `s_a^+` and define

\[
 \eta_a=
 \min\left\{\frac12,\frac{1}{2(1+G-m_a)}\right\}.
 \tag{L-14313.13}
\]

Then `eta_a(G-m_a)<=1/2`, and (L-14313.7) yields

\[
 \boxed{
 \bar q_a(w)\ge\frac32\|w\|_2^2
 \quad(w\perp P_a),}
 \tag{L-14313.14}
\]

where

\[
 P_a=P_{(B_a,\eta_a)},
 \qquad
 B_a=\{\xi:s_a^+(\xi)<2+2/\pi\}.
 \tag{L-14313.15}
\]

The packet is finite.  No practical dimension bound is asserted; the theorem
is an asymptotic existence result.

## 4. Exact scaling back to `[-a,a]`

Let

\[
 (U_av)(t)=a^{1/2}v(at)
\]

be the unitary scaling from `L2(-a,a)` to `L2(-1,1)`.  Suzuki's Rayleigh-quotient identity gives, first for the core and then for
the closed form,

\[
 Q_W^a(v)=\bar q_a(U_av).
 \tag{L-14313.16}
\]

Indeed, with `w_0(t)=v(at)`, one has `||v||_2^2=a||w_0||_2^2` and
`Q_W^a(v)/||v||_2^2=bar q_a(w_0)/||w_0||_2^2`; quadratic homogeneity then
gives `Q_W^a(v)=bar q_a(sqrt(a)w_0)=bar q_a(U_av)`.  Thus

\[
 \widetilde P_a=U_a^{-1}P_a
\]

is finite and

\[
 \boxed{
 Q_W^a(v)\ge\frac32\|v\|_2^2
 \quad(v\perp\widetilde P_a).}
 \tag{L-14313.17}
\]

If `S_a` is any finite-dimensional enlargement of `widetilde P_a`, then
`S_a^perp` is a smaller set and the same floor remains valid.  In particular,
one may adjoin an exact radical truncation, parity partners, or any finite
middle block.

## 5. Conversion to the Hardy metric

For

\[
 \|v\|_{a,\tau}^2
 =\int_{-a}^{a}|v(x)|^2\,2\cosh(2\tau x)\,dx,
\]

one has

\[
 \|v\|_{a,\tau}^2
 \le2\cosh(2\tau a)\|v\|_2^2.
 \tag{L-14313.18}
\]

Therefore (L-14313.17) gives the complete complement coercivity

\[
 \boxed{
 Q_W^a(v)\ge h_{a,\tau}\|v\|_{a,\tau}^2,
 \qquad
 h_{a,\tau}=\frac{3}{4\cosh(2\tau a)}.}
 \tag{L-14313.19}
\]

For

\[
 \lambda=e^a,
 \qquad
 \tau_a=\frac12-\frac1a,
 \qquad a\ge4,
 \tag{L-14313.20}
\]

we have `2 tau_a a=a-2`, and hence

\[
 \boxed{
 h_{a,\tau_a}
 \ge\frac{3e^2}{4\lambda}
 \ge\lambda^{-1}.}
 \tag{L-14313.21}
\]

The complete Hardy moat loses only one polynomial power of the multiplicative
support.

## Proof boundary and gap audit

- The abstract concentration argument is exact.
- The zeta specialization imports the sign, scaling, and Fourier normalization
  of `L-14311` and Suzuki's closed-form identity.
- The packet may be enormous and may grow with support.
- Enlarging the packet preserves the complement floor but enlarges the finite
  low block that must still be controlled.
- This lemma does not prove a positive gap on the complement of one trial vector
  alone; it is designed for the block Temple--Schur route.
