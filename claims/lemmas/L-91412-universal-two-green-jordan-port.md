# L-91412 — A universal two-Green Jordan port is unconditionally positive at every horizontal scale

Claim ID: `L-91412`  
Status: **PROPOSED COMPLETE UNCONDITIONAL ARITHMETIC/HARDY SOURCE THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-12  
Authoring agent: `gpt56-pro`  
Depends on: PR #396 `L-91023` and the elementary harmonic-sum inequality  
RH status: **unproved**

## 1. Positive generalized-Jordan source

For `s>0`, put

\[
F_s(n)=\prod_{p\mid n}(1-p^{-s}),
\qquad
c_s=\frac1{\zeta(1+s)},
\]

and

\[
Z_s(q)=\frac{\zeta(1+q)}{\zeta(1+s+q)}
      =\sum_{n\ge1}\frac{F_s(n)}{n^{1+q}},
\qquad q>0.
\]

Retain the Green states

\[
E_{s,m}(t)
=
\sum_{n\ge1}\frac{F_s(n)}n
 \frac{(t-\log n)_+^m}{m!}
-c_s\frac{t^{m+1}}{(m+1)!}.
\tag{L-91412.1}
\]

PR #396 proves

\[
E_{s,m}(t)>0
\qquad(t>0,m\ge0).
\]

## 2. A uniform lower bound for the first Green derivative

Let

\[
\delta=1-\log2.
\]

### Theorem 2.1

For every `s>0` and `t>=0`,

\[
\boxed{
E_{s,0}(t)\ge c_s\delta.
}
\tag{L-91412.2}
\]

At `t=0`, `E_(s,0)(0)=1`, so the assertion is immediate. For `t>0`, put

\[
N=\lfloor e^t\rfloor.
\]

The weighted Harris–FKG inequality of `L-91023` gives

\[
\sum_{n\le N}\frac{F_s(n)}n
>c_s H_N.
\]

Therefore

\[
E_{s,0}(t)>c_s(H_N-t)
\ge c_s\bigl(H_N-\log(N+1)\bigr).
\]

The sequence

\[
H_N-\log(N+1)
\]

is increasing because

\[
\frac1{N+1}
-\log\left(1+\frac1{N+1}\right)>0.
\]

Its first value is `1-log2=delta`, proving (L-91412.2).

This is considerably stronger than mere nonnegativity and is uniform in the
horizontal scale `s` after the natural factor `c_s` is removed.

## 3. Remove two Green factors with one fixed safe pole

Let

\[
\mathcal G_s(q)
=
q(q+4)
\frac{Z_s(q)-c_s/q}{q^2}.
\tag{L-91412.3}
\]

Since

\[
\frac{Z_s(q)-c_s/q}{q^2}
=\int_0^\infty e^{-qt}E_{s,1}(t)\,dt,
\]

and `E_(s,1)(0)=0`, `E_(s,1)'=E_(s,0)`, distributional integration by parts
gives

\[
\boxed{
\begin{aligned}
\mathcal G_s(q)
={}&1+
 \sum_{n\ge2}\frac{F_s(n)}n n^{-q}\\
&+\int_0^\infty e^{-qt}
 \bigl[-c_s+4E_{s,0}(t)\bigr]dt.
\end{aligned}}
\tag{L-91412.4}
\]

The continuous density has the strict lower bound

\[
\boxed{
-c_s+4E_{s,0}(t)
\ge c_s(3-4\log2)>0.
}
\tag{L-91412.5}
\]

The last constant is positive because `log2<3/4`.

Consequently

\[
\boxed{
q\longmapsto\mathcal G_s(q)
\text{ is completely monotone for every }s>0.
}
\tag{L-91412.6}
\]

No terminal-scale restriction and no compact middle interval remain.

More generally, the same proof works with any fixed pole

\[
A\ge(1-\log2)^{-1};
\]

`A=4` is a convenient rational choice aligned with the radix-four architecture.

## 4. Exact phase-resolved Hilbert feature

For `Re z_i>0`, put

\[
\mathcal K_s(z_i,z_j)
=
\mathcal G_s(z_i+\overline{z_j}).
\]

Equation (L-91412.4) gives the explicit Gram decomposition

\[
\boxed{
\begin{aligned}
\mathcal K_s(z,w)
={}&1\\
&+\sum_{n\ge2}
 \left(\sqrt{\frac{F_s(n)}n}n^{-z}\right)
 \overline{
 \left(\sqrt{\frac{F_s(n)}n}n^{-w}\right)}\\
&+\int_0^\infty
 \left(\sqrt{-c_s+4E_{s,0}(t)}e^{-zt}\right)
 \overline{
 \left(\sqrt{-c_s+4E_{s,0}(t)}e^{-wt}\right)}dt.
\end{aligned}}
\tag{L-91412.7}
\]

Thus every finite matrix `K_s(z_i,z_j)` is PSD. Vertical phases are retained;
no termwise absolute value is taken in the Euler series.

The source environment is completely explicit:

```text
one contact coordinate;
one positive coordinate for every arithmetic atom log n;
one continuous Hardy coordinate with density -c_s+4E_(s,0).
```

## 5. Relation to the open Cauchy–Jordan route

PR #396 removed three Green factors using the sharp scale-dependent Cauchy
numerator. Its resulting density

\[
-c_{2a}+\kappa aE_{2a,0}+4a^2E_{2a,1}
\]

is positive at terminal scales and outside a compact middle interval, but its
full sign for `0<a<1/2` is open.

The present theorem changes the source design rather than estimating that same
density. It gives an unconditionally positive two-Green source port at every
scale, with a fixed safe pole at four.

A conclusion-producing continuation may now try to factor the completed Cauchy
output through (L-91412.7), using the extra stable source coordinate as an
auxiliary environment. The remaining theorem is an archimedean/pole
source-to-Hardy intertwiner; the arithmetic source positivity is no longer the
obstruction for this redesigned port.

This theorem does **not** assert that the new port is already identical to the
sharp residual of PR #396. Such an identity or contractive colligation must be
constructed explicitly.

## 6. Proof boundary

```text
uniform E_(s,0) lower bound                         PROPOSED COMPLETE
exact two-Green boundary-jet identity                EXACT
strict positive continuous density for all s,t       PROPOSED COMPLETE
complete monotonicity and phase-resolved Gram         PROPOSED COMPLETE
explicit arithmetic Hardy source environment          EXACT
identification with completed Cauchy output            OPEN / RH-BEARING
Riemann Hypothesis                                    UNPROVED
```
