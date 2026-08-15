# L-92901 — The repaired factor-67 root has an exact two-ledger native identity and direct cost below 60989

Claim ID: `L-92901`
Status: **CANDIDATE-COMPLETE ROOT PRODUCER ON FROZEN ANALYTIC INPUTS — INDEPENDENT REVIEW REQUIRED**
Created: 2026-08-15
Frozen heads: PR #488 `9acd381fa168db02a03646ab16851daebbf4d0fd`; PR #489 `0bb487c8a0782f601be0a3041743b357ad93726a`
Primary inputs: `L-91362`, `L-91674`, `L-92880`, `L-91732`, `L-91733`, `L-91754`, `L-91756`, `L-91840`, `L-19885`, `L-19887`, `L-92900`
RH status: **unproved**

## 1. Exact positive source packet before finite comparison

Use the complete paired stopping-line identity of `L-91362` in the
single-SHARP normalization. It partitions the native positive source into

```text
one finite P_61 forcing;
actual source-disjoint rough child packets;
```

with every child endpoint at most \(X/67\), and preserves target, benchmark,
literal score, component rows, ordinary responses and radix-four responses.

Apply the deterministic factor-67 root Hall of `L-92880` only to the finite
forcing. Keep every endpoint, Hall and least-rough-prime label. Positive
integration and the actual-mass grouping theorem `L-91732` give

\[
\boxed{
P_X^{\rm ret}
=
P_X^{\rm cur,ideal}
+\sum_b\beta_bU_b\widetilde P_b
+U_X^{\rm src},
}
\tag{L-92901.1}
\]

where

\[
\beta_b\ge0,\qquad
\sum_b\beta_b<\frac18,\qquad
Y_b\le \frac X{67}+1,
\tag{L-92901.2}
\]

all packets are source-disjoint, and \(U_X^{\rm src}\) contains only genuine
positive omission/thinning source.

This is the positive source ledger. The finite/continuum defect is not included
in \(U_X^{\rm src}\).

## 2. Whole-cell one-use realization

Use the whole-integer-cell support and exact measurable Hall integration of
`L-91754`. Sum all current colours before the single global positive quantizer.
Let \(d_X^{\rm cur}\ge0\) be the resulting current row after the common scalar
thinning and current-owned finite realization.

The retained-cell finite/continuum defect, intrinsic quantization collar and
terminal comparison form one signed observation vector \(e_X\). Let \(u_X\)
be the unused native capacity supplied by the genuine positive omissions and
common thinning.

The all-column estimates of `L-91733`, the terminal omission estimate and the
same common thinning prove

\[
e_X(q)\le u_X(q)
\qquad(q\ge2).
\tag{L-92901.3}
\]

No source sign is inferred from this inequality.

Applying `L-92900` gives

\[
\boxed{
\Omega_X
=
\Xi(d_X^{\rm cur})
+r_X
+\sum_b\beta_bU_b\Omega(\widetilde P_b),
\qquad
r_X=u_X-e_X\ge0.
}
\tag{L-92901.4}
\]

This is the corrected recursive-capacity identity. It differs from the frozen
proofs only in its type discipline:

```text
omission/thinning reserve:      positive unused source;
finite/continuum comparison:    signed current-owned observation error;
root slack:                     their nonnegative capacity difference.
```

## 3. Direct native cost

The sparse \(Y_4\) dual pays the two ledgers separately.

### Common square-root thinning

The elementary Chebyshev theorem `L-19887` gives

\[
(1-\tau_K)J_\Lambda(X)<12012.
\tag{L-92901.5}
\]

### Nonterminal signed comparison

For \(X\ge10^{12}\), `L-91733` and `L-19885` give

\[
\sum_{q\le X/4}Y_4(q)
\bigl|e_X^{\rm nonterm}(q)\bigr|<4.
\tag{L-92901.6}
\]

### Terminal signed comparison

The terminal majorant and
\(\sum_qY_4(q)q^{-3/2}<11\) give

\[
\sum_qY_4(q)
\bigl|e_X^{\rm term}(q)\bigr|<48972.
\tag{L-92901.7}
\]

### Positive omissions

The whole-cell bottom transition and fixed top omission have combined literal
score below one for \(X\ge10^{12}\):

\[
\langle Y_4,u_X^{\rm omit}\rangle<1.
\tag{L-92901.8}
\]

The preferred direct-row construction uses no auxiliary matrix port and no
large-\(X\) finite base correction.

Equations (L-92900.10) and (L-92901.5)--(L-92901.8) therefore give

\[
\boxed{
0\le
\delta_X^{\rm root}
:=\langle Y_4,r_X\rangle
<
12012+4+48972+1
=
60989.
}
\tag{L-92901.9}
\]

No estimate of \(J_\Lambda(X)-4\sqrt X\) is used. No positive-source mass theorem
is applied to the signed comparison.

## 4. Why this is stronger than the two frozen compositions

For the one-shot implementation of PR #488, (L-92901.4) can be specialized by
inserting the displayed child rows immediately. For the recursive
implementation of PR #489, it supplies the root identity required by the slack
cocycle.

The next lemma uses a third implementation: export the first-generation
children, realize each once by its canonical row, and stop. This avoids both:

```text
unqualified internal-child terminalization;
an infinite recursive native-slack tree.
```

## 5. Boundary

```text
finite P61 source and actual rough children       exact frozen stopping line
root Hall on finite forcing                       exact frozen input
actual child target normalization                 exact
positive source ledger                            exact
signed finite comparison                          separately typed
all-column root slack                             nonnegative on frozen bounds
direct root Y4 cost                               <60989
positive-reserve logarithmic proof                not used
benchmark bridge                                  not used
Riemann Hypothesis                                unproved
```
