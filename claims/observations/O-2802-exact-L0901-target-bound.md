# O-2802 — Exact certification of the optimized L-0901 target bound

Claim ID: O-2802  
Title: The proposed uniform correction at the optimized carrier is exactly bounded below `5e-10`  
Status: PARTIAL  
Authoring agent: `gpt56-04-c`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: L-2801; L-0901; L-2803; X-2801  
Scope: exact target arithmetic, conditional on the proposed analytic bound  
Related counterexample candidates: none

## Statement

After `gpt56-04-c` independently reconstructed the compact source formulas in
L-2801, the base branch of draft PR #44 added the sharper uniform
integration-by-parts estimate L-0901. L-2803 and X-2801 now independently
certify its target specialization using exact rational arithmetic.

At

```text
c = 10^11
K = 1024
T = 4709203636353.65
```

the proposed normalized operator correction is bounded by

\[
 E_{\rm var}=
 \frac{136091541158257193750}
 {292731105330133011007855861857}
 <\frac1{2000000000}.
\]

The decimal size is approximately

```text
4.6490290468e-10.
```

Draft PR #44's complete-leading margin is empirically

```text
+2.6896626427230785e-4,
```

about `5.785e5` times the exact rational budget. The empirical value is not a
directed interval and is not promoted by this observation.

## Independent-check architecture

The source work is split deliberately:

1. L-2801 re-derives the exact compact archimedean and pole formulas without
   importing the carrier search implementation.
2. L-0901, authored concurrently on the base branch, derives a sharper uniform
   oscillatory operator bound.
3. L-2803 exactifies the target constants using only rational inequalities.
4. `verify_variation_budget.py` independently reproduces all target fractions
   with Python integers and `fractions.Fraction`.

This is a meaningful independence fingerprint, although it is not yet an
independent full proof review of L-0901.

## Proof boundary

The result certifies no complete carrier sign because the prime-side leading
margin still lacks:

- a frozen exact vector;
- directed range reduction of every `T log(q)` phase;
- directed accumulation of all `4,118,082,969` terms;
- a rigorous Rayleigh or eigenvalue interval;
- the final D-0801 admissibility and Guinand--Weil normalization audit.

No counterexample or positive RH theorem is claimed.

## Suggested next attack

The omitted-term problem is now negligible at this target. Concentrate all
proof-grade effort on a fixed-vector prime producer. A leading interval whose
lower endpoint exceeds `1/2000000000` certifies positivity after L-0901's
correction; a leading upper endpoint below its negative survives the correction
and advances to the normalization review gate.
