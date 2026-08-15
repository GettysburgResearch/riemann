# L-92930 — The native least-prime source tree and the `P_61` rough lift are different functorial constructions

Claim ID: `L-92930`
Status: **PROVED EXACT TYPE-SEPARATION AND NORMALIZATION THEOREM**
Created: 2026-08-15
Primary inputs: the paired least-prime identity `L-91362`; native normalization `L-91377`; rough-lift identities `L-91379/L-91688`; rank-one Volterra identity `L-91760/L-91761`
RH status: **unproved**

## 1. Observe after splitting the native source

For `a=2`, the parity observation of the positive paired squarefree source is

\[
 \mathcal O\mathbf P_1^{(2)}(x)
 =\sum_{n\le x}\frac{\mu(n)}{\sqrt n}
  \left(2\sqrt{x/n}-1\right)
 =L(x).
\tag{L-92930.1}
\]

The exact stopping-line identity through `61` is

\[
 \mathbf P_1^{(2)}(x)
 =\mathbf F_{61}^{(2)}(x)
 +\sum_{d\mid P_{61}}
  \sum_{\substack{p\ge67\\dp\le x}}
  (dp)^{-1/2}S^{\omega(d)+1}
  \mathbf P_{p+}^{(2)}(x/(dp)).
\tag{L-92930.2}
\]

Every source occurrence appears exactly once. Applying the parity/endpoint observation **after** this source split gives

\[
\boxed{
 L(x)G_s
 =\mathcal O\mathbf F_{61}^{(2)}(x;G_s)
 +\sum_{d,p}\mathcal O\mathbf C_{d,p}(x;G_s).
}
\tag{L-92930.3}
\]

Here every child keeps its parity, least-prime and same-index source labels. Equation (L-92930.3) is a decomposition of the native endpoint source.

## 2. Rough-lift after observing a native row

By contrast, if `N_X` is first observed as a native row and then lifted through the finite Euler block, the result is

\[
 \mathfrak D_X
 =\sum_{m\in\mathcal R_{67}}m^{-1/2}U_mN_{X/m}.
\tag{L-92930.4}
\]

First-owner deletion gives

\[
\boxed{
 \mathfrak D_X=N_X+\sum_iC_{i,X}.
}
\tag{L-92930.5}
\]

The `C_i` are the positive **capacity reservoir after observation**. They are not the paired source-tree children in (L-92930.2), whose channel signs and source ownership are retained before observation.

## 3. The operations do not commute after labels are forgotten

Write `S` for source splitting, `O` for the signed parity/physical observation and `R` for row-first rough lifting. The native construction is

\[
 O\circ S,
\]

while the finite-Euler rough lift is

\[
 R\circ O.
\]

The equality `O S = R O` is false in general. At the native detail coordinate `q=2`, `R-92930` gives a strict separator for `X>=536`.

The only valid interchange is the labelled identity in which the parity channel, first rough owner and same-index placement are retained through the observation. Erasing those labels and then summing every rough colour positively produces (L-92930.4), not (L-92930.3).

## 4. Native Volterra normalization

The rank-one Volterra identity gives

\[
 \overline c_X
 =\int_1^X\frac{2L(X/s)}s p_s\,ds,
 \qquad p_s\ge0,
\tag{L-92930.6}
\]

and

\[
 c_X=\overline c_X+\mathcal R E_X.
\tag{L-92930.7}
\]

Applying ordinary response at `q` and `4q` separately gives

\[
 w_X=C_{\overline c_X}+v(E_X),
 \qquad
 \Omega_X=\Xi_{\overline c_X}+\mathcal D_4v(E_X).
\tag{L-92930.8}
\]

Equations (L-92930.6)--(L-92930.8), not the rough lift, fix the native continuum-to-finite normalization.

On the factor-67 retained window `1<X/s<67`, `L(X/s)>0`; the complete-graph rank-one coupling exhausts all negative Möbius colours and leaves the positive residual `L(X/s)p_s`. This is a literal source-owned native fibre.

## 5. Compiler contract

A physical coupling compiler is native-normalized if and only if its input marginal is linked to one of the following exact identities before labels are erased:

1. the native Volterra identity (L-92930.6)--(L-92930.8); or
2. the paired stopping-line identity (L-92930.2)--(L-92930.3), including every channel and actual child packet.

It is invalid to use (L-92930.4) and then call the sum of all internal rough colours the native parent.

```text
native paired source-tree identity             exact
row-first P61 rough lift                       exact
source-tree child versus rough reservoir       distinct types
q=2 regression                                 strict separator
native Volterra normalization                  exact
compiler normalization contract                explicit
Riemann Hypothesis                             unproved
```
