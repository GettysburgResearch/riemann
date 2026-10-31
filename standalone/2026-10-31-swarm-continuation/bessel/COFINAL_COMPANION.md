# Cofinal Bessel approximation: an explicit limiting companion and exponentially paired zeros

Status: proposed component theorems with complete arguments below. These results apply to the actual theta coefficients along an unbounded cofinal family. They do not prove RH, a smaller zero-free strip, or the remaining companion-sign statement.

The main improvement over the preceding packet is analytic control of the cancellation that made its Bessel boundary numerics difficult. The numerator and denominator, after explicit normalization, approximate the same source transform with an exponentially small difference. The difference has a fixed limiting source companion. Thus the tiny residues are structural and can be rescaled before they are evaluated.

## 1. Definitions and main statements

Use the actual theta source and its Fourier normalization from the preceding theta proof:

\[
\Phi(t)=\sum_{n\ge1}(4\pi^2n^4e^{9t/2}-6\pi n^2e^{5t/2})
 e^{-\pi n^2e^{2t}},\qquad
\Xi(z)=\int_{\mathbb R}\Phi(t)e^{izt}\,dt.
\]

Put

\[
w(x)=\Phi(\tfrac12\operatorname{arsinh}x),\qquad
c_n=I_n(a)w(n/a),\qquad S=M/a,
\]

\[
\mathcal K_{a,M}(t)=e^{-a\cosh(2t)}\sum_{|n|\le M}c_{|n|}e^{2nt}.
\]

For an energy E let nu satisfy nu²=-E, and define entire functions of E

\[
\mathscr X(E)=\Xi(2\sqrt E),\qquad
F_{a,M}(E)=\int_0^\infty\mathcal K_{a,M}(t/2)\cosh(\nu t)\,dt.
\tag{1}
\]

The choice of square root is immaterial. For the polynomial reduction in the preceding boundary note write

\[
F=A(E)y(E)+B(E)\dot y(E),\qquad
y(E)=K_\nu(a),\quad\dot y(E)=a\partial_a K_\nu(a).
\tag{2}
\]

Weights c_n are fixed when the differential operators defining A,B are applied. Introduce the real entire growing solution and its radial derivative

\[
u(E)=\tfrac12(I_\nu(a)+I_{-\nu}(a)),\quad
\dot u(E)=a\partial_a u(E),\quad
J_{a,M}(E)=A(E)u(E)+B(E)\dot u(E).
\tag{3}
\]

Here and below a dot differentiates the Bessel argument at fixed order; it does not differentiate c_n.

### Theorem A: a quantitative complete-source rate

For every R>=0 and every 0<c<2*pi there is a finite source-dependent constant C_(R,c) such that, for a>=1 and integers M>=0,

\[
\int_{\mathbb R}|\mathcal K_{a,M}(t)-\Phi(t)|e^{R|t|}\,dt
\le C_{R,c}\left(a^{-1}+e^{-cM/(2a)}\right).
\tag{4}
\]

In particular the explicit cofinal schedule

\[
M(a)=\left\lceil a(3+2\log a)\right\rceil
\tag{5}
\]

gives O_R(1/a) convergence in every such norm. This supplies a rate for the full source, including the finite cutoff.

### Theorem B: a fixed limiting companion

The following is a real entire function of E:

\[
\begin{split}
J_\infty(E)={}&\frac1\pi\int_0^\pi w(i\sin\theta)\cos(\nu\theta)\,d\theta\\
&+\frac{\sin(\pi\nu)}\pi\int_0^\infty\Phi(t/2)\sinh(\nu t)\,dt.
\end{split}
\tag{6}
\]

The boundary values in the first integral exist smoothly, including theta=pi/2. For every compact energy disk |E|<=R and c in (0,2*pi),

\[
\sup_{|E|\le R}|J_{a,M}(E)-J_\infty(E)|
\le C_{R,c}\left(a^{-1}+e^{-cS/2}+e^{aH(S)}\right),
\tag{7}
\]

