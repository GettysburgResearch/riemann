# Finite theta jets with prescribed nonreal zeros and the unchanged envelope

**Status:** Proposed analytic component theorem; full proof below. Independent mathematical review is required. The theta corollary consumes the finite source theorem in PR #1003; its primitive theta integration and original certificate have not been independently replayed here.

**Scope:** Fixed finite Taylor order. The constructed functions are auxiliary entire functions, not the Riemann xi function. No off-critical zeta zero, new zeta zero-free region, or RH conclusion is asserted. No worldwide novelty claim is made.

## 1. Source and normalization

Frozen source: GettysburgResearch/riemann, PR #1003, commit
`669b6a01f4d4858ae1ef806b07547be95c08c935`.

Load-bearing files under `standalone/2026-10-18-theta26-and-critical-family/theta/`:

* `PROOF_GAUSSIAN.md`: the finite real-node theorem and contraction.
* `gaussian_parameters.json`: exact rational centers, active coordinates and preconditioner. Blob SHA-1 `432904733cb860eddec4ad82f9c1add9de13e37f`.
* `WEIGHTED_CANONICAL.md`: the correct cofinal positive-weight consumer.
* `extension/POWER_SUM_EXTENSION.md`: moving anchors, conjugate pairs, and the conditional normality barrier.

In physical coordinates put

\[
F_\theta(w)=\frac{\xi(1/2+iw)}{\xi(1/2)},\qquad
v=\mathbb E_\theta T^2,\qquad H(z)=F_\theta(z/\sqrt v).
\]

Thus `z=sqrt(v)*w`, not the reverse. The source has `1/25<v<1/20` and

\[
\log H(z)=-z^2/2-\sum_{r\ge2}Q_rz^{2r}/r.
\]

The source's order-26 result supplies a function

\[
P(z)=e^{-az^2}\prod_{j=1}^{128}(1-b_jz^2),\quad
a>0,\quad b_j>0,\quad a+\sum_jb_j=1/2,
\]

with `sum_j b_j^r=Q_r` for `2<=r<=13`. Its twelve selected active nodes are distinct. Its whole-plane bound is `|P(z)|<=exp(|z|^2/2)`.

The argument below applies to any such finite nonsingular model, not just this source.

## 2. The insertion theorem

**Theorem A.** Suppose a finite positive-node model as above matches powers `2,...,M`, with `M-1` distinct active nodes and strictly positive Gaussian reserve. Fix `v>0` and `B>0`. For every sufficiently large real `T`, there is an even real entire function `G_T` such that:

1. `G_T-H=O(z^(2M+2))` at zero.
2. `|G_T(z)|<=exp(|z|^2/2)` on the entire complex plane, with precisely the same bound as the original model.
3. In physical coordinates `g_T(w)=G_T(sqrt(v)*w)`, its only nonreal zeros are the four prescribed points `+/-T +/- iB`. All its other zeros are real.
4. If `mathcal T_T` denotes the sum of the squared absolute values of its canonical nodes, then

\[
\mathcal T_T
 =Q_2+\frac{16T^2B^2}{v^2(T^2+B^2)^4}
 =Q_2+O_{v,B}(T^{-6}).
\]

The quantifier is fixed `M`, followed by sufficiently large `T`. It does not furnish a cofinal sequence of moment matches for one target.

### Proof

Let

\[
c=\frac1{v(T+iB)^2}=u+iy,
\quad
u=\frac{T^2-B^2}{v(T^2+B^2)^2},\quad
y=-\frac{2TB}{v(T^2+B^2)^2}.
\]

Retune only the active real nodes so that

\[
\sum_j\widetilde b_j^r=Q_r-2\Re(c^r),\qquad 2\le r\le M.\tag{A1}
\]

The derivative of the old moment map is

\[
J_{rj}=r b_j^{r-1}.
\]

It is a nonsingular diagonal multiple of a Vandermonde matrix on the distinct positive active nodes. Since `c->0` as `T->infinity`, the real implicit-function theorem solves (A1), with `tilde b_j->b_j`. In particular, every old node remains positive and

\[
\widetilde a=1/2-\sum_j\widetilde b_j-2u>0
\]

for all sufficiently large `T`. Define

\[
G_T(z)=e^{-\widetilde a z^2}
 \prod_j(1-\widetilde b_jz^2)(1-cz^2)(1-\bar c z^2).\tag{A2}
\]

Its logarithm and (A1) prove exact agreement through degree `2M`. The pair factors give precisely the four physical zeros in the statement; positivity of the old nodes locates the remaining zeros on the real axis.

The important point is that the old envelope need not deteriorate. For sufficiently large `T`, `u>0` and `y^2<=u^2`; the latter condition is equivalent to

\[
2TB\le T^2-B^2.
\]

For `t=|z|^2` the pair polynomial satisfies

