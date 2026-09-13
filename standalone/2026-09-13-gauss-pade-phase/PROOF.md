# GPP26 — exact Padé phase, compensated spectral trace, and a second eta correction

Date: 2026-09-13. **Proposed component proofs, requiring independent mathematical review. RH is not proved.**

This is an additive continuation of GHE26, PR #877 at
`ec60ea46318143e9a7908aab3239fbdb327045df`. It preserves the actual Gauss–Thorin source. It does not change the predecessor, main, canonical status, or another contributor's branch. The new phase is a phase of a rational approximation in the **Laplace-frequency coordinate**, not the argument of xi in its spectral coordinate.

The contribution has three parts. First, the Gaussian nodes are phase crossings of an explicit diagonal Padé approximant, and the gamma shapes are their reciprocal phase slopes. Second, that identity supplies an exact, endpoint-compensated Poisson trace formula for the complete complex Mellin error. Third, a second-order expansion gives the next shifted-eta correction with a full-tail little-o remainder. None supplies the missing global zero-confinement sign.

Classical ingredients include diagonal Padé approximation, Bessel/Lommel polynomials, Gaussian quadrature, the Poisson approximate identity, and the Fermi–Dirac integral. These mechanisms are not claimed new. The statements below give their source-specific composition and the additional second-order formula. No exhaustive novelty search or independent analytic review has been performed.

## 1. Exact source, coordinates, and inherited input

Let

\[
 \alpha_j=6/(\pi^2j^2),\qquad
 L_*(t)=\frac{\sqrt{6t}}{\sinh\sqrt{6t}},\qquad
 g(t)=-L_*'(t)/L_*(t)=\sum_{j\ge1}\frac{\alpha_j}{1+\alpha_jt}.
 \tag{1}
\]

The probability measure \(\nu=\sum_j\alpha_j\delta_{\alpha_j}\) has total mass one. Its m-node Gaussian quadrature has nodes \(x_i>0\), weights \(w_i>0\), and gamma shapes \(k_i=w_i/x_i\). Define

\[
 L_m(t)=\prod_i(1+x_it)^{-k_i},\quad
 g_m(t)=\sum_i\frac{w_i}{1+x_it}=Q_m(t)/P_m(t),\quad
 P_m(t)=\prod_i(1+x_it).
 \tag{2}
\]

Here and below m>=1. Put \(A=m(2m+3)/2\), \(n=2m+1\). The predecessor derives the exact continuants

\[
 P_0=1,\ P_1=1+2t/5,\quad Q_0=0,\ Q_1=1,
\]
\[
 Y_{m+1}=(1+b_mt)Y_m-\lambda_mt^2Y_{m-1},\quad
 b_m=\frac{12}{(4m+1)(4m+5)},\quad
 \lambda_m=\frac{36}{(4m-1)(4m+1)^2(4m+3)}.
 \tag{3}
\]

In particular \(\sum_i k_i=A\), and the first 2m cumulants of the finite and infinite gamma sources agree. The exact square residual from GHE26 gives

\[
 0\le g(t)-g_m(t)\le\frac3{\sqrt{6t}}
   \left(\frac{(\prod_i x_i)t^m}{P_m(t)}\right)^2,
 \qquad t>0.                                             \tag{4}
\]

Our full-tail expansion uses (4), not a numerical extrapolation. The source identification with xi is the classical Biane–Pitman–Yor identity in the predecessor. The new phase and trace identities themselves only need (1)–(3).

For later use define

\[
 D_m(y)=A^{-1}\log[L_m(A^2y)/L_*(A^2y)],\quad
 K_m(q)=\int_0^\infty y^{-q-1}D_m(y)\,dy,
 \quad\tfrac12<\Re q<n.                                \tag{5}
\]

The eta coordinate of this error transform is **s=2q-1**. This is not the Brownian source's original moment coordinate s/2. Positive real powers use real logarithms throughout.

The predecessor's exact fractional-power formula, initially for 1/2<Re(q)<1 and then by analytic continuation with removable integer values, is

