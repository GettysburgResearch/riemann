# L-24516 — Prime-power cube budget and bounded consecutive runs

Claim ID: `L-24516`  
Status: `PROPOSED — complete elementary arithmetic`  
Scope: descending primitive correction bookkeeping  
Issue: #245

For an integer `n>=2`, let

\[
P_3(n)=\sum_{p^a\mid n}(p^a)^3,
\tag{L-24516.1}
\]

where every prime-power divisor `p,p^2,...,p^{v_p(n)}` is included.

## 1. Non-prime-power cube budget

If `n` is not a prime power, then

\[
\boxed{
P_3(n)\le\frac{35}{216}n^3.
}
\tag{L-24516.2}
\]

Equality holds only at `n=6`.

Write the distinct prime-primary components as

\[
n=x_1\cdots x_r,
\qquad x_i=p_i^{a_i},
\qquad r\ge2.
\]

For one component put

\[
S_3(p,a)=p^3+p^6+\cdots+p^{3a}.
\]

If the smallest component is at least `4`, the bounds

\[
\frac{S_3(2,a)}{2^{3a}}<\frac87,
\qquad
\frac{S_3(p,a)}{p^{3a}}\le\frac{27}{26}\quad(p\ge3)
\]

already give, for the two smallest components `x>=4`, `y>=3`,

\[
\frac{P_3(xy)}{(xy)^3}
\le\frac8{7y^3}+\frac{27}{26x^3}
<\frac{35}{216}.
\]

If the smallest component is `2`, the other component is an odd prime power
`y`, and

\[
\frac{P_3(2y)}{(2y)^3}
=\frac1{y^3}+\frac18\frac{S_3(y)}{y^3}.
\]

At `y=3` this is `(8+27)/216=35/216`. For every larger odd prime power the
value is strictly smaller. Additional coprime primary components can only lower
the ratio. This proves (L-24516.2).

## 2. Proper divisors of a prime power

If `n=p^a`, then its proper prime-power divisors obey

\[
\boxed{
\sum_{1\le k<a}(p^k)^3
<\frac1{p^3-1}n^3
\le\frac17n^3.
}
\tag{L-24516.3}
\]

Combining both cases, after excluding `n` itself whenever it is a prime power,

\[
\boxed{
\sum_{\substack{q=p^a\mid n\\q<n\text{ if }n\text{ is a prime power}}}q^3
\le\frac{35}{216}n^3.
}
\tag{L-24516.4}
\]

## 3. Consecutive prime-power runs

A run of four consecutive prime powers contains two even members. Every even
prime power is a power of `2`; the only powers of `2` differing by `2` are
`2` and `4`. Hence

\[
\boxed{
\text{the only length-four run is }2,3,4,5,
}
\tag{L-24516.5}
\]

and every run beginning at `7` or later has length at most three.

For a run of length `ell`, the local spike matrix is

\[
H_\ell=
\begin{pmatrix}
2&-1&&\\
-1&2&-1&\\
&\ddots&\ddots&\ddots\\
&&-1&2
\end{pmatrix},
\tag{L-24516.6}
\]

with explicit positive inverse

\[
(H_\ell^{-1})_{ij}
=\frac{\min(i,j)(\ell+1-\max(i,j))}{\ell+1}.
\tag{L-24516.7}
\]

Thus every nonnegative residual on one consecutive run has a unique
nonnegative local correction, with absolute inverse constants beyond the finite
initial run.

## 4. Application boundary

The cube budget is adapted to the exact spike identity

\[
\Delta v_q(F_j)
=F_j(\mathbf1_{q\mid j+1}-2\mathbf1_{q\mid j}+\mathbf1_{q\mid j-1}).
\]

After adjacent prime powers are grouped into one short run, (L-24516.4) gives an
absolute weighted budget for every remaining lower prime-power destination
dividing `j-1` or `j+1`.

This controls balanced descending leakage in a positive cube moment. It does not
control the objective cost after mass reaches very small prime powers; the
high-order mean-zero taper remains necessary for that unbalanced channel.

## Status boundary

The arithmetic inequalities and run classification are complete. Their
composition with tapered cancellation into a global signed transport proof
remains separate.
