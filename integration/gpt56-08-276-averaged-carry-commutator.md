# Integration handoff — averaged carry commutator

Branch:

```text
agent/gpt56-08/276-averaged-carry-commutator
```

Base:

```text
PR #269 head 4c67408f1dd7cd3d6574bafbf51c50a280bc0384
```

## New canonical connection

```text
PR #269 zeroth carry-window pole cancellation
-> uniform average of carry positions
-> PR #252 canonical carry-resolvent kernel
-> first logarithmic commutator
-> ordinary-prime top-quarter wavelet
-> exact discrete factor-five carry scalar
-> explicit bounded 3/8 boundary.
```

The new source is compatible with:

- PR #241: the local energy must use the independent-frequency normal Gram;
- PR #263: the parity-paired channels reconstruct `omega_2` finitely;
- PR #268: the same source has the bottom-charge consumer;
- PR #269: the discrete commutator uses exactly its factor-five wavelets and generalized-prime coefficients;
- PR #252: the uniform carry-position average is exactly its continuum carry kernel.

## Recommended canonical target

Replace the abstract final physical/carry source map by the exact scalar identity in `L-27604`. The remaining theorem should be registered as

```text
PAE:
int_J^(J+1)|P_omega(exp t)|^2dt=exp(o(J)).
```

A production proof may still use the full BCF5TC matrices, but it must reproduce the prime-annulus scalar and the `3/8` boundary as mutations.

## Status

```text
new exact source map             PROPOSED COMPLETE
new positive RH consumer         COMPLETE CONDITIONAL
PAE                              OPEN / RH-BEARING
RH                               UNPROVED
```
