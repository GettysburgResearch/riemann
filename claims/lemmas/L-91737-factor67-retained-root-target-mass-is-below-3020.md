# L-91737 — The retained factor-67 positive root packet has uniformly bounded exact target mass

Claim ID: `L-91737`
Status: **PROVED EXACT FIXED-WINDOW TARGET-MASS BOUND ON THE FROZEN ENDPOINT-MEASURE INTERPRETATION**
Created: 2026-08-15
Depends on: `L-91690`, the factor-67 endpoint measure of `L-91724`, positive integration in `L-91674`
Purpose: supplies the uniform native-mass premise of `T-91305` for the retained positive recursive certificate
RH status: **unproved**

## 1. Normalized endpoint measure

On the retained factor-67 root window, write

\[
 d\nu(x)=\frac{2L(x)}x\,dx,
 \qquad 1\le x<67.
\tag{L-91737.1}
\]

The directed cell theorem retained in `L-91692` gives

\[
 0<L(x)<\frac{183}{100}.
\tag{L-91737.2}
\]

Since `log(67)<5`,

\[
 \boxed{
 \nu([1,67))
 <\frac{183}{50}\log67
 <\frac{183}{10}.
 }
\tag{L-91737.3}
\]

The elementary inequality `log(67)<5` is exact: the positive exponential
series through degree five already gives `e^5>67`.

## 2. Uniform target bound on one Hall fiber

For a squarefree source node `k<=x`, the positive target atom is

\[
 T_x(k)=\frac{4\sqrt x}{k}-\frac3{\sqrt k}.
\]

The positive Hall residual has target exactly the signed target and is bounded
above by the complete positive target supply.  Hence

\[
\begin{aligned}
 m(P_x)
 &\le\sum_{\substack{k\le x\\\mu(k)=1}}T_x(k)\\
 &<4\sqrt{67}\sum_{k\le66}\frac1k.
\end{aligned}
\tag{L-91737.4}
\]

The exact elementary estimates

\[
 \sqrt{67}<\frac{33}{4},
 \qquad
 H_{66}<5
\]

give

\[
 \boxed{m(P_x)<165.}
\tag{L-91737.5}
\]

Hall row bonuses are target-null and do not change this mass.

## 3. Integrated root mass

Let `P_X` be the positive residual root packet obtained by integrating the
Hall fibers over the retained endpoint measure.  Positive integration and
(L-91737.3)--(L-91737.5) give

\[
\begin{aligned}
 M_X:=m(P_X)
 &=\int m(P_x)d\nu(x)\\
 &<165\cdot\frac{183}{10}
 =\frac{6039}{2}
 <3020.
\end{aligned}
\]

Therefore

\[
 \boxed{m(P_X)<3020.}
\tag{L-91737.6}
\]

Any common bottom/top/knot restriction or scalar safety thinning only decreases
this value.  A positive same-cell barycentric pushforward preserves the same
bound by convexity.

## 4. Child-envelope consequence

The actual-mass normalization of `L-91732` produces children
`\widetilde P_b` with

\[
 m(\widetilde P_b)=m(P_X)=M_X,
 \qquad
 \sum_b\beta_b<\frac18.
\]

If `C_+` is the mass-one positive causal deficit bound, then

\[
 \sum_b\beta_b\Delta(\widetilde P_b)
 \le C_+M_X\sum_b\beta_b
 <\frac{3020}{8}C_+.
\tag{L-91737.7}
\]

Thus the complete child contribution is uniformly bounded.  This is the exact
uniform-mass premise required by the measure-valued consumer `T-91305`; the
historical certificate-count bound `54` is not substituted for physical target
mass.

## 5. Scope

The theorem uses the frozen interpretation that (L-91737.1) is the actual
positive endpoint measure and that the target coordinate integrated by
`L-91674` is the target atom of `L-91690`.  Independent review must reconstruct
that source/measure interpretation.  No claim about RH is made.

```text
factor-67 endpoint measure finite and atomless        exact on frozen input
one Hall-fiber target mass                            <165
retained integrated exact target mass                 <3020
common restriction/thinning                           preserves bound
positive causal child contribution                    O(1)
certificate count 54 as target-mass substitute        not used
Riemann Hypothesis                                    unproved
```
