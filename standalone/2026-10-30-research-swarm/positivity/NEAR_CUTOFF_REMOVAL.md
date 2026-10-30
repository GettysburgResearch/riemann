# Removing reciprocal-xi factors to a bounded distance below the verified height

Status: **source-qualified finite corollary, with a complete analytic proof; independent review requested.**  
Date: 2026-10-30. This supplements the hash-reviewed `report.md` without changing it.

The earlier finite corollary removed factors through one eighth of a verified height. The bilateral Lévy representation permits a substantially sharper finite statement: at the supplied verified height \(3\times10^{12}\), every real-zero factor through \(3\times10^{12}-70\) can be removed while preserving strict log-concavity of the reciprocal density.

This does not verify another zero or improve an all-height zero-free boundary. The mechanism extends Sra's tilted-law argument; no global novelty claim is made. It does not establish a positive **one-sided clock** after these removals. That extra property is unnecessary for the bilateral construction below.

## 1. Inputs and exact claim

Use the notation and source inputs of Sra v2, dated 29 October 2026:

- \(\rho=\tfrac12+\delta_\rho+i\gamma_\rho\), with \(|\delta_\rho|<1/2\), and upper-half-plane zeros counted with multiplicity.
- Every zero with \(0<\gamma\le U\) is on the critical line.
- With \(M(y)=y(\log(y/(2\pi))-1)/(2\pi)\),
  \[
  |N(y)-M(y)|\le\tfrac18\log(y+2)+4.
  \]
- Consequently, for \(U\ge100\),
  \[
  \sum_{\gamma>U}\gamma^{-2}\le\frac{2(\log U+1)}U.
  \]
- The normalized reciprocal density \(p\) has characteristic function
  \[
  \phi(u)=\frac{\xi(1/2)}{\xi(1/2+u)}
  \]
  and bilateral Lévy density \(A(|x|)/|x|\), where
  \[
  A(x)=\sum_{\gamma>0}e^{-\gamma x}\cos(\delta_\rho x),\qquad x>0.
  \]

The last representation is Sra Proposition 3.3; its construction uses the actual zeros, including any unverified off-line zeros. The ordinary theta Fourier kernel is not involved.

For \(V\ge0\), let
\[
P_V(s)=\prod_{0<\gamma\le V}(1-s^2/\gamma^2)
\]
where these zeros are real in the xi coordinate and multiplicities are retained. When \(V\le U\), this is a finite verified product.

**Theorem.** Suppose
\[
10^6\le U\le3\times10^{12},\qquad 0\le V\le U-70.
\]
Then
\[
\phi_V(u)=\phi(u)\prod_{0<\gamma\le V}(1+u^2/\gamma^2)
\]
is the characteristic function of an even probability law with an entire, positive, strictly log-concave density \(p_V\). Its bilateral Laplace transform on its convergence strip is
\[
\int_{\mathbb R}e^{sx}p_V(x)\,dx
=\frac{\Xi(0)P_V(s)}{\Xi(s)}.
\]

Strict log-concavity means strict concavity of \(\log p_V\) in the two-point sense. The proof does not claim that its second derivative is negative at every isolated point.

At the published verified height the allowed deletion reaches
\[
V=2,999,999,999,930.
\]

## 2. A counting interval and two retained zeros

For every \(y\ge10^5\), the counting input gives
\[
\begin{aligned}
N(y+15)-N(y)
&\ge\frac{15}{2\pi}\log\frac y{2\pi}
-\tfrac18\log(y+17)-\tfrac18\log(y+2)-8\\
&>2\log(y/7)-\tfrac14\log(2y)-8\\
&=\tfrac74\log y-2\log7-\tfrac14\log2-8>21/4.
\end{aligned}
\tag{2.1}
\]
Here \(\pi<22/7\), \(y+17\le2y\), \(\log y>10\), \(\log7<2\), and \(\log2<1\) suffice. The logarithmic bounds follow, for example, from \(e<3\), \(e>8/3\), and \(3^{10}<10^5\). In particular every such interval contains a zero.

Put \(B=\max(V,10^5)\). Since \(U\ge10^6\), \(B\le U-70\). Let \(a\) be the smallest ordinate remaining after deletion through \(V\). By (2.1), \(a\le B+15\). Retain another ordinate
\[
\eta\in(B+30,B+45].
\]
Both are verified real ordinates, and
\[
\eta-a>15,\qquad U-\eta\ge25,\qquad a\le U-55.
\tag{2.2}
\]
All statements allow repeated zeros. Only one occurrence of \(a\) will be extracted below.

