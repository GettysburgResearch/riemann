# Multiplicity-profile frontier from the parameter-c rank–trace inequality

**Status:** `PROPOSED NATIVE THEOREM / EXACT FINITE ALGEBRA`

The headline `2/3` and `5/6` statements discard information. The full parameter-`c` inequality retains an exact charge for every on-line multiplicity and every off-line reflected pair. This note records the resulting joint frontier.

## 1. Multiplicity data

Inside one localized zero window let

```text
a_m = number of distinct on-line zeros of multiplicity m,
b_m = number of reflected off-line pairs whose two members each have multiplicity m.
```

Thus

```text
N = sum_(m>=1) m a_m + 2 sum_(m>=1) m b_m,
S1 = a_1,
D = sum_(m>=1) a_m + 2 sum_(m>=1) b_m.
```

Boundary and tail terms can be appended exactly as in the main paper; they are omitted here to expose the finite algebra.

Define

```text
C_c(R) = 2c tr(R)-||R||_F^2,
k_c(m) = c^2-(c-m)_+^2.
```

For integer `m`,

```text
k_c(m)=2cm-m^2  if m<=c,
k_c(m)=c^2      if m>=c.
```

## 2. Generating inequality

For every `c>0`,

```text
C_c(R)
 <= sum_(m>=1) k_c(m) a_m + c^2 sum_(m>=1) b_m.        (GF)
```

### Proof sketch

Put every on-line atom, with its integer multiplicity, into the positive part `P`; put all reflected off-line pairs into `Q`. The multiplicity-aware rank–trace inequality gives the charge `k_c(m)` for an on-line atom of multiplicity `m` and the flat charge `c^2` for each positive direction of `Q`. Each reflected pair contributes at most one positive direction after pullback. `square`

This single family is a finite-dimensional linear-programming interface: any affine majorant of the right-hand charges yields a certified count statistic.

## 3. Refined simple-on-line inequality at c=2

At `c=2`,

```text
k_2(1)=3,
k_2(m)=4 for m>=2.
```

Define the nonnegative multiplicity penalty

```text
P2 = 2 sum_(m>=3) (m-2)a_m
     +4 sum_(m>=2) (m-1)b_m.
```

Then

```text
S1 >= C_2(R)-2N+P2.                                  (S)
```

### Proof

The charge in `(GF)` is

```text
3a_1+4 sum_(m>=2)a_m+4 sum_(m>=1)b_m.
```

Direct expansion gives the identity

```text
2N+S1
 = [that charge] + P2.
```

Hence `C_2(R)<=2N+S1-P2`, which rearranges to `(S)`. `square`

The usual simple-zero theorem drops `P2`. Therefore any on-line multiplicity at least three, or any off-line pair of multiplicity at least two, forces a strictly stronger simple-on-line count.

## 4. Refined distinct-zero inequality at c=3

At `c=3`,

```text
k_3(1)=5,
k_3(2)=8,
k_3(m)=9 for m>=3.
```

Define

```text
P3 = sum_(m>=3) (3m-7)a_m
     +sum_(m>=1) (6m-5)b_m.
```

Every coefficient in `P3` is positive. Then

```text
D >= [C_3(R)-3N+P3]/2.                              (D)
```

### Proof

The charge in `(GF)` is

```text
5a_1+8a_2+9 sum_(m>=3)a_m+9 sum_(m>=1)b_m.
```

Expanding `3N+2D` gives exactly this charge plus `P3`. Thus

```text
C_3(R)<=3N+2D-P3,
```

which is `(D)`. `square`

Unlike `P2`, the penalty `P3` already charges a simple off-line pair: its coefficient is `6*1-5=1`. Therefore the `5/6` distinct-zero floor is sharp only in an on-line double-zero direction; off-line pairs push the distinct count upward.

## 5. Asymptotic consequences at bandwidth one

If

```text
tr(R)=N+o(N),
||R||_F^2=(4/3)N+o(N),
```

then

```text
S1/N >= 2/3 + P2/N-o(1),
D/N  >= 5/6 + P3/(2N)-o(1).
```

Let `p=sum b_m` be the number of distinct reflected off-line pairs. Since `P3>=p`,

```text
D/N >= 5/6 + p/(2N)-o(1).
```

Equivalently, if `Ostar=2p` counts the distinct off-line points,

```text
D/N >= 5/6 + Ostar/(4N)-o(1).
```

This is a genuine joint tradeoff: the extremal configuration for the on-line count and the extremal configuration for the distinct count cannot be the same.

Since `S1<=N`, `(S)` also gives

```text
P2 <= (1/3)N+o(N).
```

In particular,

```text
sum_(m>=3)(m-2)a_m <= N/6+o(N),
sum_(m>=2)(m-1)b_m <= N/12+o(N).
```

These are coarse corollaries of the full charge family, but they quantify how little high multiplicity can coexist with the support-one moments.

## 6. LP interface

For any desired statistic

```text
L = sum ell_m a_m + sum r_m b_m,
```

one may choose finitely many parameters `c_j` and solve the dual problem of expressing a lower bound for `L` from the charge inequalities `(GF)` and the mass identity for `N`. The script `experiments/X-zeta23-multiplicity-frontier/frontier.py` verifies the exact identities above and exposes the charge table for further optimization.

## 7. Scope boundary

This note does not prove a better unconditional headline constant without additional information about the multiplicity profile. It proves a sharper **frontier theorem** whose zero-penalty projection is the published result.
