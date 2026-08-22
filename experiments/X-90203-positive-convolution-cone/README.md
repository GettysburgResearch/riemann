# X-90203 — Positive Dirichlet-convolution cone replay

This package independently replays the finite arithmetic identities behind
`L-90203` and the source-cone part of `T-90203`.

Run:

```bash
python3 verify.py
```

The verifier uses only the Python standard library and exact
`fractions.Fraction` arithmetic.

A successful run prints:

```text
PASS_X_90203_POSITIVE_CONVOLUTION_CONE
```

It checks:

1. `b=mu*h` and `1*b=h` for a deliberately **nonmultiplicative** positive `h`;
2. arbitrary nonnegative prime-power extraction by a separable valuation potential;
3. exact factorization `b*g=h*(mu*g)` and pointwise domination;
4. embedding of a rational interior point of the real prime cube via
   `h_x(p^a)=1+x_p`;
5. the maximality probe `(b*v_p)(mp)=h(m)` for fresh primes `p`;
6. complete-additive versus strongly-additive prime-power extraction.

The endpoint-dilation formula in `T-90203` is a formal finite reindexing using
the already replayed critical scaling identity from `X-90201`; this package
does not duplicate the large GFEP kernel implementation.
