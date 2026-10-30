# Independent exact check of one endpoint inequality

**Status:** Exploratory independent arithmetic check; not a proof of L-function nonvanishing or of the imported analytic estimates.

**Scope:** The endpoint and two-bin obstruction expressions in Section 5 of Leo Wei, *A refinement of the 7/8 zero-free boundary for the Riemann zeta function*. The scripts independently transcribe equations (2) and (7), with the balanced count given immediately before (7), using SymPy exact rationals. They do not read the author's Lean code or certificate data, and do not derive the count from analytic inputs.

**Source:** [preprint.pdf at commit b83dbbd914c5751acf9bc3389cde58970437278f](https://github.com/LW56e2/quasi-riemann-improved/blob/b83dbbd914c5751acf9bc3389cde58970437278f/preprint.pdf), SHA-256 `bdf1702fa288da52d8df686d21d8f443f176f64fba38f245e0006dd74aedc0f9`. The source itself cites 003 at commit `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`. No independent audit of that analytic source is supplied here. Section 5 also points to [TunedEndpoint.lean](https://github.com/LW56e2/quasi-riemann-improved/blob/b83dbbd914c5751acf9bc3389cde58970437278f/lean/Transport/TunedEndpoint.lean); our arithmetic check does not replay Lean.

## What was run

Python 3 with SymPy 1.14.0:

```text
$ python research/exploratory/zero_free_endpoint/check_endpoint.py
Q degree (2, 3)
nodes 79 leaves 40 maxdepth 33 smallest Bernstein coefficient 40890761721949/17394617548800000000000000 ~ 2.350770955856395e-12
$ python research/exploratory/zero_free_endpoint/check_obstruction.py
t signs True True
weights positive True True sum 1 b canceled True
S positive True pstar equals stated True
0 < (pstar-p)/4 < 10^-12: True exact 55218022707346449/66426847593426519505000000000 approx 8.31260622893246e-13
```

The first script forms `Q = J*(-E-10^-12)` from the stated formulas, and certifies nonnegativity on the whole rectangle `[1/50,3/4] × [0,1/2]` using an adaptive binary subdivision into rational rectangles and exact nonnegative Bernstein coefficients of bidegree `(2,3)`. Each split partitions its parent, so terminal leaves cover the original rectangle. On this rectangle `5/6−δ ≥ 1/12`, `Dx ≥ 37/18`, and `Px ≥ 7/9`, hence the denominator `J` is positive. This proves the stated inequality for the transcribed rational expression. The second script checks the two rational bins, positive weights, cancellation of `b`, the stated threshold `p*`, and the numerical comparison, for the same expression.

**Smallest remaining gap:** The computations do not establish that the formula for `E` and the balanced count correctly bound the physical probe for all required bins, nor the reflected-energy, moment, contour, uniformity, and transfer assumptions used in the preprint. They do not validate the claimed zero-free region or establish novelty. Their source is an external, unreviewed preprint; successful arithmetic checks are independent of whether its analytic proof is valid.
