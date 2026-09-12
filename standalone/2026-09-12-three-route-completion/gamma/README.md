# Gamma route: a signed defect balance from a real-zero anchor

**Proposed component proofs. RH and the cofinal signed-production estimate remain open.**

This packet continues the exact gamma sources of [#862](https://github.com/GettysburgResearch/riemann/pull/862) and [#865](https://github.com/GettysburgResearch/riemann/pull/865). It does not improve their approximation rate again. It constructs an explicit positive convolution path from a Bessel/Sturm real-zero source to each native compressed source, proves enough parameter regularity for the reciprocal square root, and obtains an integrated Jensen balance which includes zero births, collisions, and crossings without assigning differentiable labels to zeros.

The new exact closing target is a signed integral of source-defined quantities, with a complete spectral-radius remainder. No vanishing estimate for that integral has been established. The frozen centered-N=5 disk from #858 makes its total production strictly positive at that stage; a proposed nonpositive production rule at every finite stage is therefore false on the native family itself.

Read [PROOF.md](PROOF.md), particularly Sections 5–8. [SOURCES.json](SOURCES.json) records imports and their status. [check.py](check.py) reconstructs bounded rational controls and [results.json](results.json); these controls do not replay #858's defining-integral certificate, evaluate a new Jensen integral, or verify the infinite analytic theorems.

```text
python -I -S -B check.py
python -I -S -B -O check.py
```

The principal difference from an endpoint-error calculation is the initial condition: the anchor has defect exactly zero independently of RH. A variation integral starting at xi would instead retain the unknown constant Delta_xi and could not close the problem merely by tending to zero.
