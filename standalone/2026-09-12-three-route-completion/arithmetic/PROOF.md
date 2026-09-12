# Sharp degree exponents and a finite native-energy adapter

**Status: proposed component proofs; RH and the required arithmetic upper
bound remain open.** This packet attempts the arithmetic completion path. It
does not publish an RH proof, an evaluation of the rightmost zero abscissa,
or independent acceptance of its predecessor packets.

The main new result removes the factor-ten loss in DG26's all-degree zero
witness: the exact logarithmic growth exponent of its positive trace and
operator norm is the same as XCC26's native energy exponent. A second result
transfers a completely finite ordinary-Mobius energy bound to that trace,
with an explicit polynomial scale cost and a paid origin remainder. These
are usable source-preserving bridges, not an estimate of the remaining
native covariance.

## 0. Frozen sources and conventions

Main is `f99d9e3908dde4865377c75d9ca051c1f545bf4f`. The two direct research
predecessors are:

* DG26, PR866 at `14b20cc85aec1dc1909990d2d8a517740f2dd536`,
  `standalone/2026-09-12-astra-polynomial-degree-growth/PROOF.md`.
* XCC26, PR848 at `99101457b32b6f10f4eda88ca998048404b860ea`,
  `standalone/2026-09-12-astra-crossing-cofinal/PROOF.md`.

Their proofs were read, including XCC26's generalized Littlewood argument.
No parent checker is executed or promoted. Classical inputs are the Euler
product and continuation of zeta, its functional equation and classical
zero-free line one, existence of nontrivial zeros, ordinary Legendre
orthogonality, and elementary Fourier approximation. The upper exponent
uses the classical generalized Littlewood implication, whose application
is stated in Section 4. No novelty claim is made for these classical tools.

Let

\[
 m_o(x)=\sum_{n\le x,\ n\text{ odd}}\frac{\mu(n)}n,
 \quad m_a(x)=\sum_{n\le x}\frac{\mu(n)}n,
 \quad F_Y=\sum_{k=1}^{Y}m_a(k)^2.
\]

Both summatory functions are zero for \(x<1\). All norms without a displayed
interval are ordinary Lebesgue \(L^2\) norms on the intervals specified below;
all polynomials and pairings may be complex. Put

\[
 Z(s)=(1-2^{-s})\zeta(s),\qquad a(s)=(s-1)Z(s).
\]

The entire function \(a\) has \(a(1)=1/2\). For an odd polynomial \(p\), define

\[
 Q_p(t)=\sum_{n\text{ odd}}p(t/n)/n,\quad
 Ap(t)=tQ_p'(t)\quad(0<t<1),
\]
\[
 Ep(t)=Q_p(1)-\sum_{n\ge3,\ n\text{ odd}}p(t/n)/n
 \quad(1<t<3).
\]

Let \(\Pi_N=\operatorname{span}\{t,t^3,\ldots,t^{2N-1}\}\), and set

\[
 (Kf)(t)=\int_0^1m_o(t/u)f(u)\,\frac{du}{u},\quad
 \phi_j(u)=\sqrt{4j+3}\,P_{2j+1}(u),
\]
\[
 \Lambda_N=\sup_{0\ne p\in\Pi_N}\frac{\|Ep\|_{(1,3)}^2}
 {\|Ap\|_{(0,1)}^2},\qquad
 S_N=\sum_{j<N}\|K\phi_j\|_{(1,3)}^2.
\]

