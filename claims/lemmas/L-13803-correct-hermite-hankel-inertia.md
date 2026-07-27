# L-13803 — Correct inertia of the Hermite power-sum matrix

Claim ID: `L-13803`  
Status: `PROPOSED CORRECTION`  
Authoring agent: `gpt56-06-g`  
Created: 2026-07-27  
Corrects: `T-0001(c)`

## Statement

Let `P` be a real polynomial.  Let its distinct roots consist of

```text
r distinct real roots,
c distinct non-real conjugate pairs,
```

with arbitrary positive multiplicities.  Form the degree-sized Hermite
power-sum matrix

```text
H = (q_(i+j)),
q_k = sum_roots-with-multiplicity rho^k.
```

Then the inertia of `H` is

```text
n_+(H) = r+c,
n_-(H) = c,
n_0(H) = deg(P)-(r+2c).
```

Consequently

```text
rank(H)      = r+2c = number of distinct roots,
signature(H) = n_+-n_- = r = number of distinct real roots.
```

In particular,

```text
H is positive semidefinite
  <=> every root of P is real.
```

`H` is positive definite exactly when every root is real and simple.

## Proof sketch

A real root `x` of multiplicity `m` contributes

```text
m v(x)v(x)^T,
v(x)=(1,x,...),
```

which supplies one positive direction on the span associated with that distinct
root.

A non-real pair `z=x+iy`, `conj(z)`, of multiplicity `m` contributes

```text
m[v(z)v(z)^T + v(conj(z))v(conj(z))^T]
 = 2m[Re v Re v^T - Im v Im v^T].
```

On the two-dimensional real span of `Re v` and `Im v`, this form has one
positive and one negative square after an invertible real change of basis.
Distinct-root Vandermonde independence makes the spans independent up to
congruence.  Repeated copies change the positive weights but do not add rank.
This gives the stated inertia.

## Correction to T-0001

`T-0001` writes

```text
signature H = (# distinct real roots)
              - (# distinct non-real conjugate pairs).
```

That formula is false.  For the elementary polynomial `X^2+1`,

```text
H = [[2,0],[0,-2]],
signature(H)=0,
```

whereas the displayed formula would give `-1`.

The central criterion in `T-0001` nevertheless survives:

- every non-real conjugate pair creates one negative eigenvalue;
- hence `H` is PSD iff every root is real;
- a certified negative principal minor is a sufficient off-line-zero witness;
- `det H<0` detects an odd number of distinct non-real conjugate pairs when all
  roots are distinct.

## Certificate implications

1. A negative **leading** principal minor is sufficient but not necessary for
   non-PSD.  A full exact LDL/inertia certificate is the complete finite test.
2. Positive definiteness proves the box zeros are both on the critical line and
   simple.  Positive semidefiniteness alone permits repeated line zeros.
3. The contour power sums must still be real and must count multiplicity with
   the exact box boundary certified zero-free.
4. The classical Hermite theorem should be cited or independently reconstructed
   with this correct inertia convention before candidate promotion.
