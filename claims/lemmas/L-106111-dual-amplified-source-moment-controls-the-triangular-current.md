# L-106111 — The dual-amplified source moment controls the least-discrepancy current

Claim ID: `L-106111`  
Programme aliases: `LFAM1.DUAL_AMPLIFIED_MOMENT`, `LFAM2.SOURCE_DUAL_G_ELL_WEIGHT`, `STRESS.LEAST_DISCREPANCY_PLANCHEREL`  
Status: **PROVED EXACT MELLIN--GAUSS NORMAL FORM AND CONDITIONAL DOMINATION**  
Created: 2026-08-25  
Depends on: `L-106093`; `L-106110`; parent `L-102956--L-102959`, `T-102990`  
Programme issues: #743, #736, #737  
RH status: **not assumed**

Let `kappa` be the fixed compact logarithmic observation kernel used in the
parent Boolean incidence frontier.  The exact Mellin polarization of
`L-106093`, followed by the complete opposite-owner amplification of
`L-106110`, writes the coprime two-sided least-discrepancy current on one
dyadic horizon as

\[
 \mathcal C_{\rm LDRT}
 =-{2\over2\pi}\operatorname{Re}
 \sum_{g,\ell}\sum_{\sigma=\pm1}
 \int_{\mathbb R}
 |\widehat\kappa(t)|^2
 \mathcal Z_{g,\ell,\sigma,0}(t)\,dt.
\tag{L-106111.1}
\]

All shell cutoffs and source-incidence masks are retained inside
`mathcal Z`; (L-106111.1) is a finite identity on every horizon.

## 1. Natural source-dual moment

Define

\[
\boxed{
\begin{aligned}
 \mathfrak M_{\rm DA}(Y)
 ={1\over2\pi}
 \sum_{g,\ell}g^2\ell
 \sum_{\sigma=\pm1}
 \int_{\mathbb R}|\widehat\kappa(t)|^2
 \Bigg[&
 {\ell+1\over\ell-1}
 |\mathcal Z_{g,\ell,\sigma,1}(t)|^2\\
 &+{2\ell\over\ell-1}
 \sum_{\substack{\eta(-1)=1\\\eta\ne1}}
 |\mathcal Z_{g,\ell,\sigma,\eta}(t)|^2
 \Bigg]dt.
\end{aligned}
}
\tag{L-106111.2}
\]

The weight is exactly

\[
 \boxed{g^2\ell.}
\tag{L-106111.3}
\]

It is dual to the common-square coefficient `g^{-2}` and the selected literal
core-prime coefficient carried by the least-discrepancy anchor.  There is no
external `Q`: every opposite-owner coefficient remains inside the complete
family member.

## 2. Principal domination

By (L-106110.3)--(L-106110.5), the bracket in (L-106111.2) is exactly the
nonzero additive-phase energy and dominates

\[
 |\mathcal Z_{g,\ell,\sigma,0}(t)|^2.
\]

Cauchy in the finite index set `(g,ell,sigma)` gives

\[
\begin{aligned}
 \left|
 \sum_{g,\ell,\sigma}
 \mathcal Z_{g,\ell,\sigma,0}(t)
 \right|^2
 &\le
 \left(
 2\sum_{g,\ell}{1\over g^2\ell}
 \right)
 \sum_{g,\ell,\sigma}
 g^2\ell
 |\mathcal Z_{g,\ell,\sigma,0}(t)|^2.
\end{aligned}
\tag{L-106111.4}

On a physical horizon,

\[
 \sum_g{1\over g^2}<\infty,
 \qquad
 \sum_{\ell\le16Y}{1\over\ell}\ll\log\log(3Y).
\]

Hence Mellin--Plancherel and (L-106111.4) yield

\[
\boxed{
 \|\mathcal C_{\rm LDRT}\|_{L^2(dX/X)}^2
 \ll (\log\log(3Y))^{O(1)}
 \mathfrak M_{\rm DA}(Y).
}
\tag{L-106111.5}
\]

The same estimate holds after every finite/polylogarithmic carrier, shell,
marked-prime and renewal recombination inherited from the parent.

## 3. Conclusion-facing negative mass

On one dyadic interval, Cauchy in logarithmic scale gives

\[
 \int_Y^{2Y}(\mathcal C_{\rm LDRT}(X))_-{dX\over X}
 \le (\log2)^{1/2}
 \|\mathcal C_{\rm LDRT}\|_{L^2(dX/X)}.
\]

Therefore

\[
\boxed{
 \mathfrak M_{\rm DA}(Y)=Y^{o(1)}
 \quad\Longrightarrow\quad
 \text{the least-discrepancy coprime two-sided current has subpower
 logarithmic negative mass.}
}
\tag{L-106111.6}
\]

By the exact incidence partition of `L-106090` and the inherited closed
Boolean sectors, this implies `BCI102990`.

## 4. Genuine conjunction

Because (L-106111.2) is a positive decomposition, define

```text
DAPRIN106111:
  its complete dual-amplified principal/quadratic-root contribution is Y^o(1);

DAFAM106111:
  its complete dual-amplified nonprincipal even-character contribution is
  Y^o(1).
```

Then

\[
\boxed{
 \mathrm{DAPRIN}_{106111}
 \wedge
 \mathrm{DAFAM}_{106111}
 \Longrightarrow
 \mathfrak M_{\rm DA}(Y)=Y^{o(1)}
 \Longrightarrow
 \mathrm{BCI}_{102990}.
}
\tag{L-106111.7}

Neither premise is proved here.  The atomic diagonal and the exact
semiprime-owner factorization are treated in `L-106112--L-106113`.
