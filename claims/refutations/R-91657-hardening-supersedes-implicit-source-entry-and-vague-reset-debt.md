# R-91657 — Final hardening supersedes the implicit source entry and ambiguous reset ledger in `T-91654`

Claim ID: `R-91657`  
Status: **EXACT SCOPE CORRECTION AND SUPERSESSION RECORD**  
Created: 2026-08-14  
Reviewed precursor: PR #455 through head
`1a6443778095ef2af434c28a53ab2edb347499e3`  
Replacement target: `L-91668`, corrected `L-91669`, `R-91658`, corrected
`T-91655`  
RH status: **unproved pending independent reconstruction**

## 1. The source partition was available but not explicitly consumed

`L-91621` assumes an exact labelled positive source identity and then proves
that leafwise Hall outputs sum to one native row.  `L-91667/T-91654` cited its
conclusion without naming the theorem which supplies that antecedent.

The source theorem is `L-91333`, after the atomwise two-channel split of
`L-91330`.  `L-91668` now:

1. states the finite stopping rule;
2. proves unique ownership of every active squarefree source atom;
3. writes the exact direct-sum source identity;
4. identifies its signed observation with the native row \(c_X\);
5. only then invokes leafwise Hall.

Accordingly:

```text
L-91621 abstract Fubini theorem              retained
unnamed source-identity antecedent            removed
L-91668 explicit source-entry theorem         normative
```

## 2. The old `C_reset` wording allowed hidden leaf and depth overcounts

The precursor stated a bounded per-generation recurrence but did not make it
impossible to charge either one terminal constant per stopped leaf or one root
target at every depth.

The final ledger separates two charges:

```text
current analytic/discrete charge: one effective constant per generation;
terminal arithmetic charge: proportional only to target mass which terminates.
```

Source disjointness makes terminal target telescope over all leaves and depths.
The number of current generations is \(O(\log X)\).  Hence the complete debt is
\(O(\log X)\), with no leaf-count factor and no source fraction multiplying an
unrelated signed deficit.

## 3. The first hardening draft overcorrected the outer/current layer

The first versions of `L-91669/T-91655` attempted to delete the historical
outer equality realization and identify the exact equality score directly with
one finite arithmetic packet.  `R-91658` withdraws that compression.

The reciprocal-zeta equality weight is signed globally and positive only on the
certified first factor-\(54.2\) quotient window.  The final proposal therefore
retains, as one-use current objects:

```text
finite-window equality producer;
one endpoint quantization;
collar and finite/continuum mismatch;
top omission and terminal annulus;
corrected boundary reserve where invoked;
score/normalization bridge L-91557.
```

They are not independent capacity copies added on top of \(c_X\).  They are the
current realization stage of the same root equality datum.  The direct
arithmetic row closes the recursive physical replacement stage.

## 4. Retained mathematics

```text
exact native response Gamma(c_X)=w_X                  retained
exact native detail response Xi(c_X)=Omega_X          retained
finite-window equality-weight positivity              retained
one-use endpoint realization                          retained
same-index ordinary/detail child replacement          retained
global fixed-67 entropy theorem L-91666                retained
finite von-Mangoldt dual                              retained
prime-square and Landau endpoint chain                retained
```

Superseded formulations:

```text
implicit use of the L-91621 source antecedent;
vague C_reset ownership;
outer packet deletion in the first hardening draft;
T-91654 as the normative conclusion target.
```

## 5. Current status

```text
L-91667 / T-91654                         historical precursors
L-91668                                  explicit source entry
R-91658                                  outer-sign/realization firewall
corrected L-91669                        final one-use current/recursive ledger
corrected T-91655                        normative complete proposal
Riemann Hypothesis                       not accepted before review
```
