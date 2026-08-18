**Explicit status.** $$\boxed{\text{The Riemann Hypothesis remains unproved.}}$$

# Frozen genealogy, reconstruction rule, and result

The mathematical base is PR #566 at exact commit $$\texttt{2407b4ffe5024a2e3898922cf0b722d5cf69e496}.$$ The two mandatory adversarial inputs are PR #574 at $$\texttt{74fba7f3e55fa9a53d1eb814e5067f5011ef5e86}$$ and PR #575 at $$\texttt{265c481ebd02807ab7d9a95cb0cf905a22c1876f}.$$ All three hashes are frozen. Same-numbered repository claims are provenance only and are not counted as independent confirmation.

The reconstruction rule is the following. For each arrow we record what the preceding statement proves, what the next arrow needs, and whether the coordinates, orientation, source measure, quantifiers and normalization coincide. A retained computation is accepted only at the contract checked by its code and proof object. A local determinant sign is not silently promoted to a global Hall theorem, a scalar identity is not promoted to row positivity, and an unsigned source identity is not promoted to a parity-observed native identity.

<div id="thm:main" class="theorem">

**Theorem 1** (Corrected main theorem). *The completed-parity factor–67 route reduces exactly to the uniform scalar Lorenz inequality $\mathrm{CPSL}_{67}$ of Definition <a href="#def:cpsl" data-reference-type="ref" data-reference="def:cpsl">8</a>. More precisely, $$\mathrm{CPSL}_{67}\Longrightarrow R_X\ge0\ \text{for all sufficiently large real }X
\Longrightarrow \mathrm{RH}.$$ The second implication is proved unconditionally in this paper. The first implication is finite-dimensional at each $X$ and its primal and dual are explicit. Uniform $\mathrm{CPSL}_{67}$ is not proved.*

</div>

The theorem identifies where the zero-free-strip strength lives: it is not in the finite owner ledger, local MPFR terminal certificate, Cauchy–Binet propagation, or Mellin algebra. It is in the all-endpoint global Lorenz inequality.

# Notation

Let $\mu$ be the Möbius function, and put $$P_{61}=\prod_{p\le61}p.$$ For $u>0$ and an integer $m\ge1$ define the logarithmic hinge $$h_m(u)=\frac1{\sqrt m}\log\frac um\,\mathbf 1_{u\ge m}.$$ The project uses two kinds of parity. Arithmetic parity is the sign $\mu(k)$ of a squarefree source index. Channel parity is represented by an ordered positive pair $(E,O)$ and the swap $$\mathsf S(E,O)=(O,E).$$ Signed observation is $$\mathcal O(E,O)=E-O.$$ Thus $\mathcal O(\mathsf S^hP)=(-1)^h\mathcal O(P)$.

For a finite family of positive atoms, target coordinates are denoted $t_i>0$ and scalar coordinates $r_i$. These letters never denote a physical component row unless explicitly stated.

| Symbol                       | Meaning                                                      |
|:-----------------------------|:-------------------------------------------------------------|
| $Q_Y(j)$                     | canonical logarithmic parabolic component row                |
| $c_X(j)$                     | full native Möbius row $\sum_k\mu(k)k^{-1/2}Q_{X/k}(j)$      |
| $Q_*(Y)$                     | unsieved scalar packet $5Q_Y(2)+3Q_Y(3)$                     |
| $R_X$                        | native scalar $5c_X(2)+3c_X(3)$                              |
| $r=p^{-1/2}$                 | rough-prime scale coefficient                                |
| $\lambda=r$ and $\alpha=r^2$ | one-prime specialization of the predecessor’s causal weights |
| $\delta_p=r-2r^2$            | missing native parity compensation in the $\alpha$ recursion |
| $\Phi_X$                     | completed-parity scalar Lorenz envelope                      |
| $\mathrm{CPSL}_{67}$         | uniform all-endpoint scalar Lorenz feasibility               |

# Canonical rows and the unique positive scalar

