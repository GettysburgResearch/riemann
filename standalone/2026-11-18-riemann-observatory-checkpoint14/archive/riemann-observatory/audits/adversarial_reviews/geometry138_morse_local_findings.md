# Lagarias’s Morse paper | Two proposed local findings

I verified two auxiliary claims against the rendered arXiv v6 and publisher journal. Both manifestations contain the same formulas and assertions at issue. The fixed-boundary Morse spectral results and the separately defined \(h=0\) arithmetic function survive these checks. I propose two version-specific local findings for director consideration. This note does not change the paper’s Level 1 reading status or register a canonical finding.

## Controlling primary manifestations

| Manifestation | Pin | Relevant pages and equations |
|---|---|---|
| Jeffrey C. Lagarias, arXiv:0712.3238v6, posted 18 August 2009 | 33 pages. SHA-256 307d253d70abc7d8ef3d24355e9ab7708010bda18c7b9060a4913033c6e224be. [Pinned PDF](../../sources/prefix_skeptic62_spectral/lagarias_morse.pdf) | p. 19: (5.1) and extraction of \(A,B\). p. 20: nonzero-\(h\) display and (5.5). p. 21: (5.6). p. 23: (6.1)–(6.2). |
| *Communications in Number Theory and Physics* 3(2), 323–361 (2009), DOI 10.4310/CNTP.2009.v3.n2.a3 | 510,426 bytes, 40 PDF pages including provider cover. SHA-256 268dff410dae549b457c45375007922e91cc8b9b7e23530814044d42bb54b280. [Pinned publisher PDF](../../sources/geometry120_morse_references/lagarias_morse_journal.pdf) | Printed p. 344 (PDF 22): (5.1) and extraction of \(A,B\). Printed p. 346 (PDF 24): nonzero-\(h\) display and (5.5). Printed p. 347 (PDF 25): (5.6). Printed p. 349 (PDF 27): (6.1)–(6.2). |

I inspected the actual renderings, rather than inferring signs from PDF text extraction. The source receipt records the publication URL, page mapping, and image hashes. [Source receipt](../../sources/geometry120_morse_references/SOURCES.md) · [v6 p. 19](../../sources/geometry120_morse_references/geometry120v6-19.png) · [v6 p. 20](../../sources/geometry120_morse_references/geometry120v6-20.png) · [v6 p. 21](../../sources/geometry120_morse_references/geometry120v6-21.png) · [v6 p. 23](../../sources/geometry120_morse_references/geometry120v6-23.png) · [Journal p. 344](../../sources/geometry120_morse_references/geometry120jnl-22.png) · [Journal p. 346](../../sources/geometry120_morse_references/geometry120jnl-24.png) · [Journal p. 347](../../sources/geometry120_morse_references/geometry120jnl-25.png) · [Journal p. 349](../../sources/geometry120_morse_references/geometry120jnl-27.png)

## Proposed finding 1 — the displayed nonzero-shift family fails (5.1)

**Source claim.** Set \(s=\tfrac12-iz\), \(P(z)=\xi(s+h)\), \(Q(z)=\xi(s-h)\). The display immediately before (5.5) gives, for real \(h\ne0\),
\[
 E_h^{\rm print}=\tfrac12(P+Q)-\frac{i}{2h}(P-Q).
\]
The following prose asserts that these are de Branges structure functions unconditionally for \(|h|\ge\tfrac12\), and under RH for all nonzero \(h\). The test is the strict inequality \(|E(z)|>|E(\bar z)|\) for \(\Im z>0\) in (5.1).

