# Independent spectral audit and two additional deductions

Reviewer/author: the `family_escape` agent, separate from `spectral_escape`.
Date: 24 October 2026.

## Review scope

I independently reconstructed the arguments in
`spectral/THETA_JUMP_FORM_AND_RESOLVENT_DELOCALIZATION.md` at SHA-256
`ee3ec380524ba59a153fc8cf99df3cf0f3a47fe15f9484e092e699949707b0f7`.
The review is of that local source version. It is not an external peer review,
a formal verification, or a fresh review of the complete imported PR #1017.

No material gap was found in its weighted-jump identity, the rank-two
hyperbolic decomposition, the broadened approximate null vectors, or the
resolvent delocalization inequality. In particular:

- The symmetric prime atoms contribute exactly one copy of the displayed
  positive jump energy, not two.
- The hyperbolic multiplication term remains negative after the two pole
  constraints; it cannot be discarded.
- The broadening scale \(a/2\) gives a source distance at least \(a/2-1\)
  at the cutoff, hence a residual \(\exp(Ca-ce^a)\).
- The bound \(e^{-2|x\pm\log n|}\le e^{2a}n^{-2}\), for \(|x|\le a\),
  controls every prime power, including those beyond the finite window.
- Coercive minimization has denominator \(\lambda_0(a)-\kappa_a\).
  Replacing it by \(|\kappa_a|\) without a relative-gap assumption would
  be invalid; the note retains the correct denominator.
- Plancherel plus \(F_a(0)=1\) proves the stated failure of local normality.

One extra justification was requested from the author in the neutral-vector
paragraph. The derivative *upper* bound alone does not prove integrability of
\(|\phi^{(k)}|^2/\phi\). The \(n=1\) positive theta term supplies

\[
 \phi(x)\ge c\exp((9/2)|x|-\pi e^{2|x|}),\qquad |x|\ge1.
\]

Combined with the displayed derivative bounds, it gives
\(|\phi^{(k)}(x)|/\phi(x)=O_k(e^{2k|x|})\), so the weighted integrals and
smooth truncations do converge. This is an elementary addition to the proof,
not an additional RH-bearing premise.

The following two lemmas were derived during the independent review and
communicated to the spectral author. Their proofs are recorded here so they
can be incorporated or reviewed separately.

## Lemma A: quantitative variance cost of delocalization

Let \(f\in L^2(\mathbb R)\) have compact support and let its Fourier transform
\(F(z)=\int f(x)e^{-izx}dx\) be even, real on the real axis, normalized by
\(F(0)=1\), and have only real zeros. Then

\[
 V=-F''(0)>0,
 \qquad
 V\ge\frac1{16\pi^2\|f\|_2^4}.
\tag{A.1}
\]

Here \(V=\int x^2f(x)dx\) need not be interpreted as the variance of a
probability measure unless \(f\ge0\). The theorem does not require that
positivity.

**Proof.** Compact support makes \(F\) entire of exponential type. Its
Hadamard factorization, pairing real zeros \(\pm t_j\) with multiplicity,
is

\[
 F(z)=\prod_j(1-z^2/t_j^2),\qquad
 \sum_jt_j^{-2}<\infty.
\]

Evenness removes the possible linear exponential, and the normalization fixes
the constant. There is no quadratic exponential at order at most one. A
zero-free function in this class would be constant, which is impossible for
the Fourier transform of an \(L^2\) function with \(F(0)=1\). Thus
\(V=2\sum_jt_j^{-2}>0\).

For real \(|t|\le V^{-1/2}\), the nonnegative numbers
\(x_j=t^2/t_j^2\) have sum at most \(1/2\). Every finite product obeys
\(\prod(1-x_j)\ge1-\sum x_j\), so passage to the convergent product gives
\(F(t)\ge1/2\). Consequently

\[
 2\pi\|f\|_2^2=\int_{\mathbb R}|F(t)|^2dt
 \ge\int_{-V^{-1/2}}^{V^{-1/2}}\frac14\,dt
 =\frac1{2\sqrt V},
\]

which proves (A.1). \(\square\)

Apply this to the even real-zero resolvents of the spectral note, retaining
that imported real-zero property. With

