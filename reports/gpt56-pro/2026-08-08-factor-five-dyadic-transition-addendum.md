# Factor-five dyadic transition addendum

Date: 2026-08-08  
Agent: `gpt56-pro`  
Branch: `agent/gpt56-pro-262-dyadic-two-contact`  
Parent proposal: PR #269  
Status: **EXACT NEW SOURCE IDENTITIES; FACTOR-FIVE PHYSICAL TRANSITION LMI OPEN; RH UNPROVED**

## 1. Why this continuation was needed

The first version of PR #269 made two genuine advances:

1. the fixed-`q_0=2` Möbius packet was traced through the complete
   two-frequency normal matrix;
2. the dyadic coefficient `b_2` collapsed pointwise to two carry contacts and
   to the Green dipole `-3e_2+e_3`.

It then nominated odd-column leakage in the exact digital lift as the smallest
half-scale obstruction. That description was correct for columnwise
feasibility, but it was not yet sharp at the signed RH-bearing scalar.

This addendum separates the easy signed load from the hard target and applies
one additional safe dyadic Euler factor to both.

## 2. New exact source

Put

```text
omega_2
 = b_2-(1/2) delta_2*b_2
 = mu-(3/2)delta_2*mu+(1/2)delta_4*mu.
```

Its Dirichlet multiplier is

```text
(1-2^-s)(1-2^(-s-1))/zeta(s).
```

The second factor has zeros only on `Re s=-1`, so `omega_2` retains the full
rightmost-zero obstruction. The `b_2` and `omega_2` Riesz coordinates are
connected by mutually inverse causal geometric filters.

## 3. Pointwise scaled carry identity

For every scale `m`, parent row `n`, and carry position `j`, define

```text
Y_(n,m)(j)=sum_(k<=n/m)b_2(k) chi_(n,mk)(j).
```

The exact identity is

```text
Y_(n,m)(j)
 =1_(m<=n<2m)
  -1_(m<=j<2m)
  -1_(m<=n-j<2m).
```

The complete opposite-parity source is therefore

```text
Z_(n,m)(j)
 =Y_(n,m)(j)-(1/2)Y_(n,2m)(j)
 =g_m(n)-g_m(j)-g_m(n-j),

g_m=1_[m,2m)-(1/2)1_[2m,4m).
```

This is a source identity, not a face-counting or rank assertion.

## 4. Exact sign geometry

The wavelet is pointwise nonnegative in the inner band

```text
m<=n<2m
```

and pointwise nonpositive in the outer band

```text
2m<=n<4m.
```

For `n>=4m`, its coupling with

```text
F_n(j)=log binom(n,j)
```

is

```text
D(n,m)/(n+1),
D(n,m)=sum_(2m<=j<4m)F_n(j)-2sum_(m<=j<2m)F_n(j).
```

Two elementary exact arguments close the infinite quotient tail:

1. `D(n,m)` is strictly increasing in `n` for every `n>=4m`; its increment is
   the logarithm of a termwise-larger positive integer product.
2. At `n=5m`, binomial symmetry and monotonicity give `D(5m,m)>=0`.

Therefore

```text
negative logarithmic Kummer row
=> 2m<=n<5m.
```

The quotient tail `n/m>=5` is completely nonnegative.

## 5. Odd leakage scope correction

For the odd Möbius coefficient,

```text
sum_(q odd<=x)mu(q)floor(x/q)
 =1+floor(log_2 x).
```

Hence the signed odd carry row has an explicit binary-level formula. When it is
paired with any feasible lower-scale carry vector, the signed odd-column load
is `O(log^2 X)` by the universal feasible moment bound.

However the odd target has Dirichlet series

```text
1/[(1-2^-s)zeta(s)],
```

so it remains RH-equivalent. Thus controlling only the leakage load cannot
close the source. The target and load must be recombined before the estimate;
`omega_2` does exactly that.

## 6. New smallest honest target

The preferred next object is no longer an all-packet theorem or an unsigned
odd-leakage estimate. It is one source-specific two-frequency transition LMI
covering only

```text
2m<=n<5m.
```

A fail-closed certificate must include:

- all four physical translate channels from the corrected normal block;
- the extra `epsilon-(1/2)delta_2` source sibling;
- quotient cells `2`, `3`, and `4`;
- every endpoint and noncoprime correction;
- the retained positive inner and far ledgers;
- a strict Schur reserve;
- an explicit map from the transition inequality to DSS or directly to
  subexponential shell energy;
- the fixed-ratio Mertens mutation.

No generic operator norm, bounded-rank theorem, or unsigned carry bound is
permitted.

## 7. Exact replay

The new standard-library verifier checks:

```text
scaled b_2 box profile cells                   386,270
pointwise omega_2 wavelet cells                386,270
pointwise sign-band cells                       71,610
factor-five exact Kummer product cases           2,505
far-field increment products                     2,940
odd Möbius pointwise carry cells                13,040
actual negative transition examples               300
```

Retained digest:

```text
b2ff53b948da65a81082fa9a14d7f990c227bb47a6bb592458655ccec7a03f95
```

The negative examples are retained intentionally: they reject any accidental
promotion of the transition sector to automatic positivity.

## 8. Exact boundary

```text
correct two-frequency source trace            retained exact
b_2 two-contact / Green dipole                 retained exact
omega_2 pointwise compact carry wavelet        proposed complete
negative Kummer tail outside factor five       eliminated exactly
signed odd-column load                         automatic O(log^2 X)
odd target                                     RH-bearing
factor-five physical transition LMI            open
DSS / shell contraction                        open
Riemann Hypothesis                             unproved
```

This is a strict narrowing of the open theorem, not an unconditional proof.
