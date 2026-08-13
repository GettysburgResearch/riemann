# L-91634 — One exact parent row realizes the natural five-level quarter-score cascade

Claim ID: `L-91634`  
Status: **DIRECTED-EXACT SCORE CLOSURE ON THE FROZEN ONE-USE ROW IDENTITY; LIVE REPLAY AND INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-14  
Depends on: `R-91633`; `L-91559`; `L-91621`; exact replay `X-91634`  
Corrects the physical interpretation of: `L-91632`  
RH status: **unproved**

## 1. Correct score demand

Retain

\[
\Sigma(y)=\sum_{m\le y}\frac{\mu(m)}{\sqrt m}
\left(5\sqrt{\frac ym}-3\right),
\qquad
\mathcal P(y)=\sum_{q\le y}\frac{\Lambda(q)}{\sqrt q}\log\frac yq.
\]

The natural parent-oriented declared score is

\[
\boxed{
\mathcal A_4(x)=\sum_{j=0}^4 2^{j-4}\Sigma(4^jx)
=\Sigma(256x)+\frac12\Sigma(64x)+\frac14\Sigma(16x)
 +\frac18\Sigma(4x)+\frac1{16}\Sigma(x).
}
\tag{L-91634.1}
\]

The coefficients `2^(j-4)` belong to the declared score ledger. `R-91633` proves that they cannot also be installed as five independent literal-row scores inside one parent capacity. A one-use physical row is counted once, so its correct loss is

\[
\boxed{
\mathcal L^{\rm one}_4(x)=\mathcal A_4(x)-\mathcal P(256x).
}
\tag{L-91634.2}
\]

## 2. Directed-exact uniform moat

Put `n_j=floor(4^j x)` and define

\[
A(N)=\sum_{m\le N}\frac{\mu(m)}m,
\quad B(N)=\sum_{m\le N}\frac{\mu(m)}{\sqrt m},
\quad C(N)=\sum_{q\le N}\frac{\Lambda(q)}{\sqrt q},
\quad E(N)=\sum_{q\le N}\frac{\Lambda(q)\log q}{\sqrt q}.
\]

On every common open cell of `4^-4 Z`,

\[
\mathcal L^{\rm one}_4(x)=\alpha\sqrt x+\beta\log x+\gamma,
\tag{L-91634.3}
\]

with

\[
\alpha=5\sum_{j=0}^4 2^{2j-4}A(n_j),
\qquad
\boxed{\beta=-C(n_4)<0,}
\tag{L-91634.4}
\]

\[
\gamma=-3\sum_{j=0}^4 2^{j-4}B(n_j)
       -4\log4\,C(n_4)+E(n_4).
\tag{L-91634.5}
\]

The derivative has at most one zero. If it has an interior zero, then `alpha>0` and the second derivative there is positive, so the critical point is a minimum. The cell maximum is therefore at a one-sided endpoint. Activation knots are checked separately because the arithmetic prefixes may jump.

`X-91634` uses exact Möbius and prime-power prefixes, integer-isqrt square-root enclosures, an atanh logarithm expansion with explicit positive tail, and outward fixed-point interval arithmetic. It checks both one-sided endpoints of every cell and all activated knots:

```text
PASS_ONE_USE_PARENT_QUARTER_SCORE_K4_ENDPOINT_CERTIFICATE
checks:                                  50,689
common cells:                            16,896
cells with beta >= 0:                         0
largest certified upper bound: -40.905782490079282354
largest-upper-bound location:           x=1
```

Hence

\[
\boxed{
\mathcal L^{\rm one}_4(x)<-40.905782490079282354
\qquad(1\le x\le67).
}
\tag{L-91634.6}
\]

This is weaker than the scalar theorem `L-91632`, because four favorable literal-entropy terms have been removed, but it retains a large strict moat.

## 3. Exact entropy of one parent row

`R-91633` proves

\[
G_n=\sum_{q\ge2}\Lambda(q)\beta_{nq}.
\tag{L-91634.7}
\]

Therefore every finite row `d` with exact ordinary response `C_d=w_X` has

\[
\boxed{\mathcal S(d)=\sum_nd(n)G_n=\mathcal P(X).}
\tag{L-91634.8}
\]

For completeness, the retained equality-row decomposition is

