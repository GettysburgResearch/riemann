# L-91014 — Exact Pick positivity on one safe uniqueness set already forces global Schur continuation

Claim ID: `L-91014`  
Status: **PROPOSED COMPLETE NEVANLINNA--PICK COMPLETION THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: classical finite Nevanlinna--Pick interpolation and Montel compactness  
RH status: **unproved**

## 1. Abstract theorem

Let

\[
 \mathbb H_a=\{z\in\mathbb C:\Re z>a\},
\]

let `U` be a nonempty connected open subset of `H_a`, and let `f` be analytic on
`U`.  Assume that for every finite set `z_1,...,z_N` in `U`,

\[
 \boxed{
 \left(
 \frac{1-f(z_i)\overline{f(z_j)}}
      {z_i+\overline{z_j}-2a}
 \right)_{i,j=1}^N\succeq0.
 }
\tag{L-91014.1}
\]

Then there is a unique Schur function `F` on `H_a` such that

\[
 F|_U=f.
\tag{L-91014.2}
\]

In particular the same kernel is positive for every finite set in the whole
half-plane.

The hypothesis may be restricted to a countable subset of `U` having an
accumulation point in `U`.  Consequently an interval of safe real points, or
rational points dense in such an interval, is enough.

## 2. Proof

Choose a sequence `z_1,z_2,...` in `U` with an accumulation point in `U` and
which is a uniqueness set for analytic functions there.  By the finite
Nevanlinna--Pick theorem, (L-91014.1) supplies, for every `N`, a Schur function

\[
 F_N:\mathbb H_a\to\overline{\mathbb D}
\]

interpolating

\[
 F_N(z_j)=f(z_j),
 \qquad 1\le j\le N.
\]

The family is locally bounded by one.  Montel's theorem gives a subsequence
`F_(N_l)` converging locally uniformly on `H_a` to an analytic Schur function
`F`.  For every fixed `j`, all sufficiently large members of the subsequence
interpolate `z_j`, so

\[
 F(z_j)=f(z_j)
\]

for every `j`.  The identity theorem on `U` gives `F=f` there.  Uniqueness follows
from the same identity theorem.  Positivity of the full kernel is the standard
Schur-kernel theorem.

If `f` is the restriction to `U` of a meromorphic function on `H_a`, equality on
`U` identifies its meromorphic continuation with `F`; every putative pole in
`H_a` is therefore removable.

## 3. Application to the completed horizontal transport

For `u>0`, put

\[
 a_u=\frac{1+u}{2},
 \qquad
 \Theta_u(s)=\frac{\xi(s-u)}{\xi(s)},
\tag{L-91014.3}
\]

and, for `q>0`,

\[
 \vartheta_u(q)
 =\Theta_u(1+u+q)
 =\frac{\xi(1+q)}{\xi(1+u+q)}.
\tag{L-91014.4}
\]

Every value in (L-91014.4) lies in the absolutely convergent Euler half-plane.
The exact target Pick matrix on safe real points is

\[
 \boxed{
 \mathcal P_u(q_1,\ldots,q_N)
 =\left(
 \frac{1-\vartheta_u(q_i)\vartheta_u(q_j)}
      {1+u+q_i+q_j}
 \right)_{i,j=1}^N.
 }
\tag{L-91014.5}
\]

If (L-91014.5) is positive semidefinite for every finite set of positive rational
`q_i` in any fixed open interval, then `Theta_u` has a Schur continuation to

\[
 \Re s>\frac{1+u}{2}.
\tag{L-91014.6}
\]

No separate analytic-continuation argument is needed: finite Pick positivity on
the safe slice already performs the continuation.

## 4. Countable RH criterion entirely in safe Euler values

Let `U_0` be any countable dense subset of `(0,1)`, for example the positive
rationals below one.  Consider the assertion

\[
 \boxed{
 \mathcal P_u(q_1,\ldots,q_N)\succeq0
 }
\tag{L-91014.7}
\]

for every `u in U_0`, every `N`, and every positive rational `q_1,...,q_N`.

Subject only to the standard bounded-type fact that the pole-free completed
quotient is inner/Schur in its moving half-plane, (L-91014.7) is equivalent to RH.

### RH implies (L-91014.7)

Under RH, `xi(s)` has no zeros to the right of `1/2`.  The quotient
`Theta_u` is analytic in `H_(a_u)`, has unimodular boundary values by the
functional equation, and is of bounded type with nonpositive mean type.  Hence it
is inner and its Pick kernel is positive.

### (L-91014.7) implies RH

Suppose `rho` is a zero with `beta=Re(rho)>1/2`.  Choose rational

\[
 0<u<\min(1,2\beta-1)
\]

such that `xi(rho-u) != 0`.  This is possible because the zeros of the entire
function `v -> xi(rho-v)` are discrete.  Then `rho` lies in `H_(a_u)` and is an
uncancelled pole of `Theta_u`.  But (L-91014.7) and the theorem above give an
analytic Schur continuation throughout that half-plane, a contradiction.
Functional-equation symmetry then puts every nontrivial zero on the line.

Thus false RH forces a **finite** safe-real Pick matrix with a strict negative
eigenvalue.  By continuity the parameters may all be chosen rational, and every
entry is a finite combination of safe values of `xi`, hence can be evaluated with
directed Euler tails.

## 5. Strategic meaning

The continuation requested by the horizontal-flow programme is automatic once
the exact target Pick matrices are positive on a safe uniqueness set.  The real
problem is not analytic continuation of a known positive kernel; it is proving
that the unconditional safe feature kernel is **the target contractive multiplier
kernel**.

`R-91005` proves that one-Green positivity and Jordan positivity do not supply
that identification.  `L-91015` writes the missing finite contraction explicitly.

## 6. Boundary

```text
finite Pick data -> global Schur completion          PROPOSED COMPLETE
safe real uniqueness set suffices                    PROPOSED COMPLETE
countable safe-Euler matrix criterion                 PROPOSED COMPLETE
false RH -> finite rational safe Pick failure         PROPOSED COMPLETE
one-Green/Jordan positivity -> target Pick matrices   FALSE IN GENERAL
actual-xi target Pick contraction                     OPEN / RH-EQUIVALENT
Riemann Hypothesis                                    UNPROVED
```
