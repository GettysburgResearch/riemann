# O-15106 — Public-source executability audit for the first singular-seam row

Observation ID: `O-15106`  
Status: **SOURCE AUDIT WITH MACHINE-CHECKED MANIFEST**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-01  
Scope: determine whether the public Shimizu v8/v6 manuscript fixes enough data
to emit `c_(4,M),A_M,K_M,a_(4,M)^lin` at one actual finite window

## 1. Audit standard

An `actual` quartic row must be reproducible from source-bound inputs.  It may
not choose an auxiliary cutoff, probe basis, projection, or finite-part rule
merely because the manuscript proves that some such object exists.

The machine-readable manifest is

```text
experiments/X-15120-singular-seam-source-producer/
  certificates/shimizu-public-source-v8-v6-audit.json
```

and its exact producer verdict is

```text
SOURCE_SPECIFICATION_INCOMPLETE
missing_count = 17
manifest_sha256 =
40a2cedeac541318f44a8aba9d7b1a00dc431ac8d271a3e0add5ca4f552dcf1a
```

## 2. Source facts that are fixed

The public text fixes, among other abstract data:

- the zero-area carrier `Gamma_R=[0,1] x {0}`;
- the seam coding `kappa(u)=(1/2+arctan(u)/pi,0)`;
- the centered kernel `h_w(u)=(exp(wu)-1)/u`;
- the formal chain
  
  ```text
  D_R --Tr_cmp--> D'_R,adm --LCI_R--> X --Pi_R--> K_R;
  ```
- the use of the Moore--Penrose finite readout reconstruction;
- existence of a closed singular-boundary space and its orthogonal projector;
- a seam involution and abstract Schatten-class estimates.

These are sufficient to state the construction, but not to evaluate one finite
row.

## 3. Unbound public-source data

The audit found the following source-binding fields absent from a public
executable package:

```text
bindings.normalization_sha256
bindings.source_map_sha256
window.identifier
window.cutoff_definition
parameters.alpha
parameters.s_R
parameters.a_tr
readout.gram
readout.quartic_jet_coordinate
chain.raw_coordinate_matrix
chain.jet_coordinate_matrix
chain.seam_transpose_matrix
chain.comparison_trace_matrix
chain.lci_matrix
chain.projection_matrix
chain.seam_involution
classical.a4_linear_interval
```

The independent `tau_4` interval is already available and is not missing.

Several omissions are not cosmetic formatting choices:

1. `S_M^cfw` is called finite dimensional, but no first-window dimension,
   basis, or coordinate functions are emitted.
2. `FP_M^ct` and the “standard finite-window Mellin contour test” are named,
   but no executable contour formula or finite-part algorithm is emitted.
3. the fixed scalar probe `eta_M^fp` is characterized by the contour convention,
   but no coordinate vector is emitted.
4. the transverse/interior cutoffs are chosen once and for all, but no formulas
   are fixed in the public source package.
5. `Pi_R^+` is supplied by the Hilbert projection theorem onto an abstract
   closed subspace, not by a finite matrix, Galerkin scheme, or directed
   approximation bound.
6. the compact-resolvent eigenspace bases are chosen abstractly; no basis is
   bound to the finite readout.
7. no complete matrix for `Tr_cmp`, `LCI_R`, or the realized seam involution is
   emitted at an identified window.

## 4. Exact consequence

Without these fields the public source does not determine numerical values for

```text
c4_vector
raw_operator_A
renormalized_operator_K
a4_linear
trace_A4
trace_K4
quartic_target_verdict
```

This is an executability statement, not a theorem that no admissible
instantiation exists.  The author or another agent may supply the missing
source package.  Once supplied, `L-15141/X-15120` emit the row deterministically.

## 5. Why no surrogate row is retained

Selecting `alpha`, cutoffs, a probe basis, and a Galerkin projector ad hoc would
evaluate a new discretization.  Without a theorem binding that discretization
to the manuscript's declared finite coordinate ledger, its output cannot be
labelled the manuscript's `actual` row.

Accordingly, the public-source certificate reports the missing fields and stops.
The separate synthetic certificate exists only to verify the assembler,
invariants, and fail-closed logic.

## 6. Projection simplification

`L-15142` proves from the manuscript's own closure definitions that

\[
H_R^{\rm res}=H_{\alpha,+},\qquad \Pi_R^+=I.
\]

Thus the one-sided abstract projection theorem need not be numerically solved.
The manifest still requests `chain.projection_matrix` because `LCI_R` is declared
to land in the ambient direct sum `X`; the finite coordinate package must bind
the analytic-block projection `J_an J_an^*` in that ambient basis.
