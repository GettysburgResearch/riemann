# R-105380 — A positive Fourier density does not by itself force source Stieltjes positivity

Claim ID: `R-105380`  
Status: **PROVED EXACT SCOPE REFUTATION**  
Created: 2026-08-23  
Depends on: `L-105380--L-105383`  
RH status: **not assumed**

The source formulas use a positive tilted probability law. Positivity of that
law alone is not enough to prove the required moment-shape inequalities.

## 1. Odd shifted separator

Let `X` take the values `1` and `9`, each with probability `1/2`. Then

\[
x=\mathbb E[X]=5,
\qquad
y=\mathbb E[X^2]=41,
\qquad z_3=\mathbb E[X^3]=365.
\]

The unshifted order-two determinant is still positive:

\[
\det\mathsf A_2^{(0)}
={5x^2-3y\over90}
={1\over45}>0.
\tag{R-105380.1}
\]

But the shifted determinant is

\[
\boxed{
\det\mathsf A_2^{(1)}
={35x^2y+15xz_3-42y^2\over37800}
=-{919\over4725}<0.
}
\tag{R-105380.2}
\]

Thus positivity of the density, positivity of the first source pivots, and even
positivity of the first unshifted `2 by 2` block do not force the shifted
source block.

## 2. Even first-pivot separator

Let `X` take the values `1` and `16`, each with probability `1/2`. Then

\[
\mathbb E[X]={17\over2},
\qquad
\mathbb E[X^{-1}]={17\over32},
\]

so

\[
\alpha=\mathbb E[X]\mathbb E[X^{-1}]
={289\over64}>3.
\]

The first regularized even source coefficient is

\[
\boxed{
 a_0^{\rm ev}
={3-\alpha\over6}
=-{97\over384}<0.
}
\tag{R-105380.3}
\]

Hence even the first source matrix can fail for an elementary positive
probability law.

## 3. Consequence

```text
positive Xi Fourier kernel alone
  does not imply odd all-order source positivity;
  does not imply even regularized source positivity;
  does not imply OSCC105371 or BRP105220.
```

The real-saddle concentration in `L-105385`, not positivity alone, is the
additional structure that moves each fixed high-derivative source order into
the trigonometric positive cone.

## 4. Scope

These two-point laws are abstract separators, not the actual Xi tilted laws.
They prove only that a proof must use concentration or other source-specific
structure. They do not refute the Xi source inequalities.
