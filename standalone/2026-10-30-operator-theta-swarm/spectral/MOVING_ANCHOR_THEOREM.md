# A moving-anchor Li covariance criterion and its unconditional blind regime

Status: proposed mathematical component with full proofs below; no RH proof or improved zero-free half-plane.

Scope: the actual completed Riemann xi function. The finite covariance criterion and Herglotz machinery are classical in substance. The contribution developed here is the cofinal moving-anchor criterion, its degree/anchor scaling, and a matching qualitative obstruction supplied by an unconditional large-anchor positivity theorem. No worldwide priority claim is made.

Exact dependencies: the standard entire xi function, its functional equation and zero strip; its logarithmic-derivative partial fraction identity; the finite trigonometric moment theorem; Schwarz's lemma and normal families; the digamma Binet formula. Detailed source URLs are in SOURCES.md.

What was actually run: see verify_spectral.py and its output. Numerical checks are diagnostics, not directed interval certificates or an infinite positivity proof.

Smallest remaining gap: control of the actual covariance matrices in a cofinal regime N/a_N tending to infinity. The unconditional theorem below reaches the opposite regime.

## 1. Exact source and covariance

Write

\[
 \xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),\qquad
 f(s)=\xi'(s)/\xi(s).
\]

For a real anchor parameter \(a\ge1\), put \(\sigma_a=1/2+a\),

\[
 s_a(z)=\tfrac12+a\frac{1+z}{1-z},\qquad
 C_a(z)=2af(s_a(z))=c_0(a)+2\sum_{n\ge1}c_n(a)z^n.
\]

The series is initially local at zero; no analyticity throughout the unit disk is assumed. The coefficients are real. Let

\[
 T_N(a)=(c_{j-k}(a))_{0\le j,k\le N},\quad c_{-n}=c_n.
\]

These are actual xi coefficients, not a zero-truncated model. If

\[
 \log\frac{\xi(s_a(z))}{\xi(\sigma_a)}
   =\sum_{n\ge1}\frac{\lambda_n(a)}n z^n,
 \qquad \lambda_0(a)=0,
\]

then direct differentiation gives

\[
 c_0=\lambda_1=2af(\sigma_a),\qquad
 2c_n=\lambda_{n+1}-2\lambda_n+\lambda_{n-1}\quad(n\ge1).
\]

Thus these are discrete second differences of generalized Li coefficients. At a=1/2 this is the ordinary Li normalization, but the arguments below use anchors safely to the right of one.

For later use, the classical partial fraction identity gives, wherever \(\sigma>1\),

\[
 \Re f(\sigma+it)=
 \sum_\rho\frac{\sigma-\Re\rho}
 {(\sigma-\Re\rho)^2+(t-\Im\rho)^2}>0.
\tag{1}
\]

The real-part sum converges absolutely locally away from zeros. This uses only the unconditional zero strip \(0<\Re\rho<1\), not RH. Under RH the same formula is positive for every \(\sigma>1/2\).

## 2. Cofinal moving anchors: no logarithmic loss

**Theorem 1.** Let \(N_j\) be positive integers and \(a_j\ge1\), with

\[
 \frac{N_j}{a_j}\longrightarrow\infty.
\tag{2}
\]

Then RH is equivalent to \(T_{N_j}(a_j)\succeq0\) for every j. It is also equivalent to this positivity holding for all sufficiently large j, or merely along a subsequence for which (2) holds.

**Proof, forward direction.** Under RH, (1) holds on the half-plane \(\Re s>1/2\). Therefore \(C_a\) is analytic with positive real part in the unit disk. Its Herglotz measure makes every Toeplitz matrix \(T_N(a)\) positive semidefinite.

**Proof, reverse direction.** Fix a positive semidefinite matrix in the proposed sequence. The finite trigonometric moment theorem supplies a finite positive measure \(\mu_j\) on the unit circle with moments \(c_n(a_j)\) for \(|n|\le N_j\). It follows that there is a holomorphic function \(H_j\) on the unit disk with nonnegative real part and

