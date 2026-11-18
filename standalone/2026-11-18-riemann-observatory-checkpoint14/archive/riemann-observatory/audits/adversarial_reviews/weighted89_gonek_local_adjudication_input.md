# Gonek 1984 | Independent checks of three local issues

This review checks the specific locations raised by the [whole-work advocate](geometry88_gonek_whole_advocate.md) and [whole-work skeptic](prime88_gonek_whole_skeptic.md). I rendered PDF pages 1, 3, 7, 18 and 19 from the pinned 19-page journal scan, SHA-256 \(\texttt{dfdd2444a2f62f1947c897e87101080225714dbf1f21db8ca19096d2a6e80fc3}\). Page numbers below are the printed journal numbers. This is a targeted third review of these findings. [Primary scan](../../sources/classical63_lfunctions/gonek1984.pdf)

## p. 123, contextual equation (2)

The print gives
\[
\int_1^T\zeta^{(\mu)}(1/2+it)\zeta^{(\nu)}(1/2-it)\,dt
\sim \frac{T(\log T)^{\mu+\nu+1}}{\mu+\nu+1}.
\]
The next sentence defines \(\zeta^{(\mu)}(s)\) to be the \(\mu\)-th derivative of \(\zeta(s)\). In particular the second slot is evaluated at \(1/2-it\) after differentiation in the complex argument. There is no factor from differentiating a composition in \(t\) in the displayed notation.

