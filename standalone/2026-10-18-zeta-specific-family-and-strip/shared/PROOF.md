# A quadratic family that retains ordinary zeta: exact capture and full residual geometry

**Status:** PROPOSED native component theorems and an exploratory consequence,
awaiting independent mathematical review. No improved zero-free strip, new
Möbius cancellation estimate, auxiliary GRH, or RH proof is claimed.

**Scope:** actual imaginary quadratic fields of discriminant \(-8u\), with
\(u\) odd and squarefree; all finite arithmetic horizons; a quantitative
critical-energy transfer; and a full-product residual limit for each fixed
mollifier and \(\Re s>3/4\). An explicitly separated random Euler identity holds
on the larger domain \(\Re s>1/2\).

**Dependencies:** elementary quadratic factorization, quadratic reciprocity,
the classical Pólya–Vinogradov estimate (a reduction is supplied below), and the
standard approximate functional equation, derived in Section 7. No proposed
quasi-RH theorem is used. The optional converse identifying the critical energy
criterion with ordinary RH uses the classical RH-to-Mertens implication.

**What was run:** `check_shared_factor.py`, an exact rational/integer checker
of finite arithmetic and probability identities. It does not certify an
infinite Euler product, an analytic continuation, or a zero-free region.

**Smallest remaining gap:** a genuinely better upper bound for the retained
ordinary Möbius source, or for the complete full-product residual. Increasing
the discriminant family by itself does not supply that bound.

## 1. What is different from the existing fixed-field routes

For a single quadratic field, proving RH for its Dedekind zeta function proves
both ordinary RH and GRH for its additional quadratic Dirichlet factor. The
primitive-core theorem in PR #996, at
`56ec8747ccf75d7fc19c2395a6523a664938b9f6`, explicitly preserves this stronger
fixed-field target. PR #998, at
`65a0e7e4016aad5aeb099973c0d079c6059a6c76`, captures an original fixed-field
source by averaging Euler-deleted replicas. Its source remains that original
field's Möbius function.

Here the fields themselves vary. The exact mean of their **full inverse
Dedekind coefficients is ordinary rational Möbius**. At second order, the whole
family contains the ordinary source with positive, explicitly known weights.
This removes the need to prove a separate quadratic GRH. The resulting
critical criterion is equivalent to ordinary RH, using the classical converse,
and retains any hypothetical ordinary zeta zero in every family member.

The full-product residual calculation also answers a more delicate question.
The mean of \(L(s,\chi_d)\) times a triangular inverse Dedekind mollifier is
**not** the ordinary Möbius mollifier. Square aliases survive. We identify an
invertible correction and the complete nonnegative variance, and construct an
explicit correction that makes that mean exactly the ordinary mollifier.

These are extraction and diagnostic theorems. They do not manufacture the
missing cancellation. No literature-priority claim is made for the elementary
Euler/probability ingredients.

## 2. An actual arithmetic family and its local law

For \(Q\ge2\), let

\[
\mathcal U(Q)=\{u:Q<u\le2Q,\ u\text{ odd and squarefree}\},\qquad
d_u=-8u,\qquad \chi_u=\chi_{d_u}.
\]

Every \(d_u\) is a negative fundamental discriminant. Put
\(N_Q=|\mathcal U(Q)|\), so
\(N_Q=(4/\pi^2)Q+O(\sqrt Q)\). An expectation \(\mathbb E_Q\) below means
the uniform average over these actual fields. Prime 2 is always ramified.
For every positive odd integer \(r\), define

\[
g(r)=\prod_{p\mid r}\frac p{p+1},\qquad g(1)=1.
\]

The following estimate is uniform in positive odd integers \(n\):

\[
\mathbb E_Q\chi_u(n)
=\mathbf1_{n=\square}\,g(\operatorname{rad}n)
 +O\!\left(Q^{-1/2}n^{1/4}\log(2n)\right).                 \tag{2.1}
\]

For even \(n\), the expectation is zero exactly. The absolute implied constant
may be enlarged to cover the finitely many small \(Q\). Section 6 proves (2.1).

Consequently the limiting values at distinct odd primes are independent with

