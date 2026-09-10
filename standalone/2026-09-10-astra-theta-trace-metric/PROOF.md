# Whole-theta trace positivity and the cost of a spectral metric

Date: 2026-09-10. Status: **PROPOSED component proofs; independent mathematical review required.**

**No complete RH proof is obtained.** This paper attacks the end of the whole-xi operator route rather than its integration machinery. It proves a stronger obstruction to one proposed finish, replaces that finish by an exact scalar positivity obligation, checks the scalar obligation at order four directly from the complete theta source, and disproves a tempting generic induction principle. The all-order theta-specific positivity assertion remains open.

The principal predecessor is PR #834, `standalone/2026-09-09-centered-theta-determinant/PROOF.md`, at `f0e34780f4fe91bd5d07e791e8855189838c3df5`. Its general determinant construction, its failure of bounded metrics on the full space and finite derivative cuts, and its still-open infinite-cut possibility motivate this work. We do not claim to have independently accepted that entire packet. The eigenvector identities needed for our obstruction are reconstructed below; the scalar criterion can also be obtained directly from classical Hadamard factorization, without relying on the proposed operator determinant.

Metric conditioning, finite-difference cancellation, moment problems and entire-function products are classical mechanisms. No external novelty or priority claim is made for those mechanisms or for reformulating RH through positive power sums. The source-specific quantitative application and numerical enclosure are submitted for review.

## 1. One unchanged source and its operators

Use the entire continuation of

$$\xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),\qquad \xi(0)=\xi(1)=\tfrac12,$$

and the real entire even function $\Xi(z)=\xi(1/2+iz)$. The full-line theta convention is

$$\Xi(z)=\int_{\mathbb R}\phi(t)e^{izt}\,dt,$$

$$\phi(t)=\sum_{n\ge1}\left(4\pi^2n^4e^{9t/2}-6\pi n^2e^{5t/2}\right)e^{-\pi n^2e^{2t}}.\tag{1}$$

Jacobi inversion makes the **complete sum** even. For $t\ge0$ each displayed summand is positive. Put $Z=\Xi(0)>0$, $w=\phi/Z$, and $\mu_k=\int t^k w(t)\,dt$. All moments and all exponential moments exist. Negative time is treated by evenness of the whole source, not evenness of each summand.

Let $H_w=L^2(\mathbb R,w(t)dt)$, with scalar product conjugate-linear in the first variable, $F(t)=\int_{-\infty}^tw$, and $Q=1-F$. The centered antiderivative is

$$(Kf)(x)=\int_{\mathbb R}\bigl(\mathbf1_{t<x}-Q(t)\bigr)f(t)\,dt.\tag{2}$$

The integration on the right is with respect to Lebesgue measure. Its squared Hilbert--Schmidt norm is

$$\|K\|_{\rm HS}^2=\int_{\mathbb R}\frac{F(t)Q(t)}{w(t)}\,dt<\infty.\tag{3}$$

Indeed, for fixed $t$, the weighted squared norm of the numerator in (2), as a function of $x$, is $F(t)Q(t)$. The source tail is

$$\phi(t)=4\pi^2e^{9t/2-\pi e^{2t}}(1+O(e^{-2t})),\qquad t\to+\infty,$$

with differentiated remainders at each fixed order. Writing $V=-\log w$ gives $V'(t)\ge c e^{2t}$ and increasing $V'$ for sufficiently large $t$. Consequently $Q(t)/w(t)\ll e^{-2t}$; reflection handles the other tail. Compact intervals present no singularity.

On compact inputs, $(Kf)'=f$ and $\int Kf\,w=0$. Density and distributional passage on compact intervals extend both identities to every $f\in H_w$. The unique mean-zero antiderivative of $e^{ut}$ is therefore

$$K e^{ut}=\frac{e^{ut}-M(u)}u,\qquad M(u)=\int e^{ut}w(t)dt,\quad u\ne0.\tag{4}$$

The exponential and its antiderivative lie in $H_w$ for every complex $u$ by the complete source tail. If $\gamma$ is a real zero of $\Xi$, then

$$K e^{i\gamma t}=\frac1{i\gamma}e^{i\gamma t}.\tag{5}$$

