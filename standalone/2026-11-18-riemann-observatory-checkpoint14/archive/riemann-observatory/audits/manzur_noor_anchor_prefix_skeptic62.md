# Manzur–Noor transport, the nonprincipal anchor, and prefix rates

The single-generator criterion in Manzur–Noor works in the zeta disk Hardy space. Its exact step-space transport has a nonprincipal analogue, but that analogue meets the anchor obstruction at a specific evaluation. For a fixed nonprincipal character $\chi$, a translated anchored generator cannot belong to the anchored closure unless its dilation index and translation parameter satisfy an explicit resonance. Even for the zeta criterion, the transported vector has infinitely many nonzero formal divisor coefficients. Membership in its closure supplies no fixed-prefix approximation rate. [Manzur–Noor, arXiv v1](../sources/prefix_skeptic62_criteria2/manzur_noor.pdf) · [Nonprincipal anchor proof](adversarial_reviews/director_imprimitive_anchor_round8.md)

## Source criterion and exact dictionary

The original paper uses $H^2(\mathbb D)=\ell^2(\mathbb N_0)$, with its coefficient norm. For $k\ge2$ its vector is $h_k(z)=(1-z)^{-1}\log[(1+z+\cdots+z^{k-1})/k]$. Let $\mathcal N$ be their closed span. The bounded Copson operator $C$ has norm at most 2 on $\ell^2$. The operators from the source are
$$
T_\tau=D_\tau+CQ_\tau,\quad D_\tau e_j=(j+1)^{i\tau}e_j,\quad
Q_\tau e_j=j[(j+1)^{i\tau}-j^{i\tau}]e_j\ (j\ge1),\quad Q_\tau e_0=0.
$$
They form a group with $\|T_\tau\|\le1+2|\tau|$ by the source's difference identity $(I-S^*)T_\tau=D_\tau(I-S^*)$. The kernel $k_s$ represents the functional $\Lambda_s$, for $\Re s>1/2$. The source computes
$$
T_\tau^* k_s=(\bar s+i\tau)k_{s-i\tau}/\bar s,\qquad
\Lambda_s(h_k)=-\frac{\zeta(s)}s(k^{1-s}-1).
$$
If $T_\tau h_k\in\mathcal N$ for one $k$ and $\tau\ne0$, each hypothetical off-line zero $\rho$ forces $\rho-i\tau$ also to be a zero, since $|k^{1-\rho+i\tau}|>1$. Iteration contradicts the Ingham bound $N(\sigma,T)=o(T)$ at any fixed $1/2<\sigma<\Re\rho$, using conjugation if the progression has eventually negative ordinates. Conversely RH gives density of $\mathcal N$, so membership follows. This verifies the analytic hypotheses and the actual one-vector condition in Theorem 5.1. It concerns kernel evaluation strictly inside the half-plane. The proof here does not need a boundary interpretation of $k_s$. [Manzur–Noor, §§2–5](../sources/prefix_skeptic62_criteria2/manzur_noor.pdf)

There is an explicit bounded isomorphism to the arithmetic step space $S$ with cells $[n,n+1)$, $n\ge1$, and norm $\sum_{n\ge1}|b_n|^2/[n(n+1)]$. Define
$$
(Ba)_n=b_n=\sum_{j=0}^{n-1}a_j-na_n,\qquad
a_0=\sum_{j\ge1}\frac{b_j}{j(j+1)},\qquad
a_n=\sum_{j\ge n}\frac{b_j}{j(j+1)}-\frac{b_n}{n}\quad(n\ge1).
$$
Boundedness of $B$ follows from the discrete Hardy inequality applied to the prefix sums and from $n/\sqrt{n(n+1)}\le1$. The inverse is verified by setting $q_n=(a_0+\cdots+a_n)/(n+1)$, so $q_{n-1}-q_n=b_n/[n(n+1)]$ and $q_n\to0$. It is bounded because $b_j/[j(j+1)]=d_j/\sqrt{j(j+1)}$ with $d\in\ell^2$. The tail sum is bounded on $\ell^2$ by a Copson tail plus its diagonal, and $|b_n|/n\le\sqrt2|d_n|$; $a_0$ is bounded by Cauchy–Schwarz.

