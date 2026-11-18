# A fixed Weil window can miss a high defect in a zeta-density model

**Status.** Proposed solution of the model-theoretic interpretation of [Observatory question I2](https://github.com/GettysburgResearch/riemann/blob/2dbadaef2014cbebd1881b5ce261575e14f4edb7/research/exploratory/riemann-observatory/frontiers/unsolved_questions.md). For each prescribed finite $L>0$ and any fixed $0<\delta<1/2$, there is an even real entire completed-function model of order one, with the zeta counting main term up to $O(1)$ and a quartet of depth $\delta$, for which the zero-side Weil form is strictly coercive on $C_c^\infty(-L,L)$. One may impose any finite initial symmetric census of real ordinates. The model has no asserted Euler product or zeta prime explicit formula. The model may depend on $L$; a single off-line quartet cannot escape all unbounded windows simultaneously.

## Baseline

Take for large $j$ the increasing positive solutions $t_j$ of
\[
 M(t_j)=2j,\qquad M(t)=\frac{t}{2\pi}\log\frac{t}{2\pi e}+\frac78.
\]
Use double real zeros at $\pm t_j$. An arbitrary finite initial symmetric real zero census, all ordinates nonzero, may precede this tail. Then $N_+(T)=M(T)+O(1)$ counting multiplicities and $t_{j+1}-t_j\to0$. The product $\prod_j(1-z^2/t_j^2)^2$ times the corresponding finite factors converges locally uniformly because $\sum t_j^{-2}<\infty$. The bound $\sum_j\log(1+r^2/t_j^2)=O(r\log(2+r))$ follows by partial summation; the counting main term forces order at least one by Jensen. The completed function is thus even, real entire, and of order one. In the variable $s=1/2+iz$ it satisfies the usual reflection and reality equations. If desired, dividing the completion by $s(s-1)\pi^{-s/2}\Gamma(s/2)/2$ produces a model with the usual gamma factor and a simple pole at one; scalar normalization fixes its residue.

## Every fixed window has a strictly positive sampling floor

Write $F(z)=\int_{-L}^L g(u)e^{izu}du$. There exists $c_L>0$ such that the sum of $|F(t)|^2$ over the baseline zeros, with multiplicities, is at least $c_L\|g\|_2^2$. Suppose otherwise and take smooth $g_n$ of norm one with sums tending to zero. Pass to a weakly convergent subsequence in $L^2(-L,L)$. The limit has transform vanishing at every baseline zero. A nonzero transform obeys $|F(z)|\le\sqrt{2L}\|g\|_2 e^{L|\Im z|}$ and has $O(r)$ zeros on the disk of radius $r$ by Jensen (divide out any zero at zero). The baseline has $\gg r\log r$ distinct zeros there. Hence the weak limit is zero.

Fix $h<\pi/L$. For all large $|k|$, choose a baseline zero $s_k$ nearest $kh$. Then $|s_k-kh|\to0$; these choices are eventually distinct. If $|s_k-kh|\le\epsilon<h/3$ outside a finite set, the intervals between these endpoints are disjoint, and Cauchy–Schwarz followed by Plancherel gives
\[
 \sum_{\rm tail}|F_n(s_k)-F_n(kh)|^2
 \le\epsilon\int_{\mathbb R}|F_n'(t)|^2dt\le2\pi\epsilon L^2.
\]
The sum of squared samples at the $s_k$ tends to zero by hypothesis; at the remaining finitely many lattice nodes weak convergence gives the same conclusion. But Parseval for the zero extension on $[-\pi/h,\pi/h]$ yields $\sum_k |F_n(kh)|^2=2\pi/h$. Taking $\epsilon$ arbitrarily small is a contradiction.

## A quartet may be moved a fixed distance

At any sufficiently high $T=t_j$ replace the double zeros at $\pm T$ by the four zeros $\pm T\pm i\delta$ with multiplicity one. This finite change preserves the counting function by real ordinate exactly and the entire symmetries, by replacing the matching factors in the product. Write $W_T$ and $W_0$ for the resulting and baseline Weil forms. We claim $W_T(g)\ge(c_L/2)\|g\|_2^2$ for all sufficiently high choices of $T$.

Otherwise let $T_n\to\infty$ and choose normalized violating tests $g_n$. The eight old and new evaluations in the difference $W_0-W_{T_n}$ are uniformly bounded in modulus by $\sqrt{2L}e^{L/2}$, including multiplicities. Thus $W_0(g_n)$ stays bounded. Since $W_0(g_n)-W_{T_n}(g_n)>c_L/2$, at least one affected evaluation has modulus bounded below by a positive constant depending only on $L$. Pass to a subsequence fixing the center sign and the offset $z_0\in\{0,i\delta,-i\delta\}$. The functions $F_n(\pm T_n+z)$ form a locally bounded family and converge on compact sets along a further subsequence to an entire function with nonzero value at $z_0$.

On every finite real interval around the shifted center, the baseline ordinates become uniformly dense as $T_n\to\infty$, with the number in each subinterval of positive length tending to infinity. If the locally uniform limit were nonzero at any real point, an interval of uniformly bounded-below samples would force $W_0(g_n)\to\infty$. The entire limit must vanish on the real axis, a contradiction. This proves coercivity after perturbation without a separation assumption on its distance to surrounding real ordinates.
