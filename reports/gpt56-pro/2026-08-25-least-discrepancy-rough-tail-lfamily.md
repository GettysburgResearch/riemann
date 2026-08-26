# Least-discrepancy rough-tail L-family repair

Date: 2026-08-25  
Execution PR: #751  
Programmes: #743, #736, #737  
Parent source lock: PR #719 at `ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc`  
Status: **major exact repair; distinct-anchor hybrid moment open; RH unproved**

## Why the frontier changed

The internal audit of `T-106080` correctly rejected a core-only use of the
old phase theorem.  The parent has since repaired the analytic layer:

```text
literal physical-product phase kernels;
arbitrary source-incidence masks;
Boolean Type-I global transport;
exceptional-owner elimination;
canonical equal-pair owner gauge;
owner/phase gauge decoupling.
```

The clean live obstruction is `BCI102990`, the coprime two-sided Boolean core
in the symmetric owner gauge.

## New exact coordinate

After common-core extraction,

\[
N=P g^2c^2,\qquad M=Q g^2d^2,
\qquad c,d>1,\quad(c,d)=1.
\]

Let \(p=P^-(c)\), \(q=P^-(d)\), and orient by the smaller one.  If \(p<q\),
then

```text
p divides N and not M;
every prime of d is larger than p;
1 = -sum_(h=1)^(p-1) e_p(h(N-M)).
```

Thus every remaining interaction has one unique least-discrepancy conductor,
and the opposite source is strictly rough with respect to that conductor.

## New local L-family

For one anchor and one fixed opposite owner,

\[
F_h=\sum_d z_d e_p(-hu d^2)
\]

has the exact even-character decomposition

\[
\sum_{h\ne0}\|F_h\|^2
=
\frac{p+1}{p-1}\|F_0\|^2
+
\frac{2p}{p-1}\sum_{\eta\ {m even},\,\eta\ne1}\|M_\eta\|^2.
\]

Since \(P^-(d)>p\), every fixed fibre is automatically in the long-core
range.  Its whole principal-plus-nonprincipal family moment is bounded by the
literal reciprocal source energy.

## Anchor amplification before squaring

The local theorem cannot be summed source-blindly over the left anchors.
Mellin polarization repairs that problem without duplicating the opposite
tail: for fixed \(g,p,Q,\sigma\), the anchor is assembled inside

\[
Z_{g,p,Q,\sigma,h}(t)
=
\sum_\alpha \overline{A_\alpha(t)}B_{\alpha,h}(t)
\]

before the family square is taken.

The resulting exact positive moment has the source-dual weight

\[
g^2pQ.
\]

Its principal channel is the literal native rough-tail amplitude and its
nonprincipal channels are new even Dirichlet-L members.  A \(g^2pQ\)-weighted
moment bound controls the direct current because

\[
\sum_{g,p,Q}\frac1{g^2pQ}=Y^{o(1)}.
\]

`L-106094` further pays the complete same-anchor diagonal.  Only
distinct-anchor correlations remain.

The live alternatives are therefore:

```text
LDART106090:
  direct one-sided triangular current;

LDRPCX106090 AND LDRNEX106090:
  distinct-anchor principal and nonprincipal amplified moments.
```

Either route closes `BCI102990` and hence the frozen detector chain.  Neither
distinct-anchor theorem is proved here.

## Function-field role

The least-discrepancy prime becomes one least irreducible.  The opposite core
is rough, and the additive phase becomes an Artin--Schreier trace whose
multiplicative transform is a complete even Kummer family.  The useful
function-field theorem must expose which constant/resonant strata survive and
what number-field trace or exponential-sum theorem replaces them.

## Exact status

```text
least-discrepancy partition              proved exact;
rough-tail property                      proved exact;
local Gauss/even-character family        proved exact;
fixed-fibre long-core moment             proved;
anchor-amplified Mellin--Gauss form      proved exact;
same-anchor diagonal                     proved subpower;
distinct-anchor principal/nonprincipal   open;
BCI102990                                open;
RH                                       unproved.
```