Writing $\rho_k(x)=\lfloor x/k\rfloor-\lfloor x\rfloor/k$, the coefficient differences of $h_k$ are $(1-k\mathbf1_{k\mid j})/j$ for $j\ge1$. Summation by parts gives $Bh_k=k\rho_k$, and $B1=\mathbf1_{x\ge1}$. For the step Mellin transform $\mathcal M_-(b)(s)=\int_1^\infty b(x)x^{-s-1}dx$, on finite disk sequences the coefficient of $a_0$ is $1/s$ and that of $a_j$ is $((j+1)^{1-s}-j^{1-s})/s$ for $j\ge1$. Density and boundedness extend $\mathcal M_-(Ba)(s)=-\Lambda_s(a)$ to $\Re s>1/2$. Thus $J_\tau=BT_\tau B^{-1}$ is the bounded step operator satisfying
$$
s\,\mathcal M_-(J_\tau b)(s)=(s-i\tau)\mathcal M_-(b)(s-i\tau).
$$
On a sufficiently far right line, $s\mathcal M_-b(s)=\sum_n (b_n-b_{n-1})n^{-s}$, with $b_0=0$. This series converges absolutely there because $b_n=O(n)$ for $b\in S$. Uniqueness of the Dirichlet series proves the exact jump formula
$$
(J_\tau b)_n-(J_\tau b)_{n-1}=n^{i\tau}(b_n-b_{n-1}).
$$
The dictionary is in fact unitary. The image of $e_0$ is the constant 1. For $j\ge1$, the image of $e_j$ is 0 at $n<j$, $-j$ at $n=j$, and 1 at $n>j$. Its squared norm is $j/(j+1)+1/(j+1)=1$. Its pairing with the image of any earlier basis vector is $-1/(j+1)+1/(j+1)=0$. Surjectivity from the inverse formulas gives unitarity. [Independent check and sharp transport norm](adversarial_reviews/witness62_manzur_noor_step_bridge.md)

## Nonprincipal anchor and the resonance condition

For a nonprincipal $\chi$, use $S_\chi(x)=\sum_{n\le x}\chi(n)$, and let $\mathcal V_\chi^0\subset S$ be the closed span of
$$
g_{\chi,k}(x)=S_\chi(x/k)-S_\chi(x)/k,\quad k\ge2.
$$
The Mellin transform is $F(s)(k^{-s}-k^{-1})/s$, with $F=L(s,\chi)$. Bounded partial sums justify Hardy membership. Every element of $\mathcal V_\chi^0$ has $\mathcal M_-(b)(1)=0$, whereas the target $B1$ has value 1. Evaluation here has norm 1, represented by the constant step function. In zeta the apparent zero of $k^{-s}-k^{-1}$ cancels the pole rather than forcing zero evaluation: the generator's value at 1 is $-(\log k)/k$. This is the structural distinction behind the nonprincipal anchor obstruction.

For the transported nonprincipal generator the dictionary gives the exact evaluation
$$
\mathcal M_-(J_\tau g_{\chi,k})(1)
=\frac{F(1-i\tau)}{k}(k^{i\tau}-1).
$$
Classical Dirichlet nonvanishing on $\Re s=1$ and the norm-1 functional imply the unconditional bound
$$
\operatorname{dist}_S(J_\tau g_{\chi,k},\mathcal V_\chi^0)
\ge \frac{|F(1-i\tau)|}{k}|k^{i\tau}-1|.
$$
In particular, the zeta membership criterion does not carry over in its all-$\tau$, some-$k$ form. Outside the countable set $2\pi\mathbb Z/\log k$ for $k\ge2$, it fails for every generator regardless of GRH. In fact, a source-style invariance condition $J_\tau\mathcal V_\chi^0\subseteq\mathcal V_\chi^0$ is impossible for every $\tau\ne0$, since simultaneous resonance for $k=2,3$ contradicts irrationality of $\log2/\log3$.

