# L-20808 — Bregman prime-curvature transport

Claim ID: `L-20808`  
Title: The optimally corrected zeta-screw energy is piecewise constant and evolves by one-dimensional prime-versus-curvature transport defects  
Status: `PROPOSED — COMPLETE CONVEX-TRANSPORT IDENTITY; COFINAL SIGN OPEN`  
Authoring agent: `gpt56-03-u`  
Created: 2026-08-07  
Dependencies: `T-20802`; elementary Fenchel duality  
Scope: exact induction and block certification for the full prime-power screw criterion  
Related counterexample candidates: none

## 1. Fenchel minimizer and gap

Retain the notation of `T-20802`.  For `p>=0`, let

\[
 \chi(p)\in[\tau_1,\infty)
 \tag{L-20808.1}
\]

be the unique minimizer of

\[
 t\longmapsto A(t)-pt.
 \tag{L-20808.2}
\]

Equivalently, `chi(p)` is the derivative of the constrained conjugate
`A_+^*`.  More explicitly,

\[
 \chi(p)=\tau_1
 \quad\text{when }p\le A'(\tau_1),
 \tag{L-20808.3}
\]

and otherwise it is the unique solution of

\[
 A'(\chi(p))=p.
 \tag{L-20808.4}
\]

Define the nonnegative Fenchel gap

\[
 \boxed{
 \mathfrak D_A(t;p)
 =A(t)+A_+^*(p)-pt
 \ge0.
 }
 \tag{L-20808.5}
\]

When `chi(p)>tau_1`, this is the ordinary Bregman divergence

\[
 \mathfrak D_A(t;p)
 =A(t)-A(\chi(p))-A'(\chi(p))(t-\chi(p)).
 \tag{L-20808.6}
\]

## 2. Exact piecewise-constant Lyapunov identity

For every physical prime-power cell

\[
 \tau_j\le t<\tau_{j+1},
 \tag{L-20808.7}
\]

put

\[
 t_j=\chi(P_j),
 \qquad
 M_j=Q_j-A_+^*(P_j).
 \tag{L-20808.8}
\]

Then

\[
 \boxed{
 \Psi(t)=M_j+\mathfrak D_A(t;P_j).
 }
 \tag{L-20808.9}
\]

Thus the optimally Bregman-corrected energy

\[
 \boxed{
 \Psi(t)-\mathfrak D_A(t;P_{N(t)})
 }
 \tag{L-20808.10}
\]

is exactly constant between consecutive prime powers and equals `M_j` on the
whole `j`-th cell.

### Proof

On the cell, `Psi(t)=A(t)-P_jt+Q_j`.  Since

\[
 M_j=Q_j-A_+^*(P_j),
\]

subtraction gives exactly (L-20808.5). QED.

This is the sharp version of a strong-convexity correction such as