\[
 H_j(z)=c_0(a_j)+2\sum_{n=1}^{N_j}c_n(a_j)z^n+O(z^{N_j+1}).
\]

Define on \(\Re s>1/2\)

\[
 F_j(s)=\frac1{2a_j}H_j\!\left(
  \frac{s-1/2-a_j}{s-1/2+a_j}\right).
\]

It has nonnegative real part and agrees with f through Taylor degree \(N_j\) at \(\sigma_j=1/2+a_j\). Degenerate Toeplitz matrices cause no problem: the representing measure can be finitely supported. Also \(c_0(a_j)>0\), by (1), so the representing function is not identically zero.

Apply the fixed Cayley transform

\[
 B_j(s)=\frac{F_j(s)-1}{F_j(s)+1},\qquad
 B(s)=\frac{f(s)-1}{f(s)+1}.
\]

Each \(B_j\) is a disk-valued holomorphic function on \(\Re s>1/2\). By (1), B is disk-valued on \(\Re s>1\). On this latter half-plane, \(B_j-B\) is bounded in modulus by two and has a zero of order at least \(N_j+1\) at \(\sigma_j\). The repeated Schwarz lemma, after mapping that half-plane to the disk, therefore gives the exact bound

\[
 |B_j(s)-B(s)|\le
 2\left|\frac{s-\sigma_j}{s+\sigma_j-2}\right|^{N_j+1},
 \qquad \Re s>1.
\tag{3}
\]

The denominator has no zero there. For each fixed real \(s_0>1\), the right side tends to zero under (2). If \(a_j\) stays bounded, the modulus is bounded away from one; if it is unbounded, its logarithm is \(-2(s_0-1)/a_j+O_{s_0}(a_j^{-2})\). The same convergence holds locally on the safe half-plane, or alternatively on all its real points followed by the identity theorem.

The family \(B_j\) is normal on the entire critical right half-plane. Every convergent subsequence has a holomorphic disk-valued limit \(\widetilde B\) agreeing with B on \(\Re s>1\). Since \(|B(s_0)|<1\), the maximum principle ensures \(|\widetilde B|<1\) throughout \(\Re s>1/2\). Consequently

\[
 \widetilde f=\frac{1+\widetilde B}{1-\widetilde B}
\]

is holomorphic on that half-plane and agrees with f in the safe region. The analytic identity

\[
 \xi'(s)=\widetilde f(s)\xi(s)
\]

holds throughout by analytic continuation. A nonzero analytic solution of this first-order equation has no zeros in the domain: a zero of multiplicity m would give orders m-1 and m on its two sides. Thus xi has no zero with real part exceeding 1/2. The functional equation supplies RH. This proves the theorem.

**Why the scale is useful.** A coefficient-tail estimate would introduce a spurious logarithmic factor through the growing value \(f(\sigma_a)\). The Cayley-transform Schwarz estimate (3) avoids this. Arbitrarily slowly diverging \(N_j/a_j\) is sufficient. This is an exact criterion, not a claim that its matrices have been proved positive.

## 3. An unconditional regime that cannot settle RH

**Theorem 2.** For every integer \(N\ge1\) and every real

\[
 a\ge100(N+1),
\]

the actual xi covariance matrix satisfies

\[
 T_N(a)\succ \frac a6 I.
\tag{4}
\]

This theorem is unconditional. It supplies all-order positivity along, for example, \(a_N=100(N+1)\), but that family does not meet Theorem 1's detection condition.

**Proof.** In \(\Re s>1\), separate the source exactly as

\[
 f(s)=\tfrac12\log(s/(2\pi))+R(s),
\]

\[
 R(s)=\frac1s+\frac1{s-1}
 +\tfrac12\big(\psi(s/2)-\log(s/2)\big)
 -\sum_{m\ge2}\frac{\Lambda(m)}{m^s}.
\tag{5}
\]

All logarithms have their analytic right-half-plane branches. Put
\(q=(a-1/2)/(a+1/2)\in(0,1)\). The main term is

