# Noor's original Hardy-space criterion: source audit and exact unitary reconstruction

Researcher/reviewer: `li_advocate`. Date: 2026-11-17. Source: **PAPER-NOOR-A001**, S. Waleed Noor, *A Hardy space analysis of the Báez-Duarte criterion for the RH*, arXiv:1809.09577v4 (9 May 2019), all 11 preprint pages read. Published identity: *Advances in Mathematics* 350 (2019), 242–255, DOI 10.1016/j.aim.2019.04.064. The publisher PDF was inaccessible; no claim of a journal/preprint comparison. Primary private source: `sources/noor_advocate_round4/noor2019_advocate.pdf`; metadata: `sources/noor_advocate_round4/noor_advocate_crossref_round4.json`.

## Exact spaces and maps

Noor's equation (0.1), p1, uses the sequence norm
\(\|x\|^2=\sum_{n\ge1}|x(n)|^2/[n(n+1)]\). His weighted Bergman space \(A\), equations (1.1)–(1.2), p2, has
\[
\|g\|_A^2=\sum_{n\ge0}\frac{|g_n|^2}{(n+1)(n+2)}
=\int_{\mathbb D}|g(z)|^2(1-|z|^2)\,dA(z).
\]
Here area is normalized. This norm is equivalent, **not identical**, to the later coefficient norm of \(D_{-2}\):
\(\tfrac12\|g\|_{D_{-2}}^2\le\|g\|_A^2\le\|g\|_{D_{-2}}^2\).

