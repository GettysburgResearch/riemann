# The zero envelope of both signs of the third Mertens mean

Assume the zeta zeros have real parts with supremum one. With the notation of the [product-mean argument](zhao-third-mertens-nov18.md), put
\[
 B(v)=e^{-v-\gamma_E}\int_2^{e^v} E_3(x)\,dx,\qquad
 W(u)=\min\{u/2,\inf_{\gamma>0}[(1-\beta)u+2\log\gamma]\}=2F(u/2).
\]
For each fixed \(h>0\), set \(M_\pm(u)=\max_{u\le v\le(1+h)u}(\pm B(v))\). The proposed local law is
\[
                 -\log M_+(u)\sim W(u),\qquad -\log M_-(u)\sim W(u).
\]
In particular both maxima are strictly positive eventually. The second logarithm of height in the envelope comes from integrating the prime error. It is essential to control the nonlinear term on this more precise scale. All limits below concern a fixed zeta function.

## An absolute upper estimate with two powers of the ordinate

Write \(P(t)=\int_2^t(\pi(y)-\operatorname{li}(y))dy\) and \(H(t)=\int_2^t(\vartheta(y)-y)dy\). The once-integrated explicit formula, together with removal of the higher prime powers, gives
\[
 |H(t)|\ll t^{3/2}\log^2(2t)+\sum_{\beta>1/2} t^{1+\beta}/|\rho|^2 .
\]
This uses absolute convergence of the integrated formula for \(\psi\). Partial summation gives
\[
 |P(t)|\ll t+ |H(t)|+t\int_2^t |H(z)|z^{-2}dz .
\]
Indeed the weight for \(\int(\vartheta(z)-z)dz\) before integration by parts is \(1/\log z+(t-z)/(z\log^2 z)\), whose derivative is \(O(t/z^2)\). The choice of additive constant in li contributes \(O(t)\). Each term with \(\beta>1/2\) in the bound for \(H\) survives with an absolute change of constant since \(\int_2^t z^{\beta-1}dz\le2t^\beta\).

By Zhao's partial summation identity (18), or the elementary identity for an integrated prime harmonic sum,
\[
 e^{-v}J_1(e^v)=-\int_{e^v}^\infty (\pi(t)-\operatorname{li}(t))t^{-2}dt+O(e^{-v}).
\]
Integrating once by parts with primitive \(P\) and using the classical zero-free region \((1-\beta)^{-1}\ll\log(2+|\gamma|)\) gives
\[
 |e^{-v}J_1(e^v)|\ll (1+v)^2e^{-v/2}
      +\sum_{\beta>1/2}\frac{\log(2+|\gamma|)}{|\gamma|^2}e^{-(1-\beta)v}.
\]
In particular for every \(\epsilon>0\) this is \(\ll_\epsilon\exp(-(1-\epsilon)W(v))\). For real parts below a fixed \(b_0<1\) this follows from \(W(v)=o(v)\). For the remaining zeros use the definition of \(W\) and retain the summable weight \(\log(2+|\gamma|)|\gamma|^{-2\epsilon}\), taking \(b_0\) close enough to 1 in Ingham's density theorem. The quadratic estimate (4) of the product-mean argument and \(W(v)\le2F(v)\) give the same upper estimate for \(|B(v)|\). Since \(W\) increases, this proves the lower bound 1 on the limiting inferior of either logarithmic ratio whenever the maxima are positive.

## A strict separation from the nonlinear error

Fix \(0<\eta<\min(h/4,1/10)\). Let \(w=(1+2\eta)u\), and select a minimizing zero for \(W(w)=d w+2b\), where \(d=1-\beta\) and \(b=\log\gamma\). The dummy line is eventually inactive. We have \(b=o(u)\), \(d=o(1)\), and \(du\gg u^{1/4}\) by the Vinogradov–Korobov zero-free region, since \(b\le u\). The same lower bound applies to the horizontal cost \(d_1u\) of any minimizer of \(F(u)\). Concavity, or simply evaluating the minimizing line for \(F(u)\) at \(w/2\), gives
\[
  2F(u)-W(w)\ge d_1(2u-w)\gg u^{1/4}.
\]

Apply the adaptive Gaussian lower estimate to the selected zero in a strict interior subinterval of \([(1+\eta/4)u,(1+\eta)u]\). On that subinterval the modulated source costs at most \((1+\eta)du+o_\eta(du)\). Twice integrating by parts costs \(2b+O_\eta(\log u)\). Transferring the unsigned mass to an ordinary narrow Gaussian gives a point of either sign. The resulting normalized linear values exceed \(\exp(-W(w))\) in absolute magnitude, by an exponential factor \(\exp(\eta du/2)\) for large \(u\).

On the same interval the delayed upper estimate gives \(e^{-v}J_2(e^v)\ll_\eta (1+u)^C e^{-2F(u)}\). For clarity, in the explicit formula at \(z=e^t\), \(t\ge(1+\eta/8)u\), split at height \(\exp(4F(u))\). Above this split use summability of \(|\gamma|^{-1/2}\) for the fixed rightmost strip and the pointwise factor \(|\gamma|^{-1/2}\le e^{-2F(u)}\). Below it group the defects in bins \([j/u,(j+1)/u]\). Each term costs at most \(e^{-F(u)-j(t/u-1)}\). Ingham bounds the number in a bin by \((1+u)^C\exp(C(j+1)F(u)/u)\), summable against the extra saving for large \(u\). Zeros outside the rightmost strip cost \(O(e^{-ct}(1+t)^2)\). For the tail integral in prime partial summation one can use the delayed bound up to \(t=u^4\), and the global bound \(\exp(-c\sqrt t)\) thereafter. Polynomial factors in \(u\) are harmless. Integrating the square up to \(e^v\) costs at most the displayed polynomial times \(e^v\), with the early part \(t<(1+\eta/8)u\) exponentially smaller after normalization. This proves the delayed estimate without any quantitative regularity of the minimizing defect.

It follows that the quadratic correction and the finite-product tail \(O(v e^{-v})\) are negligible compared with either signed linear excursion. Hence \(M_\pm(u)\ge\exp(-W((1+2\eta)u))\) eventually. Positivity and concavity give \(W((1+2\eta)u)\le(1+2\eta)W(u)\). Sending the fixed \(\eta\) to zero gives the other half of the asserted equivalence.

The adaptive lower estimate used here is proved in the [companion on uniform windows](zhao-shrinking-windows-nov18.md). The exact envelope needs its version for an arbitrary selected zero with \(b=o(u),\ d=o(1),\ du\gg u^{1/4}\). A bound proved only for a minimizer of \(F(u)\) would not suffice.
