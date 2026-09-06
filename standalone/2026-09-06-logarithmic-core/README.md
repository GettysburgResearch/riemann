# From energy completion to finite, two-sided source certificates

**PROPOSED COMPLETE COMPONENT PROOFS — independent review required. RH is NOT proved.**
No actual new window has been certified positive or negative in this packet.

This is new research after the A/C review work, not a review acceptance or a
modification of the original research. Base main is
`051808c1f8367b4320c52f94b40908eb2173d622`. The exact #792 source is
`465cb28ed8cbfa1bb071d9a85eeda9890decfe6b`; its files remain unchanged.

## The connection

The source's compact positive block has an unbounded inverse. Its energy
completion makes the Schur form meaningful, but the parent explicitly does
not infer convergence of its strong residual from energy convergence.

Use the **derivative of the clamped primitive** as the Hilbert coordinate
instead. The positive sector becomes an unbounded logarithmic Fourier
operator plus an explicitly bounded arithmetic perturbation. Carleman's
integral inequality controls the logarithmic operator's leakage outside the
interval. This identifies the full operator domain and gives a smooth
operator core. The resulting residual range is dense in its entire target
space. Ridge least squares, including dependent columns, then produces a
predetermined sequence with residual Gram tending to zero.

The exact source-defined matrices satisfy

    U_m - C_kappa R_m <= S_L <= U_m,
    R_m -> 0,  U_m -> S_L,
    C_kappa=3, or 15/8 for the inherited length-one subspace.

The inequality is inherited; **convergence of its lower side is the new
component theorem**. No uncontrolled inverse, source replacement, sampled
constraint, or suppressed prime tail is used.

A second connection uses compact-distribution Fourier uniqueness. Under RH,
the complete positive zero representation and classical Littlewood zero-count
bound force S_L to be **strictly positive** at each finite L, even though
its energy minimizers need not initially be L2 functions. Therefore every
integer window would admit a finite strict positive certificate under RH.
The gap and the search cost need not be uniform in L.

## Exact boundaries

| Object | Scope |
|---|---|
| LC1 logarithmic coordinate | Exact source; bounded perturbation; primitive norm, not original L2 norm |
| LC2 Carleman/core theorem | Full domain and operator-core proof, including endpoint distributions |
| LC3 ridge construction | Exact continuum constraints; complete strong residual convergence |
| LC4 Schur bounds | Both bounds converge; strict-sign certificates complete at a fixed gap |
| LC5 primitive budgets | Explicit gamma/prime/constant tails; computable rational lengths; algorithm contract |
| LC6 strictness and RH criterion | Under RH every finite effective matrix is PD; universal finite certificates equivalent to RH |
| Missing theorem | Actual Schur positivity at every integer length; NOT supplied |

`PROOF.md` contains all arguments, an exact hypothetical-RH endpoint, and
synthetic countercontrols. `SOURCES.md` records imported classical results,
reading limits, and the distinction from existing heat/Bernstein work.
`verify.py` runs bounded rational and Gaussian-rational controls only.
It is NOT an actual-W interval quadrature engine, zero verifier, Lean proof,
or an implementation of the entire proposed search algorithm.

## Replay

From this directory, with Python 3.13 (standard library only):

```sh
python -I -S verify.py --check result.json
python -I -S -O verify.py --check result.json
python -I -S test_rejections.py
```

The publication consists only of this new directory. No canonical status,
trusted formal source, workflow, reviewer report, or original branch is
modified. The source inequalities that would finish RH remain open.
