# R-90302 — Small inertia defect does not bound the Q4 current

Claim ID: `R-90302`  
Title: The zero-bare Q4 curvature becomes positive for sufficiently large current; therefore a lower-order negative spectral mass cannot by itself imply the RH-scale innovation bound  
Status: **PROPOSED COMPLETE EXACT FIREWALL — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-10  
Dependencies: `L-90304`  
Scope: logical no-go for inertia-only closure; no statement against the full all-pass/state recurrence

## 1. The zero-bare curvature matrix

On a deep balanced row, `L-90304` gives

\[
K(I)=
\begin{pmatrix}
R&EI-T/2\\
EI-T/2&I^2
\end{pmatrix},
\tag{R-90302.1}
\]

with

\[
R\asymp n\log n,
\qquad
E=O(\log n),
\qquad
T=O(n),
\qquad
R-E^2>0
\tag{R-90302.2}
\]

cofinally.  The variable `I` is the RH-sensitive compact current innovation.

## 2. Large current makes the matrix positive

The determinant is

\[
\det K(I)
=RI^2-(EI-T/2)^2
\]

or

\[
\boxed{
\det K(I)
=(R-E^2)I^2+ETI-\frac{T^2}{4}.
}
\tag{R-90302.3}
\]

Because `R-E^2>0`, this is an upward-opening quadratic in `I`.  Hence

\[
\det K(I)\longrightarrow+\infty
\qquad(|I|\to\infty).
\]

The leading principal minor is `R>0`. Therefore there exists a finite interval

\[
[I_-,I_+]
\]

such that

\[
\boxed{K(I)\succeq0\quad\text{for every }I\notin[I_-,I_+].}
\tag{R-90302.4}
\]

The roots are explicitly

\[
I_\pm
=\frac{-ET\pm |T|\sqrt R}{2(R-E^2)}.
\tag{R-90302.5}
\]

Thus the negative spectral mass is **exactly zero** for all sufficiently large positive or negative currents.

## 3. Consequence

No implication of the form

```text
negative spectral mass delta(K) is small
    =>
|I| is small
```

can be valid, even qualitatively.

In particular, the cofinal theorem

\[
\delta(K)=O(n/\log n)
\]

from `L-90304` is a genuine removal of the former matrix-sign obstruction, but it is not an upper estimate for the RH-sensitive innovation.

The same warning applies after `L-90305`: lifting the small defect to complete blocks does not manufacture a current bound.

## 4. What inertia is still good for

The inertia theorem remains useful at the **synthesis/state** interface.  In an exact all-pass identity, a state curvature occurs with a sign.  `L-90306` shows that if this state is indefinite, only its negative spectral mass has to be paid when the current state is moved to the dissipative side.

That is a different logical use:

```text
valid:
    exact state telescope
    + small negative mass
    -> lower-order forcing;

invalid:
    small negative mass of the current matrix
    -> current amplitude bound.
```

A successful QIDR proof therefore still needs an exact coefficient-one trace/state identity which transports the **positive** current mass rather than merely proving that the matrix has few or small negative directions.

## 5. Relation to the Anthropic failure ledger

The 95-page Anthropic campaign repeatedly found that the wrong spectral statistic can be perfectly controlled while the desired zero statistic remains free: the negative-index route was structurally in the wrong direction, while its positive-index dual was useful.  The present firewall is the direct Q4 analogue.

The object to transport is not `delta(K)` by itself.  It is the complete source/state curvature through the exact all-pass recurrence, with `delta(K)` entering only as a correction.

## 6. Proof boundary

Closed exactly:

1. determinant as an upward-opening quadratic in the unknown current;
2. exact roots of the indefinite interval;
3. PSD for all sufficiently large `|I|`;
4. impossibility of an inertia-only current bound.

Unaffected/open:

1. `L-90306` all-pass state-telescope use of inertia;
2. a coefficient-one upper recurrence for the positive current mass;
3. RH.