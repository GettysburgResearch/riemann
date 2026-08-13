# O-91312 — Adversarial response to PR #431 and corrected factor-54 frontier

Claim ID: `O-91312`  
Status: **CURRENT ROUTE HANDOFF / NO RH CLAIM**  
Created: 2026-08-13  
Depends on: PR #431; `R-91310`; `L-91352/L-91353`; `T-91305`  
RH status: **unproved**

## 1. Review findings accepted

PR #431 is correct that:

```text
L-91350.2 drops the parent cutoff d<=py;
X-91127 does not certify the stated causal packet;
an isolated hidden hazard is not an r-scaled canonical child;
pointwise source fractions do not imply T-91304.6;
L-91346 alone does not ledger all frontier rows.
```

Accordingly `T-91304` must not be treated as a proof of RH.

## 2. Finite repair completed

`L-91352/X-91130` replace the false Hall reduction by a causal checker which includes every parent activation `d/p`, every child activation, and every possible cell minimum. It proves strict target and score Hall margins for all `P_61` thresholds.

`L-91353` converts a true shifted-eight target flow into a positive all-row packet with one uniform score-debt constant. This avoids the invalid inference that a Hall residual equals the signed arithmetic row.

## 3. Consumer repair completed

`T-91305` replaces the undefined scalar recurrence by a measure-valued recurrence on the actual restricted packets. It permits signed child losses and uses the positive mass ledger only to control the sum of local debts.

Thus two objections in PR #431 are repaired without weakening their firewalls:

```text
false finite certificate       replaced by true causal certificate;
undefined scalar theta_b       replaced by actual packet recursion.
```

## 4. Hazard obstruction and the new proof architecture

The hidden hazard theorem remains useful source infrastructure, but its branch must not be identified with an `r`-scaled native child. The repaired proposal does not make that identification.

Instead the proof-producing architecture must establish one exact packet regrouping before observation:

\[
\boxed{
\text{paired least-prime source tree}
=
\text{current positive packets}
+
\sum_b\text{complete causal one-prime packets}_b,
}
\tag{O-91312.1
}

where:

```text
every source atom occurs once;
every target/detail column is allocated once;
every child packet is an actual packet in the cone of T-91305;
the child mass ledger is substochastic;
all remaining boundary and collar debt is charged once.
```

After (O-91312.1), `L-91352/L-91353` produce each one-prime all-row packet; an additional source-cone/capacity typing theorem is required before `L-91343` can be invoked; and `T-91305` closes the score tree.

## 5. Smallest exact obstruction

The first live RH-bearing theorem is now:

> **Causal Packet Regrouping.** Prove (O-91312.1) as an equality in source, target, endpoint-score, every component row, ordinary/radix-four capacity, and the common endpoint-port ledger, with a uniformly bounded normalized mass.

The exact paired least-prime identity `L-91333` and the hidden hazard identity `L-91336` give positive source disintegrations, but neither currently proves this complete packet regrouping after physical observation.

## 6. Correct status

```text
PR #431 support-cutoff refutation               VERIFIED
old X-91127 proof object                        REJECTED
true P61 causal target/score Hall               PROVED
positive all-row Hall packet                    PROVED
standard kernel-cone/capacity typing            OPEN
uniform score debt                              PROVED
measure-valued branching consumer               PROVED CONDITIONAL
causal packet regrouping                        OPEN / RH-BEARING
Riemann Hypothesis                              UNPROVED
```

This is a serious repaired proposal, not a completed proof.
