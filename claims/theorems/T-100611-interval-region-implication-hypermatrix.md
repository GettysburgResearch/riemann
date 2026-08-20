# T-100611 — Interval-region implication hypermatrix

Claim ID: `T-100611`  
Status: **PROVED DEPENDENCY/COMPOSITION THEOREM; TWO MARGINAL ESTIMATES OPEN**  
Created: 2026-08-20  
Depends on: `L-100600--L-100612`; `T-100610`; PRs #652, #671, #674, #676, #688, #690  
RH status: **unproved**

The implication graph is not a list of rival routes. It is a matrix whose rows
are least-prime owners and whose columns are greatest-prime owners. The exact
entry is

\[
A_{ij}(X)
=
\sqrt{r_ir_j}\,
\Delta_i\Delta_jE_{i+1:j-1}\Psi(X),
\qquad i<j.
\tag{T-100611.1}
\]

`L-100610` proves that row marginals are the sequential first-owner currents;
column marginals are the reversed/largest-owner currents. `L-100611` supplies
the positive bi-parameter energy identity, and `T-100610` proves that subpower
row and column Schur masses together imply RH.

## Proven hyperedges

### H1 — opposite owner decompositions combine

\[
\boxed{
\text{first-owner source identity}
\ \wedge\ 
\text{largest-owner source identity}
\Longrightarrow
\text{one exact two-ended interval tensor}.
}
\tag{T-100611.2}
\]

This is `L-100605` at coefficient level and `L-100610--L-100611` at positive
hazard/energy level.

### H2 — source tensor and cubic geometry combine

\[
\boxed{
\text{two-ended hazard tensor}
\ \wedge\ 
\text{global monotonicity/convexity of }\Psi
\Longrightarrow
\text{all possible negativity lies in nonempty interior intervals}.
}
\tag{T-100611.3}
\]

Root, singleton, and adjacent-owner regions are closed exactly by
`L-100612`.

### H3 — opposite marginal estimates combine

\[
\boxed{
\mathrm{FOCR100610}
\ \wedge\ 
\mathrm{LOCR100610}
\Longrightarrow
\text{subpower cubic negative mass}
\Longrightarrow RH.
}
\tag{T-100611.4}
\]

The first implication is the two-sided Schur theorem `T-100610`; the second is
the fixed centered-cubic Mellin--Landau detector of PR #676.

Neither Schur marginal may be deleted. Exact one-column and one-row matrices
show that either one-sided condition alone permits a square-root collapse
loss.

## Regional arithmetic matrix

The nonempty interval entries are divided by endpoint geometry.

| matrix region | exact structure | proved incoming tools | remaining local obligation |
|---|---|---|---|
| `j=i` and `j=i+1` | no interior Euler product | `L-100612` endpoint positivity | none |
| short interval `p_j/p_i<=8` | one compact multiplicative shell | ratio-eight finite-band kernels; complex shifted-square positivity | row/column absolute Schur summation over actual prime cores |
| long interval `p_j/p_i>8` | finite interior prime interval | source-faithful interior Euler squaring `L-100600`; square-root cutoff `L-100601--L-100602` | oriented comparison before physical collapse |
| divisor-exposed entries | one explicit native sign `beta(d)` | positive dilation renewal `L-99961`, with `d^epsilon` Mellin cost | Schur summation of the outer owner/divisor signs |
| smooth/deep sectors | no critical cross-core interaction | PR #688 smooth removal; PR #683 deep-history absolute closure | none |

Thus the previous global gates

```text
FCHD67, HDRB100603, ODSB100604, DOEC100601
```

are not four independent conjectures. They are different marginals or
regional projections of the same interval matrix (T-100611.1).

## Minimal paired frontier

After all exact zero-interior, smooth, deep, and positive-renewal transports
are removed, the conclusion-facing arithmetic frontier is the pair

```text
FOCR100610:
  subpower integrated row Schur mass of the residual interval matrix;

LOCR100610:
  subpower integrated column Schur mass of the same residual matrix.
```

Their conjunction is sufficient by `T-100610`. This is strictly more
informative than another single RH-equivalent scalar statement:

- the row condition is adapted to future-prime/first-owner tools;
- the column condition is adapted to cofactor/largest-prime tools;
- each controls the multiplicity that the other leaves untouched;
- the Schur composition is lossless in the number of active labels because the
  endpoint survival vectors have `ell^2` norm at most one.

## Exact status

```text
coefficient double-owner tensor                 PROVED EXACT
positive two-ended hazard tensor                PROVED EXACT
bi-parameter Littlewood--Paley identity         PROVED EXACT
critical cubic endpoint positivity              PROVED EXACT
two-sided Schur AND-gate to negative mass       PROVED EXACT
semantic identification of old terminal gates  PROVED
regional arithmetic estimates                   PARTIAL
FOCR100610                                       OPEN
LOCR100610                                       OPEN
Riemann Hypothesis                               UNPROVED
```

This theorem is the integration result of the matrix pass. It does not promote
an unproved row or column estimate to a proof of RH.