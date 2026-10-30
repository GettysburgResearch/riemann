# Gaussian posterior moments as a factor-removal diagnostic

Status: **exact identities and a constructive diagnostic; no new RH equivalence asserted as a solution.**  
Date: 2026-10-30. This note leaves the hash-reviewed main report unchanged.

The reciprocal density in Sra's construction is a Gaussian variance mixture. The identities below translate the fourth-order factor-removal condition into four conditional moments of one positive variable. They identify which variance control is missing and why self-decomposability by itself does not provide it.

## 1. The exact posterior

Let \(S>0\) be the one-sided reciprocal-xi variable, in the normalization
\[
\mathbb E e^{-sS}=\frac{\xi(1/2)}{\xi(1/2+\sqrt s)},
\qquad X=\sqrt{2S}\,Z,\quad Z\sim N(0,1).
\]
Then
\[
p(x)=\mathbb E\!\left[(4\pi S)^{-1/2}
e^{-x^2/(4S)}\right].
\]
Put \(U=1/(4S)\), let \(\mu\) be its law, and define the posterior
\[
\nu_x(du)=\frac{\sqrt{u/\pi}\,e^{-x^2u}}{p(x)}\,\mu(du),
\qquad m_j(x)=\mathbb E_x[U^j].
\]
For \(x\ne0\), the needed integrals converge under the mixture formula. At \(x=0\) the following identities require the corresponding inverse moments of \(S\); these exist for the actual reciprocal-xi law, whose Laplace transform decreases faster than every exponential in \(\sqrt s\).

Differentiating under the integral gives
\[
\frac{d}{dx}\mathbb E_x[g(U)]
=-2x\,\operatorname{Cov}_x(g(U),U).
\tag{1.1}
\]
Equivalently, with \(z=x^2\),
\[
\frac{dm_j}{dz}=-m_{j+1}+m_jm_1.
\tag{1.2}
\]
Thus the conditional moments follow an explicit differential hierarchy as the spatial parameter varies.

The first derivatives of the mixture are
\[
\begin{aligned}
p'/p&=-2xm_1,\\
p''/p&=4x^2m_2-2m_1,\\
p'''/p&=12xm_2-8x^3m_3,\\
p''''/p&=12m_2-48x^2m_3+16x^4m_4.
\end{aligned}
\tag{1.3}
\]
In particular,
\[
\boxed{-\,(\log p)''(x)=2\mathbb E_xU
-4x^2\operatorname{Var}_x(U).}
\tag{1.4}
\]
Log-concavity therefore requires an **upper** variance bound:
\[
2x^2\operatorname{Var}_x(U)\le\mathbb E_xU.
\tag{1.5}
\]
The ordinary positivity of posterior moment matrices supplies lower bounds such as \(m_2\ge m_1^2\); it does not supply (1.5).

## 2. One factor removal: an explicit four-moment region

For a real zero pair \(\pm a\), put \(h=p-a^{-2}p''\), as in the main report. Define
\[
\begin{aligned}
A&=a^2+2m_1-4x^2m_2,\\
B&=a^2m_1+6m_2-4x^2m_3,\\
C&=-2a^2m_1+(4a^2x^2-12)m_2
+48x^2m_3-16x^4m_4.
\end{aligned}
\]
Then
\[
h=\frac{pA}{a^2},\qquad
h'=-\frac{2xpB}{a^2},\qquad
h''=\frac{pC}{a^2}.
\]
Consequently
\[
\boxed{K_a[p]/p^2=4x^2B^2-AC,\qquad
-\,(\log h)''=\frac{4x^2B^2-AC}{A^2}.}
\tag{2.1}
\]
The exact target is therefore
\[
A>0,\qquad 4x^2B^2\ge AC
\quad\text{for every }x.
\tag{2.2}
\]
This is a concrete conditional-moment region that a source-specific preservation argument would have to maintain. Equations (1.2) allow its boundary to be differentiated, exposing the next moments needed for a differential barrier argument. No invariant-region theorem is claimed here.

