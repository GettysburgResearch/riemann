# T-15117 — Finite-notch exhaustion gives a sharp RH dichotomy

Claim ID: `T-15117`  
Title: Successively notching certified critical-line ordinates drives one corrected prime signal uniformly to zero under RH, while every finite notch family retains the full false-RH growth exponent  
Status: **PROPOSED PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-07  
Dependencies: `L-15143`; `L-15406`; `L-15409`; the same smoothed explicit-formula normalization as `T-15406`  
Scope: a global two-parameter proof/disproof architecture for RH

## 1. Exact finite notch windows

Retain the triangular pole-free window `G_h` from `L-15409`. Enumerate the
distinct positive ordinates at which a critical-line zero occurs as

\[
 0<\gamma_1<\gamma_2<\cdots.
\]

Let `m_k` denote the multiplicity at the positive ordinate `gamma_k`. The zero
at `-gamma_k` has the same multiplicity by conjugation; the explicit factor `2`
in the real bounds below accounts for that conjugate pair.

For each `k`, put

\[
 r_k=\frac{2\pi}{\gamma_k}
\]

and define the normalized box

\[
 u_{r_k}(t)=r_k^{-1}\mathbf1_{[0,r_k]}(t).
\]

For every finite `M`, define

\[
 \boxed{
 G_M=G_h*u_{r_1}*\cdots*u_{r_M}.}
 \tag{T-15117.1}
\]

Its Laplace transform is

\[
 \boxed{
 \widehat G_{M,L}(z)
 =\widehat G_{h,L}(z)
 \prod_{k=1}^{M}
 \frac{1-e^{-r_kz}}{r_kz}.}
 \tag{T-15117.2}
\]

Every `G_M` is compactly supported, with

\[
 \operatorname{supp}G_M
 \subseteq
 \left[0,3h+2\pi\sum_{k=1}^{M}\frac1{\gamma_k}\right].
 \tag{T-15117.3}
\]

The pole zero survives:

\[
 \widehat G_{M,L}(1/2)=0.
\]

Every box factor is nonzero in `Re z>0`; therefore

\[
 \boxed{
 \widehat G_{M,L}(z)\ne0
 \qquad(0<\Re z<1/2).}
 \tag{T-15117.4}
\]

On the imaginary axis,

\[
 \left|
 \frac{1-e^{-ir_kt}}{ir_kt}
 \right|\le1,
\]

and the `k`th factor vanishes at `t=+-gamma_k`.

## 2. Prime statistic and known-term correction

Define the finite prime-power statistic

\[
 \boxed{
 Q_M(x)=
 \sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
 G_M(x-\log n).}
 \tag{T-15117.5}
\]

For each fixed `M` and `x`, only prime powers in one finite multiplicative
annulus occur.

Let `E_M^known(x)` be the fully explicit contribution of the trivial zeros,
endpoint terms, and any fixed initial-segment convention in the smoothed
explicit formula. The zeta pole contributes nothing because
`Ghat_M(1/2)=0`. Put

\[
 \boxed{
 R_M(x)=Q_M(x)-E_M^{\rm known}(x).}
 \tag{T-15117.6}
\]

Then the exact nontrivial-zero expansion is

\[
 \boxed{
 R_M(x)=
 -\sum_{\rho}m_\rho
 \widehat G_{M,L}(\rho-1/2)
 e^{(\rho-1/2)x}.}
 \tag{T-15117.7}
\]

The correction in (T-15117.6) is arithmetic and source-computable; it does not
insert or assume a nontrivial zero.

## 3. RH side: uniform spectral exhaustion

Assume RH. Every nontrivial zero is `rho=1/2+-i gamma_k`. The first `M`
ordinate pairs vanish exactly from (T-15117.7), and all remaining box factors
have modulus at most one. Therefore

\[
 \boxed{
 \|R_M\|_{L^\infty(\mathbb R)}
 \le
 2\sum_{k>M}m_k
 |\widehat G_{h,L}(i\gamma_k)|.}
 \tag{T-15117.8}
\]

Because

\[
 \widehat G_{h,L}(it)=O((1+|t|)^{-2})
\]

and the unit-interval zero count is `O(log(2+|t|))`, the series on the right
converges. Its tail tends to zero, so

\[
 \boxed{
 \mathrm{RH}
 \Longrightarrow
 \lim_{M\to\infty}\|R_M\|_\infty=0.}
 \tag{T-15117.9}
\]

The same conclusion holds for every fixed-length local energy:

\[
 \boxed{
 \lim_{M\to\infty}
 \sup_{X\ge0}
 \int_X^{X+1}|R_M(x)|^2dx=0.}
 \tag{T-15117.10}
\]

Thus the notch sequence does more than keep the prime signal bounded under RH:
it annihilates the complete nontrivial spectrum uniformly.

## 4. False-RH side: no finite notch can hide the rightmost zero

Let `Theta_zeta` be the rightmost-zero displacement from `L-15143`. For every
finite `M`, (T-15117.4) says that no shifted off-critical zero can be canceled by
the notch product. Applying `L-15143` with `G_M` instead of `G_h` gives

\[
 \boxed{
 \Theta_\zeta
 =\limsup_{X\to\infty}
 \frac{
 \log\left(
 1+\int_X^{X+1}|R_M(x)|^2dx
 \right)}{2X}}
 \qquad(M<\infty).
 \tag{T-15117.11}
\]

Therefore, if RH is false, then for **every** finite notch family and every
`theta<Theta_zeta`,

\[
 e^{-2\theta X}
 \int_X^{X+1}|R_M(x)|^2dx
\]

is unbounded on the tail.

No amount of finite certified line-zero suppression can erase, phase-cancel, or
turn an off-line mode into a bounded residual.

