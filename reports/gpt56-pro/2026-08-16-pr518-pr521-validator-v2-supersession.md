# Validator v2 supersession note

The mathematical review and its activation-knot counterexample are unchanged.

The original lightweight `verify.py` encoded the strict primitive estimate

```text
log(4) > 4/3 and sqrt(134) < 12
```

as the false rational assertion

```text
(4/3)/12 > 1/9.
```

The rational endpoints are equal; strictness comes from the two strict primitive inequalities. Consequently the original executable and its predeposited result are superseded for publication-authentication purposes.

The corrected fail-closed executable is

```text
experiments/reviews/X-94030-pr518-activation-and-pr521-registry/verify_v2.py
```

with verdict and proof object

```text
PASS_PR518_PR521_VALIDATOR_V2
53a713f47f0db6ed47614c6399f62ff52e2a182431b8c1436cec6c614b4f7f90
```

It independently recomputes the exact activation witness, the 327 source atoms, 2473 finite occurrences, four zero boundaries, 132 terminal primes, the negative-q2/JNTLC firewalls, and the exclusion of PR #508 interval evidence.

```text
scientific verdicts changed    no
old executable                  superseded
validator v2                    controlling
RH                              unproved
```
