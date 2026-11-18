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

## The long-dual face outside this geometry

Take zero rescaling, \(M+\ell=1+\kappa\), \(\kappa>0\), and the formal dyad
\[
 O=A_0=N_0=B_0=S_0=\ell_b=e_\lambda=0,\qquad
 H=M,\quad z=\ell,\quad v=T=2M+\ell-1=M+\kappa .
\]
This is the squarefree residual row, with every physical mark active and a unit cube factor. For \(M+\kappa\ge2\ell\), both the original hybrid saving and (2) give \(U=z\). The kernel saving vanishes, and the squared energy majorant is \(\max(H,v)=M+\kappa\). Thus this strengthening of the positive cubic large sieve still pays \(\kappa/2\) after Cauchy–Schwarz. It reproduces the difference \(L_K-L_0=(M+\ell-1)/2\) between the two direct planes in Liu's Proposition 6.5. This exhibited dyad saturates the **inequality**, and gives no lower bound on the actual arithmetic contribution. Saving a power there requires control of the squarefree quadratic transform with its actual cubic-theta coefficient, or an estimate that keeps its coupling to the additive factor. The [moving calibration calculation](nov18b-calibration-prime.md) gives the corresponding punctured-row upper bound.

### Sharpness for bounded dual coefficients

A single chosen quadratic row attains the long-dual bound to subpower accuracy once the dual coefficient is allowed to be any bounded function. This can be proved while keeping the squarefree support, the cubic mark characters, and the phases between marked primes.

Let \(P\) range over squarefree products of primes in the fixed disjoint mark slots, of norms \(q_P\asymp L\). Absorb the mark–mark phases into \(c_P\), assume \(|c_P|\ll L^{-1/2}\), and suppose \(\sum_P |c_P|^2\ge Z^{-o(1)}\). The lengths are fixed positive powers of a common \(Z\), up to bounded factors. These hypotheses hold, for example, for actual fixed nonzero annular weights at every slot on fixed allowed prime ray classes, with arbitrary modulus-one mark phases: on interior subannuli the weights are bounded away from zero, and the prime ideal theorem in the fixed classes supplies the required mass. Individual mark supports and any fixed admissible ray-sector choices may be included in those lists. Put
\[
 A(n)=\sum_P c_P [P,n].
\]
Suppose \(N\ge L^4\), and let \(k_0\) be a good primary prime row of norm \(q_{k_0}\asymp K\), with \(K\ge L^{1+\sigma}\) for fixed \(\sigma>0\). Take it outside the mark supports. The prime ideal theorem supplies such rows in any fixed admissible ray class at the large lengths in question. Then
\[
 \sum_{\substack{n\ \mathrm{squarefree},\ q_n\asymp N\\(n,k_0)=1}}
 |A(n)|\gg_\epsilon N Z^{-\epsilon} .                         \tag{4}
\]
Here and below the \(n\) are primary ideals outside the old fixed bad-prime set. One may restrict the sum to a fixed admissible ray class for \(n\).

For the second moment choose a nonnegative smooth test \(V(q_n/N)\) supported in the indicated annulus and positive on a subinterval. The diagonal count of squarefree \(n\) coprime to \(P\) is
\[
 C_V N\prod_{p\mid P}(1+q_p^{-1})^{-1}+O_\epsilon(N^{1/2+\epsilon}L^\epsilon)
\]
with the fixed bad-prime or ray factors included in \(C_V>0\). This follows from the squarefree Dirichlet series for the ray characters, shifted to real part \(1/2+\epsilon\) after extracting the principal pole. At a nondiagonal pair \(P_1\ne P_2\), cubic reciprocity expresses its phase as a character of \(n\) ramified at a prime of the symmetric difference. Every old ray twist stays nonprincipal. The conductor norm is \(O_{\rm fixed}(L^2)\); the common prime divisors supply only zero masks. For a character \(\psi\) with these original masks its squarefree series is \(L(s,\psi)/L(2s,\psi^2)\). On the same line the inverse at \(2s\) is absolutely bounded, the extra deleted factors cost \(L^\epsilon\), and the classical conductor convexity bound for the degree-two Hecke numerator is \(O_\epsilon(L^{1/2+\epsilon}(1+|t|)^C)\). Mellin decay therefore bounds each smoothed off-diagonal sum by \(O_\epsilon(N^{1/2+\epsilon} L^{1/2+\epsilon})\). Since \((\sum_P|c_P|)^2\ll L^{1+\epsilon}\), the combined error is \(O_\epsilon(N^{1/2+\epsilon}L^{3/2+\epsilon})\). It is a power saving here. Excluding multiples of \(k_0\) costs at most \(O((N/K+1)L^{1+\epsilon})\), also a power saving. The weighted second moment on the required support is consequently \(\gg_\epsilon NZ^{-\epsilon}\).

