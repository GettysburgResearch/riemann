# The actual theta ground-state form and delocalization of safely shifted resolvents

Status: proposed analytic component theorems, with complete proofs below.
Scope: the ordinary Riemann xi source and its full semilocal Weil form.
No new zero-free region or RH proof is claimed.
Date: 24 October 2026.

This note pursues a different mechanism from the recent character-moment
estimates. It first converts the exact theta annihilator into a weighted jump
form. It then proves that a broad class of the real-zero resolvent functions
constructed in PR #1017 cannot converge locally uniformly to Xi. This is a
specific obstruction to that selection rule, not an obstruction to the
Hilbert--Polya programme or to all resolvent constructions.

## 1. Source and normalization

Put

\[
 \Xi(z)=\xi(1/2+iz),\qquad X(z)=\Xi(z)/\Xi(0),
\]

and use the Fourier convention \(\widehat f(z)=\int_{\mathbb R}f(x)e^{-izx}dx\).
The even, strictly positive, smooth probability density \(\phi\) is

\[
 \phi(x)=\Xi(0)^{-1}\sum_{n\ge1}
 (4\pi^2n^4e^{9x/2}-6\pi n^2e^{5x/2})e^{-\pi n^2e^{2x}},\quad x\ge0,
 \qquad \phi(-x)=\phi(x).
\]

The classical theta formula gives \(\widehat\phi=X\). Positivity follows
term by term on \(x\ge0\) from \(2\pi n^2e^{2x}>3\). For fixed \(j\),

\[
 |\phi^{(j)}(x)|\le C_j
 \exp((9/2+2j)|x|-\pi e^{2|x|})\qquad(|x|\ge1).                 \tag{1}
\]

The positive \(n=1\) term also gives
\(\phi(x)\ge c\exp((9/2)|x|-\pi e^{2|x|})\) for \(|x|\ge1\).
In particular \(|\phi^{(j)}(x)|/\phi(x)=O(e^{2j|x|})\). This lower
bound is used whenever division by \(\phi\) occurs below.

Let

\[
 A(t)=\frac{e^{-t/2}}{1-e^{-2t}}\quad(t>0),\qquad c_0=\log(4\pi)+\gamma.
\]

On smooth functions with sufficient decay, the additive Weil convolution
operator is

\[
\begin{split}
(K_W*f)(x)={}&2\int_{\mathbb R}\cosh((x-y)/2)f(y)dy-c_0f(x)\\
&-\int_0^\infty A(t)
 [f(x+t)+f(x-t)-2e^{-t/2}f(x)]dt\\
&-\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
 [f(x+\log n)+f(x-\log n)].                                    \tag{2}
\end{split}
\]

The cancellation inside the archimedean integral is part of the definition.
Every prime power appears. For compactly supported smooth \(f\), set
\(q[f]=\int\overline f(K_W*f)\). Restriction to \([-a,a]\), with zero
extension, is the closed, lower bounded form \(q_a\), with associated
self-adjoint operator \(A_a\) and lowest eigenvalue \(\lambda_0(a)\).

We use the classical explicit formula and theta identity to obtain

\[
 K_W*\phi=0.                                                    \tag{3}
\]

Indeed the zero-side transform of the convolution contains \(X(z_\rho)\)
at \(z_\rho=(\rho-1/2)/i\), which vanishes for every nontrivial zero,
irrespective of its real part. The fixed-strip exponential Fourier decay
of Xi and the unconditional \(O(T\log T)\) zero count justify the sum.
The arithmetic side is absolutely convergent after the local cancellation
in (2), by (1). Testing against compact smooth functions therefore proves
(3) distributionally; (2) makes its left side continuous, so it holds
pointwise. This identity does not assume RH.

All the above source facts are classical, or are the standard operator
realization of the Weil form. PR #1017 uses the same normalization. Its
approximate-null-vector estimate is not assumed below: the cutoff and
convolution bounds needed here are proved explicitly.

## 2. Exact weighted jump identity

For \(g\in C_c^\infty(\mathbb R)\), put \(f=\phi g\). Define

