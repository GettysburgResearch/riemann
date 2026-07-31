# L-15401 — Exact jump–potential–polar decomposition of Suzuki's localized Weil form

Claim ID: `L-15401`  
Title: The logarithmic and smooth archimedean terms combine into one positive jump kernel, while the polar part has signature `(+,−)`  
Status: `PROPOSED`  
Authoring agent: `gpt56-05-l`  
Created: 2026-07-31  
Dependencies: Suzuki, arXiv:2606.09096, equations (4.4)–(4.6) and the decomposition `r=r_0+r_1` on page 11  
Scope: the scaled localized form `q_a` on the core `H_0^1(-1,1)`  
Related counterexample candidates: none

## Setup

Fix `a>0` and put

\[
 I=(-1,1),\qquad
 c_n=\frac{\Lambda(n)}{\sqrt n},\qquad
 \delta_n=\frac{\log n}{a}.
\]

Only `n\le e^{2a}` occur.  At the endpoint `\delta_n=2`, all translated
integrals below are empty and may be retained harmlessly.

Suzuki's equation (4.5) gives, for `w\in H_0^1(I)`,

\[
\begin{aligned}
 q_a(w)={}&\bigl[-\log a-(2A+1)\bigr]\|w\|_2^2+\mathcal L(w)\\
 &-\sum_{n\le e^{2a}}c_n\left(
   \int_{-1}^{1-\delta_n}w(x+\delta_n)\overline{w(x)}\,dx
  +\int_{-1+\delta_n}^{1}w(x-\delta_n)\overline{w(x)}\,dx\right)\\
 &-a\int_I\int_I r''(a(x-y))w(y)\overline{w(x)}\,dx\,dy,
\end{aligned}
\tag{L-15401.1}
\]

where

\[
 \mathcal L(w)=\frac14\int_I\int_I
 \frac{|w(x)-w(y)|^2}{|x-y|}\,dx\,dy
 -\frac12\int_I|w(x)|^2\log(1-x^2)\,dx.
\tag{L-15401.2}
\]

The source decomposes

\[
 r=r_0+r_1,
\qquad
 r_0(t)=-4(e^{t/2}+e^{-t/2}-2),
\tag{L-15401.3}
\]

and proves

\[
 r_1''(t)=\frac{e^{-|t|/2}}{1-e^{-2|t|}}-\frac1{2|t|}.
\tag{L-15401.4}
\]

## Positive continuous jump kernel

For `t>0`, define

\[
 K_a(t)=a\frac{e^{-at/2}}{1-e^{-2at}}
\tag{L-15401.5}
\]

and

\[
 F_a(t)=\frac1{2t}-K_a(t).
\tag{L-15401.6}
\]

The expansion

\[
 \frac{e^{-u/2}}{1-e^{-2u}}
 =\frac1{2u}+\frac14-\frac{u}{48}+O(u^2)
\]

shows that `F_a` extends continuously to zero with

\[
 \boxed{F_a(0)=-\frac a4.}
\tag{L-15401.7}
\]

Put

\[
 U_a(x)=\int_I F_a(|x-y|)\,dy.
\tag{L-15401.8}
\]

This is a finite continuous even function.  Equivalently,

\[
 U_a(x)=G_a(1+x)+G_a(1-x),
\qquad
 G_a(r)=\int_0^rF_a(t)\,dt.
\tag{L-15401.9}
\]

## Prime degree function

For `0<\delta\le2`, define

\[
 d_\delta(x)
 =\mathbf 1_{\{x+\delta\in I\}}
  +\mathbf 1_{\{x-\delta\in I\}}.
\tag{L-15401.10}
\]

Thus `d_\delta` records how many translated neighbors of `x` remain inside
`I`.

## Exact local potential

Define

\[
\boxed{
 V_a(x)=
 -\log a-(2A+1)
 -\frac12\log(1-x^2)
 +U_a(x)
 -\sum_{n\le e^{2a}}c_n d_{\delta_n}(x).}
\tag{L-15401.11}
\]

The endpoint logarithm is positive and locally integrable.  Every other term is
finite on the closed interval apart from the harmless endpoint convention.

## Jump form

Set

\[
\begin{aligned}
 \mathcal E_a(w)={}&
 \frac12\int_I\int_I
 K_a(|x-y|)|w(x)-w(y)|^2\,dx\,dy\\
 &+\sum_{n\le e^{2a}}c_n
 \int_{-1}^{1-\delta_n}|w(x+\delta_n)-w(x)|^2\,dx\\
 &+\int_I V_a(x)|w(x)|^2\,dx.
\end{aligned}
\tag{L-15401.12}
\]

The two nonlocal energies in (L-15401.12) have nonnegative kernels and weights.

## Polar channels

Define

\[
 C_a(w)=\int_I\cosh(ax/2)w(x)\,dx,
\qquad
 S_a(w)=\int_I\sinh(ax/2)w(x)\,dx.
\tag{L-15401.13}
\]

Then the complete scaled localized Weil form satisfies the exact identity

\[
\boxed{
 q_a(w)=\mathcal E_a(w)
       +2a|C_a(w)|^2
       -2a|S_a(w)|^2.}
\tag{L-15401.14}
\]

In particular, after the logarithmic and `r_1''` terms are combined, **no
signed smooth convolution remainder remains**.  The only non-Markov part is a
finite polar correction with one positive even and one negative odd rank-one
channel.

