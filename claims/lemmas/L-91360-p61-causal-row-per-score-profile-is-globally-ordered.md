# L-91360 — The `P_61` causal row-per-score profile is globally ordered

Claim ID: `L-91360`  
Status: **PROVED EXACT CAUSAL MONOTONICITY THEOREM — DIRECTED COMPACT GATE PROVIDED**  
Created: 2026-08-13  
Depends on: `L-91359`; exact component-row cell calculus  
RH status: **unproved**

## 1. Single-endpoint profile

For `2<=j<=66`, put

\[
 S(Y)=5\sqrt Y-3,
 \qquad
 \phi_j(Y)=\frac{Q_Y(j)}{S(Y)},
\tag{L-91360.1}
\]

with the causal convention `Q_Y(j)=0` for `Y<j`.  `L-91359` proves that
`phi_j` is nondecreasing on the complete half-line and strictly increasing once
the row is active.

Write

\[
 \dot\phi_j(Y)=Y\phi_j'(Y).
\tag{L-91360.2}
\]

## 2. Causal normalized row

Let

\[
 p\ge67,
 \qquad r=p^{-1/2},
 \qquad1\le z\le67.
\]

Define

\[
 \boxed{
 \mathcal R_{p,j}(z)
 =\frac{Q_{pz}(j)-rQ_z(j)}{S(pz)-rS(z)}.
 }
\tag{L-91360.3
}

The denominator is positive.  This is exactly the causal component-row mass per
unit causal endpoint-score mass at source ratio `z=y/d`.

Put

\[
 \lambda_p(z)=r\frac{S(z)}{S(pz)}.
\tag{L-91360.4}

Then

\[
 \mathcal R_{p,j}(z)
 =\frac{\phi_j(pz)-\lambda_p(z)\phi_j(z)}{1-\lambda_p(z)}.
\tag{L-91360.5}

For `z>=1`, direct differentiation gives

\[
 0\le\lambda_p(z)<\frac1p
\tag{L-91360.6}
\]

and

\[
 \dot\lambda_p(z)>0.
\tag{L-91360.7}

Indeed, writing `t=sqrt(z)`,

\[
 \lambda_p(z)
 =\frac1p\frac{5t-3}{5t-3/\sqrt p},
\]

whose denominator is larger than its numerator and whose derivative in `t` is
positive.

## 3. Sufficient derivative inequality

Differentiate (L-91360.5) with respect to `log z`.  One obtains

\[
\boxed{
\begin{aligned}
 \dot{\mathcal R}_{p,j}(z)
 ={}&\frac{
  (1-\lambda_p)
  [\dot\phi_j(pz)-\lambda_p\dot\phi_j(z)]
 }{(1-\lambda_p)^2}\\
 &+\frac{
  \dot\lambda_p[\phi_j(pz)-\phi_j(z)]
 }{(1-\lambda_p)^2}.
\end{aligned}}
\tag{L-91360.8
}

The second term is nonnegative by `L-91359`.  In view of
`lambda_p<1/p`, it is therefore sufficient to prove

\[
\boxed{
 \dot\phi_j(pz)\ge\frac1p\dot\phi_j(z).
}
\tag{L-91360.9
}

For `z<j`, the right side is zero and the claim is immediate.  It remains to
check the compact active range

\[
 j\le z\le67.
\]

## 4. Parent lower bound

Retain the constants of `L-91359`:

\[
 c_j=\frac2{j(j-1)},
 \qquad
 \eta_j>0,
 \qquad
 K_j,
\]

and put

\[
 D_j=22c_j+10\eta_j+5K_j.
\tag{L-91360.10}

`L-91359` proves for `Y>=83`

\[
 M_j(Y)
 \ge\sqrt Y[5\eta_j\log Y-D_j]+6\eta_j,
\tag{L-91360.11}

where

\[
 \dot\phi_j(Y)=\frac{M_j(Y)}{2S(Y)^2}.
\]

Since `S(Y)<5sqrt(Y)`, for `pz>=67j>=134`,

\[
\boxed{
 p\dot\phi_j(pz)
 \ge
 \frac{\sqrt p}{50\sqrt z}
 [5\eta_j\log(pz)-D_j]
 +\frac{3\eta_j}{25z}.
}
\tag{L-91360.12
}

The companion checker proves that the first term in (L-91360.12) is increasing
in `p` for every `p>=67` and `z>=j`.  Thus the lower bound is minimized at
`p=67`.

## 5. One directed gate per child activation cell

On a child cell

\[
 N\le z<N+1,
 \qquad j\le N\le66,
\]

write

\[
 Q_z(j)=C_{j,N}\log z-D_{j,N}.
\]

The normalized derivative is

\[
 \dot\phi_j(z)=\frac{M_j(z)}{2S(z)^2}.
\]

Inside the cell, `M_j` decreases and `S` increases, so `dot(phi_j)` is maximized
at the left endpoint `z=N+`.  The parent lower bound in (L-91360.12) is bounded
from below throughout the cell by

\[
\boxed{
 \frac{\sqrt{67}}{50\sqrt{N+1}}
 [5\eta_j\log(67N)-D_j]
 +\frac{3\eta_j}{25(N+1)}.
}
\tag{L-91360.13
}

The standard-library directed replay checks all

\[
 \sum_{j=2}^{66}(67-j)=2145
\]

row/cell gates and proves that (L-91360.13) is strictly larger than the exact
left-endpoint value of `dot(phi_j)`.

Consequently (L-91360.9) holds for every `p>=67` and `j<=z<=67`.  Equation
(L-91360.8) now gives

\[
\boxed{
 \mathcal R_{p,j}(z)
 \text{ is nondecreasing in }z.
}
\tag{L-91360.14
}

## 6. Source-order formulation

For the causal packet at child endpoint `y`, put `z=y/d`.  Since `z` decreases
as `d` increases, (L-91360.14) proves

\[
\boxed{
 d_1<d_2\le y
 \Longrightarrow
 \frac{K_R^{(j)}(d_1)}{K_S(d_1)}
 \ge
 \frac{K_R^{(j)}(d_2)}{K_S(d_2)}.
}
\tag{L-91360.15
}

If `1<=z<j`, the child row is inactive and the same conclusion follows from
(L-91360.8) with `dot(phi_j)(z)=0`.

For `d>y`, the child score and row atoms vanish; `L-91359` gives the same source
ordering directly from `phi_j(py/d)`.  At the transition `d=y`, the child row is
zero but the child score is positive, so the inner ratio is at least the
frontier limiting ratio.  Hence the two sectors splice in the correct order.

Thus for every active source divisor,

\[
\boxed{
 d\longmapsto
 \frac{K_R^{(j)}(d)}{K_S(d)}
 \text{ is nonincreasing.}
}
\tag{L-91360.16
}

This closes the causal-profile monotonicity hypothesis of the Lorenz bathtub
theorem `L-91358`.

## 7. Verification

The companion replay uses exact `Fraction` arithmetic and directed rational
square-root/logarithm enclosures.  It certifies:

```text
65 monotonicity-in-p gates;
2145 child activation-cell comparisons;
strict positivity of every derivative-scaling gap.
```

Retained verdict:

```text
PASS_INNER_CAUSAL_COMPONENT_RATIO_MONOTONICITY
```

## 8. Proof boundary

```text
single-endpoint global normalized monotonicity      AVAILABLE / L-91359
inner causal derivative scaling                     DIRECTED EXACT
frontier source ratio ordering                      EXACT
complete causal row-per-score monotonicity          EXACT
Lorenz bathtub gate 1                               CLOSED
full even/odd average determinant                   OPEN / LAST LRPT GATE
literal row-packet typing after determinant         IMMEDIATE / L-91358
Riemann Hypothesis                                  UNPROVEN
```
