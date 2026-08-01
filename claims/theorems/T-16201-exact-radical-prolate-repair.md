# T-16201 — A mode-8 repair makes the prolate target exactly radical without changing the d4/d8 hierarchy

Claim ID: `T-16201`  
Status: **PROVED FINITE PROLATE-SPECTRAL THEOREM; E-DOMAIN EXTENSION OPEN**  
Authoring agent: `gpt56-pro-12`  
Created: 2026-07-31  
Depends on: fixed-mode prolate asymptotics; `L-16203`, `L-16204`

## 1. The missing second source constraint

The radical theorem for the arithmetic map `E` applies to even source
functions satisfying

```text
f(0)=0,
hat(f)(0)=integral f=0.                                  (T-16201.1)
```

The moving CCM `0/4` combination imposes the second condition but, because the
two finite prolate eigenvalues are not exactly equal, it need not impose the
first. Thus it is a near-radical source rather than an exact radical source.

A third positive prolate mode repairs this defect at relative size
`d_4/d_8`, preserving the mode hierarchy.

## 2. Prolate data

Let `e_0,e_4,e_8,...` be orthonormal time-limited positive-Fourier prolate
modes. Write

```text
F_lambda e_n=chi_n e_n on [-lambda,lambda],
0<chi_n<1,
d_n=1-chi_n,
q_n=e_n(0).                                               (T-16201.2)
```

For these positive modes,

```text
ell_n:=integral e_n=chi_n q_n.                            (T-16201.3)
```

Let

```text
D_lambda=I-F_lambda,
D_lambda e_n=d_n e_n.                                    (T-16201.4)
```

For a coefficient vector `c`, the two radical constraints become

```text
sum c_n q_n=0,
sum c_n ell_n=0.                                         (T-16201.5)
```

Since `ell_n=(1-d_n)q_n`, this is equivalently

```text
<c,q>=0,
<c,Dq>=0.                                                (T-16201.6)
```

## 3. Exact repaired target

Define

```text
p_rad = c_0e_0+c_4e_4+c_8e_8,                            (T-16201.7)
```

where

```text
c_0=q_4q_8(d_8-d_4),

c_4=q_8q_0(d_0-d_8),

c_8=q_0q_4(d_4-d_0).                                     (T-16201.8)
```

Then exactly

```text
p_rad(0)=0,
integral p_rad=0.                                        (T-16201.9)
```

Thus any admissible extension of the `E`-radical theorem to these prolate
sources places `E(p_rad)` in the full Weil radical.

## 4. Target asymptotics

Assume

```text
d_0/d_4->0,
d_4/d_8->0,                                              (T-16201.10)
```

and the fixed-mode point-value limit

```text
q_4^2/q_0^2->3/8.                                        (T-16201.11)
```

After scaling by `q_8d_8`,

```text
p_rad/(q_8d_8)
 -> q_4e_0-q_0e_4.                                       (T-16201.12)
```

The mode-8 repair coefficient relative to the leading coefficients is

```text
O(d_4/d_8)=O(lambda^-8).                                 (T-16201.13)
```

Its defect Rayleigh quotient

```text
mu_rad=<D p_rad,p_rad>/||p_rad||^2                       (T-16201.14)
```

satisfies

```text
boxed:
mu_rad/d_4 -> q_0^2/(q_0^2+q_4^2)=8/11.                 (T-16201.15)
```

Thus imposing the second exact radical constraint does not change the target
scale or its leading constant.

## 5. The complete exact-radical source space

Let `S_lambda` be a finite positive-prolate source sector containing the first
four fixed modes and put

```text
R_lambda
 ={c in S_lambda: <c,q>=<c,Dq>=0}.                       (T-16201.16)
```

Let

```text
nu_1(lambda)<=nu_2(lambda)<=...
```

be the eigenvalues of `D_lambda` compressed to `R_lambda`.

For comparison, let

```text
rho_1(lambda)<=rho_2(lambda)<=...
```

be the eigenvalues of `D_lambda` compressed only to `q^perp`. Since
`R_lambda` has codimension one inside `q^perp`, interlacing gives

```text
rho_1<=nu_1<=rho_2<=nu_2<=rho_3... .                     (T-16201.17)
```

## 6. Tail susceptibility gates

Assume

```text
d_4 sum_(n>=8) q_n^2/d_n ->0,                            (T-16201.18)

d_8 sum_(n>=12)q_n^2/d_n ->0,                            (T-16201.19)
```

where the sums range over the declared finite near-one prolate sector. These are
finite Christoffel/evaluation-kernel conditions. They are expected when the
sector dimension and point-evaluation kernel grow polynomially while
`d_4/d_8` and `d_8/d_12` are `Theta(lambda^-8)`, but they are explicit proof
gates rather than silently assumed.

Then the first two rank-one constrained eigenvalues satisfy