For $j\ge2$ put $$A_j=\frac{j+1}{j-1},\qquad
B_j=\frac{(j+1)(j-2)}{j(j-1)},\qquad
C_j=\frac2{j(j-1)}.$$ Define $$\label{eq:Q}
Q_Y(j)=A_jh_j(Y)-B_jh_{j+1}(Y)+C_j\sum_{m\ge j+2}h_m(Y).$$ The sum is finite. A hinge vanishes at its activation point, so $Q_Y(j)$ is continuous on $(0,\infty)$ and affine in $\log Y$ on every open activation cell. The left and right limits at every integer knot equal the value at the knot.

The full native row is $$\label{eq:crow}
c_X(j)=\sum_{k\ge1}\frac{\mu(k)}{\sqrt k}Q_{X/k}(j).$$ For each real $X$ this is finite. The same hinge argument proves continuity at every source-activation point $X=km$; no integer-only interpolation is needed.

For rows two and three, $$Q_Y(2)=3h_2(Y)+\sum_{m\ge4}h_m(Y),$$ $$Q_Y(3)=2h_3(Y)-\frac23h_4(Y)+\frac13\sum_{m\ge5}h_m(Y).$$

<div id="lem:qstar" class="lemma">

**Lemma 2** (Positive $5{:}3$ dictionary). *Put $$Q_*(Y)=5Q_Y(2)+3Q_Y(3).$$ Then $$Q_*(Y)=\sum_{m\ge1}\frac{q_*(m)}{\sqrt m}\log(Y/m)_+,$$ where $$q_*(1)=0,\quad q_*(2)=15,\quad q_*(3)=6,\quad q_*(4)=3,
\quad q_*(m)=6\ (m\ge5).$$ In particular every unsieved scalar atom is nonnegative.*

</div>

<div class="proof">

*Proof.* Substitute the two displayed row dictionaries. At $m=2,3,4$ the coefficients are respectively $15,6,5-2=3$; from $m=5$ onward they are $5+1=6$. ◻

</div>

Define $$\label{eq:R}
R_X=5c_X(2)+3c_X(3)
    =\sum_{k\ge1}\frac{\mu(k)}{\sqrt k}Q_*(X/k).$$ Finite Dirichlet convolution gives $$\label{eq:astar}
a_*(n)=6\mathbf 1_{n=1}-6\mu(n)
+9\mathbf 1_{2\mid n}\mu(n/2)-3\mathbf 1_{4\mid n}\mu(n/4)$$ and $$R_X=\sum_{n\le X}\frac{a_*(n)}{\sqrt n}\log(X/n).$$

# The completed owner and parity ledger

Every squarefree source index has a unique decomposition $$\label{eq:factor}
k=d p_1\cdots p_t,
\qquad d\mid P_{61},
\qquad67\le p_1<\cdots<p_t.$$ The ordered tuple $h(k)=(p_1,\ldots,p_t)$ is the rough history. Moving one rough prime from the source index to the history sends $(X,k)$ to $(X/p,k/p)$ and satisfies $$\label{eq:activation}
\frac{X/p}{k/p}=\frac Xk,
\qquad
p^{-1/2}(k/p)^{-1/2}=k^{-1/2}.$$ It also swaps the parity channels once. Therefore a source occurrence retains the exact activation $X/k$, coefficient magnitude $k^{-1/2}$, and sign $$\mu(d)(-1)^t=\mu(k).$$ At fixed $X$, $t\le\lfloor\log X/\log67\rfloor$, so the completed history expansion is finite. Grouping all $d\mid P_{61}$ colors acts diagonally on the two parity channels and commutes with $\mathsf S$; the $5{:}3$ scalar does not erase the accumulated character.

This proves source provenance. It does not make a swapped terminal packet positive.

# The exact coefficient delta omitted by the parity-resummed source claim

The predecessor uses, for one rough prime, $$r=p^{-1/2},\qquad s=1-r,\qquad \lambda=r,
\qquad\alpha=r\lambda=r^2.$$ Its unsigned packet identity is $$\label{eq:unsigned}
P=sP+\lambda(P-rC)+\alpha C.$$ Equation <a href="#eq:unsigned" data-reference-type="eqref" data-reference="eq:unsigned">[eq:unsigned]</a> is correct as an unsigned linear identity. The next step of the proof, however, needs the parity-observed native source.

