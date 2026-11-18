# Rank-by-rank zero repulsion sufficient for weak Mertens

Assume RH and simplicity. For $\gamma\in(T,2T]$ let $h_j(\gamma)$
be its distance to the $j$th nearest other ordinate, ordered by absolute
distance. This count includes other ordinates outside $(T,2T]$. Ties may
be placed in either order. Let $J=\lceil C_0\log T/\log\log T\rceil$,
with $C_0$ large enough for Littlewood's RH unit-interval counting error.
Consider the following unproved estimates for the actual zeros:
$$
 \#\{\gamma\in(T,2T]:h_j(\gamma)<ju/\log T\}
 \le T^{1+o(1)} e^{Cj^2} u^{\nu_j}
 \quad(1\le j\le J,\ 0<u<1).
 \tag{1}
$$
The little-oh is uniform in $j,u$. If $\nu_j\asymp j^2$ and
$H=\sum_{j\ge1}1/\nu_j<1$, then (1) implies weak Mertens.
More precisely,
$$
 \sum_{T<\gamma\le2T}|\zeta'(1/2+i\gamma)|^{-\lambda}
       \le T^{1+o(1)}\qquad(0<\lambda<1/H).
 \tag{2}
$$
For the unitary-model exponents $\nu_j=j(j+2)$ one has $H=3/4$ and
$J_{-1}(2T)-J_{-1}(T)\le T^{3/2+o(1)}$.
This is an implication from unweighted marginal spacing counts. There is
no joint-independence hypothesis and no bound assumed on derivatives.
The required estimates are on shrinking scales and increasing ranks.
Fixed-scale Montgomery pair correlation and the restricted Fourier-support
correlations of Rudnick–Sarnak do not provide (1).
[Montgomery](https://doi.org/10.1090/pspum/024/9944) ·
[Rudnick–Sarnak](https://doi.org/10.1215/S0012-7094-96-08115-6)

## From marginal counts to negative moments

Put $D=(\log T)/\log\log T$ and
$Y_j(\gamma)=\log^+(j/(h_j(\gamma)\log T))$.
There are at most $J$ other ordinates at distance $<1/\log\log T$,
by the RH counting formula with Littlewood's bound on $S(t)$.
By [the local product formula, equation (12)](trace-weak-mertens-nov18.md),
$$
 \log|\zeta'(1/2+i\gamma)|^{-1}
 \le o(\log T)+\sum_{j\le J}Y_j(\gamma).
$$
Indeed the discarded baseline is at most $\sum_{j\ge1}\log^+(D/j)=O(D)$
by Stirling; each relevant $\log(D/(h_j\log T))$ is bounded by the sum of
the two positive parts.

Choose $0<\theta<1$ with $\lambda H/\theta<1$ and $p_j=\theta\nu_j$.
Layer-cake integration of (1) gives
$$
 \sum_{T<\gamma\le2T} e^{p_jY_j(\gamma)}
 \le N(2T)-N(T)+T^{1+o(1)}e^{Cj^2}\frac{\theta}{1-\theta}.
$$
Generalized Hölder with weights $\lambda/p_j$ and unused weight placed
on the function one bounds $\sum_\gamma\exp(\lambda\sum_j Y_j)$ by
$T^{1+o(1)}\exp(O(\sum_{j\le J}j^2/p_j))=T^{1+o(1)}$.
This proves (2). Take any $1<\lambda<\min(2,1/H)$ and use
$\sum a_\gamma^2\le(\sum a_\gamma^\lambda)^{2/\lambda}$ for
$a_\gamma=|\zeta'(\rho)|^{-1}$. The resulting power saving from $T^2$
implies the hypotheses of [Meng, Theorem 6](https://arxiv.org/abs/1408.0429).
For $H=3/4$ take fixed $\lambda\uparrow4/3$ in the limiting log exponent.
Known estimates of Bui, Florea and Milinovich already give the same
$T^{3/2+o(1)}$ bound for zeros uniformly separated from others by
a fixed positive multiple of $1/\log T$. Equation (1) addresses the
remaining small-gap clusters. [Source](https://arxiv.org/abs/2310.03949)

## Verification in the unitary bulk model

The reduced Palm process of the sine-kernel determinantal process gives
(1)'s exponents and dependence on rank for a typical point, with unconditional
probability at most $e^{Cj^2}u^{j(j+2)}$. Indeed the intensity is one
and the $(j+1)$-point correlation pinned at $x_0=0$ is the Gram determinant
of $f_{x_i}(\xi)=e^{2\pi i\xi x_i}$ in $L^2[-1/2,1/2]$. At the $i$th
Gram–Schmidt step, interpolate the vector-valued map $x\mapsto f_x$
at the previous $i$ points. Its distance to their span is at most
$$
 \frac{\pi^i}{i!}\prod_{\ell<i}|x_i-x_\ell|
 \le\frac{(2\pi ju)^i}{i!}
$$
on $|x_\ell|\le ju$, by the divided-difference integral formula and
$\|\partial_x^i f_x\|_2\le\pi^i$. Coincident points have zero determinant.
A process with at least $j$ neighbors in this interval contributes at
least one unordered $j$-tuple. Integrating the determinant gives the bound
$$
 \frac{(2ju)^j}{j!}\prod_{i=1}^j\frac{(2\pi ju)^{2i}}{(i!)^2}
 \le e^{Cj^2}u^{j(j+2)}.
$$
For the last step use $\log(i!)\ge i\log i-i$ and
$\sum_{i\le j}i\log(j/i)=O(j^2)$. The argument applies at every rank and
scale in this model. Its analogue for actual zeta zeros remains open.

The restriction to marginal counts is substantive: this proof never
conditions a close second neighbor on a close first one. Conversely,
first-neighbor repulsion alone does not control the product over neighbors.
For instance four other points placed at respective distances comparable
to $T^{-1/3}/\log T$ from a point would be compatible with the scale of a
bounded exceptional count under the first-rank exponent three. Their four
factors alone would give a squared local inverse derivative product of
size $T^{8/3+o(1)}$ in the geometry of equation (12). This illustrates
the logical gap in using a pair bound alone; no such cluster is asserted
for zeta.
