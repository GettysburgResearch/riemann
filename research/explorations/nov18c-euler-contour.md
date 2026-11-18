# Removing the poles of a symmetrized Euler product creates off-line zeros

**Proposed analytic results.** A finite Euler product is zero-free wherever it is holomorphic. Trying to prove RH by completing, reflecting, and passing to the limit introduces poles on two vertical lines. We calculate the least possible cost of removing them by a bounded holomorphic multiplier. An additive construction converges locally uniformly to the ordinary completed zeta function and provides alternating strict upper and lower bounds on its entire critical line. Yet every sufficiently large approximant has off-line zeros inside a classical zero-free region of zeta. We prove a growing lower bound for their number and identify the heights at which they occur.

Fix $0<\delta<1/2$, $\ell=-\delta$, $r=1+\delta$, and $S=\{\ell<\Re s<r\}$. Set
\[
 B(s)=\tfrac12 s(s-1)\pi^{-s/2}\Gamma(s/2),\quad
 Z_Y(s)=\prod_{p\le Y}(1-p^{-s})^{-1},\quad
 H_Y(s)=B(s)Z_Y(s)+B(1-s)Z_Y(1-s).
\]
Use the removable value of $B$ at zero, and take $Y\ge2$. On the two boundary lines $H_Y\to\xi$, dominated by an integrable bound uniform in $Y$. Indeed $Z_Y$ converges uniformly to zeta on the right line. On the left line its absolute value is at most $\prod_{p\le Y}(p^\delta-1)^{-1}\to0$. Gamma decay bounds both prefactors uniformly in the ordinate. The same reasoning gives locally uniform convergence on either outer open strip up to the next pole of the gamma prefactor.

## The sharp multiplicative cost

Fix real $s_0\in(1,r)$. Among $M\in H^\infty(S)$ satisfying $M(s_0)=1$ and $MH_Y$ holomorphic on $S$, the least possible supremum norm satisfies
\[
 \log\inf_M\|M\|_\infty
       =(r-s_0)\sum_{p\le Y}\log p+O_{\delta,s_0}(\pi(Y))
       =(r-s_0+o(1))Y.                                             \tag{1}
\]
Here $\pi(Y)$ counts primes. In particular, a family of multipliers of norm $\exp(o(Y))$ that clears the poles must tend to zero at $s_0$. Normalization there is essential because the unregularized products already converge to the desired nonzero value.

For each prime $p\le Y$, the two lists of poles are
\[
 x+2\pi i k/\log p,\qquad x=0,1,\quad k\in\mathbb Z.
\]
At nonzero ordinates different primes do not coincide by unique factorization. The prefactor is nonzero at these poles and the other summand is regular. At ordinates zero the common orders equal $\pi(Y)$ because $B(0)\ne0$. For the positive strip Green function $G(s_0,z)$ with $-\Delta_zG=2\pi\delta_{s_0}$ and zero boundary values, the exact logarithmic minimum is the sum of $G$ over these poles with multiplicity. To verify this, map the strip conformally to the unit disk. At each required zero the usual Blaschke factor costs the pseudohyperbolic distance from that zero to $s_0$. Dividing a bounded holomorphic function by any finite subset of these factors preserves its supremum bound. The full strip Blaschke product, normalized at $s_0$, attains the resulting bound. It converges because the Green function decays exponentially in $|\Im z|$ on the lines used here.

For $x=0,1$, the smooth function $g_x(v)=G(s_0,x+iv)$ has integrable derivative. Both facts follow, for example, by mapping $S$ to the upper half-plane by $z\mapsto e^{i\pi(z-\ell)/(r-\ell)}$ and taking the logarithm of the ratio of distances to the reflected and original points. The Riemann-sum error bound from $\int|g_x'|$ gives
\[
 \sum_{k\in\mathbb Z}g_x(2\pi k/\log p)
      =\frac{\log p}{2\pi}\int_{\mathbb R}g_x(v)\,dv+O_{\delta,s_0}(1).
\]
Integrating the Green equation in the ordinate gives
\[
 \frac1{2\pi}\int G(s_0,x+iv)\,dv
 =\frac{(\min(x,s_0)-\ell)(r-\max(x,s_0))}{r-\ell}.
\]
This is the continuous piecewise linear function with zero boundary values and derivative jump $-1$ at $s_0$. Summing at $x=0,1$ gives $r-s_0$. Summation over primes proves (1) by the prime number theorem.

## Additive pole removal and compact convergence

Define the symmetric holomorphic approximant
\[
 R_Y(s)=\frac1{2\pi}\int_{\mathbb R}
 \left(\frac{H_Y(r+iv)}{r+iv-s}
       -\frac{H_Y(\ell+iv)}{\ell+iv-s}\right)dv,\qquad s\in S .
                                                                    \tag{2}
\]
The boundary convergence above and the Cauchy formula for $\xi$ show that $R_Y\to\xi$ uniformly on compact subsets of $S$. Reflection gives $R_Y(s)=R_Y(1-s)$, and complex conjugation gives the usual reality symmetry. For each fixed $Y$, $R_Y$ has only finitely many zeros on $0\le\Re s\le1$.

