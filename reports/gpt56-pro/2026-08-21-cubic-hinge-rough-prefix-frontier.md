# Cubic hinge / compensated rough-prefix frontier

## Decision

The post-`T100710` matrix cannot separate its source regions before the leading
carrier cancels.  The newest cubic matrix on PR #691 preserves that carrier and
reduces all possible negativity to joint min--max mixed-activation collars.
This pass opens those collars exactly rather than applying another regional
absolute norm.

## Main identities

In square-root coordinate `t=sqrt(y)`, the critical cubic is

```text
Psi(t^2)
 = 384 integral_0^1 (t-s)_+ (1-s) ds
 = 192t - 64 + 64(1-t)_+^3.
```

For endpoints `p<q` and interior prime interval `P`, the physical entry is

```text
H = positive deep carrier
    + 64 Delta_p Delta_q E_P (1-t)_+^3.
```

The derivative is a positive coarea of one explicit arithmetic scalar:

```text
B_(p,q;P)(x)
 = A_P(x)
   -p^(-1/2)A_P(x/p)
   -q^(-1/2)A_P(x/q)
   +(pq)^(-1/2)A_P(x/(pq)),

A_P(x)=sum_(d<=x,d in <P>) mu(d)/d.
```

Tao's semigroup theorem gives `|A_P(x)|<=1`, hence a derivative bound uniform
in the number and length of the interior prime interval.

The centered collar has a third derivative with coefficients `d^-2`, endpoint
weights `p^-3/2,q^-3/2`, and step supports `sqrt(d)`.  Its total variation is
therefore controlled by the convergent prime `3/2` mass.  The same remains true
after averaging against the exact joint min--max source law.

## Two source-owned certificates

Taylor expansion from the activation origin and from the completed deep end
gives positive quantities `L_(p,q;P)` and `R_(p,q;P)` satisfying

```text
H_-^2 <= L R.
```

They are attached to the same source occurrence before any first-owner or
largest-owner marginal is taken.

```text
left certificate:
  finite compensated prefix / activation origin;

right certificate:
  future product boundary / completed carrier.
```

Their joint-min--max averages define `LPCC100723` and `FPCC100723`.  The exact
composition proves

```text
LPCC100723 AND FPCC100723 -> RH.
```

## What is closed

```text
cubic hinge and carrier/collar split       exact
arithmetic rough-prefix derivative          exact
uniform history-free derivative bound       proved
third-variation source                      summable
finite source exhaustion                    exact
same-occurrence left/right Taylor gate       exact
```

## What remains

The two critical integrated certificate estimates remain open.  The uniform
regularity bounds do not imply them: a scaled compact cubic bump has uniformly
bounded derivative and third variation while its logarithmic negative mass is
of square-root size.

The proper next attacks are therefore:

1. **LPCC:** combine the compensated-prefix coarea with first-owner finite
   prefix and activation-endpoint tools, without taking absolute values before
   the four endpoint terms cancel;
2. **FPCC:** combine the right Taylor tail with largest-prime interior
   squaring and positive divisor renewal, retaining the same joint min--max
   coefficient.

RH remains unproved.
