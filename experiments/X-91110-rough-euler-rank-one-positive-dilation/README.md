# X-91110 — Rough Euler rank-one positive dilation

This exact `Fraction` replay checks `L-91323` on generic rational controls.

It verifies:

```text
J Mtilde(A,B) = M(A,B) J;
Mtilde(A,B) is entrywise nonnegative for 0<=B<=A;
two-factor positive composition retains the physical action;
adding (A-B)R(2,1) makes the physical output nonnegative;
no smaller coefficient on the ray (2,1) works for every L,R>=0.
```

Run:

```bash
python3 verify.py
sha256sum -c SHA256SUMS
```

Retained verdict:

```text
PASS_ROUGH_EULER_RANK_ONE_POSITIVE_DILATION
```

The replay proves finite algebra only. The physical-column projection and the
scalar auxiliary-port capacity inequality remain open.
