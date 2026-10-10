# An all-row sextic sieve and a proved large-gcd fourth-moment range

Status: proved consequences of the established squarefree sextic large sieve. These results do not assume the proposed fourth moment or an improved zero-free region.

Scope: the Eisenstein field, fixed excluded column primes, all nonzero element rows, arbitrary squarefree column coefficients, and the exact gcd decomposition of the inverse square. The remaining small-gcd contribution is not bounded at the desired scale here.

Primary input: Blomer–Goldmakher–Louvel, *L-functions with n-th order twists*, Theorem 1.3, [arXiv:1112.1650](https://arxiv.org/abs/1112.1650). In the source's primary-element convention, the same estimate is stated as Lemma "Sextic large sieve", label lem:sextic-large-sieve, in the [September 30 manuscript at adc7f124](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex).

## 1. Conventions and squarefree input

Let \(K=\mathbb Q(\sqrt{-3})\), \(\mathcal O=\mathbb Z[\omega]\), and \(N\) be the ideal norm or element norm as appropriate. Columns \(n\) denote integral ideals prime to a fixed finite set \(S\), with primary generators used in sextic symbols. The character \(\chi_n(u)\) retains its zero extension when a column prime divides \(u\).

All constants may depend on \(K,S\), the fixed smooth tests and the indicated positive exponent loss. They are uniform in any moving exclusions inserted in column coefficients.

The squarefree sieve input says, for arbitrary complex coefficients \(a_n\) on squarefree columns \(Nn\le L\),

\[
\sum_{\substack{Na\le M\\a\ {\rm squarefree}\\(a,S)=1}}
\left|\sum_n a_n\chi_n(a)\right|^2
\ll_\epsilon (ML)^\epsilon
\left(M+L+(ML)^{2/3}\right)\sum_n|a_n|^2.
\tag{1.1}
\]

The finite primary/ray reciprocity factors can be separated into a fixed finite number of row and column classes. This is the source convention in the cited lemma. Unit multiples of a primary row multiply each column by a fixed unit phase and are handled by the same arbitrary-coefficient estimate. The six units change only the constant.

## 2. Extending the sieve to every element row

### Proposition 2.1

For \(H,L\ge1\) and arbitrary squarefree column coefficients supported on \(Nn\le L\),

\[
\boxed{
\sum_{\substack{u\in\mathcal O\\0<Nu\le H}}
\left|\sum_n a_n\chi_n(u)\right|^2
\ll_\epsilon (HL)^\epsilon
\left(H+H^{1/2}L+(HL)^{2/3}\right)
\sum_n|a_n|^2 .
}
\tag{2.1}
\]

In particular, if \(L\le H^{1/2}\), this is at most
\((HL)^\epsilon H\sum|a_n|^2\).

**Proof.** Factor the ideal of each nonzero row uniquely as

\[
(u)=a b,
\]

where \(a\) is the product of the primes whose valuation in \((u)\) is exactly one, while \(b\) consists of all prime powers of valuation at least two. Thus \(a\) is squarefree, \(b\) is powerful, and \((a,b)=1\). Include a unit after choosing primary generators outside the fixed bad primes.

The primes of \(S\) that occur to valuation one are a divisor \(q\) of the fixed product of primes in \(S\). Fix this \(q\), the unit, and \(b\). The remaining \(a\) is squarefree and prime to \(S\), with norm at most \(H/(Nq\,Nb)\). By complete multiplicativity, the factors \(\chi_n(qb)\) and the unit character can be absorbed into \(a_n\). Their absolute values are at most one, and they are independent of the varying squarefree row. The restriction \((a,b)=1\) can be discarded after taking the absolute square, since the summands are nonnegative.

Apply (1.1) for each \(b\). Since there are only finitely many \(q\), their norms affect only the constant. It remains to sum

\[
(HL)^\epsilon
\sum_{\substack{Nb\le H\\b\ {\rm powerful}}}
\left(\frac H{Nb}+L+
\left(\frac{HL}{Nb}\right)^{2/3}\right)
\sum_n|a_n|^2 .
\tag{2.2}
\]

No zero-extension factor has been removed: all factors from \(b,q\), and the unit are in the fixed coefficient vector for that application of the sieve.

A powerful ideal has a unique representation \(b=c^2d^3\) with \(d\) squarefree: use exponent zero in \(d\) for an even valuation and exponent one for an odd valuation at least three. Elementary ideal counting therefore gives

\[
\#\{b\ {\rm powerful}:Nb\le R\}
\ll R^{1/2}\sum_d(Nd)^{-3/2}\ll R^{1/2}.
\tag{2.3}
\]

The associated Dirichlet sums converge at every real exponent \(s>1/2\); alternatively,
\[
\sum_{b\ {\rm powerful}}(Nb)^{-s}
\le \zeta_K(2s)\zeta_K(3s)<\infty .
\]
Consequently the \(b^{-1}\) and \(b^{-2/3}\) sums in (2.2) are bounded, whereas the unweighted sum is \(O(H^{1/2})\). This proves (2.1). If \(L\le H^{1/2}\), each of its three terms is \(O(H)\). \(\square\)

This is an elementary extension of an established sieve, not a claim that its exponent is a new large-sieve record. It is useful here because it includes the target's sixth-power rows and permits arbitrary moving column masks.

## 3. Apply the all-row sieve to the balanced squarefree core

Fix a bounded smooth function \(W\) supported in \([a,b]\subset(0,\infty)\), a fixed finite-order Hecke character \(\nu\), and the fixed exclusions \(S\). For \(X\ge1\), set

\[
B_{c,u}(X)=
\sum_{\substack{r\ {\rm squarefree}\\(r,cS)=1}}
\mu_K(r)\nu(r)\chi_r(u)\mathcal W_X(r),
\]
\[
\mathcal W_X(r)=
\sum_{d\mid r}W(Nd/X)
W\!\left(\frac{Nr}{XNd}\right).
\tag{3.1}
\]

The squarefree coefficient is supported on \(Nr\le b^2X^2\). The divisor bound, the \(O_W(X^2)\) pairs of supported factors and boundedness of \(W\) give

\[
\sum_r|\mu_K(r)\nu(r)\mathcal W_X(r)1_{(r,cS)=1}|^2
\ll_{W,\epsilon}X^{2+\epsilon}.
\tag{3.2}
\]

For completeness, bound one divisor multiplicity in the square by \(O_\epsilon((Nr)^\epsilon)\), and sum the absolute weight over the pairs of ideals of norm \(O_W(X)\). Removing the coprimality mask only enlarges this upper bound. Its constant is independent of \(c\).

Taking \(L\asymp_W X^2\) in Proposition 2.1 gives the proved estimate

\[
\boxed{
\sum_{0<Nu\le H}|B_{c,u}(X)|^2
\ll_{W,\epsilon}(HX)^\epsilon
\left(HX^2+H^{1/2}X^4+H^{2/3}X^{10/3}\right).
}
\tag{3.3}
\]

This is uniform in every moving \(c\). It supplies the desired \(HX^2\) bound when \(X\ll_W H^{1/4}\). For bounded \(X<1\) with nonempty support, the polynomial has a fixed finite number of columns and is bounded directly by \(O_W(H)\).

## 4. The large-gcd part of the actual fourth moment

The exact inverse-square identity is

\[
A_u(D)^2=
\sum_{\substack{c\ {\rm squarefree}\\(c,S)=1}}
\mu_K(c)^2\nu(c)^2\chi_c(u)^2 B_{c,u}(D/Nc).
\tag{4.1}
\]

For \(1\le C\le D\), let \(T_{\ge C,u}(D)\) denote its entire sum over \(Nc\ge C\). The coefficients in (4.1) have not been modified; this is an actual part of \(A_u(D)^2\).

### Theorem 4.1

For \(D,H\ge2\),

\[
\boxed{
\sum_{0<Nu\le H}|T_{\ge C,u}(D)|^2
\ll_{W,\nu,S,\epsilon}(DH)^\epsilon
\left(
HD^2+\frac{H^{1/2}D^4}{C^2}
+\frac{H^{2/3}D^{10/3}}{C^{4/3}}
\right).
}
\tag{4.2}
\]

In particular, when

\[
C\ge \max(1,DH^{-1/4}),
\tag{4.3}
\]

the entire large-gcd contribution has the target fourth-moment size

\[
\sum_{0<Nu\le H}|T_{\ge C,u}(D)|^2
\ll (DH)^\epsilon HD^2.
\tag{4.4}
\]

**Proof.** Multiplication by \(\chi_c(u)^2\) contracts the row \(\ell^2\) norm. Minkowski and the square root of (3.3), with \(X=D/Nc\), give

\[
\|T_{\ge C}\|_2
\ll (DH)^\epsilon
\left[
D H^{1/2}\sum_{C\le Nc\le D}\frac1{Nc}
+D^2H^{1/4}\sum_{Nc\ge C}\frac1{(Nc)^2}
+D^{5/3}H^{1/3}\sum_{Nc\ge C}\frac1{(Nc)^{5/3}}
+D H^{1/2}
\right].
\tag{4.5}
\]

The last term covers \(D<Nc\le bD\), if present: each such residual factor has bounded norm, there are \(O_W(D)\) labels, and its row norm is \(O_W(H^{1/2})\). The ideal harmonic sum is \(O(\log(2D))\), and the two convergent tails are respectively \(O(C^{-1})\) and \(O(C^{-2/3})\), by ideal counting and partial summation. Squaring (4.5), using \((x+y+z)^2\le3(x^2+y^2+z^2)\), and absorbing logarithms proves (4.2), after choosing smaller preliminary exponent losses.

Under (4.3), \(H^{1/2}D^4/C^2\le HD^2\) and
\(H^{2/3}D^{10/3}/C^{4/3}\le HD^2\). This proves (4.4). \(\square\)

### Near-linear row length

At the target \(H=D^{1+\theta}\), \(0<\theta\le1/10\), the cutoff is

\[
C_0=D^{\,3/4-\theta/4}.
\tag{4.6}
\]

All common-factor contributions with \(Nc\ge C_0\) therefore have the required fourth-moment size without a new arithmetic hypothesis.

Let \(T_{<C_0}=A^2-T_{\ge C_0}\). The full desired fourth moment is equivalent, up to constants and arbitrarily small exponent losses, to the same \(HD^2\) estimate for \(T_{<C_0}\): use both triangle inequalities in the row \(\ell^2\) space and (4.4). Thus this theorem removes a specified part of the actual moment; it does not merely alter the coefficient class of an unproved estimate.

The small-gcd region includes \(c=1\), where the two factors are coprime and the residual product length is \(D^2\). That region is not controlled at the target size by this argument.

## 5. Scope of the remaining problem

The fourth-moment conclusion \(HD^2\) for all gcds, the \(17/24\) zero-free consequence and the all-\(k\) moment theorem remain unproved. The present result relies on the established squarefree sextic sieve and elementary ideal estimates. It does not rely on the imported quasi-Riemann theorem or the new conditional constant refinement.

The same all-row sieve resolves general-\(k\) incidence configurations whose remaining singleton product length is at most \(H^{1/2}\). The exact normalized summation of those configurations is proved in the companion general-moment note; multiple shared factors must be counted by their incidence sets, not independently inserted as new coefficient freedom.
