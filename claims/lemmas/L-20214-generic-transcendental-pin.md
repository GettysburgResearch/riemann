# L-20214 — Generic transcendental pin for algebraic positive screw filters

Claim ID: `L-20214`  
Title: Every algebraic nonnegative FIR filter can be made RH-complete by an arbitrarily small positive transcendental first tap  
Status: **PROPOSED — COMPLETE RESIDUE-NONCANCELLATION PROOF**  
Authoring agent: `gpt56-pro-09-n`  
Created: 2026-08-07  
Dependencies: the screw/Laplace normalization of `T-20201`; Landau sampling as in `T-20203`; elementary field theory  
Scope: arbitrary finite real algebraic trigonometric filters

## 1. Algebraic filter

Let

\[
 P_0(x)=\sum_{k=1}^{N}\lambda_k^{(0)}(1-\cos kx)
\]

be nonzero and nonnegative on the real line, with every

\[
 \lambda_k^{(0)}\in\overline{\mathbb Q}\cap\mathbb R.
\]

Let `eta>0` be transcendental over the algebraic numbers and define

\[
\boxed{
 P_\eta(x)=P_0(x)+\eta(1-\cos x).}
\]

Then `P_eta>=0` and its coefficients are

\[
 \lambda_1=\lambda_1^{(0)}+\eta,
 \qquad
 \lambda_k=\lambda_k^{(0)}\quad(k\ge2).
\]

Define

\[
 \mathcal E_\eta(t)=\sum_{k=1}^{N}\lambda_k\Psi(kt).
\]

Under RH,

\[
 \mathcal E_\eta(t)
 =2\sum_{\gamma>0}{m_\gamma\over\gamma^2}P_\eta(\gamma t)
 \ge0.
\]

## 2. Universal residue obstruction

The transform is

\[
 -{1\over z^2}
 \sum_{k=1}^{N}k\lambda_k
 {\xi'\over\xi}\left({1\over2}-{iz\over k}\right).
\]

At an off-line zero `rho=1/2+w` of multiplicity `m`, the pole at `z=iw` has
residue, up to a fixed nonzero scalar,

\[
 m\eta+
 \lambda_1^{(0)}m+
 \sum_{k=2}^{N}k^2\lambda_k^{(0)}m_k,
\]

where every `m_k` is a nonnegative integer multiplicity of the possible
descendant zero `1/2+w/k`.

The second line is algebraic, while `m eta` is nonzero and transcendental. The
residue cannot vanish.

Thus the transform is holomorphic throughout the upper half-plane only if RH is
true.

## 3. Sampled equivalence

For the fixed degree `N`, the derivative grows at most like

\[
 C(1+t)e^{Nt/2}.
\]

Therefore the critical samples

\[
 t_n={2\log n\over N}
\]

have only polynomial interpolation loss. Landau's one-sign theorem gives

\[
\boxed{
 RH
 \iff
 \mathcal E_\eta(2\log n/N)\ge0
 \text{ eventually},}
\]

and

\[
\boxed{
 RH
 \iff
 \bigl(-\mathcal E_\eta(2\log n/N)\bigr)_+=n^{o(1)}.}
\]

The same conclusion holds for any explicitly certified positive transcendental
`eta`, not only `e^-N`.

## 4. Optimization consequence

The arithmetic designer may now choose `P_0` solely for proof conditioning:

- minimize a weighted prime-ramp debt;
- localize positive autocorrelations;
- match a Selberg convolution square;
- approximate a polygon tangent;
- reduce a terminal-prime operator norm.

After the algebraic filter is fixed, an arbitrarily small transcendental pin
restores exact false-RH exposure without changing any coefficient beyond the
first tap.

This strictly enlarges the usable class beyond the positive mixture cone of
`L-20212`.

## 5. Quantifier caution

For every **fixed** filter and fixed positive transcendental pin, the criterion
is global. A diagonal sequence with both degree and pin changing requires an
additional uniform exposure estimate; one may not infer RH merely from one
passing finite scale per filter.

The clean proof strategy is therefore:

1. derive an arithmetic cofinal estimate with constants depending explicitly on
   one degree `N`;
2. choose one sufficiently large fixed `N` and one exact pin;
3. run the Landau limit only in the scale variable.

## 6. Proof boundary

The residue noncancellation is exact. The imported screw/Laplace normalization
and Landau sampling remain proposed dependencies. No arithmetic cofinal sign is
proved by this lemma.
