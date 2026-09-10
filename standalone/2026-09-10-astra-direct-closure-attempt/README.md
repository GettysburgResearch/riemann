# Direct closure attempt after the exact-tail theorem

**Not a complete proof of RH.** This packet records an unsuccessful attempt
at the original global sign and cross-checks the new exact determinant route.
Read `ATTEMPT.md`, especially Sections 2 and 5. No predecessor is changed.

The first-order condition `Im(Q_N' conjugate(Q_N))<=0` in the upper critical
strip would suffice directly. It is **unproved**. Proving the stronger
normalized complex Laguerre sign would likewise suffice without an additional
normalization-error domination theorem. That is a simplification of the
logical endpoint, not a proof of its premise.

The manuscript establishes why two proposed finishing arguments do not work:
a fixed nonzero relative tail tolerance cannot certify the global sign, and
a positive singular-value operator does not give the required real spectrum.
Its explicit modified sources are not Xi and are never claimed to disprove RH.

This continuation was prepared in a session whose GitHub connection exposed
only reads. Publication has not been performed by this session. The intended
base is PR #835 at `4b8fa9abfa9aac5ed1feb7f30acaeeb418ed405c`.
The proposed independent branch is
`research/astra/20260910-direct-closure-attempt`.

Run the bounded algebra and inventory checks from this directory:

```sh
python -I -S -B check.py
python -I -S -B -O check.py
python -I -S -B test_check.py
python -I -S -B -O test_check.py
```

The checks are not a formal proof or an actual Xi evaluation. Full execution
scope is recorded in `VALIDATION.md`. Analytic statements await independent
review; no merge, source substitution, or canonical-status promotion is requested.
