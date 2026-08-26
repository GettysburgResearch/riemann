# X-105500 — Native F1 tail-pair replay

This finite replay supports `T-105500`.

It verifies:

```text
exact dyadic polynomial (I-S)^2(I-sqrt(2)S)^2;
local endpoint rigidity of contraction-free squarefree factorization;
prime-color factorization of finite Möbius Euler products;
prime-color covariance of the balanced Vaughan source;
a_U = 1*nu_U and a_U*a_U*mu = a_U*nu_U;
b_U(n)=0 for n<=U^2;
explicit derivative same-K1 kernel and all five jumps;
right-endpoint Hardy identity and atomic jump filter;
reflection alignment/mismatch polarization;
exact signed-cell negative-area primitive.
```

Run:

```bash
python experiments/X-105500-native-f1-tail-pair/verify.py
```

Expected banner:

```text
PASS_T105500_NATIVE_F1_TAIL_PAIR
e25255643bfd11e9fc931b4484189d0f6178bcf5537f39d734acb0b3da84a386
checks=161264
rh_established=false
```

The reported native negative mass through `5000` is a regression diagnostic
only.  The replay proves neither `NATIVEF1XD105504`, `NATIVECELL105504`, nor
RH.
