# Integration handoff — X-16207 v2 relative-normalization correction

Retain:

```text
source-derived normalized radial coefficient tail
source-derived normalized frequency-derivative tail
source-derived horizontal-strip coefficient tail
exact first-alias profile Gram
```

Withdraw from the first X-16207 packet:

```text
absolute source ||f^(4)||_1 as a unit-profile endpoint bound
endpoint point <=1e-5
endpoint L2^2 <=2e-10
deterministic error <=1/40000
```

Reason:

```text
unit-profile endpoint remainder
 = absolute source remainder / sqrt(first_alias_energy).
```

Add `R-16205`. Replace `L-16230` by its corrected radial/derivative-only
statement. The X-16207 v2 binder requires both:

```text
endpoint_relative_ledger.normalized_fourth_derivative_l1_upper
complete_arithmetic_alias.cross_error_upper
complete_arithmetic_alias.full_upper
```

before it emits any downstream profile-Gram or deterministic-error field.

Current status:

```text
normalized radial/derivative coefficient tails  closed
first-alias Gram                               closed
normalized endpoint remainder                  open
complete cross-alias operator                  open
production wrapper promotion                   refused
```
