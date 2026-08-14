# R-91657 — Hardening supersedes the implicit source entry and vague reset-debt ledger in `T-91654`

Claim ID: `R-91657`  
Status: **EXACT SCOPE CORRECTION AND SUPERSESSION RECORD**  
Created: 2026-08-14  
Reviewed precursor: PR #455 through head
`1a6443778095ef2af434c28a53ab2edb347499e3`  
Replacement target: `L-91668`, `L-91669`, `T-91655`  
RH status: **unproved pending independent reconstruction**

## 1. The source partition was mathematically available but not explicitly consumed

`L-91621` begins with an exact labelled positive source identity and then proves
that leafwise Hall outputs sum to one native row.  `L-91667/T-91654` cited the
conclusion without naming the exact theorem which supplies that antecedent.

The source theorem is `L-91333`.  Together with the atomwise two-channel split
of `L-91330`, it supplies the complete positive nonduplicating least-prime tree.
`L-91668` now:

1. states the finite stopping rule;
2. proves unique ownership of every active squarefree source atom;
3. writes the exact direct-sum source identity;
4. identifies its signed row observation with \(c_X\);
5. then invokes leafwise Hall.

Accordingly:

```text
L-91621 abstract Fubini theorem              retained
unnamed source-identity antecedent            removed
L-91668 explicit source-entry theorem         normative
```

## 2. The old `C_reset` wording concealed two different possible overcounts

The precursor stated

\[
 \operatorname{Loss}_X
 \le
 \operatorname{Loss}_{X/67+C_0}+C_{\rm reset}
\]

and described a bounded current ledger.  That wording did not make it
impossible for a reader to charge either:

```text
one terminal constant per stopped leaf;
or one root-target constant at every depth.
```

Neither is the load-bearing accounting.

The correct global object is terminal target mass.  At each fixed-\(67\) split,

\[
 M_r=M_{r+1}+M_r^{\rm term}.
\]

Source disjointness gives

\[
 \sum_rM_r^{\rm term}=M_0=\log X.
\]

Since terminal declared-minus-literal score is at most \(2M^{\rm term}\), the
complete all-depth debt is at most \(2\log X\).  `L-91669` records this
telescoping ledger and `T-91655` obtains the explicit final bound

\[
 \operatorname{Loss}_X<6\log X.
\]

Thus:

```text
constant per leaf                                 forbidden
target mass times depth                           forbidden
terminal target telescoped once                   normative
vague C_reset                                     superseded
```

## 3. Historical outer packets are not physical summands in the direct route

The ownership table in `L-91667` listed the outer equality producer,
quantization collar, finite/continuum mismatch, top omission, and common port.
That made it possible to read the proposal as adding those rows on top of the
exact native row \(c_X\).

The hardened route does not do this.  Its sole physical row is assembled from:

```text
the positive leafwise realization of c_X;
canonical current-minus-child component rows;
same-index recursive child rows;
positive Hall bonuses.
```

`L-26204` is consumed only for the exact root target \(\log X\) and declared
score \(4\sqrt X\).  It supplies no second finite row.

The outer/collar/mismatch/port construction remains an independent historical
route and audit.  It is not load bearing in `T-91655`.

## 4. Retained mathematics

The following precursor results are retained:

```text
exact native response Gamma(c_X)=w_X;
exact native detail response Xi(c_X)=Omega_X;
same-index ordinary/detail child replacement;
global fixed-67 entropy theorem L-91666;
finite von-Mangoldt dual;
prime-square and Landau endpoint chain.
```

The following precursor formulations are superseded:

```text
implicit use of the L-91621 source antecedent;
vague C_reset recurrence;
outer/current ownership table in the direct-row proof;
T-91654 as the normative conclusion target.
```

## 5. Current status

```text
L-91667 / T-91654                         historical precursors
L-91668                                  explicit source entry
L-91669                                  explicit all-depth score/capacity ledger
T-91655                                  normative complete proposal
Riemann Hypothesis                       not accepted before review
```
