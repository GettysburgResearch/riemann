# Cubic Gauss factorization at every cusp and the full coupled mean square

**Status:** new source-qualified analytic extension, proposed for independent review. The explicit classical cusp formulas remove the standard-cusp restriction from the quadratic–cubic composition. Together with the exact reunited-divisor cutoff, they give a mean-square bound for the whole coupled theta completion over squarefree primary rows. The stronger numerical exponent uses the separately reviewed source-conditional angular mean-square adapter. The full generalized moment hierarchy remains unproved.

**Primary coefficient source:** A. Dunn and M. Radziwiłł, *Bias in cubic Gauss sums: Patterson's conjecture*, arXiv:2109.07463v3, 14 May 2024, equations (1.7), (1.5), (5.7)–(5.8), (5.13)–(5.16), and Appendix A, viewed at https://arxiv.org/html/2109.07463v3. We use their explicit classical coefficient identities and the classical upper large sieves, not the paper's GRH-conditional main theorem or its conditional lower bounds.

**Exact companion inputs:** centered_a2_attack.md, frozen SHA-256 bbc139f956731482fcf9e33645bfe2832b7b7471594d9cbc1f21cd08eaf2ac5a, especially Corollary 6.4, Theorem 7.1, and its exact moving-mask proof; reunited_cusp_cutoff.md, frozen SHA-256 89cd204ae66ef615e7d630bf2c1e5524e134b76e30789dce7796a229e53a4340, especially Theorem 3.1 and its smooth insertion before the \(e,f\) split; PR #915 9959364671f89b86f3992ec5ed5e19f804eb607b; imported OpenAI math source adc7f1241b42e322a6451854ab7e4b4c146bf78a.

## 1. The exact coupled object and two scalar inputs

Keep the original object of PR #915:

\[
\mathcal C_{A,B}(k)=\frac1{\sqrt A}
\sum_a^*a_\xi(a)\chi_a(k)W_1(Na/A)\,T(B;k,a),\qquad
a_\xi(a)=\overline{\alpha(a)}\gamma_2(a)\xi(a).            \tag{1.1}
\]

Here \(a\) is squarefree primary outside a fixed \(S\), \(k\) is squarefree primary outside \(S\), and \(T\) is the original completed theta sum. The weights are fixed smooth compactly supported norm weights, and \(A,B,H\ge1\) are polynomially bounded in a common parameter \(D\). We average over \(H\le Nk<2H\). The literal character \(\chi_a(k)\) already makes \((a,k)>1\) terms zero.

The cube-free face of (1.1) is exactly

\[
\frac1{\sqrt{AB}}
\sum_{a,n}^*a_\xi(an)\chi_{an}(k)
W_1(Na/A)W_2(Nn/B)\mathbf1_{(a,n)=1}.                  \tag{1.2}
\]

It is essential that (1.1), not an uncompleted or arbitrarily weighted two-axis family, is the object estimated below.

We use a uniform bound for the particular negative-divisor sum

\[
\sum_{(g,S\mathfrak d)=1}
\mu(g)\eta(g)\alpha(g)^{-3}\chi_k(g)^3 V(Ng/G)
\ll D^\epsilon G^\beta\|V\|_{C^J},                      \tag{1.3}
\]

with \(Nk,N\mathfrak d,G\) polynomially bounded and \(\eta\) in the fixed finite ray family. Two inputs are available.

- \(\beta=1\): elementary ideal counting proves (1.3), with no canonical moment theorem or zero-free input.
- \(\beta=11/12\): Corollary 6.4 of the companion angular note proves (1.3), conditionally on the explicitly named imported canonical mean-square inputs after the native fixed-angle adapter. This is not an application of a finite-order theorem to an infinite-order character.

Throughout the general component theorem assume \(1/2<\beta\le1\) and (1.3). All allocation blocks use a fixed smooth dyadic partition in \(Ne,Nf,Ng\), including the scalar variable \(g\).

## 2. Translate the primary Gauss-sum normalization exactly

The primary source uses

