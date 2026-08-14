# PR #455 direct native-row factor-67 review handoff

Review date: `2026-08-14`  
Frozen proposal head: `9dba11b2f1130c0aa8dba5846ec3c2e658326474`  
Proposal base: `f41797c91497dc462f549a127d8494bbe4ccde2f`  
Main at review freeze: `9c7538559d7f56c2914b39aed5a1fb3fbf7ce131`  
Status: **proposal rejected as proof; RH unproved**

## First reconstruction target

Read, in order:

```text
claims/lemmas/L-91668-exact-labelled-source-partition-closes-native-row-entry.md
frozen L-91330 at blob 50df537eeb6c2f69c106cae2d65997849fe8c4c0
claims/lemmas/L-91669-direct-row-proof-ledger-has-no-hidden-outer-packet.md
claims/refutations/R-91658-equality-weight-only-window-positive-and-outer-realization-remains-load-bearing.md
claims/theorems/T-91655-hardened-direct-row-factor67-resolution-proposal.md
```

The decisive calculation is

\[
\begin{aligned}
&w_a(X,n)=n^{-1/2}(a\sqrt{X/n}-1),\\
&\mathcal Q_{j,a}(X/n)=Q_{X/n}(j)/(a\sqrt{X/n}-1),\\
&w_a\mathcal Q_{j,a}=n^{-1/2}Q_{X/n}(j),\\
&(1+\kappa_*)+(2-\kappa_*)=3.
\end{aligned}
\]

Hence the two-channel observation in `L-91668.5` is three copies of the row, contradicting `L-91668.10`.

## Exact surviving spine

```text
L-91666 fixed-67 entropy inequality             retain
L-91663 native ordinary/detail response          retain
L-91556/L-91560 one-prime native cocycle         retain
same-index arbitrary-child replacement           retain
L-91622 logarithmic packet envelope              retain as conditional
L-91660 finite endpoint dual                     retain
```

## Blocked chain

```text
positive balanced/reserve root source
  -/-> one copy of c_X                           FALSE / factor 3
  -/-> positive native parent row                BLOCKED
  -/-> one-use current plus recursive row         BLOCKED
  -/-> logarithmic native loss                    BLOCKED
  -/-> RH                                         BLOCKED
```

## Repair obligations

A successor must:

1. correct the balanced/reserve row normalization;
2. rerun Hall row and score superordination with that correction;
3. prove an exact source-faithful bridge from the positive continuum equality window to the corrected finite native row;
4. prove all one-use current corrections in the same typed row ledger;
5. regenerate the manifest from the final blobs and include `R-91658`;
6. rerun the validator on the exact final head.

## Freeze audit

The current manifest is not valid for the reviewed head:

```text
L91669 locked 2563665b... actual ed35b648...
T91655 locked 393df457... actual 7c282e7d...
R91658 absent
```

The advertised `REVIEW_SPECIFICATION.md`, `X-91669-hostile-direct-row-audit`, and `t91654-hardening-lock-v2.json` are not present at the frozen head.

## Integration recommendation

Do not merge or promote the conclusion-producing theorem. Preserve the verified local lemmas as route infrastructure, and record `L-91668.10--11` as refuted unless a corrected normalization theorem is deposited and independently reconstructed.
