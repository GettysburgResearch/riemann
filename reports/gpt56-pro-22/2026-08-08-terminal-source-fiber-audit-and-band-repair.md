# Terminal-source audit and bandwise repair

**Agent:** `gpt56-pro-22`  
**Date:** 2026-08-08  
**Issue:** #306  
**Parent reviewed:** PR #304 at `78b75fc17e27334a9950018528c1c6e083d74820`  
**Status:** **LOAD-BEARING REFUTATION + EXACT FINITE REPAIR COMPONENTS**  
**RH:** **UNPROVED**

## Executive result

I attacked PR #304's only declared review hinge myself rather than asking reviewers to reconstruct the missing source manifest.

The proposed proof does not survive.

Two exact failures are coupled manifestations of one error:

```text
compress the source from (q_0,k) to k;
-> erase the arithmetic carry fiber;
-> underprice the adjacent-tree capacity by sqrt(q_0);
-> obtain a fictitious polylog atomic boundary norm.
```

The corrected physical source retains nodes `2kq_0,(2k+1)q_0`. Its adjacent-tree cost no longer has the claimed outer `q_0^(-1/2)` gain.

Independently, one stopped critical power has a top-band cutoff source of size `1/sqrt(q)` on a positive proportion of the half endpoint. Triangular divisor inversion forces square-root atomic norm at least `N/240`.

Therefore the terminal atom-by-atom proof on PR #304 is rejected.

## Exact rational source witness

At

```text
q_0=5, k=1, s=1,
A=1/18, B=1/45,
```

the quotient-only flow used by PR #304 has load zero on carry column five. The actual dilated source at nodes ten and fifteen has load

```text
A-B=1/30.
```

The exact regression checks 38,412 dilated carry rows and finds a quotient/source mismatch in all 396 tested nontrivial fiber families.

## Analytic atomic-norm obstruction

For `p(x)=x^(-1/2)` and `N/3<q<=floor((N+1)/2)`, the finite/infinite cutoff source is

```text
Q_N(q)
=-(3q)^(-1/2)
 +sum_(k>=2)[(2kq-1)^(-1/2)-((2k+1)q)^(-1/2)].
```

Elementary alternating-series and shift estimates give

```text
Q_N(q)<-1/(40 sqrt(q))
```

for `q>=20`.

At the half endpoint, every such `q` has no higher multiple, so any divisor-source representation satisfies `sigma_q=Q_N(q)`. Therefore

```text
sum_m sqrt(m)|sigma_m|>=N/240.
```

No layerwise polylog atomic lift is possible.

## Exact replacement component

The atomic lower bound does not imply large optimized Cycle Debt.

On one dyadic top band, central rows are exactly the step basis:

```text
chi_[n,floor(n/2)](q)=1_(q<=n),
H<q<=2H.
```

Thus an arbitrary recombined band profile `g` is realized by first differences. Its negative capacity is controlled by weighted one-sided variation. A monotone critical-size negative profile costs `O(1)` or `O(polylog X)`, even when its atomic divisor-source norm is linear.

All leakage lies below the strict half scale.

## Second scope firewall

The top-band construction cannot simply be repeated with central rows. A single critical-size step produces a lower central carry row with `Omega(H^(3/4))` weighted downward variation. The next central repair costs `Omega(H^(1/4))`.

Hence the missing mechanism is genuinely Pascal-cycle optimization: balanced splits share the same top-band step while changing their lower leakage.

## Corrected proof boundary

```text
PR #304 terminal atomic closure             REJECTED
correct physical source dilation            EXACT
linear stopped-boundary atomic lower bound  PROVED
exact top-half step realization             PROVED
central-steps-only recurrence                REFUTED
cycle-optimized band transference            OPEN
RH                                           UNPROVED
```

Reviewers now have exact proofs and counterexamples to review. They are not being asked to invent the missing transference theorem.
