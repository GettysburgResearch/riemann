# O-26901 — Factor-five transition program for the dyadic source

Claim ID: `O-26901`  
Title: The broad odd-leakage problem reduces to one finite-ratio opposite-parity transition block  
Status: **RESEARCH PROGRAM BUILT ON EXACT `L-26901/R-26901`; PRODUCTION LMI OPEN**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08

## 1. Corrected live source

The fixed-`q_0=2` physical source of `L-26204` is

\[
b_2=(\varepsilon-\delta_2)*\mu.
\]

Apply one further safe Euler factor:

\[
\omega_2
=\left(\varepsilon-\frac12\delta_2\right)*b_2.
\tag{O-26901.1}
\]

For its critical Riesz coordinate,

\[
\mathcal R_{\omega}(X)
=\sum_{q\le X}{\omega_2(q)\over\sqrt q}\log{X\over q},
\]

one has exactly

\[
\boxed{
\mathcal R_{\omega}(X)
=\mathcal R_2(X)
 -2^{-3/2}\mathcal R_2(X/2).
}
\tag{O-26901.2}
\]

Conversely,

\[
\boxed{
\mathcal R_2(X)
=\sum_{r\ge0}2^{-3r/2}
 \mathcal R_{\omega}(X/2^r),
}
\tag{O-26901.3}
\]

with the usual floor/zero convention. Thus the two sources have the same
subpower status and neither can cancel an off-line zeta zero.

At physical level this is only a bounded two-translate change of source. Every
cross term remains covered by PR #241's independent-frequency block.

## 2. What is now closed

`L-26901` proves the complete pointwise carry source

\[
Z_{n,m}(j)=g_m(n)-g_m(j)-g_m(n-j),
\]

where

\[
g_m=\mathbf1_{[m,2m)}-rac12\mathbf1_{[2m,4m)}.
\]

Its logarithmic Kummer coupling has the exact sign localization

\[
(\mathcal K(n,m))_-\ne0
\quad\Longrightarrow\quad
2m\le n<5m.
\tag{O-26901.4}
\]

The infinite quotient tail `n>=5m` is already nonnegative. The inner band
`m<=n<2m` is pointwise nonnegative. The fully negative pointwise band is
`2m<=n<4m`, and only the single transition cell `4m<=n<5m` has mixed pointwise
sign.

`R-26901` also proves that the signed odd-column **load** of the exact digital
lift is automatically `O(log^2 X)`. The remaining odd target is itself
RH-equivalent, so controlling leakage load without changing the source cannot
close the proof.

## 3. Preferred production object: `F5TC`

A useful next certificate should no longer enumerate all balanced packets. It
should emit one complete source-bound block for

\[
2m\le n<5m.
\]

Call such an object a **Factor-Five Transition Certificate (`F5TC`)**. It must
contain:

1. the exact fixed-`q_0=2` source and the additional factor
   `epsilon-(1/2)delta_2`;
2. the complete two-frequency physical normal matrix, with every translate
   cross term retained;
3. the pointwise wavelet `Z_(n,m)` and its exact carry/Kummer source map;
4. all rows in the quotient cells `2`, `3`, and `4`;
5. the positive inner-band and far-tail ledgers before any subtraction;
6. every endpoint and noncoprime residue correction;
7. one strict Schur inequality paying the transition block from the retained
   positive reserve and declared lower-delay channels;
8. the dyadic/`2/3` fixed-ratio Mertens mutation.

A candidate certificate fails if it:

```text
drops the half-shifted source sibling;
uses scalar H(z)^2 in place of the reflected modulus square;
takes absolute values before omega_2 recombination;
claims positivity in 4m<=n<5m without a certificate;
reintroduces the infinite n/m tail after L-26901 closed it;
controls only the odd leakage load and omits the odd target;
uses a generic bounded-rank or generic operator-norm theorem.
```

## 4. Why this is a strict narrowing

The previous open objects asked for one of:

```text
all balanced Type-II packets;
all greedy slack;
all Green energy;
all odd-column leakage;
a generic parity-kernel inverse.
```

The new object asks for one fixed source and a bounded set of ratio cells. The
same-sign odd Möbius cube is present in the source but comes with its actual
three opposite-parity dyadic siblings.

This does not make `F5TC` routine. The first fixed-ratio Mertens cell can still
sit inside the transition block. The exact gain is that no proof may now hide
behind an uncontrolled infinite quotient tail: every potentially negative
logarithmic Kummer row is explicitly listed in `2<=n/m<5`.

## 5. Conditional role

The established proof consumer remains DSS:

\[
\Pi_2^{\rm gr}(X)=X^{o(1)}\Longrightarrow\mathrm{RH}.
\]

A successful `F5TC` must be accompanied by a written source map showing how its
strict transition reserve implies DSS or directly gives subexponential
`omega_2` shell energy. That source map is not silently assumed in this note.

Thus the exact current boundary is

```text
pointwise omega_2 carry wavelet             CLOSED / proposed exact
negative Kummer rows outside factor five    CLOSED: none
signed odd leakage load                     CLOSED: polylogarithmic
factor-five physical transition LMI         OPEN
transition LMI -> DSS/shell energy map       OPEN as part of F5TC
RH                                           UNPROVED
```