<div id="prop:delta" class="proposition">

**Proposition 3** (One-prime conservation audit). *The native paired one-prime occurrence is $(P,rC)$, whose signed observation is $P-rC$. If the causal current is represented positively and the $\alpha$ child is recursed in the swapped channel, then the current and recursive child account for odd coefficient $2r^2$, not $r$. The exact missing compensation is $$\boxed{\delta_p=r-2r^2=r(1-2r)>0.}$$*

</div>

<div class="proof">

*Proof.* Represent the causal difference by the positive pair $(P,rC)$. The current part is $$s(P,0)+\lambda(P,rC)=(P,\lambda rC)=(P,\alpha C).$$ The swapped recursive child contributes another $(0,\alpha C)$. Hence the total odd coefficient is $2\alpha=2r^2$. Subtracting from the native coefficient $r$ gives the formula. Since $p\ge67$, $r<1/2$. ◻

</div>

At $p=67$, the compensation is approximately $0.0923$, whereas $\alpha\approx0.0149$. Thus it is not a negligible terminal correction. A completed proof must specify its source atoms, target mass, scalar or row coordinates, barycenter, owner, and interaction with every other reserve. The eleven-line statement called “reserve-preserving grouped Hall” in the predecessor does not do this.

# A valid narrow positivity theorem

The preceding obstruction concerns the native parity ledger. One local scalar fact does survive and is useful as a firewall against overstatement.

<div id="lem:localcausal" class="lemma">

**Lemma 4** (Unsieved one-prime scalar causal positivity). *For every prime $p\ge67$ and every $Y\ge p$, $$Q_*(Y)-p^{-1/2}Q_*(Y/p)\ge0.$$*

</div>

<div class="proof">

*Proof.* At source indices not divisible by $p$, the difference retains the positive coefficient $q_*(n)$. At $n=pm$ the only nonzero coefficient changes are $6,-9,0,3$ for $m=1,2,3,4$. With $y=Y/p$, their contribution times $\sqrt p$ is $$b(y)=6\log y-\frac9{\sqrt2}\log(y/2)_+
+\frac32\log(y/4)_+.$$ It is $6\log y$ on $[1,2]$. On $[2,4]$ it is affine in $\log y$ with negative slope and positive terminal value $(12-9/\sqrt2)\log2$. On $[4,\infty)$ its slope is $15/2-9/\sqrt2>0$. Thus $b\ge0$. ◻

</div>

This lemma neither survives arbitrary signed $P_{61}$ convolution nor supplies the missing compensation of Proposition <a href="#prop:delta" data-reference-type="ref" data-reference="prop:delta">3</a>. It is not a proof of the global producer.

# What the directed terminal certificate actually proves

The terminal computer-assisted theorem is local. For canonical even orientation, $p\ge67$, $1\le y<67$, and rows $2\le j\le66$, it studies the complete grouped $P_{61}$ terminal source. A target-exact leftmost even submeasure is compared with odd demand. The compact proof owns $py<166000$; the MPFR proof owns $py\ge166000$ and reports a strict determinant lower bound $$26.7858198871370094575061.$$ The MPFR implementation uses 256-bit downward and upward rounding for primitive square roots and logarithms, integer event ordering, and outward interval arithmetic. The retained campaign contains $51{,}118{,}080$ event records. The splice point $py=166000$ belongs only to the tail.

At its stated scope, the certificate proves canonical-orientation target and row margins for the complete grouped color family. It does not prove any of the following:

1.  that an odd-history leaf has the canonical orientation;

2.  that other histories globally compensate a reversed target deficit;

3.  that the compensation source in Proposition <a href="#prop:delta" data-reference-type="ref" data-reference="prop:delta">3</a> has a Hall owner;

4.  that scalar exactness gives nonnegative rows;

5.  that local determinant signs imply global target-prefix capacity.

These are composition questions, not numerical margins.

# The binding odd-history witness

