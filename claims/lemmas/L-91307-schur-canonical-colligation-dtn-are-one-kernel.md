# L-91307 — Schur, de Branges, conservative-colligation, and Dirichlet-to-Neumann positivity are four realizations of one kernel

Claim ID: `L-91307`  
Status: **PROPOSED COMPLETE ABSTRACT EQUIVALENCE; SOURCE-SPECIFIC REALIZATION STILL REQUIRED**  
Created: 2026-08-12  
RH status: **unproved**

## 1. Horizontal Xi quotient and its Cayley impedance

Fix `a>0`. Put

\[
E_a(z)=\xi\!\left(\frac12+a-iz\right),
\qquad
E_a^\#(z)=\xi\!\left(\frac12-a-iz\right),
\]

and

\[
\Theta_a(z)=\frac{E_a^\#(z)}{E_a(z)}
=\frac{\xi(\frac12-a-iz)}
       {\xi(\frac12+a-iz)}.
\tag{L-91307.1}
\]

On the real axis the functional equation and Schwarz symmetry give

\[
|\Theta_a(x)|=1.
\tag{L-91307.2}
\]

Whenever `1+Theta_a(z) != 0`, define

\[
\ell_a(z)=\frac{1-\Theta_a(z)}{1+\Theta_a(z)}.
\tag{L-91307.3}
\]

In the right-half-plane coordinate used by the safe-Pick programme, this is the
same Cayley impedance as

\[
d_a(r)=\frac{M(r-a)}{M(r+a)},\qquad
M(r)=\frac{\xi(\frac12+r)}{\xi(\frac12)},
\qquad
\ell_a(r)=\frac{1-d_a(r)}{1+d_a(r)}.
\tag{L-91307.4}
\]

## 2. Exact Cayley congruence

Define the Schur and positive-real kernels

\[
K_a^\Theta(z,w)
=
\frac{1-\Theta_a(z)\overline{\Theta_a(w)}}
     {-i(z-\bar w)},
\tag{L-91307.5}
\]

\[
K_a^\ell(z,w)
=
\frac{\ell_a(z)+\overline{\ell_a(w)}}
     {-i(z-\bar w)}.
\tag{L-91307.6}
\]

Direct algebra gives

\[
1-\Theta_a(z)\overline{\Theta_a(w)}
=
\frac{
2\bigl(\ell_a(z)+\overline{\ell_a(w)}\bigr)
}{
(1+\ell_a(z))(1+\overline{\ell_a(w)})
}.
\tag{L-91307.7}
\]

Hence

\[
\boxed{
K_a^\Theta(z,w)
=
\frac{2}{1+\ell_a(z)}
K_a^\ell(z,w)
\frac{1}{1+\overline{\ell_a(w)}}.
}
\tag{L-91307.8}
\]

Every finite Schur Pick matrix is therefore positive if and only if the
corresponding positive-real matrix is positive.

## 3. Exact de Branges congruence

The de Branges kernel attached to `E_a` is

\[
K_a^E(z,w)
=
\frac{
E_a(z)\overline{E_a(w)}
-
E_a^\#(z)\overline{E_a^\#(w)}
}{
-2\pi i(z-\bar w)
}.
\tag{L-91307.9}
\]

Using `E_a^#=Theta_a E_a`,

\[
\boxed{
K_a^E(z,w)
=
\frac{E_a(z)\overline{E_a(w)}}{2\pi}
K_a^\Theta(z,w).
}
\tag{L-91307.10}
\]

Thus the Hermite–Biehler/de Branges positivity problem, the Schur-Pick problem,
and the positive-real impedance problem are the same finite matrix cone up to
diagonal congruence.

## 4. Canonical-system realization

Let

\[
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},
\qquad
J\partial_tY_a(t,z)=zH_a(t)Y_a(t,z),
\tag{L-91307.11}
\]

with `H_a(t)=H_a(t)^T >= 0` almost everywhere. The Lagrange identity is

\[
\frac{
Y_a(T,w)^*JY_a(T,z)-Y_a(0,w)^*JY_a(0,z)
}{
z-\bar w
}
=
\int_0^T
Y_a(t,w)^*H_a(t)Y_a(t,z)\,dt.
\tag{L-91307.12}
\]

For the standard de Branges boundary normalization, the left side is
`2*pi*K_a^E(z,w)`. Hence a positive Hamiltonian whose terminal structure
function is `E_a` gives

\[
K_a^E(z,w)
=
\left\langle
H_a^{1/2}Y_a(\cdot,w),
H_a^{1/2}Y_a(\cdot,z)
\right\rangle.
\tag{L-91307.13}
\]

This is route I.

## 5. Conservative-colligation realization

For a unitary colligation

\[
\mathbb U_a=
\begin{pmatrix}
A_a&B_a\\
C_a&D_a
\end{pmatrix}
:
\mathcal X_a\oplus\mathcal U
\longrightarrow
\mathcal X_a\oplus\mathcal Y,
\tag{L-91307.14}
\]

the disk transfer function

\[
S_a(\zeta)
=
D_a+\zeta C_a(I-\zeta A_a)^{-1}B_a
\tag{L-91307.15}
\]

satisfies the optical theorem

\[
\frac{
I-S_a(\zeta)S_a(\eta)^*
}{
1-\zeta\bar\eta
}
=
C_a(I-\zeta A_a)^{-1}
(I-\bar\eta A_a^*)^{-1}C_a^*.
\tag{L-91307.16}
\]

After the Cayley map between the disk and upper half-plane, a colligation with
scalar transfer `Theta_a` factors `K_a^Theta`. This is route II.

## 6. Dirichlet-to-Neumann realization

Let `H_a` be a positive self-adjoint bulk operator with a boundary triple
`(Gamma_0,Gamma_1)`. Its Weyl/Dirichlet-to-Neumann function `m_a(z)` obeys
Green's identity

\[
\frac{
m_a(z)-\overline{m_a(w)}
}{
z-\bar w
}
=
\left\langle
\gamma_a(w),\gamma_a(z)
\right\rangle_{\mathcal H_a},
\tag{L-91307.17}
\]

with `gamma_a(z)` the Poisson solution operator. In the right-half-plane
positive-real normalization this becomes a Gram factorization of `K_a^ell`. If
`m_a=ell_a`, (L-91307.8) gives the Schur kernel. This is route III.

## 7. Abstract equivalence and the non-circularity requirement

Standard realization theory gives the abstract equivalence

```text
positive Schur kernel
<=> positive-real Cayley kernel
<=> de Branges kernel
<=> positive canonical system
<=> conservative colligation
<=> positive DtN/Weyl realization.
```

For RH this abstract equivalence is not the proof: beginning by assuming the
target kernel positive is circular. The conclusion-producing theorem must
construct one of these realizations from the positive arithmetic, theta,
Brownian, and local `p=2` source data before the Xi kernel is known to be
positive.

The rest of the proposal supplies one common source-ordered construction target
whose three readings are precisely the three requested routes.