Equations (1.3)–(1.4), pp2–3, are
\[
\Psi x(z)=\sum_{n\ge0}x(n+1)z^n,
\qquad Tg=\frac{((1-z)g)'}{1-z}=g'-\frac g{1-z}.
\]
The direction of the source's unitary map is **\(T:H^2\longrightarrow A\)**. Its inverse composed with \(\Psi\) is \(\Phi=T^{-1}\Psi:\ell^2_\omega\to H^2\). Source p3 cites a Dirichlet-space textbook for the isometry; the following gives an independent proof of that particular dependency.

## Independent complete proof of the unitary assertion

Put \(v_n=Tz^n\). Then \(v_0=-1/(1-z)\), while for \(n\ge1\),
\[
v_n=nz^{n-1}-\sum_{j\ge n}z^j.
\]
Thus
\[
\|v_n\|_A^2=\frac{n^2}{n(n+1)}+
\sum_{j\ge n}\frac1{(j+1)(j+2)}=1.
\]
The case \(n=0\) follows from the same telescoping tail. For \(m>n\), the product of the spike at \(m-1\) with the earlier tail contributes \(-1/(m+1)\), and the common tail contributes \(+1/(m+1)\). Hence the \(v_n\) are orthonormal. The polynomial operator therefore extends isometrically from \(H^2\) to a closed range in \(A\). Convergence in either space implies locally uniform convergence, so this extension agrees with the displayed differential formula.

Every polynomial \(q\) lies in its range. Indeed set
\[
f(z)=\frac{c+\int_0^z(1-w)q(w)\,dw}{1-z},\qquad
c=-\int_0^1(1-w)q(w)\,dw.
\]
The numerator is a polynomial vanishing at 1, so \(f\) is polynomial and \(Tf=q\). Since polynomials are dense in \(A\), the closed range is all of \(A\). This proves the claimed unitary isomorphism without using the cited textbook lemma.

## Exact target and preimages

Noor Theorem 1, p1, imports the sequence Báez-Duarte/Bagchi equivalence: RH iff the constant sequence 1 is in the closed span of \(r_k(n)=k\{n/k\}\), \(k\ge2\). Theorem 6 and Lemma 7, pp4–5, transport this criterion to
\[
h_k(z)=\frac1{1-z}\log\frac{1+z+\cdots+z^{k-1}}k.
\]
The analytic logarithm is fixed by the value \(-\log k\) at zero; the finite geometric sum has no zeros in the disk. The exact identities are
\[
T(-1)=\Psi1=\frac1{1-z},\quad
Th_k=\Psi r_k=\frac1{1-z}\left[\log(1+z+\cdots+z^{k-1})\right]'.
\]
The apparently free constant in a formal preimage is removed by \(H^2\)-membership: among
\((1-z)^{-1}\log[(1+\cdots+z^{k-1})/c]\), the allowed positive normalization is \(c=k\). A nonzero extra multiple of \((1-z)^{-1}\) does not lie in \(H^2\). Noor proves the valid preimage belongs to \(H^2\) using local Dirichlet spaces at 1.

The coefficient identity, displayed on p6, is
\[
[z^n]h_k=H_n-H_{\lfloor n/k\rfloor}-\log k,\qquad H_0=0.
\]
It also follows directly by expanding \(\log(1-z^k)-\log(1-z)-\log k\) and multiplying by \((1-z)^{-1}\).

## Closure, projection, and domain distinctions

* Theorem 8, p6: RH is equivalent to \(\overline{\mathcal N}^{H^2}=H^2\), where \(\mathcal N=\operatorname{span}\{h_k:k\ge2\}\). The operators \(W_nf=(1+\cdots+z^{n-1})f(z^n)\) preserve this span because \(W_nh_k=h_{nk}-h_n\). The constant 1 is cyclic for this semigroup.
* Theorem 9 and Lemma 11, pp7–8: **unconditionally**, \((I-S)\mathcal N\) is dense in \(H^2\). In particular, \(\sum_{k=2}^N\mu(k)k^{-1}(I-S)h_k\to1-z\) in \(H^2\). Noor uses PNT identities \(\sum\mu(k)/k=0\), \(\sum\mu(k)\log k/k=-1\), and a square-summable divisor-bound tail. Reconstructing that proof found no issue: the tail coefficients are \(j^{-1}\sum_{d\mid j,d\le N}\mu(d)\) for \(j>N\), dominated in square by \(\tau(j)^2/j^2\), whose sum converges using \(\tau(j)\ll_\epsilon j^\epsilon\), \(\epsilon<1/2\).
* Theorem 10, pp7–8: \(\mathcal N\) is dense for the **compact-open** topology. Multiplication by \((1-z)^{-1}\) is continuous in that topology, but is unbounded on \(H^2\). The paper explicitly distinguishes these topologies. Its result cannot be inverted into norm density in \(H^2\).
* Theorem 12, p9: \(\mathcal N^\perp\cap D_{\delta_1}=\{0\}\), with **local** Dirichlet space at 1. For \(\varphi=(1-z)^{-1}\), the unbounded multiplication domain is \(\{f\in H^2:\varphi f\in H^2\}\); the adjoint domain is identified with \(D_{\delta_1}\) using cited results. Density of \((I-S)h_k\), followed by the adjoint argument, proves the stated restricted orthogonality result. It is not a general bounded inverse or a graph-core theorem. The source's \(P_+\) is the Hardy orthogonal projection in Toeplitz definitions; its later \(P:H^2\to H_0^2\), p10, deletes the constant coefficient. Neither projection licenses an inverse on an arbitrary weighted closure.
* Theorem 13, p10, gives an embedding into the periodic dilation-completeness problem, not a surjective identification; the source explicitly supplies a vector outside the image.

## Relation to Gallardo–Gutiérrez–Seco 2025

The original Noor map is the strict case \((\alpha,a)=(-2,1)\), so it has no critical-range defect. It does **not** by itself establish a bounded inverse for \(T_1:D_{-1}\to D_{-3}\). That operator is injective with dense proper nonclosed range, as independently reconstructed in the separate operator reviews.

The later Theorem 5.5 is visibly stated for \(\alpha\in[-3,-2]\), \(1\le a<(1-\alpha)/2\), with target \((1-z)^{1-a}\) in \(D_{\alpha+2}\). Its only critical pair in that parameter range is \((-3,1)\), with target 1 in \(D_{-1}\). A separate repair of that target statement is proved in `proposals/independent_campaigns/noor_critical_bergman_advocate_round4.md`; it uses the exact Noor coefficients, a quantitative unconditional Mertens bound, weak convergence, and the semigroup invariance. It does not invert \(T_1\).

For general \(a>1\), the source multiplier \(h=(1-z)^{a-1}\) is not bounded away from zero. The original Noor arguments do not automatically provide the stronger weighted-range closure required by a compositional inverse there. The precise missing statement remains the weighted-core/approximation implication in `audits/adversarial_reviews/gallardo_seco_operator_impact_advocate_round4.md`. No assertion that the later Theorem 5.5 is false follows from that unresolved implication.

## Audit status and limitations

Whole preprint: substantive Level 1 reading. Targeted Level 2 reconstruction: exact unitary map, preimage/coefficients, semigroup identity, and Lemma 11's elementary convergence argument. The external Báez-Duarte/Bagchi equivalence and the cited local-Dirichlet/adjoint-domain theorems have not all been independently reconstructed here. The newly supplied Bergman repair is a separate argument, not an attribution to Noor and not a novelty claim. Classification for the inspected original arguments: independently checked with no issue found in the portions stated above.