\[
 C_a^0(z)=a\log(\sigma_a/(2\pi))
 +a\log(1+qz)-a\log(1-z).
\]

Its Toeplitz diagonal is \(a\log(\sigma_a/(2\pi))\), and its n-th off-diagonal is

\[
 \frac a{2n}\big(1+(-1)^{n+1}q^n\big)>0.
\]

The sum of the alternating decreasing terms \(\sum_{n=1}^N(-1)^{n+1}q^n/n\) is at most q, hence at most one. The elementary shift bound therefore gives

\[
 \lambda_{\min}(T_N^0)
 \ge a\left[\log\frac{\sigma_a}{2\pi}-H_N-1\right]
 >a\left[\log\frac{100}{2\pi}-2\right]>rac a2.
\tag{6}
\]

Here \(H_N\le1+\log N\), and the final strict elementary inequality follows, for example, from \(\pi<22/7\) and \(e<11/4\).

To control the complete remainder without summing coefficient errors separately, let S be the nilpotent unilateral shift on \(\mathbb C^{N+1}\), with \(S^{N+1}=0\), and let \(r=N/(N+1)\). On \(|z|\le r\),

\[
 \Re s_a(z)\ge\frac12+a\frac{1-r}{1+r}
 =\frac12+\frac a{2N+1}>50.
\]

Binet's formula, factored as \(t^2+w^2=(w+it)(w-it)\), yields for \(x=\Re s>0\)

\[
 \left|\psi(s/2)-\log(s/2)+\frac1s\right|
 \le\frac1{3x^2}.
\]

Indeed the corresponding bound for \(w=s/2\) is \(1/[12(\Re w)^2]\), because \(2\int_0^\infty t/(e^{2\pi t}-1)\,dt=1/12\). Thus, for x>50,

\[
 |R(s)|\le\frac{3}{2x}+\frac1{x-1}+\frac1{6x^2}
 +\sum_{m\ge2}\frac{\log m}{m^x}<\frac1{19}.
\tag{7}
\]

For an entirely coarse elementary tail bound, use \(\log m\le m\) and
\(\sum_{m\ge2}m^{-49}\le2^{-49}+2^{-48}/48<1/1000\). Then the right side of (7) is below
\(3/100+1/49+1/15000+1/1000<1/19\).

Write \(E(z)=2aR(s_a(z))\). It is analytic in a neighborhood of \(|z|\le r\) and bounded there by \(2a/19\). For a diagonal similarity D with condition number \(r^{-N}<e<3\),

\[
 E(S)=D E(rS)D^{-1}.
\]

The contraction functional calculus for the nilpotent shift gives
\(\|E(rS)\|\le\sup_{|z|\le r}|E(z)|\). This can also be obtained directly by realizing \(E(rS)\) as a compression of multiplication by \(E(rz)\) on the Hardy space. Therefore

\[
 \|\Re E(S)\|\le\|E(S)\|<\frac{6a}{19}.
\tag{8}
\]

The Toeplitz source identity is exactly
\(T_N(a)=T_N^0+\Re E(S)\), since \(T_N(a)=\Re C_a(S)\). Combining (6)--(8),

\[
 \lambda_{\min}(T_N(a))>
 a\left(\frac12-\frac6{19}\right)
 =\frac{7a}{38}>\frac a6.
\]

No RH or finite zero census entered this argument.

## 4. Exact arithmetic coefficients and finite dissipative realization

The ordinary generating identity

\[
 \exp\!\left(-\frac{xz}{1-z}\right)
 =\sum_{n\ge0}L_n^{(-1)}(x)z^n
\]

turns the prime contribution in (5) into the absolutely convergent coefficient formula

\[
 c_n^{\rm prime}(a)=
 -a\sum_{m\ge2}\Lambda(m)m^{-\sigma_a}
 L_n^{(-1)}(2a\log m),\qquad n\ge1,
\tag{9}
\]

while \(c_0^{\rm prime}=-2a\sum_m\Lambda(m)m^{-\sigma_a}\). The diagonal factor of two is essential. For each fixed n, the Laguerre polynomial has finite degree, so absolute convergence follows from \(\sigma_a>1\).

