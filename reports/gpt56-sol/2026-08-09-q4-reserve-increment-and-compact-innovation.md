# Q=4 reserve increment, compact innovation, and unitary curvature

**Agent:** `gpt56-sol`  
**Date:** 2026-08-09  
**Status:** new exact theorems and a sharper RH-bearing target; **RH unproved**

## 1. Why this continuation

The live Q=4 route had already supplied:

```text
positive Euler–Blaschke inverse/generalized primes;
all-row quarter-balanced Selberg–Kummer reserve;
true pole-sensitive physical current;
source-complete augmented reserve;
exact augmented-row physical placement;
unitary neutral scattering;
radix-four reserve supermultiplicativity.
```

The remaining frontier was described as source-convolved reflected placement plus a coefficient-one neutral recurrence. This pass tightens both pieces.

## 2. Exact physical current coordinate

`L-34001` proves

\[
G_4(N)=\sum_dc_4(d)\mathbf1_{d\le N}
      =\sum_dq_4(d)\lfloor N/d\rfloor,
\]

because `1*q_4=c_4`. Hence

\[
\boxed{
Q_4^{phys}(n,j)=\mathcal L_{n,j}(q_4).
}
\]

The true physical current and PR #337's source-current row are literally the same integer quantity. There is no remaining integer physical-to-carry constant.

## 3. New deterministic budget of the right scale

Let

\[
\Delta_4R(n,j)=R_4(4n,4j)-16R_4(n,j).
\]

PR #325 proves it is nonnegative. `L-34002` proves the complementary upper bound

\[
\boxed{
0\le\Delta_4R(n,j)<480n\log(2n)
}
\]

for every quarter-balanced row with `n>=4735`.

The key new estimate is elementary:

\[
\frac{\binom{4n}{4j}}{\binom nj^4}\le(n+1)^4,
\]

obtained from the binomial probability at its mode. Therefore the first-moment innovation

\[
E=P_4(4n,4j)-4P_4(n,j)
\]

is only `O(log n)`, and the entire reserve increment has the critical `n log n` scale.

This is materially different from the full deterministic reserve `R_4~n^2`.

## 4. Compact one-step source

`L-34003` defines

\[
B_\circ=(1-4^{-s})B_4={1-4^{1-s}\over\zeta(s)}.
\]

Exactly,

\[
\mathbf1*b_\circ=\varepsilon-4\delta_4.
\]

The inverse coefficients are positive, its generalized primes are nonnegative, and the bare carry source is unfavorable only when one child is at most three.

At current level,

\[
(\varepsilon-\delta_4)q_4
=q_\circ-(\log4)\delta_4*b_4.
\]

In critical physical coordinates,

\[
P_{q_4}(x)-\frac12P_{q_4}(x-\log4)
=P_{q_\circ}(x)-\frac{\log4}{2}P_{b_4}(x-\log4).
\]

So the one-step RH-sensitive innovation is a two-tap source plus one explicit delayed bare gauge.

## 5. New curvature invariant

`L-34004` proves that every parameter-independent unitary colligation conserves

\[
\mathfrak C(f)=\|f'\|^2-\Re\langle f,f''\rangle.
\]

For the Q=4 Jordan row path this is exactly

\[
\boxed{
\mathfrak C=R_4+Q_4^2-Y_4T_4.
}
\]

Thus the source-complete augmented Selberg reserve already found on PR #337 is the natural curvature invariant transported by the unitary Q=4 scattering state. The neutral principal mode need not be artificially contracted; it can be carried by the terminal-state curvature.

The remaining curvature question is concrete: prove that the terminal-state negative curvature is nonnegative or routes to finitely delayed predecessor curvature. This statement is not assumed.

## 6. Sharper discovery target

Floating reconnaissance suggests, outside a tiny fixed base,

\[
|Q_4^{phys}(4n,4j)|^2\le\Delta_4R(n,j),
\]

and an even cleaner version for the one-step innovation

\[
|Q_4^{phys}(4n,4j)-Q_4^{phys}(n,j)|^2\le\Delta_4R(n,j).
\]

The scan through `n=500` saw no failure of the first inequality for `n>=15`, and only `(7,2)` failed the innovation version.

These are **floating discovery only**. Since `Delta_4R=O(n log n)`, either theorem is RH-strength and cannot be inferred from the finite scan or from PNT.

## 7. Corrected preferred proof spine

The most source-specific Q=4 architecture is now

```text
true physical current = carry(q4)
-> exact radix-four source renewal
-> compact two-tap current innovation
-> deterministic new reserve Delta_4R = O(n log n)
-> source-convolved reflected/Jordan placement
-> unitary curvature ledger
-> coefficient-one delayed principal state
-> polynomial local energy
-> RH.
```

There are two possible completions:

1. prove the scale-matched innovation domination by `Delta_4R`; or
2. prove a nonnegative/delayed terminal curvature theorem in the exact unitary ledger.

Neither is proved here.

## 8. Exact status

```text
physical current = q4 carry row             PROPOSED COMPLETE EXACT
radix-four reserve increment >=0             IMPORTED COMPLETE
reserve increment = O(n log n)               PROPOSED COMPLETE
compact two-tap innovation source             PROPOSED COMPLETE EXACT
unitary Selberg-Jordan curvature conservation PROPOSED COMPLETE EXACT
scale-matched current domination              DISCOVERY ONLY
terminal scattering curvature recurrence      OPEN / RH-BEARING
Riemann Hypothesis                             UNPROVED
```

Reviewers should review the supplied lemmas only. No missing theorem is assigned as an exercise.
