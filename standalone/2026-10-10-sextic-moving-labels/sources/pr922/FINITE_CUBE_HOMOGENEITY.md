# The reflected finite rays have the contragredient cube law

**Status:** proposed source-conditional finite covariance theorem. The
actual reunited source coefficients satisfy a cube-scaling identity.
Their multiplicative finite-character expansion is therefore supported
on the single cubic coset `bar(rho) · {xi : xi^3=1}`. This supplies
the finite-character compatibility needed for a subsequent completed
theta transformation; it does not itself prove a moment estimate.

**Authorship:** finite_ray_residue. Independent review is to be recorded
against the exact frozen contents.

**Dependencies:** Sections 1–4 of
[FINITE_RAY_REUNION.md](FINITE_RAY_REUNION.md), with its exact PR #920
and primitive-source locks; the imported `paper2.tex` finite Fourier,
reduced-denominator, `eq:ray-multiplier`, and `eq:ray-additive-crt`
formulas; and the explicitly derived all-cusp coefficient shape in
[ALL_CUSP_COEFFICIENT_ADAPTER.md](ALL_CUSP_COEFFICIENT_ADAPTER.md).
The present proof does not assume the cube covariance used as an
explicit hypothesis in Section 4 of that adapter: it proves that
hypothesis from the actual Fourier data. The adapter's Sections 1–3
are its independent coefficient input.

## 1. The finite output coefficient

Retain the fixed characters eta,rho, bad set S, period L, squarefree
primary row k, and the baseline source labels h of the reunion note.
For each h, let `c0,h`, `sigma_h`, `psi_h`, `kappa0,h` be the
source's bad denominator, cusp, additive phase, and bad Kubota factor
at active product k. Write

\[
\begin{aligned}
C_h(s,k)&=\widehat\phi_\rho(h)\overline{\kappa_{0,h}(k)}
\alpha(c_{0,h})^2(Nc_{0,h})^{1-2s}\Gamma_{c_{0,h}}(k),\\
\Gamma_{c_0}(k)&=\mu(k)\alpha(k)\gamma_2(k)
\chi_k(-4)\chi_k(\lambda)^3\chi_k(c_0)^2.
\end{aligned}
\tag{1.1}
\]

Fix a bad denominator c0, including its source normalizing unit, and
a cusp sigma. Define the finite periodic function on integral m by

\[
F_{\sigma,c_0}(s,k;m)
=\sum_{\substack{h\bmod L\\c_{0,h}=c_0,\ \sigma_h=\sigma}}
C_h(s,k)\psi_h(m).
\tag{1.2}
\]

Empty index sets give the zero function. Dependence on the fixed
residue of k is retained. Every phase has a period supported at S,
and a single fixed S-supported modulus may be used for all functions
in (1.2). No value of m at a bad prime is discarded.

### Theorem 1.1

For every primary b coprime to S, every integral m, and every s,

\[
\boxed{
F_{\sigma,c_0}(s,k;b^3m)
=\overline{\rho(b)}^{\,3}F_{\sigma,c_0}(s,k;m).
}
\tag{1.3}
\]

The element b need not be squarefree and need not be coprime to m
or k. The statement is about the fixed finite function; it does not
replace any separate row-character zero mask.

## 2. The exact Fourier relabeling

For fixed b, use the permutation

\[
h\longmapsto h_b=b^3h\pmod L.
\tag{2.1}
\]

As in the reunion proof, representatives can be chosen at arbitrarily
high fixed bad precision. This does not change the translated theta
function, since changing h by L changes its translation by `3O`.
The primary support and bad-prime mask of the actual multiplier give
`phi_rho(bx)=rho(b)phi_rho(x)` for every residue x. Finite Fourier
inversion consequently gives

\[
\boxed{
\widehat\phi_\rho(b^3h)
=\rho(b)^{-3}\widehat\phi_\rho(h)
=\overline{\rho(b)}^{\,3}\widehat\phi_\rho(h).
}
\tag{2.2}
\]

