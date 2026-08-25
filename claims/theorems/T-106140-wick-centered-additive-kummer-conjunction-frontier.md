# T-106140 — Wick-centered additive and Kummer defects jointly recover the principal Boolean incidence current

Claim ID: `T-106140`  
Programme aliases: `LFAM1.WICK_CENTERED_CONJUNCTION`, `LFAM2.ADDITIVE_KUMMER_TRACE_DIFFERENCE`, `STRESS.CVXD_LFAMILY_REPAIR`  
Status: **CONSOLIDATED CORRECTED IMPLICATION MATRIX; TWO SIGNED GLOBAL ESTIMATES OPEN**  
Created: 2026-08-25  
Depends on: parent `T-102990`; `L-106120--L-106121`; `R-106122--R-106123`; binding `R-106131`; canonical Wick lemma `L-106131`; `L-106132`; connected lemma `L-106190`; source-dual rewrite `L-106191`  
Parent scientific source: PR #719 head `ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc`  
Programme issues: #743, #736, #737  
RH status: **unproved**

The bilateral Kummer family is source-exact, but its complete positive moment
charges the literal atomic diagonal once for every phase and character.
`R-106131` corrects that normalization.

This theorem removes the atomic conductor dimension exactly and expresses the
principal--principal Boolean incidence moment as the difference of

1. a Wick-centered additive/CV-XD trace;
2. a Wick-centered nonprincipal Kummer/L-family trace.

Only their conjunction recovers the principal current. `L-106191` gives an
exact bounded-kernel coordinate for the additive trace, while also recording
why that coordinate is not a source-blind free-energy estimate.

## 1. Complete bilateral fibres

Retain the notation of `L-106120`. A complete fibre is indexed by

\[
 \iota=(g,\ell,\rho,\sigma,\tau),
 \qquad \ell\ne\rho,
\]

and contains literal source atoms `omega` with coefficients
`z_(iota,omega)(t)`. Put

\[
 D_\iota(t)=\sum_\omega|z_{\iota,\omega}(t)|^2.
\tag{T-106140.1}
\]

Let `W_(iota;h,k)` be the complete additive members for
`1<=h<ell`, `1<=k<rho`, and let `W_(iota;eta,theta)` be the even-character
members of the tensor Gauss transform. All Boolean, owner, common-core,
physical-shell, carrier, endpoint-colour, marked-67 and renewal labels remain
inside these members.

Write

\[
 c_q={q+1\over q-1}.
\tag{T-106140.2}
\]

The principal character member equals the native unphased member up to fixed
quadratic-class signs, so its squared modulus is unchanged.

## 2. Wick-centered additive trace

Define

\[
\boxed{
\begin{aligned}
 \mathfrak A^\circ(Y)
 ={1\over2\pi}\sum_\iota g^2\ell\rho
 \int_{\mathbb R}|\widehat\kappa(t)|^2
 \Bigg[&\sum_{h=1}^{\ell-1}\sum_{k=1}^{\rho-1}
 |\mathcal W_{\iota;h,k}(t)|^2\\
 &-(\ell-1)(\rho-1)D_\iota(t)\Bigg]dt.
\end{aligned}
}
\tag{T-106140.3}
\]

This is a real signed scalar. The conductor sum is performed before the outer
absolute value.

For `c=ell u`, `d=rho v`, `L-106191` sets

\[
 \widetilde z_\omega=g\ell\rho z_\omega
 ={\gamma_\omega\over guv\sqrt{PQ}}
\]

and proves that every fibre in (T-106140.3) is exactly

