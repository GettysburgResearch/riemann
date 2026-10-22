# L-19870 — The optimal positive symmetrizer defect is exactly the nonreal spectral radius

Claim ID: `L-19870`  
Status: **PROVED FINITE-DIMENSIONAL THEOREM / SCOPE FIREWALL**  
Authoring agent: `gpt56-pro-09-p`  
Created: 2026-08-12  
Dependencies: elementary finite-dimensional spectral theory; companion operator of `L-19869`  
Scope: distinguishes a source-bound positive symmetrizer from unrestricted metric optimization  
Nonclaim: no Riemann-data symmetrizer is constructed and RH is not proved

## 1. Statement

Let `T` be a complex linear operator on a finite-dimensional vector space `V`.
For every positive definite Hermitian matrix `H`, define

\[
 \varepsilon_H(T)
 :=\frac12\left\|
 H^{-1/2}(HT-T^*H)H^{-1/2}
 \right\|_{\rm op}.
 \tag{L-19870.1}
\]

Then

\[
 \boxed{
 \inf_{H\succ0}\varepsilon_H(T)
 =\max_{z\in\operatorname{Spec}(T)}|\operatorname{Im}z|.
 }
 \tag{L-19870.2}
\]

If `T` is diagonalizable, the infimum is attained.  If `T` has a nontrivial
Jordan block, the same value is the infimum, although it need not be attained.

Applied to the induced CCM companion operator on
`E_N/\mathbb C\xi`, the right side is exactly the largest imaginary part of a
nonuniversal zero of the finite Fourier transform of `xi`.

Consequently, merely allowing an arbitrary positive metric cannot turn the
symmetrizer method into an independent proof mechanism.  The metric in
`L-19869` must be constructed from source-bound arithmetic/residual data before
its defect is estimated.

## 2. Universal lower bound

Let `Tv=zv`, `v\ne0`.  Then

\[
\begin{aligned}
 v^*(HT-T^*H)v
 &=z\,v^*Hv-\overline z\,v^*Hv\\
 &=2i\,\operatorname{Im}(z)\,v^*Hv.
\end{aligned}
 \tag{L-19870.3}
\]

Put `u=H^{1/2}v`.  Dividing (L-19870.3) by `v^*Hv=\|u\|^2` gives

\[
 \left\|
 H^{-1/2}(HT-T^*H)H^{-1/2}
 \right\|_{\rm op}
 \ge 2|\operatorname{Im}z|.
 \tag{L-19870.4}
\]

Taking the maximum over the spectrum and then the infimum over `H` proves

\[
 \inf_{H\succ0}\varepsilon_H(T)
 \ge\max_{z\in\operatorname{Spec}(T)}|\operatorname{Im}z|.
 \tag{L-19870.5}
\]

## 3. Attainment in the diagonalizable case

Assume

\[
 T=VZV^{-1},
 \qquad Z=\operatorname{diag}(z_1,\ldots,z_d).
 \tag{L-19870.6}
\]

Choose

\[
 H=(V^{-1})^*V^{-1}.
 \tag{L-19870.7}
\]

Then `V^*HV=I`; equivalently, the columns of `V` are orthonormal in the
`H`-inner product.  The matrix

\[
 U=H^{1/2}V
 \tag{L-19870.8}
\]

is unitary, and

\[
 H^{1/2}TH^{-1/2}=UZU^*.
 \tag{L-19870.9}
\]

Therefore

\[
\begin{aligned}
&H^{-1/2}(HT-T^*H)H^{-1/2}\\
&\qquad=H^{1/2}TH^{-1/2}
 -(H^{1/2}TH^{-1/2})^*\\
&\qquad=U(Z-Z^*)U^*.
\end{aligned}
 \tag{L-19870.10}
\]

Its operator norm is

\[
 2\max_j|\operatorname{Im}z_j|.
 \tag{L-19870.11}
\]

This proves equality and attainment in (L-19870.2).

## 4. Jordan blocks

Write

\[
 T=VJV^{-1},
 \qquad
 J=\bigoplus_\nu(z_\nu I+N_\nu),
 \tag{L-19870.12}
\]

where every `N_nu` is a standard nilpotent Jordan block.  For `R>1`, let

\[
 S_{\nu,R}
 =\operatorname{diag}(1,R^{-1},R^{-2},\ldots)
 \tag{L-19870.13}
\]

on that block.  Then

\[
 S_{\nu,R}^{-1}N_\nu S_{\nu,R}=R^{-1}N_\nu.
 \tag{L-19870.14}
\]

With `S_R` the block direct sum and `V_R=VS_R`, choose

\[
 H_R=(V_R^{-1})^*V_R^{-1}.
 \tag{L-19870.15}
\]

In the `H_R`-metric the operator is represented by

\[
 S_R^{-1}JS_R
 =\bigoplus_\nu(z_\nu I+R^{-1}N_\nu).
 \tag{L-19870.16}
\]

Hence

\[
 \varepsilon_{H_R}(T)
 \le
 \max_\nu|\operatorname{Im}z_\nu|+O(R^{-1}).
 \tag{L-19870.17}
\]

Letting `R\to\infty` and combining with (L-19870.5) proves (L-19870.2) in
general.

## 5. CCM consequence

Let `xi` be normalized by `eta^*xi=1`, let `T_xi` be the CCM companion, and
let `bar T_xi` be the induced operator on `E_N/\mathbb Cxi`.  By the determinant
identity, its spectrum is the set of nonuniversal zeros of `hat xi`, counted
with algebraic multiplicity.  Therefore

\[
 \boxed{
 \inf_{H\succ0}\varepsilon_H(\bar T_\xi)
 =\max_{\widehat\xi(z)=0}^{\rm nonuniversal}
   |\operatorname{Im}z|.
 }
 \tag{L-19870.18}
\]

Thus the following two statements are equivalent for a sequence of finite
vectors:

```text
there exist unrestricted positive metrics with defect -> 0;
all nonuniversal finite transform zeros enter a shrinking real strip.
```

Together with locally uniform convergence to `Xi`, either statement already
implies RH by Hurwitz.  It is not a cheaper substitute for the missing
arithmetic theorem.

## 6. Exact proof boundary

- The theorem is unconditional finite-dimensional linear algebra.
- It strengthens the one-sided zero bound in `L-19869` by optimizing over all
  possible positive metrics.
- It does not evaluate the defect of the fixed source-bound residual metric from
  `L-19867`.
- The only non-tautological route is therefore to prove small defect for one
  independently prescribed arithmetic metric before inspecting the zeros.
