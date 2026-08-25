# L-106121 — The bilateral tensor moment has the correct source-dual weight and a paid atomic diagonal

Claim ID: `L-106121`  
Programme aliases: `LFAM1.BILATERAL_TENSOR_MOMENT`, `LFAM2.G2_ELL_RHO_DUALITY`, `STRESS.DOUBLE_CORE_PHASE_ENERGY`  
Status: **PROVED EXACT CONDITIONAL DOMINATION AND UNCONDITIONAL ATOMIC-DIAGONAL BOUND**  
Created: 2026-08-25  
Depends on: `L-106120`; parent `T-102990`; fixed Mellin polarization  
Programme issues: #743, #736, #737  
RH status: **not assumed**

Let `mathcal W` be the complete bilateral member of `L-106120`.  Define

\[
\boxed{
\begin{aligned}
 \mathfrak M_{\rm BT}(Y)
 ={1\over2\pi}
 \sum_{g}\sum_{\ell\ne\rho}g^2\ell\rho
 \sum_{\sigma,\tau=\pm1}
 \int_{\mathbb R}|\widehat\kappa(t)|^2
 \sum_{\substack{\eta(-1)=1\\\theta(-1)=1}}
 w_\ell(\eta)w_\rho(\theta)
 |\mathcal W_{g,\ell,\rho,\sigma,\tau,\eta,\theta}(t)|^2dt.
\end{aligned}
}
\tag{L-106121.1}
\]

The source-dual weight is exactly

\[
\boxed{g^2\ell\rho.}
\tag{L-106121.2}
\]

There is no external owner-product weight.  Both `P^{-1/2}` and `Q^{-1/2}`
remain inside the complete tensor member.

## 1. Conditional domination of the native current

By the tensor identity and principal recombination of `L-106120`, the positive
integrand in (L-106121.1) dominates

\[
 |\mathcal W_{g,\ell,\rho,\sigma,\tau,0,0}(t)|^2.
\]

Cauchy over `(g,ell,rho,sigma,tau)` gives the reciprocal source weight

\[
 \sum_g{1\over g^2}
 \sum_{\ell\ne\rho}{1\over\ell\rho}
 \ll (\log\log(3Y))^2.
\tag{L-106121.3}
\]

Therefore Mellin--Plancherel yields

\[
\boxed{
 \|\mathcal C_{\rm BCI}\|_{L^2(dX/X)}^2
 \ll(\log\log(3Y))^{O(1)}
 \mathfrak M_{\rm BT}(Y),
}
\tag{L-106121.4}
\]

where `mathcal C_BCI` is precisely the coprime two-sided Boolean incidence
current of parent `T-102990`, after the inherited finite carrier, endpoint,
marked-prime, shell and renewal recombinations.

Consequently

\[
\boxed{
 \mathfrak M_{\rm BT}(Y)=Y^{o(1)}
 \Longrightarrow
 \mathrm{BCI}_{102990}
 \Longrightarrow
 \mathrm{RH}.
}
\tag{L-106121.5}
\]

The last implication is the frozen parent detector/Mellin consumer.

## 2. Literal atomic diagonal

A complete source atom in `mathcal W` has coefficient

\[
 z_\omega(t)
 ={\gamma_\omega(t)\over g^2cd\sqrt{PQ}},
 \qquad
 |\gamma_\omega(t)|\le X^{o(1)}.
\tag{L-106121.6}
\]

On the atomic diagonal the moment weight gives

\[
 g^2\ell\rho|z_\omega(t)|^2
 \ll
 X^{o(1)}
 {\ell\rho\over g^2c^2d^2PQ}.
\]

Since `ell<=c` and `rho<=d`,

\[
 {\ell\rho\over c^2d^2}
 \le {1\over cd}.
\tag{L-106121.7}
\]

The finite source sums satisfy

\[
 \sum_g{1\over g^2}<\infty,
 \qquad
 \sum_{c,d\le16Y}{1\over cd}\ll(\log Y)^2,
\]

and

\[
 \sum_P{1\over P},\quad\sum_Q{1\over Q}
 \ll(\log\log(3Y))^2
\]

for squarefree semiprime owner products.  Boolean representation and shell
multiplicities are subpower, while the compact Mellin kernel has finite `L2`
norm.  Thus

\[
\boxed{
 \mathfrak M_{\rm BT}^{\rm atomic\ diagonal}(Y)=Y^{o(1)}.
}
\tag{L-106121.8}
\]

## 3. Both owner amplifiers are Wick squares

Apply `L-106112.4` separately to the anchor owner product `P` and the opposite
owner product `Q`.  Modulo the inherited repeated-prime fields, every tensor
member is built from

\[
 {1\over4}
 \mathcal P_{\psi,c}(s)^2
 \mathcal P_{\chi,d}(s)^2.
\tag{L-106121.9}
\]

Hence the four tensor channels are explicit moments of two one-prime
Dirichlet polynomials.  The only literal diagonal is already paid by
(L-106121.8); equal products and repeated owner labels remain in the inherited
closed ledger.

## Scope

The lemma proves the exact controlling moment, its implication to `BCI102990`,
and the atomic diagonal.  It does not control off-atomic correlations between
the two prime-Wick amplifiers.  Their exact double product-collision form is
`L-106122`.