\[
\Pr(X_p=0)=\frac1{p+1},\qquad
\Pr(X_p=1)=\Pr(X_p=-1)=\frac p{2(p+1)},\qquad X_2=0.        \tag{2.2}
\]

This is not an assertion of independence at finite \(Q\). Finite mixed moments
converge by (2.1); since the local state spaces are finite, these moments
determine the limiting joint distribution. Write \(X(n)\) for the completely
multiplicative extension. In particular, for odd squarefree \(m,n\),

\[
\mathbb E X(m)=\mathbf1_{m=1},\qquad
\mathbb E X(m)X(n)=\mathbf1_{m=n}\,g(m).                    \tag{2.3}
\]

## 3. Ordinary Möbius is the mean full inverse source

Let

\[
\frac1{\zeta(s)L(s,\chi_u)}
 =\sum_{n\ge1}\frac{a_u(n)}{n^s},\qquad \Re s>1.
\]

All ramified, split and inert factors are included. Euler multiplication gives

\[
a_u=\mu*(\mu\chi_u).                                      \tag{3.1}
\]

For a rational prime with \(\chi_u(p)=0,1,-1\), respectively, the local inverse
factor is \(1-x\), \((1-x)^2\), or \(1-x^2\), where \(x=p^{-s}\). Thus (3.1)
is the literal Dedekind Möbius source aggregated by rational norm.

Define, with both functions zero below 1,

\[
M(x)=\sum_{n\le x}\mu(n),\qquad A_u(x)=\sum_{n\le x}a_u(n).
\]

For every finite real \(x>0\), the exact finite convolution is

\[
A_u(x)=\sum_{\substack{m\le x\\m\text{ odd squarefree}}}
                  \mu(m)\chi_u(m)M(x/m).                    \tag{3.2}
\]

### Theorem A: mean and complete second moment

For every finite \(x,y>0\),

\[
\lim_{Q\to\infty}\mathbb E_Q A_u(x)=M(x),                  \tag{3.3}
\]

\[
\lim_{Q\to\infty}\mathbb E_Q[A_u(x)A_u(y)]
 =\sum_{\substack{m\le\min(x,y)\\m\text{ odd squarefree}}}
          g(m)M(x/m)M(y/m).                                \tag{3.4}
\]

There is no surviving off-diagonal \(m\ne n\) in this limit, because both
inverse-character indices are squarefree. At finite \(Q\) all of those terms
remain, with (2.1) supplying their error. In particular, for \(x\ge2\),

\[
\mathbb E_Q A_u(x)=M(x)+O(Q^{-1/2}x^{5/4}\log(2x)),         \tag{3.5}
\]

\[
\mathbb E_Q |A_u(x)|^2
=\sum_{\substack{m\le x\\m\text{ odd squarefree}}}g(m)|M(x/m)|^2
 +O(Q^{-1/2}x^{5/2}\log(2x)).                              \tag{3.6}
\]

**Proof.** Insert (2.1) in (3.2) and its product. Equation (2.3) gives the exact
limiting terms. For the errors use \(|M(x/m)|\le x/m\) and
\(\sum_{m\le x}m^{-3/4}\ll x^{1/4}\). For the second moment the error is at
most an absolute constant times

\[
Q^{-1/2}\log(2x)
 \left(\sum_{m\le x}m^{1/4}|M(x/m)|\right)^2
 \ll Q^{-1/2}x^{5/2}\log(2x).
\]

The signs in (3.2) have only been discarded in this explicitly bounded
finite-family error, not in the main source. This proves the theorem.

### Theorem B: quantitative capture at the critical energy

For a source \(B\) that is zero below 1 put

\[
E_\sigma(B;T)=\int_1^T |B(x)|^2x^{-2\sigma}\,\frac{dx}{x}.
\]

For \(1/2\le\sigma\le1\) and \(T\ge2\),

\[
\mathbb E_Q E_\sigma(A_u;T)
=\sum_{\substack{m\le T\\m\text{ odd squarefree}}}
      \frac{g(m)}{m^{2\sigma}}E_\sigma(M;T/m)
 +O\!\left(Q^{-1/2}T^{5/2-2\sigma}\log(2T)\right).         \tag{3.7}
\]