At \(x=0\), \(A=a^2+2m_1>0\) and
\(C=-2a^2m_1-12m_2<0\), so \(K_a[p](0)>0\) automatically. Checking only the origin supplies essentially no evidence for the global factor-removal condition.

## 3. Why positivity cannot be propagated by a naive posterior reweighting

Direct differentiation of the Gaussian kernel gives
\[
h(x)=p(x)\,
\mathbb E_x\!\left[1+\frac{2U-4x^2U^2}{a^2}\right].
\tag{3.1}
\]
For every \(x\ne0\), the bracket becomes negative for sufficiently large \(U\). It is not a positive posterior weight, and it depends on \(x\). Treating (3.1) as a new positive Gaussian-mixture representation would silently assume the missing result.

If \(S\) has density \(\theta\), \(\theta(0)=0\), and integration by parts is justified, the genuinely appropriate one-sided factor removal is instead
\[
\theta_a(s)=\theta(s)+a^{-2}\theta'(s).
\tag{3.2}
\]
Indeed its Laplace transform is \((1+u/a^2)\mathbb E e^{-uS}\). The positivity of \(\theta_a\) is an additional assertion. If \(\theta(0)\ne0\), a boundary atom of mass \(\theta(0)/a^2\) must also be included.

This distinction matters for the bounded-buffer theorem in `NEAR_CUTOFF_REMOVAL.md`: that theorem constructs a positive **bilateral** law directly. It does not establish a positive one-sided clock after the same near-cutoff removals, so the posterior identities cannot automatically be iterated through that entire finite ladder.

## 4. Self-decomposability alone fails to control the posterior variance

Take \(S\sim\operatorname{Gamma}(\alpha,b)\), with \(1/2<\alpha<1\). This clock is self-decomposable, since its Lévy numerator is \(\alpha e^{-bs}\). Its Gaussian mixture has density
\[
p_\alpha(x)=
\frac{b^\alpha}{\Gamma(\alpha)\sqrt{4\pi}}
\int_0^\infty s^{\alpha-3/2}
e^{-bs-x^2/(4s)}\,ds.
\]
The saddle at \(s=|x|/(2\sqrt b)\), or the equivalent modified-Bessel integral, gives the differentiated asymptotic
\[
p_\alpha(x)=C_\alpha |x|^{\alpha-1}e^{-\sqrt b|x|}
\bigl(1+O(|x|^{-1})\bigr),
\]
with the expansion differentiable term by term on \(x>0\). Hence
\[
(\log p_\alpha)''(x)=\frac{1-\alpha}{x^2}+O(x^{-3})>0
\]
for all sufficiently large \(x\). The posterior variance bound (1.5) fails, even though the clock is self-decomposable and the mixture has a finite positive density at the origin.

This example is not a counterexample to Sra's result: his proof establishes self-decomposability for a carefully controlled family of **bilateral exponential tilts**, followed by unimodality and a score bound. It does not infer log-concavity of a Gaussian mixture from self-decomposability of its clock alone.

## 5. Concrete next use

The four moments in §2 can be recovered from \(p,p',\ldots,p''''\) by (1.3) away from \(x=0\), or computed directly from inverse-moment integrals of the one-sided clock. A rigorous numerical certificate would need interval enclosures for those quantities and a tail bound; an ordinary finite grid is insufficient.

A productive continuation would derive a source-specific inequality controlling the fourth-order expression \(4x^2B^2-AC\), then prove its preservation under the genuine update (3.2) wherever that update remains positive. The existing finite cutoff theorem supplies examples of successful removals; the exact countermodel in the main report supplies a failure case that any proposed general invariant must exclude. This is a targeted closure problem, not a proof that such an invariant exists.

Source normalization and Gaussian subordination: Sra, author v2, §2 and Proposition 3.3, [primary PDF](https://github.com/suvrit/preprints/blob/main/preprints/riem-xi/v2/riem-xi-v2.pdf), blob `f98e0bd0d2d1353245a482581ffa74580c644996`. The identities above are obtained by the displayed differentiation and integration by parts; no novelty claim is made for Gaussian-mixture posterior calculus.

