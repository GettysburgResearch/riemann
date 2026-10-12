# A growing collision ridge survives total-frequency balance

**Status:** proposed proved structural obstruction for the exact finite collision factor. This is not a lower bound for the signed physical row trace, a counterexample to the moment conjecture, or a proof that its open complementary trace contract is false.

**New point:** at every fixed moment order \(2k\ge4\), a source-compatible independent-frequency choice with total frequency zero makes the collision factor grow like
\[
\exp\!\left(c\,Y^{1-2\sigma}/\log Y\right),
\qquad 1/3<\sigma<1/2,
\]
uniformly over polynomially bounded rows and moving source masks. All selected frequencies tend to zero. Thus total-frequency conservation from a scale integral does not extend the proved decay on the common conjugate tube.

## 1. Exact source and the only prime-distribution input

The source is PR #911 at commit **2f8b6a3898a722d0602a91dea73bac344a3bb7dd**, in the directory research/exploratory/2026-10-10-two-hour-continuation/literature:

- PRIME_SLOT_CANCELLATION.md, P2–P4, SHA-256 d37ad696b46c7dda15a7faf314c46cda2d7d67e25ac8d3288c7f138aac373c13;
- WIDE_SUBCRITICAL_TUBE.md, WT1–WT5, SHA-256 53568631060432784811d8474e8d774257664826e8fb9fa59c0ba47959745f02;
- SHORT_POLYNOMIAL_COLLISION_TRANSPORT.md, SC1–SC6, SHA-256 c538719277b1e7de70a7e3f872fb2720668bd43ca57c9cffff6ff29b6766d5ac;
- COMPLEMENTARY_SHORT_TRACE_CONTRACT.md, CT1–CT6, SHA-256 968a2bee6d47f0a92fded0ab32c23963d31332f649dc0046604b7b568d48640c.

We use only the fixed-field prime-ideal supply
\[
\#\{\mathfrak p:Y/2<N\mathfrak p\le Y,\ \mathfrak p\notin S\}
\gg_{K,S}Y/\log Y.
\tag{1.1}
\]
This follows from the classical prime ideal theorem for the fixed Eisenstein field. The same fixed-field input is explicitly used for prime replicas in the imported October 5 paper2.tex, section sec:reduction, at OpenAI/math commit **adc7f1241b42e322a6451854ab7e4b4c146bf78a**, SHA-256 d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d. No moving-conductor prime theorem or quasi-RH zero-free hypothesis is assumed. The rest of the proof uses finite Euler algebra and the elementary ideal-count upper bound.

Fix the source finite-order coefficient character \(\nu\), its fixed bad set \(S\), and a nonzero element row \(u\). Put \(\eta_u(\mathfrak p)=\nu(\mathfrak p)\chi_{\mathfrak p}(u)\), with its literal zeros. For a moving squarefree mask \(Q\), define precisely
\[
\mathcal Q_{Y,Q,u}(\mathbf s)
=\prod_{\substack{N\mathfrak p\le Y\\\mathfrak p\notin SQ}}
\frac{1-\sum_{i=1}^{2k}z_{i,\mathfrak p}}
     {\prod_{i=1}^{2k}(1-z_{i,\mathfrak p})},
\]
\[
z_{i,\mathfrak p}=
\begin{cases}
\eta_u(\mathfrak p)(N\mathfrak p)^{-s_i},&i\le k,\\
\overline{\eta_u(\mathfrak p)}(N\mathfrak p)^{-s_i},&i>k.
\end{cases}
\tag{1.2}
\]
This is the source's \(Q_{\rm coll}\), not its finite coprime numerator and not its short polynomial \(T_{i,Y}\). A prime dividing \(u\) contributes one in (1.2).

## 2. A balanced frequency choice

Fix \(k\ge2\), and let \(n=2\lfloor k/2\rfloor\), the largest even integer at most \(k\). Write \(s_i=\sigma+it_i\). Among the first \(k\) slots take \(n/2\) frequencies equal to \(+\pi/\log Y\), \(n/2\) equal to \(-\pi/\log Y\), and, if \(k\) is odd, the one remaining frequency equal to zero. Take every right-slot frequency equal to zero. Consequently
\[
\sum_{i=1}^{2k}t_i=0,\qquad
\max_i|t_i|=\pi/\log Y.
\tag{2.1}
\]

