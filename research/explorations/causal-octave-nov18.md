# A first-octave criterion for the Dickman-corrected source

Proposed analytic observation, 18 November 2026. The source and the Dickman correction are exactly those of [DC1 and DC6](https://github.com/GettysburgResearch/riemann/blob/cdf2f15965decbd35afbbd09a16c89cb3e215737/standalone/2026-09-05-three-route-assault/pass7-dickman-completion/PROOF.md). The only imported number-theoretic conclusion used below is the classical equivalence between RH and the prime-counting error bound of exponent one half with arbitrary positive slack. No original-priority claim is made.

Fix the omitted prime 67, a real cutoff $X\ge67$, and $a>0$. Use $M(y)=\sum_{n\le y,67\nmid n}\mu(n)$ and its restriction $M_X$ to integers whose prime factors are at most $X$. Write $F_a(x)=e^{-ax}M(e^x)$ and define $F_{X,a}$ similarly. Extend them by zero on the negative axis. The corrected source is $G_{X,a}=F_{X,a}-k_{X,a}*F_{X,a}$ with $L=\log X$ and $k_{X,a}(u)=e^{(1-a)u}[-\rho'(u/L)]/L$, where $\rho$ is Dickman's function. These definitions make sense on bounded intervals with no global integrability hypothesis.

Put $E(y)=\pi(y)-\int_2^y dt/\log t$. For $X\le y\le2X$,
$$
y^a(G_{X,a}-F_a)(\log y)=E(y)-E(X).
$$
Indeed an excluded squarefree integer in this interval of summation must itself be a prime greater than $X$: its cofactor would otherwise be at least two. Thus $M_X(y)-M(y)=\pi(y)-\pi(X)$. In the convolution the support restricts $u$ to $[L,\log y]$. Here $-\rho'(u/L)/L=1/u$ almost everywhere by the Dickman delay equation. The residual factor $M_X(ye^{-u})=1$ almost everywhere since its argument lies in $[1,2]$. Multiplication by $y^a$ gives $\int_L^{\log y}e^u du/u$. This proves the identity, including both endpoints and real nonintegral cutoffs.

**Uniform overlap lemma.** Let $D$ be a locally square-integrable real function defined pointwise on $[67,\infty)$. Suppose $b>0$ and for every real $X\ge67$,
$$
\int_X^{2X}|D(y)-D(X)|^2\,dy/y\le A^2 X^{2b}.
$$
For $X\le Z\le3X/2$, use the triangle inequality in $L^2([Z,2X],dy/y)$ on the two increments. The resulting constant function has norm at least $\sqrt{\log(4/3)}|D(Z)-D(X)|$. The upper bound is $A(X^b+Z^b)$. Iterating from 67 in steps of factor $3/2$, followed by a final partial step, gives $D(t)=D(67)+O_b(A t^b)$ by geometric summation. A single fixed sequence of disjoint octaves is outside this proof's hypotheses.

**Consequence.** RH is equivalent to the following property for every fixed $a>1/2$:
$$
\sup_{X\ge67}\|G_{X,a}-F_a\|_{L^2([\log X,\log(2X)],dx)}<\infty .
$$
Indeed bounded norm implies the lemma's hypothesis with $D=E$, $b=a$, since $y^a\le(2X)^a$. Applying this for all $a>1/2$ gives the classical bound. Conversely under RH the classical estimate $E(t)=O(\sqrt t\log t)$ makes the displayed norm $O_a(X^{1/2-a}\log X)$ for large $X$. No estimate outside this octave is required for either implication.

In particular, a proposed unconditional global norm bound at a fixed $a$ on the corrected *difference* must already control these overlapping prime-counting increments. The unresolved source estimate is uniform boundedness of the displayed octave norm for every $a>1/2$. The identity and overlap argument supply no cancellation estimate for those increments.

## Disjoint octaves suffice, even after freely fitting one constant per octave

There is a stronger conclusion for the actual prime source. Fix $1/2<a<1$. Suppose there are real numbers $c_j$, one for each integer $j\ge1$, and a common $B$ such that
$$
\int_{2^j}^{2^{j+1}} |E(y)-c_j|^2\,dy/y\le B^2 2^{2aj}.
$$
Then zeta has no zero in $\Re s>a$. The forward implication uses the classical unconditional zero-density theorem $N(\sigma,T)=o(T)$ for fixed $\sigma>1/2$ (for instance Ingham's density estimate). The same criterion imposed for every $a>1/2$ is consequently equivalent to RH, by the classical conditional prime-counting bound for the converse. One may omit any finite number of blocks.

**Proof.** Let $C(y)=c_j$ on the half-open octave and set $h=2\pi/\log 2$. By Cauchy–Schwarz on each block,
$$
R(s)=s\int_2^\infty (E(y)-C(y))y^{-s}\,dy/y
$$
is holomorphic for $\Re s>a$ by locally uniform absolute convergence. The constants are $O(2^j)$ by the hypothesis and the elementary $E(y)=O(y)$, so the separate transforms converge on $\Re s>1$. Write $Q(s)=s\int_2^\infty E(y)y^{-s}dy/y$. There
$$
Q(s)-R(s)=(1-2^{-s})\sum_{j\ge1}c_j 2^{-js}.
$$
The right-hand side is invariant under $s\mapsto s+ih$. Hence $Q'(s+ih)-Q'(s)$ extends holomorphically to $\Re s>a$, as $R'(s+ih)-R'(s)$.

By integrating each prime step and the continuous main term before differentiating in $\Re s>1$, we have
$$
Q'(s)=\frac{\zeta'}{\zeta}(s)+\sum_{p,k\ge2}^{*}(\log p)p^{-ks}
       +\frac{2^{1-s}}{s-1}.
$$
Here the starred sum ranges over every prime $p$ and every integer $k\ge2$. It converges locally absolutely for $\Re s>1/2$. The rational-exponential term cancels the pole of the logarithmic derivative at 1. Thus the meromorphic continuation of $Q'$ in this half-plane has precisely the zeta zeros as poles, with residues their multiplicities. The identity theorem applied to the derivative difference shows that a zero $\beta+i\gamma$ with $\beta>a$ forces zeros at every $\beta+i(\gamma+mh)$ for positive integers $m$, with the same multiplicity. Their number at heights in $(0,T]$ grows at least as $T/h-O_\gamma(1)$, contradicting $N(\beta,T)=o(T)$. This proves the assertion.

The least-squares choice is the logarithmic average of $E$ on each block. Equivalently one may project the rescaled first-octave residual $y^a(G_{X,a}-F_a)(\log y)$ off constants on dyadic blocks, since the $E(X)$ term vanishes under that projection. This removes every block's unknown level from the target. A sufficient source estimate remains square-root-scale within-block variation on all large dyadic blocks with arbitrary positive exponent slack.

## An unconditional lower bound for the actual dyadic prime error

Let $X_j=2^j$, $L=\log2$, and let $V_j$ be the $L^2([X_j,2X_j],dy/y)$ distance of $E$ from the constants. Then
$$
\limsup_{j\to\infty}\frac{\log X_j}{\sqrt{X_j}}V_j>0.046 .
$$
This constrains the strength of any proposed upper bound after optimal recentering. No zero-free half-plane beyond the classical one is assumed.

To see this, use the lowest positive ordinate $14<\gamma_1<15$ on the critical line, put $z=1/2+i\gamma_1$ and $w=z-ih$ with $h=2\pi/L$. There is no zero at $w$ since $0<\Im w<\gamma_1$. These low-zero facts may be imported from the verified-height census and the classical first-zero enclosure. Write $m\ge1$ for the multiplicity at $z$. For real $\eta>0$ put $s=z+\eta$ and $s'=w+\eta$. The function $Q'(s)-Q'(s')$ has principal part $m/\eta$ at $\eta=0$, by its meromorphic formula above.

Suppose the limsup in the assertion is finite, say $B$. Choose $C(y)$ to be the least-squares block constant. The transform of $E-C$ and its differentiated integral converge in $\Re s>1/2$ under this finite-limsup assumption. The periodic cancellation gives $Q'(s)-Q'(s')=R'(s)-R'(s')$ there as a meromorphic identity; possible individual poles away from the boundary therefore cause no problem in using the difference. On a block write $y=X_j e^u$, $0\le u\le L$. In the difference of the differentiated kernels the term proportional to $\log X_j$ is, up to sign and a common factor $X_j^{-s}$,
$$
(\log X_j) K_\eta(u),\qquad K_\eta(u)=s e^{-su}-s'e^{-s'u}.
$$
The two remaining terms (the derivatives of the prefactors and the terms involving $u$) have uniformly bounded $L^2[0,L]$ norm as $\eta\downarrow0$. For any $b>B$ all sufficiently large blocks have $V_j\le b\sqrt{X_j}/\log X_j$. By Cauchy–Schwarz the leading terms in the difference are bounded by $b\|K_\eta\|_2\sum_j e^{-j\eta L}$. The remainder is $O(\sum_{j\ge1}e^{-j\eta L}/j)$ plus finitely many bounded terms, hence vanishes after multiplication by $\eta$. Taking $\eta\downarrow0$ and then $b\downarrow B$ gives
$$
 B\ge m L/\|K_0\|_2.
