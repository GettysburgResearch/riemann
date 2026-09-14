## T-106600 — adaptive-scale shallow endpoint gate

The positive companion shift is not topologically forced to be constant.
For every holomorphic scale `a_T` that is real and strictly positive on the
real window, the endpoint quotient

```text
U_(5,a)
=(Xi-i a Xi')(Xi^(5)+i a Xi^(6))
 /(Xi+i a Xi')(Xi^(5)-i a Xi^(6))
```

has the same winding `R_0-R_5` as the constant-shift quotient.

Uniformly small analytic scales retain the closed `3/4000 N` denominator
height budget by the same regular-window Rouché argument as `L-106591`.
At height cutoff `1/100`, all deep directions still cost at most `3/40 N`.
The sole new gate is therefore:

```text
ADAPTIVESH106600:
choose one admissible positive analytic scale whose shallow
canonical-correlation defect is < 11/500 N.
```

It implies more than 90% using the pinned `R_5/N>997/1000-o(1)` input.
Constants are admissible, so this is a genuine weakening of
`SHALLOWCORR106591`, not a new burden.

Exact calibration: a monochromatic carrier with scale equal to reciprocal
frequency gives `U=-1` after reduction and zero Hankel charge.

Binding firewall: pointwise `U_a -> 1` can coexist with charge exactly one
because the denominator phase measure concentrates. No unweighted WKB or
pointwise-angle shortcut is used.

`ADAPTIVESH106600`, 90%, density one, and RH remain unproved.
