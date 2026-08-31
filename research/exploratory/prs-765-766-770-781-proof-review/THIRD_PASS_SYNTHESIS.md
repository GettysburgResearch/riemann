# Third proof pass: source-normalized endpoint closure and the divisor-renewal transition

**Date:** 2026-09-01  
**Branch:** `research/gpt56-pro/pr765-766-770-781-proof-review`  
**PR:** #783  
**Status:** proposed analytic theorems; independent review required  
**RH/GRH:** RH and GRH remain unproved.

This pass independently reconstructs the second-pass Hecke and divisor
arguments, repairs the load-bearing import boundary, and replaces the
Miller-echel​​on growth bottleneck by the exact source-normalized Poincare
coefficient frame already present in PR #766.

## Current front doors

* [Hecke-scale reconstruction](HECKE_SCALE_RECONSTRUCTION.md)
* [Poincare-frame endpoint ladder](POINCARE_FRAME_ENDPOINT_LADDER.md)
* [Critical divisor-renewal transition](CRITICAL_DIVISOR_RENEWAL_TRANSITION.md)

---

## 1. Reconstruction verdict on the Hecke theorem

The matched Hecke theorem survives reconstruction.

The exact parent identities are retained:

\[
M_X(e_f)
=1+
\frac{\pi}{2L(1,\operatorname{sym}^2 f)}
\sum_n\frac{\lambda_f(n)^2}{n}Q(k,4\pi n),
\]

and

\[
\sum_n\lambda_f(n)^2n^{-s}
=
\frac{\zeta(s)L(s,\operatorname{sym}^2 f)}{\zeta(2s)}.
\]

The Gamma-tail Mellin inequality preserves this exact positive series and
gives

\[
M_X(e_f)\ll\log k.
\]

The one additional automorphic input is now reconstructed explicitly: the
standard comparison

\[
L(1+u,\operatorname{sym}^2f)
\ll L(1,\operatorname{sym}^2f),
\qquad0\le u\le1/\log k,
\]

follows by integrating the usual logarithmic-derivative bound in the
symmetric-square zero-free strip already imported by the parent.  It remains
an imported classical fact, not a new zero-free theorem.

For every adversarial selected set of `r_k` Hecke eigenlines,

\[
\frac1kG_S^{-1/2}I_S(1-c/k)G_S^{-1/2}
=
-\frac1{2c}I
+O\!\left(\frac{r_k\log k}{k}\right),
\]

so `r_k=o(k/log k)` is endpoint-zero-free.  The open Hecke question is the
constant-scale window, not the former four-logarithm gap.

---

## 2. Source-normalized Poincare frame

For the first `M` coefficient functionals, PR #766 gives the exact normalized
Poincare Gram

\[
K_{mn}=\delta_{mn}+
2\pi i^k\sum_{q\ge1}\frac{S(m,n;q)}q
J_{k-1}(4\pi\sqrt{mn}/q).
\]

When `M=o(k/log k)`, its distance from the identity is
superpolynomially small.  The Gram-dual vectors `w_l` therefore satisfy

\[
a_{w_l}(m)=\delta_{lm}\quad(m\le M),
\qquad
G(w_l)=A_l(1+o(k^{-N}))
\]

for every fixed `N`.

Their leading Fourier mode already consumes essentially their entire
Petersson energy.  Consequently the complete low-domain mass and the entire
Fourier tail above mode `M` are superpolynomially small.  This replaces the
old `k^{2J}` Miller-echel​​on cost by an exact minimum-energy source statement.

No unauthenticated projection or fitted basis is introduced.

---

## 3. Exact one-mode centers

The pure source mode `q^m` has the completed scalar period

\[
T_m(c)=
C(s)\frac{\Gamma(k-1+s)}{(4\pi m)^{k-1+s}}
+D(s)\frac{\Gamma(k-s)}{(4\pi m)^{k-s}},
\qquad s=1-c/k.
\]

Its unique endpoint zero satisfies

\[
\widehat c_{k,m}
=12m+
\frac{288m^2}{k}\log\frac{k}{4\pi m}
+O\!\left(
\frac{m^2}{k}+
\frac{m^3\log^2(k/m+2)}{k^2}
\right),
\]

and

\[
\widehat c_{k,m+1}-\widehat c_{k,m}=12+o(1)
\]

uniformly for `m=o(k/log k)`.

This corrects the interpretation of the previous pass.  The scale
`J^2/k` governs finite-block coupling **after recentering**, while the literal
center `12J` first drifts by order

\[
J^2\log(k/J)/k.
\]

Thus fixed-center and recentered transitions are different.

---

## 4. Recentered determinant closure

Let

\[
L(k)\log(k+2)=o(k).
\]

For every `J<=L(k)`, take a fixed-radius disc about the exact center
`chat_{k,J}`.  Split

\[
S_k=
\operatorname{span}\{w_1,\ldots,w_{2L}\}
\mathbin{\perp_G}W_{2L+1}.
\]

The far block is coercive by order `k/L`, hence invertible.  Its Schur
correction is superpolynomially small.  In the finite block, symmetric
source scaling makes every off-diagonal entry exponentially small:

