# Affine Pascal dilation and positive rough-state completion

Date: 2026-08-12  
Branch: `research/gpt56-pro/91101-moment-neutral-shadow-transport`  
PR: #399  
Status: **exact structural advance; RH remains unproved**

## 1. Exact affine carry covariance

The averaged Pascal denominator `n+1` selects the affine, not homogeneous,
dilation

\[
 \Phi_m(n)=m(n+1)-1.
\]

For the canonical real-column extension

\[
 \overline\beta_n(q)
 =\frac{a((a+1)q-(n+1))}{n+1},
 \qquad
 a=\left\lceil\frac{n+1}{q}\right\rceil-1,
\]

one has exactly

\[
 \overline\beta_{\Phi_m(n)}(mq)=\overline\beta_n(q).
\]

At atomized split level,

\[
 \chi_{m(n+1)-1,\,mj+r}(mq)=\chi_{n,j}(q)
\]

for every `0<=r<m`. Thus the rough-child lift is exact before averaging.

The critical target and its radix-four detail have the same covariance. A child
row vector lifts with nonnegative coefficient `m^-1/2` and preserves every
matched colored capacity exactly.

## 2. Entropy is amplified

A direct block injection gives

\[
 \binom{m(n+1)-1}{mj+r}\ge\binom nj^m.
\]

Averaging over `j,r` proves

\[
 G_{m(n+1)-1}\ge mG_n.
\]

Hence the naturally scaled affine lift has score at least `sqrt(m)` times the
child score. Rough dilation is strongly score-favorable and cannot create the
coefficient-greater-than-one entropy debt feared in earlier reset proposals.

## 3. Positive completion of the two-state Euler map

In `(L,R)` coordinates one rough factor has the signed matrix

\[
 M_p=(1-r)
 \begin{pmatrix}1+2r&-2r\\r&1-r\end{pmatrix},
 \qquad r=p^{-1/2}.
\]

Its unique negative entry is removed by the minimal correction preserving the
SHARP functional `(1,2)`:

\[
 N_p=(1-r)
 \begin{pmatrix}1+2r&0\\r&1-2r\end{pmatrix}.
\]

For every `p>=5`, `N_p` is entrywise nonnegative. Moreover

\[
 (1,2)N_p=(1,2)M_p
\]

exactly, while the endpoint-score functional satisfies

\[
 (2,1)N_p-(2,1)M_p=(0,3r(1-r))\ge0.
\]

Thus the completion preserves the RH-sensitive scalar and improves score.

## 4. Absorb 59 and 61

Extending the finite Boolean block from primes through 53 to primes through 61
creates `262,144` activation states. Directed exact arithmetic proves the same
global margins:

```text
reserve channel:  minimum sqrt(2)-1 at x=2;
equality channel: minimum >0.3186 at x=33.
```

The rough renewal now begins at prime 67. The endpoint Schur port still has
strict `1/9` reserve. For every `p>=67`,

\[
 p^{-1/2}(1-p^{-1/2})<1/9,
\]

because the worst case reduces exactly to

\[
 81\cdot67<76^2.
\]

Therefore every remaining projective correction fits strictly inside its own
Schur reserve.

## 5. Corrected frontier

The following are now exact and compatible:

```text
finite P_61 Boolean forcing;
rough delay >= log 67;
strict endpoint Schur port;
positive SHARP-preserving state matrix;
score-favorable state conversion;
positive coefficient-one support routing;
exact colored affine Pascal carry lift.
```

The single remaining operation is the positive projection from colored rough
fibers to the ordinary physical column space. The affine lift leaks
nonnegatively into columns not carrying its selected color; several children
cannot be superposed until that leakage is recombined without spending one
physical target column twice.

```text
state/projective obstruction                 CLOSED
colored capacity lift                        CLOSED
colored-to-uncolored physical projection     OPEN / RH-BEARING
Riemann Hypothesis                           UNPROVED
```

## 6. Replays

```text
PASS_AFFINE_PASCAL_DILATION_AND_SCORE_AMPLIFICATION
PASS_POSITIVE_SHARP_PRESERVING_ROUGH_STATE_COMPLETION
PASS_FACTOR54_P61_BOOLEAN_AND_SCHUR_THRESHOLD
```