\[
\begin{aligned}
|(1-cz^2)(1-\bar c z^2)|
&=|1-2uz^2+(u^2+y^2)z^4|\\
&\le1+2ut+(u^2+y^2)t^2\\
&\le1+2ut+2u^2t^2\le e^{2ut}.
\end{aligned}\tag{A3}
\]

Together with `|1-tilde b_j z^2|<=exp(tilde b_j|z|^2)` and the definition of `tilde a`, this proves the unchanged envelope.

Finally, the matched second power gives

\[
\begin{aligned}
\mathcal T_T-Q_2
&=2|c|^2-2\Re(c^2)\\
&=4y^2
 =\frac{16T^2B^2}{v^2(T^2+B^2)^4}.
\end{aligned}
\]

This proves all assertions. QED.

## 3. A quantitative contraction adapter

Suppose the source moment equation `f(x)=0` has a cube of radius `rho` about `x_0`, with a fixed preconditioner `R`, and

\[
\|Rf(x_0)\|_\infty\le\beta,\qquad
\sup_{x\in C}\|I-RDf(x)\|_\infty\le L<1.
\]

For `|c|<=1`, the added moment vector has infinity norm at most `2|c|^2`. The **same cube and same preconditioner** therefore solve the perturbed equations whenever

\[
\boxed{\beta+L\rho+2\|R\|_\infty |c|^2<\rho.}\tag{A4}
\]

The derivative has not changed. An additional explicit guard is required for the new Gaussian reserve:

\[
\inf_{x\in C}\left(1/2-\sum_j b_j(x)\right)>2u.\tag{A5}
\]

Do not silently replace (A5) by a rounded point value of the reserve.

Here is a bound for `R` that does not require copying its large rational matrix. If there are `m=M-1` active nodes, each in `[b_min,b_max]`, with pairwise separation at least `Delta`, Lagrange interpolation gives

\[
\|J^{-1}\|_\infty
\le\frac{(1+b_{\max})^{m-1}}{2b_{\min}\Delta^{m-1}}.\tag{A6}
\]

Indeed, `J=diag(2,...,M) V diag(b_j)`. The absolute coefficient sum of each Lagrange cardinal polynomial is at most `(1+b_max)^(m-1)/Delta^(m-1)`. If `||I-RJ||<1`, then `||R||<2||J^{-1}||`.

For the twelve active order-26 nodes, the transcribed outward intervals in `source_excerpt.json` verify

\[
b_{\min}>1/1000,\quad b_{\max}<1/8,\quad\Delta>1/2000,
\quad \|R\|_\infty<10^{40}.
\]

Using the **reported, not independently replayed**, coarsenings `beta<10^-80`, `L<10^-30`, `rho=10^-50` and `v>1/25`, the moment-equation perturbation at `T=10^25`, `B=2/5` consumes less than `1.26*10^-7` of the cube radius. The reserve guard (A5) was **not** independently recomputed. Accordingly this numerical adapter is not presented as a complete new theta certificate. The qualitative sufficiently-large-`T` corollary follows from Theorem A using the source's strict positive reserve.

## 4. Meaning and non-meaning

Taking `B=2/5` places the auxiliary xi-type zeros at real parts `1/10` and `9/10` after `s=1/2+iw`. This does not locate any zero of zeta. It shows that the finite match, exact normalization, whole-plane Gaussian envelope and a very small canonical quadratic-mass budget do not, by themselves, exclude that geometry in an auxiliary model.

This does **not** refute `WEIGHTED_CANONICAL.md`. Its hypothesis is feasibility at unbounded moment orders for the same source. Here the moment order is fixed; sending the inserted zero to infinity returns the old finite approximant, not the actual xi function.

The conclusion is not that finite certificates are useless. They supply valid local solutions and nonsingular starting points. It is that their existence, even with strong global envelopes, does not provide the missing all-order extension theorem.

## Relationship to the newer PR #1005

During the final live-repository read, PR #1005 appeared at commit `d3b3d19573b8dc47ac6e37abd108d54982e9e5f1`. Its `theta/KERNEL_STRIP_INSTABILITY.md` already proves a related and, in several directions, stronger obstruction: arbitrarily small smooth, strongly log-concave perturbations of the actual theta density can preserve any fixed finite list of moments and acquire an escaping nonreal zero. Accordingly, the general warning about finite moments is not claimed as a new repository insight here.

The more specific contribution of Theorem A is the explicit two-node insertion inside the existing canonical model, retention of its exact Gaussian whole-plane envelope, and the exact `O(T^-6)` canonical-mass cost. The companion probability theorem adds prescribed confinement of *all* zeros, a variance-based envelope, and calibrated leading zero-count/growth/tail terms; unlike #1005's density perturbation theorem, its theta application consumes the nonsingular finite Ising realization. Neither construction proves a new zeta boundary.
