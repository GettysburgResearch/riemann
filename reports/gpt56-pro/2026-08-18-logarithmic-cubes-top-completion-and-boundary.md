# Logarithmic cubes, top-prime completion, and the final activation boundary

## Result of the pass

The post-`LAPBR67` root Bellman problem admits two independent sharpenings.

### Unfiltered route

The complete native rough cube is positive not merely through
`(log X)^(1/4)`, but through

```text
Z=(log X)^2 log log X.
```

The proof no longer requires the complete primorial to fit below `X`; it uses a
half-weight Rankin bound for the unactivated divisor tail. At the other end,
exact top-history completion turns every owner above

```text
H=exp((log log X)^4)
```

into a fully completed PNT state plus a short rough-product boundary controlled
by the upper-bound sieve. That whole high range is `O((loglog X)^-2)` against a
positive cube of order `1/loglog X`.

Thus the only unfiltered root correlation left is owner-supported on

```text
(log X)^2 loglog X < p < exp((loglog X)^4).
```

This is `QPCB67`.

### Constant-killing filtered route

The additional scale difference

```text
b^Delta(Y)=b(Y)-b(Y/4)
```

cancels the base's constant asymptotic coordinate and retains half of the
positive square-root term. It is Mellin-safe: it adds only another factor
`1-4^-s`.

The complete filtered cube can therefore be extended through

```text
Z=X^(1/(loglog X)^2).
```

Rankin's method makes every unactivated divisor tail exponentially smaller than
the positive Euler product. Exact top completion and PNT close every remaining
history whose terminal endpoint is at least `exp((loglog X)^2)`.

The sole survivor is a centered activation-boundary fluctuation on

```text
X/exp((loglog X)^2) < n <= X/2,
P^-(n)>X^(1/(loglog X)^2),
omega(n)<=(loglog X)^2.
```

The positive cube and this boundary cancel to leading order. The sign of the
centered remainder is `FABP67`; it is still open and RH-bearing.

## Exact new identities

The top-history completion is

```text
U_(P,<p)(Y)
 = sum_(S subset primes>p) 1/q_S
   U^(hat({p} union S))(Y/q_S).
```

It follows from the commuting identity `E_q+q^-1 T_q=I`. Summing owner `p`
and its top set gives every nonempty squarefree high-prime product exactly once.
At terminal endpoints below the omitted primes, the omitted state equals the
fully completed state literally.

## Replay

```bash
python3 experiments/X-97900-log-cube-boundary/verify.py
```

Expected:

```text
PASS_X_97900_LOG_CUBE_AND_BOUNDARY_ALGEBRA
171f49bf4688d0d54ac53e00e4aaef8d916f7e625beab82ebb47137d8dd1b352
```

The replay is exact-rational finite algebra plus non-probative parameter
hierarchy diagnostics. It does not replay PNT, Rankin asymptotics, the
upper-bound sieve, `QPCB67`, `FABP67`, or RH.

## Scientific status

```text
complete quadratic-log native cube       PROVED POSITIVE
quasipolylog high-owner range             CLOSED
QPCB67 unfiltered corridor                OPEN / RH-BEARING
constant-killing scale filter             PROVED EXACT
positive subpower filtered cube           PROVED
filtered interior histories               CLOSED BY PNT
FABP67 activation-boundary sign           OPEN / RH-BEARING
Riemann Hypothesis                        UNPROVEN
```