# T-91006 — RH is equivalent to a countable family of finite Pick matrices using only safe Euler values

Claim ID: `T-91006`  
Status: **PROPOSED COMPLETE RH-EQUIVALENT CRITERION — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: `L-91014`, the standard bounded-type property of completed xi quotients  
RH status: **unproved**

## Statement

For positive rational `u,q`, define

\[
 \vartheta_u(q)=\frac{\xi(1+q)}{\xi(1+u+q)}.
\]

For a finite tuple `q_1,...,q_N` of positive rationals, put

\[
 \boxed{
 \mathcal P_u[\mathbf q]
 =\left(
 \frac{1-\vartheta_u(q_i)\vartheta_u(q_j)}
      {1+u+q_i+q_j}
 \right)_{i,j=1}^N.
 }
\tag{T-91006.1}
\]

Then

\[
 \boxed{
 \mathrm{RH}
 \quad\Longleftrightarrow\quad
 \mathcal P_u[\mathbf q]\succeq0
 }
\tag{T-91006.2}
\]

for every positive rational `u<1`, every `N`, and every positive rational tuple
`q_1,...,q_N`.

Every entry of (T-91006.1) is evaluated at real arguments strictly larger than
one.  Thus this is a countable, finite-matrix criterion living entirely in the
absolute Euler domain.

## Proof

Under RH, the quotient

\[
 \Theta_u(s)=\frac{\xi(s-u)}{\xi(s)}
\]

is an inner function of the half-plane `Re(s)>(1+u)/2`: it is analytic there,
unimodular on the boundary by the functional equation, and of bounded type with
nonpositive mean type.  Hence its de Branges--Rovnyak kernel is positive.  Taking
`s_i=1+u+q_i` gives (T-91006.1).

Conversely assume every matrix (T-91006.1) is positive.  Fix rational `u`.  By
`L-91014`, the safe real data of `Theta_u` extend to a Schur function on the full
moving half-plane.  If RH were false, choose a zero `rho` with `Re(rho)>1/2`.
There is a rational

\[
 0<u<\min(1,2\Re(rho)-1)
\]

for which `xi(rho-u) != 0`.  Then `rho` is an uncancelled pole of `Theta_u` inside
that moving half-plane, contradicting its Schur continuation.  Functional-equation
symmetry finishes the argument.

Strict failure is finite: if RH is false, finite Nevanlinna--Pick interpolation
supplies a finite rational tuple for which (T-91006.1) has a negative eigenvalue.
Directed evaluation of the safe Euler products can in principle certify that
negative eigenvalue.

## What this theorem changes

The previous proposed interface asked to continue a positive feature kernel from
the safe domain.  `R-91005` proves that the available safe positive kernels are not
the target kernel.  The present theorem gives the exact replacement:

```text
prove finite Cauchy-multiplier contractions at safe real points;
Nevanlinna--Pick compactness performs the continuation automatically.
```

This criterion is not itself a proof of those contractions and therefore does
not prove RH.

## Boundary

```text
safe-real finite Pick criterion             PROPOSED COMPLETE
all entries in Re(s)>1                      EXACT
false RH -> finite rational matrix witness  PROPOSED COMPLETE
unconditional positivity of those matrices OPEN / RH-EQUIVALENT
Riemann Hypothesis                          UNPROVED
```
