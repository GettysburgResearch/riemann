# T-97800 — Uniform growing-prime two-row tail theorem and the exact FPCB23 frontier

Claim ID: `T-97800`  
Status: **UNCONDITIONAL UNIFORM ADVANCE + EXACT CONCLUSION-PRODUCING REDUCTION**  
Created: 2026-08-18  
Base: PR #579 at `9f56688236d33c515a92032c640888488c06ed6e`  
Compared: PR #580 at `812e7fcbaff2dd1c2c53c885def7b6c0d0e68a05`; PR #589 at `ff5156cf6aa469bb7a2155ff4aa7c094bd75b9b6`  
RH status: **unproved**

## Theorem packet

1. The literal finite Euler rows with the exact row-two and sharp-row-three dictionaries satisfy explicit prefix and all-real lower bounds uniformly in the cutoff.
2. There is a maximal certified cutoff `z_*(X)` with

   \[
   z_*(X)=(1+o(1))\log X
   \]

   such that both truncated physical rows are strictly positive for every sufficiently large real `X`.
3. The full rows satisfy

   \[
   C_{j,\infty}(X)=C_{j,z_*}(X)-\mathcal G_j(X;z_*).
   \]

4. Consequently eventual positivity of both rows is equivalent to

   \[
   \boxed{
   \Gamma_{23}(X)=
   \max\left\{
   {\mathcal G_2\over C_{2,z_*}},
   {\mathcal G_3^\sharp\over C_{3,z_*}^\sharp}
   \right\}\le1.
   }
   \]

Call this theorem `FPCB23`.

## Relation to existing frontiers

- `LAPBR67` is not the extremal theorem: PR #589 refutes its fixed adaptive depth.
- Squared dyadic blocks have the same coprime Type-II sign geometry as `SACF`, but SACF energy is phase-blind and does not imply the one-sided sign alone.
- The sharp Farkas separators are the individual row rays. A `5:3` scalar or completed-parity Lorenz hinge does not automatically lift to both rows.

## Consumer

PR #579 retains the exact two-row Mellin-Landau consumer. Therefore

\[
 \boxed{
 \mathrm{FPCB23}
 \Longleftrightarrow
 \text{eventual }\mathrm{LPTRP}_{23}
 \Longrightarrow
 \mathrm{RH}.
 }
\]

The finite theorem through `10^8` and the uniform truncated-row theorem leave no finite-range or fixed-sieve gap. The one remaining arithmetic producer is the explicit all-depth future-prime bilinear correlation (L-97801.5) with sharp normalization (L-97801.6).

```text
literal coefficient dictionaries                 RETAINED EXACTLY
all real activation cells                         RETAINED EXACTLY
fixed finite sieves                               CLOSED
uniform cutoff z_*(X)~log X                       PROVED
exact least-prime future tail                     PROVED
LAPBR67                                           REFUTED / NOT USED
SACF relation                                     EXACT PROJECTION, NOT EQUIVALENCE
FPCB23                                            OPEN / RH-BEARING
Riemann Hypothesis                                UNPROVED
```
