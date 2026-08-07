# L-25301 — The parabolic seed contains a macroscopic constraint dipole

Claim ID: `L-25301`  
Title: Positive and negative von-Mangoldt weighted constraint defects are both of square-root size, so a sharp carry repair must transport rather than delete defect  
Status: **PROPOSED COMPLETE CONSEQUENCE OF `R-25301` AND THE PNT**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-07  
Issue: #253  
Dependencies: `R-25301`; PR #248 `L-24501`, `L-24502`  
Scope: structural theorem and corrected proof target; no RH conclusion

## 1. Signed defect identity

For the parabolic seed define

\[
d_X(q)=v_q(b_X^{(0)})-w_X(q)
\qquad(q=p^a\le X)
\tag{L-25301.1}
\]

and its von-Mangoldt weighted positive and negative masses

\[
D_X^+
=
\sum_{q=p^a\le X}\Lambda(q)(d_X(q))_+,
\qquad
D_X^-
=
\sum_{q=p^a\le X}\Lambda(q)(-d_X(q))_+.
\tag{L-25301.2}
\]

The exact dual identity of `L-24501` gives

\[
\begin{aligned}
D_X^+-D_X^-
&=
\sum_{q=p^a\le X}\Lambda(q)d_X(q)\\
&=
J_X(b_X^{(0)})
-
\sum_{q=p^a\le X}
 \frac{\Lambda(q)}{\sqrt q}\log\frac Xq.
\end{aligned}
\tag{L-25301.3}
\]

No inequality or loss enters this identity.

## 2. The signed total is sub-square-root

Elementary integral comparison applied to the explicit seed gives

\[
J_X(b_X^{(0)})
=
4\sqrt X+O(\log X).
\tag{L-25301.4}
\]

Partial summation and the prime number theorem give

\[
\sum_{q=p^a\le X}
 \frac{\Lambda(q)}{\sqrt q}\log\frac Xq
=
4\sqrt X+o(\sqrt X).
\tag{L-25301.5}
\]

Therefore

\[
\boxed{
D_X^+-D_X^-=o(\sqrt X).
}
\tag{L-25301.6}
\]

## 3. Both signs are macroscopic

`R-25301` proves

\[
D_X^+\ge\frac{\sqrt X}{4000}
\tag{L-25301.7}
\]

for all sufficiently large `X`. Combining (L-25301.6)--(L-25301.7) yields,
after enlarging the threshold,

\[
\boxed{
D_X^-\ge\frac{\sqrt X}{8000}.
}
\tag{L-25301.8}
\]

Thus the parabolic seed is not “almost feasible” in an unsigned sense. It has
two macroscopic dual ledgers which cancel almost completely:

\[
\boxed{
\text{positive defect }\asymp_{\rm lower}\sqrt X,
\qquad
\text{negative slack }\asymp_{\rm lower}\sqrt X,
\qquad
\text{signed difference }=o(\sqrt X).
}
\tag{L-25301.9}
\]

This explains why a positive-part cover loses the sharp constant even though
the seed objective and the exact prime ramp are close.

## 4. Exact adjacent-flow coordinate

Retain the adjacent-flow correction from `L-24502`:

\[
b_F(m)=b_X^{(0)}(m)+F_{m-1}-F_m,
\qquad F_1=F_X=0.
\tag{L-25301.10}
\]

Its constraint change is

\[
\boxed{
v_q(b_F)-v_q(b_X^{(0)})
=
\sum_{j=2}^{X-1}F_j
\left(
 \mathbf1_{q\mid j+1}
 -2\mathbf1_{q\mid j}
 +\mathbf1_{q\mid j-1}
\right),
}
\tag{L-25301.11}
\]

while its exact objective cost is

\[
\boxed{
J_X(b_X^{(0)})-J_X(b_F)
=
\sum_{j=2}^{X-1}
F_j\log\frac{j^2}{j^2-1}.
}
\tag{L-25301.12}
\]

The cost weight is `j^-2+O(j^-4)`. Hence signed transport at large indices can
be far cheaper than deleting the same amount of dual defect by a monotone tail
cover.

## 5. Divisor descent of one diagonal repair

If `j=q` is a prime power, the diagonal term in (L-25301.11) is `-2F_q`.
Every positive cross term lands at a prime power dividing `q-1` or `q+1`.

Except when `q-1` or `q+1` is itself a prime power, every such child is at most

\[
\frac{q+1}{2}.
\tag{L-25301.13}
\]

The same-scale exceptions form uniformly bounded consecutive-prime-power
clusters. Indeed, any four consecutive integers beginning above `2` contain
an even integer congruent to `2 mod 4` and greater than `2`; that integer has
both an odd factor and a factor `2`, so it is not a prime power. Hence every
cluster has length at most three, except the single cluster

\[
\{2,3,4,5\}.
\]

For a cluster of length at most three above `5`, the same-scale repair matrix is
the path M-matrix

\[
A_r=2I-\operatorname{Adj}(P_r),
\qquad r\le3,
\]

whose inverse is entrywise nonnegative. The exceptional cluster has the
complete matrix

\[
A_{\rm exc}=
\begin{pmatrix}
2&-2&2&-2\\
-1&2&-1&-1\\
0&-1&2&-1\\
0&0&-1&2
\end{pmatrix},
\]

with

\[
A_{\rm exc}^{-1}=
\begin{pmatrix}
3/2&2&1&3\\
3/2&3&2&4\\
1&2&2&3\\
1/2&1&1&2
\end{pmatrix}\ge0.
\]

Thus every nonnegative same-scale defect vector can be removed by a
nonnegative joint cluster flow. After that solve, every remaining positive
child is a proper prime-power divisor of `q-1` or `q+1` and is at most
`(q+1)/2`.

This gives a genuine scale mechanism:

```text
jointly repair one consecutive-prime-power cluster
-> same-scale defect removed
-> all remaining positive children have endpoint at most half scale.
```

It does not by itself prove the required cost or preserve `b_F>=0`.

## 6. Corrected load-bearing theorem

A proof of the parabolic carry route should now target the following
**Constraint-Dipole Transport** statement.

For every `epsilon>0` and all sufficiently large `X`, construct a real flow
`F_X` such that

\[
b_{F_X}(m)\ge0
\qquad(2\le m\le X),
\tag{L-25301.14}
\]

\[
v_q(b_{F_X})\le w_X(q)
\qquad(q=p^a\le X),
\tag{L-25301.15}
\]

and

\[
\sum_{j=2}^{X-1}
F_X(j)\log\frac{j^2}{j^2-1}
\le X^\epsilon.
\tag{L-25301.16}
\]

Negative and positive flow values are permitted, subject to (L-25301.14).
Equivalently, one may use the tapered primitive-neighbor flow of `L-24503`,
provided the complete signed defect and slack ledgers are retained.

The theorem must exploit both sides of (L-25301.9). Any proof that replaces
`d_X` by `(d_X)_+` before transport is ruled out by `R-25301`.

## 7. Proof boundary

Established:

- exact signed-defect identity;
- macroscopic positive and negative dual masses;
- exact adjacent-flow objective and constraint maps;
- a factor-two divisor-descent mechanism outside uniformly bounded consecutive
  prime-power clusters.

Open:

- a flow satisfying (L-25301.14)--(L-25301.16);
- sharp carry feasibility with subpolynomial loss;
- RH.