\[
c_X(n)=\sum_{k\le X/n}\frac{\mu(k)}{\sqrt k}Q_{X/k}(n).
\tag{L-91634.9}
\]

Using the component response of `L-91559`, `C_Y(q)=q^(-1/2)H(Y/q)`, expanding `H`, and writing `r=km`,

\[
\begin{aligned}
C_{c_X}(q)
&=\frac1{\sqrt q}\sum_{r\le X/q}
 \frac{\log(X/(qr))}{\sqrt r}\sum_{k\mid r}\mu(k)\\
&=\frac1{\sqrt q}\log\frac Xq\,\mathbf1_{q\le X}=w_X(q),
\end{aligned}
\tag{L-91634.10}
\]

because `sum_(k|r)mu(k)` vanishes unless `r=1`. Its radix-four response is exactly `Omega_X`.

On the frozen entry of `L-91621`, leafwise Hallization and the controlled stopping-line cocycle produce nonnegative finite residual rows and nonnegative row bonuses whose coefficientwise sum is this exact parent equality row. `L-91559` inserts every canonical child by the identity map in the same physical row space. Thus, for `X=256x`, the resident one-use construction furnishes `d_X>=0` with

\[
\boxed{
C_{d_X}=w_X,
\qquad
\mathcal D_4C_{d_X}=\Omega_X,
\qquad
\mathcal S(d_X)=\mathcal P(X).
}
\tag{L-91634.11}
\]

The labels in `L-91621` are mutually singular, and every raw residual is consumed together with its unique raw child. Equation (L-91634.11) is therefore a one-use row identity, not merely equality of total target masses.

## 4. Four positive current rows and one terminal child

The component rows of `L-91559` are coefficientwise nondecreasing in their endpoint. Hence for every positive component atom `aQ_(256y)`,

\[
\boxed{
\begin{aligned}
aQ_{256y}={}&a(Q_{256y}-Q_{64y})+a(Q_{64y}-Q_{16y})\\
&+a(Q_{16y}-Q_{4y})+a(Q_{4y}-Q_y)+aQ_y,
\end{aligned}
}
\tag{L-91634.12}
\]

and every row on the right is nonnegative. Apply this identity to each positive labeled component source in `L-91621`, and place every target-null positive Hall bonus in the top current packet. Positive summation gives

\[
\boxed{
d_X=d_X^{(4)}+d_X^{(3)}+d_X^{(2)}+d_X^{(1)}+d_X^{\rm term},
\qquad d_X^{(j)},d_X^{\rm term}\ge0.
}
\tag{L-91634.13}
\]

Applying ordinary carry or radix-four detail response to (L-91634.13) gives the exact parent response (L-91634.11). No ordinary column, detail column, source atom, or row bonus is replayed. The physical telescoping coefficients are one; the coefficients `2^(j-4)` remain only in the declared score (L-91634.1). This distinction is forced by `R-91633`.

## 5. Corrected positive one-use realization

Combining (L-91634.6) and (L-91634.11),

\[
\boxed{
\mathcal A_4(x)-\mathcal S(d_{256x})
=\mathcal A_4(x)-\mathcal P(256x)
<-40.905782490079282354.
}
\tag{L-91634.14}
\]

Equivalently,

\[
\boxed{
\mathcal S(d_{256x})>
\mathcal A_4(x)+40.905782490079282354
\qquad(1\le x\le67).
}
\tag{L-91634.15}
\]

Thus the exact positive row consisting of four current factor-four packets and one terminal child realizes more than the complete five-level declared-score demand while consuming the single parent capacity exactly once. The impossible weighted sum of five literal entropies is neither constructed nor needed.

## 6. Boundary

```text
natural five-level declared-score coefficients          EXACT
weighted five-literal-row interpretation                 IMPOSSIBLE / R-91633
correct single-parent loss                               L-91634.2
uniform corrected negative moat                          DIRECTED EXACT
single exact parent entropy                              P(256x)
positive four-current-plus-terminal row partition        EXACT ON FROZEN ROW IDENTITY
ordinary and radix-four one-use accounting               EXACT ON FROZEN ROW IDENTITY
live arithmetic/Hall replay                              REQUIRED
independent reconstruction                               REQUIRED
Riemann Hypothesis                                       UNPROVEN
```
