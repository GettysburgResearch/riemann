# T-19817 — Source-owned radial kernel domination gives a corrected full RH proposal

Claim ID: `T-19817`  
Status: **PROPOSED CONDITIONAL FULL RESOLUTION COMPOSITION — PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-09-v`  
Created: 2026-08-14  
Dependencies: PRs #400, #404, #421, #425, #427, #430, #435, #468–#470; `T-14301`, `L-19868`, `L-19873`; Krein–Langer crossed-zero ledger used on the radial source/model branches  
Scope: corrected post-review salvage of the former `T-19807`; no RH claim

## 1. Why a different conclusion mechanism is mandatory

The historical prolate resolution `T-19807` cannot be repaired by improving
constants.  The review `R-19805-quarter-power-and-complete-d8-gap.md` proves
that:

1. the support-translation factor cancels in the polarized zero-side form, and
   the required scaled support derivative estimate was not established;
2. the complete signed CCM space contains a `d_6`-scale complement direction,
   so the claimed complete `d_8` gap is false.

The later conditional obstruction `R-19846` shows that, in a false-RH world, an
even Xi-cardinal quartet produces a fixed negative finite-Hardy direction while
the Xi-like radical target has value tending to zero.  Therefore making that
target the complete finite ground line is itself an RH-bearing theorem.

Accordingly, this proposal does **not** use complete finite ground selection as
the conclusion step.  The prolate/CCM stack is retained only as an independent
finite approximation and normalization audit.

## 2. Completed arithmetic radial source

Fix a safe horizontal offset `a>0`.  Let

\[
 \mathsf A_a(I)
\]

be the completed arithmetic positive operator-valued measure on half-open
radial-depth intervals `I`, assembled from the coefficient-one source factors
already constructed in the repository:

```text
ordinary-prime additive Clark/Jordan innovations;
paired eta detail;
compact dyadic/gamma bridge;
gamma/pole Fisher connection;
both Hardy orientations and the bridge;
compressed-delay returned and leakage channels.
```

The exact prime component has the radial representation

\[
 d\nu_{p^k}(r)
 =2\log p\,p^{-k(\sigma+2r)}\,dr,
\tag{T-19817.1}
\]

multiplying the polarized feature

\[
 1-e^{-itk\log p}.
\]

The eta, compact-bridge and gamma contributions have the corresponding positive
interval refinements on PRs #427 and #430.  Hence

\[
 \mathsf A_a\ll dr;
\tag{T-19817.2}
\]

the completed arithmetic radial source is diffuse.

## 3. Completed model radial measure

Let

\[
 \mathsf M_a(I)
 =\mathsf C_a(I)+\mathsf S_a(I)
  +\mathsf H_a(I)+\mathsf E_a(I)
\tag{T-19817.3}
\]

be the completed model-space decomposition into critical, stable, hyperbolic
and auxiliary positive kernels.  The Krein–Langer ledger identifies every
crossed off-critical zero at horizontal depth `x>0` with a positive atom of
`\mathsf H_a` at that exact depth.  Thus

\[
 \mathsf H_a
\]

is pure point on positive radial depth.

PRs #430 and #435 prove the following abstract conclusion chain: intervalwise
Loewner domination of the complete model measure by the diffuse arithmetic
measure glues, by minimal Kolmogorov uniqueness, to an interval-natural module
isometry; the pure-point hyperbolic output is then dominated by a diffuse
source and must vanish.

## 4. Source-Owned Radial Kernel-Measure Domination (`SORKMD`)

The one open theorem proposed here is a proof-producing strengthening of
`RKMD`, incorporating the exact source-ownership lesson of PRs #468–#470.

For every safe `a>0`, every finite carrier/delay/orientation/bridge packet
`F`, and every half-open rational radial interval `I`, construct a finite or
countable common feature dictionary

\[
 \{v_{a,I,\alpha}^{F}\}_{\alpha\in\mathcal J_{a,I,F}}
\]

and nonnegative source, model and slack coefficients

\[
 c_{a,I,\alpha},\quad
 d_{a,I,\alpha},\quad
 s_{a,I,\alpha}=c_{a,I,\alpha}-d_{a,I,\alpha}\ge0
\tag{T-19817.4}
\]

such that

\[
 [\mathsf A_a(I)]_F
 =\sum_\alpha c_{a,I,\alpha}
   v_{a,I,\alpha}^{F}(v_{a,I,\alpha}^{F})^*,
\tag{T-19817.5}
\]

\[
 [\mathsf M_a(I)]_F
 =\sum_\alpha d_{a,I,\alpha}
   v_{a,I,\alpha}^{F}(v_{a,I,\alpha}^{F})^*,
\tag{T-19817.6}
\]

and hence

\[
 [\mathsf A_a(I)-\mathsf M_a(I)]_F
 =\sum_\alpha s_{a,I,\alpha}
   v_{a,I,\alpha}^{F}(v_{a,I,\alpha}^{F})^*
 \succeq0.
\tag{T-19817.7}
\]

The dictionary and coefficients must be compatible under:

```text
refinement and disjoint union of radial intervals;
enlargement of finite carrier packets;
ordinary-prime and radix-four response maps;
both Hardy orientations, bridge and compressed delays;
archimedean/gamma/pole completion;
source provenance and one-use capacity.
```

### Native source-ownership clause

At every finite arithmetic truncation, the coefficients `c` must arise from one
atomwise source partition satisfying the surviving `SONTR` requirements of PR
#470:

```text
one source-owned recursive packet with total coefficient mass <1/8;
one detail-slack vector;
coefficientwise nonnegative reconstructed current;
one-use ordinary/detail/shared-port capacity;
exact target, score, row and current-debt constraints;
source-bound finite corrections;
Y4-weighted slack O(1), or at least o(log^2 X).
```

The exact native-capacity separator on PR #470 proves that the raw current
cannot serve as this source: it must be thinned or replaced source-by-source.
The zero-weight triangular repair cone may be used, but its full tail and
provenance must be retained.

### Radial source-lock clause

The source-owned native atoms must map to the additive Clark/Jordan innovations
through the exact radial density (T-19817.1), with the eta, bridge and gamma
analogues attached coefficient one.  This is the missing native-to-radial
column lock.  Total entropy or total norm equality without this atomwise lock is
insufficient.

## 5. Conditional proof of RH from `SORKMD`

Assume `SORKMD_a` for one fixed safe `a>0`.

By (T-19817.7), for every rational interval and finite packet,

\[
 \mathsf M_a(I)\preceq\mathsf A_a(I).
\tag{T-19817.8}
\]

Countable additivity and local Kolmogorov uniqueness give the interval-natural
module isometry of PR #435.  Since all four model components are positive,

\[
 0\preceq\mathsf H_a(I)
 \preceq\mathsf M_a(I)
 \preceq\mathsf A_a(I).
\tag{T-19817.9}
\]

For every singleton depth `x>0`, diffuseness gives

\[
 \mathsf A_a(\{x\})=0.
\]

Therefore (T-19817.9) implies

\[
 \mathsf H_a(\{x\})=0.
\]

As `\mathsf H_a` is pure point, it follows that

\[
 \boxed{\mathsf H_a=0.}
\tag{T-19817.10}
\]

The Krein–Langer ledger then has no crossed-zero port, so

\[
 \xi(s)\ne0
 \qquad(\Re s>1/2+a).
\tag{T-19817.11}
\]

If `SORKMD_(a_j)` holds for one explicit sequence

\[
 a_j\downarrow0,
\]

then (T-19817.11) holds for every right half-strip.  Functional-equation
symmetry gives

\[
 \boxed{\mathrm{RH}.}
\tag{T-19817.12}
\]

## 6. Independent prolate/CCM audit

The same source-owned map should intertwine the radial source generator with the
finite/model-space generator:

\[
 A_aW_a-W_a\Lambda_a
 =|g_a\rangle\langle\eta_a|+R_a.
\tag{T-19817.13}
\]

If the relative Hilbert–Schmidt error tends to zero along a finite Galerkin
sequence, `L-19873` controls the total vertical finite-zero defect.  Together
with the complete moving-Hardy target rate `L-19868` and the verified
conditional implication `T-14301`, this supplies an independent finite spectral
audit of the source construction.

This audit is not used to choose the complete finite ground state and therefore
does not reintroduce either false step of `T-19807`.

## 7. What is proved and what is open

The implication

```text
SORKMD_(a_j) for a_j -> 0
 -> interval-natural source/model isometry
 -> diffuse source dominates pure-point hyperbolic port
 -> hyperbolic port vanishes
 -> zero-free half-planes
 -> RH
```

is complete conditional on the imported radial ledger and is the content of
this proposed theorem.

No current PR proves `SORKMD`.  In particular:

- PR #427 proves the completed positive arithmetic Julia cascade but not its
  model allocation;
- PR #435 reduces the conclusion to intervalwise domination but does not prove
  that domination;
- PR #470 proves that the raw native current is infeasible and formulates
  source-owned thinning, but does not construct the completed radial dictionary;
- the prolate stack does not prove the missing sign and is retained only as an
  audit.

The smallest explicit obstruction is therefore:

\[
 \boxed{
 \text{construct the common source-owned native/radial feature dictionary and
 prove every coefficient slack in (T-19817.4) is nonnegative.}
 }
\]

This is a new source-allocation theorem.  It is not a repair of the rejected
`T-19807`, and it must receive independent review before any RH claim.
