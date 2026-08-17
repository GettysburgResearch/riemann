# L-97401 — The repaired `1/42` bias is exactly sufficient for a genuine `<1/8` source-complete parity recursion

Claim ID: `L-97401`  
Status: **PROVED EXACT CONDITIONAL COMPOSITION AND ONE-PRIME COROLLARY**  
Created: 2026-08-18  
Depends on: `L-97400`  
RH status: **unproved because the source-complete recursion is not supplied**

## 1. One-prime canonical domination

Let `p>=67`, `y=x/p>=67`, and `r=p^{-1/2}`.  Monotonicity of the positive
unsigned source gives `M(y)<=M(x)`.  By `L-97400`,
\[
F(x)-rF(y)
\ge\frac1{42}M(x)-\frac r8M(y)
\ge\left(\frac1{42}-\frac1{8\sqrt{67}}\right)M(x)>0.
\tag{L-97401.1}
\]
Since `sqrt(67)>65/8`, the last coefficient is larger than
\[
\frac1{42}-\frac1{65}=rac{23}{2730}.
\]
Thus every genuine one-prime high-scale finite-Euler scalar difference is
strictly positive.

This is a scalar theorem.  It does not say that a parity-swapped difference is
a positive source packet, and it does not iterate through arbitrary rough
histories.

## 2. Critical contraction lemma

Suppose a **genuine source-complete** parent identity has current unsigned mass
`M-H`, current scalar at least
\[
\frac1{42}(M-H),
\]
recursive child unsigned mass `H`, and total signed recursive loss at most
\[
\frac16H.
\]
If
\[
H\le\rho M,
\qquad \rho<\frac18,
\]
then
\[
\begin{aligned}
f(\text{parent})
&\ge\frac1{42}(M-H)-\frac16H\\
&=\frac{1-8H/M}{42}M\\
&>0.
\end{aligned}
\tag{L-97401.2}
\]
For the factor-67 coefficient bound `rho<1/sqrt(67)`,
\[
f(\text{parent})
>\frac{1-8/\sqrt{67}}{42}M
>\frac1{2730}M.
\tag{L-97401.3}
\]

The value `1/42` is the exact critical lower constant paired with a child upper
constant `1/6` and threshold `rho=1/8`:
\[
\frac1{42}(1-\rho)-\frac16\rho
=\frac{1-8\rho}{42}.
\]
Consequently the false `1/40` constant is not needed for the numerical
contraction.  What remains indispensable is an actual one-use source identity
whose parent is the native rough Möbius source.  `R-97401` and `R-97402` show
that PRs #565 and #566 do not yet supply it.
