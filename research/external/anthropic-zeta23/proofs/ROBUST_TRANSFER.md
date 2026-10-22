# Stable finite-error rank–trace transfer

**Status:** `PROPOSED NATIVE THEOREM / ELEMENTARY CONSEQUENCE OF IMPORTED ZERO-SIDE LEMMAS`

This note isolates the exact finite inequality needed by directed computations. It deliberately abstracts away the analytic source of the trace bounds.

## 1. Setup

Fix a height window and an enlarged localization window. Let

```text
R = A + E
```

be a normalized Hermitian compression, where:

- `A` is the contribution of zeros in the enlarged window;
- `E` is the far-zero tail;
- one isolated simple on-line zero has atom trace at most one;
- `N` is the full multiplicity count in the target window;
- `NII` is the multiplicity count in the two boundary collars;
- `S` is the number of simple on-line zeros in the target window;
- `D` is the number of distinct zeros in the target window.

Assume the zero-side algebra has produced finite constants `Delta_2,Delta_3>=0` such that

```text
S >= 4 tr(R) - ||R||_F^2 - 2N - Delta_2,
D >= [6 tr(R) - ||R||_F^2 - 3N - Delta_3]/2.
```

In the paper, `Delta_2,Delta_3` are explicit functions of the tail trace norm, the tail operator norm, `||R||_F`, and `NII`.

## 2. Theorem

Suppose `N>0` and certified estimates give

```text
tr(R)       >= (1-eta_1)N,
||R||_F^2   <= (kappa+eta_2)N,
Delta_2     <= delta_2 N,
Delta_3     <= delta_3 N,
```

with all error parameters nonnegative. Then

```text
S/N >= 2-kappa-4 eta_1-eta_2-delta_2,
D/N >= (3-kappa)/2-3 eta_1-eta_2/2-delta_3/2.
```

The same first inequality holds for the number of distinct on-line points if the corresponding zero-side rank bound is used.

### Proof

Substitute the certified trace estimates into the first count inequality:

```text
S
 >= 4(1-eta_1)N-(kappa+eta_2)N-2N-delta_2 N
 = [2-kappa-4eta_1-eta_2-delta_2]N.
```

Likewise,

```text
D
 >= [6(1-eta_1)N-(kappa+eta_2)N-3N-delta_3N]/2
 = [(3-kappa)/2-3eta_1-eta_2/2-delta_3/2]N.
```

No asymptotic passage is used. `square`

## 3. One-parameter corollary

If one common relative error `eta` controls both moments and both normalized tail terms,

```text
eta_1,eta_2,delta_2,delta_3 <= eta,
```

then

```text
S/N >= 2-kappa-6 eta,
D/N >= (3-kappa)/2-4 eta.
```

A less wasteful implementation should keep the four errors separate.

## 4. Support-one specialization

At bandwidth one, `kappa=4/3`, so

```text
S/N >= 2/3-4 eta_1-eta_2-delta_2,
D/N >= 5/6-3 eta_1-eta_2/2-delta_3/2.
```

For the optimized scalar window, replace `kappa` by `1/c_MT`, where

```text
c_MT = sqrt(2) tan(1/sqrt(2)) /
       [1+(1/sqrt(2))tan(1/sqrt(2))].
```

## 5. Directed-computation contract

A proof-producing finite run should output outward-directed intervals

```text
tr(R) in [T_lo,T_hi],
||R||_F^2 in [F_lo,F_hi],
||E||_1 <= e_1,
||E||   <= e_op,
NII     <= n_boundary,
```

and a checker should recompute the deterministic map from these quantities to `Delta_2,Delta_3` and the final count lower bounds. The checker must authenticate the primitive prime-power and archimedean inputs, not merely accept derived trace intervals.

## 6. Why this matters

The asymptotic theorem proves a limit. This transfer theorem gives the repository a clean finite consumer. It also makes failure transparent: at currently accessible heights, taper and endpoint losses may overwhelm the asymptotic gain. That is a quantitative result, not a reason to weaken the certification contract.
