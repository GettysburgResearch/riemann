# L-20304 — Möbius-tail support retreat and the evaluation uncertainty principle

Claim ID: `L-20304`  
Title: Moving an exact local-inverse residual farther below the support forces its Hardy norm to grow unless every relevant zero evaluation is already small  
Status: `PROPOSED — COMPLETE WEIGHTED CAUCHY–SCHWARZ PROOF`  
Authoring agent: `gpt56-03-p`  
Created: 2026-08-01  
Dependencies: `L-20301`; the reciprocal Hardy metric and evaluation convention used in `L-15304/L-14320`  
Scope: cutoff scheduling for the explicit complete-kernel Möbius tail  
Related counterexample candidates: none

## 1. Retreating exact local inverse

Let \(h\) be supported in \([a,b]\), with \(0<a<b\), and put

\[
g(u)=u^{-1/2}h(u).
\]

Choose an integer \(M\) satisfying

\[
Ma>b.
\tag{L-20304.1}
\]

Use the complete Möbius prefix

\[
c_n=\mu(n)\qquad(1\le n\le M)
\tag{L-20304.2}
\]

in `L-20301`. Define

\[
\rho_M=\frac{b}{M+1}<a.
\tag{L-20304.3}
\]

Choose the source-integral corrector \(\psi_M\) with

\[
\operatorname{supp}\psi_M\subset(0,\rho_M),
\qquad
\int\psi_M=1.
\tag{L-20304.4}
\]

Let

\[
r_M=E(f_{M,h}),
\qquad
t_M=r_M-h.
\tag{L-20304.5}
\]

Then the exact reconstruction of `L-20301` holds on \([a,b]\), and the complete
residual obeys

\[
\boxed{
\operatorname{supp}t_M\subset(0,\rho_M).
}
\tag{L-20304.6}
\]

Indeed every physical divisor term has \(k>M\), hence is supported at
\(u\le b/k\le b/(M+1)\), and the correction has the same support bound.

## 2. Weighted lower-tail norm

For \(0<\tau<1/2\), write

\[
\|q\|_{-,\tau}^2
=
\int_0^1|q(u)|^2u^{-2\tau}\,d^*u.
\tag{L-20304.7}
\]

This is one positive component of the complete reciprocal Hardy metric

\[
\|q\|_\tau^2
=
\int_0^\infty|q(u)|^2
\left(u^{2\tau}+u^{-2\tau}\right)d^*u.
\tag{L-20304.8}
\]

Therefore

\[
\|q\|_\tau\ge\|q\|_{-,\tau}.
\tag{L-20304.9}
\]

## 3. Evaluation on a retreating lower tail

Let

\[
z=x+iy,
\qquad
|y|<\tau.
\tag{L-20304.10}
\]

If \(q\) is supported in \((0,\rho]\), Cauchy–Schwarz gives

\[
\begin{aligned}
|\widehat q(z)|
&=
\left|
\int_0^\rho q(u)u^{-iz}\,d^*u
\right|\\
&\le
\left(
\int_0^\rho|q(u)|^2u^{-2\tau}\,d^*u
\right)^{1/2}
\left(
\int_0^\rho u^{2(\tau+y)}\,d^*u
\right)^{1/2}\\
&=
\frac{\rho^{\tau+y}}
{\sqrt{2(\tau+y)}}
\|q\|_{-,\tau}.
\end{aligned}
\tag{L-20304.11}
\]

Hence

\[
\boxed{
\|q\|_\tau
\ge
\sqrt{2(\tau+y)}\,
\rho^{-(\tau+y)}
|\widehat q(z)|.
}
\tag{L-20304.12}
\]

For a real critical-line ordinate \(z=\gamma\), this becomes

\[
\boxed{
\|q\|_\tau
\ge
\sqrt{2\tau}\,\rho^{-\tau}
|\widehat q(\gamma)|.
}
\tag{L-20304.13}
\]

## 4. Exact Möbius-tail lower bound

At every nontrivial zeta zero parameter \(z_\rho\), `L-20301` gives

\[
\widehat t_M(z_\rho)=-\widehat h(z_\rho).
\tag{L-20304.14}
\]

Combining (L-20304.6) and (L-20304.12) yields

\[
\boxed{
\|t_M\|_\tau
\ge
\sqrt{2(\tau+\operatorname{Im}z_\rho)}
\left(\frac{M+1}{b}\right)^{
\tau+\operatorname{Im}z_\rho}
|\widehat h(z_\rho)|.
}
\tag{L-20304.15}
\]

For a critical-line zero,

\[
\boxed{
\|t_M\|_\tau
\ge
\sqrt{2\tau}
\left(\frac{M+1}{b}\right)^\tau
|\widehat h(\gamma)|.
}
\tag{L-20304.16}
\]

Thus increasing the exact Möbius prefix pushes the residual farther into the
lower tail but imposes a polynomial Hardy cost on every nonzero zero
evaluation.

## 5. Packet form

Let \(J:\mathbb C^d\to K\) be a finite complete-kernel basis. At a zero
parameter \(z\), define the evaluation row

\[
v_zc=\widehat{Jc}(z).
\tag{L-20304.17}
\]

The tail synthesis \(T_M\) satisfies the operator inequality

\[
\boxed{
T_M^*G_\tau T_M
\succeq
2(\tau+\operatorname{Im}z)
\left(\frac{M+1}{b}\right)^{2(\tau+\operatorname{Im}z)}
v_z^*v_z.
}
\tag{L-20304.18}
\]

For any finite positive weighted set of critical-line zeros one may sum the
corresponding inequalities after inserting a valid Bessel/frame normalization.
A raw sum without controlling overlap of the evaluation functionals is not
licensed.

## 6. Optimal-cutoff implication

The exact local inversion requirement is only

\[
M>b/a.
\tag{L-20304.19}
\]

Equation (L-20304.16) shows that taking \(M\) much larger than this minimum can
make the Hardy realization strictly worse. A valid scheduler must balance:

- physical divisor-tail cancellation;
- source-integral correction size;
- Hardy support-retreat amplification;
- the Schur cross metric;
- packet zero-evaluation size.

The cutoff is therefore an optimization variable, not a monotone precision
parameter.

## 7. False-RH and near-radical alternatives

If a complete hierarchy captures an off-line cardinal direction, one zero
evaluation remains bounded away from zero. Then (L-20304.15) rules out every
vanishing Hardy-tail estimate and in fact forces growth when the cutoff
retreats.

For a genuine near-radical packet, the evaluation row may be
superexponentially small. A sufficient compatibility condition is

\[
\boxed{
\left(\frac{M_j+1}{b_j}\right)^{
\tau_j+\operatorname{Im}z}
\|v_{z,j}G_j^{-1/2}\|
\longrightarrow0
}
\tag{L-20304.20}
\]

for the zero evaluations entering the proof metric. This condition is
necessary for the corresponding Hardy tail to vanish, but not sufficient for
the complete Weil-form/Schur estimate.

## 8. Proof boundary

- The support retreat and weighted evaluation inequality are exact.
- The theorem gives lower bounds, not an upper tail estimate.
- It prevents the unsupported claim that larger Möbius cutoffs automatically
  improve the proof norm.
- The complete cofinal upper bound remains open.
- No proof of RH is claimed.
