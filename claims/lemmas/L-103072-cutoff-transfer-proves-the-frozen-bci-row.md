# L-103072 — Exact cutoff transfer proves the frozen BCI row

Claim ID: `L-103072`  
Status: **PROVED COMPLETE BCI REDUCTION ON THE FROZEN SOURCE STACK**  
Created: 2026-08-26  
Depends on: `L-102951--L-102954`, `L-103070--L-103071`; `T-102990`  
RH status: **not assumed in the proof**

For any cutoff `U`, write the exact Boolean Vaughan identity as

\[
\mu_{\rm sf}
=
\mathcal T_U+\mathcal B_U,
\tag{L-103072.1}
\]

where

\[
\mathcal T_U
=
2\mu_U-\mu_U\star\mu_U\star\mathbf1_{\rm sf},
\]

and

\[
\mathcal B_U
=
a_U\star a_U\star\mu_{\rm sf}.
\]

The identity is coefficientwise on the finite squarefree Euler algebra and
survives every fixed linear owner, completion, equal-pair, shell and physical
observation functor.

## 1. Exact transfer between two cutoffs

For any two cutoffs `U,V`, subtracting (L-103072.1) gives

\[
\boxed{
\mathcal B_U-\mathcal B_V
=
\mathcal T_V-\mathcal T_U.
}
\tag{L-103072.2}
\]

No approximation, asymptotic expansion or source-mass comparison occurs.

## 2. Block-dependent quarter-power cutoff

On the dyadic physical block `Y<=X<2Y`, let `Pi_A` be the source projection
onto canonical owner products

\[
A\le P<2A.
\]

Let `U_0` be the historical sixth-root cutoff frozen in `T-102990`, and put

\[
V_A=\left\lfloor(2Y/A)^{1/4}\right\rfloor.
\]

The owner blocks are disjoint. The cutoff is fixed on each block before the
physical observation. The canonical equal-pair completion functor and `Pi_A`
are linear, so (L-103072.2) gives the exact source identity

\[
\boxed{
\Pi_A\mathfrak B_{U_0}^{\rm eq}
=
\Pi_A\mathfrak B_{V_A}^{\rm eq}
+
\Pi_A\mathfrak T_{V_A}^{\rm eq}
-
\Pi_A\mathfrak T_{U_0}^{\rm eq}.
}
\tag{L-103072.3}
\]

`L-103071` proves that the physical observation of the first term on the
right vanishes identically. Therefore

\[
\boxed{
\mathcal O_{K_L}[\Pi_A\mathfrak B_{U_0}^{\rm eq}]
=
\mathcal O_{K_L}[\Pi_A\mathfrak T_{V_A}^{\rm eq}]
-
\mathcal O_{K_L}[\Pi_A\mathfrak T_{U_0}^{\rm eq}].
}
\tag{L-103072.4}
\]

The second term is power-saving by `L-102953`. The first term is subpower by
`L-103070`. Summing the `O(log Y)` owner blocks and the inherited
polylogarithmic equal-pair collapse gives

\[
\boxed{
\int_Y^{2Y}
\left(
\mathcal O_{K_L}[\mathfrak B_{U_0}^{\rm eq}](X)
\right)_-
\frac{dX}{X}
=
Y^{o(1)}.
}
\tag{L-103072.5}
\]

All equal-product, repeated-label, squared-activity, marked-prime and finite
terminal fields remain in the inherited closed ledger.

## 3. BCI

`T-102990` defines `BCI102990` as precisely the carrier-recombined physical
orientation of the coprime two-sided part of the historical balanced row.
Equation (L-103072.5) controls the complete historical balanced row before its
closed equal-, one-sided- and common-core strata are removed. It therefore
implies the narrower statement:

\[
\boxed{\mathrm{BCI}_{102990}.}
\tag{L-103072.6}
\]

The former incidence, Kummer, Plücker and reflection frontiers become optional
coordinate descriptions of a row already controlled by cutoff transfer.

## 4. Direct harmonic-source closure

The same argument may be read without reference to the historical cutoff.
On each owner block,

\[
\mu_{\rm sf}=\mathcal T_{V_A}+\mathcal B_{V_A},
\]

and `L-103071` gives

\[
\mathcal O_{K_L}[\Pi_A\mathcal B_{V_A}^{\rm eq}]=0.
\]

Therefore

\[
\boxed{
\mathcal O_{K_L}[\Pi_A\mu_{\rm sf}]
=
\mathcal O_{K_L}[\Pi_A\mathcal T_{V_A}^{\rm eq}].
}
\tag{L-103072.7}
\]

Summing the owner blocks and restoring the already-closed squared Hodge ideal
shows directly that the full carrier-recombined harmonic derivative observation has subpower
logarithmic absolute mass. The frozen Mellin--Landau consumer may therefore be
fed without passing through any intermediate incidence or Kummer criterion.
