# Native heat defect and an exact prime-removal target

**Status:** proposed exact finite-prime identities, their source-faithful
application, and a method-specific obstruction. The final defect estimate is
an explicitly unproved conditional target. No improved moment, zero-free
boundary, or RH claim is made.

**Scope:** the literal squarefree native product-column covariance after the
complete signed auxiliary reunion. All moving column exclusions, nonunit
character zeros, the physical product diagonal, and the original row weight
are retained. The finite diagnostic checks algebra, not asymptotic transfer.

**Exact source dependencies:**

- PR #927, commit `f9939c957f5aac6b2099b591e4988991700a152b`,
  `standalone/2026-10-10-sextic-signed-reunion/SIGNED_AUXILIARY_REUNION.md`,
  especially its complete signed auxiliary collapse and second Poisson
  identity; and `SMALL_W_CORE_AUDIT.md`, (1.3)--(1.5) and Section 4.
- PR #928, commit `ab98878279cd5614fe79bb94aa916e97c9ee50b4`,
  `standalone/2026-10-10-signed-graph-and-joint-descent/`, for the distinction
  between the physical product diagonal and artificial principal aliases.
- PR #911, commit `2f8b6a3898a722d0602a91dea73bac344a3bb7dd`,
  `research/exploratory/2026-10-10-two-hour-continuation/literature/PRIME_SLOT_ROUTE_STATUS.md`:
  the complementary
  independent-frequency short trace remains open; local Euler kernels need
  not be positive even after the radial unit projection.

The first source has already reunited the complete signed auxiliary sum and
returned the original native covariance. This note does not present that
round trip as new cancellation. Its additional result identifies precisely
which part of a positive finite-prime heat identity can see the remaining
coprime covariance, and expresses that part using the exact shorter native
prime-removal profiles.

## 1. The actual finite polynomial and the actual row measure

Work over the same Eisenstein ring and outside the fixed bad prime set as
the sources. The following argument also works over a finite product of
residue fields with nonprincipal multiplicative characters. Ideals use
their fixed source generators. Write \(\mathrm N\) for ideal or element norm.

Fix the reference parameter \(D\), the number of factors \(k\), and
\(L=D^k\). Let \(v(n)\) be the original finitely supported smooth native
\(k\)-factor coefficient, including its moving exclusions. In particular,
every nonzero column is squarefree and prime to the original fixed and
moving exclusions. Fix a finite-ray character \(\nu\).

The exclusions include the conductor of \(\nu\), so \(|\nu(n)|=1\) for
every column with \(v(n)\ne0\). This is the unitary source convention used
by the physical diagonal and the common-factor cancellation below. Put

\[
a_n=\mu(n)\overline{\nu(n)}v(n),\qquad
F(x)=\sum_{n\ {\rm sf}}a_n\chi_n(x).
\tag{1.1}
\]

Choose a finite set \(\mathcal P\) containing all primes appearing in these
columns and put

\[
M=\prod_{p\in\mathcal P}p,\qquad
\Omega=\prod_{p\in\mathcal P}\mathcal O/p.
\tag{1.2}
\]

Equip \(\Omega\) with normalized counting measure \(m\). This is a proof
device; the original physical rows are not replaced by independent random
coordinates. Define

\[
X_p(x)=\chi_p(x_p),\quad X_p(0)=0,\quad
\rho_p=1-\frac1{\mathrm Np}.
\tag{1.3}
\]

The good-prime characters are nonprincipal, so
\(\int X_p=0\) and \(\int|X_p|^2=\rho_p\). The zero at a nonunit is part of
every identity below.

For the actual radial Schwartz row test \(\Phi\), define the physical
density relative to \(m\) by

\[
w_H(x)=(\mathrm NM)
\sum_{\substack{s\ne0\\s\bmod M=x}}
\Phi(\mathrm Ns/H).
\tag{1.4}
\]

The sum converges absolutely, and for every function \(G\) on \(\Omega\),

\[
\int_\Omega w_HG\,dm
=\sum_{s\ne0}\Phi(\mathrm Ns/H)G(s\bmod M).
\tag{1.5}
\]

There is no assumption that \(w_H\) is close to constant. All scalar
identities below are stated for real \(w\); a complex \(\Phi\) is handled
exactly by applying them separately to its real and imaginary parts. Only
statements explicitly invoking positivity require \(w\ge0\).

The literal source diagonal is

\[
\Delta_v(x)=\sum_n|v(n)|^2\mathbf1_{(n,x)=1}.
\tag{1.6}
\]

