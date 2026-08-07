# L-15133 — The finite Guinand–Weil contour biform has a canonical connected cyclic cumulant

Claim ID: `L-15133`  
Status: **PROVED FINITE CONTOUR-TENSOR CONSTRUCTION; IDENTIFICATION WITH THE DISPLAYED ONE-PROBE SCALAR IS A SEPARATE GATE**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-01  
Dependencies: Shimizu v6/v8 finite-window contour definitions; `L-15132`; finite-dimensional tensor calculus  
Scope: construct explicitly the nonlinear “universal Cauchy–Laplace coefficient object” named, but not coordinatized, in the manuscript  
Related counterexample candidates: none

## 1. Actual finite contour data

For a fixed centered window `M`, the manuscript defines:

- a logarithmic-representative space `T_(log,M)`;
- a finite contour-probe/readout space
  
  \[
  E_M=\mathfrak S_M^{\rm cfw};
  \]
- a universal contour finite-part biform
  
  \[
  \mathcal Z_M(\psi,\eta)
  =\mathsf{FP}^{\rm ct}_M
    [\mathcal M_{\rm fw}(\psi,\eta)];
  \tag{L-15133.1}
  \]
- the Moore--Penrose finite readout reconstruction
  
  \[
  \mathcal V_{R,M}^{\rm Gram}=G_M^\dagger.
  \tag{L-15133.2}
  \]

Let `E_(M,N)` be one finite readout subspace, with synthesis/logarithmic lift

\[
\Lambda_{M,N}:E_{M,N}\longrightarrow\mathcal T_{\log,M}
\tag{L-15133.3}
\]

and probe inclusion

\[
\iota_{M,N}:E_{M,N}\longrightarrow E_M.
\]

The lift is the finite LCI/seam representative used by the same readout family; it may not be replaced independently at different tensor orders.

Choose a coordinate basis `e_1,...,e_n` and define the actual finite contour seam tensor

\[
\boxed{
 B_{ab}^{M,N}
 =\mathcal Z_M
   (\Lambda_{M,N}e_b,\iota_{M,N}e_a).}
\tag{L-15133.4}
\]

Let

\[
G_{ab}^{M,N}
 =\langle U_{M,N}e_a,U_{M,N}e_b\rangle
\tag{L-15133.5}
\]

be the readout Gram and let `G^dagger` denote its Moore--Penrose inverse. Redundant readouts are allowed.

## 2. Contour tensorization

The contour finite-part biform has an ordinary tensor power

\[
\mathcal Z_M^{\otimes\ell}:
(\mathcal T_{\log,M}\otimes E_M)^{\otimes\ell}
\longrightarrow\mathbb C.
\tag{L-15133.6}
\]

Equivalently, this is the product-contour finite part

\[
(\mathsf{FP}^{\rm ct}_M)^{\otimes\ell}
\left[
 \mathcal M_{\rm fw}(\psi_1,\eta_1)
 \otimes\cdots\otimes
 \mathcal M_{\rm fw}(\psi_\ell,\eta_\ell)
\right].
\tag{L-15133.7}
\]

The common one-leg Archimedean/reference and finite-jet subtraction is applied on each factor before contraction. Since the readout is finite, no interchange of infinite sums occurs in this definition.

## 3. Cyclic Moore--Penrose coevaluation

Put `a_(ell+1)=a_1` and define the oriented cyclic coevaluation tensor

\[
\boxed{
\operatorname{coev}^{\rm cyc}_{G^\dagger,\ell}
=
\sum_{a_1,b_1,\ldots,a_\ell,b_\ell}
\prod_{j=1}^{\ell}
 (G^\dagger)_{b_j a_{j+1}}
\bigotimes_{j=1}^{\ell}(e_{a_j}\otimes e_{b_j}).}
\tag{L-15133.8}
\]

This is the quotient Hilbert-space coevaluation glued along one connected oriented cycle. It is intrinsic to `E/ker U`.

## 4. Nonlinear universal coefficient object

Define the connected order-`ell` Guinand--Weil contour coefficient by

\[
\boxed{
\mathfrak A^{\rm GW,cyc}_{\ell,M,N}
=
\left[
 \mathcal Z_M^{\otimes\ell}
 \circ(\Lambda_{M,N}\otimes\iota_{M,N})^{\otimes\ell}
\right]
\left(
 \operatorname{coev}^{\rm cyc}_{G^\dagger,\ell}
\right).}
\tag{L-15133.9}
\]

In readout coordinates,

