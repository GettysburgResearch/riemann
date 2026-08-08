# M-23803 — Canonical balanced-flow review order

Claim ID: `M-23803`  
Status: **REVIEW AND CANONICALIZATION LEDGER**  
Authoring agent: `gpt56-pro-09-v`  
Created: 2026-08-08  
Issue: #238

## 1. Canonical claim order

Review the balanced-flow continuation in this order.

1. `L-23808-atomized-carry-entropy-and-pascal-cocycle.md`
2. `L-23810-carry-flow-divergence-and-mobius-inversion.md`
3. `L-23813-balanced-fragmentation-farkas-and-randomized-producer.md`
4. `L-23811-explicit-binary-ternary-signed-carry-flow.md`
5. `L-23812-weighted-negative-variation-implies-sharp-prime-ramp.md`
6. `T-23803-binary-ternary-signed-flow-full-rh-proposal.md`
7. `L-23814-universal-one-pass-balanced-carry-packing.md`
8. `L-23815-mixed-one-third-half-pascal-renewal.md`
9. `R-23803-pure-central-and-one-third-renewals-do-not-close-bct.md`
10. `X-23802-binary-ternary-flow/`
11. `X-23803-mixed-pascal-renewal/`
12. the final report and PR status comment.

The preferred theorem is the weighted-negative-variation statement `BTF` in
`L-23812/T-23803`. The pointwise mixed-renewal sign `MPR` of `L-23815` is a
stronger alternative producer and must not be substituted silently for BTF.

## 2. Superseded duplicate paths

Concurrent work briefly created duplicate numeric claim IDs. The following
paths are **SUPERSEDED — DO NOT REVIEW AS CANONICAL CLAIMS**:

```text
claims/lemmas/L-23810-mobius-divergence-balanced-fragmentation-equivalence.md
claims/lemmas/L-23811-universal-one-pass-balanced-carry-packing.md
claims/lemmas/L-23812-mixed-one-third-half-pascal-renewal.md
experiments/X-23802-mixed-pascal-renewal/
```

Their durable content has been moved respectively to canonical IDs
`L-23813`, `L-23814`, `L-23815`, and `X-23803`. No theorem should cite the
superseded paths.

## 3. Status boundary

```text
atomized carry/Pascal identities                    proposed exact
Möbius divergence and exact flow reconstruction     proposed exact
Farkas dual and randomized producer                 proposed exact
unconditional one-pass 4 log(2) packing             proposed exact
binary-ternary exact signed flow                    proposed exact
BTF weighted negative variation                     OPEN / LOAD BEARING
mixed 31/32--1/32 pointwise sign MPR                 OPEN / STRONGER ALTERNATIVE
BTF or MPR -> sharp prime ramp -> RH                 proposed complete
accepted proof of RH                                 NO
```

Finite LP and renewal scans are evidence only. A production proof must be
symbolic and cofinal.

## 4. Mandatory adversarial tests

1. Reconstruct the multiple-Möbius divergence and all node-one conventions.
2. Check every child multiplicity, especially central doubled children.
3. Verify exact carry-column reconstruction before any clipping.
4. For BTF, reconstruct how weighted negative mass is repaired into a feasible
   positive packing; do not infer feasibility by naïvely taking the positive
   part.
5. For MPR, search quotient-layer knots and mutate `31/32,1/32`.
6. Retain the fixed-ratio `2/3` Mertens/Farey firewall.
7. Reject any proof that takes total variation before recombining binary and
   ternary channels.
8. Recheck the square-screw upper-envelope and Landau orientation independently.

## 5. Publication boundary

The branch is a serious full conditional architecture with one explicit signed
flow theorem. It is not a genuine unconditional proof until BTF—or the stronger
MPR—is established together with every inherited analytic transfer.