It is not the constant Haar diagonal
\(\sum_n|v(n)|^2\prod_{p\mid n}\rho_p\). The pinned #927 return identity is

\[
\mathcal O_\xi[v]=\frac1L\sum_\eta c_\eta
\int w_H\bigl(|B_{\xi\eta,v}|^2-\Delta_v\bigr)\,dm.
\tag{1.7}
\]

The family of \(\eta\)'s is fixed and finite. Its coefficients need not be
positive. Equation (1.7), including its normalization, is imported from the
source; the finite-prime results below are proved here.

## 2. A positive identity with an explicit physical defect

Let \(E_p\) average the \(p\)-coordinate while fixing all other coordinates.
For positive weights \(\lambda_p\), define

\[
A=\sum_{p\in\mathcal P}\lambda_p(I-E_p),\qquad
P_t=e^{-tA}
=\prod_p\bigl(E_p+e^{-t\lambda_p}(I-E_p)\bigr).
\tag{2.1}
\]

The coordinate averages commute and are self-adjoint projections. Thus
\(P_t\) is a positive, constant-preserving, self-adjoint heat-bath
semigroup. For the arithmetic choice \(\lambda_p=\log\mathrm Np\),

\[
A\chi_n=(\log\mathrm Nn)\chi_n,\qquad
P_tF=\sum_n a_n(\mathrm Nn)^{-t}\chi_n.
\tag{2.2}
\]

Squarefreeness gives the unique decomposition

\[
F=F_{0,p}+X_pF_{1,p},
\tag{2.3}
\]

where both polynomials on the right are independent of \(x_p\). Define

\[
\begin{split}
\Gamma_p(F)
&=E_p|F|^2+|F|^2-2\operatorname{Re}(\overline F E_pF)\\
&=\mathop{\mathbb E}_{y_p}
 |F(x)-F(x_{\widehat p},y_p)|^2\\
&=(|X_p|^2+\rho_p)|F_{1,p}|^2\ge0,
\qquad \Gamma_A=\sum_p\lambda_p\Gamma_p.
\end{split}
\tag{2.4}
\]

**Theorem 2.1 (weighted heat identity).** For every real function \(w\) on
\(\Omega\),

\[
\boxed{\quad
2\operatorname{Re}\int w\overline F AF\,dm
=\int w\Gamma_A(F)\,dm+\int(Aw)|F|^2\,dm.
\quad}
\tag{2.5}
\]

**Proof.** Self-adjointness gives
\(\int wE_p|F|^2=\int(E_pw)|F|^2\). Add
\(\int(w-E_pw)|F|^2\) to the integral of the first line of (2.4). The result
is \(2\operatorname{Re}\int w\overline F(I-E_p)F\). Multiply by
\(\lambda_p\) and sum. Expanding (2.3), using
\(E_pX_p=0\) and \(E_p|X_p|^2=\rho_p\), proves the final line of (2.4).
All sums are finite. \(\square\)

For the physical density, the additional term is exactly
\(\int(Aw_H)|F|^2\). Dropping it is valid for constant Haar density and is
not valid for the original short rows. A pointwise or quadratic-form
estimate for this term is additional arithmetic input.

For completeness, its local expansion is

\[
\int (I-E_p)w\,|F|^2\,dm
=\int w\left[
 (|X_p|^2-\rho_p)|F_{1,p}|^2
 +2\operatorname{Re}(X_pF_{1,p}\overline{F_{0,p}})
\right]dm.
\tag{2.6}
\]

Thus the defect contains a signed cross-term between a prime-removed
polynomial and a polynomial omitting that prime. It is not itself a
positive influence energy.

## 3. The coprime sector is invisible to the positive innovations

For a real \(w\), define the exact coprime product-column covariance

\[
\mathcal C_w^{\rm cop}(F)=
\sum_{\substack{(n,m)=1\\(n,m)\ne(1,1)}}
a_n\overline{a_m}\int w\chi_n\overline{\chi_m}\,dm.
\tag{3.1}
\]

Here \((n,m)\ne(1,1)\) excludes the ordered pair of two unit ideals;
\((n,m)=1\) on the first line denotes coprimality. The selector is applied
to the original coefficient indices before any estimate. It is not a
positivity-preserving projection.