At a nondeleted prime of norm \(q\), put \(x=\pi\log q/\log Y\) and \(a=\eta_u(\mathfrak p)\), so \(|a|=1\). Remove the common modulus \(q^{-\sigma}\) and write the remaining slot values as \(v_i\). Their sums and squared sums are
\[
\sum_{i\le k}v_i=A(x)a,\quad
\sum_{i\le k}v_i^2=B(x)a^2,\quad
A(x)=k-n+n\cos x,\quad B(x)=k-n+n\cos 2x,
\]
\[
\sum_{i>k}v_i=k\overline a,\qquad
\sum_{i>k}v_i^2=k\overline a^2.
\]
Thus the full pair sum has the exact real part
\[
\Re\sum_{i<j}v_iv_j
=kA(x)+\frac{A(x)^2-B(x)+k^2-k}{2}\Re(a^2).
\tag{2.2}
\]
All same-side pairs and all \(k^2\) cross pairs are present.

At \(x=\pi\), (2.2) becomes
\[
\begin{cases}
-k^2+k(k-1)\Re(a^2)\le-k,&k\text{ even},\\
-k(k-2)+(k-1)(k-2)\Re(a^2)\le-(k-2),&k\text{ odd}.
\end{cases}
\tag{2.3}
\]
Set \(c_k=k\) for even \(k\), and \(c_k=k-2\) for odd \(k\). Then \(c_k>0\).

Changing \(x\) from \(\pi\) by at most \(\delta\) changes each left slot by at most \(\delta\), each pair product by at most \(2\delta\), and the total pair sum by at most \(2k(2k-1)\delta\). Choose
\[
\delta_k=\frac{c_k}{4k(2k-1)},\qquad
\varepsilon_k=\delta_k/\pi.
\tag{2.4}
\]
For every \(q\ge Y^{1-\varepsilon_k}\), the complete pair sum therefore satisfies
\[
\Re\sum_{i<j}v_iv_j\le-c_k/2
\tag{2.5}
\]
uniformly in the actual ray phase \(a\).

For \(k=2\), the choice is simply
\[
(t_1,t_2;t_3,t_4)
=(\pi/\log Y,-\pi/\log Y;0,0),
\]
and (2.3) reads \(-4+2\Re(a^2)\le-2\). This is an admissible independent-frequency point of the complete fourth-moment expansion; it is not required to lie on the conjugately paired plane.

## 3. The growing factor theorem

### Theorem 3.1

Fix \(k\ge2\), \(1/3<\sigma<1/2\), and \(C>0\). For the frequency choice (2.1), there are positive constants \(c,Y_0\), depending only on the fixed data and these parameters, such that for every \(Y\ge Y_0\), every nonzero source row \(u\), and every source mask \(Q\) with \(N(u)NQ\le Y^C\), one has
\[
\boxed{
|\mathcal Q_{Y,Q,u}(\sigma+i\mathbf t)|
\ge\exp\!\left(c\,\frac{Y^{1-2\sigma}}{\log Y}\right).
}
\tag{3.1}
\]

In particular no polynomial bound in \(Y\) and the independent frequencies holds for the absolute collision factor on the hyperplane \(\sum_i t_i=0\). The theorem allows every exact incidence mask of the source, since those masks have \(NQ\le Y^k\).

**Proof.** Put \(\lambda=2\sigma\in(2/3,1)\). For sufficiently large fixed \(q\), the sum of the \(2k\) slot moduli is at most one half. The absolutely convergent logarithm series gives
\[
\log\left|
\frac{1-\sum_i z_i}{\prod_i(1-z_i)}
\right|
=-q^{-\lambda}\Re\sum_{i<j}v_iv_j+O_{k,\sigma}(q^{-3\sigma}).
\tag{3.2}
\]
The degree-one term cancels and the degree-two term is exactly the negative of the full pair sum. Since \(3\sigma>1\), the total error in (3.2) is \(O_{k,\sigma}(1)\), uniformly in all masks and phases.

