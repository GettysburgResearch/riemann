# Full direct-row factor-67 closure packet

**Packet ID:** `SPP-91666`  
**Date:** 2026-08-14  
**Status:** **complete RH proof proposal; independent reconstruction required**  
**Riemann Hypothesis:** **not treated as established before that review**

## Why this packet exists

The earlier standalone packet `SPP-91661` correctly left two root routes open:
`GRRT` and `CFFP`. Subsequent direct-row work changes the root architecture
rather than assuming either open theorem.

The new route uses one exact native equality row `c_X` with

\[
\Gamma(c_X)=w_X,
\qquad
\Xi(c_X)=\Omega_X,
\]

proves a positive source-disjoint Hall realization of that same row, subtracts
one complete canonical fixed-67 child, and inserts an arbitrary feasible child
at the same row indices. Thus, after the complete current row is summed,

\[
\Gamma(d_X)=w_X-\Gamma(R_{ch})+\Gamma(d_{ch})\le w_X,
\]

\[
\Xi(d_X)=\Omega_X-\Xi(R_{ch})+\Xi(d_{ch})\le\Omega_X.
\]

This directly answers the root-capacity objection to `L-91659`.

## Main theorem files

```text
claims/lemmas/L-91666-fixed67-literal-entropy-difference-pays-native-score.md
claims/lemmas/L-91667-direct-native-equality-row-gives-complete-one-use-root-reset.md
claims/theorems/T-91654-full-direct-row-factor67-resolution-proposal.md
claims/refutations/R-91656-old-grrt-cffp-frontier-is-superseded-by-direct-native-row-reset.md
```

The closure is

\[
\operatorname{Loss}_X
\le
\operatorname{Loss}_{X/67+C_0}+C_{reset},
\]

hence

\[
\operatorname{Loss}_X=O(\log X)=o(\log^2X).
\]

The exact finite dual gives

\[
F_\Lambda(X)\le\operatorname{Loss}_X,
\]

and the prime-square/Landau endpoint theorem then yields the proposed RH
conclusion.

## New proof supplied here

The former `L-91664` was only an index to a partial replay. `L-91666` now gives a
complete proof of

\[
E(Y)-E(Y/67)
\ge5(\sqrt Y-\sqrt{Y/67})
\qquad(Y\ge67).
\]

It consists of:

```text
base F(67)>3;
402 exact directed derivative cells through 469;
an analytic monotone integral tail for all Y>=469.
```

Retained exact margins:

```text
F(67)                         > 3.2764007195549669
minimum finite derivative     > 22.1747542920858
analytic-tail base G(469)     > 131.798262054325
```

## Exact one-use ledger

The root theorem fixes ownership before optimization:

```text
outer equality packet         current only
one global quantization       current only
width-three collar            same quantization
finite/continuum mismatch     current only
safety factor                 once after current sum
fixed top/terminal packet     current only
corrected P61/67 port         current only
Hall bonuses                  current only
canonical restricted child    recursive, child-owned capacities only
```

No correction is copied to a child, no finite small-prime block is reintroduced,
and no affine or fractional-column child placement is used.

## Verification

```bash
cd experiments/X-91666-full-direct-row-closure
python3 verify.py --json results/verification.json
```

Retained verdict:

```text
PASS_FULL_DIRECT_ROW_CLOSURE_ALGEBRA
proof object: 2162b25bbfc824848bdd1fbf9bdf074f07194de23d21de510c48d39c0f33004d
```

The replay checks the new fixed-67 theorem and algebraic shell. It does not
replace hostile reconstruction of the frozen Hall, source-tree, mismatch,
collar, terminal, port, or endpoint analytic inputs, and explicitly records
`rh_established_by_replay=false`.

## Review order

1. `L-91666` and `X-91666`.
2. `L-91621/L-91663`: native equality row and leafwise Hall identity.
3. `L-91559/L-91667`: same-index arbitrary-child replacement.
4. `L-91114/L-91115/L-91320`: one-use finite current packets.
5. `L-91557`: equality score front door and native benchmark bound.
6. `T-91654`: recurrence, finite dual, prime-square drift, Landau.

## Status boundary

```text
fixed-67 score theorem                    PROVED
native ordinary/detail response           EXACT
positive leafwise Hall row                EXACT ON FROZEN INPUTS
same-index arbitrary-child replacement    EXACT
one-use finite current ledger             PROPOSED COMPLETE / RECONSTRUCT
loss O(log X)                             CONSEQUENCE
full theorem                              COMPLETE PROPOSAL / REVIEW REQUIRED
Riemann Hypothesis                        NOT YET ACCEPTED
```
