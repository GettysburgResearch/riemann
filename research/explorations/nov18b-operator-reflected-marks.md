# Cubic cancellation between reflected prime marks

**Result.** In the Eisenstein-field completed-row estimate of OpenAI, §15.1, one may replace the excess in the squared row norm by
\[
 \left(\frac{1+\ell'-2M'}3\right)_++O(\eta)
\]
whenever \(M'+\ell'\le1\). Here \(\eta\) is the maximum individual mark length, \(M'\) is the row-length exponent and \(\ell'\) is the total surviving marked length. This uses the actual product-form prime marks. The original exponent argument gives \(((1+3\ell'-2M')/4)_+\). Two changes give the improvement. Cubic reciprocity allows some prime marks to join the squarefree dual variable in Heath–Brown's large sieve. A count conditioned on the radical of the powerful row gives the remaining saving. [OpenAI, §§14–15, pinned source](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex)

## 1. The actual coefficient in the cubic large sieve

Write \([a,b]=(a/b)_3^2\) for primary squarefree ideals in the Eisenstein integers, using zero extension. Cubic reciprocity makes this symmetric. The active mark at \(p\) couples to squarefree dual column \(j\) by \(\chi_p(j)^{-2}=[p,j]\). Two active marks \(p,q\) have pair factor \([p,q]\), since their two local exponents in the reflection-pair-phase identity are both zero. A residual row prime has exponent one and its pair factor with a mark is one off the collision locus.

Fix the frozen data in the proof of the reflected energy lemma. The cross-prime-phase identity at the end of §5's reflection calculation gives a product of single-prime scalars and the factors just described. Fixed-conductor terms depend only on the active product modulo the fixed reflection modulus squared. Fix the classes of each of two groups of active marks, retaining only class pairs inducing the prescribed total class. The angular conductor character factors over the groups. All interactions with frozen primes, including fixed Möbius divisors below, factor by mark. The separate mark annular weights factor after the source's Fourier separation on the actual joint support. Primal marked-row collisions vanish by the whole-index marked reflection. This leaves product-form groups with the indicated cubic cross-character. No general bounded function of the entire tuple has been assumed to factor.

