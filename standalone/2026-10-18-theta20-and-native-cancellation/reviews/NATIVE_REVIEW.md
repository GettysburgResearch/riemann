# Independent mathematical review: complete native denominator removal

**Reviewer:** `/root/critical_coupling`, 2026-10-18.  
**Decision:** accepted as the scoped unconditional component argument stated in the reviewed proof. No mathematical correction is required. The remaining large-denominator, large-squarefree-core energy estimate and RH remain open.

The reviewer did not author `native/PROOF.md`. I read the complete proof, independently reconstructed its load-bearing identities and inequalities, and checked the precise #848 dependency used by its sparse-cutoff consumer. This review concerns mathematical correctness of the argument at the exact identities below. It is not a worldwide novelty assessment or a machine-formal proof.

## 1. Exact source identities and review scope

| Object | Bytes | SHA-256 | Git blob |
|---|---:|---|---|
| `native/PROOF.md` | 26356 | `e1b70817cbc349f020356d21127f55f7a8c8202ed10abdc46ad785812545cfe3` | `f8abf7967e8d71dfed4a506827401df96f6cdb34` |
| #848 `standalone/2026-09-12-astra-crossing-cofinal/PROOF.md` | 20973 | `f13a0ccb4c8f5a0b8b96285d89de8d9bd4e62281051e6534865264204c07d9aa` | `0f9eac82fcbca61c7887a9fb71eb29d5a4181ce9` |

The #848 file was fetched from `GettysburgResearch/riemann` at head
`7de75c02417d5d8db7eafb1ceba364380e72d16a` and its complete local bytes were authenticated against the returned Git blob. The earlier parent head printed inside that file is its historical context, not the identity used here. The load-bearing part reviewed is its fixed objects, all-prefix growth theorem, generalized Littlewood argument, sparse-scale implication, and Landau crossing proof: Sections 0–2. I do not extend this verdict to every other theorem or checker on PR #848.

