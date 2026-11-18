# Corrected HLZ smoothing sufficient for Proposition 3

Reviewer /root/geometry_corpus_64. Source is Heap–Li–Zhao, *Algebra & Number Theory* 16 (2022), 1589–1625, journal Theorem 5, (24), and §3.2, in the pinned PDF with SHA-256 6162632530cbeee8c1664d7ea53e844cffa9dbc53fe00a8cd8270e2d713b6a82. This statement repairs the use of diagonal smoothing in Proposition 3. It takes the explicit unsmoothed Theorem 5 as input. [Journal PDF](../../sources/classical63_derivative_moments/hlz2022print.pdf) · [Version and dependency receipt](../../sources/geometry75/hlz_witnesses.sha256)

## Statement

Fix \(0<\theta<1/2\), write \(L=\log T\), and take three fixed radii \(0<r_1<r_2<r_3\) sufficiently small for the shifts in journal Theorem 5. Put \(C_i=\{|z_i|=r_i/L\}\). For \(z_i\in C_i\) define
\[
H_{\mathbf z}(w)=e^{w^2}\prod_{i\ne j}
 \left(1-\frac{2w}{z_i-z_j}\right),
\qquad
(\alpha,\beta,\gamma)=(z_1,-z_2,z_3).
\]
One common kernel serves all permutations of the nodes. Let \(Z_{\alpha,\beta,\gamma;h,k}\) be the explicit local kernel in (24), for coprime \(1\le h,k\le T^\theta\). Define
\[
D_{\mathbf z;h,k}
 = \frac1{2\pi i}\int_{(c_0/L)}\frac{H_{\mathbf z}(w)}{w}\,
 \sum_{hm=kn}\frac{ f_{\alpha,\gamma}(m)n^{-\beta}}
 {\sqrt{hkmn}}\left(\frac{T^2}{mn}\right)^w\,dw ,
\]
where \(c_0>0\) is fixed sufficiently large relative to \(r_3\), and the initial line places all zeta numerator arguments to the right of 1. Then for every \(A>0\) there is a fixed integer \(B_0\) such that, uniformly on the three circles and for the stated \(h,k\),
\[
 hk D_{\mathbf z;h,k}
 =Z_{\alpha,\beta,\gamma;h,k}
   +O_{A,\theta,\mathbf r}\bigl(\tau(k)^{B_0}L^{-A}\bigr).
\tag{S}
\]
The same assertion holds with permuted node slots. This includes weights with fixed divisor envelopes in the \(g,h,k\) sum of (24), because for every fixed \(M\) the divisor-weighted harmonic sums over \(g,h,k\le T^\theta\) grow by at most a fixed power of \(L\).

Let \(R(t;\alpha,\beta,\gamma)\) be the sum of the three **unsmoothed** choices in (24), including their powers of \(t/(2\pi)\) and the fixed arithmetic coefficients or the \(g,h,k\) sum. For the outer shifts assume \(|\alpha|,|\beta|,|\gamma|<r_1/(2L)\). First represent the combined \(R\) by its three-variable squared-Vandermonde integral. In this representation one can replace each unsmoothed value on \(C_1\times C_2\times C_3\) by \(hkD_{\mathbf z;h,k}\). After integrating over \(0<t<T\) and taking any fixed number of derivatives in the outer shifts on a smaller polydisc, this costs \(O_A(TL^{-A})\) for every fixed \(A\). This corrected, contour-based statement is sufficient for the \(\alpha,\beta,\gamma\) derivatives used in Proposition 3. The extension across collision hyperplanes applies to the **combined outer expression**, including its contour approximation. No separate \(H_{\mathbf z}\) is defined for colliding nodes.

## Proof of pointwise smoothing

For \(m=k\ell,n=h\ell\), the Dirichlet expression in the integrand equals
\[
\frac{T^{2w}}{(hk)^{1+w}h^\beta}
\frac{\zeta(1+\alpha+\beta+2w)\zeta(1+\beta+\gamma+2w)}
     {\zeta(1+\beta+2w)}
\prod_{p^e\parallel k}
\frac{\sum_{j\ge0} f_{\alpha,\gamma}(p^{j+e})p^{-j(1+\beta+2w)}}
     {\sum_{j\ge0} f_{\alpha,\gamma}(p^j)p^{-j(1+\beta+2w)}} .
\]
The numerator pole conditions are \(2w=-\alpha-\beta,-\beta-\gamma\), or \(z_2-z_1,z_2-z_3\) in node coordinates. The six factors cancel every ordered difference that can occur, with the necessary multiplicities. The kernels are normalized at zero, since the radii force pairwise separations at least \(\min_{i<j}(r_j-r_i)/L\).