## 3. Positivity of all required tilted bilateral Lévy numerators

After deleting the factors through \(V\), define
\[
A_V(x)=\sum_{V<\gamma\le U}e^{-\gamma x}
+\sum_{\gamma>U}e^{-\gamma x}\cos(\delta_\rho x).
\]
Also define
\[
B_V(x)=A_V(x)-e^{-ax},
\]
which additionally extracts one Laplace factor at the first remaining ordinate. The retained term at \(\eta\) is present in both.

Fix a tilt \(s\) with \(|s|<a\). We prove that each of
\[
e^{sx}A_V(x),\quad e^{-sx}A_V(x),\quad
e^{sx}B_V(x),\quad e^{-sx}B_V(x)
\]
is strictly positive and strictly decreasing for \(x>0\).

For \(0<x\le\pi\), the high-zero terms and their negative derivatives are nonnegative. Indeed \(\cos(\delta x)\ge0\), \(\delta\sin(\delta x)\ge0\), and the tilted rates \(\gamma\mp s\) are positive. The retained term at \(\eta\) makes both inequalities strict.

For \(x>\pi\), divide the potentially negative tail by the retained term \(e^{-(\eta-s)x}\), treating the other tilt identically. The numerator ratio is at most
\[
\begin{aligned}
E_0
&=\sum_{\gamma>U}e^{-\pi(\gamma-\eta)}\\
&\le U^2e^{-\pi(U-\eta)}
  \sum_{\gamma>U}\gamma^{-2}\\
&\le2U(\log U+1)e^{-\pi(U-\eta)}.
\end{aligned}
\tag{3.1}
\]
The maximum used here is valid because \(y^2e^{-\pi(y-\eta)}\) decreases for \(y\ge U\).

For the negative derivative, use
\[
|\gamma-s-i\delta|\le\gamma+a+\tfrac12<2\gamma,\qquad
\eta-s\ge\eta-a>15.
\]
The relative absolute tail is at most
\[
\begin{aligned}
E_1
&\le\frac2{\eta-a}\sum_{\gamma>U}\gamma
     e^{-\pi(\gamma-\eta)}\\
&\le\frac{2U^3}{\eta-a}e^{-\pi(U-\eta)}
     \sum_{\gamma>U}\gamma^{-2}\\
&\le\frac4{15}U^2(\log U+1)e^{-25\pi}.
\end{aligned}
\tag{3.2}
\]
The analogous monotonicity of \(y^3e^{-\pi(y-\eta)}\) holds because \(U\ge10^6\).

These bounds are uniform in the tilt. At \(U\le3\times10^{12}\), both are less than \(10^{-4}\), with ample room. One exact conservative verification uses
\[
\log U+1<31,\qquad
e^{25\pi}>e^{75}>2^{100}.
\]
The first follows from \(e>8/3\) and \((8/3)^{30}>3\times10^{12}\); the second uses \(\pi>3\) and
\[
e^{3/4}>1+\tfrac34+\frac{(3/4)^2}2+\frac{(3/4)^3}6
=\frac{269}{128}>2.
\]
Thus
\[
E_1<
\frac{(4/15)(3\times10^{12})^2\,31}{2^{100}}
<10^{-4}.
\tag{3.3}
\]
The unsimplified right side of (3.2) is about \(5.55\times10^{-9}\) in ordinary binary64 arithmetic; that numerical value is illustrative, and (3.3) is the proof bound.

All remaining verified terms have positive coefficients and positive tilted rates. This proves the four positivity and monotonicity statements.

## 4. Constructing the probability laws directly

This step is necessary: Sra Theorem C.3 restricts its retained ordinate to at most about \(U/2\), so it cannot simply be cited for the near-\(U\) retained ordinate above.

