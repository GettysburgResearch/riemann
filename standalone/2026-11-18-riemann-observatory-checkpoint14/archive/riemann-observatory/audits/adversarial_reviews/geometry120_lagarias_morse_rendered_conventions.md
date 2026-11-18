# Rendered check of the de Branges conventions in Lagarias’s Morse paper

This check concerns two literal formulas in §5 and §6. I inspected the actual v6 rendering at printed pp. 19–20 and 23, and the publisher rendering of journal pp. 346 and 349 (publisher PDF pp. 24 and 27, which includes its extra cover). The formulas at issue are the same in both manifestations. The fixed-boundary Morse theorems and the ordinary Weyl–Titchmarsh quotient are separate. [v6 decomposition](../../sources/geometry120_morse_references/geometry120v6-19.png) · [v6 arithmetic family](../../sources/geometry120_morse_references/geometry120v6-20.png) · [v6 quotient](../../sources/geometry120_morse_references/geometry120v6-23.png) · [Journal arithmetic family](../../sources/geometry120_morse_references/geometry120jnl-24.png) · [Journal quotient](../../sources/geometry120_morse_references/geometry120jnl-27.png)

## Literal shifted family fails the strict inequality

Let \(s=1/2-iz,\ P(z)=\xi(s+h),\ Q(z)=\xi(s-h)\), with \(h\) real and nonzero. Both printed manifestations give
\[
 E_h^{\rm print}=(P+Q)/2-i(P-Q)/(2h).
\]
The actual rendered \(i\) is in the numerator. The functional equation and conjugation give \(P^\#=Q\) and \(Q^\#=P\) for \(f^\#(z)=\overline{f(\bar z)}\). Consequently \((E_h^{\rm print})^\#=E_h^{\rm print}\) identically. Equivalently, on the real \(z\)-axis the two summands are real. It follows that \(|E_h^{\rm print}(z)|=|E_h^{\rm print}(\bar z)|\) at every point, contradicting the strict inequality (5.1) at, for example, \(h=1/2,z=i\). This is an unconditional equality counterexample to the stated unconditional subrange. The failure persists for any nonzero \(h\), irrespective of RH. Taylor expansion on compact sets gives \(E_h^{\rm print}\to\xi(s)-i\xi'(s)\), while both versions display \(E_0=\xi(s)+\xi'(s)\) in (5.5).

Lagarias's cited [40], *Zero Spacing Distributions for Differenced L-Functions*, uses the single shifted function \(\xi(1/2+h-iz)\) in the proof of Theorem 2.1 and in the explicit §6 Lemma 6.1, (6.6). Its positive shift is the form needed here. Algebraically, an expression consistent both with that positive-shift modulus inequality and the displayed \(h=0\) limit is
\[
 \widetilde E_h=(P+Q)/2+(P-Q)/(2h),\qquad
 |\widetilde E_h|^2-|\widetilde E_h^\#|^2
     = (|P|^2-|Q|^2)/h .
\]
This algebraic repair is even in \(h\), reduces its HB test to the cited positive-shift test, and tends to \(\xi(s)+\xi'(s)\). It is a reconstruction, with no claim of an author-issued correction. The literal error does not disprove the separately cited \(h=0\) derivative theorem. [Primary cited paper, Lemmas 2.1, 2.2, 6.1 and Theorem 2.1](https://arxiv.org/pdf/math/0601653v2)

## The quotient sign is fixed by the explicit Morse example

Under the actual notation \(E=A-iB\) with real entire \(A,B\), reflection gives \(E^\#=A+iB\). At any point of the upper half-plane the strict inequality excludes a zero of \(A\), and
\[
 |E|^2-|E^\#|^2=4\Im(B\bar A),
 \qquad \Im(B/A)>0 .
\]
Thus the Herglotz quotient in this convention is \(B/A\). The displayed \(B=(E-E^\#)/(2i)\) on v6 p. 19 has the opposite sign from the \(B\) in the decomposition. Interpreting that displayed formula as a redefinition of \(B\) could reconcile (6.1) in isolation, but cannot reconcile the explicit (5.6)–(6.2) pairing.

Indeed both versions of (6.2), evaluated at \(z=i,\ x=e^u>0\), give
\[
 -B(i)/A(i)=-\,i e^{-x}
            \frac{W_{-1/2,1}(x)}{W_{1/2,1}(x)} .
\]
Here \(iz=-1\), changed to \(1\) by evenness of \(W\). Both Whittaker values are strictly positive because \(W_{\kappa,1}(x)=e^{-x/2}x^{3/2}U(3/2-\kappa,3,x)\), and the real Kummer \(U\) integral has positive integrand at parameters \(3/2-\kappa=1,2\). This is a source-specific negative imaginary value at an explicit upper-half-plane point. Hence (6.2), together with the asserted positive-imaginary convention in §6, fixes a genuine local inconsistency rather than an OCR ambiguity. The ordinary \(m=y'/y\) from Appendix B retains the Herglotz sign by Green's identity. [v6 source and exact Morse reconstruction](geometry120_lagarias_morse_whole_advocate.md)