On any fixed real strip and for each fixed derivative order \(j\), the Gaussian kernel has a uniform seminorm bound
\[
|\partial_w^j H_{\mathbf z}(\sigma+iv)|
   \ll_{j,\mathbf r,\mathrm{strip}}
    L^6(1+|v|)^{6+j}e^{-v^2}.
\]
No shift derivatives of \(H_{\mathbf z}\) are needed. For the local factor use \(U=p^{-\alpha},V=p^{-\gamma},x=p^{-1-\beta-2w}\). The exact quotient is
\[
 V^e+(U-1)\Big(\sum_{j=0}^{e-1}U^jV^{e-1-j}\Big)\frac{1-Vx}{1-x}.
\]
For \(\Re w\ge -c/\log_3 T\) and sufficiently large \(T\), \(|x|\le p^{-3/4}\). Taking the product over \(p^e\parallel k\) then bounds it by a fixed power of \(\tau(k)\) times \(k^{O(1/L)}=O_{\theta,\mathbf r}(1)\). This bound is independent of \(\Im w\).

Truncate at \(|\Im w|=M\sqrt{\log_2 T}\) for a sufficiently large constant \(M\) depending on \(A\). Absolute Euler bounds on the initial line give polynomial \(L\) factors, so the omitted tails are \(O_A(L^{-A}\tau(k)^{B_0}/hk)\). On the finite rectangle move to \(\Re w=-c/\log_3 T\). Choose the fixed \(c>0\) small enough for the zeta zero-free region at the indicated heights and leave margin for the \(O(1/L)\) shifts. The reciprocal zeta has a zero at its pole at 1 and no additional poles in this rectangle. The normalization and pole cancellation leave exactly the \(w=0\) residue \(Z/(hk)\). Bounds for the zeta factors in the rectangle are polynomial in \(L\) on the horizontal and left segments. The Gaussian makes the horizontal terms smaller than the desired log power, and the left factor \((T^2/(hk))^{-c/\log_3 T}\) gives every log saving. This proves (S). The rendered \(\log_3 T\) really is an iterated logarithm.

## Confluence and the Proposition 3 bound

