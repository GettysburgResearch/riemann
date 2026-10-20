# Universal Hecke zero-freeness: all Artin representations and Chebotarev intervals

Date: 2026-10-20.

## Status and external input

This note proves two consequences of a universal finite-order Hecke zero-free half-plane: the same half-plane for **all finite-image Artin representations**, including nonmonomial representations, and a power-saving Chebotarev theorem for each fixed finite Galois extension. The numerical boundary is preserved. This is an extension of the families and consequences, not an improvement of the numerical boundary.

For a real number \(B\in[1/2,1)\), write \(\mathrm H(B)\) for the assertion

\[
 L_E(s,\eta)\ne0\qquad (\operatorname{Re}s>B)
 \tag{H}
\]

for every number field \(E\) and every finite-order Hecke character \(\eta\), with the principal pole at \(s=1\) permitted.

Baiying Liu, *Zero-free half-planes for Hecke L-functions over number fields*, [arXiv:2610.26835v1](https://arxiv.org/abs/2610.26835v1), Theorem 17.1, asserts \(\mathrm H(B_\flat)\), where

\[
 B_\flat=0.874886647039964\ldots,
 \qquad
 133488B_\flat^4-376596B_\flat^3+384534B_\flat^2
       -167541B_\flat+26231=0.
\]

The root is specified by its interval near \(0.8749\). In the source, the all-field passage is Theorem 18.2 followed by Proposition 19.1. Its Corollary 19.2(2) explicitly lists monomial Artin representations and their direct sums. The arguments below remove that representation restriction by classical Brauer induction. Instantiation at \(B_\flat\) inherits the external analytic input (H); the implication proved here does not independently certify Liu's complete analytic proof.

## 1. Brauer closure of a zero-free half-plane

Let \(L/K\) be a finite Galois extension, let \(G=\operatorname{Gal}(L/K)\), and let \(\rho\) be a finite-dimensional complex representation of \(G\). Use the full Artin Euler factors, including the factors at ramified primes. Put

\[
 m(\rho)=\dim V_\rho^G=\langle\chi_\rho,1_G\rangle_G.
\]

### Theorem 1

Assume \(\mathrm H(B)\). Then

\[
 (s-1)^{m(\rho)}L_K(s,\rho)
 \tag{1.1}
\]

extends to a holomorphic, nowhere-zero function on \(\operatorname{Re}s>B\), where its value at \(s=1\) is supplied by continuation. Consequently:

- \(L_K(s,\rho)\) has no zeros and no poles on that half-plane away from \(1\).
- Its pole at \(1\), if present, has order exactly \(m(\rho)\).
- If \(\rho\) contains no invariant vectors, its Artin \(L\)-function is holomorphic and nowhere zero throughout the half-plane.

This applies to every continuous finite-image complex Galois representation, by choosing a finite Galois extension through which it factors.

### Proof

Brauer's induction theorem supplies subgroups \(H_i\leq G\), one-dimensional characters \(\lambda_i:H_i\to\mathbb C^\times\), and integers \(n_i\), possibly negative, such that

\[
 \chi_\rho=\sum_{i=1}^r n_i\operatorname{Ind}_{H_i}^G\lambda_i.
 \tag{1.2}
\]

Set \(K_i=L^{H_i}\). Each \(\lambda_i\) factors through the finite abelian group \(H_i/\ker\lambda_i\); class field theory therefore identifies it with a finite-order Hecke character \(\eta_i\) of \(K_i\). Additivity and inductivity of the full Artin Euler factors give

\[
 L_K(s,\rho)=\prod_{i=1}^r L_{K_i}(s,\eta_i)^{n_i}
 \tag{1.3}
\]

first for \(\operatorname{Re}s>1\), and then as a meromorphic identity. These are standard Brauer-Artin facts; useful source locators are [Cogdell, pp. 10-12, equation (2) and the discussion of ramified factors](https://math.osu.edu/~cogdell/artin-www.pdf), and [Milne, *Class Field Theory*, v4.03, VIII Section 10](https://www.jmilne.org/math/CourseNotes/CFT.pdf). The original Brauer reference is listed below.

Let \(e_i=1\) if \(\eta_i\) is principal, and \(e_i=0\) otherwise. By (H) and the simple-pole theorem for Dedekind zeta functions,

\[
 U_i(s)=(s-1)^{e_i}L_{K_i}(s,\eta_i)
\]

is holomorphic and nowhere zero on \(\operatorname{Re}s>B\). This includes \(s=1\): a nonprincipal factor is nonzero there, while a principal factor has a nonzero zeta residue. Thus every integer power \(U_i^{n_i}\) is holomorphic and nowhere zero there, even when \(n_i<0\).

Taking the inner product of (1.2) with the trivial character and applying Frobenius reciprocity gives

\[
 m(\rho)
 =\sum_i n_i\langle\operatorname{Ind}_{H_i}^G\lambda_i,1_G\rangle_G
 =\sum_i n_i\langle\lambda_i,1_{H_i}\rangle_{H_i}
 =\sum_i n_i e_i.
 \tag{1.4}
\]

Equations (1.3)-(1.4) now give

\[
 (s-1)^{m(\rho)}L_K(s,\rho)=\prod_i U_i(s)^{n_i},
\]

which proves every assertion. No cancellation claim about unknown zeros is needed: the individual Hecke factors have no zeros anywhere in the region in question. \(\square\)

### Virtual representations and operations

The same proof applies to any virtual representation \(\tau\in R(G)\), with \(m(\tau)=\langle\tau,1_G\rangle_G\in\mathbb Z\). Away from \(1\), its meromorphic Artin function is a holomorphic unit. At \(1\), its order is exactly \(-m(\tau)\); a negative \(m(\tau)\) gives a zero of order \(-m(\tau)\). Tensor products, symmetric powers, exterior powers, duals, and induced representations of finite-image representations remain finite-image representations, so Theorem 1 covers their Artin functions as well.

Finite omission of Euler factors does not change the half-plane assertion: their eigenvalues are roots of unity, and each nonconstant factor \(1-\alpha(N\mathfrak p)^{-s}\) has zeros on \(\operatorname{Re}s=0\). This observation is not a substitute for using full Euler factors in the induction identity; it only records the consequence for incomplete functions afterward.

## 2. A fixed-character prime-sum lemma

We give the analytic step explicitly, so the Chebotarev conclusion does not require assuming the global Artin holomorphy conjecture or applying an unproved global Artin zero formula.

For a number field \(E\), define the ideal von Mangoldt function by

\[
 \Lambda_E(\mathfrak a)=
 \begin{cases}
 \log N\mathfrak p,&\mathfrak a=\mathfrak p^r,\ r\geq1,\\
 0,&\text{otherwise}.
 \end{cases}
\]

### Lemma 2

Fix \(E\) and a finite-order Hecke character \(\eta\). If its \(L\)-function has no zeros in \(\operatorname{Re}s>B\), allowing the principal pole at \(1\), then for every \(a\in(B,1)\),

\[
 \sum_{N\mathfrak a\leq x}\Lambda_E(\mathfrak a)\eta(\mathfrak a)
 =e_\eta x+O_{E,\eta,a}\bigl(x^a(\log(2x))^2\bigr),
 \qquad x\geq2,
 \tag{2.1}
\]

where \(e_\eta=1\) for a principal character and zero otherwise. In particular the error is \(O_{E,\eta,\epsilon}(x^{B+\epsilon})\) for every \(\epsilon>0\).

### Proof

One can remove the finitely many extra Euler factors of an imprimitive presentation at a cost \(O_{E,\eta}(\log(2x))\) in the sum. It therefore suffices to treat a primitive character, including the principal zeta function.

The completed primitive finite-order Hecke function, after cancellation of the principal poles, is entire of order one. Its Hadamard product and its fixed-character local zero count

\[
 \#\{\rho:|\operatorname{Im}\rho-t|\leq1\}
 \ll_{E,\eta}\log(|t|+3)
 \tag{2.2}
\]

give, uniformly for \(a\leq\sigma\leq2\) and \(|t|\geq2\),

\[
 -\frac{L_E'}{L_E}(\sigma+it,\eta)
 \ll_{E,\eta,a,B}\log(|t|+3).
 \tag{2.3}
\]

For precision, subtract the logarithmic derivative at \(2+it\) in the partial-fraction expansion. Zeros with \(|\operatorname{Im}\rho-t|\leq1\) have distance at least \(a-B>0\) from the line, and contribute \(O_{E,\eta,a,B}(\log(|t|+3))\) by (2.2). The difference of the two reciprocals for distant zeros is \(O_a((1+|t-\operatorname{Im}\rho|)^{-2})\); summing the unit-height zero counts proves the same bound for them. The gamma terms are bounded by Stirling's formula; the value at \(2+it\) is bounded by its absolutely convergent series. For a primary reference for the completed Hecke function and (2.2), see [Thorner-Zaman, arXiv:1803.02823v3, Section 2.3 and Lemma 2.5](https://arxiv.org/abs/1803.02823v3); their Section 4.2 also gives a smoothed explicit formula.

Write

\[
 -\frac{L_E'}{L_E}(s,\eta)=\sum_{n\geq1}\frac{A_\eta(n)}{n^s}.
\]

Its coefficients vanish unless \(n\) is a rational prime power, and

\[
 |A_\eta(p^r)|
 \leq \log p\sum_{\substack{\mathfrak p\mid p\\f(\mathfrak p/p)\mid r}}
 f(\mathfrak p/p)
 \leq [E:\mathbb Q]\log p.
 \tag{2.4}
\]

Choose \(X=\lfloor x\rfloor+1/2\), \(c=1+1/\log X\), and \(T=X^2\). The sums up to \(X\) and \(x\) are identical. Truncated Perron inversion, using (2.4) and the distance of \(X\) from every integer, has an error \(O_E((\log(2X))^2)\). Shift its vertical contour from \(c\) to \(a\). Only the principal logarithmic-derivative pole at \(s=1\) is crossed, contributing \(e_\eta X\). Equation (2.3) bounds the horizontal segments by \(O(X^c\log T/T)\) and the vertical segment by

\[
 O_{E,\eta,a}\left(X^a\left(1+\int_2^T\frac{\log t}{t}\,dt\right)\right)
 =O_{E,\eta,a}(X^a(\log(2X))^2).
\]

The bounded-height portion of the line is compact and zero-free. Replacing \(X\) by \(x\) in the main term costs \(O(1)\). This proves (2.1). Choosing \(B<a<B+\epsilon\) and absorbing the logarithms proves the final assertion. \(\square\)

## 3. General Chebotarev prime counts

For a class function \(f:G\to\mathbb C\), put

\[
 \overline f=\frac1{|G|}\sum_{g\in G}f(g),
 \qquad
 \Psi_f(x)=\sum_{\substack{\mathfrak p\text{ unramified in }L\\r\geq1,
                          \ (N\mathfrak p)^r\leq x}}
 f(\operatorname{Frob}_{\mathfrak p}^{\,r})\log N\mathfrak p.
 \tag{3.1}
\]

Here \(\operatorname{Frob}_{\mathfrak p}\) denotes a conjugacy class; a class function makes (3.1) well-defined. Powers of Frobenius, not Frobenius itself, occur at prime powers.

### Theorem 3

Assume \(\mathrm H(B)\), and fix \(L/K\) and \(f\). For every \(\epsilon>0\),

\[
 \Psi_f(x)=\overline f\,x+
 O_{L/K,f,\epsilon}(x^{B+\epsilon}).
 \tag{3.2}
\]

If \(C\subseteq G\) is a union of conjugacy classes and

\[
 \pi_C(x;L/K)=\#\{\mathfrak p\text{ unramified in }L:
        N\mathfrak p\leq x,\ \operatorname{Frob}_{\mathfrak p}\subseteq C\},
\]

then

\[
 \pi_C(x;L/K)=\frac{|C|}{|G|}\operatorname{Li}(x)
       +O_{L/K,C,\epsilon}(x^{B+\epsilon}).
 \tag{3.3}
\]

### Proof

Expand \(f\) in the orthonormal basis of irreducible characters:

\[
 f=\sum_{\rho\in\widehat G}\langle f,\chi_\rho\rangle_G\chi_\rho.
\]

For each \(\rho\), differentiate the finite Brauer factorization (1.3). The logarithmic derivative of its Artin Euler product has coefficient
\(\operatorname{tr}\rho(\operatorname{Frob}_{\mathfrak p}^{\,r})\log N\mathfrak p\)
at an unramified prime power. At each ramified prime the coefficient is the corresponding trace on the inertia-invariant space, bounded by \(\dim\rho\). Removing all ramified-prime powers costs \(O_{L/K,\rho}(\log(2x))\).

On the Hecke side of the differentiated identity, apply Lemma 2 to its finitely many characters over the fields \(K_i\). The sum of the main terms is

\[
 x\sum_i n_i e_i=m(\rho)x
\]

by (1.4). Thus \(\Psi_{\chi_\rho}(x)=m(\rho)x+O(x^{B+\epsilon})\). Only the trivial irreducible representation has \(m(\rho)=1\); its coefficient in the class expansion is \(\overline f\). Finite linear combination proves (3.2).

For \(f=1_C\), remove powers \(r\geq2\). They contribute
\(O_K(x^{1/2}(\log(2x))^2)\), since every underlying prime ideal then has norm at most \(x^{1/2}\). This fits the error as \(B\geq1/2\). The resulting weighted prime sum is

\[
 \vartheta_C(x)=\frac{|C|}{|G|}x+O_{L/K,C,\epsilon}(x^{B+\epsilon}).
\]

Partial summation, with a smaller positive epsilon first if necessary, gives (3.3). \(\square\)

## 4. Short intervals with prescribed Frobenius

### Corollary 4

Assume \(\mathrm H(B)\). Fix a finite Galois extension \(L/K\), a nonempty union \(C\) of conjugacy classes, and \(\alpha\) with \(B<\alpha<1\). Then

\[
 \pi_C(x+x^\alpha;L/K)-\pi_C(x;L/K)
 \sim \frac{|C|}{|G|}\frac{x^\alpha}{\log x}
 \qquad (x\longrightarrow\infty).
 \tag{4.1}
\]

In particular every sufficiently large interval \((x,x+x^\alpha]\) contains a prime ideal of the prescribed Frobenius type.

### Proof

Apply (3.3) with \(\epsilon=(\alpha-B)/2\). Subtract at \(x+x^\alpha\) and \(x\). Since \(\alpha<1\),

\[
 \operatorname{Li}(x+x^\alpha)-\operatorname{Li}(x)
 \sim x^\alpha/\log x.
\]

The two error terms total \(O(x^{(B+\alpha)/2})\), whose ratio to the main-term scale is
\(O(x^{-(\alpha-B)/2}\log x)=o(1)\). Nonemptiness of \(C\) makes the limiting main coefficient positive. \(\square\)

At Liu's boundary, one can take any fixed \(\alpha>0.874886647039964\ldots\), for example \(\alpha=0.88\). This includes prescribed splitting patterns of a fixed separable polynomial: take its splitting field and the union of Frobenius classes with the required cycle type. For base field \(K=\mathbb Q\), these are ordinary rational primes.

The extension, character data, and \(\alpha\) are fixed in (4.1). The proof supplies no numerical onset uniform in degree, discriminant, or conductor, and gives no conclusion at \(\alpha=B\). It also supplies neither a smaller \(B\) nor global Artin holomorphy. The gain is the passage from universal abelian analytic inputs to arbitrary finite Galois representations and splitting conditions without loss in the boundary.

## References and checked locators

1. Baiying Liu, *Zero-free half-planes for Hecke L-functions over number fields*, [arXiv:2610.26835v1](https://arxiv.org/abs/2610.26835v1), submitted 2026-10-19. External numerical input: Theorem 17.1; transfer: Theorem 18.2 and Proposition 19.1; explicitly stated Artin consequence: Corollary 19.2(2). PDF SHA-256: `5d0fd10274c8444c789b0b7925a1cd3419017fe760be3219b6be51d7fbed9bd5`.
2. Richard Brauer, *On Artin's L-series with general group characters*, Annals of Mathematics (2) **48** (1947), 502-514, [DOI 10.2307/1969183](https://doi.org/10.2307/1969183). Original induction reference; the bibliographic data and the needed integer-induction statement were cross-checked through the author-hosted reference below, rather than a newly inspected copy of the 1947 article.
3. James W. Cogdell, *On Artin L-functions*, [author-hosted manuscript](https://math.osu.edu/~cogdell/artin-www.pdf). Page 10, equation (2): Brauer factorization with integer exponents. Pages 11-12: ramified Euler factors and inductivity. The needed statements were inspected.
4. J. S. Milne, *Class Field Theory*, version 4.03 (2020), [author's notes](https://www.jmilne.org/math/CourseNotes/CFT.pdf), VIII Section 10, *More on L-series*: induction, Hecke identification, and integral factorization; global class-field and zeta residue background elsewhere in the notes.
5. Jesse Thorner and Asif Zaman, *A unified and improved Chebotarev density theorem*, [arXiv:1803.02823v3](https://arxiv.org/abs/1803.02823v3), Algebra & Number Theory **13** (2019), 1039-1068, [DOI 10.2140/ant.2019.13.1039](https://doi.org/10.2140/ant.2019.13.1039). Section 2.3: completed finite-order Hecke functions; Lemma 2.5: local zero count; Section 4.2: explicit-formula argument. Used for these classical analytic ingredients, not as a source asserting the new numerical value.