Indeed in the defining sum for the left side substitute `y=b^3x`.
This is a permutation of all residues, with all nonunit zeros intact.

Write the source matrices for h and h_b as

\[
g=\begin{pmatrix}a&\beta\\c&\delta\end{pmatrix},
\qquad
g_b=\begin{pmatrix}a_b&\beta_b\\c_b&\delta_b\end{pmatrix}.
\tag{2.3}
\]

Multiplication of h by a bad-modulus unit preserves the reduced bad
denominator. Because b is primary, it also preserves the normalizing
unit. Thus `c_b=c=c0 k`. At sufficiently high fixed bad precision,
the source numerator and its CRT inverse satisfy

\[
\boxed{
a_b\equiv b^3a,\qquad
\delta_b\equiv b^{-3}\delta,\qquad
\beta_b\equiv\beta.
}
\tag{2.4}
\]

To see this, choose the good-prime Fourier representatives zero at
that precision. The numerator
`a=lambda^2c(h/L+sum_(p|k)h_p/p)` then scales by b cubed. At primes
of c0, delta is the inverse of a; at the other bad primes it is zero.
These are exactly the source CRT conditions, so delta scales by
`b^{-3}`. Comparing `a delta-1` before dividing by c gives the last
congruence. The independent good-prime congruences for delta are
imposed by CRT. No claim of an integral global diagonal scaling is
needed.

Since b is primary, `b^3=1 mod3`. The source H matrix selecting the
cusp depends only on the required residues of a and c modulo 3.
Those are unchanged. Hence (2.1) permutes the label set with the fixed
c0 and sigma in (1.2), including the two nonstandard cusps.

## 3. Kubota and additive phases at every cusp

### Lemma 3.1

Under (2.1),

\[
\kappa_{0,h_b}(k)=\kappa_{0,h}(k),
\qquad
\psi_{h_b}(b^3m)=\psi_h(m).
\tag{3.1}
\]

**Proof.** Check the three cases of the source's fixed multiplier.

When `3|c`, the bad Kubota factor is `(c0/a)_3`. Its primary
denominator scales by b cubed at its fixed supplementary conductor,
so the ratio is `(c0/b^3)_3=1`.

When `v_lambda(c)=1`, the factor is

\[
\kappa_0=
\left(\frac{-u_0}{a-u_0\beta}\right)_3
\left(\frac{c_0/u_0}{a}\right)_3,
\qquad u_0\in\{\lambda,-\lambda\}.
\tag{3.2}
\]

The same u0 is used because c is unchanged. The second denominator
scales by b cubed and contributes ratio one. For the first factor,
the numerator is supported at lambda. Since lambda divides c0, the
source construction has `beta=0` to its fixed large lambda-adic
precision. We may choose that precision greater than the conductor
of the fixed denominator character `(-u0/·)_3`. The same holds for
beta_b, by (2.4). Thus `a_b-u0 beta_b` is congruent to
`b^3(a-u0 beta)` at that conductor. The first ratio is therefore
`(-u0/b^3)_3=1`. This retains the ramified multiplier rather than
silently applying the unramified formula there.

When lambda does not divide c, the factor is `(a/c0)_3`, whose
ratio is `(b^3/c0)_3=1` directly. Unit c0 is included. This proves
the first assertion in all cases.

For the second assertion, the exact bad additive factor is

\[
\psi_h(m)=e\!\left(-\frac{\delta_0 k^{-1}m}{\lambda^3c_0}\right).
\tag{3.3}
\]

The congruence `delta_b=b^{-3}delta` holds modulo
`lambda^3c0`, while k and c0 are fixed. Substitution of b cubed m
cancels this factor exactly. QED.

**Proof of Theorem 1.1.** In (1.2) evaluated at b cubed m, reindex
by `h_b=b^3h`. The label set is preserved. All factors in C except
the finite Fourier coefficient are unchanged by Lemma 3.1 and the
fixed c0. Equation (2.2) contributes `bar(rho(b))^3`; the additive
phase is exactly psi_h(m). Summing proves (1.3). QED.

## 4. Compatibility with the actual cusp coefficients