**Exact witness.** For \(F^\#(z)=\overline{F(\bar z)}\), conjugation of \(\xi\) and its functional equation give \(P^\#=Q\) and \(Q^\#=P\). Reflection both exchanges the two terms in \(P-Q\) and conjugates the factor \(-i\), so \((E_h^{\rm print})^\#=E_h^{\rm print}\) identically. The moduli in (5.1) are equal at every \(z\). In particular \(h=\tfrac12,z=i\) gives equality in the source’s unconditional range. Changing the name or sign of \(B\), or multiplying \(E_h\) by a constant of modulus one, preserves this equality.

**Reconstruction and impact.** Taylor expansion gives the locally uniform limit \(\xi(s)-i\xi'(s)\), while (5.5) separately prints \(\xi(s)+\xi'(s)\) and defines the derivative with respect to \(s\). A compatible reconstruction is
\[
 \widetilde E_h=\tfrac12(P+Q)+\frac{P-Q}{2h},
 \qquad
 |\widetilde E_h|^2-|\widetilde E_h^\#|^2
       =\frac{|P|^2-|Q|^2}{h}.
\]
The reconstruction is even in \(h\), tends to the displayed \(E_0\), and for positive \(h\) inherits the strict inequality exactly from the single shifted function \(P=\xi(\tfrac12+h-iz)\). That single-shift result is the one used in the cited differenced-\(L\) paper, Theorem 2.1 proof and §6 Lemma 6.1, (6.6), unconditionally for \(h\ge\tfrac12\) and under RH for positive \(h<\tfrac12\). The finding concerns the formula printed in the Morse paper and its attached assertion. The replacement is a reconstruction, with no author-issued correction established here. It leaves the separately stated \(E_0\) criterion and the original single-shift theorem outside the finding. [Cited differenced-\(L\) primary source](https://arxiv.org/pdf/math/0601653v2) · [v6 p. 20](../../sources/geometry120_morse_references/geometry120v6-20.png) · [Journal p. 346](../../sources/geometry120_morse_references/geometry120jnl-24.png)

## Proposed finding 2 — the explicit quotient has negative imaginary part

**Source claim and notation.** Section 5 writes \(E=A-iB\), where \(A,B\) are real entire, but extracts \(B=(E-E^\#)/(2i)\). That extraction has the opposite sign from the decomposition, which requires \(B=(E^\#-E)/(2i)\). Section 6 defines \(m_E=-B/A\) in (6.1), calls it Herglotz in the immediately stated positive-imaginary convention, and evaluates it explicitly in (6.2). The extraction formula alone is a notation inconsistency. Under a consistent convention \(E=A+iB\), the negative quotient could have the correct sign. That relabeling does not alter the explicit expression in (6.2).

**Invariant witness.** With \(x=e^u>0\) and \(z=i\), equation (6.2) gives the actual number
\[
 -\,i e^{-x}\frac{W_{-1/2,1}(x)}{W_{1/2,1}(x)}.
\]
Here \(iz=-1\) and the second index can be changed to \(1\) by Whittaker evenness. In \(W_{\kappa,1}(x)=e^{-x/2}x^{3/2}U(3/2-\kappa,3,x)\), the two relevant first \(U\)-parameters are \(2\) and \(1\). The positive real integral for \(U(a,3,x)\) gives \(U(1,3,x)=x^{-1}+x^{-2}\) and \(U(2,3,x)=x^{-2}\). Hence the displayed value is exactly \(-ie^{-x}/(1+x)\), or \(-i/(2e)\) at \(u=0\). This is a strictly negative imaginary value at an upper-half-plane point and decides the displayed sign independently of the name assigned to \(B\).

**Reconstruction and impact.** In \(E=A-iB\), reflection gives \(E^\#=A+iB\), and
\[
 |E|^2-|E^\#|^2=4\,\Im(B\bar A).
\]
Under (5.1), \(A\) cannot vanish in the upper half-plane and \(\Im(B/A)>0\). Thus keep the stated decomposition and use \(+B/A\) with the corresponding opposite overall sign in the explicit expression. In (5.6) the actual components are \(A=e^{(x-u)/2}W_{1/2,iz}(x)\) and \(B=z e^{-(x+u)/2}W_{-1/2,iz}(x)\), which give the factor \(e^{-x}\) in their quotient. The nearby standalone display of \(A\) uses a different positive prefactor at fixed \(u\), which does not change its zeros. It should not be used as the normalization for the quotient.

The sign does not invalidate the HB property of the Morse function (5.6). One direct check uses \(Q_+=d/dt+e^t/2\) and \(y(t)=e^{-t/2}W_{1/2,iz}(e^t)\). The factorization \((-d/dt+e^t/2)Q_+\) gives the \(k=-1/2\) expression. Intertwining and the normalized Whittaker asymptotic give \(Q_+y=z^2e^{-t/2}W_{-1/2,iz}(e^t)\), with the factor \(z^2\) fixed by the first inverse-\(e^t\) term. Let \(I=\int_u^\infty|y|^2dt\) and \(D=\int_u^\infty|Q_+y|^2dt\). Green’s identity gives \(z^2 I=D+(Q_+y)(u)\overline{y(u)}\). If \(y(u)=0\), this would force \(z^2\ge0\) real, impossible for \(z\) in the open upper half-plane. The corrected quotient is therefore \(e^{-x}(zI-D/z)/|y(u)|^2\), of strictly positive imaginary part there. The principal Weyl–Titchmarsh quotient in Appendix B uses energy \(E=z^2\) and has its own correct sign, \(\Im(y'/y)=\Im(E)\int|y|^2/|y(u)|^2\) for \(\Im E>0\). Neither sign issue changes that theorem or a Dirichlet eigenvalue. [v6 p. 23](../../sources/geometry120_morse_references/geometry120v6-23.png) · [Journal p. 349](../../sources/geometry120_morse_references/geometry120jnl-27.png)

## Decision boundary

The whole-work advocate covers the scope and reconstruction of the Morse spectral claims. The independent whole-work skeptic derives the shifted-function contradiction and the sign via the first-order system. The separate rendered-conventions review independently checks both manifestations, the fixed point \(z=i\), and the differential identity. The earlier supplemental render note provides the exact versioned images and cited-source comparison. I recommend at most the two findings above, one for the false nonzero-shift HB assertion and one for the explicit Herglotz sign contradiction. The extraction sign and limit mismatch are supporting evidence within those findings, not additional entries. No independent reconstruction of the arithmetic canonical-system transformation or whole-paper Level 3 assessment is implied. [Whole advocate](geometry120_lagarias_morse_whole_advocate.md) · [Whole skeptic](analytic120_lagarias_morse_whole_skeptic.md) · [Independent rendered review](weighted128_morse_conventions_adjudication.md) · [Supplemental rendered conventions](geometry120_lagarias_morse_rendered_conventions.md)
