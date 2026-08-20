# Review specification

Review in this order:

1. `L-99100.5--.9`: coefficient identities and the strict `1/8` reserve.
2. `L-99100.1--.4`: Radon--Nikodym cumulative-interval construction.
3. `R-99100`: reject total-mass-only ownership arguments.
4. `L-99101`: verify one common normalization denominator.
5. `R-99101`: reject expectation-only physical feasibility.
6. `L-99102`: verify that the actual constraint matrix is genuinely a network matrix with integral right-hand sides.
7. `M-99100`: reconstruct the native source-to-leaf interface.

Immediate falsifiers:

```text
weighted child not dominated in the common raw source;
normalization performed independently before partition;
source atom used by two children;
score or endpoint constraint absent from the integral leaf polytope;
feasibility asserted only in expectation;
construction chosen after reading the desired RH-bearing sign.
```
