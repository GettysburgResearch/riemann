# R-15102 — Cardinal truncation obstructs automatic cofinal Finsler completion

Claim ID: `R-15102`  
Status: **PROVED EXACT OBSTRUCTION**  
Authoring agent: `gpt56-04-f`  
Created: 2026-07-31  
Dependencies: elementary alternating-series algebra; the Mittag--Leffler expansion of `pi csc(pi z)`; `L-15108` for the special-completion interpretation  
Scope: finite Fourier/cardinal truncations and the logical gap between local-uniform convergence and eventual finite real-rootedness  
Related counterexample candidates: none

## 1. Purpose

The cofinal target-pinned program asks for finite transforms with only real zeros
that converge locally uniformly to `Xi`. It is tempting to infer eventual finite
real-rootedness from increasingly accurate approximation of the limiting entire
function.

That inference is false, even when the limit is the nonzero constant function.
The obstruction below is exact and persists at every finite cardinal level.

It does not refute every possible repaired-Hermite target sequence. It proves
that local-uniform convergence, target-tail decay, and coefficient convergence
alone cannot establish the cofinal Finsler/Bézoutian inequality. A separate
arithmetic or root-separation theorem is indispensable.

## 2. Exact cardinal family

Fix an integer `N>=1`. Put

\[
 D_N(z)=\prod_{m=-N}^{N}(z-m)
 \tag{R-15102.1}
\]

and

\[
 R_N(z)=\sum_{n=-N}^{N}\frac{(-1)^n}{z-n}.
 \tag{R-15102.2}
\]

The poles are canceled by

\[
 \boxed{
 P_N(z)=D_N(z)R_N(z)
 =\sum_{n=-N}^{N}(-1)^n\frac{D_N(z)}{z-n}.}
 \tag{R-15102.3}
\]

Thus `P_N` is a real polynomial of degree `2N`.

The corresponding entire cardinal transform is

\[
 \boxed{
 F_N(z)=\sin(\pi z)R_N(z).}
 \tag{R-15102.4}
\]

Its zeros away from the integer lattice are exactly the zeros of `P_N`; the
remaining uncanceled sine zeros are real.

## 3. No finite numerator has a real zero

For every `N>=1`,

\[
 \boxed{P_N(x)\ne0\qquad(x\in\mathbb R).}
 \tag{R-15102.5}
\]

Consequently all `2N` roots of `P_N` are nonreal.

### Proof between consecutive nodes

Take

\[
 x=k+a,
 \qquad -N\le k\le N-1,
 \qquad 0<a<1.
\]

Split (R-15102.2) at the two neighboring poles. A direct reindexing gives

\[
 \boxed{
 (-1)^kR_N(k+a)
 =\sum_{j=0}^{k+N}\frac{(-1)^j}{a+j}
  +\sum_{j=0}^{N-k-1}\frac{(-1)^j}{1-a+j}.}
 \tag{R-15102.6}
\]

For every `b>0` and every integer `M>=0`, define

\[
 S_M(b)=\sum_{j=0}^{M}\frac{(-1)^j}{b+j}.
\]

Every finite alternating sum is strictly positive. Indeed,

\[
 S_{2r+1}(b)
 =\sum_{q=0}^{r}
 \left(\frac1{b+2q}-\frac1{b+2q+1}\right)>0,
\]

and

\[
 S_{2r}(b)=S_{2r-1}(b)+\frac1{b+2r}>0.
\]

Both sums on the right of (R-15102.6) are therefore positive. Hence

\[
 (-1)^kR_N(x)>0
\]

throughout every open interval `(k,k+1)`, and `R_N` has no zero there.

### Outside the node interval

For `x=N+a`, `a>0`,

\[
 (-1)^NR_N(N+a)
 =\sum_{j=0}^{2N}\frac{(-1)^j}{a+j}>0.
 \tag{R-15102.7}
\]

The family is odd,

\[
 R_N(-x)=-R_N(x),
\]

so there is no zero on `(-infinity,-N)` either.

### At the nodes

At an integer node `n`, the removable numerator value is

\[
 P_N(n)=(-1)^nD_N'(n)\ne0.
 \tag{R-15102.8}
\]

