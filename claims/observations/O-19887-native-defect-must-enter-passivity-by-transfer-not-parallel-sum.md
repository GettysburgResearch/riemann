# O-19887 — The native defect must enter a passive Xi realization through transfer, not parallel addition

Claim ID: `O-19887`  
Status: **PROPOSED RESEARCH HANDOFF — PENDING REVIEW**  
Created: 2026-08-15  
Depends on: `R-19883`

`R-19883` closes the direct positive-parallel PSSI route. The reason is spectral type, not a missing constant: the critical Xi admittance has a pure-point Stieltjes measure under RH, while the native defect has a nonzero absolutely continuous measure.

The viable replacement must therefore have one of the forms

```text
passive block operator + Schur complement;
Redheffer / linear-fractional transform;
source environment orthogonal to the observed cyclic vector;
nonlocal transfer which changes spectral type before observation.
```

A minimal corrected target is:

> Construct a positive self-adjoint block realization whose source/environment block contains the native row and defect measures, while the observed scalar Weyl function is `p_Xi`. Prove passivity of the full block and the exact arithmetic transfer law. Do not require the native defect measure to be a positive submeasure of the Xi zero measure.

This is not proved here. It replaces the false parallel-sum target rather than renaming it.
