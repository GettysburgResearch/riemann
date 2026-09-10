# Intrinsic entropy: identifying the actual remaining obstruction

**RH, J=0, and the growing-horizon proof remain unproved.** Proposed component
proofs and a bounded actual-source certificate; independent review required.

This add-only continuation of #817 stops treating better finite correction as
if it removed the intrinsic source-domain minimum. For the same arithmetic
source and the unit exponential target, it gives exactly

    delta=1-exp(-2J),
    J=(1/(2pi)) integral_R log|zeta(1/2+it)|/(t^2+1/4)dt.

This is the classical Balazard--Saias--Yor criterion in the project's source
normalization, not a newly discovered RH criterion. Its essential equality
J=0 has NOT been proved. The functional equation does not supply that equality.

## Reviewable work

- Exact intrinsic errors for the unit exponential and the old ramp target,
  with a sharp cubic sensitivity comparison. Low ramp error can attenuate
  the remaining defect. The targets and their norms are not interchanged.
- A strip-qualified positive decomposition of the ramp error in two actual
  logarithmic moments; every possible off-line zero is retained.
- Full-source Toeplitz determinant ratios decrease to J. A rate corollary
  inherits HC26; it does not say that their limiting entropy is zero.
- One original-metric, full-tail certificate for a rational degree-six trial
  approximating exp(-t/2): squared error <13/250 and 0<=J<27/1000.
  It is NOT a prefix-matching output, not a compact-input realization, and
  not a zero-free-region or competitive zero-height calculation.

Start with [PROOF.md](PROOF.md), then [REVIEW_AND_SOURCES.md](REVIEW_AND_SOURCES.md)
and [VALIDATION.md](VALIDATION.md). No original research file is modified.

## Bounded replay

Run from this directory:

```bash
python -B check.py
python -B -O check.py
python -B test_check.py
python -B -O test_check.py
```

Python standard library only. The copied 160-bit integer interval core is
independently byte-checked against its literal predecessor identity before
execution. No zeta, gamma, zero or numerical integration oracle is used.

The mathematical stopping point is explicit: the new certificate gives a
small positive upper bound for J, not J=0 or a sequence of bounds tending to
zero. The final section of the proof records the failed completion arguments.