For the last assertion let $m_j$ be the difference of the boundary integrals of $w^jH_Y(w)$ on the two vertical lines, both parametrized upwards with measure $dv/(2\pi)$. Some $m_j$ is nonzero. Otherwise
\[
 L_b(u)=\frac1{2\pi}\int H_Y(b+iv)e^{(b+iv)u}\,dv,\qquad b=\ell,r,
\]
would satisfy $L_\ell=L_r$ for all real $u$, since all derivatives at zero agree and these functions are analytic for $|\Im u|<\pi/4$ by Stirling's formula. Call the common function $L$. For each boundary line $L(u)e^{-bu}$ is Schwartz: the boundary values of $H_Y$ and all their derivatives are rapidly decreasing for fixed $Y$. The bilateral Laplace transform of $L$ is therefore holomorphic inside $S$, continuous up to both boundaries, and agrees there with $H_Y$ by Fourier inversion. Near the right boundary, subtract the meromorphic expression for $H_Y$, which is holomorphic in that neighborhood. The difference has continuous zero values on the boundary line and extends by reflection as zero by the identity theorem. Thus $H_Y$ would coincide meromorphically throughout $S$ with a holomorphic function. Its actual pole at zero rules this out.

For the first $j$ with $m_j\ne0$, expanding the Cauchy kernels in (2) at large vertical height yields $R_Y(s)=-m_j/s^{j+1}+O_Y(|s|^{-j-2})$, uniformly on the closed critical strip. On $|\Im w|\le|\Im s|/2$ use the finite geometric expansion with uniformly bounded remainder after integration. On its complement the boundary data decrease exponentially and the denominators are bounded below by $\delta$. There are consequently no zeros in this strip at large enough height for a fixed $Y$. The compact remainder has finitely many zeros by analyticity.

If an unbounded sequence of these holomorphic approximants were zero-free on $1/2<\Re s<1$, Hurwitz's theorem would give RH. The last section proves that every sufficiently large Cauchy projection violates this zero-free condition. Formula (1) quantifies the cost of a multiplicative replacement of that projection.

## A signed error bound on the entire critical line

The Cauchy projection also admits an explicit physical kernel. Put \(k=\pi(Y)\), \(P=\prod_{p\le Y}p\), and write \(\mathcal S_Y\) for the positive integers whose prime factors are at most \(Y\), including one. For all sufficiently large \(Y\) and uniformly in \(|\Re z|\le1/2\),
\[
 R_Y(1/2+z)-\xi(1/2+z)
  =(-1)^{k+1}\frac{30\pi Z_Y(2)}{P^2(25/4-z^2)}
      +O\!\left(\frac{P^{-4}+e^{-cY^2}}{1+|z|^2}\right)              \tag{3}
\]
with an absolute \(c>0\). This gives strict upper and lower bounds for \(\xi(1/2+it)\) **at every real ordinate simultaneously**: the sign of \(R_Y(1/2+it)-\xi(1/2+it)\) is \((-1)^{k+1}\). The integral on the critical line is real. Since \(1\le Z_Y(2)\le\zeta(2)\) and \(\log P\le Y\log Y\), the error is smaller than the signed term uniformly there.

Use the Mellin convention \(\mathcal M b(s)=\int_0^\infty b(x)x^s\,dx/x\). Two differentiations of the Gaussian give \(\mathcal M b(s)=B(s)\) for
\[
                  b(x)=(4\pi^2x^4-6\pi x^2)e^{-\pi x^2}.
\]
Indeed the starting Gaussian has transform \(\pi^{-s/2}\Gamma(s/2)/2\), and \(({-x\partial_x})^2-({-x\partial_x})\) supplies \(s(s-1)\). Integration first on \(\Re s>0\) and analytic continuation give the direct transform for \(\Re s>-2\) since \(b(x)=O(x^2)\) at zero. On the right boundary use the exact identity
\[
                   Z_Y(1-s)=(-1)^k P^{1-s} Z_Y(s-1).
\]
The finite-prime Dirichlet expansion of \(Z_Y(s-1)\) is absolutely convergent on that line. The inverse Mellin kernel of \(B(1-s)\) is \(x^{-1}b(1/x)\). Scaling by \((Pn)^{1-s}\) therefore gives \(x^{-1}b(1/(Pnx))\). Mellin inversion on the right boundary is justified termwise by absolute convergence and gamma decay. The inverse Mellin kernel of \(H_Y\) there is
\[
 h_Y(x)=\sum_{n\in\mathcal S_Y} b(nx)
           +(-1)^k x^{-1}\sum_{n\in\mathcal S_Y} b(1/(Pnx)).
\]
For the right boundary term of (2), use \((r+iv-s)^{-1}=\int_0^\infty e^{-(r+iv-s)u}\,du\). Inversion yields \(\int_0^\infty h_Y(e^u)e^{su}\,du\). Substitution \(v\mapsto-v\) and the symmetry of \(H_Y\) make the other boundary term the same expression at \(1-s\). Consequently
\[
 R_Y(1/2+z)=2\int_0^\infty K_Y(u)\cosh(zu)\,du,\qquad
 K_Y(u)=e^{u/2}h_Y(e^u).                                             \tag{4}
\]
The corresponding expression for \(\xi\) has \(K(u)=e^{u/2}\sum_{n\ge1}b(ne^u)\). This follows by applying the same boundary formula directly to \(\xi\), whose right-boundary inverse kernel is \(\sum_{n\ge1}b(nx)\), and using its functional equation on the other boundary.