where

\[
H(S)=1+\sqrt{1+S^2}-S\operatorname{arsinh}S.
\tag{8}
\]

This is useful when S>=3, for which H(S)<=H(3)<0. In particular J_(a,M) is uniformly bounded on every fixed energy compact along every cofinal sequence a->infinity, M/a->infinity. It converges to J_infinity, and the schedule (5) makes the convergence O_R(1/a).

### Theorem C: exact cancellation scale, pole residues, and local sign

Uniformly on every fixed energy compact, u and dot u are nonzero for all sufficiently large a, and

\[
-\frac{B(E)}{u(E)}=F_{a,M}(E)-\frac{y(E)}{u(E)}J_{a,M}(E),
\qquad
\frac{A(E)}{\dot u(E)}=F_{a,M}(E)-\frac{\dot y(E)}{\dot u(E)}J_{a,M}(E).
\tag{9}
\]

Along any cofinal sequence, the differences on the right are O_R(e^(-2a)). Both normalized expressions converge locally uniformly to the actual energy transform X. Consequently their zeros, counted with multiplicity, have the same eventual counts as X on any fixed bounded domain whose boundary is zero-free for X.

Suppose E_* is a simple zero of X. There are unique nearby zeros e_a of F, lambda_a of B, and mu_a of A for all sufficiently large a. Then

