# R-97700 - `LAPBR67` residual nonnegativity is false at the published adaptive depth

Claim ID: `R-97700`  
Status: **PROVED UNCONDITIONAL ASYMPTOTIC NO-GO**  
Created: 2026-08-18  
Frozen target: PR #578 at `981bfef5fcfa3a39ccf4f50875cf8a6057650268`  
Inputs: PR #578 `L-97501`; PR #576 `L-97400`; classical Mertens estimates  
RH status: **unproved**

Let `b(Y)` be the complete `P_61` annular `5:3` base scalar. For the root state
`p_0=67`, define the positive rough layer

\[
 B_r(X)=
 \sum_{\substack{m\ \mathrm{squarefree}\\P^-(m)\ge67\\\omega(m)=r}}
 \frac1{\sqrt m}\,b(X/m),
\]

with `b(u)=0` below support. The exact even-depth current is

\[
 C_L(X)=\sum_{r=0}^{L-1}(-1)^rB_r(X).
\]

Put

\[
 Z_X=(\log X)^{1/4},\qquad
 z_X=\sum_{67\le p\le Z_X}\frac1p,
\]

and let `L_X` be the smallest even integer satisfying

\[
 L_X\ge8(z_X+1).
\]

This is exactly the depth used in PR #578. Let `S_X` be its proven positive
small-prime cube and let `L_X^{\rm res}` be the complementary current containing
at least one prime greater than `Z_X`, so

\[
 C_{L_X}(X)=S_X+L_X^{\rm res}.
\]

Then, for all sufficiently large `X`,

\[
 \boxed{C_{L_X}(X)<0}
\]

and therefore

\[
 \boxed{L_X^{\rm res}<-S_X<0.}
\]

In fact `-L_X^{res}/S_X -> infinity`. Hence `LAPBR67` as stated in
`T-97500.2` is false; no improvement of its numerical constant can repair it.

## Proof by product-safe elementary symmetric sums

The directed theorem `L-97400` gives

\[
 b(Y)=a_*\sqrt Y+c_*+O(Y^{-3/2}),
 \qquad
 a_*=12\prod_{p\le61}\left(1-\frac1p\right)>0.
\]

Consequently there are constants `c_0,C_0,Y_0>0` such that

\[
 b(Y)\ge c_0\sqrt Y\quad(Y\ge Y_0),
 \qquad
 0\le b(Y)\le C_0\sqrt Y\quad(Y\ge1).
\tag{R-97700.1}
\]

Write

\[
 r=L_X-1,
 \qquad
 \Lambda_X=\sum_{67\le p\le X}\frac1p,
 \qquad
 Y=X^{1/(2r)},
 \qquad
 A_Y=\sum_{67\le p\le Y}\frac1p.
\]

Mertens' theorem gives

\[
 \Lambda_X=\log\log X+O(1),
 \qquad
 A_Y=\Lambda_X-\log(2r)+O(1).
\tag{R-97700.2}
\]

Since `r=O(log log log X)`, one has

\[
 \frac r{A_Y}\to0,
 \qquad
 \frac{r\log(2r)}{\Lambda_X}\to0.
\tag{R-97700.3}
\]

Every product of `r` primes at most `Y` is at most `sqrt X`; hence its child
endpoint is at least `sqrt X` and lies in the lower bound of (R-97700.1) for
large `X`. If `e_r(Y)` denotes the elementary symmetric sum of the weights
`{1/p:67<=p<=Y}`, then

\[
 B_r(X)\ge c_0\sqrt X\,e_r(Y).
\tag{R-97700.4}
\]

Let

\[
 S_2=\sum_{p\ge67}p^{-2}<\infty.
\]

The ordered distinct-prime sum is `r!e_r(Y)`. Expanding `A_Y^r` and applying a
union bound to tuples with a repeated coordinate gives the exact inequality

\[
 r!e_r(Y)
 \ge A_Y^r-\binom r2S_2A_Y^{r-2}
 =A_Y^r(1-o(1)).
\tag{R-97700.5}
\]

For every `j<r`, the upper bound in (R-97700.1) and Maclaurin's elementary
estimate give

\[
 B_j(X)
 \le C_0\sqrt X\frac{\Lambda_X^j}{j!}.
\tag{R-97700.6}
\]

Because `r/\Lambda_X -> 0`, the terms on the right increase throughout
`0<=j<r`, and therefore

\[
 \sum_{j<r}B_j(X)
 \le 2C_0\sqrt X\frac{\Lambda_X^{r-1}}{(r-1)!}
\tag{R-97700.7}
\]

for large `X`. Combining (R-97700.4)--(R-97700.7),

\[
 \frac{B_r(X)}{\sum_{j<r}B_j(X)}
 \ge \frac{c_0}{2C_0}\frac{A_Y}{r}
 \left(\frac{A_Y}{\Lambda_X}\right)^{r-1}(1-o(1))
 \longrightarrow\infty.
\tag{R-97700.8}
\]

Indeed the power in (R-97700.8) tends to one by (R-97700.2)--(R-97700.3),
while `A_Y/r -> infinity`. Since `r=L_X-1` is odd, the last layer enters
`C_{L_X}` with a minus sign and dominates the absolute sum of every preceding
layer. Thus `C_{L_X}(X)<0`.

Finally, the predecessor's small-prime cube obeys

\[
 0<S_X\le C_0\sqrt X
 \prod_{67\le p\le Z_X}(1+p^{-1})
 \le C_0\sqrt X e^{z_X}.
\]

The lower bound (R-97700.4)--(R-97700.5), together with
`A_Y~log log X` and `r=O(z_X)`, shows

\[
 B_r(X)/(\sqrt X e^{z_X})\to\infty.
\]

This proves `-L_X^{res}/S_X -> infinity`.

## Consequence

The adaptive small-prime theorem survives. What fails is the decision to stop
the full rough expansion at a depth chosen only from the reciprocal mass below
`Z_X`. The large-prime layers must be resummed rather than required to be
positive as a separate truncated current.