Take $$X=67\cdot71\cdot13=61841,
\qquad h=(67),
\qquad(p,y)=(71,13).$$ For each active $d\mid P_{61}$ define $$t_d=d^{-1/2}\left[T(923/d)-71^{-1/2}T(13/d)\right],
\qquad T(u)=(4\sqrt u-3)\mathbf 1_{u\ge1}.$$ There are $239$ active divisors. Independent 80-digit reconstruction gives $$E_T=238.236769968802241851178078781701\ldots,$$ $$O_T=221.231683430583189260479623028094\ldots,$$ and hence $$\label{eq:oddgap}
\boxed{E_T-O_T=17.005086538219052590698455753606\ldots>17.}$$ The incoming history has odd length. Actual even capacity is therefore $O_T$ and actual odd demand is $E_T$. Leafwise exact-target Hall is impossible.

Other histories might pay the deficit. Proving that they always do is exactly the global capacity theorem; it cannot be inferred from the local terminal certificate.

# Why TP2 and scalar exactness do not repair the gap

## Cauchy–Binet transports minors, not capacity

Let $H$ be terminal-by-source owner incidence and let $K$ be terminal-by-feature. The correct source-feature matrix is $M=H^{\mathsf T}K$. Ordering sources by owner makes the relevant incidence minors nonnegative. Cauchy–Binet then transports $2\times2$ determinant signs.

This does not imply Hall. The exact finite countermodel $$H=I_2,
\qquad K=\begin{pmatrix}1&1\\2&4\end{pmatrix}$$ has positive entries and positive determinant, but if row one is even supply and row two odd demand, target capacity is $1<2$. No coefficient $0\le u\le1$ can match the target. Thus checkerboard/TP2 is not global Lorenz dominance.

## The scalar-to-row normalization error

Define $$\rho(Y)=\frac{Q_Y(3)}{Q_Y(2)}\qquad(Y>2).$$

<div id="lem:rho" class="lemma">

**Lemma 5** (Terminal row ratio). *The function $\rho$ is nondecreasing on $(2,\infty)$ and strictly increasing on $(3,\infty)$.*

</div>

<div class="proof">

*Proof.* For $2<Y\le3$, $Q_Y(3)=0$. For $3<Y<4$, direct differentiation gives the sign $\log(3/2)>0$. For $Y\ge4$ the infinite tails cancel: $$3Q_Y(3)-Q_Y(2)=3D(Y),
\quad D(Y)=2h_3(Y)-h_4(Y)-h_2(Y)=A\log Y-B,$$ where $$A=\frac2{\sqrt3}-\frac12-\frac1{\sqrt2}<0,
\quad
B=\frac{2\log3}{\sqrt3}-\left(1+\frac1{\sqrt2}\right)\log2>0.$$ On a cell $N\le Y<N+1$, write $Q_Y(2)=S_N\log Y-T_N$ with $S_N,T_N>0$. Then $$\rho'(Y)=\frac{BS_N-AT_N}{YQ_Y(2)^2}>0.$$ Continuity at knots completes the proof. ◻

</div>

Row-two exactness is compatible with Lemma <a href="#lem:rho" data-reference-type="ref" data-reference="lem:rho">5</a>. Scalar exactness is not.

<div id="prop:tradeoff" class="proposition">

**Proposition 6** (Exact scalar tradeoff). *Let $Y_e\ge Y_o>2$, $q_i=Q_{Y_i}(2)$ and $\rho_i=\rho(Y_i)$. If $u$ is chosen by $5{:}3$ scalar exactness $$uq_e(5+3\rho_e)=bq_o(5+3\rho_o),$$ then $$\Delta_2=-\frac{3bq_o(\rho_e-\rho_o)}{5+3\rho_e}\le0,$$ $$\Delta_3=\frac{5bq_o(\rho_e-\rho_o)}{5+3\rho_e}\ge0,
\qquad5\Delta_2+3\Delta_3=0.$$ For $Y_e>Y_o>3$, both inequalities are strict.*

</div>

Hence a scalar coupling may be valid for the direct scalar Mellin consumer, but it cannot be promoted to the row-valued terminal theorem. A proof must choose one state space and stay in it.

