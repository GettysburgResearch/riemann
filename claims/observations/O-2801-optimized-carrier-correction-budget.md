# O-2801 — Exact correction budget for the optimized carrier basin

Claim ID: O-2801  
Title: The omitted exact D-0801 correction is bounded far below the PR #44 leading margin  
Status: PARTIAL  
Authoring agent: `gpt56-04-c`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: L-2801; L-2802; X-2801; empirical leading result in draft PR #44  
Scope: analytic correction reduction, not a complete prime-side sign certificate  
Related counterexample candidates: none

## Statement

At the optimized carrier parameters

```text
c = 10^11
K = 1024
T = 4709203636353.65
```

L-2802 and the exact rational checker X-2801 prove that, for every unit
coefficient vector in the D-0801 equal-cell family,

\[
 \left|
 \frac{\mathcal A+\mathcal R}{h}
 -\frac{\log(T/(2\pi))}{2\pi}
 \right|
 <\frac1{750000}.
\]

The checker's sharper exact radius is

\[
 \frac{98759175269343099756340}
 {79835755999127184820324325961}
 \approx1.2370293741\times10^{-6}.
\]

Draft PR #44 reports the ordinary-floating complete-leading margin

\[
 +2.6896626427230785\times10^{-4},
\]

which is approximately 217.43 times the exact correction radius.

## Consequence

The missing archimedean and pole blocks are not the likely source of a sign
change at this cell. A complete proof of positivity would now require only a
directed leading-prime margin with lower endpoint above `1/750000` plus the
normalization/admissibility audit. Conversely, a future leading negative whose
upper endpoint is below `-1/750000` would survive every exact correction covered
by L-2802.

This is a rigorous reduction of the proof obligation, not a certification of
the PR #44 floating-point margin.

## Exact computation

X-2801 uses:

```text
log-ratio bit majorant  36
log(T) bit majorant     43
log(3T/2) majorant      43
ceil(sqrt(10^11))       316228
```

and exact rational arithmetic for all four contributions:

- central Fourier mass;
- remote Fourier tail;
- pointwise digamma asymptotic;
- pole term.

No special function is called by the checker.

## Proof boundary

The following remain unresolved:

1. directed range reduction for all `T log(q)` phases;
2. directed accumulation of the complete `4,118,082,969` prime-power terms;
3. a fixed dyadic vector and a rigorous prime Rayleigh interval;
4. independent review of D-0801 admissibility and the Guinand--Weil source
   normalization.

Accordingly no complete positive theorem, negative witness, or `Z-####`
candidate is asserted.

## Gap audit

- The empirical leading margin can still contain an unmeasured phase or
  accumulation error.
- A universal correction bound says nothing about a different carrier or
  cutoff basin.
- The exact budget is conditional on L-2801's source normalization.
- The result must not be presented as evidence for RH.

## Suggested next attack

Freeze the `c=10^11`, `K=1024` vector and emit a directed prime-margin interval.
The target is now explicit: prove its lower endpoint exceeds `1/750000`, or find
a separately certified leading negative below `-1/750000`.
