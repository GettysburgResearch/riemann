# L-91344 — A finite Euler component row is one positive rough-lattice Green bulk plus two adjacent boundary splines

Claim ID: `L-91344`  
Status: **PROVED EXACT GREEN-DECOMPOSITION THEOREM — TWO-SPLINE SIGN GATE OPEN**  
Created: 2026-08-12  
Depends on: retained component-row formula `L-91112.25`; `O-91309`  
RH status: **unproved**

## 1. Logarithmic ramp notation

For real `x>=1` and integer `k>=1`, put

\[
 \ell_x(k)=k^{-1/2}\log(x/k)\,\mathbf1_{k\le x}.
\tag{L-91344.1}
\]

Let `P` be any finite squarefree product and define

\[
 \boxed{
 \mathcal G_P(z)
 =\sum_{\substack{d\mid P\\d\le z}}
  \frac{\mu(d)}{\sqrt d}\log(z/d),
 }
\tag{L-91344.2
}

and the positive rough-lattice Green sum

\[
 \boxed{
 \mathcal R_P(x)
 =\sum_{\substack{k\le x\\(k,P)=1}}
  \frac1{\sqrt k}\log(x/k).
 }
\tag{L-91344.3
}

The first function is a finite signed activation spline.  The second is
coefficientwise positive.

## 2. Exact three-sector form of one component row

For integer `j>=2`, the positive component row can be written as

\[
\boxed{
 Q_Y(j)
 =A_j\ell_Y(j)+B_j\ell_Y(j+1)
  +C_j\sum_{m\ge j+2}\ell_Y(m),
}
\tag{L-91344.4
}

where

\[
 A_j=\frac{j+1}{j-1},
 \qquad
 B_j=-\frac{(j+1)(j-2)}{j(j-1)},
 \qquad
 C_j=\frac2{j(j-1)}.
\tag{L-91344.5
}

The identities

\[
 \boxed{
 A_j-C_j=\frac{j+2}{j},
 \qquad
 B_j-C_j=-1
 }
\tag{L-91344.6
}

are the source of the collapse below.

## 3. Finite Euler transform

Define the finite-block transformed row

\[
 \boxed{
 \mathcal Q_{P,x}(j)
 =\sum_{d\mid P}\frac{\mu(d)}{\sqrt d}
  Q_{x/d}(j),
 }
\tag{L-91344.7
}

with causal zero extension.

Substitute (L-91344.4), put `k=dm`, and collect the coefficient of the formal
ramp `ell_x(k)`.  The tail sector contributes

\[
 C_j\sum_{\substack{d\mid P\\d\mid k}}\mu(d),
\]

except for the two removed boundary values `m=j,j+1`.  Therefore the complete
coefficient is

\[
\begin{aligned}
 &C_j\sum_{\substack{d\mid P\\d\mid k}}\mu(d)\\
 &\quad +(A_j-C_j)
   \mu(k/j)\mathbf1_{j\mid k,\;k/j\mid P}\\
 &\quad +(B_j-C_j)
   \mu(k/(j+1))
   \mathbf1_{j+1\mid k,\;k/(j+1)\mid P}.
\end{aligned}
\tag{L-91344.8}

The divisor sum is exactly `1_((k,P)=1)`.  Using (L-91344.6) and resumming the
two boundary sequences gives the exact Green decomposition

\[
\boxed{
\begin{aligned}
 \mathcal Q_{P,x}(j)={}&
 \frac2{j(j-1)}\mathcal R_P(x)\\
 &+\frac{j+2}{j\sqrt j}
   \mathcal G_P(x/j)\\
 &-\frac1{\sqrt{j+1}}
   \mathcal G_P(x/(j+1)).
\end{aligned}}
\tag{L-91344.9
}

No approximation or unreviewed endpoint identity is used.

## 4. One-prime splice normal form

For `p>1`, put `r=p^-1/2` and define

\[
 \Delta_p\mathcal R_P(y)
 =\mathcal R_P(py)-r\mathcal R_P(y),
\tag{L-91344.10}
\]

\[
 \Delta_p\mathcal G_P(z)
 =\mathcal G_P(pz)-r\mathcal G_P(z).
\tag{L-91344.11}
\]

The exact one-prime row splice of `O-91309` is therefore

\[
\boxed{
\begin{aligned}
 \mathscr R_{p,y}(j)={}&
 \frac2{j(j-1)}\Delta_p\mathcal R_P(y)\\
 &+\frac{j+2}{j\sqrt j}
  \Delta_p\mathcal G_P(y/j)\\
 &-\frac1{\sqrt{j+1}}
  \Delta_p\mathcal G_P(y/(j+1)).
\end{aligned}}
\tag{L-91344.12
}

Thus the unbounded component-row sum has disappeared.  The only signed terms
are two adjacent evaluations of one scalar finite spline.

## 5. The Green bulk is coefficientwise positive

For every integer `k` coprime to `P`,

\[
 \ell_{py}(k)-r\ell_y(k)\ge0,
\]

with causal interpretation when `y<k<=py`.  Hence

\[
 \boxed{
 \Delta_p\mathcal R_P(y)>0.
 }
\tag{L-91344.13
}

The single term `k=1` gives the explicit lower bound

\[
\boxed{
 \Delta_p\mathcal R_P(y)
 \ge\log p+(1-r)\log y
 \ge\log p.
}
\tag{L-91344.14
}

Every possible failure of the one-prime row splice must therefore come from the
finite boundary combination

\[
\boxed{
 \mathfrak B_{p,y,j}
 =\frac{j+2}{j\sqrt j}
  \Delta_p\mathcal G_P(y/j)
 -\frac1{\sqrt{j+1}}
  \Delta_p\mathcal G_P(y/(j+1)).
}
\tag{L-91344.15
}

## 6. Specialization to the current route

Take

\[
 P=P_{79}=\prod_{q\le79}q,
 \qquad
 p\ge83,
 \qquad
 1\le y<83.
\]

Only inherited rows `2<=j<=y` occur in the child packet.  Therefore the complete
open row theorem is the finite-index scalar family

\[
\boxed{
 \mathfrak B_{p,y,j}
 \ge-rac2{j(j-1)}\Delta_p\mathcal R_{P_{79}}(y),
 \qquad
 2\le j\le y<83,
 \quad p\ge83.
}
\tag{L-91344.16
}

Rows `j>y` have no inherited child contribution and belong to the
current-generation frontier.

This replaces an unbounded row/carry statement by:

```text
81 possible inherited row indices;
one rough-prime parameter p>=83;
one bounded child variable 1<=y<83;
two scalar P_79 activation splines;
one explicit positive Green lower bound.
```

The target and score splice still require their own source-level inequalities,
but the row part has no remaining matrix or high-dimensional kernel.

## 7. Exact verification of the algebra

The companion checker treats every ramp `ell_x(k)` as an independent formal
symbol.  For multiple finite prime sets and rows it compares:

1. direct expansion of the finite Euler transform of (L-91344.4);
2. the coefficient dictionary produced by (L-91344.9);
3. the one-prime difference (L-91344.12).

Retained verdict:

```text
PASS_FINITE_EULER_GREEN_DECOMPOSITION
```

## 8. Proof boundary

```text
finite Euler component-row Green identity          EXACT
positive rough-lattice bulk                         EXACT
explicit bulk lower bound log p                     EXACT
one-prime row reduced to two scalar splines         EXACT
P_79 two-spline inequality                          OPEN / FINITE-PARAMETRIC
one-prime target/score source splice                OPEN
Riemann Hypothesis                                  UNPROVEN
```