# The exact completed-parity scalar Lorenz problem

We now formulate the strongest state space compatible with the direct scalar consumer.

Fix real $X$. Expand the literal squarefree source completely and retain cumulative parity. Equivalently, index the even atoms by squarefree $k$ with $\mu(k)=1$ and the odd atoms by $\mu(k)=-1$. Give an atom its positive coefficient $k^{-1/2}$, the project target $$t_X(k)=\frac1{\sqrt k}T(X/k),$$ and scalar $$r_X(k)=\frac1{\sqrt k}Q_*(X/k)\ge0.$$ The owner tree is a provenance partition of this finite set; it does not alter these coordinates.

Let $a_i$ be the available even coefficient after any literal source restriction, and let $T_O,R_O$ be total odd target and scalar demand. A scalar common-source coupling is a vector $u$ satisfying $$\label{eq:lp}
0\le u_i\le a_i,
\qquad\sum_i t_i u_i=T_O,
\qquad\sum_i r_i u_i\ge R_O.$$ Residual even atoms are scalar-nonnegative, so <a href="#eq:lp" data-reference-type="eqref" data-reference="eq:lp">[eq:lp]</a> implies $R_X\ge0$.

<div id="thm:lorenz" class="theorem">

**Theorem 7** (Finite Lorenz primal and dual). *Define $$\Phi_X(T)=\max\left\{\sum_i r_i u_i:
0\le u_i\le a_i,\ \sum_i t_i u_i=T\right\}.$$ Then <a href="#eq:lp" data-reference-type="eqref" data-reference="eq:lp">[eq:lp]</a> is feasible if and only if $$T_O\le\sum_i a_it_i,
\qquad R_O\le\Phi_X(T_O).$$ If $\theta_i=r_i/t_i$ are arranged in decreasing order, $\Phi_X$ is the fractional-knapsack Lorenz curve and has at most one fractional atom. Its exact dual is $$\label{eq:dual}
\boxed{
\Phi_X(T)=\min_{\lambda\in\mathbb R}
\left[\lambda T+\sum_i a_i(r_i-\lambda t_i)_+\right].}$$*

</div>

<div class="proof">

*Proof.* If two non-boundary coefficients satisfy $\theta_i>\theta_j$, transferring a small fixed amount of target from $j$ to $i$ increases the scalar objective. Therefore every optimizer saturates larger ratios before smaller ratios. This proves the primal formula. Weak duality for <a href="#eq:dual" data-reference-type="eqref" data-reference="eq:dual">[eq:dual]</a> is immediate; equality holds at a threshold equal to the ratio of the fractional atom. ◻

</div>

<div id="def:cpsl" class="definition">

**Definition 8** (Completed-parity scalar Lorenz theorem). *$\mathrm{CPSL}_{67}$ is the assertion that the inequalities of Theorem <a href="#thm:lorenz" data-reference-type="ref" data-reference="thm:lorenz">7</a> hold for the literal completed-parity factor–67 source at every sufficiently large real endpoint $X$, including all open activation cells and both one-sided knot limits.*

</div>

The one-dimensional dual makes the next research step fail-closed. If $\mathrm{CPSL}_{67}$ is false at a finite endpoint, an optimizing $\lambda$ is an exact separating witness. If it is true uniformly, it proves the scalar needed for Mellin–Landau. The finite directed terminal theorem, TP2, and ratio monotonicity are useful ingredients but do not prove it.

# The predecessor’s $g\ge Tg$ claim in the correct state space

Let $T$ be a positive nilpotent operator on a finite ordered vector space. The abstract identity $$F+TF=g$$ and inequality $g\ge Tg$ imply $$F=(I-T^2)^{-1}(g-Tg)\ge0.$$ This algebra is exact.

The composition gap is prior to the algebra. To apply it one must define:

1.  the literal source atoms represented by each component of $g$;

2.  the child coefficients represented by $T$;

3.  the compensation atoms of Proposition <a href="#prop:delta" data-reference-type="ref" data-reference="prop:delta">3</a>;

