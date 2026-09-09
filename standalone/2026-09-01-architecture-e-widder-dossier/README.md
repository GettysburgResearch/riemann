# Architecture E: invariant determinant, theta–Fock gate, and E–Widder source criterion

Status: **PROPOSED PROOF-ORIENTED DOSSIER; INDEPENDENT REVIEW REQUIRED; RH REMAINS UNPROVED.**

This packet collects the full review of PRs #765, #766, #769, #770 and #781,
the source–Hermite–Stieltjes closure, the invariant E–Widder criterion, the
finite-height cone through trillions of orders, and the latest structural
advance: one exact radial determinant and one explicit theta–Fock mixture
whose source-local quasi-free closure would prove RH.

No predecessor branch is modified.  No proposed claim is promoted to
canonical status.  The all-order E–Widder inequality and RH remain unproved.

## 1. Current leading state

Let

\[
 \mathfrak X(s(s-1))=\xi_{\rm R}(s),
 \qquad
 u>0,
 \qquad
 x=\sqrt{u+\frac14},
 \qquad
 s=\frac12+x>1,
\]

and define

\[
 q(u)=2\frac{\mathfrak X'(u)}{\mathfrak X(u)}
 =\frac1x\frac{\xi_{\rm R}'}{\xi_{\rm R}}(s).
\]

For `k>=1`,

\[
 \mathcal W_k(u)=(-1)^{k-1}D_u^{2k-1}[u^kq(u)].
\]

The dossier proves the proposed exact chain

\[
 \boxed{
 \mathrm{RH}
 \iff q\text{ is Stieltjes}
 \iff \mathcal W_k(u)\ge0
 \quad(\forall u>0,\ k\ge1).
 }
 \tag{1.1}
\]

On the Euler-safe half-plane,

\[
 \mathcal W_k(u)
 =\mathcal G_k(u)
 -\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
  \mathcal L_k(u,\log n),
\]

with absolute convergence after every fixed order of differentiation.  Thus
the remaining arithmetic theorem is

\[
 \boxed{
 \sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
 \mathcal L_k(u,\log n)
 \le\mathcal G_k(u)
 \qquad(u>0,\ k\ge1).
 }
 \tag{EW}
\]

## 2. New leverage I — all Widder orders form one radial determinant

Let `a` run over the invariant zero parameters

\[
 a=-\rho(\rho-1).
\]

Define

\[
 \lambda_u(a)=\frac{4ua}{(u+a)^2},
 \qquad
 C_k(u)=\frac{(4u)^k}{2(2k-1)!}\mathcal W_k(u).
\]

Then, without assuming RH,

\[
 \boxed{C_k(u)=\sum_a\lambda_u(a)^k.}
 \tag{2.1}
\]

For nonzero `r`, put

\[
 w=-\frac{(r-1)^2}{4r}.
\]

The complete order product is

\[
 \boxed{
 \Delta_u(w)
 =\prod_a(1-w\lambda_u(a))
 =\frac{\mathfrak X(ur)\mathfrak X(u/r)}
        {\mathfrak X(u)^2}.
 }
 \tag{2.2}
\]

Hence

\[
 \boxed{
 \sum_{k\ge1}C_k(u)w^{k-1}
 =-\frac{\Delta_u'(w)}{\Delta_u(w)}
 =\frac{2u[r^2q(ur)-q(u/r)]}{r^2-1}.
 }
 \tag{2.3}
\]

On the unit circle, `r=e^(i theta)` and
`w=sin^2(theta/2)`,

\[
 \boxed{
 \Delta_u(w)
 =\frac{|\mathfrak X(ue^{i\theta})|^2}{\mathfrak X(u)^2}.
 }
 \tag{2.4}
\]

The invariant function has strictly positive coefficients, so

\[
 0\le\Delta_u(w)\le1
 \qquad(0\le w\le1)
\]

unconditionally.  Therefore

\[
 -\log\Delta_u(w)
 =\sum_{k\ge1}\frac{C_k(u)}k w^k\ge0
\]

through its first zero barrier.  This is a genuine all-order averaged
positivity theorem.  The remaining strengthening is coefficientwise
positivity of every `C_k(u)`.

A nonreal invariant atom `a=|a|e^(i alpha)` creates, at `u=|a|`, the interior
order pole

\[
 w_a=\cos^2(\alpha/2)\in(1/2,1).
\]

Thus

\[
 \boxed{
 \mathrm{RH}
 \iff
 -\Delta_u'(w)/\Delta_u(w)
 \text{ is holomorphic in }|w|<1
 \text{ for every }u>0.
 }
 \tag{2.5}
\]

Read
[`09_INVARIANT_ORDER_PRODUCT_AND_COUNT_LAW.md`](09_INVARIANT_ORDER_PRODUCT_AND_COUNT_LAW.md).

## 3. New leverage II — one positive count law

Write

\[
 \mathfrak X(u)=\sum_{n\ge0}c_nu^n.
\]

The split theta integral gives `c_n>0` for every `n`.  For each `v>0`,

\[
 P_v(z)=\frac{\mathfrak X(vz)}{\mathfrak X(v)}
 =\sum_{n\ge0}p_n(v)z^n
\]

is therefore a probability-generating function.

For one, equivalently every, `v>0`,

\[
 \boxed{
 \mathrm{RH}
 \iff (p_n(v))\in PF_\infty
 \iff P_v\text{ is Poisson-binomial}
 \iff P_v(z)=\det(I-K_v+zK_v)
 }
 \tag{3.1}
\]

for one positive trace-class contraction `K_v`.

This is a one-scale constructive endpoint: build `K_v` directly from the
theta/prime source and RH follows.

## 4. New leverage III — explicit theta–Fock mixture

The logarithmic theta coordinate gives

\[
 \mathfrak X(v)
 =\frac12+2v\int_0^\infty
 e^{\tau/2}\psi(e^{2\tau})
 \cosh\left(\tau\sqrt{v+\frac14}\right)d\tau.
\]

For fixed `tau`,

\[
 \frac{\cosh(\tau\sqrt{vz+1/4})}
      {\cosh(\tau\sqrt{v+1/4})}
 =\prod_{j\ge0}(1-p_j+p_jz),
\]

where

\[
 p_j=p_j(\tau;v)
 =\frac{v}{v+\frac14+\pi^2(j+1/2)^2/\tau^2}.
\]

Consequently `P_v` is exactly

```text
a vacuum atom at N=0
+
a positive theta mixture of counts
N=1+sum_j independent Bernoulli(p_j(tau;v)).
```

Every fiber is a fermionic quasi-free determinant.  The completed arithmetic
law is a positive mixture of those determinants.  RH is equivalent to this
specific mixture itself being one determinant.

The exact gate is:

> **Theta quasi-free gate `TQF(v)`.** Construct from the theta source one
> positive trace-class contraction `K_v` satisfying
> 
> \[
>  \mathfrak X(vz)/\mathfrak X(v)=\det(I-K_v+zK_v).
> \]

A direct integral or convexly averaged fiber operator is insufficient: an
arithmetic mixture of determinants is not the determinant of the average.
The latent theta selector must be removed by a genuine exterior-power,
conservative-colligation or planar-network theorem.

The fiber coefficient kernel is

\[
 [v^n]\cosh\left(\tau\sqrt{v+\frac14}\right)
 =\frac{\sqrt\pi}{2n!}
  \tau^{n+1/2}I_{n-1/2}(\tau/2).
\]

A July 2026 theorem of D. S. P. Salazar proves strict total positivity of
`(x,s)->I_s(x)`.  This supplies a serious Darboux mechanism before theta
mixing; the common-selector composition theorem is the precise missing step.

Read
[`10_THETA_FOCK_MIXTURE_AND_QUASIFREE_GATE.md`](10_THETA_FOCK_MIXTURE_AND_QUASIFREE_GATE.md).

## 5. New leverage IV — Toeplitz sector, cubic tail, and reciprocal duality

Let

\[
 G(z)=\frac18\xi_{\rm R}\left(\frac12+\frac{\sqrt z}{2}\right)
 =\sum a_nz^n.
\]

Then

\[
 \mathfrak X(u)=8G(4u+1).
\]

A July 2026 theorem of W. Michałowski proves for the centered coefficients

\[
 D^G_{r,k}>0
 \qquad(k\ge10^{18}r^3).
\]

The same paper records the Schoenberg-sector consequence of the verified zero
height.  Conservatively, for both centered and invariant coefficients,

\[
 r\le9{,}419{,}999{,}999{,}999
 \Longrightarrow
 \text{all Toeplitz minors of order }r\text{ are nonnegative at every shift}.
\]

The cubic wedge is imported only for the centered sequence; no unproved
translation of its constant is made.

For any normalized sequence

\[
 A(z)=\sum\alpha_nz^n,
 \qquad
 B(z)=1/A(-z)=\sum\beta_nz^n,
\]

the new exact reciprocal rectangle identity is

\[
 \boxed{
 \det[\alpha_{k+j-i}]_{i,j=0}^{r-1}
 =
 \det[\beta_{r+j-i}]_{i,j=0}^{k-1}.
 }
 \tag{5.1}
\]

It is the equality of the dual and ordinary Jacobi--Trudi formulas for the
same rectangle.  Large order at fixed shift becomes fixed order at large
shift in the reciprocal, bosonic coordinate.

This does not manufacture finite-order reciprocal closure, but it opens a
second tail and makes the quasi-free endpoint literal fermion--boson Schur
positivity.

Read
[`11_TOEPLITZ_SECTOR_AND_RECIPROCAL_DUALITY.md`](11_TOEPLITZ_SECTOR_AND_RECIPROCAL_DUALITY.md).

## 6. Previous finite-height theorem retained

For

\[
 F_{n,k}(u)=(-1)^nD_u^{n+k}[u^kq(u)],
\]

the invariant atom formula and angular theorem imply:

> If RH is verified through height `H`, then `F_(n,k)(u)>0` for all `u>0`
> whenever
> 
> \[
>  \max\{k,n+1\}\arctan(1/H)<\pi/2.
> \]

Using the repository's conservative Platt--Trudgian lock `H=3*10^12`,

\[
 \boxed{
 F_{n,k}(u)>0
 \quad\text{when}\quad
 \max\{k,n+1\}\le4{,}710{,}000{,}000{,}000.
 }
\]

In particular `(EW)` is strict for every `u>0` through the same Widder order.
No simplicity assumption is used, and the external computation was not
rerun.

Read
[`08_FINITE_HEIGHT_WIDDER_CONE.md`](08_FINITE_HEIGHT_WIDDER_CONE.md).

## 7. Complete Architecture E chain

\[
 \begin{array}{c}
 \text{actual theta source }\Phi\\
 \Downarrow\\
 \mathcal A_\Phi\\
 \Updownarrow\\
 K_0\succeq0\\
 \Updownarrow\\
 \mathcal B_X\succeq0\\
 \Updownarrow\\
 \Theta_\lambda\text{ has zero negative squares}\\
 \Updownarrow\\
 q\text{ is Stieltjes}\\
 \Updownarrow\\
 \mathcal W_k(u)\ge0\quad(\forall u,k)\\
 \Updownarrow\\
 \text{one-scale count law is }PF_\infty\\
 \Updownarrow\\
 \text{one theta-built quasi-free determinant}\\
 \Updownarrow\\
 \mathrm{RH}.
 \end{array}
\]

The main remaining theorem is no longer merely “prove positivity.”  It is the
specific source operation

```text
positive theta mixture of quasi-free fibers
-> one positive trace-class contraction
```

with all exterior powers matched.  That is the primary next attack.

## 8. Frozen provenance

| Source | Frozen head / identifier | Role |
|---|---|---|
| `main` | `6dda8b5125457ed936330229f8c9eb6491728e76` | branch base |
| PR #765 | `8f01064df805624c045877655893c324a220975d` | actual-Xi companions and asymptotics |
| PR #766 | `17c7624a0bd56c5356d00278b2a846d2efdbdccc` | positive-source counterexamples |
| PR #769 | `f36576faf7853a56bd1f64edd29c4df662cae849` | ternary Segre/Chow resolution |
| PR #770 | `9421846721cd788ab01615c8b6d459d9de849df7` | source-faithfulness barriers |
| PR #781 | `ea282c4e73ecd2d8cad44587da5ffa135df67e98` | Segre, deformation and Epstein data |
| PR #783 | `1db60cddb723ea921c1cc73edaa0334b72679156` | proof review and negative index |
| PR #784 | `d6d326b21d9526d9c91b18017bf550003f8f4f9b` | source–Hermite–Stieltjes closure |
| Platt--Trudgian | `EXT.XI.PLATT_TRUDGIAN.2021` | verified height |
| Michałowski | arXiv:2607.16795 | centered cubic Toeplitz wedge |
| Salazar | arXiv:2607.02778 | strict Bessel spectral total positivity |

The two July 2026 papers are imported current literature, not claimed as
repository discoveries.

## 9. Reading order

1. [`09_INVARIANT_ORDER_PRODUCT_AND_COUNT_LAW.md`](09_INVARIANT_ORDER_PRODUCT_AND_COUNT_LAW.md)
2. [`10_THETA_FOCK_MIXTURE_AND_QUASIFREE_GATE.md`](10_THETA_FOCK_MIXTURE_AND_QUASIFREE_GATE.md)
3. [`11_TOEPLITZ_SECTOR_AND_RECIPROCAL_DUALITY.md`](11_TOEPLITZ_SECTOR_AND_RECIPROCAL_DUALITY.md)
4. [`02_SOURCE_HERMITE_STIELTJES_CLOSURE.md`](02_SOURCE_HERMITE_STIELTJES_CLOSURE.md)
5. [`03_E_WIDDER_SCALAR_ENDPOINT.md`](03_E_WIDDER_SCALAR_ENDPOINT.md)
6. [`08_FINITE_HEIGHT_WIDDER_CONE.md`](08_FINITE_HEIGHT_WIDDER_CONE.md)
7. [`01_FROZEN_SOURCE_REVIEW.md`](01_FROZEN_SOURCE_REVIEW.md)
8. [`04_FIREWALLS_AND_SCOPE.md`](04_FIREWALLS_AND_SCOPE.md)
9. [`05_IMPORTED_VS_NEW_CLAIM_LEDGER.md`](05_IMPORTED_VS_NEW_CLAIM_LEDGER.md)
10. [`06_NEXT_ATTACK.md`](06_NEXT_ATTACK.md)
11. [`07_LITERATURE_BOUNDARY.md`](07_LITERATURE_BOUNDARY.md)
12. [`VALIDATION.md`](VALIDATION.md)

## 10. Validation boundary

Three standard-library rational checkers cover:

- Widder atoms, recurrences, microscope and Loewner algebra: 217 controls;
- finite-height angular geometry: 66 controls;
- radial product, matching pole, reciprocal rectangle and Bernoulli-string
  algebra: 173 controls.

```text
combined bounded authoring controls                456
repository-wide CI                                  NOT RUN
source/Hermite/Stieltjes proofs                      REVIEW REQUIRED
radial product and count-law proofs                 REVIEW REQUIRED
theta mixture and reciprocal duality                REVIEW REQUIRED
all-order theta quasi-free gate / (EW)              OPEN / RH-EQUIVALENT
Riemann Hypothesis                                  UNPROVED
```

The checks authenticate finite algebra and indexing only.  They do not replay
external computations, prove infinite-product interchanges, establish the
source composition gate, or prove RH.
