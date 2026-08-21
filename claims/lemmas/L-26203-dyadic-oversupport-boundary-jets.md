# L-26203 — Dyadic oversupport and the exact Mertens boundary jets

Claim ID: `L-26203`  
Title: Completing every dyadic pair makes the full source half-pole-null, while the oversupport collar retains exactly the dyadic Mertens shell and its logarithmic companion  
Status: **PROPOSED EXACT FINITE LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-02-r`  
Created: 2026-08-08  
Dependencies: `L-26201`; dyadic coefficient identity of PRs #234/#236  
Scope: every real endpoint `Y>=1`

## 1. Truncated Möbius source

Put

\[
\eta_Y
=
\sum_{n\le Y}\frac{\mu(n)}{\sqrt n}\,\delta_{\log n}
\tag{L-26203.1}
\]

and complete it by the weighted dyadic difference

\[
\boxed{
\widetilde\eta_Y
=(I-2^{-1/2}\tau_{\log2})\eta_Y.}
\tag{L-26203.2}
\]

Its support lies in `[0,log(2Y)]`.

## 2. Exact half-pole cancellation

The weighted half-pole moment is

\[
\begin{aligned}
A(\widetilde\eta_Y)
&=\sum_{n\le Y}\mu(n)
 -\sum_{n\le Y}\mu(n)\\
&=0.
\end{aligned}
\tag{L-26203.3}
\]

Therefore the complete oversupported source lies in the exact positive cone of
`L-26201`.

## 3. Inner dyadic coefficient

For every integer `m<=Y`, the coefficient of `delta_(log m)` in
`widetilde eta_Y` is

\[
\boxed{
\frac{b_2(m)}{\sqrt m},
\qquad
b_2(m)=\mu(m)-\mathbf1_{2\mid m}\mu(m/2).}
\tag{L-26203.4}
\]

Thus the inner block is exactly the Euler-aligned dyadic shell source, with no
approximation.

## 4. Oversupport collar

For `Y<m<=2Y`, only the shifted term survives. Writing `m=2n`, the collar is

\[
\boxed{
\eta_Y^{\rm bd}
=-\sum_{Y/2<n\le Y}
\frac{\mu(n)}{\sqrt{2n}}\,\delta_{\log(2n)}.}
\tag{L-26203.5}
\]

Its two boundary jets are

\[
\boxed{
A_Y^{\rm bd}
=-\sum_{Y/2<n\le Y}\mu(n)
=-\bigl[M(Y)-M(Y/2)\bigr],}
\tag{L-26203.6}
\]

and

\[
\boxed{
B_Y^{\rm bd}
=-\sum_{Y/2<n\le Y}\mu(n)\log(2n).}
\tag{L-26203.7}
\]

The inner dyadic block has the opposite half-pole moment, so the complete source
is null as required.

## 5. Firewall property

Equation (L-26203.6) is the fixed-ratio Mertens shell. It is not discarded,
smoothed away, or replaced by a generic operator norm. Any claimed boundary
reserve must pay this coherent scalar mode.

By the causal all-ratio transfer of PR #236, control of the dyadic shell is
exponentially equivalent to control of the exact `2/3` first Farey cell. Thus a
production certificate must export both scalar projections.

## 6. Digital endpoint ledger

The coefficient dual to the dyadic aligned source is

\[
c_2(n)=1-v_2(n),
\]

and its exact partial sum is

\[
\boxed{
\sum_{n\le N}c_2(n)=s_2(N)\ge0,}
\tag{L-26203.8}
\]

where `s_2(N)` is the sum of the binary digits of `N`. This positive endpoint
identity is retained as a reserve; it is not used to infer a false Hankel
positivity statement.

## 7. Proof boundary

Closed exactly:

- oversupport half-pole cancellation;
- the inner dyadic source;
- the boundary collar;
- the two Mertens jets;
- the binary endpoint identity.

Open:

- a source-specific reflected/digital inequality paying the boundary jets;
- RH.