4.  an atomwise conservation identity whose root signed observation is exactly $R_X$;

5.  a proof of $g-Tg\ge0$ in the same target-plus-scalar or row-valued state.

The predecessor does not provide these definitions. Its $g\ge Tg$ sentence is a restatement of the missing global coupling, not a consequence of the local Hall certificate.

If the state is row-valued, Proposition <a href="#prop:tradeoff" data-reference-type="ref" data-reference="prop:tradeoff">6</a> is binding. If the state is scalar-only, the row-valued MPFR theorem cannot be imported as though its coefficient vector were scalar-exact. In scalar state, the correct theorem is $\mathrm{CPSL}_{67}$.

# All real endpoints and activation sides

Every object in the direct source formulation is continuous in real $X$. A new hinge at $X=km$ enters with coefficient zero. On an open cell between consecutive activation points, every target and scalar coordinate is affine in $\log X$ plus square-root target terms, and the finite Lorenz LP varies continuously. At a knot, the newly entered atom has zero scalar hinge and its target has the explicitly chosen one-sided convention. Therefore a universal proof must state which side owns the target activation and verify both limiting LPs. Sampling integer endpoints is insufficient.

The retained terminal certificate does include one-sided local activation cells. This does not supply the global source LP, but it removes an unrelated interpolation ambiguity at the local canonical leaf.

# Complete Mellin transform and growth audit

We now prove the analytic consumer without repository shorthand.

<div id="lem:growth" class="lemma">

**Lemma 9** (Growth). *For $X\ge2$, $$|R_X|\le60\sqrt X(1+\log X).$$*

</div>

<div class="proof">

*Proof.* The function $t^{-1/2}\log(Y/t)$ decreases on $[1,Y]$, and integral comparison gives $$\sum_{m\le Y}\frac1{\sqrt m}\log(Y/m)\le4\sqrt Y.$$ Since $0\le q_*(m)\le15$, $Q_*(Y)\le60\sqrt Y$. Hence $$|R_X|\le60\sqrt X\sum_{k\le X}\frac1k
\le60\sqrt X(1+\log X).$$ ◻

</div>

Thus $R_X$ is locally integrable and has finite Mellin abscissa. For $\sigma=\Re s>1/2$, absolute Fubini is justified. Substituting $X=kY$ gives the essential factor $$k^{-s-1/2}.$$ Also, $$\int_m^\infty\log(X/m)X^{-s-1}\,dX=\frac{m^{-s}}{s^2}.$$ The Dirichlet series of $q_*$ is $$\sum_{m\ge1}\frac{q_*(m)}{m^z}
=6\zeta(z)-6+9\,2^{-z}-3\,4^{-z},
\qquad z=s+\tfrac12.$$ Multiplying by $\sum\mu(k)k^{-z}=1/\zeta(z)$ yields

<div id="thm:mellin" class="theorem">

**Theorem 10** (Exact scalar Mellin transform). *Initially for $\Re s>1/2$, $$\label{eq:mellin}
\boxed{
\int_1^\infty R_X X^{-s-1}\,dX
=\frac6{s^2}
-\frac{3(1-2^{-z})(2-2^{-z})}{s^2\zeta(z)},
\quad z=s+\tfrac12.}$$ The right side gives the meromorphic continuation to $\Re s>0$.*

</div>

# Real-axis removability, pole survival, and Landau

For real $z>1$, $\zeta(z)>0$. For $0<z<1$, the alternating eta series is positive and $$\eta(z)=(1-2^{1-z})\zeta(z),$$ so $\zeta(z)<0$. Hence zeta has no real zero in $(0,\infty)$. At $z=1$, $1/\zeta(z)$ has a zero, so <a href="#eq:mellin" data-reference-type="eqref" data-reference="eq:mellin">[eq:mellin]</a> is removable. Therefore the continuation is analytic at every real $s>0$.

If $\rho$ is a nontrivial zero with $\Re\rho>1/2$, then $$|2^{-\rho}|=2^{-\Re\rho}<1.$$ Thus $2^{-\rho}$ equals neither $1$ nor $2$. The finite numerator in <a href="#eq:mellin" data-reference-type="eqref" data-reference="eq:mellin">[eq:mellin]</a> is nonzero. A zero of arbitrary multiplicity $m$ therefore gives a pole of order $m$ at $s=\rho-1/2$.