Because \(B_V(x)>0\), the symmetric density \(B_V(|x|)/|x|\) is a valid Lévy measure. Its small-\(x\) integrability is inherited from \(A\) after removal of finitely many exponential numerators; its large-\(x\) integrability follows from the retained positive rates and absolute convergence of the high-zero tail. Define \(R_V\) by this Lévy measure, retaining the original symmetric Gaussian component (zero for the source's drift-free clock) and using zero symmetric drift. This specifies a centered symmetric infinitely divisible law. By the proved monotonicity it is self-decomposable.

Subtracting a numerator \(e^{-\gamma|x|}\) removes exactly the Lévy exponent of the centered Laplace law \(\operatorname{Lap}(\gamma)\). Hence the characteristic function of \(R_V\) is
\[
\phi(u)\prod_{0<\gamma\le V}(1+u^2/\gamma^2)(1+u^2/a^2).
\]
Consequently
\[
p_V=\ell_a*r_V,\qquad
\ell_a(x)=\frac a2e^{-a|x|},
\tag{4.1}
\]
where \(r_V\) is the density of \(R_V\). This gives \(\phi_V\) and positivity of \(p_V\).

The original \(\phi(u)\) decreases faster than every exponential on the real axis; multiplication by a fixed finite polynomial preserves that property. Fourier inversion therefore gives entire densities for both \(R_V\) and \(p_V\).

For completeness, \(R_V\) has support on the whole real line. Equations (3.1) and the small-\(x\) positivity show
\[
B_V(x)\ge(1-E_0)e^{-\eta x}\quad(x>0),\qquad E_0<1.
\]
It therefore contains an independent difference of two \(\operatorname{Gamma}(1-E_0,\eta)\) variables. That difference has a positive density on all of \(\mathbb R\), so convolution with the remaining probability law preserves positivity. In particular (4.1) gives
\[
|p_V'(x)|<a\,p_V(x)
\quad\text{for every }x\in\mathbb R.
\tag{4.2}
\]

For every \(|s|<a\), the exponential moments of \(p_V\) exist: the Lévy measure has the required exponential integrability at infinity. Tilting multiplies its bilateral Lévy density by \(e^{sx}\). The four inequalities in §3, or the two involving \(A_V\), show that each such tilt is self-decomposable and hence unimodal, by the same classical theorem used in Sra Proposition 3.3.

If \((\log p_V)''(x_0)>0\), choose
\[
s=-p_V'(x_0)/p_V(x_0).
\]
Equation (4.2) gives \(|s|<a\); the tilted density has a strict local minimum at \(x_0\), contradicting unimodality. Thus \(\log p_V\) is concave. Its analyticity excludes any affine interval unless \(p_V\) is a global exponential, impossible for a positive probability density on the whole line. This proves the theorem.

## 5. General retained-gap form and the remaining boundary

The constants 70, 15 and 25 are convenient, not optimal. More generally, if two undeleted verified ordinates satisfy
\[
\eta-a\ge g>0,\qquad U-\eta\ge d>0,\qquad a+\tfrac12\le U,
\]
the same proof works whenever
\[
2U(\log U+1)e^{-\pi d}<1,\qquad
\frac{4U^2(\log U+1)}g e^{-\pi d}<1.
\tag{5.1}
\]
Together with the counting interval of §2, this allows a buffer of order \(\log U\) for general large verified heights \(U\): choose \(g=15\), place the second retained zero within 45 above \(B\), and take
\[
d>\frac1\pi\log\!\left(\frac4{15}U^2(\log U+1)\right).
\]
This explains which exact quantities control the finite extraction, instead of merely reporting a large count of removable factors.

The argument still requires the two retained zeros to lie below a height where **all** zeros have been verified on the line. The residual is not proved to preserve the same property after an arbitrary next removal beyond that boundary. The countermodel in the main report shows why initial strict log-concavity and even very small total variation from a PF-infinity density do not supply that missing induction.

## 6. Reproduction and source scope

Run:
```sh
python swarm/positivity/near_cutoff_check.py
```

The standard-library script checks the exact rational inequalities in (2.1) and (3.3); `near_cutoff_results.json` records the result. It performs no new zero verification and no numerical sampling of the astronomically long finite product.

Primary source: Suvrit Sra, [author repository v2 PDF](https://github.com/suvrit/preprints/blob/main/preprints/riem-xi/v2/riem-xi-v2.pdf), blob `f98e0bd0d2d1353245a482581ffa74580c644996`, especially Proposition 3.3 and Appendix C.2. The exact distinction from C.3's retained-zero restriction is explained in §4.

The pinned Polson–Sokolov sections screened in `REVIEW_HEAT_TRACE.md` do not state this bounded-buffer removal result. That is a limited prior-art comparison, not a claim of global priority. The new content of this note is the explicit bilateral retained-gap criterion and its bounded-buffer specialization, derived from the source's mechanism.