Every coefficient pair in \(\Gamma_p(F)\) comes from two columns both
divisible by \(p\). Therefore its coprime off-product part is identically
zero, coefficient by coefficient. The same is true of the squared norm of
\(\prod_{p\in J}(I-E_p)F\) for every nonempty set \(J\): both contributing
columns contain every prime in \(J\). This statement concerns those
coordinate innovations; it does not assert that all possible positive
operators have this property. Mixed derivatives on different left and
right prime sets can see coprime pairs, but their pairing has no automatic
positivity.

For coprime squarefree \(n,m\), every prime of \(nm\) occurs in exactly one
of the two characters. Consequently

\[
A(\chi_n\overline{\chi_m})
=(\log\mathrm Nn+\log\mathrm Nm)
  \chi_n\overline{\chi_m}.
\tag{3.2}
\]

Define \(\mathcal D_w^{\rm cop}(F)=\mathcal C_{Aw}^{\rm cop}(F)\). Projecting
(2.5) coefficientwise onto (3.1) gives

\[
\mathcal D_w^{\rm cop}(F)
=\sum_{\substack{(n,m)=1\\(n,m)\ne(1,1)}}
(\log\mathrm Nn+\log\mathrm Nm)a_n\overline{a_m}
\int w\chi_n\overline{\chi_m}\,dm.
\tag{3.3}
\]

This is the whole coprime sector of the left side of (2.5). None of it is
supplied by its positive \(\Gamma_A\) term. A proposed prime-influence
argument for the leading coprime covariance must estimate the signed
\(F_{0,p}\)--\(F_{1,p}\) cross-terms in (2.6).

## 4. Exact Duhamel formula and the cancellation of apparent heat decay

Write \(F_t=P_tF\). Differentiating the finite sum and using (2.5) gives

\[
-\frac{d}{dt}\int w|F_t|^2\,dm
=\int w\Gamma_A(F_t)\,dm+\int(Aw)|F_t|^2\,dm.
\tag{4.1}
\]

The constant term \(F_\infty=a_1\) is retained when it is present. Integrating
over \([0,\infty)\) is valid after subtracting that constant term. On the
coprime off-product sector, all surviving frequencies have strictly
positive eigenvalue and the positive innovation term is zero. Hence

\[
\boxed{\quad
\mathcal C_w^{\rm cop}(F)
=\int_0^\infty\mathcal D_w^{\rm cop}(F_t)\,dt.
\quad}
\tag{4.2}
\]

For every finite \(T\), the exact remainder is

\[
\mathcal C_w^{\rm cop}(F)
=\int_0^T\mathcal D_w^{\rm cop}(F_t)\,dt
 +\mathcal C_w^{\rm cop}(F_T).
\tag{4.3}
\]

No smallness of the last term is asserted without an estimate. Equivalently,
self-adjointness and (3.2) give the conservation law

\[
\boxed{\quad
\mathcal C_{P_tw}^{\rm cop}(F)
=\mathcal C_w^{\rm cop}(P_tF).
\quad}
\tag{4.4}
\]

This equality explains why independent coordinate noise alone does not
produce the missing saving. If the native factor variables satisfy
\(x_j=\mathrm Nn_j/D\), then

\[
F_t=L^{-t}B_{\nu,v_t},\qquad
V_t(x_1,\ldots,x_k)=(x_1\cdots x_k)^{-t}V(x_1,\ldots,x_k).
\tag{4.5}
\]

For \(t\) in a fixed bounded interval, this is the same permitted family of
smooth profiles with controlled finite seminorms. The exclusions are
unchanged. The factor \(L^{-2t}\) apparently gained by smoothing the row
measure is exactly the factor acquired by damping the native coefficients.
Restoring the original normalization restores it. Large \(t\) also changes
profile seminorms; it is not a uniform free parameter in an imported native
estimate.

There is likewise the positive identity

\[
P_t|F|^2-|P_tF|^2
=\int_0^tP_s\Gamma_A(P_{t-s}F)\,ds\ge0.
\tag{4.6}
\]

To prove it, differentiate \(P_s|P_{t-s}F|^2\). This identity retains the
same shared-prime support restriction. It does not bound the coprime
covariance by a new nonzero positive source term.

## 5. A native-only prime-removal formulation of the missing input

The Möbius relation is exact:

\[
\mu(n)\overline{\nu(n)}\log\mathrm Nn
=-\sum_{p\mid n}\log\mathrm Np\,
 \overline{\nu(p)}\mu(n/p)\overline{\nu(n/p)}.
\tag{5.1}
\]

For each prime \(p\), the actual coefficient in (2.3) is therefore

