# The finite prefix-cost germ determines the multiplicity weights

Let $W_m\ge0$ for integers $m\ge1$, and assume $W_1<\infty$ and
$$
\sum_{m\ge2}W_m e^{\eta m}<\infty
$$
for some $\eta>0$. For the zeta specialization, $W_m$ is the sum of $|\rho|^{-2}$ over distinct critical-line zeros of order $m$. Set $C(b)=\sum_m W_m c_m(b)$ using the exact finite moment cost. The Taylor germ of $C$ at zero determines every $W_m$. The statements here concern this zero sum and the finite cost only. [Finite cost derivation](../prefix_formula62_finite_cost.md)

## Exact coefficients and their triangular recovery

Write $\mu=m(m-1)$ and $s=b/(1-b)$. The finite identity is
$$
c_m(b)=m^2+\int_0^s G_m(u)^2\,du,\qquad
G_m(u)=2P_{m-1}'(1+2u)=\sum_{j\ge0}A_j(\mu)u^j,
$$
where
$$
A_j(\mu)=\frac{\prod_{\ell=0}^j[\mu-\ell(\ell+1)]}{j!(j+1)!}.
$$
Indeed, differentiating $P_{m-1}(1+2u)=\sum_{i=0}^{m-1}\binom{m-1}{i}\binom{m-1+i}{i}u^i$ gives the product identity after pairing factors $(m-1-\ell)(m+\ell)$. For $m\ge2$ these coefficients are positive for $j\le m-2$ and vanish for $j\ge m-1$. For $m=1$ they all vanish and $c_1(b)=1$.

For $k\ge1$ put $T_k(\mu)=[b^k](c_m(b)-m^2)$. Expanding $(b/(1-b))^\ell$ gives the exact polynomial
$$
T_k(\mu)=\sum_{\ell=1}^k\frac{\binom{k-1}{\ell-1}}{\ell}
            \sum_{i+j=\ell-1}A_i(\mu)A_j(\mu).
$$
It is divisible by $\mu^2$. The $\ell$th inner sum has degree $\ell+1$, so the leading coefficient of $T_k$ comes only from $\ell=k$. It is
$$
\frac1k\sum_{i+j=k-1}\frac1{i!(i+1)!j!(j+1)!}
=\frac{\binom{2k}{k}}{k!(k+1)!}.
$$
The last step is Vandermonde's identity on $\binom{k-1}{i}\binom{k+1}{i+1}$. In particular $T_1=\mu^2$ and $T_2=\mu^3/2$. If $T_k/\mu^2=\sum_{j=0}^{k-1}t_{k,j}\mu^j$ and
$$
M_j=\sum_{m\ge2}W_m\mu_m^2\mu_m^j,\qquad \mu_m=m(m-1),
$$
then $[b^k]C=\sum_{j=0}^{k-1}t_{k,j}M_j$ with nonzero last coefficient. This gives the moments $M_j$ recursively from the germ.

## Justifying the germ and its exact radius

For actual integer $m$ all nonconstant Taylor coefficients of $c_m$ in $b$ are nonnegative, by the displayed integral and substitution. In particular $|c_m(b)|\le c_m(|b|)$ for $|b|<1$. For $r\in(0,1)$ and $S=r/(1-r)$, use $A_j(\mu)\le\mu^{j+1}/(j!(j+1)!)$ and $\sum_{j\ge0}x^j/(j!)^2\le e^{2\sqrt x}$ for $x\ge0$. The latter series is dominated by the diagonal part of $(\sum_{j\ge0}(\sqrt x)^j/j!)^2$. It follows that
$$
c_m(r)\le m^2+S\mu_m^2 e^{4\sqrt{\mu_m S}}.
$$
Choose $r>0$ sufficiently small that $4\sqrt S<\eta$. Polynomial factors are absorbed by the strict exponent gap, so summation is uniformly absolutely convergent on $|b|\le r$. Termwise coefficient extraction there is legitimate. If every exponential moment in $m$ is finite the same argument applies for every $r<1$.

