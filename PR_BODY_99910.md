## Purpose

Continue PR #665 from exact head
`a771772682a2c09c026348b176618c302c49c223` and compress its corrected
seven-band decorated-`beta` shell to the smallest possible ordinary-Mobius
wavelet.

**The Riemann Hypothesis remains unproved.**

## Main exact result

The unique minimal causal dyadic annihilator of the local box modes
`sqrt(y), 1, log(y)` is

```text
D=(I-sqrt(2)S_2)(I-S_2)^2.
```

Its image has support only in

```text
[1,8] union [67,536]
```

and satisfies the exact anti-symmetry

```text
(DW)(67y)=-(DW)(y),  1<=y<=8.
```

Therefore

```text
D B = (I-S_67) G_beta,
G_beta = (I-67^(-1/2)S_67) G_mu,
```

with both inverses positive. The final scalar is

```text
G_mu(X)=sum_(X/8<=n<=X) mu(n)n^(-1/2)K_0(X/n),
```

where `K_0` has only three activation bands.

## Analytic consumer

```text
Mellin(G_mu)(s)
 = (s+3/2)(1-sqrt(2)2^-s)(1-2^-s)^2
   / [s^2(s-1/2)zeta(s+1/2)].
```

No open-strip reciprocal-zeta pole is cancelled. Subpower logarithmic
negative mass of `G_mu` implies RH, and RH gives the converse.

Pointwise positivity is false already at `X=4`:

```text
-1.4620 < G_mu(4) < -1.4618.
```

Thus the remaining theorem is a fixed ratio-eight signed Hardy/Carleson
estimate, `MWOC99910`.

## Replay

```bash
python3 experiments/X-99910-minimal-mobius-wavelet/verify.py \
  --output experiments/X-99910-minimal-mobius-wavelet/results/verification.json
sha256sum -c T99910_CONTENT_SHA256SUMS
```

Expected:

```text
PASS_T99910_MINIMAL_MOBIUS_WAVELET
2196daa3e18202a0c20a5a3a596dd3975989bea035934db1d4bdf7ff842239fa
```

## Exact boundary

```text
minimal dyadic annihilator                   PROVED
factor-67 two-shell anti-symmetry             PROVED
positive box desmoothing                      PROVED
positive duplicate-67 source resolvent        PROVED
ordinary-Mobius ratio-eight shell             PROVED
Mellin/Landau equivalence                     PROVED
three-band / three-state Hardy compression    PROVED
pointwise wavelet positivity                  REFUTED
MWOC99910 signed cross-core packing           OPEN / RH-EQUIVALENT
Riemann Hypothesis                            UNPROVEN
```
