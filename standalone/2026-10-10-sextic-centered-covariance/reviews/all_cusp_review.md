# Independent review of the full-cusp Gauss-factorization extension

**Verdict: PASS with the dependency distinction stated in the note.**

The frozen note correctly removes the standard-cusp restriction from the coupled quadratic–cubic estimate. Its coefficient normalization, conjugation, treatment of fixed bad primes, separation of moving masks, and summation over the full theta support are valid. Combining this extension with the independently reviewed reunited-divisor cutoff proves the displayed bound for the complete coupled theta sum over squarefree primary rows.

The \(\beta=1\) consequence uses elementary scalar counting and the named classical theta/coefficient/upper-sieve inputs. The \(\beta=11/12\) consequence additionally depends on the companion source-conditional canonical/angular adapter. This audit does not turn that latter input into an unconditional theorem and does not certify the imported paper's main theorem.

## 1. Byte-bound scope and source inspection

| Reviewed file | Bytes | SHA-256 |
|---|---:|---|
| all_cusp_gauss_factorization.md | 16,992 | b596f3f7c43bb84c699201f3b14c81eae18ae89d3b45e2357bcdccfb9eb3ea1c |

The file was read in full and contains no control bytes except line feeds. It is reviewed against these exact companion snapshots:

| Input | SHA-256 |
|---|---|
| centered_a2_attack.md | bbc139f956731482fcf9e33645bfe2832b7b7471594d9cbc1f21cd08eaf2ac5a |
| reunited_cusp_cutoff.md | 89cd204ae66ef615e7d630bf2c1e5524e134b76e30789dce7796a229e53a4340 |