This proves (R-15102.5). QED.

## 4. The entire transforms converge to a zero-free limit

The classical Mittag--Leffler expansion is

\[
 \frac{\pi}{\sin(\pi z)}
 =\sum_{n\in\mathbb Z}\frac{(-1)^n}{z-n},
 \tag{R-15102.9}
\]

with symmetric summation, equivalently

\[
 \frac{\pi}{\sin(\pi z)}
 =\frac1z+
  \sum_{n=1}^{\infty}
  (-1)^n\frac{2z}{z^2-n^2}.
 \tag{R-15102.10}
\]

The paired series converges normally on compact sets away from the integer
lattice. Multiplication by `sin(pi z)` removes all singularities, and the
resulting convergence extends locally uniformly across the lattice. Therefore

\[
 \boxed{F_N(z)\longrightarrow\pi}
 \tag{R-15102.11}
\]

locally uniformly on `C`.

The limit has no zeros. Nevertheless every finite `F_N` has `2N` nonreal zeros,
namely the roots of `P_N`.

Thus:

\[
 \boxed{
 \text{local-uniform convergence to a zero-free entire function}
 \not\Rightarrow
 \text{eventual real-rootedness of the finite cardinal transforms}.}
 \tag{R-15102.12}
\]

## 5. Consequence for special-matrix completion

Use the equally spaced nodes `-N,...,N` and target residues

\[
 p_n=(-1)^n.
\]

The associated interpolation polynomial is `P_N`, up to a fixed nonzero
orientation factor. Since `P_N` has no real roots, `L-15108` implies that no
positive special matrix with one-dimensional kernel `Rp` exists. In particular,
no target-pinned scalar completion can satisfy

\[
 T_p(c)\succeq0,
 \qquad
 \ker T_p(c)=\mathbb Rp.
 \tag{R-15102.13}
\]

Equivalently, the Finsler isotropic-cone condition and the simple-root threshold
separation both fail at every level of this family.

This is a finite exact obstruction, not a conditioning or floating-point effect.

## 6. Fixed-band perturbative corollary

Fix `N`. Let `a_n(L)` be real amplitudes satisfying

\[
 a_n(L)\longrightarrow a_*>0
 \qquad(|n|\le N)
 \tag{R-15102.14}
\]

and set

\[
 p_n(L)=(-1)^na_n(L).
\]

The coefficients of the associated interpolation polynomial converge to those
of `a_*P_N`. Polynomial roots depend continuously on the coefficients. Because
`P_N` has finitely many roots and none is real, there is an `L_N` such that the
perturbed polynomial also has no real root for every `L>=L_N`.

Therefore any repaired target diagonal with fixed Fourier band and coefficients
approaching a nonzero constant profile fails finite real-rootedness eventually.
The same applies whenever the coefficient vector remains in a sufficiently
small neighborhood of the alternating cardinal vector.

This corollary is directly relevant near the center of an expanding support:
for a smooth even target transform `H` with `H(0)!=0`, fixed-index Fourier
coefficients sample `H` at frequencies tending to zero and hence approach a
constant amplitude profile. Merely sending the support to infinity while
keeping a fixed or undersampled band cannot establish the desired completion.

## 7. What a viable cofinal diagonal must do

The obstruction shows that a successful diagonal must simultaneously:

1. increase the finite band fast enough to leave the cardinal constant-profile
   regime;
2. control the spurious numerator roots globally, not only on fixed compact
   subsets;
3. prove a genuinely arithmetic sign or metric separation, since target-tail
   convergence alone permits nonreal roots to approach the real axis or escape
   along the expanding cardinal scale.

The mode-8 prolate gap and the Hermite radical tail estimates address target and
local-complement scales. They do not, by themselves, control these global
cardinal roots.

## 8. Gap audit

- The theorem does not assert that every growing-band repaired-Hermite sequence
  fails. It refutes the automatic implication from convergence and the complete
  fixed-band regime.
- The exact family converges to a constant, not to `Xi`; its role is logical and
  structural.
- A future successful proof may use a different finite approximation family or
  an arithmetic completion theorem strong enough to eliminate cardinal roots.
- No numerical root finder enters the proof.