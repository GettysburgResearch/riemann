# R-32405 — A nonnegative scale filter cannot cancel the real prime pole

Claim ID: `R-32405`  
Title: Any scale filter whose logarithmic Riesz kernel is nonnegative at every source age has strictly positive scale symbol on `(0,1)`, so it cannot cancel the real zeta pole at `2^-1/2`  
Status: **PROPOSED COMPLETE GENERAL NO-GO THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: elementary Laplace transform  
Scope: rules out an entire class of positive filtered-prime proofs; does not rule out signed filters with a globally positive aggregate

## 1. Scale-filtered logarithmic Riesz sums

Let

\[
 P_\Lambda(X)
 =\sum_{n\le X}{\Lambda(n)\over\sqrt n}\log{X\over n}.
\]

Take a real scale filter `(a_k)_(k>=0)`, finite or absolutely summable with enough first moment for the formulas below, and define

\[
\boxed{
 \mathcal F_a(X)
 =\sum_{k\ge0}a_kP_\Lambda(X/2^k).
}
\tag{R-32405.1}

Put

\[
 A(t)=\sum_{k\ge0}a_kt^k.
\tag{R-32405.2}

For one prime-power source at logarithmic age

\[
 x={\log(X/n)\over\log2}\ge0,
\]

only indices `k<=x` are active. Apart from the common positive factor `log 2`, its filtered weight is

\[
\boxed{
 W_a(x)=\sum_{0\le k\le x}a_k(x-k).
}
\tag{R-32405.3}

Thus

\[
 \mathcal F_a(X)
 =\log2\sum_{n\le X}{\Lambda(n)\over\sqrt n}
 W_a\!\left({\log(X/n)\over\log2}\right).
\tag{R-32405.4}

A proof based solely on termwise positivity of the prime source would require

\[
 W_a(x)\ge0\qquad(x\ge0).
\tag{R-32405.5}

## 2. Exact Laplace transform of the source-age kernel

For `s>0`, finite Fubini or absolute convergence gives

\[
\begin{aligned}
 \int_0^\infty W_a(x)e^{-sx}dx
 &=\sum_{k\ge0}a_k
   \int_k^\infty(x-k)e^{-sx}dx\\
 &=\sum_{k\ge0}a_k{e^{-sk}\over s^2}.
\end{aligned}
\]

Therefore

\[
\boxed{
 \int_0^\infty W_a(x)e^{-sx}dx
 ={A(e^{-s})\over s^2}.
}
\tag{R-32405.6}

This identity is the complete filter geometry. No prime estimate enters it.

## 3. Positivity forces a zero-free scale symbol

Assume

\[
 W_a(x)\ge0\qquad(x\ge0)
\]

and `W_a` is not identically zero. Then its Laplace transform is strictly positive for every `s>0`. Equation (R-32405.6) gives

\[
\boxed{
 A(e^{-s})>0\qquad(s>0).
}
\tag{R-32405.7]

Equivalently,

\[
\boxed{
 A(t)>0\qquad(0<t<1).
}
\tag{R-32405.8}

The closing bracket in tag (R-32405.7) is typographical only.

This conclusion does not require finite support, double interior cancellation, or any special choice of dyadic moments.

## 4. Real-pole cancellation is incompatible with termwise positivity

The Mellin transform of `P_Lambda` is

\[
 {1\over z^2}
 \left[-{\zeta'\over\zeta}\left(z+{1\over2}\right)\right].
\]

The scale filter multiplies it by

\[
 A(2^{-z}).
\]

The real zeta pole `s=1`, corresponding to `z=1/2`, is cancelled exactly when

\[
\boxed{
 A(2^{-1/2})=0.
}
\tag{R-32405.9]

But

\[
 0<2^{-1/2}<1,
\]

so (R-32405.8) and (R-32405.9) are incompatible.

Hence:

\[
\boxed{
 \begin{gathered}
 W_a(x)\ge0\text{ for all }x\ge0,\quad W_a\not\equiv0\\
 \Longrightarrow
 A(2^{-1/2})>0.
 \end{gathered}}
\tag{R-32405.10}

No nontrivial termwise-nonnegative scale filter can cancel the real prime pole.

## 5. Finite-filter interpretation

For a polynomial

\[
 A(t)=\sum_{k=0}^Ka_kt^k,
\]

on the annulus `r<=x<=r+1`, `r<K`, the kernel is the affine function

\[
 W_a(x)=x\sum_{k=0}^ra_k-\sum_{k=0}^rk a_k.
\]

If additionally `A(1)=A'(1)=0`, write

\[
 A(t)=(1-t)^2B(t),
 \qquad
 B(t)=\sum_{r=0}^{K-2}b_rt^r.
\]

Then exactly

\[
 W_a(r+1)=b_r,
 \qquad
 W_a(r)=b_{r-1}.
\]

So annulus-by-annulus positivity is equivalent to `b_r>=0`; the impossibility of a positive root of `A` in `(0,1)` is then visible coefficientwise. The Laplace proof above shows that the same obstruction persists without the two moment conditions and beyond finite filters.

## 6. Consequence for the live RH attacks

This rejects the tempting architecture

```text
positive von-Mangoldt coefficients
-> choose a finite/multiscale filter with nonnegative source weights
-> cancel the s=1 pole
-> Landau
-> RH.
```

The real-pole cancellation itself forces some signed physical source-age region.

Therefore any successful pole-cancelled prime proof must exploit cancellation **after aggregation**, for example through:

- a Hermitian square;
- a source-specific carry/Pascal identity;
- a signed Brownian cumulative-tail estimate;
- a coupled Selberg reserve;
- or another nonlocal positive structure.

The theorem explains why the cubic filter

\[
 (1-t)^2(1-\sqrt2t)
\]

necessarily develops a negative annular lobe despite cancelling both the deep logarithmic polynomial and the real pole.

## 7. Proof boundary

Refuted exactly:

- every finite termwise-positive pole-cancelling scale filter;
- every absolutely summable extension with a nonnegative nonzero source-age kernel;
- attempts to turn `T-32404` into an RH proof by sourcewise-positive scale filtering alone.

Not refuted:

- signed filters whose complete aggregate is positive;
- two-frequency/Hermitian mechanisms;
- carry-cycle or Brownian cumulative cancellation;
- `T-32404` itself;
- RH.