In particular, if the error in (3.7) is denoted by \(\mathcal E\),

\[
E_\sigma(M;T)-O(\mathcal E)
\le \mathbb E_Q E_\sigma(A_u;T)
\le D_\sigma(T)E_\sigma(M;T)+O(\mathcal E),                \tag{3.8}
\]

where

\[
D_\sigma(T)=\sum_{\substack{m\le T\\m\text{ odd squarefree}}}
                         \frac{g(m)}{m^{2\sigma}}
\le
\begin{cases}
1+\log T,&\sigma=1/2,\\
\displaystyle\prod_{p\text{ odd}}(1+g(p)p^{-2\sigma})<\infty,
 &\sigma>1/2.
\end{cases}                                               \tag{3.9}
\]

**Proof.** Integrate (3.6); changing variables \(x=my\) in each diagonal term
gives (3.7). The integrated error is bounded as displayed because
\(5/2-2\sigma\ge1/2\). The term \(m=1\) gives the lower bound. Monotonicity
of the cumulative energy and the harmonic-sum bound give the upper bounds.
Every endpoint \(T/m\), including the small-source boundary, is retained.

At the critical value choose any fixed \(\delta>0\) and any
\(Q(T)\ge T^{3+\delta}\). The additive error is
\(O(T^{-\delta/2}\log(2T))\), so

\[
E_{1/2}(M;T)\ll_\varepsilon T^\varepsilon\quad\text{for all }\varepsilon>0
\quad\Longleftrightarrow\quad
\mathbb E_{Q(T)}E_{1/2}(A_u;T)\ll_\varepsilon T^\varepsilon
\quad\text{for all }\varepsilon>0.                         \tag{3.10}
\]

The constants in this equivalence do not assume any individual auxiliary
Dirichlet zero-free theorem. The conductors in this moving family are between
\(8Q(T)\) and \(16Q(T)\); the polynomial family growth is explicit.

### Signed averaging reduces the required conductor growth

There is a stronger sampling statement when the signed source is averaged
**before** taking its energy. Let \(\overline A_Q(x)=\mathbb E_Q A_u(x)\).
Squaring the already-proved deterministic mean error (3.5) and integrating gives

\[
E_\sigma(\overline A_Q-M;T)
\ll Q^{-1}T^{5/2-2\sigma}(\log(2T))^2,
\qquad 1/2\le\sigma\le1.                                 \tag{3.11}
\]

At the critical value it is enough to take
\(Q(T)\ge T^{3/2+\delta}\). The discrepancy energy is then
\(O(T^{-\delta}(\log(2T))^2)\). The triangle inequality for the square root
of this energy proves

\[
E_{1/2}(M;T)\ll_\varepsilon T^\varepsilon\ (\forall\varepsilon>0)
\quad\Longleftrightarrow\quad
E_{1/2}(\overline A_{Q(T)};T)
                   \ll_\varepsilon T^\varepsilon\ (\forall\varepsilon>0).
                                                               \tag{3.12}
\]

This is a statement about a signed mean of whole trajectories on \([1,T]\).
It does not assert that averaging the individual energies has the smaller
conductor requirement. The same family is fixed throughout each energy
integral. No arithmetic upper bound for either side of (3.12) is supplied.

The left side of (3.10) implies ordinary RH. Indeed, on \(\Re s>1\),

\[
\int_1^\infty M(x)x^{-s}\,\frac{dx}{x}=\frac1{s\zeta(s)}.
\]

Cauchy–Schwarz on \([X,2X]\), followed by (3.10), bounds the absolute integral
there by \(O(X^{1/2-\Re s+\varepsilon/2})\). For every fixed \(\Re s>1/2\)
choose \(\varepsilon<2\Re s-1\) and sum the dyadic intervals. This continues
\(1/(s\zeta(s))\) holomorphically to that half-plane. A zeta zero there would
give a nonremovable pole. Reflection supplies ordinary RH. Conversely,
ordinary RH gives the standard all-epsilon Mertens bound and hence the left
side of (3.10). This last converse is classical input, not newly proved here.