A witness within the source's conventions takes \((\mu,\nu)=(1,0)\) and \(s=1/2+it\). Differentiate \(\zeta(s)=\chi(s)\zeta(1-s)\) and multiply by \(\zeta(1-s)\). Using \(\chi(s)\zeta(1-s)=\zeta(s)\) and conjugation yields
\[
2\Re\bigl(\zeta'(s)\zeta(1-s)\bigr)
=\frac{\chi'}{\chi}(s)|\zeta(s)|^2.
\]
By the gamma formula (8) and Stirling, \(\chi'/\chi(s)=-\log(t/(2\pi))+O(1/t)\). Partial summation of (1), the Hardy–Littlewood continuous second moment, gives
\[
\Re\int_1^T\zeta'(s)\zeta(1-s)\,dt
=-\tfrac12 T(\log T)^2+o(T(\log T)^2).
\]
The imaginary integrand is \(-\tfrac12(d/dt)|\zeta(s)|^2\), whose integral is lower order by the classical strip bound. This supplies the opposite leading sign from the print, unconditionally.

The correction for every fixed pair of nonnegative derivative orders is to multiply the right side of (2) by \((-1)^{\mu+\nu}\). A check from the source's diagonal formula (3) and functional equation works as follows. Let \(C_k(T)=\int_1^T\zeta^{(k)}(s)\zeta(1-s)\,dt\). Integrating the \(t\)-derivative of a product moves one derivative between the slots at a boundary cost \(O(T^{1/2+\eta})\) for any small fixed \(\eta>0\), by fixed-order convexity. Thus the moments of total order \(m\) have the same leading coefficient as \(C_m(T)\), with even \(m\) given by (3). For odd \(m\), insert the \(m\)-times differentiated form of (9) in the second slot. The coefficient of \(\zeta^{(k)}(s)\zeta(1-s)\) is \((-1)^k\binom{m}{k}\chi^{(m-k)}(1-s)/\chi(1-s)\). By fixed-order Stirling this has leading factor \((-1)^m\binom{m}{k}(\log(t/(2\pi)))^{m-k}\). For \(k=m\) the coefficient is exactly \(-1\). For \(k<m\) the Stirling error after integration is \(O(T^{1/2+\eta}(\log T)^m)\) by convexity, and partial summation preserves the lower-order moment coefficient after log weighting. Inductively, if \(C_k(T)\sim(-1)^k T(\log T)^{k+1}/(k+1)\) for \(k<m\), the leading coefficient of \(2C_m(T)\) is
\[
(-1)^m\sum_{k=0}^{m-1}\binom{m}{k}\frac{(-1)^k}{k+1}
=(-1)^m\int_0^1\bigl((1-x)^m-(-x)^m\bigr)\,dx
=-\frac{2}{m+1}.
\]
The discrepancy is in Gonek's introductory display. No inference about the notation or printing of Ingham's original paper follows from this check. Equation (3) uses even total order and (4) already prints the sign.

## p. 129, proof of Lemma 1

The change of variables \(t=r(1+x)\) is printed with \(e^{-ir}\) outside \(I_1\) and then with
\[
f(x)=(1+x)\log(1+x)-(1+x)
\]
in the exponential of \(I_1\). The very next line asserts \(f(z)=z^2/2+\cdots\) and a double zero at \(z=0\). The printed function has \(f(0)=-1\), \(f'(0)=0\), and \(f''(0)=1\). At \(t=r\) the original phase is \(-r\), whereas counting the exterior \(e^{-ir}\) and the printed inner phase at \(x=0\) gives \(e^{-2ir}\). Since the lemma is for all sufficiently large real \(r\) and fixed \(a\), restricting subsequent applications to \(r=2\pi n\) cannot justify the intermediate equality.

Keeping the exterior factor, the inner function is \(F(x)=f(x)+1=(1+x)\log(1+x)-x\). Directly, \(t\log(t/(er))=-r+rF(x)\). On a small fixed neighborhood of zero, use the analytic square-root branch \(u=x\sqrt{2F(x)/x^2}=x+O(x^2)\). The amplitude becomes \(1+O(u)\), and its difference from one contributes \(O(1/r)\) to the rescaled integral by integration by parts. The truncated Fresnel integral contributes \((2\pi/r)^{1/2}e^{i\pi/4}+O(1/r)\). With the exterior factor and Jacobian \((2\pi)^{1/2-a}r^{a+1/2}e^{-ir}\), this gives exactly the printed \((2\pi)^{1-a}r^a e^{-ir+i\pi/4}+O(r^{a-1/2})\). The printed lemma statement survives the correction of its auxiliary definition.

## pp. 125 and 140, Corollary 3

Page 125 defines
\[
\lambda=\limsup_n (\gamma_n-\gamma_{n-1})\frac{\log\gamma_n}{2\pi}
\]
and states \(\lambda\ge 1.9\) under RH. Page 140, §6, prints
\[
\beta>\lambda=\limsup_n \frac{(\gamma_n-\gamma_{n-1})2\pi}{\log\gamma_n}.
\]
The scale in the latter display is reciprocal to the scale in the definition and to the one needed for the windows. The distinction is substantive even as a standalone expression. The classical Riemann–von Mangoldt count with an \(O(\log T)\) error places a zero in every interval of a sufficiently large fixed length at all sufficiently large heights. Hence \(\gamma_n-\gamma_{n-1}=O(1)\), and the p. 140 expression at the printed scale has limsup zero.

With the p. 125 scale restored, §6 says that the sum of the window integrals exceeds the continuous integral over \([1,T]\). The displayed integrals alone do not provide this conclusion by coverage. The first zero is above height 1, and the radii \(\beta/(2L)\) tend to zero for fixed \(\beta\), so a fixed initial subinterval is missed. The same observation applies between fixed distinct ordinates. There is also no general flanking window beyond \(T\) in the displayed sum. This is a gap in a literal full-interval covering justification, independent of the normalization typo. It does not establish that the aggregate integral inequality is false.

For a repair, assume RH and a finite \(\lambda\), with the infinite case immediate. Fix \(\lambda<\beta'<\beta\) and \(0<\epsilon<1/2\). The zero count puts flanking ordinates in \([\epsilon T/2,\epsilon T]\) and \([(1-\epsilon)T,(1-\epsilon/2)T]\) for large \(T\). Between them, \(\log\gamma_n=\log T+O_\epsilon(1)\). The definition of limsup gives \(\gamma_n-\gamma_{n-1}\le \beta' 2\pi/\log\gamma_n\) eventually. This is strictly smaller than \(\beta/L\), twice the radius, for sufficiently large \(T\). Thus the windows included in the sum cover \([\epsilon T,(1-\epsilon)T]\). Multiplicities only add nonnegative interval integrals.

Integrating Corollary 2 over the fixed range \([-\beta/2,\beta/2]\) and converting \(d\alpha=L\,dt\) gives the sum of window integrals as \(F(\beta)T\log T+O_\beta(T)\), where
\[
F(\beta)=\int_{-\beta/2}^{\beta/2}
\left[1-\left(\frac{\sin(\pi x)}{\pi x}\right)^2\right]dx .
\]
The second-moment formula (1) gives continuous mass \((1-2\epsilon)T\log T+o_\epsilon(T\log T)\) in the covered interval. Taking \(T\to\infty\) then \(\epsilon\downarrow0\) proves \(F(\beta)\ge1\) for every \(\beta>\lambda\). Passing to leading coefficients of an inequality yields a weak inequality. Strict monotonicity of \(F\) for \(\beta>0\) can also supply the printed strict form by first applying the weak bound at a smaller \(\beta>\lambda\).

For an independent numerical check, the cosine series yields
\[
F(b)=b\left[1-\sum_{j\ge0}\frac{(-1)^j 2(\pi b)^{2j}}{(2j+2)!(2j+1)}\right].
\]
At \(b=19/10\), I used exact rational interval arithmetic for \(j=0,\ldots,20\) with consecutive decimal endpoints \(3.14159265358979323846264338327950288\) and \(3.14159265358979323846264338327950289\) for \(\pi\). These endpoints follow from truncations with 30 and 31 terms in Machin's arctangent formula. The alternating remainder is bounded by the absolute \(j=21\) term evaluated at the upper endpoint. Monotonicity in this tail follows from the term ratio \((\pi b)^2(2j+1)/[(2j+4)(2j+3)^2]\). The resulting enclosure is \(0.99726619997764485<F(1.9)<0.99726619997764486\). Hence continuity gives \(F(\beta)<1\) for some \(\beta>1.9\), forcing \(\lambda\ge\beta>1.9\). In particular this proves the printed weak bound.

## Effect on the derivative statistic

The contextual sign error and the gap argument are outside the derivation of Corollary 1. The stationary-phase correction preserves the result the subsequent proof uses. In the unconditional main theorem (4), the unshifted \(\mu=\nu=1\) bracket is \(1/3-2/(2!\,4)=1/12\). Under RH the reflected derivative becomes the conjugate, giving \(\sum_{0<\gamma\le T}|\zeta'(1/2+i\gamma)|^2=T(\log T)^4/(24\pi)+O(T(\log T)^3)\), with multiplicities as in the residue calculation. These witnesses concern the pinned printing. This note supplies targeted evidence for adjudication.
