# Integration handoff — X-16207 source-derived moat

Add:

```text
L-16230  adaptive cofinal decay of source-derived radial/endpoint fields
X-16207  fail-closed source-derived moat emitter and checker
```

Replace in production certificates:

```text
tail_l2_sq_upper                 1       -> source-derived
derivative_tail_l2_sq_upper      4       -> source-derived
derivative_l1_upper              10^100  -> source-derived
scalarization.deterministic_error       -> reconstructed, not declared
```

Do not populate `profile_gram.lower` from the first alias alone. Require

```text
complete_arithmetic_alias.cross_error_upper
complete_arithmetic_alias.full_upper
```

and bind

```text
profile_gram.lower
 = first_alias.lower-cross_error_upper.
```

Current status:

```text
source fields and deterministic error  closed
first-alias Gram                       closed
complete cross-alias operator          open
production wrapper promotion           refused
```
