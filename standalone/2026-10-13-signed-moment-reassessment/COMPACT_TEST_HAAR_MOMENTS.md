# The compact-test hierarchy and the exact physical comparison

**Status:** standalone corollaries of the determinant-model theorem, with
complete test adapters. No estimate for the physical discrepancy below
is proved.

**Author:** root. The source theorem was developed by the replica agent
with root and signed-family contributions. The compact-test deductions
in this file are reviewed separately in
[CAUSAL_HAAR_INDEPENDENT_REVIEW.md](CAUSAL_HAAR_INDEPENDENT_REVIEW.md).

**Exact local source:**
[CAUSAL_ORBITS_AND_DENSE_LIFTS.md](CAUSAL_ORBITS_AND_DENSE_LIFTS.md),
44,355 bytes, SHA-256
dc8f645731302f2e2059cd115cc70564409af98c08c48a3f30f7d081c917a817,
Theorems 6.2, 7.2, 7.4 and Lemma 7.3. The enclosing frozen commit
binds those unchanged bytes.

Keep its fixed group representation \(\rho\), primitive target
\(\nu_0\), independent local probability space \(\Omega\), and the
specified fixed \(S\). In particular retain the local deletion
probability \(1/N\mathfrak p\). Put \(m_0=\dim V^{\mathcal G}\) and
retain its determinant coefficients \(b_\omega(\mathfrak n)\).

## 1. Sufficiency for every smooth compact norm test

For \(W\in C_c^\infty((0,\infty))\), define

\[
\mathcal B_\omega(D;W)=
\sum_{\mathfrak n}b_\omega(\mathfrak n)W(N\mathfrak n/D),
\qquad
\widehat W(s)=\int_0^\infty W(y)y^s\,\frac{dy}{y}.
\tag{1.1}
\]

The sum is finite for every \(D>0\). The test may be complex.

### Theorem 1.1

If \(m_0=0\), then for every fixed \(k\ge1\), every fixed such
\(W\), and every \(\epsilon>0\),

\[
\boxed{
\mathbb E_\Omega|\mathcal B_\omega(D;W)|^{2k}
\ll_{\rho,S,\nu_0,k,W,\epsilon}D^{k+\epsilon}
\qquad(D\ge2)
}
\tag{1.2}
\]

unconditionally. If \(m_0>0\), the same conclusion follows from
\(L_K(s,\nu_0)\ne0\) throughout \(\Re s>1/2\).

**Proof.** With \(y=e^x\), the Mellin transform is
\(\int W(e^x)e^{sx}\,dx\), over a fixed compact interval.
It is entire. Repeated integration by parts shows, for every
fixed closed real strip and every integer \(N\ge0\),

\[
|\widehat W(\sigma+it)|\ll_{W,N,\alpha,c}(1+|t|)^{-N},
\qquad \alpha\le\sigma\le c.
\tag{1.3}
\]

Under exactly the alternatives in the statement, source
Theorems 7.2 and 7.4 provide the holomorphic
\(L^{2k}(\Omega)\)-valued continuation

\[
F(s)=\frac{\mathcal H(s)}{L_K(s,\nu_0)^{m_0}}X(s),
\qquad
\|F(\sigma+it)\|_{2k}\ll(2+|t|)^A
\tag{1.4}
\]

on any closed strip \(1/2<\alpha\le\sigma\le c\).
When \(m_0=0\), take \(A=0\). The constants here are for the
fixed character, order, representation and strip.

On \(c>1\), the coefficient majorant
\(\sum |b_\omega(\mathfrak n)|(N\mathfrak n)^{-c}
\le\zeta_K(c)^{\dim V}\), uniformly in \(\omega\), and (1.3)
justify Mellin inversion in the Banach space:

\[
\mathcal B_\omega(D;W)=\frac1{2\pi}\int_{\mathbb R}
\widehat W(c+it)D^{c+it}F(c+it)\,dt.
\tag{1.5}
\]

Choose \(N>A+2\) in (1.3). The two vertical integrals on the
strip are absolutely convergent in \(L^{2k}\), and its
horizontal integrals at height \(T\) have norm
\(O_D((1+T)^{A-N})\). Banach-valued Cauchy integration
therefore shifts (1.5) to \(\Re s=\alpha\). It follows that

\[
\|\mathcal B_\omega(D;W)\|_{2k}
\le\frac{D^\alpha}{2\pi}\int_{\mathbb R}
|\widehat W(\alpha+it)|\,\|F(\alpha+it)\|_{2k}\,dt
\ll D^\alpha.
\]

Set \(\alpha=1/2+\epsilon/(2k)\), with
\(c>\max(1,\alpha)\), and raise to the power \(2k\).
This proves (1.2). Only the analytically continued \(F\)
is shifted; no raw Euler-product convergence below one
is asserted. \(\square\)

## 2. A converse for the full compact-test class

A single arbitrary compact test need not have a zero-free
Mellin transform. The preceding sufficiency statement alone
does not give a converse for that single test.

### Theorem 2.1

