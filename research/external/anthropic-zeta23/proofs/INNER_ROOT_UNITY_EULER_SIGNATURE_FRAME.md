# Common-pole-killed inner root-of-unity Euler signature frame

Status: **PROPOSED COMPLETE EXACT SOURCE/SPECTRAL THEOREM — independent review required**  
Date: 2026-08-10  
Dependencies: PR #325 Q4 Euler–Blaschke scattering and balanced reserve; PR #363 reflected-pair spectrum  
RH status: **unproved**

## 1. Q4 inner factors and the load-bearing common factor

Put

\[
a=\frac12,\qquad L=\log4,
\]

and work in centered coordinates \(s=\tfrac12+z\). For \(|\omega|=1\), define

\[
\boxed{
\phi_\omega(z)
={a-\omega e^{-Lz}\over1-a\omega e^{-Lz}}.
}
\tag{IRU.1}

Then

\[
|\phi_\omega(it)|=1,
\qquad
\phi_\omega(-\overline z)
={1\over\overline{\phi_\omega(z)}},
\tag{IRU.2}

and \(|\phi_\omega(z)|<1\) for \(\Re z>0\).

A rotated phase factor does **not** by itself vanish at the zeta main pole.
Therefore every channel must retain one common pole-killing Q4 factor. Define

\[
\boxed{
\Psi_{\omega,k}(z)
=\phi_1(z)\phi_\omega(z)^k,
\qquad k\ge1.
}
\tag{IRU.3}

At \(s=1\), equivalently \(z=1/2\), one has \(e^{-Lz}=a\), so

\[
\boxed{\phi_1(1/2)=0.}
\tag{IRU.4}

Hence every \(\Psi_{\omega,k}\) kills the deterministic main pole.

Let \(\Omega_{M,\eta}=e^{i\eta}\Omega_M\). Since both factors are all-pass,

\[
\boxed{
{1\over M}\sum_{\omega\in\Omega_{M,\eta}}
|\Psi_{\omega,k}(it)|^2=1
}
\tag{IRU.5}

for every \(k,M,\eta\). The frame normalization is independent of the power.

## 2. Exact reflected-pair block

Let \(z\) be a right-half-plane zero coordinate. Put

\[
c=|\phi_1(z)|,
\qquad
r_\omega=|\phi_\omega(z)|.
\]

For normalized channel evaluation vectors, reflection gives

\[
A_k=c^2{1\over M}\sum_\omega r_\omega^{2k},
\qquad
B_k=c^{-2}{1\over M}\sum_\omega r_\omega^{-2k},
\tag{IRU.6}

and the reflected cross is exactly

\[
\boxed{\langle u,v\rangle=1.}
\tag{IRU.7}

The common factor cancels from \(A_kB_k\). A reflected pair of multiplicity
\(m\) therefore has exactly two nonzero eigenvalues

\[
\boxed{
\lambda_\pm=m(1\pm\sqrt{A_kB_k}).
}
\tag{IRU.8}

## 3. Generic strictness and exponential depth

Write \(t=e^{-Lz}=Re^{i\psi}\), with \(0<R<1\). Then

\[
|\phi_\omega(z)|^2
={a^2+R^2-2aR\cos(\arg\omega+\psi)
 \over
 1+a^2R^2-2aR\cos(\arg\omega+\psi)}.
\tag{IRU.9}

This ratio is strictly decreasing in the displayed cosine because

\[
(a^2+R^2)-(1+a^2R^2)
=-(1-a^2)(1-R^2)<0.
\]

For every \(M\ge2\), all but finitely many rotations \(\eta\) therefore give

\[
0<r_{\min}<r_{\max}<1.
\tag{IRU.10}

For such a rotation,

\[
\boxed{
\sqrt{A_kB_k}
\ge{1\over M}
 \left({r_{\max}\over r_{\min}}\right)^k.
}
\tag{IRU.11}

Thus

\[
\boxed{
-\lambda_-
\ge m\left[
 {1\over M}(r_{\max}/r_{\min})^k-1
\right],
}
\tag{IRU.12}

which is exponentially large for every fixed off-line zero.

A single scalar inner power remains exactly reflected-\(J\)-unitary. The gain
in (IRU.12) is created by the phase-resolved bank, not by scalar repetition.

## 4. Every channel has a main-pole-free Dirichlet system

Define

\[
\boxed{
B_{\omega,k}(s)
={\Psi_{\omega,k}(s-1/2)\over\zeta(s)},
\qquad
A_{\omega,k}=B_{\omega,k}^{-1}.
}
\tag{IRU.13}

Let

\[
D_\omega
=L\sum_{r\ge1}\omega^r(4^r-1)\delta_{4^r}.
\tag{IRU.14}

The generalized-prime sequence is

\[
\boxed{
\Lambda_{\omega,k}
=\Lambda+D_1+kD_\omega.
}
\tag{IRU.15}

The common part

\[
\Lambda_1=\Lambda+D_1
\]

is precisely the Q4 main-pole-killing system whose complete balanced
Selberg–Kummer reserve is proved on PR #325.

Fix a carry endpoint \(n\), let \(R_0=\lfloor\log_4n\rfloor\), and choose

\[
\boxed{M>2R_0.}
\tag{IRU.16}

For a carry row \(e=(n,j)\), put

\[
P_1(e)=\mathcal L_e(\Lambda_1),
\qquad
d_r(e)=kL(4^r-1)\chi_{n,4^r}(j).
\]

Then

\[
P_\omega(e)=P_1(e)+\sum_{r=1}^{R_0}\omega^rd_r(e),
\]

and root-of-unity orthogonality gives

\[
\boxed{
{1\over M}\sum_\omega|P_\omega(e)|^2
=P_1(e)^2+\sum_{r=1}^{R_0}d_r(e)^2.
}
\tag{IRU.17}

Let

\[
C_{\omega,k}
=\Lambda_{\omega,k}\log
 +\Lambda_{\omega,k}*\Lambda_{\omega,k}.
\]

Every term containing a phase-dependent local factor has nonzero total phase
modulo \(M\). Therefore

\[
\boxed{
{1\over M}\sum_\omega C_{\omega,k}
=C_1,
}
\tag{IRU.18}

where

\[
C_1=\Lambda_1\log+\Lambda_1*\Lambda_1.
\]

The correctly oriented imaginary/Hermitian row curvature is consequently

\[
\boxed{
\begin{aligned}
\mathcal R_{M,k}(e)
&={1\over M}\sum_\omega
 \left(|P_\omega(e)|^2-
       \operatorname{Re}\mathcal L_e(C_{\omega,k})\right)\\
&=P_1(e)^2-\mathcal L_e(C_1)
  +\sum_{r=1}^{R_0}d_r(e)^2\\
&\ge0.
\end{aligned}}
\tag{IRU.19}

Thus arbitrary phase depth is compatible with the **complete Q4 positive
reserve**. The scalar-power failure is repaired because phase-dependent local
levels are separated before the Hermitian square.

## 5. Genuine pole-current frame and deterministic gauge

Let

\[
B_0={1\over\zeta},\qquad q_0=B_0'.
\]

The separate-system current is

\[
\boxed{
\begin{aligned}
q_{\omega,k}=B_{\omega,k}'
={}&\Psi_{\omega,k}q_0\\
&+\left[
 \phi_1'\phi_\omega^k
 +k\phi_1\phi_\omega^{k-1}\phi_\omega'
 \right]B_0.
\end{aligned}}
\tag{IRU.20}

The first term is the genuine externally filtered ordinary pole current. By
(IRU.5),

\[
\boxed{
{1\over M}\sum_\omega
|\Psi_{\omega,k}q_0|^2=|q_0|^2
}
\tag{IRU.21}

on the critical line.

For Q4,

\[
|\phi_\omega'|
\le3L
\tag{IRU.22}

on the critical line. Hence

\[
\boxed{
{1\over M}\sum_\omega
\left|
 \left[
 \phi_1'\phi_\omega^k
 +k\phi_1\phi_\omega^{k-1}\phi_\omega'
 \right]B_0
\right|^2
\le9L^2(k+1)^2|B_0|^2.
}
\tag{IRU.23}

After multiplication by the atomized physical factor
\(\zeta(s)N_\theta(s)\), \(B_0\) cancels. The gauge is deterministic and has
only polynomial \((k+1)^2\) energy.

Every channel is now simultaneously:

```text
main-pole killing;
critical-line all-pass;
exponentially sensitive to an off-line reflected pair;
source-matched to the complete positive Q4 reserve;
gauge equivalent to the genuine ordinary pole current with polynomial cost.
```

## 6. Stable causal realization

Each \(\phi_\omega\) is a first-order causal all-pass filter with geometric tail
\(a^r\). The channel \(\Psi_{\omega,k}\) is a cascade of \(k+1\) unitary
one-state colligations. Therefore:

1. full critical-line \(L^2\) energy is conserved exactly;
2. state dimension is \(k+1\);
3. truncating after a fixed multiple of \(k+1\) delays has exponentially small
   tail.

The exponential off-line signature is not purchased by an exponential
critical-frame, main-pole, gauge, or truncation cost.

## 7. Remaining theorem

A hypothetical off-line zero now creates exponential negative spectral depth in
a bank whose critical norm is fixed, every channel kills the main pole, the
complete averaged row reserve is positive, and the physical gauge is
polynomial.

The remaining theorem is a complete independent-frequency arithmetic estimate:

> prove that the normalized source-convolved reflected block of the common-pole-
> killed phase bank grows subexponentially in \(k\), uniformly after finite-delay
> truncation and endpoint collars.

Such a bound would contradict (IRU.12) and prove RH.

This file does not assert that final growth bound. It closes the main-pole,
spectral, source-sign, channel-proliferation, critical-frame, and deterministic-
gauge components of the proposed contradiction.
