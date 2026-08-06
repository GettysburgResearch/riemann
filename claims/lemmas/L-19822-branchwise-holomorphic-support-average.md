# L-19822 — Branchwise holomorphic support averaging with the correct derivative scale

Claim ID: `L-19822`  
Status: **PROPOSED CONDITIONAL ANALYTIC THEOREM — WKB/AIRY/ALIAS INPUTS OPEN**  
Authoring agent: `gpt56-pro-09-o`  
Created: 2026-08-07  
Dependencies: abstract Hilbert-valued support large sieve `L-16226`; a holomorphic Dunster/WKB decomposition in a shrinking strip  
Scope: correct replacement for rejected `L-19821`; no RH claim

## 1. Purpose

The support translation in the normalized omitted-tail transform cancels from the
polarized zero-side quadratic kernel. Horizontal displacement must instead be
handled inside the incoming/outgoing radial branch decomposition.

This lemma gives an exact sufficient interface. It proves that a branchwise
holomorphic WKB expansion with one correctly scaled support derivative implies a
vanishing off-line support average. It does not claim that the required WKB,
Airy, endpoint, or infinite-alias estimates have already been proved for the
complete CCM packet.

## 2. Profile and strip

Let

\[
 m_R=O((\log R)^A)
\]

and let

\[
 \Phi_R(z):\mathbb C^{m_R}\longrightarrow Y_R
\]

be a finite-rank profile synthesis into a Hilbert space. Fix a compact real
frequency-ratio interval `I` and the shrinking strip

\[
 \mathcal S_R
 =\{z=x+iy:x\in I,\ |y|\le1/(2R)\}.
 \tag{L-19822.1}
\]

Assume a fixed finite branch decomposition

\[
 \boxed{
 \Phi_R(z)
 =\sum_{\nu=1}^{B}
   a_{\nu,R}(z)e^{iRS_\nu(z)}+e_R(z),}
 \tag{L-19822.2}
\]

where:

1. `B` is independent of `R`;
2. each `S_nu` is holomorphic near `I`, real-valued on `I`, and has uniformly
   bounded derivatives through order three;
3. each `a_(nu,R)` is operator-valued and holomorphic on `S_R`;
4. for one fixed `C`, uniformly on `S_R`,

   \[
   \begin{aligned}
   &\|a_{\nu,R}\|+\|\partial_z a_{\nu,R}\|
    +\|\partial_z^2a_{\nu,R}\|\\
   &\qquad
    +R\|\partial_Ra_{\nu,R}\|
    +R\|\partial_R\partial_za_{\nu,R}\|
    \le(\log R)^C;
   \end{aligned}
   \tag{L-19822.3}
   \]

5. the remainder and one support derivative satisfy

   \[
   \|e_R\|+R\|\partial_Re_R\|
   \le R^{-1}(\log R)^C.
   \tag{L-19822.4}
   \]

The norms may be operator or Hilbert--Schmidt norms, provided one convention is
used throughout.

## 3. Polarized branch products

Let

\[
 s_\rho=\gamma+i\delta,
 \qquad |\delta|<1/2,
 \qquad z_\rho={s_\rho\over R}=x+i\delta/R.
 \tag{L-19822.5}
\]

The support translation has already cancelled by `R-19805`. Expanding

\[
 \overline{\Phi_R(\overline z_\rho)}^{\,*}
 \Phi_R(z_\rho)
\]

using (L-19822.2), the `(nu,mu)` branch product contains the phase

\[
 \exp\{iR[S_\mu(z_\rho)-S_\nu(z_\rho)]\}.
 \tag{L-19822.6}
\]

Put

\[
 \Delta S_{\nu\mu}=S_\mu-S_\nu.
\]

Uniform Taylor expansion in the shrinking strip gives

\[
 R\Delta S_{\nu\mu}(x+i\delta/R)
 =R\Delta S_{\nu\mu}(x)
  +i\delta\Delta S_{\nu\mu}'(x)
  +O(R^{-1}),
 \tag{L-19822.7}
\]

and therefore

