# Central-zero scope of the Nakamura–Suzuki Selberg-class criterion

The formula for the drift in arXiv:2307.02027v1 needs the **regular part of the logarithmic derivative at the center** when the central zero has positive multiplicity. The completed function in (2.6) still contains that zero. Removing its factor when computing the drift gives a finite real coefficient, preserves the Gaussian variance \(m_0\), and produces the transform in (2.13) with the full completed function. The zero-location criterion then follows directly from Lévy–Khintchine growth and that transform. [Primary v1 PDF](../../sources/positivity64_operator_probability/suzuki_2307.pdf)

## Exact version and scope

I read all six pages of Takashi Nakamura and Masatoshi Suzuki, *A probabilistic interpretation for central zeros of L-functions in the Selberg class*. I checked the typeset pages 3–5 visually against the extracted text. The arXiv record shows one submission, v1 posted 5 July 2023, and the document footer says version of 6 July 2023. The version-specific and unversioned PDFs retrieved on 18 November 2026 had identical bytes and matched the previously cached primary PDF. Suzuki's publication page lists the work as forthcoming in the *Lithuanian Mathematical Journal*. Searches of the exact title and title with “erratum”, the journal's Online First page and Crossref returned no matching published text or correction. This is a finding about the publicly checked version. [Version and source receipts](../../sources/geometry64_central_zero_scope/receipts.jsonl) · [ArXiv history](https://arxiv.org/abs/2307.02027) · [Author’s publication page](https://sites.google.com/view/msuzuki/home/articles)

On p. 3, (2.6) defines \(\xi_F(s)\) as \(s^{m_F}(s-1)^{m_F}Q^s\prod_j\Gamma(\lambda_j s+\mu_j)F(s)\). Here \(m_F\) is the pole-clearing integer from (S2) on p. 2. There is no divisor at \(s=1/2\) in (2.6). The gamma factors are regular and nonzero there, since their arguments have positive real part. On the same page, (2.7) displays \(B_F=i(\xi'_F/\xi_F)(1/2)\), labels \(m_0\) as the central multiplicity, and separates \(-m_0t^2/2\) from the nonzero-zero sum. Theorems 2.1 and 2.2 allow all \(F\) in the Selberg class. The displayed product at the bottom of p. 4 explicitly retains \(z^{m_0}\), and the first line of p. 5 repeats evaluation at zero. Section 3 then gives cusp-form examples with \(m_0>0\). The literal quotient has a simple pole in that case. [Rendered p. 3](../../sources/geometry64_central_zero_scope/rendered-3.png) · [Rendered p. 4](../../sources/geometry64_central_zero_scope/rendered-4.png) · [Rendered p. 5](../../sources/geometry64_central_zero_scope/rendered-5.png)

## The corrected coefficient and transform

Put \(c=1/2\), \(E(z)=\xi_F(c-iz)\), \(J(s)=(s-c)^{-m_0}\xi_F(s)\), and extend \(J\) holomorphically through \(c\), where \(J(c)\ne0\). The coefficient consistent with the factored product on p. 4 is
\[
B_F^{\rm reg}=i\,\frac{J'(c)}{J(c)}
=i\lim_{s\to c}\left(\frac{\xi_F'(s)}{\xi_F(s)}-\frac{m_0}{s-c}\right).
\]
The sign comes from the linear factor \(e^{-B_F^{\rm reg}z}\) in \(E(z)/z^{m_0}\). Every noncentral genus-one factor has logarithmic derivative zero at \(z=0\), so \(B_F^{\rm reg}=-(E/z^{m_0})'(0)/(E/z^{m_0})(0)\). Equation (2.5) gives \(E(z)=\omega\overline{E(\bar z)}\), and division by \(z^{m_0}\) retains this reflection. Its logarithmic derivative on the real axis near zero is real. Consequently \(B_F^{\rm reg}\) is real, independent of the constant used to normalize the completion. For \(m_0=0\) it recovers the literal quotient in v1. Within a product \(F_1F_2\), the central orders and regular logarithmic derivatives add, which retains the additivity noted after Theorem 2.1. [Primary text, (2.5)–(2.7) and Hadamard factorization on p. 4](../../sources/positivity64_operator_probability/suzuki_2307.pdf)

Use this coefficient in
\[
g_F^{\rm reg}(t)=-\frac{m_0}{2}t^2+iB_F^{\rm reg}t+
  \sum_{\gamma\ne0}m_\gamma\frac{e^{-i\gamma t}-1}{\gamma^2}.
\]
For \(\operatorname{Im}z>1/2\) the strip and inverse-square summability justify absolute termwise integration. Equations (2.11)–(2.12) give
\[
\int_0^\infty g_F^{\rm reg}(t)e^{izt}\,dt
= \frac{i}{z^2}\left(\frac{m_0}{z}-B_F^{\rm reg}+
  \sum_{\gamma\ne0}m_\gamma\left(\frac{1}{z-\gamma}+\frac1\gamma\right)\right)
= \frac{1}{z^2}\frac{\xi_F'}{\xi_F}(c-iz).
\]
The \(im_0/z^3\) contribution is exactly the central pole term from the **full** logarithmic derivative. Taking a regular part in the drift and simultaneously dropping the central pole on the transform side would lose the Gaussian term. The functional equation is used here only for reflection and reality. Choosing the line \(\operatorname{Im}z>1/2\) also dominates the constant part of each summand. [Primary text, (2.11)–(2.13)](../../sources/positivity64_operator_probability/suzuki_2307.pdf)

## Impact on Theorems 2.1 and 2.2

Under GRH the ordinates \(\gamma\) are real and \(\nu_F=\sum_{\gamma\ne0}(m_\gamma/\gamma^2)\delta_{-\gamma}\) is a finite positive measure. The corrected exponent is the Gaussian plus finite-jump Lévy–Khintchine exponent with triplet \((m_0,B_F^{\rm reg},\nu_F)\) in the uncompensated convention of (2.3). The Gaussian variance remains the central order \(m_0\).

For the converse, suppose \(e^{g_F^{\rm reg}}\) is infinitely divisible. The Lévy–Khintchine exponent and \(g_F^{\rm reg}\) are continuous logarithms with value zero at \(t=0\), so their difference is continuous, belongs to \(2\pi i\mathbb Z\), and vanishes. Every such exponent has \(O(1+t^2)\) growth. For \(|x|\le1\), the compensated integrand in (2.1) has absolute value bounded by \((t^2/2+|t|)x^2\), using the quadratic Taylor bound on \(e^{itx}\). For \(|x|>1\) it is bounded by \(2+|t|/2\), and (2.2) gives finite mass on that set. Drift and the Gaussian term obey the same quadratic bound. The integral therefore defines a holomorphic function for \(\operatorname{Im}z>0\). Equality with (2.13) in the smaller half-plane and the meromorphic identity theorem rule out every pole in the upper half-plane. A zero of \(E\) there would give a pole with nonzero residue because \(z^{-2}\ne0\). Reflection rules out the lower half-plane as well. This verifies the reverse implication with the regularized drift without a separate cancellation estimate for the zero sum. The same reasoning applies if the corrected \(g_F\) already satisfies \(|g_F(t)|=O_\epsilon(e^{\epsilon t})\) for each \(\epsilon>0\) as \(t\to+\infty\). The implication from GRH supplies a quadratic bound directly. [Primary text, (2.1)–(2.3), Theorems 2.1–2.2 and (2.13)](../../sources/positivity64_operator_probability/suzuki_2307.pdf)

## Verified examples with a central zero

The paper's own \(f=\Delta E_6\) is a concrete example of a central zero, independently of any numerical claim about other real zeros. It is the normalized Hecke eigenform spanning the one-dimensional cusp space \(S_{18}(\mathrm{SL}_2(\mathbb Z))\). For \(F(s)=L(s+17/2,f)\), the Mellin continuation gives an entire finite-order \(F\), and the normalized Hecke coefficients satisfy \( |a_F(n)|\le d(n)\ll_\epsilon n^\epsilon\) by the unit-modulus local parameters (Deligne). This gives (S1), (S2) and (S4). The completion uses \(\Gamma(s+17/2)\) and \(Q=1/(2\pi)\) up to a nonzero constant, has sign \(i^{18}=-1\), and fulfills (S3). The Euler-log coefficients at \(p^r\) are \((\alpha_p^r+\beta_p^r)/r\) with \(|\alpha_p|=|\beta_p|=1\); this verifies (S5) with \(\theta=0\). Thus \(F\in\mathcal S\) and \(F(1/2)=0\).

In fact this example has \(m_0=1\). Let \(\Lambda_f(u)=(2\pi)^{-u}\Gamma(u)L(u,f)\). Splitting its Mellin integral at \(y=1\) and using \(f(i/y)=-y^{18}f(iy)\) gives
\[
\Lambda_f(9+h)=\int_1^\infty f(iy)\bigl(y^{9+h}-y^{9-h}\bigr)\frac{dy}{y}.
\]
For \(y>1\), \(\Delta(iy)>0\) by its product and \(E_6(iy)>E_6(i)=0\) by its Fourier expansion \(1-504\sum_{n\ge1}\sigma_5(n)e^{-2\pi n y}\), together with the inversion formula at \(i\). Differentiation at \(h=0\) therefore gives a strictly positive integral \(2\int_1^\infty f(iy)y^9\log y\,dy/y\). The central logarithmic derivative has residue one. The sign relation makes \(J(c+h)\) even in \(h\), hence \(B_F^{\rm reg}=0\). [Primary text, §3 p. 5](../../sources/positivity64_operator_probability/suzuki_2307.pdf) · [LMFDB newform 1.18.a.a](https://www.lmfdb.org/ModularForm/GL2/Q/holomorphic/1/18/a/a/)

An elliptic example is \(E/\mathbb Q:y^2+y=x^3-x\), LMFDB 37.a1. Its discriminant is \(37\); the model has good reduction away from \(37\) and multiplicative reduction at \(37\). Modulo \(37\) the unique affine singular point is \((5,18)\), where the tangent cone is \(Y^2-15X^2\). Since \(15^{18}\equiv-1\pmod {37}\), the node is nonsplit. The local root number at \(37\) is \(+1\), all good finite primes have root number \(+1\), and the archimedean root number is \(-1\). The global sign is therefore \(-1\), in agreement with the linked database. Modularity identifies the curve's L-function with that of a weight-two newform, and \(F(s)=L(E,s+1/2)\) is the normalized Selberg-class element. The arguments for (S1), (S2) and (S4) are as above. The gamma argument is \(s+1/2\) and \(Q=\sqrt{37}/(2\pi)\), giving (S3). For (S5), the two normalized good Euler parameters have modulus one by the Hasse bound, and the one at the multiplicative bad prime has modulus \(37^{-1/2}\). Thus the Euler-log coefficients remain uniformly bounded. The sign forces a positive odd central order. Exactly knowing that order for this curve is unnecessary for the quotient test. [LMFDB curve and equation](https://www.lmfdb.org/EllipticCurve/Q/37/a/1) · [LMFDB L-function and sign](https://www.lmfdb.org/L/EllipticCurve/Q/37/a/)

The examples establish the scope issue unconditionally. Their central zeros alone do not settle the relevant GRH hypotheses. For the classical ζ case, \(m_0=0\) and the regularized drift agrees with the existing zero drift, so the original ζ criterion is outside the ambiguity audited here.
