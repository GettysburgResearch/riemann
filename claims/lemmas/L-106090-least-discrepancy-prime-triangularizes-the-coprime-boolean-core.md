# L-106090 — The coprime two-sided Boolean core has a unique long least-discrepancy phase

Claim ID: `L-106090`  
Programme aliases: `LFAM1.LEAST_DISCREPANCY_TRIANGULARIZATION`, `LFAM2.ROUGH_TAIL_KUMMER_COORDINATE`, `STRESS.BOOLEAN_CORE_FIRST_DIFFERENCE`  
Status: **PROVED EXACT INCIDENCE PARTITION AND NONZERO-PHASE NORMAL FORM**  
Created: 2026-08-25  
Depends on: parent `L-102955`, `L-102957--L-102959`, `L-102962--L-102963`, `T-102990`; PR #751 `L-106080`  
Programme issues: #743, #736, #737  
RH status: **not assumed**

Work in the only cofinal Boolean-core sector left by `L-102955`.  After
exact common-square extraction and the inherited clean owner/core renewals,
one interaction has the form

\[
N=P\,g^2c^2,\qquad M=Q\,g^2d^2,
\tag{L-106090.1}
\]

where

\[
c>1,\qquad d>1,\qquad \mu^2(cd)=1,\qquad(c,d)=1.
\tag{L-106090.2}
\]

The owner pairs are retained in the canonical equal-pair gauge of
`L-102962`.  The clean sector also has

\[
(c,Q)=(d,P)=1
\tag{L-106090.3}
\]

after the already-proved owner/core-overlap renewal.

## 1. Unique least-discrepancy orientation

Put

\[
p=P^-(c),\qquad q=P^-(d).
\]

Because `(c,d)=1`, one has \(p\ne q\).  Exactly one of \(p<q\) or \(q<p\)
holds.  Orient the interaction so that

\[
\ell:=p<q.
\tag{L-106090.4}
\]

Then

\[
\ell\mid N,\qquad \ell\nmid M.
\tag{L-106090.5}
\]

Indeed, \(\ell\mid c\), while squarefreeness, (L-106090.2), (L-106090.3)
and the common-core extraction show that \(\ell\) divides none of
\(g,Q,d\).

Moreover every prime factor of the opposite reduced core is strictly larger
than \(\ell\):

\[
\boxed{P^-(d)=q>\ell.}
\tag{L-106090.6}
\]

Thus the opposite reduced core is an exact \(\ell\)-rough source.  In
particular,

\[
\boxed{\ell<d.}
\tag{L-106090.7}
\]

Every coprime two-sided pair occurs in exactly one oriented sector
\((g,\ell,\rightarrow)\).  There is no phase-choice multiplicity.

## 2. Exact nonzero Ramanujan phase

For \(e_\ell(x)=\exp(2\pi i x/\ell)\), (L-106090.5) gives

\[
\sum_{h=0}^{\ell-1}e_\ell(h(N-M))=0.
\]

Therefore

\[
\boxed{
1=-\sum_{h=1}^{\ell-1}e_\ell(h(N-M))
=-\sum_{h=1}^{\ell-1}e_\ell(-hM).
}
\tag{L-106090.8}
\]

The phase on the \(\ell\)-divisible side is constant.  The entire nontrivial
phase acts on the opposite \(\ell\)-rough tail.

This is a source-exact pair-incidence decomposition of `BCI102990`.  It does
not identify the owner pair with the phase prime: \(\ell\) is a literal
reduced-core label, endpoint-placed independently by `L-102963`.

## 3. Dyadic long-core consequence

Place the opposite reduced core in one octave

\[
D\le d<2D.
\]

Equation (L-106090.7) implies

\[
\boxed{D>\ell/2,\qquad 1+\ell/D<3.}
\tag{L-106090.9}
\]

Hence every least-discrepancy phase is locally in the one-prime long-core
range, with an absolute margin.  No exceptional or short-conductor sector
remains at fixed fibre.

## 4. Exact triangular form

Let \(\alpha\) denote all retained source data on the \(\ell\)-divisible
anchor:

\[
\alpha=(g,c,P,\text{Boolean representation, owner pair, shell, carrier,
marked-67 and renewal labels}).
\]

Let \(A_\alpha\) be its physical observation vector.  Let
\(R_{\alpha,h}\) be the complete opposite packet satisfying

```text
P^-(d)>ell;
(d,c)=1;
clean owner/core incidence;
the fixed ratio-eight physical shell;
all inherited literal source weights.
```

Then the oriented two-sided current is coefficient-exactly

\[
\boxed{
\mathcal C_{\rm 2s}
=
-\,2\operatorname{Re}
\sum_\alpha\sum_{h=1}^{\ell_\alpha-1}
\langle A_\alpha,R_{\alpha,h}\rangle ,
}
\tag{L-106090.10}
\]

with the harmless convention that the factor \(2\) records the two ordered
copies of one unordered Gram interaction.  Equivalently, one may sum each
unordered interaction once and omit that factor.

The form is triangular in the ordered prime filtration:

```text
anchor least prime = ell;
every prime in the opposite reduced core > ell.
```

## Scope

The lemma resolves the source-exact discrepancy-prime assignment required by
`L-102963`: it is the first differing core prime after common-core extraction.
It also proves that each fixed phase conductor is paid by the opposite reduced
core.

It does **not** bound the coherent sum over the anchors \(\alpha\).  The exact
rough-tail family attached to one anchor is `L-106091`; the fixed-fibre phase
bound is `L-106092`; the remaining global amplifier is stated in `T-106090`.
