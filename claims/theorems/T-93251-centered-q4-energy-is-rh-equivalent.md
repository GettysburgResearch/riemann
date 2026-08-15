# T-93251 — Centered compact-Q4 endpoint energy is directly RH-equivalent

Claim ID: `T-93251`  
Status: **PROPOSED COMPLETE RH-EQUIVALENT THEOREM — INDEPENDENT REVIEW REQUIRED; RH UNPROVED**  
Created: 2026-08-15  
Depends on: `L-93250`; the classical functional equation and von Koch implication under RH  
Scope: the centered continuous-position endpoint field of the complete actual compact-Q4 source; no mean coordinate and no global QIDR recurrence

## 1. Statement

Let \(\mathscr V_\circ(N)\) be the centered endpoint energy of
`L-93250.6`. Then

\[
 \boxed{
 \mathrm{RH}
 \quad\Longleftrightarrow\quad
 \mathscr V_\circ(N)
 \ll(\log(2N))^A
 \quad(N\ge2)
 }
\tag{T-93251.1}
\]

for some fixed exponent \(A\).

More precisely, RH gives \(A=4\), while any fixed polylogarithmic bound in the reverse direction excludes every zero with real part greater than \(1/2\).

This theorem removes the endpoint mean from the conclusion mechanism. The variance component alone retains every open-strip zeta zero.

## 2. RH implies centered PIG

Assume RH. The von Koch estimate gives

\[
 \psi(x)-x\ll\sqrt x\log^2(2x).
\tag{T-93251.2}
\]

The complete compact source prefix therefore satisfies

\[
 C_\circ(x)\ll\sqrt x\log^2(2x)
\tag{T-93251.3}
\]

up to the bounded floor residue and the explicit logarithmic four-adic term. Uniformly in \(0\le j<N\),

\[
 R_N(j)\ll\sqrt N\log^2(2N).
\tag{T-93251.4}
\]

Hence

\[
 {1\over N^2}\sum_{j=0}^{N-1}|R_N(j)|^2
 \ll\log^4(2N).
\]

Orthogonal projection away from the constant row can only decrease the square, so

\[
 \boxed{
 \mathscr V_\circ(N)\ll\log^4(2N).
 }
\tag{T-93251.5}
\]

## 3. Centered PIG implies the cubic square-root bound

Assume that for some fixed \(A\),

\[
 \mathscr V_\circ(N)
 \ll(\log(2N))^A.
\tag{T-93251.6}
\]

The exact Cauchy bridge `L-93250.12` gives

\[
 \boxed{
 \mathcal A_\circ(N)
 \ll\sqrt N\,(\log(2N))^{A/2}.
 }
\tag{T-93251.7}
\]

By `L-93250.22`, the same estimate holds for every real \(X\ge1\).
Consequently, for every \(\varepsilon>0\),

\[
 \mathcal A_\circ(X)=O_\varepsilon(X^{1/2+\varepsilon}).
\tag{T-93251.8}
\]

## 4. Pole exclusion

The Mellin integral

\[
 \int_1^\infty
 \mathcal A_\circ(X)X^{-s-1}dX
\]

is therefore holomorphic in \(\Re s>1/2\). But `L-93250.19` gives its exact continuation from \(\Re s>1\), and `L-93250` proves that every nontrivial zero \(\rho\) with \(\Re\rho>1/2\) would be a nonremovable pole of that expression. Hence no such zero exists.

The functional equation reflects the conclusion to the other half of the strip, giving RH.

This proves (T-93251.1).

## 5. Quantitative obstruction from one off-line zero

Suppose \(\zeta(\rho)=0\) and

\[
 \beta:=\Re\rho>{1\over2}.
\]

For every \(0<\varepsilon<\beta-1/2\), one cannot have

\[
 \mathscr V_\circ(N)
 =O\left(N^{2\beta-1-2\varepsilon}\right).
\tag{T-93251.9}
\]

Otherwise `L-93250.12` and endpoint interpolation would imply

\[
 \mathcal A_\circ(X)=O(X^{\beta-\varepsilon}),
\]

making the Mellin transform holomorphic in a half-plane containing \(\rho\), contrary to the surviving pole.

Thus a single off-line zero forces super-polylogarithmic growth in the **centered**, nonconstant Q4 field; the zero mode is not necessary.

## 6. Why this is stronger than the earlier endpoint consumer

The prior direct consumer used

\[
 \mathscr P_\circ(N)
 ={1\over N^2}\sum_j|R_N(j)|^2
 ={ |M_N|^2\over N}+\mathscr V_\circ(N)
\]

and extracted the zero-safe mean. The present theorem instead uses one bounded mean-zero test vector and proves

\[
 \mathscr V_\circ
 \longrightarrow
 \mathcal A_\circ
 \longrightarrow
 \text{the same open-strip pole exclusion}.
\]

Therefore all future Q4 major-arc work may discard the mean coordinate completely and target only nonzero modes.

## 7. Proof boundary

Proposed complete, subject to review:

1. RH implies centered endpoint PIG;
2. centered endpoint PIG controls the cubic scalar at square-root scale;
3. integer control extends to the Mellin variable;
4. every off-line zero survives the cubic multiplier;
5. centered endpoint PIG implies RH;
6. one off-line zero forces centered-energy growth.

Still open:

1. an unconditional polylogarithmic estimate for \(\mathscr V_\circ\);
2. the corresponding distinct-prime major-arc estimate;
3. RH.
