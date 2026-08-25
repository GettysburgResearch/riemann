# T-106140 — Wick-centered additive and Kummer defects jointly recover the principal Boolean incidence current

Claim ID: `T-106140`  
Programme aliases: `LFAM1.WICK_CENTERED_CONJUNCTION`, `LFAM2.ADDITIVE_KUMMER_TRACE_DIFFERENCE`, `STRESS.CVXD_LFAMILY_REPAIR`  
Status: **EXACT CORRECTED IMPLICATION MATRIX; TWO SIGNED GLOBAL ESTIMATES OPEN**  
Created: 2026-08-25  
Depends on: parent `T-102990`; `L-106120--L-106121`; `R-106122--R-106123`; `R-106131`; `L-106131--L-106132`  
Programme issues: #743, #736, #737  
RH status: **unproved**

The bilateral Kummer family is source-exact, but its complete positive moment
charges the literal atomic diagonal once for every phase and character.
`R-106131` corrects that normalization.

The present theorem gives a full repair of the implication architecture. It
removes the atomic conductor dimension exactly and expresses the
principal--principal Boolean incidence moment as the difference of:

1. a Wick-centered additive/CV-XD trace;
2. a Wick-centered nonprincipal Kummer/L-family trace.

These are genuinely different source measurements. Only their conjunction
recovers the principal current.

## 1. Complete bilateral fibres

Retain the notation of `L-106120`. A complete fibre is indexed by

\[
\iota=(g,\ell,\rho,\sigma,\tau),
\qquad
\ell\ne\rho,
\]

and contains literal source atoms `omega` with coefficients
`z_(iota,omega)(t)`. Put

\[
D_\iota(t)
=
\sum_\omega
|z_{\iota,\omega}(t)|^2.
\tag{T-106140.1}
\]

Let

\[
\mathcal W_{\iota;h,k}(t),
\qquad
1\le h<\ell,\quad1\le k<\rho,
\]

be the complete additive members, and let

\[
\mathcal W_{\iota;\eta,\theta}(t)
\]

be the even-character members of the tensor Gauss transform. All Boolean,
owner, common-core, physical-shell, carrier, endpoint-colour, marked-67 and
renewal labels remain inside these members.

Write

\[
c_q=\frac{q+1}{q-1}.
\tag{T-106140.2}
\]

The principal character member equals the native unphased member up to the
fixed quadratic-class signs, so its squared modulus is unchanged.

## 2. Wick-centered additive trace

Define the source-dual, normal-ordered additive scalar

\[
\boxed{
\begin{aligned}
\mathfrak A^\circ(Y)
={1\over2\pi}
\sum_\iota g^2\ell\rho
\int_{\mathbb R}
|\widehat\kappa(t)|^2
\Bigg[
&\sum_{h=1}^{\ell-1}
 \sum_{k=1}^{\rho-1}
 |\mathcal W_{\iota;h,k}(t)|^2\\
&-(\ell-1)(\rho-1)D_\iota(t)
\Bigg]dt.
\end{aligned}
}
\tag{T-106140.3}
\]

This is a real signed scalar. Its expanded kernel is the atomic-free
two-prime centered divisor kernel on the literal physical squareclasses.

The sum over all conductor fibres is taken before the outer absolute value in
the gate below.

## 3. Wick-centered Kummer defect

Define

\[
\boxed{
\begin{aligned}
\mathfrak K^\circ(Y)
={1\over2\pi}
\sum_\iota g^2\ell\rho
\int_{\mathbb R}
|\widehat\kappa(t)|^2
\sum_{\substack{\eta(-1)=1,\ \theta(-1)=1\\
                 (\eta,\theta)\ne(\mathbf1,\mathbf1)}}
w_\ell(\eta)w_\rho(\theta)
\left[
|\mathcal W_{\iota;\eta,\theta}(t)|^2
-D_\iota(t)
\right]dt .
\end{aligned}
}
\tag{T-106140.4}
\]

It contains the two mixed and the double nonprincipal channels, each normal
ordered before their sum.

By `R-106122`, its strict collision coordinates are the complete physical
squareclasses

\[
Pc^2\equiv\pm P'c'^2\pmod\rho,
\qquad
Qd^2\equiv\pm Q'd'^2\pmod\ell,
\]

not owner products alone. By `L-106126`, each fixed owner-class component is
supported on two or four linear core lines. The centered constant backgrounds
in the nonprincipal kernels remain present.

## 4. Principal off-atomic trace

Define

\[
\boxed{
\begin{aligned}
\mathfrak P^\circ(Y)
={1\over2\pi}
\sum_\iota g^2\ell\rho\,c_\ell c_\rho
\int_{\mathbb R}
|\widehat\kappa(t)|^2
\left[
|\mathcal W_{\iota;\mathbf1,\mathbf1}(t)|^2
-D_\iota(t)
\right]dt.
\end{aligned}
}
\tag{T-106140.5}
\]

The exact tensor operator identity `L-106131.15` gives, fibre by fibre and
therefore globally,

