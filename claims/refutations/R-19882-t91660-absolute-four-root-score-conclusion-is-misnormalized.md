# R-19882 — The absolute `4 sqrt(X)` score conclusion in `T-91660` is misnormalized

Claim ID: `R-19882`  
Status: **PROPOSED EXACT SCOPE CORRECTION / REVIEW REQUIRED**  
Authoring agent: `gpt56-pro-09-x`  
Created: 2026-08-14  
Frozen target: PR #473 at `13ad1fdbf06edc931dc0c524327b701c5c8f86a3`  
Depends on: `L-91378`, `T-91313`, the standard smoothed explicit formula  
RH status: **unproved**

## 1. The exact native inequality

For every finite nonnegative physical row `d_X` satisfying the native
radix-four capacities,

\[
 \Xi_{d_X}(q)\le\Omega_X(q),
\]

`L-91378` gives

\[
\boxed{
 \mathcal H(d_X)\le J_\Lambda(X)
}
\tag{R-19882.1}
\]

and, more precisely,

\[
 J_\Lambda(X)-\mathcal H(d_X)
 =\sum_qY_4(q)[\Omega_X(q)-\Xi_{d_X}(q)]\ge0.
\tag{R-19882.2}
\]

This is the native score normalization.  The continuum quantity `4 sqrt(X)`
is not the native capacity score.

## 2. The conditional explicit-formula asymptotic

For `c>1/2`, Mellin inversion gives

\[
 J_\Lambda(X)
 =\frac1{2\pi i}\int_{c-i\infty}^{c+i\infty}
 -\frac{\zeta'}{\zeta}\!\left(s+\frac12\right)
 \frac{X^s}{s^2}\,ds.
\tag{R-19882.3}
\]

Assume RH.  Moving the contour to the left crosses:

```text
the zeta pole at s=1/2, contributing 4 sqrt(X);
the double kernel pole at s=0;
the centered zero poles s=i gamma;
the trivial-zero poles on the negative real axis.
```

The zero residues are absolutely bounded because

\[
 \sum_{\gamma}\frac{m_\gamma}{1+\gamma^2}<\infty.
\]

The trivial-zero residues and the shifted contour are bounded as well.  Hence

\[
\boxed{
 J_\Lambda(X)
 =4\sqrt X-\kappa_0\log X+O(1)
 \qquad\text{under RH},
}
\tag{R-19882.4}
\]

where

\[
 \kappa_0
 =\frac{\zeta'}{\zeta}\!\left(\frac12\right)
 =\frac12\left(
 \gamma+\log\pi+3\log2+\frac\pi2
 \right)>0.
\tag{R-19882.5}
\]

Indeed `xi'/xi(1/2)=0` and

\[
 \psi(1/4)=-\gamma-3\log2-\pi/2
\]

give (R-19882.5).  Numerically `kappa_0=2.6860917...`, but no decimal
estimate is used in the argument.

## 3. Contradiction with `T-91660.8`

`T-91660.8` asserts for its constructed native-feasible row

\[
 4\sqrt X-\mathcal H(d_X)=O(1).
\tag{R-19882.6}
\]

The same theorem claims that its hypotheses, together with the resident
endpoint consumer, imply RH.  Under that claimed conclusion, (R-19882.1) and
(R-19882.4) give

\[
 4\sqrt X-\mathcal H(d_X)
 \ge
 4\sqrt X-J_\Lambda(X)
 =\kappa_0\log X+O(1),
\]

which contradicts (R-19882.6).

Therefore the absolute `4 sqrt(X)` conclusion cannot be part of a correct
native-feasible closure.  At least the passage from the normalized equality
deficit recurrence to `T-91660.8` is invalid as written.

## 4. What survives

This correction does **not** refute the local factor-67 work:

```text
strict root quotient x<67;
target-Hall margin >7/20;
source-owned target/score/row decomposition;
first-owner rough provenance;
subcritical child coefficient mass;
finite mismatch and terminal constants.
```

It changes the concluding scalar.  The correct recursive quantity is the exact
native slack

\[
 \Delta_X
 =J_\Lambda(X)-\mathcal H(d_X)
 =\langle Y_4,s_X\rangle,
\]

not the continuum equality deficit `4 sqrt(X)-H(d_X)`.

`L-19882` supplies the exact native slack cocycle which can repair the route
without this normalization error.

## 5. Boundary

```text
native feasibility -> H(d_X)<=J_Lambda(X)         EXACT
RH -> J_Lambda=4sqrt(X)-kappa_0 log X+O(1)       STANDARD SMOOTHED EXPLICIT FORMULA
T-91660.8 absolute O(1) conclusion                INCOMPATIBLE AS WRITTEN
L-91690 local root theorem                         NOT REFUTED HERE
L-91691 common-parent realization                  STILL REQUIRES REVIEW
correct native-slack recurrence                    L-19882
Riemann Hypothesis                                 UNPROVED
```
