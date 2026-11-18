# What prime-power rigidity decides for a finite Euler modification

**Status.** Proposed exact results. Both use ordinary Dirichlet series and the degree-one zeta gamma factor. The first classifies every finite polynomial change of Euler factors compatible with a scalar functional equation. The second constructs a pair whose comparison plants a prescribed off-line zero while preserving finite analytic data and arbitrarily close positive arithmetic coefficients. Both arguments are symbolic.

## A local classification from the global functional equation

Let
\[
 F(s)=\zeta(s)D(s),\qquad D(s)=\prod_{p\in S}P_p(p^{-s}),\qquad
 P_p(X)=1+\cdots+c_{p,e_p}X^{e_p}
\]
for a finite set of primes, with \(e_p\ge1\) and nonzero leading coefficients. Assume that \(H_F(s)=(Q/\pi)^{s/2}\Gamma(s/2)F(s)\) satisfies \(H_F(s)=\omega\overline{H_F(1-\bar s)}\), where \(Q>0\) and \(|\omega|=1\). For each modified prime, define \(\Lambda_F(p^k)\) by the local expansion of \(-F'/F\) sufficiently far to the right. Write
\[
 b_p=\limsup_{k\to\infty}\frac{\log(1+|\Lambda_F(p^k)|)}{k\log p}.
\]
Then \(Q=\prod_{p\in S}p^{e_p}\), and \(b_p\) equals the greatest real part of a zero introduced by \(P_p(p^{-s})\). Each \(b_p\ge1/2\). If every \(b_p\le1/2\), all introduced zeros are on the critical line. A strict bound below \(1/2\) at every altered prime rules out every nonconstant modification.

To see this, cancel the meromorphic completed zeta factor and write \(D(s)=\sum d_n n^{-s}\). Its functional equation becomes
\[
 \sum_n d_n n^{-s}=\omega\sqrt Q\sum_n\frac{\overline{d_n}}n(Q/n)^{-s}.
\]
Distinct positive exponential frequencies are linearly independent. The smallest and largest elements of the support on the left are \(1\) and \(M=\prod p^{e_p}\). Matching extreme frequencies gives \(Q=M\). Coefficient comparison gives \(d_n=\omega n\overline{d_{Q/n}}/\sqrt Q\) on all divisors of \(Q\), taking missing coefficients to be zero. Divide by the equation for \(d_1\) and use multiplicativity to obtain
\[
 c_{p,j}=p^j\,\overline{c_{p,e_p-j}}/\overline{c_{p,e_p}},\qquad
 |c_{p,e_p}|=p^{e_p/2}.
\]
Thus, writing \(P_p(X)=\prod_j(1-\alpha_jX)\), the multiset of \(\alpha_j\) is invariant under \(\alpha\mapsto p/\bar\alpha\). Its largest modulus \(A\) is at least \(\sqrt p\). Direct expansion gives
\[
 \Lambda_F(p^k)=(\log p)\Big(1-\sum_j\alpha_j^k\Big).
\]
The generating series of the parenthesized quantities for \(k\ge1\) has radius \(A^{-1}\). At a point \(1/\alpha_j\) on this circle, each appearance of the same root contributes the identical nonzero residue, and the geometric series for the constant sequence is regular there. Cauchy–Hadamard gives \(b_p=\log A/\log p\). A root with local parameter \(\alpha_j\) contributes a vertical progression at real part \(\log|\alpha_j|/\log p\). The symmetry proves the assertions.

In particular the actual zeta values \(\Lambda(p^k)=\log p\) have local exponent zero at every prime. The classification concerns a *finite* modification of a source whose zeros are already present. It supplies no bound for the zeros of that source.

For an elementary integer-coefficient example, take an even integer \(d\ge4\) and integers \(0<v<d/2<u<d\) with \(u+v=d\). The polynomial factor
\[
                 (1+p^{u-ds})(1+p^{v-ds})
\]
adds zeros at real parts \(u/d\) and \(v/d\). Its comparison \((1+p^{d/2-ds})^2\) adds only central zeros. Both yield the same conductor \(p^{2d}\) and positive bounded integer Dirichlet coefficients after multiplication by zeta. Every prime value and every prime power through exponent \(d-1\) agree. The more general construction below also enforces analytic matching at prescribed points.

## Preserving finite analytic information and all prime coefficients

Fix \(s_*=\beta+i\gamma\) with \(1/2<\beta<1\) and \(\gamma\ne0\). Prescribe values and derivative orders to be *matched between the two series* at any finite list of points disjoint from \(s_*,\bar s_*,1-s_*,1-\bar s_*\). Fix \(0<\epsilon<1\) and an integer \(J\ge1\).

There exist two series \(F_i=\zeta D_i\) of the above type, with the same single modified prime \(p\), conductor \(Q\), root number \(+1\), simple pole at one and the same residue there. Their Dirichlet coefficients \(a_i(n)\) are positive, bounded for each series, and multiplicative. They agree with \(1\) on every \(n\) indivisible by \(p^d\) for some \(d>J\). In particular they agree with zeta at every prime, at each prime power of exponent at most \(J\), and on a set whose complement can be prescribed to have arbitrarily small upper density. At every \(n\),
\[
             (1-\epsilon)a_0(n)<a_1(n)<(1+\epsilon)a_0(n).
\]
The meromorphic functions, and their completions, match through all prescribed finite orders, using Laurent coefficients at poles. Every zero of \(D_0\) has real part \(1/2\). The only zeros of \(D_1\) away from that line are the symmetry quartet of \(s_*\) and its translates by \(2\pi i\mathbb Z/(d\log p)\). Zeta contributes its own zeros to both series. Here conductor denotes the scale in the displayed functional equation. It depends on the requested data.

### Choosing a reciprocal polynomial

Put \(y=p^{d(1/2-s)}\), \(w=y+y^{-1}\), and write \(w_*=w(s_*)\). Choose \(p,d\) so that \(\Re w_*<0\), \(\Im w_*\ne0\), and none of the prescribed nodes maps to \(w_*\) or \(\bar w_*\). Here are the choices explicitly. For every nonzero frequency \(v\) in the finite list consisting of \(\gamma\) and the nonzero differences \(\Im s_j\pm\gamma\), at most one prime makes \(v\log p/(2\pi)\) rational. Two such primes would have rational log ratio, contrary to unique factorization. Choose a prime outside this finite set. A collision in \(w\) would require equal or reciprocal \(y\)'s, possibly after conjugation. Their moduli either differ or their arguments would give one of the forbidden rational relations, since the four exact symmetry partners were excluded. Irrational rotation permits arbitrarily large \(d>J\) with \(d\gamma\log p\) in an open arc where the cosine is negative and the sine nonzero. The same \(d\) can enforce any requested bound on \(p^{-d}\).

For \(-2<u<0\), the quadratic \(1-uy+y^2\) has positive coefficients and both roots on \(|y|=1\). The product
\[
 (1-w_*y+y^2)(1-\bar w_*y+y^2)
 =1-2\Re(w_*)y+(2+|w_*|^2)y^2-2\Re(w_*)y^3+y^4
\]
also has positive coefficients. Its roots are exactly \(y(s_*),y(s_*)^{-1}\) and their conjugates. We will compare it to two central quadratics while varying some additional central quadratics to match all the jets.

### Matching the jets with central roots

Collect the distinct nodes \(w_j=w(s_j)\) and their conjugates, adding \(w(0)=w(1)\) to match the pole residue. Require sufficiently many jet orders at each node, including one additional order at a pole of the common completed zeta. Jets in \(w\) then suffice by analytic composition. Choose a real \(u_0\in(-2,0)\) away from the nodes and put
\[
 T(w)=\frac{(w-w_*)(w-\bar w_*)}{(w-u_0)^2}.
\]
This is strictly positive on \([2,\infty)\) and at every real node. Its logarithm \(h\) can be chosen real on that interval and at real nodes, with conjugate analytic germs at nonreal nodes. Its value at infinity is zero.

For every \(\eta>0\) there is a real rational function
\[
 A(w)=\sum_i\frac{a_i}{w-u_i},\qquad -2<u_i<0,
\]
with distinct poles away from all nodes, whose jets agree with those of \(h\) at the nodes and such that \(\sup_{w\ge2}|h(w)-A(w)|<\eta\). For a proof take \(t=1/(w-u_0)\). A real Hermite interpolant matches the target jets at all the finite transformed nodes and its value zero at \(t=0\). Subtract the interpolant and divide by the real nodal polynomial with matching multiplicities, including the factor at zero. The quotient extends continuously on the compact interval corresponding to \([2,\infty]\). Weierstrass approximation there, followed by multiplication and adding back the interpolant, gives the desired uniform approximation by a polynomial in \(t\) with zero constant term and all jets exact. Finite differences in the pole position replace its terms \((w-u_0)^{-j}\) by linear combinations of simple real poles arbitrarily close to \(u_0\), uniformly on the interval and on all prescribed jets. To correct the resulting small jet errors, fix as many distinct new poles as there are real jet coordinates, counting both coordinates of each complex derivative. The jet map of their simple fractions is an isomorphism. A kernel vector would have a numerator of degree less than the total prescribed zero multiplicity, hence would vanish identically. Fixed-dimensional linear inversion corrects the errors at arbitrarily small uniform cost.

Take these extra poles as adjustable parameters in the following expression, including them even if their initial coefficients vanish. For integers \(m\) sufficiently large, real \(a_{i,m}=a_i+O(1/m)\) can be chosen so that
\[
 R_m(w)=T(w)\prod_i\left(\frac{w-u_i-a_{i,m}/m}{w-u_i}\right)^m
\]
has all jets of \(R_m-1\) zero through the requested orders. Indeed on the chosen germs the added logarithmic terms are \(x^{-1}\log(1-xa_{i,m}/(w-u_i))\) with \(x=1/m\). Their continuation at \(x=0\) equals \(-a_i/(w-u_i)\). The jet equations for the logarithm hold at zero, and their Jacobian in the adjustable coefficients is the invertible jet map above up to sign. The real implicit function theorem supplies the stated choices. Uniform convergence of these same logarithmic terms on \([2,\infty]\) gives \(\sup_{w\ge2}|\log R_m(w)|<2\eta\) for all sufficiently large \(m\). Every shifted parameter stays in \((-2,0)\).

Take
\[
 \begin{split}
 P_0(y)&=(1-u_0y+y^2)^2\prod_i (1-u_i y+y^2)^m,\\
 P_1(y)&=(1-w_*y+y^2)(1-\bar w_*y+y^2)
              \prod_i(1-(u_i+a_{i,m}/m)y+y^2)^m .
 \end{split}
\]
Their ratio at \(y\ne0\) is exactly \(R_m(y+y^{-1})\) wherever the denominator is nonzero. In this expression all denominators at the interpolation nodes were chosen nonzero. With \(\eta\) small enough the ratio lies strictly between \(1-\epsilon\) and \(1+\epsilon\) for all real \(y\ge0\), with value one at both endpoints of the compactified half-line.

### Passing the bound to every arithmetic coefficient

Both \((1+\epsilon)P_0-P_1\) and \(P_1-(1-\epsilon)P_0\) have strictly positive homogenizations on the compact unit simplex. Multiplication by a common \((1+y)^K\) therefore makes both polynomials coefficientwise strictly positive. For completeness, for a polynomial \(U(y)=\sum_{j=0}^D u_j y^j\) the coefficient at \(k\) after this multiplication, divided by \(\binom{K+D}{k}\), is
\[
 \sum_{j=0}^D u_j\frac{(k)_j(K+D-k)_{D-j}}{(K+D)_D}.
\]
Here \((n)_r\) is the falling factorial. Uniformly in \(0\le k\le K+D\), this equals \(\sum_j u_j t^j(1-t)^{D-j}+O_U(1/K)\) with \(t=k/(K+D)\). Strict positivity on the compact interval proves the assertion. This common multiplier adds only critical-line zeros.

Use the resulting padded polynomials in \(D_i(s)=P_i(p^{d(1/2-s)})\), now writing \(D\) for their common polynomial degree. They are reciprocal, with constant term and leading coefficient one, so \(Q=p^{dD}\) yields the stated scalar functional equation. Substituting \(y=p^{d/2}(p^{-s})^d\) preserves coefficient inequalities on the occupied indices. Euler multiplication by zeta takes partial sums of these positive coefficients at the prime \(p\), and at every other prime it keeps the original factor. Thus the coefficient ratio bounds hold at every integer, including all the coefficients equal to one. Each series has bounded coefficients because it has a single finite polynomial alteration. The jet comparison gives equal pole residues. The displayed factors account for every added zero.

## Consequences for an attempted proof of RH

Finite interpolation data, matching prime values, degree-one symmetry at a common unspecified conductor, a positive Euler product on the real absolute-convergence line, and relative closeness of every positive Dirichlet coefficient can coexist with the exact extra zero divisor above. The local classification explains the price: the altered Euler logarithm at one prime has a prime-power growth exponent \(\beta>1/2\). The physical zeta Euler law excludes such a tower at every prime. The comparison also uses a conductor greater than one. It therefore identifies data that a faithful rigidity proof must exploit and leaves the infinite-prime argument at conductor one open.

## The sharp convergence boundary for a sequence of central Euler factors

There is also an exact answer to the passage from finitely many primes to infinitely many in the preceding comparison class. Fix an integer \(m\ge2\). Let \(D_j(s)\) be finite products of normalized local polynomials \(P_{j,p}(p^{-s})\) of uniformly bounded degree, with every zero on \(\Re s=1/2\). Assume every nonconstant term of each polynomial has degree at least \(m\), and all modified primes are at least \(Y_j\) with \(Y_j\to\infty\). Then
\[
             D_j(s)\longrightarrow 1
 \quad\text{locally uniformly for }\Re s>\tfrac12+\tfrac1m .
\]
The boundary is sharp, even among positive-coefficient series with exact degree-one functional equations after multiplication by zeta. At any prescribed \(s_*=\beta+i\gamma\) with \(1/2<\beta\le1/2+1/m\) there are two arrays \(D_{j,0},D_{j,1}\) with the same conductor at each \(j\). Both tend to one locally uniformly on \(\Re s>\beta\), yet
\[
                  D_{j,0}(s_*)\longrightarrow1,\qquad
                  |D_{j,1}(s_*)|\longrightarrow\infty.
\]
Every added zero of both arrays is on the critical line. After multiplication by zeta, both have positive multiplicative coefficients, the exact prime coefficients of zeta at *every* prime, and eventual equality with the zeta coefficient at *each* integer. Their local logarithmic coefficients satisfy \(|\Lambda_F(p^k)|\le(2m+1)p^{k/2}\log p\) for every \(j,p,k\).

For the upper bound, each root parameter \(\alpha\) of a local polynomial has modulus \(\sqrt p\). Its logarithmic coefficient at degree \(k\) has modulus at most \(C p^{k/2}/k\), where \(C\) bounds the degree. All degrees below \(m\) vanish. Thus, with \(u=\sigma-1/2>1/m\), an absolute majorant for the full logarithm is
\[
 C\sum_{p\ge Y_j}\sum_{k\ge m}p^{-ku}/k\ll_{m,u,C}
 \sum_{p\ge Y_j}p^{-mu}\longrightarrow0.
\]
This holds uniformly on closed half-planes at positive distance from the specified boundary.

For sharpness put \(b=\beta-1/2\) and take \(Y_j=\exp(j^2)\). When \(\gamma\ne0\), the primes with \(\cos(m\gamma\log p)>1/2\) have divergent reciprocal sum. Indeed one may take disjoint intervals \([A,cA]\) of a fixed ratio \(c>1\) in this phase arc, with \(\log A\) growing along an arithmetic progression. The prime number theorem supplies \(\gg1/\log A\) reciprocal mass per interval. For \(\gamma=0\) all primes qualify. Since \(mb\le1\), choose a finite set \(S_j\) of these primes above \(Y_j\) with
\[
                         j\le\sum_{p\in S_j}p^{-mb}\le j+1.
\]
At \(p\in S_j\) put \(y=p^{1/2-s}\) and use respectively
\[
                        1+y^{2m},\qquad 1+y^m+y^{2m}.
\]
All roots lie on the unit circle, both polynomials are reciprocal of degree \(2m\), and every coefficient is nonnegative. Their common conductor is \(\prod_{p\in S_j}p^{2m}\). At \(s_*\) the error sum \(\sum_{p\in S_j}|y|^{2m}\le (j+1)Y_j^{-mb}\) tends to zero, so the first product tends to one. The real logarithm of the modulus of the second is at least \(j/2-O((j+1)Y_j^{-mb})\). For \(\sigma>\beta\), both logarithms have absolute majorant \(O((j+1)Y_j^{-m(\sigma-\beta)})\) once \(j\) is sufficiently large. This proves all convergence assertions. The local coefficient bound follows by summing at most \(2m\) root powers and adding the single original zeta term.

In particular, at a point of the open critical strip where \(\zeta(s_*)\ne0\), a single common normalization cannot make both completed comparisons converge locally to the same nonzero zeta value there: their ratio already tends to infinity. The example explains the need for control uniform in the growing prime set even after each finite polynomial has all its zeros on the line.

The complementary positive statement for the actual prime powers is elementary. Suppose two Euler logarithms have the same linear coefficient at each prime and, for every \(\delta>0\), their higher coefficients at \(p^k\) have modulus \(\ll_\delta p^{k\delta}\) with the constant uniform in \(p,k\). Their difference is an absolutely, locally uniformly convergent logarithm on \(\Re s>1/2\) because its double sum begins at \(k=2\). Consequently, wherever the two original series continue meromorphically to that half-plane, their divisors there agree. The zeta coefficients \(1/k\) satisfy this uniform bound. In an argument using the actual Euler logarithm, all potential off-line singularities on the right must therefore be accounted for by the first powers of the primes.

## What an exhaustive rearrangement of the genuine prime factors can interpolate

Fix \(1/2<\beta\le1\) and a finite or countable sequence of distinct positive ordinates \(\gamma_l\). For any prescribed nonzero complex values \(z_l\), there are nested finite sets \(E_j\) of genuine primes, exhausting all primes, such that
\[
 Z_{E_j}(s)=\prod_{p\in E_j}(1-p^{-s})^{-1},\qquad
 Z_{E_j}(\beta+i\gamma_l)\longrightarrow z_l\quad\text{for each }l.
\]
At the same time \(Z_{E_j}\to\zeta\) locally uniformly on \(\Re s>1\). The result concerns the exhausted sets at the displayed endpoints. It uses an order selected for the interpolation. No assertion about the products at the usual cutoffs \(p\le X\) follows. Each local factor and its logarithmic coefficients here are exactly the physical ones.

For a fixed finite group of \(h\) ordinates write
\[
 v(t)=(e^{-i\gamma_1t},\ldots,e^{-i\gamma_ht})\in\mathbb C^h
\]
and view the latter as a real vector space. The convex hull of finitely many values \(v(t_a)\) contains a ball around zero. Indeed each nonzero real linear functional on \(v(t)\) is a trigonometric polynomial with time mean zero and strictly positive mean square, by the distinct positive frequencies. It takes both signs, since a nonnegative bounded function satisfies \(f^2\le\|f\|_\infty f\). The separation theorem shows that zero is interior to the closed convex hull, and a finite choice of values retains a smaller ball. Thus every \(w\) has a representation \(w=\sum_a c_av(t_a)\), \(c_a\ge0\), \(\sum_a c_a\le C_h\|w\|\).

For any fixed neighborhood of any of these values, the primes with \(v(\log p)\) in that neighborhood have divergent reciprocal sum. The closure of the one-parameter group \(v(\mathbb R)\) is a compact group. Finite covering by translates of a smaller neighborhood makes its return times relatively dense. Uniform continuity gives fixed positive lengths of log intervals inside the original neighborhood, spaced with bounded gaps after taking a disjoint sequence. The prime number theorem gives reciprocal prime mass \(\gg1/t\) on each such interval with left endpoint \(t\), as in the preceding proof. Their sum diverges. Since \(\beta\le1\), the corresponding \(p^{-\beta}\) sum also diverges.

It follows that for any \(w\in\mathbb C^h\), tolerance \(\tau>0\), and sufficiently large lower cutoff \(Y\), one can select a finite set of primes \(S\) above \(Y\) with
\[
 \left\|\sum_{p\in S}p^{-\beta}v(\log p)-w\right\|<\tau .
\]
Choose the neighborhoods sufficiently small relative to \(\tau/(1+\sum c_a)\). In each choose new primes until their scalar mass first reaches \(c_a\), omitting a group of zero mass. There is overshoot at most \(Y^{-\beta}\) per group, and discarding finitely many previously used primes preserves divergence. In particular \(\sum_{p\in S}p^{-\beta}\le C_h\|w\|+O_h(Y^{-\beta})\).

At stage \(j\) first include all primes through an integer \(N_j\) larger than \(j\) and every prime used at preceding stages. Take the first \(j\) ordinates, or the full list if it is shorter. At each point use for the finite product the unambiguous Euler logarithm \(\sum_{p\le N_j}\sum_{k\ge1}p^{-ks}/k\). Form \(w\) by subtracting these values from fixed choices of \(\log z_l\). Use the construction with tolerance \(1/j\) and \(Y>N_j\) as large as necessary. The omitted higher powers in the added logarithm have absolute total at most
\[
        \sum_{p>Y}\frac{p^{-2\beta}}{1-p^{-\beta}}=o(1),
\]
independently of the selected primes and ordinates. Take \(Y\) so this is at most \(1/j\). The union of the initial segment and the selected set is \(E_j\). The logarithms converge to the prescribed logarithm at every fixed node by diagonalization. Absolute convergence of the ordinary Euler product on the right gives the claimed locally uniform convergence there. No analytic normalization or assumption on zeta zeros was used. Thus cofinal agreement with every physical Euler factor allows even countably many freely chosen endpoint limits on this vertical line. A continuation argument must supply stronger convergence information for its particular exhaustion.
