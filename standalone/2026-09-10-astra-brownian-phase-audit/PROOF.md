# BRN27: the native phase target fails; a full renormalization-mode hierarchy

**Status: PROPOSED component mathematics and a directed computational refutation, pending independent mathematical and implementation review. RH is not proved or disproved.**

This continues BRN26 in PR846 at `d9b60f8569af65b6787fc33c75c849640c8974e6`, without altering it. The conclusion concerns the **literal prescribed companion**, not a changed density or a finite approximant. The old construction and convergence assertions are not thereby refuted. The old sufficient condition OPEN-BRN is refuted under the explicit certificate contract below.

## 1. Exact objects and the finding

Use the entire xi function, including its removable values,

\[
\xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),\qquad A(z)=\xi(1/2+iz).
\]

Let independent mean-one exponentials define

\[
X=\frac6{\pi^2}\sum_{j\ge1}\frac{E_j}{j^2},\qquad
L(t)=\mathbb E e^{-tX}=\frac{\sqrt{6t}}{\sinh\sqrt{6t}}.
\tag{1}
\]

The value at zero is one. All probability powers use the real logarithm. The Brownian/zeta identity of Biane--Pitman--Yor gives, with an independent copy X',

\[
\xi(2q)=\tfrac12(\pi/6)^q\mathbb E(X+X')^q. \tag{2}
\]

Their notation is X=3 Sigma_1, X+X'=3 Sigma_2 and Sigma_2=(2/pi)Y^2, with E Y^s=2xi(s). This is a classical imported identity, not a new result or an assumed zero geometry.

Let V have density (24/7)u^(-4) on [1,2], and define the independent perpetuity and its companion sum

\[
W=\sum_{j\ge1}\Big(\prod_{i=1}^j V_i^{-2}\Big)X_j,\qquad C=W+X_0,
\quad P(t)=\mathbb E e^{-tW},\quad H(t)=P(t)L(t).
\tag{3}
\]

These are the B_* and C_* of BRN26. We rename B_* to W to distinguish it from the entire odd companion

\[
G(s)=\tfrac12(\pi/6)^{s/2}(s/2)(s/2-1)\mathbb E C^{s/2-2},
\quad B(z)=\frac{G(1/2+iz)-G(1/2-iz)}{2i}. \tag{4}
\]

**BRN27-1 (native phase counterexample, certificate-backed).** At

\[
z_0=119/2+i/5,
\]

the complete-source certificate described here gives

\[
\boxed{-4{,}700{,}000< e^{119\pi/4}\operatorname{Im}(A(z_0)\overline{B(z_0)})
       <-4{,}600{,}000.} \tag{5}
\]

Consequently OPEN-BRN, which requires this phase to be strictly positive at every point of 0<Im z<1/2, is false. The positive exponential in (5) only rescales the sign. A(z_0) is not zero: its rescaled real part is near -373.256, enclosed away from zero by the certificate. Thus this is **not an off-line zeta zero**.

Equations (1)--(4), the lemmas in Sections 2--4, the implementation of the outward arithmetic and the full replay are the dependencies of (5). They need review; a checksum alone does not prove this assertion.

## 2. Whole-law bounds and the exact delay equation

Put a_j=integral_1^2 u^(-2j)du, so a_0=1 and a_j=(1-2^(1-2j))/(2j-1) for j>=1. Let b_j=a_(j+2)/a_2. The positive series (3) has finite mean because b_1=93/140<1; its mean is 93/47. The affine recursion and induction give every finite positive moment. C>=X gives every negative moment, since (1) decays exponentially in sqrt(t) on the positive real axis. In particular, the Mellin transform of C is entire.

Write x_n=E X^n/n!, p_n=E W^n/n! and h_n=E C^n/n!. The positive weighted-exponential representation of X gives x_n<=1 by convexity. Exactly,

\[
p_0=1,\quad p_n=\frac{b_n}{1-b_n}\sum_{j=0}^{n-1}p_jx_{n-j}. \tag{6}
\]

For n=1, b_1<2/3; for n>=2,

\[
b_n<\frac{24}{7(2n+3)}\le\frac2{n+2}.
\]

Induction in (6) now proves p_n<=n+1, and convolution gives h_n<=(n+1)(n+2)/2. Thus, for 0<=v<1,

\[
\mathbb E e^{vX}\le(1-v)^{-1},\qquad
\mathbb E e^{vW}\le(1-v)^{-2},\qquad
\mathbb E e^{vC}\le(1-v)^{-3}. \tag{7}
\]

These are bounds on the **whole** distributions, not finite moment matching. Their transforms are holomorphic on Re t>-1. In every disk of radius 1/2 centered on the imaginary axis, |L|<=2, |P|<=4 and |H|<=8. For J(r)=-d[L(-ir)^2]/dr, the bound is |J|<=16 in the corresponding r disk: use E[(X+X')exp((X+X')/2)]<=16. At the origin, disks of radius 3/4 instead give |H|<=64 and |J|<=128.