\[
\frac{|H_{lm}|}{\sqrt{A_lA_m}}
\ll
\sigma_{-1}(|l-m|)
\exp[-c k|l-m|/L].
\]

Rouche against the product of exact one-mode diagonals therefore proves:

* for every `i<=J`, `D_i` has exactly one simple real zero in the `J`-th
  recentered disc;
* `D_{J+1}` is nonzero there;
* the result is simultaneous for all `J<=L(k)`;
* the zeros weakly interlace.

This gives a fixed-weight determinant census throughout the essentially
maximal endpoint range `L=o(k/log k)`.

Weak rather than strict interlacing is necessary.  Equality occurs exactly
when the source Schur coupling vanishes, in which case the two simple
determinant zeros cancel in their quotient.

---

## 5. Strict subcritical ladder

If

\[
\frac{L(k)^2\log(L(k)+2)}{k}\to0,
\]

the source coupling remains perturbative:

\[
\frac{b_{i,J}}{A_J}
=
\sigma_{-1}(J-i)(1+o(1)).
\]

All weak inequalities become strict and the parent gap and residue formulas
hold in recentered form.  If also

\[
L^2\log(k/L+2)=o(k),
\]

the centers are `12J+o(1)` and the literal fixed-center laws are recovered.

This improves the earlier cube-root theorem to the source-natural
square-root/logarithmic regime.  The older theorem remains a valid smaller
subregime but is no longer the front boundary.

---

## 6. Critical divisor-renewal law

At fixed offset `h=J-i` and

\[
J^2/k\to\tau\in(0,\infty),
\]

the intermediate column-scaled source matrix tends to

\[
(\mathcal C_\tau)_{rs}
=
\begin{cases}
r/(24\tau),&r=s,\\
\sigma_{-1}(r-s),&r>s,\\
0,&r<s.
\end{cases}
\]

The effective coupling is

\[
\boxed{
 g_h(\tau)
 =-rac{h}{24\tau}[z^h]
 \exp\!\left[
 -24\tau
 \sum_{r\ge1}\frac{\sigma_{-1}(r)}r z^r
 \right].
}
\]

Equivalently, the integrating factor is built from

\[
\Phi(z)
=-\sum_{d\ge1}\frac{\log(1-z^d)}{d^2}.
\]

Away from a root of `g_h`, strict interlacing survives and

\[
c_{J-h,J}-c_{J-h+1,J}
=
\frac{6912\tau^2}{h}g_h(\tau)^2
\frac{A_J}{A_{J-h}}(1+o(1)),
\]

\[
\operatorname{Res}_sQ_{J-h}
=
\frac{288J^2A_J}{k^2}g_h(\tau)^2(1+o(1)).
\]

The first polynomials are

\[
g_1=1,
\qquad
g_2=\frac32-24\tau,
\qquad
g_3=\frac43-54\tau+288\tau^2.
\]

Therefore

\[
\boxed{\tau=1/16}
\]

is the first exact leading merger resonance.  This proves that the parent
coefficient `sigma_{-1}(h)` cannot remain the uniform coupling through the
square-root scale.

At a resonance the present relative gap law stops.  No exact finite-weight
cancellation is asserted without the next source term.

---

## 7. Imported versus new

### Imported from PR #766

* coefficient Poincare series and exact Petersson Gram;
* completed period normalization and coefficient flags;
* Fourier expansion and complex Bessel bound;
* exact arithmetic cross coefficient;
* source Schur identities, reflection, and Schwarz symmetry;
* the symmetric-square zero-free machinery used in the Hecke lane.

### New in this pass

1. an explicit reconstruction of the near-one Hecke import;
2. the Gram-dual Poincare flag and complete energy-saturation estimate;
3. exact recentered one-mode centers and their spacing;
4. the `L=o(k/log k)` determinant census;
5. exact weak interlacing and the coupling/cancellation criterion;
6. the strict square-root/logarithmic subcritical theorem;
7. the triangular critical divisor block;
8. the renewal generating function and critical gap/residue laws;
9. the first exact merger resonance `J^2/k ->1/16` at offset two.

### Not claimed

* strict interlacing throughout the full `o(k/log k)` range;
* exact cancellation at a critical resonance;
* a complete root law for the coupling polynomials;
* a growing-offset critical theorem;
* a sharp constant in the Hecke `k/log k` window;
* critical-line purity, RH, or GRH.

---

## 8. Best next closure target

The next theorem-sized target is the all-offset resolvent of

\[
(\mathcal L_\tau x)_r
=
\frac{r}{24\tau}x_r
+
\sum_{s<r}\sigma_{-1}(r-s)x_s.
\]

Its generating-function form is

\[
z\frac d{dz}+24\tau S(z),
\qquad
S(z)=\sum_{n\ge1}\sigma_{-1}(n)z^n.
\]

A full spectral analysis should classify which weak interlacings remain
strict, resolve the resonance scaling, and then feed the resulting leverage
profiles into the constant Hecke-support window.  Finite computations may
suggest that analysis, but the current pass stops at the proved fixed-offset
renewal law.