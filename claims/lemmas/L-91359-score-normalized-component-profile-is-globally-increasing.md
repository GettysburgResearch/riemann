# L-91359 — The score-normalized component profile is globally increasing

Claim ID: `L-91359`  
Status: **PROVED EXACT GLOBAL MONOTONICITY THEOREM — DIRECTED FINITE GATE PROVIDED**  
Created: 2026-08-13  
Depends on: retained component-row formula `L-91112.25`; `L-91341/L-91342`; elementary integral comparison  
RH status: **unproved**

## 1. Component row and normalization

For an integer row

\[
 2\le j\le66
\]

and real endpoint `Y>=1`, retain the exact positive component row

\[
 Q_Y(j)
 =(j+1)\Delta^2\left[\frac{S_Y(j)}{j-1}\right]\ge0.
\tag{L-91359.1}
\]

Define

\[
 \boxed{
 \Phi_j(Y)=\frac{Q_Y(j)}{5\sqrt Y-3}
 }
\tag{L-91359.2}
\]

on the active range `Y>=j`.  The denominator is positive there.

`L-91341/L-91342` already prove by directed cell calculus that `Phi_j` is
strictly increasing through `Y<83`.  The purpose here is to close the complete
half-line.

## 2. Exact Green form

Put

\[
 c_j=\frac2{j(j-1)},
 \qquad
 a_j=\frac{j+2}{j\sqrt j},
 \qquad
 b_j=\frac1{\sqrt{j+1}}.
\tag{L-91359.3}

For

\[
 \mathscr S(Y)=
 \sum_{m\le Y}\frac1{\sqrt m}\log\frac Ym,
\tag{L-91359.4}

and `Y>=j+1`, the corrected finite-Green identity gives

\[
\boxed{
\begin{aligned}
 Q_Y(j)={}&c_j\mathscr S(Y)
 -c_j\sum_{m<j}\frac1{\sqrt m}\log\frac Ym\\
 &+a_j\log\frac Yj
 -b_j\log\frac Y{j+1}.
\end{aligned}}
\tag{L-91359.5
}

No asymptotic expansion of zeta is used below.

## 3. Elementary upper bound for the logarithmic lattice ramp

For fixed `Y`, the function

\[
 f_Y(t)=t^{-1/2}\log(Y/t)
\]

is positive and decreasing on `[1,Y]`.  Therefore

\[
 \sum_{m\le Y}f_Y(m)
 \le f_Y(1)+\int_1^Yf_Y(t)dt.
\]

The integral is elementary:

\[
 \int_1^Yt^{-1/2}\log(Y/t)dt
 =4\sqrt Y-4-2\log Y.
\]

Hence

\[
\boxed{
 \mathscr S(Y)
 \le4\sqrt Y-4-\log Y.
}
\tag{L-91359.6
}

## 4. Fixed row constants

Put

\[
 H_{j-1}=\sum_{m<j}m^{-1/2},
 \qquad
 L_{j-1}=\sum_{m<j}m^{-1/2}\log m,
\tag{L-91359.7}

and define

\[
\boxed{
 \eta_j=c_j(1+H_{j-1})-a_j+b_j,
}
\tag{L-91359.8
}

\[
\boxed{
 K_j=-4c_j+c_jL_{j-1}-a_j\log j+b_j\log(j+1).
}
\tag{L-91359.9
}

Substitution of (L-91359.6) into (L-91359.5) gives

\[
\boxed{
 Q_Y(j)
 \le4c_j\sqrt Y-\eta_j\log Y+K_j.
}
\tag{L-91359.10
}

The companion directed checker proves

\[
 \boxed{
 \eta_j>0
 \qquad(2\le j\le66).
 }
\tag{L-91359.11
}

## 5. Bounds for the logarithmic derivative coefficient

On one activation cell `N<=Y<N+1`, write

\[
 Q_Y(j)=C_{j,N}\log Y-D_{j,N}.
\]

For `N>=j+1`, differentiation of (L-91359.5) gives

\[
 C_{j,N}
 =c_j\sum_{m\le N}m^{-1/2}
  -c_jH_{j-1}+a_j-b_j.
\tag{L-91359.12}

At the right endpoint `Y=N+1`, the elementary sum bounds

\[
 2(\sqrt Y-1)
 \le\sum_{m\le N}m^{-1/2}
 \le2\sqrt Y-1
\]

give

\[
\boxed{
 2c_j\sqrt Y-c_j-\eta_j
 \le C_{j,N}
 \le2c_j\sqrt Y-\eta_j.
}
\tag{L-91359.13
}

## 6. Global derivative lower bound

The normalized derivative numerator is

\[
 M_j(Y)
 =5\sqrt Y\,[2C_{j,N}-Q_Y(j)]-6C_{j,N}.
\tag{L-91359.14}

As in `L-91341`,

\[
 M_j'(Y)=-\frac{5Q_Y(j)}{2\sqrt Y}\le0
\]

inside one activation cell, so the cell minimum is at its right endpoint.
Using the lower bound for `C`, the upper bound for `Q`, and then the upper bound
for the final negative `-6C` term yields

\[
\boxed{
 M_j(Y)
 \ge
 \sqrt Y\left[
  5\eta_j\log Y-22c_j-10\eta_j-5K_j
 \right]+6\eta_j.
}
\tag{L-91359.15
}

The bracket is increasing in `Y`.  The companion exact checker evaluates the
65 fixed row constants and proves

\[
\boxed{
 5\eta_j\log83-22c_j-10\eta_j-5K_j>0
 \qquad(2\le j\le66).
}
\tag{L-91359.16
}

Therefore `M_j(Y)>0` at every right cell endpoint `Y>=83`, and hence throughout
every such cell.

Combining with the directed finite-window theorem below `83` gives

\[
\boxed{
 \Phi_j(Y)=\frac{Q_Y(j)}{5\sqrt Y-3}
 \text{ is strictly increasing for every }Y\ge j.
}
\tag{L-91359.17
}

## 7. Frontier consequence for the causal packet

For a causal one-prime source `d>y`, the child term is inactive.  Thus

\[
 \frac{K_R^{(j)}(d)}{K_S(d)}
 =\Phi_j(py/d).
\tag{L-91359.18}

Since `py/d` decreases with `d`, (L-91359.17) gives

\[
\boxed{
 y<d_1<d_2
 \Longrightarrow
 \frac{K_R^{(j)}(d_1)}{K_S(d_1)}
 >
 \frac{K_R^{(j)}(d_2)}{K_S(d_2)}.
}
\tag{L-91359.19
}

Hence the complete child-inactive activation/frontier sector has the required
monotone row-per-score order.  The only remaining profile-monotonicity question
in `L-91358` is the bounded inner sector `d<=y<=67`, where both parent and child
terms are active.

## 8. Verification

The companion replay uses exact `Fraction` arithmetic and directed rational
square-root/logarithm enclosures to prove (L-91359.11) and (L-91359.16) for all
65 rows.

Retained verdict:

```text
PASS_GLOBAL_SCORE_NORMALIZED_COMPONENT_MONOTONICITY_REDUCTION
```

## 9. Proof boundary

```text
finite-window normalized monotonicity             IMPORTED DIRECTED EXACT
elementary global lattice-ramp bound              EXACT
65 large-Y constant gates                         DIRECTED EXACT
global score-normalized component monotonicity    EXACT
causal frontier ratio monotonicity                 EXACT
bounded inner causal ratio monotonicity            OPEN / FINITE
full even/odd average determinant                  OPEN
literal row-packet typing                          OPEN / LRPT
Riemann Hypothesis                                 UNPROVEN
```
