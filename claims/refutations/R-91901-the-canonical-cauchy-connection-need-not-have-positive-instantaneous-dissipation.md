# R-91901 — The canonical Cauchy connection need not have positive instantaneous dissipation

Claim ID: `R-91901`  
Status: **EXACT MOVING-METRIC FIREWALL**  
Created: 2026-08-13  
Depends on: `L-91902`  
RH status: **unproved**

## 1. The tempting shortcut

`L-91902` gives the exact identity

\[
 P'-\Gamma^*P-P\Gamma
 =\mathcal R_\Gamma.
\]

It is tempting to take the canonical metric connection

\[
 \Gamma^{\rm C}=\frac12C^{-1}C'
\]

and hope that positivity of the moving contraction implies

\[
 \mathcal R_{\Gamma^{\rm C}}\succeq0.
\]

This is false even for a two-dimensional rational control at a point where the
defect itself is strictly positive.

## 2. Exact control path

Take the constant positive metric

\[
 C=\begin{pmatrix}
  1&9/10\\
  9/10&1
 \end{pmatrix}
 \tag{R-91901.1}
\]

and the diagonal multiplier path

\[
 D(u)=\operatorname{diag}(e^{-u},e^{-10u}).
 \tag{R-91901.2}
\]

Since `C'=0`, the canonical connection is

\[
 \Gamma^{\rm C}=0.
\]

Evaluate at

\[
 u_0=\log3.
\]

Then

\[
 D=D(u_0)
 =\operatorname{diag}(1/3,3^{-10}),
 \qquad
 D'=-\operatorname{diag}(1,10)D.
 \tag{R-91901.3}

## 3. The contraction defect is strictly positive

Put

\[
 P=C-DCD.
\]

Its entries are

\[
 P_{11}=\frac89,
 \qquad
 P_{22}=1-3^{-20},
 \qquad
 P_{12}=\frac9{10}(1-3^{-11}).
\]

The determinant is

\[
 \boxed{
 \det P
 =\frac{61897597351}{784526490225}>0.
 }
 \tag{R-91901.4}

Since both diagonal entries are positive,

\[
 \boxed{P\succ0.}
 \tag{R-91901.5}

Thus `D(u_0)` is a strict contraction in the `C` metric.

## 4. The canonical instantaneous remainder is indefinite

Because `Gamma^C=0`,

\[
 \mathcal R_{\Gamma^{\rm C}}
 =-\bigl[D'^*CD+DCD'\bigr].
\]

Its entries are

\[
 \mathcal R_{11}=\frac29,
 \qquad
 \mathcal R_{22}=\frac{20}{3^{20}},
 \qquad
 \mathcal R_{12}=\frac{11}{196830}.
\]

But

\[
 \boxed{
 \det\mathcal R_{\Gamma^{\rm C}}
 =-\frac{5801}{3138105960900}<0.
 }
 \tag{R-91901.6}

Hence

\[
 \boxed{
 \mathcal R_{\Gamma^{\rm C}}
 \text{ has signature }(1,1).
 }
 \tag{R-91901.7}

The moving system is contractive at `u_0`, yet its canonical instantaneous
dissipation is indefinite there.

## 5. Interpretation

A pointwise positive bounded-real remainder is a useful sufficient condition,
but it is not a necessary consequence of contractivity.  The failure is caused
by unequal decay rates coupled through a non-diagonal metric.

For the completed Xi system this means that the connection cannot be chosen
from the Cauchy metric alone.  Any successful differential proof must use the
additional source-ordered skew gauge supplied by the returned Euler,
gamma/pole, compact-bridge, reflection and delay channels.

Equivalently, one must prove a global small-gain theorem directly rather than
assume that the simplest local Lyapunov density has one sign.

## 6. Exact boundary

```text
strict moving-metric contraction                     EXACT
canonical metric connection                          ZERO IN CONTROL
canonical instantaneous dissipation                  INDEFINITE EXACTLY
contractivity -> canonical pointwise dissipation     FALSE
source-specific completed gauge                      OPEN
safe Xi global small gain                            OPEN / RH-EQUIVALENT
Riemann Hypothesis                                   UNPROVED
```