For \(0\le a\le2\), the derivatives of order \(a\) in \(u\) of the omitted first-sum tail, at \(u\ge0\), satisfy
\[
 \left|\partial_u^a\left[e^{u/2}\sum_{n\notin\mathcal S_Y}b(ne^u)\right]\right|
           \ll e^{-cY^2}e^{-3u}.
\]
Every omitted \(n\) exceeds \(Y\). The differentiated summands are \(e^{u/2}\) times polynomials in \(ne^u\) times \(e^{-\pi n^2e^{2u}}\), which give the displayed bound after summing the Gaussian tail. For the reflected sum, \(b(x)=-6\pi x^2+O(x^4)\) uniformly on \(0\le x\le1/2\), with the same order of remainder after zero, one or two applications of \(x\partial_x\). Hence
\[
 K_Y(u)-K(u)=(-1)^{k+1}6\pi P^{-2}Z_Y(2)e^{-5u/2}+g_Y(u),\qquad
 |g_Y^{(a)}(u)|\ll P^{-4}e^{-9u/2}+e^{-cY^2}e^{-3u}
 \quad (0\le a\le2).                                                 \tag{5}
\]
Here the sums of \(n^{-2}\) and \(n^{-4}\) over \(\mathcal S_Y\) are \(Z_Y(2)\) and \(Z_Y(4)\). For \(|\Re z|\le1/2\), integration of the main term uses \(\int_0^\infty e^{-5u/2}\cosh(zu)\,du=(5/2)/(25/4-z^2)\). For \(|z|\le1\) bound the remainder integral directly. For \(|z|>1\) integrate it by parts twice to obtain
\[
 \int_0^\infty g_Y(u)\cosh(zu)\,du
      =\frac{g_Y'(0)+\int_0^\infty g_Y''(u)\cosh(zu)\,du}{z^2}.
\]
All boundary terms at infinity vanish uniformly by (5), and \(|\cosh(zu)|\le e^{u/2}\) throughout the strip. This proves (3).

For large \(Y\) the first nonzero boundary moment in the preceding section is exactly \(m_1\). Indeed symmetry gives \(m_0=0\) and \(m_1=-2K_Y'(0)\), by differentiating \(L_r(u)=h_Y(e^{-u})\) and \(L_\ell(u)=e^u L_r(-u)\) at zero. For \(\xi\) both boundary transforms agree by shifting its entire contour, which gives \(K'(0)=0\). Equation (5) now yields
\[
                 m_1=(-1)^{k+1}30\pi P^{-2}Z_Y(2)
                        +O(P^{-4}+e^{-cY^2}).
\]
The strict envelopes in (3) locate each approximant vertically relative to the real value of \(\xi\) on its symmetry axis. The behavior away from that axis is determined in the rectangles below.

## Every sufficiently large additive approximant has off-line zeros

Let \(T=(8/\pi)\log P\) and \(L=\log T\). There is an absolute \(0<\eta_0<1/2\) such that for either \(\eta=\eta_0\) or \(\eta=L^{-3/4}\), all sufficiently large \(Y\) have at least \(c\eta L^2\) zeros of \(R_Y\), counted with multiplicity, in
\[
  1-\eta<\Re s<1,\qquad
  T+\frac4\pi(4-\eta/4)L\ <\ \Im s\ <  T+\frac4\pi(4-\eta/8)L.                                             \tag{6}
\]
In the shrinking rectangle these zeros are inside the classical Vinogradov–Korobov zero-free region of the **actual** zeta function. In particular the suggested zero-free subsequence of additive approximants cannot exist. The zeros just established escape to increasing heights, consistently with compact convergence to \(\xi\).

We use the classical Richert bound \(|\zeta(\sigma+it)|\ll(\log t)^C t^{C(1-\sigma)^{3/2}}\) on \(1/2\le\sigma\le1\), \(t\ge3\), and the classical zero-free region \(\sigma\ge1-c(\log t)^{-2/3}(\log\log t)^{-1/3}\). Only the latter comparison with the actual zeros uses this full zero-free width. The bound on the right side of the rectangle is the standard \(|\log\zeta(1+it)|\ll\log\log t\) for the branch continued horizontally from the Euler product. For example, the ordinary zero-free strip \(\sigma\ge1-c/\log t\), the local logarithmic-derivative formula, and the \(O(\log t)\) count of zeros within unit height give \(|\zeta'/\zeta|\ll(\log t)^2\) on \(1\le\sigma\le1+(\log t)^{-2}\). Integrate across that segment from the Euler logarithm, bounded there by \(\log\zeta(1+(\log t)^{-2})\ll\log\log t\). [Ford, *Vinogradov's integral and bounds for the Riemann zeta function*](https://doi.org/10.1112/S0024611502013655) · [Author’s copy with the estimates and zero-free region](https://www.ford126.web.illinois.edu/wwwpapers/zetabd.pdf)

Write \(t=T+(4/\pi)aL\) in the band of (6). Thus \(e^{-\pi t/4}=P^{-2}T^{-a}\) exactly. Uniformly for bounded \(\sigma\) near the two sides, Stirling gives \(|B(\sigma+it)|\asymp T^{3/2+\sigma/2}e^{-\pi t/4}\). Choose \(\eta_0\) so small that \(C\sqrt{\eta_0}<1/8\). On the left side, comparison with the size \(P^{-2}T^{-2}\) of the rational term in (3) gives
\[
 \frac{|\xi(1-\eta+it)|}{P^{-2}T^{-2}}
   \ll L^C T^{4-\eta/2+C\eta^{3/2}-a}
   \le L^C T^{-\eta/8}=o(1).
\]
This holds for both choices of \(\eta\), since \(\eta L\gg L^{1/4}\). On the right side
\[
 \frac{|\xi(1+it)|}{P^{-2}T^{-2}}
   \gg L^{-C} T^{4-a}\ge L^{-C} T^{\eta/8}\longrightarrow\infty.
\]
By (3) the approximant on the left is the explicit rational function times \(1+o(1)\). Its denominator for \(z=1/2-\eta+it\) is \(t^2(1+O(1/t))\), so the continuous argument has net change \(O(1)\) throughout this side. On the right it is \(\xi(1+it)(1+o(1))\). For heights \(t_1<t_2\) in the band the right-side argument change, oriented upwards, is
\[
             \tfrac12(t_2-t_1)\log(T/(2\pi))+O(L).
\]
This follows from Stirling's phase for the gamma factor, the elementary polynomial factors, and the bounded endpoint changes from the chosen logarithm of zeta. All relative-error terms remain in a fixed disk around one, so they cost \(O(1)\) in net argument.

Here is the bound on the two horizontal edges. Equation (4) extends the approximant analytically to \(|\Re z|<5/2\), by (5) and the rapid decay of \(K\) on \(u\ge0\). The proof of (3), including the twice-integrated bound, works on the larger closed strip \(|\Re z|\le5/4\) as well. At any height \(t\) in the band the disk \(|w-1|\le3/4\) therefore has
\[
 \sup|R_Y(w+it)|\ll P^{-2}T^{C'},\qquad |R_Y(1+it)|\gg P^{-2}T^{-2}.
\]
The first bound uses polynomial growth of zeta on this fixed strip, Stirling, and (3). Set \(\theta=\arg R_Y(1+it)\). The analytic function
\[
 G(w)=\tfrac12\left(e^{-i\theta}R_Y(w+it)
        +e^{i\theta}\overline{R_Y(\bar w+it)}\right)
\]
has \(G(1)=|R_Y(1+it)|\) and the same upper bound on the disk. Jensen's inequality on concentric disks shows that it has \(O(L)\) zeros in \(|w-1|\le1/2\). On the real segment \(1-\eta\le w\le1\), these include every sign change of the real part of the rotated \(R_Y\). Choose \(t_1\) in the first unit interval inside the band and \(t_2\) in the last, avoiding zeros on the horizontal edges. The isolated zeros of a nonzero holomorphic function allow such choices. Between consecutive zeros of that real part the argument stays in a single open half-plane, so the net change on each horizontal edge is \(O(L)\). This argument does not require any separation of the edge from neighboring zeros.

The counterclockwise argument principle gives \((t_2-t_1)\log(T/(2\pi))/(4\pi)+O(L)\) zeros in the enclosed rectangle. Its height is \(\eta L/(2\pi)+O(1)\), so the claimed lower bound follows. Finally \(L^{-3/4}=o(L^{-2/3}(\log L)^{-1/3})\), placing the shrinking rectangle strictly inside the stated zeta zero-free region.
