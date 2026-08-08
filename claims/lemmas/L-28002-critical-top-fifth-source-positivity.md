# L-28002 — Critical top-fifth source positivity

Claim ID: `L-28002`  
Title: The exact Möbius node divergence of the critical carry target is nonnegative throughout the top fifth of every endpoint  
Status: **PROPOSED COMPLETE ELEMENTARY LEMMA WITH EXACT INTERVAL GATE**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: `L-23810`; elementary calculus; `X-28001` exact rational interval gate  
Scope: exact source sign on `m>=ceil(X/5)`; no claim below that scale

## 1. Critical divergence

Fix `X>=2` and put

\[
w_X(q)=q^{-1/2}\log(X/q),\qquad 1\le q\le X,
\]

with `w_X(q)=0` for `q>X`. Define

\[
U_X(m)=\sum_{k\le X/m}\mu(k)w_X(mk),
\qquad
R_X(m)=U_X(m)-U_X(m+1).
\tag{L-28002.1}
\]

This is the exact target divergence used by the balanced fragmentation programmes.

## 2. Scaled quotient-cell formula

Write

\[
\theta=m/X,\qquad L=\log(1/\theta).
\]

On a quotient cell

\[
\frac1{N+1}<\theta\le\frac1N,
\]

one has exactly

\[
U_X(m)=X^{-1/2}u_N(\theta),
\tag{L-28002.2}
\]

where

\[
u_N(\theta)=
\sum_{k=1}^{N}\frac{\mu(k)}{\sqrt{k\theta}}
\log\frac1{k\theta}.
\tag{L-28002.3}
\]

The entering summand at `theta=1/N` has logarithm zero, so the functions join continuously at quotient boundaries.

For `theta>=1/5`, only

\[
\mu(1)=1,\qquad \mu(2)=\mu(3)=-1,\qquad \mu(4)=0
\]

occur; the possible `k=5` term at the endpoint `theta=1/5` is zero.

## 3. Exact derivative

Differentiation inside a quotient cell gives

\[
-u_N'(\theta)=\theta^{-3/2}C_N(L),
\tag{L-28002.4}
\]

with

\[
C_N(L)=
\sum_{k=1}^{N}\frac{\mu(k)}{\sqrt k}
\left(1+\frac12(L-\log k)\right).
\tag{L-28002.5}
\]

We prove `C_N(L)>0` on every cell meeting `[1/5,1]`.

### Cell `N=1`

\[
C_1(L)=1+L/2>0.
\]

### Cell `N=2`

\[
C_2(L)=1+L/2-rac1{\sqrt2}
\left(1+\frac12(L-\log2)\right).
\]

Its coefficient of `L` is positive, so the minimum occurs at `L=log 2`; there

\[
C_2(\log2)=1+\frac12\log2-\frac1{\sqrt2}>0.
\tag{L-28002.6}
\]

### Cells `N=3,4`

Since `mu(4)=0`, both use

\[
C_3(L)=1+L/2
-\frac1{\sqrt2}\left(1+\frac12(L-\log2)\right)
-\frac1{\sqrt3}\left(1+\frac12(L-\log3)\right).
\tag{L-28002.7}
\]

The coefficient of `L` is negative, so the minimum on `log3<=L<=log5` is at `L=log5`. The exact rational interval consumer `X-28001`, using positive atanh-series enclosures for the logarithms and rational square brackets, proves

\[
\boxed{C_3(\log5)>\frac1{25}.}
\tag{L-28002.8}
\]

Hence `C_N(L)>0` throughout every relevant cell.

## 4. Source sign

Equations (L-28002.4)--(L-28002.8) show that the continuous scaled function `u_N(theta)` is strictly decreasing as `theta` increases through `[1/5,1]`. It is continuous at the reciprocal knots. Therefore

\[
U_X(m)\ge U_X(m+1)
\]

whenever

\[
m\ge\lceil X/5\rceil.
\]

Thus

\[
\boxed{
R_X(m)\ge0
\qquad(\lceil X/5\rceil\le m\le X).
}
\tag{L-28002.9}

The endpoint `m=X` has equality. Away from a zero-width endpoint coincidence, the derivative moat gives strict positivity.

## 5. Consequence for first entrance

Let `S_X(m)=mR_X(m)` be the size-biased source of `L-28001`. If

\[
n\ge\lceil X/5\rceil,
\]

then every source state `m>=n` in the first-entrance sum is nonnegative. Since the entrance probabilities are nonnegative,

\[
\boxed{
\Sigma_{X,n}(p)\ge0
\quad\text{for all }n\ge\lceil X/5\rceil.
}
\tag{L-28002.10}

Therefore the proposed First-Entrance Positivity theorem is already closed on the entire top fifth. Its sole arithmetic burden lies below that scale, where all higher generations must be recombined before a sign is taken.

## 6. Why this does not solve RH

The statement

\[
R_X(m)\le0\quad(m<X/5)
\]

is strongly suggested by finite computation but is not asserted here. Nor would a one-crossing source sign by itself prove fragmentation positivity: mixed-size transition constraints remain.

The exact advance is the unconditional positive base region for the global spine induction.

## 7. Proof boundary

Closed:

- quotient-cell formula for the top fifth;
- strict derivative sign with an exact `>1/25` moat in the worst cell;
- `R_X(m)>=0` for every `m>=ceil(X/5)`;
- FEP on the top fifth.

Open:

- first-entrance positivity below `X/5`;
- producer positivity;
- RH.
