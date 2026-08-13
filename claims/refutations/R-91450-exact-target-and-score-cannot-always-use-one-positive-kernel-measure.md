# R-91450 — Exact target and score cannot always be represented by one common positive kernel measure

Claim ID: `R-91450`  
Status: **EXACT SOURCE-CONE FIREWALL / TARGET-SUBORDINATION IS NECESSARY**  
Created: 2026-08-12  
Depends on: `L-91113`, `L-91339`, `L-91340`  
Corrects: any strengthening of `L-91340` from score-exact/target-subordinate to exactness in both ledgers  
RH status: **unproved**

## 1. The common-measure cone

Retain the positive kernels

\[
 W_\Psi(x,n)=\frac{4\sqrt x}{n}-\frac3{\sqrt n},
 \qquad
 W_S(x,n)=\frac{5\sqrt x}{n}-\frac3{\sqrt n}.
\]

For every positive coefficient measure `nu`, put

\[
 T_x(\nu)=\sum_n\nu(n)W_\Psi(x,n),
 \qquad
 S_x(\nu)=\sum_n\nu(n)W_S(x,n).
\]

Pointwise,

\[
\boxed{
 4W_S(x,n)-5W_\Psi(x,n)=\frac3{\sqrt n}>0.
}
\tag{R-91450.1}
\]

Therefore every nonzero common positive measure satisfies

\[
\boxed{
 4S_x(\nu)-5T_x(\nu)>0,
 \qquad
 \frac{S_x(\nu)}{T_x(\nu)}>\frac54.
}
\tag{R-91450.2}
\]

This is an intrinsic cone restriction. It is independent of the chosen Hall
transport.

## 2. An exact finite-forcing witness outside the cone

Take the small-prime Boolean forcing of `L-91113` at `x=5`. The active divisors
of `P_53` are exactly

\[
 1,2,3,5.
\]

Put

\[
 A=1-\frac1{\sqrt2}-\frac1{\sqrt3}-\frac1{\sqrt5},
 \qquad
 B=1-\frac12-\frac13-\frac15=-\frac1{30}.
\]

The finite forcing target and score are

\[
 T=4\sqrt5\,B-3A,
 \qquad
 S=5\sqrt5\,B-3A.
\tag{R-91450.3}
\]

Both are positive. Indeed, using

\[
 \sqrt2<\frac32,
 \qquad
 \sqrt3<\frac74,
 \qquad
 \sqrt5<\frac94,
\]

one obtains

\[
\begin{aligned}
 T
 &=-\frac{2\sqrt5}{15}-3
   +\frac3{\sqrt2}+\frac3{\sqrt3}+\frac3{\sqrt5}\\
 &> -\frac3{10}-3+2+\frac{12}{7}+\frac43
 =\frac{367}{210}>0.
\end{aligned}
\tag{R-91450.4}
\]

The same radical bounds give

\[
 \frac1{\sqrt2}+\frac1{\sqrt3}+\frac1{\sqrt5}
 >\frac23+\frac47+\frac49>1,
\]

so `A<0`. Directly,

\[
\boxed{
 4S-5T=3A<0.
}
\tag{R-91450.5}
\]

Consequently

\[
 0<S<\frac54T.
\]

No common positive measure `nu` can reproduce both values exactly.

## 3. Correct interpretation of `L-91340`

`L-91340` does **not** make the false assertion refuted above. It represents the
score exactly and proves that the target consumed by the same positive measure
is no larger than the available signed target.

The strict asymmetry

```text
score exact;
target subordinate;
```

is therefore necessary, not cosmetic. At some finite forcing states exactness
in both ledgers is algebraically impossible inside the one-measure kernel cone.

## 4. Consequence for the reset splice

A complete reset must carry the unused target as genuine positive capacity; it
must not silently identify it with zero or demand equality of target measures.
The all-generation physical row theorem must preserve the order

\[
 T_{\rm child+output}\le T_{\rm parent}
\]

while preserving endpoint score exactly. `L-91451` records the larger physical
two-ray cone in which both ledgers may be represented, but that enlargement by
itself does not supply the favorable score orientation of `L-91340`.

```text
common positive W_Psi/W_S measure cone              S/T>5/4 EXACT
finite P53 forcing at x=5                            OUTSIDE CONE EXACT
exact target and score from one positive measure     IMPOSSIBLE IN GENERAL
score-exact / target-subordinate representation      NECESSARY
all-generation ordered capacity splice               OPEN / RH-BEARING
Riemann Hypothesis                                   UNPROVEN
```
