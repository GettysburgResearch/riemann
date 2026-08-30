# L-104602 — Reconstructed Conrey variational functional

Claim ID: `L-104602`  
Status: **RECONSTRUCTED PUBLISHED UNCONDITIONAL THEOREM**  
Created: 2026-08-26  
Primary source: J. B. Conrey, *Zeros of derivatives of Riemann's xi-function on the critical line*, JNT 16 (1983), 49--74  
Repository source: PR #742, `experiments/X-105075-quantitative-converse-rolle/conrey_I_full.txt`  
RH status: **not assumed**

## 1. Admissible data

Fix an integer `m>=0`, `R>0`, and a real `C^1` function
`phi:[0,1]->R` satisfying

\[
\phi(0)=1,
\qquad
\phi'(x)=\phi'(1-x).
\tag{L-104602.1}
\]

Put

\[
q_m(x)=\phi(x)(1-2x)^m,
\tag{L-104602.2}
\]

\[
\Phi_m(R,\phi)=\int_0^1 e^{2Rx}q_m(x)^2\,dx,
\tag{L-104602.3}
\]

and

\[
\Psi_m(R,\phi)=\int_0^1 e^{2Rx}q_m'(x)^2\,dx.
\tag{L-104602.4}
\]

Define

\[
A_m(R,\phi)^2
=
\frac{
\Psi_m+R\bigl(e^{2R}\phi(1)^2-1\bigr)-R^2\Phi_m
}{4\Phi_m}.
\tag{L-104602.5}
\]

For the certificates below this quantity is strictly positive. Finally set

\[
\boxed{
\mathcal F_m(R,\phi)
=2\Phi_m A_m\coth A_m
+\frac{e^{2R}\phi(1)^2+1}{2}.
}
\tag{L-104602.6}
\]

## 2. The published implication

Let `alpha_m` be Conrey's short-window lower critical-line proportion for zeros
of `xi^(m)`. His argument gives

\[
\boxed{
\alpha_m>1-\frac{\log\mathcal F_m(R,\phi)}{R}.
}
\tag{L-104602.7}
\]

The statement is unconditional.

## 3. Reconstruction of the functional

The primary proof has five conclusion-facing stages.

1. Write the completed derivative as a reflected pair
   \[
   \xi^{(m)}(s)=Q_m(s)+(-1)^mQ_m(1-s)
   \]
   with the gamma carrier kept inside `Q_m`.

2. Apply the argument principle/Littlewood lemma to the mollified reflected
   combination on the short rectangle.

3. Expand the mean square by the approximate functional equation. The
   derivative polynomial is exactly `q_m=phi(1-2x)^m`; the symmetry in
   (L-104602.1) is what matches the reflected endpoints.

4. After partial summation, the entire polynomial dependence reduces to the two
   weighted quadratic forms `Phi_m` and `Psi_m`, together with the displayed
   endpoint term.

5. Optimize the remaining one-dimensional mollifier energy. The Euler--Lagrange
   minimizer is the hyperbolic-sine profile
   \[
   \mu_A(x)=\frac{\sinh(Ax)}{\sinh A}.
   \]
   Its minimum is `A coth A`, yielding (L-104602.5--6).

The replay in `X-104620` independently checks every finite algebraic and
transcendental inequality used by the explicit certificates. It does not
replace Conrey's classical approximate-functional-equation and off-diagonal
error estimates; those are reconstructed from, and locked to, the primary
source.

## 4. Useful rational ansatz

A convenient admissible polynomial family is

\[
\phi(x)=1-x+\sum_{j=1}^{d}a_jx(1-x)(1-2x)^{2j-1}.
\tag{L-104602.8}
\]

Indeed every added summand is antisymmetric about `x=1/2`, so its derivative is
symmetric, and every such `phi` satisfies `phi(0)=1` and `phi(1)=0`.

For rational `R,a_j`, the integrals are finite combinations of `e^(2R)` with
rational coefficients. Consequently every candidate can be certified by
rational interval arithmetic.
