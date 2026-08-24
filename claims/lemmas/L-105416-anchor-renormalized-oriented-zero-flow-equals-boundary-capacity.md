# L-105416 — Anchor-renormalized oriented shifted-zero flow equals the complete boundary capacity

Claim ID: `L-105416`  
Status: **PROVED EXACT FINITE-WINDOW IDENTITY**  
Created: 2026-08-24  
Depends on: `L-105214`, `L-105340--L-105341`, `L-105350--L-105370`  
RH status: **not assumed**

## 1. Setup and the shifted companion

Let `F` be entire, real on the real axis, and of definite parity. Let `Omega`
be a bounded parity- and conjugation-symmetric regular window containing the
origin. Assume first that the critical points in the closed window are simple
and noncommon; the confluent ledger is retained separately.

Put

\[
E_\alpha(z)=F'(z)-\alpha F(z),
\qquad
E_{-\alpha}(z)=F'(z)+\alpha F(z),
\tag{L-105416.1}
\]

and

\[
\mathcal M_\alpha(z)={E_\alpha(z)\over E_{-\alpha}(z)}.
\tag{L-105416.2}
\]

For odd `F`, define

\[
\mathcal M_\alpha^\sharp=\mathcal M_\alpha.
\]

For even `F`, the zero of `F'` at the origin moves. Let `c_\alpha` be the
analytic zero branch of `E_\alpha` with `c_0=0`. Then

\[
c_\alpha'(0)=\rho_0={F(0)\over F''(0)},
\qquad
c_{-\alpha}=-c_\alpha,
\]

and define the central-branch-removed ratio

\[
\boxed{
\mathcal M_\alpha^\sharp(z)
={E_\alpha(z)\over E_{-\alpha}(z)}
 {z-c_{-\alpha}\over z-c_\alpha}.
}
\tag{L-105416.3}
\]

Use the regularized source ratio

\[
\widehat m_F(z)=
\begin{cases}
F(z)/F'(z),&F\text{ odd},\\[1mm]
F(z)/F'(z)-\rho_0/z,&F\text{ even}.
\end{cases}
\tag{L-105416.4}
\]

Then direct differentiation gives the exact tangent identity

\[
\boxed{
\left.\partial_\alpha
\log\mathcal M_\alpha^\sharp(z)
\right|_{\alpha=0}
=-2\widehat m_F(z).
}
\tag{L-105416.5}
\]

For even `F`, the central factor contributes `2rho_0/z`, exactly cancelling
the removed principal part. This correction is load bearing.

## 2. Polynomial-square Cauchy tests

Let

\[
q(s)=\sum_{j=0}^{k-1}q_js^j
\]

be a real polynomial and let `a in {0,1}`. Define

\[
\boxed{
K_{q,a}(z)
=z^{-2a-2}q(z^{-2})^2.
}
\tag{L-105416.6}
\]

It has the single-valued meromorphic primitive

\[
\boxed{
\Psi_{q,a}(z)
=-\sum_{r,s=0}^{k-1}
{q_rq_s\over2(a+r+s)+1}
 z^{-[2(a+r+s)+1]},
}
\tag{L-105416.7}
\]

so that

\[
\Psi_{q,a}'=K_{q,a}.
\tag{L-105416.8}
\]

Define the oriented companion flow

\[
\boxed{
\mathfrak J_{F,\Omega}^{(a)}(q;\alpha)
={1\over2\pi i}
\int_{\partial\Omega}
\Psi_{q,a}(z)
 {\partial_z\mathcal M_\alpha^\sharp(z)
  \over\mathcal M_\alpha^\sharp(z)}\,dz.
}
\tag{L-105416.9}
\]

The test has a pole at the source anchor `0`, but is analytic on the regular
outer contour. This pole is precisely what retains the source budget.

## 3. Exact first-variation identity

Differentiate (L-105416.9), use (L-105416.5), and integrate by parts along the
closed contour:

\[
\begin{aligned}
{1\over2}
\left.\partial_\alpha
\mathfrak J_{F,\Omega}^{(a)}(q;\alpha)
\right|_0
&=-{1\over2\pi i}
\int_{\partial\Omega}
\Psi_{q,a}(z)\widehat m_F'(z)\,dz\\
&={1\over2\pi i}
\int_{\partial\Omega}
K_{q,a}(z)\widehat m_F(z)\,dz.
\end{aligned}
\tag{L-105416.10}
\]

Write

\[
\widehat m_F(z)=z\sum_{n\ge0}a_n(F)z^{2n}
\]

