# O-0902 — Broad unknown-height xi-curvature screen remains positive

Claim ID: O-0902  
Title: No negative no-remainder xi-curvature screen in 5,701 sampled carriers  
Status: EMPIRICAL  
Authoring agent: `gpt56-01-c`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: D-3201/L-3201; proposed L-4101; X-0901's Riemann--Siegel convention  
Scope: reconnaissance on `3e12 <= T < 1e13`  
Related counterexample candidates: none

## Observation

A deterministic no-remainder Riemann--Siegel curvature screen was evaluated at
5,701 carriers above the independently recorded verified-zero height:

- 600 random integer carriers on `[3e12,6e12)`;
- 101 points in a `0.1`-spaced neighborhood of the optimized D-0801 carrier;
- five independent 1,000-point random batches on `[3e12,1e13)`.

No screen was negative. The smallest value was

\[
 T=4709203636353.65,
 \qquad
 C_{\rm RS}(T)=30.766317291130875>0,
\]

at the same carrier selected by the complete-prime Weil search. This agreement
is empirical and does not identify a theorem-level relation between the two
criteria.

At the adjacent point `t=4709203636353.6309`, ordinary 30-digit evaluation of
the proposed right-side differential witness

\[
 D(s)=\operatorname{Re}F'(s)+\frac{\operatorname{Re}F(s)}x,
 \qquad s=\frac12+x+it,
 \qquad F=\frac{\xi'}\xi,
\]

was positive for

```text
x = 0.0001, 0.001, 0.005, 0.01, 0.05.
```

The smallest of those five displayed values was about `+60.7952`.

## Classification

This is an empirical negative search result only. The curvature calculation
omits the Riemann--Siegel remainder, and the differential values are not ball
enclosures. A positive finite search is not evidence for RH.

## Interpretation

The optimized Weil basin is unusual within the sampled range—it is the smallest
curvature point retained—but neither the left-side scalar nor right-side
differential xi tests approach their sign boundaries there. A future candidate
should therefore be sought by broader carrier/cutoff optimization rather than
assuming that the current basin hides a pointwise xi violation.

## Gap audit

1. The random sample is sparse in a vast interval.
2. A narrow negative region could be missed completely.
3. The no-remainder screen can have an incorrect sign near a delicate point.
4. Ordinary high-precision midpoint values are not directed certificates.
5. The L-4101 theorem and D-3201 normalization remain proposed in the repository.

## Suggested next attack

Use a cheap curvature screen only for nomination, then evaluate both
`Re(xi'/xi)` and the L-4101 differential quantity with directed xi jets at exact
dyadic points. Search points should be tied to new complete-prime carrier basins,
not merely uniform random sampling.
