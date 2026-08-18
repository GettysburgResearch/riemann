# L-97700 — Every native rough occurrence has one exact first-owner threshold ledger

Claim ID: `L-97700`  
Status: **PROVED EXACT SOURCE THEOREM**  
Created: 2026-08-18  
Frozen base: PR #587 at `8a0f074c5b96600b461fdd6e23b47ee2162c4a70`  
RH status: **not assumed**

Let

\[
q_*(2)=15,\qquad q_*(3)=6,\qquad q_*(4)=3,
\qquad q_*(n)=6\quad(n\ge5),
\]

and let `b(X)=F_61(X)` be the complete grouped `P_61` annular `5:3`
scalar. Thus `b=q_* * mu_{P_61}` in the annular logarithmic-hinge
coordinate. Write

\[
\mathcal R_{67}^{\rm sf}
 =\{m:\ m\text{ squarefree and }p\mid m\Rightarrow p\ge67\}.
\]

Then the native annular scalar is exactly

\[
\boxed{
\mathcal A_X
 =\sum_{m\in\mathcal R_{67}^{\rm sf}}
   {\mu(m)\over\sqrt m}\,b(X/m).
}
\tag{L-97700.1}
\]

The sum is finite because the annular hinge vanishes below its first
activation.

## 1. Atomwise owner

Every native squarefree index has the unique factorization

\[
k=d p_1\cdots p_t,
\qquad d\mid P_{61},
\qquad 67\le p_1<\cdots<p_t.
\tag{L-97700.2}
\]

Its owner label is

\[
(d; p_1,\ldots,p_t;\epsilon),
\qquad
\epsilon=\mu(d)(-1)^t=\mu(k).
\]

Moving one rough prime into the history preserves both activation and
coefficient magnitude:

\[
{X/p\over k/p}={X\over k},
\qquad
p^{-1/2}(k/p)^{-1/2}=k^{-1/2}.
\tag{L-97700.3}
\]

It swaps the paired parity channel once. Thus the complete ordered history
carries the exact native sign and no history may be reoriented before
observation.

## 2. Threshold policy

At a state `v` and a raw edge `v -> w` labelled by rough prime `p`, put

\[
r_{v,w}=p^{-1/2}.
\]

A threshold policy may choose any coefficient

\[
0\le a_{v,w}\le r_{v,w}.
\]

The raw child occurrence is partitioned, in the positive paired-source cone,
into the disjoint suboccurrences

\[
(r_{v,w}-a_{v,w})S P_w
\quad\text{and}\quad
a_{v,w}S P_w.
\tag{L-97700.4}
\]

The first is current-owned and the second is recursively owned. At every edge

\[
\boxed{(r_{v,w}-a_{v,w})+a_{v,w}=r_{v,w}.}
\tag{L-97700.5}
\]

Induction along (L-97700.2) proves that every labelled native occurrence is
spent once: a deterministic threshold gives one terminal owner, while a
fractional threshold gives a disjoint partition whose coefficient sum is the
original

\[
\prod_{i=1}^t p_i^{-1/2}=m^{-1/2}.
\]

No source atom is created by ownership or scale descent.

## 3. Root identification

The finite and rough Euler factors are disjoint, so

\[
\mu=\mu_{P_{61}}*\mu_{\mathcal R_{67}^{\rm sf}}.
\]

Convolving `q_*` and applying the same annular hinge proves (L-97700.1)
coefficient by coefficient, at every real endpoint. Hence the root observation
of the exact owner tree is the native quantity

\[
5[c_X(2)-c_{X/4}(2)]+3[c_X(3)-c_{X/4}(3)],
\]

not the finite `P_61` base `b(X)`.

At `X=184` this distinction is strict: the six rough primes
`67,71,73,79,83,89` contribute a total deleted term greater than `1.36314`.
The directed replay verifies the exact finite identity.