The masked reciprocal estimate is reproduced completely in the new proof. I independently retrieved Tao's [A remark on partial sums involving the Möbius function](https://arxiv.org/pdf/0908.4323), whose PDF identifies itself as arXiv:0908.4323v5, dated 5 October 2009. I checked Theorem 1.1 on page 3, its proof, and the exact coprimality specialization (9) on page 4. I also read the matching argument in the author's [30 August 2009 exposition](https://terrytao.wordpress.com/2009/08/30/an-elementary-inequality-involving-the-mobius-function/). These support the classical attribution, equation numbering and uniform mask scope. The elementary proof itself was independently reconstructed.

The Newton and harmonic identities credited to #905/#988 are reproduced and verified here; their correctness is not being inferred from PR status. No CT, character-family theorem, or estimate from #990/#991 is needed for this argument. The ordinary prime number theorem is an explicit classical input for the vanishing balance limit. Classical continuation, existence of nontrivial zeta zeros, zero freedom on the line one, and reflection enter the source-qualified crossing and growth arguments.

No native checker execution is claimed in this review. The mathematical infinite arguments are independent of finite fixtures and numerical QA; runtime review and publication manifests are separate objects.

## 2. Complete masked factorization and mass

The native coefficient is

\[
C_Y(q)=\sum_{d\le Y^2,\ q\mid d}\frac{(g_Y*g_Y)(d)}d.
\]

Its complete rectangular product range is essential. I checked the factorization prime by prime. A prime appearing squared in (q=r^2s) must divide both old inputs. A prime appearing to the first power contributes the exact union identity

\[
1_{p\mid ac}=1_{p\mid a}+1_{p\mid c}-1_{p\mid a}1_{p\mid c}.
\]

After writing (T(d)=\mu(d)m_d(Y/d)/d), the ordered partition (uvw=s) produces denominator (r^2sw) and common sign \(\mu(s)\). This gives precisely (2.2), with both literal masks (ruw) and (rvw). Prime cubes give zero because both old inputs are squarefree. Mask arguments below one correctly give empty sums. In particular, the argument neither inserts extra coprimality restrictions nor drops products above a later output (k).

The proof of \(|m_d(x)|\le1\) is valid uniformly in the mask (d): divisor inversion counts the complementary prime semigroup; the two sets of integers intersect only at 1; and the fractional-part bound is applied for integer (x). Passing to real (x) by the integer part preserves the sum. Therefore

\[
|qC_Y(q)|\le\prod_{p\mid s}(2+1/p).
\]

For the squared mass, the squarefree local perturbation of (d_4) is correctly expanded as a nonnegative divisor sum. I verified (d_4(ab)\le d_4(a)d_4(b)), the elementary bound \(\sum_{n\le x}d_4(n)\le xH_{\lfloor x\rfloor}^3\), and the resulting convergent Euler majorant. Its log is bounded by

\[
4\sum_{n\ge2}n^{-2}+\sum_{n\ge2}n^{-3}\le13/4<\log32.
\]

Thus the displayed complete bound

\[
\sum_{q\le Q}q^2|C_Y(q)|^2\le32Q(1+\log Q)^3
\]

has the claimed constant, includes the whole prime tail, and is uniform in (Y). It is not being asserted for an internally product-truncated (C_Y).

## 3. Exact native identity and the annular low-denominator bound

The centered modes (S_q) include \(\Lambda(q)\). Pairing conjugate radial logarithms gives the correct real centering. I independently checked the equivalent finite divisor formula

\[
S_q(x)=\sum_{d\mid q}\mu(q/d)R(x/d),\qquad q\ge2.
\]

The \(\log x\) and Euler constant terms cancel exactly. Consequently (S_q) is constant on each full integer cell, including cells with (x<q). This verifies both the complete mode identity (3.1) and its centering (3.2). In particular, for (d>k), the nonzero contribution (R(k/d)=-\log(k/d)-\gamma\) is retained. The Newton convolution defect starts at (b^2), so the declared interval (b\le k<b^2) is correct. The possible defect \(\mu(b)^2\) explains why the proof does not extend the strict endpoint.

For the Abel expansion I checked the sign and index in its leading term. Multiplying the tail by (1-e(\theta)) gives the stated (k+1) denominator, and a second summation by parts yields the full remainder bound. The complete reduced-frequency coefficient mass is at most \(8QL^3\), where (L=1+\log Q\). Circular Farey spacing is at least (Q^{-2}); summing both semicircles bounds the Gram row by (K+2Q^2L). This pays the cross-denominator terms before the norm.

The two contributions are bounded by

\[
8QL^3/K+16Q^3L^4/K^2,
\qquad 8Q^4L^3/K^3,
\]

respectively. Combining them with (Q\le K) yields the stated constant 64. The dyadic substitution (Q_j=\lfloor X_j^\rho\rfloor), \(1/2<\rho<2/3\), and \(\alpha=2-3\rho\) gives both powers at most (X_j^{-\alpha}). The log bound and complete geometric series yield exactly

\[
\frac{2048}{1-2^{-\alpha}}b^{-\alpha}(1+\log b)^4.
\]

The shortened last annulus is bounded by its full positive dyadic estimate. There is no deletion of unfavorable output cells, hidden product cutoff, or replacement of a coherent norm by diagonal energy.

## 4. Balance coordinates and cofinal cuts

The finite harmonic divisor identity gives (5.2) with the displayed sign of (L_Y). The Euler remainder formula is valid at the right-hand integer value and implies \(|R(t)|\le1/t\) for (t\ge1\). This proves the unconditional bound on (B_Y).

For the stronger limit (B_Y=o(1)), the split at \(\eta Y\) is legitimate: the small indices cost at most \(\eta\); for fixed \(\eta>0\), the remaining function (R(1/u)/u) has bounded variation on \([\eta,1]\). Ordinary PNT and Abel summation therefore pay this second part. The proof takes the limits in the required order and does not invoke an unbounded weighted integral whose convergence is unknown.

The cell count and logarithmic square sum in (5.3) give the constants \(\sqrt6\) and \(\sqrt3\). The (R)-mode cost in (5.4) follows from \(\sum_{k\ge Y+1}k^{-2}\le1/Y\). At a literal weak reciprocal crossing, \(|M_Y|\le1/Y\), so the total error \(\eta_Y\) indeed tends to zero.

The Landau argument establishes unboundedly many positive and negative values of (m), and hence unboundedly many weak crossings. The Mellin transform is analytic at every real (z>-1) but has a genuine nonreal pole in that half-plane. Eventual one-sidedness would force its convergence abscissa to be a real singularity and is therefore impossible. This is cofinality only. The proof never requires bounded crossing gaps.

The final comparison is a root-norm inequality. Orthogonal projection is a contraction, so the projected version follows. The text correctly retains the mixed term when passing to squared energies.

## 5. All square denominators and a growing small-core sector

I separately reviewed the added Section 6. Its argument is valid over the entire physical range (x>0), which is stronger than an annulus-specific estimate and is what prevents a loss from the number of annuli.

The complete bound \(\|R\|_{L^2(dx)}^2\le3\) follows by evaluating the part below one and integrating (x^{-2}) above one. Dilation of the exact divisor formula then gives

\[
\|S_q\|_2\le\sqrt{3q}\prod_{p\mid q}(1+p^{-1/2}).
\]

For squarefree (r), the exact coefficient identity

\[
C_Y(r^2)=\frac{m_r(Y/r)^2}{r^2}\ge0
\]

is a direct specialization of the checked factorization. Expanding the positive divisor product and paying its convergent (e^{-3/2}) sum gives the full coherent square-sector norm bound \(3\sqrt3 H_Y\).

For general (q=r^2s), the masks supply (a(s)/(r^2s)), while the kernel norm supplies (r\sqrt{s}\,\beta(r)\beta(s)\). The (r)-sum costs at most (3H_Y\). On squarefree (s), I checked

\[
a(s)\beta(s)\le\frac98d_4(s),\qquad
\sum_{s\le S}\frac{d_4(s)}{\sqrt{s}}\le2\sqrt{S}H_S^3.
\]

This produces \((27\sqrt3/4)H_Y\sqrt{S}H_S^3<12H_Y\sqrt{S}H_S^3\), with no unbounded divisor average left unpaid.

Arbitrary measurable multipliers \(|\omega_q(x)|\le1\) contract the individual (L^2) norms, and the finite triangle inequality pays their coherent sum. Thus a multiplier selecting precisely the output annuli on which (q>Q_j) is allowed. There is no dyadic-count factor. Integer endpoints and step constancy identify that masked integral norm exactly with the discrete norm.

The resulting error after small-core removal is explicitly not claimed to vanish. If \(\log S(Y)=o(\log Y)\), its square is (Y^{o(1)}), as required by the consumer. All square denominators are included when (S=1), and the separately paid (q=1) balance mode is not reintroduced by using (r=1) in a positive numerical majorant.

## 6. Exact Mellin realization and the remaining estimate

The Mellin transform (7.2) is correct on \(-1<\Re z<0\). The integral above one extends to \(\Re z>-1\), and the elementary integral below one exactly cancels the two subtraction terms. The function (e^{u/2}R(e^u)) belongs to both (L^1\) and (L^2\); its Fourier transform is

\[
\frac{\zeta(1/2+it)}{-1/2+it}.
\]

Under the stated Fourier convention, dilation by (d) gives (d^{1/2-it}), which yields (J_{1-s}(q)) and the exact polynomial (D_{Y,Q}(s)). The finite divisor identity recovers (G_Y(s)^2\), including its (q=1) term before that term is removed.

The physical annular window remains a Fourier convolution with factor (1/(2\pi)\). Its integral is defined pointwise by (L^2\) Cauchy–Schwarz, and inversion/Plancherel is used in (L^2\), so no unjustified absolute frequency integral is assumed. Step constancy gives

\[
\int |e^{u/2}V(e^u)|^2du=\int |V(x)|^2dx
 =\sum_{k=b}^{b^2-1}|V(k)|^2
\]

exactly on the native cells. The rough-core polynomial and its windowed version in (7.8)–(7.9) preserve the same normalization and all remaining cross terms. The unwindowed identity (7.7) is valid on its own stated domain and is not used to identify non-native output beyond the strict square step.

## 7. Verification of the #848 sparse-cutoff dependency

The genuinely necessary point is the all-prefix limit

\[
\lim_{Y\to\infty}\frac{\log(1+F_Y)}{\log(Y+1)}=2\Theta-1,
\]

rather than a limsup or a bound on crossing gaps. I independently reconstructed the following parts of #848.

- The completed prefix has exact energy (E_Y\), with (E_Y=F_Y-(Y+1)u_Y^2\le F_Y\).
- Its causal convolution kernel (d) has \(\|d\|_1\le6\), and its output agrees with (e^{-t/2}(t-t^2/2)) before \(\log(Y+1)\). Evaluating at any fixed zero \(\rho\) with \(\Re\rho>1/2\), and bounding only the remaining tail, gives the displayed lower bound at **every** (Y). No rightmost zero or spacing assertion is required.
- In a fixed zero-free half-plane \(\Re s>\theta\), with \(\theta<1\), the Borel–Carathéodory/three-circles construction yields subpower inverse-zeta growth on each narrower half-plane. The half-integer Perron contour and its explicit truncation error then give (M(x)=O(x^{\theta+\varepsilon})\). Partial summation yields the required upper bound for (F_Y\).
- The separate case \(\Theta=1\) uses the elementary \(|m(Y)|\le1\) bound and is not silently excluded. Thus lower and upper logarithmic exponents really coincide.

Consequently, on any unbounded sequence of native crossings, the still-open estimate

\[
\|V^{\rm rough}_{Y,\rho,S(Y)}\|_2^2
 \le Y^{o(1)}(1+F_Y)^{2-\delta},\qquad 0<\delta<1,
\]

together with the proved root-norm error, gives an upper exponent at most \((2-\delta)\kappa\) for an output whose all-prefix lower exponent is (2\kappa\), where \(\kappa=2\Theta-1\). The original (F_Y\) term is smaller when \(\kappa>0\), and the removed core sector contributes exponent zero. This is a valid contradiction if the open estimate is supplied. It neither interpolates between the sparse scales nor establishes that estimate.

## Disposition

The packet establishes concrete complete-sector upper bounds, eliminates the two balance coordinates on cofinal native crossings, and removes every square denominator and a growing small-core sector in coherent norm. Its exact remaining object is correctly specified. These are substantive reductions of the native arithmetic target. The proof's own limitation is also correct: none of the established estimates supplies the required signed upper bound on the remaining large-denominator, large-core sector, so none constitutes a full proof of RH.
