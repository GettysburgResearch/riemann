# L-15627 — Support averaging turns a sub-square-root complete frame into a cofinal complement floor

Claim ID: `L-15627`  
Title: A support-averaged local-Weyl theorem annihilates the extra-low spectral trace under one quantitative complete-frame condition  
Status: `PROPOSED — COMPLETE ABSTRACT COMPOSITION; ZETA FRAME-CONDITIONING GATE OPEN`  
Authoring agent: `gpt56-08`  
Created: 2026-08-01  
Dependencies: `L-15626`; the support large sieve of `L-16226`; the line-centered operator local-Weyl and alias ledgers `L-16220`--`L-16227`  
Scope: the last cofinal spectral-tail term in `L-15625`  
Related counterexample candidates: none

## 1. Effective complement family

Let `T` run through an unbounded sequence of dyadic scales. For every

\[
 R\in[T,2T]
\]

let `A_R` be a localized Weil operator, let `P_R` be the proof-grade
near-radical packet, and put

\[
 Q_R=I-P_R.
 \tag{L-15627.1}
\]

All finite visible and ambient positive blocks may first be Schur eliminated;
`Q_RA_RQ_R` below denotes the resulting exact effective complement
compression. Let `G_R` be its positive production metric and whiten by
`G_R^(1/2)`.

Assume the complete effective complement admits a common coefficient
identification on each dyadic block and a decomposition

\[
 \boxed{
 G_R^{-1/2}Q_RA_RQ_RG_R^{-1/2}
 = (\log R)D_R+C_R+E_R^{\rm reg}+H_R.}
 \tag{L-15627.2}
\]

Here:

1. `D_R` is the main zero-density/profile Gram;
2. `C_R` is the bounded logarithmic-density correction;
3. `E_R^reg` contains the critical-line counting remainder, endpoint jets,
   Poisson aliases, finite prefix terms, Airy windows, and all directed
   approximation errors already handled without horizontal zero displacement;
4. `H_R` is the complete reflected off-line cross-branch contribution.

The decomposition is an interface: no sign is assigned to `H_R`.

## 2. Uniform positive main profile

Assume there is one constant `c_0>0` such that

\[
 \boxed{D_R\succeq c_0I}                                 \tag{L-15627.3}
\]

for all sufficiently large `T` and all retained `R in [T,2T]`, and

\[
 \boxed{
 \sup_{R\in[T,2T]}\|C_R\|=O(1),
 \qquad
 \sup_{R\in[T,2T]}\|E_R^{\rm reg}\|=o(\log T).}
 \tag{L-15627.4}
\]

The dimension-free line-centered estimates of `L-16220/L-16223`, the radial
normalization and alias Gram of `L-16222/L-16227`, and the endpoint ledger of
`L-16221` are designed to produce precisely (L-15627.3)--(L-15627.4) on a
complete, uniformly conditioned profile frame.

## 3. Support-averaged horizontal term

Assume the horizontal term is a fixed finite sum of Hilbert-valued radial phase
families to which `L-16226` applies after whitening. Let

\[
 \mathfrak B_T
\]

be a basis-invariant upper envelope for the corresponding whitened amplitudes
and their support derivatives. Concretely it bounds, for every phase family,

\[
 \|A_{\rho,R}\|_{\mathrm{HS}}
 +T\|\partial_RA_{\rho,R}\|_{\mathrm{HS}}
 \le\mathfrak B_T,                                       \tag{L-15627.5}
\]

where Hilbert--Schmidt operators are used as the coefficient Hilbert space.
The unit-interval zero count is `O(log T)`, so the support large sieve gives

\[
 \boxed{
 {1\over T}\int_T^{2T}\|H_R\|_{\rm op}^2\,dR
 \le
 C{\mathfrak B_T^2(\log T)^3\over T}
 +o((\log T)^2).}
 \tag{L-15627.6}
\]

The operator norm is bounded by the Hilbert--Schmidt norm used in the large
sieve.

The exact subcritical conditioning target is

\[
 \boxed{
 \mathfrak B_T
 =o\!\left(\sqrt{T\over\log T}\right).}
 \tag{L-15627.7}
\]

Under (L-15627.7), the right side of (L-15627.6) is `o((log T)^2)`.
Consequently there exists

\[
 R_T\in[T,2T]
 \tag{L-15627.8}
\]

such that

\[
 \boxed{\|H_{R_T}\|=o(\log R_T).}                        \tag{L-15627.9}
\]

The point `R_T` may simultaneously avoid every prescribed countable set and
satisfy any finite or polylogarithmic collection of additional averaged error
budgets whose summed exceptional measures tend to zero.

## 4. Cofinal complement floor

Combining (L-15627.2)--(L-15627.4) and (L-15627.9) gives

\[
 G_{R_T}^{-1/2}Q_{R_T}A_{R_T}Q_{R_T}G_{R_T}^{-1/2}
 \succeq
 [c_0\log R_T-o(\log R_T)]I.
 \tag{L-15627.10}
\]

Hence, on an unbounded subsequence `R_j`, one may take

