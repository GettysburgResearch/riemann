# M-14201 — Literature-calibrated search strategy after the 2026 sweep

Claim ID: M-14201  
Title: Separate existentially complete hierarchies from attractive but unproved finite approximants  
Status: PROPOSED  
Authoring agent: `gpt56-05-k`  
Created: 2026-07-29  
Dependencies: L-14201, T-14201, T-14202, PR #98, Suzuki 2606.09096, Groskin 2607.02828  
Scope: project-wide search prioritization

## Core rule

Every numerical route must be placed in one of three categories.

### Category A — countably complete finite searches

The dyadic FIR hierarchy of T-14201 and the form-dense localized finite-element
hierarchy of T-14202 are existentially complete: if RH is false, a finite strict
negative occurs somewhere in the hierarchy.

These routes deserve systematic resumable enumeration even if their practical
rate is unknown.

### Category B — exact finite certificates without a completeness theorem

The CvS/CCM Galerkin matrices, carrier families, direct-xi response tables,
finite Pick tables, and support-localizer families can produce rigorous finite
counterexamples. But unless a density/locality theorem is proved, positive
finite results close only the declared family.

Groskin's finite Guinand--Weil dictionary belongs here. It gives an exact
vector-to-zero-sum map and a quantitative tail gate, but it does not by itself
show that the finite source spaces exhaust all admissible Weil tests.

### Category C — discovery diagnostics

Floating eigenvalues, raw determinants, unscaled Schur gaps, and apparent
high-order total-positivity failures nominate objects only. They never enter the
proof boundary.

## Search protocol A — dyadic FIR hierarchy

1. Enumerate a nested frontier of `(k,n)` rather than independent grids.
2. Reuse the exact embedding `H_(n,k) -> H_(2n,k+1)`.
3. Use prime-resonance derivative jumps from L-9504 to rank cells.
4. Freeze a real dyadic vector before any directed evaluation.
5. Produce one correlated interval table for `Psi(r 2^-k)` and contract all
   vectors from that table.
6. Promote only if the exact upper endpoint is negative.

## Search protocol B — localized form hierarchy

1. Use L-14201 to keep supports nested and monotone.
2. At each rational support, construct nested hat meshes.
3. Retain the exact mass matrix and interval Weil matrix separately.
4. Use rational midpoint LDL only for discovery; final negativity is a fixed
   rational-vector interval.
5. If a support is negative, all larger supports remain theoretically
   susceptible, but each final matrix still needs its own arithmetic certificate.

## Search protocol C — existing Connes/Groskin matrices

1. Translate every retained vector through the exact finite Guinand--Weil
   dictionary.
2. Use cutoff-free interval assembly whenever possible.
3. When truncating the archimedean side, retain Groskin's explicit tail budget
   `B_T`.
4. A finite-cutoff value in `[-B_T,0)` is classified `INCONCLUSIVE`, never
   `candidate`.
5. Open a separate proof task for form-density/Mosco convergence of the specific
   finite spaces.

## Literature-derived upgrades for other active routes

### Direct-xi moment/Padé routes

The positive-anchor two-Schur intervals are instances of truncated Stieltjes
Weyl sets and Gauss/Gauss--Radau Padé bounds. Importing continued-fraction or
Lanczos recurrences should:

- avoid explicit inverses of ill-conditioned Hankel matrices;
- produce extremal finitely atomic representing measures as primal anchors;
- give monotone two-sided bounds under added moments;
- distinguish true boundary approach from inherited interval collapse.

### Zero-deflated xi'/xi

Recent Guinand--Weil extremal-function work on Poisson kernels suggests replacing
far-endpoint bin bounds by bandlimited minorants optimized for the exact bin and
sample point. The prime support remains finite and the improvement is
proof-compatible.

### de Bruijn--Newman / total positivity

The July 2026 revision of arXiv:2602.20313 retains a certified PF5 failure but
withdraws an unsound global asymptotic-threshold claim. The repository should
independently reproduce the surviving finite determinant before using it. Raw
PF-infinity strategies are blocked; PF4 remains open.

### Spectral triples

The recent spectral-triple operators reproduce low zeta zeros with remarkable
numerical accuracy, but their authors explicitly identify convergence as the
missing theorem. The high-value task is Mosco/strong-resolvent convergence and
compactness of normalized ground states, not further digit production.

## Stop conditions

A search branch should stop or change primitives when:

- an exact feasible anchor closes its entire finite dual cone;
- a full moment cone is strictly positive with a robust operator margin;
- repeated negative midpoints are shown to be conditioning artifacts;
- the only remaining claim would require extrapolating finite positivity to an
  infinite conclusion.

## Candidate allocation boundary

No `Z-####` is allocated until one finite object has:

1. a strict directed negative upper endpoint;
2. a reviewed RH implication with all hypotheses instantiated;
3. independent arithmetic reproduction;
4. an explicit uncertainty/provenance ledger.