<div id="thm:landau" class="theorem">

**Theorem 11** (Mellin–Landau implication). *If $R_X\ge0$ for all sufficiently large real $X$, then RH holds.*

</div>

<div class="proof">

*Proof.* Discard the finite initial interval; its Mellin transform is entire. Put $f(t)=R_{e^t}$ on the remaining half-line. By Lemma <a href="#lem:growth" data-reference-type="ref" data-reference="lem:growth">9</a>, $f$ is locally integrable and of exponential order. Its Laplace transform is <a href="#eq:mellin" data-reference-type="eqref" data-reference="eq:mellin">[eq:mellin]</a>. Landau’s theorem for nonnegative Laplace transforms says that a finite real abscissa of convergence is a singular point. Since the continuation is analytic at every positive real $s$, the abscissa is at most zero. The defining transform is therefore holomorphic throughout $\Re s>0$. An off-line zero $\rho$ would create the nonremovable pole at $\rho-1/2$ found above, a contradiction. The functional equation reflects zeros across $\Re z=1/2$, so every nontrivial zero lies on the critical line. ◻

</div>

Combining Theorems <a href="#thm:lorenz" data-reference-type="ref" data-reference="thm:lorenz">7</a> and <a href="#thm:landau" data-reference-type="ref" data-reference="thm:landau">11</a> proves Theorem <a href="#thm:main" data-reference-type="ref" data-reference="thm:main">1</a>.

# Independent executable reconstruction

The accompanying program uses exact rational arithmetic for the coefficient identities, causal weights, scalar tradeoff, Cauchy–Binet countermodel, Lorenz primal/dual fixtures, and Mellin numerator. It uses directed Decimal intervals for the $239$-atom odd-history target witness and a separate floating diagnostic for finite scalar LP instances and the prefix state. The latter is explicitly falsification, not proof.

The mutation suite rejects:

1.  dropping cumulative history parity;

2.  replacing the native rough coefficient $r$ by $2r^2$;

3.  omitting the compensation $r-2r^2$;

4.  using $HK$ instead of $H^{\mathsf T}K$;

5.  inferring Hall from positive minors;

6.  claiming scalar exactness gives two nonnegative rows;

7.  treating the local terminal certificate as global capacity;

8.  checking only integer endpoints;

9.  omitting $k^{-s-1/2}$ in Mellin Fubini;

10. promoting finite scans to $\mathrm{CPSL}_{67}$ or RH.

# Response to the mandatory adversarial inputs

| Input   | Finding                                                                 | Disposition                                                                                                                                 |
|:--------|:------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------|
| PR #574 | Correct feature product is $H^{\mathsf T}K$ and owner ordering matters. | Independently reproved; retained only for determinant propagation.                                                                          |
| PR #574 | Cauchy–Binet does not prove target capacity or global Lorenz dominance. | Accepted as binding; exact $2\times2$ countermodel included.                                                                                |
| PR #574 | Odd-history witness blocks leafwise Hall.                               | Independently recomputed with gap $17.0050865\ldots$.                                                                                       |
| PR #575 | Completed parity owner ledger is finite and exact.                      | Independently reproved in Section 4.                                                                                                        |
| PR #575 | $Q_3/Q_2$ is monotone.                                                  | Independently reproved; used only for the row-two-exact edge.                                                                               |
| PR #575 | Scalar exactness does not lift to two rows.                             | Accepted as binding; exact formulas in Proposition <a href="#prop:tradeoff" data-reference-type="ref" data-reference="prop:tradeoff">6</a>. |
| PR #575 | Scalar Hall is a finite Lorenz LP with one-dimensional dual.            | Made the canonical producer frontier, Theorem <a href="#thm:lorenz" data-reference-type="ref" data-reference="thm:lorenz">7</a>.            |
| PR #575 | Uniform $\mathrm{CPSL}_{67}$ is open.                                   | Accepted as the first unsupported arrow and the theorem carrying zero-free strength.                                                        |

