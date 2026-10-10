# A squarefree-column reduction for the fourth moment

Status: independent mathematical review; two proved structural reductions and a clearly unproved analytic target.

Scope: the completed height theorem and conditional prime extraction in `UPSTREAM_HEIGHT_AND_MOMENTS.md`; the coefficient class needed for its proposed fourth-moment input. This note proves no new zero-free region.

Exact dependencies: OpenAI source commit [`adc7f1241b42e322a6451854ab7e4b4c146bf78a`](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a), particularly [October 5, `paper2.tex`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex), labels `eq:T`, `eq:completed-twist`, `lem:quadratic`, `eq:prepared-theta-sum`, `eq:auxiliary-conductor-bound`, `eq:theta-separated-columns`, and `lem:squarefree-completed`. The squarefree marked-column restriction is in [September 30, `paper.tex`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex), original lines 9306–9320.

What was checked: exact source interfaces and complete arguments, not numerical zeros or independent verification of the imported theta-reflection theorem and quadratic large sieve. No new analytic computation was required.

Smallest remaining gap: a mean-square estimate for the squarefree balanced divisor coefficients in Proposition 3 below, uniform under its explicit moving coprimality exclusions.

## 1. Audit verdict on the two proposed deductions

### 1.1 Completed height theorem

No mathematical correction was identified in Proposition 4.4 of `UPSTREAM_HEIGHT_AND_MOMENTS.md`, under its stated dependence on the imported arithmetic inputs. The proof uses more than the formal gamma-factor asymptotic: the exact prepared dual family was checked against the source.

In the reflected weight, put \(R=1+|t|\) and write

\[
\mathcal T V_t(x)=G(it)(cx)^{-it}F_t(cx/R^4).
\]

At the prepared argument

\[
x=\frac{3^mNn\,(Nb)^3\mathcal H_0^2}{Y(Nk_0)^2},
\]

the removed phase is a product of a column phase \((Nn)^{-it}(Nb)^{-3it}\), a row phase \((Nk_0)^{2it}\), and fixed-label phases. The column phase preserves the coefficient bound and independence from \(k_0\). The source quadratic sieve accepts arbitrary complex column coefficients. The source's separation is only in the scaled column variable \(Nn/U\), and the demodulated profile has the required uniform derivatives there. Consequently the effective length changes from \(Y\) to a constant times \(R^4Y\); the arithmetic coefficient/conductor updates remain unchanged.

The resulting prepared estimate is

\[
\ll a^2(DR)^\epsilon(\mathcal H_0+R^4Y),
\]

and the source inequality

\[
a^2Y\ll\frac{\mathcal H_0^2}{X}N(t_0)^2N(g)
\]

gives exactly the advertised completed bound. Here \(t_0\) is the frozen squarefree ideal in the source, not the real height. The final squareful-row sum still has the convergent weight \((Nv)^{-2}\).

The distinction between this completed theorem and the uncompleted inverse-family theorem is necessary. The source's two-Poisson canonical descent has additional transformed profiles, and no height-uniform closure of that entire family was proved by the completed calculation alone.

### 1.2 Higher-moment prime extraction

No mathematical correction was identified in Proposition 7.2. In particular, the recursion is essential and works with the same fixed data \(\nu,S,W\):

\[
A_1(x)=B_p(x)-\nu(p)B_p(x/Np),\qquad
B_p(x)=\sum_{j\ge0}\nu(p)^jA_1(x/(Np)^j).
\]

The sum is finite by the lower support threshold. Taking prime ideals of norm \(\asymp D^{h/6}\) produces distinct permitted sixth-power rows. Hölder gives the exponent

\[
\frac{k+h-h/6}{2k}=\frac12+\frac{5h}{12k}.
\]

For any slightly larger positive exponent \(\beta\), the smaller-scale part is at most

\[
C_\beta C D^\beta D^{-h\beta/6},
\]

which closes induction on sufficiently large dyadic intervals. It does not require a moment theorem whose implied constants depend on the moving prime. Retention of the sixth-power rows and a moment hypothesis for every test needed by the subsequent Mellin argument are both indispensable.

## 2. The sextic diagonal has the expected size at every fixed moment

The fourth-power coefficient in the proposed moment has cube-free support. At higher moments \(k\ge6\), unequal product columns can have a quotient that is a sixth power. These additional algebraic diagonals still have the expected order of magnitude as an upper bound.

### Proposition 2.1. Counting the full algebraic sextic diagonal

Fix an integer \(k\ge1\), a compact support interval \([a,b]\subset(0,\infty)\), and the fixed field \(K=\mathbb Q(\sqrt{-3})\). For every \(\epsilon>0\), the number of tuples of squarefree integral ideals

