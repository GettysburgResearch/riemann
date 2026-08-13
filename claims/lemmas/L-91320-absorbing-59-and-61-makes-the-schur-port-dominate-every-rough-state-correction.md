# L-91320 — Absorbing 59 and 61 makes the endpoint Schur reserve dominate every remaining rough-state correction

Claim ID: `L-91320`  
Status: **PROVED EXACT FINITE-BLOCK / MATRIX-PORT THEOREM — PHYSICAL COLOR PROJECTION OPEN**  
Created: 2026-08-12  
Depends on: `L-91113`, `L-91316`–`L-91319`  
RH status: **unproved**

## 1. Enlarge the finite Boolean block

Let

\[
 \mathcal P_{61}
 =\{2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61\},
\]

\[
 P_{61}=\prod_{p\in\mathcal P_{61}}p.
\]

For `a in {1,2}`, define

\[
 \boxed{
 F_a^{(61)}(x)
 =\sum_{\substack{d\mid P_{61}\\d\le x}}
 \mu(d)
 \left(\frac{a\sqrt x}{d}-\frac1{\sqrt d}\right).
 }
\tag{L-91320.1}
\]

There are

\[
 2^{18}=262144
\]

activation states. The directed exact checker `X-91111` proves

\[
 \boxed{
 F_1^{(61)}(1)=0,
 \qquad
 F_1^{(61)}(x)>\sqrt2-1>0.4142
 \quad(x\ge2),
 }
\tag{L-91320.2}
\]

and

\[
 \boxed{
 F_2^{(61)}(x)>0.3186
 \qquad(x\ge1).
 }
\tag{L-91320.3}

The minima remain exactly the same as in the `P_53` certificate: `x=2` in the
reserve channel and `x=33` in the equality channel. Thus absorbing 59 and 61
creates no new finite sign obstruction.

## 2. The delayed renewal now begins at 67

Put

\[
 \mathcal M_{67}
 =\{m\ge1:p\mid m\Longrightarrow p\ge67\}.
\]

The coefficient-wise divisor calculation of `L-91113` gives

\[
 \boxed{
 \sum_{\substack{m\in\mathcal M_{67}\\m\le x}}
 m^{-1/2}U_a(x/m)
 =F_a^{(61)}(x),
 \qquad
 U_1=R,
 \quad U_2=L.
 }
\tag{L-91320.4}

Every nontrivial delay contracts scale by at least 67, still strictly beyond the
factor-54 reset window.

## 3. The enlarged endpoint Schur port remains bounded

Define `mathcal B_61` and `mathcal V_61` as in `L-91316`, with divisors of
`P_61`. The same termwise theorem gives

\[
 \boxed{
 |\mathcal B_{61}(x)|<\frac89\mathcal V_{61}(x),
 }
\tag{L-91320.5}
\]

and

\[
 \boxed{
 \begin{pmatrix}
  \mathcal V_{61}&\mathcal B_{61}\\
  \mathcal B_{61}&\mathcal V_{61}
 \end{pmatrix}
 \succeq\frac19\mathcal V_{61}I_2.
 }
\tag{L-91320.6}
\]

Its exact normalized endpoint mass is

\[
 \boxed{
 \prod_{p\le61}\left(1+\frac1p\right)
 =\frac{399441300081868800}{86204059532560853}
 <\frac{14}{3}.
 }
\tag{L-91320.7}

The finite enlargement therefore keeps the positive port uniformly bounded.

## 4. Every remaining projective correction is below the `1/9` reserve

For `p>=67`, put

\[
 r=p^{-1/2},
 \qquad
 \tau_p=r(1-r).
\]

The function `r(1-r)` increases on `0<r<1/2`, so its largest value occurs at
`p=67`. The exact integer-square comparison

\[
 81\cdot67<76^2
\]

is equivalent to

\[
 \frac1{\sqrt{67}}-\frac1{67}<\frac19.
\]

Hence

\[
 \boxed{
 \tau_p<\frac19
 \qquad(p\ge67).
 }
\tag{L-91320.8}

`L-91319` shows that the unique minimal SHARP-preserving correction of the signed
rough-state matrix transfers exactly `tau_p` units out of the positive
`R`-output channel. Equation (L-91320.6) supplies at least `1/9` of strict
diagonal endpoint reserve in the same normalized two-port coordinate.

Therefore the positive matrix completion of every remaining rough factor fits
strictly inside the available endpoint Schur port:

\[
 \boxed{
 \tau_p\mathcal V_{61}
 <\frac19\mathcal V_{61}
 \le\lambda_{\min}
 \begin{pmatrix}
  \mathcal V_{61}&\mathcal B_{61}\\
  \mathcal B_{61}&\mathcal V_{61}
 \end{pmatrix}.
 }
\tag{L-91320.9}

No accumulation of projective state debt occurs on a least-prime branch: the
correction is taken from that branch's own diagonal port before it enters the
next contracted generation.

## 5. Positive completed rough transition

For each `p>=67`, use the completed matrix

\[
 N_p=(1-p^{-1/2})
 \begin{pmatrix}
  1+2p^{-1/2}&0\\
  p^{-1/2}&1-2p^{-1/2}
 \end{pmatrix}.
\tag{L-91320.10}

Then:

1. `N_p` is entrywise nonnegative;
2. it preserves the exact SHARP output `(1,2)`;
3. it improves the endpoint score `(2,1)`;
4. its required projective transfer is strictly covered by the `P_61` Schur
   reserve;
5. `L-91317` routes its support into the already paid outer block or below the
   contracted endpoint;
6. `L-91318` gives an exact positive affine Pascal lift on every colored rough
   fiber and amplifies score.

Thus the complete rough transition is positive and coefficient one in the
**finite-state/colored-capacity extension**.

## 6. What remains

The finite Boolean sign, additive boundary port, projective state correction,
support contraction, colored carry lift, SHARP scalar, and entropy score are all
closed compatibly.

The sole remaining operation is the forgetful projection

\[
 \{\text{colored columns }(m,q)\}
 \longrightarrow
 \{\text{one physical column }Q\}.
\]

The affine Pascal lift has nonnegative leakage into physical columns not carrying
the selected rough color. The positive least-prime tree prevents source
duplication, but a final proof must show that forgetting colors does not spend
one physical radix-four capacity more than once.

```text
P_61 Boolean forcing                            DIRECTED EXACT
rough delay starts at 67                        EXACT
strict endpoint Schur reserve                   EXACT
all rough projective corrections < reserve      EXACT
positive SHARP-preserving state transition      EXACT
colored affine Pascal carry lift                EXACT
colored-to-physical capacity projection         OPEN
Riemann Hypothesis                              UNPROVED
```