There is also a sharp radius criterion for general nonnegative weights. Assume only $\sum_m m^2W_m<\infty$, and put
$$
\eta_*=-\log\!\left(\limsup_{m\to\infty}W_m^{1/m}\right)\in[0,\infty],
$$
where $-\log0=\infty$. If some $W_m>0$ for $m\ge2$, then the Taylor radius of the zero sum is
$$
r_*=\tanh^2(\eta_*/4)
$$
with the conventions $r_*=0$ for $\eta_*=0$ and $r_*=1$ for $\eta_*=\infty$. When $\eta_*=0$ this means there is no positive convergence disk. If each coefficient is finite, the formal power series then has radius zero. If all nonsimple weights vanish the function is constant and entire.

To prove the radius statement, set $a=(1+r)/(1-r)$ and $\rho_r=a+\sqrt{a^2-1}=(1+\sqrt r)/(1-\sqrt r)$. The ordinary integral representation of $P_n(a)$ shows $P_n(a)^{1/n}\to\rho_r$. The integrand base reaches its maximum at zero, and a fixed small neighborhood gives a matching root lower bound as that neighborhood shrinks. Cauchy–Schwarz gives
$$
\int_1^a P_n'(x)^2dx\ge [P_n(a)-1]^2/(a-1).
$$
For the reverse growth bound $P_n'(x)$ is increasing on $[1,a]$ from the nonnegative expansion at one. Differentiating the integral representation at the fixed $a>1$ gives $|P_n'(a)|\le n(1+a/\sqrt{a^2-1})\rho_r^{n-1}$. Thus $c_m(r)^{1/m}\to\rho_r^2$. The root test decides $\sum_mW_mc_m(r)$ strictly on each side of $2\log\rho_r=\eta_*$. Nonnegative coefficients and Tonelli identify the sum at real $r$ with evaluation of its Taylor series whenever finite, and show convergence fails above the threshold. At $r=1$, any single nonsimple summand diverges, since $G_m(0)=m(m-1)>0$ and $G_m(u)\ge G_m(0)$ for $u\ge0$. This covers the $\eta_*=\infty$ upper endpoint. The root test does not decide convergence at an intermediate threshold. The stronger fixed-$r$ asymptotic in the finite cost derivation does give an endpoint criterion if desired. When $0<\eta_*<\infty$, the positive factor in $c_m(r_*)\sim K(r_*)e^{\eta_*m}$ gives equivalence to $\sum_mW_m e^{\eta_* m}<\infty$. In particular, subject to finite $C(0)$, the existence of a local analytic zero-sum germ is equivalent to some positive exponential moment in $m$.

## Determinacy and direct reconstruction

