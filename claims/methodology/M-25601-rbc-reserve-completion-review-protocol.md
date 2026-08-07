# M-25601 — RBC reserve-completion review protocol

Claim ID: `M-25601`  
Status: **PROPOSED FAIL-CLOSED REVIEW PROTOCOL**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-07  
Issue: #256

## 1. Frozen continuation

Review this continuation on top of PR #250 at the exact branch head recorded by
the pull request.  The objective was to prove, rather than rename, the two open
RBC obligations:

```text
actual source-bound reflected reserve;
actual bounded charge injection.
```

The resulting classification is:

```text
source map/cross terms                 closed by matrix depth lift;
finite depth incidence                 closed;
meromorphic charge rank                one;
charge logarithmic scale               full X scale;
aggregate reflected Schur reserve      exactly zero;
source-specific anchor reserve         open and RH-bearing.
```

## 2. Review order

1. PR #241 `L-9518` two-frequency physical block.
2. `R-25601` synthesis-Gram reserve obstruction.
3. `L-25601` nilpotent matrix depth lift.
4. `L-25602` meromorphic charge conservation.
5. `R-25602` far-right contraction barrier.
6. `L-25603` rank-one anchor reduction.
7. `L-25604` cyclic phase frame.
8. `T-25601` exact completion boundary.
9. `X-25601` exact synthetic regression.
10. report and integration handoff.

## 3. Mandatory algebra replay

A reviewer should reconstruct independently:

- `A_K B_K=I` for the nilpotent depth matrices;
- the orientation `ell_K=e_(K-1)` for the declared forward shift;
- the matrix logarithmic derivative coefficients;
- the finite endpoint tail `R'R^(K-1)/(1-R)`;
- the independent two-frequency tensor synthesis;
- the zero Schur complement of the aggregate packet Gram;
- finite Fourier Parseval for the phase lift;
- the local-order alternatives in `L-25602`;
- the exact fixed-ratio anchor transform.

## 4. Scope mutations

The continuation must fail closed under the following mutations.

1. **First-row mutation.** Replace `ell_K=e_(K-1)` by `e_0` while retaining the
   forward shift. The synthesis identity must fail.
2. **Missing depth.** Delete the highest retained depth. The exact tail identity
   must change by `R'R^(K-2)`.
3. **False reserve.** Replace the Schur complement zero by a positive number.
4. **Independent packet mutation.** Apply the aggregate identity to
   `(v,-v)` and require a positive packet norm; this must be rejected.
5. **Pole deletion.** Make both the base and terminal residual holomorphic at
   one zeta zero; the local-order checker must reject it.
6. **Rank/scale conflation.** Replace the full-scale anchor by one `V`-bounded
   coordinate; the fixed-ratio support check must fail.
7. **Vertical-line shortcut.** Claim a gain from increasing `sigma` without
   paying physical deweighting; the exponent identity must reject it.
8. **Lost shell.** Remove the fixed-ratio anchor projection.

## 5. What would constitute a genuine completion

A subsequent proof must add one independently reviewed source-specific theorem
of the form

\[
E_{c,B}(J)
\le e^{o(J)}
\left[1+\max_{u\le(1-\delta)J+C}E_{c,B}(u)\right]
\]

or prove the direct block estimate `E_(c,B)(J)=e^(o(J))`.  The proof object must
preserve the first Farey/Mertens cell and cannot use:

```text
aggregate synthesis positivity;
unsigned residual multiplier norms;
finite meromorphic rank;
face count without coefficient support;
a different resolvent which moves the pole to an unestimated base row.
```

## 6. Verdict discipline

A rejection of the reserve construction does not disprove the fixed-ratio
shell theorem.  The correct statuses are:

```text
aggregate-reserve construction          REFUTED;
finite source-map theorem               PROPOSED EXACT;
rank-one anchor reduction               PROPOSED EXACT;
anchor shell estimate                    OPEN;
RBC conditional implication to RH       RETAINED;
RH                                       UNPROVED.
```