\[
e^{2a}(\lambda_a-e_a)\longrightarrow
\pi\frac{J_\infty(E_*)}{\mathscr X'(E_*)},\qquad
e^{2a}(\mu_a-e_a)\longrightarrow
-\pi\frac{J_\infty(E_*)}{\mathscr X'(E_*)}.
\tag{10}
\]

If J_infinity(E_*) is nonzero, the nearby B zero is a genuine pole of r=-A/B, and its residue obeys

\[
\frac{\operatorname{Res}_{E=\lambda_a}r(E)}{2\pi a e^{-2a}}
\longrightarrow \frac{J_\infty(E_*)}{\mathscr X'(E_*)}.
\tag{11}
\]

For a simple real positive E_*, these nearby zeros are real by conjugation. Thus the eventual sign of this pole residue is exactly the sign of the fixed source ratio in (11), whenever that ratio is nonzero. If J_infinity(E_*)=0, the limit is zero and the next term or an exact common factor must be investigated; no sign conclusion follows.

Finally, away from any fixed neighborhoods of the zeros of X, the rational boundary sign is automatically correct at large a:

\[
\frac{\operatorname{Im}r(E)}{\operatorname{Im}E}
=-\frac1{2a}+O_{R,\delta}(a^{-2})+O_{R,\delta}(ae^{-2a})<0.
\tag{12}
\]

Here |E|<=R, Im E is nonzero, and the distance of E from the zero set of X is at least delta>0. The last strict inequality holds for sufficiently large a along the cofinal sequence. This is complete complex-domain control on that set, rather than a grid observation. The excluded zero neighborhoods contain the remaining RH-bearing problem.

## 2. The closed-strip cusp lemma

**Lemma.** The function w is holomorphic in |Im x|<1. It and every derivative extend continuously to |Im x|<=1, are flat at x=+i and x=-i, and decay exponentially along both horizontal boundary lines. Consequently, with

\[
\widehat w(\omega)=\int_{\mathbb R}w(x)e^{-i\omega x}\,dx,
\]

for every integer N>=0 there is C_N such that

\[
|\widehat w(\omega)|\le C_N e^{-|\omega|}(1+|\omega|)^{-N}.
\tag{13}
\]

**Proof.** The principal arsinh maps the open strip into |Im arsinh x|<pi/2. Thus its half lies in the known holomorphic strip of Phi. The identity w(-x)=w(x) follows from evenness of Phi and oddness of arsinh.

For large positive Re x on the closed strip, set

\[
Y=x+\sqrt{1+x^2}=e^{\operatorname{arsinh}x}.
\]

Then Re Y=2 Re x+O(1/Re x). The literal theta series and each fixed derivative are bounded by a polynomial times exp(-pi Re Y). The negative real direction follows by evenness. This proves uniform horizontal exponential decay, away from the two possible branch points.

At x=i put v=x-i and epsilon=Y-i. For v in the closed strip near zero, Im v<=0, and

\[
\epsilon=\sqrt{2iv+v^2}+v.
\]

The square root has argument between -pi/4 and pi/4 to leading order. For a sufficiently small fixed neighborhood this gives Re epsilon>=c|epsilon|>0 and Re(1/epsilon)>=c/|epsilon|, for an absolute c>0. Gaussian Poisson summation gives

\[
\theta(i+\epsilon)=\epsilon^{-1/2}
\sum_{k\in\mathbb Z}e^{-\pi(k+1/2)^2/\epsilon}.
\tag{14}
\]

Every fixed epsilon derivative is bounded by a power of |epsilon|^(-1) times exp(-c'/|epsilon|). The factors in Phi are analytic and bounded functions of Y near i. Differentiating Y with respect to x introduces only further powers of epsilon^(-1). Therefore w and every fixed x derivative tend to zero faster than every power of |x-i|, uniformly from the closed strip. This proves the claimed flat extension at i. Conjugation handles -i.

The boundary derivatives are consequently integrable. Shift the Fourier contour to Im x=-1 for omega>0 and to Im x=+1 for omega<0; the shift follows first at heights below one and then by dominated convergence, using the flatness and uniform tails just proved. N integrations by parts along the boundary line give (13) for |omega|>=1; enlarging the constant treats small omega. In particular

\[
\int_{\mathbb R}|\widehat w(\omega)|e^{|\omega|}(1+|\omega|^k)\,d\omega<\infty
\quad\hbox{for every fixed }k.
\tag{15}
\]

This endpoint improvement is source-specific: the non-analytic cusp is infinitely flat in the sectors relevant to the horizontal x-strip. It does not assert holomorphic continuation through either cusp. ∎

## 3. Complete-source rate: proof of Theorem A

For fixed real t let s=sinh(2t), d=cosh(2t), and let N=X-Y for independent Poisson variables with means ae^(2t)/2 and ae^(-2t)/2. The exact tilted Skellam identity gives

\[
\mathcal K_a(t)=\mathbb E_t[w(N/a)],\quad
\mathbb E_t(N/a)=s,\quad\operatorname{Var}_t(N/a)=d/a.
\tag{16}
\]

The actual source satisfies, for every c<2*pi and every fixed derivative order k,

\[
|w^{(k)}(x)|\le C_{c,k}e^{-c|x|}\qquad(x\in\mathbb R).
\tag{17}
\]

This follows by differentiating the theta series and absorbing its polynomial factors into the exponential; it was also used in the earlier approximation proof.

It suffices to take t>=0 by evenness. Write Z=N/a and Delta=Z-s. When 0<=s<=1, the global second-derivative bound and E Delta=0 give |E w(Z)-w(s)|<=C/a. When s>=1, split according to |Delta|<=s/2. On that event Taylor's remainder is bounded by C exp(-cs/2) Delta², and its expectation is at most C s exp(-cs/2)/a.

For the complementary event use the centered moment generating function

\[
\mathbb E e^{\lambda(N-as)}
=\exp\{a d(\cosh\lambda-1)+as(\sinh\lambda-\lambda)\}.
\]

Since d<=3s/2 for s>=1, the elementary estimates
cosh lambda-1<=lambda² and |sinh lambda-lambda|<=lambda² for |lambda|<=1/4 give, at lambda=+/-1/10,

\[
\Pr(|\Delta|>s/2)\le2e^{-as/40},\qquad
\mathbb E(|\Delta|\mathbf1_{|\Delta|>s/2})
\le\sqrt{3s/a}\,e^{-as/80}.
\tag{18}
\]

The Taylor remainder on the bad event is at most 2||w||_infinity+||w'||_infinity|Delta|. Splitting the exponents and maximizing the remaining factors of a and as bounds its expectation by C a^(-1)exp(-s/160). Therefore, for some fixed kappa>0,

\[
|\mathcal K_a(t)-\Phi(t)|
\le \frac C a(1+|\sinh2t|)e^{-\kappa|\sinh2t|}.
\tag{19}
\]

The finite cutoff also has a complete tail bound. On |Z|>S,
w(Z)<=C exp(-cS/2)exp(-c|Z|/2). With delta=c/(2a),

\[
\mathbb E e^{-\delta|N|}\le\mathbb E e^{-\delta N}
=\exp\{ad(\cosh\delta-1)-as\sinh\delta\}.
\]

Use d<=s+1, a(cosh(c/(2a))-1)<=cosh(c/2)-1, and
a(1-exp(-c/(2a)))>=1-exp(-c/2). This proves

\[
0\le\mathcal K_a(t)-\mathcal K_{a,M}(t)
\le C_c e^{-cS/2}e^{-(1-e^{-c/2})|\sinh2t|}.
\tag{20}
\]

Every right side in (19)–(20), multiplied by exp(R|t|), is integrable. Integrating proves (4). Taking c=1 and (5) proves the explicit O_R(1/a) cofinal statement. No finite arithmetic prefix or fitted theta moments enter this proof. ∎

## 4. An integral formula for the companion

For a>0 and complex nu, the standard Bessel integral formula gives

\[
u(E)=\frac1\pi\int_0^\pi e^{a\cos\theta}\cos(\nu\theta)\,d\theta
+\frac{\sin\pi\nu}\pi\int_0^\infty e^{-a\cosh t}\sinh(\nu t)\,dt.
\tag{21}
\]

This is obtained by averaging I_nu and I_(-nu) in [DLMF 10.32.4](https://dlmf.nist.gov/10.32.E4); the plus sign in the second term is important.

Let

\[
P_{a,M}(\theta)=\sum_{|n|\le M}I_{|n|}(a)w(n/a)e^{in\theta}.
\]

The finite operator c0+2 sum_(n=1)^M c_n T_n(-partial_a), with c_n held fixed, maps K_nu to F and u to J. Applying it under (21), using T_n(cos theta)=cos(n theta) and T_n(cosh t)=cosh(nt), gives the exact identity

\[
\begin{split}
J_{a,M}(E)={}&\frac1\pi\int_0^\pi e^{a\cos\theta}P_{a,M}(\theta+\pi)
\cos(\nu\theta)\,d\theta\\
&+\frac{\sin\pi\nu}\pi\int_0^\infty\mathcal K_{a,M}(t/2)\sinh(\nu t)\,dt.
\end{split}
\tag{22}
\]

Thus the companion can be evaluated through the source rather than by subtracting two exponentially large polynomial/Bessel products.

## 5. Uniform angular cancellation: proof of Theorem B

For the full Fourier series P_a, Fourier inversion of w and the Bessel generating function give

\[
e^{a\cos\theta}P_a(\theta+\pi)
=\frac1{2\pi}\int_{\mathbb R}\widehat w(\omega)
\exp\{a[\cos\theta-\cos(\theta+\omega/a)]\}\,d\omega.
\tag{23}
\]

All exchanges are absolutely justified by (13) and sum_n I_|n|(a)=e^a. The cosine is globally Lipschitz on the real line, so the exponential in (23) is at most exp(|omega|). The argument converges to omega sin theta, uniformly in theta for each fixed omega. More quantitatively,

\[
|a[\cos\theta-\cos(\theta+\omega/a)]-\omega\sin\theta|
\le\omega^2/(2a).
\]

Both real exponents are bounded above by |omega|. The mean value theorem and (15) therefore prove, uniformly for 0<=theta<=pi,

\[
e^{a\cos\theta}P_a(\theta+\pi)
=w(-i\sin\theta)+O(a^{-1})
=w(i\sin\theta)+O(a^{-1}).
\tag{24}
\]

The cutoff error is also uniform. For any positive h, the Bessel generating function bounds

\[
\sum_{n>M}I_n(a)\le e^{-hM+a\cosh h}.
\]

Consequently, putting h=arsinh S,

\[
\sup_\theta e^{a\cos\theta}|P_a(\theta+\pi)-P_{a,M}(\theta+\pi)|
\le2\|w\|_\infty e^{aH(S)}.
\tag{25}
\]

Insert (24)–(25) in the first integral of (22). The second integral converges at the rate in Theorem A, because |sinh(nu t)|<=exp(sqrt(R)t) on |E|<=R. This proves (6)–(7), including uniformity on complex energy compacts. The integrals are even entire functions of nu and therefore entire in E. They are real for real E by conjugation. ∎

The angular integral can equivalently be folded to

\[
\frac{2\cos(\pi\nu/2)}\pi
\int_0^{\pi/2}\Phi(i\theta/2)
\cos\bigl(\nu(\theta-\pi/2)\bigr)\,d\theta.
\tag{26}
\]

One must not assume this is a positive source kernel. In fact Phi(i theta/2) is negative sufficiently close to theta=pi/2. The leading term of (14), including the two theta derivatives in Phi, gives a negative real multiple of a positive power times exp(-pi/(4 epsilon)) along that arc. This is consistent with its flat endpoint and prevents a naive positivity proof for J_infinity.

## 6. Exponentially paired zeros and exact residues

The Bessel Wronskian [DLMF 10.28.2](https://dlmf.nist.gov/10.28.E2), unchanged when I_nu is replaced by its symmetric average, gives

\[
y\dot u-\dot y u=1.
\tag{27}
\]

Inverting (2)–(3) proves (9) exactly. The standard large-positive-argument expansions, uniform for nu in any fixed compact set, are

\[
\begin{split}
u(E)&=\frac{e^a}{\sqrt{2\pi a}}\left(1+\frac{4E+1}{8a}+O_R(a^{-2})\right),\\
y(E)&=\sqrt{\frac\pi{2a}}e^{-a}\left(1-\frac{4E+1}{8a}+O_R(a^{-2})\right),\\
\frac yu&=\pi e^{-2a}(1+O_R(a^{-1})),\qquad
\frac{\dot y}{\dot u}=-\pi e^{-2a}(1+O_R(a^{-1})),\\
m_u:=\frac{\dot u}{u}
&=a-\frac12-\frac{4E+1}{8a}+O_R(a^{-2}).
\end{split}
\tag{28}
\]

See [DLMF 10.40.1–4](https://dlmf.nist.gov/10.40). The needed compact-order uniformity also follows directly by Laplace expansion in (21) and in the K integral; bounded nu and its E derivatives have common integrable majorants. The remainders are holomorphic in E on slightly larger disks, so Cauchy estimates give the corresponding E-derivative bounds.

Theorem B makes J uniformly bounded along a cofinal sequence. Equations (9) and (28) prove the O(e^(-2a)) assertion. Theorem A gives local uniform convergence to X. Rouché's theorem then gives the zero counts. This statement concerns zeros of the actual polynomials A,B before cancellation; a common factor remains a separate part of the transform, as in the preceding boundary note.

For a simple target zero E_*, Rouché gives one nearby zero of each normalized expression and of F, counted with multiplicity. Their derivatives tend to the nonzero X'(E_*). Apply the mean-value expansion to

\[
D(E):=-B(E)/u(E)=F(E)-(y/u)J(E)
\]

at its zero lambda_a and the zero e_a of F. First this gives |lambda_a-e_a|=O(e^(-2a)); then dividing by e^(-2a) and using J->J_infinity gives the first limit in (10). The A limit follows from dot y/dot u. Conjugation makes each unique nearby zero real when E_* is real.

There is an exact rational identity, valid away from poles,

\[
r(E)=-A(E)/B(E)=m_u(E)+\frac{J(E)}{u(E)^2D(E)}.
\tag{29}
\]

If J_infinity(E_*) is nonzero, then J(lambda_a) is nonzero for large a. Hence A and B have no common root there, and

\[
\operatorname{Res}_{\lambda_a}r
=\frac{J(\lambda_a)}{u(\lambda_a)^2D'(\lambda_a)}.
\tag{30}
\]

Since 1/u²=2*pi*a*exp(-2a)(1+O_R(1/a)), this proves (11). It also shows that the residue is asymptotically a times the B-zero/A-zero separation. Common-factor cancellations are not silently discarded.

## 7. What the remaining sign problem becomes

Fix R and delta>0 and exclude delta-neighborhoods of the zero set of X. Local uniform convergence gives a uniform lower bound for |D| on the remaining compact set. Equation (29), Theorem B and (28) then give r-m_u=O_(R,delta)(a exp(-2a)). Cauchy estimates give the same bound for its derivative in any smaller zero-free neighborhood.

To control Im(r-m_u)/Im E uniformly even as E approaches the real axis, split into |Im E|>=delta/4 and its complement. In the first case the absolute bound suffices. In the second, the vertical segment to the real axis and a fixed smaller neighborhood remain separated from every zero, so the derivative bound applies. The function is real on that real segment. The holomorphic O_R(a^(-2)) remainder in m_u is handled the same way on a slightly larger disk. This proves (12).

For a simple real target zero, (11) identifies the remaining residue sign with

\[
J_\infty(E_*)/\mathscr X'(E_*).
\tag{31}
\]

The companion in (6) is a fixed source object; its definition contains no degree M, parameter a, polynomial root finder, or exponentially large cancellation between A and B. Its angular and sine pieces can still cancel at large real energy, so their direct numerical subtraction also needs controlled precision.

No theorem proving (31)>0 at every real zero is supplied here. More basically, no theorem excluding nonreal zeros of X is supplied. If X has a nonreal simple zero, the polynomial zero-count result puts corresponding nonreal zeros of B near it; exact common factors, if present, still belong to F. Thus the cofinal pole condition cannot be assumed from the asymptotic normalization itself.

There is a useful all-order simplification on the negative energy axis. For actual positive coefficients and M>=1, the recurrence P_(n+1)=P_(n-1)+2(nu+n)P_n/a has nonnegative coefficients, while the corresponding Q_n has nonpositive coefficients. Taking even parts and substituting nu²=-E proves

\[
A(E)>0,\qquad B(E)<0,\qquad r(E)>0\quad(E\le0).
\tag{32}
\]

The positive c0 and c1 make the inequalities strict. The ordinary decaying Weyl function m_a(E)=aK'_(sqrt(-E))(a)/K_(sqrt(-E))(a) is negative there. Thus the negative-energy pole/intersection exclusion in the preceding local gate holds automatically, for every order and every a>0. Equivalently, the original positive kernel has F(z)>0 for purely imaginary z. At M=0 the pure Dirichlet case is already positive.

## 8. Scope, calculations, and next mathematical obligation

These results establish a quantitative cofinal approximation, a closed-strip Fourier estimate using the actual theta cusp, a fixed limiting companion, exact exponential pairing of numerator and denominator zeros, a residue asymptotic, and automatic boundary sign away from target zeros. They explain the severe conditioning observed in the preceding packet without treating that conditioning as numerical evidence of RH.

The diagnostic program compares the first few limiting residue ratios with rescaled finite-a polynomial residues. It uses ordinary numerical arithmetic; it is not a directed certificate. The exact structural checker separately verifies finite algebraic identities and sign patterns. Neither finite program proves the analytic theorems above or an all-height zero statement.

The next genuine source question is whether the companion ratio (31) admits a sign representation, while complex pole exclusion requires an independent argument. The explicit limit may be compared with contour or de Branges companions, but no identification or positivity theorem is assumed. The underlying Bessel, Fourier-contour, and Rouché tools are classical; worldwide novelty of the source-specific combination is not established.

## Appendix: exact companion controls and a restriction on global Pick shortcuts

Let L=pi/2 and put

\[
\mathcal C(E)=\int_0^L\Phi(i\theta/2)\cos(\nu(\theta-L))\,d\theta
+\sin(\pi\nu/2)\int_0^\infty\Phi(t/2)\sinh(\nu t)\,dt.
\]

Then C is entire in E and the folded identity is

\[
J_\infty(E)=\frac2\pi\cos(\pi\nu/2)\,\mathcal C(E).
\tag{33}
\]

For E>=0 the cosine is cosh(pi sqrt(E)/2)>0, so C can replace J_infinity in the residue sign test. The factor also proves the exact identities

\[
J_\infty(-(2k+1)^2)=0\qquad(k=0,1,2,\ldots).
\tag{34}
\]

There is a useful independent normalization value:

\[
J_\infty(-1/16)=-\frac1{2\sqrt2\,\pi}.
\tag{35}
\]

To prove it, set h(t)=exp(t/4)theta(exp t) and k(t)=h(t)-exp(t/4). The theta relation gives h'(0)=0, hence k'(0)=-1/4, while k decays on the positive real axis. Direct differentiation gives g(t):=Phi(t/2)=2h''(t)-h(t)/8=2k''(t)-k(t)/8. Both h and its derivatives vanish at iL by the cusp lemma. Define

\[
H_c=\int_0^L h(i\theta)\cos(\nu\theta)\,d\theta,
\quad H_s=\int_0^L h(i\theta)\sin(\nu\theta)\,d\theta,
\quad S_k=\int_0^\infty k(t)\sinh(\nu t)\,dt.
\]

Two integrations by parts in the angular and real integrals give

\[
\pi J_\infty(E)=
(2\nu^2-1/8)\big[(1+\cos\pi\nu)H_c+\sin\pi\nu(H_s+S_k)\big]
-2\nu\sin\pi\nu.
\tag{36}
\]

At nu=1/4 the bracket coefficient vanishes, proving (35). This exact value checks the radial normalization, Fourier factor, and sign in the I integral independently of polynomial root finding.

Neither J_infinity/X nor the reduced C/X is globally anti-Herglotz. For the first quotient, X(E)>0 on E<=0, whereas (34) gives repeated distinct real zeros; a nonconstant anti-Herglotz function analytic across the negative real axis is strictly decreasing there and cannot have them. It is nonconstant by (35).

For the reduced quotient, take nu=2k+1 real and E=-nu². The angular integral in C is uniformly bounded because its cosine is bounded. Write G(nu)=integral_0^infinity Phi(t/2)exp(nu t)dt. Positivity gives G(nu)->infinity and G(-nu)->0, so

\[
\frac{\int_0^\infty\Phi(t/2)\sinh(\nu t)dt}
{\mathscr X(-\nu^2)}
=\frac{G(\nu)-G(-\nu)}{G(\nu)+G(-\nu)}\longrightarrow1.
\]

Consequently C(-(2k+1)²)/X(-(2k+1)²)-(-1)^k tends to zero. These negative-axis sign oscillations also exclude a global anti-Herglotz representation for that quotient. The universal term m_u in (29) must therefore be retained in any argument about the actual finite impedance. This observation does not decide the needed positive-energy residue signs.