Parity anticommutes with $K$. Thus $T=-K^2$ restricted to the odd subspace is trace class, and $\sin(\gamma t)$ is its eigenvector with eigenvalue $\gamma^{-2}$.

For $q_j=w^{(j)}/w$, the differentiated tail gives $q_j\in H_w$. Define

$$W_\infty=\{f\in H_w:\langle q_j,f\rangle=0\text{ for every }j\ge0\}.\tag{6}$$

Every real-zero exponential belongs to this intersection: integration by parts $j$ times gives

$$\langle q_j,e^{i\gamma t}\rangle=(-i\gamma)^j\Xi(\gamma)/Z=0.\tag{7}$$

All endpoint products vanish by the source tail. Sines belong as well. The predecessor's identities $K^*q_0=0$, $K^*q_{j+1}=-q_j$ show that $W_\infty$ is $K$-invariant; they also follow directly by integration by parts in (2). The following obstruction therefore applies **after every derivative constraint has been imposed**, not merely to the old adjoint-kernel defect.

## 2. The exact two-vector cost

**TMC1.** Let $f,g$ be distinct normalized vectors in a Hilbert space, with $c=|\langle f,g\rangle|<1$. Among positive definite metrics on their span that make $f$ and $g$ orthogonal, the smallest condition number is

$$\frac{1+c}{1-c}.\tag{8}$$

Here $\operatorname{cond}(G)=M/m$ when $mI\preceq G\preceq MI$ and the bounds are optimal on the stated subspace.

**Proof.** Rotate $g$ so $\langle f,g\rangle=c\ge0$. Orthogonality in the new metric implies

$$\|f+g\|_G^2=\|f-g\|_G^2.$$

The original squared norms are $2(1+c)$ and $2(1-c)$, so $m(1+c)\le M(1-c)$. Equality is attainable: in the original orthonormal directions proportional to $f+g$ and $f-g$, give $G$ eigenvalues $(1+c)^{-1}$ and $(1-c)^{-1}$. Direct substitution makes the cross inner product zero. This proves both necessity and sharpness.

For the source (1), real-zero exponentials have