Let \(u=(\alpha,-\beta,\gamma)\), \(t_0=t/(2\pi)\), \(\Delta(\mathbf z)=\prod_{i<j}(z_j-z_i)\) and \(P_u(z)=\prod_i(z-u_i)\). For distinct \(u_i\), the unsmoothed three-choice combination for one arithmetic pair is exactly
\[
-\frac{t_0^{-(u_1-u_2+u_3)/2}}{2(2\pi i)^3}
 \int_{C_1}\int_{C_2}\int_{C_3}
  \frac{\Delta(\mathbf z)^2\,t_0^{(z_1-z_2+z_3)/2}
         Z_{z_1,-z_2,z_3;h,k}}
       {\prod_i P_u(z_i)}\, dz_3\,dz_2\,dz_1 .
\]
The unsmoothed \(Z\) kernel has at most a simple pole on each of \(z_1=z_2,z_2=z_3\), and the exact local quotients above are regular in the shifts, including \(z_1=z_3\). Thus \(\Delta^2 Z\) is holomorphic in the working polydisc and zero on each repeated-selection diagonal. Evaluating the residues leaves only the six permutations. The ratio \(\Delta(u)^2/\prod_i P_u'(u_i)=-1\); the two choices of ordered outside slots for each middle slot give the factor 2. The multipliers are precisely \(1,t_0^{-\alpha-\beta},t_0^{-\beta-\gamma}\). The integral extends holomorphically to colliding **outer** shifts. This computation must precede smoothing. Clearing the denominator of \(H_{\mathbf z}\) by \(\Delta^2\) may spend both copies of a collision factor, and alone it cannot prove that repeated selections vanish for a residue calculation with the smoothed integrand.

Apply (S) only on the separated contours. Their lengths and the Vandermonde respectively cost \(L^{-3}\) and \(L^{-6}\), the nine denominators cost \(L^9\), and each fixed outer derivative costs a fixed additional log power. No loss obstructs a prescribed saving. The \(t\)-power factors have integral \(O(T)\), uniformly on the small shift polydisc, and any fixed derivatives of those factors add only powers of \(L\). With divisor envelopes the arithmetic sum also adds only fixed log powers. This proves the extension and differentiated error in the statement.

For Proposition 3, now unfold the diagonal in §3.2 using \(N=a+b\) and \(x=T^{\theta/N}\). In the \(2N\) Mellin variables take \(\Re s_j=\kappa=\lambda/\log_2 T\) for a sufficiently small fixed \(\lambda>0\). Move \(w\) from \(\Re w=1\) to \(-2\kappa/3\), truncating at \(M'\sqrt L\). At this stage the Gaussian tail beats \(T^{2+2\theta\kappa}\) for \(M'\) sufficiently large. All fractional zeta arguments involving any unbounded imaginary \(s_j\) have real part to the right of 1 by at least \(\kappa/3-O(1/L)>0\). The bare reciprocal \(\zeta(1-z_2+2w)^{-1}\) is handled by the zero-free rectangle, choosing \(\lambda\) small enough for height \(O(\sqrt L)\). On the left line the net \(T\)-power is \(T^{(-4/3+2\theta)\kappa}\), which beats the fixed log loss. The cancellation signs are unchanged from (S). The residue at \(w=0\) has \(H_{\mathbf z}(0)=1\).

The subsequent §3.2 Mellin localization on \(\Re s_j=1/\log x\) uses the first prime coefficients of (22), the \(B\)-power denominators, and the pole expansion at 1. As in (23), its uniform log power is \(N^2/b^2-2N/b+1=k^2\), with \(k=a/b\) and \(B\ge\lceil14+12k\rceil\). The triple derivative therefore gives \(O(TL^{k^2+3})\). The separately estimated \(J\)-term has the same upper bound from §3.1. For the mollifier's coefficient hypothesis use the divisor-envelope quadratic padding detailed in the advocate review before applying Theorem 5. This completes the smoothing dependency of the proposition. It does not serve as an independent proof of Theorem 5 or its sharp continuous moment input. [Whole-work advocate review](geometry75_hlz_whole_advocate.md)

## Proof dependencies

1. Journal Theorem 5 with bounded complex shifts supplies the explicit \(J\) term and both reflected, unsmoothed \(Z\) combinations. Coefficient padding precedes this input.
2. The local Euler identity and the zeta zero-free region give (S) on separated node circles. Independently, the unsmoothed residues and the Vandermonde give the holomorphic combined expression.
3. Apply (S) inside that expression, using divisor sums and complex differentiation bounds to retain arbitrary log savings.
4. Section 3.2's Euler-factor expansion and localized Mellin estimate bound the smoothed \(Z\) portion. Section 3.1 bounds the independent \(J\) portion. Their sum gives Proposition 3.

## Independent comparison and source error

Release75 takes the same unsmoothed-first route, identifies the same pairwise pole factors, uses one \(L^6\)-bounded common symmetric kernel on separated contours, and retains the final factor \(T\). The proof above makes the error quantifiers explicit, separates the two contour heights \(M\sqrt{\log_2 T}\) and \(M'\sqrt L\), and gives the residue identity and its repeated-selection condition. The small constants in the contour widths are chosen from the actual zero-free region. [Release75 independent repair](release75_hlz_whole_skeptic.md)

The printed Lemma 6 and Theorem 4 specify zeros at \(2w=\beta-\alpha,\beta-\gamma\) in the named shift coordinates. Uniform75 gives a separated-shift example with \(h=k=1\), the printed weight conditions and a missed residue of order \(\log T\). That is a counterexample to the literal Lemma 6 estimate. The repaired assertion uses the actual negative sums and imposes separated nodes, quantitative Gaussian bounds and the explicit confluence procedure above. It makes no assertion for arbitrary printed weights or about the full \(h,k\le T\) range of the source lemma. Theorem 5 alone does not use this smoothing step. [Uniform75 counterexample and journal comparison](uniform75_hlz_lemma6_review.md)
