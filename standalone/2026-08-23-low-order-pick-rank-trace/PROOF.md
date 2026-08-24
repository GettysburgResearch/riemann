# The low-order residue Pick matrix

Let `p` be real of degree `n` and assume first that `p'` has simple zeros not
shared by `p`. With

```text
q=p/p',   rho_c=p(c)/p''(c),
```

partial fractions give

```text
q(z)=z/n+alpha+sum_c rho_c/(z-c).
```

Hence the affine-centered Pick divided difference is

```text
K_p(z,w)
 = [q(z)-conj(q(w))]/[z-conj(w)]-1/n
 = -sum_c rho_c/[(z-c)(conj(w)-c)].
```

Every finite observation produces a Hermitian congruence of this source
matrix. At a real `c`, the atom is `-rho_c u_c u_c*`; it is positive exactly
when the extremum is Rolle-generating. A nonreal conjugate pair has coefficient
matrix

```text
[ 0       -rho ]
[-conj(rho)  0  ]
```

and therefore one positive and one negative eigenvalue. A real pole of order
`m` gives an anti-triangular Hankel block congruent to a scalar multiple of the
reversal matrix and has positive index at most `ceil(m/2)`; a nonreal pair of
order `m` has positive index at most `m`.

For any compression `K`, if `G` is the number of good simple real critical
points and `nu` is the nonreal/confluent positive-index charge, then

```text
n_+(K) <= G+nu,
(tr K)_+^2 <= n_+(K)||K||_HS^2,
```

so

```text
G >= (tr K)_+^2/||K||_HS^2 - nu.
```

Let `N,S,D` denote total multiplicity, simple-real count and distinct count for
xi-prime. With `E=N-D` and `U=D-S`, blockwise signature gives

```text
nu <= 3E/4+U/2.
```

The unconditional quartic-window constants

```text
S/N >= 5429/6250-o(1),
D/N >= 11679/12500-o(1)
```

imply

```text
nu/N <= 821/10000+o(1).
```

If a source-fixed Xi/Xi-prime compression has normalized effective rank

```text
eta=(tr K)_+^2/[N||K||_HS^2],
```

then reverse Rolle yields

```text
N_0/N_zeta >= 2eta-1-821/5000-o(1).
```

Thus `eta>=919/1000` gives `N_0/N>=3369/5000=0.6738`, numerically above the
published Montgomery–Taylor constant. This is a conditional target, not a new
proportion theorem.

The positive Cauchy-power gamma model of `L-105312` has normalized
effective-rank limit at least `49/51`. Its correlations are

```text
|r_(k,L)|^2=(1+h_L^2 k^2/(4 eta^2))^(-Q_L),
Q_L ~ (2/5) eta^2 L^2,
```

and the Hilbert--Schmidt row sum converges to
`sum_k exp(-2 pi^2 k^2/5)<51/49`. If the arithmetic Xi matrix loses at
most 1% in trace and gains at most 1% in HS norm, then

```text
eta >= (49/51)(99/101)^2
    = 160083/173417
    > 919/1000.
```

The sole conclusion-facing open theorem is the source-faithful explicit-formula
comparison and canonical-product positive-index tail bound `LPRT105310`.
