# Independent finite-jet review on the triangular multiplicity lattice

17 November 2026. The stated tail certificate is valid, including the empty-product case \(M=1\). The proofs below concern the zero-sum profile for critical-line zeros and extend to nonnegative synthetic weights with the required moments. RH is needed to infer statements about every nontrivial zero from this critical-line profile. The identification of the profile with an arithmetic prefix limit is a separate theorem. The general discrete boundary theory has a direct antecedent in Infusino–Kuna–Lebowitz–Speer, discussed below. This review makes no publication-priority claim. [Prefix adjudication](director_prefix_inverse_round8.md) · [Adjacent primary readings](../latest62_inverse_adjacent_fullreads.md)

## Taylor inversion

Write \(x_m=m(m-1)\), \(t_m=x_m^2W_m\), \(y_j=\sum_{m\ge2}t_mx_m^j\), and \(a_k=[b^k]C(b)\) for \(k\ge1\). Set \(s=b/(1-b)\). The shifted Rodrigues formula reads

\[
 P_n(1+2s)=\frac{1}{n!}\frac{d^n}{ds^n}\{s^n(1+s)^n\}
 =\sum_{j=0}^n\binom{n}{j}\binom{n+j}{j}s^j.
\]

With \(n=m-1\), differentiation and the pairing \((n-i)(n+i+1)=x_m-i(i+1)\) give

\[
 2P'_{m-1}(1+2s)=x_m\sum_{j\ge0}r_j(x_m)s^j,
 \qquad r_j(x)=\frac{\prod_{i=1}^j(x-i(i+1))}{j!(j+1)!}.
\]

Each sum terminates at \(j=m-2\) for \(m\ge2\). Substituting \(x=1+2u\) into the given finite cost, then squaring, integrating and expanding \(s^\ell=b^\ell(1-b)^{-\ell}\), gives

\[
 a_k=L(p_{k-1}),\qquad L(p)=\int p\,d\nu,
 \qquad p_{k-1}(x)=\sum_{\ell=1}^k\binom{k-1}{\ell-1}\frac1\ell
      \sum_{i=0}^{\ell-1}r_i(x)r_{\ell-1-i}(x).
\]

The only term of degree \(k-1\) comes from \(\ell=k\). Its coefficient is

\[
 \lambda_k=\frac1k\sum_{i=0}^{k-1}\frac{1}{i!(i+1)!(k-1-i)!(k-i)!}
 =\frac{\binom{2k}{k}}{k!(k+1)!}>0,
\]

by Vandermonde convolution. Thus \(y_0,\ldots,y_{M-1}\) follow by triangular substitution from \(a_1,\ldots,a_M\). In particular \(a_1=y_0\), \(a_2=y_1/2\), and \(a_3=(5y_2+8y_1)/36\). Exponential tails are more than sufficient for this finite extraction. In fact \(0\le r_j(x_m)\le x_m^j/(j!)^2\) and \(\sum u^j/(j!)^2\le e^{2\sqrt u}\) for \(u\ge0\), since the series is bounded by the square of \(\sum (\sqrt u)^j/j!\). Therefore

\[
 |c_m(b)-m^2|\le |s|x_m^2 e^{4\sqrt{x_m|s|}}.
\]

