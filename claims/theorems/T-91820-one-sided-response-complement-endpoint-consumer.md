# T-91820 — A native-feasible row with sub-log-squared response-complement cost implies the endpoint sign and, on the frozen Mellin–Landau inputs, RH

Claim ID: `T-91820`  
Status: **CONDITIONAL ENDPOINT CONSUMER / FROZEN-INPUT RECONSTRUCTION REQUIRED**  
Created: 2026-08-15  
Depends on: the exact finite von Mangoldt dual, frozen prime-square occupancy theorem, frozen endpoint Mellin transform and Landau one-sign theorem  
RH status: **conditional at this theorem**

## 1. Hypothesis

Assume that for every sufficiently large integer `X` there is a coefficientwise nonnegative finite row `d_X` such that

\[
 \Gamma_q(d_X)\le w_X(q),
 \qquad
 \Xi_q(d_X)\le\Omega_X(q)
 \qquad(q\ge2),
\tag{T-91820.1}
\]

and

\[
 \Delta_X
 :=J_\Lambda(X)-\mathcal H(d_X)
 =o(\log^2X).
\tag{T-91820.2}

## 2. Correct one-sided orientation

The exact finite duality theorem has the orientation

\[
\boxed{
 F_\Lambda(X)
 \le J_\Lambda(X)-\mathcal H(d_X)
 =\Delta_X.
}
\tag{T-91820.3}

Thus (T-91820.2) gives

\[
 F_\Lambda(X)=o(\log^2X)
\tag{T-91820.4}

as an upper bound.  No lower bound and no absolute-value estimate is required.

## 3. Prime-square moat

The frozen unconditional prime-square occupancy theorem gives the endpoint decomposition

\[
\boxed{
 A(X)
 =F_\Lambda(X)
 -\kappa_2\log^2X
 +o(\log^2X),
}
\tag{T-91820.5}
\]

where

\[
 \kappa_2=\frac{-1-\zeta(1/2)}4>0.
\tag{T-91820.6}

Combining (T-91820.4)–(T-91820.6),

\[
 A(X)
 \le-\kappa_2\log^2X+o(\log^2X)<0
\tag{T-91820.7}
\]

for all sufficiently large `X`.

## 4. Mellin pole audit and Landau theorem

The frozen endpoint Mellin transform represents the relevant logarithmic derivative with every nontrivial zeta zero `rho` contributing a nonremovable singularity at the corresponding translated exponent.  If a zero had

\[
 \Re\rho>\frac12,
\]

the rightmost such singularity would force the inverse Mellin endpoint function to have the opposite eventual one-sign behavior by the frozen Landau theorem.  This contradicts (T-91820.7).

Therefore the frozen analytic consumer yields

\[
 \zeta(s)\ne0
 \qquad(\Re s>1/2).
\tag{T-91820.8}
\]

The functional equation and conjugation symmetry then place every nontrivial zero on

\[
 \Re s=\frac12.
\tag{T-91820.9}
\]

## 5. Forbidden shortcut

This theorem does not assume or use

\[
 J_\Lambda(X)-4\sqrt X=O(\log X).
\]

Any proof importing that statement as an unconditional pre-RH bridge is outside the theorem and must be rejected.

## 6. Boundary

```text
finite dual orientation F_Lambda <= deficit     frozen exact / reconstruct
positive prime-square moat                       frozen unconditional / reconstruct
Mellin pole audit                                frozen / reconstruct
Landau one-sign implication                      frozen / reconstruct
sub-log-squared native producer                  supplied by separate theorem
Riemann Hypothesis                               follows conditionally on all inputs
```
