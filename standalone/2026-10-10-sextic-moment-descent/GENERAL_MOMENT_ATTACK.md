# General inverse moments: incidence decomposition, proved overlap ranges, and optimal extraction scale

Status: new proposed mathematics, continuing PR #910 at `670a76c1a3a8f325c43c1755b1cfc24d313a3e3c`. No full fourth-moment or higher-moment theorem is claimed.

Scope: exact identities for the actual Möbius/sextic source; a general-k norm reduction; analytic estimates for specified overlap pieces using existing large-sieve inputs; exact sixth-power extraction with positive-density bases. The balanced cores left outside the proved ranges are explicitly identified.

The main analytic additions are two proved ranges, with no new moment premise: the part of the k-th polynomial whose singleton product is at most \(H^{1/2}\), and the entire common-gcd tail above
\(\max\{1,(D^k/H^{5/6})^{1/(2k-2)},(D^{2k}/H)^{1/(5k-6)}\}\), each has energy \(\ll D^{k+\epsilon}H\). The second range uses the refined all-row sieve and is stronger than the initial powerful-ideal argument retained below. The exact identities specify these pieces before any norms are taken. The full moment remains open.

Exact sources: [OpenAI September 30 manuscript, commit adc7f1241b42e322a6451854ab7e4b4c146bf78a](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex), labels `lem:sextic-large-sieve` and `lem:planar-additive-sieve`; [October 5 manuscript at the same commit](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex), labels `prop:canonical`, `prop:poisson-reduction`, and `lem:remove-exclusions`. The previous fourth-moment reduction is preserved in [PR #910's frozen packet](https://github.com/GettysburgResearch/riemann/blob/670a76c1a3a8f325c43c1755b1cfc24d313a3e3c/standalone/2026-10-10-quasi-riemann-height-descent/FOURTH_MOMENT_REDUCTION.md).

What was checked: complete finite algebra and analytic deductions below; the existing squarefree large-sieve normalization was checked against its exact source statement. The imported analytic theorem itself is an input, not independently re-proved here. No zero computation establishes any of the claims.

Additional dependencies for the strongest bounds: [REFINED_ALL_ROW_SIEVE.md](REFINED_ALL_ROW_SIEVE.md), Theorem 3.4, reviewed at SHA-256 `6879e094fb63969ddc88c637bf633cf46360d144d2b1615573647e734b4141e8`. It uses Blomer–Goldmakher–Louvel's order-three and order-six squarefree sieves, the Goldmakher–Louvel quadratic large sieve in the imported October 5 `lem:quadratic`, and an ordinary primitive-character large sieve proved there from Gauss sums, character orthogonality, and the planar additive sieve. These classical inputs are distinct from the imported quasi-Riemann zero-free theorem; the latter is not used in the overlap estimates.

Smallest remaining gap: a mean square for long squarefree product columns with the exact k-way balanced divisor coefficient. The general-k overlap ranges in Theorems 4.1–4.2 are proved using the stated classical sieves; their complement is not.

## 1. Fixed source and exact incidence decomposition

Work over \(K=\mathbb Q(\sqrt{-3})\). Ideal indices use the source's chosen primary generators outside the fixed finite bad-prime set \(S\). Fix an integer \(k\ge2\), a finite-order character \(\nu\), and a smooth function \(W\) supported in a fixed interval \([a,b]\subset(0,\infty)\). Put

\[
A_u(D)=\sum_{(n,S)=1}\mu_K(n)\nu(n)\chi_n(u)W(Nn/D),
\qquad D\ge2.
\tag{1.1}
\]

All row sums below include every nonzero element \(u\) in the indicated norm ball. No sixth-power row is discarded.

For every nonempty subset \(I\subseteq[k]\), attach a squarefree ideal \(c_I\). Require all these ideals to be pairwise coprime and prime to \(S\). The incidence representation of a tuple of squarefree ideals \((n_1,\ldots,n_k)\) is

\[
n_i=\prod_{I\ni i}c_I.
\tag{1.2}
\]

It is unique: a prime belongs to \(c_I\) exactly when it divides precisely the factors indexed by \(I\). Write \(a_i=c_{\{i\}}\) for the singleton factors, and retain only the shared ideals \(\mathbf c=(c_I)_{|I|\ge2}\) as exterior indices. Define

\[
Q_i=\prod_{\substack{I\ni i\\|I|\ge2}}Nc_I,
\quad X_i=D/Q_i,
\quad C=\prod_{|I|\ge2}c_I,
\quad R(\mathbf c)=\prod_{|I|\ge2}(Nc_I)^{|I|},
\quad P(\mathbf c)=\prod_iX_i=\frac{D^k}{R(\mathbf c)}.
\tag{1.3}
\]

Only configurations with \(X_i\ge1/b\) can contribute. Every shared ideal then satisfies \(Nc_I\le bD\), and \(NC\le(bD)^{k/2}\).

Define the squarefree core

\[
B_{C,u}(\mathbf X)=
\sum_{\substack{a_1,\ldots,a_k\ \mathrm{squarefree}\\
                  (a_i,a_j)=1\ (i\ne j)\\
                  (a_1\cdots a_k,CS)=1}}
\mu_K(a_1\cdots a_k)\nu(a_1\cdots a_k)
\chi_{a_1\cdots a_k}(u)
\prod_iW(Na_i/X_i).
\tag{1.4}
\]

Equivalently,

\[
B_{C,u}(\mathbf X)=
\sum_{\substack{r\ \mathrm{squarefree}\\(r,CS)=1}}
\mu_K(r)\nu(r)\chi_r(u)\mathcal W_{\mathbf X}(r),
\quad
\mathcal W_{\mathbf X}(r)
=\sum_{a_1\cdots a_k=r}\prod_iW(Na_i/X_i).
\tag{1.5}
\]

Because \(r\) is squarefree, each factorization in (1.5) is automatically pairwise coprime.

### Proposition 1.1. Exact source identity

For every row \(u\),

\[
A_u(D)^k
=\sum_{\mathbf c}
\left\{\prod_{|I|\ge2}
\mu_K(c_I)^{|I|}\nu(c_I)^{|I|}\chi_{c_I}(u)^{|I|}\right\}
B_{C,u}(\mathbf X).
\tag{1.6}
\]

**Proof.** Expand the ordinary k-th power, not a Hermitian power. All nonzero coefficient tuples are squarefree. Apply the unique incidence decomposition (1.2). Multiplicativity, including every zero extension, splits each factor exactly as displayed. The smooth weight at index \(i\) becomes \(W(Na_i/X_i)\). The singleton Möbius signs combine to \(\mu_K(a_1\cdots a_k)\) because those ideals are pairwise coprime. Regrouping a finite sum proves (1.6). \(\square\)

The exterior coefficient has modulus at most one. Its character powers need not be primitive, and for multiples of six they can be principal with exclusions. No assertion about those characters is needed to use multiplication by this exterior coefficient as a contraction in the row \(\ell^2\) norm.

## 2. The exact normalized overlap cost

### Proposition 2.1. Harmonic pair overlaps and convergent higher overlaps

Suppose a collection \(\mathcal C\) of incidence configurations satisfies, for every \(\epsilon>0\),

\[
\|B_{C,\cdot}(\mathbf X)\|_{\ell^2(0<Nu\le H)}
\ll D^\epsilon\sqrt{H P(\mathbf c)}
\tag{2.1}
\]

with one implied constant independent of the moving \(C\) and the configurations in that collection. Then their portion \(F_{\mathcal C}\) of the right side of (1.6) satisfies

\[
\|F_{\mathcal C}\|_2
\ll D^\epsilon\sqrt H D^{k/2}
\bigl(\log(2D)\bigr)^{\binom{k}{2}}.
\tag{2.2}
\]

**Proof.** The triangle inequality and the exterior contraction give the norm bound

\[
D^\epsilon\sqrt H D^{k/2}
\sum_{\mathbf c\in\mathcal C}
\prod_{|I|\ge2}(Nc_I)^{-|I|/2}.
\]

Drop all pairwise-coprimality and coupled support restrictions. For subsets of size two use
\(\sum_{Nc\le bD}(Nc)^{-1}\ll\log(2D)\). For each subset of size \(m\ge3\), use the convergent sum \(\sum_c(Nc)^{-m/2}=\zeta_K(m/2)\). Thus the overlap sum is at most

\[
\left(\sum_{Nc\le bD}\frac1{Nc}\right)^{\binom{k}{2}}
\prod_{m=3}^k\zeta_K(m/2)^{\binom{k}{m}}.
\tag{2.3}
\]

This proves the claim. \(\square\)

For fixed \(k\), the squared logarithmic cost is absorbed in an arbitrarily small power. The only critical overlap summations are the pair incidences. Prime factors repeated three or more times have genuinely summable normalized cost. This is an unconditional statement about the exact decomposition; (2.1) is a separate analytic premise whenever it has not already been established for the chosen configurations.

The full new target would be (2.1) for every admissible configuration. It is a squarefree-column statement with the exact divisor weight (1.5), not a theorem for arbitrary coefficients of length \(P\). The changing exclusions remain explicit.

## 3. An existing squarefree large sieve does extend to every row

The imported source's `lem:sextic-large-sieve` states, for arbitrary complex coefficients fixed before the row sum,

\[
\sum_{\substack{a\ \mathrm{squarefree}\\Na\le M}}
\left|\sum_{\substack{n\ \mathrm{squarefree}\\Nn\le N}}
z_n\chi_n(a)\right|^2
\ll_{S,\epsilon}(MN)^\epsilon
\bigl(M+N+(MN)^{2/3}\bigr)\sum_n|z_n|^2.
\tag{3.1}
\]

All displayed squarefree indices are outside \(S\). Its zero extensions are retained.

### Initial all-row route, retained for provenance

For the same squarefree column coefficients, independent of the row,

\[
\sum_{0<Nu\le H}\left|\sum_nz_n\chi_n(u)\right|^2
\ll_{S,\epsilon}(HN)^\epsilon
\left(H+N H^{1/2}+(HN)^{2/3}\right)\sum_n|z_n|^2.
\tag{3.2a}
\]

**Proof.** First separate the unit of \(u\), and the product \(q\) of bad primes whose valuations in \(u\) equal one. There are only a fixed finite number of choices for these labels. Write the remaining row uniquely as \(u=u_0qab\), where \(a\) is squarefree, prime to \(S\), and consists of the primes with valuation exactly one; \(b\) is powerful, meaning every nonzero prime valuation in \(b\) is at least two. Also \((a,b)=1\).

Fix \(u_0,q,b\). The coefficient multiplier \(\chi_n(u_0qb)\) is independent of \(a\), has modulus at most one, and keeps every forced zero. Extend the positive row sum from \((a,b)=1\) to all allowed squarefree \(a\), and apply (3.1) with \(M=H/N(qb)\). Empty ranges are omitted.

Powerful ideals have counting function \(O_K(X^{1/2})\): uniquely write such an ideal as \(r^2s^3\), with \(s\) squarefree, and sum the bound \(O_K((X/Ns^3)^{1/2})\) over \(s\). Their weighted sum \(\sum_{b\ \mathrm{powerful}}(Nb)^{-t}\) converges for every \(t>1/2\), either by this counting estimate or its absolutely convergent Euler product. Sum the three terms in (3.1) over powerful \(b\):

\[
H\sum_b(Nb)^{-1}\ll H,
\quad N\#\{b:Nb\le H\}\ll NH^{1/2},
\quad (HN)^{2/3}\sum_b(Nb)^{-2/3}\ll(HN)^{2/3}.
\]

The fixed labels only change the implied constant, and \((MN)^\epsilon\le(HN)^\epsilon\). This proves (3.2a). \(\square\)

This initial extension and its fourth-moment application were independently developed by the parent research pass. The exact source hypotheses, including coefficients independent of the squarefree row, bad-prime rows, units, and zero extensions, were checked here. It adds no conjectural moment input. The following stronger result supersedes its bound in all subsequent deductions.

### Lemma 3.1. Refined all-row extension

For \(H,N\ge1\) and the same squarefree column coefficients, independent of the row,

\[
\sum_{0<Nu\le H}\left|\sum_nz_n\chi_n(u)\right|^2
\ll_{S,\epsilon}(HN)^\epsilon
\left(H+N H^{1/6}+(HN)^{2/3}\right)\sum_n|z_n|^2.
\tag{3.2}
\]

**Proof and exact dependency.** This is Theorem 3.4 of [REFINED_ALL_ROW_SIEVE.md](REFINED_ALL_ROW_SIEVE.md), at the reviewed hash above. Its proof writes every row uniquely as a unit times \(v^6a_1a_2^2a_3^3a_4^4a_5^5\), with pairwise-coprime squarefree \(a_j\) and arbitrary \(v\), retaining the exact column mask \((n,v)=1\). On dyadic blocks it combines the order-three, order-six, and quadratic squarefree sieves with the ordinary primitive-character sieve for the full sixth-free core. The latter has bounded multiplicity because each good local character determines its exponent \(j\). Bad-prime and unit patterns form only fixed finite classes. The block optimization and logarithmic summation give (3.2), uniformly in all coefficient masks fixed before the row sum. Thus moving column exclusions are permitted without a moving implied constant. The cited proof supplies all Gauss-sum normalizations, primitive-conductor checks, and monomial inequalities; no higher-moment or zero-free premise enters. \(\square\)

### Lemma 3.2. Coefficient mass of a balanced squarefree core

For every \(\epsilon>0\), uniformly in the moving exclusion \(C\) and all admissible \(\mathbf X\),

\[
\sum_{\substack{r\ \mathrm{squarefree}\\(r,CS)=1}}
|\mu_K(r)\nu(r)\mathcal W_{\mathbf X}(r)|^2
\ll_{k,W,\epsilon}D^\epsilon P.
\tag{3.3}
\]

**Proof.** A product \(r\) lies in a fixed multiple of the norm range \(P\). It has at most \(d_{k,K}(r)\ll_{k,\epsilon}(Nr)^\epsilon\) ordered factorizations. Apply Cauchy–Schwarz inside (1.5), then sum the absolute squared weights over the ordered tuples. Ideal counting gives \(O_W(X_i)\) possibilities for each factor because \(X_i\ge1/b\). Their product is \(O_{k,W}(P)\). Deleting columns by \((r,C)=1\) can only decrease this coefficient mass. Since \(P\le D^k\), absorb the fixed-order divisor loss into \(D^\epsilon\). \(\square\)

Combining these lemmas gives the already-proved core estimate

\[
\|B_{C,\cdot}(\mathbf X)\|_2^2
\ll D^\epsilon\left(HP+H^{1/6}P^2+H^{2/3}P^{5/3}\right).
\tag{3.4}
\]

For bounded \(P<1\), replace the column upper cutoff by a fixed constant; the displayed estimate still holds with a constant depending on \(k,W\), since \(P\ge b^{-k}\) whenever the core is nonempty.

## 4. A proved part of every general moment

For \(P_0\ge1\), let \(F_{\le P_0}(u)\) be exactly the portion of (1.6) whose singleton product length satisfies \(P(\mathbf c)\le P_0\). It is a specified part of the polynomial \(A_u(D)^k\); its norm is not being silently identified with a moment of a different truncated \(A_u\).

### Theorem 4.1. Short singleton-product range

For fixed \(k,W,S,\nu,C_0\), every \(\epsilon>0\), \(D\ge2\), and \(1\le H\le D^{C_0}\),

\[
\|F_{\le P_0}\|_2^2
\ll D^\epsilon D^k
\left(H+H^{1/6}P_0+H^{2/3}P_0^{2/3}\right).
\tag{4.1}
\]

In particular,

\[
\boxed{\quad P_0\le H^{1/2}
\quad\Longrightarrow\quad
\|F_{\le P_0}\|_2^2\ll D^{k+\epsilon}H.\quad}
\tag{4.2}
\]

**Proof.** Taking the square root of (3.4), summing by Minkowski, and using (1.3), gives three sums proportional to

\[
\sqrt H\sum P^{1/2},\qquad
H^{1/12}\sum P,\qquad
H^{1/3}\sum P^{5/6},
\tag{4.3}
\]

over the stated configurations. The first is at most \(D^{k/2}\) times the overlap cost (2.3).

For \(r>1/2\), put \(T=D^k/P_0\). The condition \(P\le P_0\) means \(R(\mathbf c)\ge T\). If \(T\ge1\), choose any sufficiently small \(\delta>0\). Rankin's inequality and absolute convergence give

\[
\sum_{R\ge T}R^{-r}
\le T^{-(r-1/2-\delta)}
\prod_{|I|\ge2}\sum_{c_I}(Nc_I)^{-|I|(1/2+\delta)}
\ll_{k,\delta}T^{-(r-1/2-\delta)}.
\tag{4.4}
\]

Dropping pairwise-coprimality and support restrictions is legitimate in this positive majorant. Taking \(r=1\) and \(r=5/6\), and choosing \(\delta\) small in terms of the requested loss, proves

\[
\sum_{P\le P_0}P\ll D^{k/2+\epsilon}P_0^{1/2},
\qquad
\sum_{P\le P_0}P^{5/6}\ll D^{k/2+\epsilon}P_0^{1/3}.
\tag{4.5}
\]

If \(T<1\), use the unrestricted convergent sums at \(r=1,5/6\); the same right sides dominate because \(P_0>D^k\). Squaring the sum of the three bounds from (4.3) proves (4.1). The two extra terms are at most \(H\) when \(P_0\le H^{1/2}\), proving (4.2). \(\square\)

For \(H=D^{1+\theta}\), this handles every incidence configuration satisfying

\[
\prod_{|I|\ge2}(Nc_I)^{|I|}
\ge D^{k-(1+\theta)/2}.
\tag{4.6}
\]

For \(k=2\), the sole shared ideal is the ordinary gcd \(c\), and this is precisely
\(Nc\ge D H^{-1/4}\). Thus the complete large-gcd part already has the desired fourth-moment energy. The remaining squarefree cores have product length \(P>H^{1/2}\), and their exact divisor weights must still be used to improve (3.4).

This isolates a genuine analytic remainder. It does not turn the full k-th polynomial into a sum of independently estimated terms without accounting for interference: the final combination with a future estimate for the complement uses the norm triangle inequality.

### Theorem 4.2. A common-gcd tail at every moment

Let \(G_{\ge C_1}^{(k)}\) be the part of \(A_u(D)^k\) whose original tuple has \(N\gcd(n_1,\ldots,n_k)\ge C_1\), with \(C_1\ge1\). Then

\[
\|G_{\ge C_1}^{(k)}\|_2^2
\ll D^\epsilon\left(
HD^k+H^{1/6}D^{2k}C_1^{2-2k}
+H^{2/3}D^{5k/3}C_1^{2-5k/3}\right).
\tag{4.7}
\]

Consequently this entire common-gcd tail has the desired diagonal moment scale if

\[
C_1\ge\max\left\{1,
\left(\frac{D^k}{H^{5/6}}\right)^{1/(2k-2)},
\left(\frac{D^{2k}}H\right)^{1/(5k-6)}\right\}.
\tag{4.8}
\]

**Proof.** The full common gcd is exactly the incidence ideal \(c_{[k]}\). Repeat (4.3), this time restricting that one ideal to \(Nc_{[k]}\ge C_1\). The first normalized overlap sum is bounded by (2.3). For the second sum, use the convergent weights \((Nc_I)^{-|I|}\) on all other shared ideals and
\(\sum_{Nc\ge C_1}(Nc)^{-k}\ll C_1^{1-k}\) on \(c_{[k]}\). The third sum uses exponents \(5|I|/6>1\), and its common-gcd tail is \(O(C_1^{1-5k/6})\). Thus the three norm terms are at most

\[
D^\epsilon\left(
\sqrt H D^{k/2}+H^{1/12}D^kC_1^{1-k}
+H^{1/3}D^{5k/6}C_1^{1-5k/6}\right).
\]

Squaring proves (4.7). The second term is at most \(HD^k\) when \(C_1^{2k-2}\ge D^k/H^{5/6}\). The third is at most \(HD^k\) when \(C_1^{5k-6}\ge D^{2k}/H\). Together with \(C_1\ge1\), these are precisely (4.8). Unlike the initial powerful-ideal estimate, neither requirement may be discarded for all \(k\). \(\square\)

At \(H=D^{1+\theta}\), the sufficient common-gcd threshold is

\[
C_1=D^{\gamma_k(\theta)},\qquad
\gamma_k(\theta)=\max\left\{0,
\frac{6k-5-5\theta}{12k-12},
\frac{2k-1-\theta}{5k-6}\right\}.
\tag{4.9}
\]

For \(0<\theta\le1/10\), this gives \(D^{(3-\theta)/4}\) at \(k=2\), \(D^{(5-\theta)/9}\) at \(k=3\), and \(D^{(19-5\theta)/36}\) at \(k=4\). The initial route gave \(D^{(2k-1-\theta)/(4k-4)}\), so the sixth- and eighth-moment common-gcd ranges have strictly increased; the fourth-moment threshold is unchanged. These ranges can include configurations whose singleton product exceeds \(H^{1/2}\). They therefore add a second family of already-controlled pieces to Theorem 4.1. Their union still leaves long balanced cores with small common gcd.

## 5. A complementary common-gcd estimate from the ordinary character sieve

There is also a direct estimate in which the common gcd remains the oscillating variable. It gives an independent bound from the ordinary planar sieve, without using the higher-order large-sieve input (3.1).

### Lemma 5.1. Ordinary all-row character estimate

Let \(j\not\equiv0\pmod6\), and let \(z_c\) be arbitrary coefficients on squarefree primary \(c\) outside \(S\), with \(C\le Nc<2C\). Then

\[
\sum_{0<Nu\le H}\left|\sum_c z_c\chi_c(u)^j\right|^2
\ll_S (H+C^2)\sum_c|z_c|^2.
\tag{5.1}
\]

**Proof.** At every good prime dividing \(c\), the power \(\chi_p^j\) is nontrivial. The product character is primitive modulo the squarefree ideal \(c\). Its Gauss expansion expresses it as a sum over reduced residue fractions \(x/c\), with coefficient modulus \((Nc)^{-1/2}\). Distinct reduced fractions with \(Nc<2C\) have separation \(\gg C^{-1}\) in the fixed Eisenstein torus: their difference modulo the lattice is a nonzero algebraic integer divided by \(cc'\). The source's planar additive large sieve gives the factor \(H+C^2\). The total squared mass of the expanded coefficients is at most \(\sum_c |z_c|^2\), since there are \(\varphi(c)\le Nc\) reduced residues for each denominator. Fixed normalization factors at bad primes or units are separated into finitely many classes. The primitive Gauss identity is valid at nonunits too, and therefore keeps the original zero extensions. \(\square\)

Let \(G_{\ge C_0}^{(k)}(u)\) be the part of the expanded polynomial \(A_u(D)^k\) with \(N\gcd(n_1,\ldots,n_k)\ge C_0\). For \(6\nmid k\), (5.1) gives

\[
\|G_{\ge C_0}^{(k)}\|_2
\ll_{k,W,S}D^k
\left(\sqrt H\,C_0^{1/2-k}+C_0^{3/2-k}\right),
\quad k\ge2.
\tag{5.2}
\]

To prove this, on a gcd dyad \(Nc\asymp C\), write \(n_i=ca_i\), freeze the residual tuple, and retain its exact common-gcd and coprimality restrictions. There are \(O_{k,W}((D/C)^k)\) tuples. For each, the c-coefficients have squared mass \(O_{k,W}(C)\), including all moving exclusions and smooth weights. The row multiplier from the residual tuple has modulus at most one. Apply (5.1), then Minkowski over the tuples and dyadic \(C\ge C_0\). Both geometric sums converge.

For \(H=D^{1+\theta}\), this reaches \(\|G\|_2^2\ll HD^k\) when

\[
C_0\ge D^{\gamma_k},\qquad
\gamma_k=max\left\{\frac{k}{2k-1},\frac{k-1-\theta}{2k-3}\right\},
\quad 6\nmid k.
\tag{5.3}
\]

For \(6\mid k\), the common-factor character can be principal, so (5.1) cannot be used. Direct counting instead gives

\[
\|G_{\ge C_0}^{(k)}\|_2
\ll\sqrt H\,D^k C_0^{1-k},
\tag{5.4}
\]

which reaches the target when \(C_0\ge D^{k/(2k-2)}\). These are proved partial ranges, not a claim that the residual common-gcd-one portion is controlled.

For \(k=2\), (5.2) reads

\[
\|G_{\ge C_0}^{(2)}\|_2^2
\ll D^4\left(H/C_0^3+1/C_0\right).
\tag{5.5}
\]

It needs \(C_0\ge\max(D^{2/3},D^2/H)\). The stronger squarefree-core route in Section 4 needs only \(C_0\ge DH^{-1/4}\) for the intended \(H=D^{1+\theta}\), \(0<\theta\le1/10\). The bounds use different reductions and agree at the expected crossover \(H=D^{4/3}\); this note does not substitute the weaker bound for the stronger one.

## 6. Positive-density sixth-power extraction

Prime sixth-power rows are not necessary for extraction. Averaging suitable composite bases removes the logarithmic sparsity of prime bases without changing the power exponent.

Write

\[
B_v(x)=A_{v^6}(x)
=\sum_{(n,vS)=1}\mu_K(n)\nu(n)W(Nn/x).
\]

Euler factors, or finite coefficient convolution, give the exact identity

\[
B_v(x)=\sum_{\operatorname{rad}(r)\mid v}\nu(r)A_1(x/Nr).
\tag{6.1}
\]

The sum is finite for each \(x\), because \(A_1(y)=0\) below the fixed support threshold. This is an exact treatment of moving exclusions; no constant is permitted to depend on \(v\).

### Lemma 6.1. A fixed roughness condition makes the recurrence contractive

Fix \(\beta>0\). There exists a fixed finite set \(Q\supseteq S\) of primes such that, for

\[
\mathcal V_Q(Y)=\{v:(v,Q)=1,\ Y/2<Nv\le Y\},
\qquad J_Q(Y)=|\mathcal V_Q(Y)|,
\]

one has \(J_Q(Y)\asymp_Q Y\) and, for all sufficiently large \(Y\),

\[
\frac1{J_Q(Y)}\sum_{v\in\mathcal V_Q(Y)}
\sum_{\substack{r\ne1\\\operatorname{rad}(r)\mid v}}(Nr)^{-\beta}
\le\frac12.
\tag{6.2}
\]

**Proof.** Counting nonzero Eisenstein lattice points in a disk and dividing by the six units gives \(\#\{v:Nv\le x\}=\kappa_Kx+O_K(\sqrt x+1)\). Finite inclusion–exclusion at the fixed set \(Q\) therefore gives \(J_Q(Y)\asymp_Q Y\). For every fixed \(r\) coprime to \(Q\), apply the same count after writing \(v=\operatorname{rad}(r)w\); the proportion of these bases divisible by \(\operatorname{rad}(r)\) tends to \(1/N\operatorname{rad}(r)\). Uniformly for sufficiently large \(Y\), that proportion is at most \(C_Q/N\operatorname{rad}(r)\), by the elementary upper bound for ideals of bounded norm. The positive sum

\[
E_{\beta,Q}
=\sum_{\substack{r\ne1\\(r,Q)=1}}
\frac{(Nr)^{-\beta}}{N\operatorname{rad}(r)}
=\prod_{p\notin Q}
\left(1+\frac1{Np((Np)^\beta-1)}\right)-1
\tag{6.3}
\]

converges for \(\beta>0\). Consequently dominated convergence identifies the limit of the left side of (6.2) as \(E_{\beta,Q}\). Enlarging the fixed set \(Q\) makes this Euler-product tail as small as desired. Choose it so \(E_{\beta,Q}<1/4\); then (6.2) follows for large \(Y\). No prime ideal theorem is used. \(\square\)

### Proposition 6.2. Endpoint-preserving extraction

Let \(p\ge1\), \(h>0\), and \(\beta>0\). Suppose

\[
\sum_{0<Nu\le D^h}|A_u(D)|^p
\ll D^{p\beta+h/6}
\qquad(D\ge2).
\tag{6.4}
\]

Then \(A_1(D)\ll D^\beta\), with no additional logarithmic or arbitrarily-small-power loss.

**Proof.** Let \(Y=D^{h/6}\) and average (6.1) over \(v\in\mathcal V_Q(Y)\), with \(Q\) chosen by Lemma 6.1 and enlarged to contain every prime of norm at most two. The sixth-power rows are distinct and lie in the permitted row ball. Hölder and \(J_Q(Y)\asymp_Q Y\) bound the average of \(B_v(D)\) by \(O(D^\beta)\). The remaining terms all have argument at most \(D/2\). Assuming the induction bound \(|A_1(x)|\le Cx^\beta\) at smaller scales, their average is at most \(CD^\beta/2\) by (6.2). Choose \(C\) to absorb the first term and the bounded initial interval, and induct on dyadic intervals. This proves the claim. \(\square\)

For the proposed diagonal \(2k\)-th moment \(D^{k+\epsilon}D^h\), this gives

\[
\beta=\frac12+\frac{5h}{12k}+\frac{\epsilon}{2k}.
\tag{6.5}
\]

The arbitrarily small loss comes from the input moment, not from sparsity of the extraction set. The moment premise could be restricted to these fixed-roughness sixth-power rows alone; no such restricted estimate is proved here. Since those rows reproduce the target up to the exact exclusion recurrence, restricting to them does not by itself make the analytic problem easy.

The limiting hierarchy has a precise strength: [MOMENT_OBSTRUCTIONS.md, Theorem 10.1](MOMENT_OBSTRUCTIONS.md#10-the-unbounded-moment-hierarchy-is-an-rh-level-assertion) proves that, for fixed \(\nu,S\) and one fixed \(h>0\), these diagonal moments for an unbounded set of fixed \(k\), every fixed smooth test, and every positive loss are equivalent to GRH for the entire sextic row-twist family \(\nu(n)\chi_n(r)\). Constants may depend on each fixed \(k\). This identifies the strength of the unproved hierarchy; it supplies no missing moment estimate.

### Proposition 6.3. Cardinality barrier for a pure moment-to-copy extraction

There are \(O(H^{1/6})\) distinct sixth-power rows in \(0<Nu\le H\). For any weights on such rows with \(\sum_v\lambda_v=1\), Hölder's conjugate norm satisfies

\[
\|\lambda\|_{p/(p-1)}\ge N^{-1/p}
\gg H^{-1/(6p)},
\tag{6.6}
\]

where \(N\) is the number of supported rows; for \(p=1\), use the maximum norm. This follows from \(1\le\sum|\lambda_v|\le N^{1/p}\|\lambda\|_{p/(p-1)}\).

Therefore a direct weighted Hölder extraction using only the moment budget \(D^kH\) cannot improve the power \(D^{1/2}H^{5/(12k)}\). Uniform weights on the positive-density bases above attain the cardinality scale up to constants. Signed or sieve weights do not improve this norm bound. This is a limitation of that inference from moment information, not a lower bound on actual Möbius sums and not a prohibition on a new arithmetic identity.

## 7. Result of this attack

The repeated-prime obstruction has been reduced completely at the level of the norm: every fixed moment has an exact squarefree-core representation, and only pair overlaps cost logarithms. The refined classical large-sieve combination proves the desired diagonal moment scale for all configurations with singleton product \(P\le H^{1/2}\), and for the larger common-gcd range (4.8); the complement is a precisely specified long-column problem. The ordinary-character argument in Section 5 gives a separate independent estimate. None of these overlap bounds uses the metaplectic descent or a quasi-Riemann zero-free theorem.

The higher-moment extraction is now available with positive-density sixth-power bases and no artificial prime-counting loss, but the cardinality calculation shows that changing those weights alone cannot turn the existing second moment into the proposed \(17/24\) exponent. A new estimate for the long balanced cores, or another source-specific identity controlling their off diagonal, is still required. No fourth moment at \(H=D^{1+\theta}\), and no further zero-free boundary, has been established here.
