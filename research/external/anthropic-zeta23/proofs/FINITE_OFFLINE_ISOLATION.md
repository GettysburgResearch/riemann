# Finite off-line isolation and the Gram-conditioning dichotomy

**Status:** `PROPOSED NATIVE THEOREM / EXACT FINITE HILBERT-SPACE ALGEBRA`

The complete critical Gabor frame can interpolate arbitrary values on every finite set of distinct zero coordinates. Consequently one off-line pair can be annihilated against all other zeros in a finite localization window exactly. The only quantitative cost is one inverse evaluation-Gram scalar.

This turns the repository's qualitative complete-kernel capture obligation into a concrete finite conditioning problem.

## 1. Evaluation Gram

Let `psi` be a real window supported in an interval `I` of length `L`, and suppose

```text
v=psi^2>0
```

almost everywhere on a subinterval of positive length. Use the complete critical modulation lattice and the paper's coefficient normalization.

For distinct complex coordinates

```text
Z={z_1,...,z_n},
```

let `E_Z` be the evaluation map from coefficient space to `C^n`, and let

```text
K_Z=E_Z E_Z*.
```

By the analytically continued Poisson identity,

```text
(K_Z)_(ij)
 =L int_I v(u) exp(i(z_i-conj(z_j))u)du.             (FI1)
```

## 2. Positive definiteness theorem

For every finite set of distinct coordinates, `K_Z` is positive definite.

### Proof

For `alpha in C^n`,

```text
alpha* K_Z alpha
 =L int_I v(u)
    |sum_j alpha_j exp(i z_j u)|^2 du.               (FI2)
```

If this vanishes, the exponential polynomial

```text
sum_j alpha_j exp(i z_j u)
```

vanishes on a set of positive measure and hence, by analyticity, on an interval. Distinct exponentials are linearly independent: differentiating `0,...,n-1` times at one point gives a Vandermonde system. Therefore every `alpha_j=0`. `square`

Thus `E_Z` is onto. Exact finite interpolation is automatic; no zero separation hypothesis is needed for existence.

## 3. Minimum-norm cardinal interpolation

Given target values `t in C^n`, the unique minimum-coefficient-norm interpolant is

```text
boxed:
c_t=E_Z* K_Z^(-1)t.                                 (FI3)
```

It satisfies

```text
E_Z c_t=t,
||c_t||^2=t* K_Z^(-1)t.                             (FI4)
```

### Proof

Equation `(FI3)` gives `E_Zc_t=K_ZK_Z^(-1)t=t`. Every other interpolant is `c_t+k` with `k in ker E_Z`, while `c_t` lies in the orthogonal complement of that kernel. Pythagoras proves minimality and `(FI4)`. `square`

Define the **capture cost**

```text
C_Z(t)=t* K_Z^(-1)t.                                (FI5)
```

## 4. Exact isolation of one reflected pair

Suppose `z_r=z` and `z_s=conj(z)` are an off-line pair of multiplicity `m`. Set

```text
t_r=1,
t_s=-1,
t_j=0 for j not in {r,s}.                           (FI6)
```

Then the contribution of every zero in `Z` except the target pair vanishes, while the pair contributes exactly

```text
boxed:
W_Z(c_t,c_t)=-2m.                                   (FI7)
```

This is the finite Gabor version of the Xi-cardinal difference.

## 5. Far-tail criterion

Write the full compression as

```text
G=G_Z+E_far,
```

and assume

```text
||E_far||<=epsilon.
```

Then the interpolant `(FI3)` obeys

```text
boxed:
c_t*G c_t
 <=-2m+epsilon C_Z(t).                              (FI8)
```

Therefore

```text
boxed:
epsilon C_Z(t)<2m
```

is a sufficient finite certificate of a negative Weil direction.

### Proof

Use `(FI7)` and

```text
|c_t*E_far c_t|
 <=epsilon ||c_t||^2
 =epsilon C_Z(t).
```

`square`

## 6. Target-pair Schur complement

Partition the Gram matrix into target-pair and nuisance coordinates:

```text
K_Z=[[A,B],[B*,D]].
```

The nuisance block `D` is positive definite. Put

```text
S=A-BD^(-1)B*.
```

For `t_pair=(1,-1)`,

```text
boxed:
C_Z(t)=t_pair* S^(-1)t_pair.                        (FI9)
```

Thus nuisance zeros affect the pair only through the exact selected-zero Schur complement. Adding interpolation constraints can only increase `C_Z(t)`, because it minimizes the norm over a smaller affine set.

This is the same Schur geometry as the repository's corrected-kernel program, now on the zero-evaluation Gram rather than the Weil form.

## 7. No-nuisance formula

With no other local zeros, use the notation of `OFFLINE_PAIR_SPECTRUM.md`:

```text
K_pair=C[[r_y,1],[1,r_y]],
C=L int v,
r_y=[int v cosh(2yu)]/[int v].
```

Then

```text
boxed:
C_pair(1,-1)=2/[C(r_y-1)].                           (FI10)
```

The tail criterion `(FI8)` becomes

```text
boxed:
epsilon<m C(r_y-1),                                (FI11)
```

exactly the magnitude of the negative pair eigenvalue computed in the preceding theorem.

## 8. Floor-versus-conditioning dichotomy

Suppose, more generally, that a proposed arithmetic theorem supplies a lower floor

```text
G>=-delta I.                                         (FI12)
```

Combining `(FI8)` with `(FI12)` gives

```text
2m<=(epsilon+delta) C_Z(t).                          (FI13)
```

Let `lambda_min(K_Z)` be the smallest Gram eigenvalue. Since `||t||^2=2`,

```text
C_Z(t)
 <=2/lambda_min(K_Z).
```

Therefore every off-line pair forces the alternative

```text
boxed:
lambda_min(K_Z)
 <=(epsilon+delta)/m.                                (FI14)
```

In words:

> an almost-nonnegative complete compression can coexist with an off-line pair only if the local zero-evaluation Gram becomes comparably ill-conditioned.

If a hierarchy has

```text
epsilon_j->0,
delta_j->0,
```

then a counterexample to RH forces

```text
lambda_min(K_(Z_j))->0
```

along every localization hierarchy containing the pair.

This is a concrete dichotomy, not a restatement of positivity: the two possible failure mechanisms are now separated into

```text
persistent negative corrected kernel
or
collapse of the finite zero-interpolation Gram.
```

## 9. What remains to prove

Exact interpolation is not the obstacle. Uniform conditioning is.

A full proof can now target any one of the following:

1. a lower bound for the target Schur complement `S` in `(FI9)` strong enough to beat the far tail;
2. a theorem that the Gram collapse in `(FI14)` contradicts bandwidth-one pair-correlation data plus a higher local statistic;
3. a complete Xi-cardinal capture theorem whose native metric directly bounds `C_Z(t)`;
4. a cluster decomposition showing that every badly conditioned nuisance packet can be recombined into a smaller source with a preserved negative moat.

The first-two-moment Zeta23 theorem controls an average spectral quantity and cannot by itself bound `lambda_min(K_Z)`. This identifies precisely why the proportion theorem stops short of RH.

## 10. Scope boundary

This theorem proves:

- exact finite interpolation at arbitrary distinct complex zero coordinates;
- exact local isolation of one reflected pair;
- an explicit minimum-norm capture cost;
- a finite far-tail negativity criterion;
- a floor-versus-conditioning alternative.

It does not prove a uniform Gram lower bound, a complete corrected-kernel floor, or RH.