The coefficient adapter proves directly from the source's tau,
tau1, and tau2 formulas that, for every primary b coprime to 3,

\[
\boxed{
d_\sigma(b^3\ell)=\sqrt{Nb}\,d_\sigma(\ell)
\quad(\sigma\in\{0,+,-\},\ \ell\in\lambda^{-4}O).
}
\tag{4.1}
\]

The squarefree factor, unit class, and ramified exponent stay fixed
under this operation. There is no requirement that b be coprime to
the squarefree factor. Zero support cases remain zero.

For clarity, the intrinsic additive phases in the two nonstandard
cusps do not change this conclusion. Their phase is `breve e(ell)`.
Writing `b=1+3t` gives

\[
b^3-1=9t+27t^2+27t^3\in9O=\lambda^4O.
\tag{4.2}
\]

Hence `(b^3-1)ell` is integral and its trace is an integer, so
`breve e(b^3ell)=breve e(ell)`. The external source phase is handled
separately and exactly by Lemma 3.1; the two phases are not confused.

After extracting `gamma2(n)` and the explicit norm and angular
factors, the remaining n-dependence in a fixed unit and ramified
sector consists of:

- the function `F_(sigma,c0)(s,k;u lambda^(j+4)n)`;
- the fixed cubic supplementary character in n from that cusp;
- the intrinsic finite additive phase, if present.

Every supplementary character has cube one, and the intrinsic phase
is invariant under multiplying n by a primary cube by (4.2). Thus
their product, denoted `E(n)` on primary n coprime to S, satisfies

\[
\boxed{E(b^3n)=\overline{\rho(b)}^{\,3}E(n).}
\tag{4.3}
\]

All unit and ramified sectors are retained. The same statement holds
for every finite linear combination in the complete reflected
coefficient. Row masks and good-prime deformation factors are separate
from E and are retained in applications.

## 5. The exact multiplicative ray support

Choose a fixed S-supported period B for E and rho, including 3, and
let

\[
G=\{x\in(O/B)^*:x\equiv1\pmod3\}.
\tag{5.1}
\]

This is the finite group of primary unit residues. Each class has a
primary representative coprime to S. All the functions just defined
restrict to functions on G, and rho is a character of G. Expand E by
ordinary finite character orthogonality:

\[
E(n)=\sum_{\rho'\in\widehat G}c_{\rho'}\rho'(n),
\qquad
c_{\rho'}=\frac1{|G|}\sum_{x\in G}E(x)\overline{\rho'(x)}.
\tag{5.2}
\]

### Theorem 5.1

If `c_(rho')` is nonzero, then

\[
\boxed{(\rho')^3=\overline\rho^{\,3}\quad\text{on }G.}
\tag{5.3}
\]

Equivalently the expansion is supported only on

\[
\boxed{\rho'=\overline\rho\,\xi,\qquad\xi^3=1.}
\tag{5.4}
\]

**Proof.** For each b in G, apply (4.3) to the expansion (5.2).
Uniqueness of finite Fourier coefficients gives

\[
c_{\rho'}\rho'(b)^3
=c_{\rho'}\overline{\rho(b)}^{\,3}.
\tag{5.5}
\]

When the coefficient is nonzero, division proves (5.3) for every b.
Multiplying rho' by rho gives (5.4), and the converse is immediate.
All statements concern primary residues; they therefore respect the
source's unique primary-generator convention. Extend each character
by the literal zero mask at S when writing the arithmetic series.
QED.

## 6. What the identity supplies

For the next completed theta series, each finite ray character rho'
in the actual output has the **same cube**, namely `bar(rho)^3`.
The cube Euler factors may therefore be matched uniformly across the
finite decomposition, including all three cusps. One must still carry
the actual archimedean character, row character, divisibility weights,
and zero masks when applying the next transformation.

This conclusion is stronger than expanding an arbitrary finite
periodic function into unrelated ray characters. It follows from the
homogeneous actual source multiplier. It establishes no bound for the
remaining signed row covariance and no generalized moment estimate.
