# Positive Gaussian averages of the actual 5:3 Möbius detector

Status — Proposed all-scale arithmetic positivity theorem with a finite interval checker, and a separate exact asymptotic criterion.

Let \(w(v)=5c_{e^v}(2)+3c_{e^v}(3)\) for \(v\ge0\), extended by zero for \(v<0\). For \(U,\epsilon>0\) set
\[
 g_\epsilon(U)=\int_\mathbb R
   \frac{\exp[-(v-U)^2/(4\epsilon U)]}{\sqrt{4\pi\epsilon U}}w(v)\,dv .
\]
Then **\(g_\epsilon(U)>0\) for every \(U>0\) and every \(\epsilon\ge10^{-6}\)**. The variance in logarithmic coordinates is \(2\epsilon U\). The kernel depends on the center, which changes the relation between the transform and the zeros.

There is also an exact formula for the infimum of parameters giving *eventual* positivity:
\[
 \epsilon_*=\sup_{\rho=\beta+i\gamma}
    \frac{\max(\beta-1/2,0)}{\gamma^2-(\beta-1/2)^2}.
 \tag{1}
\]
The supremum runs over nontrivial zeta zeros. The denominators are positive since \(|\gamma|>14\). The published zero census to height \(3\cdot10^{12}\) gives \(\epsilon_*<5.56\cdot10^{-26}\). Thus even at \(\epsilon=5.56\cdot10^{-26}\) the averages are strictly positive for all sufficiently large centers. RH is equivalent to \(\epsilon_*=0\). The possible positive value below the verified upper bound remains unresolved. [Platt and Trudgian, The Riemann hypothesis is true up to \(3\cdot10^{12}\)](https://arxiv.org/abs/2004.09765)

## Arithmetic data

The physical source and its transform on \(\Re s>1/2\) are
\[
 \begin{split}
 q(n)&=6{\bf1}_{n=1}-6\mu(n)+9{\bf1}_{2\mid n}\mu(n/2)
                         -3{\bf1}_{4\mid n}\mu(n/4),\\
 w(v)&=\sum_{n\le e^v}q(n)n^{-1/2}(v-\log n),\\
 F(s)&=\frac{H(s)}{s^2},\quad H(s)=6+\frac{P(1/2+s)}{\zeta(1/2+s)},\quad
 P(z)=-3(2^{-z}-1)(2^{-z}-2).
 \end{split}
\]
Let \(A=H(0)>6\) and \(B=H'(0)>-1\). On the critical strip \(P\) never vanishes. [Frozen 5:3 row identity](https://github.com/GettysburgResearch/riemann/blob/433fd3662f7b2e4ba384ce64f196380e88624090/claims/lemmas/L-99261-five-three-row-zero-free-mellin-witness.md)

## 1. A finite rectangle determines the large-center sign

Write \(p_\epsilon(s)=s+\epsilon s^2\). The Gaussian Fourier identity and the initial absolutely convergent transform give
\[
 g_\epsilon(U)=\frac1{2\pi i}\int_{1-i\infty}^{1+i\infty}
                       e^{U p_\epsilon(s)}F(s)\,ds .
 \tag{2}
\]
For instance Fourier inversion applies to \(e^{-v}w(v)\), since \(F(1+it)=O((1+t^2)^{-1})\). Its inverse integral can be integrated against the Gaussian by absolute convergence.

Fix \(\epsilon>0\). Choose \(0<b<\min(1,1/(2\epsilon))\) and \(H_0\) sufficiently large that \(1+\epsilon-\epsilon H_0^2<-1\), keeping the lines \(\Re s=-b\) and \(\Im s=\pm H_0\) away from poles in the finite rectangle. The two tails on the initial line contribute \(O(e^{-U})\) by absolute integrability. The finite horizontal segments satisfy the same bound, as \(\sigma+\epsilon\sigma^2\) on \([-b,1]\) is maximized at 1. The bounded left segment contributes \(O(e^{(-b+\epsilon b^2)U})\). The double pole at zero supplies \(AU+B\). The remaining terms are the residues of nontrivial shifted zeros in the rectangle, each an exponential \(e^{U p_\epsilon(s_\rho)}\) times a polynomial in \(U\), where \(s_\rho=\rho-1/2\). Every pole with \(\Re p_\epsilon(s_\rho)\ge0\) is crossed, since
\[
 \Re p_\epsilon(s_\rho)=a+\epsilon(a^2-\gamma^2),\qquad a=\Re\rho-1/2.
\]
In particular such a pole has \(a>0\), and the choice of height includes it.

If \(\epsilon>\epsilon_*\), all nonreal residues in this finite sum decay exponentially, including their polynomial factors. We obtain
\[
 g_\epsilon(U)=AU+B+O_\epsilon(e^{-d_\epsilon U})
\]
for some \(d_\epsilon>0\). If \(0<\epsilon<\epsilon_*\), the largest crossed real exponent \(\lambda\) is positive. Among the poles attaining it select the largest order \(m\). After division by \(e^{\lambda U}U^{m-1}\) the leading sum is a nonzero real trigonometric polynomial with zero mean, up to \(o(1)\). Indeed each leading Laurent coefficient is multiplied by \(p_\epsilon'(s_\rho)^{m-1}/(m-1)!\ne0\). Distinct leading poles have distinct images under \(p_\epsilon\), since equal images for distinct points would force their sum to equal \(-1/\epsilon\), while both have positive real part. Their imaginary frequencies \(\gamma(1+2\epsilon a)\) are nonzero. A finite real trigonometric polynomial of this kind attains both signs bounded away from zero on every sufficiently long interval: its first mean is \(O(1/L)\) and its second mean tends uniformly on intervals of length \(L\) to a strictly positive sum of squared coefficients. Boundedness then gives uniformly positive averages of both one-sided parts. Thus \(g_\epsilon\) has exponentially large values of each sign in every sufficiently long interval of large centers. These two implications give the infimum (1) without deciding the sign at equality.

For the numerical asymptotic upper bound, any off-line zero has \(|\gamma|>3\cdot10^{12}\) by the cited census, while \(a<1/2\). Substitution in (1) gives \(\epsilon_*\le(1/2)/[(3\cdot10^{12})^2-1/4]<5.56\cdot10^{-26}\). This use of the large census is separate from the following all-center certificate, which only requires ordinates through 2000.

## 2. A certificate at \(\epsilon=10^{-6}\) for \(U\ge4\)

Use (2) with the rectangle \(-1\le\Re s\le1\), \(|\Im s|\le2000\). The [checker](check_detector_diffusion_nov18.py) verifies the complete set of 1517 positive ordinates below this height with indexed FLINT enclosures, the exact critical real parts and nonzero derivative enclosures. Together with their conjugates the sum of the absolute residues of \(F\) at these shifted zeros is less than \(0.37\). Their exponential factors have modulus \(e^{-\epsilon\gamma^2 U}\le1\). The checker also encloses \(|F|<1\) on each of 256 closed boxes covering the upper horizontal line. Conjugation covers the lower line.

The right tails satisfy \(|F(1+it)|\le40/(1+t^2)\) by \(|1/\zeta(3/2+it)|\le\zeta(3/2)<3\). After division by \(2\pi\), the total contribution of right tails and both horizontal lines has modulus at most \(2e^{-2U}\), since \(1+\epsilon-\epsilon(2000)^2<-2\).

On the left line the functional equation and the gamma recurrence give the exact modulus
\[
 |\chi(-1/2+it)|=\frac{\sqrt{1/4+t^2}}{2\pi},
 \qquad \zeta(z)=\chi(z)\zeta(1-z).
\]
Thus \(|1/\zeta(-1/2+it)|\le4\pi\zeta(3/2)<38\). Here \(|P(-1/2+it)|\le3(1+\sqrt2)(2+\sqrt2)<25\). We obtain \(|F(-1+it)|\le 956/(1+t^2)\); the left contribution has modulus less than \(500e^{-0.99U}\). The residue from zero is \(AU+B\), and the checker verifies \(A>6,\ B>-1\). Consequently
\[
 g_\epsilon(U)>6U-1-0.37-500e^{-0.99U}-2e^{-2U}>0\quad(U\ge4).
\]

## 3. The native prefix for \(0<U\le4\)

The checker verifies nonnegativity of \(w\) up to \(v=8\). It sieves the exact Möbius coefficients, updates the piecewise-constant derivative and integrates it to every knot through \(\log3000>8\). The source is zero through \(\log2\) and the later knot values are positive; linearity fills the intervals. On \([1,21/20]\) precisely the \(n=2\) term contributes, giving \(w(v)=(15/\sqrt2)(v-\log2)>3\).

For \(v\ge0\), \(|w(v)|\le96e^{v/2}\). To see this, use \(|q(n)|\le24\) and compare the decreasing nonnegative summand \(x^{-1/2}(v-\log x)\) with its integral from 1 to \(e^v\) plus its first value. The resulting bound is \(24(4e^{v/2}-4-v)\le96e^{v/2}\).

Write \(d=4\epsilon U\le16\cdot10^{-6}\) and omit the common positive Gaussian normalizing factor. The contribution from \([1,21/20]\) is at least \((3/20)e^{-9/d}\), since \(|v-U|\le3\) there. The possible negative contribution from \(v\ge8\) is at most
\[
 96 e^4\frac{e^{-16/d}}{8/d-1/2},
\]
using \((v-U)^2\ge16+8(v-8)\). The ratio of this upper bound to the positive term is at most \(640 e^4e^{-7/d}<1\). All remaining contributions up to 8 are nonnegative. This proves the claimed strict sign on the entire small-center range.

## 4. Increasing the variance preserves positivity

For \(s\) real and sufficiently large,
\[
 \widehat g_\epsilon(s)=q_\epsilon'(s)F(q_\epsilon(s)),\qquad
 q_\epsilon(s)=\frac{\sqrt{1+4\epsilon s}-1}{2\epsilon}.
 \tag{3}
\]
Indeed the integral in \(U\) of the Gaussian density times \(e^{-sU}\) is
\(q_\epsilon'(s)e^{-vq_\epsilon(s)}\) for \(v\ge0\), by the elementary Gaussian integral. Fubini holds when \(q_\epsilon(s)>1/2\) by the primitive absolute arithmetic bound.

If \(\eta>\epsilon\), set \(k=\epsilon/\eta\) and \(\phi(s)=k s+(1-k)q_\eta(s)\). Then \(q_\epsilon(\phi(s))=q_\eta(s)\). Differentiation in (3) gives
\[
 \widehat g_\eta(s)=\phi'(s)\int_0^\infty e^{-u\phi(s)}g_\epsilon(u)\,du .
\]
Here \(\phi'(s)=k+(1-k)(1+4\eta s)^{-1/2}\) is the transform of a positive measure with an atom of mass \(k\) at zero. For \(u>0\), \(e^{-u\phi(s)}\) is the Laplace transform of a strictly positive density on \((ku,\infty)\): translate by \(ku\) the inverse Gaussian density
\[
 \frac{z}{\sqrt{4\pi\eta t^3}}\exp[-(t-z)^2/(4\eta t)],\quad
 z=(1-k)u,\quad t>0 .
\]
Its transform is \(e^{-zq_\eta(s)}\) by the same Gaussian integral. Thus the right side is the transform of a positive measure whenever \(g_\epsilon\ge0\). If \(g_\epsilon>0\) for all \(u>0\), the atom already contributes a strictly positive density at every positive time. More explicitly, near each \(U>0\) restrict \(u\) to a small fixed closed subinterval of \((0,U/k)\), where both the inverse Gaussian kernel and \(g_\epsilon\) have uniform positive lower bounds. Uniqueness of Laplace transforms and continuity of \(g_\eta\) give \(g_\eta(U)>0\) for all \(U>0\). Sections 2–3 at \(\epsilon=10^{-6}\) therefore prove the full all-center statement.

## Verification scope

Run the finite checker at the repository root with python-flint 0.9.0.

    python research/explorations/check_detector_diffusion_nov18.py

The 96-bit ball computation returns total signed-ordinate absolute residue sum \(0.366816599536684361093675\) with printed radius \(5.57\cdot10^{-25}\). Coverage uses FLINT's consecutive indexed zero routine from index one through a certified height above 2000. Finite arithmetic and analytic continuation rely on Arb/FLINT; this is a single implementation. Checker SHA-256 is 547621376936ae4cc670ca96928519ad3f36733d9bf07b6006c06bdb68c2163c.

The proof supplies global positivity for the stated averages. As the variance is proportional to \(U\), it does not yield an upper bound for the negative mass of the unsmoothed source or exclude an off-line zero above the verified census.