\[
 R_a=\frac{C|\kappa_a|/a+\varepsilon_a}
            {\lambda_0(a)-\kappa_a},
\]

its bound \(\|f_a\|_2^2\le R_a\) gives

\[
 -F_a''(0)\ge\frac1{16\pi^2R_a^2}.
\tag{A.2}
\]

Thus the explicit safe shifts with \(R_a=O(1/a)\) have second coefficients
growing at least quadratically in \(a\). A proposed exact matching
\(-F_a''(0)=V_\theta=-X''(0)\) would necessarily satisfy

\[
 \lambda_0(a)-\kappa_a
 \le4\pi\sqrt{V_\theta}\,[C|\kappa_a|/a+\varepsilon_a].
\tag{A.3}
\]

This is a sharper necessary selection window, not proof that an admissible
shift attaining the target second coefficient exists. The ratio of resolvent
matrix elements defining that coefficient has no automatic monotonicity.

## Lemma B: positive actual null sources with an added quartet in a chosen strip

Use the actual theta density \(\phi\), normalized Fourier transform \(X\),
and complete source identity \(K_W*\phi=0\) from the spectral note. Fix
\(\eta>0\). For sufficiently small \(\epsilon>0\), set

\[
 \delta=4\eta^2\epsilon(1+\eta^2\epsilon),
\qquad
 \phi_{\epsilon,\eta}
 =\phi+\frac{2\epsilon\phi''+\epsilon^2\phi''''}{1+\delta}.
\tag{B.1}
\]

Then \(\phi_{\epsilon,\eta}\) is an even, strictly positive smooth
probability density with the same super-exponential tail class, and
\(K_W*\phi_{\epsilon,\eta}=0\). Its Fourier transform is

\[
 X_{\epsilon,\eta}(z)=X(z)
      \frac{(1-\epsilon z^2)^2+\delta}{1+\delta}.
\tag{B.2}
\]

The added polynomial has the four zeros

\[
 z=\pm\sqrt{\epsilon^{-1}+\eta^2}\ \pm i\eta,
\tag{B.3}
\]

with independent choices of signs. These give extra nonreal zeros at an
arbitrarily high real coordinate and any prescribed positive imaginary
distance \(\eta\). Its second coefficient is

\[
 -X_{\epsilon,\eta}''(0)
 =-X''(0)+\frac{4\epsilon}{1+\delta}.
\tag{B.4}
\]

**Proof.** The leading theta term gives
\(\phi^{(2j)}(x)/\phi(x)\sim(2\pi e^{2|x|})^{2j}\) for
\(|x|\to\infty\), for each fixed \(j\). Thus \(\phi''\) and
\(\phi''''\) are both nonnegative outside one fixed compact interval.
On that interval \(\phi>0\) and both derivative ratios are bounded below.
Choose \(\epsilon\) small enough that
\(2\epsilon\sup(-\phi''/\phi)_+
+\epsilon^2\sup(-\phi''''/\phi)_+<1\). Formula (B.1) is then strictly
positive everywhere. The total mass is one because the two derivative
integrals vanish. All integrations and differentiations are justified by the
theta tails. Evenness and the tail statement follow directly.

Convolution with the source commutes with these derivatives, so the null
identity follows. Fourier differentiation gives (B.2). Let
\(T=\sqrt{\epsilon^{-1}+\eta^2}\). Then
\(\epsilon(T\pm i\eta)^2=1\pm2i\epsilon T\eta\), and
\(4\epsilon^2T^2\eta^2=\delta\), proving (B.3). Expansion at the origin
gives (B.4). \(\square\)

If all zeros of \(X\) are already known to lie in a strip
\(|\Im z|\le b\), choosing \(0<\eta\le b\) preserves that strip while
adding the quartet. Thus positivity, normalization, exact annihilation by the
*actual* Weil source, and an inherited positive-width strip do not uniquely
identify \(X\). The second coefficient can also be made arbitrarily close
to its target. Exact second-coefficient matching is not asserted by this
example, and the example does not refute a selection theorem that imposes
that additional exact condition.

This is a source-identification obstruction, not a fake zero of the Riemann
xi function and not a zero-free theorem.
