# T-98700 — Fractional Julia–Tao–Hermite completion: a complete RH proof candidate

Claim ID: `T-98700`  
Status: **PROPOSED COMPLETE THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-18  
Base: PR #610 at `edf28c9ad14ccbf5b18b9ced45f3c2fc4ce8221d`  
RH status: **candidate proof, not accepted**

## Theorem

The Riemann Hypothesis holds.

## Proof candidate

1. `L-98700` gives an exact fractional positive-chaos representation of the reciprocal-Julia function and isolates every open-strip singularity in the explicit generalized-prime carrier.
2. `L-98701` refines the Tao local completion into source-labelled positive atoms, so prime updates and Stieltjes integration share one Gram rather than independent pointwise ports.
3. `L-98702` proves that an off-line zero at horizontal displacement `delta` produces First-Hermite heat energy with exponential rate `2 delta^2`.
4. `L-98703` proves an unconditional source-side upper rate `96 theta`, plus a sublinear `T^(3/4)log^2T` term, for every fractional intensity `theta>0`.
5. Given an off-line zero, choose `theta` strictly smaller than `delta^2/192`. `L-98704` gives a contradiction.
6. Hence no zero lies to the right of the critical line. The functional equation excludes zeros to the left except for the reflected critical-line zeros. Therefore every nontrivial zero has real part `1/2`.

No named producer is left outside this chain. The load-bearing new mathematics is the finite-cutoff Fock exhaustion and trace estimate in `L-98703`; it is proved in the submitted candidate and is the mandatory first target of hostile review.

## Exact status boundary

```text
fractional positive Julia chaos               proved exact
atomwise Tao source Gram                      proved exact
heat transform and pole growth                proved analytic
fractional source heat-energy estimate        proposed new proof
heat-rate contradiction                       exact composition
Riemann Hypothesis                            candidate / unproved pending review
```
