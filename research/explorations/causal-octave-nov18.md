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