\[
 \begin{split}
 E_\infty[g]&=\int_0^\infty A(t)\int_{\mathbb R}
       \phi(x)\phi(x+t)|g(x+t)-g(x)|^2dx\,dt,\\
 E_p[g]&=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
       \int_{\mathbb R}\phi(x)\phi(x+\log n)
       |g(x+\log n)-g(x)|^2dx,\\
 E_h[g]&=\iint_{\mathbb R^2}\cosh((x-y)/2)\phi(x)\phi(y)
       |g(x)-g(y)|^2dx\,dy.
 \end{split}                                                    \tag{4}
\]

**Theorem 1 (complete theta jump form).** All three quantities in (4) are
finite, and

\[
                  q[\phi g]=E_\infty[g]+E_p[g]-E_h[g].           \tag{5}
\]

*Proof.* The difference in (4) is \(O(t)\) near zero, uniformly where
either term is nonzero; \(A(t)=O(1/t)\), so the archimedean singularity is
integrable. All distant terms converge by (1), including the entire prime
sum using \(\Lambda(n)\le\log n\). For a regularized symmetric convolution
kernel, expand \(|g(x)-g(y)|^2\). The two square terms give
\(2\int\phi(x)|g(x)|^2(K_W*\phi)(x)dx=0\), by (3). The cross terms give
\(-2q[\phi g]\). Removing the regularization is justified by the preceding
bounds. The diagonal distribution contributes zero because the difference
vanishes at \(x=y\). The two symmetric prime atoms give exactly the second
line of (4), with no missing factor two. The continuous off-diagonal part
of (2) is \(2\cosh(t/2)-A(|t|)\), giving (5). QED.

Since \(\phi\) is positive and smooth, every compact smooth \(f\) equals
\(\phi g\) with compact smooth \(g\). Consequently the global inequality

\[
                  E_\infty[g]+E_p[g]\ge E_h[g]\quad
                  (g\in C_c^\infty)                            \tag{6}
\]

is exactly a source-specific Weil-positivity criterion. It is not proved
here. The right side cannot be discarded or treated as an unsigned error.

### 2.1 Why two pole constraints do not remove the difficult term

Write

\[
 M=\int\cosh(x/2)\phi(x)dx=\frac{1}{2\Xi(0)},\quad
 c_f=\int\cosh(x/2)f(x)dx,\quad s_f=\int\sinh(x/2)f(x)dx.
\]

Expanding the hyperbolic difference gives the exact identity

\[
 E_h[g]=2M\int\cosh(x/2)\frac{|f(x)|^2}{\phi(x)}dx
              -2|c_f|^2+2|s_f|^2.                              \tag{7}
\]

Thus imposing \(\widehat f(i/2)=\widehat f(-i/2)=0\) removes the last
two rank-one terms but leaves the positive multiplication integral in
(7), which enters (5) with a negative sign. It would be incorrect to call
(5) a positive jump form on that constrained subspace without proving
the remaining weighted inequality.

### 2.2 The limiting problem has infinitely many neutral directions

Convolution of (3) with a compact smooth \(h\) gives
\(K_W*(\phi*h)=0\). Every derivative \(\phi^{(k)}\) is also annihilated.
For example, the functions

\[
 f_k=(\partial_x^2-1/4)\phi^{(k)},\qquad k\ge1,                 \tag{8}
\]

are nonzero and linearly independent, have integral zero, and satisfy
both pole constraints. Their weighted square integrals in (7) are finite
by (1) and the lower bound following it. For the prime-energy convergence,
the elementary envelope \(\phi(y)\ll e^{-2|y|}\), split at
\(n=e^{|x|}\), gives
\(\sum_{n\ge2}\Lambda(n)n^{-1/2}
[\phi(x+\log n)+\phi(x-\log n)]
\ll(1+|x|)e^{|x|/2}\).
Together with the derivative-ratio bounds, this supplies an integrable
dominating function. The local archimedean part uses the same derivative
ratio bounds and a first difference, and its distant part is exponentially
integrable. Smooth truncation therefore extends (5) to these functions
and gives equality in (6), in its natural weighted completion.

Independence follows on Fourier transforming: a finite linear dependence
would make a nonzero polynomial times \(X(z)\) identically zero. The pole
constraints follow by integration by parts, because
\((\partial_x^2-1/4)e^{\pm x/2}=0\). The integral is zero for \(k\ge1\).
This is why a strictly positive gap after removing only finitely many
scalar directions cannot be the full-line mechanism.

