# O-91540 — The recursive channel-type gate is removed; the live factor-54 frontier is a one-step producer audit

Claim ID: `O-91540`  
Status: **INTEGRATION HANDOFF / CANDIDATE CLOSURE, NOT AN RH CLAIM**  
Created: 2026-08-13  
Frozen live parent: PR `#399` at `15edbccaeedd96cfa76783713b41715d8ad7d8e5`  
Frozen binary-return branch: PR `#416` at `23aa9adc48a6c3176b799944dfbac11e665407ef`  
RH status: **unproved**

## 1. What changed

The live parent isolates one signed-arithmetic entry theorem and then invokes
`L-91343`, whose positive recursion is written only for the native common
`W_Psi/W_S` kernel type.

The binary-return branch produces two positive types instead:

```text
survival target/score type;
hazard target/score type.
```

The hazard type need not lie in the common-measure cone.  The branch therefore
left “all-generation channel-type stability” open.

`L-91540` shows that common-kernel re-entry is unnecessary.  Every positive
paired affine target/score type is hereditary under the same pointwise
subprobability branching.  Its target, score and every exact component row have
positive residuals.  Any adverse residual score orientation costs at most one
unit of target-normalized local debt, which the typed consumer `T-91541`
absorbs once per generation.

Hence the recursive type-stability sentence on PR `#416` is not a new
RH-bearing theorem.

## 2. Exact frozen one-prime algebra

For \(r=p^{-1/2}\) and \(z=\sqrt{x/n}\), the frozen branch gives

\[
 T_s+T_h=4z-3,
 \qquad
 S_s+S_h=5z-3+r(1-r)(z-1)\ge5z-3.
 \tag{O-91540.1}
\]

Both target-per-score ratios lie in the uniform physical corridor

\[
 \frac12\le T_s/S_s<1,
 \qquad
 \frac12\le T_h/S_h<2.
 \tag{O-91540.2}
\]

The target-Hall version of the branch claims that the two positive row packets
represent their targets exactly and their scores superordinately.  If that
one-step producer is correct in the exact normalization of the live `P_61`
splice, its output enters the class of `L-91540` with zero entry debt.

## 3. Candidate composition

The proposed proof diagram is now

```text
live P_61 + one rough prime signed packet
    |
    |  frozen PR #416 target-exact branch Hall/row producer
    v
positive survival/hazard paired types
    |
    |  L-91540 exact hereditary branching
    v
target-subprobability typed tree, local debt <= 1
    |
    |  L-91329 one-use quantization
    |  L-91334 one global observation port
    v
T-91541 typed score consumer
    |
    v
o(log^2 X) native loss
    |
    v
PR #352 RH consumer
```

The recursive arrow in this diagram is proved by `L-91540/T-91541`.

## 4. What still must be audited before any RH claim

The remaining load-bearing audit is **one-step and finite-interface**, not
all-generation:

1. verify that the target-exact Hall measures of frozen PR `#416` are exactly
   the source measures of the live `P_61` one-prime packet, with no normalization
   mismatch;
2. verify that their row coefficient is the one used by the physical
   ordinary/radix-four capacity maps after affine pushforward;
3. verify that the common observation-port correction remains additive debt
   after target normalization and is not counted once per type;
4. replay the directed Hall and component-row certificates on the merged tree.

Until those four joints are independently reconstructed, the composition is a
candidate full proposal, not an established proof.

## 5. Current boundary

```text
survival/hazard target and score algebra             EXACT
uniform physical-corridor bounds                     EXACT
paired-type all-generation branching                 EXACT
typed branching consumer                             EXACT CONDITIONAL
recursive channel-type stability                     NO LONGER OPEN
one-step live-P61 / PR416 normalization match         AUDIT REQUIRED
merged directed row/capacity replay                   AUDIT REQUIRED
Riemann Hypothesis                                    UNPROVEN
```