```text
rho_1/d_4 -> q_0^2/(q_0^2+q_4^2),                        (T-16201.20)

rho_2/d_8 -> (q_0^2+q_4^2)/(q_0^2+q_4^2+q_8^2).          (T-16201.21)
```

## 7. Exact-radical mode-8 theorem

Assume additionally

```text
d_8/d_12->0,
q_8^2/q_0^2->35/128.                                     (T-16201.22)
```

Then

```text
boxed:
nu_1/d_4 ->8/11,                                         (T-16201.23)

nu_2/d_8 ->176/211.                                      (T-16201.24)
```

Thus the exact two-constraint radical source hierarchy has the **same** target
and next-mode constants as the previous near-radical model.

## 8. Proof of the exact constraints and target limit

The two sums in (T-16201.6), evaluated on (T-16201.8), are

```text
q_0q_4q_8[(d_8-d_4)+(d_0-d_8)+(d_4-d_0)]=0
```

and

```text
q_0q_4q_8[
 d_0(d_8-d_4)+d_4(d_0-d_8)+d_8(d_4-d_0)
]=0.
```

This proves (T-16201.9). Dividing the coefficient vector by `q_8d_8` and using
(T-16201.10) proves (T-16201.12)--(T-16201.13). In the Rayleigh quotient, the
mode-4 energy is the only leading term, which proves (T-16201.15).

## 9. Proof of the rank-one constrained limits

For a finite diagonal matrix with distinct entries `d_n` and a vector with
nonzero coordinates `q_n`, the eigenvalues of the compression to `q^perp` are
the roots, between consecutive `d_n`, of

```text
sum_n q_n^2/(d_n-x)=0.                                   (T-16201.25)
```

For the first root set `x=c d_4`, multiply (T-16201.25) by `d_4`, and use
`d_0/d_4->0` and (T-16201.18). Uniformly for `c` in compact subintervals of
`(0,1)`, the equation tends to

```text
-q_0^2/c+q_4^2/(1-c)=0.
```

This proves (T-16201.20).

For the second root set `x=c d_8`, multiply by `d_8`, and use
`d_4/d_8->0` and (T-16201.19). The limiting equation is

```text
-(q_0^2+q_4^2)/c+q_8^2/(1-c)=0,
```

which proves (T-16201.21).

## 10. Upper bounds inside the exact-radical space

The repaired target `p_rad` is an admissible trial vector, so

```text
nu_1<=mu_rad.
```

Together with `rho_1<=nu_1`, equations (T-16201.15) and (T-16201.20) prove
(T-16201.23).

For `nu_2`, work in the first four modes `0,4,8,12`. There is a unique vector
`v_rad`, up to scale, satisfying

```text
<v_rad,q>=0,
<v_rad,Dq>=0,
<v_rad,p_rad>=0.                                         (T-16201.26)
```

It is given exactly by the alternating `3 x 3` minors of the matrix whose rows
are `q`, `Dq`, and `p_rad`. Expanding those minors using
`d_4/d_8->0` and `d_8/d_12->0` gives, after normalization,

```text
v_rad ->
 [q_0q_8 e_0+q_4q_8e_4
  -(q_0^2+q_4^2)e_8]
 /
 sqrt((q_0^2+q_4^2)(q_0^2+q_4^2+q_8^2)).                 (T-16201.27)
```

Its Rayleigh quotient divided by `d_8` tends to the right side of
(T-16201.21). The two-dimensional trial space spanned by `p_rad,v_rad` has
maximum Rayleigh quotient with the same limit, because the target quotient is
`o(d_8)` and the mixed `D` pairing is bounded by the geometric mean of the two
energies. Hence

```text
nu_2/d_8
 <=(q_0^2+q_4^2)/(q_0^2+q_4^2+q_8^2)+o(1).
```

The lower bound `rho_2<=nu_2` and (T-16201.21) prove (T-16201.24). QED.

## 11. Consequence for the positive route

If the repaired prolate source belongs to the exact domain of the `E`-radical
theorem, then `L-16203` applies with no approximate-radical cross terms. The
source-block localized Weil form factors exactly through its omitted tails.
The remaining comparison becomes only:

```text
tail Gram = prolate defect at relative mode-8 scale,
normalized tail Weil form has spectral diameter o(lambda^(-2tau)).
                                                                    (T-16201.28)
```

The first two source eigenvalues already have the required `d_4,d_8` hierarchy.

## 12. Proof boundary

The prolate spectral algebra is exact under the declared finite-sector and tail
susceptibility gates. The unresolved analytic point is whether the time-limited
prolate combinations, extended by zero, lie in a domain on which the theorem
that `E(S_0)` is contained in the full Weil radical applies without boundary
corrections. A smooth exact repair must preserve the relative `d_8` scale.
Neither that domain extension nor the tail-Weil scalarization is proved here.
No RH proof is claimed.