$$
Now $\|K_0\|_2\le(|z|+|w|)\sqrt{1-e^{-L}}<21.1/\sqrt2$, using $14<\gamma_1<15$ and $9<h<9.1$ (so $|z|<15.01$ and $|w|<6.03$). Thus $B\ge L\sqrt2/21.1>0.046$. If the limsup is infinite the assertion is immediate. This argument proves a lower bound on a subsequence and makes no assertion that the normalized variance stays bounded.

### Combining independent rotations

One can strengthen $0.046$ to **0.1969** by using prime squares and the first 64 pairs of zeros together. Here is a proof of the simultaneous inequality underlying the computation. Take finitely many points $z_v=1/2+it_v$ for which $e^{it_v L}$ are pairwise distinct. Choose $w_v=z_v-ik_v h$ with nonzero integers $k_v$. Suppose $Q'$ is meromorphic near all of these points, and let $r_v$ be the residue at $z_v$ minus the residue at $w_v$, treating regular points as having residue zero. Assume its poles there are at most simple. Put $K_v(u)=z_v e^{-z_v u}-w_v e^{-w_v u}$. Then
$$
 B^2\ge \sum_v |L r_v|^2/\|K_v\|_2^2 .
$$

For finite $B$ form the real functions $f_j(u)=jL\,2^{-j/2}(E(2^j e^u)-c_j)$ with $c_j$ the fitted mean. Their norms have limsup $B$. Use weights $p_j=(1-e^{-\eta L})e^{-(j-1)\eta L}$ on $j\ge1$. The preceding differentiated-kernel argument, keeping the complex phase and the leading minus sign, yields
$$
 \lim_{\eta\downarrow0}\sum_j p_j e^{-ijt_vL}\int_0^L f_j(u)K_v(u)du=-L r_v .
