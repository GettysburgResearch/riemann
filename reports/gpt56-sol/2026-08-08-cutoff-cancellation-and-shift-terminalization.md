# Cutoff cancellation, terminal lattice shifts, and the corrected eta core

**Agent:** `gpt56-sol`  
**Date:** 2026-08-08  
**Branch:** `research/gpt56-sol/304-cutoff-cancellation-critical-jet`  
**Parent:** PR #304 at `78b75fc17e27334a9950018528c1c6e083d74820`  
**Status:** **exact refutation plus new finite construction; RH unproved**

## 1. Why this continuation was necessary

PR #304 proposed to split the finite central operator into:

```text
contracted analytic continuation
+
finite cutoff source,
```

convert the cutoff source to a divisor-source vector of polylogarithmic
square-root atomic norm, and terminate that source by adjacent-tree
commutators.

The user correctly required that the source manifest be proved by the author,
not reconstructed by a reviewer. Direct reconstruction shows that the claimed
atomic norm is false.

## 2. Exact macroscopic obstruction

For the stopped pure power `f(n)=n^(-1/2)`, the cutoff tail on every integer

```text
N/3 < q <= N/2
```

has normalized size bounded away from zero:

```text
sqrt(q) B_N(q) < -1/10.
```

At the next-half endpoint `M=floor((N+1)/2)`, these `q` lie above `M/2`.
Therefore the upper-multiples incidence transform is triangular there and any
divisor source representing the tail must satisfy

```text
sigma_N(q)=B_N(q).
```

Consequently

```text
sum_m sqrt(m)|sigma_N(m)| >= N/100.
```

This is a cofinal analytic lower bound. The cutoff source is large because it
cancels a comparably large analytic continuation on the same quotient cell.
Separating the two and norming them independently destroys the cancellation.

The positive stopped-power layer cake does not repair the issue. If layers are
terminally lifted separately, each weighted layer costs an absolute constant,
so the total cost is order `X`. Any valid use of the layer cake must recombine
endpoint layers before measuring variation.

Thus the full-proof status of PR #304 is withdrawn.

## 3. A valid exact terminal source

The one-step lattice shift is different. For any finite residual `r`,

```text
(T_N-U_N)r(q)
 =sum_k [r(2kq-1)-r(2kq)]
 =sum_(q|m) sigma_r(m),

sigma_r(m)=r(2m-1)-r(2m).
```

This is an actual next-half divisor source. It is realized exactly by

```text
Phi_N(r)=sum_m sigma_r(m)[T_m-T_(m-1)].
```

The adjacent-tree capacity theorem gives

```text
N_omega(Phi_N(r))
 <=24 sum_m sqrt(m)|sigma_r(m)|.
```

After critical normalization `G_n=sqrt(n)r(n)`, the atomic source norm is
bounded by

```text
TV(G)+2 sum_n |G_n|/n.
```

The central first-difference flow is controlled by the same functional.

## 4. The corrected exact finite producer

One stage now reads

```text
input residual r
-> central first-difference flow
-> terminal adjacent-commutator flow for the `-1` shift
-> propagated unshifted residual U_N r.
```

The stage is exact in every carry column. Since `U_N` halves support, iteration
terminates after `O(log X)` stages and emits a complete finite signed balanced
flow.

No analytic cutoff tail is created or normed.

## 5. Exact logarithmic eta coordinate

For

```text
r(n)=n^(-1/2)G(log(N/n)),
G(t)=0 for t<0,
```

the propagated residual satisfies exactly

```text
sqrt(q) U_Nr(q)=(beta*G)(log(N/q)),
```

where

```text
beta=sum_k [(2k)^(-1/2) delta_log(2k)
            -(2k+1)^(-1/2) delta_log(2k+1)].
```

Endpoint causality is already retained by `G(t)=0` for `t<0`; no separate
boundary source is needed.

The new weighted-jet theorem proves

```text
J_M(beta*G)
 <=theta J_M(G)+c 2^M ||G^(M+1)||_1,
theta<1,
```

with the explicit elementary bound

```text
theta < 1/16 + 5/(4sqrt(2)) <1.
```

The strict reserve comes from pairing the eta atoms and charging adjacent
translations by one derivative. Termwise atomic variation is never used.

## 6. Honest remaining frontier

The exact modified producer gives

```text
N_omega(d_X)
 <=50 sum_j V_(N_j)(r_j),

r_(j+1)=U_(N_j)r_j.
```

The remaining theorem is the explicit Critical Eta Variation estimate

```text
sum_j V_(N_j)(r_j)=X^o(1).
```

This is not proved on the branch and is therefore not assigned to reviewers.
The branch supplies a complete finite producer and a strict analytic reserve,
but it does not claim RH.

## 7. Exact state

```text
PR #304 terminal atomic cutoff source           REFUTED
macroscopic N/100 atomic lower bound             PROVED
critical eta weighted-jet contraction            PROVED
lattice shift divisor-source factorization       PROVED
terminal shift commutator flow                    PROVED
modified support-halving producer                 PROVED
Critical Eta Variation                            OPEN / RH-BEARING
Riemann Hypothesis                                UNPROVEN
```
