# L-91308 — A lossless `p=2` port regularizes the Suzuki–de Branges construction without changing the open-strip Xi zeros

Claim ID: `L-91308`  
Status: **FULL CONSTRUCTIVE CANONICAL-SYSTEM PROGRAMME; ONE POSITIVE MARCHENKO IDENTITY OPEN**  
Created: 2026-08-12  
RH status: **unproved**

## 1. The exact local port

Let

\[
Q_*(y)=(1-y)(1-2y)(2-y)(1-4y)
      =2-15y+35y^2-30y^3+8y^4.
\tag{L-91308.1}
\]

The self-dual adelic wavelet of the parent programme has completed Tate scalar

\[
\Xi_*(s)=2^{2s}Q_*(2^{-s})\xi(s).
\tag{L-91308.2}
\]

Its local factor is

\[
\boxed{
2^{2s}Q_*(2^{-s})
=
16A_2(s)A_2(1-s),
\qquad
A_2(s)=(1-2^{-s})(1-2^{-s-1}).
}
\tag{L-91308.3}
\]

Neither `A_2(s)` nor `A_2(1-s)` vanishes in `0<Re(s)<1`. Thus

\[
\Xi_*(s)=0,\quad 0<\Re s<1
\iff
\xi(s)=0.
\tag{L-91308.4}
\]

The local factor is not to be ignored: it has known zeros outside the open
critical strip. It must be represented as a finite lossless boundary port and
Schur-eliminated before the reduced characteristic determinant is interpreted.

## 2. Stable radial synthesis

The radial `p=2` shell space is identified with `ell^2(Z)`. The dyadic dilates
of the local wavelet have synthesis symbol

\[
G(z)=2\sqrt2-13z+11\sqrt2 z^2-4z^3.
\tag{L-91308.5}
\]

The phase-lock theorem gives

\[
\inf_{|z|=1}|G(z)|>0.
\tag{L-91308.6}
\]

Hence the local synthesis map is boundedly invertible: there is no hidden local
kernel, missing radial state, or conditioning escape.

## 3. Regularized multiplicative Hankel operator

Let `H_a` denote Suzuki's multiplicative Hankel operator formally associated
with `Theta_a`. Let `R_2` be the finite Laurent polynomial in the dyadic
dilation induced by `Q_*`. Define the regularized operator

\[
\mathsf H_{a,*}
=
\mathsf R_2\,\mathsf H_a\,\mathsf R_2^\sharp.
\tag{L-91308.7}
\]

On the Mellin boundary its multiplier is the original `Theta_a` multiplied
by the explicit finite local all-pass ratio arising from (L-91308.3). The
period-16 packet has four vanishing moments; after the pole/gamma subtraction
already present in the completed kernel, the proposed operator `H_(a,*)` has
trace-class compact truncations

\[
\mathsf K_{a,x}
=
P_x\mathsf H_{a,*}P_x.
\tag{L-91308.8}
\]

The analytic task here is a direct kernel estimate from the explicit
theta-wavelet formula, not a zero-side assumption.

## 4. Suzuki–Marchenko tau functions

For `x>0`, define

\[
\tau_{a,\pm}(x)=\det(I\pm\mathsf K_{a,x}).
\tag{L-91308.9}
\]

When both determinants are nonzero, the standard Burnol–Suzuki Marchenko
construction forms a positive diagonal Hamiltonian, up to the normalization of
the canonical coordinate, from the determinant ratio

\[
m_a(x)=\frac{\tau_{a,+}(x)}{\tau_{a,-}(x)},
\qquad
H_a(x)=
\begin{pmatrix}
m_a(x)^{-2}&0\\
0&m_a(x)^2
\end{pmatrix}.
\tag{L-91308.10}
\]

The exact normalization is to be matched against Suzuki's canonical-system
convention before promotion. Positivity of (L-91308.10) is automatic once the
tau functions are real and nonzero.

## 5. The canonical-route closing identity

The source-specific theorem to prove is:

> **Regularized Marchenko Identity (`RMI_a`).**  
> For every rational `0<a<1/2`, the trace-class operators
> `K_(a,x)` satisfy
> \[
> \tau_{a,+}(x)\tau_{a,-}(x)>0\qquad(x>0),
> \]
> and the canonical system obtained from (L-91308.10), after exact Schur
> elimination of the finite `p=2` port, has terminal structure function
> \[
> E_a(z)=\xi\!\left(\frac12+a-iz\right)
> \]
> up to a real zero-free scalar factor.

This is not a restatement of innerness if it is proved from the explicit
theta-wavelet kernel and Fredholm resolvent equations. It is circular if
nonvanishing of the tau functions is inferred from assumed innerness.

## 6. Why `RMI_a` finishes route I

`RMI_a` yields `H_a(x)>=0` and recovers `E_a`. The de Branges Lagrange
identity then gives `K_a^E>=0`, hence `K_a^Theta>=0` by `L-91307`.
Therefore `Theta_a` is meromorphic inner.

For any predetermined `a_j -> 0`, innerness for every `a_j` excludes
all zeros to the right of the critical line. Functional symmetry then gives RH.

## 7. What remains to be established on this route

1. Trace-class bounds for `K_(a,x)` from the explicit regularized theta kernel.
2. A source-side proof that `I+/-K_(a,x)` are injective for every `x`, without
   assuming innerness.
3. Exact matching of the recovered terminal structure function after local
   port elimination.

These three steps are the canonical-system reading of the single optical
theorem stated in `T-91302`.
