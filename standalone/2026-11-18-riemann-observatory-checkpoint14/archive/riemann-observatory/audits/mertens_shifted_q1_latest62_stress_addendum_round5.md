# Boundary and source checks for the classical shifted Möbius candidate

17 November 2026. This is the candidate author's adversarial check. The original proof candidate is preserved, and independent review remains pending. No change to its stated range of fixed \(A>C\) was needed in these checks. [Frozen candidate](../proposals/independent_campaigns/mertens_shifted_q1_latest62_round5.md)

## Source-uniform high region

The primary Balazard–de Roton manuscript on printed p. 6 assumes \(0<\epsilon\le1/2\) and gives Proposition 4(i) uniformly there:
\[
|\zeta(s)/\zeta(s+\epsilon)|^2\ll |s|^\epsilon,\qquad \Re s=1/2.
\]
The bound follows from the RH Hadamard ratios with modulus at most one and the completion gamma factor. Thus its dyadic squared contribution with the classical weight is \(O(T^{-1+\epsilon})\), at most \(O(T^{-1/2})\). For the polynomial contribution, apply Montgomery–Vaughan to the coefficients \(\mu(n)n^{-1/2-\epsilon}\), whose squared sum is \(O(1+\log N)\) uniformly for \(\epsilon>0\). Convexity with any fixed \(0<\eta<1/200\) yields a dyadic squared bound
\[
 O_\eta\big((T+N)(1+\log N)T^{-3/2+2\eta}\big).
\]
Starting at \(T=N^{3/4}\) and summing dyadically gives \(O(N^{-1/9})\), since the term involving \(N\) starts at \(N^{-1/8+(3/2)\eta}(1+\log N)\). This independently verifies the precise high-tail input from Proposition 13. It does not invoke Propositions 3, 10, or 14. The manuscript's printed equation (16) indeed omits the reciprocal superscript, which was checked on the rendered p. 18. The dyadic definition (17) immediately below and the displayed proof use the reciprocal. [Balazard–de Roton v1](https://arxiv.org/pdf/0812.1689v1)

## Shift and height table for the twisted contour

Put \(U=\log x\), \(\phi(U)=\sqrt{U/\log U}\), and \(x_0=e^{\phi(U)}\). The height \(x\) can be adjusted to the half-integer \(\lfloor x\rfloor+1/2\), with a bounded relative effect on all displayed estimates and with the same partial sum. The same estimates apply if the upper range is \(|t|\le2x^{3/4}\); in particular the replacement interval stays well below the terminal connector for large \(x\).

| Contour region | Shift and estimate | Kernel check |
|---|---|---|
| Central panel \(|v|\le x_0\) | \(b(x_0)=B_0/(\phi(U)\log\phi(U))\). Here \(b(x_0)U=O(\phi(U))\). Pointwise (8.1) gives reciprocal cost \(e^{O(\phi(U))}\). Any fixed compact range of \(v\) also follows by local factorization at finitely many zeros. | Integrate \((1/4+(v-t)^2)^{-1/2}\) over the panel to get \(O(1+\log x_0)\) uniformly in \(t\). |
| Ordinary dyadic panels away from \(t\) | \(b(Y)=B_0/(\log Y\log\log Y)\). The value \(b(Y)\log Y=B_0/\log\log Y\) is above the lower edge of Theorem 1.2 (1.4) at \(\varepsilon=1/3\) for \(B_0\ge C_1(1/3)\), and is \(o((\log\log\log Y)^{-c})\) for each fixed \(0<c<1\). The first reciprocal moment on a full panel, or a positive integrand on a subset of it, costs at most \(Y\exp((\log Y)^{1/3})\). | \(|v-t|\gg |v|\asymp Y\) on retained panels, so the kernel cancels the factor \(Y\). Reflected panels use conjugation. |
| Panels below \(16x_0\) with \(|t|<4x_0\) | At their original shifts, (2.8) gives reciprocal cost \(e^{O(\phi(U))}\), since their heights are comparable to \(x_0\). Across any ordinary connector the shifts stay between two comparable values. | Kernel integrated absolutely over finitely many panels. Horizontal kernel bounded by 2. Above \(16x_0\) the ordinary dyadic bound applies. |
| Replacement \([a_1,a_2]\) when \(t\ge4x_0\) | With \(t/4<a_1\le t/2\), \(2t\le a_2<4t\), set \(w=\log t\), \(a=\min(U^{-1/2},w/(U\log w))\). We have \(w\ge\phi(U)+O(1)\), \(w\le U\), \(a\log w=o(1)\), \(\log(1/a)=O(\log w)\). For \(v\) on the replacement, \(\log v=w+O(1)\). | The integral of \(|z-it|^{-1}\) is \(O(1+w)\), absorbed by the stated exponential bound. |
| Replacement connectors | Shifts between \(a\) and \(b(Y)\) obey the same small-shift condition, and \(\log(1/\beta)\le\log w+O(\log\log U)\). For \(a=w/(U\log w)\), this follows from \(U/w^2\le\log U\). For the capped shift and \(b(Y)\), it is immediate from \(w\ge\phi(U)\). Thus (2.8) gives at most \(t^{2/3}\) for large \(U\), while \(x^\beta\le e^{O(\phi(U))+w/\log w}\). | At \(a_1\) and \(a_2\) the distance from \(t\) is \(\gg t\). Length is bounded. |
| Terminal connectors \(v=\pm x\) | At \(b\asymp1/(U\log U)\), the exact small-shift formula gives inverse \(\le e^{U/2+O(U/\log U)}\). At \(\alpha=1/4\), Bui–Florea Lemma 2.2's third case gives inverse \(e^{o(U)}\). Paired-\(\xi\) monotonicity and the Stirling ratio interpolate each of these base bounds to its right. The resulting \(x^{\alpha-1/2}/|\zeta|\) is bounded by \(x^{3/8+o(1)}\) below shift \(1/4\) and \(x^{1/8+o(1)}\) above it. | \(v=\pm x\) remains \(\gg x\) away from \(t\), so the kernel is \(O(1/x)\), including when \(|t|\) reaches \(x^{3/4}\). |