There is a compact exact realization. Define

\[
 A_N=\tfrac12I+a(I+S)(I-S)^{-1},\qquad
 B_N=A_N-\tfrac12I,
\]

and let \(\mathbf1=(1,\ldots,1)^T\). Then

\[
 \Re B_N=a\mathbf1\mathbf1^*,\qquad
 T_N(a)=\Re\{2af(A_N)\}.
\tag{10}
\]

The matrix function is defined by the finite Taylor expansion at the sole eigenvalue \(\sigma_a>1\); no matrix inverse of xi at unknown zeros is assumed. Every prime is the same semigroup evaluated at its logarithm:

\[
 m^{-A_N}=e^{-(\log m)A_N}.
\]

If \(U_t=e^{-tB_N}\), differentiation gives the exact rank-one energy identity

\[
 I-U_t^*U_t
 =2a\int_0^t U_v^*\mathbf1\mathbf1^*U_v\,dv\succeq0.
\tag{11}
\]

Thus each prime operator is contractive with
\(\|m^{-A_N}\|\le m^{-1/2}\). This does **not** justify summing those norm bounds: \(\sum\Lambda(m)m^{-1/2}\) diverges. For each fixed N the actual matrix series still converges, because its entries are \(m^{-\sigma_a}\) times polynomials in \(\log m\). Equation (11) retains the common rank-one observation vector and the exact prime phases; replacing the sum by independent absolute norms destroys precisely the cancellation needed beyond the easy regime.

## 5. Translation model and an exact completeness threshold

Choose the upper shift convention \(S_{j,j+1}=1\). Define the observation map

\[
 (\mathcal O_{N,a}q)(u)=\sqrt{2a}\,\mathbf1^*U_uq,
 \qquad u\ge0.
\]

Since the only eigenvalue of \(B_N\) is a>0, \(U_t\to0\) as t tends to infinity. Taking the limit of (11) proves that \(\mathcal O_{N,a}\) is an isometry from \(\mathbb C^{N+1}\) into \(L^2(0,\infty)\). The finite Laguerre expansion, or summing the \(L_k^{(-1)}\) coefficients, gives

\[
 \mathcal O_{N,a}e_j(u)=\sqrt{2a}\,e^{-au}L_j(2au),
 \qquad 0\le j\le N,
\tag{12}
\]

where \(L_j=L_j^{(0)}\). Thus its range is the classical finite Laguerre space

\[
 V_{N,a}=\{e^{-au}p(u):\deg p\le N\}.
\]

The semigroup law gives an exact intertwining with right translation of the argument:

\[
 \mathcal O_{N,a}(U_tq)(u)=\mathcal O_{N,a}q(u+t).
\tag{13}
\]

Consequently, for \(\phi=\mathcal O_{N,a}q\),

\[
 \langle q,m^{-A_N}q\rangle
 =m^{-1/2}\int_0^\infty\overline{\phi(u)}\phi(u+\log m)\,du.
\tag{14}
\]

The prime side is a common autocorrelation sampled at the actual logarithms of prime powers. Independent contractivity estimates discard those correlations.

**Theorem 3 (sharp completeness scale).** Let \(a_j\ge1\), and let \(P_j\) be the orthogonal projection onto \(V_{N_j,a_j}\). Then

\[
 P_j\longrightarrow I\text{ strongly on }L^2(0,\infty)
 \quad\Longleftrightarrow\quad
 N_j/a_j\longrightarrow\infty.
\tag{15}
\]

**Proof.** For \(b>0\), put \(h_b(u)=\sqrt{2b}e^{-bu}\), a unit vector. The finite polynomial identity

\[
 \int_0^\infty e^{-pu}L_n(qu)\,du=
 \frac{(p-q)^n}{p^{n+1}},\qquad p>0,
\]

gives the exact coefficients

\[
 \langle\sqrt{2a}e^{-au}L_n(2au),h_b\rangle
 =\frac{2\sqrt{ab}}{a+b}
 \left(\frac{b-a}{b+a}\right)^n.
\]

