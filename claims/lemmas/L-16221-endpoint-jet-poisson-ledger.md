# L-16221 — Exact endpoint-jet ledger for every Poisson alias and radial remainder

Claim ID: `L-16221`  
Status: **PROVED ANALYTIC LEDGER; PROLATE JET-CORRECTOR ASYMPTOTICS OPEN**  
Authoring agent: `gpt56-pro-12`  
Created: 2026-08-01

## 1. Purpose

The radial PSWF has an oscillatory inverse-power far field. Bounding every
Poisson alias by absolute values before accounting for the endpoint terms is too
wasteful and, at the first inverse power, may not even be summable.

This lemma gives an exact finite endpoint expansion, sums each endpoint channel
through a polylogarithm, and bounds the remaining infinite alias tail by one
positive zeta constant. It supplies a directed proof interface for the second
requested gate.

## 2. Fourier endpoint expansion

Use

```text
Ff(xi)=integral_(-lambda)^lambda
 f(x)exp(2pi i xi x)dx.                                   (L-16221.1)
```

Let `p>=1` and assume

```text
f in W^(p,1)([-lambda,lambda]).                           (L-16221.2)
```

Repeated integration by parts gives, for `xi!=0`,

```text
boxed:
Ff(xi)
 =sum_(r=0)^(p-1)
  (-1)^r/(2pi i xi)^(r+1)
  [f^(r)(lambda)e^(2pi i lambda xi)
   -f^(r)(-lambda)e^(-2pi i lambda xi)]

 +(-1)^p/(2pi i xi)^p
  integral_(-lambda)^lambda
  f^(p)(x)e^(2pi i xi x)dx.                              (L-16221.3)
```

Thus the directed remainder bound is

```text
boxed:
|Rem_p(xi)|
 <=||f^(p)||_1/(2pi|xi|)^p.                              (L-16221.4)
```

No asymptotic notation occurs.

## 3. Exact alias summation

For `v>0`, define the aliases beyond the first sample

```text
b_f(v)=sum_(k>=2) Ff(kv).                                 (L-16221.5)
```

For `r>=1`, the `r`th endpoint channel in (L-16221.3) is absolutely summable and
is exactly

```text
E_r(v)
 =(-1)^r/(2pi i v)^(r+1)
  {f^(r)(lambda)
    [Li_(r+1)(e^(2pi i lambda v))-e^(2pi i lambda v)]

   -f^(r)(-lambda)
    [Li_(r+1)(e^(-2pi i lambda v))-e^(-2pi i lambda v)]}.
                                                                    (L-16221.6)
```

The `r=0` term is interpreted by symmetric summation. It is the elementary
periodic sawtooth furnished by `Li_1(z)=-log(1-z)`, with exact one-sided values
at resonances. A proof certificate must either:

1. retain this sawtooth channel with directed branch and endpoint conventions;
2. or impose `f(lambda)=f(-lambda)=0` so that it vanishes identically.

After the first `p` endpoint channels are retained, the remaining alias obeys

```text
boxed:
|b_f(v)-sum_(r=0)^(p-1)E_r(v)|
 <=[zeta(p)-1]||f^(p)||_1/(2pi v)^p,                     (L-16221.7)
```

for `p>1`.

Equation (L-16221.7) is obtained by summing (L-16221.4) at `xi=kv` and using

```text
sum_(k>=2)k^(-p)=zeta(p)-1.                              (L-16221.8)
```

## 4. Endpoint-jet cancellation

If

```text
f^(r)(+-lambda)=0,
0<=r<=p-1,                                                (L-16221.9)
```

then every explicit endpoint channel vanishes and

```text
boxed:
|b_f(v)|
 <=[zeta(p)-1]||f^(p)||_1/(2pi v)^p.                     (L-16221.10)
```

The positive-ray `L2` alias norm satisfies

```text
boxed:
||b_f||_(L2(lambda,infinity))
 <=[zeta(p)-1]||f^(p)||_1
   /[(2pi)^p sqrt(2p-1) lambda^(p-1/2)].                 (L-16221.11)
```

This is an explicit replacement for the unresolved qualitative alias estimate
in `L-16207`.

## 5. Derivative and horizontal-strip ledger

For an integer `q>=0`,

```text
partial_xi^q Ff(xi)
 =(2pi i)^q F(x^qf)(xi).                                 (L-16221.12)
```

If the endpoint jets (L-16221.9) hold, then the same jets vanish for `x^qf`.
Applying (L-16221.10) gives

```text
boxed:
|partial_v^q b_f(v)|
 <=[zeta(p-q)-1] C_(p,q)(f)/(2pi v)^(p-q),               (L-16221.13)
```

whenever `p-q>1`, where a fully explicit choice is

```text
C_(p,q)(f)
 =(2pi)^q sum_(j=0)^p binomial(p,j)
  (q)_(p-j) lambda^(q-p+j)||f^(j)||_1.                   (L-16221.14)
```

Here `(q)_k` is the falling factorial, with zero terms omitted. Equations
(L-16221.13)--(L-16221.14) follow by Leibniz applied to `(x^qf)^(p)`.

The Mellin transform of the omitted multiplicative tail is an integral of
`b_f(v)v^(-1/2+is)`. Bounds (L-16221.10)--(L-16221.14) therefore give directed
absolute convergence, differentiation in `s`, and holomorphic continuation to
every strip whose width is below the retained inverse-power margin. In
particular, `p>=3` gives a uniform first horizontal derivative after scaling.

## 6. Even sources and finite constraint cost

For an even source, endpoint values at `-lambda` are determined by those at
`+lambda`. Thus cancellation through order `p-1` costs only `p` independent
linear constraints:

```text
f^(r)(lambda)=0,
0<=r<=p-1.                                                (L-16221.15)
```

Together with the two exact radical constraints, the total codimension is
`p+2`. A prolate packet with `p+3` or more modes contains nonzero exact
radical-and-jet combinations.

The concentration defects of consecutive positive modes remain separated by
the same fixed `lambda^-8` ratio. Therefore a fixed number of extra jet
constraints may shift the first target and complement mode indices, but does
not destroy the eight-power hierarchy. What still requires proof is that the
jet-corrector determinants are uniformly nondegenerate and that the corrected
target continues to approximate the global Xi source.

## 7. Proof-producing schema

A directed certificate may contain:

```text
exact source coefficients;
interval endpoint jets f^(r)(+-lambda);
interval L1 bounds for f^(p) and (x^qf)^(p);
exact p,q,lambda;
directed polylogarithm enclosures for every retained E_r;
the positive rational bound for zeta(p)-1;
the final alias and strip budgets.                        (L-16221.16)
```

The checker performs only interval additions, products, powers, and one final
positive comparison. It never truncates the Poisson alias sum silently.

## 8. Strategic consequence

The requested task

```text
directed propagation of every Poisson endpoint and radial remainder
```

is closed at the analytic-ledger level by (L-16221.3)--(L-16221.14). The
remaining prolate-specific choice is explicit:

- retain the endpoint polylogarithm channels and prove their oscillatory
  zero-measure contribution is small;
- or impose enough endpoint jets to suppress them before applying the
  dimension-free local Weyl theorem.

## 9. Proof boundary

The endpoint expansion, polylogarithm summation and remainder bounds are exact.
This lemma does not prove the existence of a cofinal uniformly conditioned
prolate jet-corrector frame, nor does it prove RH.