\[
(\mathfrak a_1,\ldots,\mathfrak a_k,
  \mathfrak b_1,\ldots,\mathfrak b_k),\qquad
aD\le N\mathfrak a_i,N\mathfrak b_j\le bD,
\]

satisfying

\[
v_{\mathfrak p}\!\left(\prod_i\mathfrak a_i\right)
-v_{\mathfrak p}\!\left(\prod_j\mathfrak b_j\right)
\equiv0\pmod6
\quad\text{for every prime ideal }\mathfrak p
\tag{2.1}
\]

is \(O_{K,k,a,b,\epsilon}(D^{k+\epsilon})\).

**Proof.** Each occurring prime ideal has a unique incidence pattern \((I,J)\), where \(I\subseteq\{1,\ldots,k\}\) is the set of left factors containing it and \(J\subseteq\{1,\ldots,k\}\) is the corresponding right set. Condition (2.1) requires \(|I|-|J|\equiv0\pmod6\). A nonempty permitted pattern has total multiplicity

\[
m_{I,J}=|I|+|J|\ge2.
\]

Let \(\mathfrak q_{I,J}\) be the product of the primes with that pattern. There are a fixed finite number \(r_k\) of permitted patterns. The original tuple is recovered uniquely from these squarefree, pairwise coprime ideals. Moreover,

\[
\prod_{I,J}(N\mathfrak q_{I,J})^{m_{I,J}}
=\prod_iN\mathfrak a_i\prod_jN\mathfrak b_j
\le(bD)^{2k}.
\]

Since every nonempty exponent is at least two,

\[
\prod_{I,J}N\mathfrak q_{I,J}\le(bD)^k.
\]

Discarding their coprimality and squarefreeness only enlarges the count. It is bounded by

\[
\sum_{N\mathfrak q\le(bD)^k}d_{r_k,K}(\mathfrak q)
\ll_{K,k,\epsilon}D^{k+\epsilon},
\]

using the fixed-order ideal divisor bound and ideal counting in this fixed quadratic field. This proves the claim. \(\square\)

If the quotient of two sextic column characters is principal, the standard Kummer valuation condition gives (2.1). Thus this count bounds the whole principal-character contribution, even if further fixed local conditions make the actual principal set smaller. Fixed bounded smooth weights and the unit-modulus factor \(\nu\) do not enlarge its absolute size beyond \(D^{k+\epsilon}\).

This is a compatibility check on the proposed \(D^kH\) moment. It supplies no cancellation in nonprincipal row sums. At large \(k\), constants and divisor orders depend on \(k\); the statement is for each fixed \(k\).

## 3. Fourth moments reduce to squarefree balanced divisor columns

The repeated-prime cubic factor can be removed from the *analytic closure target* at only a logarithmic cost. It must first be retained in the exact identity.

Use ideals throughout, with the source's chosen primary generators whenever a sextic symbol is evaluated. Let

\[
A_u(D)=\sum_{(n,S)=1}\mu_K(n)\nu(n)\chi_n(u)W(Nn/D),
\]

where \(W\) is fixed, smooth, and supported in \([a,b]\subset(0,\infty)\). For a squarefree ideal \(c\) prime to \(S\), define

\[
B_{c,u}(X)=
\sum_{\substack{(a,b)=1\\(ab,cS)=1}}
\mu_K(a)\mu_K(b)\nu(ab)\chi_{ab}(u)
W(Na/X)W(Nb/X).
\tag{3.1}
\]

The Möbius coefficients enforce squarefreeness. This has only squarefree product columns:

\[
B_{c,u}(X)=
\sum_{\substack{r\ \mathrm{squarefree}\\(r,cS)=1}}
\mu_K(r)\nu(r)\chi_r(u)\,\mathcal W_X(r),
\tag{3.2}
\]

where

\[
\mathcal W_X(r)=\sum_{d\mid r}W(Nd/X)
W\!\left(\frac{Nr}{XNd}\right).
\tag{3.3}
\]

The notation \(cS\) means the union of the prime divisors of \(c\) and the fixed bad-prime set \(S\).

### Proposition 3.1. Exact decomposition and a sufficient squarefree-column estimate

For every row \(u\), including its exact zero extensions,

\[
A_u(D)^2=
\sum_{\substack{c\ \mathrm{squarefree}\\(c,S)=1}}
\mu_K(c)^2\nu(c)^2\chi_c(u)^2
B_{c,u}(D/Nc).
\tag{3.4}
\]

Fix \(0<\theta\le1/10\) and put \(H=D^{1+\theta}\). Suppose that for every \(\epsilon>0\),

\[
\boxed{\displaystyle
\sum_{0<Nu\le H}|B_{c,u}(X)|^2
\ll_{W,\theta,\nu,S,\epsilon}D^\epsilon H X^2}
\tag{3.5}
\]