Consider the positive cubic sum in the source equation labelled `eq:hybrid-after-quadratic-reduction`. Fix \(D,r,h,t\) there. The sum over \(j=c'm\) is positive after taking absolute squares, with divisor multiplicity \(\ll Z^\epsilon\). The condition on \(ht\) and the character at \(r\) factor by mark for fixed \(r,h,t\). The divisor \(D\mid P\) consists of actual selected primes. Disjoint prime supports specify the slot of each such prime. Remove those fixed primes and keep their induced one-group weights. Their normalization \(q_D^{-1}\) in the squared outer bound is already present.

Partition the original active slots into groups with lengths \(a,b\), \(a+b=z\). Their remaining products, denoted \(A,B\), have norm bounds \(X\ll Z^a\), \(Y\ll Z^b\), including all annular constants. The actual normalized coefficients \(g_A,h_B\) include \(q_A^{-1/2},q_B^{-1/2}\) and satisfy \(\sum_A|g_A|^2,\sum_B|h_B|^2\ll Z^\epsilon\). Disjoint lists give unique reconstruction. The positive norm squared for this part is bounded by
\[
 \sum_{q_j\ll Z^v}\left|\sum_{A,B}g_Ah_B[A,B][A,j][B,j]\right|^2
 \ll Z^\epsilon
  \{Z^v X+Y+(Z^v XY)^{2/3}\}.
 \tag{1}
\]
To prove (1), pair the vector in \(j\) with arbitrary \(d_j\) of squared norm one. Put
\[
 e_w=\sum_{jA=w}d_jg_A[A,j].
\]
The zero convention forces \(w\) to be squarefree. Divisor Cauchy gives \(\sum_w|e_w|^2\ll Z^\epsilon\). The remaining sum is \(\sum_{w,B}e_w h_B[w,B]\). Cauchy and the squarefree cubic large sieve prove (1). The source allows the permitted fixed primes in \(j\), and uses precisely this primary large-sieve orientation, with units already fixed. All fixed-class splits admit finitely many terms.

If \(v\le z\), choose \(a\) within \(\eta\) of \((z-v)/2\) by greedy selection. When \(v>z\), take \(a=0\). The exponent inside (1) is at most \(\max(v,2(v+z)/3)+O(\eta)\). The source proof counts the \(h\)'s by \(O(G/C)\), sums \(q_D^{-1}\) over each dyad at logarithmic cost, and uses the same \(r,t\) and quadratic-sieve bounds. Those factors are independent of the cubic estimate. The resulting change in its reflected energy exponent is
\[
 \min\{v,z,(v+z)/3\}\quad\longrightarrow\quad
 U=\min\{z,(v+z)/3\},
 \tag{2}
\]
with an additive \(O(\eta)\) in the energy. Fixing additional primes in \(D\) only shrinks the two ranges in (1). When the right side of the balance has size at least \(6\eta\), the balanced branch incurs no mesh loss, since \((v+z)/2+\eta\le2(v+z)/3\).

## 2. The powerful row with its active primes fixed in size

Use the specialized low row of §15.1, with \(f=\rho=1\). Write \(O\) for the norm exponent of the powerful part, \(A_0\) for the exponent of its active radical off the fixed set, and bin both with fixed-factor precision. A prime of valuation exactly two outside the fixed set has nonzero local exponent two and is active in every branch. Primes in the fixed set have at most logarithmically many valuation patterns. Let \(a\) be the product of the primes outside the fixed set with row valuation exactly two. Then \(q_a\ll Z^{A_0}\) and the complementary variable part of the powerful row is cubefull. The number of cubefull ideals of norm at most \(X\) is \(\ll_\epsilon X^{1/3+\epsilon}\), by convergence of the cubefull ideal series at every real argument bigger than \(1/3\). Consequently the number of possible powerful rows in these bins is at most
\[
 Z^\epsilon\sum_{q_a\ll Z^{A_0}}(Z^O/q_a^2)^{1/3}
 \ll Z^{(O+A_0)/3+\epsilon}.
\]
Subunit ranges are empty. The unrestricted \(Z^{O/2+\epsilon}\) estimate still applies. Local branch labels cost a divisor factor for each row. Thus the fixed-row count in the source's energy may be replaced by
\[
 C=\min\{O/2,(O+A_0)/3\}.
 \tag{3}
\]

## 3. The completed energy

All formulas below suppress the fixed-dyad offsets, the source's freely chosen retention and Gaussian losses, and the mesh error in (2). Keep the source notation. With \(\Delta=M'-O-H\ge0\), \(z\le\ell'\), and \(y=v+3l_b+e\), one has
\[
 T=2H+2A_0+2z-1-\ell'-N_0-3B_0,\qquad
 y\le T,\qquad 2A_0\le O,\qquad N_0\le A_0.
\]
The hypothesis \(M'+\ell'\le1\) implies \(T\le H\), so \(\max(H,v+l_b)=H\). If \(U=z\), the energy is \(\le C+H\le M'\). Otherwise
\[
 U+l_b+2e/3+(T-y)_+/2
   \ge (T+z)/3 .
\]
Substituting in the reflected energy gives
\[
 E-M'\le
 \frac{1+\ell'-2M'}3
 +C-\frac O3-\frac{2A_0-N_0}{3}-\frac\Delta3-S_0.
\]
Formula (3) and \(N_0\le A_0\) make every term after the first nonpositive. This proves the stated excess. Restoring the dyadic offsets costs \(O(1/\log Z)\), and the retention and Gaussian tolerances can be chosen within any prescribed \(\epsilon\), as in the original proof. The mesh contributes \(O(\eta)\).

For the common geometry \(M=1-\ell\), fixed rescaling length \(d\in[0,\ell]\) gives \(M'=1-\ell-2d\), \(\ell'=\ell-d\). The extra squared row exponent is at most \((\ell+d-1/3)_++O(\eta)\). In the final Cauchy bound its cost is half that exponent, while the rescaled tuple saves \(d\), as in the source's quantitative compensated-low estimate. Hence this particular loss is absorbed for every \(d\) when \(\ell\le1/3\), up to the freely chosen fine mesh. The low-only calculation also requires positive remaining probe scales and the separate additive Gram bound in its stated domain.

Baiying Liu's November comparison has strict slack in the earlier completed-row constraint at its optimizing geometry. Its lower bound for the specified positive comparison also grants extra moment ranges. Thus the strengthened row lemma alone gives no improvement to the reported zero-free boundary \(0.8733458561\ldots\). The positive cubic norm in (1) concerns the completed arithmetic row and does not by itself correlate that row with the separate additive Gram factor. [Liu, §§5.2, 7](https://hexagonmath.org/2611.00421v1)