The unit-window zero count with multiplicities is \(O(\log(2+T))\), so \(m\le K\log(2+|\gamma|)\), and the ordinate window near height \(n\) contributes \(O(n^{-2}\log^5(2+n)(2+n)^{aK})\) to \(\int e^{a\sqrt x}\,d\nu\). Choose \(0<aK<1\). The constant term sum converges by the same counting bound. Normal convergence in a sufficiently small complex neighborhood of zero now justifies coefficient extraction. [Archived tail argument](director_prefix_inverse_round8.md#2-actual-zeros-give-enough-determinacy)

## Tail mass and weight recovery

For \(M\ge1\), set \(P_M(x)=\prod_{m=2}^{M}(x-x_m)\), \(x_*=x_{M+1}\), \(D=P_M(x_*)\), \(I=L(P_M)\), and \(T=\sum_{m>M}t_m\). The polynomial vanishes at its specified lattice nodes and is positive at all later nodes. It is strictly increasing past \(x_M\) for \(M\ge2\). For \(M=1\), use \(P_1\equiv1\). Thus

\[
 0\le T\le I/D,\qquad
 D=\prod_{m=2}^M(M+1-m)(M+m)=\frac{(M-1)!(2M)!}{(M+1)!}.
\]

The inequality is attained with all positive tail mass at \(x_*\). For \(M\ge2\), equality requires this support condition or an empty tail. In every case \(I=0\) if and only if the tail is empty. When \(M=1\), \(D=1\) and the equality \(I=T=C'(0)\) always holds. For \(M\ge2\), if \(I=0\) then the first \(M-1\) moments recover the masses at \(x_2,\dots,x_M\) by the square Vandermonde system. The extra moment certifies that reduction. For \(M=1\) there are no multiple weights to recover. Add \(W_m=t_m/x_m^2\) for recovered nodes and \(W_1=C(0)-\sum_{m\ge2}t_m/(m-1)^2\) if the constant term is supplied.

The same jets give certified approximate individual recovery. For \(2\le j\le M\), set

\[
 \ell_j(x)=\frac{P_M(x)}{(x-x_j)P_M'(x_j)}.
\]

This polynomial is the cardinal function on the first \(M-1\) lattice nodes. On the tail its sign is \((-1)^{M-j}\). Consequently

\[
 0\le(-1)^{M-j}\bigl(L(\ell_j)-t_j\bigr)
 \le\frac{I}{|P_M'(x_j)|(x_*-x_j)}.
\]

The upper error bound is attained when all tail mass is at \(x_*\). Any certified upper bound for \(I\) can replace \(I\), and the recovered interval for \(t_j\) can be intersected with \([0,\infty)\). The omitted contribution to \(\sum m^2W_m\) lies between zero and \(I/(M^2D)\), and the omitted contribution to \(\sum W_m\) lies between zero and \(I/(x_*^2D)\).

Additional moments give \(I^2/L(P_M^2)\le T\) when \(I>0\) by Cauchy–Schwarz on the tail, with equality for a single tail node. One extra moment beyond the original certificate gives a different sharp lower bound for its filtered data. For \(M\ge2\), take \(J=L(xP_M)\), \(I>0\), and \(q=J/I\). The filtered probability \(P_M\nu/I\) has mean \(q\ge x_*\), and \(T/I\) is its average of \(f(x)=1/P_M(x)\). The function \(f\) is strictly decreasing and strictly convex on \((x_M,\infty)\), since \(f''/f=(\sum_{m=2}^M 1/(x-x_m))^2+\sum_{m=2}^M 1/(x-x_m)^2\). Let \(f_{\rm lin}\) interpolate \(f\) linearly between consecutive tail nodes. Its slopes are increasing, so Jensen gives the sharp filtered lower bound

\[
 T\ge I f_{\rm lin}(q).
\]

The two adjacent nodes bracketing \(q\) attain equality by matching \(I,J\). For only these two filtered moments, the original upper bound \(I/D\) remains the supremum, by using \(x_*\) and a remote node to reach the prescribed mean and letting the remote node tend to infinity. The supremum is attained exactly when \(q=x_*\). Further constraints from the unfiltered moments can change both extrema. With just \(I>0\) and no other constraint, a single remote node of mass \(I/P_M(x_m)\) gives arbitrarily small positive \(T\) for \(M\ge2\).

With two extra moments, let \(H=L((x-x_*)^2 P_M)\). If \(H>0\), Cauchy–Schwarz applied to the filtered probability gives \(\Pr(x>x_*)\ge (J-x_*I)^2/(IH)\). Since \(f(x)\le f(x_{M+2})<f(x_*)\) on those nodes,

\[
 T\le I/D-\bigl(1/D-1/P_M(x_{M+2})\bigr)\frac{(J-x_*I)^2}{H}.
\]

This improves the basic upper bound whenever the filtered tail includes a node above \(x_*\), and it is exact for a tail supported on \(x_*\) and \(x_{M+2}\). If \(H=0\), the only possible positive tail node is \(x_*\) and the basic bound is exact.

## Rigorous rounding and the zero test

With \(A_{kj}=[x^j]p_{k-1}(x)\) and column indices \(j=0,\ldots,M-1\), compute the exact rational row \(u=([x^j]p)_j A^{-1}\). Then \(L(p)=\sum_{k=1}^M u_k a_k\). For independent certified intervals \(a_k\in[\hat a_k-\epsilon_k,\hat a_k+\epsilon_k]\), the exact projection of the box is the interval centered at \(\sum u_k\hat a_k\) with radius \(\sum|u_k|\epsilon_k\). This accounts for the dependencies that arise if each recovered moment is enclosed separately. Use exact decimal-to-rational endpoints or directed outward rounding. The enclosure covers the quantity only if the input intervals cover the true Taylor coefficients.

For \(p=P_M\), write \(I^+\) for the certified upper endpoint. A negative \(I^+\) rules out positive lattice feasibility. If the data are feasible and \(I^+=0\), there is an exact support certificate. A positive \(I^+\) gives the mass bound \(I^+/D\). The diagonal raw moment sensitivity from \(a_M\) is \(1/\lambda_M\), which grows rapidly. For the normalized statistic \(I/D\), its last coefficient is instead

\[
 \frac1{\lambda_M D}=\frac{M(M+1)^2}{\binom{2M}{M}^2}.
\]

The full row and the actual coefficient uncertainties determine the normalized error. For example at \(M=3\), \(I=12a_1-(96/5)a_2+(36/5)a_3\) and \(D=60\). A box of half-width \(10^{-6}\) around \((8,18,104/3)\) certifies \(T\le1/1562500\). The exact center has zero tail, whereas the box permits a positive remote atom.

For simplicity on the critical line, \(a_1=0\) suffices by positivity and is necessary. Every \(a_k\) with \(k\ge1\) is at least \(y_0\), since the \(\ell=1\) term in \(p_{k-1}\) is 1 and each other term is nonnegative on the lattice. Thus an exactly zero nonconstant coefficient, or a rigorous upper endpoint of zero with feasibility, suffices. A box around an admissible positive constant profile with each coefficient upper endpoint strictly positive permits a multiple atom. Indeed take \(W_2=\delta>0\), reduce \(W_1\) by \(4\delta\), and use \(c_2(b)=4/(1-b)\) to obtain all \(a_k=4\delta\). A sufficiently small \(\delta\) keeps the data in the box. More generally, for a jet in the interior of a positive-width coefficient box with \(C(0)>0\), one can scale the existing profile by \(1-\epsilon\) and put the freed constant-term budget on any prescribed remote node, preserving \(C(0)\) and remaining in the box for sufficiently small \(\epsilon>0\) depending on the node. These are statements about positive profiles with exponential tails, including finitely supported fixtures. Finite-\(N\) staircase derivatives do not furnish the input intervals for the limiting profile.

## The lattice moment problem and certified optimization

Infusino, Kuna, Lebowitz and Speer prove an exact realizability procedure for the truncated moments of probability measures on \(\mathbb N_0\) and extend it to infinite discrete, lower-semibounded sets in §8. Normalize by \(y_0>0\) and shift the lattice by \(x_2\) to apply their result. Their §2 sign-admissible family is built from adjacent pairs, with an additional factor at the minimum support node in odd degree. The first \(M-1\) nodes used in \(P_M\) have exactly this pattern. Lemma 4.2, Theorem 4.4 and Remark 4.5 give the underlying exact boundary and extension theory. In particular, boundary realizability yields a unique measure contained in the zeros of a nonnegative polynomial of the available degree, with additional moment compatibility determined by that measure. The triangular normalization and error propagation above specialize this setting to the prefix profile. [Primary preprint, §§2, 4 and 8](../../sources/latest62_inverse_adjacent/1504.02989.pdf) · [Published article](https://doi.org/10.1016/j.jmaa.2017.02.060)

For interior exact moment data, one can prescribe the presence of any lattice node by subtracting a sufficiently small positive mass times its moment vector, representing the remaining nearby interior datum, and restoring the atom. Thus the pure moments at an interior point cannot bound the maximum multiplicity. If \(C(0)\) is also fixed, the moment measures must satisfy the separate inequality \(\sum_{m\ge2}t_m/(m-1)^2\le C(0)\), since the difference is \(W_1\). The interior planting argument still works if a profile with the given jet has \(W_1>0\). Mix a sufficiently small amount of the representing measure with the prescribed atom into that profile to preserve the inequality and the exact moments.

For an example with zero simple slack, prescribe \(y_0=1\), \(y_1=6\), \(C(0)=1/4\). The pure moment pair is interior since its mass is positive and its mean exceeds \(x_2=2\). Define \(g(x)=u^{-2}\) with \(u=(\sqrt{1+4x}-1)/2\), so \(g(x_m)=1/(m-1)^2\). The derivative \(g'(x)=-2/(u^3(2u+1))\) is strictly increasing on \(x>0\), making \(g\) strictly convex there. Jensen gives \(\int g\,d\nu\ge g(6)=1/4\), with equality only for \(\nu=\delta_6\). The constant term inequality therefore forces the unique measure \(\delta_6\) and \(W_1=0\), even though the pure moment data are interior.

For measured moments through degree \(d\), Hankel PSD conditions apply to \(L(q^2)\). Localizing PSD conditions apply to \(L(gq^2)\) when \(g\) is nonnegative on the lattice and the degree fits. Examples are \(x-x_2\), each gap polynomial \((x-x_j)(x-x_{j+1})\), and their products. The Stieltjes-type half-line tests alone allow \(\delta_4\), which a single gap test excludes since \((4-2)(4-6)=-4\). Even every degree-\(d\) test \(L(p)\ge0\) for \(p\) nonnegative on the lattice characterizes only the closure of the moment cone. For \(d\ge2\) an explicit counterexample is

\[
 (1,2,2^2,\ldots,2^d)+e_d,
\]

where \(e_d\) is the unit vector in the final coordinate. It is a limit of moments of \(\delta_2+x_m^{-d}\delta_{x_m}\). Any positive representing measure would have mass 1 and mean 2, forcing \(\delta_2\), whose final moment is \(2^d\). Each approximating measure has finite support and hence all square-root exponential moments. An asserted exponential tail without a common bound leaves this escape possible. Exact Hankel or polynomial zeros can give genuine finite-support certificates when feasibility is already known.

For a bounded lattice observable \(h\), a polynomial \(p\) of degree at most \(d\) with \(p(x_m)\ge h(x_m)\) gives the certified upper bound \(L(p)\ge\sum t_m h(x_m)\). A pointwise minorant gives the corresponding lower bound. This includes tail mass and single-node weights by taking indicators. Exact rational polynomials give finite checks for these indicators. Past the last breakpoint, \(p-h\) is a single polynomial. If it is nonzero of positive degree, its leading sign controls the whole tail past a rational root bound such as \(1+\max_{i<n}|c_i/c_n|\). Evaluate the finitely many nodes up to that bound and handle constant or zero polynomials directly. The same procedure applies to minorants by negation. With \(C(0)\) supplied, a pointwise majorant \(p(x_m)+\kappa/(m-1)^2\ge h(x_m)\), \(\kappa\ge0\), gives the upper bound \(L(p)+\kappa C(0)\). It can be checked for indicator \(h\) by multiplying by \((m-1)^2\) and testing the resulting polynomial in \(m\) past the breakpoint. Use the projected interval formula above to evaluate a certificate, or optimize the linear functional over the original jet constraints. A floating-point SDP or finite-column LP value requires a verified one-sided certificate on the full lattice to bound the full problem.

For exact feasible moment data, optimization over these polynomial certificates yields the true supremum and infimum for bounded \(h\), with possible nonattainment. Here is a proof for \(d\ge1\). Adjoin the \(h\) coordinate to \(v(x)=(1,x,\dots,x^d)\), normalize the joint vectors by \(1+x^d\), and add their limit \((e_d,0)\). Their convex hull is compact. Its conic hull is closed since each normalized generator satisfies \(y_0+y_d=1\), so this is the closure of the joint lattice moment cone. The section at measured \(y\) is compact in the objective coordinate because \(|\sum t_m h(x_m)|\le\|h\|_\infty y_0\). Close the objective coordinate downward by adding the downward ray. The resulting cone remains closed since a sequence with bounded moment coordinates also has bounded original objective and downward shift. For \(R\) above the section maximum, separate \((y,R)\) strictly from this cone. The separating functional has form \((p,-\beta)\) with \(\beta\ge0\) by the downward ray. Evaluating at any feasible \((y,z)\) and at \((y,R)\) forces \(\beta>0\). Evaluation on each lattice generator gives the polynomial majorant \(p/\beta\) and its value at \(y\) is below \(R\). Replace \(h\) by \(-h\) for the lower bound.

To see that escape does not change these extreme values at a feasible exact \(y\), represent any point of the joint closed cone as a finite positive lattice measure \(\eta\) and an escape contribution \(a e_d\), \(a\ge0\). If \(a=0\) the representing measure has the required moments. If the first \(d\) moment coordinates lie on the boundary of their closed cone, a nonzero supporting polynomial of degree at most \(d-1\) is nonnegative on the lattice and has integral zero. Both \(\eta\) and every true representing measure live on its finite zero set, with weights fixed by the lower moments. Thus feasibility forces \(a=0\) in this case.

If \(a>0\), the lower moment vector is interior. Choose \(d\) distinct lattice nodes \(z_1,\dots,z_d\). There is a finite anchor measure matching the lower moments with positive weights at these nodes. To construct it, subtract a sufficiently small positive mass at each proposed node from the lower moment vector, which leaves an interior point. An interior point of the closed cone belongs to the finite lattice cone, since it can be enclosed by a simplex whose vertices are approximated by points of the finite cone. Mix an arbitrarily small amount of the anchor into \(\eta\), keeping the top moment below \(y_d\). Let \(B=(z_i^j)_{0\le j<d,1\le i\le d}\). Adding mass \(w\) at a remote lattice node \(x\) and subtracting the weight vector \(w B^{-1}(1,x,\dots,x^{d-1})^T\) from the anchor nodes preserves all lower moments. The change in top moment per unit \(w\) is \(x^d-O(x^{d-1})\), positive for large \(x\). Choose \(w\) to fill the top-moment deficit. Then \(w=O(x^{-d})\) and the correction at the anchor nodes is \(O(x^{-1})\), which preserves positive weights for large \(x\). The effect on any bounded objective tends to zero. Let the initial anchor mixing tend to zero. This proves sharpness for feasible exact moments while the counterexample above shows a separate feasibility issue. For \(d=0\) and the indicator objectives, the upper and lower bounds follow directly by putting the prescribed total mass at a node attaining the desired indicator value. An interval relaxation that admits escape may include infeasible moment vectors, so sharpness for feasible exact moments does not by itself certify interval feasibility.

A known uniform moment cap \(B_0\ge\int x^{d+1}\,d\nu\) permits a finite rational LP enclosure with convergence, including for interval jets. For each cutoff at \(x_N\), retain nonnegative lattice weights through \(N\), enforce that their \((d+1)\)-st moment is at most \(B_0\), and add residual variables

\[
 0\le r_j\le B_0/x_{N+1}^{d+1-j},\qquad 0\le j\le d.
\]

Apply the measured jet constraints to the retained sums plus residuals, preserving the linear relations between moments and jets. If the constant term is supplied, constrain the retained sum of \(g(x_m)t_m\) by the upper endpoint for \(C(0)\). The same constraint for the full sum follows at the limit. For \(0\le h\le1\), the omitted objective is between zero and \(B_0/x_{N+1}^{d+1}\). The finite LP contains every admissible vector by restricting its measure. Conversely, along any sequence of feasible cutoffs tending to infinity, bounded masses and diagonal subsequences produce limiting lattice weights. The cap and the displayed tail bounds control moments through \(d\) uniformly, so these weights have the required data, respect the cap by Fatou, and give the limit of the objective. Thus for feasible compact interval data the lower and upper outer bounds converge to the true extrema with this cap. The LP and its rational dual certificates use the cap as an additional verified input. For example, if \(\int e^{a\sqrt x}\,d\nu\le A_0\) is explicit, use \(B_0=A_0(2(d+1)/(ae))^{2(d+1)}\) or any rational upper bound. The existential actual-zero exponential estimate supplies finiteness, while a numerical certificate needs a numerical bound.

## Exact controls

An ephemeral SymPy calculation used Rodrigues polynomials to compare 132 exact pairs \((m,k)\) with \(2\le m\le12\), \(1\le k\le12\), against the triangular formula. For every \(1\le M\le12\), it independently checked the denominator, the normalized last-coefficient sensitivity, exact saturation at \(M+1\), and zero after deleting that atom. It checked all 66 reconstructed masses on the resulting finite lattices and the rational interval example at \(M=3\). The fixtures used synthetic masses \(t_m=m+1\) on the tested support. Separate rational fixtures at \(M=4\) checked equality in the improved upper bound for two successive tail nodes and strict improvement when a third tail node has mass.
