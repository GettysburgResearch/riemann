# BRN27 — a native phase counterexample and the renormalization hierarchy

**PROPOSED component mathematics and a directed certificate, awaiting independent review. RH is not proved or disproved.**

The target proposed in PR846 has the wrong sign at the exact point `119/2+i/5`. This is not a changed source and not an off-line zeta zero. With A=Xi and the literal BRN26 companion B,

```
-4700000 < exp(119*pi/4) Im(A(119/2+i/5) conj(B(119/2+i/5))) < -4600000.
```

The bound comes from the full source, 512-bit outward complex balls, an exact differential-delay equation, and bounds on both complete integration tails. No zeta/zero oracle, unquantified perpetuity truncation, or floating quadrature enters acceptance.

## Read

[PROOF.md](PROOF.md) states the native counterexample and gives its complete analytic dependencies. [CERTIFICATE.md](CERTIFICATE.md) specifies the arithmetic and every remainder. [VALIDATION.md](VALIDATION.md) separates what ran from what did not. [SOURCES.json](SOURCES.json) fixes the parent and classical imports.

The second result identifies the whole integer-mode family of the Brownian smoothing linearization: positive-law eigenfunctions `D_m=t^m P_m` with eigenvalues `2 integral_1^2 u^(-2m)du`, diagonalizing every finite Taylor jet. This is not a spectral characterization of zeta zeros. The modes m=0,1 have exact companions `G_0=xi`, `G_1=-s xi/4`; in particular `B_1=-z Xi/4`. That neutral direction's positive phase vanishes at every zero of Xi and cannot prove RH.

The m=2 phase condition from the parent is refuted; no replacement global phase theorem is claimed. Exploratory higher-mode tests and a neutral-mode derivative also have mixed signs. The remaining possibility of a source-specific signed combination or nonlinear zero-control mechanism is a research question, not a proved conclusion.

## Reproduce

Run from this directory, using ordinary Python with its standard library:

```sh
python -S -B check.py --full --self-test
python -S -B -O check.py --full --self-test
```

Each full run authenticates all packet hashes, reconstructs bounded algebra, then recomputes the complete native phase from the primitive source and compares the whole typed receipt. The nine altered-receipt/format refusals exercise the validation/comparison functions; they are not nine separate full numerical reruns or nine subprocesses.

Without `--full`, the checker authenticates and checks bounded algebra but explicitly prints that it did **not** recompute the phase. `certify.py --out FILE` is a producer, not independent evidence. Numeric progress prints are nonbinding; acceptance uses exact integer endpoint comparisons.

Optional `scout_fast.py` and `mode_scout.py` require NumPy/SciPy/mpmath and use noncertifying floating arithmetic. `SCOUTS.json` records their important limitations. They are not imported by either accepting program.

## Provenance and scope

This is an add-only continuation of PR846 at `d9b60f8569af65b6787fc33c75c849640c8974e6`. The preceding proof remains unchanged. Its construction, convergence and exact defect formula are not invalidated by this counterexample to its explicitly open phase target.

The code and the mathematical argument have the same author. Their agreement, normal/optimized executions and packet authentication do not substitute for independent mathematical review. No whole-repository build, Lean proof, remote CI success, new zero census, or global zero-geometry conclusion is claimed.
