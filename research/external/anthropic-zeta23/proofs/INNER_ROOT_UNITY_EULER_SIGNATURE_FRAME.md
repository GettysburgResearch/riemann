# Inner root-of-unity Euler signature frame

Status: **PROPOSED COMPLETE EXACT SOURCE/SPECTRAL THEOREM — independent review required**  
Date: 2026-08-10  
Dependencies: PR #325 Q4 Euler–Blaschke scattering and root-of-unity reserve; PR #363 reflected-pair spectrum  
RH status: **unproved**

## 1. Phase-shifted critical inner factors

Fix \(Q=2^d\), put

\[
a=Q^{-1/2},\qquad L=\log Q,
\]

and work in centered coordinates \(s=\tfrac12+z\). For \(|\omega|=1\), define

\[
\boxed{
\phi_\omega(z)
=Q^{-1/2}
 {1-\omega Q^{1-s}\over1-\omega Q^{-s}}
={a-\omega e^{-Lz}\over1-a\omega e^{-Lz}}.
}
\tag{IRU.1}

Then

\[
\boxed{|\phi_\omega(it)|=1}
\tag{IRU.2}

and

\[
\boxed{
\phi_\omega(-\overline z)
={1\over\overline{\phi_\omega(z)}}.
}
\tag{IRU.3}

For \(\Re z>0\), \(|\phi_\omega(z)|<1\).

Let \(\Omega_{M,\eta}=e^{i\eta}\Omega_M\) be a rotated root-of-unity set and
consider the powered channel family

\[
\boxed{F_{\omega,k}(z)=\phi_\omega(z)^k.}
\tag{IRU.4}

Every individual channel is all-pass on the critical line, so

\[
\boxed{
{1\over M}\sum_{\omega\in\Omega_{M,\eta}}
|F_{\omega,k}(it)|^2=1
}
\tag{IRU.5}

for every \(k,M,\eta\). No power-dependent frame normalization is required.

## 2. Exact reflected-pair block

Let \(z\) be a right-half-plane zero coordinate and put

\[
r_\omega=|\phi_\omega(z)|\in(0,1).
\]

For normalized channel evaluation vectors, (IRU.3) gives

\[
A_k={1\over M}\sum_\omega r_\omega^{2k},
\qquad
B_k={1\over M}\sum_\omega r_\omega^{-2k},
\tag{IRU.6}

and the reflected cross is exactly

\[
\boxed{\langle u,v\rangle=1.}
\tag{IRU.7}

Therefore a reflected zero pair of multiplicity \(m\) has exactly two nonzero
eigenvalues

\[
\boxed{
\lambda_\pm=m(1\pm\sqrt{A_kB_k}).
}
\tag{IRU.8}

Cauchy–Schwarz gives \(A_kB_k\ge1\). Equality holds only if all
\(r_\omega\) are equal.

## 3. Generic strictness and exponential depth

Write \(t=e^{-Lz}=Re^{i\psi}\), with \(0<R<1\). Then

\[
|\phi_\omega(z)|^2
={a^2+R^2-2aR\cos(\arg\omega+\psi)
 \over
 1+a^2R^2-2aR\cos(\arg\omega+\psi)}.
\tag{IRU.9}

Because

\[
(a^2+R^2)-(1+a^2R^2)
=-(1-a^2)(1-R^2)<0,
\]

the ratio (IRU.9) is a strictly decreasing function of the displayed cosine.
For every \(M\ge2\), all but finitely many rotations \(\eta\) therefore give

\[
0<r_{\min}<r_{\max}<1.
\tag{IRU.10}

For such a rotation,

\[
A_k\ge{r_{\max}^{2k}\over M},
\qquad
B_k\ge{r_{\min}^{-2k}\over M},
\]

and hence

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

The gain is unavailable to a single scalar inner power, where exact
\(J\)-unitarity leaves the pair contribution unchanged. It arises from the
phase-resolved channel geometry.

## 4. Powered separate systems retain an exact averaged reserve

Define

\[
\boxed{
B_{\omega,k}(s)={\phi_\omega(s-1/2)^k\over\zeta(s)},
\qquad A_{\omega,k}=B_{\omega,k}^{-1}.
}
\tag{IRU.13}

A constant normalization does not affect logarithmic derivatives. The
generalized-prime sequence is

\[
\boxed{
\Lambda_{\omega,k}
=\Lambda
 +kL\sum_{r\ge1}
  \omega^r(Q^r-1)\delta_{Q^r}.
}
\tag{IRU.14}

Fix a carry endpoint \(n\), let \(R_0=\lfloor\log_Qn\rfloor\), and choose

\[
\boxed{M>2R_0.}
\tag{IRU.15}

For a carry row \(e=(n,j)\), put

\[
F(e)=\log\binom nj,
\qquad
d_r(e)=kL(Q^r-1)\chi_{n,Q^r}(j).
\]

Root-of-unity orthogonality gives

\[
\boxed{
{1\over M}\sum_\omega|P_\omega(e)|^2
=F(e)^2+\sum_{r=1}^{R_0}d_r(e)^2.
}
\tag{IRU.16}

For

\[
C_{\omega,k}
=\Lambda_{\omega,k}\log
 +\Lambda_{\omega,k}*\Lambda_{\omega,k},
\]

every local logarithmic, ordinary/local, and active local/local term has a
nonzero phase modulo \(M\). Hence

\[
\boxed{
{1\over M}\sum_\omega C_{\omega,k}
=\Lambda\log+\Lambda*\Lambda
}
\tag{IRU.17}

through endpoint \(n\). Therefore

\[
\boxed{
\begin{aligned}
\mathcal R_{M,k}(e)
&={1\over M}\sum_\omega
 \left(|P_\omega(e)|^2-
       \mathcal L_e(C_{\omega,k})\right)\\
&=F(e)^2-S_0(e)
  +\sum_{r=1}^{R_0}d_r(e)^2\\
&\ge0.
\end{aligned}}
\tag{IRU.18}

This is the complete powered source reserve. Unlike scalar Q4 powers, no mixed
local forcing is stacked in one row.

## 5. Genuine pole-current frame and deterministic gauge

Let

\[
B_0={1\over\zeta},\qquad q_0=B_0'.
\]

The separate-system current is

\[
q_{\omega,k}=B_{\omega,k}'
=\phi_\omega^kq_0
 +k\phi_\omega^{k-1}\phi_\omega'B_0.
\tag{IRU.19}

The first term is the genuine externally filtered ordinary pole current. By
(IRU.5), on the critical line

\[
\boxed{
{1\over M}\sum_\omega
|\phi_\omega^kq_0|^2=|q_0|^2.
}
\tag{IRU.20}

Moreover

\[
\phi_\omega'(z)
=L(1-a^2)
 {\omega e^{-Lz}\over(1-a\omega e^{-Lz})^2}.
\tag{IRU.21}

On the critical line,

\[
|\phi_\omega'|
\le L{1+a\over1-a}.
\tag{IRU.22}

Thus the normalized gauge obeys

\[
\boxed{
{1\over M}\sum_\omega
|k\phi_\omega^{k-1}\phi_\omega'B_0|^2
\le
k^2L^2\left({1+a\over1-a}\right)^2|B_0|^2.
}
\tag{IRU.23}

After multiplication by the common atomized physical factor
\(\zeta(s)N_\theta(s)\), \(B_0\) cancels. The gauge is therefore deterministic
and has only polynomial \(k^2\) energy.

The channel family simultaneously has:

```text
critical frame norm                    exactly one;
off-line reflected-pair depth          exponential in k;
complete averaged Selberg reserve       ordinary reserve + local squares;
genuine pole-current reconstruction     exact;
separate-system gauge                   deterministic and polynomial.
```

## 6. Stable causal realization

Each \(\phi_\omega\) is a first-order causal all-pass filter. Its impulse
response has geometric tail \(a^r\), uniformly in \(\omega\). The powered
channel is a cascade of \(k\) unitary one-state colligations. Consequently:

1. its full critical-line \(L^2\) norm is exactly conserved;
2. its state dimension is \(k\);
3. finite-delay truncation errors are exponentially small once the truncation
   length is a fixed multiple of \(k\).

Thus the exponential off-line signature is not purchased by an exponential
critical-frame or truncation cost.

## 7. Remaining theorem

A hypothetical off-line zero now creates exponential negative spectral depth in
a channel bank whose critical norm is fixed, source reserve is positive, and
physical gauge is polynomial.

The remaining step is a complete independent-frequency arithmetic estimate:

> prove that the normalized source-convolved reflected block of the powered
> inner phase bank grows subexponentially in \(k\), uniformly after its
> finite-delay truncation and endpoint collars are included.

Such a bound would contradict (IRU.12) and prove RH.

This file does not assert that bound. It closes the spectral, source-sign,
channel-proliferation, critical-frame, and deterministic-gauge components of
that proposed contradiction.