For an individual field the analogous Mellin transform is
\(1/[s\zeta(s)L(s,\chi_u)]\). A hypothetical zeta zero is present in every
member. A zero of an auxiliary entire factor can only increase its pole order.
The moving-family criterion therefore preserves the target zero while avoiding
a demand for every individual auxiliary GRH.

## 4. The complete full-product residual, including square aliases

The preceding theorem concerns native summatory sources. We now separately
analyze the user's finite Dirichlet-polynomial residual. Fix \(X\ge1\) and set

\[
M_X(s)=\sum_{m\le X}\mu(m)m^{-s},\qquad M_X(s)=0\ (X<1),
\]

\[
\mathcal M_{u,X}(s)=\sum_{mn\le X}\mu(m)\mu(n)\chi_u(n)(mn)^{-s}.
                                                               \tag{4.1}
\]

This is the truncation of the full inverse Dedekind coefficients (3.1).
It is not the product of two independently truncated polynomials.

For the local law (2.2), the random Euler product

\[
\mathcal L(s)=\prod_{p\text{ odd}}(1-X_pp^{-s})^{-1}
\]

exists in every fixed finite \(L^k\) when \(\sigma=\Re s>1/2\), with the
usual locally uniform analytic interpretation. Its factors have mean
\(1+O(p^{-2\sigma})\), and the same is true of their fixed absolute moments;
normalizing by the means gives the bounded product martingale proof. The
Dirichlet-polynomial partial sums also converge in \(L^2\), since

\[
\sum_{nm=\square}(nm)^{-\sigma}
\le\zeta(2\sigma)^3<\infty.                                \tag{4.2}
\]

For each odd prime put

\[
x_p=p^{-s},\quad g_p=\frac p{p+1},\quad
d_p=1-(1-g_p)x_p^2,
\]

\[
C(s)=\prod_{p\text{ odd}}\frac{d_p}{1-x_p^2},\qquad
t_p(s)=\frac{g_px_p^2}{d_p},\qquad
v_p(s)=\frac{g_p|x_p|^2[1+(1-g_p)|x_p|^2]}{|d_p|^2}.       \tag{4.3}
\]

All these products and the products used below converge absolutely on compact
subsets of \(\sigma>1/2\); \(C(s)\) is holomorphic and nonzero there. Extend
\(t\) and \(v\) multiplicatively on odd squarefree integers. For every such
integer \(r\), define the finite sum

\[
S_{X,r}(s)=
\sum_{\substack{n\le X\\n\text{ odd squarefree}}}
\mu(n)\,t\!\left(\frac n{(n,r)};s\right)M_{X/n}(s).         \tag{4.4}
\]

For fixed \(X\), this depends on \(r\) only through its primes at most \(X\).

### Theorem C: exact nonnegative decomposition

Replace \(\chi_u\) in (4.1) by \(X(n)\), writing the result as
\(\mathcal M_X\). For \(\sigma>1/2\),

\[
\mathbb E[\mathcal L(s)\mathcal M_X(s)]=C(s)S_{X,1}(s).       \tag{4.5}
\]

For any complex scalar \(z\),

\[
\boxed{
\mathbb E|z\mathcal L\mathcal M_X-1|^2
=|zC S_{X,1}-1|^2
 +|zC|^2\!\sum_{\substack{r>1\\r\text{ odd squarefree}}}
                    v(r)|S_{X,r}|^2.}                    \tag{4.6}
\]

Every term on the second line is nonnegative. The series is absolutely
convergent for fixed \(X\). The theorem includes the ramified state \(X_p=0\);
replacing \(g_p\) by 1 silently changes the family.

For the **actual arithmetic family**, each fixed \(X\ge1\), and each fixed
\(s\) with \(\Re s>3/4\), \(s\ne1\), the following limit exists and equals
the right side of (4.6) with \(z=\zeta(s)\):

\[
\lim_{Q\to\infty}\mathbb E_Q
  |\zeta(s)L(s,\chi_u)\mathcal M_{u,X}(s)-1|^2.             \tag{4.7}
\]

Convergence is uniform for \(s\) in fixed compact subsets of that domain. The
proof in Section 7 uses no zeta or quadratic GRH. The random identity on
\(1/2<\sigma\le3/4\) is **not** promoted to an actual full-L-value family
limit by this note. The native source theorems in Section 3 have no such gap.

