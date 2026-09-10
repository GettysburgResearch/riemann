# SC26: infinite spectral core and the attempted trace-sign finish

**Proposed component proofs; independent mathematical review pending.**
**RH and all-order positivity for the actual theta source remain unproved.**

Read [PROOF.md](PROOF.md), especially Sections 3, 5 and 6. This is a separate
research contribution, not a change to main, another research branch, or the
pending integration candidate.

## Mathematical outcome

The new source-specific result rules out a bounded coercive positive metric
for the actual centered theta operator even on the infinite derivative-orthogonal
core. The obstruction is spectral crowding: distinct eigenstates become almost
parallel, forcing metric condition numbers to grow at least as a constant times
log-squared height under the supposed spectral reality/simplicity. Thus deleting
all the finite adjoint chains does not repair the bounded-metric finishing plan.
This does not refute RH or exclude unbounded metrics or other operators.

A classical power-sum/Hankel mechanism is reconstructed with a complete
small-eigenvalue tail estimate and all algebraic multiplicities retained.
It gives the exact alternative condition Tr[T^2 p(T)^2]>=0 for every real
polynomial p. Its application to the literal theta source is OPEN. The trace
is not an automatically positive adjoint-square norm.

The attempt to derive that sign from positive strongly log-concave source
shape fails: the explicit complete density proportional to
(1+x^4/16) exp(-x^2-x^4/1024) stays within the same Hilbert--Schmidt/trace-class
construction, but its exact complete moment bounds give Tr(T^2)<-1/256.
This is a CHANGED SOURCE, not an off-line zeta zero or an RH counterexample.
No external novelty is claimed for the general interpolation/trace machinery.

## Exact sources and reading depth

* Base main: `f99d9e3908dde4865377c75d9ca051c1f545bf4f`.
* Main AGENTS, README, STATUS and PROGRAMMES were read, with relevant portions
  of RESULTS and research/integrated/CURRENT_RESULTS.md. This is not a whole-repo audit.
* Primary mathematical source: PR834 at
  `f0e34780f4fe91bd5d07e791e8855189838c3df5`,
  `standalone/2026-09-09-centered-theta-determinant/PROOF.md`,
  blob `ef01f74c50d4efacb615176cbfed4a3de2fd1147`. Its full proof was read.
  Its exact theta source, centered-operator construction and determinant are
  imported as specified, not promoted to independent acceptance.
* Recently updated PR descriptions, including #803, #825, #828--838, supplied
  orientation only where returned. Their proofs, computations, and later
  source changes are not newly audited or imported by that reading.
* External sources and import boundaries are listed in PROOF.md. The zero-count
  asymptotic is classical and unconditional. The Grommer/Chebotarev attribution
  is not an imported proof of SC26-2, whose full argument is supplied here.

## Executed bounded validation

From this directory:

```sh
python -I -S -B check.py --check results.json --self-test
python -I -S -B -O check.py --check results.json --self-test
```

Both final commands passed with identical mathematical results and summary
stdout. The checker reconstructs the full expected receipt, rather than merely
hashing supplied answers. Its acceptance arithmetic uses only standard-library
integers, Fractions and Gaussian rationals; no assertion is used as an acceptance
gate. Coverage is six sharp two-vector metric panels, fifteen synthetic spectral
panels with their ENTIRE geometric tails, 48 formal cumulant/logarithm identities,
16 exact Jordan traces, and one complete changed-density moment certificate.
These are bounded algebra panels, not a count of infinite theorems or actual
Riemann zeros. Both source-density and synthetic-spectrum distinctions are explicit.

Each mode executes a pristine child-process CLI acceptance and five actual
changed-receipt refusals: a false RH flag, Boolean/integer alias, floating-point
alias, duplicate key, and changed trace-bound sign. An initial self-test correctly
rejected a mutation that had accidentally changed no bytes; the mutation was
corrected, and both final commands then passed. No mathematical result changed.
The emitter is a producer: `python -I -S -B check.py --emit /tmp/sc26.json`.

No actual theta Hankel matrix or zero, large spectral discretization, parent
checker, repository-wide validation, Lean/kernel proof, remote CI, or independent
referee acceptance was executed. The checker does not authenticate or prove the
written infinite arguments. The Git commit pins their bytes; source-independent
mathematical review remains necessary. This is not a complete Riemann checkout.

## Local file fingerprints

The following SHA256 values identify the locally tested payload; they are not
an independent mathematical certificate:

- `PROOF.md`: `45171f2123d878024e7a425a8fd885adeab5408b6d7db347474c93624bcaf302`
- `check.py`: `626b4cbc7520617dd127600f6e5ca73354077fd5a60f61d73f623c7ebdfecfe9`
- `results.json`: `9154657d335d5e7ced09a8db3b3db7dec3dafda85fc875226dcce8bbe235b5a0`