Suppose \(m_0>0\), and fix one integer \(k\ge1\).
The assertion that (1.2) holds for **every**
\(W\in C_c^\infty((0,\infty))\) and every \(\epsilon>0\)
is equivalent to

\[
L_K(s,\nu_0)\ne0\qquad(\Re s>1/2).
\tag{2.1}
\]

Each test's implied constants may depend on that fixed test.
It is enough to assume the asserted moments for all
nonnegative real compact tests.

**Proof of necessity.** For a fixed \(W\), write
\(M_W(D)=\mathbb E\mathcal B_\omega(D;W)\).
Hölder and the assumed moment give
\(|M_W(D)|\ll_{W,\eta}D^{1/2+\eta}\) for every
\(\eta>0\). If \(\operatorname{supp}W\subset[a,b]\),
then \(M_W(D)=0\) for \(0<D<1/b\).
Consequently

\[
\int_0^\infty M_W(D)D^{-s}\,\frac{dD}{D}
\tag{2.2}
\]

is holomorphic for \(\Re s>1/2\), with compact-uniform
absolute domination. Absolute interchange on \(\Re s>1\)
identifies it with

\[
\widehat W(s)\,
\frac{\mathcal H(s)}{L_K(s,\nu_0)^{m_0}}.
\tag{2.3}
\]

Suppose the target had a zero \(\rho\) with \(\Re\rho>1/2\).
Choose a nonzero nonnegative
\(\varphi\in C_c^\infty((-\delta,\delta))\), where
\(\delta=\pi/[4(1+|\Im\rho|)]\), and put
\(W(y)=\varphi(\log y)\). Then

\[
\Re\widehat W(\rho)
=\int\varphi(x)e^{(\Re\rho)x}\cos((\Im\rho)x)\,dx>0.
\tag{2.4}
\]

This is one fixed admissible test. Its Mellin transform does
not cancel the target zero, and \(\mathcal H(\rho)\ne0\)
by the source theorem. Thus (2.3) has a pole at \(\rho\),
contradicting the holomorphy of (2.2) and meromorphic
uniqueness. A principal pole at one gives a zero of the
reciprocal and causes no exception. This proves necessity.
Sufficiency is Theorem 1.1. \(\square\)

The test in this contradiction may depend on a hypothetical
zero because the premise covers every fixed test. This
argument does not assume a bound uniform across all tests.
The source's single Gaussian detector gives its stronger
single-test equivalence separately.

## 3. The native compact-test benchmark and the missing discrepancy

For the original one-dimensional sextic representation
\(\rho(g)=g\), the local masked mean is exactly one, so
\(m_0=0\), \(\mathcal H=1\), and no additional small-prime
deletion is needed for either mean normalization. For primitive
\(\nu\), the original fixed native \(S\) suffices. If \(\nu\)
is imprimitive, include among the fixed exclusions every prime
where its zero extension differs from its primitive inducing
character. This leaves the literal physical coefficients unchanged:
columns divisible by those primes already have coefficient zero.
With these existing coefficient exclusions, its random coefficients
are the literal \(\mu_K(\mathfrak n)\nu(\mathfrak n)
\chi_\omega(\mathfrak n)\), and the primitive inducing character
agrees with \(\nu\) outside the excluded primes.
Theorem 1.1 therefore gives the compact-test
Haar benchmark at every fixed order, unconditionally.

Now retain the actual physical row sum \(A_u(D;W)\), its
nonnegative Schwartz weight \(\Phi(u/\sqrt H)\), and all
nonzero rows. For \(H\ge1\), put

\[
Z_H=\sum_{u\ne0}\Phi(u/\sqrt H)\ll_\Phi H,
\]

\[
\Delta_{2k}(D,H;W)=
\sum_{u\ne0}\Phi(u/\sqrt H)|A_u(D;W)|^{2k}
-Z_H\,\mathbb E_\Omega|A_\omega(D;W)|^{2k}.
\tag{3.1}
\]

All these sums are well defined; compact support gives a
uniform finite column majorant, and \(\Phi\) is summable
on the lattice. The second term is
\(O_{\epsilon,k,W,\nu,S,\Phi}(H D^{k+\epsilon})\).
Therefore the desired bound for this **same smoothed
physical row measure** is equivalent to a bound
\[
|\Delta_{2k}(D,H;W)|\ll_\epsilon H D^{k+\epsilon}.
\tag{3.2: OPEN}
\]

This equivalence is an exact subtraction using a proved
reference estimate; it is not a new estimate on
\(\Delta_{2k}\). In one direction use the triangle
inequality; in the other add the reference term back.
If \(\Phi\) majorizes the unit norm ball, the smoothed
physical bound implies the original hard row bound.
No converse from a single hard cutoff to this Schwartz
measure is used.

The earlier PR #911 CRT translation theorem explains why
complete local laws alone do not give (3.2). The physical
short row measure retains correlations that the independent
probability model does not determine. Proving the signed
comparison at the required height remains the arithmetic
task. This note does not claim it, even at order four.
