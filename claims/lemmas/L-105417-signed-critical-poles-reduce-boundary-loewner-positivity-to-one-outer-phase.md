# L-105417 — Signed critical poles reduce the boundary Loewner gate to one scalar outer-phase condition

Claim ID: `L-105417`  
Status: **PROVED EXACT HARMONIC REDUCTION; XI OUTER-PHASE ESTIMATE OPEN**  
Created: 2026-08-24  
Depends on: `L-105214`, `L-105217`, `L-105350`, `L-105416`  
RH status: **not assumed**

## 1. Meromorphic Pick setup

Let `F` be a nonconstant real entire function of definite parity and put

\[
m(z)={F(z)\over F'(z)}.
\tag{L-105417.1}
\]

Assume every zero of `F'` is real, every nonremovable critical pole is simple,
and

\[
\boxed{
\rho_c={F(c)\over F''(c)}\le0.
}
\tag{L-105417.2}
\]

Common zeros are interpreted by the removable/confluent ledger. Under these
hypotheses `m` is holomorphic in the open upper half-plane. Near a real pole,

\[
m(c+iy)={\rho_c\over iy}+O(1)
=i{-\rho_c\over y}+O(1),
\]

so its imaginary part is nonnegative on every sufficiently small upper
semicircle around the pole.

For even `F`, one may equivalently remove the central pole and work with

\[
\widehat m(z)=m(z)-\rho_0/z.
\]

The removed central term is itself a Pick atom when `rho_0<=0`.

## 2. One scalar exhaustion gate

Let `D_R` be a cofinal exhaustion of the upper half-plane by bounded Jordan
domains. Its lower boundary lies on the real axis with small upper
semicircular detours around the real critical poles; write `Gamma_R` for the
remaining outer boundary.

Define

```text
OPG105417 — outer phase gate

There is such an exhaustion for which

    epsilon_R := max(0,-inf_(z in Gamma_R) Im m(z)) -> 0.
```

For the centrally regularized even coordinate, replace `m` by `mhat`; the
removed central Pick atom is then restored at the end.

## 3. Maximum-principle closure

Put

\[
u(z)=\operatorname{Im}m(z).
\]

This is harmonic in every `D_R`. On the real boundary away from poles its
continuous boundary value is zero. On the small pole semicircles it is
nonnegative after the radii are chosen sufficiently small. On `Gamma_R`,

\[
u\ge-\varepsilon_R.
\]

The harmonic minimum principle therefore gives, at every fixed point contained
in `D_R`,

\[
u(z)\ge-\varepsilon_R.
\]

Letting `R` tend cofinally to infinity proves

\[
\boxed{
\operatorname{Im}m(z)\ge0
\qquad(\operatorname{Im}z>0).
}
\tag{L-105417.3}
\]

Since `m` is nonconstant, the strong minimum principle makes the inequality
strict. Thus `m` is a meromorphic Pick function.

Conversely, if `m` is Pick, then `OPG105417` holds on every regular exhaustion
with `epsilon_R=0`. Under the signed-real-pole hypothesis, `OPG105417` is
therefore exactly the missing escape-at-infinity condition.

## 4. Herglotz representation and automatic capacity

The meromorphic Herglotz representation has the form

\[
\boxed{
m(z)=az+b+
\sum_c(-\rho_c)
\left({1\over c-z}-{c\over1+c^2}\right),
\qquad a\ge0,
}
\tag{L-105417.4}
\]

with the usual locally uniform symmetric summation. Definite parity forces the
constant term to vanish after pairing. In the origin Stieltjes coordinate,

\[
\boxed{
\widehat m(z)
=az+
\sum_{c>0}
W_c{z\over1-s_cz^2},
\qquad
W_c={-2\rho_c\over c^2}\ge0,
\quad s_c=c^{-2}.
}
\tag{L-105417.5}
\]

Consequently the complete source measure is

\[
\boxed{
\nu_{\rm source}
=a\delta_0+
\sum_{c>0}W_c\delta_{s_c}.
}
\tag{L-105417.6}
\]

Every finite-window boundary remainder consists of the nonnegative affine atom
plus the positive atoms outside that window. Hence both Stieltjes matrix
families are positive at every order and in every window:

\[
\boxed{
\mathrm{OPG105417}
\wedge
\mathrm{CRVH105330}
\Longrightarrow
\mathrm{OASH105350}
\Longleftrightarrow
\mathrm{BRP105220}.
}
\tag{L-105417.7}
\]

The scalar endpoint condition is automatic:

\[
\boxed{
\widehat a_0-
\sum_{c>0}W_c
=a\ge0.
}
\tag{L-105417.8}
\]

Thus `ZCAP105412` is the nonnegative linear coefficient in the global Herglotz
representation, not a separate remote-moment phenomenon.

## 5. Exclusion of nonreal zeros

If `F(z_0)=0` in the upper half-plane, then `m(z_0)=0`, with the quotient
understood removably at a multiple zero. A nonconstant Pick function has
strictly positive imaginary part in the upper half-plane and cannot vanish
there. Therefore

\[
\boxed{
\mathrm{CRVH105330}
\wedge
\mathrm{OPG105417}
\Longrightarrow
F\text{ has only real zeros}.
}
\tag{L-105417.9}
\]

For the last defective Xi derivative in the frozen reverse-Rolle programme,
this supplies both the pointwise residue and boundary negative-square closures.

## 6. Oriented phase form

For real `alpha`, the regularized shifted ratio of `L-105416` satisfies

\[
\boxed{
\left.\partial_\alpha
\arg\mathcal M_\alpha^\sharp(z)
\right|_{0}
=-2\operatorname{Im}\widehat m(z).
}
\tag{L-105417.10}
\]

Hence `OPG105417` is equivalently the scalar outer-boundary statement

\[
\boxed{
\limsup_R
\sup_{z\in\Gamma_R}
\left.
\partial_\alpha
\arg\mathcal M_\alpha^\sharp(z)
\right|_0
\le0.
}
\tag{L-105417.11}
\]

The former all-packet boundary Loewner problem has therefore become, after the
sharp critical sign is retained, one infinitesimal oriented phase inequality
on one cofinal outer boundary.

## 7. Scope and firewalls

- The critical-pole sign and reality hypotheses are indispensable. A positive
  residue creates a negative upper-half-plane singularity and defeats the
  maximum principle.
- A finite collection of boundary sample points does not imply `OPG105417`.
- Safe-axis positivity alone is insufficient without control of the outer
  boundary; `R-105360` remains binding.
- The theorem does not prove the Xi outer-phase estimate, `CRVH105330`, the
  low-order descent, or RH. It replaces an all-packet matrix gate by the exact
  scalar harmonic escape condition that generates it.