and use the source, critical and boundary matrices of `L-105370`. The anchor
residue in (L-105416.10) is

\[
\operatorname{Res}_{z=0}
K_{q,a}(z)\widehat m_F(z)
=q^T\mathsf A_k^{(a)}(F)q.
\tag{L-105416.11}
\]

At one nonzero critical pair `+-c`, with

\[
\rho_c={F(c)\over F''(c)},
\qquad
s_c=c^{-2},
\qquad
W_c=-2\rho_c/c^2,
\]

the two residues contribute

\[
2\rho_cK_{q,a}(c)
=-W_cs_c^a q(s_c)^2.
\tag{L-105416.12}
\]

Summing all critical pairs in the window gives

\[
\boxed{
{1\over2}
\left.\partial_\alpha
\mathfrak J_{F,\Omega}^{(a)}(q;\alpha)
\right|_0
=q^T
\left(
\mathsf A_k^{(a)}(F)-
\mathsf C_{k,\Omega}^{(a)}(F)
\right)q
=q^T\mathsf S_{k,\Omega}^{(a)}q.
}
\tag{L-105416.13}
\]

This is an identity, not an estimate.

## 4. Zero-motion form and the source counterterm

Let `mathfrak Z_alpha^sharp(Psi;Omega)` be the oriented sum of `Psi` over the
zeros of `E_alpha` minus those of `E_(-alpha)` in the window, with the moving
central branch deleted in the even case. The implicit function theorem gives
at every nonzero simple critical point

\[
c_\alpha'(0)=\rho_c,
\qquad
c_{-\alpha}'(0)=-\rho_c.
\]

Therefore

\[
\boxed{
{1\over2}
\left.\partial_\alpha
\mathfrak Z_\alpha^\sharp(\Psi_{q,a};\Omega)
\right|_0
=-q^T\mathsf C_{k,\Omega}^{(a)}q.
}
\tag{L-105416.14}
\]

The pole of `Psi_(q,a)` at the origin supplies the missing anchor term:

\[
\boxed{
{1\over2}
\left.\partial_\alpha
\operatorname{Res}_{z=0}
\left[
\Psi_{q,a}(z)
 {\partial_z\mathcal M_\alpha^\sharp(z)
  \over\mathcal M_\alpha^\sharp(z)}
\right]
\right|_0
=q^T\mathsf A_k^{(a)}q.
}
\tag{L-105416.15}
\]

Thus boundary capacity is the **source-renormalized zero motion**, not the raw
critical-zero motion.

## 5. Exact equivalence with the boundary hierarchy

Equation (L-105416.13) proves

\[
\boxed{
\mathrm{OASH105350}
\Longleftrightarrow
\left.\partial_\alpha
\mathfrak J_{F,\Omega}^{(a)}(q;\alpha)
\right|_0\ge0
}
\tag{L-105416.16}
\]

for every regular window, every finite real polynomial `q`, and both
`a=0,1`. Through `L-105350` and `T-105371`, this is also exactly the
all-packet boundary Loewner/capacity gate.

The scalar endpoint condition of `L-105412` is the smallest member:

\[
\boxed{
\mathrm{ZCAP105412}
\quad\Longleftrightarrow\quad
\left.\partial_\alpha
\mathfrak J_{F,\Omega}^{(0)}(1;\alpha)
\right|_0\ge0.
}
\tag{L-105416.17}
\]

It is not an unrelated tail hypothesis; it is the first oriented-flow test.

## 6. Parity and safe-line folding

For either parity,

\[
\boxed{
\mathcal M_\alpha^\sharp(-z)
=\mathcal M_\alpha^\sharp(z)^{-1}.
}
\tag{L-105416.18}
\]

In the Riemann `s` coordinate this is the functional-equation folding of
`L-105341`. Hence the left and right safe-line pieces of every flow in
(L-105416.13) are one oriented copy, not independent boundary estimates.

Moreover, on the right safe line the alpha tangent is the single reciprocal
source `F/F'` of `L-105331`. The real frozen coefficient family has one global
sign (`L-105420`) and the one-sided Hardy representation has the explicit phase
gap of `L-105422`. The remaining burden is the physical realization and its
archimedean, horizontal and taper errors, not a new source identity.

## 7. Scope

This theorem does not prove the first variation nonnegative for Xi. It proves
that the source-capacity, boundary-Loewner and oriented shifted-zero programmes
are the same typed object after the anchor and central branch are retained.
The all-order safe-line estimate, complete critical-residue sign, low-order
descent and RH remain open.