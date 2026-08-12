# L-91324 — Fractional-column Green identity promotes the factor-54 producer to continuous-column feasibility

Claim ID: `L-91324`  
Status: **PROPOSED COMPLETE EXACT FRACTIONAL-RESPONSE / CONTINUOUS-CAPACITY THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-12  
Depends on: `L-90028`, `L-91110`, `L-91111`, `L-91114`, `L-91115`, `L-91318`  
RH status: **unproved**

## 1. Continuous Pascal columns

For a finite seed `F` on the integers `n>=2`, put

\[
 A_F(n)=\frac{F(n)}{n-1},
 \qquad
 d_F(n)=(n+1)\Delta^2 A_F(n).
\tag{L-91324.1}
\]

For real `q>0`, define the continuous-column Pascal kernel

\[
 \boxed{
 \overline\beta_n(q)
 =\frac{a((a+1)q-(n+1))}{n+1},
 \qquad
 a=\left\lceil\frac{n+1}{q}\right\rceil-1.
 }
\tag{L-91324.2}
\]

At integer `q` this is the ordinary averaged Pascal carry coefficient. Define

\[
 \overline v_q(F)=\sum_{n\ge2}d_F(n)\overline\beta_n(q).
\tag{L-91324.3}
\]

## 2. Exact fractional Green identity

For `M>=1`, let

\[
 H_q(M)=M\overline\beta_{M-1}(q).
\]

If `a=ceil(M/q)-1`, then

\[
 H_q(M)=a((a+1)q-M)
       =\sum_{j\ge1}(2jq-M)\mathbf1_{jq<M}.
\tag{L-91324.4}
\]

Discrete summation by parts therefore gives

\[
 \overline v_q(F)
 =\sum_{m\ge2}A_F(m)
  [H_q(m+1)-2H_q(m)+H_q(m-1)].
\tag{L-91324.5}
\]

For `x=jq`, write

\[
 k_j=\lfloor jq\rfloor,
 \qquad
 \vartheta_j=\{jq\}.
\]

The contribution of the single breakpoint `jq` to (L-91324.5) is

\[
 (k_j+2\vartheta_j-1)A_F(k_j)
 -(k_j+2\vartheta_j)A_F(k_j+1).
\]

Since `F(k)=(k-1)A_F(k)`, this proves the exact identity

\[
 \boxed{
 \overline v_q(F)
 =\sum_{j\ge1}
 \left[
  F(k_j)-F(k_j+1)
  +2\vartheta_j
   (A_F(k_j)-A_F(k_j+1))
 \right].
 }
\tag{L-91324.6}
\]

The sum is finite. At an integer column every `vartheta_j=0`, so (L-91324.6)
reduces to ordinary carry switching.

The radix-four fractional detail is consequently

\[
 \boxed{
 \overline{\mathcal D}_4\overline v_q(F)
 =\overline v_q(F)-2\overline v_{4q}(F).
 }
\tag{L-91324.7}
\]

This identity is the exact analytic description of the former off-color
leakage: no unspecified interpolation error remains.

## 3. Uniform fractional-response bound

Assume `q>=K>=2`, `F` is eventually zero, and

\[
 |F(n)-F(n+1)|\le Cn^{-3/2}
 \qquad(n\ge K).
\tag{L-91324.8}
\]

Tail summation gives

\[
 |F(n)|\le3Cn^{-1/2}.
\tag{L-91324.9}
\]

Moreover

\[
\begin{aligned}
 |A_F(n)-A_F(n+1)|
 &\le\frac{|F(n)-F(n+1)|}{n-1}
   +\frac{|F(n+1)|}{n(n-1)}\\
 &\le8Cn^{-5/2}.
\end{aligned}
\tag{L-91324.10}
\]

Because `q>=2`,

\[
 k_j=\lfloor jq\rfloor\ge jq/2.
\]

Using

\[
 \sum_{j\ge1}j^{-3/2}<3,
 \qquad
 \sum_{j\ge1}j^{-5/2}<\frac53,
 \qquad
 2^{3/2}<3,
 \qquad
 2^{5/2}<6,
\]

in (L-91324.6) yields

\[
 \boxed{
 |\overline v_q(F)|<89Cq^{-3/2}.
 }
\tag{L-91324.11}
\]

Therefore

\[
 \boxed{
 |\overline{\mathcal D}_4\overline v_q(F)|
 <112Cq^{-3/2}.
 }
\tag{L-91324.12}
\]

The constants are deliberately conservative and elementary.

## 4. Application to the finite/continuum mismatch and B-spline collar

`L-91114` gives, for the finite/continuum seed mismatch `E_X`,

\[
 |E_X(n)-E_X(n+1)|<\frac{17}{2}n^{-3/2}.
\tag{L-91324.13}
\]

`L-91111` gives the positive quantization collar

\[
 0\le C_X(n)<8(n-1)^{-3/2}.
\]

Hence

\[
 |C_X(n)-C_X(n+1)|<32n^{-3/2}.
\tag{L-91324.14}
\]

For the complete signed discrepancy `C_X-E_X`, take