$$
In detail, the geometric normalization divided by $\eta$ tends to $L$, the terms with $1/(jL)$ vanish in weighted mean, and replacing the shifted kernels by their boundary values costs $o(1)$ since $\sup_j\|f_j\|_2<\infty$. View the sequences $e^{ijt_vL}\overline{K_v}/\|K_v\|_2$ in the direct sum of the complex block spaces with weights $p_j$. Their Gram matrix tends to the identity: for distinct rotations the geometric mean of $e^{ij(t_v-t_w)L}$ tends to zero. Projection onto this finite span, or the finite Gram matrix inequality, bounds the sum of the squared limiting coefficients by $\limsup_{\eta\downarrow0}\sum_jp_j\|f_j\|^2\le B^2$. This proves the claim.

For the computation take $t_v=0$ and both signs of the first 64 positive ordinates. The residue at $1/2$ is $1/2$ from prime squares: the $k=2$ sum differs from $-\zeta'(2s)/\zeta(2s)$ by a series holomorphic near $\Re s=1/2$. All higher powers converge there. Away from $t=0$ on this line $\zeta(2s)$ has no zeros or poles by the classical nonvanishing theorem on the one-line. Thus the other selected points have residues at least one. The translated points all have nonzero ordinate of absolute value below 14 and are regular. The rotations are certified distinct by complex ball arithmetic. For $\Delta=k_vh$, the exact norm is
$$
 \|K_v\|^2=(|z_v|^2+|w_v|^2)/2-\Re\big[z_v\bar w_v/(1+i\Delta)\big].
$$
The script uses Arb enclosures for indexed zeta zeros and tests all these predicates with 128-bit precision. Running it under python-flint 0.9.0 yields a lower bound expression enclosed in $0.196979277039101672326354616605373432\pm1.16\cdot10^{-37}$. The bound on $B$ uses the lower endpoint of that enclosure. [Reproduction script](check_octave_nov18.py)
