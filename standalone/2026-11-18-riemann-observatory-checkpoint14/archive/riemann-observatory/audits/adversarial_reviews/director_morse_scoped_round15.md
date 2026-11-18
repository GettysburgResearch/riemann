# Two versioned auxiliary formula repairs in the Morse paper

18 November 2026. The director inspected the actual rendered arXiv v6 formulas and the publisher's printed pp.344, 346 and 349, read the independent whole-work advocate and skeptic and the separate rendered-sign adjudications, and checked the invariant witnesses below. Two local formula assertions are false as printed. The fixed-boundary Morse spectral theorems and the separately defined zero-shift arithmetic criterion are outside these findings. The whole paper remains at Level 1; these are scoped adjudications.

The controlling manifestations of Jeffrey C. Lagarias, *The Schrödinger operator with Morse potential on the right half line*, are arXiv:0712.3238v6 (33 pages, SHA-256 `307d253d70abc7d8ef3d24355e9ab7708010bda18c7b9060a4913033c6e224be`) and *Communications in Number Theory and Physics* 3(2) (2009), 323–361, DOI [10.4310/CNTP.2009.v3.n2.a3](https://doi.org/10.4310/CNTP.2009.v3.n2.a3) (40 PDF pages including cover, SHA-256 `268dff410dae549b457c45375007922e91cc8b9b7e23530814044d42bb54b280`). Both inspected manifestations contain the controlling displays. [Full scoped reconstruction and source receipt](geometry138_morse_local_findings.md).

## The nonzero-shift function is self-reflected

Put \(s=1/2-iz\), \(P(z)=\xi(s+h)\), \(Q(z)=\xi(s-h)\), with real \(h\ne0\). At v6 p.20 and journal p.346, the displayed family is

\[
E_h=(P+Q)/2-i(P-Q)/(2h).
\]

For \(F^\#(z)=\overline{F(\bar z)}\), the functional equation and reality of \(\xi\) give \(P^\#=Q\), \(Q^\#=P\). Conjugating the coefficient \(-i\) as well as exchanging \(P,Q\) gives \(E_h^\#=E_h\). Thus \(|E_h(z)|=|E_h^\#(z)|\) everywhere, contrary to the strict inequality (5.1) required of the structure function. Taking \(h=1/2,z=i\) puts this witness in the source's unconditional assertion. A constant phase or relabeling of real components cannot remove the equality.

The displayed functions tend to \(\xi(s)-i\xi'(s)\). Equation (5.5) separately defines \(E_0=\xi(s)+\xi'(s)\), with derivative in \(s\). A compatible reconstruction replaces the coefficient \(-i\) by \(+1\):

\[
\widetilde E_h=(P+Q)/2+(P-Q)/(2h),\qquad
|\widetilde E_h|^2-|\widetilde E_h^\#|^2=(|P|^2-|Q|^2)/h.
\]

It is even in \(h\), has the displayed zero-shift limit, and inherits the single-shift Hermite–Biehler inequality in the appropriate ranges. The latter single-shift result belongs to the separately cited differenced-L-function paper, not to the false formula tested here. The replacement is our reconstruction; no author-issued correction is asserted. The finding does not challenge the source's separately defined \(E_0\) criterion.

## The explicit quotient has the opposite Herglotz sign

The source uses \(E=A-iB\), but its extraction display gives the opposite sign for \(B\). That inconsistency alone could be repaired by changing conventions. A numerical value of the explicit function is invariant under such relabeling: at v6 p.23 / journal p.349, (6.2) evaluates the function called Herglotz, in the stated positive-imaginary convention, as

\[
-z e^{-x}\frac{W_{-1/2,iz}(x)}{W_{1/2,iz}(x)},\qquad x=e^u>0.
\]

At \(z=i\), Whittaker evenness in its second index and the elementary integral for \(U\) give

\[
U(1,3,x)=x^{-1}+x^{-2},\quad U(2,3,x)=x^{-2},\quad
\frac{W_{-1/2,1}(x)}{W_{1/2,1}(x)}=\frac1{1+x}.
\]

The printed value is \(-ie^{-x}/(1+x)\), and in particular \(-i/(2e)\) at \(u=0\). Its imaginary part is strictly negative at an upper-half-plane point. The denominator is positive, so no pole qualification is involved.

Under the stated decomposition, \(|E|^2-|E^\#|^2=4\Im(B\bar A)\), so the strict Hermite–Biehler condition gives \(\Im(B/A)>0\). Keeping that convention requires the positive quotient. The independent factorization check also verifies this globally for the Morse function: with \(Q_+=d/dt+e^t/2\), subordinate \(y\), \(I=\int_u^\infty|y|^2\), and \(D=\int_u^\infty|Q_+y|^2\), Green's identity gives \(z^2I=D+(Q_+y)(u)\overline{y(u)}\). The corrected quotient is \(e^{-x}(zI-D/z)/|y(u)|^2\), with positive imaginary part for \(\Im z>0\). The Appendix B Weyl function in the energy variable has its separate correct sign; its spectral theorem is unaffected.

The two findings group their supporting notation and limiting inconsistencies rather than multiplying entries for the same repair. Independent evidence: [whole advocate](geometry120_lagarias_morse_whole_advocate.md), [whole skeptic](analytic120_lagarias_morse_whole_skeptic.md), [rendered-conventions review](weighted128_morse_conventions_adjudication.md), and [final scoped comparison](geometry138_morse_local_findings.md). No inference about a full arithmetic canonical-system construction or a proof of RH follows. The next useful task is to carry the corrected normalization consistently through a canonical-system comparison, keeping the spectral parameter \(z\) distinct from the Schrödinger energy \(z^2\).