\[
F_{1,p}(x)=
-\overline{\nu(p)}
\sum_{\substack{m\ {\rm sf}\\(m,p)=1}}
\mu(m)\overline{\nu(m)}v(pm)\chi_m(x).
\tag{5.2}
\]

All original exclusions are still inside \(v(pm)\). For an ordered native
\(k\)-factor convolution, a prime dividing the squarefree product lies in
exactly one factor. Consequently (5.2) is exactly the sum of \(k\) native
families in which one factor has scale \(D/\mathrm Np\), the other factors
have scale \(D\), and all remaining factors exclude \(p\). For a coupled
smooth profile, replace its selected argument by
\((\mathrm Np)\mathrm Nm_j/D\); no tensor factorization is assumed. Empty
or bounded subunit scales are treated by the original physical support.

For the coprime sector define the oriented prime-removal pairing

\[
\begin{split}
\mathcal J_{p,w}(t)=
-\overline{\nu(p)}(\mathrm Np)^{-t}
\sum_{\substack{m,b\ {\rm sf}\\(m,b)=1,\ (mb,p)=1}}
&\mu(m)\mu(b)\overline{\nu(m)}\nu(b)
v(pm)\overline{v(b)}(\mathrm Nm\,\mathrm Nb)^{-t}\\
&\cdot\int wX_p\chi_m\overline{\chi_b}\,dm.
\end{split}
\tag{5.3}
\]

The repeated symbol \(dm\) outside the sum is Haar measure, not the ideal
index; all ideals in the sum retain the exclusions in their displayed
coefficients. A zero coefficient simply contributes zero. Grouping the
left-column primes in (3.3) proves

\[
\mathcal D_w^{\rm cop}(F_t)
=2\operatorname{Re}\sum_p(\log\mathrm Np)\mathcal J_{p,w}(t).
\tag{5.4}
\]

Thus (4.2) is an exact signed prime-removal formula, with the native
coefficient vector preserved. It can be decomposed into any disjoint prime
norm bands before integration. For an individual ordered pair, the
normalized weights are

\[
\frac{\log\mathrm Np}{\log\mathrm Nn+\log\mathrm Nm},
\qquad p\mid nm,
\tag{5.5}
\]

and their sum is exactly one. There is no extra divisor-counting or
logarithmic loss in this exact allocation. Taking absolute values before
the signed prime sum would be an additional relaxation.

Here is an explicit way to include every common-factor sector. For each
squarefree \(g\), put

\[
F_g=\sum_{\substack{a\ {\rm sf}\\(a,g)=1}}
\mu(a)\overline{\nu(a)}v(ga)\chi_a,
\qquad
w_g=w_H\mathbf1_{(g,x)=1}.
\tag{5.6}
\]

Uniquely writing the two original columns as \(n=ga,m=gb\), with
\(g=(n,m)\), gives

\[
\int w_H(|F|^2-\Delta_v)\,dm
=\sum_{g\ {\rm sf}}\mathcal C_{w_g}^{\rm cop}(F_g)
=\sum_g\int_0^\infty
\mathcal D_{w_g}^{\rm cop}(P_tF_g)\,dt.
\tag{5.7}
\]

The unit primitive pair is excluded, so (5.7) subtracts the physical
product diagonal exactly. The sums over \(g\) are finite. For each \(g\),
the active heat coordinates omit primes dividing \(g\); its row mask is
then independent of every active coordinate. No moving mask has been
averaged away. Formula (5.3) applies with \(v(n)\) replaced by \(v(gn)\),
with the added exclusion \((n,g)=1\), and with the row weight \(w_g\).

**Explicit unproved native defect criterion.** Uniformly over precisely the
source-required smooth profiles, finite rays, polynomial moving exclusions,
and physical heights, it would suffice to prove

\[
\left|\sum_g\int_0^\infty
\mathcal D_{w_g}^{\rm cop}(P_tF_g)\,dt\right|
\ll_{\epsilon,V,\Phi,k} H L D^\epsilon.
\tag{5.8}
\]

The fixed finite sum in (1.7) would then give the desired normalized signed
comparison \(\mathcal O_\xi[v]\ll H D^\epsilon\). For a complex row profile
one may use (5.8) for both real and imaginary parts. This is a sufficient
source-qualified input, not a theorem proved in this note.

