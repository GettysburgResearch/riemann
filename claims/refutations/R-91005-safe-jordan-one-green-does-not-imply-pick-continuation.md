# R-91005 — Positive Jordan and one-Green kernels do not imply Pick continuation

Claim ID: `R-91005`  
Status: **EXACT ABSTRACT REFUTATION / CONTROL MODEL**  
Created: 2026-08-11  
Depends on: `L-9506`, `L-91003`, `T-91001`  
RH status: **unproved**

## 1. The proposed implication

The horizontal-transport programme starts from three true facts on the safe side:

1. the arithmetic quotient
   \[
   \zeta(s-u)/\zeta(s)
   \]
   has positive Jordan coefficients and a compound-Poisson vertical normalization in
   `Re(s)>1+u`;
2. the completed one-Green ratio
   \[
   \mathcal H_u(q)=\frac1q\frac{\xi(1+q)}{\xi(1+u+q)}
   \]
   is completely monotone for `q>0`;
3. the completed horizontal quotient
   \[
   \Theta_u(s)=\frac{\xi(s-u)}{\xi(s)}
   \]
   obeys the cocycle law and is unimodular on `Re(s)=(1+u)/2`.

The desired conclusion is positivity of the de Branges--Rovnyak kernel

\[
 K_u(s,w)=
 \frac{1-\Theta_u(s)\overline{\Theta_u(w)}}
      {s+\overline w-(1+u)}
\tag{R-91005.1}
\]

throughout the moving half-plane.  This note proves that the conclusion does **not**
follow from the three positivity/symmetry properties above as abstract data.  The exact
archimedean--arithmetic coupling must be used in a stronger way than positivity of its
safe restrictions.

## 2. Bare symmetric control

Fix

\[
 0<y<\frac12,
 \qquad 0<u<2y,
\]

and put

\[
 F_y(s)=\left(s-\frac12\right)^2-y^2,
 \qquad
 \Theta^{F}_{u,y}(s)=\frac{F_y(s-u)}{F_y(s)}.
\tag{R-91005.2}
\]

Then

\[
 F_y(1-s)=F_y(s),
 \qquad
 F_y(\overline s)=\overline{F_y(s)},
\tag{R-91005.3}
\]

so, on the moving symmetry boundary `Re(s)=(1+u)/2`,

\[
 s-u=1-\overline s,
 \qquad
 \left|\Theta^{F}_{u,y}(s)\right|=1.
\tag{R-91005.4}
\]

The family has the exact cocycle

\[
 \Theta^{F}_{u+v,y}(s)
 =\Theta^{F}_{u,y}(s)\Theta^{F}_{v,y}(s-u).
\tag{R-91005.5}
\]

Nevertheless `Theta^F_(u,y)` has an uncancelled pole at

\[
 s_0=\frac12+y,
\]

and `s_0` lies in the target half-plane precisely when `u<2y`.

### 2.1 The safe one-Green kernel is positive

At a safe real point put

\[
 f_{u,y}(q)
 =\Theta^{F}_{u,y}(1+u+q)
 =\frac{(q+\frac12-y)(q+\frac12+y)}
 {(q+\frac12+u-y)(q+\frac12+u+y)}.
\tag{R-91005.6}
\]

The one-Green ratio

\[
 h_{u,y}(q)=\frac{f_{u,y}(q)}q
\tag{R-91005.7}
\]

has the positive partial-fraction decomposition

\[
 \boxed{
 h_{u,y}(q)
 =\frac{c_0}{q}
  +\frac{c_-}{q+\frac12+u-y}
  +\frac{c_+}{q+\frac12+u+y},
 }
\tag{R-91005.8}
\]

where

\[
 c_0=\frac{\frac14-y^2}{(\frac12+u)^2-y^2}>0,
\]

\[
 c_-=
 \frac{u(2y-u)}{2y(\frac12+u-y)}>0,
 \qquad
 c_+=
 \frac{u(u+2y)}{2y(\frac12+u+y)}>0.
\tag{R-91005.9}
\]

Thus `h_(u,y)` is completely monotone and

\[
 \left(h_{u,y}\left(\frac{q_i+q_j}{2}\right)\right)_{i,j}
 \succeq0
\tag{R-91005.10}
\]

for every finite set of positive real points.

### 2.2 The target Pick kernel already fails on two safe real points

Let

\[
 a=\frac{1+u}{2},
 \qquad s_q=1+u+q.
\]

The target half-plane Pick matrix on two safe points is

\[
 \Pi(q,r)=
 \begin{pmatrix}
 \dfrac{1-f(q)^2}{1+u+2q}
 &\dfrac{1-f(q)f(r)}{1+u+q+r}\\[3mm]
 \dfrac{1-f(q)f(r)}{1+u+q+r}
 &\dfrac{1-f(r)^2}{1+u+2r}
 \end{pmatrix},
\tag{R-91005.11}
\]

with `f=f_(u,y)`.  Direct simplification gives

\[
 \boxed{
 \det\Pi(q,r)=
 -\frac{
  256u^2(q-r)^2(2y-u)(2y+u)
 }{
  D(q)^2D(r)^2
 },
 }
\tag{R-91005.12}
\]

where