$$c=\left|\frac{\Xi(\gamma-\gamma')}{Z}\right|.$$

If $\Delta=\gamma-\gamma'\to0$, then $c=1-\mu_2\Delta^2/2+O(\Delta^4)$, and (8) is asymptotic to $4/(\mu_2\Delta^2)$. This is a source-normalized conditioning statement, not a numerical assertion about any particular pair of zeros. The stronger cluster argument below does not need a quantitative minimum-gap theorem.

## 3. A cluster forces factorial metric cost

**TMC2.** Suppose $\gamma_1,\ldots,\gamma_r$ are distinct real frequencies in an interval of length $L>0$, $r\ge2$. Any metric $mI\preceq G\preceq MI$ on their exponential span that orthogonalizes $e^{i\gamma_jt}$ satisfies

$$\operatorname{cond}(G)\ge\frac{((r-1)!)^2}{rL^{2r-2}\mu_{2r-2}}.\tag{9}$$

For the sine span, if every $\|\sin(\gamma_jt)\|_w^2\ge1/4$ and the positive frequencies are distinct, the corresponding bound is

$$\operatorname{cond}(G)\ge\frac{((r-1)!)^2}{4rL^{2r-2}\mu_{2r-2}}.\tag{10}$$

**Proof.** Write $\gamma_j=\Gamma+\delta_j$, $0\le\delta_j\le L$. Choose a real vector $a$ of Euclidean norm one in the nullspace of the $(r-1)\times r$ Vandermonde matrix $(\delta_j^k)_{0\le k<r-1}$. Its rank is $r-1$ because the frequencies are distinct. The real-parameter Taylor formula with integral remainder gives

$$\left|e^{i\delta t}-\sum_{k=0}^{r-2}\frac{(i\delta t)^k}{k!}\right|\le\frac{L^{r-1}|t|^{r-1}}{(r-1)!},$$

for real $t$ and $0\le\delta\le L$. There is **no** extra $e^{|t|}$ factor: the differentiated oscillatory exponential has modulus at most one. Cancellation of every polynomial term and $\sum|a_j|\le\sqrt r$ give

$$\left\|\sum a_je^{i\gamma_jt}\right\|_w^2\le \frac{rL^{2r-2}\mu_{2r-2}}{((r-1)!)^2}.\tag{11}$$

In the $G$ norm the same sum has squared norm $\sum |a_j|^2\|e^{i\gamma_jt}\|_G^2\ge m$. Its upper bound is $M$ times (11), proving (9).

For sines use the Taylor formula in the frequency variable for $\sin((\Gamma+\delta)t)$. Every frequency derivative has modulus at most $|t|^k$, so the identical upper bound applies. Orthogonality gives the lower bound $m/4$. Distinct positive sine frequencies are linearly independent, completing (10).

## 4. The complete theta tail and superpolynomial cost in zero height

The metric lower bound is useful only if the moments in its denominator are actually controlled. The source permits a simple all-order bound.

**Lemma 4.1.** For every integer $k\ge1$,

$$\mu_k^{\rm abs}:=\int |t|^k w(t)dt\le C\,[2\log(k+2)]^k,\qquad C=32\pi^2/Z.\tag{12}$$

**Proof.** On $t\ge0$ the negative part in each summand of (1) may be discarded for an upper bound. Since $e^{-3\pi}<1/1000$ and $n^2-1\ge3(n-1)$,

$$\sum_{n\ge1}n^4 e^{-\pi(n^2-1)e^{2t}}\le\sum_{n\ge1}n^4 1000^{-(n-1)}<2.$$

The last bound follows either by summing the differentiated geometric series or directly by its term ratios. Hence $\phi(t)\le8\pi^2e^{9t/2-\pi e^{2t}}\le8\pi^2e^{-e^t}$. For the second inequality put $r=e^t\ge1$: $(9/2)\log r-\pi r^2+r<0$, since its derivative is already negative at one and is strictly decreasing.

Take $L=2\log(k+2)>2$. On $[0,L]$, $t^k\le L^k$ and $\int_0^\infty e^{-e^t}dt\le e^{-1}$. On the tail put $t=L+u$. Then

$$(L+u)^k\le L^ke^{ku/L},\qquad e^{L+u}\ge(k+2)^2(1+u).$$

Its integral is at most

$$L^k\frac{e^{-(k+2)^2}}{(k+2)^2-k/L}\le L^k.$$

Reflection, normalization and these two estimates prove (12).

We use two **classical unconditional** zero-count inputs, not a new numerical zero census:

$$N(T)=\frac{T}{2\pi}\log\frac{T}{2\pi}-\frac{T}{2\pi}+O(\log T),\qquad
N_0^*(T)\ge c_0T\log T\quad(T\text{ sufficiently large}),\tag{13}$$

where $N_0^*$ counts **simple** critical-line zeros and $c_0>0$. The second follows, for example, from Bui--Conrey--Young, Theorem 1.1, whose stated lower simple proportion is $0.4058$. The unit-length argument uses only a positive proportion. The explicit nonoptimal strengthening below uses the weaker consequence that the simple proportion exceeds $2/5$; the published proportion is not recomputed here. The first is the classical Riemann--von Mangoldt count.

**TMC3.** There are constants $c>0$ and $T_0$ such that the following holds for every $T\ge T_0$. Any positive metric that orthogonalizes all the simple critical-line exponential modes with ordinates in $(0,T)$ has

$$\operatorname{cond}(G_T)\ge\exp(c\log T\log\log T).\tag{14}$$

The same statement holds for their sine modes. Consequently no bounded coercive positive metric makes $iK|_{W_\infty}$ self-adjoint, or makes $T|_{W_\infty\cap H_o}$ self-adjoint. Even a family of equivalent finite-height metrics with polynomial condition number is impossible.

**Proof.** The upper count in (13) removes only $O(\sqrt T\log T)$ zeros below $\sqrt T$. Partition $[\sqrt T,T]$ into at most $T+1$ intervals of length at most one. The remaining lower count yields a bin containing at least $c_1\log T$ distinct simple real ordinates, for all sufficiently large $T$. Select exactly $r=\lfloor c_1\log T\rfloor$ of them, decreasing $c_1$ if necessary.

For exponentials use (9) with $L=1$ and (12). Stirling's elementary factorial bounds give

$$\log\frac{((r-1)!)^2}{Cr[2\log(2r)]^{2r-2}}
=2r\log r-2r\log\log r-O(r).\tag{15}$$

This is bounded below by $c\log T\log\log T$. For sines, the Riemann--Lebesgue lemma gives

$$\|\sin(\gamma t)\|_w^2=\tfrac12[1-\Xi(2\gamma)/Z]\to\tfrac12.$$

The selected ordinates exceed $\sqrt T$, so their squared norms are at least $1/4$ eventually and (10) gives the same result.

For the operator consequence, distinct eigenvalues of an operator symmetric in a positive metric have orthogonal eigenvectors in that metric. Equations (5)--(7) place all these eigenvectors in the indicated infinite intersections. A bounded coercive metric on either full remaining space would induce uniformly bounded condition numbers on the finite spans, contradicting (14). No completeness or Riesz-basis assertion was assumed. No effective $T_0$ or numerical value of $c$ is supplied.

### A stronger stretched-exponential lower bound

The same argument permits a growing cluster interval and gives more than (14). For all sufficiently large $T$, every metric in TMC3 in fact satisfies

$$\operatorname{cond}(G_T)\ge\exp\!\left(\frac1{1000}T^{1/1000}\log T\right).\tag{14a}$$

The constants are deliberately nonoptimal; the height threshold remains unevaluated.

To see this, the simple proportion greater than $2/5$, the classical count and $\pi<4$ imply $N_0^*(T)\ge T\log T/20$ eventually. Removing ordinates below $\sqrt T$ leaves at least $T\log T/25$ eventually. Put $L=T^{1/1000}$ and partition $[\sqrt T,T]$ into at most $2T/L$ bins of length at most $L$. Some bin contains at least $L\log T/50$ simple ordinates. Select $r=\lfloor L\log T/100\rfloor$, and set $m=r-1$.

By (9)--(12), with a factor 4 allowed to include the sine case,

$$\operatorname{cond}(G_T)\ge\frac1{4Cr}\left(\frac{m}{2eL\log(2m+2)}\right)^{2m},$$

using the elementary bound $m!\ge(m/e)^m$. The expression inside parentheses tends to $5/e>5/3$, so it exceeds $3/2$ eventually. Now $m\sim L\log T/100$ and $\log(3/2)>1/3$. The logarithm of the last display consequently exceeds $L\log T/1000$ for all sufficiently large $T$, proving (14a). All selected ordinates still exceed $\sqrt T$, so the same sine normalization applies. This argument introduces no zero-location computation or RH assumption.

**Scope.** This result extends the predecessor's finite-cut obstruction to its proposed infinite derivative-cut escape. It is **not** a counterexample to RH. Real spectrum is compatible with arbitrarily ill-conditioned eigenvectors of a nonnormal compact operator. Unbounded metrics, nonequivalent norms and entirely different Hilbert--Polya constructions are not ruled out.

There is another reason not to demand such a metric indiscriminately: self-adjointness excludes nontrivial Jordan chains. If $(A-\lambda)u_1=u_0$, $(A-\lambda)u_0=0$, then metric symmetry for real $\lambda$ implies $\langle u_0,u_0\rangle_G=0$. In the centered-antiderivative realization, every nonzero eigenspace is one-dimensional and multiple xi zeros generate Jordan chains by differentiating (4). A metric argument on all generalized eigenvectors would therefore demand simplicity as well as RH. The scalar route next does not demand simplicity.

## 5. Scalar replacement: one Hankel tower with multiplicities retained

A self-adjointization is more than the desired zero-location assertion. We now remove that unnecessary requirement. The resulting criterion is in the classical power-sum/moment tradition; related positive-zero criteria and RH applications are given by R. Zhang, *On Power Sums of Positive Numbers*, arXiv:1510.03420. We use no theorem from that paper without proof: the precise version needed here follows below.

**Lemma 5.1.** Let $(\lambda_j)$ be a finite or countable multiset of nonzero complex numbers, with positive integer multiplicities absorbed in its listing, and $\sum_j|\lambda_j|<\infty$. Suppose every $s_m=\sum_j\lambda_j^m$ is real, $m\ge1$. Then

$$(s_{i+j+1})_{0\le i,j\le N}\succeq0\text{ for every }N
\quad\Longleftrightarrow\quad \lambda_j\in(0,\infty)\text{ for every }j.\tag{16}$$

An empty multiset is allowed. Algebraic multiplicity is never replaced by distinct-node counting.

**Proof of necessity.** Write $h_n=s_{n+1}$, $R=\sup|\lambda_j|$ and $C_1=\sum|\lambda_j|$. The empty case is immediate; otherwise $R>0$ and $|h_n|\le C_1R^n$. Hankel positivity defines a positive functional $L(x^n)=h_n$ on complex polynomials, with $\langle p,q\rangle=L(\bar p q)$.

For fixed $p$ let $a_n=L(x^{2n}|p|^2)\ge0$. Cauchy--Schwarz implies $a_n^2\le a_{n-1}a_{n+1}$, and the moment bound gives $a_n\le C_p R^{2n}$ with a finite $p$-dependent constant. If $a_0>0$ and $a_1>R^2a_0$, log-convexity forces $a_n\ge a_0(a_1/a_0)^n$, contradicting that growth. If $a_0=0$, Cauchy--Schwarz between $p$ and $x^2p$ gives $a_1=0$. Thus

$$L(x^2|p|^2)\le R^2L(|p|^2).$$

Multiplication by $x$ descends to the null quotient and extends to a bounded self-adjoint operator on its Hilbert completion. The classical spectral theorem applied to the vector 1 gives a positive finite measure $\nu$ supported in $[-R,R]$ with $h_n=\int x^n d\nu(x)$. This use of the bounded self-adjoint spectral theorem is a declared classical input, not an assertion that the original $T$ was self-adjoint.

For $|z|>R$, absolutely convergent series give

$$C(z):=\sum_j\frac{\lambda_j}{z-\lambda_j}=\int\frac{d\nu(x)}{z-x}.\tag{17}$$

The left side is meromorphic away from zero, with the only possible accumulation of poles at zero. A nonreal $\lambda$ would be an isolated pole of residue $m_\lambda\lambda\ne0$. Analytic continuation of (17) into the upper or lower half-plane contradicts that pole, since the positive-measure transform is analytic there. Hence all nodes are real.

For a negative node $\lambda$, the left side has residue $m_\lambda\lambda<0$. On the right,

$$\lim_{\eta\downarrow0}i\eta C(\lambda+i\eta)=\nu(\{\lambda\})\ge0,$$

by dominated convergence, since $|i\eta/(\lambda+i\eta-x)|\le1$. The same limit on the meromorphic side is the negative residue, a contradiction. Thus every node is positive. This argument also treats repeated nodes: their residues add with the same nonzero sign, rather than canceling.

**Sufficiency.** If every node is positive, then for any polynomial $p$,

$$\sum_{i,j}\bar a_i a_j s_{i+j+1}=\sum_j\lambda_j|p(\lambda_j)|^2\ge0.$$

Absolute convergence follows from bounded nodes and $\sum|\lambda_j|<\infty$. This proves (16).

### The literal theta traces

Define cumulants by $\log M(u)=\sum_{n\ge1}\kappa_nu^n/n!$ near zero, where $M(u)=\int e^{ut}w(t)dt$. Set

$$s_m=\frac{(-1)^{m+1}\kappa_{2m}}{2(2m-1)!},\qquad
H_N=(s_{i+j+1})_{0\le i,j\le N}.\tag{18}$$

The moments determining these numbers are those of (1), not sums over a supplied zero table. Cumulants can be computed without numerical differentiation by

$$\kappa_n=\mu_n-\sum_{j=1}^{n-1}\binom{n-1}{j-1}\kappa_j\mu_{n-j}.\tag{19}$$

For the predecessor's operator these are $\operatorname{Tr}T^m$. Independently, classical entire-function growth and Hadamard factorization give the same identification: the even function $G(v)=\Xi(\sqrt v)/Z$, defined by its power series, has order $1/2$ and genus zero. If one zero $z_j$ from each pair $\pm z_j$ is retained with its multiplicity, then

$$G(v)=\prod_j(1-v/z_j^2),\qquad \sum_j|z_j|^{-2}<\infty.$$

There is no undetermined exponential factor for this order, and $G(0)=1$. Comparing logarithms at zero with $M(iz)=\Xi(z)/Z$ gives $s_m=\sum_j z_j^{-2m}$, with complete multiplicity. The zero-count/growth and Hadamard facts are classical inputs; no unknown zero is assigned a numerical value.

**TMC4 (complete scalar consumer).** The following are equivalent:

1. RH.
2. Every $H_N$ in (18) is positive semidefinite.
3. Every leading determinant $\det H_N$ is strictly positive.

**Proof.** Apply Lemma 5.1 to $\lambda_j=z_j^{-2}$. Positive $\lambda_j$ mean $z_j^2>0$, hence every $z_j$ is real, which is RH. Under RH there are infinitely many distinct positive nodes. A nonzero polynomial cannot vanish at all of them, so the displayed weighted sum is strictly positive and all finite $H_N$ are positive definite. This yields the determinant assertion. Conversely strict positivity of every leading principal determinant is the positive-definite Sylvester criterion for each finite matrix, and implies item 2. This strict criterion must not be confused with the false assertion that nonnegative leading minors alone characterize semidefiniteness.

The theorem preserves multiple zeros. It neither constructs a bounded metric on the old operator nor assumes eigenvector completeness. It is an exact consumer of the still-missing all-order scalar sign, not a proof of that sign.

## 6. A whole-source fourth-order certificate

**TMC5 (finite, proposed certificate-backed component).** For the literal source (1), $H_3=(s_{i+j+1})_{0\le i,j\le3}$ is strictly positive definite.

The proof is the finite outward computation specified completely in [NUMERICS.md](NUMERICS.md) and regenerated by `theta_moments.py`. It integrates all even moments through degree 14 from the defining theta series. All omitted indices, all times beyond the finite integration interval, and every Taylor remainder are bounded before cumulants and interval LDL are formed. Neither a zeta evaluator nor a zero ordinate enters the calculation.

Conservative readable enclosures for the four positive LDL pivots are

| Pivot | Lower bound | Upper bound |
|---|---:|---:|
| 1 | 0.0231049931154 | 0.0231049931155 |
| 2 | 0.00000008436858410 | 0.00000008436858411 |
| 3 | 0.0000000000001114641604 | 0.0000000000001114641605 |
| 4 | 0.00000000000000000005419624538 | 0.00000000000000000005419624539 |

In particular $1.1775\cdot10^{-41}<\det H_3<1.1777\cdot10^{-41}$. Exact dyadic intervals, not these shortened decimal displays, are the accepting receipt. This is one matrix theorem with nested lower-order consequences, **not four independent RH tests or an unbounded hierarchy**. It supplies no new zero-free height range by itself.

## 7. The attempted generic induction is false even with strong source hypotheses

A natural attempted last step would use positivity, evenness, strict log-concavity and very rapid source decay to propagate the observed trace positivity. These properties do not suffice.

**TMC6.** There exist smooth positive even strictly log-concave densities with double-exponential tails, all exponential moments and a Hilbert--Schmidt centered antiderivative, for which $s_1>0$ but $s_3<0$. Their trace-Hankel matrix $H_1$ is not positive semidefinite.

**Proof.** Start with the normalized Gaussian mixture

$$w_0(t)=\pi^{-1/2}\left[\tfrac34e^{-t^2}+\tfrac18e^{-(t-1/2)^2}+\tfrac18e^{-(t+1/2)^2}\right].$$

It is the law of an independent centered Gaussian of variance $1/2$ plus a variable taking $-1/2,0,1/2$ with probabilities $1/8,3/4,1/8$. Its exact cumulants are

$$\kappa_2=9/16,\qquad \kappa_4=1/256,\qquad \kappa_6=-7/2048.\tag{20}$$

For any such mixture, differentiation of the tilted finite mixture gives $(\log w_0)''=-2+4\operatorname{Var}_t(A)\le-1$, since $|A|\le1/2$. Now use the normalized density

$$w_\epsilon(t)=c_\epsilon e^{-\epsilon\cosh(2t)}w_0(t),\qquad\epsilon>0.\tag{21}$$

It remains positive, even, smooth, and $(\log w_\epsilon)''\le-1-4\epsilon\cosh(2t)<0$. Its tails satisfy

$$-\log w_\epsilon(t)=\tfrac\epsilon2e^{2|t|}+t^2-|t|+O_\epsilon(1).$$

In particular the same $FQ/w$ tail argument as (3) proves Hilbert--Schmidt boundedness. All exponential moments exist. Dominated convergence for each of the first six moments, and their polynomial cumulant formulas, shows that $\kappa_6(w_\epsilon)<0$ for every sufficiently small positive $\epsilon$. The variance stays positive. Hence (18) gives $s_1>0$ and $s_3<0$, which already violates a diagonal condition for $H_1$.

The limiting Gaussian mixture itself is not claimed to have a Hilbert--Schmidt centered antiderivative; the positive damping in (21) is essential for that property. No numerical epsilon or zero is needed for this existence proof. These are deliberately **changed sources**, not the actual theta density and not off-line zeta zeros. The actual theta arithmetic identity is not preserved by (21).

## 8. End-to-end attack: precisely where it stops

The operator route has an exact characteristic function, but a bounded or polynomially conditioned positive spectral metric is now ruled out even on the infinite derivative-cut space. That is a stronger conclusion than the finite-cut obstruction, not progress toward a metric that cannot exist.

The replacement route is fully specified:

$$\text{literal whole theta density}\longrightarrow
\text{moments and cumulants}\longrightarrow
\boxed{H_N\succeq0\ \text{for every }N}\longrightarrow
\text{positive reciprocal-squared zero nodes}\longrightarrow\mathrm{RH}.$$

The first construction and final consumer are justified above, and the box is checked for $N\le3$. The boxed **all-order** assertion is not proved. Section 7 shows why a broad log-concavity/decay induction cannot fill it, and Section 4 shows why a bounded-metric argument on the original operator cannot fill it either.

A further productive attempt must use a theta-specific identity controlling every Schur pivot or an equivalent complete scalar inequality. Its quantifiers, cumulant subtractions and complete source must remain intact. The finite positive determinant is not represented as making that remaining task routine. No claim of a complete proof, new zeta zero, canonical mathematical acceptance or repaired Lean implementation is made.

## References and input boundaries

- **Repository source:** PR #834 at the exact commit above, principal proof Sections 1--8, including the infinite derivative-cut proposal. No parent executable was run. This paper reconstructs its needed eigenvectors and derives the scalar consumer independently through Hadamard factorization.
- **H. M. Bui, J. B. Conrey, M. P. Young:** *More than 41% of the zeros of the zeta function are on the critical line*, arXiv:1002.4127v2, Theorem 1.1. The first PDF page was read and visually checked. Only the stated simple-proportion theorem is imported (positivity for (14), the weaker $>2/5$ consequence for (14a)); the proof of their theorem and its numerical optimization were not replayed.
- **Classical Riemann--von Mangoldt count, xi entire growth and Hadamard factorization:** standard analytic-number-theory/entire-function inputs at the scopes explicitly stated in (13) and Section 5. Hasanalizade--Shen--Wong, arXiv:2107.06506v1, Corollary 1.2 and Section 2, were read and visually checked for the count and entire order (their xi differs by a factor of two). Only the qualitative count is consumed, not a new optimization of their constants. NIST DLMF 25.4 and 25.10 were consulted for normalization, symmetry and zero context; they are not represented as complete proofs of all these inputs.
- **Classical bounded self-adjoint spectral theorem:** used in the polynomial moment-functional proof of Lemma 5.1, not assumed for the original nonsymmetric operator.
- **R. Zhang:** *On Power Sums of Positive Numbers*, arXiv:1510.03420v2, abstract consulted for prior power-sum/moment criteria and RH applications. No theorem is imported from an unread proof, and the present criterion is not claimed to originate here.

Detailed exact source locks and orientation-only reads are in [SOURCES.json](SOURCES.json); executed evidence and omissions are in [VALIDATION.md](VALIDATION.md).
