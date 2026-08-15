# L-93900 — The SHARP target and score have an exact unique equality/reserve two-channel factorization

Claim ID: `L-93900`  
Status: **PROVED EXACT ALGEBRAIC TYPE FACTORIZATION**  
Created: 2026-08-16  
Repairs: `R-93900`; the target/score interface left implicit by PR #509  
RH status: **unproved**

## 1. Root atoms

For `1<=k<=x`, define

\[
E_x(k)=\frac1{\sqrt k}
 \left(2\sqrt{\frac xk}-1\right),
\qquad
R_x(k)=\frac1{\sqrt k}
 \left(\sqrt{\frac xk}-1\right).
\]

Both are nonnegative.  Direct addition gives

\[
\boxed{T_x(k)=E_x(k)+2R_x(k),}
\tag{L-93900.1}
\]

\[
\boxed{S_x(k)=2E_x(k)+R_x(k).}
\tag{L-93900.2}
\]

The inverse formulas are

\[
\boxed{E_x(k)=\frac{2S_x(k)-T_x(k)}3,}
\qquad
\boxed{R_x(k)=\frac{2T_x(k)-S_x(k)}3.}
\tag{L-93900.3}
\]

The determinant of the target/score matrix

\[
\begin{pmatrix}1&2\\2&1\end{pmatrix}
\]

is `-3`; hence the positive two-channel factorization is unique.

## 2. Typed features

The equality channel has typed unit feature

```text
target  1
score   2
row     the positive equality/Volterra component row
q,4q    the ordinary observations of that row
```

and the reserve channel has

```text
target  2
score   1
row     0
q,4q    0.
```

Thus the row-first scalar of PR #509 is the equality channel only.  The missing
reserve channel is invisible to every component-row observation but is
load-bearing in target and score.

## 3. Causal leaf atoms

For `p>=67`, `1<=y<67`, `d|P_61`, and causal zero extension below quotient one,
put

\[
E_{p,y}(d)=\frac1{\sqrt d}
 \left[E(py/d)-p^{-1/2}E(y/d)\right],
\]

\[
R_{p,y}(d)=\frac1{\sqrt d}
 \left[R(py/d)-p^{-1/2}R(y/d)\right].
\]

These are nonnegative on the active causal source.  The literal causal target
and score atoms satisfy

\[
\boxed{K_T(d)=E_{p,y}(d)+2R_{p,y}(d),}
\tag{L-93900.4}
\]

\[
\boxed{K_S(d)=2E_{p,y}(d)+R_{p,y}(d).}
\tag{L-93900.5}
\]

Attach the complete positive causal component row `K_R(d)` and all its
ordinary/detail observations to the equality channel.  The reserve channel is
row-zero.  Their sum is the original complete target/score/row atom.

## 4. One coefficient per arithmetic occurrence

Whenever a source occurrence is used with coefficient `u_d`, the **same**
coefficient is applied to both channels.  The channel split is an exact
coordinate decomposition of one occurrence, not two independently spendable
copies.

Consequently the Target-Lorenz coefficient vector continues to act
simultaneously in target, score, every component row, ordinary `q`, ordinary
`4q`, and every additive boundary coordinate.

```text
channel positivity                         exact
target/score reconstruction                exact
uniqueness                                 exact
row assigned only to equality channel      exact
same source coefficient on both channels   mandatory
rough-lift substitution                    not used
Riemann Hypothesis                         unproved
```
