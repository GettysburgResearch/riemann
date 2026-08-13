# L-91561 — The component-row entropy has an exact logarithmic kernel and dominates every rough score residual

Claim ID: `L-91561`  
Status: **PROVED EXACT SCORE-TO-ROW BRIDGE**  
Created: 2026-08-13  
Depends on: the exact component row `Q_Y(j)` and entropy row `G_j`  
RH status: **unproved**

## 1. Actual entropy of one component packet

For real `Y>=1`, put

\[
 h_Y(m)=m^{-1/2}\log(Y/m)\mathbf1_{m\le Y},
 \qquad
 S_Y(j)=\sum_{m\ge j}h_Y(m),
\]

and

\[
 Q_Y(j)=(j+1)\Delta^2\left[\frac{S_Y(j)}{j-1}\right]
 \qquad(j\ge2).
\]

Let

\[
 G_j=\frac1{j+1}\sum_{r=0}^j\log\binom jr
\]

be the actual average-binomial entropy row and define

\[
 \mathcal H(Y)=\sum_{j\ge2}Q_Y(j)G_j.
\tag{L-91561.1}
\]

All sums are finite.

## 2. Swap the triangular sums

Expanding the second difference and collecting the coefficient of `h_Y(m)`
gives

\[
 \mathcal H(Y)=\sum_{m\le Y}h_Y(m)K_m,
\tag{L-91561.2}
\]

where

\[
\boxed{
 K_m=
 \frac{m+1}{m-1}G_m
 -\frac{m(m-3)}{(m-1)(m-2)}G_{m-1}
 +2\sum_{j=2}^{m-2}\frac{G_j}{j(j-1)}.
}
\tag{L-91561.3}
\]

The absent terms are interpreted as zero.

## 3. Exact coefficient collapse

Put

\[
 P_j=\prod_{r=0}^j\binom jr,
 \qquad
 (j+1)G_j=\log P_j.
\]

Direct subtraction gives, for `m>=3`,

\[
 K_m-K_{m-1}
 =\frac{m+1}{m-1}G_m
 -\frac{2m}{m-1}G_{m-1}
 +G_{m-2}.
\tag{L-91561.4}
\]

The binomial products satisfy

\[
\boxed{
 \frac{P_mP_{m-2}}{P_{m-1}^2}
 =\left(\frac m{m-1}\right)^{m-1}.
}
\tag{L-91561.5}
\]

Hence

\[
 K_m-K_{m-1}=\log\frac m{m-1}.
\]

Since `K_2=3G_2=log 2`, induction yields

\[
\boxed{K_m=\log m.}
\tag{L-91561.6}
\]

Substituting in (L-91561.2),

\[
\boxed{
 \mathcal H(Y)
 =\sum_{2\le m\le Y}
 \frac{\log m}{\sqrt m}\log\frac Ym.
}
\tag{L-91561.7}
\]

This is the exact dictionary from component rows to the actual entropy consumed
by PR #352.

## 4. Global rough-threshold bound

A directed rational logarithm certificate gives

\[
\boxed{
 \mathcal H(67)>5\sqrt{67}-3
}
\tag{L-91561.8}
\]

with margin greater than `1.2764`.

On an open cell `N<Y<N+1`,

\[
 \mathcal H'(Y)
 =\frac1Y\sum_{m=2}^N\frac{\log m}{\sqrt m}.
\tag{L-91561.9}
\]

The function `log(t)/sqrt(t)` decreases for `t>=8`.  The tail from
`ceil(N/3)` through `N` therefore gives, for `N>=67`,

\[
 \sum_{m=2}^N\frac{\log m}{\sqrt m}
 \ge\frac{2N}{3}\frac{\log N}{\sqrt N}
 >\frac83\sqrt N
 >\frac52\sqrt{N+1}.
\tag{L-91561.10}
\]

Thus

\[
 \mathcal H'(Y)>\frac5{2\sqrt Y}.
\]

Together with (L-91561.8),

\[
\boxed{
 \mathcal H(Y)>5\sqrt Y-3
 \qquad(Y\ge67).
}
\tag{L-91561.11}
\]

## 5. Residual entropy dominates the inherited survival score

Fix `p>=67`, put `r=p^-1/2`, and let `Y>=p`.  Define

\[
 D_p(Y)=\mathcal H(Y)-\mathcal H(Y/p).
\]

At `Y=p`, (L-91561.11) gives

\[
\begin{aligned}
 D_p(p)
 &=\mathcal H(p)\\
 &>5\sqrt p-3\\
 &>5(1-p^{-1})(1-p^{-1/2})\sqrt p.
\end{aligned}
\tag{L-91561.12}
\]

On a cell `N<Y<N+1`, let `M=floor(Y/p)`.  Then

\[
 D_p'(Y)
 =\frac1Y
 \left[
  \sum_{m=2}^N\frac{\log m}{\sqrt m}
  -\sum_{m=2}^M\frac{\log m}{\sqrt m}
 \right].
\tag{L-91561.13}
\]

Because `p>=67`, one has `M<N/3`.  The same last-two-thirds estimate gives

\[
 D_p'(Y)
 >\frac5{2\sqrt Y}
 >\frac{5(1-p^{-1})(1-p^{-1/2})}{2\sqrt Y}.
\tag{L-91561.14}
\]

Integrating from `p` to `Y`,

\[
\boxed{
 \mathcal H(Y)-\mathcal H(Y/p)
 >5(1-p^{-1})(1-p^{-1/2})\sqrt Y.
}
\tag{L-91561.15}
\]

The right side is exactly the survival source-score residual for the canonical
unscaled component type.  The hazard score residual is smaller, since

\[
 p^{-1/2}(1+4p^{-1/2})
 <5(1-p^{-1}).
\]

Therefore the actual component-row residual entropy dominates both inherited
rough score residuals whenever the row normalization is the canonical one
`kappa=1`.

## 6. Boundary

The theorem supplies the score-to-row identity missing from an abstract paired
type.  It does not prove that every Hall residual on PR #424 has exactly the
canonical row normalization; that is a finite producer-normalization audit.

```text
component-row entropy kernel                    EXACT
K_m=log m coefficient collapse                  EXACT
H(Y)>5sqrt(Y)-3 for Y>=67                       DIRECTED + ANALYTIC
rough residual entropy domination               EXACT
survival/hazard canonical inherited debt        NONPOSITIVE
Hall residual row normalization kappa=1          AUDIT REQUIRED
Riemann Hypothesis                              UNPROVEN
```
