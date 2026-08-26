# Primewise flat gauge and endpoint-owner normal form

## Result

The complementary-temperature family is not merely one-dimensional. On every
finite horizon, every labelled prime may carry its own real or complex
temperature while the product source remains exactly

```text
eta*eta = beta*beta_square.
```

All coordinate connections commute and have zero curvature.

## Canonical gauge

For one prime, the combined free-energy coefficient is

```text
|1-t_p|^2 + |t_p|^2
  = 1/2 + 2|t_p-1/2|^2.
```

Thus `t_p=1/2` is the unique local minimum and the unique first-chaos-balanced
split.

A source-owned sparse set of labels may instead use endpoint temperatures
`0` or `1`. The energy cost is

```text
exp(O(sum_(p in S) 1/p)),
```

which is polylogarithmic on every finite horizon.

## Exact owner placement

At an endpoint, the local target

```text
(1-x)(1-x^2)
```

has a unique allocation of exponents `0,1,2,3` between one native factor and
one squared factor. Hence every selected owner or discrepancy prime can be
placed on one physical side before phases and collapse, without changing the
detector.

## Walsh form

Let

```text
M=(E+C)/2,
D=(E-C)/2.
```

Then

```text
EC=M^2-D^2,
D^2=x^2(1-x)^2/4.
```

Independent endpoint-color averaging removes all mixed midpoint/fluctuation
coordinates. Every nonempty color variance begins at squared activity. The
only critical mean coordinate is the arithmetic midpoint square, which is
subcritically gauge-equivalent to the geometric midpoint square.

## Exact scientific boundary

The new packet removes:

```text
global-temperature rigidity;
owner-factor assignment ambiguity;
discrepancy-factor assignment ambiguity;
all nonempty endpoint-color critical variance.
```

It does not orient the remaining arithmetic midpoint core. The primewise first-
chaos sum is always `-1`, and arithmetic convolution is not pointwise
multiplication.

The surviving interface `PCOI102930` is a normal form of the existing
`SGIC102890` / `CTZD102897` endpoint difficulty, not a third independent
criterion.

```text
PASS_T102930_PRIMEWISE_FLAT_GAUGE
31dc10d61baa6633f810387c102458642885f18c9b9e561529803ce271c6da79

PCOI102930  open / RH-bearing
RH           unproved
```
