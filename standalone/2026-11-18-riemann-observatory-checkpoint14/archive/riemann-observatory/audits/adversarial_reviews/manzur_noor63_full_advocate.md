# Manzur–Noor v1 whole-work technical advocate review

Date 2026-11-17. I read all seven pages of Manzur–Noor, *A Hardy-space operator acting on \(\zeta\)-zeros*, and reconstructed the mathematical claims in §§1–6. The bounded group, its kernel action, and the RH equivalence in Theorem 5.1 check out. The covariance signs in §6 do not agree with the same paper's Proposition 4.1 or matrix. This is a whole-work advocate review of the pinned preprint, with dependency access reported separately. [Pinned arXiv v1](https://arxiv.org/pdf/2610.03568v1)

The primary local PDF SHA-256 is \(\texttt{ba5c1ab46edf1dbef9741dd1e999ec492c0be59bc65d82cc7ac7dfab8520c076}\). The unversioned arXiv PDF returned the same hash. The submission history lists only v1, dated 2 October 2026, and the explicit v2 page returned article not found. The checked arXiv record and targeted title/correction search yielded no erratum. I compared the page images for the conjugations, closure bars, and covariance signs. [arXiv metadata and version history](https://arxiv.org/abs/2610.03568)

## Coverage checklist

| Source location | Checked status |
| --- | --- |
| Abstract and §1, p. 1, through (A)–(D) | Hardy normalization, analytic log branch, \(h_k\in H^2\), exact kernel coefficients, removable point at 1, and the simultaneous annihilation criterion verified. (A) is the exact Noor dependency. |
| End of §1, p. 2 | The motivating positive-real shift needs nonzero kernel multipliers for its propagation argument. The displayed \(T_\tau\) supplies a vertical shift. An explicit bounded extension below supplies the positive-real variant. |
| §2, p. 2, (1)–(7) | Diagonal and Copson operators, coordinate convergence, adjoint, Hardy bound, and construction verified. |
| §3, pp. 3–4, (8)–(18) | Coefficient estimate, boundedness, exact difference intertwining, group, adjoints, and cumulative coefficients verified, including index zero. |
| §4, p. 4, (19)–(20) | Kernel scalar, sign of the shift, and all coordinate indices verified. |
| §5, pp. 5–6, (21)–(25) | Three implications, fixed \(\tau\ne0\), multiplicity-tolerant progression, density contradiction and quantitative distance verified. |
| §6, p. 6, \(W_n\), covariance, and matrix | \(W_n^*k_s\) and the matrix verified. Both positive covariance signs fail for the stated \(T_\tau\). Exact correction and a two-dimensional test are below. |
| §6 disclosure and references [1]–[7], pp. 6–7 | Mathematical reading of the matrix and bibliography below. The historical AI interaction is identified as author-reported, outside the mathematical verification. |

## Sections 1 and 4 input conventions

On the unit disk let \(e_j(z)=z^j\) and take the inner product linear in its first argument. The function \((1-z^k)/(k(1-z))\) is zero-free in the open disk and has value \(1/k>0\) at zero. Choose the analytic logarithm with value \(-\log k\) there. Expanding gives the coefficient of \(z^j\) in \(h_k\) as
\[
 a_j=H_j-H_{\lfloor j/k\rfloor}-\log k,\qquad H_0=0.
\]
The harmonic-number asymptotic shows \(a_j=O_k(1/(1+j))\), so \(h_k\in H^2\). A change of branch would add a nonzero multiple of \(1/(1-z)\) and would leave \(H^2\). The density statement (A) is exactly Noor's Theorem 8 for this normalization. Noor's Theorem 6 first gives approximation to the constant 1, and his semigroup argument gives full norm density. [Noor v4, Theorems 6 and 8](https://arxiv.org/pdf/1809.09577v4)

For \(j\ge1\), the difference in (B) can be written
\[
 (j+1)^{1-\bar s}-j^{1-\bar s}
     =(1-\bar s)\int_j^{j+1}x^{-\bar s}\,dx .
\]
It is \(O_s(j^{-\Re s})\), uniformly on compact subsets, so the displayed \(k_s\) is in \(H^2\). The functional \(\Lambda^{(s)}(f)=\langle f,k_s\rangle\) is holomorphic in \(s\) on \(\Re s>1/2\) by the same bound and Cauchy–Schwarz. In particular \(k_s\ne0\) since its constant coefficient is \(-1/\bar s\). These coefficients match Ghosh–Kremnizer–Noor–Santos (7). Their \(h_k\) carries an extra factor \(1/k\), so multiplying their (6) by \(k\) gives the normalization of (C). [Ghosh–Kremnizer–Noor–Santos v4, p. 6, (6)–(7)](https://arxiv.org/pdf/2206.00434v4)

For an independent check of (C), use \(a_{n-1}-a_n=(k\mathbf1_{k\mid n}-1)/n\) and summation by parts in (B). The terminal coefficient \(a_J(J+1)^{1-s}\) tends to zero. On \(\Re s>1\) one obtains
\[
 \langle h_k,k_s\rangle
       =-\frac1s\sum_{n\ge1}(k\mathbf1_{k\mid n}-1)n^{-s}
       =-\frac{\zeta(s)}s(k^{1-s}-1).
\]
Holomorphy continues the identity. At \(s=1\), the pole of \(\zeta\) is canceled. The value is \(\log k\), also obtained from \(k_1=-1\) and \(a_0=-\log k\). Thus (C) is read by removable continuation there. The Appendix of Calderaro–Manzur–Noor–Santos gives the same normalization by coefficient summation. [Calderaro–Manzur–Noor–Santos v4, §1.7 and Appendix](https://arxiv.org/pdf/2203.05030v4)

For (D), at \(\Re s\ne1\) each \(k^{1-s}-1\) is nonzero by modulus. At \(s=1+it\) with \(t\ne0\), the factors for \(k=2,3\) cannot both vanish, since that would make \(\log2/\log3\) rational. At \(s=1\) the above evaluation is nonzero. Therefore simultaneous annihilation of all \(h_k\) is exactly the zero predicate for \(\zeta(s)\) on the stated half-plane. Orthogonality against their algebraic span and against its closure are equivalent.

The question on p. 2 asks for a shift \(s+\alpha\) with \(\Re\alpha>0\). The formula later proved in (20) has \(\alpha=-i\tau\) with real \(\tau\), so it provides the vertical version used in the theorem. For a positive-real-part shift the formal propagation argument needs the scalar multipliers to remain nonzero at the propagated kernels. With that condition, the progression eventually hits \(\Re s>1\) and contradicts the Euler product directly. A bounded extension that supplies the literal shift question is obtained by replacing the phase \(n^{i\tau}\) by \(n^{-\alpha}\) throughout (7). For \(\Re\alpha\ge0\) the diagonal has norm at most 1 and the other diagonal is bounded by \(|\alpha|\), since
\[
 j\big|(j+1)^{-\alpha}-j^{-\alpha}\big|
 \le |\alpha|j\int_j^{j+1}x^{-\Re\alpha-1}\,dx\le|\alpha|.
\]
The cumulative coefficient computation then gives the adjoint action
\((\bar s+\bar\alpha)k_{s+\alpha}/\bar s\), whose scalar is nonzero. This extension is a review calculation; the printed theorem uses the vertical group.

## Sections 2–3, equations (1)–(18)

Put \(d_n=n^{i\tau}\) for \(n\ge1\). The diagonal in (1)–(2) is unitary because \(|d_n|=1\), with adjoint obtained by \(\tau\mapsto-\tau\). Define the operator on the right of (4) by \(Hb\). Relabel \(x_n=b_{n-1}\) in the discrete Hardy inequality to get \(\|Hb\|_2\le2\|b\|_2\). For complex inputs the pointwise triangle inequality reduces it to the nonnegative form from the primary book. Theorem 326 on p. 239 is the discrete statement with constant \((p/(p-1))^p\); Theorem 327 on p. 240 is the corresponding integral statement. [Hardy–Littlewood–Pólya, second-edition scan, pp. 239–240](https://mathematicalolympiads.wordpress.com/wp-content/uploads/2012/08/inequalities-hardy-littlewood-polya.pdf#page=252)

The adjoint \(H^*\) is \(C\) in (3), by testing on coordinate vectors. Each row sum \(\sum_{j>k}a_j/j\) is absolutely convergent by Cauchy–Schwarz. The basis formulas and (6) follow on the whole space. There is also a short independent check of the exact \(p=2\) bound. For the matrix indexed from 1 with entries \(1/n\) for \(k\le n\), use the Schur weights \(w_1=1\) and \(w_{n+1}=(1-1/(2n))w_n\). Then
\(\sum_{k\le n}w_k=2n w_{n+1}\) and \(\sum_{n\ge k}w_n/n=2w_k\) by telescoping. The weights tend to zero, since their defining product is bounded by \(\exp(-\frac12\sum_{n<k}1/n)\). The row and column bounds give operator norm at most 2.

For \(j\ge1\),
\[
 |d_{j+1}-d_j|\le|\tau|\log(1+1/j)\le|\tau|/j,
\]
so \(Q_\tau\) is bounded by \(|\tau|\) and has zeroth diagonal zero. This proves (8)–(10). Applying \(C\) to \(Q_\tau a\) gives the exact coefficient expression
\[
 (T_\tau a)_k=d_{k+1}a_k+\sum_{j>k}(d_{j+1}-d_j)a_j .
\]
The series again converges absolutely in every coordinate by the \(1/j\) bound. Taking the difference of coordinates \(k,k+1\) gives \(\Delta T_\tau=D_\tau\Delta\), where \(\Delta=I-S^*\). An \(\ell^2\) constant sequence is zero, so \(\Delta\) is injective. Its range is dense since \(\ker\Delta^*=\ker(I-S)=0\). The intertwining, multiplicativity of \(D_\tau\), and injectivity yield the group identity, \(T_0=I\), and \(T_\tau^{-1}=T_{-\tau}\). This proves (11)–(14).

Taking adjoints yields exactly (15)–(16). With \(B_j=\sum_{k=0}^j b_k\), the expression for \(Q_\tau^*C^*\) in coordinate \(j\ge1\) is \((d_{j+1}^{-1}-d_j^{-1})B_{j-1}\). Adding \(d_{j+1}^{-1}b_j\) gives
\[
 (T_\tau^*b)_j=d_{j+1}^{-1}B_j-d_j^{-1}B_{j-1}.
\]
At \(j=0\) the answer is \(b_0\). This is (17)–(18) with the sign of the exponents fixed by the adjoint.

## Sections 4–5, equations (19)–(25)

Cumulative summation of (B) gives \(B_j=-(j+1)^{1-\bar s}/\bar s\). Substituting in the adjoint formula changes the power in the coefficient difference to \(1-\bar s-i\tau\), with the constant coefficient still \(-1/\bar s\). Since \(\overline{s-i\tau}=\bar s+i\tau\), this proves the exact kernel identity
\[
 T_\tau^*k_s=\frac{\bar s+i\tau}{\bar s}\,k_{s-i\tau}.
\]
It takes place throughout the open half-plane since the shift is vertical and both denominators are nonzero. In the linear-first inner product the scalar is conjugated when inserted in the second slot. Therefore
\[
 \langle T_\tau h_k,k_\rho\rangle
 =-\frac{\zeta(\rho-i\tau)}{\rho}
              (k^{1-\rho+i\tau}-1)
\]
for a critical-strip zero with \(\Re\rho>1/2\), with the same normalization as (22).

Under RH the closure of \(\mathcal N\) is all of \(H^2\) by (A), and invariance immediately gives the single-member condition. For the converse, fixing any \(k\ge2\) under this condition makes the last displayed expression vanish at each right-half-strip zero. The second factor has modulus-separated terms because \(k^{1-\Re\rho}>1\). At each iterate the real part is unchanged, so induction gives the full progression \(\rho-in\tau\) for \(n\ge0\). Under failure of RH one can take \(1/2<\Re\rho<1\) with positive imaginary part using the usual zeta symmetries. To check the endpoints, there are no real zeros in \((0,1)\) by the positive alternating eta series and \(1-2^{1-s}<0\). The Euler product gives no zeros on \(\Re s>1\); the usual inequality \(\zeta(\sigma)^3|\zeta(\sigma+it)|^4|\zeta(\sigma+2it)|\ge1\) for \(\sigma>1\), obtained from \(3+4\cos v+\cos 2v\ge0\), rules out zeros at \(1+it\), \(t\ne0\), by letting \(\sigma\downarrow1\).

For fixed \(\sigma\) with \(1/2<\sigma<\Re\rho\), Ingham's exponent \(3(1-\sigma)/(2-\sigma)\) is strictly below 1. Thus the quoted bound with \((\log T)^5\) gives \(N(\sigma,T)=o(T)\). If \(\tau<0\), the progression eventually has positive ordinates increasing by \(|\tau|\). If \(\tau>0\), take conjugates of its eventual negative-ordinate tail to obtain the same positive-ordinate count. The distinct progression supplies at least \(T/|\tau|-O(1)\) zeros, irrespective of their multiplicities. This contradicts (25). The proof needs only \(\sigma<\min(\Re\rho,3/4)\), so it also follows directly using the exact range of Ingham's bound quoted by Huxley at (1.8), p. 164, with \(-T\le\gamma\le T\) usable as an upper bound for the one-sided count. The modern Chourasiya–Simonič source corroborates the printed Ingham attribution including the one-sided multiplicity convention. [Huxley 1972, p. 164](../../sources/prefix_formula62_classical2/hux1972.pdf#page=173) · [Chourasiya–Simonič v2, introduction](https://arxiv.org/pdf/2507.15184v2)

Finally, \(k_\rho\) is a nonzero annihilator of the closed approximation space. Cauchy–Schwarz applied after subtracting any vector in that space gives the lower bound \(|\langle T_\tau h_k,k_\rho\rangle|/\|k_\rho\|\). Combining with (22) proves (21). Positivity follows from the stated nonvanishing of the translated zeta value and the same modulus-separated factor. This quantitative step does not use the density estimate.

## Section 6, covariance, matrix, and disclosure

The coefficient action of \(W_n\) repeats every input coefficient \(n\) times, so \(W_n\) is bounded with norm \(\sqrt n\). The adjoint sums consecutive blocks of \(n\) coefficients. Applying the block sums to differences of the cumulative kernel coefficients in (19) gives \(W_n^*k_s=n^{1-\bar s}k_s\), also at index zero. This agrees with Calderaro–Manzur–Noor–Santos Proposition 22. More generally if \(b\ne0\) is a common eigenvector, its zeroth block identity implies \(b_0\ne0\) and \(b_j=b_0(\lambda_{j+1}-\lambda_j)\) with \(\lambda_0=0\), \(\lambda_1=1\); the semigroup implies multiplicativity of \(\lambda_n\). The converse follows by taking a block sum of these differences. This verifies the cited common-eigenvector description in the normalization used here. [Calderaro et al. v4, Proposition 22](https://arxiv.org/pdf/2203.05030v4) · [Manzur–Noor–Santos v2, Lemma 3](https://arxiv.org/pdf/2111.05398v2)

The kernels used in the covariance test are total. In fact for \(f\) with coefficients \(a_j\in\ell^2\) and \(\Re s>3/2\), (B) and summation by parts express the pairing as
\[
 -\frac1s\sum_{n\ge1}(a_{n-1}-a_n)n^{1-s}.
\]
This converges absolutely by Cauchy–Schwarz. If all the pairings vanish, uniqueness of Dirichlet series forces \(a_{n-1}-a_n=0\) for all \(n\), and hence \(f=0\). Uniqueness here can be seen by isolating the least nonzero coefficient and taking the real variable to infinity after multiplying by its frequency.

For any bounded \(T\) with \(T^*k_s=c(s)k_{s-i\tau}\), the exact factor comparison on \(k_s\) is
\[
 W_n^*T^*k_s=c(s)n^{1-\bar s-i\tau}k_{s-i\tau},
 \qquad
 T^*W_n^*k_s=c(s)n^{1-\bar s}k_{s-i\tau}.
\]
Thus \(W_n^*T^*=n^{-i\tau}T^*W_n^*\) by totality. Taking adjoints gives \(TW_n=n^{i\tau}W_nT\), or
\[
 W_nT=n^{-i\tau}TW_n.
\]
The p. 6 image prints positive \(i\tau\) exponents in both displayed relations. This is a literal sign mismatch. For an exact finite test with the paper's \(T_\tau\), \(W_2T_\tau e_0=1+z\), while \(T_\tau W_2e_0=2^{i\tau}(1+z)\) by (11). At \(\tau=\pi/(2\log2)\) the printed positive-sign right side is \(-(1+z)\). The corrected negative-sign relation gives \(1+z\). The check uses only two coefficients.

The matrix on p. 6 nevertheless agrees exactly with (11), including the positive phases \(n^{i\tau}\) on its diagonal. Under the corrected covariance, \(T_\tau e_0=e_0\) and \(W_ne_0=1+\cdots+z^{n-1}\) force that polynomial to have eigenvalue \(n^{i\tau}\). Taking consecutive differences recovers every column, giving precisely the printed matrix. Using \(T_{-\tau}\) would give the printed covariance but would reverse both the phases in the matrix and the shift in (20). No such reparameterization occurs in v1. The proof of Theorem 5.1 depends on (20), which the independent coefficient calculation confirms. The covariance display is separate from that proof.

The statements about prompts and model suggestions are the authors' disclosure. This review checks the mathematical relations and the displayed matrix; it has no access to the prompt history and makes no claim about the provenance of any error or correction.

## Reference access and exact dependencies

| Reference | Checked locator and limits |
| --- | --- |
| [1] Calderaro–Manzur–Noor–Santos, arXiv:2203.05030v4 (2024) | §1.7 (1.3)–(1.4), Proposition 22 and the Appendix for the zeta kernel, its covariance eigenvalue, and (C). The pin matches the year of the cited preprint. [Primary source](https://arxiv.org/pdf/2203.05030v4) |
| [2] Copson, *Note on Series of Positive Terms*, JLMS 3 (1928), 49–51 | Publisher identity verified. Full text was unavailable on the checked publisher route, and the 1927 same-title article is a separate citation. The Copson formula and bound used here were verified by adjoint calculation and the Hardy theorem independently. [1928 publisher identity](https://doi.org/10.1112/jlms/s1-3.1.49) |
| [3] Hardy–Littlewood–Pólya, *Inequalities*, 2nd ed. (1952) | Printed §9.8, Theorem 326 p. 239 and Theorem 327 p. 240 checked in the scan. The source (5) is the discrete Theorem 326 and its complex-input consequence. Scan SHA-256 \(\texttt{7e5cc81e29de1f15f3b3794f8f452f61a97259dcc4512bdc2cd99a46000fe211}\). [Scanned edition](https://mathematicalolympiads.wordpress.com/wp-content/uploads/2012/08/inequalities-hardy-littlewood-polya.pdf#page=252) |
| [4] Ghosh–Kremnizer–Noor–Santos, *Zero-free half-planes*, Advances in Mathematics 455 (2024), 109872 | Author v4 Lemma 2.1 and (6)–(7), p. 6, verify the half-plane, coefficients, and the exact \(1/k\) difference between the two \(h_k\) conventions. [Primary source](https://arxiv.org/pdf/2206.00434v4) |
| [5] Ingham, QJM 11 (1940), 201–202 | Oxford and Crossref verify the publication and the direct PDF route returned HTTP 403. I could verify the needed exponent and logarithmic power through the explicit quotation in Huxley's original p. 164 and the independent modern primary paper cited above. The scope is verification of the input needed for the progression contradiction, without a reading of the original two-page note. [Ingham publisher identity](https://doi.org/10.1093/qmath/os-11.1.201) |
| [6] Manzur–Noor–Santos, JMAA 525(1) (2023), 127261 | Author v2 §1 (1.1), and §3 Lemma 3, verify the operator and block adjoint formulas. [Primary source](https://arxiv.org/pdf/2111.05398v2) |
| [7] Noor, Advances in Mathematics 350 (2019), 242–255 | Author v4 Theorem 6 and Lemma 7 give the exact \(h_k\) and its membership. Theorem 8 gives the exact norm-density equivalence. This is the cited classical input, with no stronger RH consequence imported. [Author v4](https://arxiv.org/pdf/1809.09577v4) · [Journal identity](https://doi.org/10.1016/j.aim.2019.04.064) |

The established Sklyar–Marchenko antecedent for this underlying group after adjoint and time reversal gives separate historical context. It is outside the seven references of the pinned preprint and does not affect the covariance calculation or the RH criterion. [Exact operator-family comparison](finite_moment63_manzur_noor_operator_antecedents.md)