\[
g_{\rm DR}(t,n)
=\sum_{x\bmod n}\left(\frac{x}{n}\right)_3
\check e(tx/n),\qquad
\check e(z)=\exp(2\pi i(z+\overline z)).
\]

The imported source uses \(e(z)=\check e(z/\lambda)\), where \(\lambda=\sqrt{-3}\). Define, for every squarefree primary \(n\) coprime to \(\lambda\),

\[
\Gamma(n)=\frac1{\sqrt{Nn}}
\sum_{x\bmod n}\left(\frac{x}{n}\right)_3e(x/n).           \tag{2.1}
\]

This uses the cubic symbol, which is defined also at the prime above \(2\). For \((n,S)=1\), it is exactly the previously used \(\gamma_2(n)\). We do not define a sextic residue symbol at the prime above \(2\).

For \(t\in\{1,\lambda^2,\omega\lambda^2,\omega^2\lambda^2\}\), every \(\lambda t\) is a unit modulo \(n\). Rescaling the summation variable gives

\[
\boxed{
\frac{g_{\rm DR}(t,n)}{\sqrt{Nn}}
=\left(\frac{\lambda t}{n}\right)_3^{-1}\Gamma(n).
}                                                       \tag{2.2}
\]

Indeed \(\check e(tx/n)=e(\lambda t x/n)\), and the variable change contributes the inverse cubic character. On \((n,S)=1\), the factor is \(\chi_n(\lambda t)^{-2}\). The supplementary laws make it a fixed ray factor, since \(\lambda t\) is supported on the fixed ramified prime and units.

### Lemma 2.1. Structure of all three source cusp coefficients

For \(\sigma\in\{0,+,-\}\), a fixed theta unit \(u\), and each allowed \(m\ge-4\), the coefficient of the imported conjugate cusp has the form

\[
\boxed{
d_\sigma(u\lambda^mnb^3)
=c_{\sigma,u,m}\,|b|\,\Gamma(n)\rho_{\sigma,u,m}(n)
\,\psi_\sigma(\lambda^4u\lambda^mnb^3),
}                                                       \tag{2.3}
\]

or it is zero. Here \(n,b\) are primary, \(n\) is squarefree, \(\rho_{\sigma,u,m}\) lies in a fixed finite family of cubic supplementary ray factors, \(\psi_\sigma\) is a fixed finite additive character, and

\[
|c_{\sigma,u,m}|\le27\cdot3^{m/6}.                      \tag{2.4}
\]

No restriction \((nb,S)=1\) is imposed.

**Proof.** The primary formulas (5.7), (5.13), and (5.14) all contain \(\overline{g_{\rm DR}(t,n)}\,|b/n|\), with \(t\) in the fixed four-element set above. Their remaining factors depend only on the displayed unit/ramified sector and are powers of \(3\) times roots of unity. Taking the conjugate cusp coefficient converts the conjugated Gauss sum to \(g_{\rm DR}(t,n)\); this conjugation is material and is visible in the HTML equations.

For clarity, the supported sectors and radial magnitudes from those equations are as follows:

| Underlying coefficient | Ramified exponent | Unit sectors | Magnitude before \(|b/n|\) |
|---|---:|---|---:|
| \(\tau\), first three cases | \(m=3r-4,\ r\ge1\) | \(\pm1,\pm\omega,\pm\omega^2\) | \(3^{r/2+2}|g_{\rm DR}(t,n)|\) |
| \(\tau\), fourth case | \(m=3r-3,\ r\ge0\) | \(\pm1\) | \(3^{r/2+5/2}|g_{\rm DR}(1,n)|\) |
| \(\tau_1\) | \(m=-4\) | \(1,\omega,\omega^2\) | \(9|g_{\rm DR}(t,n)|\) |
| \(\tau_2\) | \(m=-4\) | \(-1,-\omega,-\omega^2\) | \(9|g_{\rm DR}(t,n)|\) |

The imported cusp conventions are exactly

