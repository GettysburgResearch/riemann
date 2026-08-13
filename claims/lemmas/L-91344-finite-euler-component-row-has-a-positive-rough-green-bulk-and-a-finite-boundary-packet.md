# L-91344 — A finite Euler component row is one positive rough-lattice Green bulk plus a finite boundary packet

Claim ID: `L-91344`  
Status: **PROVED EXACT GREEN-DECOMPOSITION THEOREM — FINITE BOUNDARY SIGN GATE OPEN**  
Created: 2026-08-12  
Corrected before promotion after exact formal-symbol replay  
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
\tag{L-91344.2}
\]

and the coefficientwise positive rough-lattice Green sum

\[
 \boxed{
 \mathcal R_P(x)
 =\sum_{\substack{k\le x\\(k,P)=1}}
  \frac1{\sqrt k}\log(x/k).
 }
\tag{L-91344.3}
\]

## 2. Exact three-sector component row

For integer `j>=2`,

\[
\boxed{
 Q_Y(j)
 =A_j\ell_Y(j)+B_j\ell_Y(j+1)
  +C_j\sum_{m\ge j+2}\ell_Y(m),
}
\tag{L-91344.4}

where

\[
 A_j=\frac{j+1}{j-1},
 \qquad
 B_j=-\frac{(j+1)(j-2)}{j(j-1)},
 \qquad
 C_j=\frac2{j(j-1)}.
\tag{L-91344.5}

The useful corrections to the full tail coefficient are

\[
 A_j-C_j=\frac{j+2}{j},
 \qquad
 B_j-C_j=-1.
\tag{L-91344.6}

For the previously absent sectors `1<=m<j`, the correction is `-C_j`.

## 3. Exact finite Euler transform

Define

\[
 \mathcal Q_{P,x}(j)
 =\sum_{d\mid P}\frac{\mu(d)}{\sqrt d}Q_{x/d}(j).
\tag{L-91344.7}

Substitute (L-91344.4), write `k=dm`, and regard every `ell_x(k)` as an
independent formal symbol.  Starting from the full tail coefficient `C_j`, the
coefficient at `k` is

\[
\begin{aligned}
 &C_j\sum_{\substack{d\mid P\\d\mid k}}\mu(d)\\
 &\quad-C_j\sum_{m=1}^{j-1}
  \mu(k/m)\mathbf1_{m\mid k,\;k/m\mid P}\\
 &\quad+\frac{j+2}{j}
  \mu(k/j)\mathbf1_{j\mid k,\;k/j\mid P}\\
 &\quad-\mu(k/(j+1))
  \mathbf1_{j+1\mid k,\;k/(j+1)\mid P}.
\end{aligned}
\tag{L-91344.8}

The complete divisor sum in the first line is `1_((k,P)=1)`.  Resumming the
finite correction sectors gives

\[
\boxed{
\begin{aligned}
 \mathcal Q_{P,x}(j)={}&
 C_j\mathcal R_P(x)\\
 &-C_j\sum_{m=1}^{j-1}\frac1{\sqrt m}
   \mathcal G_P(x/m)\\
 &+\frac{j+2}{j\sqrt j}\mathcal G_P(x/j)\\
 &-\frac1{\sqrt{j+1}}\mathcal G_P(x/(j+1)).
\end{aligned}}
\tag{L-91344.9}

This is an exact finite identity.  The boundary packet has at most `j+1`
scalar spline evaluations.  An earlier two-spline compression omitted the
sectors `m<j`; the exact formal-symbol replay caught and removed that
unpromoted over-compression.

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

Then the exact one-prime row splice of `O-91309` is

\[
\boxed{
\begin{aligned}
 \mathscr R_{p,y}(j)={}&
 C_j\Delta_p\mathcal R_P(y)\\
 &-C_j\sum_{m=1}^{j-1}\frac1{\sqrt m}
   \Delta_p\mathcal G_P(y/m)\\
 &+\frac{j+2}{j\sqrt j}
   \Delta_p\mathcal G_P(y/j)\\
 &-\frac1{\sqrt{j+1}}
   \Delta_p\mathcal G_P(y/(j+1)).
\end{aligned}}
\tag{L-91344.12}

The unbounded component-row sum has therefore collapsed to one positive Green
bulk and a finite boundary packet whose size is bounded by the inherited row
index.

## 5. The Green bulk is coefficientwise positive

For every `k` coprime to `P`,

\[
 \ell_{py}(k)-r\ell_y(k)\ge0
\]

with causal zero extension. Hence

\[
 \boxed{
 \Delta_p\mathcal R_P(y)>0.
 }
\tag{L-91344.13}

The single term `k=1` gives

\[
\boxed{
 \Delta_p\mathcal R_P(y)
 \ge\log p+(1-r)\log y
 \ge\log p.
}
\tag{L-91344.14}

All possible negativity is confined to the explicit finite boundary packet

\[
\boxed{
\begin{aligned}
 \mathfrak B_{p,y,j}={}&
 -C_j\sum_{m=1}^{j-1}\frac1{\sqrt m}
   \Delta_p\mathcal G_P(y/m)\\
 &+\frac{j+2}{j\sqrt j}
   \Delta_p\mathcal G_P(y/j)\\
 &-\frac1{\sqrt{j+1}}
   \Delta_p\mathcal G_P(y/(j+1)).
\end{aligned}}
\tag{L-91344.15
}

## 6. Specialization to the current route

Take

\[
 P=P_{79},
 \qquad p\ge83,
 \qquad1\le y<83.
\]

Only inherited rows `2<=j<=y` occur.  The complete row gate is now

\[
\boxed{
 \mathfrak B_{p,y,j}
 \ge-\frac2{j(j-1)}
       \Delta_p\mathcal R_{P_{79}}(y),
 \qquad2\le j\le y<83,
 \quad p\ge83.
}
\tag{L-91344.16
}

Thus the open row statement has:

```text
81 possible inherited row indices;
one rough-prime parameter p>=83;
one bounded child variable 1<=y<83;
at most 83 scalar P_79 activation-spline evaluations;
one explicit positive Green lower bound.
```

Rows `j>y` have no inherited child contribution and belong to the
current-generation frontier.

## 7. Exact verification

The companion checker treats every `ell_x(k)` as an independent formal symbol.
For several finite prime sets and rows it verifies:

1. direct expansion of the finite Euler transform;
2. the complete coefficient dictionary in (L-91344.8);
3. the Green formula (L-91344.9);
4. adjoining one new prime by the exact shifted-symbol identity;
5. coefficientwise positivity of the rough Green difference.

Retained verdict:

```text
PASS_FINITE_EULER_GREEN_DECOMPOSITION
```

## 8. Proof boundary

```text
finite Euler component-row Green identity          EXACT
positive rough-lattice bulk                         EXACT
explicit bulk lower bound log p                     EXACT
one-prime row reduced to finite scalar packet       EXACT
P_79 finite-boundary inequality                     OPEN / FINITE-PARAMETRIC
one-prime target/score source splice                OPEN
Riemann Hypothesis                                  UNPROVEN
```