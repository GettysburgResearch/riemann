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
