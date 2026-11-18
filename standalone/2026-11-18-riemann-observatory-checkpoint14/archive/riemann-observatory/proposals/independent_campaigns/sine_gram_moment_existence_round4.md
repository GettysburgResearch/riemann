# Absolute graph integrals give every expected sine-Gram moment limit

2026-11-17. Proposer `/root/li_skeptic`. Advocate independently reconstructed and challenged the graph argument before reading this draft, finding no issue. Root adjudication requested. No novelty or RH claim. This supplies the model moment-existence step deliberately left conditional in the earlier sine-Gram proofs; it does not evaluate any arithmetic zeta/prime moment.

## Statement

Let `X` be the stationary unit-intensity sine determinantal process, with `K(t)=sin(pi t)/(pi t)`, `K(0)=1`. For `S_R=(K(x-y))_{x,y in X cap[0,R]}`, define

\[
 \mu_R=R^{-1}E\sum_{j=1}^{N_R}\delta_{\lambda_j(S_R)}.
\]

Then **every** expected normalized trace moment has a finite limit as `R` tends to infinity. Consequently the previously proved uniform factorial bound and no-atom theorem imply a unique full weak limit of these expected probability measures, with all moments converging, no atom at zero, a finite exponential moment, and a determinate moment problem. No ergodic theorem or almost-sure integrated density of states is asserted or needed.

## Lemma: a bridgeless graph makes the absolute sinc integral finite

Let `G` be a connected finite undirected multigraph on vertices `1,...,k`, with no loops and no bridges, where `k>=2`. Parallel edges are distinguished. Put `u_1=0` and `a(t)=|K(t)|`. Then

\[
 I_G=\int_{\mathbb R^{k-1}}\prod_{e=(i,j)\in E(G)}a(u_i-u_j)
                 \,du_2\cdots du_k<\infty.
\]

Proof: take the uniform probability distribution on the finite nonempty set of spanning trees of `G`. Let `p_T` be its weights and

\[
 \theta_e=\sum_{T\ni e}p_T.
\]

Every edge lies in some spanning tree, so `theta_e>0`; because it is not a bridge, deleting it leaves a connected graph with a spanning tree, so `theta_e<1`. Thus `r_e=1/theta_e>1`. Pointwise, with all factors nonnegative,

\[
 \prod_e a_e=
 \prod_T\left[\prod_{e\in T}a_e^{1/\theta_e}\right]^{p_T}.
\]

Generalized Hölder with the finite probability weights gives

\[
 I_G\le\prod_T\left[
  \int_{\mathbb R^{k-1}}\prod_{e\in T}a(u_i-u_j)^{1/\theta_e}du
                    \right]^{p_T}.
\]

For each rooted spanning tree the integral factors, by removing leaves, into
`product_{e in T} integral_R a(t)^{1/theta_e}dt`. Every factor is finite since `a in L^p(R)` for every `p>1`. Explicitly, the elementary envelope `a(t)<=min(1,1/(pi|t|))` gives

\[
 \int a(t)^pdt\le\frac{2p}{\pi(p-1)}<\infty.
\]

Combining the finite products proves the lemma and the useful bound

\[
 I_G\le\prod_e\left[\int a(t)^{1/\theta_e}dt\right]^{\theta_e}.
\]

No cancellation, Fourier-distribution product, or unproved absolute convergence is used. The absence of bridges is a real condition: a graph of two vertices and one edge gives the divergent integral `integral|sinc t|dt`.

## Why the trace partition graphs meet the lemma

Expand

\[
 \operatorname{Tr}S_R^m=\sum_{i_1,\ldots,i_m}
 K(x_{i_1}-x_{i_2})\cdots K(x_{i_m}-x_{i_1}).
\]

Partition the `m` cyclic positions according to equality of their point indices. A partition `pi` with `k` blocks creates a multigraph by identifying the corresponding vertices of the original closed cycle. Its edges retain their multiplicity; loops contribute `K(0)=1` and may be removed.

The quotient is connected. It is Eulerian: each block has equal incoming and outgoing degrees inherited from the closed walk; removing a loop removes one of each. Equivalently all undirected degrees remain even. A bridge would be the unique edge crossing some cut, contradicting parity of the sum of degrees inside that cut. Thus for `k>=2` the nonloop graph is connected and bridgeless, exactly the hypothesis of the lemma. The `k=1` term is simply `EN_R/R=1` and needs no integration argument.

## The exact moment-limit formula

Order the blocks of `pi` by first occurrence; let `b(l)` be the block label of cyclic position `l`, and put `u_1=0`. The factorial moment identity yields its contribution

\[
 \int_{[0,R]^k}\rho_k(x_1,\ldots,x_k)
       \prod_{l=1}^mK(x_{b(l)}-x_{b(l+1)})dx_1\cdots dx_k,
 \quad b(m+1)=b(1).
\]

The correlation determinant `rho_k` is translation invariant and satisfies `0<=rho_k<=1`. Translate `x_1=t`, `u_j=x_j-x_1`. Integrating over `t` and dividing by `R` gives exactly the multiplier

\[
 w_R(u)=\left(1-
 \frac{\max(0,u_2,\ldots,u_k)-\min(0,u_2,\ldots,u_k)}R\right)_+.
\]

It lies between zero and one and tends pointwise to one. The remaining integrand is

\[
 F_\pi(u)=\rho_k(0,u_2,\ldots,u_k)
        \prod_{l=1}^mK(u_{b(l)}-u_{b(l+1)}).
\]

Its absolute value is bounded by the graph integrand in the lemma, hence is integrable. Dominated convergence therefore proves the finite limit of each partition contribution. There are finitely many partitions at each fixed `m`, so

\[
 \boxed{\quad m_m=\lim_{R\to\infty}R^{-1}E\operatorname{Tr}S_R^m
    =\sum_{\pi\in\mathcal P_m}
      \int_{\mathbb R^{|\pi|-1}}F_\pi(u)\,du.\quad}
\]

For one-block partitions the integral over zero variables is defined as one. Every displayed integral is absolutely convergent, although individual values can have either sign because the sinc edge product can change sign. Their total is a nonnegative spectral moment.

## Full expected-law convergence and its boundary

The independently proved bound `integral lambda^m dmu_R<=4^m m!` is uniform in `R`. The first moment gives tightness, and higher moment bounds give uniform integrability of every fixed moment. All weak subsequential limits consequently have the same just-established moments `m_m`. Carleman makes that moment problem determinate, so all subsequential limits coincide. This proves full weak convergence of the **expected, per-length probability measures**.

The previous global-thinning/interpolation proof applies to every weak limit, so the unique limit has no atom at zero. Its exponential moment and the vanishing Christoffel minima follow as previously proved. This closes the purely model-side law-existence issue. It does **not** prove matching of zeta or prime-side trace moments to this law, does not establish almost-sure spectral convergence, and does not independently audit all claims in AF§7.2.

## Reusable mathematical connection and next step

The exact missing analytic hypothesis was absolute integrability after anchoring one point. A closed trace walk supplies a connected Eulerian quotient graph; its lack of bridges supplies spanning-tree edge marginals strictly below one; these marginals choose Hölder exponents above one, precisely the integrability range of the sinc kernel. This is an actionable graph-to-analysis implication, not a vocabulary analogy.

The resulting finite partition-integral representation can be used to compute further moments or derive better bounds. A rigorous next step is to expand each correlation determinant and use Fourier band indicators to express the anchored sinc integrals as volumes of finite rational flow polytopes, preserving signs and normalization. That algorithmic representation and any higher exact moment values have not been proved or computed in this note. Priority of the graph-integrability assembly remains unassessed.