I independently retrieved the primary text of Dunn–Radziwiłł, [Bias in cubic Gauss sums: Patterson's conjecture, arXiv:2109.07463v3](https://arxiv.org/html/2109.07463v3), dated 14 May 2024. The inspected formulas are the additive and cubic-symbol normalizations (1.4)–(1.7), (2.1)–(2.3), the theta coefficients (5.7)–(5.8), the two other cusp sequences (5.13)–(5.14), and conjugation (5.16). They provide the classical coefficient identities used here. The GRH-dependent prime asymptotic, dispersion result, and lower large-sieve assertions in that paper are not inputs to this extension.

The mixed reflection and its outer scalar retain the PR #915 pin 9959364671f89b86f3992ec5ed5e19f804eb607b and the imported October 5 source pin adc7f1241b42e322a6451854ab7e4b4c146bf78a. The corresponding byte-bound source audit is recorded separately in support_cutoff_independent_review.md.

## 2. Gauss-sum normalization and conjugation: PASS

The primary source uses the trace-real additive character \(\check e\), while the imported source uses \(e(z)=\check e(z/\lambda)\). For the note's normalized cubic Gauss sum \(\Gamma(n)\), changing variables by the unit \(\lambda t\) modulo \(n\) gives

\[
\frac{g_{\rm DR}(t,n)}{\sqrt{Nn}}
=\left(\frac{\lambda t}{n}\right)_3^{-1}\Gamma(n).
\]

The inverse cubic character is the correct orientation. Outside \(S\), \(\Gamma(n)=\gamma_2(n)\), so the factor is \(\chi_n(\lambda t)^{-2}\). The factor \(\lambda\) cannot be omitted from this conversion.

The four possible numerators \(t\) are \(1,\lambda^2,\omega\lambda^2,\omega^2\lambda^2\). Hence their supplementary factors belong to a fixed finite ray family. In particular the apparently varying coefficient has not introduced a growing conductor.

The primary formulas contain \(\overline{g_{\rm DR}(t,n)}\). The imported coefficient is \(d_\sigma(\ell)=\overline{t_\sigma(-\ell)}\), so it contains \(g_{\rm DR}(t,n)\), and therefore \(\Gamma(n)\), after conversion. Using a conjugated Gauss sum in the final coefficient would change the cubic interaction; the note uses the correct orientation.

For the two nontrivial cusp functions, conjugating the coefficient evaluated at \(-\ell\) changes its factor \(\breve e(-\ell)\) back to \(\breve e(\ell)\). This is a fixed periodic character of \(\lambda^4\ell\). The unit rotations in \(t_-\) and \(t_+\) change only the fixed unit sector and root-of-unity factors.

The radial bounds are also correct. In the sector \(m=3r-4\), the ratio of \(3^{r/2+2}\) to \(3^{m/6}\) is \(3^{8/3}\); in the sector \(m=3r-3\), the ratio is \(27\); and at the two \(m=-4\) cusps, the ratio of \(9\) to \(3^{m/6}\) is \(3^{8/3}\). Thus \(27\cdot3^{m/6}|b|\) bounds all sectors.

These checks establish the note's actual coefficient structure

\[
d_\sigma(u\lambda^mnb^3)
=c_{\sigma,u,m}|b|\,\Gamma(n)\rho_{\sigma,u,m}(n)
\psi_\sigma(\lambda^{m+4}u n b^3),
\]

with fixed finite phase data and the stated radial bound. No equality of the three cusp coefficient sequences is being assumed.

## 3. Bad-prime squarefree factors and cubic CRT: PASS

The introduction of \(\Gamma(n)\) through the cubic symbol is necessary and valid: this symbol is defined for squarefree primary \(n\) coprime to \(\lambda\), including a factor above \(2\). The proof does not attempt to define a sextic symbol at that prime.

After \(n=en'\), the split \(n'=n_Sn_0\) has finitely many squarefree \(S\)-parts \(n_S\). Every factor is primary and \(\lambda\)-coprime; all \(\lambda\)-valuation has already been assigned to \(m\).

Normalized cubic Gauss CRT for coprime primary factors gives the product of the two reciprocal cubic symbols. Cubic reciprocity identifies those symbols, so their product is the square of one cubic symbol, equivalently the fourth power of the sextic symbol when its denominator is outside \(S\). Applying this twice yields exactly

\[
\Gamma(en_Sn_0)
=\Gamma(n_S)\gamma_2(e)\gamma_2(n_0)
\chi_e(n_S)^4\chi_{n_0}(n_S)^4\chi_{n_0}(e)^4.
\]

Both sextic denominators \(e,n_0\) lie outside \(S\). The factors involving \(n_S\) are separate bounded coefficients in these two variables. The only moving two-column interaction is \(\chi_{n_0}(e)^4\), and its zero retains \((e,n_0)=1\). The fixed factor \(\Gamma(n_S)\) has only finitely many possibilities and changes the constants, not a moving conductor.

This is the extra arithmetic input needed to extend the standard-cusp composition to the other cusp coefficients and the bad-prime squarefree support.

## 4. Additive phases with nonunit bad parts: PASS

The proof correctly freezes \(u,m,n_S,f,b'\), including the complete cube index \(b'\), before applying either sieve. It never assumes that \(b'\) is a unit at the bad-prime modulus.

For these fixed data, the combined additive phase is a bounded function of \(en_0\) modulo a fixed \(S\)-supported ideal. Its prefactor can be nonunit, but \(e,n_0\) are units. Restricting the function to the finite unit group therefore permits a character expansion

\[
F(en_0)=\sum_\rho a_\rho\,\rho(e)\rho(n_0),
\]

with the number of characters fixed and their normalized coefficients uniformly bounded. This remains true for every frozen value of \(m,f,b'\); no growing modulus is required.

The fixed ray restrictions on \(efg,k\) are expanded before the negative-divisor estimate. Consequently the \(g\)-factor is still a member of the admitted finite family

\[
\mu(g)\eta(g)\alpha(g)^{-3}\chi_k(g)^3.
\]

The factors involving \(n_S,b'\), the theta unit, and the ramified power are fixed row contractions after their labels are frozen. None becomes a hidden moving coefficient jointly in \(g,n_0\).

The arithmetic expression is thus genuinely the same separated expression used in the companion moving-mask proof. The forbidden extra condition \((g,n'b')=1\) has not been inserted.

## 5. Moving divisor mask and full support summation: PASS

The remaining mask \((g,e)=1\) is expanded by inclusion–exclusion before the scalar estimate. With \(g=dg'\), \(e=de'\), the squarefree restrictions retain \((g',d)=(e',d)=1\), while no new mask \((g',e')=1\) survives. The \(g'\)-sum has scale \(G/Nd\), exclusion \(df\), and is independent of both remaining column indices.

After the scalar estimate and the quadratic–cubic composition, the squared normalizing factor is

\[
\frac{F^2}{AFG}(G/Nd)^{2\beta}(E/Nd)
\asymp G^{2\beta-2}(Nd)^{-2\beta-1}.
\]

Taking square roots for Minkowski leaves the summable ideal weight \((Nd)^{-\beta-1/2}\), since \(\beta>1/2\). The row mask \((k,e')=1\) remains the one treated in the previously reviewed two-sieve composition.

The full coefficient normalization introduces \(3^{-m/3}/Nb'\), up to fixed \(n_S\)-constants. Its squarefree length is

\[
U\asymp \frac{Y}{3^mNn_S(Nb')^3}.
\]

For each cube dyad, ideal counting gives \(\sum_{b'}1/Nb'\ll1\), with all bad-prime valuations included. The number of dyads below the transformed scale is logarithmic, and the inherited smooth transformed-weight majorant controls the remaining tails. For \(m\ge0\), the effective squarefree scale decreases with \(m\), while \(\sum_m3^{-m/3}\) converges in the Minkowski norm; the finitely many negative valuations cause only a fixed change of constants. The finite \(n_S\)-sum is harmless.

Thus the use of the same bracket \(HE+Y+(EY)^{2/3}\) is justified for the full support. The proof has not replaced infinitely many cube cases by a finite case split or dropped the reflected bad-prime terms.

It follows that Theorem 4.1 is a valid extension of the companion component estimate:

\[
\sum_{k\sim H}^*|\mathcal C_{E,F,G}(k)|^2
\ll D^\epsilon G^{2\beta-2}
[HE+Y+(EY)^{2/3}].
\]

This use of the earlier composition argument is explicitly conditional on the named upper-sieve inputs and the scalar hypothesis (1.3); no new claim of having proved those imported inequalities is made in this audit.

## 6. Full completed sum and quantitative ranges: PASS

The independent cutoff review established exact vanishing of reunited blocks for \((Ng)^2>C_*B\), at all source cusps. Its smooth cutoff is inserted before the positive \(e/f\) split. That operation preserves the complete sum exactly, so the new all-cusp component theorem applies with

\[
G\ll \min(A,\sqrt B).
\]

Let \(M_{A,B}=\min(A,\sqrt B)\). Substitution of \(EFG\asymp A\) gives the three component terms

\[
\frac{HA}{F G^{3-2\beta}},
\qquad
\frac{H^2A}{BF^2}G^{2\beta-1},
\qquad
\left(\frac{H^2A^2}{B}\right)^{2/3}
\frac{G^{2\beta-2}}{F^2}.
\]

For \(1/2<\beta\le1\), these are respectively bounded by

\[
HA,\qquad
\frac{H^2A}{B}M_{A,B}^{2\beta-1},\qquad
\left(\frac{H^2A^2}{B}\right)^{2/3}.
\]

The finite ray branches and smooth dyadic allocations cost a subpower by Minkowski. This verifies the note's Theorem 5.1 for the whole completed object, without a standard-face projection.

At \(A=B=D\), the bound becomes

\[
D^\epsilon
[HD+H^2D^{\beta-1/2}+H^{4/3}D^{2/3}].
\]

For \(\beta=1\), the target \(D^{2+\epsilon}\) holds for \(H\le D^{3/4}\). For \(\beta=11/12\), it holds for \(H\le D^{19/24}\). These are dual-row norm exponents. They are not zero-free boundaries and are not the initial fourth-moment dual range.

The dependency distinction is substantive. The proof of the component estimate uses the companion angular machinery only through the scalar bound (1.3). Substituting elementary counting with \(\beta=1\) removes that canonical/angular dependency. Substituting the stronger derived value \(11/12\) retains it.

## 7. Scope retained and what has changed

This review supplies the additional coefficient-factorization proof that was explicitly left open in the cutoff review's standard-face limitation. The complete first-reflection cusp spectrum and unrestricted cube completion are now covered by the stated coupled estimate.

The result still concerns the exact completed object \(\mathcal C_{A,B}(k)\), with squarefree primary rows outside \(S\). This audit supplies neither completion inversion for the literal squarefree two-axis polynomial nor the arbitrary-row and auxiliary families needed in the original short-row fourth moment. It also supplies no estimate for the centered sesquilinear expression after the product-column diagonal is removed.

The final observation about the \(g=1\) sector is correct: the support cutoff removes large negative divisors but need not reduce the positive conductor \(h=a\). The note does not claim that repeating the kernel involution gives a contracting iteration.

No new finite computation was used as an analytic certificate in this review. The affirmative verdict rests on the explicit coefficient identities, the elementary normalization/CRT checks above, the finite phase separation, and the previously identified analytic inputs. No unresolved mathematical defect was found in the frozen snapshot.