## 3. Delocalized approximate null vectors

Fix a nonnegative \(\eta\in C_c^\infty((-1,1))\) of integral one. Set
\(L=a/2\), \(\eta_L(x)=L^{-1}\eta(x/L)\), and

\[
 w_a=\phi*\eta_L.
\]

Choose a fixed smooth cutoff profile and let \(\chi_a\) equal one on
\([-a+1,a-1]\), vanish outside \((-a,a)\), and have first derivative
bounded independently of \(a\). Write

\[
 m_a=\int\chi_aw_a,\qquad v_a=\chi_aw_a/m_a.
\]

**Theorem 2 (mass-one delocalized theta vectors).** There are constants
\(C,c,a_0>0\), depending only on the fixed profiles, such that for all
\(a\ge a_0\),

\[
 \int v_a=1,\qquad
 \|v_a\|_2^2\le C/a,\qquad
 |q_a[v_a]|\le\varepsilon_a,
 \quad\varepsilon_a=C\exp(Ca-c e^a).                            \tag{9}
\]

In addition \(v_a\) is smooth with compact support in \((-a,a)\), so
there is no form-domain or boundary ambiguity.

*Proof.* Young's inequality and \(\|\phi\|_1=1\) give
\(\|w_a\|_2\le\|\eta_L\|_2\ll a^{-1/2}\). The mass outside
\([-a+1,a-1]\) tends to zero super-exponentially: for \(|x|\ge a-1\)
and \(|y|\le a/2\), one has \(|x-y|\ge |x|-a/2\), and (1) bounds
\(\phi(x-y)\) and its first derivative. Thus \(m_a\to1\), and the
norm assertion follows.

For completeness, put \(r_a=(1-\chi_a)w_a\). The same bound, including
the fixed transition layer, gives

\[
 |r_a(x)|+|r_a'(x)|\le B_a e^{-2|x|},\qquad
 B_a\le C\exp(Ca-c e^a).                                      \tag{10}
\]

This follows by maximizing the exponent for \(|x|\ge a-1\); for large
\(a\) it is decreasing there. The factor \(e^{2|x|}\), the linear
exponents in (1), and the cutoff derivative are absorbed into \(Ca\).
The main negative term at the boundary is
\(-\pi e^{2((a-1)-a/2)}=-\pi e^{a-2}\), so some fixed \(c>0\) works.

Convolution and (3) imply \(K_W*w_a=0\). Hence

\[
 A_a(\chi_aw_a)=-(K_W*r_a)|_{[-a,a]}.                           \tag{11}
\]

In (2), the pole term of \(K_W*r_a\) on \([-a,a]\) is
\(O(B_ae^{a/2})\). For \(0<t\le1\), rewrite the archimedean bracket
as two first differences plus \(2(1-e^{-t/2})r_a(x)\); (10) makes it
\(O(B_at)\), canceling the \(1/t\) singularity. The remaining
archimedean integral is \(O(B_a)\). For all prime powers, including
those beyond \(e^{2a}\), use

\[
 e^{-2|x\pm\log n|}\le e^{2a}n^{-2},\qquad
 \sum_{n\ge2}(\log n)n^{-5/2}<\infty.
\]

The prime contribution is therefore \(O(B_ae^{2a})\), uniformly on
\([-a,a]\). Equation (11) gives
\(\|A_av_a\|_2\ll \sqrt a B_ae^{2a}\). Pairing with
\(\|v_a\|_2\ll a^{-1/2}\) proves (9), after changing \(C,c\).
All exchanges involve a compact convolution or the absolutely convergent
resources just displayed. QED.

The broadening is essential: PR #1017's cutoff of \(\phi\) has a fixed
positive limiting \(L^2\) norm. The vectors in (9) have the same total
mass, still annihilate the full source before cutoff, and have vanishing
\(L^2\) norm. They supply lower-energy competitors for a sufficiently
negative regularizing shift.

## 4. A quantitative obstruction to safely shifted resolvent selection

Let \(\kappa_a<\min(0,\lambda_0(a))\), set

\[
 u_a=(A_a-\kappa_a)^{-1}\mathbf1,
 \qquad f_a=\frac{u_a}{\int u_a},\qquad F_a=\widehat f_a.
\]

