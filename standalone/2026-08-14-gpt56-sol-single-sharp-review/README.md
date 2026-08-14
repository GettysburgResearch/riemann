# GPT-5.6 Sol review packet — single-SHARP normalization repair and exact remaining bridge

Freeze date: 2026-08-14
Base PR: #455
Frozen base head: `c6fed57375a0eddd2d508540aee4dfb4717d6cdd`

## Executive status

This packet records the strongest conclusion I could reconstruct without overclaiming.

The exact factor-three normalization failure identified by independent review has a clean repair already present on the frozen head: replace the balanced/reserve two-channel root observation by the single SHARP channel of `L-91670`.

For one squarefree source atom with `Y=X/n`, define

\[
T_\Psi(Y)=4\sqrt Y-3,\qquad S_\Psi(Y)=5\sqrt Y-3,
\]

and

\[
\mathcal H_{\Psi,j}(Y)=\frac{Q_Y(j)}{4\sqrt Y-3}.
\]

Then exactly

\[
\frac1{\sqrt n}T_\Psi(X/n)\mathcal H_{\Psi,j}(X/n)
=\frac1{\sqrt n}Q_{X/n}(j).
\]

After the parity functional this gives precisely one copy of

\[
c_X(j)=\sum_{n\le X}\frac{\mu(n)}{\sqrt n}Q_{X/n}(j),
\]

not three copies. This is the correct native row normalization.

The same channel has

\[
q_\Psi(z)=\frac{4z-3}{5z-3},\qquad q_\Psi'(z)=\frac3{(5z-3)^2}>0,
\]

so the no-upward Hall orientation remains score-superordinate. The normalized row profile inherits the monotonicity of the `a=4/3` profile because

\[
\mathcal H_{\Psi,j}=\frac13\mathcal Q_{j,4/3}.
\]

Therefore the reviewer’s factor-three objection is repaired at the source/row normalization interface without altering the native target, score, or row triple consumed by `L-91556/L-91560`.

## What survives cleanly

The following chain is, at minimum, materially strengthened and internally consistent on the frozen inputs:

1. single-SHARP positive least-prime source recursion;
2. exact one-copy native row observation;
3. exact native target/score/row one-prime cocycle;
4. leafwise no-upward Hall residualization;
5. global source-disjoint Fubini summation;
6. same-index fixed-67 child replacement;
7. fixed-67 literal entropy difference paying the native score difference;
8. native ordinary/detail response identities for `c_X`;
9. the elementary upper bound `J_\Lambda(X)<4\sqrt X+4\log X`;
10. the finite dual and downstream prime-square/Mellin-Landau consumer, conditional on the missing root score realization below.

## The remaining gap I could not honestly close

Independent review correctly isolated a second issue that is not fixed by `L-91670`.

The finite arithmetic row has literal score

\[
\mathcal S(c_X)
=\sum_{r\le X}\frac{\Lambda(r)}{\sqrt r}\log\frac Xr,
\]

whereas the continuum equality packet is assigned score

\[
4\sqrt X.
\]

The proposal needs one exact theorem showing that the positive finite-window continuum equality realization and the single-SHARP arithmetic source tree are source-faithful representations/stages of the same root packet, with the score certificate transferred onto the actual current-minus-child finite row without double-spending capacity or adding an independent physical row.

As frozen, this identification is asserted in prose in the full proposal but is not reconstructed as an exact score-and-row preserving map. I therefore do **not** classify RH as proved.

## Minimal missing theorem

A valid closure theorem may be stated as follows.

### Root equality realization bridge

For every sufficiently large `X`, construct a single typed positive root packet `\mathcal P_X` equipped with:

- a continuum endpoint representation whose critical score is exactly `4\sqrt X`;
- a finite arithmetic observation whose signed native row is exactly `c_X`;
- the single-SHARP least-prime ownership of `L-91670`;
- one global quantization/collar/top/port correction used exactly once;
- a source-disjoint fixed-67 canonical child `\mathcal P_{X/67}`;

such that after child replacement the finite current row is nonnegative, ordinarily and radix-four feasible, and its literal score is at least the continuum root score minus an absolute current-generation constant plus the child score.

Equivalently, prove directly

\[
\operatorname{Loss}_X
\le
\operatorname{Loss}_{X/67+C_0}+C
\]

for the **same typed packet**, with no independent equality-row addend and no scalar score certificate detached from the finite row.

Once this bridge is supplied, the already-frozen fixed-67 score theorem and finite consumer would give `O(log X)` accumulated loss and the advertised downstream RH implication.

## Review recommendation

Review the successor in this order:

1. `L-91670-single-sharp-channel-has-exact-native-row-normalization.md`;
2. `L-91556` and `L-91560` for native one-prime target/score/row normalization;
3. `L-91621` for leafwise Hall/Fubini provenance;
4. `L-91559` and the same-index replacement layer;
5. `L-91666` for fixed-67 score transfer;
6. `L-91107`, `L-91110`, `L-91114`, `L-91115` for the continuum endpoint producer and finite quantization/collar assembly;
7. test whether an exact root equality realization bridge exists between items 1–5 and item 6.

## Classification

```text
factor-three root normalization                    REPAIRED / L-91670
single-SHARP native row                            EXACT / ONE COPY
one-prime native cocycle                           RETAINED EXACT
leafwise Hall/Fubini provenance                    RETAINED EXACT
same-index fixed-67 child replacement              RETAINED EXACT
fixed-67 entropy/score transfer                    RETAINED EXACT
continuum equality score = 4 sqrt(X)               RETAINED
finite arithmetic literal score                    EXACTLY P_Lambda(X)
continuum equality -> same finite root packet       OPEN / LOAD-BEARING
full unconditional RH proof                        NOT ESTABLISHED
```
