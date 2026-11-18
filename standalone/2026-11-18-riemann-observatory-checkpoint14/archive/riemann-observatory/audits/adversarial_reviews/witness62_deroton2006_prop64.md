# De Roton 2006, Proposition 6.4 and the boundary jets

I inspected the rendered original BSMF pages 440–441 (PDF pages 24–25) and the preceding definitions and Proposition 6.3. The printed Proposition 6.4 places \((1-w)^{-L}\) outside \((d/dw)^k\) in its small-\(t\) expansion. The last line of the induction on p. 440 repeats this placement after substituting the integrated power \(t^{-w}/(1-w)\). Proposition 6.5 on p. 441 differentiates the entire product \(V_F(s)t^{-s}\). The provisions below concern that specific placement in the published paper. [Primary PDF](https://www.numdam.org/item/10.24033/bsmf.2516.pdf)

The inspected PDF has SHA-256 digest `6b379ceeead2c10e614bd4be268c9672f0b364fa95799a5474a9479a82f9e445`.

## The corrected calculation

Write \(\kappa=(1+1/d)/2\), \(\varphi=U_F\chi\), and \(\Phi(t)=t\varphi'(t)\) with the source notation. On compact subsets of \(0<\Re w<\kappa\), the continuation of \(U_F\psi_{w,k}\) from Proposition 6.3 can be written
\[
 \phi_{w,k}(t)
 =-\partial_w^k\left[t^{-w}\int_t^\infty y^{w-1}\Phi(y)\,dy\right].
\]
Indeed (18) on the initial \(L^2\) range gives an integral of \(v^{-w}(\log(1/v))^k\partial_v\varphi(t/v)\) from 0 to 1. The change \(y=t/v\) gives the expression above. The tails of \(\Phi\) justify continuation and differentiation on compact subsets. Integrating by parts in the ordinary Mellin integral for \(\Phi\) gives \(\int_0^\infty y^{w-1}\Phi(y)\,dy=-U_F(w)\): the boundary terms vanish by the bounds for \(\varphi\) and the chosen open strip. The near-zero remainder can be written
\[
 \partial_w^k\int_0^1 v^{w-1}\Phi(tv)\,dv
 = O(t^{-\varepsilon})
\]
locally uniformly for \(\varepsilon<\Re w<\kappa\), by the small-\(t\) bound on \(\Phi\) and integrability of \(v^{\Re w-\varepsilon-1}|\log v|^k\).

For \(Hf(t)=t^{-1}\int_0^t f(v)\,dv\) and a compact set of \(w\) also satisfying \(\Re w<1\), holomorphic differentiation under this integral is justified by domination by a fixed integrable power times a log polynomial. Therefore \(H^L\partial_w^k[U_F(w)t^{-w}]=\partial_w^k[(1-w)^{-L}U_F(w)t^{-w}]\). The remainder remains \(O(t^{-\varepsilon})\) for \(0<\varepsilon<1\), because \(H(t^{-\varepsilon})=t^{-\varepsilon}/(1-\varepsilon)\). Consequently the correct expansion is
\[
 H^L(\phi_{w,k})(t)
 =\partial_w^k\big[(1-w)^{-L}U_F(w)t^{-w}\big]+O(t^{-\varepsilon}).
\]
These local bounds suffice at every fixed boundary point \(\Re w=1/2\). No uniformity over the entire unbounded vertical strip is required for the proof.

## Witness within the source model

Take \(F=\zeta\), \(w=1/4\), \(k=L=1\), and \(\varepsilon=1/8\). Here \(d=1\), the model is in the original \(L^2\) range, and
\[
 U_\zeta(1/4)=\pi^{1/4}\frac{\Gamma(1/8)}{\Gamma(3/8)}\frac13>0.
\]
The discrepancy between the actual and printed leading terms is
\[
 (1-w)^{-2}U_\zeta(w)t^{-w}\big|_{w=1/4}
 =\frac{16}{9}U_\zeta(1/4)t^{-1/4}.
\]
It cannot be absorbed in \(O(t^{-1/8})\), even with \(w\) fixed. The parenthesized differentiated expression and the induction on p. 440 both confirm that this is not a PDF extraction ambiguity. The printed formula agrees for \(L=0\) or \(k=0\), or if one only keeps the highest logarithmic degree and permits a larger remainder.

## Effect on Proposition 6.5 and the theorem

The Hardy multiplier is \((1-s)^{-1}\), and \(V_F=(1-H)^{2m_F}U_F\). The binomial combination of the corrected formulas yields exactly \(\partial_s^k[V_F(s)t^{-s}]\) in Proposition 6.5 by linearity of differentiation. The formula on p. 441 can thus be retained. The large-\(t\) bound follows by the unchanged Hardy iteration, because the small-\(t\) expressions are locally integrable uniformly for \(w\) in a fixed compact neighborhood of the boundary point. Once \(Q_\lambda\) removes \(0<t<\lambda\), these bounds justify the \(L^2\) limit by domination and prove the required unitarily projected zero jets. The source's §7 works with \(0<\lambda<1\).

For \(t\) between \(\lambda\) and 1, each derivative on \(V_F(s)\) lowers the logarithmic degree by at least one. After the source's scaling \(\log(1/\lambda)^{-k-1/2}\), the leading equal-ordinate Gram block therefore remains the size-\(m_\rho\) Hilbert matrix. Distinct-ordinate oscillatory integrals still tend to zero. The target pairing and orthogonality follow from unitarity and support, so the repaired step preserves the finite-window lower coefficient \(m_\rho^2/|\rho|^2\) and the subsequent lower bound in Theorem 2. This checks the effect of the identified formula on that proof chain. [Full reading and Gram argument](../prefix_formula62_deroton2006_full_reading.md)