\[
\boxed{
\mathfrak A^{\rm GW,cyc}_{\ell,M,N}
=
B_{a_1b_1}(G^\dagger)_{b_1a_2}
\cdots
B_{a_\ell b_\ell}(G^\dagger)_{b_\ell a_1}.}
\tag{L-15133.10}
\]

Repeated indices are summed. Thus the nonlinear universal object is obtained directly from the manuscript's actual contour finite-part biform by:

1. taking `ell` copies of that biform;
2. lifting every source leg through the same finite LCI/log representative;
3. closing the legs with exactly `ell` Moore--Penrose Gram coevaluations;
4. retaining the connected one-cycle contraction.

By `L-15132`,

\[
\boxed{
\mathfrak A^{\rm GW,cyc}_{\ell,M,N}
=A^{\rm sew}_{\ell,M,N}
=\operatorname{Tr}(K_{M,N}^{\ell}).}
\tag{L-15133.11}
\]

The point of the present lemma is the first equality: it realizes the sewn loop as an explicit tensor pullback of the actual contour biform, rather than merely naming a universal object.

## 5. Genuine order four

The first nontrivial even connected coefficient is

\[
\boxed{
\begin{aligned}
\mathfrak A^{\rm GW,cyc}_{4,M,N}
={}&
\sum
 B_{a_1b_1}(G^\dagger)_{b_1a_2}
 B_{a_2b_2}(G^\dagger)_{b_2a_3}\\
&\qquad\cdot
 B_{a_3b_3}(G^\dagger)_{b_3a_4}
 B_{a_4b_4}(G^\dagger)_{b_4a_1}\\
={}&\operatorname{Tr}(K_{M,N}^4).
\end{aligned}}
\tag{L-15133.12}
\]

At degree four there are also disconnected invariant contractions, for example

\[
\bigl(\operatorname{Tr}K_{M,N}^2\bigr)^2.
\]

They are not part of the logarithmic determinant coefficient. The adjective **connected** in (L-15133.9) is load bearing: the logarithm/cumulant selects one cycle, whereas an unlogged moment sums over set partitions and disjoint cycle types.

## 6. All orders and uniqueness of the connected contraction

For every `ell>=2`, the oriented one-cycle graph has one output-to-input gluing at every vertex. Once the contour biform and Hilbert coevaluation are fixed, its evaluation is uniquely (L-15133.10). Other degree-`ell` invariant contractions correspond to disjoint unions of cycles, i.e. products

\[
\prod_{C\in\pi}\operatorname{Tr}(K^{|C|})
\]

for a cycle partition `pi`. Möbius inversion on set partitions, equivalently passage from moments to connected cumulants, isolates the single-cycle coefficient.

Therefore (L-15133.9) is the unique natural coefficient satisfying all four conditions:

1. `ell`-linear in `ell` copies of the contour seam biform;
2. invariant under finite readout reparametrization and redundancy;
3. using only the Gram Hilbert structure to glue adjacent legs;
4. connected with cyclic order `1->2->...->ell->1`.

## 7. One majorant

Assume the coherent finite family satisfies

\[
\sup_{M,N}\|K_{M,N}\|_2\le C.
\tag{L-15133.13}
\]

Then

\[
\boxed{
|\mathfrak A^{\rm GW,cyc}_{\ell,M,N}|
\le C^\ell
\qquad(\ell\ge2),}
\tag{L-15133.14}
\]

and, for every `r<1/C`,

\[
\boxed{
\sum_{\ell=2}^{\infty}
|\mathfrak A^{\rm GW,cyc}_{\ell,M,N}|r^{\ell-1}
\le\frac{C^2r}{1-Cr}.}
\tag{L-15133.15}
\]

This is exactly the majorant of `L-15132`. It is now inherited by the contour-cyclic object and simultaneously justifies the readout limit, window limit, coefficient sum, and local logarithmic-derivative limit whenever the finite family is Hilbert--Schmidt coherent.

## 8. What is and is not proved

Proved:

\[
\boxed{
\text{actual contour biform}
\xrightarrow{\ \ell\text{-fold connected tensorization}\ }
\mathfrak A^{\rm GW,cyc}_{\ell,M,N}
=A^{\rm sew}_{\ell,M,N}.}
\]

Not proved here:

\[
\boxed{
A^{\rm GW,scalar}_{\ell,M}
=\mathfrak A^{\rm GW,cyc}_{\ell,M,N},}
\]

where the left side is the coefficient of the manuscript's separately displayed one-contour, fixed-probe central scalar family. That equality requires a diagonal/connected-cumulant compatibility theorem between one contour and the product-contour tensorization. `R-15110` states the exact missing identity.