\[
 \boxed{
 \gamma_j={c_0\over2}\log R_j,
 \qquad
 Q_jA_jQ_j\succeq\gamma_jG_j.}
 \tag{L-15627.11}
\]

Choose

\[
 \boxed{
 \Gamma_j={c_0\over4}\log R_j,
 \qquad
 0<t_j=o(\log R_j).}
 \tag{L-15627.12}
\]

Then

\[
 \gamma_j-\Gamma_j\asymp\log R_j,
 \qquad
 \Gamma_j-t_j\asymp\log R_j.                            \tag{L-15627.13}
\]

If the complete packet cross satisfies

\[
 P_jA_jQ_jG_j^{-1}Q_jA_jP_j\preceq\beta_j^2P_j           \tag{L-15627.14}
\]

and

\[
 \boxed{d_j\beta_j^2=o((\log R_j)^2),}                   \tag{L-15627.15}
\]

then `L-15626` gives

\[
 \begin{aligned}
 \operatorname{Tr}
 \left[Q_j(\Gamma_jI-A_j)_+Q_j\right]
 &\le
 {d_j\beta_j^2\over4(\gamma_j-\Gamma_j)}\\
 &=o(\log R_j)\\
 &=o(\Gamma_j-t_j).
 \end{aligned}                                           \tag{L-15627.16}
\]

Thus the exact final target is proved under the single complete-frame condition
(L-15627.7), together with the already-established rapidly decaying cross rate.
For the Gevrey/disjoint-bump packets, (L-15627.15) is automatic.

## 5. What is genuinely new

The prior pointwise horizontal estimate paid a worst-case factor at the
quadratic-log cutoff and met a one-log barrier. Equation (L-15627.6) uses the
support parameter itself as the averaging variable. It needs only one cofinal
sequence and therefore replaces pointwise control by the much weaker
square-root envelope (L-15627.7).

The required rate is extremely permissive:

\[
 \text{polylogarithmic conditioning}
 \quad\Longrightarrow\quad
 \mathfrak B_T=o\!\left(\sqrt{T/\log T}\right).
\]

Hence all radial, endpoint, alias, and growing-dimension estimates already
proved on the constructed prolate source frame lie safely below the threshold.
The unresolved issue is whether that well-conditioned constructed frame is a
frame for the **actual complete dangerous complement**.

## 6. Quantitative false-RH dichotomy

Assume the complete profile decomposition (L-15627.2), the positive Gram
(L-15627.3), and the regular-error estimate (L-15627.4). Assume also the
near-radical cross rates of `L-15617/L-15619`.

If a fixed extra low mode persists cofinally—for example the localized
Xi-cardinal difference produced by an off-line zero—then (L-15627.16) is
impossible. Consequently at least one of the following must occur:

\[
 \boxed{
 \begin{array}{ll}
 \text{(a)}&\inf_R\lambda_{\min}(D_R)\to0;\\[1mm]
 \text{(b)}&\displaystyle
 \limsup_{T\to\infty}
 \mathfrak B_T\sqrt{\log T\over T}>0;\\[2mm]
 \text{(c)}&\|E_R^{\rm reg}\|\not=o(\log R).
 \end{array}}
 \tag{L-15627.17}
\]

The current radial/endpoint/alias stack is aimed at excluding (c) and at proving
(a) false on the constructed frame. Therefore, for a complete frame, false RH
would force the explicit **square-root conditioning barrier**

\[
 \boxed{
 \mathfrak B_T\not=o\!\left(\sqrt{T/\log T}\right).}
 \tag{L-15627.18}
\]

This is the quantitative form of the off-line-cardinal obstruction.

## 7. Exact remaining repository gate

The existing results provide two complementary pieces:

1. the global-anchor/prolate construction has polylogarithmic coefficient
   conditioning and proof-grade radial/alias profiles;
2. generic support or local Möbius inversion gives qualitative/exact source
   surjectivity onto finite localized vectors.

They do **not** currently prove that the source right inverse onto the complete
`Q_R` packet has whitened profile envelope satisfying (L-15627.7).
`L-20301/L-20303` show why existence alone is insufficient: every exact local
extension preserves the target's zeta-zero signature in its lower tail.

Thus the exact blocker is now the quantitative complete-source-frame theorem

\[
 \boxed{
 \text{construct a cofinal complete complement frame with }
 \mathfrak B_T=o\!\left(\sqrt{T/\log T}\right).}
 \tag{L-15627.19}
\]

A polylogarithmic bound would be more than enough. Under false RH such a theorem
cannot hold, so proving it is a genuinely RH-resolving structural statement,
not completed defect bookkeeping.

## 8. Proof boundary

- The support-average-to-floor composition and the spectral-trace conclusion
  are exact under the displayed profile hypotheses.
- The support large-sieve estimate is inherited from `L-16226` and should be
  independently audited in the production normalization.
- The theorem does not prove (L-15627.7) for the actual complete zeta packet.
- No proof of RH is claimed until the complete-source-frame conditioning gate is
  supplied.
