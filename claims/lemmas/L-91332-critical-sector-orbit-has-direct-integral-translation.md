# L-91332 — The critical Jordan sectors admit an unconditional direct-integral translation representation

Claim ID: `L-91332`  
Status: **EXACT SECTOR-BUNDLE CONSTRUCTION; POSITIVE-ENERGY SELECTION REMAINS OPEN**  
Created: 2026-08-12  
Depends on: `L-91327/L-91331`; von Neumann incomplete tensor products  
RH status: **unproved**

## 1. Boundary-sector family

Fix \(0<\omega<1/2\). For each prime let

\[
\mathcal H_p=H^2(\mathbb D).
\]

At physical boundary parameter \(t\in\mathbb R\), define

\[
D_{p,t}(z)
=
\frac{
1-p^{-1/2+\omega}e^{it\log p}z
}{
1-p^{-1/2-\omega}e^{it\log p}z
}
\tag{L-91332.1}
\]

and its unit normalization

\[
\Omega_{p,t}
=
\frac{D_{p,t}}{\|D_{p,t}\|_{H^2}}.
\tag{L-91332.2}
\]

Let

\[
\mathcal H_t
=
\bigotimes_p^{\Omega_{p,t}}\mathcal H_p
\tag{L-91332.3}
\]

be the incomplete tensor product based at the \(t\)-sector vacuum

\[
\Omega_t=\bigotimes_p\Omega_{p,t}.
\tag{L-91332.4}
\]

By `L-91327`, \(\mathcal H_t\) and \(\mathcal H_{t'}\) are disjoint as fixed product sectors when \(t\ne t'\). That statement does not prevent unitary transport between distinct fibers.

## 2. Exact fiber transport

For \(a\in\mathbb R\), define the local phase rotation

\[
(R_{p,a}F)(z)=F(e^{ia\log p}z).
\tag{L-91332.5}
\]

It is unitary on \(H^2(\mathbb D)\) and satisfies

\[
R_{p,a}\Omega_{p,t}
=
\Omega_{p,t+a}.
\tag{L-91332.6}
\]

Because the reference vector is mapped exactly, the infinite tensor product

\[
\boxed{
U_{t,a}
=
\bigotimes_p R_{p,a}
:
\mathcal H_t\longrightarrow\mathcal H_{t+a}
}
\tag{L-91332.7}
\]

exists canonically and is unitary. No Kakutani summability condition is needed for a unitary between fibers whose reference vectors are matched exactly.

The cocycle law holds:

\[
\boxed{
U_{t+a,b}U_{t,a}=U_{t,a+b}.
}
\tag{L-91332.8}
\]

## 3. Direct-integral orbit representation

Trivialize the field by

\[
J_t:=U_{t,-t}:\mathcal H_t\to\mathcal H_0.
\tag{L-91332.9}
\]

This supplies a measurable constant Hilbert bundle. Define

\[
\mathscr H_{\omega}^{\rm orb}
=
\int_{\mathbb R}^{\oplus}\mathcal H_t\,dt
\cong
L^2(\mathbb R;\mathcal H_0).
\tag{L-91332.10}
\]

On sections put

\[
(\mathcal U_a\Psi)_{t+a}
=
U_{t,a}\Psi_t.
\tag{L-91332.11}
\]

Under the trivialization \(J_t\), this is the ordinary translation group:

\[
(J\mathcal U_aJ^{-1}\psi)(t)
=
\psi(t-a).
\tag{L-91332.12}
\]

Hence

\[
\boxed{
a\longmapsto\mathcal U_a
}
\]

is a strongly continuous unitary representation of \(\mathbb R\) on
\(\mathscr H_{\omega}^{\rm orb}\).

This is the correct replacement for the impossible within-sector product translation rejected by `L-91327`.

## 4. Distinguished outer section

Let

\[
r(t)=\frac1{\frac12-it}.
\tag{L-91332.13}
\]

Since \(r\in L^2(\mathbb R)\), the vacuum section

\[
\mathbf r_\omega(t)=r(t)\Omega_t
\tag{L-91332.14}
\]

belongs to \(\mathscr H_\omega^{\rm orb}\).

The completed boundary quotient

\[
\Theta_\omega(t)
=
\frac{
\xi(\frac12-\omega-it)
}{
\xi(\frac12+\omega-it)
}
\tag{L-91332.15}
\]

has unimodular real boundary values after cancelling removable common zeros. Therefore

\[
\mathbf s_\omega(t)
=
\Theta_\omega(t)r(t)\Omega_t
\tag{L-91332.16}
\]

also belongs to the direct-integral Hilbert space, with

\[
\|\mathbf s_\omega\|=\|\mathbf r_\omega\|.
\tag{L-91332.17}
\]

This equality is boundary unitarity only. It does not imply RH.

## 5. Positive-energy subspace

Under the trivialization \(J_t\),

\[
J\mathbf s_\omega(t)
=
\Theta_\omega(t)r(t)\Omega_0.
\tag{L-91332.18}
\]

Let

\[
\mathscr H_{\omega,+}^{\rm orb}
=
H^2(\mathbb C_+;\mathcal H_0)
\subset
L^2(\mathbb R;\mathcal H_0)
\tag{L-91332.19}
\]

be the positive-energy/causal Hardy subspace. Then

\[
\boxed{
\mathbf s_\omega\in\mathscr H_{\omega,+}^{\rm orb}
\iff
\Theta_\omega r\in H^2(\mathbb C_+).
}
\tag{L-91332.20}
\]

Because \(r\) is outer and \(\Theta_\omega\) is boundary unimodular, the right side is equivalent to meromorphic innerness of \(\Theta_\omega\), hence to the zero-free half-plane at scale \(\omega\).

Thus the representation-changing and translation-covariance part of `EPBOT` is constructible unconditionally. The entire RH-bearing content is the positive-energy selection of one distinguished section.

## 6. Exact boundary

```text
critical family of disjoint product sectors        EXACT
unitary transport between fibers                   EXACT
strongly continuous direct-integral translation    EXACT
boundary-unitary completed section                  EXACT
positive-energy membership                         OPEN / RH-BEARING
positive-energy membership for omega_j -> RH        PROPOSED COMPLETE
Riemann Hypothesis                                  UNPROVED
```
