# X-91144 — Native-root capacity compiler and separator replay

Run:

```bash
python3 verify.py
```

Expected verdict:

```text
PASS_EXACT_NATIVE_ROOT_COMPILATION_SEPARATOR
```

The proof-grade checks are:

1. the finite rough-monoid convolution identity;
2. the exact PR #464/native capacity separator at `(X,q)=(136,2)`, with
   margin `>1/816`;
3. rational finite-vertex regressions for the leftmost optimizer theorem;
4. an exact failed-row Farkas fixture;
5. the finite \(Y_4\) recurrence and summation-by-parts identity.

The replay does **not** prove the Native-Root Capacity Theorem or RH. It proves
that the direct PR #464 compilation, with the rough reservoir retained, is not a
native certificate, and it validates the algebra used by the two fail-closed
successor routes.