uniformly for \(D\ge2\), \(1\le X\le D\), and all squarefree \(c\) prime to \(S\) with \(Nc\le bD\).

**Unproved analytic input.** The row range in (3.5) is the full \(H=D^{1+\theta}\) for every smaller column-factor scale \(X\); it is not replaced by \(X^{1+\theta}\). The implied constant is independent of the moving exclusion \(c\).

Then

\[
\sum_{0<Nu\le H}|A_u(D)|^4
\ll_{W,\theta,\nu,S,\epsilon}D^{2+\epsilon}H.
\tag{3.6}
\]

**Proof of the identity.** In the square of \(A_u\), take \(c=\gcd(n_1,n_2)\), and write \(n_1=ca\), \(n_2=cb\). Since both original factors are squarefree, \(c,a,b\) are squarefree and pairwise coprime. Then

\[
\mu_K(ca)\mu_K(cb)=\mu_K(c)^2\mu_K(a)\mu_K(b),
\]

\[
\nu(ca)\nu(cb)=\nu(c)^2\nu(ab),\qquad
\chi_{ca}(u)\chi_{cb}(u)=\chi_c(u)^2\chi_{ab}(u).
\]

These identities include zeros when a prime divides the row. The two smooth weights have common rescaled length \(X=D/Nc\). This proves (3.4).

**Proof of the estimate.** Regard each row function as a vector in \(\ell^2(\{u:0<Nu\le H\})\). Multiplication by \(\chi_c(u)^2\) is a contraction because its modulus is either zero or one. Minkowski's inequality therefore gives

\[
\left(\sum_{0<Nu\le H}|A_u(D)|^4\right)^{1/2}
\le\sum_{Nc\le bD}\|B_{c,\cdot}(D/Nc)\|_2.
\tag{3.7}
\]

For \(Nc\le D\), hypothesis (3.5) bounds the right-hand summand by

\[
\ll D^{\epsilon/2}H^{1/2}\frac D{Nc}.
\]

The ideal harmonic sum in this fixed field satisfies
\(\sum_{Nc\le D}(Nc)^{-1}\ll\log(2D)\). If \(D<Nc\le bD\), then \(X\in[1/b,1)\); only a fixed finite set of ideals can occur in each factor of (3.1). Its norm is \(O_W(H^{1/2})\), and there are \(O_W(D)\) such \(c\). Their total is \(O_W(DH^{1/2})\). Hence

\[
\left(\sum_{0<Nu\le H}|A_u(D)|^4\right)^{1/2}
\ll D^{1+\epsilon/2}H^{1/2}\log(2D).
\]

Choosing the hypothesis's loss smaller than the requested final loss absorbs the squared logarithm and proves (3.6). \(\square\)

### What this reduction removes, and what it leaves

The new Poisson/reflection closure theorem need not itself handle a cube-free column or an exterior cubic row factor. The exact decomposition retains the latter, and the proof disposes of it only after passing to the row norm, at an explicitly bounded cost.

The new coefficient theorem must still handle the full balanced divisor weight (3.3) and the moving exclusion \((r,c)=1\), uniformly in \(c\). Neither requirement follows from the existing marked-column theorem. Nor can that exclusion be treated as part of the fixed set \(S\) while allowing an uncontrolled implied constant. Formula (3.5) remains a new analytic input, not a consequence of the source's ordinary second moment.

This is a reduction of the coefficient class, not an exponent improvement. In particular, it does not assert that discarding the common-factor phase gives cancellation; its benefit is that the common-factor sum has a harmonic cost rather than a polynomial one if the correctly normalized squarefree-column theorem is proved.

## 4. Connection to the native product machinery

The native repository already insists on retaining product collisions before squaring: CAP36 has a bilinear source pairing, and ADP37 groups complete products with their multiplicities before its phase average. The appropriate parallel here is to retain \(\mathcal W_X(r)\) exactly. Replacing it by its pointwise divisor bound would change a structured signed column into an arbitrary coefficient and lose the intended analytic theorem.

The inverse/plain product studied in `NATIVE_HEIGHT.md` has a different algebraic advantage: its full convolution is \(\mu*1=\delta_1\), so the finite defect has a zero head. The inverse/inverse product in (3.2) has no corresponding cancellation at a fixed product: for nonnegative \(W\), all its squarefree divisor allocations have the same Möbius sign. A transfer of the native inverse/plain improvement to the present fourth moment therefore needs an additional identity. These are related structured-product problems, with different local coefficients.

The most focused next theorem is (3.5), starting with \(c=1\) and then proving the stated uniform exclusion adapter. With the displayed \(H=D^{1+\theta}\), it would supply the fourth moment used by the already-checked exact prime recursion, hence the conditional limiting exponent \(17/24\). No such estimate is proved in this note.
