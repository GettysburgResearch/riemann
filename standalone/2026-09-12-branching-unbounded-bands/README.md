# BUB26: unbounded protected bands, not a gap-free RH completion

Date: 2026-09-12. **Proposed component proofs; independent analytic review required.**

This continuation of PR #870 proves two scoped results for the unchanged
Gamma(5/2, rate 5/2), shared-uniform branching orbit.

**Explicit joint height/depth comparison.** At every height R and dyadic
resolution 2^-a, a fully specified integer depth D(R,a) ensures that every
critical-strip zero of every later iterate lies within 2^-a of an ACTUAL xi
zero. Separated contours preserve all multiplicities. The depth satisfies
D(R,a) <= (88/105)R + O((a+1)log(R+10)). This compares the whole divisor; it
does not assume or prove that the divisor is central.

**Unbounded exact protected bands.** Classical Conrey simple-zero density,
reflection pairing, and the comparison theorem give infinitely many disjoint
full-width critical-strip bands at unbounded heights. Each contains exactly
one simple central zero of every sufficiently late iterate. Counting bands
by their limiting ordinates gives at least (1/10-o(1))N(T) through height T.
The proportion is a corollary of Conrey's imported theorem, not a new record.
The bands may have arbitrarily small widths, leave gaps, and have different
required depths. No single finite depth protects all bands simultaneously.

**The user-requested gap-free expanding-window theorem and RH remain OPEN.**
A hypothetical off-central xi zero is faithfully shadowed too. The new bounds
do not remove that possibility or close the gap below #860's high-height cutoff.

## Read and reproduce

Start with [PROOF.md](PROOF.md), Sections 2--5, then the failed completion in
Section 8. [SOURCES.json](SOURCES.json) pins the parent and classical imports;
[VALIDATION.md](VALIDATION.md) distinguishes paper proofs, exact finite checks,
and unperformed work.

```sh
python -I -S -B check.py --check result.json
python -I -S -B test_check.py
python -I -S -B -O check.py --check result.json
python -I -S -B -O test_check.py
```

The executable performs only bounded integer/Fraction checks: five displayed
schedules, 29 dyadic schedules, 20 multiplicity-pairing panels, nine literal
moment stages and one synthetic degree-20 polynomial. It does not evaluate
xi, a new zero, an analytic contour, or Conrey's theorem. The five test methods
include ten actual altered-receipt CLI refusals per interpreter mode.
`--emit` is producer-only, not an accepting validation command.

## Review priorities

Check the safe-centred Euler--Maclaurin disk estimate; the full local zero
count and Blaschke/Harnack lower bound; Binet's uniform gamma lower bound;
the exact integer depth arithmetic; the clean-ordinate pairing count; and the
distinction between an unbounded disjoint family and an exhaustive cover.

No earlier research file or claim status is changed. This packet does not
resolve the alternative #859/#860 source histories. No formal verification,
full repository build, external priority or non-author acceptance is claimed.
