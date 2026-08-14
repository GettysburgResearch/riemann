# T-92201 — The safe Xi impedance is matrix monotone of order two

Claim ID: `T-92201`  
Status: **PROPOSED UNCONDITIONAL THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-14  
Depends on: `L-92202`; positivity of the safe Xi logarithmic derivative  
RH status: **unproved**

## Statement

Let

\[
 Z(t)
 =\frac{\sqrt t}
 {\bigl(\xi'/\xi\bigr)(1/2+\sqrt t)},
 \qquad t>1/4.
\]

For any two distinct safe points `x,y`, form the Loewner matrix

\[
 \mathcal L_Z(x,y)
 =\begin{pmatrix}
 Z'(x)&\dfrac{Z(y)-Z(x)}{y-x}\\[3mm]
 \dfrac{Z(y)-Z(x)}{y-x}&Z'(y)
 \end{pmatrix}.
\]

Then, subject to review of `L-92202`,

\[
 \boxed{
 \mathcal L_Z(x,y)\succ0
 \qquad(1/4<x<y).
 }
\]

Equivalently, `Z` is matrix monotone of order two on the complete safe axis.

## Proof

`L-92202` proves

\[
 Z'(t)>0
\]

and strict concavity of

\[
 g(t)=\frac1{\sqrt{Z'(t)}}.
\]

Write

\[
 t_\theta=(1-\theta)x+\theta y.
\]

Concavity gives

\[
 g(t_\theta)
 \ge(1-\theta)g(x)+\theta g(y).
\]

Therefore

\[
\begin{aligned}
 \frac{Z(y)-Z(x)}{y-x}
 &=\int_0^1 Z'(t_\theta)\,d\theta\\
 &=\int_0^1\frac{d\theta}{g(t_\theta)^2}\\
 &\le\int_0^1
 \frac{d\theta}
 {\bigl((1-\theta)g(x)+\theta g(y)\bigr)^2}\\
 &=\frac1{g(x)g(y)}\\
 &=\sqrt{Z'(x)Z'(y)}.
\end{aligned}
\]

The inequality is strict for distinct points because `g` is strictly
concave.  Squaring yields

\[
 \det\mathcal L_Z(x,y)>0.
\]

Both diagonal entries are positive, completing the proof.

## Significance

The complete-Bernstein hierarchy on PR #449 is now closed through two
Loewner nodes:

```text
ordinary monotonicity and concavity                closed;
all two-node Loewner matrices                      closed;
all three-node Loewner matrices                    first open matrix order.
```

The exact control `R-92200` shows this is sharp as an abstract consequence:
a high conjugate off-line pair plus a lower real anchor can pass every scalar
curvature used above while failing a three-node Loewner determinant.

The theorem does not prove RH.  Complete Bernstein passivity requires
Loewner positivity at every matrix order.

## Exact boundary

```text
positive safe Xi slope                         PROPOSED UNCONDITIONAL
positive Xi Schwarzian                         PROPOSED UNCONDITIONAL
all two-node Xi Loewner matrices               PROPOSED UNCONDITIONAL
three-node Xi Loewner matrices                 OPEN / FIRST MATRIX GATE
all-order complete Bernstein                   OPEN / RH-EQUIVALENT
Riemann Hypothesis                             UNPROVED
```
