# T-25801 — Prime-Anchored Digit Transport implies RH

Claim ID: `T-25801`  
Title: A cofinal family of source-specific digit-depletion transport certificates gives the balanced recurrence with loss `1/K+eta_K` and forces the rightmost-zero exponent to vanish  
Status: **PROPOSED COMPLETE CONDITIONAL COMPOSITION THEOREM PENDING REVIEW**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-07  
Issue: #258  
Dependencies: `D-25801`, `L-25801`--`L-25804`; PRs #233, #235, #241, #250  
Scope: conditional finite-to-global deduction; `PADT(K)` itself remains open

## 1. Assumptions

Assume there is an unbounded sequence of packet orders `K` for which
`PADT(K)` holds with:

\[
\delta_0,\delta_1\ge\delta_*>0,
\tag{T-25801.1}
\]

and

\[
\eta_K\longrightarrow0.
\tag{T-25801.2}
\]

Let

\[
T_{K,V}=\Lambda*r_V^{*(K-1)}
\]

be the top source, and let `E_top(K,J)` denote its reviewed two-frequency
physical block energy.

The corrected packet grammar and direct terminal partition supply the complete
source as

\[
Q_K=Q_K^{\rm top}+Q_K^{\rm non-top},
\tag{T-25801.3}
\]

where the non-top part is exponentially small after the declared superorder
Euler closure.

## 2. Depleted-source estimate

A `PADT(K,J)` certificate proves for

\[
Z_{K,V,Q}=a_Q*T_{K,V}
\]

that

\[
\boxed{
E_Z(K,J)
\le
\exp\{(\eta_K+o_K(1))J\}
\left[
1+
\max_\tau
\max_{u\le(1-\delta_1)J+C_K}
E_{K,\tau}(u)
\right].}
\tag{T-25801.4}
\]

The `Q`-shifted member of the depletion dipole is routed below

\[
(1-\delta_0+O(1/K))J+O_K(1).
\]

After decreasing `delta_*` once, every destination lies below

\[
(1-\delta_*/2)J+C_K
\tag{T-25801.5}
\]

for all sufficiently large `K` in the sequence.

## 3. Exact recovery cost

By `L-25803`,

\[
T_{K,V}=H_Q*\mu_V*Z_{K,V,Q}
\tag{T-25801.6}
\]

on the complete active coefficient range.

The normalized radix inverse satisfies

\[
\|H_Q^\#\|_{\rm TV}
\le(1-Q^{-1/2})^{-1}=1+o_K(1).
\]

The one truncated Möbius coordinate satisfies

\[
\left(
\sum_{a\le V}{|\mu(a)|\over\sqrt a}
\right)^2
\le
V^{1+o(1)}
=
\exp\left[
\left({1\over K}+o_K(1)\right)J
\right].
\tag{T-25801.7}
\]

Causal shifts enlarge a unit block only by a fixed-order interval and do not
change the exponential rate. Therefore (T-25801.4)--(T-25801.7) give

\[
\boxed{
E_{\rm top}(K,J)
\le
\exp\left[
\left(
{1\over K}+\eta_K+o_K(1)
\right)J
\right]
\left[
1+
\max_\tau
\max_{u\le(1-\delta_*/2)J+C_K}
E_{K,\tau}(u)
\right].}
\tag{T-25801.8}
\]

Thus `PADT(K)` supplies `PARC(K)` with

\[
\boxed{\varepsilon_K={1\over K}+\eta_K.}
\tag{T-25801.9}
\]

## 4. Complete packet recurrence

The non-top rows are exponentially negligible and the terminal Type-I rows are
already Euler-small. Incorporating them into (T-25801.8) yields

\[
\boxed{
M_K(J)
\le
\exp\{(\varepsilon_K+o_K(1))J\}
\left[
1+
\max_{u\le(1-\delta_*/2)J+C_K}M_K(u)
\right].}
\tag{T-25801.10}
\]

No balanced inequality is imported from the withdrawn induction of old
`L-23203`; (T-25801.10) is the output of the transport certificate.

## 5. Scale contraction

Iterating (T-25801.10) gives

\[
\limsup_{J\to\infty}{\log M_K(J)\over J}
\le
{2\varepsilon_K\over\delta_*}.
\tag{T-25801.11}
\]

Under the safe-window rightmost-zero transfer, the left side dominates
`2 Theta_zeta`. Hence

\[
\boxed{
2\Theta_\zeta
\le
{2\over\delta_*}
\left({1\over K}+\eta_K\right).}
\tag{T-25801.12}
\]

Letting `K` tend to infinity along the certificate sequence gives

\[
\Theta_\zeta=0.
\]

Functional-equation symmetry therefore yields

\[
\boxed{\mathrm{RH}.}
\tag{T-25801.13}
\]

## 6. Scalar audit

The certificate exports a fixed-ratio Möbius shell. The all-ratio causal
transfer of PR #236 then gives

\[
M(x)-M(cx)=O_\varepsilon(x^{1/2+\varepsilon})
\]

for every fixed `0<c<1`, and geometric reconstruction gives the classical
Mertens formulation of RH.

This is an audit of the same proof object, not an additional hypothesis.

## 7. Why the theorem does not assume RH

The conditional chain uses:

- exact finite convolution identities;
- the reviewed physical block;
- a finite signed transport certificate;
- a stable radix filter;
- one explicit truncated-coordinate cost;
- a strict logarithmic destination gap.

It does not assume a zero-free region, generic parity-comb coercivity, a
Mertens estimate, or arbitrary-vector Type-II cancellation.

## 8. Proof boundary

Complete conditionally, subject to normalization review:

\[
\mathrm{PADT}(K)\text{ family}
\Longrightarrow
\mathrm{PARC}(K)
\Longrightarrow
\text{strict scale recurrence}
\Longrightarrow
\mathrm{RH}.
\]

Not supplied here:

- a production signed flow;
- the quadratic cost estimate (D-25801.7);
- an unbounded `PADT(K)` family;
- an unconditional proof of RH.
