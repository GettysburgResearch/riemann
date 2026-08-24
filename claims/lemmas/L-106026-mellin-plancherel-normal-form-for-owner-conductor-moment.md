# L-106026 — The owner-conductor assembly is an exact Mellin moment of mollified reciprocal-`L` defects

Claim ID: `L-106026`  
Programme aliases: `LFAM1.MELLIN_PLANCHEREL_MOMENT`, `LFAM2.TRACE_MOMENT_NORMAL_FORM`, `STRESS.SPECTRAL_OWNER_ASSEMBLY`  
Status: **PROVED EXACT FINITE-SHELL PLANCHEREL REDUCTION**  
Created: 2026-08-24  
Depends on: `L-106025`; PR #719 zero-moment derivative kernel `K_L`  
Programme issues: #743, #736, #737  
RH status: **not assumed**

Put

\[
\kappa(u)=K_L(e^u),
\qquad
\widehat\kappa(t)=\int_{\mathbb R}\kappa(u)e^{-itu}\,du.
\tag{L-106026.1}
\]

The fixed derivative kernel is compactly supported and has zero logarithmic
moment, so

\[
\boxed{\widehat\kappa(0)=0.}
\tag{L-106026.2}
\]

Because `kappa` is compact and piecewise smooth,

\[
\widehat\kappa(t)=O(t)\quad(t\to0),
\qquad
\widehat\kappa(t)=O((1+|t|)^{-1})
\quad(|t|\to\infty).
\tag{L-106026.3}
\]

Only the zero at the origin is load-bearing below; stronger decay may be used
when available.

## 1. One finite owner-conductor shell

Fix an owner pair `P=pq`, an even character `eta` modulo an opposite owner, and
a finite physical core shell `mathcal S`. Let

\[
B_{U;P,\eta}^{\mathcal S}(w)
=
\sum_{a\in\mathcal S}{\beta_{U;P,\eta}(a)\over a^w}
\tag{L-106026.4}
\]

be the coefficient projection in `L-106025.8`. Define its observed log-field

\[
\mathcal V_{U;P,\eta}^{\mathcal S}(u)
={1\over\sqrt P}
\sum_{a\in\mathcal S}{\beta_{U;P,\eta}(a)\over a}
\kappa(u-\log P-2\log a).
\tag{L-106026.5}
\]

The sum is finite. Fourier transformation gives exactly

\[
\boxed{
\widehat{\mathcal V}_{U;P,\eta}^{\mathcal S}(t)
=
\widehat\kappa(t)
P^{-1/2-it}
B_{U;P,\eta}^{\mathcal S}(1+2it).
}
\tag{L-106026.6}
\]

No analytic continuation or infinite-series interchange is used in this
identity.

## 2. Cross packet

For two finite owner-conductor shells,

\[
\boxed{
\begin{aligned}
&\int_{\mathbb R}
\mathcal V_{U;P,\eta}^{\mathcal S}(u)
\overline{\mathcal V_{V;Q,\theta}^{\mathcal T}(u)}\,du\\
&\quad={1\over2\pi}
\int_{\mathbb R}|\widehat\kappa(t)|^2
P^{-1/2-it}Q^{-1/2+it}
B_{U;P,\eta}^{\mathcal S}(1+2it)
\overline{B_{V;Q,\theta}^{\mathcal T}(1+2it)}\,dt.
\end{aligned}
}
\tag{L-106026.7}
\]

This is the exact spectral form of one physical near-collision Gram entry.

## 3. Coherent finite assembly

Let `mathcal I` be any finite source-owned collection of owner pairs,
conductors, even characters, shells and deterministic selector labels, with
literal complex coefficients `omega_i`. Put

\[
\mathcal V(u)=\sum_{i\in\mathcal I}\omega_i\mathcal V_i(u).
\]

Plancherel gives

\[
\boxed{
\int_{\mathbb R}|\mathcal V(u)|^2\,du
={1\over2\pi}
\int_{\mathbb R}|\widehat\kappa(t)|^2
\left|
\sum_{i\in\mathcal I}
\omega_iP_i^{-1/2-it}
B_i^{\mathcal S_i}(1+2it)
\right|^2dt.
}
\tag{L-106026.8}
\]

Every finite dyadic block of `SOCM106020` is of this form, followed by the
explicit positive Gauss weights from `L-106022.2`. Thus the remaining
owner-packet assembly is a hybrid moment over:

```text
Mellin frequency t;
semiprime owner amplifiers P^(-1/2-it);
owner conductors rho;
even Dirichlet characters eta modulo rho;
physical shell projections of
  (1-M_U Z_(P,eta))^2 / Z_(P,eta).
```

## 4. Principal-pole cancellation

For the principal character, `L-106025.9` shows that

\[
B_{U;P,\eta_0}(w)=O((w-1)^{-1})
\quad(w\to1).
\]

On the Plancherel line `w=1+2it`, (L-106026.2)--(L-106026.3) imply

\[
\boxed{
\widehat\kappa(t)
B_{U;P,\eta_0}(1+2it)=O(1)
\quad(t\to0).
}
\tag{L-106026.9}
\]

The derivative kernel therefore cancels the sole principal pole in the exact
moment. This is the spectral version of the zero-square-lattice Type-I
cancellation in the parent arithmetic packet.

## 5. What is now open

After this theorem, `SOCM106020` is not an unspecified occupancy estimate. It
is the subpower bound for the explicit moment in (L-106026.8), with the exact
source selector and physical shell projections retained.

One may not replace `B_i^(S_i)` by the unprojected ratio, drop the principal
root fibre, or average unrelated owner packets without proving the resulting
error. The theorem itself proves no mean-value bound and no RH result.
