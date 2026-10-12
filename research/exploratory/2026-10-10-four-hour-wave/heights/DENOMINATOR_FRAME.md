# A stronger uniform compact Pick theorem by denominator preconditioning

Status: proposed lemma, subject to independent review.

Scope: an arbitrary *declared finite* packet order on an entire compact
positive-node interval. An explicit inequality must be verified at each
order and range. No all-order or unbounded-axis conclusion is asserted.

Use the complete source, multiplicities, strip/height assumptions, and
signed-shadow estimate (5) in [PROOF.md](PROOF.md). The present lemma replaces
the crude determinant/trace lower bound by a computable inverse bound.

## The theorem

Fix `M>=1`, `n=2M`, and M distinct critical pairs, each available with
multiplicity at least one. Let their squared ordinates have disjoint
enclosures

\[
0<l_j\le r_j\le h_j<l_{j+1}.
\]

Choose `S>0`, `X>0`, put `U=X/S`, `L_j=l_j/S^2`, `R_j=r_j/S^2`,
`V_j=h_j/S^2`, and define the following nonnegative rational quantities when
the input bounds, S, X, A, H are rational:

\[
\begin{split}
\sigma_j&=\prod_{k<j}(L_j-V_k)\prod_{k>j}(L_k-V_j),\\
\tau&=\sum_{j=1}^M(1+1/L_j)
             \frac{\sum_{k=0}^{M-1}V_j^{2k}}{\sigma_j^2},\\
J&=\sum_{i=0}^{n-1}\sum_{k=0}^i
                 {i\choose k}^2U^{2(i-k)},\\
D_+(u)&=\prod_{j=1}^M(u^2+V_j),\qquad
d_i=\frac{D_+^{(i)}(U)}{i!},\\
\beta&=2S/H,\qquad
b_i=\sum_{p=0}^i d_{i-p}\beta^p,\qquad
B=\sum_{i=0}^{n-1}b_i^2.
\end{split}                                                        \tag{D1}
\]

The empty product for M=1 is one. Every `sigma_j>0` by disjointness. Let
`S_4` be any proved upper bound on the complete off-line sum `sum m/b^4`.

**Theorem D.** If

\[
\boxed{12 A^2 S_4 B < \frac{2}{S^2\tau J},}            \tag{D2}
\]

then every safe-axis Pick packet of size at most n with nodes
`0<x_i<=X` is PSD. It is positive definite when all its nodes are distinct.
There is no restriction such as `H>=2S` for this version; beta is retained
explicitly. The usual `H>A` and source hypotheses remain necessary.

## Proof of the positive anchor bound

For n distinct nodes write `u_i=x_i/S`, and let T be the Newton
divided-difference matrix on these u nodes. Put

\[
D(u)=\prod_j(u^2+R_j),\qquad
P_j(u)=\prod_{k\ne j}(u^2+R_k).
\]

Apply the invertible congruence `T diag(D(u_i))`. The selected critical
features become the divided differences of

\[
\frac{\sqrt{2R_j}}S P_j(u),\qquad
\frac{\sqrt2}S uP_j(u).
\]

Let C be the n by n real coefficient matrix of the polynomial columns
`P_j` and `uP_j`, in monomials `1,u,...,u^(n-1)`. Let W be the monomial-to-
Newton-coefficient matrix, `W_ik=[u_0,...,u_i]u^k`. The transformed anchor
Gram matrix is exactly

\[
\widehat G=\frac2{S^2}W C\operatorname{diag}(R_1,1,\ldots,R_M,1)C^T W^T.
                                                                  \tag{D3}
\]

Column order is immaterial if the diagonal metric follows it. Both C and W
are invertible. In the even block, with variable v=u^2, the polynomial
columns are `prod_{k!=j}(v+R_k)`. Evaluating at `v=-R_j` shows that row j
of its inverse is

\[
\frac{(1,-R_j,\ldots,(-R_j)^{M-1})}{\delta_j},\qquad
\delta_j=\prod_{k\ne j}(R_k-R_j).
\]

