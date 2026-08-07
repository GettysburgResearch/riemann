# Guinand–Weil contour cyclic interface: construction, order four, and the exact remaining diagonal identity

Agent: `gpt56-04-f`  
Date: 2026-08-01  
Primary PR: #158  
Status: no proof of RH claimed

## Executive result

I reconstructed the finite source types from Shimizu v6/v8 and replaced the manuscript's unnamed “universal Cauchy–Laplace coefficient object” by an explicit one.

The actual finite-window contour rule is the biform

\[
\mathcal Z_M(\psi,\eta)
=\mathsf{FP}^{\rm ct}_M
 [\mathcal M_{\rm fw}(\psi,\eta)].
\]

Tensorize this biform `ell` times, insert the manuscript's Moore--Penrose readout reconstruction at every adjacent gluing, and contract along one connected oriented cycle. The result is

\[
\mathfrak A^{\rm GW,cyc}_{\ell,M,N}
=B_{a_1b_1}(G^\dagger)_{b_1a_2}
\cdots
B_{a_\ell b_\ell}(G^\dagger)_{b_\ell a_1}.
\]

This is an actual pullback of the finite contour biform, not an operator-side definition with a contour label attached. It equals the sewn coefficient and `Tr(K_(M,N)^ell)`.

At the first nontrivial even order,

\[
\mathfrak A^{\rm GW,cyc}_{4,M,N}
=B G^\dagger B G^\dagger B G^\dagger B G^\dagger
\]

with cyclic index contraction. Disconnected degree-four contractions such as `(Tr K^2)^2` are excluded because the logarithm selects the connected one-cycle cumulant.

## Actual-manuscript audit

The accessible manuscript defines separately:

1. the contour finite-part biform and coordinate functional;
2. a fixed classical Guinand--Weil probe;
3. a central one-contour Cauchy--Laplace family;
4. finite cyclic tensor tests.

It explicitly says that scalar central tests and cyclic tensor tests are not elements of the same space, and claims that both arise by pullback from a universal coefficient object. I found no displayed construction of the nonlinear object or of the two pullback maps.

The construction in `L-15133` supplies the cyclic pullback. The remaining scalar pullback is the finite identity

\[
\mathsf{FP}^{\rm ct}_M
 [\mathcal M_{\rm fw}(\psi_{\ell-1,M},\eta_M^{\rm fp})]
=
(\mathsf{FP}^{\rm ct}_M)^{\otimes\ell}
 [\mathcal M_{\rm fw}^{\otimes\ell}
  ((\Lambda\otimes\iota)^{\otimes\ell}
   \operatorname{coev}^{\rm cyc}_{G^\dagger,\ell})].
\]

The left side is a one-contour coefficient. The right side is a connected product-contour coefficient. A proof must construct the cyclic diagonal map and show that the common finite-jet counterterm produces no residual diagonal contact term.

## Exact order-four defect

Define

\[
\Delta^{\rm CL}_{4,M,N}
=A^{\rm GW,scalar}_{4,M}
-\mathfrak A^{\rm GW,cyc}_{4,M,N}.
\]

The order-four source theorem is exactly `Delta=0`. The all-orders source theorem is `Delta_(ell,M,N)=0` for every `ell>=2`.

The contour biform and Gram do not determine the separately chosen central Taylor vector. In dimension one, keep `G=B=1` and the biform `Z(psi,eta)=psi eta` fixed. Central families `Psi_w=c w^3` have identical one-copy contour/readout data and all lower coefficients, while their order-four scalar coefficient is the arbitrary number `c`; the cyclic coefficient remains one. Thus a diagonal/cumulant relation is additional mathematical data.

## Majorant

If

\[
\sup_{M,N}\|K_{M,N}\|_2\le C,
\]

then

\[
|\mathfrak A^{\rm GW,cyc}_{\ell,M,N}|\le C^\ell
\]

and, for `r<1/C`,

\[
\sum_{\ell\ge2}
|\mathfrak A^{\rm GW,cyc}_{\ell,M,N}|r^{\ell-1}
\le\frac{C^2r}{1-Cr}.
\]

Once the finite diagonal identity is proved, this same bound automatically transfers to the actual scalar coefficients and justifies every readout/window/series limit. There is no separate analytic-limit obstruction.

## Exact control

`X-15115` verifies:

```text
connected order four      1666/81
disconnected order four   2116/81
majorant at C=3,r=1/6     3
basis invariance           PASS
11 adversarial tests       PASS
proof digest
de435821c005892e8903edf4c1e964cc9e3d7414d01eae66fbef99fd0ee7af1c
```

This is a finite source-tensor regression, not a zeta computation.

## Classification

Completed:

- explicit nonlinear universal contour coefficient object;
- genuine order-four connected arithmetic pullback;
- all-orders cyclic tensorization;
- Moore--Penrose readout invariance;
- one common Hilbert--Schmidt majorant.

Open:

- the one-contour/product-contour cyclic diagonal identity for the manuscript's actual central source family;
- cancellation of its diagonal contact/counterterm defect.

That finite source identity is the sole remaining equality between the displayed classical Guinand--Weil coefficient and the sewn determinant coefficient. Its complete even hierarchy is RH-bearing.
