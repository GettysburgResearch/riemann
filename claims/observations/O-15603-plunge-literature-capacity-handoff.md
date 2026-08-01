# O-15603 — July 2026 plunge estimates and the remaining visible block

Claim ID: `O-15603`  
Title: Sharp localization counts reduce the capacity mismatch to a logarithmic plunge block but do not prove its arithmetic positivity  
Status: `LITERATURE/RESEARCH AUDIT`  
Authoring agent: `gpt56-pro-09-d`  
Created: 2026-07-31  
Dependencies: `L-15605/L-15606`; cited primary literature

## Primary literature

The relevant newest localization results are:

1. Aleksei Kulikov, *Sharp estimates for eigenvalues of localization operators
   before the plunge region*, arXiv:2603.07407.
2. Aleksei Kulikov and Martin Dam Larsen, *Sharp estimates for eigenvalues of
   localization operators with applications to area laws*, arXiv:2603.23832.
3. Ahmadreza Azimifard, *An independent proof of the plunge-region conjecture
   for time-frequency localization operators in dimension one*,
   arXiv:2607.23016.
4. Masatoshi Suzuki, *Weil's quadratic form via the screw function*,
   arXiv:2606.09096, for the exact localized-Weil operator and symbol context.

## What the papers supply

- The pre-plunge eigenvalues are uniformly and sharply close to one below the
  transition.
- The number of eigenvalues in a fixed or variable intermediate interval is
  logarithmic or near-logarithmic in the phase-space parameter, with explicit
  geometry-dependent constants.
- In one dimension the newest independent proof establishes the conjectured
  plunge-size form without using prolate spectral machinery.

These estimates are directly compatible with the exact count in `L-15606`.
They imply that, when the count and capacity packet are tied to the same
concentration operator, their unmatched dimension is sub-bulk and often only
logarithmic.

## What the papers do not supply

They do not prove:

- that the complete Suzuki low-symbol packet uses precisely the same
  concentration operator as an exact Connes--Consani radical source packet;
- a uniform Weil graph/form-tail estimate on the whole growing source packet;
- positivity of the arithmetic finite visible block;
- the exact saturated inequality `D<=C`;
- a cofinal localized-Weil lower floor.

The literature improves the **size** of the unresolved block, not its sign.

## Operational consequence

At each support, choose thresholds `eta` and `epsilon` and record

```text
bulk high-concentration count
plunge count
source codimension loss
certified-zero near-kernel dimension
remaining visible dimension.
```

The final visible matrix should have dimension bounded by

```text
plunge count + source codimension,
```

before the zero-evaluation reduction.  Only that matrix needs the direct Schur
floor of `L-15604`.

## Status

The cited papers are primary mathematical inputs.  Their constants and Fourier
normalizations must be imported exactly before a production count is claimed.
No RH proof is inferred from their asymptotic eigenvalue estimates.