\[
 K_m(q)=\frac{\pi A^{2q-1}}{q\sin\pi q}
 \left[(6/\pi^2)^q\zeta(2q)-\sum_i k_ix_i^q\right].       \tag{6}
\]

One direct derivation integrates \(\log(1+by)\) against \(y^{-q-1}\), where its integral is \(\pi b^q/(q\sin\pi q)\), and sums the absolutely convergent infinite source for Re(q)>1/2. The common first 2m cumulants remove the apparent poles at q=1,...,2m. Equation (4) pays the small-y remainder beyond that initial strip.

## 2. The exact Padé realization

Define the polynomial

\[
 \Pi_n(r)=\sum_{j=0}^n
 \frac{(2n-j)!\,n!\,2^j}{(2n)!\,(n-j)!\,j!}\,r^j,
 \qquad a_n=[r^n]\Pi_n(r)=\frac1{(2n-1)!!}.              \tag{7}
\]

This is the diagonal Padé numerator for exp(2r): its defining coefficient identity is
\(\Pi_n(r)-e^{2r}\Pi_n(-r)=O(r^{2n+1})\). It follows either by expanding the exponential and the finite sum or by the usual diagonal Padé construction. We will not use an unproved assertion about the roots of a Padé denominator.

For n=2m+1, the exact source-specific relation is

\[
 \boxed{\Pi_{2m+1}(r)=(1+r)P_m(r^2/6)
                         +\frac{r^2}{3}Q_m(r^2/6).}     \tag{8}
\]

For example \(\Pi_3(r)=1+r+2r^2/5+r^3/15\). To prove (8), separate even and odd coefficients in (7) and compare to the explicit continuant coefficients in GHE26 equations (4)–(5), or substitute those coefficients into (3). Both are finite coefficient identities at every m. In particular the odd part is exactly \(rP_m(r^2/6)\).

Consequently the rational coth approximation is

\[
 \mathsf C_n(r)=\frac{\Pi_n(r)+\Pi_n(-r)}{\Pi_n(r)-\Pi_n(-r)},
 \qquad g_m(r^2/6)=\frac3{r^2}\bigl(r\mathsf C_n(r)-1\bigr).
 \tag{9}
\]

This connects the predecessor's positive Stieltjes compression to the classical Padé/Bessel delay construction. The general connection between Padé delay approximants and Bessel polynomials is prior work [E1]; the normalization and gamma-shape identity below are derived here.

## 3. A globally monotone phase and its exact slope

For real omega>=0 set

\[
 B_n(\omega)=|\Pi_n(i\omega)|^2.
\]

It is a positive polynomial in omega squared:

\[
 B_n(\omega)=\sum_{j=0}^n c_{n,j}\omega^{2j},\quad
 c_{n,0}=1,\quad c_{n,n}=a_n^2,
\]
\[
 \boxed{\frac{c_{n,j}}{c_{n,j-1}}=
 \frac{2(n-j+1)}{j(2n-2j+1)(2n-j+1)}>0.}                 \tag{10}
\]

Here is an all-order derivation. The coefficients in (7) satisfy

\[
 r\Pi_n''-2(n+r)\Pi_n'+2n\Pi_n=0.
\]

If f=exp(-r)Pi_n(r), then f''-(2n/r)f'-f=0; both f(r) and f(-r) solve it. Their product \(U(r)=\Pi_n(r)\Pi_n(-r)\) therefore satisfies the symmetric-square equation

