# M-15601 — Counted inverse–Ritz positive-RH pipeline

Claim ID: `M-15601`  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-09-c`  
Created: 2026-07-31

## Objective

Produce a cofinal sequence of rigorous localized-Weil lower floors without requiring convergence of a selected ground eigenvector or an explicit principal angle between two low packets.

## Per-support proof packet

For each exact support `a`:

1. **Directed symbol.** Build the complete Suzuki multiplier with all prime-power, scalar, logarithmic, and smooth terms in one normalization.
2. **Count cap.** Use either a multiband low-symbol cover and concentration trace bound, a one-band prolate cover, or another independently proved ambient complement theorem to certify
   \[
   \dim1_{(-\infty,\Gamma)}(A_a)\le d.
   \]
3. **Exact radical packet.** Select exactly `d` independent repaired sources in the Connes--Consani codimension-two domain, apply `E`, and localize them.
4. **Directed packet forms.** Compute, with a second backend where possible,
   \[
   G=J^*J,
   \quad B=J^*A_aJ,
   \quad K=J^*(A_a-t)^2J.
   \]
   The `K` matrix must include the complete ambient residual; `B^2` alone is insufficient.
5. **Strict shifted negativity.** Verify `B-tG<0`.
6. **Inverse-Ritz moat.** Find rational `q<0` and prove
   \[
   qK-(B-tG)\succeq0.
   \]
7. **Ambient floor.** Emit
   \[
   F=t+1/q.
   \]
8. **Cofinal ledger.** Preserve `a,d,Gamma,t,F`, all hashes, the count proof, the source packet, and the directed forms. Only a symbolic envelope, not a fit, may establish `liminf F>=0`.

## Discovery and certification separation

A midpoint generalized eigensolve may propose `q`, but the proof object contains only rational matrices, exact LDL/PSD pivots, and directed source bindings. A negative or zero moat is never repaired by silently increasing precision.

## Adaptive priorities

The most useful quantity is not a raw Ritz eigenvalue. At each level report:

```text
count cap d
packet rank
alpha = compression norm bound
beta  = complete cross-residual norm bound
t
F_exact
F_scalar = -(3t alpha + alpha^2 + beta^2)/(t-alpha)
```

If `d` grows faster than the number of uniformly concentrated exact radical sources, improve the symbol count before adding packet precision. If `alpha` is small but `beta` dominates, refine exterior-tail/form-dual estimates rather than the compression matrix.

## Independent audit gates

A production RH chain requires independent review of:

- Suzuki's complete symbol and scaling;
- the ambient low-mode count theorem;
- the Connes--Consani `E`-radical source domain;
- the directed `A` and `A^2` packet forms;
- the exact count/inverse-Ritz theorem;
- the cofinal rank-capacity asymptotic.
