# Wick second-chaos continuation of the common-mother programme

## Decision

The fixed outer-ray frontier still contained a visible singleton-prime carrier.
Rather than applying another regional norm, this continuation changes to the
exact Wick gauge and removes that carrier coefficientwise.

## Exact source identity

For labelled prime shifts `x_p=p^-1/2 U_p`,

```text
E = product(1-x_p),
S = product(1-x_p^2),
L = sum x_p,
R = product exp(x_p)/(1+x_p),
```

one has

```text
E = S R exp(-L).
```

Moving the gauge-covariant carrier `-RSL` once leaves

```text
D_>=2
 = R S integral_0^1 (1-t) [L exp(-tL/2)]^2 dt
   +(R-1)S.
```

The root and full first chaos have disappeared. The hard source is a continuous
average of squares of one root-free field.

## Closed costs

The free labelled `H^4` norm of the square field is polylogarithmic because

```text
V=sum_p 1/p+1/67 = log log Y+O(1)
```

and complex Khintchine plus the Steinhaus exponential moment gives

```text
||W_t^2||_H2^2 << V^2 exp(2V).
```

Same-product convolution multiplicity is subpower by the divisor bound. The
Wick and squared gauges cost only polylogarithmically.

## Remaining interface

A generic cluster of distinct logarithmic frequencies amplifies free energy by
an arbitrary factor, so the free estimate does not prove physical collapse.
The sole remaining term is the distinct-product restriction of the root-free
second-chaos square after exact greatest-owner and regional recombination.

```text
WNC102743
  -> OER102780
  -> AR-DEFECT102600
  -> RH.
```

`WNC102743` remains unproved and RH-bearing.

## Strategic meaning

The physical frontier no longer contains:

```text
unit/root coordinate;
singleton-prime carrier;
free labelled energy;
same-product factor pairs;
duplicate owner multiplicity.
```

The remaining operator is a literal arithmetic restriction theorem for two or
more distinct prime labels. The Wick, half-divisor and Euler coordinates are
now three exact gauges of that same source.
