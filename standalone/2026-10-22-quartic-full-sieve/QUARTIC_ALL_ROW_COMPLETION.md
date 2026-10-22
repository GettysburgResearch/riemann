# Quartic all-row completion with decreasing Mellin scales

## Status

This note proves an exact completion identity for the primitive quartic Gauss
polynomial, including every nonzero numerator and an external puncture. It
does **not** prove the centered mean estimate needed for a new zero-free
boundary. Every correction decreases the spectral packet parameter, and no
initial fourth-power-free reduction is needed. A decrease is not necessarily
an analytic improvement: the reciprocal packet parameter can control the
incoming cusp height.

Primary inputs are David--Dunn--Hamieh--Lin (DDHL),
[arXiv:2306.11875v4](https://arxiv.org/html/2306.11875v4), equations
(3.4)--(3.7), (4.4), (4.24)--(4.28), Proposition 4.3, and
Castillo--de Faveri--Dunn (CDFD),
[arXiv:2604.01316v2](https://arxiv.org/html/2604.01316v2), Lemma 6.1 and
Corollary 6.2. The high-valuation identity below follows directly from their
local Gauss-sum formulas. The full-numerator positive mean in
[de Faveri--Dunn--Hoffstein, arXiv:2607.07911v2](https://arxiv.org/html/2607.07911v2),
Proposition 8.1, is a separate input and must not be confused with a centered
primitive mean.

## 1. Notation

Work in \(F=\mathbb Q(i)\), write \(\lambda=1+i\), and use primary
generators for ideals prime to \(\lambda\). All radicals below omit
\(\lambda\). Let \(\xi\) be a unitary angular Hecke character and let
\(v\in\{1,1+\lambda^3\}\pmod4\). Set

\[
 \psi_Q(k,s,\xi;v)
 =\sum_{\substack{c\equiv v\ (4)\\(c,Q)=1}}
       \frac{g_4(k,c)\xi(c)}{(Nc)^s},
 \qquad \psi=\psi_1.
\]

Initially \(\Re s>3/2\). For an odd squarefree \(A\), put

\[
 \Delta_A(s,\xi)=\prod_{p\mid A}(1-\xi(p)^4(Np)^{3-4s}),
\]

\[
 \Delta_A^*(x,s,\xi)
  =\prod_{p\mid A}
       \left(1+g_2(x/p,p)\xi(p)^2(Np)^{1-2s}\right).
\]

The convention is \(g_2(x/p,p)=0\) when \(p\nmid x\). When
\(p\parallel x\), this quadratic Gauss sum has absolute value
\((Np)^{1/2}\).

For \(k\ne0\), define the mutually coprime squarefree products

\[
 a=\prod_{\operatorname{ord}_p k=1}p,\quad
 b=\prod_{\operatorname{ord}_p k=2}p,\quad
 c=\prod_{\operatorname{ord}_p k=3}p,\quad
 T=\prod_{\operatorname{ord}_p k\ge4}p.
\]

Write \(k=ab^2c^3r\). Thus \(r\) retains the entire valuations at the
primes in \(T\), as well as its fixed ramified part; we do not replace it by
a fourth-power-free numerator. For a fixed odd puncture \(Q\), let

\[
 d=\prod_{\substack{p\mid Q\\p\nmid k}}p,
 \qquad R=bcdT.
\]

Then \(\operatorname{rad}(kQ)=abcdT\), and \((abcd,r)=1\).

## 2. The high-valuation finite difference

If \(p\nmid\gamma\) and \(p^4\mid k\), then

\[
\boxed{
 \Delta_p(s,\xi)\psi_{\gamma p}(k,s,\xi;v)
 =\psi_\gamma(k,s,\xi;v)
   -\xi(p)^4(Np)^{4-4s}\psi_\gamma(k/p^4,s,\xi;v).
}
\tag{2.1}
\]

**Proof.** Write a modulus as \(p^j m\), with \((p,m)=1\). For
\(j=1,2,3\), the local Gauss sum vanishes, since \(p^4\mid k\) and the
local multiplicative character is nonprincipal. For \(j=4\), it equals
\(\varphi(p^4)=(Np)^4-(Np)^3\). For \(j\ge5\), lifting the additive
sum gives

\[
 g_4(k,p^j)=(Np)^4g_4(k/p^4,p^{j-4}).
\]

Indeed, the quartic symbols at \(p^j\) and \(p^{j-4}\) agree, and each
unit residue class modulo \(p^{j-4}\) has \((Np)^4\) lifts. The fourth
power does not alter the CRT reciprocity factor, the character at \(m\),
or the ray class modulo \(4\). Thus the sum of the terms with \(j\ge4\)
is

\[
 \xi(p)^4(Np)^{4-4s}\psi_\gamma(k/p^4,s,\xi;v)
 -\xi(p)^4(Np)^{3-4s}\psi_{\gamma p}(k,s,\xi;v).
\]

Adding the \(j=0\) term proves (2.1). This proof works equally when
\(\operatorname{ord}_p k\ge8\); it does not recursively introduce one
term for every fourth power. \(\square\)

Applying (2.1) at all primes in \(T\) gives

\[
 \psi_{abcdT}(k,s,\xi;v)
 =\Delta_T(s,\xi)^{-1}
   \sum_{t\mid T}\mu(t)\xi(t)^4(Nt)^{4-4s}
       \psi_{abcd}(k/t^4,s,\xi;v).
\tag{2.2}
\]

## 3. Exact all-row primitive completion

For \(e\mid b\) and \(f\mid d\), let

\[
\begin{split}
 C_{e,f}(k,s;\xi,v)
 ={}&\mu(ef)(-1)^{C(ef,v)}\chi_e(-1)\xi(e^3f)
       (Ne)^{2-3s}(Nf)^{-s}\\
 &\times
 \overline{g_4(k/e^2,e)}\,g_4(k/e^2,f),
\end{split}
\]

where \(C\) is the finite reciprocity sign from CDFD. Then

\[
\boxed{
\begin{split}
 \psi_{\operatorname{rad}(kQ)}(k,s,\xi;v)
 ={}&\Delta_a^*(acr,s,\xi)^{-1}\Delta_R(s,\xi)^{-1}\\
 &\times\sum_{\substack{t\mid T\\e\mid b,\ f\mid d}}
 \mu(t)\xi(t)^4(Nt)^{4-4s} C_{e,f}(k,s;\xi,v)\\
 &\hspace{25mm}\times
 \psi\left(\frac{kf^2}{t^4e^2},s,\xi;efv\right).
\end{split}
}
\tag{3.1}
\]

**Proof.** Apply CDFD Corollary 6.2 to every term of (2.2), with its
\(r\) replaced by \(r/t^4\). The factors involving \(a\), \(e\), and
\(f\) are unchanged when their numerator is divided by \(t^4\), because
\((t,aef)=1\), and fourth powers have trivial quartic and quadratic
symbols. In particular

\[
 \Delta_a^*(acr/t^4,s,\xi)=\Delta_a^*(acr,s,\xi).
\]

Combining the pairwise coprime \(\Delta\)-products gives \(\Delta_R\).
This proves (3.1). \(\square\)

The identity includes all numerator valuations. It is not an assertion only
for squarefree or fourth-power-free rows. It also retains an arbitrary
external puncture \(Q\), with its primes divided into those already in
\(k\) and the independent product \(d\).

## 4. Normalized Mellin scales

For \(W\in C_c^\infty((0,\infty))\), define

\[
 S_Q(k,D)=\sum_{\substack{n\equiv v\ (4)\\(n,kQ)=1}}
      \frac{g_4(k,n)\xi(n)}{Nn}W(Nn/D).
\]

Its Mellin integrand is
\(D^{s-1}\widehat W(s-1)\psi_{\operatorname{rad}(kQ)}(k,s,\xi;v)\).
Since the Gauss sums in \(C_{e,f}\) are primitive, their absolute values
are \((Ne)^{1/2}\) and \((Nf)^{1/2}\). Consequently each \((t,e,f)\)
term in (3.1), before expanding the two \(\Delta\)-factors, has scalar
magnitude \((Ne\,Nf)^{-1/2}\) and effective column length

\[
 D'=\frac{D}{(Nt)^4(Ne)^3Nf},
 \qquad k'=\frac{kf^2}{t^4e^2}.
\tag{4.1}
\]

If \(Nk\asymp K\), its new row scale and packet parameter are

\[
 K'=\frac{K(Nf)^2}{(Nt)^4(Ne)^2},\qquad
 L'=\frac{D'}{\sqrt{K'}}
 =\frac{L}{(Nt)^2(Ne)^2(Nf)^2},
 \quad L=\frac D{\sqrt K}.
\tag{4.2}
\]

Every one of these maps decreases \(L\). This is an exact scale statement,
not a bound on the associated automorphic norm. In particular, when
\(L'<1\), an incoming term of the form
\(y^s(L')^{s-1}\) is concentrated near \(y=1/L'\); a weighted norm can
therefore involve \(\max\{L',1/L'\}^{2-u}\), rather than just a positive
power of \(L'\). At the principal scale \(L=1\), every nontrivial scale
correction goes into this reciprocal regime.

The denominators have convergent geometric expansions for \(\Re s>3/4\).
For a \(R\)-smooth ideal \(j\), the \(\Delta_R^{-1}\) coefficient is
\(\xi(j)^4(Nj)^{3-4s}\); after Mellin normalization this is a unit phase,
an amplitude \((Nj)^{-1}\), and the further shift \(D'\mapsto D'/(Nj)^4\).
For an \(a\)-smooth ideal \(h\), the \((\Delta_a^*)^{-1}\) coefficient
has the form

\[
 \kappa_h(k)(Nh)^{3/2-2s},\qquad |\kappa_h(k)|=1,
\]

where

\[
 \kappa_h(k)=\prod_{p\mid a}
  \left(-\xi(p)^2\frac{g_2(acr/p,p)}{\sqrt{Np}}\right)^{\operatorname{ord}_p h}.
\]

After Mellin normalization it contributes amplitude \((Nh)^{-1/2}\) and
shift \(D'\mapsto D'/(Nh)^2\). Thus the complete expansion consists of
full Gauss polynomials with

\[
 \boxed{\quad
 D''=\frac{D}{(Nt)^4(Ne)^3Nf\,(Nh)^2(Nj)^4},\quad
 k'=\frac{kf^2}{t^4e^2},\quad
 L''=\frac{L}{(Nt)^2(Ne)^2(Nf)^2(Nh)^2(Nj)^4}.
 \quad}
\tag{4.3}
\]

The coefficient magnitude is
\((Ne\,Nf\,Nh)^{-1/2}(Nj)^{-1}\). For a test supported in \([1,2]\),
terms with \(D''<1/2\) vanish exactly. Thus the polynomial identity has
only finitely many nonzero terms, although the Dirichlet-series completion
uses geometric series.

## 5. Why this is not yet the needed centered estimate

At \(\Re s=1\), both inverse Euler products are bounded by
\((Nk\,NQ)^\epsilon\) for every fixed \(\epsilon>0\). That pointwise
bound follows from
\(\prod_{p\mid kQ}(1-(Np)^{-1/2})^{-1}\ll_\epsilon(Nk\,NQ)^\epsilon\).
It does not justify a centered quadratic estimate after averaging over
\(k\).

In particular, a prime in \(h\) imposes \(p\parallel k\). For an odd
exponent of \(p\) in \(h\), its coefficient contains a nontrivial
quadratic character of \(k/p\) modulo \(p\). The corrected quadratic
form therefore contains both valuation masks and quadratic row twists.
Replacing them by absolute values and applying an unweighted positive
mean generally loses their density. A sum such as
\(\sum_h(Nh)^{-1/2}\) is not convergent over all ideals.

Moreover, the first Poisson identity requires cancellation of a precise
finite-scale diagonal inside a signed coprimality expansion. A bound for
the full positive mean, even with the correct angular character, does not
identify that diagonal or bound the centered form.

## 6. Fixed angular type: a separate matrix issue

The corrected DDHL-v4 Gauss-square identity is
\(\widetilde g_4(c)^2=\mu_F(c)c/|c|\); see
[CORRECTED_QUARTIC_CODEC.md](CORRECTED_QUARTIC_CODEC.md) for its proof and
the counterexample to the extra-ray version. It converts the first Poisson
Möbius coefficient to quartic Gauss sums with angular type
\(\ell=\pm1\). DDHL Proposition 4.3 shows that their completed Dirichlet
series are entire:

\[
 \widehat\psi_i(s,k,\ell)
 =G_\infty(s,\ell)\zeta_{F,\lambda}(4s-3,\ell)\psi_i(s,k,\ell),
\]

\[
 G_\infty(s,\ell)
 =\prod_{u\in\{3/4,1/2,1/4\}}
       \Gamma_{\mathbb C}(s+|\ell|/2-u).
\]

Their functional equation swaps \((s,\ell)\) with \((2-s,-\ell)\),
including \((Nk)^{1-s}(\bar k/|k|)^\ell\) and the finite cusp matrix.
This removes the quartic theta pole, but does not by itself remove an
arithmetic diagonal from the full mean.

For \(\ell=1\), DDHL (4.4) gives explicitly

\[
 K(0,s,1)=\frac{\pi}{s-1/2}
       \begin{pmatrix}0&1\\-1&0\end{pmatrix}.
\]

Their matrix \(\phi(s,0,1)\) is diagonal, so the scattering blocks are
off-diagonal. In a fixed input column, the incoming and outgoing constant
terms are orthogonal components; their Hermitian cross term vanishes.
The Hilbert--Schmidt trace has the same property. A scalar spherical
Maass--Selberg cross term cannot simply be imported into this nonzero
angular setting. Conversely, the invariant matrix norm includes companion
Fourier coefficients, so its centered main term must be related explicitly
to the scalar primitive norm needed by the inverse problem.

## 7. What would finish the route

The missing assertion is a uniform **centered**, fixed-angular,
arithmetic-mask mean for the full Gauss polynomials in (4.3), together with
an exact identification of its main term after the signed gcd expansion.
Both the scales in (4.3) and their reciprocals must be tracked in that
estimate. Their exact form identifies the cusp and arithmetic costs but does
not show those costs are summable.

For reference, a full raw quartic inverse estimate
\(I_4(D^\alpha,D)\ll D^{\alpha+\epsilon}\), with all amplification
punctures and shorter column scales retained, would give
\(B=1/2+3\alpha/8\). The target \(B=0.85\) corresponds to
\(\alpha=14/15\). This note has not established that raw estimate.
