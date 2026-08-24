# L-105311 — Multiplicity-robust inertia charge from the xi-prime constants

Claim ID: `L-105311`  
Status: **PROVED EXACT ALGEBRAIC/COMBINATORIAL THEOREM**  
Created: 2026-08-23  
Depends on: `L-105310`; imported unconditional xi-prime proportions specified below  
RH status: **not assumed**

## 1. Confluent real blocks

Suppose `q=p/p'` has a real pole `c` of order `m`. Write its principal part as

\[
\sum_{r=1}^m a_r(z-c)^{-r},
\qquad a_m\ne0.
\]

In the pole-jet basis `((z-c)^-1,...,(z-c)^-m)`, its centered Pick block is the
real symmetric anti-triangular Hankel matrix

\[
H_{ij}=
\begin{cases}
-a_{i+j-1},&i+j-1\le m,\\
0,&i+j-1>m.
\end{cases}
\tag{L-105311.1}
\]

Successive symmetric row/column eliminations remove `a_1,...,a_(m-1)` and are
congruences. The result is `-a_m J_m`, where `J_m` is the reversal matrix.
Thus

\[
\boxed{n_+(H)\le\lceil m/2\rceil.}
\tag{L-105311.2}

## 2. Confluent nonreal pairs

A conjugate pair of order `m` has a `2m`-dimensional coefficient matrix of the
form

\[
\begin{pmatrix}0&B\\B^*&0\end{pmatrix}.
\]

Its nonzero eigenvalues occur in opposite pairs. Therefore

\[
\boxed{n_+\le m.}
\tag{L-105311.3}

Both bounds survive arbitrary finite observation maps by congruence.

## 3. Charge in terms of multiplicity excess and unprotected distinct points

Let `N` be the total number of zeros of the derivative object, counted with
multiplicity. Let

- `S` be the number that are simple and real/on the critical line;
- `D` be the number of distinct zeros;
- `E=N-D` be multiplicity excess;
- `U=D-S` be distinct points outside the protected simple-real class.

Assign the following nuisance positive-index charge:

- simple real good or bad poles: zero nuisance charge (their signs are handled
  exactly by `L-105310`);
- a real pole of multiplicity `m>=2`: at most `ceil(m/2)`;
- a nonreal conjugate pair of multiplicity `m`: at most `m`.

For a real block, with excess `e=m-1` and `u=1`,

\[
\lceil m/2\rceil\le\frac34e+\frac12u.
\]

For a nonreal pair, with `e=2(m-1)` and `u=2`,

\[
m\le\frac34e+\frac12u.
\]

Summing gives the exact global budget

\[
\boxed{
\nu\le\frac34E+\frac12U.
}
\tag{L-105311.4}

## 4. Imported xi-prime constants

The unconditional quartic-window xi-prime theorem in the Anthropic formal
artifact gives

\[
\frac SN\ge b-o(1),
\qquad b=0.86864=\frac{5429}{6250},
\]

and

\[
\frac DN\ge d-o(1),
\qquad d=0.93432=\frac{11679}{12500}
=\frac{1+b}{2}.
\]

Hence

\[
E\le(1-d)N+o(N)=\frac{821}{12500}N+o(N),
\]

and, since `E+U=N-S`,

\[
E+U\le(1-b)N+o(N)=\frac{821}{6250}N+o(N).
\]

Because the coefficient of `E` in (L-105311.4) is larger, the maximum occurs
at the largest permitted `E`. Therefore

\[
\boxed{
\nu\le\frac{821}{10000}N+o(N)=0.0821N+o(N).
}
\tag{L-105311.5}

The constant is sharp for this abstract bookkeeping: a mixture of triple real
blocks and simple nonreal pairs saturates the two linear inequalities.

## 5. Meaning

The recent xi-prime theorem does more than provide many real critical points.
Its simultaneous simple and distinct proportions give a quantitative cap on
every nonreal/confluent positive-inertia block that can contaminate the Pick
compression. This is the exact multiplicity correction needed to turn
`L-105310` into a low-order descent criterion.

## 6. Scope

The theorem imports the two published xi-prime proportions. It does not prove
them. It also does not prove the trace/HS estimate for the Xi Pick compression.