The odd block has the same inverse. Consequently, for
`B_0=C diag(R_1,1,...,R_M,1) C^T`,

\[
\operatorname{tr}(B_0^{-1})
=\sum_j(1+1/R_j)\frac{\sum_{k=0}^{M-1}R_j^{2k}}{\delta_j^2}
\le\tau.                                                        \tag{D4}
\]

The columns of `W^{-1}` are the monomial coefficients of the Newton
polynomials `prod_{q<i}(u-u_q)`. Since `0<=u_q<=U`, the elementary symmetric
coefficient bound gives

\[
\|W^{-1}\|_{\rm op}^2\le\|W^{-1}\|_F^2
\le\sum_{i=0}^{n-1}\sum_{k=0}^i{i\choose k}^2U^{2(i-k)}=J.
                                                                  \tag{D5}
\]

Equations (D3)--(D5) imply

\[
\lambda_{\min}(\widehat G)\ge\frac2{S^2\tau J}.        \tag{D6}
\]

This bound avoids multiplying all n eigenvalues and is stable under
arbitrary node collisions. It is an algebraic lower bound, not a sampled
matrix minimum.

## Proof of the complete signed error bound

For one off-line quartet let `E(u,v)=D_{a,b,m}(Su,Sv)`. Estimate (5) gives

\[
\frac{|\partial_u^p\partial_v^q E|}{p!q!}
\le\frac{2ma^2(p+q+3)(p+q+2)(S/b)^{p+q}}{b^4}
\le\frac{12ma^2}{b^4}(2S/H)^{p+q}.                    \tag{D7}
\]

The last inequality uses `(k+3)(k+2)<=6*2^k` for every integer k>=0.
Each coefficient of the even polynomial D(u) is nonnegative and bounded
by the corresponding coefficient of D_+(u). On `[0,U]`, therefore,
`|D^(i)(u)|/i!<=d_i`. The normalized Leibniz rule applied to
`D(u)D(v)E(u,v)` and (D7) yields

\[
\frac{|\partial_u^i\partial_v^j[D(u)D(v)E(u,v)]|}{i!j!}
\le\frac{12ma^2}{b^4}b_i b_j.                       \tag{D8}
\]

Mixed divided differences obey the same bound by their integral
representation. Summing the full source gives entry bounds
`|widehat E_ij|<=12A^2S_4 b_i b_j`. Thus for every real vector z,

\[
|z^T\widehat E z|
\le12A^2S_4\bigl(\sum_i b_i|z_i|\bigr)^2
\le12A^2S_4 B\|z\|^2.                               \tag{D9}
\]

For complex vectors the same bound follows using absolute values, since
the matrix is real symmetric. The estimates imply locally uniform
convergence of the error and every derivative used, so no finite tail is
substituted for the complete off-line sum.

The remaining actual critical pairs and all critical shadows are PSD after
the same congruence. Combining (D6), (D9), and (D2) proves PD on n distinct
nodes. Smaller packets are principal restrictions after appending distinct
nodes in `(0,X]`. Repeated-node packets are pullbacks by coefficient summing,
and hence PSD. This finishes the proof.

## Source and application boundary

Only the strip width A enters from quasi-RH: its improvement from 1/2 to
3/8 reduces the signed error bound by 9/16. Many successful finite-order
inequalities already hold with the classical A=1/2. The new literature is
useful without being necessary for every displayed finite-order result.

For xi, use the published Platt--Trudgian height
3,000,175,332,800 only through the weaker H=3*10^12, a source-bound classical
upper count `N_+(T)<=T log T`, and independently directed Hardy-Z sign
certificates that establish the selected low critical pairs. Inequality
(D2) is then checked using exact rational arithmetic. The theorem is
conditional on those imported analytic/height inputs; directed low-zero
signs and rational matrix bounds do not reverify the high-zero computation.

It remains open to make the finite-order inequality hold cofinally in n
and X for the single actual source. Finite tables, even ones with exact
arithmetic and large margins, do not supply that quantifier.
