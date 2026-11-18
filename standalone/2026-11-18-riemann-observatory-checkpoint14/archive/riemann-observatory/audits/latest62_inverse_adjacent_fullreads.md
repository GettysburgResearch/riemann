# Two primary readings on finite moment recovery and indeterminate operators

17 November 2026. Read all 12 published pages of Laurent–Mourrain, *A generalized flat extension theorem for moment matrices* (Arch. Math. 93 (2009), 87–98), and all 15 PDF pages, §§1–4 and references, of Berg, *Indeterminate Stieltjes moment problems revisited*, arXiv:2407.08511v1. This note records exact interfaces to the prefix inversion lemma. The analytic input from zeta that yields its moments remains the separate [prefix theorem](adversarial_reviews/director_prefix_inverse_round8.md).

## Laurent–Mourrain, sparse flat extension

Theorem 1.4 uses a finite monomial set \(C\) connected to 1, its one-variable-step border enlargement \(C^+\), and a moment sequence on \(C^+\cdot C^+\). If \(M_{C^+}\) has the same rank as its restriction \(M_C\), there is a unique full Hankel moment matrix extending the data with that rank. In real coordinates, positivity of the given matrix then supplies a finite positive atomic representing measure in Theorem 3.2 and prior Theorem 1.1. Flatness means actual exact rank equality, and does not follow from a small singular value of a noisy input. In the non-positive algebraic version the conclusion is a functional rather than a representing positive measure.

The proof of Theorem 1.5 uses (2.1) to test the kernel of the larger Hankel operator against \(C\) alone. It gives (2.2), the truncated multiplication of a kernel vector provided its product stays within \(C^+\). Choose an invertible principal submatrix indexed by \(B\subseteq C\), containing 1 if the functional is nonzero, and project polynomial coordinates to \(\operatorname{span}B\) along the truncated kernel. Lemma 2.1 proves that the compressed multiplications commute by testing the commutator against \(C\). The two candidate products in its numerator need not individually belong to the border span, but the difference does by the displayed commutator identity. Evaluation of polynomials at the commuting multiplications on the vector 1 defines \(\varphi\). In Lemma 2.2 the predecessor of \(m\in C^+\setminus\{1\}\) is chosen in \(C\), which the connected-to-1 and border hypotheses allow. This is the choice ensuring the next step of truncated multiplication applies. Lemma 2.3 proves \(\widetilde\Lambda=\Lambda\circ\varphi\) extends all the tested products. The kernel generates the entire relation ideal, fixing the extension uniquely at the same rank. Section 3 gives an example where no selected column basis is connected to 1 even though \(C\) is, and describes moment SDP and real radical uses. The separate example in §1.3 shows why disconnected \(C\) cannot be granted the theorem just because the ranks agree.

For the prefix moments \(M_j=\int x^j\,d\nu(x)\), if the exact Hankel matrix \(H_r=(M_{i+j})_{i,j=0}^r\) is singular, any positive representing measure is supported on the common zero set of its kernel polynomials. Indeed \(c^TH_rc=\int|p(x)|^2d\nu\), so \(p\) vanishes almost everywhere for every kernel vector \(c\). If the measure has exactly \(r\) distinct nodes, \(H_{r-1}\) has rank \(r\) and \(H_r\) is flat; recover the monic annihilator and solve for the weights via Vandermonde. Conversely an exact flat PSD block with moments through \(2r\) gives a unique finite atomic representation. In the prefix problem these moments need Taylor coefficients through \(b^{2r+1}\); \(C(0)\) gives the remaining simple mass. The Hankel conclusion does not infer finite support from finite precision. A measure with infinitely many positive distinct atoms has each \(H_r\) positive definite.

### A simpler certificate using the exact triangular lattice

For the proven prefix map let \(\mu_m=m(m-1)\) and \(\nu\{\mu_m\}=\mu_m^2W_m\) for \(m\ge2\). Exact prior knowledge of this lattice permits stronger one-sided certificates than positivity on \([0,\infty)\) alone. For any integer \(M\ge2\), write
\[
 P_M(x)=\prod_{m=2}^M(x-\mu_m).
\]
On the lattice, \(P_M\) vanishes at all nodes through \(M\) and is strictly positive and increasing beyond \(M\). Thus
\[
 \sum_{m>M}\mu_m^2W_m\ \le\
 \frac{\int P_M(x)\,d\nu(x)}{P_M(\mu_{M+1})},
 \qquad
 P_M(\mu_{M+1})=\frac{(M-1)!(2M)!}{(M+1)!}.
\]
The product formula uses \(\mu_{M+1}-\mu_m=(M+1-m)(M+m)\). This needs \(M_0,\ldots,M_{M-1}\), equivalently the coefficients of \(b^1,\ldots,b^M\) of \(C\). An exactly zero integral certifies no tail beyond \(M\), so once \(C(0)\) is supplied the remaining weights can be solved on the predetermined lattice by Vandermonde. An interval upper bound on the integral gives an enclosure for the total tail without implying a bound on the maximum multiplicity. The classical finite-data counterexamples in the [prefix theorem](adversarial_reviews/director_prefix_inverse_round8.md) remain compatible, since an arbitrary finite datum need not saturate this polynomial inequality.

