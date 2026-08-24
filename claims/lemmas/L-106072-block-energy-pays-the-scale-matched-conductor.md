# L-106072 — The retained stopped-Vaughan block energy pays the scale-matched conductor

Claim ID: `L-106072`  
Programme aliases: `LFAM1.CONDUCTOR_PAYMENT`, `STRESS.ROOT_OCCUPANCY_BUDGET`, `LFAM2.BLOCK_LARGE_SIEVE_WITHOUT_LOSS`  
Status: **PROVED UNCONDITIONAL GLOBAL OCCUPANCY BOUND**  
Created: 2026-08-25  
Depends on: `L-106070--L-106071`; `R-106070`; parent `L-102880`, `L-102883`, `L-102888`  
Programme issues: #743, #736, #737  
RH status: **not assumed**

Retain one block-colour piece \((\mathcal B,A)\), with

\[
B=UVM,
\qquad
16B<\ell=\ell(B,A)<256B.
\]

All estimates below are uniform in the colour, the marked-\(67\) sector, the
fixed carrier/gauge labels and the dyadic physical horizon.

## 1. The load-bearing block energy

For one owner squareclass \(P=pq\), a balanced stopped-Vaughan atom has
coefficient

\[
\frac{1}{\sqrt P}
\frac{a_U(u)a_U(v)\mu(m)}{uvm},
\qquad
u\in[U,2U),\quad v\in[V,2V),\quad m\in[M,2M).
\]

Here the first range is the ordinary variable \(u\in[U,2U)\); equivalently one
may read the display as \(u\asymp U\), \(v\asymp V\), \(m\asymp M\).

Using

\[
|a_U(n)|\le\tau(n),
\qquad
\sum_{n\sim N}\frac{\tau(n)^2}{n^2}
\ll\frac{\log^3(2N)}N,
\]

and the bounded norm of the fixed compact kernel translate gives

\[
\boxed{
E^{\rm free}_{P,\mathcal B}
:=
\sum_{u,v,m}\|z_{P;u,v,m}\|^2
\ll
\frac{(\log(2X))^{O(1)}}{P B}.
}
\tag{L-106072.1}
\]

This is the sharper estimate already present in the proof of parent
`L-102883.1`; it is retained here rather than weakened to \(X^{o(1)}/P\).

By the equal-core representation bound in `L-106071.6`,

\[
\boxed{
E_{P,\mathcal B}
:=
\sum_c\|Z_{P,c}\|^2
\ll
\frac{X^{o(1)}}{P B}.
}
\tag{L-106072.2}
\]

## 2. One owner pair

For each of the at most two collision lines, `L-106071.8` yields

\[
D_{P,Q,\pm}
\ll
E_{P,\mathcal B}E_{Q,\mathcal B}.
\]

Therefore

\[
\boxed{
D_{P,Q,+}+D_{P,Q,-}
\ll
\frac{X^{o(1)}}{P Q B^2}.
}
\tag{L-106072.3}
\]

Nonsquare owner ratios contribute zero.  Equal products and the exact diagonal
may be retained in (L-106072.3); the stronger inherited equal-product theorem
is not needed for this upper bound.

## 3. The conductor is paid exactly once

Let \(\mathcal O_{\mathcal B,A}\) be the set of owner squareclasses occurring
in the colour.  Multiplying (L-106072.3) by the modulus and summing gives

\[
\begin{aligned}
\ell
\sum_{P,Q\in\mathcal O_{\mathcal B,A}}
\sum_{\pm}D_{P,Q,\pm}
&\ll
X^{o(1)}
\frac{\ell}{B^2}
\left(\sum_{P\in\mathcal O_{\mathcal B,A}}\frac1P\right)^2\\
&\ll
\boxed{
\frac{X^{o(1)}}B
\left(\sum_{P\in\mathcal O_{\mathcal B,A}}\frac1P\right)^2.
}
\end{aligned}
\tag{L-106072.4}
\]

Every owner product satisfies \(P\le X\) on the physical horizon.  Even the
crude harmonic estimate over distinct positive integers gives

\[
\sum_P\frac1P\le1+\log X;
\]

the semiprime reciprocal estimate in the parent packet is stronger.  Since
\(B\ge1\), (L-106072.4) proves

\[
\boxed{
\ell
\sum_{P,Q,\pm}D_{P,Q,\pm}
=X^{o(1)}
}
\tag{L-106072.5}
\]

for every block colour.

The factor \(B^{-1}\) in (L-106072.4) is the exact cancellation of the
power-scale conductor.  No phase-cardinality, family-dimension or owner weight
is paid twice.

## 4. All blocks and source labels

There are only \(O((\log X)^3)\) stopped-Vaughan triple blocks and at most
seven colours per block.  The two line signs, four marked-prime sectors,
finite carrier charts, owner/core renewals and dyadic shell labels add only a
fixed or polylogarithmic factor.  Common-square extraction contributes
\(g^{-2}\) and is summable.

Consequently, with the direct-sum index \(\mathfrak a\) of `T-106060` chosen as

```text
(block, colour, owner P, owner Q, line sign,
 marked sector, carrier/gauge/shell labels),
```

one obtains on every dyadic physical horizon

\[
\boxed{
\sum_{\mathfrak a}
\ell(\mathfrak a)
D_{\mathfrak a}(X)
=X^{o(1)}.
}
\tag{L-106072.6}
\]

The estimate is uniform pointwise in the compact observation and after
logarithmic integration.  Indeed `K_L` is supported in \([1,8]\), so each
physical atom is active for only an absolute logarithmic interval.  If a
block contributes at scale \(X\), then

\[
\frac{X}{512}<P B^2\le X,
\tag{L-106072.7}
\]

which also makes all block and owner ranges finite.

## Meaning

Equation (L-106072.6) is the scale-matched form of the root-residue occupancy
theorem requested by `CROP106060`.  Unlike the earlier formulation, it does
not require the modulus itself to be \(X^{o(1)}\): the exact weighted quantity
\(\ell D\) is proved subpower directly.

The passage from this positive occupancy bound to the native HBC residual is
spelled out, without an implicit completion or principal-leverage step, in
`L-106073`.