## 5. Exact global dichotomy

Combining Sections 3 and 4 yields

\[
 \boxed{
 \mathrm{RH}
 \iff
 \lim_{M\to\infty}\|R_M\|_\infty=0}
 \tag{T-15117.12}
\]

and equivalently

\[
 \boxed{
 \mathrm{RH}
 \iff
 \lim_{M\to\infty}
 \sup_{X\ge0}
 \int_X^{X+1}|R_M(x)|^2dx=0.}
 \tag{T-15117.13}
\]

More sharply, the two alternatives are:

```text
RH true:
  finite boundary notches exhaust the entire nontrivial prime signal
  uniformly, with an explicit zero-tail majorant tending to zero.

RH false:
  every finite notch statistic retains positive exponential block-energy
  exponent exactly Theta_zeta.
```

This is an order-of-limits theorem. There is no compactly supported infinite
notch profile because `sum 1/gamma_k` diverges; every row remains a finite
prime-power object.

## 6. Directed near-notch version

Production data contain certified zero balls rather than exact ordinates.
Suppose

\[
 \gamma_k\in
 [\widetilde\gamma_k-\varepsilon_k,
  \widetilde\gamma_k+\varepsilon_k],
 \qquad0<\varepsilon_k<\widetilde\gamma_k,
\]

and use the design length

\[
 \widetilde r_k=2\pi/\widetilde\gamma_k.
\]

`L-15406` gives

\[
 \left|
 \frac{1-e^{-i\widetilde r_k\gamma_k}}
 {i\widetilde r_k\gamma_k}
 \right|
 \le
 \eta_k:=
 \frac{\varepsilon_k}
 {\widetilde\gamma_k-\varepsilon_k}.
 \tag{T-15117.14}
\]

All other notch factors have imaginary-axis modulus at most one. Hence RH
implies the fully directed finite moat

\[
 \boxed{
 \|R_M\|_\infty
 \le U_M,}
 \tag{T-15117.15}
\]

where

\[
 \boxed{
 U_M=
 2\sum_{k\le M}m_k
 \sup_{t\in I_k}|\widehat G_{h,L}(it)|\,\eta_k
 +2\sum_{k>M}m_k
 |\widehat G_{h,L}(i\gamma_k)|.}
 \tag{T-15117.16}
\]

The unlisted tail may be bounded using exact zero counts and monotone transform
envelopes; no unlisted zero ordinate must be inserted into the finite
certificate.

By tightening the first `M` zero balls while sending `M` to infinity, one can
force

\[
 U_M\to0.
\]

A single directed prime-side value satisfying

\[
 |R_M(x)|>U_M
\]

or a block lower bound satisfying

\[
 \int_X^{X+1}|R_M(x)|^2dx>U_M^2
\]

is a finite RH-disproof witness after independent prime-manifest, zero-ball,
transform, and explicit-formula review.

## 7. Repeated-averaging form

Let

\[
 (\mathcal A_rf)(x)=\frac1r\int_0^r f(x-u)\,du.
\]

Convolution gives the exact prime-side identity

\[
 \boxed{
 Q_M=
 \mathcal A_{r_M}\cdots\mathcal A_{r_1}Q_h.}
 \tag{T-15117.17}
\]

Thus the RH-positive target is a deterministic statement about repeated
positive averaging of one explicit arithmetic signal. Under RH the averaging
operators successively annihilate its Bohr frequencies. Under false RH every
finite product retains the same rightmost exponential type.

This gives a direct attack on the full problem that does not pass through a
moving target root, a shrinking matrix moat, or a sign-sensitive scalar sample.

## 8. Connections missed by the separate programmes

1. **Terminal-prime and square-screw.** `L-15143` and `L-19802` measure the same
   `Theta_zeta`; the notch theorem converts the phase-sensitive scalar
   excursions into a uniformly exhausted positive-energy family.
2. **Certified-zero deflation and prime filtering.** Direct-`xi` zero deflation
   and the factors in (T-15117.2) are dual implementations of the same spectral
   removal.
3. **Hilbert--Poisson strip energy.** For each `omega>0`, finiteness of the
   exponentially weighted `R_M` energy is equivalent to vanishing of the
   right-zero packet beyond `1/2+omega`; the prime and Hardy-space programmes
   are testing the same anti-causal component.
4. **Source-canonical matrices.** Every block energy in (T-15117.11) is a finite
   positive Gram quadratic form over the exact prime-power manifest, so it can
   be consumed by the source-bound matrix infrastructure without importing a
   zero-side sign.

## 9. What remains for a complete proof

A proof of RH would follow from a prime-side proof of either

\[
 \|R_M\|_\infty\to0
\]

or

\[
 \sup_X\int_X^{X+1}|R_M(x)|^2dx\to0
\]

for the directed finite-notch sequence, without assuming the zero expansion.
The exact recurrence (T-15117.17) and the finite prime-pair Gram representation
of `L-15143` are the two arithmetic interfaces for that attack.

This theorem proves the dichotomy and the correct target. It does not prove the
required prime-side uniform vanishing and therefore does not prove RH.

## 10. Proof boundary

- Exact notches are theorem-level analytic objects. Production notches must use
  the interval attenuation ledger in Section 6.
- The known trivial/endpoint contribution must be retained or subtracted with a
  source-bound explicit-formula convention.
- Every finite notch product is zero-free in the open counterexample strip;
  an infinite product is neither required nor silently used.
- The uniform-vanishing implication under RH uses the absolutely summable
  transform tail.
- The false-RH exponent statement is inherited from `L-15143` and the finite
  product's open-strip zero-freeness.
- No finite nonnegative scan establishes the limit in (T-15117.12).
