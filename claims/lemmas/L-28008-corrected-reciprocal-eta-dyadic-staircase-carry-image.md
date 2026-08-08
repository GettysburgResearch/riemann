# L-28008 — Corrected reciprocal-eta dyadic staircase carry image

Claim ID: `L-28008`  
Title: The reciprocal-eta carry image is an exact dyadic staircase, with zero at the two trivial splits and a strict ternary sign partition on the interior splits  
Status: **PROPOSED EXACT CORRECTION / SUPERSEDES THE POINTWISE WORDING OF `L-28002`**  
Authoring agent: `gpt56-pro-09-v`  
Created: 2026-08-08  
Parent: PR #280  
Dependencies: `L-28001`  
Scope: exact finite carry algebra

## 1. Dyadic divisor prefix

Let `b` be the coefficient sequence of `1/eta(s)`.  Then

\[
 (\mathbf 1*b)(n)=
 \begin{cases}
 2^r,&n=2^r,\\
 0,&\text{otherwise},
 \end{cases}
\]

and therefore, for integer `x>=0`,

\[
 \boxed{
 D(0)=0,
 \qquad
 D(x):=\sum_{q\le x}b(q)\left\lfloor{x\over q}\right\rfloor
 =2^{\lfloor\log_2x\rfloor+1}-1
 \quad(x\ge1).
 }
\tag{L-28008.1}

## 2. Complete atomized carry image

For `n>=2` and `0<=j<=n`,

\[
 \boxed{
 Y_n(j):=\sum_{q=2}^{n}b(q)\chi_{n,q}(j)
 =D(n)-D(j)-D(n-j).
 }
\tag{L-28008.2}

At the two trivial splits,

\[
 \boxed{Y_n(0)=Y_n(n)=0.}
\tag{L-28008.3}

Now write

\[
 P=2^{\lfloor\log_2n\rfloor},
 \qquad P\le n<2P.
\]

For every nontrivial split `1<=j<=n-1`, exactly one of the following holds:

\[
 \boxed{
 \begin{aligned}
 Y_n(j)>0
 &\iff j<P\text{ and }n-j<P,\\
 Y_n(j)<0
 &\iff j\ge P\text{ or }n-j\ge P.
 \end{aligned}}
\tag{L-28008.4}

There is no zero on the nontrivial split range.  Explicitly,

\[
 Y_n(j)=
 \begin{cases}
 2P-1-D(j)-D(n-j),&n-P<j<P,\\[1mm]
 -D(n-j),&j\ge P,\\[1mm]
 -D(j),&n-j\ge P.
 \end{cases}
\tag{L-28008.5}

## 3. Averaged row

Write `n=P+r`, `0<=r<P`.  Summing (L-28008.2), including the two zero endpoint
values, gives

\[
 \boxed{
 {1\over n+1}\sum_{j=0}^{n}Y_n(j)
 ={(2P-1)\left({P-1\over3}-r\right)\over P+r+1}.
 }
\tag{L-28008.6}

Hence the average changes sign at the exact one-third location inside every
dyadic block.

## 4. Central split

At `j=floor(n/2)`,

\[
 \boxed{
 Y_n(\lfloor n/2\rfloor)=
 \begin{cases}
 1,&n\ne2^r-1,\\[1mm]
 1-2^{r-1},&n=2^r-1.
 \end{cases}}
\tag{L-28008.7}

Thus `L-28004` and its Mersenne boundary telescope are unchanged.

## 5. Correction boundary

The original `L-28002` formulas for the divisor prefix, averaged row, ternary
threshold, and central Mersenne collapse remain correct.  Its assertion of a
strict sign at `j=0,n` is superseded by (L-28008.3).  All downstream uses in the
new proposal concern either nontrivial splits, averages, or the central split
and are unaffected.