The distributional recursion W=V^(-2)(W+X) gives

\[
P(t)=\frac{24}{7}\int_1^2u^{-4}H(t/u^2)du.
\]

Change variables v=t/u^2 and differentiate, initially on positive t and then by analyticity. The result is

\[
\boxed{2tP'(t)+3P(t)=\frac{24}{7}\{H(t)-\tfrac18H(t/4)\}.} \tag{8}
\]

For p(r)=P(-ir), h(r)=H(-ir), precisely the same equation reads
2r p'(r)+3p(r)=(24/7)[h(r)-h(r/4)/8]. The delayed source at r/4 is retained, including its coefficient 1/8.

## 3. Mellin rotation without a left-half-plane assumption

For 0<Re q<1 define

\[
K(q)=\int_0^\infty r^{1-q}H(-ir)dr,\quad
J(q)=\int_0^\infty r^{-q}\left[-\frac d{dr}L(-ir)^2\right]dr,
\quad c(q)=\frac{(\pi/6)^q e^{i\pi q/2}}{2\Gamma(1-q)}.
\]

Then exactly

\[
\xi(2q)=c(q)J(q),\qquad G(2q)=q\,c(q)K(q). \tag{9}
\]

To justify rotation from positive t to t=-ir, use the sector -pi/2<=arg t<=0. Here |P(t)|<=1 and L(t) and its derivatives decay exponentially in sqrt(|t|), uniformly away from the origin. The large connecting arcs therefore vanish. Near zero the respective integrands are O(t^(-Re q)) and O(t^(1-Re q)), so their small arcs also vanish. One may first rotate through a strict sub-sector and then use dominated convergence to reach the boundary. No unproved continuation of P beyond the Laplace half-plane is used.

For G, the factor from t^(1-q)dt is -exp(i*pi*q/2). It cancels the sign in q(q-1)/Gamma(2-q)=-q/Gamma(1-q). For xi the derivative and dt factors cancel. These observations give both signs in (9).

At z_0 set q_1=3/20+(119/4)i and q_2=7/20+(119/4)i. Real-type reflection gives

\[
A(z_0)=c(q_1)J(q_1),\quad
B(z_0)=\frac{q_1c(q_1)K(q_1)-\overline{q_2c(q_2)K(q_2)}}{2i}.
\tag{10}
\]

The implementation evaluates precisely these three integrals. It does not ask a zeta oracle for A.

## 4. Complete future tails at r=512

For real r>=512, four iterations of (3) give

\[
P(-ir)=\mathbb E\left[\prod_{j=1}^4L(-ir A_1\cdots A_j)
                       P(-ir A_1\cdots A_4)\right],\qquad A_j=V_j^{-2}\in[1/4,1].
\]

The last factor has modulus at most one. From (1), |L(-is)|<=4 sqrt(6s)exp(-sqrt(3s)) whenever s>=2. The function u exp(-sqrt(3)u) decreases for u>=1/sqrt(3). Since r/4^4>=2, each factor is bounded using the **minimum possible argument**, not its average. Including the additional factor L(-ir), this proves

\[
|H(-ir)|\le36\sqrt6\,r^{5/2}\exp[-(31/16)\sqrt{3r}]
          <100r^{5/2}e^{-(31/16)\sqrt{3r}}. \tag{11}
\]

Both Re q_j are positive, so

\[
|K(q_j)\text{ tail}|\le200\int_{\sqrt{512}}^\infty u^8 e^{-(31/16)\sqrt3\,u}du. \tag{12}
\]

Differentiating the explicit L gives, on this tail,
|J(r)|<=96 exp(-2sqrt(3r))(1+5sqrt(r))<=576sqrt(r)exp(-2sqrt(3r)). Therefore

\[
|J(q_1)\text{ tail}|\le1152\int_{\sqrt{512}}^\infty u^2e^{-2\sqrt3\,u}du. \tag{13}
\]

For rational outward evaluation replace the lower limit by v=22627/1000<sqrt(512), the rate in (12) by 13423/4000<(31/16)sqrt(3), and that in (13) by 433/125<2sqrt(3). For integer d>=0,

\[
\int_v^\infty u^d e^{-au}du
=e^{-av}\sum_{j=0}^d\frac{d!}{(d-j)!}\frac{v^{d-j}}{a^{j+1}}. \tag{14}
\]

All constants are rational except the exponential, which is bounded by its explicit series remainder. These estimates include the entire future r tail and all omitted perpetuity levels.

## 5. How (5) is proved computationally

The full arithmetic and integration contract is in [CERTIFICATE.md](CERTIFICATE.md), with executable sources [ball_core.py](ball_core.py) and [certify.py](certify.py). The actual result is [result.json](result.json).

The implementation uses dyadic complex L1 balls at 512 bits. There is no NumPy, SciPy, mpmath, zeta, gamma or quadrature library in the accepting computation. Log gamma is evaluated by an explicitly bounded Stirling expansion and recurrence; its standard error bound is attributed to DLMF 5.11(ii). Every conversion from a complex absolute-value remainder to an L1 radius pays a factor two.

The origin is integrated through degree 384, with all higher terms bounded by (7). From r=1/2 to 512, all 4092 cells of width 1/8 use degree-80 Taylor models. Equation (8) produces the true companion derivatives from the earlier delayed models; Cauchy estimates from (7) bound every omitted term. The complex weights r^(1-q) and r^(-q) are integrated through their convergent binomial expansions with explicit full remainders. Finally (12)--(14) pay both future tails. Equation (10), with c multiplied by the positive scale exp(119*pi/8), produces (5).

For orientation only, the rescaled centers are approximately

```
A: -373.255720510058 - 295.710245779740 i
B: 94003.415134953  + 61971.846736050 i
phase: -4666426.688888
```

The full L1 radius of the final complex product is less than 4026. The accepting rule compares integer endpoints against -4700000 and -4600000, not these rounded values. In particular, the refutation is not an inference from agreement between floating runs.

## 6. A whole prescribed hierarchy, not an arbitrary next companion

The failure raises the structural question: which directions does the Brownian renormalization actually supply? The following construction answers it at every finite Taylor order.

For an integer m>=0, let V_m have density u^(-2m)/a_m on [1,2]. Define

\[
W_m=\sum_{j\ge1}\Big(\prod_{i=1}^jV_{m,i}^{-2}\Big)X_j,
\quad C_m=W_m+X_0,\quad P_m(t)=\mathbb E e^{-tW_m},\quad D_m(t)=t^mP_m(t).
\]

**BRN27-2 (positive eigenmode laws).** These series converge almost surely and in L1, every positive moment is finite, C_m has every negative moment, and

\[
\mathcal L D_m=\lambda_mD_m,\qquad
(\mathcal L f)(t)=2\int_1^2L(t/u^2)f(t/u^2)du,\qquad
\lambda_m=2a_m. \tag{15}
\]

Here L is the fixed source and mathcal L is its smoothing-map linearization, **not a characteristic operator whose eigenvalues encode the zeros of xi**.

**Proof.** Put b_(m,j)=a_(m+j)/a_m<1 for j>=1. The expected positive series is b_(m,1)/(1-b_(m,1)), proving convergence. Its moment recursion is (6) with b_n replaced by b_(m,n); induction on n gives finite moments. Since C_m>=X_0, (1) gives all inverse moments. Substituting the affine fixed-point equation for P_m in mathcal L(t^mP_m) proves (15). All exchanges on t>=0 use nonnegative/ bounded probability transforms. Near zero the moment bounds give a positive exponential-moment radius: choose a finite integer K with b_(m,n)<=K/(n+K) for all n>=1 (possible because b_(m,n)=O(1/n), with every b_(m,n)<1). The same induction bounds E W_m^n/n! by binomial(n+K-1,K-1). Thus analytic germs in (15) are justified. C_m's entire Mellin transform follows from positive and inverse moments and compact-set domination. QED.

**BRN27-3 (exact diagonalization of every finite jet).** Modulo t^(N+1), D_0,...,D_N form an eigenbasis of mathcal L, with distinct eigenvalues 2a_0,...,2a_N. Indeed D_m=t^m+O(t^(m+1)), so their coefficient matrix is triangular with unit diagonal; a_m strictly decreases. Consequently every finite Taylor jet of a perturbation has a unique decomposition into these modes, and its n-th **linearized** iterate multiplies each coordinate by (2a_m)^n. This is not an asserted convergent infinite eigenfunction expansion or a nonlinear zero-preservation theorem.

Define entire Mellin companions for these integer modes by

\[
G_m(2q)=\tfrac12(\pi/6)^q(-1)^m q(q-1)\cdots(q-m+1)\,\mathbb E C_m^{q-m}.
\tag{16}
\]

The empty product is one; let B_m be the same odd reflection as in (4). This definition uses no zero positions or fitted coefficients. The preceding counterexample concerns exactly m=2.

**BRN27-4 (the apparently positive neutral direction has a shared divisor).** Exactly,

\[
P_0=L,\quad P_1=-L',\qquad G_0(s)=\xi(s),\quad G_1(s)=-\frac{s}{4}\xi(s),
\qquad B_0=0,\quad B_1(z)=-\frac z4A(z). \tag{17}
\]

For m=0, the fixed source itself solves the affine equation; uniqueness follows by the mean contraction a_1/a_0<1. For m=1, differentiate the source fixed-point identity L(t)=integral L(t/u^2)^2 du. The function -L' is the Laplace transform of the size-biased X law because E X=1, and satisfies the P_1 equation. Uniqueness again follows from affine L1 contraction. Now C_1 has Laplace transform -L'L=-(L^2)'/2, the size-biased law of X+X'. Hence E C_1^(q-1)=E(X+X')^q/2. Substitution into (16) gives G_1 and its reflection in (17).

In particular,

\[
\operatorname{Im}(A(z)\overline{B_1(z)})=\frac{\operatorname{Im}z}{4}|A(z)|^2. \tag{18}
\]

This is positive wherever A is nonzero in the upper half-plane, but vanishes at **every** zero of A, including any hypothetical off-line zero. Treating (18) as a strict zero-exclusion inequality would be circular. The fact that this neutral mode tests positively at every nonzero sample point is not evidence that it resolves RH.

## 7. What was attempted beyond the failure

A noncertifying scout evaluates higher integer modes and a difference quotient near m=1. Those tests also find mixed phase signs for the inspected m=3,4,5,6 candidates; the neutral derivative has both signs. Their exact experimental scope is in SCOUTS.json. No additional mode is declared globally ruled out by a finite scout, and continuous-m experiments are not promoted to the integer-mode theorems above.

A possible continuation is to construct source-derived **signed combinations** of the genuine modes m>=2, with complete control of their phase and of common zeros. But no such global combination is constructed or claimed here. Positivity of the probability laws, positivity of the linearized eigenvalues, finite-jet diagonalization, and the neutral identity (18) do not supply it. This pass does not replace OPEN-BRN by another condition and call the missing condition proved.

The research outcome is therefore precise: the first prescribed phase target is false; the complete source can be evaluated with rigorous full tails; the available renormalization directions are explicitly identified; and an attractive common-zero shortcut is excluded. A complete RH proof was not obtained.