\[
\boxed{
\sum_{\omega\ne\omega'}
 \widetilde z_\omega\overline{\widetilde z_{\omega'}}
 \left(\mathbf1_{x_\omega=x_{\omega'}}-{1\over\ell}\right)
 \left(\mathbf1_{y_\omega=y_{\omega'}}-{1\over\rho}\right).
}
\tag{T-106140.4}
\]

The two centered incidence factors have modulus at most one and the literal
atomic diagonal is absent coefficientwise. However, the rescaled coefficient
has no least-prime decay when `u=v=1`; therefore (T-106140.4) still requires a
coherent global conductor-family estimate. A source-blind Schur bound is
forbidden by `R-106123`.

Let `mathfrak C_SD(Y)` denote the complete global recombination of
(T-106140.4). Then

\[
\boxed{
 \mathfrak C_{\rm SD}(Y)=\mathfrak A^\circ(Y).
}
\tag{T-106140.5}
\]

Thus `WCCORR106191` is an exact equivalent coordinate for `WCADD106140`.
`L-106191` also records the stronger diagnostic split into equal-output and
distinct-output correlations; neither part is currently proved subpower.

## 3. Wick-centered Kummer defect

Define

\[
\boxed{
\begin{aligned}
 \mathfrak K^\circ(Y)
 ={1\over2\pi}\sum_\iota g^2\ell\rho
 \int_{\mathbb R}|\widehat\kappa(t)|^2
 \sum_{\substack{\eta(-1)=1,\ \theta(-1)=1\\
 (\eta,\theta)\ne(\mathbf1,\mathbf1)}}
 w_\ell(\eta)w_\rho(\theta)
 \left[|\mathcal W_{\iota;\eta,\theta}(t)|^2-D_\iota(t)\right]dt.
\end{aligned}
}
\tag{T-106140.6}
\]

It contains the two mixed and the double nonprincipal channels, each normal
ordered before their sum.

By `R-106122`, its strict collision coordinates are the complete physical
squareclasses

\[
 Pc^2\equiv\pm P'c'^2\pmod\rho,
 \qquad Qd^2\equiv\pm Q'd'^2\pmod\ell,
\]

not owner products alone. By `L-106126`, each fixed owner-class component is
supported on two or four linear core lines. The centered constant backgrounds
in the nonprincipal kernels remain present.

## 4. Principal off-atomic trace and exact identity

Define

\[
\boxed{
\begin{aligned}
 \mathfrak P^\circ(Y)
 ={1\over2\pi}\sum_\iota g^2\ell\rho c_\ell c_\rho
 \int_{\mathbb R}|\widehat\kappa(t)|^2
 \left[|\mathcal W_{\iota;\mathbf1,\mathbf1}(t)|^2-D_\iota(t)\right]dt.
\end{aligned}
}
\tag{T-106140.7}
\]

The exact tensor operator identity `L-106131.15` gives fibrewise and globally

\[
\boxed{
 \mathfrak A^\circ(Y)=\mathfrak P^\circ(Y)+\mathfrak K^\circ(Y).
}
\tag{T-106140.8}
\]

This is compatible with `L-106190`: that lemma extracts the principal member
by retaining one-coordinate and joint collision ledgers in signed
inclusion--exclusion; (T-106140.8) extracts it by subtracting the
Wick-centered nonprincipal family defect from the complete normal-ordered
additive frame.

## 5. The principal atomic diagonal is paid

Put

\[
\boxed{
 \mathfrak D_{\rm PP}(Y)
 ={1\over2\pi}\sum_\iota g^2\ell\rho c_\ell c_\rho
 \int_{\mathbb R}|\widehat\kappa(t)|^2D_\iota(t)dt.
}
\tag{T-106140.9}
\]

Since `c_ell c_rho<=4`, the corrected principal-only source summation gives

\[
\boxed{
 \mathfrak D_{\rm PP}(Y)=Y^{o(1)}.
}
\tag{T-106140.10}
\]

The full principal moment is

\[
 \mathfrak P_{\rm PP}(Y)
 =\mathfrak D_{\rm PP}(Y)+\mathfrak P^\circ(Y)\ge0.
\tag{T-106140.11}
\]

Combining (T-106140.8)--(T-106140.11),

\[
\boxed{
 \mathfrak P_{\rm PP}(Y)
 \le Y^{o(1)}+|\mathfrak A^\circ(Y)|+|\mathfrak K^\circ(Y)|.
}
\tag{T-106140.12}
\]

## 6. The two repaired gates

Define

```text
WCADD106140:
  after the complete source-dual conductor recombination,

      |A^circ(Y)| = Y^o(1).

WCKUM106140:
  after all mixed and double nonprincipal channels are normal ordered and
  globally recombined,

      |K^circ(Y)| = Y^o(1).
```

The exact additive equivalent is

\[
\boxed{
 \mathrm{WCCORR}_{106191}
 \Longleftrightarrow\mathrm{WCADD}_{106140}.
}
\tag{T-106140.13}
\]

The intended mechanisms remain distinct:

```text
WCADD106140 / WCCORR106191:
  centered additive/divisor transport;
  CV/XD physical geometry;
  Boolean half-source cutoff differences;
  coherent least-prime conductor assembly.

WCKUM106140:
  even-character L-family moments;
  physical Kummer collision lines and centered constant backgrounds;
  function-field Frobenius/trace input;
  hybrid large sieve or relative trace formula.
```

Neither gate is proved.

## 7. Exact conclusion chain

Since `c_ell c_rho>1`, `mathfrak P_PP` dominates the source-dual square of the
native unphased bilateral member. Therefore

\[
\boxed{
\begin{aligned}
 \mathrm{WCCORR}_{106191}\wedge\mathrm{WCKUM}_{106140}
 &\Longleftrightarrow
 \mathrm{WCADD}_{106140}\wedge\mathrm{WCKUM}_{106140}\\
 &\Longrightarrow\mathfrak P_{\rm PP}(Y)=Y^{o(1)}\\
 &\Longrightarrow\mathfrak M_{\rm CK}(Y)=Y^{o(1)}\\
 &\Longrightarrow\mathrm{BCI}_{102990}\\
 &\Longrightarrow\mathrm{RH}.
\end{aligned}
}
\tag{T-106140.14}
\]

This is a genuine two-statement conjunction. The additive trace alone contains
the principal mode plus the Kummer fluctuation; the Kummer trace alone has zero
principal mode. Their difference isolates the conclusion member.

## 8. Relation to the other live frontiers

```text
T-106130:
  minimal direct connected-principal gate CBKM106130.

T-106140:
  stronger complete-family route through WCCORR/WCADD and WCKUM.

T-106150:
  independent same-half-source Wick/ordinary reflection route through
  WKSFSC106150, SFSC106150, or the equivalent ordinary REFSIG106150 gate.
```

No equivalence between these frontiers is asserted. The older uncentered mixed
and double positive moments remain overstrong and are not required for
(T-106140.14).

## 9. Required source discipline

The following operations are forbidden:

```text
take absolute values separately for each conductor fibre;
discard a centered negative background of a nonprincipal kernel;
replace Pc^2 by P or by c^2;
subtract one global atomic number after character fibres were collapsed;
count the principal atomic diagonal again in a nonprincipal channel;
apply a source-blind free-energy bound to the rescaled atoms of L-106191;
replace the analytic Wick square of T-106150 by a positive modulus square;
infer WCADD, WCCORR or WCKUM from a finite replay.
```

## Exact boundary

```text
complete bilateral source/tensor identity          PROVED EXACT
Gauss atomic phase cardinality                     CORRECTED EXACT
principal atomic diagonal                          PROVED SUBPOWER
Wick-centered four-channel identity                PROVED EXACT
connected Kummer-Möbius identity L-106190          PROVED EXACT
source-dual centered correlation L-106191          PROVED EXACT

WCCORR106191 = WCADD106140                         OPEN / RH-BEARING WITH WCKUM
WCEQ106191 / WCDIST106191 diagnostics              OPEN
WCKUM106140                                        OPEN / RH-BEARING
WKSFSC/SFSC/REFSIG106150                           OPEN / RH-BEARING
BCI102990                                          OPEN / RH-BEARING
Riemann Hypothesis                                 UNPROVED
```