### Proof of the mean and variance

At one prime use the orthonormal basis of its three-state probability space

\[
1,\qquad e_1=\frac{X_p}{\sqrt{g_p}},\qquad
e_2=\frac{X_p^2-g_p}{\sqrt{g_p(1-g_p)}}.
\]

With \(f_p=(1-X_px_p)^{-1}\) and \(C_p=d_p/(1-x_p^2)\), elementary algebra
gives

\[
\frac{f_p}{C_p}=1+\alpha_pe_1+\beta_pe_2=1+Z_p,
\quad
\alpha_p=\frac{\sqrt{g_p}x_p}{d_p},\quad
\beta_p=\frac{\sqrt{g_p(1-g_p)}x_p^2}{d_p},
\]

\[
\frac{X_px_pf_p}{C_p}=t_p+Z_p.                            \tag{4.8}
\]

Also \(\mathbb E Z_p=0\) and \(\mathbb E|Z_p|^2=v_p\).
Products \(Z_r=\prod_{p\mid r}Z_p\), with \(Z_1=1\), are mutually orthogonal
because a prime in the symmetric difference contributes a factor with mean
zero. Their squared norms are \(v(r)\).

In a summand of the mollifier, a prime dividing the squarefree inverse index
\(n\) contributes \(t_p+Z_p\) by (4.8); a prime not dividing it contributes
\(1+Z_p\). Therefore the coefficient of \(Z_r\) in
\(\mathcal L\mathcal M_X/C\) is exactly (4.4). This proves, in \(L^2\),

\[
\mathcal L\mathcal M_X=C\sum_{r\text{ odd squarefree}}S_{X,r}Z_r.
\]

For fixed \(X\) there are finitely many possible values of \(S_{X,r}\), while
\(\sum_rv(r)=\prod_p(1+v_p)<\infty\). Thus the series and Parseval step are
justified. Its constant term gives (4.5), and orthogonality gives (4.6).

This computation retains the entire square-alias correction. For example,
expanding the mean directly forces the index from the full L-series to be
\(n a^2\), not merely \(n\), and yields

\[
\sum_{a\text{ odd}}g(na)a^{-2s}
=C(s)\prod_{p\mid n}\frac{g_p}{d_p}.
\]

That is the origin of the \(t_p\) factors in (4.4).

## 5. A bounded inverse and a constructive removal of square aliases

For a function of the cutoff let \(R_b f(X)=f(X/b)\). Define

\[
T_s=\sum_{b\text{ odd squarefree}}\mu(b)t(b;s)R_b.
\]

Since \(\sum_p|t_p|<\infty\), \(|t_p|<1\), and

\[
\prod_{p\text{ odd}}(1-t_p)=C(s)^{-1},                    \tag{5.1}
\]

this is an invertible causal dilation operator. Its inverse is

\[
T_s^{-1}=\sum_{b\text{ odd}}\widetilde t(b;s)R_b,
\qquad \widetilde t(p^j;s)=t_p(s)^j.                       \tag{5.2}
\]

The forward and inverse absolute coefficient masses are at most
\(\prod_p(1+|t_p|)\) and \(\prod_p(1-|t_p|)^{-1}\), respectively. These
bounds are uniform in the observation horizon.

More precisely, for \(0\le\eta<2\sigma-1\), both corresponding weighted
masses, with an additional factor \(b^\eta\), are finite. Consequently they
act boundedly and invertibly on every finite-horizon norm

\[
\|f\|_{\eta,H}=\sup_{0<X\le H}X^\eta|f(X)|,               \tag{5.3}
\]

with constants independent of \(H\). Dilation by \(b\) has norm at most
\(b^\eta\), proving the assertion. At the largest local value allowed by
\(p\ge3\) and \(\eta<2\sigma-1\), \(|t_p|p^\eta<1\); the product
increments are \(O(p^{-2\sigma+\eta})\).

Let \(r_X(s)=\zeta(s)M_X(s)-1\) for **all** \(X>0\), so \(r_X=-1\) below
1. Put \(h_X(s)=\zeta(s)C(s)S_{X,1}(s)-1\). Equations (4.4) and (5.1) give
the exact identities