\[
t_0(\ell)=\tau(\ell),\quad
t_-(\ell)=\omega^2\tau_1(\omega^2\ell)\breve e(\ell),\quad
t_+(\ell)=\omega\tau_2(\omega\ell)\breve e(\ell),\qquad
d_\sigma(\ell)=\overline{t_\sigma(-\ell)}.
\]

Thus the extra rotations change only the finite unit sectors and fixed root factors. The extra exponential in the nontrivial cusps becomes \(\breve e(\ell)\), a fixed periodic function of \(x=\lambda^4\ell\). Substitution of (2.2) proves (2.3).

For the first and the last two rows of the table, dividing the radial magnitude by \(3^{m/6}\) leaves \(3^{8/3}\); the fourth case of \(\tau\) leaves \(27\). This proves (2.4). The support conditions, ray family, and additive periods are all fixed. The calculation uses the explicit classical coefficient identities, independently of the GRH-conditional assertions elsewhere in the primary paper. \(\square\)

## 3. The fixed bad primes and all cube valuations are retained

The first coupled reflection and the exact local allocation write \(a=efg\), with \(e,f,g\) pairwise coprime squarefree outside \(S\), followed by

\[
n=en',\qquad b=fb',\qquad
(e,n')=1,\quad(f,en')=1.
\]

The negative \(g\)-term has no condition \((g,n'b')=1\). Its exact coefficient is the one in (1.3). The zero row mask remains \(\mathbf1_{(k,ef)=1}\), and the row character is \(\chi_k(gn'b')^3\).

Now split \(n'=n_Sn_0\), where \(n_S\) is the squarefree part supported on \(S\setminus\{\lambda\}\), and \((n_0,S)=1\). There are finitely many choices of \(n_S\). In particular the ramified prime does not occur in this primary squarefree index; its full valuation was already recorded by \(m\).

The cubic CRT law and reciprocity give

\[
\begin{aligned}
\Gamma(en_Sn_0)
={}&\Gamma(n_S)\gamma_2(e)\gamma_2(n_0)
\chi_e(n_S)^4\chi_{n_0}(n_S)^4\chi_{n_0}(e)^4.           \tag{3.1}
\end{aligned}
\]

Every sextic denominator in (3.1) is outside \(S\). The possibly problematic small prime is confined to the fixed cubic Gauss factor \(\Gamma(n_S)\); no sextic character at that prime has been introduced. The symbols involving \(n_S\) are separate bounded factors of \(e\) and \(n_0\). The only moving interaction between them is precisely \(\chi_{n_0}(e)^4\), with its required coprimality zero.

Fix \(u,m,n_S,f,b'\) before applying either sieve. The full cube index \(b'\) is frozen, including all its powers at primes of \(S\). The combined additive phase from (2.3) and the original reflection is a periodic function of

\[
u\lambda^{m+4}n_S f^3(b')^3\,e n_0
\]

modulo a fixed \(S\)-supported ideal. The prefactor here may be a nonunit; nevertheless \(e,n_0\) are units modulo that fixed ideal. The resulting function of \(en_0\) on its finite unit group has a finite character expansion with uniformly bounded coefficients. Each character factors as \(\rho(e)\rho(n_0)\). The character family is independent of \(m,f,b'\); only its bounded Fourier coefficients may vary. This handles arbitrary bad-prime cube valuations without dropping them.

Likewise expand the first reflection's fixed ray restrictions on \(efg,k\) into their fixed finite character family before any scalar estimate. Their \(g\)-dependence is a character \(\eta(g)\) admitted in (1.3). The factor \(\chi_k(n_S(b'))^3\) is a fixed row contraction after these indices have been frozen.

After these exact steps, the arithmetic sum in \(e,g,n_0\) has the same form as the reviewed standard-cusp expression:

\[
\sum_{e,g,n_0}^*
\frac{u_e v_{n_0}}{\sqrt{Nn_0}}\,
\mu(g)\eta(g)\alpha(g)^{-3}
\chi_k(gn_0)^3\chi_{n_0}(e)^4
\mathbf1_{(k,ef)=1}\mathbf1_{(g,ef)=1}.                 \tag{3.2}
\]

