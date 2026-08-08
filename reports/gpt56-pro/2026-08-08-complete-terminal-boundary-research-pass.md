# Complete terminal-boundary research pass

## Frozen target

```text
PR #304
head 78b75fc17e27334a9950018528c1c6e083d74820
```

This report consolidates only theorems and counterexamples actually proved on the continuation branch. No missing theorem is delegated to a reviewer.

## 1. Exact rejection of the frozen proof

### Source typing

The `q`-dependent coefficients of the frozen proposal are not a divisor source. At `(N,q,k,s)=(18,5,2,1)`:

```text
actual boundary       49/19000
claimed source load   -1/250
```

### Correctly inverted source

Let `sigma_N` be the unique genuine finite divisor source of the complete critical cutoff boundary. Then

```text
||sigma_N||_at > N/480
```

for every `N>=30`.

Every exact source decomposition satisfies

```text
sum_a ||sigma_(N,a)||_at
 >=||sigma_N||_at
 >N/480.
```

Therefore no absolute adjacent-tree termination can have polylogarithmic total cost. The terminal theorem and RH deduction of PR #304 are rejected.

## 2. Exact cancellation-preserving decomposition

The complete boundary is

```text
H_N=P_N+E_N+C_N.
```

Here:

```text
P_N    unshifted alternating parity tail;
E_N    shifted-even one-lattice commutator;
C_N    at most one cutoff collar atom.
```

Completed bounds:

```text
||source(C_N)||_at =1/sqrt(2) when present;

sum_q sqrt(q)E_N(q)<3;

||source(E_N)||_at=O_epsilon(N^epsilon).
```

Thus all non-parity pieces are already closed at the required scale.

## 3. Exact analytic parity shell

For `Re(s)>1`, analytic multiple-Möbius inversion gives

```text
Sigma_(N,s)(m)
 =m^(-s)[2^(1-s)1_(m>N/2)-1_(m>N)].
```

At `s=1/2`, the regularized source is

```text
m^(-1/2)[sqrt(2)1_(m>N/2)-1_(m>N)].
```

Against a compact half-pole-null window `W`, its physical output is

```text
sqrt(N)(R_2W)(x-log N)+O_W(e^(-x/2)),
```

with

```text
widehat(R_2W)(z)
 =(e^(z log2)-1)/(z-1/2) widehat(W)(z).
```

The transform preserves compact support and lowers the half-pole zero order by exactly one.

## 4. Exact finite source recurrence

Let

```text
M_s(y)=sum_(d<=y)mu(d)d^(-s),
Q=floor((N+1)/2).
```

The finite parity source is exactly

```text
sigma_(N,s)(m)
 =m^(-s)[
  -M_s(N/m)
  +(1-eta(s))M_s(Q/m)
  +1-2^(1-s)].
```

At the critical real exponent:

```text
sigma_N
 =-Mfrak_N+rho_2 Mfrak_Q+(1-sqrt(2))m^(-1/2),

rho_2=1-eta(1/2),
0<rho_2<1.
```

This is a strict **source-coordinate** recurrence.

## 5. Exact all-order positive Selberg hierarchy

For

```text
C_r=mu*(1 log^r),
```

the exponential generating function is

```text
sum_r C_r(n)t^r/r!
 =n^t product_(p|n)(1-p^(-t)).
```

Every coefficient is nonnegative. More precisely:

```text
C_r(n)=0  for r<omega(n),
C_r(n)>0  for r>=omega(n).
```

The positive recursion is

```text
C_(r+1)=C_r log+Lambda*C_r.
```

The first moments of the Möbius–Riesz state are therefore

```text
F_0(N)=1,
F_1(N)=sum_(n<=N)Lambda(n)/sqrt(n),
F_2(N)=sum_(n<=N)
 [Lambda(n)log n+(Lambda*Lambda)(n)]/sqrt(n)>=0,
```

and every higher moment is positive as well.

## 6. Exact scope correction: no physical contraction from rho_2

A logarithmic frequency `t` sees the parity child multiplier

```text
1-eta(1/2+it),
```

not the scalar `rho_2`.

At every zeta zero `rho`,

```text
eta(rho)=0,
1-eta(rho)=1.
```

Thus every critical-line zero mode, and every hypothetical off-line zero mode, exactly saturates the parity renewal. A strict translation-invariant norm contraction with coefficient below one cannot follow from `rho_2<1` alone.

This rejects the tempting but false final step

```text
strict scalar source coefficient
-> strict physical energy contraction.
```

## 7. Correct surviving production theorem

A complete proof now needs one concrete, pole-preserving reflected theorem, not a generic terminal estimate.

The theorem must:

1. use the complete independent-frequency physical block before the eta/carry zeta factor appears;
2. retain the boundary/commutator channel which does not vanish at a zeta zero;
3. insert the exact first and second source moments;
4. retain the full `Lambda*Lambda` cross-term ledger;
5. allow genuine critical-line modes in an explicit tempered channel;
6. prove a source-specific Schur or lower-scale inequality whose strictness comes from the physical boundary, not from `rho_2` alone.

This theorem is not proved on the branch and is not presented as a reviewer exercise. The completed contribution of this pass is the exact source normal form, all-order positive hierarchy, and the elimination of every incorrectly typed or impossible shortcut.

## Final status

```text
PR304 absolute terminal proof              false
correct source absolute terminal route     false
shift and collar                           closed
parity source normal form                  closed
physical safe-order descent                closed
all-order Selberg hierarchy                closed
scalar rho_2 physical contraction          false
pole-preserving reflected boundary theorem open
RH                                         unproved
```