## Proof

### 1. Logarithmic jump plus `r_1''`

For `t=|x-y|>0`, equation (L-15401.4) gives

\[
 -a r_1''(at)=\frac1{2t}-K_a(t)=F_a(t).
\]

Using symmetry and taking the real part of the Hermitian quadratic value,

\[
\begin{aligned}
 &\frac14\int\!\!\int\frac{|w(x)-w(y)|^2}{|x-y|}
 -a\int\!\!\int r_1''(a(x-y))w(y)\overline{w(x)}\\
 &\quad=\frac12\int\!\!\int
 K_a(|x-y|)|w(x)-w(y)|^2
 +\int U_a(x)|w(x)|^2\,dx.
\end{aligned}
\tag{L-15401.15}
\]

One may verify (L-15401.15) first with a diagonal cutoff
`|x-y|>\varepsilon`.  Expanding the squared difference cancels the two cross
terms exactly.  The remaining diagonal coefficient is

\[
 \int_I\left(\frac1{2|x-y|}-K_a(|x-y|)\right)dy=U_a(x),
\]

whose integrand is continuous at the diagonal by (L-15401.7).  Dominated
convergence removes the cutoff.

This is the load-bearing cancellation.  Bounding `\mathcal L` and the
`r_1''` convolution separately destroys it.

### 2. Each prime translation

Fix `\delta=\delta_n` and write

\[
 I_\delta=(-1,1-\delta).
\]

The two source integrals are conjugates, so their sum is

\[
 2\operatorname{Re}\int_{I_\delta}
 w(x+\delta)\overline{w(x)}\,dx.
\]

The elementary identity

\[
\begin{aligned}
 -2\operatorname{Re}\int_{I_\delta}w(x+\delta)\overline{w(x)}\,dx
 ={}&\int_{I_\delta}|w(x+\delta)-w(x)|^2\,dx\\
 &-\int_I d_\delta(x)|w(x)|^2\,dx
\end{aligned}
\tag{L-15401.16}
\]

proves the prime part of (L-15401.12) and the last term of (L-15401.11).

### 3. Polar term

Differentiating (L-15401.3) twice gives

\[
 r_0''(t)=-(e^{t/2}+e^{-t/2}).
\]

Therefore

\[
\begin{aligned}
 &-a\int_I\int_I r_0''(a(x-y))w(y)\overline{w(x)}\,dx\,dy\\
 &\quad=a\left(A_-\overline{A_+}+A_+\overline{A_-}\right),
\end{aligned}
\]

where

\[
 A_\pm=\int_Ie^{\pm ax/2}w(x)\,dx=C_a(w)\pm S_a(w).
\]

Taking the real part yields

\[
 a\left(A_-\overline{A_+}+A_+\overline{A_-}\right)
 =2a\left(|C_a(w)|^2-|S_a(w)|^2\right).
\tag{L-15401.17}
\]

Combining (L-15401.15)–(L-15401.17) with the scalar and endpoint terms in
Suzuki's equation (4.5) proves (L-15401.14).  QED.

## Parity

The kernel `K_a`, the potential `V_a`, and every prime-shift energy commute with
reflection `w(x)\mapsto w(-x)`.  Moreover,

- `C_a(w)=0` for odd `w`;
- `S_a(w)=0` for even `w`.

Hence

\[
 q_a|_{\rm even}=\mathcal E_a|_{\rm even}+2a|C_a|^2,
\qquad
 q_a|_{\rm odd}=\mathcal E_a|_{\rm odd}-2a|S_a|^2.
\tag{L-15401.18}
\]

Only the odd polar channel can lower the Markov base.

## Form-closure use

The identity is proved on Suzuki's common core `H_0^1(-1,1)`.  Corollary 1.2
of the source identifies the localized ground value with the infimum over a
smooth compactly supported form core.  Consequently, any uniform lower bound
proved from the right side of (L-15401.14) on that core passes to the closed
localized form.  No assertion that every individual term has the same maximal
closed domain is required.

## Numerical algebra control

An independent midpoint quadrature at `a=1.3` and a smooth complex test function
checked

```text
logarithmic jump + r1 convolution
=
K_a jump + U_a potential
```

to approximately `2.2e-16`.  Separate prime-shift and polar-channel controls
agreed to machine precision.  These checks are not proof dependencies.

## Why this matters

PR #152 treated the smooth convolution by an absolute operator charge and the
prime terms by either an absolute sum or a frequency-symbol enclosure.  The
present identity exposes a different exact structure:

```text
complete infinite-dimensional Markov jump form
+ explicit scalar potential
+ one positive even rank-one channel
- one negative odd rank-one channel.
```

This makes nonlocal ground-state representations and Barta-type ambient lower
bounds available without selecting or exhausting a prolate complement basis.

## Gap audit

- Every constant and sign inherits Suzuki's exact normalization and must be
  independently reconstructed from the cited source.
- `F_a` and `U_a` must be evaluated as the cancellation-safe differences in
  (L-15401.6)–(L-15401.9); subtracting two large floating quantities near zero
  is unsafe.
- The polar term is **indefinite**.  Calling it positive is false.
- Dropping the positive even polar channel is safe for a lower bound, but
  dropping the negative odd channel is not.
- A positive jump kernel does not by itself prove the total potential is
  nonnegative.
- This lemma is an exact structural decomposition, not a proof of RH.