# Conclusion and exact status

The manuscript resolves the deltas rather than the Riemann Hypothesis. The finite owner ledger, parity character, local directed terminal certificate, ratio monotonicity, scalar dictionary, Mellin transform, noncancellation, and Landau consumer are mutually compatible at their actual scopes. What fails is the transition from local certified leaves to one global source-faithful capacity statement.

The first unsupported arrow is $$\boxed{
\text{literal completed-parity source}
\not\Longrightarrow_{\text{proved}}
\text{uniform target-exact scalar-superordinate Lorenz coupling}.}$$ In the predecessor this arrow was named “reserve-preserving grouped Hall” and written as $g\ge Tg$. The missing $r-2r^2$ source, the odd-history target deficit, the Cauchy–Binet capacity gap, and the scalar-to-row tradeoff show why it cannot be accepted as bookkeeping.

The strongest honest result is the exact criterion $$\boxed{\mathrm{CPSL}_{67}\Longrightarrow R_X\ge0\text{ eventually}\Longrightarrow\mathrm{RH}.}$$ Uniform $\mathrm{CPSL}_{67}$ is open and RH-bearing. No equivalent cancellation or benchmark estimate is assumed elsewhere.

# Interface contract table

| Interface                                 | What is proved                                   | What is needed                  | Verdict            |
|:------------------------------------------|:-------------------------------------------------|:--------------------------------|:-------------------|
| Canonical rows to real endpoints          | continuous zero-entry hinges                     | all cells and knot sides        | exact              |
| Owner ledger                              | unique factorization, coefficient and activation | one owner and parity            | exact              |
| Unsigned causal identity to native source | $P=sP+\lambda(P-rC)+\alpha C$                    | odd coefficient $r$ after swap  | mismatch: $2r^2$   |
| Compensation to Hall                      | required $r-2r^2$ demand                         | disjoint owned global capacity  | open               |
| Local AVLT to odd leaf                    | canonical orientation row margins                | reversed/global compensation    | fails leafwise     |
| TP2 to Hall                               | determinant signs                                | target capacity/Lorenz prefixes | false implication  |
| Scalar to rows                            | scalar equality                                  | two nonnegative rows            | false              |
| Global source to scalar Hall              | finite Lorenz LP                                 | uniform $\mathrm{CPSL}_{67}$    | open               |
| Scalar positivity to RH                   | exact Mellin and Landau                          | eventual $R_X\ge0$              | proved conditional |

# Hostile-review checklist

Reject the route at the first occurrence of any of the following:

1.  a source occurrence whose coefficient or activation changes under ownership transfer;

2.  an $\alpha$ child recursed without the $r-2r^2$ compensation source;

3.  a compensation atom with no unique owner;

4.  use of a canonical terminal coefficient vector after an odd history;

5.  use of determinant signs as total target capacity;

6.  scalar exactness promoted to row feasibility;

7.  score, port or barycenter coordinates silently erased from a scalar LP;

8.  integer samples substituted for real activation cells;

9.  a pointwise transcendental value represented as a directed interval;

10. omission of the factor $k^{-s-1/2}$ in the Mellin substitution;

11. a finite diagnostic represented as proof of $\mathrm{CPSL}_{67}$ or RH.

<div class="thebibliography">

9 E. C. Titchmarsh, revised by D. R. Heath-Brown, *The Theory of the Riemann Zeta-Function*, 2nd ed., Oxford University Press, 1986. D. V. Widder, *The Laplace Transform*, Princeton University Press, 1941. G. H. Hardy, J. E. Littlewood, and G. Pólya, *Inequalities*, 2nd ed., Cambridge University Press, 1952. L. Fousse, G. Hanrot, V. Lefèvre, P. Pélissier, and P. Zimmermann, “MPFR: A Multiple-Precision Binary Floating-Point Library with Correct Rounding,” *ACM Trans. Math. Software* 33 (2007), no. 2. T. M. Apostol, *Introduction to Analytic Number Theory*, Springer, 1976.

</div>