The vectors are separate and bounded. They retain \((e,f)=1\), \((n_0,f)=1\), all fixed exclusions, and the finite ray factors. The factor \((e,n_0)=1\) is already the zero of the cubic cross-symbol. The common normalization, up to fixed \(n_S\)-constants, is

\[
\frac{3^{-m/3}}{\sqrt{AFG}\,Nb'},\qquad EFG\asymp A,     \tag{3.3}
\]

and the common squarefree scale is

\[
U\asymp \frac{Y}{3^mNn_S(Nb')^3},\qquad
Y=\frac{H^2EG^2}{BF}.                                  \tag{3.4}
\]

These formulas follow from (2.4), the coefficient denominator \(\sqrt{N\ell}\), and the original Ramanujan amplitude. Fixed \(n_S\) factors introduce only fixed constants.

## 4. The stronger component theorem at every cusp

### Theorem 4.1. Full-cusp quadratic–cubic composition with angular cancellation

Under (1.3), every smooth allocation component of the full coupled reflection satisfies

\[
\boxed{
\sum_{k\sim H}^*|\mathcal C_{E,F,G}(k)|^2
\ll D^\epsilon G^{2\beta-2}
\left[HE+Y+(EY)^{2/3}\right],
\qquad Y=\frac{H^2EG^2}{BF}.
}                                                       \tag{4.1}
\]

All three source cusp sequences, theta units, ramified valuations, fixed bad-prime squarefree parts, and unrestricted cube indices are included.

**Proof.** Separate the common smooth norm kernel before the scalar bound or either sieve. The source's Mellin majorant preserves the factor \((1+3^m U(Nb')^3/Y)^{-L}\), with arbitrarily many polynomial frequency moments. After the fixed choices and finite character expansions in Section 3, apply the exact proof of the companion angular note, Theorem 7.1, to (3.2). We spell out its moving interface.