The pointwise source check used the actual published Bui–Florea Lemma 2.2, pp. 8–9. Equation (2.8) applies uniformly along the local panel because \(a\log\log v\to0\) uniformly and its logarithmic error is \(O(\log\log v)\) inside the factor \((\log v)/(\log\log v)^2\). More explicitly, when \(a\log w=o(1)\) and \(\log(1/a)=O(\log w)\), the main logarithm is \(\log(1/a)-\log\log w+O(1)\), and the two errors total \(O(w/\log w)\). Varying \(v\) through the panel changes \(w\) by \(O(1)\). The resulting change in the displayed estimate is absorbed in the \(O(w/\log w)\) allowance. The small-shift estimate is used only for the displayed admissible shifts. [Bui–Florea published PDF](https://pure.manchester.ac.uk/ws/portalfiles/portal/280630528/BuiFlorea_negative_moments.pdf) · [Bui–Florea–Heycock §8.1](https://arxiv.org/pdf/2610.27591v1#page=40)

## Exact optimization check

The local exponent after removing \(t^{1/2}\), including the cost of multiplying by critical-line zeta, is bounded by
\[
aU+\frac{w}{2\log w}\big(\log(1/a)-\log\log w-\log w+O(1)\big).
\]
For the uncapped shift, rewrite it as
\[
\frac{\sqrt U}{2\log w}\,r\log(K/r^2),\qquad r=w/\sqrt U,
\]
with \(K\) an absolute sufficiently large constant. The global maximum of \(r\log(K/r^2)\) over \(r>0\) is \(2\sqrt K/e\), from its derivative \(\log(K/r^2)-2\). Hence the bound is \(O(\sqrt U/\log U)\), including at the lower endpoint \(w\asymp\phi(U)\). For the capped shift, \(w\ge\sqrt U\log w\), so \(\log w\ge\tfrac12\log U+\log\log w\). The bracket is at most \(-2\log\log w+O(1)\), and this eventually offsets the whole \(aU=\sqrt U\). Neither branch needs a numerical approximation.

## A simpler optional low–middle junction

In place of the candidate's \(T_0=\exp(B\phi(L))\), one may take \(T_0=\exp(\sqrt L)\), with \(L=\log N\). It is between 1 and \(N^{3/4}\) for sufficiently large \(N\). For the low branch, RH gives
\[
\sup_{|t|\le T_0}\log^+|\zeta(1/2+it)|=O(\sqrt L/\log L)=o(\phi(L)).
\]
Thus any fixed positive margin \(A-C\) beats this cost at sufficiently large \(N\). The Abel tangent also has \(\epsilon-C\phi'(L)\asymp\epsilon\) for fixed \(A>C\). For the middle branch, the first term of the twisted contour contributes at most \(e^{B_1\phi(L)}\|\zeta/s\|_{2,\,|t|\ge T_0}\). Convexity gives the upper bound \(\exp(B_1\phi(L)-\sqrt L/8)\), which is much smaller than \(e^{-c\phi(L)}\) for every fixed \(B_1\). This proves the constant separation directly. The second twisted term loses only \(O(\sqrt L)\) in the classical norm and uses no \(C_*\). The high bound starts at exactly \(N^{3/4}\) with no gap. Choosing \(A-C\) arbitrarily small affects the threshold \(N_0\) but does not require any replacement of \(A>C\) by \(A>C_*\).

The half-integer Perron error itself is \(O(\log x)\) before recentring. For nearby integers \(n\asymp x\), the absolute truncation error is bounded by a constant times \(\sum_{n\asymp x}1/|n-x|=O(\log x)\). Far integers contribute \(O(\zeta(1+1/\log x))=O(\log x)\). Recentering costs \(O(|t|\log x)\), and the factor from multiply by critical-line zeta is absorbed by \(\sqrt x(1+|t|)^{1/2}\) because \(t\ll x^{3/4}\) and a fixed Lindelöf exponent smaller than \(1/6\) suffices.

No new priority, optimality, or publication claim follows from these checks. The result is pending the two independent reconstructions.