The \(\phi_j\) are orthonormal on \((0,1)\). Direct odd Mobius inversion gives
\(Ep=K(Ap)\); the constant term \(Q_p(1)\) is retained. In fact, after writing
\(q=Q_p\) and \(f=tq'\), its coefficient inside the integral is \(m_o(t/u)\)
for \(u<t/3\), and is \(1=m_o(t/u)\) for \(u>t/3\). Absolute interchange
holds because the input vanishes linearly at zero. Since \(A\) multiplies
the monomial \(t^r\) by \(rZ(r+1)>0\), it is a bijection on \(\Pi_N\).
Consequently

\[
 \Lambda_N=\|K|_{\Pi_N}\|_{\rm op}^2\le S_N.
 \tag{0.1}
\]

This is a finite-rank statement. No bounded extension of \(K\) to all of
unweighted \(L^2(0,1)\) is assumed.

## 1. High-order odd-polynomial approximation with explicit degree

**Lemma 1.** Let \(g\) be an odd \(C^{r+1}\) function on \([-1,1]\), with
integer \(r\ge2\). For every \(N\ge2\) there is an odd polynomial
\(p_N\in\Pi_N\) such that

\[
 \|p_N'-g'\|_\infty
 \le C_r N^{1-r}\max_{1\le j\le r+1}\|g^{(j)}\|_\infty.
 \tag{1.1}
\]

The constant depends on \(r\), not on \(g\) or \(N\). This is an existence
construction by Fourier integrals, not an optimization over unspecified
approximants.

**Proof.** The function \(h(\theta)=g'(\cos\theta)\) is \(C^r\), even,
\(2\pi\)-periodic, and also \(\pi\)-periodic because \(g'\) is even. Its
Fourier coefficients vanish at odd frequencies. Repeated integration by
parts has no boundary term and gives

\[
 |\widehat h(2j)|\le (2|j|)^{-r}\|h^{(r)}\|_\infty,
 \qquad j\ne0.
\]

Repeated ordinary chain and product rules give
\(\|h^{(r)}\|_\infty\le C'_r\max_{1\le j\le r+1}\|g^{(j)}\|_\infty\).
Only finitely many products of bounded sine/cosine derivatives occur.
The Fourier series is absolutely uniformly convergent. Truncating it at
frequencies \(|j|<N\) leaves an error bounded by the right side of (1.1),
since \(\sum_{j\ge N}j^{-r}=O_r(N^{1-r})\). Evenness gives

\[
 v_N(t)=\widehat h(0)+2\sum_{j=1}^{N-1}\widehat h(2j)T_{2j}(t).
\]

This is an even polynomial of degree at most \(2N-2\), and its error on
\([-1,1]\) is precisely controlled by the Fourier tail. Set
\(p_N(t)=\int_0^t v_N(u)du\). It is odd and has degree at most \(2N-1\),
which proves the lemma. Complex coefficients cause no change; evenness
means \(\widehat h(-2j)=\widehat h(2j)\), not a conjugacy assumption. QED.

For a \(C^1\) error \(e\) on \([0,1]\) with \(e(0)=0\) and
\(\|e'\|_\infty\le D\), the literal dilation sums give

\[
 \|Ae\|_{(0,1)}\le\frac{5D}{4\sqrt3},\qquad
 \|Ee\|_{(1,3)}\le2\sqrt2D.
 \tag{1.2}
\]

Indeed \(|e(u)|\le Du\), \(Z(2)=\pi^2/8<5/4\), and
\(|Ee(t)|\le D[Z(2)+3(Z(2)-1)]<2D\). These are supremum-derivative
approximation estimates. They are not the false unweighted-to-weighted
\(L^2\) derivative comparison refuted in PR861.

## 2. A smooth cutoff at a hypothetical zero

Choose once and for all a smooth function \(\chi\) equal to zero on
\(( -\infty,1]\), one on \([2,\infty)\), and taking values in \([0,1]\).
One explicit choice is

\[
 \chi(v)=\frac{\eta(v-1)}{\eta(v-1)+\eta(2-v)},\qquad
 \eta(t)=\begin{cases}e^{-1/t},&t>0,\\0,&t\le0.\end{cases}
\]

Its denominator is always positive. Every derivative is bounded; it is
constant outside its transition interval. Fix \(s\) with
\(1/2<\beta=\Re s<1\), and let \(0<\epsilon<1/2\). On the positive axis put

\[
 g_{s,\epsilon}(t)=t^{s-1}\chi(t/\epsilon),
\]

and extend it oddly across zero. It is smooth on \([-1,1]\), including an
open interval around zero on which it vanishes. For every integer \(j\ge0\),

\[
 \|g_{s,\epsilon}^{(j)}\|_\infty
 \le C_{s,j,\chi}\epsilon^{\beta-1-j}.
 \tag{2.1}
\]

To see this, differentiate the product. A cutoff derivative is supported on
\([\epsilon,2\epsilon]\) and supplies its corresponding inverse power of
\(\epsilon\); outside that interval the derivatives are those of the power
function and attain their largest magnitude at the lower endpoint. The
flat matching of \(\chi\) handles all transition endpoints.

For completeness, the full cutoff calculation used here is rederived.
With
\(d_o(x)=\lfloor(x+1)/2\rfloor-x/2\), so \(|d_o|\le1/2\), Euler summation
gives

\[
 Q_g(t)=c_s\epsilon^{s-1}+Z(s)t^{s-1}
              +t^{s-1}R_s(t/\epsilon),
 \tag{2.2}
\]
\[
 c_s=\frac12\int_0^\infty y^{-s}\chi(1/y)dy,
\]
\[
 R_s(v)=\int_0^\infty d_o(x)x^{-s-1}
 \{s[\chi(v/x)-1]+(v/x)\chi'(v/x)\}\,dx.
 \tag{2.3}
\]

Here \(Z(s)=s\int_0^\infty d_o(x)x^{-s-1}dx\) for \(0<\Re s<1\), as
follows by splitting the usual Euler formula at one. At zero
\(d_o(x)=-x/2\); at infinity it is bounded. Thus both endpoint terms in
the integration by parts vanish in this strip. The integrand in (2.3)
vanishes for \(x<v/2\), and differentiation of its bracket gives
\((s+1)(v/x)\chi'(v/x)+(v/x)^2\chi''(v/x)\), supported in \([v/2,v]\).
Consequently, with constants depending only on \(s,\chi\),

\[
 |R_s(v)|+|vR_s'(v)|\le C_{s,\chi}v^{-\beta}.
 \tag{2.4}
\]

This controls the complete infinite Euler remainder. The potentially large
first term in (2.2) is constant in \(t\) and cancels in both \(A\) and \(E\).

Now suppose \(\rho=\beta+i\gamma\) is a hypothetical nontrivial zero with
\(\beta>1/2\), and put \(\delta=\beta-1/2\). Since \(Z(\rho)=0\), (2.2)--(2.4)
imply

\[
 \|Ag_{\rho,\epsilon}\|_{(0,1)}\le C_\rho\epsilon^\delta,
 \qquad
 \|Eg_{\rho,\epsilon}-t^{\rho-1}\|_{(1,3)}
       \le C'_\rho\epsilon^\beta.
 \tag{2.5}
\]

For the first estimate the derivative remainder is bounded by
\(C\epsilon^\beta/t\) for \(t\ge\epsilon\) and is zero below \(\epsilon\);
its squared integral is \(O(\epsilon^{2\beta-1})\). For the second, use
\(E g=Q_g(1)-Q_g(t)+g(t)\) and note that \(g(t)=t^{\rho-1}\) on \([1,3]\).
Only the prescribed values on \([0,1]\) enter the original definition of
\(Eg\); this equivalent calculation does not impose extra input data.

## 3. Nearly sharp power witnesses at every sufficiently large degree

**Theorem 2.** For every hypothetical zero \(\rho=\beta+i\gamma\) with
\(\beta>1/2\), and every fixed \(0<b<1\), there are positive constants
\(c_{\rho,b}\), \(N_{\rho,b}\) such that

\[
 \Lambda_N\ge c_{\rho,b}N^{b(2\beta-1)}
 \qquad\text{for every }N\ge N_{\rho,b}.
 \tag{3.1}
\]

No zero is assumed simple or used to define \(S_N\) or \(\Lambda_N\).

**Proof.** Choose an integer \(r\ge2\) satisfying

\[
 (1-b)r>1+\frac32b,
\]

and set \(\epsilon=N^{-b}\). Apply Lemma 1 to the odd smooth cutoff from
Section 2. By (2.1) its derivative approximation error is

\[
 D_N\le C N^{1-r}\epsilon^{\beta-2-r}
       =C N^{1-r+b(r+2-\beta)}
       =O(N^{-b\delta}).
 \tag{3.2}
\]

The displayed inequality on \(r\) is exactly what is needed, since
\(2-\beta+\delta=3/2\). Constants may depend on \(b,\rho,r,\chi\), but not
on \(N\). Equations (1.2) and (2.5) give actual polynomials \(p_N\in\Pi_N\)
at every sufficiently large degree budget with

\[
 \|Ap_N\|=O(N^{-b\delta}),\qquad
 Ep_N\longrightarrow t^{\rho-1}\text{ in }L^2(1,3).
\]

The limiting output norm is strictly positive. Injectivity of \(A\) on
polynomials and the definition of \(\Lambda_N\) now prove (3.1). QED.

This removes DG26's fixed factor-ten loss by allowing a fixed higher
approximation order for each chosen \(b<1\). It does not set \(b=1\), assume
uniformity as \(b\uparrow1\), or give effective constants uniform in zero
height. None of those strengthenings is needed for the next theorem.

## 4. The exact common logarithmic growth exponent

Let \(\Theta\) be the supremum of the real parts of the nontrivial zeta zeros.
Classically \(1/2\le\Theta\le1\). The endpoint \(\Theta=1\) is included.

**Theorem 3.** Unconditionally as a relation to this unknown supremum,

\[
 \boxed{\lim_{N\to\infty}\frac{\log(1+\Lambda_N)}{\log N}
       =\lim_{N\to\infty}\frac{\log(1+S_N)}{\log N}
       =2\Theta-1.}
 \tag{4.1}
\]

This does not evaluate \(\Theta\), prove regular variation, or assert a
positive asymptotic constant.

**Upper bound and its exact classical input.** The generalized Littlewood
implication says that zero freedom on \(\Re s>\theta\), \(1/2\le\theta<1\),
gives \(M_a(x)=O_\varepsilon(x^{\theta+\varepsilon})\). XCC26 Section 1.2
reconstructs the applicable proof: Borel--Caratheodory and three circles
give a subpower inverse-zeta bound inside the zero-free half-plane, then
truncated Perron on a strictly interior vertical line gives the Mertens
bound. No estimate on the zero boundary itself is used here.

It follows by separating even integers and partial summation that, for any
\(\Theta<\beta<1\),
\(|m_o(x)|=O_\beta(x^{\beta-1})\). DG26's whole-trace estimate, whose short
proof is included below, then gives \(S_N=O_\beta(N^{2\beta-1})\). Let
\(\beta\downarrow\Theta\). If \(\Theta=1\), use the elementary uniform
bound \(|m_o|\le2\), giving \(S_N=O(N)\). These prove the upper exponent in
all cases, including \(\Theta=1/2\).

For the stated whole-trace estimate let \(d=2N-1\). The Legendre boundary
bound

\[
 \left(\sum_{j<N}|\phi_j(u)|^2\right)^{1/2}
       \le9d^{3/2}u,\qquad0\le u\le1/2,
 \tag{4.2}
\]

follows from the classical Laplace integral for \(P_l\): on \(|u|\le1/2\)
it gives \(|P_l'(u)|\le5\sqrt l\), hence the normalized derivative is at
most \(9l\); integrate from zero and sum \(l^2\le d^3\). More explicitly
the bracket \(u+i\sqrt{1-u^2}\cos v\) has derivative modulus below two and
modulus squared at most \(1-3\sin^2v/4\). Gaussian integration bounds its
\(q\)-th absolute moment by \(3/(2\sqrt q)\) for \(q\ge1\), proving the
derivative estimate; \(l=1\) is direct.

Split the finite-rank kernel at \(u=1/d\). Under
\(|m_o(x)|\le M_\beta x^{\beta-1}\), its low-input Hilbert--Schmidt norm is
bounded by
\(9M_\beta\sqrt{I_\beta}d^{\beta-1/2}/(2-\beta)\), where
\(I_\beta=\int_1^3t^{2\beta-2}dt\). The high-input kernel is square
integrable, and projection cannot increase its Hilbert--Schmidt norm; its
bound is \(M_\beta\sqrt{I_\beta}d^{\beta-1/2}/\sqrt{2\beta-1}\).
Adding and squaring proves the assertion with no dimension loss. For
\(M_1=2\) it gives \(S_N\le800d\); \(N=1\) follows directly.

**Lower bound.** For every right-of-line zero, Theorem 2 and (0.1) give
both lower exponents at least \(b(2\beta-1)\), for every fixed \(b<1\).
Take the supremum over these \(b\) and zeros. This gives \(2\Theta-1\).
If \(\Theta=1/2\), nonnegativity of the logarithmic ratios supplies zero.
No supremum need be attained. QED.

In particular, if an actual unbounded subsequence satisfies
\(S_{N_j}\le N_j^{r+o(1)}\), or the corresponding bound for \(\Lambda\),
then all nontrivial zeros obey \(\Re\rho\le(1+r)/2\). This sharpens the
quantitative sparse implication, not just the already-known subpower case.
For \(r=0\), functional-equation reflection gives RH.

There is also a sparse relative-gain criterion: for fixed \(q>1\) and
\(0<\delta<q\), a bound

\[
 1+S_{\lfloor N_j^q\rfloor}
 \le N_j^{o(1)}(1+S_{N_j})^{q-\delta}
 \tag{4.3}
\]

on any unbounded sequence forces RH. If \(2\Theta-1=\kappa>0\), taking
logarithms contradicts \(q\kappa\le(q-\delta)\kappa\). The same assertion
holds for \(\Lambda\). No spacing condition on the selected degrees is
needed. No such source-relative gain is proved in this packet.

### An unconditional subpower effective-rank bound

There is a quantitative corollary whose conclusion does not contain the
unknown zero abscissa. For every \(\varepsilon>0\) there is a finite
\(C_\varepsilon\) such that

\[
 1\le\frac{S_N}{\Lambda_N}\le C_\varepsilon N^\varepsilon
 \qquad(N\ge1).
 \tag{4.4}
\]

Indeed \(S_N\) and \(\Lambda_N\) are bounded below by their positive
first-degree values, so replacing \(\log(1+X)\) by \(\log X\) changes
each normalized logarithm by a vanishing quantity. Subtract the two limits
in (4.1), then absorb finitely many initial degrees. This improves the
generic finite-rank inequality \(S_N\le N\Lambda_N\) to a subpower loss
for this actual arithmetic source, without assuming RH. Its constants are
not evaluated or claimed effective by this argument.

If \(\tau_{N,j}\) are the eigenvalues of the positive output covariance
\(K_NK_N^*\), then \(\Lambda_N=\max_j\tau_{N,j}\) and
\(S_N=\sum_j\tau_{N,j}\). Hence for any fixed relative threshold
\(\alpha>0\),

\[
 \#\{j:\tau_{N,j}\ge\alpha\Lambda_N\}
       \le C_\varepsilon\alpha^{-1}N^\varepsilon.
 \tag{4.5}
\]

Thus a subpower number of source-dependent modes suffices for approximation
in RELATIVE OPERATOR NORM. This does not give a prescribed approximation
basis, an effective mode census, or capture of the whole trace in that many
modes: many small eigenvalues may retain trace mass. In particular it does
not control the largest eigenvalue itself.

Combining (4.1) with XCC26's exact all-integer energy exponent also gives a
same-index asymptotic adapter: for every \(\varepsilon>0\), after changing
its finite constant,

\[
 C_\varepsilon^{-1}N^{-\varepsilon}F_N
       \le\Lambda_N\le S_N
       \le C_\varepsilon N^\varepsilon F_N.
 \tag{4.6}
\]

This is again an unconditional, non-effective consequence of matching
growth exponents, not a new bound on their common magnitude. The following
finite adapter supplies explicit constants and a finite coverage rule
instead of this asymptotic constant.

## 5. A fully finite adapter from ordinary Mobius energy to the trace

**Theorem 4.** For \(N\ge1\), \(d=2N-1\), and any integer \(M\ge2\),

\[
 S_N\le\left[
 \sqrt{(6+4\sqrt2)\log3\;F_{3M}}
       +\frac{18\sqrt2\,d^{3/2}}M\right]^2.
 \tag{5.1}
\]

In particular, for \(N\ge2\), choosing \(M=\lceil d^{3/2}\rceil\) gives

\[
 \boxed{S_N\le26F_{3\lceil(2N-1)^{3/2}\rceil}+1296.}
 \tag{5.2}
\]

The entire right side uses native coefficients only through its displayed
finite index. The residual constant pays every omitted smaller input scale;
it is not an omitted future or an assumption on future Mobius signs.

**Proof.** First,

\[
 m_o(x)=\sum_{j\ge0}2^{-j}m_a(x/2^j).
 \tag{5.3}
\]

At every finite \(x\) only finitely many terms occur; this follows by
separating even indices in the Mobius sum. Minkowski and dilation on
\(L^2(0,X)\) give

\[
 \int_0^X|m_o(x)|^2dx
 \le(2+\sqrt2)^2\int_0^X|m_a(x)|^2dx.
 \tag{5.4}
\]

The coefficient is the squared sum \((\sum_{j\ge0}2^{-j/2})^2\).
For integer \(X=3M\), the final integral equals \(F_{3M-1}\le F_{3M}\).
This explicitly translates the odd source to the all-integer source of
the Newton/crossing construction.

Now split \(K_N=K\operatorname{Proj}_{\Pi_N}\) at \(u=1/M\). The full
high-input kernel has squared Hilbert--Schmidt norm

\[
 \int_1^3\int_{1/M}^1\frac{|m_o(t/u)|^2}{u^2}\,du\,dt
 =\int_1^3\frac{dt}{t}\int_t^{Mt}|m_o(x)|^2dx
 \le\log3\int_0^{3M}|m_o(x)|^2dx.
 \tag{5.5}
\]

Projection in its input does not increase that norm. For the low input use
\(|m_o|\le2\) and (4.2). The Hilbert--Schmidt triangle inequality for its
rank-one integral gives the bound

\[
 \int_0^{1/M}\frac{2\sqrt2}{u}
 \left(\sum_{j<N}|\phi_j(u)|^2\right)^{1/2}du
 \le18\sqrt2\,d^{3/2}/M.
 \tag{5.6}
\]

Here \(1/M\le1/2\), so the boundary estimate applies throughout. Equations
(5.4)--(5.6), added before squaring, prove (5.1). Using
\((a+b)^2\le2a^2+2b^2\), \(2(6+4\sqrt2)\log3<26\), and \(M^2\ge d^3\)
proves (5.2). For the numerical coefficient, the elementary bounds
\(\sqrt2<10/7\), \(\log3<11/10\) already suffice; the latter follows from
the positive Taylor polynomial for \(e^{11/10}\) through degree five. QED.

This is an explicit finite-index adapter. It does not identify the trace
with XCC26's covariance or its diagonal. A proved bound for the COMPLETE
native energy transfers; a bound for one component of that energy does not.

## 6. Attempted completion and the remaining obstruction

The sharper witness calculation succeeds: the spectral abscissa, trace,
and native-energy logarithmic exponents now agree exactly. The finite
adapter succeeds with a displayed \(N^{3/2}\) arithmetic coverage cost.
Neither argument gives a new upper bound on that common exponent.

At the latest crossing cuts, XCC26 supplies a cheap sign-faithful completion
and the reduction

\[
 F_{(Y+1)^2-1}\le F_Y+8/Y+576H_{4Y^2}^4+2C_Y.
\]

Its same-product diagonal is paid, but the signed distinct-product
covariance \(C_Y\) is still unbounded at the needed scale. Substituting its
diagonal alone into (5.1) would be invalid: (5.1) consumes the entire \(F\).
The exact exponent theorem likewise cannot prove its own upper exponent
zero by renaming that exponent \(2\Theta-1\).

The next completion theorem remains an actual subpower upper estimate for
\(S_N\), for its complete positive block increments, or for the native
energy/covariance at an unbounded sequence. The present work removes a
quantitative approximation loss and supplies a missing source adapter; it
does not supply that arithmetic cancellation. The trace is known to grow
at least logarithmically from a classical critical-line zero, so bounded
finite-degree plots are not an admissible substitute.

The accompanying computation reconstructs small actual traces in directed
arithmetic and finite native energy identities, with complete polynomial
integrals. It tests these normalizations and finite inequalities, not the
infinite Fourier argument, the generalized Littlewood theorem, or RH.
