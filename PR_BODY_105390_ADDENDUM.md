## T105390 addendum — growing central-prefix capacity exclusion

**The Riemann Hypothesis remains unproved.**

### Growing trigonometric window

The real-saddle concentration now controls the normalized high-derivative Xi
functions on any fixed-height complex strip whose rescaled real length obeys

```text
Y_r / sqrt(r omega_r) -> 0.
```

Uniformly there, the normalized function and its first two derivatives differ
from sine or cosine by

```text
O((1+Y_r)/sqrt(r omega_r)).
```

Consequently every critical cell in a prefix `J_r=O(Y_r)` is real and simple,
with

```text
omega_r c_(r,j) = y_j + O(epsilon_r),
omega_r^2 rho_(r,j) = -1 + O(epsilon_r).
```

Thus the actual critical atoms converge uniformly to the tangent/cotangent
atoms throughout a growing prefix.

### Quantitative trigonometric tail reserve

After deleting the first `J` tangent or cotangent atoms, the remaining order-k
source matrix has

```text
lambda_min >= c_(k,a) J^(-d_(k,a)),

d_(k,a)=3k(k-1)+2+2a.
```

For both Stieltjes blocks one may use

```text
d_k=3k(k-1)+4.
```

This follows from an exact reciprocal-square Vandermonde determinant on `k`
consecutive tail atoms.

### Growing-prefix theorem

For fixed matrix order `k`, choose

```text
0 < gamma_k < 1/[2(3k(k-1)+5)],
J_r=floor(r^gamma_k).
```

The source approximation error and the actual-prefix atom error are both
`o(J_r^(-d_k))`, so the positive trigonometric tail margin wins. Therefore,
for all sufficiently high derivatives,

```text
C_(k,r,J_r)^(a) < A_(k,r)^(a),  a=0,1.
```

Explicit admissible exponents include

```text
k=1: gamma<1/10;
k=2: gamma<1/22;
k=3: gamma<1/46.
```

A polynomially growing central prefix cannot cause high-Xi capacity failure.
Every persistent failure must involve critical cells beyond that prefix,
nonreal or positive-residue events there, collective remote-tail overfilling,
or the outer exhaustion interface.

### Binding tail firewall

Prefix domination does not imply complete domination. The exact separator

```text
A=I,
C_prefix=(2/5)I,
C_tail=(7/10)I
```

has `A-C_prefix>0` but `A-C_prefix-C_tail<0`. The omitted Xi critical tail
remains open.

### Publication correction

`L-105386` is a non-normative malformed display draft. The clean compact-cell
theorem is `L-105387`, and all later dependencies use the corrected ID.

### Replay

```text
PASS_X_105390_GROWING_PREFIX_CAPACITY
200 exact rational checks
```

The replay authenticates reciprocal-square Vandermonde and growth-exponent
algebra only. It records the Xi real-saddle, growing-cell, complete-tail and RH
flags as false.