Under the separately proved unanchored GRH approximation for fixed $\chi$, the unanchored span of $S_\chi(x/k)$, $k\ge1$, is dense in $S$. It contains the target in its closure, and remains closed under integer dilation, which gives all step tails $\mathbf1_{x\ge k}$ and hence all finite-cell vectors by subtraction. Every unanchored finite vector can then be corrected to have evaluation zero by subtracting a multiple of the fixed vector $S_\chi(x)$, whose evaluation is $F(1)\ne0$. The correction tends to zero on a sequence approximating a vector in the evaluation kernel. Consequently $\mathcal V_\chi^0=\ker[\mathcal M_-(\,\cdot\,)(1)]$ in $S$ under GRH. At resonance, the particular $J_\tau g_{\chi,k}$ belongs to this zero-evaluation space under GRH. This does not make the target approximable there. The converse at resonance uses a classical fixed-strip zero count. If the translated generator is in $\mathcal V_\chi^0$, its Mellin transform vanishes at any zero $\rho$ with $\Re\rho>1/2$, since this evaluation is bounded and vanishes on the generators. The transport identity evaluates it there as $F(\rho-i\tau)(k^{-\rho+i\tau}-k^{-1})/\rho$. The second factor is nonzero for $\Re\rho<1$, so a zero propagates vertically in steps of $-\tau$. For fixed modulus $q$ and $1/2<\sigma<\Re\rho$, the classical Montgomery density estimate quoted in Jutila (1.1) bounds the number of zeros in $\Re s\ge\sigma$, $|\Im s|\le T$ by $O_{q,\sigma}(T^{3(1-\sigma)/(2-\sigma)}(\log T)^{14})=o(T)$. It bounds a whole product over characters, hence applies to the given one and both signs. The progression contradicts this count. The functional equation of the inducing primitive character then gives GRH for its nontrivial zeros. This proves a tailored equivalence for each resonant pair $(k,\tau)$ with $\tau\ne0$, while the all-$\tau$ formulation and the invariance formulation fail in the anchored nonprincipal space. [Jutila, Acta Fennica no. 520, §1.1](https://www.acadsci.fi/mathematica/1972/no520pp01-13.pdf) [Fixed-character approximation](adversarial_reviews/director_dirichlet_transfer_round6.md) · [Anchor and Euler factors](adversarial_reviews/director_imprimitive_anchor_round8.md)

## Length obstruction and missing quantitative estimate

Even for zeta, $J_\tau$ fails to preserve finite Dirichlet length. For $\tau\ne0$, the jumps of $J_\tau\rho_k$ are $n^{i\tau}(\mathbf1_{k\mid n}-1/k)$. The formal floor coefficients are unique by divisor inversion. For primes $p\nmid k$ they are
$$
v_p=-\frac{p^{i\tau}-1}{k}.
$$
At most one prime can satisfy $p^{i\tau}=1$, since the logarithms of distinct primes cannot have rational ratio. Infinitely many such coefficients are nonzero. Consequently a transported generator does not lie in any finite length span, although it lies in the closure under RH. The identity gives no length budget for approximating it, much less the prescribed coefficients of an independent approximation to the constant.

The exact arithmetic test needed for the prefix multiplicity question can be stated without Hardy terminology. Under the fixed-$b$ arithmetic identity $L\,d_{N,b}^2\to C(b)$, a sufficient estimate is the existence of fixed fractions $b_j\uparrow1$ and actual admissible arithmetic approximants at each $b_j$ such that
$$
\limsup_{N\to\infty}L\|e_{N,b_j}\|^2\ \le\ \frac{\epsilon_j}{1-b_j},
\qquad\epsilon_j\to0.
$$
No uniformity in $b_j$ at finite $N$ is demanded. The established lower bound $c_m(b)\ge 4/(1-b)$ for $m\ge2$ then makes every multiple-zero weight zero. For this last bound one may use $c_m(b)\ge m^2+m^2(m-1)^2b/(1-b)$. A single exact equality $C(b)=C(0)$ at any fixed $b>0$ would also suffice. The missing input is an upper estimate for length-$N$ actual polynomials with every coefficient through $N^b$ equal to the prescribed taper. Source-level density and boundedness of $T_\tau$ do not give that estimate. [Fixed-prefix arithmetic limit](rstation48_fixed_prefix_lower_skeptic62.md) · [Aggregate and simple-support test](adversarial_reviews/director_prefix_inverse_round8.md)

## Countermodel to an abstract rate inference

Take $\ell^2(\mathbb N)$, the nested first-$N$ coordinate spaces, target $e_1$, and a bounded transport group of diagonal unitaries $T_\tau e_n=n^{i\tau}e_n$. The target and its transported vector belong to every admissible unconstrained space and have exactly zero unconstrained error. Prescribe the first coordinate as 1 and prescribe, for $2\le n\le N^b$,
$$
a_{n,N}=\frac{1}{L\sqrt n(1-\log n/L)},\qquad L=\log N.
$$
This is one prefix rule independent of the fraction used to truncate it. The remaining coordinates can be zero. The optimized constrained squared error is the sum of the imposed squares, and the change of variables $u=\log x/L$ gives
$$
L\,d_{N,b}^2
=\frac1L\sum_{2\le n\le N^b}\frac{1}{n(1-\log n/L)^2}
\longrightarrow \int_0^b\frac{du}{(1-u)^2}=\frac b{1-b}.
$$
For each fixed $b<1$, sum–integral comparison is uniform in $N$, for example by monotonicity of the summand as a function of $x$ once $L(1-b)>2$. Thus exact single-generator membership, density, a norm-1 group, and even perfect unanchored approximation coexist with a non-subreciprocal fixed-fraction limit. This is an obstruction to that abstract inference. It makes no assertion about the specific arithmetic Möbius prefix.
