# Validation and precise review boundary

Date: 2026-10-16. Status: same-author component proofs and finite checks.
No independent mathematical referee, proof assistant, upstream Lean build,
formal comparator, full repository validator or remote CI run was performed.
No numerical experiment on zeta zeros or a full field moment census was run.

## Executed

- `python verify.py`: PASS, reproduces results.json.
- `python -O verify.py`: PASS, byte-identical output.
- Python syntax compilation of verify.py and fetch_sources.py.
- Packet SHA-256 and Git-blob manifest creation, local hash verification,
  and ZIP round-trip verification.

The 791 finite predicates include 96 local power-series identities through
degree 36 (32 q/eta cases); 128 coefficient-mass predicates; 144 literal
prime-mask recursions; seven reconstructed paper-table rows; ten contour
checks; 380 rational exponent-model points; 17 scalar-bootstrap examples;
four version/loss checks; and five explicit false-substitution controls.
They are not 791 independent asymptotic cases. The integer mask tests use
all relevant integer ideals through each listed scale, a fixed character
modulo 5, and exclusions 2,3,5; they are NOT a general-field sextic census.
The diagnostic hard and polynomial windows are not smooth analytic tests.

The first script run exposed an accidental float in the reciprocal-series
constant (Python 1/int). It was replaced by explicit Fraction division,
and both full modes were rerun successfully. No mathematical claim rests
on the failed floating output. The final arithmetic is integer/rational.
The five negative controls are explicit disagreeing substitutions, not five
whole-package mutation runs. fetch_sources.py was syntax-checked only.

## What the checks do not authenticate

They do not prove normal convergence, Mertens' theorem, the prime ideal
theorem in a class, Dirichlet's unit theorem, theta compatibility, a native
moment upper bound, or any imported Lean result. Those are either named
classical inputs, analytic arguments written in the proof notes, or explicit
remaining hypotheses. Proof and verifier have the same author.

The source paper was read through web-rendered TeX/PDF, including screenshots
of the v1 theorem and v2 Table 1. Full paper bytes were not downloaded into
the execution container. A local git clone failed DNS; this packet is a
standalone local directory, not a clean full-repository clone. Publication
uses connected GitHub actions. The PR records the final immutable commit
and remote tree/blob read-back; that is a transport check, not proof review.

## Review priorities and invalidating gaps

1. EULER_STRIPPING Proposition 2: the coefficientwise inverse majorant,
   q^2 rather than q^3, shared-factor convolution, and same-height quantifier.
2. EULER_STRIPPING Proposition 1: local nonvanishing versus global product
   convergence; the angular character and the exact boundary Re(s)>1/2.
3. FIELD_MOMENT_BRIDGE: actual balanced integral prime generators, finite
   row count, prime-mask recurrence and finite scalar-exponent bootstrap.
   In particular the all-test moment hypothesis remains essential.
4. The boundary between the compact-test moment comparison and the fixed
   Gaussian detector; no automatic transfer between them is asserted.
5. PARAMETER_BARRIER: its stated restricted exponent regime, not a universal
   no-go claim about arithmetic or theta methods.

The smallest open analytic statements are the full native signed moment
estimate (FIELD_MOMENT_BRIDGE (4)) and, on the alternative route, a critical
bound for the coupled source detector (EULER_STRIPPING Section 5). Neither
is replaced by an imported finite-order half-plane or a randomized reference.