Expand \(\mathbf1_{(g,e)=1}=\sum_{d\mid g,e}\mu(d)\), set \(g=dg'\), \(e=de'\), and retain squarefreeness and \((g',d)=(e',d)=1\). There is no remaining mask \((g',e')=1\). The \(g'\)-sum is (1.3) at length \(G/Nd\), with exclusion \(df\), independent of the two column indices. It gives \((G/Nd)^\beta D^\epsilon\). The remaining \(e',n_0\) sum is the same quadratic–cubic composition with its surviving row mask \((k,e')=1\). Gauss CRT in (3.1) places every new \(d\)-factor into a separate column vector.

The \(e'\)-normalization and Minkowski over \(O(F)\) choices of \(f\) give the exact squared factor

\[
\frac{F^2}{AFG}\left(\frac G{Nd}\right)^{2\beta}
\frac E{Nd}
\asymp G^{2\beta-2}(Nd)^{-2\beta-1}.
\]

Minkowski over \(d\) is therefore controlled by the convergent sum \(\sum_d(Nd)^{-\beta-1/2}\). The quadratic–cubic sieve gives the bracket \(HE+Y+(EY)^{2/3}\), as in the companion proof.

For each cube dyad, \(\sum_{b'}(Nb')^{-1}\ll1\), regardless of its bad-prime content. The amplitude \(3^{-m/3}\) in (3.3) makes the ramified sum convergent after taking square roots; the effective length in (3.4) supplies still more decay in the long-column terms. The finitely many \(n_S\)-patterns and ray families cost only fixed constants. The remaining norm dyads cost a subpower, and the source's transformed-weight bounds control all tails. This proves (4.1). \(\square\)

## 5. The whole coupled completion after the exact support cutoff

The reunited-divisor cutoff is applied before splitting the positive choices into \(e,f\) and before any truncation of theta indices. It states that every reunited \(h,g\) term vanishes when \((Ng)^2>C_*B\), at every cusp. Insert its smooth cutoff in \(Ng/\sqrt{C_*B}\), equal to one on the permitted range, and then recover the \(e,f,g\) expansion. This operation preserves the full coupled sum (1.1) exactly.

Theorem 4.1 applies to the resulting modified components, whose smooth scalar cutoffs have uniform rescaled derivatives. Their nonempty dyads have

\[
G\ll\min(A,\sqrt B).                                   \tag{5.1}
\]

### Theorem 5.1. A quantitative bound for the full coupled completion

Let \(M_{A,B}=\min(A,\sqrt B)\). Under the scalar input (1.3),

\[
\boxed{
\sum_{k\sim H}^*|\mathcal C_{A,B}(k)|^2
\ll D^\epsilon
\left[
HA+\frac{H^2A}{B}M_{A,B}^{\,2\beta-1}
+\left(\frac{H^2A^2}{B}\right)^{2/3}
\right].
}                                                       \tag{5.2}
\]

At balanced \(A=B=D\), this gives

\[
\boxed{
\sum_{k\sim H}^*|\mathcal C_{D,D}(k)|^2
\ll D^\epsilon
\left[HD+H^2D^{\beta-1/2}+H^{4/3}D^{2/3}\right].
}                                                       \tag{5.3}
\]

**Proof.** Since \(EFG\asymp A\),

\[
Y\asymp\frac{H^2AG}{BF^2},\qquad
EY\asymp\frac{H^2A^2}{BF^3}.
\]

The three terms of (4.1) are

\[
\frac{HA}{FG^{3-2\beta}},\qquad
\frac{H^2A}{BF^2}G^{2\beta-1},\qquad
\left(\frac{H^2A^2}{B}\right)^{2/3}
\frac{G^{2\beta-2}}{F^2}.
\]

Use \(F,G\gg1\), \(1/2<\beta\le1\), and (5.1). Each is bounded by its corresponding term in (5.2). Summing the smooth dyads and fixed ray branches by Minkowski costs only \(D^\epsilon\). No projection onto a single cusp remains. \(\square\)

Two consequences have different dependency strengths.

1. **Elementary scalar input, \(\beta=1\).** Classical theta reflection, the exact cutoff, and the quadratic/cubic upper sieves give

   \[
   \sum_{k\sim H}^*|\mathcal C_{D,D}(k)|^2
   \ll D^\epsilon\left[HD+H^2D^{1/2}+H^{4/3}D^{2/3}\right]
   \ll D^{2+\epsilon}
   \quad(1\le H\le D^{3/4}).
   \]

   This consequence does not use the imported canonical moment induction or an angular zero-free theorem.

2. **Derived angular input, \(\beta=11/12\).** Under the source-conditional angular mean-square adapter and its proved moving-conductor scalar consequence,

   \[
   \sum_{k\sim H}^*|\mathcal C_{D,D}(k)|^2
   \ll D^\epsilon\left[HD+H^2D^{5/12}+H^{4/3}D^{2/3}\right]
   \ll D^{2+\epsilon}
   \quad(1\le H\le D^{19/24}).
   \]

   The exponent \(19/24\) is a bound on the dual-row norm range. It is not a new zero-free boundary.

## 6. Remaining boundary

The standard-cusp restriction has been removed from this coupled estimate using the actual primary coefficient formulas, with their conjugation and additive normalization checked. The result includes every cusp of the first reflection and the full cube completion.

It still averages only squarefree primary rows outside the fixed bad set. The literal short-row fourth moment requires an arbitrary-row and auxiliary family at a much larger dual range, together with completion inversion and signed product-column covariance control. In the initial balanced fourth-moment reduction that dual range is about \(D^{3-\vartheta}\), while the proved bounds above reach \(D^{3/4}\) or \(D^{19/24}\).

Moreover, the paired second reflection has a noncontracting sector: when the negative label is \(g=1\), the remaining positive conductor can retain all primes of \(h=a\), restoring the original axis scale. The exact support cutoff alone supplies no iterative decrease of the adverse row-to-column ratio. A further saving must come from a quantitative centered transformation or a direct signed estimate, not from formally repeating the kernel involution.

No full fourth-moment theorem, generalized \(2k\)-th hierarchy, or RH claim is made.

