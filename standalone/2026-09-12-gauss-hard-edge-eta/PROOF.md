# GHE26 — exact Gauss–Thorin tails, the odd-square edge, and an eta-valued quadrature error

Date: 2026-09-12. **Proposed component proofs; not independently reviewed. RH is not proved.**

This is an additive continuation of #851, informed by #862, #872, #874 and #876. It does not accept every result in those packets or modify their claims. The new calculations below concern the unchanged Gaussian quadrature of the actual Brownian logarithmic-Laplace source. The main result identifies, including its first correction, the complex Mellin transform of the *moving-scale logarithmic approximation error*. That transform contains the actual Dirichlet eta function. This is a connection between the quadrature, gamma-tail, and hyperbolic programmes, not a proof that the zeros of eta are central.

Classical ingredients are Gaussian quadrature, Lambert's continued fraction, its Lommel-type continuants, elementary spectral compression, gamma infinite divisibility, and the Fermi–Dirac Mellin integral. No priority claim is made for these ingredients, the general type of edge limit, or zeta integral representations. The proposed contribution relative to the inspected packets is their exact source-specific composition, the independent positive thin-tail decomposition, the uniform complex error limit and first correction, and the resulting auxiliary-zero displacement formula. An exhaustive novelty search was not performed.

## 1. Source and notation

Use independent mean-one exponentials and set