Coercivity makes \(\int u_a>0\). The normalized vector is the unique
minimizer of \(q_a[f]+|\kappa_a|\|f\|_2^2\) under \(\int f=1\),
including complex-valued test functions. Write
\(d_a=\lambda_0(a)-\kappa_a>0\).

**Theorem 3 (resolvent delocalization).** With \(C,\varepsilon_a\) as in
(9),

\[
 \boxed{\displaystyle
 \|f_a\|_2^2\le
 \frac{C|\kappa_a|/a+\varepsilon_a}{d_a}.}                      \tag{12}
\]

If

\[
 \frac{C|\kappa_a|/a+\varepsilon_a}{d_a}\longrightarrow0,        \tag{13}
\]

then \(F_a\) has no locally uniformly convergent subsequence on any
complex neighborhood of zero. In particular it cannot converge locally
uniformly to \(X\).

*Proof.* Coercivity and minimality, with competitor \(v_a\), give

\[
 d_a\|f_a\|_2^2
 \le q_a[f_a]+|\kappa_a|\|f_a\|_2^2
 \le q_a[v_a]+|\kappa_a|\|v_a\|_2^2
 \le\varepsilon_a+C|\kappa_a|/a.
\]

Under (13), Plancherel implies
\(\int_{\mathbb R}|F_a(t)|^2dt=2\pi\|f_a\|_2^2\to0\).
If a subsequence converged locally uniformly on a neighborhood of zero
to a holomorphic function \(F\), its restriction to a real interval
would have zero \(L^2\) norm. Thus \(F\) would vanish on that interval
and identically near zero. But \(F_a(0)=1\) for every \(a\), so
\(F(0)=1\), a contradiction. QED.

**Corollary 3.1.** The conclusion holds whenever

\[
 d_a\ge c_1|\kappa_a|\quad\text{for a fixed }c_1>0,
 \qquad \varepsilon_a/|\kappa_a|\to0.                           \tag{14}
\]

This allows \(\kappa_a\to0\), provided it does not do so at the
super-exponential residual scale and the stated relative spectral
margin remains available. It also includes fixed negative shifts
wherever their legality and relative margin hold.

### 4.1 An explicit unconditional safely shifted family

The elementary source lower bound used in PR #1017 is

\[
 b_a=-\gamma-\pi/2-3\log2-\log\pi
       -2(\sinh a-a)
       -2\sum_{2\le n\le e^{2a}}\frac{\Lambda(n)}{\sqrt n},
 \qquad \lambda_0(a)\ge b_a.                                  \tag{15}
\]

It follows from the digamma lower bound, the pole decomposition into
cosh and sinh rank-one terms, and the norm-one bound on each partial
translation. In particular \(b_a<0\).

Choose the completely explicit legal shift

\[
                     \kappa_a=2b_a-1.                          \tag{16}
\]

