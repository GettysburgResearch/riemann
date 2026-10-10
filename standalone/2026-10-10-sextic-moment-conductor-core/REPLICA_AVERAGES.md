# Sixth-power averages as bounded operators, and a sharper finite-moment obstruction

**Status:** proposed component proofs, 2026-10-10. The full short-row fourth or generalized moment is not proved. No new zero-free boundary is claimed.

**Scope:** exact Euler removal for the Eisenstein sextic family; a bounded inverse for averages over moving sixth-power lifts in Mellin-weighted spaces; a logarithm-free, deletion-tolerant extraction theorem; and two explicitly non-native examples showing why finitely many moments cannot bootstrap through removal identities alone.

**Dependencies:** elementary Eisenstein ideal counting; the exact removal identity in MOMENT_OBSTRUCTIONS.md, Section 3, the refined sieve in REFINED_ALL_ROW_SIEVE.md, and the incidence decomposition in GENERAL_MOMENT_ATTACK.md, all under standalone/2026-10-10-sextic-moment-descent at PR #913 head 6498d6cc2eded03159c7332b25fd224ad07f89c1; and the nonvanishing Mellin test in standalone/2026-10-10-generalized-inverse-moments/MELLIN_AND_SPIKES.md at PR #912 head 6afd64e042ce7b59d550c3d76e9e2cca8b2c7379. These are separate source packets. No imported quasi-RH conclusion is used.

**What was actually done:** mathematical derivation and source inspection. No zero computation, formal proof build, or independent validation of the external manuscripts was performed.

**Smallest missing arithmetic statement:** an estimate for the actual signed balanced coefficients that excludes the finite-ladder behavior exhibited below. The bounded averaging operator is an adapter for such an estimate, not a source of extra cancellation.

## 1. A common averaged Euler estimate

All ideal sums are over nonzero integral ideals of \(K=\mathbb Q(\sqrt{-3})\). Write \(q_p=Np\). Eisenstein lattice counting gives

\[
\#\{v:Nv\le Y\}=\kappa_KY+O_K(\sqrt Y+1),
\qquad \#\{v:Nv\le Y\}\le C_KY\quad(Y\ge1).
\tag{1.1}
\]

For a finite prime set \(Q\), let

\[
\mathcal V_Q(Y)=\{v:(v,Q)=1,\ Y/2<Nv\le Y\},
\quad J_Q(Y)=|\mathcal V_Q(Y)|,
\quad \delta_Q=\prod_{p\in Q}(1-q_p^{-1}).
\]

Finite inclusion-exclusion proves

\[
J_Q(Y)\sim \frac{\kappa_K\delta_Q}{2}Y.
\tag{1.2}
\]

If \((r,Q)=1\), then

