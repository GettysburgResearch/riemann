# T-25801 — Prime-Anchored Digit Transport implies RH

Claim ID: `T-25801`  
Title: A cofinal family of source-specific fixed-scale digit-transport certificates gives the balanced recurrence with loss `eta_K` and forces the rightmost-zero exponent to vanish  
Status: **PROPOSED COMPLETE CONDITIONAL COMPOSITION THEOREM PENDING REVIEW**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-07  
Corrected: 2026-08-07 after `R-25802`  
Issue: #258  
Dependencies: corrected `D-25801`; `L-25801`--`L-25806`; PRs #233, #235, #241, #250  
Scope: conditional finite-to-global deduction; `PADT(K)` itself remains open

## 1. Assumptions

Assume there is an unbounded sequence of packet orders `K` for which
`PADT(K)` holds with

\[
\delta_0,\delta_1\ge\delta_*>0
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

The corrected packet grammar supplies the complete source as

\[
Q_K=Q_K^{\rm top}+Q_K^{\rm non-top},
\tag{T-25801.3}
\]

where every non-top and terminal complete-lattice row has the separately
declared Euler or contour estimate.

## 2. Fixed-scale depletion dipole

Choose the dyadic radix

\[
Q=2^{L(J)},
\qquad
\log Q=\delta_0J+O(1),
\]

and put

\[
D_{K,V,Q}
=(\varepsilon-\delta_Q)*T_{K,V}
=\mu_V*Z_{K,V,Q}.
\tag{T-25801.4}
\]

A `PADT(K,J)` certificate proves

\[
\boxed{
E_D(K,J)
\le
\exp\{(\eta_K+o_K(1))J\}
\left[
1+
\max_\tau
\max_{u\le(1-\delta_1)J+C_K}
E_{K,\tau}(u)
\right].}
\tag{T-25801.5}

This is a direct estimate for the complete signed dipole `D`. It is not an
estimate for `Z` followed by an absolute recovery.

## 3. Exact physical recurrence

The coefficient identity

\[
T=\delta_Q*T+D
\]

becomes in the square-root normalized physical field

\[
\boxed{
\mathcal T_J
=Q^{-1/2}\mathcal T_{J-\log Q}
+\mathcal D_J.}
\tag{T-25801.6}

Therefore

\[
\boxed{
E_{\rm top}(K,J)
\le
2Q^{-1}E_{\rm top}(K,J-\log Q)
+2E_D(K,J).}
\tag{T-25801.7}

Since

\[
Q^{-1}=\exp\{-\delta_0J+O(1)\}
\]

and

\[
J-\log Q=(1-\delta_0)J+O(1),
\]

the first term is an exponentially damped strict lower-scale destination.

Combining (T-25801.5)--(T-25801.7), and replacing `delta_*` by a smaller fixed
constant once, gives

\[
\boxed{
E_{\rm top}(K,J)
\le
\exp\{(\eta_K+o_K(1))J\}
\left[
1+
\max_\tau
\max_{u\le(1-\delta_*/2)J+C_K}
E_{K,\tau}(u)
\right].}
\tag{T-25801.8}

Thus `PADT(K)` supplies the prime-anchored contraction with

\[
\boxed{\varepsilon_K=\eta_K.}
\tag{T-25801.9}

No `1/K` absolute-recovery loss is needed.

## 4. Complete packet recurrence

The non-top rows are exponentially negligible and the terminal Type-I rows are
already Euler-small. Incorporating them into (T-25801.8) yields

\[
\boxed{
M_K(J)
\le
\exp\{(\eta_K+o_K(1))J\}
\left[
1+
\max_{u\le(1-\delta_*/2)J+C_K}M_K(u)
\right].}
\tag{T-25801.10}

No balanced inequality is imported from the withdrawn induction of old
`L-23203`; (T-25801.10) is the output of the signed dipole certificate.

## 5. Scale contraction

Iteration gives

\[
\limsup_{J\to\infty}{\log M_K(J)\over J}
\le
{2\eta_K\over\delta_*}.
\tag{T-25801.11}

Under the safe-window rightmost-zero transfer, the left side dominates
`2 Theta_zeta`. Hence

\[
\boxed{
2\Theta_\zeta
\le
{2\eta_K\over\delta_*}.}
\tag{T-25801.12}

Letting `K` tend to infinity along the certificate sequence gives

\[
\Theta_\zeta=0.
\]

Functional-equation symmetry therefore yields

\[
\boxed{\mathrm{RH}.}
\tag{T-25801.13}

## 6. Scalar audit

The certificate exports a fixed-ratio Möbius shell. The all-ratio causal
transfer of PR #236 then gives

\[
M(x)-M(cx)=O_\varepsilon(x^{1/2+\varepsilon})
\]

for every fixed `0<c<1`, and geometric reconstruction gives the classical
Mertens formulation of RH.

The dyadic implementation additionally exports the parity-comb mutation of
`L-25806`. These are audits of the same proof object, not additional
hypotheses.

## 7. Why the theorem does not assume RH

The conditional chain uses:

- exact finite convolution identities;
- the reviewed physical block;
- a finite signed `mu_V` transport certificate;
- a positive nonmultiple-count potential;
- one explicit fixed-scale radix dipole;
- a strict logarithmic destination gap.

It does not assume a zero-free region, generic parity-comb coercivity, a
Mertens estimate, absolute recovery of `Z`, or arbitrary-vector Type-II
cancellation.

## 8. Proof boundary

Complete conditionally, subject to normalization review:

\[
\mathrm{PADT}(K)\text{ family}
\Longrightarrow
\text{fixed-scale prime-anchored recurrence}
\Longrightarrow
\mathrm{RH}.
\]

Not supplied here:

- a production signed flow;
- the quadratic dipole-cost estimate (D-25801.9);
- an unbounded `PADT(K)` family;
- an unconditional proof of RH.
