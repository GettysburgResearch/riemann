# Positive triangular-window attack

Date: 2026-07-31  
Agent: `gpt56-05-l`  
Issue: #180  
Branch: `agent/gpt56-05-l/154-nonlocal-barta-floor`

## Requested objective

Prove either

\[
 \sup_x|Q_*(x)|<\infty
\]

or bounded Cesaro mean square for the pole-free prime statistic, thereby proving
RH.

## Outcome

No valid proof of either cofinal bound was found. The attack did, however,
remove the infinite-window complexity, derive several exact positive
representations, and identify the quantitative cancellation that every future
proof must supply.

## `L-15409` / `T-15406` — finite triangular universal window

Set `h=log 4`, let `b_h` be the normalized box on `[0,h]`, and let
`F_h=b_h*b_h`. The signed window

```text
G_h(u)=F_h(u)-2F_h(u-h)
```

has only three linear pieces and support `[0,3h]`. Its transform is

```text
Ghat_h(z)=((1-exp(-hz))/(hz))^2(1-2exp(-hz)).
```

The first factor has zeros only on `Re z=0`; the second cancels the shifted zeta
pole and has all zeros on `Re z=1/2`. Hence no shifted off-line zero in
`0<Re z<1/2` is canceled.

The raw statistic

```text
Q_h(x)=sum Lambda(n)/sqrt(n) G_h(x-log n)
```

uses exactly the prime powers in a ratio-64 annulus. RH is equivalent to either
boundedness or bounded Cesaro mean square of this one function.

The independent four-hinge formula is

```text
Q_h=h^-2[K(x)-4K(x-h)+5K(x-2h)-2K(x-3h)],
K(x)=sum_(log n<=x) Lambda(n)/sqrt(n)(x-log n).
```

## Exact Abel--Hardy target

Bounded Cesaro mean square is equivalent, up to explicit constants, to

```text
sup_(sigma>0) sigma/(2pi) integral_R
|Ghat_h(sigma+it) zeta'/zeta(1/2+sigma+it)|^2 dt < infinity.
```

This permits the simple boundary poles arising from critical-line zeros and
excludes every interior pole.

## `L-15410` — positive primitive and screw bridge

A compact kernel `H_h>=0` satisfies

```text
A_h(x)=sum Lambda(n)/n H_h(x-log n)>=0,
Q_h(x)=exp(x/2)A_h'(x),
A_h(x)->1/log4.
```

Thus the positive theorem is a critical weighted derivative estimate for a
positive convergent arithmetic function.

The same `Q_h` is one fixed finite difference of Nakamura--Suzuki's exact zeta
screw function plus a completely explicit `O(exp(-5x/2))` correction. The
prime-window and screw/infinite-divisibility programmes are the same route.

## `L-15412` / `L-15413` — renewal and Markov absorption

The logarithmic measures

```text
nu=sum 1/n delta_(log n),
mu=sum Lambda(q)/q delta_(log q)
```

obey exactly

```text
mu*nu=t nu.
```

Hence the positive primitive solves a causal renewal equation with an explicit
all-integer forcing.

For a moving probability law

```text
pi_x(N) proportional to log(N)/N * H_h(x-log N),
```

`A_h/Z_h` is exactly the probability that one step of the von Mangoldt downward
chain lands at `1`.

The desired bound requires `exp(-x/2)` cancellation between two polynomial-size
derivatives of this absorption mass. Ordinary Markov contractivity and the PNT
asymptotic do not supply that scale.

## `L-15411` — exact mean-square barrier

The diagonal prime-power contribution over logarithmic length `X` is

```text
(4/(3 log4)) X^2 + O(X).
```

Therefore an `O(X)` total mean square requires the signed off-diagonal
correlations to contribute

```text
-(4/(3 log4)) X^2 + O(X).
```

This rules out any proof whose final step drops cross terms, takes termwise
absolute values, or uses only a prime number theorem error estimate.

The required cancellation may be represented as:

- a signed compact prime-pair autocorrelation;
- a critical renewal square function;
- a compensated von Mangoldt-chain martingale energy;
- a finite-difference conditional-negative-definiteness statement for the screw
  function.

## X-15405

The standard-library Fraction checker reconstructs:

```text
(1-r)^2(1-2r)=1-4r+5r^2-2r^3,
```

the double root at `r=1`, the pole root at `r=1/2`, the normalized window energy
`8/3`, and a nontrivial direct-versus-hinge value `1/15`.

Eight adversarial tests pass.

## Literature synthesis

- Brent--Platt--Trudgian quantify the RH-conditional critical mean square of the
  PNT error and show false RH makes the normalized mean square unbounded.
- Nakamura--Suzuki identify infinite divisibility of `exp(g_zeta)` as an RH
  criterion.
- Alexeev et al. develop von Mangoldt downward/upward chains and an invariant
  zeta-process weight from the same divisor identity.
- Current zero-density and PNT techniques do not exclude one off-line zero and
  therefore do not prove the uniform square function.

## Truth boundary

```text
finite triangular criterion       PROPOSED
positive primitive identity       PROPOSED
renewal and absorption identities PROPOSED / elementary core
exact window checker              8/8 finite tests
critical square-function bound    NOT PROVED
Riemann Hypothesis                NOT PROVED
```

## Next analytic target

Construct a compensated carré-du-champ identity for the upward/downward von
Mangoldt adjoint pair whose quadratic variation is exactly the signed
triangular prime-pair kernel and is `O(X)`. This is Issue #180.
