# Full-source operators and arithmetic divisor geometry

[Guide](README.md) · [Proof library](SOURCE_INDEX.md) · [Evidence](EVIDENCE.md)

**Status:** reviewed component selections in an integration candidate; no unconditional RH conclusion or approval of a newly composed argument. Earlier heat, cardinal and xi statements remain in [the cumulative statement guide](../CURRENT_RESULTS.md#operators).

## 1. A complete fixed-window form, not just a matrix sample

Fix the source-defined even arithmetic kernel $W$ in the [logarithmic-core manuscript](../../../standalone/2026-09-06-logarithmic-core/PROOF.md). On $x\ge0$ it is

$$W(x)=\frac{e^{x/2}}2+C_b e^{-bx}+S(x)-\frac{P_2}{b}\cosh(bx)
 +\frac1b\sum_{2\le n\le e^x}\frac{\Lambda(n)}{\sqrt n}\sinh(b(x-\log n)),$$

where $b=3/2$, $C_b=(1-\gamma-\log(2\pi))/3$, $P_2=-\zeta'(2)/\zeta(2)$ and

$$S(x)=\sum_{j\ge1}\frac{e^{-(2j+1/2)x}}{(2j+1/2)^2-b^2}.$$

Every prime power and the complete safe prime tail belong to this definition. Boundary activations have zero value but retain their derivative jumps. For a finite interval $I$ the form is the double integral with kernel $W(t-u)$ on complex $L^2(I)$, with any additional damping handled by its stated conjugation in the source.

**Selected theorem:** this form is strictly positive on every nonzero complex $L^2$ test supported on an interval of length at most one. The certificate proves a positive extension with all 2,049 finite Fourier coefficients and a bound for every later coefficient. Its coercive lower norm is of $H^{-1}$ type. It is **not** a uniform $L^2$ eigenvalue gap, and its rational witness parameters are not certified zeta zeros.

**Proof route.** Keep the exact gamma and prime cusp in $W$, construct the source-defined positive extension on the required difference interval, certify the finite Fourier part and its complete residue-class tail, and pass from the extension to all complex tests. The corresponding effective $S_1$ bound uses the dual $H^1$ Gram, not an identification of the primal $L^2$ Gram with its dual. See the [full theorem, extension and source-to-form argument](../../../standalone/2026-09-06-logarithmic-core/window-one-positivity/PROOF.md) and [replay boundary](EVIDENCE.md#unit-window).

For each fixed larger window, the logarithmic-core theorem supplies an operator domain and core, dense strong-residual constructions, and converging lower and upper effective Schur enclosures. Constants may depend on the window. A strict finite-certificate consequence for all windows remains **conditional on RH and its stated classical multiplicity input**. The unconditional core theorem neither supplies the actual signs on all windows nor a rate uniform in length. Galerkin upper matrices alone are not lower certificates.

## 2. Quantitative control of the complete divisor graph

Let $S$ be a nonempty finite divisor-closed set of positive integers, with prime factors at most $P\ge2$. For complex Hilbert-valued $f$ use the harmonic norm and the full prime-power energy

$$\|f\|_S^2=\sum_{n\in S}\frac{\|f(n)\|^2}{n},\qquad
\mathcal E_S(f)=\sum_{jp^k\in S}\frac{\log p}{jp^k}\|f(jp^k)-f(j)\|^2.$$

Put $\bar f=(\sum_{n\in S}1/n)^{-1}\sum_{n\in S}f(n)/n$. The selected all-support bound is

$$\sum_{n\in S}\frac{\|f(n)-f(1)\|^2}{n}
 \le\kappa(P)\mathcal E_S(f),\qquad
\kappa(P)=48[1+\log(16\log P)].$$

Replacing $f(1)$ by the minimizing mean gives the centered bound. It is independent of exponent depth and support size. A complementary bound has inverse cost at most $24r$, where $r=\max_{n\in S}\omega(n)$ counts distinct primes; the singleton case is handled without dividing by zero. A selected original-edge decoder and a convergent full Poisson iteration have explicit costs after factorization and parent pointers are supplied.

**Proof route.** Remove the entire least-prime power on each tree edge. Descendants have smaller prime factors; a positive Euler-mass estimate bounds their harmonic congestion. The two proofs use related paths with different weights and quantitative costs. They are complementary bounds, not two unrelated mechanisms. See [depth-independent proof](../../../standalone/2026-09-08-astra-divisor-gap/PROOF.md) and [rank-sensitive decoder and spectra](../../../standalone/2026-09-08-astra-divisor-poincare/PROOF.md).

Fixed-finite-prime countable reservoirs have the stated closed form and self-adjoint domains. Exact one-prime and rectangular-product spectra do not tensorize the conditioned support $n\le N$, and do not define an unrenormalized all-prime infinite operator.

<a id="anchoring"></a>
## 3. A constant centered gap does not make anchoring cheap

For the squarefree prime box and the full geometric-exponent reservoir on primes through $P$, normalize harmonic mass to a probability. Set

$$ (b_p,a_p)=\left(p^{-1},(1+p^{-1})\log p\right)\quad\text{or}\quad
\left((p-1)^{-1},\frac{p\log p}{p-1}\right),$$

respectively. For a nonempty subset $D$ of the prime alphabet let $b_D=\prod_{p\in D}b_p$, $a_D=\sum_{p\in D}a_p$. The squared norm of root-minus-mean evaluation in the energy metric is

$$G_P=\sum_{D\ne\varnothing}\frac{b_D}{a_D}.$$

The optimal constant $C_P$ in $\|f-f(1)\|^2\le C_P\mathcal E(f)$ is the unique root above the inverse centered gap of

$$\sum_{D\ne\varnothing}\frac{b_D}{C_Pa_D-1}=1.$$

When the alphabet contains all primes through $P$ and $P\to\infty$,

$$G_P=\zeta(2)^{-1}\log\log P+O(1)\quad\text{(squarefree)},\qquad
G_P=\log\log P+O(1)\quad\text{(geometric)},$$

and $C_P-G_P=O(1/\log\log P)$. The centered gaps on these same reservoirs, when 2 is included, are $(3/2)\log2$ and $2\log2$.

**Proof route.** Diagonalize the product graph with its actual root weights. Root evaluation annihilates all higher exponent modes in the geometric case, so the displayed subset sum is exact, not a numerical truncation. A rank-one resolvent gives the secular equation. Elementary positive Euler products and the pole at real $s=1$ give the asymptotic; no nontrivial-zero spectrum is identified with this graph.

The common squarefree result is one selection with [grounding-capacity](../../../standalone/2026-09-08-astra-grounding-capacity/PROOF.md) and [coherent-channel](../../../standalone/2026-09-08-astra-coherent-channel-synthesis/PROOF.md) attributions. The geometric extension belongs to the former; the latter separately supplies the root-killed survival law with its full squared-norm normalization.

For the **specified** root coupling $\ell(f)=f(1)-\bar f$ on the mean-zero space,

$$c|a|^2+2\Re(\bar a\tau\ell(f))+\mathcal E(f)\ge0\quad\text{for all }a,f
\quad\Longleftrightarrow\quad c\ge|\tau|^2G_P.$$

No theorem here identifies the missing full xi/Weil coupling with this root coupling.

<a id="strong-schur"></a>
## 4. Current strong-residual Schur statement (R05)

Let $A$ be self-adjoint on a Hilbert space $U$, with $A\ge\gamma I$, $\gamma>0$. Let $B:H\to U$ be bounded and $H_0$ bounded self-adjoint on $H$. Require a bounded trial map $Y:H\to U$ with

$$Y(H)\subseteq\operatorname{Dom}(A),\qquad AY\text{ bounded}.$$

Define $R=B-AY$, $V=Y^*B+B^*Y-Y^*AY$, and $S=H_0-B^*A^{-1}B$. Then

$$B^*A^{-1}B-V=R^*A^{-1}R,\qquad
H_0-V-\gamma^{-1}R^*R\preceq S\preceq H_0-V.$$

**Proof.** Since $0\preceq A^{-1}\preceq\gamma^{-1}I$, the domain hypothesis allows $A^{-1}R=A^{-1}B-Y$. Expanding its quadratic form gives the identity and both inequalities. In finite dimension the domain condition is automatic. A bounded map into the form domain alone does not suffice in infinite dimension: for eigenvalues comparable to $j$, $\sum j^{-3/2}e_j$ is in the form domain but not $\operatorname{Dom}(A)$.

This is the repaired current statement, distinct from the preserved [original application wording](../../../standalone/2026-09-08-astra-divisor-gap/APPLICATION.md). Its [reviewed repair and actual one-prime example](../../../reviews/2026-09-08-postintegration/pass4/REPAIRS.md#r05--domain-of-trial-maps-for-the-infinite-schur-extension-new) remain separate provenance. It does not identify an actual xi coupling. The finite $N=32$ inverse uses all **65 edges and eleven prime bases**, with $0.7444806194657<b^TK^{-1}b<0.7444806194659$; the old count of ten bases is not retained (R04).

<a id="coherent-source"></a>
## 5. The native coherent channel is not a disposable mean

Take $\phi(t)=e^{-t/2}\mathbf1_{t\ge0}$, $v_n=\mu(n)S_{\log n}\phi$, $H_N=\sum_{n\le N}1/n$, and $M(k)=\sum_{n\le k}\mu(n)$. The literal stopped source satisfies

$$J_N=\left\|\sum_{n\le N}\frac{\mu(n)}{\sqrt n}S_{\log n}\phi\right\|_2^2
=\sum_{k<N}\frac{M(k)^2}{k(k+1)}+\frac{M(N)^2}{N}.$$

Projection of the Hilbert-valued vertex field onto $\{c/\sqrt n:c\in L^2\}$ has squared norm $J_N/H_N$. The full prime-power edge energy of the same field is $N\log N/\zeta(2)+O(N)$. Thus the graph gap bounds the **complement** and gives no upper bound on $J_N$. The last summand is the entire stable future of the stopped source, not future arithmetic events.

**Proof route.** Integrate on every integer cell and the final infinite interval; compute the harmonic projection before taking absolute values; expand every prime-power edge using the literal Möbius signs. See [complete source and delayed zero-detection proof](../../../standalone/2026-09-08-astra-coherent-channel-synthesis/COHERENT_SOURCE.md).

The exact work is $J_N=\sum\mu(n)^2/n+2\sum\mu(n)M(n-1)/n$. A subpower upper bound along an unbounded sequence would suffice for RH through its stated factorial-source convolution and zero-safe target. **That upper bound is open.** This simple exponential filter is not the cubic inverse-input filter in [the work campaign](CAUSAL.md#work).
