# O-91401 — Adversarial response to PR #431 and corrected factor-54 frontier

Claim ID: `O-91401`  
Status: **CURRENT HANDOFF / NO RH CLAIM**  
Created: 2026-08-13  
Review frozen at PR #431 head `78a622e32ef36e587099bb95cb791461b75d26bf`  
RH status: **unproved**

## 1. Review findings accepted

The following PR #431 findings are exact:

```text
historical L-91350.2 drops d<=py                 FALSE
historical X-91127 complete-certificate claim    FALSE
hidden hazard = r canonical child                FALSE LITERALLY
pointwise source fractions -> native scalar loss NOT DERIVED
noninherited/current residual rows               NOT LEDGERED BY T-91304
split proof DAG                                   REPOSITORY DEFECT
```

`R-91401` preserves the finite support-cutoff counterexample.

## 2. Repairs now available

### True causal finite problem

`L-91401` gives the correct truncated Hall identity and a finite cell reduction including every parent activation surface `y=d/p`.

### No hidden-hazard observation

`L-91402` works in the exact paired squarefree source tree, keeps the channel parameter attached to the parity pair, and regroups complete finite packets at a stopping line before physical observation. The hidden pure-reserve counterexample is therefore fenced rather than contradicted.

### No undefined scalar branch weights

`T-91401` replaces the native scalar-loss recurrence by a worst-normalized-packet envelope. Arbitrary positive restrictions are controlled by their actual packet masses times the worst child-scale packet loss. Negative losses and non-native packet shapes cause no sign error.

## 3. Corrected proof DAG

```text
paired balanced/reserve source tree
  -> exact positive stopping-line packet partition       L-91402
  -> true causal finite P79/P61 splice cells             L-91401
  -> terminal complete-packet projection                 resident
  -> current residual packet in target/score/row cone    FIRST OPEN ARROW
  -> packet-valued positive reset producer
  -> packet-envelope substochastic consumer              T-91401
  -> o(log^2 X) endpoint loss
  -> resident endpoint criterion
  -> RH.
```

The hidden-hazard lemmas `L-91336/L-91337` and the scalar recurrence in historical `T-91304` are not dependencies of this repaired DAG.

## 4. Smallest exact remaining theorem

For every stopped complete one-prime packet, construct a current-generation packet `R` satisfying simultaneously:

\[
R_{\rm row}(j)\ge0\quad\text{for every row }j,
\]

\[
0\le R_{\rm target}\le R_{\rm score},
\]

and all ordinary/radix-four/boundary capacities with one-use assembly and bounded debt.

The inherited range is supported by the existing Green-boundary theorem. The finite true-causal Hall reduction supplies the correct scalar prefix problem. What is not yet proved is one common cone-membership certificate for the complete current residual, including the noninherited/frontier rows.

Equivalently, prove the local packet inequality in the packet cone:

\[
\boxed{
P_{\rm parent}
\succeq_{m packet}
P_{\rm child}+R,
\qquad R\in\mathscr C_{\rm current}^{+}.
}
\tag{O-91401.1}
\]

This is finite-window and source-bound, but remains RH-bearing through the reset consumer.

## 5. Status

```text
PR431 support-cutoff refutation                    VERIFIED
true causal identity and finite reduction          PROVED
paired stopping-line regrouping                    PROVED
packet-envelope consumer                           PROVED ABSTRACTLY
true finite directed Hall replay                   REQUIRED / PROPOSED
complete current residual packet cone membership   OPEN / RH-BEARING
Riemann Hypothesis                                 UNPROVED
```
