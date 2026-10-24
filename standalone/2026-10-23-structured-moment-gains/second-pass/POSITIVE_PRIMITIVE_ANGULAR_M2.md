# Positive primitive angular quartic second moments

Research note, 23 October 2026. This file is outside the frozen PR1020 packet.

## 0. Result and its precise limitation

Write \(\mathcal O=\mathbb Z[i]\), \(\lambda=1+i\), and \(N a=|a|^2\).
All good ideals are represented by their primary generators. Let
\(\alpha(c)=c/|c|\), \(\xi(c)=\alpha(c)^{-\ell}\), with
\(\ell\in\{-1,1\}\). For either primary class \(v\pmod4\), put

\[
 \psi(k,s;\xi,v)=
 \sum_{c\equiv v\ (4)}\frac{g_4(k,c)\xi(c)}{(Nc)^s},
 \qquad
 P_Q(k,s;\xi,v)=
 \sum_{\substack{c\equiv v\ (4)\\\mu^2(c)=1\\(c,Q)=1}}
 \frac{g_4(k,c)\xi(c)}{(Nc)^s}.                     \tag{0.1}
\]

Here \(g_4\) is the **unnormalized** quartic Gauss sum. The sums initially
converge absolutely for \(\Re s>3/2\); their continuations are used below.
The parameter \(Q\) is a squarefree good ideal. It does not change the
fixed automorphic level used in the proof.

**Theorem.** Fix \(\delta>0\), \(\epsilon>0\), and a compact interval
\(1+\delta\leq\sigma\leq S\). There is a finite exponent \(A\), depending
only on the fixed interval and fixed geometric data, such that, for
\(s=\sigma+it\), \(T=1+|t|\), and \(K\geq1\),

\[
 \sum_{0<Nk\leq K}|\psi(k,s;\xi,v)|^2
 \ll_\delta T^A K,                                      \tag{0.2}
\]

and

\[
 \sum_{0<Nk\leq K}|P_Q(k,s;\xi,v)|^2
 \ll_{\delta,\epsilon}T^A K^{1+\epsilon}(NQ)^\epsilon
       \sum_{f\mid Q}(Nf)^{3-2\sigma}.                    \tag{0.3}
\]

In particular, for \(\sigma=1+\delta\),

\[
 \sum_{0<Nk\leq K}|P_Q(k,1+\delta+it;\xi,v)|^2
 \ll_{\delta,\epsilon}T^A K^{1+\epsilon}
       (NQ)^{\max(1-2\delta,0)+\epsilon}.                 \tag{0.4}
\]

The \(k\)-sum includes ramified rows, repeated prime factors, and fourth
powers. The implicit constants are independent of \(K,t,Q\).

**This theorem does not yet improve the zero-free boundary.** With the
quartic convention in (0.1),
\(g_4(k,c)=\overline{\chi_c(k)}g_4(1,c)\) when \((k,c)=1\).
Consequently the inverse expression with the Möbius factor has the
physical numerator \(k^3\), not \(k\); see §7. A bound for that sparse
subsequence is an additional analytic requirement. In particular, (0.2)
or (0.3) must not be substituted for a \(k^3\)-indexed moment.

## 1. Primary sources and what is derived here

The source conventions are those of:

1. David, Dunn, Hamieh, Lin, *Quartic Gauss sums over primes and metaplectic
   theta functions*, [arXiv:2306.11875v5](https://arxiv.org/html/2306.11875v5),
   §4.4, especially (4.4), the defining arithmetic coefficient following
   (4.6), and (4.11)–(4.13). Abbreviated **DDHL**.
2. Castillo, de Faveri, Dunn, *Non-vanishing for quartic Hecke L-functions
   and ranks of elliptic curves*,
   [arXiv:2604.01316v1](https://arxiv.org/html/2604.01316v1),
   §6, Lemma 6.1 and Corollary 6.2. Abbreviated **CDFD**.

The fixed angular second moment is proved below; it is not imported from
a spherical second-moment theorem. The analytic proof uses the spinor
Dirac operator to obtain uniform polynomial spectral-height bounds,
followed by a Bessel Wronskian and a positive ordinary-height majorant.
The transfer from \(\psi\) to \(P_Q\) uses CDFD's exact local identities.

Version 4 of DDHL (4.6) displayed the two matrices in the wrong order.
Version 5, dated 30 January 2026, has already corrected that order and
uses the full Fourier-index lattice \(\lambda^{-2}\mathcal O\).
The direct computation below both fixes conventions and agrees with
the current primary source; it is not a claim of a new source erratum.

## 2. The arithmetic matrix is on the right

Use the upper-half-space point

\[
 w=\begin{pmatrix}z&-y\\y&\bar z\end{pmatrix},\qquad
 \widetilde c=\operatorname{diag}(c,\bar c),\qquad
 j(\gamma,w)=\frac{\widetilde c w+\widetilde d}
 {\det(\widetilde c w+\widetilde d)^{1/2}}.
\]

The star in DDHL is conjugate transpose. For \(c\ne0\), direct
multiplication gives

\[
 (\widetilde c w+\widetilde d)^*
 =\begin{pmatrix}
   \bar z+\bar d/\bar c&y\\-y&z+d/c
  \end{pmatrix}\operatorname{diag}(\bar c,c).       \tag{2.1}
\]

The last matrix is therefore on the **right** after the Fourier integral
in \(z\). At a cusp with scaling matrix \(\sigma_j\), use the unitary
frame \(j(\sigma_j,w)^*E_i(\sigma_jw,s,1)\). Its nonzero-frequency
expansion is

\[
 \sum_{k\in\lambda^{-2}\mathcal O\setminus\{0\}} y^{2-s}
 K(ky/\lambda^4,s,1)\Phi_{ij}(s,k,1)
 \check e(kz/\lambda^4),                            \tag{2.2}
\]

where \(\Phi_{ij}\) is DDHL's diagonal arithmetic matrix. The constant
terms are \(\delta_{ij}y^sI\) and
\(y^{2-s}K(0,s,1)\Phi_{ij}(s,0,1)\).
Both the current DDHL (4.6) and its scattering matrix (4.9) have the
order \(K\Phi\). Equation (2.1) proves the order directly. The
integral rows occurring in (0.1) form a subset of this full Fourier
lattice, so restricting Parseval to them is legitimate.

In particular a single inducing column \(e_r\), \(r=1,2\), has the
single common arithmetic coefficient \(\Phi_{ij,rr}(s,k,1)\) in both
of its spinor components. DDHL (4.11)–(4.13) identify the relevant
coefficients at infinity with \(\psi(k,s;\alpha^{-1},v)\) and
\(\psi(k,s;\alpha,v)\), up to fixed volume and unit factors.

The Fourier integral in DDHL (4.4) can be evaluated by differentiating
the scalar Fourier transform of \((1+|z|^2)^{-s-1/2}\). Put
\(r_u=|u|\), \(R=4\pi r_u\), \(\nu=s-3/2\), and
\(C_s=(2\pi)^{s+1/2}/\Gamma(s+1/2)\). For \(u\ne0\),

\[
 K(u,s,1)=C_s r_u^{s-1/2}
 \begin{pmatrix}
  -i(u/r_u)K_\nu(R)&K_{\nu+1}(R)\\
  -K_{\nu+1}(R)&-i(\bar u/r_u)K_\nu(R)
 \end{pmatrix}.                                    \tag{2.3}
\]

Also

\[
 K(0,s,1)=\frac{\pi}{s-1/2}
 \begin{pmatrix}0&1\\-1&0\end{pmatrix}.             \tag{2.4}
\]

The diagonal Bessel order is \(s-3/2\), and the off-diagonal order is
\(s-1/2\). The correction in (2.2) does not interchange these orders.

## 3. A fixed-level polynomial cusp bound

### 3.1. Dirac equation and its resolvent

Let \(z=x_1+ix_2\). In this spinor frame the hyperbolic Dirac operator is

\[
 \mathcal D=-i
 \begin{pmatrix}
  y\partial_y-1&2y\partial_z\\
  2y\partial_{\bar z}&-y\partial_y+1
 \end{pmatrix}.                                    \tag{3.1}
\]

It is covariant under the unitary factor \(j\). This can be checked
directly under translations, rotations, positive dilations and inversion,
which generate the action. Thus it descends to the fixed quotient with
the additional flat unitary multiplier \(\chi\). It is formally
self-adjoint for measure \(y^{-3}dx_1dx_2dy\): the operator
\(y\partial_y-1\) is skew-adjoint, as are the horizontal derivatives.

On the complete quotient the operator is essentially self-adjoint.
For completeness, choose compactly supported cutoffs \(\eta_R\to1\)
with \(|\nabla\eta_R|\ll1/R\). A vector in either deficiency space
is locally regular by ellipticity. Applying formal symmetry to
\(\eta_R\) times that vector bounds its norm by the commutator
\([\mathcal D,\eta_R]\), whose operator norm is \(O(1/R)\).
Letting \(R\to\infty\) makes both deficiency spaces zero. We use the
resulting self-adjoint realization.

The two incoming sections satisfy

\[
 \mathcal D(y^se_1)=-i(s-1)y^se_1,\qquad
 \mathcal D(y^se_2)= i(s-1)y^se_2.                    \tag{3.2}
\]

Covariance and the absolutely convergent defining Eisenstein sum prove
the same equations for its two columns when \(\sigma>2\).
One may independently check them on (2.3), using
\(RK_\nu'=\nu K_\nu-RK_{\nu+1}\) and
\(RK_{\nu+1}'=-RK_\nu-(\nu+1)K_{\nu+1}\).
The outgoing vector in (2.4) has the same Dirac eigenvalue as its
incoming vector.

Choose disjoint fixed cusp neighborhoods and a smooth cutoff of the
incoming term for the chosen cusp and column. Call the resulting
global section \(F_s\). Write \(z_s=\mp i(s-1)\), with the sign chosen
according to the column. Then

\[
 f_s=(\mathcal D-z_s)F_s
\]

is supported in one fixed compact cusp annulus. Its graph-Sobolev norms
are polynomial in \(T\), uniformly for \(\sigma\) in the fixed strip.
The cancellation in (3.2) leaves only derivatives of the cutoff in
\(f_s\).

For \(\sigma\geq1+\delta\),

\[
 \| (\mathcal D-z_s)^{-1}\|_{L^2\to L^2}
 \leq |\Im z_s|^{-1}=(\sigma-1)^{-1}\leq\delta^{-1}. \tag{3.3}
\]

Define

\[
 \mathcal E_s=F_s-(\mathcal D-z_s)^{-1}f_s.          \tag{3.4}
\]

For \(\sigma>2\) this equals the defining Eisenstein column. Indeed,
after subtracting its incoming cutoff that column is in \(L^2\): its
outgoing exponent is \(2-s\), and all its nonconstant Fourier terms
decay in the cusps in this absolutely convergent region. The difference
of the two constructions is an \(L^2\) solution of
\((\mathcal D-z_s)u=0\), and (3.3) makes it zero.
Equation (3.4) therefore continues the column holomorphically to
\(\sigma>1\), with the stated resolvent estimate. This argument does
not require any zero-free hypothesis or a moment estimate for its
Fourier coefficients.

### 3.2. Uniform pointwise control in every cusp

Let \(Y(w)\geq1\) be a fixed invariant height, equal up to fixed
constants to cusp height in each cusp. Fixed-radius elliptic Sobolev
estimates on \(\mathbb H^3\), applied after lifting a section from the
quotient, give

\[
 |u(w)|\ll Y(w)\sum_{j=0}^{m}\|\mathcal D^ju\|_{L^2},             \tag{3.5}
\]

for one fixed sufficiently large integer \(m\). Here is the reason
for the factor \(Y\). In a cusp at height \(Y\), a fixed hyperbolic
ball meets \(O(Y^2)\) translates of a fundamental horotorus; a lifted
\(L^2\)-norm is therefore at most \(O(Y)\) times the global norm.
The lifted local Sobolev constants are uniform because the geometry
on \(\mathbb H^3\) is fixed. In the compact part the multiplicity is
bounded. The same argument controls any fixed number of invariant
derivatives after increasing \(m\).

Since the resolvent commutes with powers of \(\mathcal D\), (3.3)
applied to \(\mathcal D^jf_s\) bounds the graph norms of the second
term in (3.4) by a power of \(T\). The incoming cutoff and its fixed
number of invariant derivatives are bounded by a power of \(T\)
times \(Y^\sigma\). As \(\sigma>1\), (3.5) consequently proves

\[
 |E_i(w,s,1)e_r|\ll_\delta T^B Y(w)^\sigma.          \tag{3.6}
\]

All cusp frames are unitary, so the same estimate holds in them.
Every constant here belongs to the original fixed quotient. There
is no varying-level evaluation norm in (3.6).

## 4. Recovering the arithmetic coefficients

The modified-Bessel Wronskian is

\[
 R\big(I_{\nu+1}(R)K_\nu(R)+I_\nu(R)K_{\nu+1}(R)\big)=1.
                                                               \tag{4.1}
\]

For the first column of (2.3), the linear combination with coefficients

\[
 A=\frac{i(\bar u/r_u)R I_{\nu+1}(R)}{C_s r_u^{s-1/2}},\qquad
 B=\frac{R I_\nu(R)}{C_s r_u^{s-1/2}}
\]

satisfies \(A K_{11}-B K_{21}=1\). The second column has the same
conclusion after exchanging the components and their unit phases.

On any compact annulus \(0<a\leq r_u\leq b\), these coefficients
are bounded by a fixed power of \(T\), uniformly in the fixed
\(\sigma\)-interval. To see this without using an asymptotic that
loses an exponential in \(t\), use the convergent power series

\[
 \Gamma(s+1/2)I_{s-1/2}(R)
 =(R/2)^{s-1/2}
 \sum_{j\geq0}\frac{(R^2/4)^j}{j!(s+1/2)_j},                    \tag{4.2}
\]

and

\[
 \Gamma(s+1/2)I_{s-3/2}(R)
 =(R/2)^{s-3/2}\left(s-1/2+
 \sum_{j\geq1}\frac{(R^2/4)^j}{j!(s+1/2)_{j-1}}\right).       \tag{4.3}
\]

Each denominator has a positive lower bound supplied by its real
part. These formulas give \(A\ll1\), \(B\ll T\) on the annulus;
allowing a larger fixed power is harmless. In particular,

\[
 \|K(u,s,1)e_r\|^2\gg T^{-B_1}.                   \tag{4.4}
\]

This avoids division by an individual Bessel function at its zeros.

It remains to average the invariant height. For real \(a>2\), let
\(E_j^{\mathrm{ord}}(w,a)\) be the ordinary positive Eisenstein
series of the fixed quotient. From the definition of the maximal
cusp height,

\[
 Y(w)^a\ll1+\sum_jE_j^{\mathrm{ord}}(w,a).           \tag{4.5}
\]

At infinity its constant terms have the form
\(\delta_{j\infty}y^a+\varphi_{j\infty}^{\mathrm{ord}}(a)y^{2-a}\).
All sums converge absolutely since \(a>2\). Integration on the
fixed horotorus and \(a=2\sigma\) therefore give, for \(0<y\leq1\),

\[
 \int_{\mathbb C/\lambda^4\mathcal O}Y(z,y)^{2\sigma}\,dz
 \ll_\delta y^{2-2\sigma}.                         \tag{4.6}
\]

Now set \(y=K^{-1/2}\). For \(K/2<Nk\leq K\), the argument
\(|k|y/|\lambda|^4\) lies in a fixed compact annulus. Parseval,
(2.2), (3.6), (4.4) and (4.6) imply

\[
 \begin{aligned}
 \sum_{K/2<Nk\leq K}|\Phi_{ij,rr}(s,k,1)|^2
 &\ll T^{B_1}y^{2\sigma-4}
       \int_{\mathbb C/\lambda^4\mathcal O}|E_i(z,y,s,1)e_r|^2\,dz\\
 &\ll T^{A}y^{2\sigma-4}y^{2-2\sigma}
  =T^A K.                                                    \tag{4.7}
 \end{aligned}
\]

The two required \(\psi\)-series are among these coefficients by
DDHL (4.11)–(4.13). Summing geometric dyadic blocks proves (0.2).

The proof also works for a fixed finite family of additional ray
masks whenever these are realized by fixed cusp sections on a fixed
congruence cover: decompose the finite bottom-row residue masks into
cusp sections, and repeat the same argument there. Constants may
depend on that fixed cover. No uniform assertion for a growing
additional ray conductor is made by this observation.

## 5. Exact primitive completion and all rows

For squarefree \(c\), \(g_4(k,c)=0\) if \((k,c)>1\). If
\((k,c)=1\), the Gauss sum vanishes unless \(c\) is squarefree.
Thus the natural row zeros give the exact identity

\[
 P_Q(k,s;\xi,v)=\psi_{\operatorname{rad}(kQ)}(k,s;\xi,v),        \tag{5.1}
\]

where \(\psi_\beta\) means that \((c,\beta)=1\) is imposed.
Fourth powers in \(k\) can be erased only while their punctures in
(5.1) are retained.

Every nonzero Gaussian row has a unique decomposition

\[
 k=\eta\lambda^{4j}a b^2c^3d^4r^4,\qquad j\geq0,\qquad
 \mu^2(abcd)=1,\qquad r\mid(abcd)^\infty,                       \tag{5.2}
\]

where \(a,b,c,d,r\) are primary and \(\eta\) is a unit times
\(\lambda^e\), \(0\leq e\leq3\). The four squarefree factors
are pairwise coprime. The factor \(d\) records primes with positive
valuation divisible by four. In particular,

\[
 P_1(k,s;\xi,v)=\psi_{abcd}(\eta ab^2c^3,s;\xi,v).              \tag{5.3}
\]

CDFD Corollary 6.2 expresses the last series as

\[
 \frac{1}{\Delta_a^*(ac\eta,s,\xi)\Delta_{bcd}(s,\xi)}
 \sum_{e\mid b,\ f\mid d} C_{e,f}(s)
       \psi(\eta ab^2c^3 f^2/e^2,s;\xi,efv),                  \tag{5.4}
\]

where its exact coefficients have modulus

\[
 |C_{e,f}(s)|=(Ne)^{5/2-3\sigma}(Nf)^{1/2-\sigma}.             \tag{5.5}
\]

To check the normalization in (5.5), its two Gauss sums have moduli
\(\sqrt{Ne}\), \(\sqrt{Nf}\); CDFD's remaining norm factor is
\((Ne)^2/N(e^3f)^s\). All omitted factors are unit phases,
Möbius signs, and values of the unitary character \(\xi\).
They do not affect this positive estimate.

The Euler factors are

\[
 \Delta_\beta(s,\xi)=\prod_{p\mid\beta}(1-(Np)^{3-4s}\xi(p)^4),
\]

\[
 \Delta_a^*(ac\eta,s,\xi)
 =\prod_{p\mid a}\left(1+g_2(ac\eta/p,p)(Np)^{1-2s}\xi(p)^2\right).
\]

On \(\sigma\geq1+\delta\), the first inverse is bounded uniformly
in \(\beta\). The second is \(\ll_{\delta,\epsilon}(Na)^\epsilon\):
the absolute value of its nonconstant local term is
\((Np)^{3/2-2\sigma}\leq(Np)^{-1/2-2\delta}<1\), and a finite
product of the resulting inverses is bounded by an arbitrarily small
power of \(Na\). This is also uniform in \(t\).

Apply rowwise Cauchy to the divisor sum in (5.4). Its number of terms
is \(\ll_\epsilon(Nk)^\epsilon\). Put \(b=e b'\), \(d=f d'\) and

\[
 n=\eta a b'^2c^3 f^2.
\]

The exact original-row scale is

\[
 k=\lambda^{4j}n e^2 f^2d'^4r^4.                  \tag{5.6}
\]

For fixed \(j,\eta,e,f,d',r\), the remaining \(a,b',c\) are
determined by \(n\), if admissible. Dropping their coprimality
restrictions therefore only enlarges the ensuing positive sum; it
does not introduce an uncontrolled multiplicity. By (0.2), (5.5)
and (5.6), the row average is bounded by a constant times

\[
 \begin{aligned}
 T^A K^{1+\epsilon}
 &\sum_{j\geq0}2^{-4j}
 \sum_e(Ne)^{3-6\sigma}
 \sum_f(Nf)^{-1-2\sigma}\\
 &\hspace{35mm}\times\sum_{d'}(Nd')^{-4}\sum_r(Nr)^{-4}.       \tag{5.7}
 \end{aligned}
\]

Every ideal sum converges for \(\sigma>1\). At \(\sigma=1\), the
displayed \(e\)- and \(f\)-exponents are already \(-3\), while
the fourth-power factors have exponent \(-4\). This proves (0.3)
for \(Q=1\), including all ramified and repeated-prime rows.

## 6. External punctures and their exact cost

For each row in (5.2), first absorb \((Q,abcd)\) into its natural
puncture and let \(Q_0=Q/(Q,abcd)\). Then \((Q_0,abcd)=1\).
Use CDFD Corollary 6.2 with its fourth squarefree factor replaced
by \(dQ_0\). Split its divisor \(f=f_0f_Q\), where
\(f_0\mid d\), \(f_Q\mid Q_0\).

The same reindexing as (5.6), now with \(f_0\) in place of \(f\),
gives original row

\[
 k=\lambda^{4j}n e^2f_0^2d'^4r^4,
\]

and unmasked Fourier row \(nf_Q^2\). The squared coefficient
of this external factor is exactly \((Nf_Q)^{1-2\sigma}\).
For any \(X\geq1\), positivity and injectivity of multiplication
by \(f_Q^2\) give

\[
 \sum_{0<Nn\leq X}|\psi(nf_Q^2,s;\xi,v')|^2
 \leq\sum_{0<Nm\leq X(Nf_Q)^2}|\psi(m,s;\xi,v')|^2
 \ll T^A X(Nf_Q)^2.                               \tag{6.1}
\]

Thus the exact coarse external factor left by this argument is

\[
 \sum_{f_Q\mid Q}(Nf_Q)^{3-2\sigma}.              \tag{6.2}
\]

The extra divisor Cauchy factor is \((NQ)^\epsilon\). All original
row scale sums are still the convergent sums in (5.7).
This proves (0.3), after replacing the small intermediate epsilon
parameters by suitable fractions of the stated epsilon. Finally

\[
 \sum_{f\mid Q}(Nf)^b\ll_\epsilon
 (NQ)^{\max(b,0)+\epsilon}
\]

gives (0.4). This is a coarse puncture cost; no claim of its
optimality is needed. In particular it is not a level-independent
bound for arbitrary growing marked characters.

## 7. Why this is not yet the inverse moment

Write \(\gamma_4(c)=g_4(1,c)/\sqrt{Nc}\). In these conventions,
for squarefree primary \(c\),

\[
 \gamma_4(c)^2=\mu(c)\alpha(c).                    \tag{7.0}
\]

Here is the unit-factor check, so the angular family is explicit.
For a degree-one primary prime \(\pi=a+bi\) of norm \(p\), DDHL
(3.11) contains the product
\((-1/\pi)_4(\bar\pi/\pi)_4^{-2}\). Modulo \(\pi\),
\(\bar\pi=2a\), and

\[
 (\bar\pi/\pi)_4^{-2}=(2a/p)=(2/p)=(-1)^{(p-1)/4}=(-1/\pi)_4.
\]

Indeed \(a\) is odd, \((a/p)=(p/|a|)=(b^2/|a|)=1\), with
the case \(|a|=1\) immediate; the sign of \(a\) is harmless since
\(p\equiv1\pmod4\). Thus the product of the two signs is one,
and the prime square is \(-\pi/|\pi|\). For an inert primary
prime \(\pi=-p\), Frobenius on \(\mathbb F_{p^2}\) conjugates
the quartic character and preserves the additive trace. Since its
quartic character is also trivial at \(-1\), its Gauss sum is
real. Its normalized square is therefore one, again
\(\mu(\pi)\alpha(\pi)\). Finally the CRT phase has square one
by quadratic reciprocity for primary Gaussian integers. This proves
(7.0) multiplicatively. This is also the normalization verified in
[the pinned quartic codec](https://github.com/GettysburgResearch/riemann/blob/7ea66551190f291101b0dd44fb1fc9b3331c560d/standalone/2026-10-22-quartic-full-sieve/CORRECTED_QUARTIC_CODEC.md).

Consequently,

\[
 \mu(c)\gamma_4(c)\overline{\chi_c(k)}
 =\alpha(c)\,
   \overline{g_4(k^3,c)/\sqrt{Nc}}.                \tag{7.1}
\]

Indeed, \(g_4(k^3,c)/\sqrt{Nc}=\chi_c(k)\gamma_4(c)\), and
\(\mu\gamma_4=\alpha\overline{\gamma_4}\). If \((k,c)>1\),
both sides vanish under the usual extension of the characters.
Conjugating the whole Gauss family changes both its Gauss factor
and its character orientation and does not remove this cube.

The issue is present on the dominant squarefree physical-row
stratum. CDFD Lemma 6.1(i) gives, for squarefree good \(k\),

\[
 P_1(k^3,s;\xi,v)
 =\Delta_k(s,\xi)^{-1}\psi(k^3,s;\xi,v).            \tag{7.2}
\]

There is no decreasing-scale divisor term in (7.2). In (5.4) this
is the case \(a=b=d=1,c=k\), so the divisor sum has one term.
The local identity is CDFD (6.7); it preserves the exponent-three
numerator exactly.

Consequently (0.2) only bounds
\(\sum_{Nk\leq K}|\psi(k^3,s)|^2\) by \(O(T^A K^3)\)
through positivity. This is a limitation of the available implication,
not a lower bound for the actual cube moment. An actual zero-free
improvement still requires a sufficiently strong sparse cube-indexed
moment, a different exact detector dictionary, or an independent
inverse estimate. No such assertion is made in this note.