\[
 D(q)=
 \bigl(1+2q+2u-2y\bigr)
 \bigl(1+2q+2u+2y\bigr)>0.
\]

Hence

\[
 \det\Pi(q,r)<0
 \qquad(q\ne r).
\tag{R-91005.13}
\]

The failure is already infinitesimal.  Since `f'(q)>0`, the half-plane
Schwarz--Pick inequality would require

\[
 f'(q)\le\frac{1-f(q)^2}{1+u+2q}.
\]

Instead one has exactly

\[
 \boxed{
 \frac{1-f(q)^2}{1+u+2q}-f'(q)
 =-\frac{16u(2y-u)(2y+u)}{D(q)^2}<0.
 }
\tag{R-91005.14}
\]

Thus positive one-Green Hankel matrices, boundary unitarity and the exact cocycle
can coexist with strict failure of every nontrivial two-point target Pick matrix.

## 3. Strengthened control retaining the zeta Jordan channel

The bare control does not contain a prime Euler product.  The following strengthened
control retains the **actual** zeta/Jordan arithmetic channel and the full positive
one-Green property.

Put

\[
 \xi_y(s)=F_y(s)\xi(s).
\tag{R-91005.15}
\]

This is entire, obeys the same functional equation and conjugation symmetry as `xi`,
and has the additional off-line zeros `1/2 +/- y`.

The one-Green ratio factors as

\[
 \frac1q\frac{\xi_y(1+q)}{\xi_y(1+u+q)}
 =R_u(q)f_{u,y}(q)B_u(q)Z_u(q),
\tag{R-91005.16}
\]

where `B_u` is the positive beta/Gamma channel and

\[
 Z_u(q)=\frac{\zeta(1+q)}{\zeta(1+u+q)}
\]

is the **unchanged** positive Jordan channel of `L-9506`, while

\[
 R_u(q)=\frac{q+1}{(q+u)(q+u+1)}.
\]

Assume now

\[
 0<u<\min\left(2y,\frac12-y\right).
\tag{R-91005.17}
\]

Then the modified rational channel has the exact positive expansion

\[
 \boxed{
 R_u(q)f_{u,y}(q)
 =\frac{A_0}{q+u}
  +\frac{A_1}{q+u+1}
  +\frac{A_-}{q+u+\frac12-y}
  +\frac{A_+}{q+u+\frac12+y},
 }
\tag{R-91005.18}
\]

with

\[
 A_0=
 \frac{(1-u)(1+2y-2u)(1-2y-2u)}{1-4y^2},
\]

\[
 A_1=
 \frac{u(1+2u-2y)(1+2u+2y)}{1-4y^2},
\]

\[
 A_-=
 \frac{u(2y-u)(1+2y-2u)}{y(1-4y^2)},
 \qquad
 A_+=
 \frac{u(u+2y)(1-2u-2y)}{y(1-4y^2)}.
\tag{R-91005.19}
\]

All four coefficients are positive and sum to one.  Thus every factor on the
right of (R-91005.16) is completely monotone, so the full one-Green realization
for `xi_y` remains positive.  Its arithmetic Jordan/compound-Poisson factor is
literally the zeta factor from the original programme.

For the concrete rational choice

\[
 y=\frac14,
 \qquad u=\frac18,
\]

one gets

\[
 R_u(q)f_{u,y}(q)
 =\frac{35/96}{q+1/8}
  +\frac{5/16}{q+3/8}
  +\frac{5/48}{q+7/8}
  +\frac{7/32}{q+9/8}.
\tag{R-91005.20}
\]

Yet the completed horizontal quotient

\[
 \Theta^{(y)}_u(s)=\frac{\xi_y(s-u)}{\xi_y(s)}
\]

has an uncancelled pole at `s=3/4`, inside the half-plane
`Re(s)>9/16`.  Its full de Branges--Rovnyak kernel therefore cannot be positive.

This control preserves:

```text
functional equation and real symmetry;
boundary unitarity;
horizontal cocycle;
the actual positive zeta Jordan channel;
a positive full one-Green Laplace measure.
```

It deliberately changes the exact completed archimedean factor.  Therefore any
successful proof for `xi` must use that exact factor and its coupling to the prime
channel, not merely positivity of the two safe feature constructions.

## 4. Correct conclusion

The proposed inference

```text
positive Jordan/compound-Poisson safe channel
+ positive one-Green safe kernel
+ cocycle and boundary unitarity
=> target Pick positivity
```

is false.

The missing theorem is precisely **contractive multiplier compatibility** with the
target Cauchy kernel.  `L-91014` shows that exact target Pick positivity on any safe
uniqueness set would already force the whole analytic continuation.  `L-91015`
identifies the finite contraction inequality that must be proved.

## 5. Boundary

```text
bare symmetric control                               EXACT
bare one-Green complete monotonicity                 EXACT
bare two-point Pick determinant                      STRICTLY NEGATIVE
zeta-Jordan-preserving completed control             EXACT
modified full one-Green positivity                   EXACT
safe positivity -> global Pick continuation          REFUTED AS AN ABSTRACT STEP
actual-xi safe Pick contraction                       OPEN / RH-EQUIVALENT
Riemann Hypothesis                                    UNPROVED
```
