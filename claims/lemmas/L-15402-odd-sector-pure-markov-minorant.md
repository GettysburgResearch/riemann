# L-15402 — A pure Markov minorant for the odd localized Weil sector

Claim ID: `L-15402`  
Title: Odd parity absorbs the negative polar rank one into a positive jump kernel  
Status: `PROPOSED`  
Authoring agent: `gpt56-05-l`  
Created: 2026-07-31  
Dependencies: L-15401; Yoshida's odd-function sufficiency as summarized and rederived in Suzuki, arXiv:2606.09096  
Scope: lower bounds for odd functions in the scaled localized form  
Related counterexample candidates: none

## Motivation

L-15401 leaves one negative odd polar channel.  T-15401 controls it through one
Birman--Schwinger scalar.  On the odd sector there is a second option: pass to
the half interval and rewrite the negative rank-one form itself as a positive
jump energy minus an explicit local potential.

The result is a pure nonlocal Schrödinger/Markov form to which the Barta identity
applies directly.  The price is that some positive cross-origin jump energies
are discarded.

## Half-interval notation

Let

\[
 I_+=(0,1),
 \qquad
 s_a(x)=\sinh(ax/2),
 \qquad
 S_a=\int_0^1s_a(y)\,dy
     =\frac2a\bigl(\cosh(a/2)-1\bigr).
\tag{L-15402.1}
\]

For `f` on `I_+`, let `w` be its odd extension:

\[
 w(x)=f(x),\quad x>0,
 \qquad
 w(-x)=-f(x).
\tag{L-15402.2}
\]

Then

\[
 \|w\|_{L^2(-1,1)}^2=2\|f\|_{L^2(0,1)}^2.
\tag{L-15402.3}
\]

Use `K_a`, `V_a`, `c_n`, and `\delta_n` from L-15401.

## Retained same-side jump form

Define

\[
\begin{aligned}
 \mathfrak h_a^-(f)={}&
 \int_0^1\int_0^1
 K_a(|x-y|)|f(x)-f(y)|^2\,dx\,dy\\
 &+2\sum_{\substack{n\le e^{2a}\\\delta_n<1}}c_n
 \int_0^{1-\delta_n}|f(x+\delta_n)-f(x)|^2\,dx\\
 &+4a\int_0^1\int_0^1
 s_a(x)s_a(y)|f(x)-f(y)|^2\,dx\,dy\\
 &+\int_0^1W_a^-(x)|f(x)|^2\,dx,
\end{aligned}
\tag{L-15402.4}
\]

where

\[
\boxed{
 W_a^-(x)=2V_a(x)-8aS_as_a(x).}
\tag{L-15402.5}
\]

Every double or translated difference term in (L-15402.4) has a nonnegative
weight.

## Odd-sector minorization theorem

For every odd core function `w` and its half-interval representative `f`,

\[
\boxed{
 q_a(w)\ge\mathfrak h_a^-(f).}
\tag{L-15402.6}
\]

Consequently, if a positive half-interval supersolution `\psi` proves

\[
 \mathfrak h_a^-(f)\ge m_a^-\|f\|_2^2
\tag{L-15402.7}
\]

for all core functions, then

\[
\boxed{
 \frac{q_a(w)}{\|w\|_2^2}\ge\frac{m_a^-}{2}
 \quad\text{for every odd }w.}
\tag{L-15402.8}
\]

No polar resolvent remains.

## Proof

### 1. Continuous jump quadrants

For odd `w`, split the continuous jump form into the four sign quadrants.  The
same-sign quadrants give

\[
 \int_0^1\int_0^1K_a(|x-y|)|f(x)-f(y)|^2\,dx\,dy.
\tag{L-15402.9}
\]

The opposite-sign quadrants give

\[
 \int_0^1\int_0^1K_a(x+y)|f(x)+f(y)|^2\,dx\,dy\ge0.
\tag{L-15402.10}
\]

Equation (L-15402.4) retains (L-15402.9) and discards only the nonnegative term
(L-15402.10).

### 2. Prime-shift jumps

For `\delta<1`, the positive-positive and negative-negative pieces of

\[
 c_n\int_{-1}^{1-\delta}|w(x+\delta)-w(x)|^2\,dx
\]

are equal and sum to

\[
 2c_n\int_0^{1-\delta}|f(x+\delta)-f(x)|^2\,dx.
\tag{L-15402.11}
\]