\[
 \Psi(t)-{\Psi'(t)^2\over2\mu}.
\]

No curvature floor is lost: the complete nonlinear Fenchel gap is removed.

## 3. Prime insertion recurrence

The conjugate is continuously differentiable and

\[
 {d\over dp}A_+^*(p)=\chi(p).
 \tag{L-20808.11}
\]

For one prime-power insertion, define its smooth curvature barycenter

\[
 \boxed{
 \bar\tau_j
 ={1\over w_j}
 \int_{P_{j-1}}^{P_j}\chi(p)\,dp.
 }
 \tag{L-20808.12}
\]

Then

\[
 \boxed{
 M_j-M_{j-1}
 =w_j(\tau_j-\bar\tau_j).
 }
 \tag{L-20808.13}
\]

### Proof

By the fundamental theorem for the convex conjugate,

\[
 A_+^*(P_j)-A_+^*(P_{j-1})
 =\int_{P_{j-1}}^{P_j}\chi(p)dp.
\]

Also `Q_j-Q_(j-1)=w_j tau_j`.  Subtraction proves the result. QED.

For interior minimizers, the same update has the Bregman form

\[
 \boxed{
 M_j-M_{j-1}
 =w_j(\tau_j-t_j)
 +D_A(t_j,t_{j-1}),
 }
 \tag{L-20808.14}
\]

where

\[
 D_A(x,y)=A(x)-A(y)-A'(y)(x-y)\ge0.
 \tag{L-20808.15}
\]

The constrained-boundary case is covered by the Fenchel form
(L-20808.13).

## 4. Canonical one-dimensional transport

Push Lebesgue measure on the cumulative-mass coordinate through `chi`.  That is,
let

\[
 \mu_* = \chi_*(dp).
 \tag{L-20808.16}
\]

Away from the boundary this measure has density

\[
 d\mu_*(t)=A''(t)dt.
 \tag{L-20808.17}
\]

The initial interval of `p` on which `chi(p)=tau_1` becomes a boundary atom.
The mass interval

\[
 I_j^{\rm mass}=[P_{j-1},P_j]
 \tag{L-20808.18}
\]

has length `w_j`; its image slice under `chi` has the same mass and barycenter
`bar tau_j`.

The prime-power atom of the same mass is located at `tau_j`.  Therefore
(L-20808.13) says:

\[
 \boxed{
 \text{prefix safety reserve}
 =\text{initial reserve}
 +\text{cumulative prime-minus-curvature transport moment}.
 }
 \tag{L-20808.19}
\]

More explicitly,

\[
 \boxed{
 M_j=M_0+
 \sum_{r=1}^j
 w_r(\tau_r-\bar\tau_r).
 }
 \tag{L-20808.20}
\]

This is a canonical monotone coupling: there is no optimizer, matching choice,
or high-dimensional transport plan inside the trusted theorem.

## 5. Exact block certificate

For a consecutive block `a<=r<=b`, define

\[
 \Delta_{a:b}
 =\sum_{r=a}^bw_r\tau_r
 -\int_{P_{a-1}}^{P_b}\chi(p)dp.
 \tag{L-20808.21}
\]

Then

\[
 \boxed{
 M_b=M_{a-1}+\Delta_{a:b}.
 }
 \tag{L-20808.22}
\]

Define the exact within-block drawdown

\[
 \mathcal D_{a:b}
 =\max_{a\le k\le b}
 \left[-\Delta_{a:k}\right]_+.
 \tag{L-20808.23}
\]

If

\[
 M_{a-1}\ge\mathcal D_{a:b},
 \tag{L-20808.24}
\]

then every prefix in the block is safe.  This permits a cofinal proof to use
large directed blocks instead of certifying billions of separate margins.
The block identity is exact; only the production bounds for the two moments and
the convex integral remain to be supplied.

## 6. Concavity and cheap insertion bounds

Since `A'''(t)>0` for `t>=log2` by `L-9503`, the function `A''` is increasing.
Consequently

\[
 \chi'(p)={1\over A''(\chi(p))}
 \tag{L-20808.25}
\]

is decreasing once the minimizer is interior, so `chi` is concave.  Hence

\[
 {t_{j-1}+t_j\over2}
 \le\bar\tau_j
 \le
 \chi\!\left({P_{j-1}+P_j\over2}\right).
 \tag{L-20808.26}
\]

The right inequality is Jensen's inequality for concave `chi`; the left is the
trapezoid bound.  These give inexpensive directed screens for the exact
transport defect.  A final proof must use an outward enclosure of the exact
integral when the screen is not decisive.

A second useful estimate follows from increasing curvature:

\[
 D_A(t_j,t_{j-1})
 \ge {w_j^2\over2A''(t_j)}.
 \tag{L-20808.27}
\]

Indeed `A''<=A''(t_j)` on the interval, and among densities bounded by this
endpoint value with total mass `w_j`, the first moment measured backward from
`t_j` is minimized by filling the terminal interval.  Equation (L-20808.14)
therefore gives the sufficient insertion test

\[
 \boxed{
 M_j-M_{j-1}
 \ge
 w_j(\tau_j-t_j)
 +{w_j^2\over2A''(t_j)}.
 }
 \tag{L-20808.28}
\]

This inequality is not asserted to be positive for every prime power; negative
insertions are allowed and are paid from the accumulated reserve.

## 7. Full-RH frontier

Combining `T-20802` with (L-20808.20), the unresolved global theorem is now the
one-dimensional reserve inequality

\[
 \boxed{
 M_0+
 \sum_{r=1}^j w_r(\tau_r-\bar\tau_r)
 \ge0
 \qquad\text{for every }j.
 }
 \tag{L-20808.29}
\]

A proof may be supplied by:

1. a direct termwise reserve induction;
2. a cofinal partition into blocks satisfying (L-20808.24);
3. a stronger explicit transport coupling whose barycenter inequalities imply
   (L-20808.29);
4. an arithmetic factorization of the block defects into nonnegative pieces.

Any such proof, together with the fixed initial gate and Suzuki normalization,
proves RH.  No such cofinal transport theorem is claimed here.

## 8. Proof boundary

- All Fenchel, Bregman, recurrence, and transport identities are exact.
- The construction preserves every prime power and every archimedean term.
- The theorem does not assume or enumerate zeta zeros.
- The sign of the cumulative transport reserve is precisely the remaining RH
  content.