\[
\frac{\#\{v\in\mathcal V_Q(Y):r\mid v\}}{J_Q(Y)}
\longrightarrow\frac1{Nr},
\qquad
\frac{\#\{v\in\mathcal V_Q(Y):r\mid v\}}{J_Q(Y)}
\le\frac{C_Q}{Nr}
\tag{1.3}
\]

for all sufficiently large \(Y\), uniformly in \(r\). For the upper bound use (1.1) after \(v=rw\); if \(Nr>Y\), the numerator is zero.

For \(\beta>0\), put

\[
G_\beta(v)=\sum_{d\mid v^\infty}(Nd)^{-\beta}
=\prod_{p\mid v}(1-q_p^{-\beta})^{-1},
\qquad R_\beta(v)=G_\beta(v)-1.
\tag{1.4}
\]

For every fixed \(a>0\), the following positive Euler product converges:

\[
\mathcal C_{a,\beta,Q}
=\prod_{p\notin Q}\left[1+
\frac{(1-q_p^{-\beta})^{-a}-1}{q_p}\right].
\tag{1.5}
\]

Indeed its prime perturbation is \(O_{a,\beta}(q_p^{-1-\beta})\). Expanding

\[
G_\beta(v)^a
=\sum_{\substack{r\mid v\\r\ {\rm squarefree}}}
\prod_{p\mid r}\big[(1-q_p^{-\beta})^{-a}-1\big]
\]

and applying (1.1) proves

\[
\sum_{Nv\le Y}G_\beta(v)^a\ll_{a,\beta,K}Y.
\tag{1.6}
\]

Applying (1.3), with dominated convergence justified by the same positive product, proves the exact conditional limit

\[
\lim_{Y\to\infty}\frac1{J_Q(Y)}
\sum_{v\in\mathcal V_Q(Y)}G_\beta(v)^a
=\mathcal C_{a,\beta,Q}.
\tag{1.7}
\]

For every integer \(p\ge1\), the limit of the corresponding average of \(R_\beta(v)^p\) also exists: expand \((G_\beta-1)^p\) as a finite polynomial in \(G_\beta\). Moreover,

\[
0\le R_\beta(v)^p\le G_\beta(v)^p-1,
\]

so its limiting mean tends to zero as the fixed set \(Q\) increases to contain all small primes. Notice that this uses \(\beta>0\), not \(\beta>1-1/p\).

## 2. An invertible averaging operator, including moving row ranges

Fix an integer \(p\ge1\), \(\beta>0\), and a completely multiplicative \(c(d)\) with \(c(1)=1\) and \(|c(d)|\le1\). Zeros in \(c\) are permitted. If \(F(D)\) vanishes below a positive scale, define its exact lifted functions

\[
B_v(D)=\sum_{d\mid v^\infty}c(d)F(D/Nd).
\tag{2.1}
\]

At every fixed \(D\), this sum is finite. With

\[
f(D)=D^{-\beta}F(D),\qquad
(T_vf)(D)=D^{-\beta}B_v(D),
\]

one has

\[
(T_vf)(D)=\sum_{d\mid v^\infty}c(d)(Nd)^{-\beta}f(D/Nd).
\tag{2.2}
\]

### Theorem 2.1. Uniformly invertible rough-base averaging

For every \(0<\eta<1\), there is a fixed finite prime set \(Q\), containing any prescribed initial finite set, and \(Y_0\ge1\), such that the following holds.

Let \(Y(D)\ge Y_0\) be any measurable function. On \(0<D\le X\), use the measure

\[
\int_0^X\frac1{J_Q(Y(D))}
\sum_{v\in\mathcal V_Q(Y(D))}(\cdot)\,\frac{dD}{D}.
\tag{2.3}
\]

Then the diagonal map \(Jf(D,v)=f(D)\) is an isometry and

\[
\boxed{\quad
\|Tf-Jf\|_{L^p((2.3))}\le\eta\|f\|_{L^p((0,X),dD/D)}.
\quad}
\tag{2.4}
\]

The constants are independent of \(X\) and of the measurable moving range \(Y(D)\). In particular,

\[
(1-\eta)\|f\|_p\le\|Tf\|_p\le(1+\eta)\|f\|_p.
\tag{2.5}
\]

The actual average

\[
(\overline T f)(D)=\frac1{J_Q(Y(D))}
\sum_{v\in\mathcal V_Q(Y(D))}(T_vf)(D)
\]

satisfies \(\|\overline T-I\|_{p\to p}\le\eta\). It therefore has the bounded inverse

\[
\boxed{\qquad
\overline T^{-1}
=\sum_{j\ge0}(I-\overline T)^j,
\qquad \|\overline T^{-1}\|_{p\to p}\le(1-\eta)^{-1}.
\qquad}
\tag{2.6}
\]

The same theorem holds on the full positive scale axis. For general \(L^p\) inputs, the operators are defined by the bounded extension from inputs supported in a compact interval of positive scales.

**Proof.** Put \(G=G_\beta\), \(R=G-1\). Weighted Hölder gives

\[
|(T_vf)(D)-f(D)|^p
\le R(v)^{p-1}
\sum_{\substack{d\ne1\\d\mid v^\infty}}
(Nd)^{-\beta}|f(D/Nd)|^p.
\tag{2.7}
\]

For \(p=1\), give \(R(v)^0\) the value one, including when \(R(v)=0\). For \(d\ne1\), with \((d,Q)=1\), define

\[
b_d(Y)=\frac{(Nd)^{-\beta}}{J_Q(Y)}
\sum_{\substack{v\in\mathcal V_Q(Y)\\\operatorname{rad}d\mid v}}
R(v)^{p-1}.
\tag{2.8}
\]

Each \(b_d(Y)\) has a limit as \(Y\to\infty\). To verify this without any unproved probabilistic assumption, expand \(R^{p-1}\) as a polynomial in \(G\), expand each power of \(G\) by the positive squarefree divisor formula preceding (1.6), and use (1.3). The extra condition \(\operatorname{rad}d\mid v\) replaces a divisor \(r\mid v\) by \(\operatorname{lcm}(r,\operatorname{rad}d)\mid v\). Absolute domination follows from this divisor expansion or the bound below.

Write \(r=\operatorname{rad}d\). Since \(G(rw)\le G(r)G(w)\), equations (1.6), (1.2) imply, uniformly for large \(Y\),

\[
b_d(Y)\le C_{Q,\beta,p}
\frac{(Nd)^{-\beta}G(r)^{p-1}}{Nr}.
\tag{2.9}
\]

The right side is summable over \(d\ne1\), because its Euler product has local nonconstant term

\[
\frac{(1-q_p^{-\beta})^{-(p-1)}}{q_p(q_p^\beta-1)}
=O_{p,\beta}(q_p^{-1-\beta}).
\]

For each \(Y\), summing (2.8) over \(d\ne1\) gives exactly the conditional mean of \(R(v)^p\). Thus dominated convergence identifies

\[
\sum_{d\ne1}b_d(\infty)
=\lim_{Y\to\infty}\frac1{J_Q(Y)}
\sum_{v\in\mathcal V_Q(Y)}R(v)^p.
\tag{2.10}
\]

Choose \(Q\) so that (2.10) is less than \(\eta^p/2\). The same summable domination, now applied to \(\sup_{Y\ge Y_0}b_d(Y)\), shows that for sufficiently large \(Y_0\),

\[
\sum_{d\ne1}\sup_{Y\ge Y_0}b_d(Y)<\eta^p.
\tag{2.11}
\]

Here each supremum converges to \(b_d(\infty)\) as \(Y_0\to\infty\); this extra step is what permits an arbitrary moving \(Y(D)\).

Average (2.7) at the actual \(Y(D)\), integrate, and dominate every coefficient by its supremum in (2.11). For every \(d\), scale invariance gives

\[
\int_0^X|f(D/Nd)|^p\frac{dD}{D}
=\int_0^{X/Nd}|f(x)|^p\frac{dx}{x}
\le\|f\|_p^p.
\]

This proves (2.4). The fiber probabilities sum to one at each \(D\), so \(J\) is an isometry; the norm triangle inequality proves (2.5). Jensen's inequality gives \(\|\overline T-I\|\le\eta\). The Banach-space Neumann series gives (2.6). All coefficients only use smaller scales, so the operator acts on the same truncated space \((0,X)\). The full-axis and extension statements follow first for compactly supported inputs and then by completion. \(\square\)

### Exact application to the native family

For a fixed base row \(r\ne0\), take

\[
F(D)=A_r(D;W),\quad
c(d)=\nu(d)\chi_d(r)\mathbf1_{(d,S)=1}.
\]

The actual identity is \(B_v(D)=A_{rv^6}(D;W)\). The set \(Q\) restricts the *bases being averaged*. It does not replace the source character, delete additional columns from \(A_r\), or assume an estimate with a moving excluded conductor.

Taking \(Y(D)=(D^h/Nr)^{1/6}\) is permitted once \(D\) exceeds a fixed threshold. One may set \(Y(D)=Y_0\) below that threshold. The bounded initial scale portion contributes only a bounded term in applications.

### Corollary 2.2. Exact limiting Mellin multiplier

At each fixed \(D\), (1.3) and the finite cutoff in (2.1) give

\[
\lim_{Y\to\infty}\frac1{J_Q(Y)}
\sum_{v\in\mathcal V_Q(Y)}B_v(D)
=\sum_{(d,Q)=1}\frac{c(d)}{N\operatorname{rad}d}F(D/Nd).
\tag{2.12}
\]

Its Mellin multiplier is

\[
\begin{aligned}
K_Q(s)
&=\prod_{p\notin Q}\left(1+
\frac{c(p)}{q_p(q_p^s-c(p))}\right)\\
&=\prod_{p\notin Q}
\frac{1-(1-q_p^{-1})c(p)q_p^{-s}}
     {1-c(p)q_p^{-s}}.
\end{aligned}
\tag{2.13}
\]

This product converges locally uniformly, is holomorphic, and is nonzero throughout \(\Re s>0\). Each local numerator and denominator is nonzero there, and the prime deviations from one are \(O(q_p^{-1-\Re s})\), locally uniformly. Mellin multiplication follows first in any initial absolute-convergence half-plane. It therefore preserves every genuine reciprocal-\(L\) pole in \(\Re s>0\).

This is a bounded adapter for an analysis of averaged lifts. Neither (2.6) nor (2.13) improves a power bound for \(F\) in the absence of a new bound for that average.

## 3. Actual moment spikes without a prime-counting logarithm

Use the single test \(W_*\) of the previous MELLIN_AND_SPIKES.md, whose Mellin transform is nonzero in \(\Re s>0\). Retain every literal zero extension in

\[
A_u(D)=\sum_{(n,S)=1}\mu_K(n)\nu(n)\chi_n(u)W_*(Nn/D).
\]

### Theorem 3.1. Positive-density record replication

Fix \(h>0\), a nonzero base row \(r\), \(\beta>0\), and an integer \(p\ge1\). If \(|A_r(D)|/D^\beta\) is unbounded, then there are scales \(D_j\to\infty\), constants \(c>0\), and numbers \(L_j\to\infty\), such that at least \(cD_j^{h/6}\) distinct permitted rows satisfy

\[
|A_u(D_j)|\ge L_jD_j^\beta.
\tag{3.1}
\]

Consequently

\[
\boxed{\quad
\frac{\displaystyle\sum_{0<Nu\le D_j^h}|A_u(D_j)|^p}
     {D_j^{p\beta+h/6}}\longrightarrow\infty.
\quad}
\tag{3.2}
\]

This removes the factor \(\log D_j\) in the earlier prime-replica lower bound.

**Proof.** Continuity and the lower support cutoff give record scales with

\[
C_j:=\frac{|A_r(D_j)|}{D_j^\beta}\longrightarrow\infty,
\qquad |A_r(x)|\le C_jx^\beta\quad(0<x\le D_j).
\]

The exact identity (2.1) gives

\[
|A_{rv^6}(D_j)-A_r(D_j)|
\le |A_r(D_j)|R_\beta(v).
\tag{3.3}
\]

Choose one fixed \(Q\) so that the limiting conditional mean of \(R_\beta\) is less than \(1/16\). For sufficiently large \(Y\), that mean is at most \(1/8\). Markov's inequality shows that at least \(3/4\) of the bases in \(\mathcal V_Q(Y)\) satisfy \(R_\beta(v)\le1/2\). Put \(Y=(D_j^h/Nr)^{1/6}\). Their rows \(rv^6\) are distinct, have norm at most \(D_j^h\), and have magnitude at least \(|A_r(D_j)|/2\). Equations (1.2) and \(C_j\to\infty\) prove (3.1) with \(L_j=C_j/2\); summation gives (3.2). This uses ideal counting, not a prime ideal theorem. \(\square\)

If the primitive character inducing the fixed row has a zero with real part \(b>\beta>0\), the nonvanishing Mellin test makes \(|A_r(D)|/D^\beta\) unbounded. Thus Theorem 3.1 applies to every such zero.

### Corollary 3.2. A weaker sufficient tail target

Fix \(\alpha>0\) and \(C_0>0\). The all-scale estimate

\[
\#\{u:0<Nu\le D^h,\ |A_u(D)|>C_0D^\alpha\}
=o(D^{h/6})
\tag{3.4}
\]

implies \(A_r(D)=O_r(D^\alpha)\) for every fixed row \(r\). Apply Theorem 3.1 with \(\beta=\alpha\): unbounded normalized values would force a positive multiple of \(D^{h/6}\) rows above the fixed threshold. The single-test Mellin identity then excludes zeros with real part greater than \(\alpha\).

The earlier \(o(D^{h/6}/\log D)\) sufficient tail condition can therefore be relaxed to (3.4). This change is logarithmic; it does not change the finite-moment power boundary.

### Corollary 3.3. A sufficiently sparse discarded set is harmless

Let \(E_D\subseteq\{u:0<Nu\le D^h\}\) be arbitrary, even selected from the values of the sums, with

\[
|E_D|=o(D^{h/6}).
\tag{3.5}
\]

Suppose for a fixed \(k\ge1\), \(e\ge0\), and every \(\epsilon>0\),

\[
\sum_{\substack{0<Nu\le D^h\\u\notin E_D}}|A_u(D)|^{2k}
\ll_\epsilon D^{k+h+e+\epsilon}.
\tag{3.6}
\]

Then every fixed row twist is zero-free in

\[
\Re s>\frac12+\frac{5h}{12k}+\frac e{2k}.
\tag{3.7}
\]

**Proof.** At the record scales of Theorem 3.1, removing (3.5) leaves at least \(cD_j^{h/6}/2\) of its large replicas. Thus (3.2) holds also on the complement of \(E_{D_j}\). A zero to the right of (3.7) permits choosing \(\beta\) between the boundary and the zero, giving \(2k\beta+h/6>k+h+e\), which contradicts (3.6) with a small fixed \(\epsilon\). \(\square\)

Hence literally every row is not a necessary quantifier: \(o(H^{1/6})\) arbitrary omitted rows are permissible. Removing all sixth-power rows, or all lifts of even one fixed sixth-power-free core, is still impermissible by this criterion: either deletion has size of order \(H^{1/6}\). No estimate satisfying (3.6) for the actual short-row family is proved here.

## 4. A model satisfying the complete removal identities

The earlier numerical-array obstruction imposed no removal identities. The following model closes that logical loophole. It is **not** the native Möbius Dirichlet polynomial.

Fix \(h>0\), an integer \(K\ge1\), and \(B>1/2\) such that

\[
B\le\frac12+\frac{5h}{12K}.
\tag{4.1}
\]

Choose \(\varphi\in C^\infty((0,\infty))\), with \(0\le\varphi\le1\), \(\varphi(D)=0\) for \(D\le1\), and \(\varphi(D)=1\) for \(D\ge2\). Put \(F_B(D)=D^B\varphi(D)\). On the genuine nonzero Eisenstein row labels define

\[
\mathscr A_u(D)=
\begin{cases}
\displaystyle\sum_{\substack{d\mid v^\infty\\(d,S)=1}}F_B(D/Nd),
 &u=v_0^6,\ (v_0)=v,\\
0,&u\text{ is not an integral sixth power}.
\end{cases}
\tag{4.2}
\]

Since every Eisenstein unit has sixth power one, \(v_0^6\) depends only on the ideal \(v\). Distinct ideals give distinct supported rows. Multiplication by a sixth power preserves the sixth-power class, including the unit class. Thus (4.2) defines all rows without a hidden unit multiplicity.

### Proposition 4.1. Exact removal, smoothness, and sharp moments

For every good prime ideal \(p\notin S\), with a chosen generator \(\pi\), the model satisfies the source-normalized identity with the genuine principal-datum sextic symbol:

\[
\boxed{\quad
\mathscr A_u(D)=\mathscr A_{u\pi^6}(D)
-\chi_p(u)\mathscr A_{u\pi^6}(D/Np).
\quad}
\tag{4.3}
\]

It is smooth in \(D\), vanishes for \(D\le1\), and satisfies, for every fixed positive integer \(j\),

\[
\boxed{\quad
\sum_{0<Nu\le D^h}|\mathscr A_u(D)|^{2j}
\asymp_{B,j,h,S}D^{2jB+h/6}
\quad(D\to\infty).
\quad}
\tag{4.4}
\]

For every \(\epsilon>0\), it also satisfies

\[
\max_{0<Nu\le D^h}|\mathscr A_u(D)|\ll_\epsilon D^{B+\epsilon}.
\tag{4.5}
\]

**Proof.** If \(u\) is not a sixth power, both lifted rows in (4.3) are also outside that class, so all three values vanish. If \(u=v_0^6\) and \(p\mid v\), then \(\chi_p(u)=0\); \(v\) and \(vp\) have the same prime support, so their defining sums agree. If \(p\nmid v\), then \(\chi_p(u)=1\), and splitting the exponent of \(p\) in the lifted sum gives

\[
\mathscr A_{u\pi^6}(D)
=\sum_{a\ge0}\mathscr A_u(D/q_p^a),
\]

whose shifted subtraction is (4.3). This also proves every finite composite removal identity by iteration. At primes in \(S\), multiplying the base by that prime does not change the sum, as the fixed deletion requires.

For \(D\ge2\), the \(d=1\) term and positivity give

\[
D^B\le\mathscr A_{v_0^6}(D)\le D^BG_B(v).
\]

There are asymptotically \(\kappa_KD^{h/6}\) supported rows in the row ball. Equation (1.6), with \(a=2j\), gives the upper bound in (4.4), and (1.1) gives the lower bound. The elementary bound \(G_B(v)\ll_\delta(Nv)^\delta\), obtained by comparing every large-prime logarithmic factor with \(\delta\log q_p\), gives (4.5). Each locally finite sum is smooth, and the cutoff is flat at its boundary. \(\square\)

At the endpoint \(B=B_K:=1/2+5h/(12K)\), this model satisfies every diagonal moment through \(2K\), while for every \(j>K\),

\[
\sum_{0<Nu\le D^h}|\mathscr A_u(D)|^{2j}
\asymp D^{h+j+\frac{5h}{6K}(j-K)}.
\tag{4.6}
\]

Thus the linear higher-moment loss survives the complete prime-removal algebra, literal zero extensions, smooth scale dependence, and the expected uniform power cap. A stronger prescribed cap \(B_{\rm cap}>1/2\) is respected by taking \(B=\min(B_K,B_{\rm cap})\): all moments through \(2K\) still hold, and the excess over \(D^{h+j}\) has positive limiting slope \(2B-1\) as \(j\to\infty\).

**Exact limitation.** This model does not come from the prescribed finite column sum, and it has no literal coefficients \(\mu_K(n)\nu(n)W(Nn/D)\). At a fixed scale it is nonzero only on integral sixth powers. Any nonzero finite sum of the source's character columns is periodic in \(u\), whereas a nonzero periodic row function cannot be supported on the zero-density set of integral sixth powers. The model also imposes no Hecke functional equation. It disproves a deduction from removal identities and finitely many norms alone, not the arithmetic moment conjecture.

## 5. A finite-ladder example on the actual sextic character kernel

The next example preserves the full finite column representation and row periodicity. Its deliberate violation is instead the finite-order Hecke condition on \(\nu\). The two examples are complementary.

Fix a nonnegative nonzero \(W\in C_c^\infty((0,\infty))\), \(h>0\), and an integer \(K\ge3h/2\). Put

\[
B=\frac12+\frac{5h}{12K},\qquad
\nu_B(p)=-q_p^{B-1}\quad(p\notin S).
\]

Extend \(\nu_B\) completely multiplicatively on the good ideals and by zero at \(S\). Then \(1/2<B\le7/9<1\), and

\[
C_u(D)=\sum_{(n,S)=1}\mu_K(n)\nu_B(n)\chi_n(u)W(Nn/D)
=\sum_{(n,S)=1}\mu_K(n)^2(Nn)^{B-1}\chi_n(u)W(Nn/D).
\tag{5.1}
\]

This is an actual finite sextic-character polynomial. Its coefficients are bounded and completely multiplicative after the Möbius factor, but \(|\nu_B(p)|<1\). Thus \(\nu_B\) is not a finite-order Hecke character and this example is explicitly outside the requested theorem.

### Lemma 5.1. General coefficient benchmark from the refined sieve

For fixed \(j\ge1\), bounded multiplicative coefficients on squarefree ideals, and a fixed compactly supported weight, the refined all-row sieve and the exact incidence decomposition give

\[
\mathcal N_{2j}(D,H)
\ll_\epsilon D^\epsilon
\left[HD^j+H^{1/6}D^{2j}+H^{2/3}D^{5j/3}\right]
\tag{5.2}
\]

when \(H\) is bounded by a fixed power of \(D\).

**Proof.** At \(j=1\), this is the refined all-row sieve multiplied by the coefficient square norm \(O(D)\). At general \(j\), use the exact incidence ideals \(c_I\), for subsets \(I\subseteq[j]\) with \(|I|\ge2\). After these are fixed, the singleton product length is

\[
P=D^j\prod_{|I|\ge2}(Nc_I)^{-|I|}.
\]

The squarefree allocation coefficient has square norm \(O(D^\epsilon P)\). The sieve bounds its row norm by

\[
D^\epsilon\big[\sqrt H P^{1/2}+H^{1/12}P+H^{1/3}P^{5/6}\big].
\]

The exterior factors have modulus at most one. Minkowski and the positive ideal sums give

\[
\sum P^{1/2}\ll D^{j/2}(\log(2D))^{\binom j2},
\quad \sum P\ll D^j,
\quad \sum P^{5/6}\ll D^{5j/6}.
\]

The last two sums converge after normalization, since \(|I|\ge2\). The first has harmonic pair overlaps and convergent larger overlaps. Square the resulting norm sum and absorb fixed-order logarithms into \(D^\epsilon\). This proves (5.2) without inverse-Möbius cancellation. \(\square\)

### Theorem 5.2. Sharp growth at and beyond a finite moment ladder

For the explicit family (5.1), every \(1\le j\le K\) satisfies

\[
\sum_{0<Nu\le D^h}|C_u(D)|^{2j}
\ll_{j,\epsilon}D^{h+j+\epsilon}.
\tag{5.3}
\]

For every fixed \(j\ge K\),

\[
D^{2jB+h/6}
\ll_j\sum_{0<Nu\le D^h}|C_u(D)|^{2j}
\ll_{j,\epsilon}D^{2jB+h/6+\epsilon}.
\tag{5.4}
\]

Thus its exact growth exponent for \(j\ge K\) is

\[
2jB+h/6=h+j+\frac{5h}{6K}(j-K).
\tag{5.5}
\]

**Upper proof.** Write \(W_B(x)=x^{B-1}W(x)\). This is another fixed smooth test, and
\(C_u(D)=D^{B-1}\sum\mu_K(n)^2\chi_n(u)W_B(Nn/D)\).
Multiply (5.2) by \(D^{2j(B-1)}\) to get

\[
\sum_{0<Nu\le D^h}|C_u(D)|^{2j}
\ll D^\epsilon\left[
D^{h+2jB-j}+D^{h/6+2jB}
+D^{2h/3+2jB-j/3}\right].
\tag{5.6}
\]

For \(j\le K\), the first exponent is at most \(h+j\), since \(K\ge3h/2>5h/6\). The second is at most \(h+j\), since \(j\le K\). For the third the needed inequality is

\[
j\left(\frac{5h}{6K}-\frac13\right)\le\frac h3.
\]

If the coefficient on the left is negative, this is immediate. Otherwise its maximum over \(j\le K\) occurs at \(j=K\), where the assertion is exactly \(K\ge3h/2\). This proves (5.3).

For \(j\ge K\), the second exponent in (5.6) dominates the first by \(j-5h/6\ge0\), and the third by \(j/3-h/2\ge0\). This proves the upper half of (5.4).

**Lower proof.** Elementary squarefree ideal density, obtained from
\(\mu_K(n)^2=\sum_{d^2\mid n}\mu_K(d)\) and (1.1), gives

\[
C_1(D)=c_{S,B,W}D^B+o(D^B),\qquad c_{S,B,W}>0.
\tag{5.7}
\]

For clarity, the unweighted squarefree count outside \(S\) has positive density: truncate the square-divisor identity at \(Nd\le R\), use (1.1) for each fixed \(d\), and bound its tail by \(CD\sum_{Nd>R}(Nd)^{-2}\). This proves the density by taking \(D\to\infty\) and then \(R\to\infty\). Partial summation against the fixed smooth \(x^{B-1}W(x)\) gives (5.7).

The same count gives \(|C_1(x)|\le Cx^B\) at every scale. The exact removal identity holds for the completely multiplicative \(\nu_B\), and \(|\nu_B(d)|\le1\), so

\[
|C_{v^6}(D)-C_1(D)|\le CD^BR_B(v).
\]

Choose one fixed \(Q\supseteq S\) so that the limiting conditional mean of \(R_B\) is sufficiently small relative to \(c_{S,B,W}/C\). Equations (1.7) and Markov show that a fixed positive proportion of the \(J_Q(D^{h/6})\asymp D^{h/6}\) bases satisfy \(|C_{v^6}(D)|\ge c_{S,B,W}D^B/4\), at every sufficiently large \(D\). Their nonnegative contributions give the lower half of (5.4). \(\square\)

For the requested \(1<h\le11/10\), one may take \(K=2\). This explicit non-Hecke family then has diagonal second and fourth moments, but its sixth and every higher moment fail the diagonal target by the power in (5.5). It is not a counterexample for any fixed finite-order Hecke datum.

Its principal Euler series exposes the artificial source of the large values:

\[
\sum_{(n,S)=1}\frac{\mu_K(n)^2(Nn)^{B-1}}{(Nn)^s}
=\frac{\zeta_K^S(s+1-B)}{\zeta_K^S(2s+2-2B)}.
\tag{5.8}
\]

The pole at \(s=B\) is a shifted zeta pole, not an off-critical zero of the native fixed Hecke \(L\)-function. The example is a stress test for arguments using only bounded multiplicativity, the sextic kernel, the removal identities, the classical sieve, and finitely many successful moment bounds.

## 6. Consequences for the next analytic step

The rough-lift average has a bounded inverse on every positive Mellin line and at every fixed integer \(p\ge1\), including an arbitrary moving row range. An estimate for that average can therefore be transferred back without a spurious restriction such as \(\beta+1/p>1\), or losses from treating each moving exclusion separately.

There is also a larger permissible exceptional set than the prime-only extraction showed: \(o(H^{1/6})\) rows may be removed from the input moment, with no restriction on their values. This could matter for a proof controlling the exact signed balanced core outside a truly sparse exceptional set. It does not justify removing all lifts of a primitive core.

The saturation examples identify what the new estimate must use. Exact removal identities with genuine sextic zero extensions are insufficient without column consistency; conversely, the actual periodic sextic kernel with bounded multiplicative coefficients and a finite diagonal moment ladder is insufficient without the native finite-order Hecke/Möbius structure. A higher-rank functional equation or signed coefficient reflection must supply a new assertion at precisely that intersection.

No estimate in this note proves \(\mathcal M_4(D,D^{1+\theta})\ll D^{2+\epsilon}D^{1+\theta}\), the \(17/24\) boundary, or an unbounded moment hierarchy.
