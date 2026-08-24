# T-105440 — Corrected F1 frontier: radial actual owners and endpoint rectangles

Claim ID: `T-105440`

Status: **PROVED SOURCE/GEOMETRIC REPAIR; COFINAL ARITHMETIC ESTIMATE OPEN**

This checkpoint supersedes the conclusion chain in `T-105430` while retaining
its finite pair-Hodge algebra.

## 1. Binding source correction

Let

\[
E_1(\mathbf x)=\prod_{j=1}^m(1-x_j),
\qquad
E_2(\mathbf x)=\prod_{j=1}^m(1-x_j^2),
\qquad
D=E_1-E_2.
\]

The complete defect has the nonzero singleton layer

\[
-\sum_jx_j+\sum_jx_j^2.
\]

An owner packet supported only on unordered pairs of actual prime labels begins
at occurrence degree two and cannot represent this source.  In the one-label
case,

\[
D=(1-x_1)-(1-x_1^2)=-x_1+x_1^2\ne0,
\]

while the actual-pair set is empty.  Thus the pair-only complete-source
promotion in `T-105430` is invalid.  `L-105431` remains a correct Hodge identity
for a genuine degree-two edge packet.

## 2. Exact radial actual-owner decomposition

For every label \(i\), define

\[
\boxed{
\begin{aligned}
C_i(\mathbf x)
={}&-x_i\int_0^1\prod_{j\ne i}(1-tx_j)\,dt\\
&+x_i^2\int_0^1\prod_{j\ne i}(1-tx_j^2)\,dt.
\end{aligned}}
\tag{T-105440.1}
\]

Differentiating the two radial products and integrating from zero to one gives

\[
\boxed{D(\mathbf x)=\sum_{i=1}^m C_i(\mathbf x).}
\tag{T-105440.2}
\]

A native monomial supported on \(k\ge1\) actual labels is divided equally,
with coefficient \((-1)^k/k\), among those labels.  A squared-completion
monomial is divided in the same way with its literal sign.  Hence the unit,
singleton, repeated-label and all higher layers are present coefficient
exactly.

The identity commutes with activation, completion-homotopy integration,
carrier recombination, the fixed common mother and every linear physical
observation.

## 3. Exact endpoint transport

For \(i\ne j\), put

\[
H^{(1)}_{ij}=\int_0^1\prod_{k\ne i,j}(1-tx_k)\,dt,
\qquad
H^{(2)}_{ij}=\int_0^1\prod_{k\ne i,j}(1-tx_k^2)\,dt.
\]

The mixed \(tx_ix_j\) terms cancel identically, leaving

\[
\boxed{
C_i-C_j
=(x_j-x_i)H^{(1)}_{ij}
-(x_j^2-x_i^2)H^{(2)}_{ij}.
}
\tag{T-105440.3}
\]

Thus every primitive owner difference is a native Frobenius endpoint boundary
minus its squared-completion endpoint boundary.  This is the exact interface
to compensated-prefix, truncated-Dickman and critical-variation geometry.

## 4. Source-complete Hodge Dirichlet form

Let \(c_i\) be the two-coordinate carrier-recombined observation of \(C_i\) on
one logarithmic block, and put \(c=\sum_i c_i\).  The complete-graph Hodge
identity is

\[
\boxed{
\|c\|^2
=m\sum_i\|c_i\|^2
-\sum_{i<j}\|c_i-c_j\|^2.
}
\tag{T-105440.4}
\]

Equivalently,

\[
\sum_i\left\|c_i-\frac cm\right\|^2
=\frac1m\sum_{i<j}\|c_i-c_j\|^2.
\]

Define

```text
F1EOT105441:
  the endpoint-owner Hodge deficit in (T-105440.4) is exp(o(T)).
```

Then the fixed outer-current block negative mass is subpower and the frozen
Mellin–Landau consumer gives RH.  `F1EOT105441` remains open.

## 5. Exact bridge to the equal-pair Wick packet

Put every support-size-one monomial of \(D\) into a singleton packet \(a_i\).
For every monomial supported on \(k\ge2\) labels, divide its coefficient equally
among its \(\binom{k}{2}\) actual unordered pairs; call the pair packet
\(b_{ij}\).  Then

\[
D=\sum_i a_i+\sum_{i<j}b_{ij}
\]

and, coefficient exactly,

\[
\boxed{C_i=a_i+\frac12\sum_{j\ne i}b_{ij}.}
\tag{T-105440.5}
\]

Indeed, half the \(k-1\) pair shares incident to \(i\) is

\[
\frac12\frac{k-1}{\binom{k}{2}}=\frac1k.
\]

This identifies the precise repair: pair geometry refines the degree-at-least-
two layer, while singleton plus half-incidence reconstructs the complete
actual-owner current before any square.

## 6. Extreme-pair and Plücker localization

Order the labels and put

\[
E_{ij}=\prod_{i<r<j}(1-x_r),
\qquad
q_{ij}=x_ix_jE_{ij}.
\]

Then

\[
\boxed{
\prod_r(1-x_r)-1+\sum_rx_r=\sum_{i<j}q_{ij};
}
\tag{T-105440.6}
\]

every squarefree occurrence of depth at least two is owned by its exact
least/greatest pair.

For \(a<b<c<d\), the four-label rectangle factors as

\[
\boxed{
\begin{aligned}
q_{ac}-q_{ad}-q_{bc}+q_{bd}
={}&E_{bc}
\left[x_aE_{ab}(1-x_b)-x_b\right]\\
&\times
\left[x_c-(1-x_c)E_{cd}x_d\right].
\end{aligned}}
\tag{T-105440.7}
\]

So a primitive four-label cycle is one left endpoint discrepancy, one middle
Euler block and one right endpoint discrepancy.

If \(w_{ij}\) is the row-zero cycle projection of an \(H\)-valued pair array,
then the three rectangle differences on every four-set satisfy

\[
\boxed{
\sum_{\text{four-sets, three bipartitions}}\|\Delta w\|^2
=(m-1)(m-2)\sum_{i<j}\|w_{ij}\|^2.
}
\tag{T-105440.8}
\]

Thus the complete degree-two cycle norm localizes exactly to the factorized
rectangles in (T-105440.7).

Define `F1RECT105443` as the subpower physical block estimate for those
source-complete endpoint rectangles after the singleton/radial recombination
(T-105440.5).  It is a concrete subproblem, not a replacement for
`F1EOT105441`.

## Exact status

```text
finite F1 Frobenius and Hodge geometry        PROVED EXACT
pair-only complete-source promotion           REFUTED
radial actual-owner decomposition             PROVED EXACT
equal-pair incidence bridge                   PROVED EXACT
owner endpoint-difference factorization       PROVED EXACT
four-cycle Pluecker factorization             PROVED EXACT
cycle norm rectangle localization             PROVED EXACT
F1EOT105441                                    OPEN / RH-BEARING
F1RECT105443                                   OPEN
Riemann Hypothesis                            UNPROVED
```
