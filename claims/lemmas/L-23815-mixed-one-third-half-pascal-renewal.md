# L-23815 — Mixed one-third/half Pascal renewal producer

Claim ID: `L-23815`  
Title: One fixed rational balanced branching law reduces BCT to positivity of a single descending renewal sequence  
Status: **PROPOSED ALTERNATIVE PRODUCER — GLOBAL SIGN OPEN**  
Authoring agent: `gpt56-pro-09-v`  
Created: 2026-08-08  
Issue: #238  
Dependencies: `L-23813`, `L-23809`  
Scope: explicit source-specific producer; finite reconnaissance is not proof

## 1. Fixed branching law

For every integer `n>=2`, put

\[
j_3(n)=\max(1,\lfloor n/3\rfloor),
\qquad
j_2(n)=\lfloor n/2\rfloor,
\]

and define

\[
\boxed{
\pi_n=\frac{31}{32}\delta_{j_3(n)}
      +\frac1{32}\delta_{j_2(n)}.}
\tag{L-23815.1}
\]

Every retained split is `1/5`-balanced.

## 2. Descending renewal

Let `R_X` be the exact Möbius-derived target divergence of `L-23810`. Starting
at `n=X` and descending, define

\[
\boxed{
d_X(n)=R_X(n)+
\sum_{m=n+1}^{X}d_X(m)
[\pi_m(n)+\pi_m(m-n)].}
\tag{L-23815.2}
\]

Put `d_X(n,j)=d_X(n)pi_n(j)`. By `L-23813`, the recurrence gives identically

\[
\partial d_X=R_X
\]

and therefore

\[
\boxed{
\sum_{n,j}d_X(n,j)\chi_{n,j}(q)=w_X(q)
\quad(2\le q\le X).}
\tag{L-23815.3}
\]

The sole sign question is

\[
\boxed{
\textbf{MPR:}\qquad d_X(n)\ge0
\quad(X\ge3,\ 2\le n\le X).}
\tag{L-23815.4}
\]

Under MPR, the mixed law gives zero-slack BCT, hence the sharp prime-ramp bound
and RH through `L-23809/T-23802`.

## 3. Why the mixture is nontrivial

Pure halving and pure one-third renewal both eventually develop negative
coefficients in finite reconnaissance; see `R-23803`. Mixing occurs in the
parent-to-child transfer before solving the renewal. The completed mixed flow is
not a convex combination of two completed pure solutions.

The dominant one-third branch retains the fixed ratio `2/3`, which is also the
first Farey/Mertens mutation elsewhere in the repository. Any proof must retain
the coherent Möbius sign and cannot estimate the two channels separately by
total variation.

## 4. Quotient-layer induction target

For fixed `Y=X/n`, the source `R_X(n)` contains only `mu(k)` with `k<=Y`, while
all incoming parents have smaller quotient. Thus MPR is a quotient-layer
induction with one fixed finite branching law.

A valid proof may use:

1. a symbolic quotient-layer reserve;
2. a finite-state `2`--`3` renewal cone;
3. Pascal-cycle repair of every downward knot;
4. a reflected Selberg square specialized to this renewal;
5. high-order Euler closure outside a finite inner layer.

## 5. Reconnaissance boundary

The accompanying directed checker certifies one modest finite endpoint. A
separate standard-library scanner reports no negative coefficient at the
retained large endpoints through `10^8`. These computations are evidence only:
they do not prove MPR, a cofinal rate, BCT, or RH.

## 6. Relationship to the preferred BTF proposal

The current preferred branch theorem `BTF` allows signed coefficients and asks
only for `X^{o(1)}` weighted negative mass. MPR is a stronger alternative: it
asks one asymmetric mixed producer to be pointwise nonnegative. A future
counterexample to MPR would not refute BTF.

## 7. Proof boundary

Closed exactly:

- the fixed rational branching law;
- descending recurrence;
- exact zero-slack saturation conditional only on coefficient sign;
- MPR implies BCT and the RH deduction.

Open and load bearing:

- MPR, equation (L-23815.4).