The positive measure $\nu=\sum_{m\ge2}W_m\mu_m^2\delta_{\mu_m}$ has moments $M_j$. It has a positive exponential moment in $\sqrt\mu$: for every sufficiently small $\kappa>0$,
$$
\int e^{\kappa\sqrt x}\,d\nu(x)
\le\sum_{m\ge2} W_m m^4e^{\kappa m}<\infty.
$$
Symmetrize its square-root pushforward as $\widetilde\nu=\tfrac12\sum_{m\ge2}W_m\mu_m^2(\delta_{\sqrt{\mu_m}}+\delta_{-\sqrt{\mu_m}})$. Its odd moments vanish and its even moments are $M_j$. Its moment generating function is holomorphic on $|\Re z|<\kappa$ and has Taylor series $\sum_j M_j z^{2j}/(2j)!$ near zero. Thus the germ determines its Fourier transform by continuation along the imaginary axis. Fourier uniqueness gives $\widetilde\nu$ and hence $\nu$. This also proves the usual Stieltjes determinacy against possible measures without a supplied exponential moment. Any competing nonnegative measure with the same moments has the same finite $\int\cosh(\kappa'\sqrt{x})$ for $0<\kappa'<\kappa$, by monotone termwise summation, and therefore has the required exponential moment.

For an explicit exact recovery, for any $y=\sqrt{\mu_m}>0$,
$$
\widetilde\nu(\{y\})=
\lim_{T\to\infty}\frac1{2T}\int_{-T}^T
      \widehat{\widetilde\nu}(t)e^{-ity}\,dt,
\qquad \widehat{\widetilde\nu}(t)=\int e^{itx}\,d\widetilde\nu(x).
$$
This follows by dominated convergence on the resulting bounded sinc kernel. The support points are distinct, so $W_m=2\widetilde\nu(\{\sqrt{\mu_m}\})/\mu_m^2$ for $m\ge2$. Finally $W_1=C(0)-\sum_{m\ge2}m^2W_m$. The reconstruction uses the exact infinite germ and gives no stability claim for a finite or noisy coefficient list.

## Zeta specialization

Let $m_\rho$ denote the order of a zeta zero on the line. The Riemann–von Mangoldt count gives $O(T\log T)$ zeros with multiplicity up to height $T$. Its classical local count gives $m_\rho=O(\log(2+|\Im\rho|))$ unconditionally. In a dyadic block $2^j\le|\Im\rho|<2^{j+1}$ the total weighted exponential contribution is therefore
$$
O\!\left((1+j)2^{-j}2^{M\eta(j+1)}\right)
$$
if $m_\rho\le M\log(2+|\Im\rho|)$ with $M$ enlarged to cover the fixed thresholds. Thus there is a positive exponential moment for $\eta$ sufficiently small, and a nontrivial disk of convergence and unique reconstruction unconditionally. On RH one can use the classical Littlewood bound $S(T)=O(\log T/\log\log T)$ in the counting formula. Taking the jump at a zero gives $m_\rho=o(\log|\Im\rho|)$. Then the preceding dyadic argument works for every $\eta>0$, using a sufficiently small coefficient of $\log T$ at large heights. This gives analyticity on $|b|<1$. The same abstract conclusion holds for any zero family satisfying these counting and multiplicity inputs. [Classical bounds and discussion](../../sources/soundararajan_round4/sound0705v2.txt)

No conclusion is drawn here that $C(b)$ equals an arithmetic prefix-distance limit. That identification requires its own theorem and hypotheses.

## Finite and inexact data

For every integer $K\ge0$, there are distinct nonnegative, finitely supported weight sequences with the same $C(0)$ and the same first $K$ nonconstant Taylor coefficients. Put $\mu_i=m_i(m_i-1)$ with $m_i=2,\ldots,K+2$, and set
$$
a_i=\frac{1}{\prod_{j\ne i}(\mu_i-\mu_j)}.
$$
Comparing leading coefficients in Lagrange interpolation gives $\sum_i a_i\mu_i^j=0$ for $0\le j<K$. There are $K+1$ distinct sites, so these are precisely the powers strictly below the degree of the top Lagrange coefficient. For $K=0$ the product is empty and there are no moment conditions. Define
$$
W_{m_i}^{+}=\frac{\max(a_i,0)}{\mu_i^2},
\qquad
W_{m_i}^{-}=\frac{\max(-a_i,0)}{\mu_i^2}.
$$
All other nonsimple weights are zero. Their measures $\nu^\pm$ have the same moments up to degree $K-1$. By the triangular formula, the first $K$ nonconstant coefficients agree. If $S^\pm=\sum_{m\ge2}m^2W_m^\pm$, choose any $A\ge\max(S^+,S^-)$ and set $W_1^\pm=A-S^\pm$. This preserves nonnegativity and matches $C(0)=A$. To match a prescribed $A>0$, first rescale all the $a_i$ by a sufficiently small positive common factor. At least one $a_i$ is nonzero, so the two profiles differ. For the displayed unscaled weights, interpolation at degree $K$ gives $\sum_i a_i\mu_i^K=1$, so their $(K+1)$st coefficients differ by the positive diagonal coefficient of $T_{K+1}/\mu^2$. This counterexample concerns abstract nonnegative profiles. It does not assert the existence of two realizable zeta-zero multisets of these types.

This is a failure of injectivity of the finite-jet map over the whole class. Particular jets can still decide a property exactly. For example, $C'(0)=\sum_{m\ge2}W_m\mu_m^2=0$ forces every nonsimple weight to vanish. In contrast, data with positive error tolerance on any fixed closed disk $|b|\le r<1$ cannot by themselves distinguish every simple-only profile from nonsimple ones. Fix a constant target $A>0$, set $W_2=\delta$ and $W_1=A-4\delta$ with $0<\delta<A/4$, and take all remaining weights zero. Then $C(0)=A$ and
$$
\sup_{|b|\le r}|C(b)-A|
=\delta\sup_{|b|\le r}|c_2(b)-4|
=\frac{4\delta r}{1-r}.
$$
It can be made smaller than any prescribed positive error. The same holds for a real compact interval of fractions. Thus the recovery result is an exact infinite-data uniqueness statement. It recovers the totals $W_m$ only. It gives no individual zero ordinates or stable finite-data algorithm.

If separately established pointwise fixed-fraction limits identify $C(b)$ with the scaled arithmetic prefix distance, one must first take the limit at fixed $b$, then extract derivatives from the limiting function. For fixed $N>1$ the arithmetic constraint set changes only at $b=\log n/\log N$. The finite-$N$ objective is therefore piecewise constant in the fraction and has derivative zero almost everywhere between thresholds. Even uniform convergence of such staircases does not justify differentiating before taking the limit. For example $C(\lfloor Nb\rfloor/N)$ converges uniformly to $C(b)$ on every fixed $[0,r]$ with $r$ inside its analytic domain, by uniform continuity, and each such staircase has derivative zero away from its thresholds. The analytic limit can have nonzero derivative. This does not give a moving-prefix theorem.

## Bounded antecedent check

I compared rStation 47 v1's logarithmic-prefix criterion, rStation 48 v2 §8.1 and its finite cost (80), de Roton's multiplicity-weighted lower theorem, and Dimitrov–Oliveira's discrete finite interpolation statements. Their inspected passages concern different statements. The closest prefix antecedent gives the forward cost, while the latter works give multiplicity lower bounds or interpolation constraints and do not identify the inverse germ in those passages. A targeted search using combinations of Nyman–Beurling, fixed Möbius prefix, multiplicity moments, Legendre, and Stieltjes mostly recovered those forward sources. The inspection does not cover rStation 16 v2 or 33 v1, which rStation 47 cites for different finite coefficient reconstructions and whose version pages were inaccessible in this search. There is no publication priority conclusion. [rStation 47 v1](../../sources/ratio62_rstation48/rstation_47_v1.md) · [rStation 48 v2](../../sources/ratio62_q1_priority/rstation_48_v2.md) · [de Roton](../../sources/prefix_formula62_generalL/deroton_lower.pdf) · [Dimitrov–Oliveira](../../sources/ratio62_rstation48/dimitrov_oliveira.pdf)

The determinacy input itself is classical. The positive exponential moment in $\sqrt x$ is Hardy's criterion for the Stieltjes problem. Stoyanov–Lin, *Hardy’s condition in the moment problem for probability distributions*, restate the criterion as Theorem 1 and discuss the Hardy 1917–1918 antecedents. The proof above supplies this input directly by square-root symmetrization and Fourier uniqueness. The Vandermonde obstruction is the elementary finite-interpolation argument displayed here. The prefix inverse calculation lies in the triangular map from the stated cost coefficients to the moment sequence. [Stoyanov–Lin, Theorem 1](https://www.mathnet.ru/links/0461aa5874852d6299a01f05abdd0c5e/tvp4485.pdf)