\[
 r^2U'''-6nrU''+(8n^2+2n-4r^2)U'+8nrU=0.
\]

The coefficient of r^(2j-1) gives (10) after r=i omega. The endpoint coefficient follows from (7). Thus Pi_n has no zero on the imaginary axis.

Let \(\vartheta_n(\omega)\) be its continuous unwrapped argument, with theta_n(0)=0. The exact Wronskian identity is

\[
 \Pi_n'(r)\Pi_n(-r)+\Pi_n(r)\Pi_n'(-r)
 =2\left[U(r)-(-1)^na_n^2r^{2n}\right].                \tag{11}
\]

Indeed the ODE implies that the derivative of the left side minus 2U is 2n/r times that difference; the leading coefficient fixes its constant. Taking real parts of Pi_n'(i omega)/Pi_n(i omega) proves

\[
 \boxed{\vartheta_n'(\omega)
 =1-\frac{a_n^2\omega^{2n}}{B_n(\omega)},\qquad
 0<\vartheta_n'(\omega)<1\quad(\omega>0).}             \tag{12}
\]

Also theta_n'(0)=1. This controls this phase at **every real frequency**, not just a bounded set.

Let the positive zeros of \(P_m(-\omega^2/6)\) be ordered
\(\omega_{m,1}<\cdots<\omega_{m,m}\). Gaussian positivity gives exactly m simple positive zeros. By (8), these are the positive zeros of Im Pi_n(i omega). Strict monotonicity, starting at zero, forces

\[
 \vartheta_n(\omega_{m,j})=j\pi,\qquad
 \lim_{\omega\to\infty}\vartheta_n(\omega)=(m+1/2)\pi.
 \tag{13}
\]

For the limit, the phase derivative is integrable at infinity by (10). After its mth crossing it can have no further integer-pi crossing, whereas the leading odd power in (7) forces the terminal angle to be the indicated half-integer. This avoids importing Hurwitz stability as a premise.

### The gamma shapes are reciprocal phase slopes

Order the Gaussian nodes decreasingly here, so \(x_{m,j}=6/\omega_{m,j}^2\). On r=i omega, (9) reads

\[
 g_m(-\omega^2/6)=-\frac3{\omega^2}
           [\omega\cot\vartheta_n(\omega)-1].
\]

At omega=omega_(m,j), its residue in t=-omega^2/6 is \(1/\vartheta_n'(\omega_{m,j})\). On the other hand the residue of k_i/(t+1/x_i) is k_i. Therefore

\[
 \boxed{x_{m,j}=\frac6{\omega_{m,j}^2},\qquad
        k_{m,j}=\frac1{\vartheta_n'(\omega_{m,j})}>1.}    \tag{14}
\]

This is an exact identity, not a fit to node locations. For the conventional rational delay response Pi_n(-i omega)/Pi_n(i omega), the group delay is 2 theta_n'; thus k=2/(group delay), not 1/(group delay). The factor two must be retained.

### A quantitative bulk window

Equations (10)–(12) immediately give, for every R>0 and 0<=omega<=R,

\[
 0\le\omega-\vartheta_n(\omega)
 \le \frac{a_n^2\omega^{2n+1}}{2n+1},\quad
 1-a_n^2R^{2n}\le\vartheta_n'(\omega)\le1.              \tag{15}
\]

There is a useful growing window with exponentially small phase error. Concavity of log, applied on each unit interval, gives
\(\log( (2n-1)!! )\ge\int_0^n\log(2x)dx=n\log(2n)-n\).
Since e<3, for R=n/2,

\[
 \boxed{1-\vartheta_n'(\omega)\le(3/4)^{2n},\qquad
 0\le\omega-\vartheta_n(\omega)
 \le\frac{n}{2(2n+1)}(3/4)^{2n},\quad0\le\omega\le n/2.}
 \tag{16}
\]

If \(j\pi+\delta\le R\), where \(\delta=a_n^2R^{2n+1}/(2n+1)\), then

\[
 j\pi<\omega_{m,j}\le j\pi+\delta,\qquad
 1<k_{m,j}\le(1-a_n^2R^{2n})^{-1}
 \tag{17}
\]

whenever the denominator is positive. Existence of the jth crossing in that interval follows directly by the intermediate value theorem; it need not be assumed separately. These are bulk **quadrature** bounds, not a growing window of Riemann-zero verification.

## 4. A complete complex Poisson trace identity

Set

\[
 \mathcal T_m(q)=\pi^{-2q}\zeta(2q)
       -\sum_{j=1}^m\frac{\omega_{m,j}^{-2q}}
                            {\vartheta_n'(\omega_{m,j})},
 \quad\Re q>1/2.
 \tag{18}
\]

For 0<a<1 let the period-pi Poisson kernel be

\[
 \mathcal P_a(v)=\frac{1-a^2}{1-2a\cos(2v)+a^2}
 =\frac{1-a^2}{(1-a)^2+4a\sin^2v}.
\]

Then, locally uniformly for \(1/2<\Re q<n\),

\[
 \boxed{\mathcal T_m(q)=\lim_{a\uparrow1}\frac1\pi
 \int_0^\infty \omega^{-2q}
 [\mathcal P_a(\omega)-\mathcal P_a(\vartheta_n(\omega))]d\omega.}
 \tag{19}
\]

This is a complete identity at arbitrary imaginary height. It is not a useful lower bound for its modulus. The bracket must be taken **before** integration: the two separate origin integrals would diverge for the stated exponents.

There is no need to evaluate an unwrapped phase to compute the second kernel. If
\(I_m(\omega)=\omega P_m(-\omega^2/6)\), then exactly

\[
 \mathcal P_a(\vartheta_n(\omega))
 =\frac{(1-a^2)B_n(\omega)}{(1-a)^2B_n(\omega)+4aI_m(\omega)^2}.
 \tag{20}
\]

Thus (19) compares a trigonometric kernel and a completely explicit rational kernel.

**Proof with both tails.** On a compact interval separated from zero and from any endpoint crossing, the Poisson approximate identity gives delta mass pi at each integer-pi crossing. Changing variable v=theta_n(omega) gives reciprocal Jacobian 1/theta_n', so the two limits give precisely the native and finite sums. This step uses no zero of zeta.

It remains to justify the singular origin and the infinite tail. Fix m and a compact exponent set with 1/2<sigma_min<=Re(q)<=sigma_max<n. Let epsilon=1-a and restrict a>=1/2. For a sufficiently small fixed delta, (15) gives theta_n(omega)>=omega/2 on [0,delta]. The derivative of the Poisson kernel there is bounded by C epsilon omega/(epsilon^2+omega^2)^2. Therefore

\[
 |\mathcal P_a(\omega)-\mathcal P_a(\vartheta_n(\omega))|
 \le C_m\frac{\epsilon\,\omega^{2n+2}}
                    {(\epsilon^2+\omega^2)^2},\quad0<\omega<\delta.
 \tag{21}
\]

After multiplying by omega^(-2 Re(q)), the integral on (0,epsilon) is O(epsilon^(2n-2sigma_max)). The integral on (epsilon,delta) is bounded by
\(C\epsilon\int_\epsilon^\delta\omega^{2n-2-2\sigma_{max}}d\omega\).
It tends to zero, including its logarithmic borderline case, because sigma_max<n. This pays the whole compensated origin, rather than canceling two divergent delta masses informally.

At infinity, the integral of P_a over any full period is pi, independently of a. Splitting into periods bounds the native weighted tail by a constant times \(\sum_{j\ge R/\pi-1}j^{-2\sigma_{min}}\), which tends to zero uniformly in a. For the finite phase, (13) puts theta_n(omega) a fixed positive distance from pi Z once omega is sufficiently large. There P_a(theta_n)<=C_m(1-a), and the remaining integral is bounded by C_m R^(1-2sigma_min), uniformly in a. This pays the complete second tail. The same majorants establish local uniform convergence in q; alternatively first use compact uniformity without q derivatives and then holomorphy. QED.

Combining (6),(14),(18) gives

\[
 \boxed{K_m(q)=\frac{\pi6^qA^{2q-1}}{q\sin\pi q}
                       \mathcal T_m(q).}                \tag{22}
\]

In particular the source moment identities become exact phase-compensated sum rules

\[
 \sum_{j=1}^m\frac{\omega_{m,j}^{-2r}}
                    {\vartheta_n'(\omega_{m,j})}
 =\pi^{-2r}\zeta(2r),\qquad r=1,\ldots,2m.              \tag{23}
\]

They are ordinary Gaussian moment matching in new coordinates, not new special values of zeta.

### Why monotone phase does not finish the Mellin argument

For every m>=1 and every a in (0,1), the bracket in (19) takes both signs. At omega=pi, theta_n(pi) is strictly between zero and pi, so the bracket is positive. The first finite crossing obeys
\(\pi<\omega_{m,1}\le\sqrt{15}<2\pi\): the upper bound follows because the largest eigenvalue of the m-by-m Jacobi compression is at least its first diagonal entry 2/5. At omega=omega_(m,1), the finite Poisson kernel has its maximum and the native one does not, so the bracket is negative.

Thus (12) supplies genuine global phase control but does **not** turn the compensated Mellin trace into an integral of fixed sign. Taking absolute values separately also loses the origin compensation. No positivity of the required complex zero-excluding expression follows from (19).

## 5. A second-order expansion with complete coefficient remainders

We now compute what the trace does at the hard edge, retaining one more order than GHE26. Put \(u=\sqrt{2/(3y)}\). The exact edge products are

\[
 \phi_m(z)=\sum_{r=0}^m\frac{(-2z/3)^r}{(2r)!}C_{m,r},
\]
\[
 C_{m,r}=\prod_{j=0}^{r-1}
 (1-j(j+3/2)/A)(1-(j-1/2)(j+1)/A),
\]
\[
 \psi_m(z)=\sum_{r=0}^m\frac{(-2z/3)^r}{(2r+1)!}
       C_{m,r}(1-r(r+3/2)/A),\quad
 A g_m(A^2y)=\frac1y\frac{\psi_m(-1/y)}{\phi_m(-1/y)}.
 \tag{24}
\]

Set C_(m,r)=0 beyond m, and define

\[
 p_1(r)=-r(4r^2-7)/6,
\]
\[
 p_2(r)=\frac{r(r-1)(2r-1)(40r^3+24r^2-124r-123)}{360},
\]
\[
 n_1(r)=-r(r+1)(2r+1)/3,
\]
\[
 n_2(r)=\frac{r(r+1)(2r+1)(40r^3+24r^2-16r-123)}{360}.
 \tag{25}
\]

For every r>=1 and m>=1, complete coefficient bounds are

\[
 |C_{m,r}-1-p_1(r)/A-p_2(r)/A^2|\le 4r^9/A^3,
\]
\[
 |C_{m,r}(1-r(r+3/2)/A)-1-n_1(r)/A-n_2(r)/A^2|
 \le16r^9/A^3.                                         \tag{26}
\]

For the second expression, the first term is zero for r>m. The r=0 coefficients are exact.

**Proof.** For r<=m, separate the single factor 1+1/(2A) and write the others as product(1-u_j), with 0<=u_j<=1. Put
\(S_r=(4r^3-7r+3)/6\), so sum u_j=S_r/A. The Bonferroni inequality gives the remainder after its quadratic elementary-symmetric expansion bounded by (sum u_j)^3/6. Multiplication by 1+1/(2A) gives p1=1/2-S_r and p2 equal to the unscaled second elementary sum minus S_r/2. Summing the polynomial factors gives (25). The bounds S_r<=r^3 and |p2|<=r^6 imply the first inequality with the stated conservative constant.

Multiply by 1-r(r+3/2)/A, which is in [0,1] for r<=m. Its first two coefficients are n1=p1-r(r+3/2) and n2=p2-r(r+3/2)p1, and its cubic cross-term is bounded by (5/2)r^8/A^3. This proves the second bound with room to spare. For r>m, A<r^2. Each of 1, r^3/A and r^6/A^2 is at most r^9/A^3, with the indicated polynomial coefficient constants. This also proves the complete omitted coefficient tail. QED.

Applying the Euler operator (u/2)d/du to cosh u and sinh(u)/u sums these coefficients. Write
\(\phi_m(-1/y)=D_0+D_1/A+D_2/A^2+\cdots\) and
\(\psi_m(-1/y)=N_0+N_1/A+N_2/A^2+\cdots\). Then

\[
 D_0=\cosh u,\quad N_0=\sinh u/u,
\]
\[
 D_1=-u^3\sinh u/12-u^2\cosh u/4+u\sinh u/2,
\quad N_1=-u^2\cosh u/12-u\sinh u/4,
\]
\[
 D_2=u^6\cosh u/288+11u^5\sinh u/240
                +11u^4\cosh u/96-u^3\sinh u/12,
\]
\[
 N_2=u^5\sinh u/288+11u^4\cosh u/240+5u^3\sinh u/32
                       +u^2\cosh u/24-u\sinh u/4.
 \tag{27}
\]

The quotient's second coefficient is

\[
 \boxed{G_2(u)=\frac{u^3}{480\cosh^3u}
 [-5u^4\sinh u+18u^3\cosh u+60u^2\sinh u
                         +30u\cosh u-180\sinh u].}       \tag{28}
\]

This follows by inserting (27) into
\((3u^2/2)[N_2/D_0-N_1D_1/D_0^2+N_0D_1^2/D_0^3-N_0D_2/D_0^2]\).
It can be verified as a finite hyperbolic-polynomial identity, without numerical differentiation.

### The passage through the entire Mellin integral

Let a compact set satisfy 1/2<Re(q)<=B. Bounds (26), summed against the complete exponential series, bound the denominator and numerator remainders by C(1+u^18)cosh(u)/A^3. The first-order bound gives relative denominator error at most C(1+u^3)/A. On 0<u<=U=A^delta, for sufficiently small positive delta, the denominator is therefore at least cosh(u)/2. Quotient expansion through second order has the conservative uniform remainder

\[
 \left|A g_m(A^2y)-G_0(u)-G_1(u)/A-G_2(u)/A^2\right|
 \le C u^2(1+u^{30})/A^3,                              \tag{29}
\]

where \(G_0=3u\tanh u/2\) and
\(G_1=-3u^2\tanh^2u/4-u^4\operatorname{sech}^2u/8\).
The constants can be chosen independent of m,u on this range; their existence follows from the finite-degree Euler polynomials and the stated denominator lower bound. They are not evaluated practical error constants.

The scaled native resolvent is exactly
\(A g(A^2y)=3u\coth(2A/u)/2-3u^2/(4A)\).
Its additional coth term is exponentially small in A/U. After integration by parts in (5), the Mellin measure is
\((4/(3q))(3/2)^q u^{2q-3}du\).
Thus the integrated remainder on (0,U), multiplied by A^2, is bounded by C U^(2B+30)/A plus an exponentially small term.

The complementary interval is paid by the **complete positive error**, not by extending (29) past its range. Take r=floor(U/8). For sufficiently large m, m>=2r. Every paired factor in (24) up to this r is at least (3/4)^2, so

\[
 \phi_m(-1/y)\ge\frac{(3u/4)^{2r}}{(2r)!}
                         \ge(3u/(8r))^{2r}.
\]

Equation (4) gives \(0\le D_m'(y)\le(3u/2)\phi_m(-1/y)^{-2}\). Its whole Mellin tail u>=U is bounded by a polynomial in U times 3^(-4r); it still tends to zero after multiplication by A^2. The complete limiting, first-, and second-correction tails have exponential bounds, since they involve 1-tanh u or sech-squared factors times polynomials.

Choose
\(0<\delta<\min(1/3,1/(2B+30))\).
All errors tend to zero uniformly on the chosen compact. Therefore

\[
 \boxed{K_m(q)=K_0(q)+K_1(q)/A+K_2(q)/A^2+o(A^{-2})}
 \tag{30}
\]

locally uniformly in Re(q)>1/2, as the finite-stage domains exhaust that half-plane. This proves a full-tail **little-o(A^-2)** remainder. No globally uniform O(A^-3) Mellin estimate is claimed.

## 6. Evaluation: the second correction involves eta two and four units to the right

Let
\(I_v=\int_0^\infty u^v\operatorname{sech}^2u\,du
      =2^{1-v}\Gamma(v+1)\eta(v)\), for Re(v)>0.
The last equality follows by integration by parts in the classical Fermi–Dirac integral [E3]. Integration of (28), using
\(\tanh u\operatorname{sech}^2u=-(\operatorname{sech}^2u)'/2\), yields

\[
 K_2(q)=\frac{(3/2)^q}{360q}
 [(5q-8)I_{2q+3}-(60q+90)I_{2q+1}+180qI_{2q-1}].        \tag{31}
\]

The boundary terms vanish for the stated domain. Put s=2q-1,
\(C(q)=8(3/8)^q\Gamma(2q-1)/q\), and \(E_m(s)=K_m(q)/C(q)\).
With the rising factorial \((s)_r=s(s+1)\cdots(s+r-1)\), the result is

\[
 \boxed{\begin{aligned}
 E_m(s)={}&\eta(s)
 +\frac1A\left[-\frac s2\eta(s)+\frac{(s)_3}{48}\eta(s+2)\right]\\
 &+\frac1{A^2}\left[
 \frac{s(s+1)}8\eta(s)
 -\frac{(s)_3(s+4)}{96}\eta(s+2)
 +\frac{(5s-11)(s)_5}{23040}\eta(s+4)\right]
 +o(A^{-2}).
 \end{aligned}}                                      \tag{32}
\]

The first-order terms reproduce GHE26. The displayed second-order terms are the new correction. The scalar eta(s) coefficients agree through this order with (1+1/(2A))^(-s); this observation is not promoted to an exact all-order law.

### A corrected approximation using only right-half-plane series

Set

\[
 d_A(s)=1-\frac s{2A}+\frac{s(s+1)}{8A^2},
\]
\[
 b_A(s)=\frac{(s)_3}{48A}-\frac{(s)_3(s+4)}{96A^2},\quad
 c_A(s)=\frac{(5s-11)(s)_5}{23040A^2}.
\]

Then

\[
 \boxed{E_m^{[2]}(s)=\frac{E_m(s)-b_A(s)\eta(s+2)-c_A(s)\eta(s+4)}{d_A(s)}
       =\eta(s)+o(A^{-2}).}                            \tag{33}
\]

The two roots of d_A have real part 2A-1/2>=9/2: their discriminant is 1-8A-16A^2<0. Thus this denominator has no zero in the critical strip. There E_m is evaluated from finite Gaussian data and the absolutely convergent zeta(s+1); the two correction series have real parts >2 and >4 respectively. This is a prescribed analytic approximation, not a call to the target eta(s) in its critical strip.

Restore reflection with

\[
 \mathcal C(s)=\frac{s(s-1)}2\pi^{-s/2}
                  \frac{\Gamma(s/2)}{1-2^{1-s}},\quad
 H_m^{[2]}(s)=\frac{\mathcal C(s)E_m^{[2]}(s)
                       +\mathcal C(1-s)E_m^{[2]}(1-s)}2.
\]

These are holomorphic on 0<Re(s)<1, respect both conjugation and s->1-s, and satisfy

\[
 H_m^{[2]}(s)=\xi(s)+o(A^{-2})                           \tag{34}
\]

locally uniformly there. They are not asserted entire outside that strip or probability transforms at finite m.

At any fixed xi zero rho of multiplicity h in the open strip, a sufficiently small fixed disk contains exactly h approximant zeros for all sufficiently large m. All lie at distance o(A^(-2/h)) from rho. Indeed xi(s)=(s-rho)^h g(s) with |g| bounded below on a small disk, and the uniform error in (34), followed by Rouche on a suitable shrinking circle, gives the bound and count. No simplicity assumption is needed for this cluster statement. At a **simple critical-line** zero, uniqueness and reflection imply exact centrality of the approximant zero. At a multiple zero, reflection alone does not prevent noncentral splitting. A hypothetical noncentral xi zero would also be faithfully tracked; none is asserted to exist.

## 7. The attempted completion and its exact unresolved boundary

The attempted finish was to convert the source's rational positivity into global Mellin zero control via its Padé phase. Equations (12) and (14) establish a genuine all-frequency phase theorem and identify the gamma weights exactly. Equation (19) transfers it to the correct complete spectral trace, retaining the singular origin and both tails. It does **not** turn that trace into a one-sign kernel: the two explicit opposite-sign points above rule out that immediate step at every order.

The second-order correction removes an explicit finite-order bias. It is stronger approximation, not a replacement for a zero-location theorem. In the eta limit, nonvanishing of K_0(q) off Re(q)=3/4 within 1/2<Re(q)<1 is RH itself; the nonzero gamma and dyadic factors have to be retained. We have not proved this nonvanishing.

A sufficient endpoint remains an unbounded sequence m_j with growing height windows and shrinking off-central allowances in which every zero of H_(m_j)^[2] is confined. Alternatively one may allow finite exceptions and prove their complete weighted cost tends to zero, as in the separately proposed #862/#881 programmes. Neither a vanishing cost nor a cofinal confinement theorem follows from this packet. In particular the phase variable omega of Pi_n is not the imaginary part of an xi zero, and the monotone theta_n cannot be substituted into #881's metric-energy inequality as a spectral symmetrizer.

The actual new proposed results are (8), (12)–(22), the full-tail second-order expansion (30)–(33), and their precisely local zero-cluster consequence. They require analytic review. The finite checker validates bounded algebraic instances and explicit rational inequalities only; it does not prove RH, the Abel limit, or the all-order asymptotic by machine.

## 8. Sources and inspection boundary

- [R1] GHE26, PR #877, frozen head `ec60ea46318143e9a7908aab3239fbdb327045df`, `standalone/2026-09-12-gauss-hard-edge-eta/PROOF.md`. Full local supplied manuscript read; live source fetched. Definitions, exact edge coefficients, positive complete source bound, and first-order Mellin theorem are inherited/rederived as identified above. Its whole test campaign was not rerun this turn.
- [R2] GZC26, PR #851, head `57726ef9b3bf90561df5a361e3b01169c892a62a`. Existing raw-seed offcentral and reflected local-zero results are context, not new zero computations or premises of (12)/(19). Local uploaded checker inspected, no new directed replay.
- [R3] PR #881, head `ab663f7d8020a62e1d8eedaf7d963d0eca3efe50`, full `standalone/2026-09-12-similarity-energy/PROOF.md` read. It proposes full nonlocal energy upper bounds for the actual defect, retaining all complementary blocks. Its native optimizing sequence remains open. No theorem here constructs those matrices.
- [R4] PR #879, head `5645f787183edefacf6402b0cff60a991fa31ba4`, `standalone/2026-09-12-astra-two-scale-cutoff/PROOF.md`, lines 1–240 read. This is a different hyperbolic cutoff with a two-scale Mellin estimate; mode index is not our quadrature order. No spectrum is identified across the two constructions.
- [R5] Current descriptions of #875, #878, #880 and other recent PRs were reconnaissance, not full proof audits. In particular #875's real-zero comparison feasibility and #880's all-order theta realization are not imported as established inputs.
- [E1] J. R. Martinez, *Transfer Functions of Generalized Bessel Polynomials*, IEEE Transactions on Circuits and Systems CAS-24 (1977), archived as arXiv:1402.7092. Abstract/metadata consulted for classical Padé/Bessel attribution; the needed identities are proved here. https://arxiv.org/abs/1402.7092
- [E2] NIST DLMF §4.39, the classical hyperbolic continued fraction. https://dlmf.nist.gov/4.39
- [E3] NIST DLMF §25.5, especially equations 25.5.3–4, Fermi–Dirac Mellin integral and its derivative. https://dlmf.nist.gov/25.5

No broad priority claim, unbounded numerical campaign, full repository mathematical audit, Lean build, remote CI, or independent referee acceptance is asserted.
