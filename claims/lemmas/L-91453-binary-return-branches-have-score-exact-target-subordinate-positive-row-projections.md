# L-91453 — Both binary-return branches have score-exact, target-subordinate positive row projections

Claim ID: `L-91453`  
Status: **PROVED EXACT ONE-PRIME SOURCE/ROW THEOREM — ALL-GENERATION TYPE STABILITY OPEN**  
Created: 2026-08-12  
Depends on: `L-91320`, both one-prime Hall theorems `L-91331`, `L-91330/L-91340/L-91341`, `L-91452`  
RH status: **unproved**

## 1. Diagonal-channel notation

Write

\[
 X=L-R,
 \qquad
 Y=L-2R,
 \qquad
 U_a=aX-Y.
\tag{L-91453.1}
\]

For one rough prime put

\[
 r=p^{-1/2},
 \quad
 A=1-r^2,
 \quad
 B=1-r,
 \quad
 d=r(1-r).
\]

Retain the positive survival and hazard returns `C_p,H_p` of `L-91452`.

## 2. Survival target and score are ordinary channels

The survival target is

\[
\begin{aligned}
 T_s
 &=tC_p(L,R)^T
 =AL+2BR\\
 &=2(A+B)X-(A+2B)Y.
\end{aligned}
\]

Since

\[
 A+B=(1-r)(r+2),
 \qquad
 A+2B=(1-r)(r+3),
\]

one obtains

\[
\boxed{
 T_s=(1-r)(r+3)U_{\alpha_s},
 \qquad
 \alpha_s=\frac{2(r+2)}{r+3}.
}
\tag{L-91453.2}
\]

Moreover

\[
\boxed{
 \frac43<\alpha_s<\frac32
 \qquad(0<r<1).
}
\tag{L-91453.3}
\]

The survival score is

\[
\boxed{
 S_s=sC_p(L,R)^T
 =A(2L+R)=3A U_{5/3}.
}
\tag{L-91453.4}

Thus the target lies in the uniformly Hall-positive one-prime SHARP corridor,
while the score is exactly the score channel of `L-91340`.

## 3. Hazard target and score are ordinary channels

The hazard target is

\[
\begin{aligned}
 T_h
 &=r^2L+2rR\\
 &=2r(r+1)X-r(r+2)Y,
\end{aligned}
\]

so

\[
\boxed{
 T_h=r(r+2)U_{\alpha_h},
 \qquad
 \alpha_h=\frac{2(r+1)}{r+2}.
}
\tag{L-91453.5}
\]

The hazard score is

\[
\begin{aligned}
 S_h
 &=2r^2L+rR\\
 &=r(4r+1)X-r(2r+1)Y,
\end{aligned}
\]

hence

\[
\boxed{
 S_h=r(2r+1)U_{\beta_h},
 \qquad
 \beta_h=\frac{4r+1}{2r+1}.
}
\tag{L-91453.6}
\]

For `p>=67`, `0<r<1/8`, and therefore

\[
\boxed{
 1<\alpha_h<\beta_h<\frac65<\frac54<a_*.
}
\tag{L-91453.7}
\]

Here `a_*=-2/zeta(1/2)>5/4` follows from the directed eta bound
`zeta(1/2)>-8/5` used in `L-91320`.

## 4. Uniform no-upward score Hall transports

The survival score channel is `3A w_(5/3)`. `L-91340` proves its no-upward
score-Hall margin is positive on the complete factor-54 window.

For the hazard score channel, `1<beta_h<a_*`. Since `w_a` and every prefix Hall
margin are affine in `a`, write

\[
 w_{\beta_h}
 =(1-\lambda)w_1+\lambda w_{a_*},
 \qquad
 \lambda=\frac{\beta_h-1}{a_*-1}\in(0,1).
\]

The reserve margin of `L-91109` is `>39/100`. The balanced margin of
`L-91320`, after removing its positive factor `1+kappa_*<3`, gives a margin
`>1/15` for `w_(a_*)`. Hence

\[
\boxed{
 \mathcal H_{\beta_h,t}(x)>\frac1{15}
}
\tag{L-91453.8}
\]

for every active odd threshold and every reset-window ratio. Thus both branch
scores admit positive Hall transports supported on

\[
 e\le o.
\]

## 5. Target per score is monotone in both branches

For a source atom put

\[
 z=\sqrt{x/n}\ge1.
\]

The survival target/score ratio is

\[
\boxed{
 q_s(z)
 =\frac{(2r+4)z-(r+3)}{(r+1)(5z-3)}.
}
\tag{L-91453.9}
\]

Direct differentiation gives

\[
\boxed{
 q_s'(z)
 =\frac{3-r}{(r+1)(5z-3)^2}>0.
}
\tag{L-91453.10}
\]

The hazard ratio is

\[
\boxed{
 q_h(z)
 =\frac{(2r+2)z-(r+2)}{(4r+1)z-(2r+1)},
}
\tag{L-91453.11}
\]

with

\[
\boxed{
 q_h'(z)
 =\frac{3r}{[(4r+1)z-(2r+1)]^2}>0.
}
\tag{L-91453.12}
\]

Therefore, in either branch,

\[
 e\le o
 \Longrightarrow
 q(e)\ge q(o).
\tag{L-91453.13}
\]

Transporting odd demand in score-mass units to no-larger even sources gives a
positive residual coefficient measure which represents branch score exactly
and consumes no more branch target than is available, exactly as in
`L-91340`.

## 6. Exact finite-row positivity

Each branch score is a positive multiple of one ordinary channel `w_beta` with
`beta>=1`. `L-91330/L-91341` prove that for every such parameter

\[
 \frac{Q_Y(j)}{\beta\sqrt Y-1}
\]

is increasing on the complete reset window.

Hence every no-upward score-Hall edge lifts to a nonnegative exact component
row, and every unmatched even residual is nonnegative. The survival and hazard
branches therefore each possess one source object which is simultaneously:

```text
score-exact;
target-subordinate;
coefficientwise nonnegative in every exact finite row.
```

## 7. One-prime physical row recurrence

`L-91452` proves

\[
 T_s+T_h=T_{parent},
 \qquad
 S_s+S_h=S_{parent}+dR\ge S_{parent}.
\]

Apply Sections 4--6 separately to the disjoint survival and hazard source
labels. Their positive row packets consume at most

\[
 T_s+T_h=T_{parent}
\]

and carry total exact score

\[
 S_s+S_h\ge S_{parent}.
\]

Thus one rough-prime step has a positive, source-labelled, target-feasible and
score-favorable exact finite-row realization. The hazard row is sent through
the affine child lift to endpoint `x/p`; the survival row remains for the next
ordered prime. Sum-before-quantize assembly applies the finite collar once.

## 8. Remaining theorem

The one-prime physical-row arrow is closed for a canonical incoming
squarefree/Mobius channel. The remaining all-generation issue is **type
stability**: prove that after the Hall residual, affine child lift and common
endpoint-port correction, every child presented to the next reset is again a
positive combination of the ordinary channel types used above, with its unique
next-prime label and without changing the coefficient-one target telescope.

```text
survival target/score channel identities             EXACT
hazard target/score channel identities               EXACT
uniform no-upward score Hall in both branches         EXACT FROM DIRECTED INPUTS
target-per-score monotonicity                         EXACT
score-exact target-subordinate branch measures        EXACT
exact finite-row positivity in both branches          EXACT
one-prime physical row recurrence                     PROPOSED COMPLETE
all-generation channel-type stability                 OPEN / RH-BEARING
Riemann Hypothesis                                    UNPROVEN
```
