# 2026-08-01 — The flat trial is erased by line-centered harmonic shorting

## Objective

Attack the sole remaining factorial-packet inequality

```text
R_M* A_WW,M^-1 R_M
 <= <A_M x_M,x_M> + g_M epsilon_M,
Lambda_M epsilon_M + delta_M -> 0.
```

The requested strategy was to put the trial energy and inverse-metric residual
into one centered-Chebyshev or line-centered contraction.

## Exact result

That contraction is now explicit. For a positive line-centered comparator

```text
H0=[[a,r*],[r,C0]], C0>0,
```

every source-normalized trial `x=e+w` shorts to the same canonical vector

```text
y0=e-C0^-1 r.
```

For `H=H0+E`, the actual source Schur value is exactly

```text
S(H)=S(H0)+<E y0,y0>
     -(P_W E y0)* C^-1 (P_W E y0).
```

Thus the graph energy and residual are indeed one joint object, but the object
is evaluated on `y0`, not on the chosen flat trial.

## Negative-channel formula

If the horizontal/off-line part is diagonalized into a finite negative channel

```text
U=[alpha;B],
H=H0-UU*,
```

then

```text
Delta=I-B* C0^-1 B,
d=alpha*-B* C0^-1 r,
```

and, whenever `Delta>0`,

```text
S(H)=S(H0)-d* Delta^-1 d.
```

This is the exact conditional defect that the inverse constrained metric was
hiding.

In an orthogonal-polynomial representation it becomes the negative Uvarov
formula

```text
h_n(new)
 =h_n-p_n(Z)*[T^-1-K_(n-1)(Z,Z)]^-1 p_n(Z).
```

The lower block is positive when the bracket is positive. The source sign is
the next Christoffel increment.

## Scope correction for the factorial packet

The raw flat vector can have a factorial zero at a fixed off-line parameter.
After harmonic shorting, its constrained component is removed exactly. The
conditional amplitude is independent of the trial:

```text
U*x-B*C0^-1(P_W H0 x)
 =alpha*-B*C0^-1 r.
```

Therefore the factorial estimates of `L-20804/L-20805` do not enter the source
Schur gate unless one additionally proves:

1. the canonical graph itself has the factorial notch; or
2. the flat trial is asymptotically harmonic in the `C0` metric.

Neither statement was previously proved.

## Exact replay

`X-20805` verifies the theorem over `Fraction`. Two very different trials
short to

```text
(1,-9/46,8/69).
```

The actual constrained block remains positive, yet a finite negative channel
changes the comparator source floor `5/4` into

```text
-7394941/7329456.
```

Direct block inversion and the Woodbury conditional-defect formula agree
exactly. Seven mutation tests pass locally.

## Correct production target

The next genuine D-0001 packet should emit

```text
positive line-centered comparator H0,
constrained block C0,
canonical source graph y0,
negative/horizontal conditional defect Delta,
conditional source amplitude d,
actual constrained block C,
source Schur = S0-d*Delta^-1 d.
```

Equivalently, it may emit the joint graph energy and residual of `L-20806.13`.
The flat vector remains useful only as an independent candidate producer and as
a possible approximation to `y0`; it cannot be substituted for `y0` in the
consumer.

## Honest frontier

The requested inequality has not been proved. It is now reduced without a trial
artifact to

```text
d_M* Delta_M^-1 d_M
 <= s_(0,M)+epsilon_M,
Lambda_M epsilon_M+delta_M -> 0.
```

On a complete hierarchy this conditional Christoffel moat is RH-bearing. Under
a false-RH off-line cardinal, either `Delta_M` loses positivity or the quotient
leaves a fixed negative source gap.

No RH conclusion is claimed.
