# Second proof pass: matched Hecke scale and a growing divisor ladder

**Date:** 2026-08-31  
**Branch:** `research/gpt56-pro/pr765-766-770-781-proof-review`  
**Parent:** PR #783  
**Status:** proposed analytic theorems; independent proof review required  
**RH/GRH:** RH and GRH remain unproved.

This pass attacks the two linked targets identified in the initial review:
the Hecke-support gap and the fixed-depth restriction in the coefficient
divisor ladder.

## Results

### 1. The four-logarithm Hecke gap is closed

[Full proof](HECKE_SUPPORT_SCALE_CLOSURE.md)

For every level-one Petersson-normalized Hecke eigenform,

\[
M_X(e_f)\ll\log k.
\]

The proof keeps the exact positive Rankin--Selberg series and dominates the
incomplete-Gamma cutoff by a Mellin shift.  It replaces the parent
coefficientwise \(d_4\) majorant, which cost four artificial logarithms.

For an arbitrary adversarial subset of \(r_k\) Hecke lines,

\[
\frac1kG_S^{-1/2}I_S(1-c/k)G_S^{-1/2}
=
-\frac1{2c}I+
O_{\mathcal K}\!\left(\frac{r_k\log k}{k}\right)
\]

uniformly on compact endpoint \(c\)-sets.  Hence

\[
r_k=o(k/\log k)
\]

is endpoint-zero-free, and even
\(r_k\le\eta_{\mathcal K}k/\log k\) is zero-free for a sufficiently
small fixed constant.

This matches the existing source theorem that a fixed-depth
cusp-localized divisor nullvector requires \(\gg_J k/\log k\) Hecke
lines.  The only remaining gap is the constant-scale window
\(r_k\asymp k/\log k\).

### 2. The original divisor ladder grows with weight

[Full proof](GROWING_DEPTH_DIVISOR_LADDER.md)

Let \(L=L(k)\) satisfy

\[
L^3\log(k+2)=o(k).
\]

Then, simultaneously for every \(1\le J\le L\), the original coefficient
determinants have their full simple interlacing cluster near

\[
k(1-s)=12J.
\]

All fixed-depth zero, pole, noncancellation, gap, and residue conclusions
hold uniformly.  Therefore the original quotient \(Q_1\), at one weight
\(k\), has at least \(L\) distinct simple right-end real zero clusters and
\(L-1\) simple right-end real pole clusters, plus reflections.

The proof identifies the present technical bottleneck: on the complex
Rouché disc the source cross bound is
\(|B_{lm}|\ll(m-l)A_m\).  In the unweighted triangular norm this produces
the factor \(J^3/k\).  The renormalized matrix itself indicates the next
natural coupling scale is \(J^2/k\), so the cube-root range is not claimed
optimal.

## Imported versus new

### Imported repository science

* the exact coefficient flag, period normalization, source echelon chart,
  Fourier projection, arithmetic cross integral, and Schur identities from
  PR #766;
* the exact Hecke Rankin--Selberg identity and period Laurent estimate;
* the symmetric-square automorphy and zero-free region already imported by
  the parent;
* the fixed-depth nullvector cusp-concentration theorem.

### Additional classical import

The Hecke proof uses the standard near-one comparison

\[
L(1+u,\operatorname{sym}^2f)\ll L(1,\operatorname{sym}^2f),
\qquad 0\le u\le1/\log k,
\]

obtained by integrating the usual logarithmic-derivative estimate in the
zero-free strip.  This is explicitly marked as an import, not a new
zero-free theorem.

### New deductions

* Gamma-tail Mellin domination preserving the exact Rankin--Selberg series;
* \(M_X(e_f)\ll\log k\);
* the matched \(k/\log k\) Hecke-selected zero-free scale;
* explicit uniform depth envelopes for the fixed-depth source proof;
* simultaneous growing-depth Rouché, simplicity, interlacing, residue, and
  gap laws;
* a fixed-weight growing zero/pole census for \(Q_1\);
* identification of \(J^2/k\) as the next renormalized coupling parameter.

## Preserved failures and stop conditions

* No sharp constant is proved in the critical Hecke window.
* No statement is made for arbitrary rotated subspaces outside a selected
  Hecke span.
* The growing ladder is not proved at square-root depth or linear depth.
* If the complex finite-block Neumann quantity ceases to be \(o(1)\), the
  present ladder architecture stops.
* The linear-depth proper theta-source theorem remains a theorem about
  different source quotients and is not substituted for this ladder.
* No RH, GRH, or critical-line-purity conclusion is drawn.