\[
 C=32+\frac{17}{2}=\frac{81}{2}.
\]

Equations (L-91324.11)--(L-91324.12) give

\[
 \boxed{
 |\overline v_q(C_X-E_X)|
 <\frac{7209}{2}q^{-3/2},
 }
\tag{L-91324.15}
\]

and

\[
 \boxed{
 |\overline{\mathcal D}_4\overline v_q(C_X-E_X)|
 <4536q^{-3/2}.
 }
\tag{L-91324.16}
\]

## 5. Continuous interior feasibility

For the real-column critical target,

\[
 \overline\Omega_X(q)
 =q^{-1/2}\log4
 \qquad(K\le q\le X/4).
\]

Since `log4>4/3`, (L-91324.16) gives

\[
 \boxed{
 \frac{
  |\overline{\mathcal D}_4\overline v_q(C_X-E_X)|
 }{\overline\Omega_X(q)}
 <\frac{3402}{q}
 \le\frac{3402}{K}.
 }
\tag{L-91324.17}
\]

Thus the stronger safety factor

\[
 \boxed{
 \sigma_K^{\rm cont}
 =\left(1+\frac{3403}{K}\right)^{-1}
 }
\tag{L-91324.18}
\]

makes every **real** interior column feasible while preserving nonnegative
endpoint weights.

The removed score is still

\[
 O(K^{-1}\sqrt X\log^2(2X))=O(1)
\]

on the factor-54 schedule `K asymp X`.

## 6. Continuous terminal closure

For `q>X/4`, the radix-four child is inactive, so ordinary response is the only
constraint. Equation (L-91324.15) gives

\[
 |\overline v_q(C_X-E_X)|
 <28836X^{-3/2}.
\tag{L-91324.19}
\]

Use the fixed top omission of `L-91115` with the enlarged but still constant
width

\[
 \boxed{W=100000.}
\tag{L-91324.20}
\]

The real-column endpoint derivative estimate in that theorem gives omitted
response

\[
 [W(2-\sqrt2)-800]X^{-3/2}.
\]

Using `sqrt2<17/12`,

\[
 W(2-\sqrt2)-800
 >\frac{172600}{3}>28836.
\tag{L-91324.21}
\]

Thus the same positive top omission dominates every fractional-column terminal
overfill. Its endpoint width is fixed, so its score cost remains `O(1)` per
reset generation.

Combining Sections 5 and 6 gives a nonnegative endpoint vector satisfying

\[
 \boxed{
 \sum_T\Lambda_T^{\rm cont}
 \overline\Xi_T(q)
 \le\overline\Omega_X(q)
 \qquad(K\le q<X)
 }
\tag{L-91324.22}
\]

for every real column `q`, for all sufficiently large `X`.

## 7. Affine rough lifts no longer create analytic color leakage

Let `d` be a continuously feasible child row at scale `Y`, and let
`mathcal A_m d` be the affine Pascal lift of `L-91318`:

\[
 n\longmapsto m(n+1)-1,
 \qquad
 D(m(n+1)-1)=m^{-1/2}d(n).
\]

For every physical integer column `Q`, exact affine covariance gives

\[
 \boxed{
 \operatorname{Resp}_{mY}(\mathcal A_md;Q)
 =m^{-1/2}
  \operatorname{Resp}_Y(d;Q/m).
 }
\tag{L-91324.23}
\]

The target has the same covariance:

\[
 \overline\Omega_{mY}(Q)
 =m^{-1/2}\overline\Omega_Y(Q/m).
\tag{L-91324.24}
\]

Hence a continuously feasible child is physically feasible after affine lift at
**every** integer column, whether or not `m` divides `Q`.

More generally, if nonnegative branch shares `theta_b` satisfy

\[
 \sum_b\theta_b\le1,
\]

then

\[
 \boxed{
 \sum_b\theta_b\mathcal A_{m_b}d_b
 }
\]

is feasible in the single uncolored physical column space. Thus the analytic
colored-to-uncolored leakage has been removed completely; the remaining problem
is only the source/state construction of a subprobability family of branch
shares.

## 8. Exact remaining gate

After this theorem the rough reset no longer needs a column-interpolation or
fractional-Pascal estimate. The sole projection question is:

> Construct source-faithful nonnegative branch shares in the completed
> `(L,R)`/Schur-port state space whose total is at most one and whose score
> transfer is coefficient one or otherwise subquadratic.

The positive state completion of `L-91319/L-91320` supplies the finite-dimensional
candidate. The present theorem proves that any such subprobability state
allocation projects to ordinary physical columns without further loss.

```text
fractional Pascal Green identity                   EXACT
uniform real-column mismatch/collar bound          EXACT
continuous interior feasibility                    PROPOSED COMPLETE
continuous terminal feasibility                    PROPOSED COMPLETE
physical affine covariance at unmatched columns    EXACT
subprobability branches -> uncolored feasibility   EXACT
source-faithful subprobability state allocation     OPEN / RH-BEARING
Riemann Hypothesis                                  UNPROVED
```
