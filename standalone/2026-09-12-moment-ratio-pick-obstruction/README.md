# Moment-ratio Pick completion: a native obstruction

**PROPOSED research, not an RH proof or disproof.** This separate add-only continuation of the #851 research programme excludes one attempted global real-zero mechanism, not the Gauss–Thorin source or the possibility of real zeros.

For the literal normalized theta Fourier source, its first ten even moments (orders2 through20) force coefficient ratios incompatible with **every complete Bernstein factor** in `Psi(u)=(u-theta)phi(u)`, uniformly for `0<=theta<=1/2`. The witness is derivative-free, exact-rational and positive for every member of that class. Directed full-source evaluation is strictly negative. An explicit `cos(z)cos(4z)` control has only simple real zeros yet also fails the test.

The exclusion survives a `10^-13` relative error in these normalized moments. Consequently no sufficiently late member of any locally convergent normalized even approximating sequence can belong to this single-factor class, even with changing theta and spectral scale. This does **not** exclude ordinary non-complete Bernstein factors, coupled Lee–Yang constructions, or real-zero approximants using another mechanism.

Read **PROOF.md** for the theorem, class boundary, cofinal consequence, analytic quadrature error proof and repository connections. **SOURCES.json** freezes the inspected sources. **VALIDATION.md** records exactly what was executed and what still requires review.

The code uses only Python's standard library. Every accepting run regenerates the source; no xi zero table, special-function library or fitted moment is trusted:

```sh
python -S -B check.py --check results.json
python -S -B -O check.py --check results.json
python -S -B tests.py
python -S -B -O tests.py
```

The seven test methods include a second complete mesh, exact positive-class and all-real controls, one actual pristine CLI acceptance and four actual altered-record CLI refusals in each mode. Passing checks authenticate the arithmetic under the supplied analytic error proof, not independent review of that proof. The script does not replay parent certificates, validate the whole repository, or build Lean.

Relation to recent work: #859/#860 control tails at each fixed branching depth; #862 gives a weighted-defect target whose vanishing remains open; #856 refutes a different native companion phase. This packet neither changes nor promotes those proposals. Its positive result is a robust exclusion theorem for an overstrong structural substitute. RH and all-height zero confinement remain unproved.