Equation (5.8) is transparently equivalent to the original centered
covariance at this level of aggregation. Its useful additional structure
is the explicit prime-local representation (5.3): the unknown term is a
signed cross-correlation with one shorter native factor. It suggests a
scale induction or commutator estimate without demanding an
arbitrary-coefficient moment theorem. The formulas provide the correct
interface for such an estimate; they do not supply it.

In particular a bound merely on
\(\sum_p(\log\mathrm Np)\int w\Gamma_p\) cannot establish (5.8) for the
leading \(g=1\) coprime sector: its relevant coefficients are all zero.

## 6. Möbius signs are a gauge symmetry of the complete-residue model

At every good sextic prime choose a nonzero residue \(u_p\) with
\(\chi_p(u_p)=-1\). Such a residue exists because the local character has
order six. Let \(u\) be their CRT tuple. For every squarefree supported
column, including all zero-coordinate cases,

\[
\chi_n(ux)=\mu(n)\chi_n(x).
\tag{6.1}
\]

If \(F^+(x)=\sum_n\overline{\nu(n)}v(n)\chi_n(x)\), then
\(F(x)=F^+(ux)\). Multiplication by \(u\) preserves Haar measure, every
nonunit mask, the coordinate expectations, \(A\), and \(P_t\). It follows
that complete-residue independence and these positive heat identities have
the same constants for the native Möbius polynomial and its unsigned
coefficient version.

For the physical measure the change of variables instead gives

\[
\int w_H(x)|F(x)|^2\,dm(x)
=\int w_H(u^{-1}x)|F^+(x)|^2\,dm(x).
\tag{6.2}
\]

The large CRT multiplier generally does not preserve the original short
radial row window. Therefore Möbius cancellation can enter through the
arithmetic geometry of this physical density, not through a generic
complete-residue positivity argument alone. This is a limitation of the
specified method, not a claim that source-specific cancellation is
impossible.

The positivity in (2.4) also does not make the signed Euler kernels of the
independent Mellin frequencies positive. The source #911 counterexamples
and its remaining complementary short trace are compatible with every
identity here.

## 7. A finite native convolution witness and exact diagnostic scope

Take four distinct good prime coordinates and write

\[
F=2\sum_{1\le i<j\le4}X_iX_j.
\tag{7.1}
\]

This is exactly the squarefree two-factor convolution of a one-factor
coefficient supported with value one on four primes. The factor two counts
the two orderings, and \(\mu(p_ip_j)=+1\). It is not an arbitrary choice of
the six product coefficients. This description takes the trivial fixed
ray; for any specified unitary fixed ray, giving the one-factor profile
value \(\nu(p)\) at the selected prime cancels the displayed
\(\overline{\nu(p)}\) and yields the same polynomial. A finite smooth norm
profile with separated bumps realizes these one-factor coefficients, with
fixed exclusions if needed to select prime ideals of equal norm. This
realization is a finite test at one scale; no uniform asymptotic assertion
about such chosen profiles is made.

At the unit tuple \(x_p=1\), \(F=12\), \(|F|^2=144\), and its coprime
off-product part is exactly \(24\): there are six ordered complementary
prime-pair columns, each contributing four. Its Haar coprime mean is zero.
For diagnostic weights \(\lambda_p=1\), \(AF=2F\). At this tuple,

\[
\sum_p\Gamma_p(F)=288-36\sum_p\frac1{\mathrm Np},\qquad
\sum_p\bigl(|F|^2-E_p|F|^2\bigr)
=288+36\sum_p\frac1{\mathrm Np}.
\tag{7.2}
\]

Their sum is \(576=2\overline F AF\). The coprime part of the first
quantity is zero; that of the second is \(96=4\cdot24\), exactly the
coprime logarithmic derivative with these unit generator weights.

The accompanying exact-rational diagnostic checks all local nonunit
patterns, the weighted identity, the coprime projection, the heat
intertwining at rational coordinate noise parameters, and the Möbius gauge
on the six-root formal character space. It also checks the common-factor
decomposition (5.7) with its literal masks and physical product diagonal.
It uses the norms
\(73,109,181,277\), so the full residue-field local multiplicities are
integers. It does not replace the physical Schwartz weight by a unit point
and then claim an asymptotic counterexample. A point mass is used only to
falsify the proposed algebraic inference from Haar independence to every
positive row measure.

The smallest missing input remains a signed physical cross-correlation
estimate of the form (5.3), summed as in (5.8), with its actual smaller
native profiles and masks. Positive innovations, exact auxiliary reunion,
and heat smoothing by themselves leave that input unproved.