For the fourth moment expand \(A(n)^2\) and take \(d=(P_1,P_2)\), \(P_1P_2=d^2 r\). The residual \(r\) is squarefree. For each fixed \(d\), its coefficient is \(O_\epsilon(L^{-1+\epsilon})\) by the divisor bound, and \(q_r\ll L^2/q_d^2\). Its coefficient vector has \(\ell^2\) norm \(O_\epsilon(L^\epsilon/q_d)\). The factor \([d,n]^2\) has modulus at most one, including its zeros, so it can be discarded after squaring the norm of this individual \(d\)-sum. Heath–Brown's squarefree cubic large sieve bounds that norm by
\[
 \ll_\epsilon \frac{Z^\epsilon}{q_d}
 \{N+L^2+(NL^2)^{2/3}\}^{1/2}\ll_\epsilon
 \frac{N^{1/2}Z^\epsilon}{q_d}.
\]
Minkowski and \(\sum_{q_d\ll L}q_d^{-1}\ll 1+\log L\) give \(\sum_{n\ {\rm sf},\,q_n\ll N}|A(n)|^4\ll_\epsilon NZ^\epsilon\). Hölder between the first, second and fourth moments proves (4), with a reduction of the preliminary losses. [Squarefree cubic large sieve and its normalization in the pinned source, §14](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex)

In the separated quadratic–cubic norm set \(b=1\). Choose a single bounded coefficient \(\beta(n,1)\) on that squarefree annulus to be the conjugate phase of \(\chi_{k_0}(n)^3 A(n)\), set it to zero when the argument vanishes, and then use this *same* coefficient at every running row. It depends on the fixed list and \(k_0\), and is independent of both the running row and the running mark tuple. Since \(k_0\) is disjoint from the marks, its one summand in the squared norm alone is \(\gg_\epsilon N^2 Z^{-\epsilon}\). Restoring the dual normalization \(N^{-1}\) in the squared reflected energy gives \(\gg_\epsilon NZ^{-\epsilon}\). Near the limiting geometry above, \(v>4\ell\), so the length hypothesis used in (4) applies. This proves that any uniform improvement of the exhibited long-dual face must use a property lost when the original cubic-theta coefficient is replaced by a freely chosen bounded coefficient, or must retain another signed coupling before this norm is taken.

The same lower bound holds with an arbitrary prescribed cube \(\beta(n,1)^3=b_n\), \(|b_n|=1\), on every squarefree index in the annulus. Choose among the three cube roots the one with argument nearest the aligned phase above. The real part of its contribution at \(k_0\) is at least \(|A(n)|/2\); the zero character terms contribute zero whatever root is chosen. In particular, the one-point identity for normalized cubic Gauss sums cannot by itself remove the adverse coefficient. For squarefree primary \(n\) the local identities \(\gamma_2(p)^3=-\alpha(p)\) and the Chinese remainder factors of order dividing three give \(\gamma_2(n)^3=\mu(n)\alpha(n)\). The freely chosen roots in this last argument need not obey the Gauss-sum identities that relate **different** indices \(n\).
