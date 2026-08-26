# L-106121 — The bilateral tensor moment has the correct source-dual weight; only its principal atomic diagonal is paid

Claim ID: `L-106121`  
Programme aliases: `LFAM1.BILATERAL_TENSOR_MOMENT`, `LFAM2.G2_ELL_RHO_DUALITY`, `STRESS.DOUBLE_CORE_PHASE_ENERGY`  
Status: **CORRECTED EXACT CONDITIONAL DOMINATION; PRINCIPAL ATOMIC BOUND PROVED; COMPLETE-MOMENT ATOMIC CLAIM RETRACTED BY `R-106131`**  
Created: 2026-08-25  
Corrected: 2026-08-25  
Depends on: `L-106120`; parent `T-102990`; fixed Mellin polarization; `R-106131`  
Programme issues: #743, #736, #737  
RH status: **not assumed**

Let `mathcal W` be the complete bilateral member of `L-106120`. The full
positive tensor moment is

\[
\begin{aligned}
\mathfrak M_{\rm BT}(Y)
={1\over2\pi}
\sum_g\sum_{\ell\ne\rho}g^2\ell\rho
\sum_{\sigma,\tau}
\int_{\mathbb R}|\widehat\kappa(t)|^2
\sum_{\eta,\theta}
w_\ell(\eta)w_\rho(\theta)
|\mathcal W_{\eta,\theta}(t)|^2dt.
\end{aligned}
\tag{L-106121.1}
\]

The external source-dual weight is exactly

\[
\boxed{g^2\ell\rho.}
\tag{L-106121.2}
\]

Both owner coefficients remain inside the complete tensor member.

## 1. Conditional domination remains exact

The principal--principal member is the native unphased member up to fixed
quadratic-class signs. Since

\[
c_q=\frac{q+1}{q-1}>1,
\]

the principal channel alone satisfies

\[
g^2\ell\rho
|\mathcal W_{0,0}(t)|^2
\le
g^2\ell\rho c_\ell c_\rho
|\mathcal W_{\mathbf1,\mathbf1}(t)|^2.
\tag{L-106121.3}
\]

Cauchy over `(g,ell,rho,sigma,tau)` has reciprocal source weight

\[
\sum_g\frac1{g^2}
\sum_{\ell\ne\rho}\frac1{\ell\rho}
\ll(\log\log(3Y))^2.
\tag{L-106121.4}
\]

Therefore the principal--principal moment

\[
\boxed{
\begin{aligned}
\mathfrak P_{\rm PP}(Y)
={1\over2\pi}
\sum_g\sum_{\ell\ne\rho}g^2\ell\rho c_\ell c_\rho
\sum_{\sigma,\tau}
\int|\widehat\kappa(t)|^2
|\mathcal W_{\mathbf1,\mathbf1}(t)|^2dt
\end{aligned}
}
\tag{L-106121.5}
\]

already gives

\[
\boxed{
\mathfrak P_{\rm PP}(Y)=Y^{o(1)}
\Longrightarrow
\mathrm{BCI}_{102990}
\Longrightarrow
\mathrm{RH}.
}
\tag{L-106121.6}
\]

The mixed and double nonprincipal positive moments are not required for this
implication.

## 2. Binding atomic correction

A complete source atom has coefficient

\[
z_\omega(t)
=
\frac{\gamma_\omega(t)}
{g^2cd\sqrt{PQ}},
\qquad
|\gamma_\omega(t)|\le X^{o(1)}.
\tag{L-106121.7}
\]

The total weight of all tensor character channels is

\[
(\ell-1)(\rho-1).
\]

Hence the atomic diagonal of the **complete** moment (L-106121.1) is

\[
\boxed{
g^2\ell\rho(\ell-1)(\rho-1)|z_\omega(t)|^2.
}
\tag{L-106121.8}
\]

The first version omitted `(ell-1)(rho-1)`.

For the principal--principal channel, however, the atomic coefficient is only

\[
g^2\ell\rho c_\ell c_\rho|z_\omega(t)|^2.
\]

Since `c_ell c_rho<=4`, `ell<=c`, and `rho<=d`,

\[
g^2\ell\rho c_\ell c_\rho|z_\omega(t)|^2
\ll
X^{o(1)}
\frac1{g^2cdPQ}.
\]

The source sums are polylogarithmic/subpower, giving

\[
\boxed{
\mathfrak D_{\rm PP}(Y)=Y^{o(1)}.
}
\tag{L-106121.9}
\]

The uncentered mixed and double nonprincipal atomic traces are not paid by this
argument.

## 3. Both owner amplifiers remain exact Wick squares

Applying `L-106112.5` on both source sides gives, modulo inherited repeated
owner labels,

\[
\boxed{
\frac14
\mathcal P_{\psi,c}(s)^2
\mathcal P_{\chi,d}(s)^2.
}
\tag{L-106121.10}
\]

This factorization survives unchanged. `R-106122` remains binding: after the
character square, the collision coordinates are the complete physical
squareclasses `Pc^2` and `Qd^2`.

## Correct scope

```text
bilateral source/tensor identity                 PROVED EXACT
source-dual conditional domination               PROVED EXACT
principal--principal atomic diagonal              PROVED SUBPOWER
complete M_BT atomic diagonal                    NOT PROVED
mixed/double uncentered atomic traces             DIMENSION-BEARING
owner Wick factorization                         PROVED EXACT
```

The atomic-free four-channel identity is `L-106131`. The preferred repaired
conjunction is `T-106140`.