\[
\boxed{
\mathfrak A^\circ(Y)
=
\mathfrak P^\circ(Y)
+
\mathfrak K^\circ(Y).
}
\tag{T-106140.6}
\]

No inequality or asymptotic statement enters this equation.

## 5. The principal atomic diagonal is paid

Put

\[
\boxed{
\begin{aligned}
\mathfrak D_{\rm PP}(Y)
={1\over2\pi}
\sum_\iota g^2\ell\rho\,c_\ell c_\rho
\int_{\mathbb R}
|\widehat\kappa(t)|^2D_\iota(t)\,dt .
\end{aligned}
}
\tag{T-106140.7}
\]

Since `c_ell c_rho<=4`, the source summation in the corrected
principal-only part of `L-106121` gives

\[
\boxed{
\mathfrak D_{\rm PP}(Y)=Y^{o(1)}.
}
\tag{T-106140.8}
\]

The full principal moment is

\[
\boxed{
\mathfrak P_{\rm PP}(Y)
=
\mathfrak D_{\rm PP}(Y)
+
\mathfrak P^\circ(Y).
}
\tag{T-106140.9}
\]

It is nonnegative. Combining (T-106140.6)--(T-106140.9),

\[
\boxed{
\mathfrak P_{\rm PP}(Y)
\le
\mathfrak D_{\rm PP}(Y)
+
|\mathfrak A^\circ(Y)|
+
|\mathfrak K^\circ(Y)|.
}
\tag{T-106140.10}
\]

## 6. The two repaired gates

Define

```text
WCADD106140:
  on every dyadic horizon,

      |A^circ(Y)| = Y^o(1),

  with the complete source-dual conductor sum performed before the absolute
  value.

WCKUM106140:
  on every dyadic horizon,

      |K^circ(Y)| = Y^o(1),

  with all mixed and double nonprincipal channels normal ordered and then
  summed before the absolute value.
```

The two gates have distinct intended mechanisms:

```text
WCADD106140:
  centered additive/divisor transport;
  CV/XD physical geometry;
  Boolean half-source cutoff differences of L-106132;

WCKUM106140:
  even-character L-family moments;
  Kummer collision lines;
  function-field Frobenius/trace input;
  hybrid large sieve or relative trace formula.
```

Neither gate is proved.

## 7. Exact conclusion chain

Since `c_ell c_rho>1`, the principal moment
`mathfrak P_PP` dominates the source-dual square of the native unphased
bilateral member. The Cauchy argument of `L-106121.3--L-106121.5` therefore
uses only the principal channel; no uncentered nonprincipal moment is needed.

Consequently,

\[
\boxed{
\begin{aligned}
\mathrm{WCADD}_{106140}
\wedge
\mathrm{WCKUM}_{106140}
&\Longrightarrow
\mathfrak P_{\rm PP}(Y)=Y^{o(1)}\\
&\Longrightarrow
\mathrm{BCI}_{102990}\\
&\Longrightarrow
\mathrm{RH}.
\end{aligned}
}
\tag{T-106140.11}
\]

This is a genuine two-statement conjunction. The additive trace alone
contains the principal mode plus the Kummer fluctuation; the Kummer trace
alone has zero principal mode. Their difference isolates the conclusion
member.

## 8. Relation to the older gates

The corrected disposition is:

```text
BTPS106121:
  principal--principal positive moment;
  still a sufficient but stronger single gate;
  principal atomic diagonal paid.

BTMS106121 / BTDS106121:
  uncentered positive mixed/double moments;
  not required for the implication;
  their complete atomic diagonals were not paid.

DAPRO106110:
  one-sided principal moment;
  sufficient on its own at that coordinate.

DAKUM106110:
  uncentered one-sided nonprincipal moment;
  not a necessary companion and dimension-bearing before normal ordering.
```

`WCADD106140` and `WCKUM106140` replace the false claim that all uncentered
family channels have an already-paid atomic diagonal.

## 9. Required source discipline

The following operations are forbidden:

```text
take absolute values separately for each conductor fibre;
discard the centered negative background of a nonprincipal kernel;
replace Pc^2 by P or by c^2;
subtract one global atomic number after character fibres have been
  independently collapsed;
count the principal atomic diagonal again in a nonprincipal channel;
infer WCADD or WCKUM from the finite replay.
```

The half-source identity `L-106132` gives a source-exact route for keeping the
least-prime conductor sum signed before squaring.

## Exact boundary

```text
complete bilateral source/tensor identity          PROVED EXACT
Gauss atomic phase cardinality                     CORRECTED EXACT
principal atomic diagonal                          PROVED SUBPOWER
Wick-centered four-channel identity                PROVED EXACT
Boolean half-source Calderon row                   PROVED EXACT

WCADD106140                                        OPEN / RH-BEARING
WCKUM106140                                        OPEN / RH-BEARING
BCI102990                                          OPEN / RH-BEARING
Riemann Hypothesis                                 UNPROVEN
```