\[
 \boxed{
 e^{iR\Delta S_{\nu\mu}(x+i\delta/R)}
 =e^{iR\Delta S_{\nu\mu}(x)}
  e^{-\delta\Delta S_{\nu\mu}'(x)}
  (1+O(R^{-1})).}
 \tag{L-19822.8}
\]

Because `|delta|<1/2` and the branch derivatives are bounded, the horizontal
multiplier in (L-19822.8) is bounded above and below by constants independent of
`R` and of the zero.

## 4. Correct amplitude derivative

Fix one off-diagonal branch pair `nu!=mu`. Extract the real support phase

\[
 e^{iR\Delta S_{\nu\mu}(\gamma/R)}.
 \tag{L-19822.9}
\]

All remaining factors define an amplitude

\[
 A_{\rho,\nu\mu}(R).
\]

Equations (L-19822.3), (L-19822.7), and

\[
 {d\over dR}{s_\rho\over R}=-{s_\rho\over R^2}=O(R^{-1})
 \tag{L-19822.10}
\]

on `|gamma| asymp R` imply

\[
 \boxed{
 \|A_{\rho,\nu\mu}(R)\|
 +R\|\partial_RA_{\rho,\nu\mu}(R)\|
 \le(\log R)^{C'}.}
 \tag{L-19822.11}
\]

The factor `R` multiplying the derivative is essential. It is obtained only
after the rapid real branch phase has been extracted. Differentiating the full
oscillatory expression before this extraction does not satisfy the large-sieve
hypothesis.

For a diagonal branch `nu=mu`, the real phase vanishes. Holomorphic Taylor
expansion directly gives

\[
 \|K_{\nu\nu}(x+i\delta/R)-K_{\nu\nu}(x)\|
 \le R^{-1}(\log R)^{C'}.
 \tag{L-19822.12}
\]

After the external zero-side normalization and summation over
`O(R log R)` zeros in a dyadic ordinate window, the complete diagonal horizontal
replacement costs

\[
 O((\log R)^{C'}/R).
 \tag{L-19822.13}
\]

## 5. Support large sieve

For one off-diagonal branch family define

\[
 Z_T(R)
 ={1\over R}
 \sum_{\gamma\in\Gamma_T}
 e^{iR\Delta S(\gamma/R)}A_\gamma(R),
 \qquad T\le R\le2T,
 \tag{L-19822.14}
\]

where the ordinates satisfy the Riemann--von Mangoldt unit-bin bound

\[
 \#(\Gamma_T\cap[u,u+1])\ll\log T.
 \tag{L-19822.15}
\]

Put

\[
 F(x)=\Delta S(x)-x\Delta S'(x).
 \tag{L-19822.16}
\]

Assume the branch window can be divided into a fixed number of intervals on
which

\[
 |F'(x)|\ge c_0>0.
 \tag{L-19822.17}
\]

Then (L-19822.11) is exactly the amplitude hypothesis of `L-16226`, with
`B_T=(log T)^(C')`. Hence

\[
 \boxed{
 {1\over T}\int_T^{2T}\|Z_T(R)\|_{\rm HS}^2dR
 \ll { (\log T)^{C''}\over T}.}
 \tag{L-19822.18}
\]

For any polylogarithmic number of branch families, Markov's inequality and a
union bound produce a positive-measure subset of every sufficiently large
dyadic block on which all such cross-branch errors tend to zero simultaneously.

## 6. Fold, endpoint, and infinite-alias clauses

The conclusion above applies directly only on nonfold compact branch windows.
A complete CCM application additionally needs:

1. a holomorphic Airy decomposition on a shrinking fold neighborhood;
2. a proof that its exceptional support measure and complete operator
   contribution are `o(1)`;
3. extraction and collective summation of every non-absolutely-summable endpoint
   channel before estimating the alias remainder;
4. an absolutely summable remainder with the same strip and support-derivative
   bounds;
5. uniformity for all modes in the `O(log^2 R)` packet and in both Fourier-sign
   sectors.

These are hypotheses, not conclusions of the present lemma.

## 7. Consequence and boundary

Under the complete branch/Airy/endpoint hypotheses, the exact zero matrix and
the line-centered zero matrix differ by `o(1)` in the whitened omitted-tail
metric at one support in every sufficiently large dyadic block. In particular,
the erroneous `R^(1/4)` mechanism is unnecessary; the corrected mean square is
stronger, of order `polylog(R)/R`.

The theorem is a valid analytic adapter. It does not establish the required
Dunster complex-strip expansion, endpoint ledger, alias sum, source-frame
conditioning, signed `d_6` hierarchy, or RH.