\[
h=C(s)T_s r,\qquad r=C(s)^{-1}T_s^{-1}h.                  \tag{5.4}
\]

Thus decay of the signed family mean residual at any power
\(\eta<2\sigma-1\) is equivalent, without exponent loss, to decay of the
ordinary rational Möbius residual at that power. The initial region \(X<1\)
is included; omitting it would insert a false constant term.

There is also an explicit legal analytic mollifier that removes the square
aliases from the mean:

\[
\widetilde{\mathcal M}_{u,X}(s)
=C(s)^{-1}\sum_{\substack{b\le X\\b\text{ odd}}}
           \widetilde t(b;s)\mathcal M_{u,X/b}(s).          \tag{5.5}
\]

This is a finite combination for each \(X\). Its coefficient functions are
explicit and holomorphic on \(\Re s>1/2\). It is **not** claimed to be a
Dirichlet polynomial with constant coefficients in \(s\); (5.5) specifies its
analytic dependence. In the random model, and in the actual limit (4.7)'s
domain,

\[
\mathbb E[\mathcal L\widetilde{\mathcal M}_X]=M_X(s).       \tag{5.6}
\]

This follows from \(T_s^{-1}T_s=I\). Its complete residual therefore has the
ordinary squared bias \(|\zeta(s)M_X(s)-1|^2\), plus its nonnegative family
variance. The construction removes an auxiliary analytic burden while
displaying exactly which rational cancellation remains.

At any ordinary zeta zero \(\rho\) in the stated domain, each original or
corrected full-product residual is exactly 1, at every finite \(Q,X\). The
extra factor is entire and the displayed correction has no pole there. Neither
averaging nor the change of mollifier discards such a zero.

## 6. Proof of the character averaging estimate

The density of odd squarefree integers follows by inserting
\(\mu^2(u)=\sum_{a^2\mid u}\mu(a)\) and counting odd multiples:

\[
\#\{u\le Y:u\text{ odd squarefree}\}
=\frac Y2\prod_{p\text{ odd}}(1-p^{-2})+O(\sqrt Y)
=\frac4{\pi^2}Y+O(\sqrt Y).
\]

For \(n=a^2\) odd, \(\chi_u(n)=\mathbf1_{(u,a)=1}\). The same expansion,
with the coprimality count included, gives

\[
\sum_{\substack{u\le Y\\u\text{ odd squarefree}}}\chi_u(a^2)
=\frac4{\pi^2}Yg(\operatorname{rad}a)
 +O(\sqrt Y\,2^{\omega(a)}).
\]

Since \(a\) is odd, \(2^{\omega(a)}\ll\sqrt a=n^{1/4}\). This proves the
square case, after taking the difference at \(2Q,Q\) and normalizing.

For nonsquare odd \(n\), quadratic reciprocity writes
\(\chi_u(n)=(-8/n)(u/n)\). The Jacobi character \((\cdot/n)\) is
nonprincipal. Its incomplete sum, including an odd-index restriction if
required, is \(O(\sqrt n\log(2n))\). To reduce this assertion to the
classical primitive Pólya–Vinogradov bound, take the squarefree odd-exponent
kernel \(r>1\) of \(n\). The character of conductor \(r\) is primitive;
the remaining zero restrictions are removed by a divisor inclusion-exclusion.
Every newly restricted prime has even exponent in \(n\), and
\(2^{\omega(h)}\sqrt r\le h\sqrt r\le\sqrt n\). Thus the stated bound
holds for this possibly imprimitive Jacobi character as well.

In the squarefree expansion split the divisor \(a\) at \(A\). The part
\(a\le A\) is bounded by \(A\sqrt n\log(2n)\); the remaining part is
\(O(Y/A)\), by counting multiples of \(a^2\). Choose
\(A\asymp\sqrt Y\,n^{-1/4}(\log(2n))^{-1/2}\) when this is at least 1.
When it is below 1 the trivial bound \(O(Y)\) is sufficient. This proves

\[
\sum_{\substack{u\le Y\\u\text{ odd squarefree}}}\chi_u(n)
\ll \sqrt Y\,n^{1/4}\log(2n).
\]

