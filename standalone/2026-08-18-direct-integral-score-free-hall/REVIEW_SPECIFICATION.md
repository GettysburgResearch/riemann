# Review specification for T-99020

Review in this order:

1. `R-99020` normalization.
2. `L-99020` Hall prefixes, score sign and row profile.
3. `L-99021` source ownership, causal identity and actual child mass.
4. `L-99022` endpoint-frame normalization and direct integration.
5. `L-99023` all-column and terminal constants.
6. `L-99024` literal-score recurrence.
7. `L-99025` benchmark and endpoint consumer.
8. `T-99020` composition.
9. Checker, mutations, hashes and locks.

Immediate falsifiers:

```text
negative Hall prefix in 1<=x<67;
negative component-row bonus;
Hall bonus assigned declared score or a child;
source occurrence with two owners;
actual child target mass >= parent/8;
wrong equality-score normalization;
q<K overfill after the stated thinning;
terminal source both output and omitted;
use of Y4 to price the complete J deficit;
incorrect prime-square or Mellin pole normalization.
```
