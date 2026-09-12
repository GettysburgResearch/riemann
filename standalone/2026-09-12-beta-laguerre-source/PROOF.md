# BLS26 — exact Laguerre coordinates and the singular endpoint of the beta–Brownian homotopy

Date: 2026-09-12.
Status: **PROPOSED component proofs. Independent mathematical review required. RH is not proved.**
Scope: the literal fixed-point path in PR #876; no replacement of the source, no claimed collision-sign theorem, and no new certified zero inside the critical strip.

The attempted completion was to bound the actual homotopy's signed zero production. A new exact source expansion makes that question directly computable with a complete error bound. Exploratory sign calculations did not survive truncation checks and are NOT evidence for a sign theorem. A separate analytic result resolves a genuine feature of this path: its nearest Mellin poles vanish quadratically at the Xi endpoint, accompanied by two real zeros outside the critical strip. None of these statements proves centrality of the nontrivial Xi zeros.

Classical inputs are beta–gamma algebra, Laguerre orthogonality/completeness, Mellin integration, the BPY endpoint identity, and Rouché's theorem. No general novelty claim is made for these tools. All new identities, constants, norms, domains and source bindings are specified below.

## 1. Fixed source, and the bounds actually used

Freeze PR #876 at `8002444ec4d4bd1c6f8fa073820bcc575cb218e1`, principal proof blob `bb82833e204abb8a69a7602642b3d0cb4e7b7024`. Let

\[
 k=5/2,\quad c=\pi/6,\quad B\sim\mathrm{Beta}(k,k),\quad W=U^{-2},\quad U\sim\mathrm{Unif}[1,2].
\]

For 0<=theta<=1 let C_theta have the probability mixture (1-theta) Law(B)+theta Law(W). The fixed law is

