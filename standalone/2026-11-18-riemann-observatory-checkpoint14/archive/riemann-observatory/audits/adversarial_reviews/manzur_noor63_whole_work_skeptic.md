# Whole-work independent audit of Manzur–Noor, arXiv 2610.03568v1

17 November 2026. I read all seven PDF pages, including §§1–6 and references, and checked the displayed claims independently. Theorem 5.1 and its distance bound are supported. Both covariance exponents as arranged in the displayed §6 relation need a minus sign. The matrix printed immediately below is the correct matrix for (7) and obeys the corrected relation. There is also a local mismatch between the right-half-plane shift requested in §1 and the vertical shift constructed in §§2–4. [Pinned PDF](https://arxiv.org/pdf/2610.03568v1) · [Pinned HTML, §6](https://arxiv.org/html/2610.03568v1#S6)

## Version and scope

The local PDF and a new public v1 download matched byte for byte by SHA-256 `ba5c1ab46edf1dbef9741dd1e999ec492c0be59bc65d82cc7ac7dfab8520c076`. The source record `PAPER-MN2026-VERTICAL` gives that same hash and seven pages. I visually checked the overbars in (20), in Theorem 5.1 and in its Hilbert-space distance argument, and the two positive phase signs on p. 6. The official arXiv history lists v1 only, submitted on 2 October 2026. The bounded title and erratum searches located no separate correction or journal version. The official record gives the arXiv repository DOI `10.48550/arXiv.2610.03568`. [Official submission history](https://arxiv.org/abs/2610.03568)

Throughout, use the complex inner product linear in the first variable. Write \(\mathcal N\) for the algebraic span of the \(h_k\) and \(W=\overline{\mathcal N}\). The source theorem and distance statements concern the closure, while \(\mathcal N^\perp=W^\perp\).

## Page 1, the generators and their kernels

On the disk, both \(1-z^k\) and \(1-z\) have positive real part. Their quotient is nonzero and its argument, as the difference of their arguments, lies in \((-\pi,\pi)\). The normalized logarithm in \(h_k\) is \(\log(1-z^k)-\log(1-z)-\log k\), using the analytic branches zero at the origin for the first two terms. Expanding gives coefficients

\[
 (h_k)_j=H_j-H_{\lfloor j/k\rfloor}-\log k,
 \qquad H_0=0.
\]

The harmonic-number estimate gives \((h_k)_j=O_k((j+1)^{-1})\). Hence \(h_k\in H^2\), with the branch normalized by the real value \(-\log k\) at zero. An additive nonzero logarithm branch constant would introduce a non-square-summable constant sequence after multiplying by \((1-z)^{-1}\).

One can check the physical identification in (A) directly from these coefficients. In the unit-cell space with weights \(1/[n(n+1)]\), the map \((Ba)_n=\sum_{j<n}a_j-na_n\) sends \(e_0\) to 1 and \(e_j\), \(j\ge1\), to the vector zero before cell \(j\), equal to \(-j\) at that cell and equal to 1 thereafter. Telescoping gives an orthonormal family. If a vector \(b\) is orthogonal to the family, its tail sums \(A_j=\sum_{n\ge j}b_n/[n(n+1)]\) satisfy \(A_1=0\) and \(A_{j+1}=b_j/(j+1)=jA_j/(j+1)\); thus all coefficients vanish. The jump at \(n\) is \(n(a_{n-1}-a_n)\). For \(h_k\) this is \(k\mathbf1_{k\mid n}-1\), so \(Bh_k=k\lfloor x/k\rfloor-\lfloor x\rfloor=-k\{n/k\}\) on the \(n\)-th cell. I checked Bagchi's Theorem 1 with these exact weights and generators up to nonzero constants. Noor's Theorem 1 states the corresponding condition for approximation of 1, and his Theorem 8 gives the full density equivalence. Another direct density step is that integer dilations preserve the floor-difference span, and dilations of 1, followed by consecutive differences, generate the individual cells. The classical Báez-Duarte approximation input remains external. [Bagchi, Theorem 1](https://arxiv.org/pdf/math/0607733v1) · [Noor, Theorems 1 and 8](https://arxiv.org/pdf/1809.09577v4)

For (B), the coefficient difference of powers is \((1-\bar s)\int_j^{j+1}x^{-\bar s}\,dx\). It gives the stated square-summability for \(\Re s>1/2\), uniformly on compact parameter sets after allowing the least real part of the set. It follows that \(\Lambda^{(s)}(a)=\langle a,k_s\rangle\) is continuous in \(a\) and holomorphic in \(s\). Its basis values match Ghosh–Kremnizer–Noor–Santos (7), including \(\Lambda^{(s)}(1)=-1/s\). That source uses \(h_k/k\); multiplying its (6) by \(k\) gives the exact normalization of (C). The growth input used by Manzur–Noor is the upper estimate and it is valid at the special point \(s=1\), where the positive-index coefficients vanish. [Ghosh–Kremnizer–Noor–Santos, (6)–(8)](https://doi.org/10.1016/j.aim.2024.109872)

Independently, for \(\Re s>1\), summation by parts on the displayed coefficients of \(h_k\) gives

\[
 s\Lambda^{(s)}(h_k)
 =-\sum_{n\ge1} n^{1-s}\big((h_k)_{n-1}-(h_k)_n\big)
 =-\sum_{n\ge1}(k\mathbf1_{k\mid n}-1)n^{-s}
 =-\zeta(s)(k^{1-s}-1).
\]

The terminal term vanishes using the coefficient bound. Both sides continue holomorphically on the required half-plane after removing the pole product at 1. This independently verifies (C) and the computation in the cited Calderaro–Manzur–Noor–Santos appendix. At 1 the value is \(+\log k\), consistent with \(k_1=-e_0\). [Calderaro–Manzur–Noor–Santos, Appendix (5.1)](https://arxiv.org/pdf/2203.05030v4)

For (D), if \(\Re s\ne1\) then each \(k^{1-s}-1\) is nonzero by modulus. At \(1+it\), \(t\ne0\), the factors for 2 and 3 cannot both vanish, since that would make \(\log 2/\log 3\) a ratio of nonzero integers. This would contradict unique factorization. At \(s=1\) the removable values are nonzero. Thus (D) holds on the whole indicated half-plane when written as membership in the zero set of the meromorphic zeta function, which excludes its pole.

For use in §6, the kernels are total. If \(a\) annihilates all of them, on \(\Re s>3/2\) reindexing (B) yields the absolutely convergent identity \(s\Lambda^{(s)}(a)=-\sum_{n\ge1}(a_{n-1}-a_n)n^{1-s}=0\). Uniqueness of an absolutely convergent Dirichlet series makes \(a\) constant, so \(a=0\) in \(\ell^2\). This argument uses the kernel family over the whole half-plane. Linear independence of finite subsets alone would not give the totality needed for an operator identity.

## Pages 2–4, equations (1)–(20)

- **Diagonals and Copson, (1)–(7).** Put \(d_j=(j+1)^{i\tau}\). The diagonal is unitary and its adjoint is obtained by replacing \(\tau\) by \(-\tau\). The individual Copson rows converge absolutely by Cauchy–Schwarz with \((1/j)_{j>k}\). On finitely supported sequences the matrix transpose gives the discrete Hardy averages in (4), including the zero coordinate at 0. Boundedness then extends both operators and that adjoint identity to all \(\ell^2\).
- **Hardy inequality, (5)–(6).** For nonnegative inputs \(x_n\), write \(u_n=(x_1+\cdots+x_n)/n\). The identity for \(x_n\) in terms of \(u_n,u_{n-1}\) and Young's inequality give
  \[
  (p-1)u_n^p-pu_n^{p-1}x_n\le (n-1)u_{n-1}^p-nu_n^p.
  \]
  Summing through \(N\) and applying Hölder proves the claimed constant \(p/(p-1)\) after taking the \(p\)-th root and then the limit. For complex inputs apply this to absolute values. At \(p=2\) it gives \(\|\mathcal C^*\|\le 2\), and the adjoint gives the same bound for \(\mathcal C\). I checked the statement and the telescoping proof in the cited section of *Inequalities*. Copson's 1928 paper gives the corresponding weighted series setting. [Hardy–Littlewood–Pólya, §9.8](https://mathematicalolympiads.wordpress.com/wp-content/uploads/2012/08/inequalities-hardy-littlewood-polya.pdf) · [Copson, original scan in the Edinburgh collection](https://era.ed.ac.uk/server/api/core/bitstreams/b6331a52-a797-4d1c-b4e4-6967eca7f1bb/content)
- **Boundedness and difference relation, (8)–(13).** Factor out \(j^{i\tau}\), use \(|e^{iu}-1|\le|u|\) and \(\log(1+1/j)\le1/j\). This gives \(\|Q_\tau\|\le|\tau|\) and the claimed \(1+2|\tau|\) bound for \(T_\tau\). The exact row is \((T_\tau a)_k=d_k a_k+\sum_{j>k}(d_j-d_{j-1})a_j\). Its series converges absolutely by the \(1/j\) bound. Consecutive row differences cancel all but \(d_k(a_k-a_{k+1})\), giving \(\Delta T_\tau=D_\tau\Delta\). The difference \(\Delta\) is injective on \(\ell^2\) since a constant sequence in that space is zero.
- **Group and adjoint, (14)–(18).** Apply \(\Delta\) to the composition, use the diagonal group law and injectivity, and note directly that \(T_0=I\). This proves composition and the inverse. The two operator adjoint formulas follow in the printed order. For prefix sums \(B_j=\sum_{r\le j}b_r\), the coordinate calculation yields \((T_\tau^*b)_0=b_0\) and \((T_\tau^*b)_j=(j+1)^{-i\tau}B_j-j^{-i\tau}B_{j-1}\) for \(j\ge1\).
- **Kernel transport, (19)–(20).** The prefixes of (B) telescope to \(-(j+1)^{1-\bar s}/\bar s\). Multiplying by the adjoint phases gives the exponents \(1-\bar s-i\tau\), and the factor \((\bar s+i\tau)/\bar s\) gives the correct zeroth coordinate. The bar in the PDF identity \(\overline{s-i\tau}=\bar s+i\tau\) is present. This proves the printed vertical action and its denominator is nonzero throughout the domain.

## Pages 5–6, all parts of Theorem 5.1

The theorem fixes an arbitrary real \(\tau\ne0\). RH gives \(W=H^2\) by (A), hence invariance. Invariance implies membership of the translated vector for every \(k\ge2\), in particular for some. For the converse, fix the one \(k\) furnished by the hypothesis. Pairing that same fixed vector against any right-strip zero kernel, using (20) with the scalar conjugated in the second variable, yields (22)

\[
 \langle T_\tau h_k,k_\rho\rangle
 =-\frac{\zeta(\rho-i\tau)}{\rho}(k^{1-\rho+i\tau}-1).
\]

For \(1/2<\beta=\Re\rho<1\), the last factor has nonzero modulus because \(|k^{1-\rho+i\tau}|=k^{1-\beta}>1\). Thus membership forces a new zero at \(\rho-i\tau\) with the same real part. Apply the same argument at each new kernel, without changing the translated vector or assuming invariance for the converse. All zeros in that sequence are distinct for \(\tau\ne0\), and each contributes at least one to the count regardless of multiplicity. The classical symmetry \(\rho\mapsto1-\bar\rho\) supplies a zero in the right half when RH fails. The paper initially chooses positive ordinate; the classical nonvanishing on the real interval \((0,1)\) follows, for example, from the positive paired alternating eta sum and its nonzero factor \(1-2^{1-s}\). Alternatively the induction can start at any ordinate and still produces the required positive sequence at large indices.

For \(\tau<0\), the original sequence has eventually positive ordinates growing by \(|\tau|\). For \(\tau>0\), take conjugates after the ordinates become negative. Each case gives at least \(T/|\tau|-O(1)\) zeros in the positive height range for any fixed \(\sigma\in(1/2,\beta)\). The Ingham exponent is strictly below 1 there since \(1-3(1-\sigma)/(2-\sigma)=(2\sigma-1)/(2-\sigma)>0\). Thus (24) implies (25), and the progression is impossible. The proof would also work with a weaker \(o(T)\) count and requires no uniformity as \(\sigma\downarrow1/2\). I verified the original 1940 bibliographic identity but the publisher text returned HTTP 403. The exact inclusive thresholds, multiplicity count and log power are corroborated by Chourasiya–Simonič's explicit Ingham paper. Guth–Maynard (1.2) independently records the power with an \(o(1)\) exponent, which is sufficient here. [Ingham 1940 publisher record](https://doi.org/10.1093/qmath/os-11.1.201) · [Chourasiya–Simonič v2, §1](https://arxiv.org/html/2507.15184v2#S1) · [Guth–Maynard (1.2)](https://arxiv.org/pdf/2405.20552v2)

For (21), \(k_\rho\) is a nonzero vector in \(W^\perp\). Pairing it against \(T_\tau h_k-y\) for each \(y\in W\), applying Cauchy–Schwarz and taking the infimum gives (21) with (22). The strict positivity uses both the stated shifted nonzero value and the nonzero exponential factor. The proof's reference to “Theorem 4.1” points to Proposition 4.1. The proof of every part of Theorem 5.1 ends before §6 and uses none of its covariance assertions. The abstract's alternative is the intermediate progression implication, which the theorem then excludes with the density input.

## Page 6, covariance, finite witness and assistance history

The operator \(W_n\) repeats each coordinate \(n\) times, and its adjoint sums each block of \(n\) coordinates. Since the prefixes of \(k_s\) are (19), the block sums give \(W_n^*k_s=n^{1-\bar s}k_s\), also for the first block. I checked the cited [1] Proposition 22 independently. For a common eigenvector \(b\ne0\), the zeroth coordinate of \(W_n^*b=\lambda_n b\) gives \(\sum_{r<n}b_r=\lambda_n b_0\), so \(b_0\ne0\) and \(b_j=(\lambda_{j+1}-\lambda_j)b_0\). The semigroup law makes \(\lambda\) completely multiplicative. Conversely that property makes each block sum \(\lambda_n b_j\) if the increments are square summable. The result gives the cited eigenvalue on choosing \(\lambda_n=n^{1-\bar s}\). [Calderaro et al., Proposition 22](https://arxiv.org/pdf/2203.05030v4) · [Manzur–Noor–Santos, Lemma 3](https://arxiv.org/pdf/2111.05398v2) · [Noor, §3](https://arxiv.org/pdf/1809.09577v4)

For a bounded \(T\) with \(T^*k_s=c_s k_{s-i\tau}\), the shifted kernel has eigenvalue \(n^{1-\overline{s-i\tau}}=n^{-i\tau}n^{1-\bar s}\). Using totality, the necessary operator relations are therefore

\[
 W_n^*T^*=n^{-i\tau}T^*W_n^*,\qquad
 W_nT=n^{-i\tau}TW_n.
\]

Both displayed exponents in v1 have the opposite sign. An independent finite witness uses \(n=2\), \(\tau=\pi/(2\log2)\) and \(e_0\). Here \(T_\tau e_0=e_0\) and \(T_\tau e_1=(i-1)e_0+ie_1\). It follows from \(W_2e_0=e_0+e_1\) that \(W_2T_\tau e_0=e_0+e_1\) and \(T_\tau W_2 e_0=i(e_0+e_1)\). Multiplying the latter by the printed \(+i\) yields \(-e_0-e_1\). The first printed identity also fails in the zeroth coordinate on \(e_0\), giving \(-i\) on the left and \(+i\) on the right. I ran a two-coordinate Gaussian-integer control and obtained these exact values. For every fixed \(\tau\ne0\) at least one of \(n=2,3\) fails the printed direct relation on \(e_0\), since the required simultaneous equality \(n^{2i\tau}=1\) would contradict unique factorization.

The displayed matrix itself is correct because column \(j\) has diagonal \(d_j\), each earlier entry \(d_j-d_{j-1}\), and subsequent entries zero. As a second verification of the corrected relation, \(\Delta W_n a\) vanishes except at end-of-block indices \(j+1=n\ell\), where it equals \((\Delta a)_{\ell-1}\). Acting by \(D_\tau\) then gives the factor \(n^{i\tau}\) on precisely those locations. Injectivity of \(\Delta\) gives \(T_\tau W_n=n^{i\tau}W_nT_\tau\), which is equivalent to the corrected direct law above. Thus the printed matrix is a counterexample to the printed system and supplies a correct solution to the corrected system.

Section 6 reports that the authors prompted a model to derive a matrix and propose operator expressions. I checked the stated mathematics independently. The public source supplies the authors' account of the prompts and their evaluation, and I had no independent access to that prompt history or the other proposed expressions. The mathematical sign error has a concrete witness regardless of that account. [Author disclosure and printed matrix](https://arxiv.org/html/2610.03568v1#S6)

## Exact scope of the motivating shift

Page 2 asks for an adjoint shift \(s\mapsto s+\alpha\) with \(\Re\alpha>0\). The constructed \(T_\tau\) in (20) implements \(s\mapsto s-i\tau\), whose real part stays fixed, so the assertion that it answers that exact question requires qualification. The motivating iteration for a general family also needs nonzero scalar multipliers along the orbit. The actual factor in (20) satisfies that requirement. For a genuinely right shift, iteration would reach \(\Re s>1\) after finitely many steps, where the Euler product excludes zeros.

There is a direct separate construction for that literal right shift. Put \(d_j=(j+1)^{-\alpha}\) with \(\Re\alpha>0\), and use the same Copson formula with diagonal \(D e_j=d_je_j\) and \(Q e_j=j(d_j-d_{j-1})e_j\) for \(j\ge1\), \(Qe_0=0\). The integral of the derivative of \(x^{-\alpha}\) over \([j,j+1]\) gives \(|j(d_j-d_{j-1})|\le|\alpha|\), so the operator is bounded. Substituting its adjoint coefficients in the kernel prefixes gives \(T^*k_s=((\bar s+\bar\alpha)/\bar s)k_{s+\alpha}\) with a nonvanishing factor. This is a reconstruction of how the motivating question can be met. The vertical criterion proved in Theorem 5.1 uses its own density argument.

## Coverage ledger

| Source location | Audit outcome |
|---|---|
| Abstract and §1, pp. 1–2 | Checked the scope of the progression claim, analytic logarithm, square summability, primary cited density criterion, (A)–(D), the value at the pole, and the real-part condition in the question. The motivational wording needs the shift and nonzero-factor qualifications above. |
| §§2–3, pp. 2–4 | Independently checked all definitions and (1)–(18), including the full \(p\)-range of the inequality, row convergence, boundedness, group law and adjoint. |
| §4, p. 4 | Independently checked (19)–(20) and visually verified the conjugation in the proof. |
| §5, pp. 5–6 | Verified each implication, the exact quantifiers, the signs in (22), both directions of the ordinate progression, inclusive density comparison, real-ordinate point and multiple zeros, and (21). The 1940 Ingham proof remains an external classical dependency. |
| §6, p. 6 | Reconstructed the cited block eigenspaces and kernel totality, falsified both printed signs by an exact finite witness, and verified the matrix and corrected law by two methods. Author assistance history is recorded as the authors' account. |
| References, pp. 6–7 | Checked [1] Proposition 22 and Appendix, [2] original accessible series paper, [3] §9.8, [4] the basis formula and scaling, [5] original bibliographic identity plus exact modern corroboration, [6] the definition and block adjoint, and [7] Theorems 1 and 8. Complete upstream proof audits, private prompt history and an exhaustive correction-history search remain outside the coverage. |

No paper-level promotion is made by this note. The completed review distinguishes the valid main theorem, the disproved printed auxiliary phase law, the exact replacement and the remaining external provenance. No publication-priority claim is made.