Summing the geometric series yields

\[
 \|(I-P_{N,a})h_b\|_2^2=
 \left|\frac{a-b}{a+b}\right|^{2(N+1)}.
\tag{16}
\]

If N_j/a_j tends to infinity, this error tends to zero for every fixed b>0. The linear span of these exponentials is dense in \(L^2(0,\infty)\), by uniqueness of the Laplace transform, and orthogonal projections have norm at most one. Hence convergence extends to every vector.

Conversely, take b=1/2. If N_j/a_j fails to tend to infinity, a subsequence has N_j/a_j bounded by some constant M. Since a_j≥1 and

\[
 -\log\frac{a-1/2}{a+1/2}
 =2\operatorname{artanh}(1/(2a))\le\frac2a,
\]

(16) is at least \(\exp[-4(M+1)]\) along that subsequence. Strong convergence is impossible. This proves (15).

This is a sharp threshold for completeness of the test spaces, not a proof that every incomplete family fails to characterize this one fixed source. Strong L² convergence alone also does not justify passing an unbounded Weil form to the limit. The independent normal-family proof of Theorem 1 supplies the actual RH implication without that unsupported form-domain step.

## 6. The same construction for a target zero-free boundary

Fix \(b\in[1/2,1)\), and replace \(s_a(z)\) by

\[
 s_{b,a}(z)=b+a\frac{1+z}{1-z},\qquad a\ge1.
\]

Let \(T_N^{(b)}(a)\) be the corresponding Toeplitz matrix from \(2af(s_{b,a}(z))\).

**Corollary 4.** For any sequence \(a_j\ge1\), \(N_j/a_j\to\infty\), the assertion that xi has no zeros with real part exceeding b is equivalent to \(T_{N_j}^{(b)}(a_j)\succeq0\) for all sufficiently large j.

**Proof.** If the stated half-plane is zero-free, all xi zeros have real part at most b, so the partial fraction identity makes f positive real there. Conversely, the finite Herglotz extensions are positive real on \(\Re s>b\); their Cayley transforms converge to the known source on \(\Re s>1\) by (3), now with \(\sigma_j=b+a_j\). The normal-family and first-order analytic-ODE argument then exclude zeros on \(\Re s>b\). No reflected lower boundary is needed for this conclusion.

The unconditional inequality (4) remains valid with \(T_N^{(b)}\): replace \(\sigma_a\) by a+b and q by \((a-b)/(a+b)\) in its proof. In its asserted regime a>=100(N+1), q remains in (0,1), and the minimum safe real part is b+a/(2N+1)>50. The translation realization becomes

\[
 A_N=bI+a(I+S)(I-S)^{-1},\quad
 \langle q,m^{-A_N}q\rangle
 =m^{-b}\int_0^\infty\overline{\phi(u)}\phi(u+\log m)\,du.
\]

This offers a target-specific interface for a proposed smaller boundary b. It does not supply the needed cofinal positivity at any b below a boundary already known by independent methods.

## 7. Explicit unfinished next step

The one-step Schur complement, whenever \(T_{N-1}(a)\) is positive definite, is

\[
 e_N(a)=c_0(a)-v_N(a)^*T_{N-1}(a)^{-1}v_N(a),
 \quad v_N=(c_N,c_{N-1},\ldots,c_1)^T.
\]

Positivity of this scalar extends the matrix by one degree. The exact arithmetic data for it are (5), (9), and (10), but no positive formula for this scalar at cofinal \(N/a\to\infty\) is proved here. Equation (11) alone is insufficient: it is available for every positive real a and every N, whereas the desired inequality concerns the signed sum with gamma compensation.

The theorem identifies a concrete analytic goal: establish a source-specific nonnegative innovation bound in a sequence of ratios N/a tending to infinity, using the common semigroup rather than absolute prime bounds. A proof only for a proportional to N, including the complete unconditional family (4), cannot be promoted to RH through Theorem 1.
