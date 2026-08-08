# L-28002 — The reciprocal-eta carry image is an exact dyadic staircase

Claim ID: `L-28002`  
Title: The complete central resolvent collapses under every atomized carry row to one explicit dyadic boundary profile with a ternary sign threshold  
Status: **PROPOSED EXACT FINITE LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-09-v`  
Created: 2026-08-08  
Parent: PR #280  
Dependencies: `L-28001`; atomized carry identity `L-23808`  
Scope: exact divisor-prefix and carry algebra; no asymptotic estimate

## 1. Reciprocal-eta coefficients

Let `b` be the coefficient sequence of `1/eta(s)` from `L-28001`:

\[
 b(n)=\sum_{2^j\mid n}2^j\mu(n/2^j).
\tag{L-28002.1}

Since

\[
 {\zeta(s)\over\eta(s)}
 ={1\over1-2^{1-s}}
 =\sum_{r\ge0}2^r(2^r)^{-s},
\]

one has the exact Dirichlet convolution

\[
 \boxed{
 \mathbf1*b
 =\sum_{r\ge0}2^r\delta_{2^r}.
 }
\tag{L-28002.2}

## 2. Dyadic divisor prefix

For an integer `x>=0`, define

\[
 D(x)=\sum_{q\le x}b(q)\left\lfloor{x\over q}\right\rfloor.
\tag{L-28002.3}

Summing (L-28002.2) through `x` gives

\[
 \boxed{
 D(0)=0,
 \qquad
 D(x)=2^{\lfloor\log_2x\rfloor+1}-1
 \quad(x\ge1).
 }
\tag{L-28002.4}

Thus the complete Möbius/eta inverse has an elementary divisor-prefix image:
one positive atom of mass `2^r` at every dyadic scale.

## 3. Pointwise atomized carry image

For integers

\[
 n\ge2,
 \qquad0\le j\le n,
\]

put

\[
 \chi_{n,q}(j)
 =\left\lfloor{n\over q}\right\rfloor
  -\left\lfloor{j\over q}\right\rfloor
  -\left\lfloor{n-j\over q}\right\rfloor.
\]

Then the complete reciprocal-eta carry profile is

\[
 \boxed{
 Y_n(j):=\sum_{q=1}^{n}b(q)\chi_{n,q}(j)
 =D(n)-D(j)-D(n-j).
 }
\tag{L-28002.5}

The `q=1` row is identically zero, so the same formula holds with the sum
starting at two.

Let

\[
 P=2^{\lfloor\log_2n\rfloor},
 \qquad P\le n<2P.
\]

Since at most one child can be at least `P`, (L-28002.5) gives the exact sign
partition

\[
 \boxed{
 \begin{aligned}
 &Y_n(j)>0
 &&\Longleftrightarrow&& j<P\text{ and }n-j<P,\\
 &Y_n(j)<0
 &&\Longleftrightarrow&& j\ge P\text{ or }n-j\ge P.
 \end{aligned}}
\tag{L-28002.6}

There are no zero values.  More explicitly,

\[
 Y_n(j)=
 \begin{cases}
 2P-1-D(j)-D(n-j),&n-P<j<P,\\[1mm]
 -D(n-j),&j\ge P,\\[1mm]
 -D(j),&n-j\ge P.
 \end{cases}
\tag{L-28002.7}

Hence the complete infinite central cascade has a compact digital boundary
shape: positive in the central window and negative only on the two endpoint
wings.

## 4. Exact averaged row and the ternary threshold

The averaged carry coefficient is

\[
 \overline Y_n
 ={1\over n+1}\sum_{j=0}^{n}Y_n(j)
 =\sum_{q=2}^{n}b(q)\beta_{nq}.
\tag{L-28002.8}

Write

\[
 n=P+r,
 \qquad0\le r<P.
\]

The complete prefix sum is

\[
 \sum_{j=0}^{P-1}D(j)
 ={2P^2-3P+1\over3}.
\tag{L-28002.9}

Using that `D(j)=2P-1` for `P<=j<=P+r`, direct substitution gives

\[
 \boxed{
 \overline Y_{P+r}
 ={(2P-1)\left({P-1\over3}-r\right)
  \over P+r+1}.
 }
\tag{L-28002.10}

Thus the averaged source changes sign at the exact one-third location inside
every dyadic block:

\[
 \boxed{
 \begin{aligned}
 \overline Y_{P+r}>0&\iff r<{P-1\over3},\\
 \overline Y_{P+r}=0&\iff r={P-1\over3}\in\mathbb Z,\\
 \overline Y_{P+r}<0&\iff r>{P-1\over3}.
 \end{aligned}}
\tag{L-28002.11}

The zero row occurs precisely when `P=2^(2m)` and
`r=(P-1)/3`.  The first strictly negative product-overlap row is already visible
at `n=3`; the first two-stage central mutation occurs at `n=6`.

## 5. Consequences for the global route

The exact dyadic staircase explains why binary and ternary structures repeatedly
appear in the live repository:

```text
dyadic scale P
+ one-third transition inside [P,2P)
= first mixed-radix boundary at 6=2*3.
```

It also gives a much smaller source-image problem than a generic balanced
packet.  Any reflected or transport proof may work directly with the two
endpoint wings and the central positive window in (L-28002.7), while preserving
the exact reciprocal-eta pole.

The profile is signed, so neither pointwise carry positivity nor a generic
positive-kernel argument follows.  The sign must be repaired by complete
binary--ternary/Pascal recombination or controlled by a reflected Hermitian
square before taking norms.

## 6. Proof boundary

Closed exactly:

- the dyadic divisor-prefix formula;
- the pointwise carry collapse;
- the complete sign partition;
- the averaged closed form;
- the exact ternary threshold in every dyadic block.

Open:

- a positive binary--ternary transport of the endpoint wings;
- a reflected source-image contraction;
- RH.