Taking the dyadic difference proves (2.1). Partial summation also gives the
same error for a differentiable weight on \([Q,2Q]\), multiplied by its
supremum plus total variation. This weighted version is used next.

## 7. Why the full-L-value limit is unconditional for Re s > 3/4

This section supplies the analytic adapter, rather than identifying an
infinite random Euler product with actual L-values by assertion. Fix a compact
set with \(3/4<\sigma_0\le\Re s\le\sigma_1<5/4\), and keep \(X\) fixed.
The portion further to the right follows from ordinary absolute convergence;
the overlap also covers points on \(\Re s=1\). For our characters the parity is odd and the root
number is 1. With \(q=8u\), the completed functional equation yields

\[
L(s,\chi_u)=P_u(s)+\epsilon_q(s)D_u(s),                   \tag{7.1}
\]

\[
P_u(s)=\sum_{n\ge1}\chi_u(n)n^{-s}V_s(n/\sqrt{q/\pi}),
\quad
D_u(s)=\sum_{n\ge1}\chi_u(n)n^{s-1}V_{1-s}(n/\sqrt{q/\pi}),
\]

\[
\epsilon_q(s)=(q/\pi)^{1/2-s}
 \frac{\Gamma((2-s)/2)}{\Gamma((s+1)/2)},
\quad
V_s(y)=\frac1{2\pi i}\int_{(c)}
 \frac{\Gamma((s+w+1)/2)}{\Gamma((s+1)/2)}e^{w^2}y^{-w}\frac{dw}{w}.
                                                               \tag{7.2}
\]

Take \(c\) sufficiently large. Formula (7.1) follows by integrating the
completed L-function against \(e^{w^2}/w\), shifting past \(w=0\), applying
its functional equation to the shifted integral, and replacing \(w\) by
\(-w\). Gamma decay and the Gaussian factor justify the shifts. Both
Dirichlet expansions then lie initially in an absolutely convergent half-plane.
There are no principal-character poles in this family.

