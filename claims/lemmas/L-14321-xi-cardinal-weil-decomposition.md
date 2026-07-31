# L-14321 — Xi-cardinal functions give exact positive Weil coordinates

Claim ID: `L-14321`  
Title: Dividing Xi by a certified simple real zero produces a two-sided rapidly decaying cardinal function and an exact Weil-orthogonal interpolation splitting  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-09-c`  
Created: 2026-07-31  
Dependencies: the Fourier-kernel representation of Riemann's `Xi`; the zero-sum Weil spectral formula; elementary first-order Fourier calculus  
Scope: exact positive coordinates for the evaluation-visible block in PR #168  
Related counterexample candidates: none

## Purpose

The preceding route used certified zero evaluations in two ways:

1. `L-15304` used them to obstruct approximation by small-tail radical vectors;
2. `L-14319/L-14320` used them as a positive frame and an S-lemma visibility metric.

There is a stronger exact construction.  If `gamma` is a certified simple real
zero of `Xi`, then

\[
 \frac{\Xi(z)}{z-\gamma}
\]

is the Fourier transform of a rapidly decaying function that evaluates to zero
at **every** zeta zero except `gamma`.  These functions are exact cardinal
coordinates for the zero spectral measure.  They split any test vector into:

```text
an exact positive selected-zero block
+
a Weil-orthogonal remainder vanishing at the selected zeros.
```

This is the completed-Xi counterpart of the zero-attached complete/minimal
systems studied by Burnol in Sonine/de Branges spaces.

## 1. Riemann Fourier kernel

Use the centered convention

\[
 \Xi(z)=\xi\!\left(\frac12+iz\right)
       =\int_{\mathbb R}\Phi(t)e^{-izt}\,dt,
 \tag{L-14321.1}
\]

where `Phi` is the standard real even Riemann kernel.  It is smooth and
superexponentially decreasing at both ends.  The proof below only needs that
`Phi` is Schwartz; the stronger tail is used for localization.

Let `gamma` be a simple real zero:

\[
 \Xi(\gamma)=0,
 \qquad
 \Xi'(\gamma)\ne0.
 \tag{L-14321.2}
\]

Define

\[
 \psi_\gamma(t)
 =i e^{i\gamma t}
   \int_{-\infty}^{t}e^{-i\gamma u}\Phi(u)\,du.
 \tag{L-14321.3}
\]

Because the complete integral equals `Xi(gamma)=0`, one also has

\[
 \boxed{
 \psi_\gamma(t)
 =-i e^{i\gamma t}
   \int_t^{\infty}e^{-i\gamma u}\Phi(u)\,du.}
 \tag{L-14321.4}
\]

Thus the same function is controlled by the left tail as `t->-infinity` and by
the right tail as `t->+infinity`.

## 2. Exact cardinal transform

Differentiating (L-14321.3) gives

\[
 (-i\partial_t-\gamma)\psi_\gamma=\Phi.
 \tag{L-14321.5}
\]

Since both boundary tails vanish, Fourier transformation yields

\[
 (z-\gamma)\widehat{\psi_\gamma}(z)=\Xi(z).
\]

Therefore

\[
 \boxed{
 \widehat{\psi_\gamma}(z)
 =\frac{\Xi(z)}{z-\gamma},}
 \tag{L-14321.6}
\]

with the singularity at `gamma` removed.  In particular,

\[
 \widehat{\psi_\gamma}(\gamma)=\Xi'(\gamma).
 \tag{L-14321.7}
\]

The two tail formulas and differentiation of (L-14321.5) show

\[
 \boxed{\psi_\gamma\in\mathcal S(\mathbb R).}
 \tag{L-14321.8}
\]

For every integer `N`, a constant depending on `N` and `gamma` satisfies

\[
 |\partial_t^j\psi_\gamma(t)|
 \le C_{N,j,\gamma}(1+|t|)^{-N}.
\]

With the explicit Riemann kernel, the decay is superexponential.

Normalize

\[
 \ell_\gamma=\frac{\psi_\gamma}{\Xi'(\gamma)}.
 \tag{L-14321.9}
\]

For every zero `lambda` of `Xi`, regardless of whether it is real or nonreal,

\[
 \boxed{
 \widehat{\ell_\gamma}(\lambda)
 =\begin{cases}
 1,&\lambda=\gamma,\\
 0,&\lambda\ne\gamma.
 \end{cases}}
 \tag{L-14321.10}
\]

The selected zero must be simple; unselected zeros may have arbitrary
multiplicity.

## 3. Exact Weil-orthogonal interpolation

Let

\[
 Z=\{\gamma_1,\ldots,\gamma_m\}
 \tag{L-14321.11}
\]

be distinct certified simple real zeros.  Define

\[
 C_Za=\sum_{j=1}^m a_j\ell_{\gamma_j},
 \qquad
 V_Zf=(\widehat f(\gamma_1),\ldots,\widehat f(\gamma_m)),
 \tag{L-14321.12}
\]

and

\[
 R_Z=I-C_ZV_Z.
 \tag{L-14321.13}
\]

Then

\[
 \boxed{V_ZC_Z=I,\qquad V_ZR_Z=0,\qquad R_Z^2=R_Z.}
 \tag{L-14321.14}
\]

Now use the polarized Weil zero-sum form in the centered convention,

\[
 Q_W(f,g)
 =\sum_\lambda m_\lambda
   \widehat f(\lambda)
   \overline{\widehat g(\overline\lambda)},
 \tag{L-14321.15}
\]

with the declared symmetric limiting convention.  Since each selected zero is
simple and real, (L-14321.10) gives

\[
 \boxed{
 Q_W(C_Za,C_Zb)=\sum_{j=1}^m a_j\overline{b_j},}
 \tag{L-14321.16}
\]

\[
 \boxed{Q_W(R_Zf,C_Za)=0,}
 \tag{L-14321.17}
\]

and therefore

\[
 \boxed{
 Q_W(f,g)
 =Q_W(R_Zf,R_Zg)
  +\sum_{j=1}^m
    \widehat f(\gamma_j)
    \overline{\widehat g(\gamma_j)}.}
 \tag{L-14321.18}
\]

In particular,

\[
 \boxed{
 Q_W(f,f)
 =Q_W(R_Zf,R_Zf)
  +\|V_Zf\|_2^2.}
 \tag{L-14321.19}
\]

This is an exact global decomposition, not an estimate.  Every unselected
critical-line zero and every hypothetical off-line zero lies entirely in the
remainder term; the cardinal block is positive and Weil-orthogonal to it.

### Proof

The algebraic identities in (L-14321.14) follow from (L-14321.10).  At an
unselected zero, every cardinal transform vanishes.  At a selected zero
`gamma_j`, `R_Zf` vanishes and only the matching cardinal has value one.
Substitution into the zero-sum formula proves (L-14321.16)--(L-14321.19).
QED.

## 4. Immediate visible-cone floor

Let `P` be any finite packet in the Weil test/form domain.  Suppose on the
selected-zero near-kernel one has

\[
 Q_W(R_Zf,R_Zf)
 \ge-\varepsilon\|R_Zf\|_X^2
 \tag{L-14321.20}
\]

and

\[
 \|R_Zf\|_X\le\kappa\|f\|_G
 \tag{L-14321.21}
\]

for the finite packet metric `G`.  On the visibility cone

\[
 \|V_Zf\|_2^2\ge\delta^2\|f\|_G^2,
 \tag{L-14321.22}
\]

(L-14321.19) gives directly

\[
 \boxed{
 Q_W(f,f)
 \ge(\delta^2-\varepsilon\kappa^2)\|f\|_G^2.}
 \tag{L-14321.23}
\]

Thus the selected-zero correctors eliminate every cross term exactly.  The
S-lemma of `L-14319` remains useful when the near-kernel and visibility bounds
are supplied only as quadratic matrix inequalities, but no arbitrary visible
block is intrinsic.

## 5. Tail control and localization

Let

\[
 A_\Phi(T)=\int_{|u|\ge T}|\Phi(u)|\,du.
 \tag{L-14321.24}
\]

The two-sided formula immediately gives

\[
 \boxed{
 |\psi_\gamma(t)|\le A_\Phi(|t|).}
 \tag{L-14321.25}
\]

This unnormalized tail bound is independent of `gamma`.  For a finite selected
set, put

\[
 M_Z=\max_{\gamma\in Z}|\Xi'(\gamma)|^{-1}.
 \tag{L-14321.26}
\]

Then

\[
 |\ell_\gamma(t)|\le M_Z A_\Phi(|t|).
 \tag{L-14321.27}
\]

The same conclusion holds in every fixed Schwartz seminorm, with a finite
constant depending on the selected ordinates.  Consequently, if `P_L` denotes
truncation to `[-L,L]`, then for every fixed finite `Z`,

\[
 \boxed{
 (I-P_L)C_Z\longrightarrow0}
 \tag{L-14321.28}
\]

in Schwartz topology and hence in every continuous Weil graph/form norm.
Localized cardinal blocks therefore converge to the exact positive diagonal
block (L-14321.16), and their cross maps to the remainder tend to zero.

For a growing set `Z_L`, the proof-facing quantity is the norm of the normalized
cardinal tail synthesis operator.  A sufficient schematic condition is

\[
 \boxed{
 \sqrt{|Z_L|}\,M_{Z_L}\,
 \|(I-P_L)\psi\|_{X,\mathrm{envelope}}
 \longrightarrow0.}
 \tag{L-14321.29}
\]

The Riemann kernel's double-exponential tail makes very rapid growth admissible,
but no unconditional cofinal bound on `M_(Z_L)` is asserted here.

## 6. Unexpected connection to Burnol's zero systems

Burnol studied complete and minimal systems intrinsically attached to zeta
zeros, including functions of the shape

\[
 \frac{\zeta(s)}{(s-\rho)^k}
\]

inside Sonine/de Branges-related Hilbert spaces.  The present
`Xi(z)/(z-gamma)` functions are their completed centered cardinal analogue.
The elementary ODE formula (L-14321.3) adds a feature tailored to the repository:
it gives an explicit two-sided tail in the original logarithmic variable, so
the zero-coordinate system can be inserted into localized Weil block
certificates.

## Strategic consequence

The growing low-block architecture can now be organized as

```text
arbitrary finite low packet
 -> exact selected-zero interpolation C_Z V_Z
    + exact zero-near-kernel R_Z
 -> positive Weil-orthogonal cardinal block
    + residual near-kernel block
 -> localize; charge only cardinal tails and the near-kernel floor
 -> combine with L-14318/L-14308/T-14302.
```

The previous principal-angle question is replaced by a more concrete corrector
capacity question: can enough normalized Xi-cardinal functions be localized
with uniformly controlled tails relative to the support-dependent low rank?

## Gap audit

- The Fourier/zero-sum normalizations are imported and must be matched exactly.
- Selected zeros must be proof-grade, simple, and on the critical line.  It is
  known unconditionally that infinitely many simple critical-line zeros exist,
  but a production packet must bind each selected zero and derivative enclosure.
- `ell_gamma` is global, not compactly supported.  The localized theorem needs
  the tail/form-continuity gate in Section 5.
- The inverse derivative factor `M_Z` may be poorly conditioned; no cofinal
  lower bound for `|Xi'(gamma)|` is proved here.
- The remainder `R_Zf` still contains every unselected and hypothetical off-line
  zero.  Its lower floor remains a genuine analytic obligation.
- No RH proof is claimed.