The remaining piece crosses the origin and is a squared modulus, hence
nonnegative.  When `\delta\ge1`, the complete translated difference crosses the
origin and is nonnegative.  Thus retaining only (L-15402.11) is a valid lower
minorant.

### 3. Polar channel

For odd `w`,

\[
 C_a(w)=0,
 \qquad
 S_a(w)=2\int_0^1s_a(x)f(x)\,dx.
\]

Therefore the polar contribution is

\[
 -2a|S_a(w)|^2
 =-8a\left|\int_0^1s_a(x)f(x)\,dx\right|^2.
\tag{L-15402.12}
\]

The exact rank-one ground-state identity

\[
\begin{aligned}
 -8a\left|\int s_af\right|^2
 ={}&4a\int_0^1\int_0^1
 s_a(x)s_a(y)|f(x)-f(y)|^2\,dx\,dy\\
 &-8aS_a\int_0^1s_a(x)|f(x)|^2\,dx
\end{aligned}
\tag{L-15402.13}
\]

follows by expanding the squared difference.  This is precisely the third line
of (L-15402.4) and the second term of (L-15402.5).

### 4. Local potential and norm

Because `V_a` is even,

\[
 \int_{-1}^1V_a(x)|w(x)|^2\,dx
 =2\int_0^1V_a(x)|f(x)|^2\,dx.
\]

Combining this identity with (L-15402.9)–(L-15402.13) proves
(L-15402.6).  Dividing by (L-15402.3) proves (L-15402.8).  QED.

## Explicit half-interval Barta residual

The jump measure in (L-15402.4) consists of:

1. continuous density `2K_a(|x-y|)` in standard
   `\frac12\int\!\int J|f(x)-f(y)|^2` normalization;
2. same-side prime atoms of weight `2c_n`;
3. continuous rank density `8a s_a(x)s_a(y)`.

For `\psi>0`, define

\[
\begin{aligned}
 b_{a,\psi}^-(x)={}&W_a^-(x)\\
 &+\frac{2}{\psi(x)}\int_0^1K_a(|x-y|)
   \bigl(\psi(x)-\psi(y)\bigr)\,dy\\
 &+\frac{2}{\psi(x)}
  \sum_{\substack{n\le e^{2a}\\\delta_n<1}}c_n
  \Bigl[
   \mathbf1_{x+\delta_n<1}
    \bigl(\psi(x)-\psi(x+\delta_n)\bigr)\\
 &\hspace{48mm}+\mathbf1_{x-\delta_n>0}
    \bigl(\psi(x)-\psi(x-\delta_n)\bigr)
  \Bigr]\\
 &+\frac{8a s_a(x)}{\psi(x)}
   \int_0^1s_a(y)\bigl(\psi(x)-\psi(y)\bigr)\,dy.
\end{aligned}
\tag{L-15402.14}
\]

T-15401 gives

\[
 m_a^-=\operatorname*{ess\,inf}_{x\in(0,1)}b_{a,\psi}^-(x)
\tag{L-15402.15}
\]

as a valid half-form floor.

The last line of (L-15402.14) combines with the polar killing term in
`W_a^-`; implementations should preserve this correlation instead of widening
them independently.

## RH consequence

Yoshida proved that strict Weil positivity on all nonzero odd compactly
supported test functions implies RH.  Thus either of the following suffices:

1. `m_a^-\ge0` for every positive rational `a`, with density/continuity filling
   all supports;
2. an unbounded support sequence with cofinal lower bounds
   `m_{a_j}^-/2\ge-\varepsilon_j`, `\varepsilon_j\to0`, together with the odd
   support monotonicity argument analogous to T-14302.

The present lemma does not construct such a cofinal supersolution family.

## Strength and weakness relative to T-15401

Advantages:

- no resolvent scalar;
- no spectral packet;
- one pure positive-jump Barta certificate on `(0,1)`;
- directly targets the odd sector, already sufficient for RH.

Cost:

- cross-origin continuous and prime difference energies are discarded;
- the resulting local potential may be substantially more negative;
- a T-15401 scalar correction may be much sharper at finite support.

Both routes should be evaluated before selecting the production architecture.

## Gap audit

- Factors of two depend on the full-to-half norm conversion and must be audited
  independently.
- Cross-origin terms are discarded only after being represented as squared
  moduli with nonnegative weights.
- The negative polar rank one must be rewritten exactly as in
  (L-15402.13); simply dropping it is invalid.
- The half-interval supersolution must be strictly positive on the interior.
- A finite set of positive supports is not RH.