Contour shifts in (7.2) give, uniformly on the fixed compact,
\(V_s(y)\to1\) as \(y\to0\), and arbitrarily fast polynomial decay as
\(y\to\infty\). The same bounds hold for \(yV_s'(y)\), except that the
limit at zero is 0. Consequently each normalized product of these weights on
\(Q<u\le2Q\) has bounded supremum and total variation, uniformly in its
summation indices. The factor \(q^{1/2-s}\) has the same property after its
absolute size \(Q^{1/2-\sigma}\) is removed.

Truncate both sums at \(N=Q^{1/2+\delta}\), with \(\delta>0\) small. By
choosing the decay order sufficiently large, both tails, including the dual
prefactor, are \(O(Q^{-A})\) for any specified \(A\). Here \(q\asymp Q\),
so ordinary absolute tail bounds suffice.

Apply the weighted (2.1) to the squared primary polynomial. Its nonsquare
error is

\[
\ll Q^{-1/2}(\log(2N))^C
 \left(\sum_{n\le N}n^{1/4-\sigma}\right)^2
\ll Q^{3/4-\sigma+\delta(5/2-2\sigma)}(\log Q)^C=o(1).    \tag{7.3}
\]

For a square character index \(k\) and a weight \(W_u\), the main term is
\(g(\operatorname{rad}k)\mathbb E_Q W_u\), not an unweighted constant at
finite \(Q\). The same error bound includes the discrepancy of square terms
from this main term. The limiting square sum is absolutely convergent by (4.2),
and the weights for every fixed pair tend to 1. Dominated convergence therefore
identifies the primary second moment and its cross moments with any fixed
polynomial in finitely many \(\chi_u(n)\) with the random Dirichlet-series
moments. Multiplying by (4.1) only introduces finitely many fixed indices;
their costs are absorbed into a constant depending on \(X\), not on \(Q\).

For completeness the dual part really tends to zero in mean square. Its
square main term is bounded by

\[
Q^{1-2\sigma}
 \sum_{\substack{n,m\le N\\nm=\square}}(nm)^{\sigma-1}
\ll Q^{1-2\sigma}N^{2\sigma-1}\log(2N)
=Q^{1/2-\sigma+\delta(2\sigma-1)}O(\log Q).                \tag{7.4}
\]

To see the sum bound, write \(n=ra^2,m=rb^2\), with \(r\) squarefree, and
sum the two power sums in \(a,b\). The remaining \(r\)-sum is harmonic.
The nonsquare error, including the dual prefactor, is

\[
\ll Q^{1/2-2\sigma}N^{2\sigma+1/2}(\log Q)^C
=Q^{3/4-\sigma+\delta(2\sigma+1/2)}(\log Q)^C=o(1).       \tag{7.5}
\]

Choose \(\delta\) small enough for (7.3)–(7.5), uniformly using
\(\sigma_0>3/4\). The cross term between primary and dual is then \(o(1)\)
by Cauchy–Schwarz. The fixed mollifier is pointwise bounded uniformly in the
character, so it does not affect disappearance of the dual term. For the
primary terms multiplied by fixed inverse indices, a condition \(nmk=\square\)
has absolute sum at most \(k^\sigma\zeta(2\sigma)^3\), since one may replace
\(n\) by \(nk\) and enlarge the resulting square-pair sum. This supplies the
claimed fixed-mollifier domination. First moments
follow either directly or by the same \(L^2\) estimates.

These facts prove convergence of the mean and second moment of
\(L(s,\chi_u)\mathcal M_{u,X}(s)\) to the model used in (4.5)–(4.6).
Expansion of the full residual proves (4.7). The proof leaves \(\zeta(s)\)
in place as the common scalar throughout; it never divides that factor out.

## 8. Consequences for the research choice

1. **Dropping field-by-field GRH is a real reduction.** The moving family in
   (3.10) tests ordinary Möbius alone. A fixed-field square-root theorem asks
   for more. Every hypothetical ordinary zeta zero remains shared by all rows.

2. **The common-factor residual is mathematically sound.** Its proposed
   strict-below-one criterion would exclude every target zero. Theorems C and
   (5.4) show the exact scalar bias and every positive fluctuation that a proof
   must control; there is no free improvement from simply adding more fields.

3. **The square correction can be removed with controlled cost.** Formula
   (5.5) is an explicit construction, and (5.4) is a uniform inverse theorem
   at every fixed distance to the right of 1/2. Neither has a critical-line
   absolute-convergence claim.

4. **The critical arithmetic averaging is already fully justified.** Unlike
   the full-L-value adapter below 3/4, (3.7)–(3.10) retain complete arithmetic
   horizons at the critical exponent, with an explicit polynomial conductor
   requirement. Averaging signs first improves the requirement from
   \(Q\ge T^{3+\delta}\) to \(Q\ge T^{3/2+\delta}\), as in (3.11)–(3.12).
   A proposed family upper bound can now be tested against a
   precise ordinary-zeta consumer.

The remaining ambitious target is a signed arithmetic estimate that actually
beats the ordinary Möbius energy. The present calculations isolate that target
more sharply and prevent a family diagonal or a square-alias omission from
being mistaken for its proof.

## References and provenance

- [PR #996 primitive-core source, frozen commit](https://github.com/GettysburgResearch/riemann/blob/56ec8747ccf75d7fc19c2395a6523a664938b9f6/standalone/2026-10-18-quadratic-angular-all-order/PRIMITIVE_CORE_EQUIVALENCE.md).
- [PR #998 fixed-field full-density Euler-mask capture, frozen commit](https://github.com/GettysburgResearch/riemann/blob/65a0e7e4016aad5aeb099973c0d079c6059a6c76/standalone/2026-10-18-full-density-causal-capture/PROOF.md).
- J. Thorner and A. Zaman, *A zero density estimate for Dedekind zeta
  functions*, [arXiv:1909.01338](https://arxiv.org/abs/1909.01338).
  This is contextual: its quotient-family zero-density theorem is not an input
  to any theorem here, and is not substituted for a full-product estimate.
- The Pólya–Vinogradov estimate, primitive quadratic functional equation,
  and RH-to-Mertens implication are classical inputs. Their exact uses and
  required normalizations are specified above. None of the recent proposed
  strip improvements is a dependency.