The primes with \(q\ge Y^{1-\varepsilon_k}\) contribute nonnegatively to the main term, by (2.5). In particular primes in \(Y/2<q\le Y\) contribute at least a fixed positive constant times \(Y^{-\lambda}\) each. Only \(O_C(1)\) primes in this final annulus can divide \(uQ\), because their product has norm at most \(Y^C\). By (1.1), the retained final-annulus contribution is at least
\[
c_{K,k,\sigma,S}\,Y^{1-\lambda}/\log Y.
\tag{3.3}
\]

Every remaining large prime below \(Y^{1-\varepsilon_k}\) has pair sum of absolute value at most \(\binom{2k}{2}\). Ideal counting and partial summation bound their total possible negative contribution by
\[
O_{K,k,\sigma}\!\left(Y^{(1-\varepsilon_k)(1-\lambda)}\right).
\tag{3.4}
\]
This is little-oh of (3.3).

It remains to bound the finitely many small-prime factors from below; zeros cannot simply be disregarded. Their numerator, at the present frequency choice, is exactly
\[
1-q^{-\sigma}\big[(k-n+n\cos x)a+k\overline a\big],
\qquad x=\pi\log q/\log Y.
\tag{3.5}
\]
As \(Y\to\infty\), this tends to \(1-kq^{-\sigma}(a+\overline a)\). If that limit is nonzero, the numerator is bounded away from zero. If it vanishes, (3.5) equals exactly \(nq^{-\sigma}a(1-\cos x)\), whose modulus is bounded below by a positive constant times \((\log Y)^{-2}\). Here \(n\ge2\). At each fixed small prime there are only finitely many possible values of \(a\), because \(\nu\) has fixed finite order and the row symbol is sextic. These lower bounds are therefore uniform in the row. A deleted small prime contributes one. The denominators in (1.2) are nonzero and bounded above by fixed constants. The complete small-prime contribution to the logarithm is consequently at least \(-O_{k,\sigma,S,\nu}(\log\log Y)\).

Combining (3.2)–(3.5) proves that the logarithm in (3.1) is at least a positive constant times \(Y^{1-\lambda}/\log Y\), once \(Y\) is large enough. All forced zero masks were retained. \(\square\)

## 4. What this changes, and what it does not show

The paid common conjugate tube requires the left frequencies to be close to one common \(t\), and the right frequencies to be close to \(-t\), with width at most a fixed small constant divided by \(\log Y\). The frequencies in (2.1) are outside that tube: two left slots are separated by \(2\pi/\log Y\). Nevertheless their total sum is zero. A scalar scale integral enforcing only total-frequency balance therefore cannot remove this growing ridge.

At order two (\(k=1\)), total-frequency balance forces the two frequencies to be conjugately paired. The construction needs at least four slots. This precisely distinguishes the useful pair geometry in the second-moment source from the independent-frequency geometry which a higher-moment extension must handle.

Theorem 3.1 is a modulus theorem for \(\mathcal Q\). The open source contract CT1 also contains the actual short Möbius polynomials, the exact exterior incidence multiplier, and a signed sum over physical rows. Those factors can cancel. This note does not bound them below, does not remove them, and does not declare CT1 false.

Its implication for strategy is substantive. CT1 asks for a polynomial bound before the physical norm tests are applied. On the displayed ridge, bounding the other factors independently by polynomial envelopes cannot control \(\mathcal Q\); one would need cancellation of its stretched-exponential inflation inside the literal signed trace. The source's complete norm-filtered coefficient identity is only polynomially large by direct counting, so cancellations across the independent Mellin frequencies are already essential. A bound for the filtered, coupled primitive covariance is a better scoped target than an absolute bound on the collision factor, and may be much weaker than CT1.

The theorem applies uniformly to every polynomially bounded physical row range and every eligible incidence allocation. It does not claim a lower bound after an unrestricted Schwartz row sum, a finite-height covariance lower bound, or an arithmetic saving. No zero-free boundary is changed.
