# Lagarias on the Morse potential | Independent rendered convention check

I independently rendered and compared the specific displays in arXiv:0712.3238v6 and the English journal manifestation of Jeffrey C. Lagarias, *The Schrödinger Operator with Morse Potential on the Right Half Line*, *Communications in Number Theory and Physics* 3(2), 323–361 (2009), DOI 10.4310/CNTP.2009.v3.n2.a3. The v6 file has 33 pages and SHA-256 \(\texttt{307d253d70abc7d8ef3d24355e9ab7708010bda18c7b9060a4913033c6e224be}\). The journal PDF used for the comparison has the 39 printed pages plus a provider cover and SHA-256 \(\texttt{268dff410dae549b457c45375007922e91cc8b9b7e23530814044d42bb54b280}\). I inspected v6 pp. 8, 19–21, 23, 26–27 and journal pp. 331, 344–347, 349, 353–354. This is a targeted primary check, not another whole-paper read. [Pinned v6](../../sources/prefix_skeptic62_spectral/lagarias_morse.pdf) · [Journal DOI](https://doi.org/10.4310/CNTP.2009.v3.n2.a3) · [Earlier rendered evidence](geometry120_lagarias_morse_rendered_conventions.md)

## The shifted arithmetic function

On v6 p. 20 and journal p. 346, with \(s=1/2-iz\), \(P(z)=\xi(s+h)\), and \(Q(z)=\xi(s-h)\), the nonzero-\(h\) display is literally
\[
 E_h(z)=\frac{P(z)+Q(z)}2-\frac{i}{2h}(P(z)-Q(z)).
\]
The hypotheses state real \(h\ne0\). Reflection \(F^\#(z)=\overline{F(\bar z)}\), reality of \(\xi\), and its functional equation give \(P^\#=Q\) and \(Q^\#=P\). Since reflection also conjugates \(-i\), \(E_h^\#=E_h\) identically. Thus \(|E_h(z)|=|E_h(\bar z)|\) throughout the plane. Taking \(h=1/2\) and \(z=i\) gives exact equality in a range in which the prose asserts the strict inequality (5.1) unconditionally. A unimodular rotation, a sign change in the notation for \(B\), and interchanging \(E_h\) with \(E_h^\#\) all leave this equality.

Taylor expansion gives the locally uniform limit \(\xi(s)-i\xi'(s)\), whereas (5.5) prints \(\xi(s)+\xi'(s)\) and explicitly differentiates with respect to \(s\). The factor \(-i\) would be the chain-rule factor for differentiation in \(z\), which explains one possible origin of the two conventions. It cannot make both definitions agree as written. For instance \(z=i/2\) gives \(s=1\) and \(\xi'(1)=\frac12(1+\gamma/2-\frac12\log(4\pi))\ne0\).

A locally consistent reconstruction is
\[
 \widetilde E_h=\frac{P+Q}2+\frac{P-Q}{2h},\qquad
 |\widetilde E_h|^2-|\widetilde E_h^\#|^2
   =\frac{|P|^2-|Q|^2}{h}.
\]
It is even in \(h\), has the stated derivative limit, and for \(h>0\) has the strict inequality precisely when the positive shift \(P\) does. The rendered Morse text cites [40]. Its actual result on shifted functions uses the single positive shift \(\xi(1/2+h-iz)\), stated explicitly in Lemma 6.1 and (6.6), unconditional for \(h\ge1/2\) and RH-conditional for all \(h>0\). That cited theorem and the separate \(h=0\) result are distinct from the false equality of conventions above. The reconstruction is not an author-issued correction. [Cited shifted-function paper](https://arxiv.org/pdf/math/0601653v2)

## The two m-functions and the sign of (6.2)

V6 p. 19 and journal p. 344 write \(E=A-iB\), with \(A,B\) real entire, but give \(B=(E-E^\#)/(2i)\), the opposite sign from that decomposition. The compatible expression is \(B=(E^\#-E)/(2i)\). The strict inequality in (5.1) implies
\[
 |E|^2-|E^\#|^2=4\Im(B\overline A)>0 .
\]
Consequently \(A\) does not vanish in the upper half-plane and \(B/A\) has positive imaginary part there. One could read the erroneous extraction formula as changing the convention to \(E=A+iB\). This resolves (6.1) in isolation, since \(-B/A\) would then be the positive-imaginary quotient. It cannot also match the explicit (5.6) and (6.2).

In fact v6 p. 23 and journal p. 349 both render (6.2) with a leading minus sign. Put \(x=e^u>0\) and \(z=i\). The displayed quotient is then
\[
 -i e^{-x}\frac{W_{-1/2,1}(x)}{W_{1/2,1}(x)} .
\]
Both real Whittaker values are strictly positive, by the integral representation of \(U(3/2-\kappa,3,x)\) in \(W_{\kappa,1}(x)=e^{-x/2}x^{3/2}U(3/2-\kappa,3,x)\); its first parameter is 2 or 1. This is an explicit negative-imaginary value independent of any naming choice for \(A,B\). The standalone display for \(A\) below (5.6) in both manifestations also reverses the real exponential prefactor from the real part of (5.6). At fixed \(u\) this changes its value by a nonzero positive factor and leaves the Dirichlet zero set comparison intact. It is not the normalization for computing the quotient.

A direct Green identity verifies the consistent sign without assuming the claimed strict inequality for the Morse example. Let \(q(t)=e^t/2\), \(Q_+=d/dt+q(t)\) and \(y(t)=e^{-t/2}W_{1/2,iz}(e^t)\). Then \(V_{-1/2}=q^2-q'\) and the differential expression factors as \((-d/dt+q)Q_+\). The Whittaker solution \(Q_+y\) solves the partner equation. Its large-\(x\) normalization, or the Whittaker differential recurrence, gives \(Q_+y=z^2 e^{-t/2}W_{-1/2,iz}(e^t)\). Indeed the \(x^{-1}\) coefficient in \(e^{x/2}y\) is \(-z^2\), so \(Q_+y\sim z^2 e^{-x/2}x^{-1}\), fixing the constant of the recessive partner. If \(z\) is in the upper half-plane, \(z^2\) is nonreal or strictly negative. Integration by parts gives
\[
 z^2\int_u^\infty |y|^2\,dt
   =\int_u^\infty |Q_+y|^2\,dt+(Q_+y)(u)\overline{y(u)} .
\]
In particular \(y(u)\ne0\) for such \(z\). Equation (5.6) implies
\[
 \frac{B(z)}{A(z)}
 = e^{-x}\frac{m(u,z^2)+x/2}{z}
 =\frac{e^{-x}}{|y(u)|^2}
    \left(z\int_u^\infty |y|^2\,dt-\frac1z\int_u^\infty |Q_+y|^2\,dt\right).
\]
Its imaginary part is strictly positive because both \(z\) and \(-1/z\) have positive imaginary parts. The printed negative quotient is therefore anti-Herglotz. The separate principal Weyl–Titchmarsh function \(m(u,E)=y'(u,E)/y(u,E)\) of Appendix B satisfies \(|y(u,E)|^2\Im m=\Im E\int_u^\infty |y|^2\,dt\) for \(\Im E>0\), so the Appendix B sign is correct. These two quotients use different spectral variables.

## Translation to the normalized potential

The introductory paragraph of v6 p. 8 and journal p. 331 prints
\[
 v=u-\tfrac12\log(A/4),\qquad k=2B/\sqrt A,\qquad
 u_0=v_0-\tfrac12\log(A/4).
\]
Direct substitution in \(A e^{2v}+Be^v\) gives \(4e^{2u}+(2B/\sqrt A)e^u\), not \(e^{2u}/4+ke^u\). Also the endpoint induced by the printed change would be \(u_0=v_0+\frac12\log(A/4)\). The simple witness \(A=B=1,v_0=0\) gives \(v=u+\log2\), hence coefficient 4 of \(e^{2u}\) and endpoint \(-\log2\), while the asserted coefficient is \(1/4\) and the asserted endpoint is \(+\log2\). There is no accompanying dilation of energy or of the kinetic term in that paragraph. The corrected triple for the stated normalization is
\[
 v=u-\tfrac12\log(4A),\qquad
 k=B/(2\sqrt A),\qquad u_0=v_0+\tfrac12\log(4A).
\]
A translation preserves the derivative and the boundary vector. The general-potential equivalence follows with this triple, and Theorem 2.1 starts directly with the correctly normalized potential.

## The intermediate Whittaker numerator

V6 p. 26 (8.4) and journal p. 354 (B.4) have numerator \(W_{1-k,iz}(x)\), with \(x=e^u\), whereas v6 p. 27 (8.7) and journal (B.7) visibly print \(W_{1-iz,\mu}(x)\). The recurrence immediately before that line raises the **first** Whittaker index and does not swap the roles of \(k\) or \(iz\). Applying it to the recessive solution yields
\[
 -\tfrac12+x\frac{W'_{-k,iz}(x)}{W_{-k,iz}(x)}
   =\tfrac x2+k-\tfrac12-\frac{W_{1-k,iz}(x)}{W_{-k,iz}(x)} .
\]
Thus (8.4)/(B.4) are correct and the intermediate line has the index slip. For an explicit check take \(k=-1/2,z=0\), using the meromorphic extension at this regular point. Then \(W_{1/2,0}(x)=x^{1/2}e^{-x/2}\), giving \(m=-x/2\). The correct numerator ratio is \(x-1\), by the recurrence. The printed intermediate ratio with \(W_{1,0}\) is asymptotic to \(x^{1/2}\) instead, so the printed expression cannot equal the true \(m\) at large \(x\).

**Disposition.** The displays above were verified on both rendered manifestations. The shifted function fails the asserted strict inequality as printed, and the explicit de Branges ratio has the opposite sign from its stated Herglotz convention. The translation and intermediate Whittaker index have direct local repairs. The principal Morse and Whittaker theorems, the Appendix B Herglotz sign, and the separately stated \(h=0\) criterion are not affected by these witnesses. No canonical file was changed. [Whole-work advocate](geometry120_lagarias_morse_whole_advocate.md) · [Whole-work skeptic](analytic120_lagarias_morse_whole_skeptic.md)