For a single known node \(\mu_m\), let \(d_m=\min_{j\ge2,j\ne m}|\mu_j-\mu_m|\), so \(d_2=4\) and \(d_m=2(m-1)\) for \(m\ge3\). The polynomial \(1-(x-\mu_m)^2/d_m^2\) is at most the indicator of that node throughout the lattice. The first three moments therefore give
\[
 \mu_m^2 W_m \ \ge\
 M_0-\frac{M_2-2\mu_m M_1+\mu_m^2 M_0}{d_m^2}.
\]
A positive certified right side proves a nonzero atom without reconstructing the others. Neither lattice inequality is a result about finite-\(N\) staircase derivatives, because they require true limiting Taylor moments or their rigorous enclosures. The identities have not been asserted as literature priority.

## Berg, Stieltjes indeterminacy and Jacobi extensions

The standing hypothesis is a normalized moment sequence which is Stieltjes and indeterminate on \(\mathbb R\). The orthonormal and second-kind polynomials determine the same Jacobi operator on finitely supported sequences for every representing measure. Its closure has deficiency indices \((1,1)\); the \(N\)-extremal measures arise as cyclic spectral measures at \(e_0\) of its different self-adjoint extensions. Sections 2 and 3 use the four Nevanlinna functions \(A,B,C,D\) and their determinant equal to 1, together with the differential sums of squares in (22)–(23) for strict zero interlacing. Proposition 3.1 uses the classical \(\alpha(s)=\lim_{x\to-\infty}D(x)/B(x)\le0\). The half-line problem can be determinate despite Hamburger indeterminacy if \(\alpha=0\). The \(N\)-extremal solutions with nonnegative support have parameters \(\alpha\le t\le0\), and the endpoint solutions are Friedrichs and Krein. Proposition 3.2 proves the same \(\alpha\) from \(C/A\) by subtracting the determinant identity at negative \(x\).

When \(\alpha<0\), Theorem 3.4 identifies the strictly positive Friedrichs support as the increasing limits of the polynomial zeros, where the limit is taken in degree for each fixed index. Rouché works locally with the normalized limit (30). To exclude additional limiting zeros, note that any compact range contains only a bounded set of possible polynomial-zero indices since \(x_{n,k}\ge\xi_k\) and \(\xi_k\to\infty\). Theorem 3.5 gives a different characterization: the unique measure that maximizes the bottom of its support among all Hamburger solutions is the Friedrichs one. Translation by its lowest support point creates a Stieltjes problem with \(\tilde\alpha=0\), calculated using the translated Nevanlinna functions, and forces uniqueness there. Section 4 removes the first Jacobi row and column; from (35) obtains \(\alpha(s^\dagger)=-b_0^2/(\alpha(s)+a_0)<0\), and compares the old and new Friedrichs supports by strict interlacing in Theorem 4.1. The zero of the original extremal support can be at 0 when \(\alpha=0\); the strictly positive support statement in §3 follows its preceding assumption \(\alpha<0\).

This is an exact operator inverse-data barrier. Even complete moment data of an indeterminate sequence fix the symmetric Jacobi operator without choosing a self-adjoint extension or its spectral measure. Berg's result is not an automatic statement about competitors supported on the triangular lattice, since the Nevanlinna measures have their own node sets. The prefix's separate lattice counterexample addresses that stronger restriction. For the actual zeta profile, the square-root exponential tail provides Stieltjes determinacy on the positive half-line. Symmetric pushforward to \(\pm\sqrt x\) also supplies Hamburger determinacy for the lifted measure by its ordinary exponential moment. One should not infer Hamburger determinacy of the original measure directly from that lift.

- [Laurent–Mourrain published primary PDF](https://homepages.cwi.nl/~monique/files/archivlm.pdf)
- [Berg pinned primary preprint](https://arxiv.org/pdf/2407.08511v1)