\[
 \alpha_j=\frac6{\pi^2j^2},\qquad
 X_* =\sum_{j\ge1}\alpha_j E_j,\qquad
 L_*(t)=\frac{\sqrt{6t}}{\sinh\sqrt{6t}},\qquad
 g(t)=-\frac{L_*'(t)}{L_*(t)}.
\]

The positive series converges in every finite positive moment. Its inverse moments exist from the displayed Laplace decay. The classical BPY source identification is

\[
 \frac12(\pi/6)^{s/2}\mathbb E(X_*+X_*')^{s/2}=\xi(s).
 \tag{1}
\]

Introduce the probability measure

\[
 \nu=\sum_{j\ge1}\alpha_j\delta_{\alpha_j},\qquad
 g(t)=\int\frac{d\nu(a)}{1+ta}.
\]

Let \(x_{m,i},w_{m,i}\) be its m-node Gaussian quadrature, with positive weights summing to one. For this manuscript suppress m in individual nodes and put

\[
 k_i=w_i/x_i,\quad
 X_m=\sum_{i=1}^m\operatorname{Gamma}(k_i,\text{scale }x_i),\quad
 L_m(t)=\prod_i(1+x_it)^{-k_i},\quad
 g_m(t)=\sum_i\frac{w_i}{1+x_it}=\frac{Q_m(t)}{P_m(t)}.
 \tag{2}
\]

Here \(P_m(t)=\prod_i(1+x_it)\), \(P_m(0)=Q_m(0)=1\). Let \(p_m(x)=\prod_i(x-x_i)\). The squared monic norm is \(h_m=\int p_m^2d\nu\), and \(d_m=h_m/(2m+1)\). The source and seed have identical cumulants and moments through order 2m.

**Two distinct Mellin coordinates:** in (1), the Brownian moment exponent is s/2. In Sections 6–9, q denotes the exponent in the Mellin transform of the *scaled log-Laplace error*, and its eta coordinate is \(s=2q-1\). These coordinates must not be identified.

## 2. All-order Jacobi and continuant formulae

Define

\[
 b_0=\frac25,\qquad b_n=\frac{12}{(4n+1)(4n+5)}\ (n\ge1),\qquad
 \lambda_n=\frac{36}{(4n-1)(4n+1)^2(4n+3)}\ (n\ge1).
 \tag{3}
\]

Then the quadrature nodes are exactly the eigenvalues of the symmetric m-by-m Jacobi matrix with diagonal \(b_0,\ldots,b_{m-1}\) and off-diagonal \(\sqrt{\lambda_1},\ldots,\sqrt{\lambda_{m-1}}\). Both continuants satisfy

\[
 Y_{m+1}=(1+b_mt)Y_m-\lambda_mt^2Y_{m-1},
\]

with \(P_0=1,P_1=1+2t/5,Q_0=0,Q_1=1\). Explicitly,

\[
 P_m(t)=\sum_{j=0}^m
 \binom{2m-j}{j}
 \frac{(3t/2)^j}{(3/2)_j(2m+3/2-j)_j},
 \tag{4}
\]

\[
 Q_m(t)=\sum_{j=0}^{m-1}
 \binom{2m-1-j}{j}
 \frac{(3t/2)^j}{(5/2)_j(2m+3/2-j)_j}.
 \tag{5}
\]

**Identification.** Write \(S(t)=1/L_*(t)={}_0F_1(3/2;3t/2)\). Direct coefficient comparison gives

\[
 {}_0F_1(a;z)-{}_0F_1(a+1;z)
 =\frac{z}{a(a+1)}{}_0F_1(a+2;z).
\]

Consequently \(g=S'/S\) has the Stieltjes continued fraction with coefficients
\(c_n=6/[(2n+1)(2n+3)]\), n>=1. Its odd convergents have numerator degree m-1 and denominator degree m. Contracting gives \(b_0=c_1,b_n=c_{2n}+c_{2n+1},\lambda_n=c_{2n-1}c_{2n}\), which are (3). Alternatively, the finite convergents agree with the source formal series through degree 2m-1, and uniqueness of Gaussian quadrature gives the same identification. This is the classical Lambert/Lommel mechanism [E1], not a new continued fraction.

For completeness, (4) follows by induction in the continuant recurrence. If C(m,j) is its coefficient and D=(2m-2j+2)(2m-2j+1), then, for 1<=j<=m,

\[
\begin{split}
 C(m+1,j)/C(m,j)&=
 \frac{(2m+2-j)(2m+1-j)(2m+3/2-j)(2m+5/2-j)}{D(2m+3/2)(2m+5/2)},\\
 C(m,j-1)/C(m,j)&=
 \frac{2j(j+1/2)(2m-j+1)(2m+3/2-j)}{3D},\\
 C(m-1,j-2)/C(m,j)&=
 \frac{4j(j-1)(j-1/2)(j+1/2)(2m-1/2)(2m+1/2)}{9D}.
\end{split}
\]

The first ratio equals one plus b_m times the second minus lambda_m times the third, by multiplication of denominators. The j=0 and leading-coefficient boundaries are immediate; the initial cases are explicit. Formula (5) has the same verification, or follows from the numerator continuant.

Set

\[
 A_m=\frac{m(2m+3)}2,\qquad \beta_m=\frac{6^m}{(4m+1)!!}.
\]

The following are **exact**, not fitted asymptotics:

\[
 \sum_i k_i=A_m,\quad
 \prod_i x_i=\beta_m,\quad
 h_m=\frac{3\beta_m^2}{4m+3},\quad
 \boxed{d_m=\frac{3\,36^m}{(2m+1)(4m+3)((4m+1)!!)^2}.}
 \tag{6}
\]

The leading coefficients of (4),(5) prove the first two identities. Also \(h_m=\prod_{j=1}^m\lambda_j\), whose ratio to \(\beta_m^2\) telescopes to \(3/(4m+3)\). Two more useful identities are

\[
 \sum_i x_i=1-\frac3{4m+1},\qquad
 \sum_i x_i^{-1}=\frac{A_m(2A_m+1)}6.
 \tag{7}
\]

The first is the trace of (3); the second is the next-to-leading coefficient of (4) divided by its leading coefficient.

### Minimal total gamma shape

Among all finite positive gamma convolutions with the same first 2m cumulants as X_*, the total gamma shape is at least A_m. Equality forces the Gaussian quadrature measure.

Indeed such a convolution defines a positive measure \(\widetilde\nu=\sum k_i x_i\delta_{x_i}\) matching the first 2m source moments, including order zero. The polynomial

\[
 R(x)=\frac{1-p_m(x)^2/p_m(0)^2}{x}
\]

has degree 2m-1, and \(1/x-R(x)=p_m(x)^2/[xp_m(0)^2]\ge0\) for x>0. Thus

\[
 \int x^{-1}d\widetilde\nu\ge\int R\,d\nu
 =\sum_iw_i/x_i=A_m.
\]

Equality confines the measure to the m Gaussian nodes, and moment matching determines the weights. The claim concerns positive gamma scales without a deterministic drift counted as a finite gamma shape.

## 3. A complete square residual and its positive comparison

The actual source solves

\[
 2tg'(t)+3g(t)+2tg(t)^2=3.
\]

Its finite quadrature satisfies the exact rational identity

\[
 \boxed{2tg_m'(t)+3g_m(t)+2tg_m(t)^2
 =3\bigl(1-\epsilon_m(t)^2\bigr),\qquad
 \epsilon_m(t)=\frac{\beta_m t^m}{P_m(t)}
 =\prod_i\frac{x_it}{1+x_it}.}
 \tag{8}
\]

To prove it, multiply the residual by P_m^2. The numerator has degree at most 2m. Matching the source series through degree 2m-1 makes every lower coefficient vanish; its leading coefficient is -3 beta_m^2. This proves the complete identity, not just its Taylor jet.

Every finite gamma shape satisfies **k_i>1**. At the simple real pole \(t_i=-1/x_i\), the residue of g_m is k_i>0. Comparing the double-pole terms of (8) gives

\[
 k_i(k_i-1)=-\frac3{2t_i}\bigl(\operatorname{Res}_{t_i}\epsilon_m\bigr)^2>0.
 \tag{9}
\]

This also gives a node-derivative formula for the shapes without a separate quadrature-weight calculation.

Let r=sqrt(6t), \(u_m(r)=r/L_m(r^2/6)\). Then

\[
 u_m''(r)=[1-\epsilon_m(r^2/6)^2]u_m(r),\quad u_m(0)=0,\quad u_m'(0)=1.
 \tag{10}
\]

The source has u_*(r)=sinh r. This is a positive Sturm comparison in the **r variable**, not a self-adjoint realization of xi zeros in the Mellin variable.

We need a quantitative consequence of (10). The potential V_m(r)=1-epsilon_m(r^2/6)^2 lies in (0,1] and is decreasing. For a fixed r compare u_m on [0,r] with \(v(x)=\sinh(\sqrt{V_m(r)}x)/\sqrt{V_m(r)}\). The derivative of \(u_m'v-u_mv'\) is nonnegative, and both functions vanish at zero with derivative one. Therefore

\[
 \sqrt{V_m(r)}\coth(r\sqrt{V_m(r)})
 \le u_m'(r)/u_m(r)\le\coth r.
\]

For 0<=v<=1, \(\coth r-v\coth(rv)\le1-v\). One verification is that \(v\mapsto v\coth(rv)-v\) is decreasing: its derivative has this sign because \((1-e^{-2rv})/2\le rv\). Since 1-sqrt(1-e^2)<=e^2, we obtain

\[
 \boxed{0\le g(t)-g_m(t)\le\frac3{\sqrt{6t}}\epsilon_m(t)^2.}
 \tag{11}
\]

All comparisons concern positive real arguments. No complex phase inequality is inferred.

## 4. A common independent core and two positive thin tails

Let \(Y_m=\sum_i x_iE_i\). There are **independent** decompositions in law

\[
 \boxed{X_m=Y_m+Z_m,\qquad X_*=Y_m+R_m,}
 \tag{12}
\]

where

\[
 Z_m=\sum_i\operatorname{Gamma}(k_i-1,x_i).
\]

For R_m, order the x_i decreasingly. Multiplication by a in L^2(nu) is unitarily represented by the infinite Jacobi matrix (3), since polynomials are dense for the compactly supported measure. Its eigenvalues are alpha_i. The min–max principle for principal compressions gives x_i<=alpha_i. Independently for each i<=m, take a variable which is zero with probability x_i/alpha_i and an exponential of scale alpha_i with the remaining probability; add the original exponential tail with indices i>m. The resulting R_m has Laplace transform

\[
 L_{R_m}(t)=P_m(t)L_*(t).
\]

Thus (12) is an independent convolution identity, not just a coupling inequality. Moreover R_m is infinitely divisible. Its Levy density is

\[
 \frac1u\left[\sum_{j\ge1}e^{-u/\alpha_j}-\sum_{i=1}^me^{-u/x_i}\right]\ge0.
 \tag{13}
\]

Termwise nonnegativity follows after the same ordering; the required integrability follows from the finite mean. Z_m is a positive gamma convolution by (9).

Both tails have the same first 2m moments, and exactly

\[
 \boxed{\mathbb ER_m=\mathbb EZ_m=\frac3{4m+1},\qquad
 \operatorname{Var}R_m=\operatorname{Var}Z_m=
 \frac{18}{(4m-1)(4m+1)^2}.}
 \tag{14}
\]

Their squared coefficient of variation is 2/(4m-1). To verify (14), subtract the cumulants of Y_m from those of either full law. The mean uses (7). For the variance use

\[
 \operatorname{tr}J_m^2=\sum_{j=0}^{m-1}b_j^2+2\sum_{j=1}^{m-1}\lambda_j.
\]

The complementary sum telescopes to 18/[(4m-1)(4m+1)^2]. Matching all lower cumulants then gives the other moments. This is a positive, high-order replacement of a small independent tail; it connects to, but is not the same construction as, the centered integer-square truncations of #862.

### The complete positive error survives removal of the core

The Gaussian resolvent remainder is

\[
 g-g_m=t^{2m}\frac{\int p_m(a)^2(1+ta)^{-1}d\nu(a)}{P_m(t)^2}.
\]

Dividing its integral by t^(2m+1) gives a positive Laplace transform B_m(t) with mass d_m. This follows by multiplying exponential/gamma Laplace transforms and integrating their positive scalings, exactly as in #851. Since R_m and Z_m are both infinitely divisible,

\[
 \frac{L_{Z_m}(t)-L_{R_m}(t)}{t^{2m+1}}
 =B_m(t)\int_0^1L_{Z_m}(t)^{1-v}L_{R_m}(t)^v\,dv
\]

is again a positive Laplace transform of mass d_m. Thus the complete positive-defect law remains valid **after independent deconvolution of Y_m**. Low moments alone would not establish this.

## 5. An explicit positive source path, and what zero control it still needs

Promote the auxiliary gamma interpolation in #851 to the fully specified path

\[
 L_{m,\theta}=L_m^{1-\theta}L_*^\theta,\qquad0\le\theta\le1.
 \tag{15}
\]

Every point is an explicit positive infinitely divisible law, with the same first 2m moments and the common independent core (12). It is not the beta/uniform fixed-point homotopy of #876; no intermediate results for that different family are transferred silently.

Writing k=2m+1, its source derivative is

\[
 -\partial_\theta L_{m,\theta}=t^kB_m(t)L_{m,\theta}(t).
\]

For \(F_{m,\theta}(s)=\tfrac12c^q\mathbb E(X_{m,\theta}+X_{m,\theta}')^q\), c=pi/6, q=s/2, the complete response is

\[
 \partial_\theta F_{m,\theta}(s)
 =d_m c^q(q)_{\underline{k}}\mathbb EW_{m,\theta}^{q-k},
 \qquad 0<\Re q<1,                                    \tag{16}
\]

where W has the positive law with Laplace transform \((B_m/d_m)L_{m,\theta}^2\). This follows from the negative-moment integral and \(\Gamma(k-q)/\Gamma(-q)=-(q)_{\underline{k}}\), since k is odd. The inverse moments needed here exist: W dominates a pair of source variables, \(L_{m,\theta}^2\le L_m^2\), and k-Re(q)<2A_m. Differentiation is justified on compact exponent sets by these bounds and the common exponential-moment domain.

At m=1 the initial reflected Mellin function is the same gamma endpoint whose all-height strip zero-safety is proved in the principal manuscript of #876. The endpoint theta=1 is the literal xi function. The proposed finishing argument would need to establish nonpositive **net** off-central weighted zero production along (15), including all collisions and boundary/tail effects. Formula (16) does not supply that sign: its complex expectation is oscillatory.

In particular, (8) cannot be presented as a positive-metric xi operator. The original #851 raw third seed already has a certified off-central Mellin zero, and its second seed fails the earlier global phase-monotonicity test. Those are existing certificates, not newly replayed here. Our new square identity holds for those same seeds. Reflection and a genuinely source-specific global sign are still necessary.

## 6. The moving-scale edge is an odd-square spectrum

The **natural scale is the exact total shape A=A_m**, not just its leading equivalent m^2. Define

\[
 \phi_m(z)=\frac{p_m(z/A^2)}{p_m(0)}.
\]

Reversing (4) and pairing its factors gives the exact coefficients

\[
 \phi_m(z)=\sum_{r=0}^m\frac{(-2z/3)^r}{(2r)!}
 \prod_{j=0}^{r-1}
 \left(1-\frac{j(j+3/2)}A\right)
 \left(1-\frac{(j-1/2)(j+1)}A\right).
 \tag{17}
\]

All factors are positive for r<=m; only the j=0 second factor exceeds one. Put

\[
 a_r=\frac{(2/3)^r}{(2r)!},\qquad
 c_{m,r}=[(-z)^r]\phi_m(z),\qquad c_{m,r}=0\ (r>m).
\]

For every r>=1,

\[
 |c_{m,r}-a_r|\le \frac{r^3}{A}a_r,\qquad
 \left|c_{m,r}-a_r\left(1+\frac{r(7-4r^2)}{6A}\right)\right|
 \le\frac{2r^6}{A^2}a_r.                              \tag{18}
\]

Here is a direct bound retaining the entire coefficient tail. For r<=m, write the product as \((1+1/(2A))\prod(1-u_j)\), with u_j in [0,1]. Their sum is

\[
 U=\frac{S_r}{A},\qquad S_r=\frac{4r^3-7r+3}{6}.
\]

The elementary bounds 0<=1-prod(1-u_j)<=U and
\(0\le\prod(1-u_j)-1+U\le U^2/2\) give (18), using A>=5/2. For r>m, A<r^2 and the same displayed bounds follow directly with c=0. These arguments prove the inequalities for all orders; the checker only verifies additional finite cases.

Consequently, locally uniformly in the **whole complex plane**,

\[
 \boxed{\phi_m(z)\longrightarrow\cos\sqrt{2z/3}.}
 \tag{19}
\]

The square-root expression denotes its entire power series. For v=sqrt(2|z|/3), an explicit complete error is

\[
 |\phi_m(z)-\cos\sqrt{2z/3}|\le
 \frac{v(1+v^2)\sinh v+3v^2\cosh v}{8A}.
 \tag{20}
\]

This is the sum of the first bound in (18), not a finite-series approximation.

Order the quadrature nodes increasingly at this point. For each fixed j,

\[
 \boxed{A_m^2x_{m,j}\longrightarrow
 z_j:=\frac{3\pi^2}{8}(2j-1)^2,\qquad
 \frac{k_{m,j}}{A_m}\longrightarrow
 \frac8{\pi^2(2j-1)^2}.}
 \tag{21}
\]

The first statement follows by Rouche around each simple zero of the limit in (19), excluding the compact intervals between them. All finite polynomial zeros are already real positive. For the second, write (9) in the z coordinate:

\[
 \frac{k_i(k_i-1)}{A^2}
 =\frac3{2z_i^3\phi_m'(z_i)^2}.
\]

At a limiting zero, \((\cos\sqrt{2z/3})'^2=1/(6z)\), giving k_i/A ->3/z_i. In particular the limiting shape fractions sum to one.

The second estimate in (18) also gives the first node correction,

\[
 A_m^2x_{m,j}=z_j-\frac{z_j+z_j^2/9}{A_m}+O_j(A_m^{-2}).
 \tag{22}
\]

Indeed the first correction to (19), with v=sqrt(2z/3), is
\((v^2/4)\cos v-(v/2+v^3/12)\sin v\). Taylor expansion at the simple zero proves (22); the complete second bound in (18) justifies the local remainder and its derivatives.

The zeros in (19)–(22) are **quadrature nodes**, not Riemann zeros.

## 7. Hyperbolic transition and an explicit positive logarithmic defect

For y>0 define

\[
 G_m(y)=A_m g_m(A_m^2y),\qquad
 D_m(y)=\frac1{A_m}\log\frac{L_m(A_m^2y)}{L_*(A_m^2y)}.
 \tag{23}
\]

Let u=sqrt(2/(3y)). From (17),

\[
 \epsilon_m(A_m^2y)=1/\phi_m(-1/y)\longrightarrow\operatorname{sech}u.
\]

Scaling (8), and using \(0\le G_m(y)\le\sqrt{3/(2y)}\), gives

\[
 \boxed{G_m(y)\longrightarrow
 G_0(y)=\sqrt{\frac3{2y}}\tanh\sqrt{\frac2{3y}}.}
 \tag{24}
\]

For example, the derivative term in the scaled Riccati equation is O(1/A) on compact positive intervals since \(-yg_m'(y)\le g_m(y)\) after consistent scaling. Alternatively the explicit numerator below proves (24) directly. The convergence extends locally uniformly to Re(y)>0 by the positive Stieltjes bound and analytic normal-family uniqueness.

Integration with the integrable bound sqrt(3/(2y)) yields

\[
 \boxed{D_m(y)\longrightarrow
 D(y)=4\int_{\sqrt{2/(3y)}}^\infty
 \frac{dv}{v^2(e^{2v}+1)}>0.}                         \tag{25}
\]

Equivalently \(D(y)=\sqrt{6y}-\int_0^yG_0(v)dv\). Thus at the moving scale t=A_m^2 y the *relative* Laplace error grows like exp(A_m D(y)); compact convergence of L_m has not controlled this region. This is not a statement about a proven height threshold for Mellin zeros.

The hyperbolic function here is related to the tanh normal form and Pareto comparison of #872, but the coordinates and operators are different. Here it arises from the odd-square edge of a finite Jacobi compression; there it arose from conjugating the literal branching linearization. No identification of their spectra is assumed.

## 8. The full complex Mellin limit is eta, including all tails

Define, initially in its absolute convergence strip,

\[
 K_m(q)=\int_0^\infty y^{-q-1}D_m(y)\,dy,
 \qquad \tfrac12<\Re q<2m+1.
 \tag{26}
\]

For any compact subset of Re(q)>1/2, this domain contains the compact set for all sufficiently large m. Then

\[
 \boxed{K_m(q)\longrightarrow
 K_0(q)=\frac8q\left(\frac38\right)^q
 \Gamma(2q-1)\eta(2q-1)}                              \tag{27}
\]

locally uniformly, where \(\eta(s)=(1-2^{1-s})\zeta(s)\).

**Uniform tail proof.** By (11),

\[
 0\le D_m'(y)\le\sqrt{\frac3{2y}}\,
               \phi_m(-1/y)^{-2}.                   \tag{28}
\]

In particular 0<=D_m(y)<=sqrt(6y), paying the entire y-infinity tail for Re(q)>1/2. For any fixed r and m>=2r, each paired factor in (17) is at least (3/4)^2, so

\[
 \phi_m(-1/y)\ge\frac{(3/8)^r}{(2r)!}\,y^{-r}.
\]

Equation (28), integrated at zero, bounds D_m by a fixed constant times y^(2r+1/2), uniformly in these m. Taking 2r+1/2 larger than the real parts on the chosen compact pays the entire y-zero tail. Dominated convergence, with the same bounds for logarithmic derivatives in q on smaller compacts, proves local uniform convergence of the holomorphic transforms.

To compute the limit, substitute (25), interchange the absolutely integrable integrals, and use the standard Fermi–Dirac Mellin integral [E2]:

\[
\begin{split}
 \int_0^\infty y^{-q-1}D(y)dy
 &=\frac4q(3/2)^q\int_0^\infty\frac{u^{2q-2}}{e^{2u}+1}\,du\\
 &=\frac8q(3/8)^q\Gamma(2q-1)\eta(2q-1).
\end{split}
\]

Absolute convergence holds throughout Re(q)>1/2. No claim about eta zero locations is used.

### A direct fractional-power quadrature identity

For 1/2<Re(q)<1, integrating each logarithm absolutely gives

\[
 \boxed{K_m(q)=\frac{\pi A_m^{2q-1}}{q\sin\pi q}
 \left[\left(\frac6{\pi^2}\right)^q\zeta(2q)
       -\sum_i k_i x_i^q\right].}                   \tag{29}
\]

Indeed \(\int_0^\infty t^{-q-1}\log(1+at)dt
=\pi a^q/(q\sin\pi q)\). The source series is absolutely summable here. At integers 1,...,2m the apparent singularities cancel by moment matching; analytic continuation within (26) is legitimate. Formula (29) shows exactly how an error in an absolutely convergent spectral zeta sum produces the shifted eta function in its scaling limit. It is not a zero-free estimate for the difference of the two terms.

For example K_0(1)=3 log 2 gives the entropy-type limit

\[
 A_m\left[\sum_i w_i\log x_i-\sum_{j\ge1}\alpha_j\log\alpha_j\right]
 \longrightarrow3\log2.                             \tag{30}
\]

## 9. The first correction and auxiliary complex-zero displacement

The locally uniform limit (27) has the first correction

\[
 \boxed{K_m(q)=K_0(q)+\frac{K_1(q)}{A_m}+o(A_m^{-1}),}
 \tag{31}
\]

locally uniformly in Re(q)>1/2, where

\[
 K_1(q)=\frac{(3/8)^q}{6q}
 \left[\Gamma(2q+2)\eta(2q+1)
             -24\Gamma(2q)\eta(2q-1)\right].         \tag{32}
\]

The following supplies the uniform passage; a pointwise edge expansion alone would not suffice.

Define the numerator edge polynomial by

\[
 \psi_m(z)=\sum_{r=0}^{m}
 \frac{c_{m,r}}{2r+1}
 \left(1-\frac{r(r+3/2)}{A_m}\right)(-z)^r.
\]

The coefficient with r=m vanishes. Reversing (5) gives exactly

\[
 G_m(y)=\frac1y\frac{\psi_m(-1/y)}{\phi_m(-1/y)}.
 \tag{33}
\]

If u=sqrt(2/(3y)), expansion of (17),(18) gives

\[
\begin{split}
 \phi_m(-1/y)&=\cosh u+\frac{-u^2\cosh u/4+(u/2-u^3/12)\sinh u}{A}+O(A^{-2}),\\
 \psi_m(-1/y)&=\sinh u/u
    +\frac{-u\sinh u/4-u^2\cosh u/12}{A}+O(A^{-2}).
\end{split}                                        \tag{34}
\]

The remainders, for arbitrary positive u, are bounded in absolute value by constants times \((u^2+u^{12})\cosh u/A^2\). To see this for the numerator, multiply the second bound in (18) by its extra factor. The first numerator coefficient correction is
\(-r(2r+1)(r+1)/3\), and the coefficient remainder before division by (2r+1) is at most \(5r^6a_r/A^2\). Summing the full even exponential series proves the stated bound. The denominator has the smaller constant 2 from (18).

On 0<u<=U=A^delta, for delta sufficiently small, the denominator is at least half cosh u, and (33) has a uniform remainder bounded by C u^2(1+u^12)/A^2. In particular

\[
 G_m(y)=\frac32u\tanh u+
 \frac{-3u^2\tanh^2u/4-u^4\operatorname{sech}^2u/8}{A}
 +O\left(\frac{u^2(1+u^{12})}{A^2}\right).
\]

The scaled native resolvent is exactly

\[
 A g(A^2y)=\frac32u\coth(2A/u)-\frac{3u^2}{4A}.
\]

The coth correction to one on this interval is exponentially small in A/U. Therefore the coefficient of 1/A in D_m'(y) is

\[
 \frac{u^2(u^2-6)}8\operatorname{sech}^2u.           \tag{35}
\]

For the omitted interval u>=U, take r=floor(U/8). For large A, m>=2r, and the coefficient lower bound used above implies

\[
 \phi_m(-1/y)\ge\frac{(3u/4)^{2r}}{(2r)!}
                  \ge (3u/(8r))^{2r}.
\]

Consequently (28) bounds its complete Mellin tail by a polynomial in U times 3^(-4r), including after multiplication by A. The limiting and first-correction tails have ordinary exponential bounds. On 0<u<=U the integrated remainder, after multiplying by A, is at most a constant times \(U^{2B+12}/A\), where B bounds Re(q) on the compact in question. Choose \(0<\delta<\min(1/3,1/(2B+12))\). Every omitted term tends to zero uniformly. This proves the claimed first-order Mellin expansion, not an O(A^-2) Mellin remainder.

Finally integration by parts in (26), followed by (35), gives

\[
 K_1(q)=\frac{(3/2)^q}{6q}
 \int_0^\infty (u^{2q+1}-6u^{2q-1})\operatorname{sech}^2u\,du.
\]

The identity \(\int_0^\infty u^{v-1}\operatorname{sech}^2u\,du
=2^{2-v}\Gamma(v)\eta(v-1)\) for Re(v)>1 follows by integrating the Fermi–Dirac kernel by parts. This proves (32) throughout the claimed domain.

### A source-only first correction using right-half-plane data

Write s=2q-1 and

\[
 C(q)=\frac8q(3/8)^q\Gamma(2q-1),\qquad
 E_m(s)=K_m((s+1)/2)/C((s+1)/2).
\]

Then locally uniformly for Re(s)>0,

\[
 \boxed{E_m(s)=\eta(s)+\frac1{A_m}
 \left[-\frac s2\eta(s)+\frac{s(s+1)(s+2)}{48}\eta(s+2)\right]
 +o(A_m^{-1}).}                                     \tag{36}
\]

Within 0<Re(s)<1, (29) evaluates E_m using only the absolutely convergent zeta(s+1) and finite positive Gaussian data. The correction

\[
 \widetilde E_m(s)=
 \frac{E_m(s)-s(s+1)(s+2)\eta(s+2)/(48A_m)}{1-s/(2A_m)}
 =\eta(s)+o(A_m^{-1})                                \tag{37}
\]

also uses only right-half-plane zeta data, because eta(s+2) has Re(s+2)>2. The displayed denominator does not vanish in the critical strip. This is an analytic approximation theorem, not a new numerical verification record or a zero-free theorem.

If rho is a **simple** eta zero with Re(rho)>0, Rouche and (36) give a unique nearby zero rho_m of E_m, and

\[
 \boxed{\rho_m=\rho-
 \frac{\rho(\rho+1)(\rho+2)}{48A_m}
 \frac{\eta(\rho+2)}{\eta'(\rho)}+o(A_m^{-1}).}        \tag{38}
\]

For a nontrivial zeta zero the numerator eta(rho+2) is nonzero by the absolutely convergent Euler product and the nonvanishing dyadic factor there. Thus the complex displacement coefficient is nonzero. **No sign of its real part is asserted.** The formula is conditional on simplicity of that particular zero and neither proves all zeros simple nor assumes RH. For multiple zeros, (27) still matches total multiplicity in sufficiently small disks; (38) is not applicable.

These are zeros of an **auxiliary quadrature-error transform**, not a newly certified collection of native xi zeros.

### Restore the functional reflection before asking for global confinement

The unreflected auxiliary functions need not have their finite-stage zeros exactly on the critical line. Removing the first correction is not the same as restoring the functional equation. A prescribed reflection-respecting construction is available: set, only in 0<Re(s)<1,

\[
 \mathcal C(s)=\frac{s(s-1)}2\pi^{-s/2}
                 \frac{\Gamma(s/2)}{1-2^{1-s}},\qquad
 \widehat H_m(s)=\frac{\mathcal C(s)\widetilde E_m(s)
                   +\mathcal C(1-s)\widetilde E_m(1-s)}2.
 \tag{38a}
\]

The prefactors are holomorphic and nonzero on this open strip, and the exact completed-zeta functional equation gives

\[
 \widehat H_m(1-s)=\widehat H_m(s),\qquad
 \widehat H_m(\bar s)=\overline{\widehat H_m(s)},\qquad
 \widehat H_m(s)=\xi(s)+o(A_m^{-1})
 \tag{38b}
\]

locally uniformly there. Its defining data still consist of finite Gaussian quadrature and absolutely convergent series: zeta(s+1), zeta(2-s), eta(s+2) and eta(3-s). This is not claimed to be a probability Mellin transform or an entire function at each finite stage; poles outside the named strip have not been discarded.

At a fixed simple critical-line xi zero, Rouche supplies one nearby zero of the corrected reflected family for all sufficiently large m. Reflection fixes that unique zero to the line exactly, and its displacement is o(A_m^-1). This is a conditional local theorem, not a computed certificate, a claim that all xi zeros are simple, or an all-height statement. Off-line xi zeros, were there any, would also be tracked by this convergence.

## 10. Where the attempted end-to-end proof stops

The proposed programme was to connect the positive complete defect to a tractable high-order transition model and establish the missing zero-confinement sign there. Sections 6–9 identify that model exactly and control the full Mellin passage. The result is not an arithmetic-free comparison: its Mellin transform is eta(2q-1), and its first correction contains eta(2q+1).

In the open strip 1/2<Re(q)<1, the gamma, q, and scale factors in (27) are nonzero. The dyadic factor in eta has no zeros there either. Therefore

\[
 K_0(q)\ne0\quad\text{for }1/2<\Re q<1,\ \Re q\ne3/4
 \tag{39}
\]

is **equivalent to RH**, not a consequence of the real positivity of D. The additional dyadic zeros lie on Re(q)=1 and cannot be deleted without their explicit factor. No proof of (39) is supplied.

A valid cofinal zero-free theorem for the corrected **reflected** functions (38a) in the two open half-strips would imply RH by their locally uniform convergence. It is not established here. Demanding exact centrality from the unreflected functions (37) is an unnecessarily stronger target and may be false; the zero displacement (38) makes that risk explicit. Nor does the common positive thin tail (12), its variance tending to zero, or the summable compact error (6) show that the weighted defect from #862 tends to zero. All are compatible with local convergence to whatever zeros the actual xi function has.

Thus the completed proposed results are exact source structure, independent positive tail removal, a quantified complex edge limit, a full eta-valued Mellin limit and first correction, and auxiliary zero displacement. **The net signed zero-production estimate / all-height confinement remains unproved.** The new connection is useful precisely because it prevents treating the transition as already solved by elementary positivity.

## 11. Validation and sources

`check.py` reconstructs the source moments from sinh, independently constructs the finite continuants, and checks the complete rational Riccati identity, Gaussian matching, adjacent continuant identity, exact norms and shape, minimal-shape dual, thin-tail traces, and coefficient bounds through order 24. Exact LDL inertia isolates the first three positive Jacobi nodes at each of orders 8, 32 and 64, with all real-axis complements inside their initial brackets accounted for. Those are not xi-zero certificates. All arithmetic in this checker is rational standard-library Python.

`diagnostic.py` is a separate nondirected mpmath calculation of the fractional-power error and its first correction. Its output is a consistency check, not an interval certificate or a premise for the proofs. The general identities, infinite-tail estimates and limiting theorems above require independent mathematical review. No Lean build or whole-repository validation was run.

Frozen repository sources and their reading scope are in `SOURCES.json`. The principal source #851 is locally retained from the conversation and authenticated against its live Git blob. The principal proofs of #862, #872 and #876 were read in the relevant sections; #874's result was inspected at metadata/description level. The inherited main baseline and recent programme/PR descriptions informed scope, not the all-order proofs here. This was not a fresh full-main or full-history audit.

External classical sources:

- [E1] NIST DLMF 4.39.1, Lambert continued fraction for tanh; inspected HTML and displayed formula. `https://dlmf.nist.gov/4.39`
- [E2] NIST DLMF 25.5.3–25.5.4, Fermi–Dirac Mellin integrals; inspected HTML and formulae. `https://dlmf.nist.gov/25.5`
- [E3] Biane, Pitman, Yor, *Probability laws related to the Jacobi theta and Riemann zeta function and Brownian excursions*, arXiv:math/9912170. Fresh abstract/metadata read; the normalization (1) is retained from the source packet and is not newly claimed. `https://arxiv.org/abs/math/9912170`

No repository publication is claimed by this local manuscript. See `PUBLICATION.md`.
