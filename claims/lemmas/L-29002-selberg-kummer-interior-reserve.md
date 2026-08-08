# L-29002 — Exact Selberg–Kummer interior reserve

Claim ID: `L-29002`  
Title: On every binomial carry row the Kummer square dominates the complete Selberg forcing, with an explicit positive reserve whose null set is exactly the endpoint contacts  
Status: **PROPOSED COMPLETE ELEMENTARY THEOREM PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-09-r`  
Created: 2026-08-08  
Dependencies: Kummer's valuation identity; the classical Selberg coefficient identity  
Scope: ordinary von Mangoldt carry rows; no source summation, cofinal estimate, or RH claim

## 1. Carry and Kummer profiles

For integers

\[
 n\ge2,
 \qquad 0\le j\le n,
 \qquad d\ge1,
\]

put

\[
 \chi_{n,d}(j)
 =\left\lfloor\frac nd\right\rfloor
  -\left\lfloor\frac jd\right\rfloor
  -\left\lfloor\frac{n-j}{d}\right\rfloor.
\tag{L-29002.1}
\]

Define the logarithmic Kummer profile

\[
\boxed{
 F_n(j)=\sum_{q\le n}\Lambda(q)\chi_{n,q}(j)
       =\log\binom nj.
}
\tag{L-29002.2}

Let

\[
\boxed{
 \mathcal C
 =\Lambda\log+\Lambda*\Lambda.
}
\tag{L-29002.3}

Every coefficient of `mathcal C` is nonnegative.  Define its carry image

\[
\boxed{
 S_n(j)=\sum_{d\le n}\mathcal C(d)\chi_{n,d}(j).
}
\tag{L-29002.4}

## 2. Exact Selberg row formula

The coefficient identity

\[
\boxed{
 \mathbf1*(\Lambda\log+\Lambda*\Lambda)(m)=\log^2m
}
\tag{L-29002.5}

is equivalent to

\[
 \zeta(s)\left[-\left(-\frac{\zeta'}\zeta\right)'(s)
                 +\left(-\frac{\zeta'}\zeta(s)\right)^2\right]
 =\zeta''(s).
\]

Applying the floor/carry functional gives

\[
\boxed{
 S_n(j)
 =\sum_{m=1}^{n}\log^2m
  -\sum_{m=1}^{j}\log^2m
  -\sum_{m=1}^{n-j}\log^2m.
}
\tag{L-29002.6}

In particular,

\[
 S_n(j)\ge0
\tag{L-29002.7}
\]

because it is also the sum of nonnegative coefficients against nonnegative
carry indicators.

## 3. Pointwise domination by the Kummer square

Assume without loss of generality that

\[
 1\le j\le n/2
\]

and put `k=n-j`.  Define

\[
 a_r=\log\frac{k+r}{r},
 \qquad
 b_r=\log(r(k+r)),
 \qquad 1\le r\le j.
\tag{L-29002.8}
\]

Then `a_r` is strictly decreasing, `b_r` is strictly increasing, and

\[
 P:=\sum_{r=1}^{j}a_r=\log\binom nj=F_n(j),
\tag{L-29002.9}
\]

while

\[
 B:=\sum_{r=1}^{j}b_r=P+2\log(j!).
\tag{L-29002.10}
\]

Equation (L-29002.6) becomes

\[
 S_n(j)=\sum_{r=1}^{j}a_rb_r.
\tag{L-29002.11}
\]

The exact reserve decomposition is

\[
\boxed{
\begin{aligned}
 F_n(j)^2-S_n(j)
={}&\frac{P}{j}
 \left[(j-1)P-2\log(j!)\right]\\
&+\frac1j
 \sum_{1\le r<s\le j}
 (a_r-a_s)(b_s-b_r).
\end{aligned}}
\tag{L-29002.12}

Indeed, insert the intermediate quantity `PB/j` and use the pairwise covariance
identity.

Both terms are nonnegative.  For the first, the elementary bounds

\[
 \binom nj\ge\binom{2j}{j}\ge2^j
\]

and

\[
 j!\le2^{j(j-1)/2}
\]

give

\[
 (j-1)P\ge2\log(j!).
\tag{L-29002.13}
\]

For the second, every factor in every summand is nonnegative.  Consequently

\[
\boxed{
 0\le S_n(j)\le F_n(j)^2
 \qquad(0\le j\le n).
}
\tag{L-29002.14}

Equivalently,

\[
\boxed{
 \left(\sum_q\Lambda(q)\chi_{n,q}(j)\right)^2
 \ge
 \sum_d[\Lambda(d)\log d+(\Lambda*\Lambda)(d)]
        \chi_{n,d}(j).
}
\tag{L-29002.15}

This is a pointwise Selberg absorption inequality before any row, source, or
frequency is discarded.

## 4. Exact null set

At the endpoint contacts `j=1` and `j=n-1`,

\[
 F_n(1)=\log n,
 \qquad
 S_n(1)=\log^2n,
\]

so equality holds in (L-29002.14).

If

\[
 2\le j\le n-2,
\]

then the second line of (L-29002.12) is strictly positive, because the two
sequences are strictly oppositely ordered. Therefore

\[
\boxed{
 F_n(j)^2-S_n(j)=0
 \iff
 j\in\{0,1,n-1,n\}.
}
\tag{L-29002.16}

The only nontrivial zero-reserve directions are precisely the two endpoint
neighbors selected by the dyadic two-contact source on PR #269.

## 5. Quantitative balanced reserve

Fix `0<eta<=1/2` and suppose

\[
 \eta n\le j\le(1-\eta)n.
\]

By symmetry take `j<=n/2`.  The elementary product bound

\[
 \binom nj\ge(n/j)^j
\]

gives

\[
 F_n(j)\ge\eta n\log2.
\tag{L-29002.17}
\]

On the other hand, (L-29002.6) gives

\[
 S_n(j)\le j\log^2n\le n\log^2n.
\tag{L-29002.18}
\]

Hence

\[
\boxed{
 S_n(j)
 \le
 \frac{\log^2n}{\eta^2n\log^22}
 F_n(j)^2.
}
\tag{L-29002.19}

In particular, on every fixed balanced cone the complete Selberg forcing uses
only `O_eta(log^2 n/n)` of the Kummer square.  The surviving reserve approaches
the full Kummer energy.

## 6. Consequence for the repository-wide reflected route

The reflected Selberg programmes repeatedly faced the possibility that moving
the Hermitian diagonal to the energy side produced only the tautology
`2E=2E`.  Equation (L-29002.12) gives the exact finite answer in carry
coordinates:

```text
interior carry rows:
    complete Selberg forcing < Kummer square, with an explicit reserve;

endpoint-neighbor rows:
    complete Selberg forcing = Kummer square, with zero reserve.
```

Thus the broad interior packet is not the irreducible obstruction.  The entire
zero-reserve channel is the endpoint commutator isolated by the pole-preserving
prime-annulus construction on PR #289.

## 7. Proof boundary

Closed elementarily, subject to review:

- exact Selberg carry row;
- exact positive reserve decomposition;
- pointwise Kummer-square domination;
- precise endpoint null set;
- quantitative asymptotic reserve on balanced rows.

Open:

- source-complete summation of the endpoint channel;
- the endpoint-tree recurrence in `T-29001`;
- RH.