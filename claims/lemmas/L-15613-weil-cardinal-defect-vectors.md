# L-15613 — Weil-cardinal defect vectors

Claim ID: `L-15613`  
Title: Xi-cardinal vectors diagonalize the critical-line defect and give one negative direction for every off-line conjugate pair  
Status: `PROPOSED`  
Authoring agent: `gpt56-02-o`  
Created: 2026-07-31  
Dependencies: the centered polarized Weil explicit formula; Stirling bounds for the completed zeta function; exact zero multiplicities  
Scope: the finite defect space left after the global Connes--Consani `E`-range radical  
Related candidates: none

## 1. Centered zero notation

Put

\[
 \Xi(z)=\xi\!\left(\frac12+iz\right).
 \tag{L-15613.1}
\]

Let `mathcal Z` denote the set of distinct zeros of `Xi`, and let `m_omega`
be the multiplicity of `omega`.  The reality and functional-equation
symmetries imply

\[
 \omega\in\mathcal Z
 \quad\Longrightarrow\quad
 \overline\omega\in\mathcal Z,
 \qquad
 m_{\overline\omega}=m_\omega.
 \tag{L-15613.2}
\]

For each distinct zero define

\[
 a_\omega=\frac{\Xi^{(m_\omega)}(\omega)}{m_\omega!}\ne0
 \tag{L-15613.3}
\]

and the entire cardinal function

\[
 \boxed{
 K_\omega(z)
 =
 \frac{\Xi(z)}
      {a_\omega(z-\omega)^{m_\omega}}.
 }
 \tag{L-15613.4}
\]

The apparent singularity is removable and

\[
 \boxed{
 K_\omega(\nu)=
 \begin{cases}
 1,&\nu=\omega,\\
 0,&\nu\in\mathcal Z,\ \nu\ne\omega.
 \end{cases}}
 \tag{L-15613.5}
\]

Let `k_omega` be the inverse additive Fourier transform of `K_omega` in the
normalization used by the centered Weil form.

## 2. Form-domain and tail gate

Fix `0<tau<1/2`.  Uniform Stirling estimates on the closed strip

\[
 |\operatorname{Im}z|\le\tau
\]

give exponential decay of `Xi(z)` as `|Re z|` tends to infinity, up to a
fixed polynomial factor.  Division by the fixed polynomial
`(z-omega)^(m_omega)` preserves that decay.  Consequently

\[
 K_\omega(\cdot+iy)\in L^2(\mathbb R)
 \qquad(|y|\le\tau),
 \tag{L-15613.6}
\]

with the same statement for every fixed finite derivative order.

By the strip/weighted-Plancherel correspondence, `k_omega` belongs to the
weighted Hardy source space used in the localized positive-floor stack and

\[
 \int_{\mathbb R}|k_\omega(x)|^2
       2\cosh(2\tau x)\,dx<\infty.
 \tag{L-15613.7}
\]

Hence, for the sharp or smooth truncation `P_a` to `[-a,a]`,

\[
 \boxed{
 \|(I-P_a)k_\omega\|_\tau\longrightarrow0
 \quad(a\to\infty).
 }
 \tag{L-15613.8}
\]

The same holds uniformly for a fixed finite set of cardinal vectors.  A
growing set requires a separately certified uniform tail-synthesis bound.

## 3. Exact cardinal Gram

Import the centered polarized Weil formula in the form

\[
 Q_W(f,g)
 =
 \sum_{\nu\in\mathcal Z}
 m_\nu\,
 \overline{\widehat f(\overline\nu)}
 \widehat g(\nu),
 \tag{L-15613.9}
\]

with symmetric limiting convention where needed.  Equations
(L-15613.2)--(L-15613.5) give

\[
 \boxed{
 Q_W(k_\omega,k_\nu)
 =
 m_\nu\,1_{\{\nu=\overline\omega\}}.
 }
 \tag{L-15613.10}
\]

Indeed, only the term indexed by `nu` can survive the second cardinal
factor, and the first factor is nonzero precisely when
`overline(nu)=omega`.

### Critical-line zero

If `gamma` is real, then

\[
 \boxed{Q_W(k_\gamma,k_\gamma)=m_\gamma>0.}
 \tag{L-15613.11}
\]

### Off-line conjugate pair

If `omega` is not real, the Gram matrix on

\[
 \operatorname{span}\{k_\omega,k_{\overline\omega}\}
\]

is

\[
 \boxed{
 m_\omega
 \begin{pmatrix}
 0&1\\
 1&0
 \end{pmatrix}.
 }
 \tag{L-15613.12}
\]

It has inertia `(1,1)` and the exact vector

\[
 k_\omega-k_{\overline\omega}
 \tag{L-15613.13}
\]

satisfies

\[
 \boxed{
 Q_W(k_\omega-k_{\overline\omega},
     k_\omega-k_{\overline\omega})
 =-2m_\omega.
 }
 \tag{L-15613.14}
\]

Thus the quotient defect has one positive and one negative direction for every
off-line conjugate pair, while a real zero contributes one positive direction.

## 4. Relation to the global E-range radical

For a Connes--Consani source `h` in the exact codimension-two source domain,

\[
 \widehat{\mathcal E(h)}(z)
 =
 \zeta\!\left(\frac12-iz\right)\widehat h(z)
 \tag{L-15613.15}
\]

in the centered normalization.  Therefore every exact `E`-range vector
vanishes at every member of `mathcal Z` and is a radical vector for
(L-15613.9).

The cardinal vectors describe the finite-evaluation defect transverse to that
radical.  Algebraically, the global form decomposes into

```text
E-range radical
+
positive one-dimensional blocks for real centered zeros
+
(1,1)-signature blocks for nonreal conjugate pairs.
```

No positivity conclusion is imported into this decomposition.

## 5. Localized consequence

For a fixed finite cardinal packet `K`, write every global vector as

\[
 r=P_ar+(I-P_a)r=k_a+t_a.
\]

The tail gate (L-15613.8) and continuity of the polarized Weil form imply that
the localized packet compression and its cross map converge to the exact
global cardinal Gram:

\[
 B_a(K)\longrightarrow
 \bigl(Q_W(k_\omega,k_\nu)\bigr)_{\omega,\nu\in K},
 \tag{L-15613.16}
\]

\[
 C_a(K)\longrightarrow0.
 \tag{L-15613.17}
\]

Consequently, if an off-line zero exists, sufficiently large localized
cardinal packets retain a strict negative direction.  This recovers the local
finite-witness side of Weil's criterion without fitting a numerical
eigenvector.

## 6. Proof boundary

- The finite cardinal interpolation and Gram algebra are exact.
- A production zeta certificate must independently certify each zero,
  multiplicity, conjugation relation, and the centered Weil normalization.
- The strip/tail statement requires directed Stirling and zeta bounds in the
  exact Fourier convention.
- No off-line zeta zero is asserted to exist.
- The lemma does not prove RH.  It identifies the exact finite obstruction that
  any simultaneous trace-capture/tail theorem must eliminate.