\[
 X_\theta\overset d=C_\theta(X_\theta+X_\theta'),\qquad E X_\theta=1,\tag{1}
\]

where the children are independent and ONE independent multiplier scales their sum. Write S_theta=X_theta+X_theta', and

\[
 M_\theta(s)=E(cS_\theta)^{s/2},\qquad
 H_\theta(s)=\frac{M_\theta(s)+M_\theta(1-s)}{2(1+M_\theta(1))}.\tag{2}
\]

Positive powers use real logarithms. All statements below use the same rate k, the same c, and the same normalization.

The parent proves existence and uniqueness by the W2 contraction sqrt(7/12), and identifies

\[
 X_0\sim\Gamma(k,\mathrm{rate}\ k),\quad
 X_1=\frac6{\pi^2}\sum_{j\ge1}\frac{E_j}{j^2},\quad
 L_1(t)=\frac{\sqrt{6t}}{\sinh\sqrt{6t}},\quad
 M_1(s)=2\xi(s),\ H_1=\xi.\tag{3}
\]

The E_j are independent mean-one exponentials. The BPY identity is classical; its normalization is rederived in the parent through the negative-moment Laplace integral, gamma duplication and xi reflection. We retain that proposed proof, not an assumption about zeros.

The source estimates needed here are

\[
 L_\theta(t)\le L_0(t)=(1+t/k)^{-k}\quad(t\ge0),\tag{4}
\]

\[
 E S_\theta^{-b}\le k^b\frac{\Gamma(5-b)}{24}\quad(0<b<5),\tag{5}
\]

and

\[
 E e^{\lambda X_\theta}\le E e^{\lambda X_1}
 =\frac{\sqrt{6\lambda}}{\sin\sqrt{6\lambda}}
 \quad(0\le\lambda<\pi^2/6).\tag{6}
\]

Here is a short reconstruction of the ordering behind them. The beta density is
\(b_C(x)=128x^{3/2}(1-x)^{3/2}/(3\pi)\); W has density \(w_C(x)=1/(2x^{3/2})\) on [1/4,1]. They agree in moments 0,1,2. The ratio w_C/b_C on (1/4,1) decreases to its minimum at 2/3 and then increases. Its value just above 1/4 is 2pi/sqrt(3)>1, its minimum is 243pi sqrt(3)/2048<1, and it diverges at 1. Thus w_C-b_C has three sign switches, in order -, +, -, +. Quadratic interpolation at the switches proves B<=_3 W for tests with nonnegative third derivative. Independent addition and positive scaling preserve this order. Starting the fixed-point iteration at the gamma law and passing to its W2 limit, using uniform fourth moments, proves nu_0<=_3 nu_theta<=_3 nu_1. Taking exp(-tx), whose third derivative is negative, gives (4). The positive negative-moment integral applied to L_theta^2 gives (5).

For positive integer moments one can instead use the elementary fixed-point recursion directly. Set

\[
 a_j(\theta)=(1-\theta)\frac{(k)_j}{(5)_j}
 +\theta\frac{1-2^{1-2j}}{2j-1}\quad(j\ge1),\quad a_0=1.\tag{7}
\]

The third-order scale comparison gives a_j(theta)<=a_j(1) for j>=3; the lower moments agree. Induction in the fixed-point moment equation shows that every positive integer moment is bounded by its endpoint value. Applying monotone convergence to the exponential series proves (6). Finiteness is justified first for finite iterations, uniformly in each fixed moment order, and then at the fixed point.

Useful explicit consequences are

\[
 E S_\theta^{-5/2}<5/8,\quad E e^{X_\theta}<4,\quad
 E e^{3X_\theta/2}<24.\tag{8}
\]

For the first, k^(5/2)<10 and Gamma(5/2)<3/2. For the last, sin(3)>1/8: use pi>157/50, 0<pi-3<1, and sin u>=u-u^3/6; at u=7/50 the latter lower bound already exceeds 1/8. For the middle, sqrt(6)<49/20 and pi-sqrt(6)>27/40, so sin(sqrt(6))>49/80>sqrt(6)/4. Only elementary trigonometric estimates occur here. Square (8)'s exponential bounds for S_theta. In particular

\[
 E[S_\theta^{-5/2}e^{S_\theta}]<18,\qquad
 E[S_\theta^{-5/2}e^{3S_\theta/2}]<580.\tag{9}
\]

Split at S=1, use (8), e<3 and e^(3/2)<5.

## 2. Uniform gamma-relative square integrability of the actual density

### Theorem BLS1

Every X_theta has a density f_theta and S_theta has density q_theta. With

\[
 g(x)=\frac{k^5}{24}x^4e^{-kx}\quad(x>0),
\]

one has, uniformly for 0<=theta<=1,

\[
 \boxed{\int_0^\infty \frac{q_\theta(x)^2}{g(x)}dx<1500^2.}\tag{10}
\]

The integral covers both endpoints and the whole physical tail. This is not an L2 assumption about a fitted density.

**Proof.** The multiplier's density is at most 32 c^(3/2) on (0,1). For the W part this follows from 1/(2c^3)<=32 on [1/4,1]; for the beta part its density constant 128/(3pi) is smaller than 32. Conditional on S, the law of CS has density S^-1 f_C(x/S). Thus absolute continuity follows, and

\[
 f_\theta(x)\le32x^{3/2}E[S_\theta^{-5/2}1_{S_\theta>x}]<20x^{3/2}.\tag{11}
\]

The same inequality with e^(3x/2)<=e^(3S/2) on S>x and (9) gives

\[
 f_\theta(x)<19000x^{3/2}e^{-3x/2}.\tag{12}
\]

Convolving once and bounding (x-y)^(3/2)<=x^(3/2) gives

\[
 q_\theta(x)<456000x^{3/2}e^{-3x/2}.\tag{13}
\]

Indeed the remaining tilted integral is at most E exp(3X_theta/2)<24. Using one copy of this bound, not squaring its large constant, gives

\[
 \int q_\theta^2/g
 \le\frac{456000\cdot24}{k^5}
 E[S_\theta^{-5/2}e^{S_\theta}]
 <114000\cdot18<1500^2,
\]

since k^5>96. This proves (10). All these estimates hold for versions of the densities almost everywhere; the convolution has its usual continuous version. □

## 3. Exact Laguerre coordinates, with a complete complex remainder

Define the classical Laguerre polynomials

\[
 \mathcal L_j(x)=L_j^{(4)}(kx)
 =\sum_{r=0}^j(-1)^r\binom{j+4}{j-r}\frac{(kx)^r}{r!},
\quad h_j=\binom{j+4}{4}.\tag{14}
\]

Their squared norms in L2(g dx) are h_j and they are orthogonal. This is the classical Laguerre normalization [D1]. It can also be derived by Rodrigues integration by parts. Completeness follows without a density assumption: if v in L2(g) is orthogonal to all polynomials, its g-weighted Laplace transform is analytic in Re t>-k/2, by Cauchy–Schwarz, and has every derivative zero at the origin. Analytic continuation and Laplace uniqueness give v=0 almost everywhere.

Let

\[
 e_j(\theta)=E X_\theta^j/j!,\qquad
 s_j(\theta)=E S_\theta^j/j!=\sum_{i=0}^j e_i e_{j-i}.
\]

Then e_0=e_1=1 and, for j>=2,

\[
 e_j=\frac{a_j}{1-2a_j}\sum_{i=1}^{j-1}e_i e_{j-i}.\tag{15}
\]

All denominators are positive on [0,1]. Define

\[
 b_j(\theta)=E\mathcal L_j(S_\theta)
 =\sum_{r=0}^j(-k)^r\binom{j+4}{j-r}s_r(\theta).\tag{16}
\]

They are rational functions of theta, with no poles on [0,1], and are rational at every rational theta. In particular

\[
 b_0=1,\quad b_1=b_2=0,\quad
 \boxed{b_3(\theta)=-\frac{35\theta}{50-\theta}.}\tag{17}
\]

Their signs must NOT be replaced by positivity merely because the underlying law is positive.

### Theorem BLS2: exact expansion of the whole source

Put p=s/2. For Re p>-5/2,

\[
 \boxed{M_\theta(s)=
  \left(\frac\pi{15}\right)^p\frac{\Gamma(5+p)}{24}
  \sum_{j=0}^\infty b_j(\theta)\frac{(-p)_j}{(5)_j}.}\tag{18}
\]

The series is absolutely convergent. Convergence is locally uniform in this half-plane and uniform in theta on [0,1]. The reflected formula is consequently valid on the common strip -5<Re s<6. These are domains of THIS L2 representation; Section 5 proves a larger meromorphic continuation by a different argument.

**Proof.** By (10) and Laguerre completeness,

\[
 q_\theta/g=\sum_{j\ge0}(b_j/h_j)\mathcal L_j,
\qquad \sum_{j\ge0}|b_j|^2/h_j<1500^2.\tag{19}
\]

For Re p>-5/2 the test x^p belongs to L2(g). Direct integration of (14), followed by the finite binomial identity (or Rodrigues integration and continuation), gives

\[
 \int x^p\mathcal L_j(x)g(x)dx
 =k^{-p}\frac{\Gamma(5+p)}{24}\frac{(-p)_j}{j!}.\tag{20}
\]

Taking the L2 pairing proves (18). Cauchy–Schwarz proves absolute convergence. The test x^p is an analytic L2-valued function in this half-plane, so its projection tails tend to zero uniformly on every compact exponent set. The uniform bound (19) makes the convergence uniform in theta as well. □

For N>=0 let M_theta,N be the sum in (18) through j=N, and let

\[
 T_N(p)=\sum_{j=N+1}^\infty
          \frac{|(-p)_j|^2}{j!(5)_j}.
\]

The entire error satisfies

\[
 \boxed{|M_\theta(s)-M_{\theta,N}(s)|
 \le1500\left|\left(\frac\pi{15}\right)^p
             \frac{\Gamma(5+p)}{24}\right|\sqrt{T_N(p)}.}\tag{21}
\]

The finite Laguerre projection of the density can be signed. It is used only together with the complete error in (21), not as a new positive law or a zero-preserving approximant.

One may replace 1500 by the square root of any valid upper bound for
\(\|q_\theta/g\|^2-\sum_{j\le N}|b_j|^2/h_j\). Finite coefficient energy alone does not upper-bound that residual.

### An explicit infinite-tail bound

Let a=Re p>-2, J=N+1, and require

\[
 J\ge\max\{1,\ |p|^2+2a\}.
\]

Then

\[
 \boxed{T_N(p)\le
 \frac{|(-p)_{N+1}|^2}{(N+1)!(5)_{N+1}}
 \frac{N+5}{4+2a}.}\tag{22}
\]

**Proof.** With t_j=|(-p)_j|^2/[j!(5)_j] and nu=5+2a>1, direct multiplication gives

\[
 t_{j+1}\le t_j\left(1-\frac\nu{j+5}\right),\quad j\ge J.
\]

The difference of the two ratio numerators is exactly j-|p|^2-2a, which is nonnegative. Define u_J=t_J and u_(j+1)=u_j(1-nu/(j+5)); the factors are positive under the stated conditions. The sequence v_j=u_j(j+4)/(nu-1) satisfies v_j-v_(j+1)=u_j. Since v_j tends to zero, summing gives sum u_j=t_J(J+4)/(nu-1). This is (22). If p is a nonnegative integer, its eventually zero Pochhammer tail is handled directly without dividing by a zero coefficient. □

As a check, the complete test-coefficient norm is

\[
 \sum_{j\ge0}\frac{|(-p)_j|^2}{j!(5)_j}
 =\frac{24\Gamma(5+2a)}{|\Gamma(5+p)|^2},\quad a>-5/2.\tag{23}
\]

This follows from Parseval applied to x^p, or the classical Gauss summation [D3]. It is not evaluated by subtracting nearly equal infinite quantities in (22).

Cauchy estimates on a slightly larger s-domain give corresponding derivative errors. No parameter derivative error is supplied by (21) alone; differentiating its finite coefficients and omitting the unknown derivative tail is forbidden.

## 4. A direct nonlinear recursion in the orthogonal coordinates

There is no need to obtain every coefficient by a cancellation-prone transform of large raw moments. A second exact recursion operates directly in gamma-adapted coordinates.

Set

\[
 \alpha_j(\theta)=E L_j^{(k-1)}(kX_\theta),\qquad
 b_j=\sum_{r=0}^j\alpha_r\alpha_{j-r}.\tag{24}
\]

The convolution identity follows from the Laguerre generating function, first on a small disk where the moment-generating integrals are uniformly dominated. It is also a finite polynomial identity. Let

\[
 w_{ij}=\sum_{h=0}^{i-j}(-1)^h\binom{k}{h}
       \frac{(5+j)_{i-j-h}}{(i-j-h)!}
       E[W^j(1-W)^{i-j-h}],\quad 0\le j\le i.\tag{25}
\]

Every entry is rational. Its diagonal is E W^i. Define the lower triangular matrix

\[
 K_{ij}(\theta)=(1-\theta)\frac{(k)_i}{(5)_i}\mathbf1_{i=j}
                 +\theta w_{ij}.
\]

Then the exact fixed equation in these coordinates is

\[
 \alpha_i=\sum_{j=0}^i K_{ij}(\theta)b_j.\tag{26}
\]

In particular alpha_0=1, alpha_1=0, and for i>=2,

\[
 \boxed{\alpha_i=
 \frac{a_i\sum_{r=1}^{i-1}\alpha_r\alpha_{i-r}
       +\theta\sum_{j=0}^{i-1}w_{ij}b_j}{1-2a_i}.}\tag{27}
\]

The first mean equation is not invertible: 1-2a_1=0. Mean one supplies alpha_1=0 explicitly. The variance equation gives alpha_2=0. This null direction must not be treated as an invertible coefficient equation.

**Derivation.** Put A(z)=(1-z)^(-k)L_theta(kz/(1-z)). For sufficiently small z, substitute the fixed-point equation to get

\[
 A(z)=(1-z)^k\int[1-(1-C)z]^{-5}
       A\!\left(\frac{Cz}{1-(1-C)z}\right)^2\mu_\theta(dC).
\]

The W coefficient is (25). For a beta multiplier the jth input monomial has expectation

\[
 z^j(1-z)^k E\{B^j[1-(1-B)z]^{-5-j}\}
 =z^j\frac{(k)_j}{(5)_j}.
\]

Expanding the beta integral proves this identity coefficientwise; the sum is the binomial function (1-z)^(-k) which cancels the outside factor. Thus the beta part is diagonal. Separating b_i=2alpha_i+sum_(1<=r<i)alpha_r alpha_(i-r) proves (27).

The diagonal inverses are uniformly bounded for i>=3 by 80/49, since a_i<=a_3(1)=31/160. The remaining triangular coefficients are signed; for example w_30=-7/32. This is not a positivity-preserving recurrence for Laguerre or Fourier coefficients, and the diagonal bound is not a zero-location theorem.

## 5. The nearest Mellin poles disappear at exactly quadratic order

This part addresses the actual analytic structure of the new path, independently of the scouts.

Write beta_k=B(k,k)=3pi/128 and b_C=1/beta_k=128/(3pi).

### Theorem BLS3: uniform small-x law and meromorphic continuation

As x decreases to zero,

\[
 f_\theta(x)=A_\theta x^{3/2}+O(x^{5/2}),\qquad
 A_\theta=(1-\theta)b_C E S_\theta^{-5/2},\tag{28}
\]

and

\[
 q_\theta(x)=B_\theta x^4+O(x^5),\qquad
 B_\theta=b_C(1-\theta)^2(E S_\theta^{-5/2})^2.\tag{29}
\]

Both remainders are uniform over 0<=theta<=1. Thus M_theta is meromorphic in Re s>-12, with its only possible pole there at s=-10. That pole is simple and genuine for EVERY theta<1. H_theta is meromorphic on -12<Re s<13, with precisely two poles there, -10 and 11, when theta<1. They have opposite residues.

The residue at -10 is

\[
 \boxed{r_H(\theta)=
 \frac{c^{-5}b_C(1-\theta)^2(E S_\theta^{-5/2})^2}{1+M_\theta(1)}>0,}
 \quad\theta<1.\tag{30}
\]

At the endpoint,

\[
 \boxed{\lim_{\theta\uparrow1}
        \frac{r_H(\theta)}{(1-\theta)^2}
       =\frac{1024\pi^5}{11907}.}\tag{31}
\]

**Proof.** The conditional-density formula is exactly

\[
\begin{aligned}
f_\theta(x)={}&(1-\theta)b_Cx^{3/2}
 E[S^{-5/2}(1-x/S)^{3/2}1_{S>x}]\\
 &+\frac\theta{2x^{3/2}}E[S^{1/2}1_{x\le S\le4x}].
\end{aligned}\tag{32}
\]

From (11) and convolution, q_theta(s)<=400 beta_k s^4<30s^4. The W contribution in (32) is therefore O(x^4), uniformly. In the first term use
\(|(1-u)^{3/2}-1|\le(3/2)u\) on [0,1], and
\(E[S^{-5/2}1_{S\le x}]\le x E S^{-7/2}\). The latter negative moment has a uniform bound by (5). This proves (28), with an O(x^(5/2)) error for x<=1. Convolve (28) with itself. The leading beta integral is A_theta^2 beta_k x^4, the two cross integrals are O(x^5), and the error product is O(x^6). This proves (29).

For p=s/2, subtract that leading term on the WHOLE interval (0,1):

\[
 M_\theta(s)=c^p\left[
 \frac{B_\theta}{p+5}
 +\int_0^1x^p(q_\theta(x)-B_\theta x^4)dx
 +\int_1^\infty x^p q_\theta(x)dx\right].\tag{33}
\]

The middle integral is holomorphic for Re p>-6 and the last is entire, using (13). Therefore the residue of M at -10 is 2c^-5 B_theta. Reflection and the actual normalizing denominator in (2) give (30). The reflected pole has the opposite sign; no pole lies in the critical strip.

As theta tends to one, negative moments converge by the positive Laplace representation and the integrable bound L_0^2; M_theta(1) tends to 1 by uniform integrability. By the EXACT BPY identity,

\[
 E S_1^{-5/2}=c^{5/2}2\xi(-5)=c^{5/2}2\xi(6),\quad
 \xi(6)=2\pi^3/63.
\]

Inserting these into (30) gives b_C*2*xi(6)^2=1024pi^5/11907, proving (31). No Xi zero assumption enters. □

### Theorem BLS4: an actual pair of real zero–pole cancellations near the endpoint

For every theta sufficiently close to one from below, H_theta has exactly one zero in each disk

\[
 |s+10|<1/4,\qquad |s-11|<1/4.
\]

Both zeros are simple and real. They lie respectively to the LEFT of -10 and to the RIGHT of 11. If the first is z_theta, then

\[
 \boxed{z_\theta=-10-
 \frac{1024\pi^5}{11907\,\xi(11)}(1-\theta)^2
 +o((1-\theta)^2).}\tag{34}
\]

The other is 1-z_theta. These are zeros of H_theta, NOT zeros of Xi. They are outside the critical strip. No effective numerical onset in theta is claimed.

**Proof.** The regular part H_theta(s)-r_H(theta)/(s+10) converges to xi(s), locally uniformly near -10. To justify this rather than appeal to pointwise probability convergence, use (32): on every fixed positive x its W expectation converges by weak convergence and the absence of endpoint atoms of S_1; the beta part vanishes. The bounds (11) give dominated convergence of its convolution, hence q_theta(x)->q_1(x). In (33), the UNIFORM O(x^5) remainder and the exponential tail (13) give locally uniform convergence after pole subtraction. The elementary difference [c^p-c^-5]/(s+10) is removable and multiplied by B_theta->0. The reflected summand and normalizing denominator converge as well.

Multiply by s+10. On the disk boundary, (s+10)H_theta tends uniformly to (s+10)xi(s). Xi is nonzero in the disk by its functional equation and the Euler product on the reflected disk Re(1-s)>1. Rouché therefore gives exactly one zero, counting multiplicity. At the center the numerator equals r_H(theta)>0, so this is an actual H_theta zero, not its pole. Conjugation forces it to be real and count one gives simplicity. Write H_theta=r_H/(s+10)+R_theta(s); then

\[
 z_\theta+10=-r_H(\theta)/R_\theta(z_\theta).
\]

Since R_theta(z_theta)->xi(-10)=xi(11)>0, its sign is negative. Equation (31) supplies (34). Reflection proves the other assertion. □

**Corollary: entire pole-clearing alone cannot put this homotopy in a global Lee–Yang class.** For every sufficiently late theta<1, let G_theta be any nonzero entire multiplier for which G_theta H_theta is entire. The product still vanishes at z_theta and 1-z_theta, because an entire multiplier cannot cancel an existing zero. Both zeros lie off Re s=1/2. Thus no such normalized product has all its zeros on that line, even arbitrarily close to theta=1. This excludes that STRONGER finishing method, not the parent's strip-only proposal, meromorphic factors allowed to cancel zeros, or RH. No existence of a particular pole-clearing G_theta is needed for the conditional statement.

This endpoint singularity does NOT contradict the parent's critical-strip homotopy or its defect continuity: its two poles and the zeros just located lie outside that strip. It does rule out calling every intermediate H_theta entire or applying an entire-function Lee–Yang theorem without an additional justified normalization.

## 6. The attempted closing sign, and what is still missing

The original purpose of these coordinates was to evaluate or prove the sign of the actual response at possible double-zero events. The parent supplies

\[
 \partial_\theta M_\theta(s)=2\chi_\theta c^p p(p-1)(p-2)
 E R_\theta^{p-3},\quad \chi_\theta=56/(50-\theta)^2,
\]

with a positive response law. The required real parts remain oscillatory. The new expansion DOES NOT turn that law into a positive Fourier transform.

In particular, differentiating the rational coefficients b_j(theta) is not, without a derivative-tail proof, an accepting calculation of partial_theta M. Nondirected endpoint-response sums of orders 1000 and 1500 disagreed materially at moderate heights. Near the tenth numerical zeta zero the apparent positive real response decreased strongly; at the eleventh it changed sign. No proposed sign theorem or actual zero/collision follows from those sums. SCOUTING.md records the failure rather than presenting a stable-looking truncated value as a discovery.

Even for function values, (21) with the deliberately conservative norm cap is not a sharp practical certificate at those ranks/heights. It is a complete theorem about the omitted source, not evidence that the scout has the displayed number of correct digits.

The precise remaining task is still one of the following, with complete boundary and collision accounting:

* a zero-location invariant for H_theta on 0<Re s<1; or
* a source-specific upper bound on the TOTAL nonreal-zero production from theta=0 to theta=1.

The parent's bounded positive inverse and (27)'s bounded diagonal inverse control a DIFFERENT issue: representing source response. They do not estimate its oscillatory sign. Our explicit residual bound permits a future certificate to test a fixed parameter/contour without deleting the source tail; it does not guarantee that every desired certificate succeeds.

The proof of RH would follow if the parent's nonnegative defect had endpoint value zero. No such inequality is established in this packet. The work is an unsuccessful completion attempt with rigorous source-coordinate and endpoint results, not a completed proposal awaiting a routine review of the last lemma.

## References and scope of attribution

[B] P. Biane, J. Pitman and M. Yor, Probability laws related to the Jacobi theta and Riemann zeta function and Brownian excursions, arXiv:math/9912170. The abstract/record was reread; the exact endpoint identity used here is reconstructed in the frozen parent. This session does not claim a fresh full-paper proof audit.
[D1] NIST DLMF, Sections 18.3 and 18.5: Laguerre orthogonality and Rodrigues/finite-sum conventions.
[D2] NIST DLMF, Section 18.17: classical Laguerre transforms. The exact scaled identity needed here is derived in (20).
[D3] NIST DLMF, Section 15.4: Gauss summation. Equation (23) also follows directly from Parseval and does not require a new analytic import.
[P] Frozen PR #876 PROOF.md, blob bb82833e204abb8a69a7602642b3d0cb4e7b7024. Its fixed-point existence, order and BPY normalization remain proposed paper mathematics pending independent review. Its executables were not rerun.

No exhaustive novelty assessment, independent referee acceptance, formal verification, new central-zero census, or actual source-specific collision certificate is claimed.