Then
\(d_a\ge1-b_a=(|\kappa_a|+1)/2\), and \(|\kappa_a|\ge1\).
Consequently (12) gives \(\|f_a\|_2^2\le C'/a+2\varepsilon_a\to0\).
Thus this safely shifted family is unconditionally nonnormal at zero.
Each member still has the real-zero property supplied by PR #1017's
domain-safe de Branges argument. Real zeros of each approximant therefore
do not supply convergence to the intended Xi source.

The theorem does **not** assert that every legal shift obeys (13), nor
that source-sensitive bottom projections cannot converge. In particular
it leaves the narrow regime \(d_a/|\kappa_a|\to0\) and the residual-scale
regime open. No conclusion about Gaussian-compensated normality is drawn
from (12) alone; multiplication by an unbounded exponential factor changes
the real-axis \(L^2\) argument.

### 4.2 A quantitative window for a different selection rule

The inherited real-zero theorem gives an even entire function of
exponential type, with \(F_a(0)=1\). Hence its paired canonical product is

\[
 F_a(z)=\prod_j(1-z^2/t_{a,j}^2),\qquad
 V_a=-F_a''(0)=2\sum_jt_{a,j}^{-2}>0.                           \tag{17}
\]

For real \(|t|\le V_a^{-1/2}\), every factor is nonnegative, and
\(\prod_j(1-r_j)\ge1-\sum_jr_j\) gives \(F_a(t)\ge1/2\).
Plancherel therefore yields

\[
 \|f_a\|_2^2\ge\frac{1}{4\pi\sqrt{V_a}},\qquad
 V_a\ge\frac{1}{16\pi^2\|f_a\|_2^4}.                           \tag{18}
\]

Thus the explicit safe family (16) has \(V_a\gg a^2\). A possible
replacement is to allow the full legal range \(\kappa<\lambda_0(a)\)
(including positive shifts if they are legal) and select by the equation

\[
 V_a(\kappa)=
 \frac{\langle x^2,(A_a-\kappa)^{-1}1\rangle}
      {\langle 1,(A_a-\kappa)^{-1}1\rangle}=V_X,
 \qquad V_X=-X''(0).                                           \tag{19}
\]

Real-zero products with this fixed second coefficient automatically form
a normal family: \(|F_a(z)|\le\exp(V_X|z|^2/2)\). They need not match
all finite moments merely to obtain compactness. Equations (12) and (18)
show that every **negative-shift** solution of (19) must satisfy

\[
 \boxed{\displaystyle
 \lambda_0(a)-\kappa\le
 4\pi\sqrt{V_X}\big(C|\kappa|/a+\varepsilon_a\big).}            \tag{20}
\]

For a nonnegative legal shift, the same variational argument gives
\(d_a\|f_a\|_2^2\le\varepsilon_a\), because the nonpositive term
\(-\kappa\|v_a\|_2^2\) can be dropped. Thus a solution of (19) in
that range satisfies \(d_a\le4\pi\sqrt{V_X}\varepsilon_a\).
Moreover \(\lambda_0(a)\le q_a[v_a]/\|v_a\|_2^2\le2a\varepsilon_a\),
where \(\|v_a\|_2^2\ge1/(2a)\); a positive legal shift is itself
confined to this residual scale.

Outside the residual scale, (20) is an \(O(1/a)\) relative neighborhood
of the true spectral bottom. This is a concrete selection target beyond
the safe-shift construction. Existence of such legal shifts is open here,
and normality is not identification of the limit with Xi.

There is a simple conditional existence bracket. If the bottom projection
\(P_a1\ne0\), its normalized Fourier transform has second coefficient
\(V_{a,0}\), and \(V_{a,0}<V_X<a^2/3\), continuity in \(\kappa\)
gives at least one solution of (19) in the full range
\(\kappa<\lambda_0(a)\). The endpoint \(a^2/3\) comes from
the strong limit \(|\kappa|(A_a-\kappa)^{-1}1\to1\) as
\(\kappa\to-\infty\); the other endpoint comes from the bottom
spectral projection. The bracket itself is not established for the
actual full operator.

Monotonicity cannot be inferred from self-adjointness alone. In spectral
coordinates (19) is a ratio with mixed numerator coefficients
\(\langle x^2,v_j\rangle\langle v_j,1\rangle\), which need not be
ordered with the eigenvalues. Any monotonicity claim requires a further
source-specific argument. Even an existence proof for (19) would leave
the complete source-identification/residual passage to be proved.

The elementary bound (18) and its combination (20) were independently
derived during the parallel review of this note.

### 4.3 A deep-shift obstruction that survives zero-free compensation

There is a stronger statement for the explicit asymptotic choice
\(\kappa_a=-e^{4a}\). It addresses Gaussian compensation as well as
the uncompensated family, but only in this deep regime.

**Theorem 4.** For all sufficiently large \(a\), this shift is legal,
and its normalized resolvent satisfies

\[
 \left\|f_a-\frac{1}{2a}\mathbf1_{[-a,a]}\right\|_2
       \le C a^{1/2}e^{-3a},\qquad
 F_a(w/a)\longrightarrow\frac{\sin w}{w}                       \tag{21}
\]

locally uniformly in \(w\in\mathbb C\), with the removable value one
at zero. In particular \(F_a\) has a real zero \(t_a\sim\pi/a\).
For **any** zero-free entire factors \(h_a\) satisfying \(h_a(0)=1\),
the functions \(h_aF_a\) have no locally uniformly convergent subsequence
on a neighborhood of zero. This includes the Gaussian compensation
suggested in PR #1017.

*Proof.* The constant function on the interval belongs to the actual
operator domain. One direct check uses the archimedean Fourier multiplier
\(w(t)=\Re\psi(1/4+it/2)-\log\pi=O(\log(2+|t|))\).
Its product with \(2\sin(at)/t\) is square integrable; for \(a\ge1\),
rescaling \(t=v/a\) bounds the squared norm by
\(Ca\int\log^2(2+|v|)\sin^2(v)/v^2\,dv\). The remaining pole and
finite prime operators are bounded on the interval. Thus

\[
 \|A_a1\|_2\le C a^{3/2}e^a.                                  \tag{22}
\]

For the primes, (22) uses only
\(\sum_{n\le e^{2a}}\Lambda(n)/\sqrt n\ll a e^a\), obtained from
\(\Lambda(n)\le\log n\). The rank-two pole operator obeys the same
bound. The lower bound (15) likewise gives \(|b_a|\ll a e^a\).

Put \(K=e^{4a}\), \(R=(A_a+K)^{-1}\), and \(u=R1\).
For large \(a\), \(K+\lambda_0(a)\ge K/2\). The domain-safe
resolvent identity gives

\[
 Ku-1=-R A_a1,\qquad \|Ku-1\|_2\le C a^{3/2}e^{-3a}.           \tag{23}
\]

Its integral is \(2a+O(a^2e^{-3a})\). Normalizing by that integral
proves the first inequality in (21). Evaluation at \(z=w/a\) costs
at most \(\sqrt{2a}e^{|\Im w|}\) in \(L^2\), proving the second.
Rouche's theorem on a fixed small circle about the simple zero \(w=\pi\)
gives a unique zero there, with \(a t_a\to\pi\). The vector \(f_a\)
is real and even by the source symmetries. Thus \(F_a\) is real entire,
and uniqueness of this nearby zero under conjugation makes it real;
this step does not need the general real-zero theorem. Every zero-free
multiplier retains this zero, while
\((h_aF_a)(0)=1\). A locally uniform limit would therefore have both
value one and a sequence of zeros tending to zero, a contradiction.
QED.

The conclusion concerns this explicit deep shift and, by the same
estimate, other sufficiently deep shifts. It does not rule out
compensation in the narrow source-sensitive window (20).

## 5. The smaller but precise remaining target

The jump representation suggests controlling the quotient by the entire
theta-annihilator family, rather than imposing finitely many moments and
expecting a fixed spectral gap. Its complete arithmetic inequality is
(6), with (7) retained. That inequality is presently open.

For the resolvent approach, a useful next theorem must demonstrate a
selection mechanism in a regime excluded from (13), together with
source identification. Simply making a known legal shift more negative
is now ruled out as a direct convergence strategy. A sharp lower bound
on the whole negative spectrum or an effective estimate for a
source-sensitive projection would be substantive; positivity of finite
matrices, extra theta moment fits, and the single approximate null vector
do not supply either statement.

The numerical working boundary \(B_\flat\) is unchanged by this note.
The point of these results is to make a different attack concrete and
reject its most tempting automatic completion before spending another
round on numerical real-zero fits.

## 6. Exact sources and review boundary

* The source convention and resolvent construction are PR #1017,
  commit `450dd8abecf58dfe60b3bc39bda0f792ea82ce95`, files
  `standalone/2026-10-23-weil-resolvent-publication/browse/PROOF.md`,
  `THETA_RESIDUAL.md`, and `CONVERGENCE.md`.
* A. Connes, C. Consani, H. Moscovici, *Zeta Spectral Triples*,
  arXiv:2511.22755v1, https://arxiv.org/html/2511.22755v1,
  supplies the full Weil operator framework. Its proposed Xi convergence
  remains open; it is not used as a proved premise.
* M. Suzuki, *Weil's quadratic form via the screw function*,
  arXiv:2606.09096v1, https://arxiv.org/html/2606.09096v1,
  provides an independent continuous-kernel operator framework. Its
  small-interval ground-state theorem is not an all-interval positivity
  theorem and is not a premise of (9)--(12).

The source identities and standard analytic facts above are identified
explicitly. Equations (5), (7), and (9)--(16) are the deductions proposed
in this note. No numerical computation, formal proof assistant,
independent external review, or new zero-free result is asserted.
