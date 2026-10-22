# Maximal positive-convolution cone and the empty-boundary frontier

Date: 2026-08-10  
Branch: `research/gpt56-pro/90102-liouville-bernstein-extremality`  
Status: exact theorem continuation; RH unproved

## 1. Why continue past the Boolean hierarchy

`L-90201/T-90201` showed that the real multiplicative cube has no independent
nonempty obstruction: its mixed derivatives are positive sums of proper
Möbius descendants. The next question was whether this was a special property
of complete multiplicativity or the shadow of a larger cone.

It is the latter.

Every normalized arithmetic source `b` has a unique factorization

```text
b = mu * h,
h = 1 * b.
```

The exact natural cone is simply

```text
h(1)=1,
h(n)>=0.
```

No multiplicativity of `h` is needed.

## 2. Maximality

For any separable valuation potential

```text
g(n)=sum_p phi_p(v_p(n)),
ell(p^a)=phi_p(a)-phi_p(a-1)>=0,
```

one has exactly

```text
mu*g = ell,
```

where `ell` is supported on prime powers. Therefore

```text
(mu*h)*g = h*ell >= ell = mu*g.
```

Conversely, the localized probes `g_p=v_p` recover the cone coordinate:
for a fresh prime `p` not dividing `m`,

```text
(b*v_p)(mp)=h(m).
```

So this is the **maximal** normalized source cone preserving every elementary
prime-valuation extraction. The completely multiplicative real cube is the
small multiplicative face

```text
h_x(p^a)=1+x_p.
```

This subsumes both the logarithmic and completely-additive Bernstein formulas
and also covers ordinary primes alone by taking strongly-additive valuation
potentials.

## 3. Endpoint descendants

For every critical scaled kernel,

```text
c_X(ad)=a^(-1/2)c_(X/a)(d),
```

and hence

```text
F_(mu*h)(X)
 =sum_a h(a)/sqrt(a) F_mu(X/a).
```

For a GFEP exit this is

```text
Sigma_(mu*h)(X,n,p)
 =sum_a h(a)/sqrt(a) Sigma_mu(X/a,n,p).
```

For the sparse producer the same formula holds with `n A_X(n)`.

Thus **every** deformation in the maximal positive cone is a positive dilation
superposition of true smaller-endpoint arithmetic. At a first failure, the
Möbius point is automatically the minimizer over the whole cone. The old WHT
class searches were finite shadows of this source-cone fact.

The unit source is `mu*1=epsilon`, so the empty renewal

```text
c_X(1)=sum_a a^(-1/2)F_mu(X/a)
```

is exactly the extreme positive deformation from the Möbius boundary to the
unit source. Its inverse is Möbius signed. That inversion is the precise place
where positivity is lost.

## 4. Ramp consequence

For the complete ramp,

```text
(mu*h)*log = h*Lambda,
```

and therefore

```text
Ramp_(mu*h)(X)
 =sum_a h(a)/sqrt(a) Ramp_mu(X/a)
 >=Ramp_mu(X).
```

So the uniform Form-A criterion remains unchanged even when the real prime
cube is enlarged to the entire maximal positive-convolution cone. Together
with `T-90202`, uniform Form A over this cone is equivalent to RH. This is a
criterion, not an unconditional proof.

## 5. Hostile continuation checks

Several tempting attempts were tested after the cone theorem.

### Fixed/adaptive Abel order

For the sparse producer, higher cumulative transforms of the Möbius-divisor
kernel often become nonnegative at surprisingly low orders (orders 4, 5, 6 at
several deep test points). But the minimal order does not obey the guessed
simple arithmetic-depth law: a shallow `X/n=5` case already violates that
formula. Moreover high-order discrete Abel transfer encounters the zero-extension
boundary of `w_X`; the critical weight is completely monotone in the interior
but not to arbitrary order across its finite endpoint. No sign theorem is
promoted from this reconnaissance.

### Sieve interpretation

The positive coefficient kernel behaves numerically like a dimension-one
sieve density:

```text
c(kp)/c(k) approximately 1/p.
```

This explains the dramatic effect of multiplicativity, but a generic
dimension-one lower-bound sieve at full sifting depth meets the classical
parity barrier. Local-density information alone therefore does not settle the
empty coefficient. A valid continuation must exploit the fragmentation/path
structure beyond those marginals.

### Diagonal root phenomenon

The common-prime-sign polynomial

```text
P(z)=sum_(k squarefree)c(k) z^omega(k)
```

continues to show all roots real and strictly left of `-1` over extensive
reconnaissance, including the sparse producer and nonnegative exit mixtures.
This is potentially stronger structure, but no proof has been obtained and it
is not promoted here. At `z=-1`, its value is exactly the Möbius coefficient,
so any theorem pinning the nearest root left of `-1` would itself close the
live sign problem.

## 6. Revised frontier

The multiplicative-bootstrap source question is now exhausted exactly:

```text
free signs                         too large / refuted;
completely multiplicative signs    descendant arithmetic;
full real prime cube               positive-convolution face;
all positive convolutions mu*h     maximal cone, classified;
empty Möbius boundary coefficient  OPEN / RH-bearing.
```

The productive next attacks must use information destroyed by arbitrary
positive convolution. The two most concrete such structures presently visible
are:

1. the fragmentation/path geometry of the sparse producer;
2. the prime-endpoint positive-occupancy/mean-age state on PR #353.

No complete unconditional RH proposal is claimed.
