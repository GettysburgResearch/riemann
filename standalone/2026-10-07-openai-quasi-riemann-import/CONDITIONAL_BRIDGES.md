# Conditional bridges from an all-height zero-free strip

Status: elementary conditional deductions and an open research target.
The upstream \(7/8\) and \(11/12\) statements are **not accepted as hypotheses known to hold** by this file. Every deduction below is an implication if the relevant upstream result and its analytic interface survive review.
No new zero-free region or RH proof is claimed.

## 1. Source definitions and analytic input

Write
\[
M(x)=\sum_{n\le x}\mu(n),\qquad
m(x)=\sum_{n\le x}\frac{\mu(n)}n,
\]
\[
E_X=\sum_{k\le X}\frac{M(k)^2}{k(k+1)},\qquad
F_X=\sum_{k\le X}m(k)^2.
\]
These are the actual native energies in [NRC32](https://github.com/GettysburgResearch/riemann/blob/0f82df3bf1d0bc669a1bbca09f8404b77c6fecde/standalone/2026-09-21-native-covariance-compression/PROOF.md) and [root-cell covariance](https://github.com/GettysburgResearch/riemann/blob/72ad9bc0fecf52769d62942a8ad307efe46847ce/standalone/2026-09-21-root-cell-covariance/PROOF.md).

Let \(1/2<\alpha<1\). The input interface is:

1. \(\zeta(s)\ne0\) for \(\Re s>\alpha\).
2. The standard growth/contour consequences have been justified on every fixed inner line; equivalently, for use in this note, take the explicit summation input
   \[
   M(x)=O_\epsilon(x^{\alpha+\epsilon})\quad(\epsilon>0).
   \]

For the actual Riemann zeta function, this is a standard analytic consequence, not an additional RH-strength conjecture. The second item is not a numerical consequence of checking zeros. In the classical zeta setting it is the usual reciprocal-zeta and Perron/Littlewood bridge from an all-height zero-free half-plane. It must be supplied with the infinite-height growth hypotheses if one derives it directly from item 1. Keeping the explicit summation interface avoids quietly assuming uniform conductor or height estimates for a changing L-function family.

For each fixed Dirichlet character, an analogous analysis can be attempted with \(\mu(n)\chi(n)\), but constants uniform in a growing modulus are an additional requirement. The words “all Dirichlet L-functions” do not, alone, specify those quantitative constants.

## 2. Energy exponents

Choose a small positive \(\epsilon\) with \(\alpha+\epsilon<1\). Partial summation and the standard identity \(\sum_{n\ge1}\mu(n)/n=0\) give
\[
m(x)=\frac{M(x)}x-\int_x^\infty\frac{M(t)}{t^2}\,dt
=O_\epsilon(x^{\alpha-1+\epsilon}).
\]
Under the summatory input, convergence of the integral is immediate; the zero value is also obtained by taking the limit of \(1/\zeta(s)\) as real \(s\downarrow1\), using convergence of the inverse Dirichlet series to the right of \(\alpha+\epsilon\). Thus the normalization is not an unspecified constant.

It follows by summing powers that
\[
E_X=O_\epsilon(X^{2\alpha-1+\epsilon}),\qquad
F_X=O_\epsilon(X^{2\alpha-1+\epsilon}).
\]
Here and below the small losses are renamed \(\epsilon\), after taking a smaller loss in each input.

| Conditional strip | Conditional \(M(x)\) scale | Conditional \(m(x)\) scale | Conditional native-energy exponent |
|---|---|---|---|
| \(\Re s>7/8\) | \(x^{7/8+\epsilon}\) | \(x^{-1/8+\epsilon}\) | \(E_X,F_X\ll_\epsilon X^{3/4+\epsilon}\) |
| \(\Re s>11/12\) | \(x^{11/12+\epsilon}\) | \(x^{-1/12+\epsilon}\) | \(E_X,F_X\ll_\epsilon X^{5/6+\epsilon}\) |
| RH endpoint, expressed with arbitrary loss | \(x^{1/2+\epsilon}\) | \(x^{-1/2+\epsilon}\) | \(E_X,F_X\ll_\epsilon X^\epsilon\) |

The fixed strip would supply a real power saving compared with the crude \(F_X\ll X\). It would not give the RH endpoint or a percentage of a proof.

## 3. The current full MHB32 estimate does not improve the seed

[MHB32, Section 6](https://github.com/GettysburgResearch/riemann/blob/8c506696d8ad7772ccaf48fbb8678fcd889e8beb/standalone/2026-09-21-mellin-hankel-bandwidth/PROOF.md) proves, for its actual complete native block \([X,M]\), \(X\le M<2X\), and \(y=\lfloor\sqrt M\rfloor\),
\[
\sum_{k=X}^{M}m(k)^2
\le C(1+\log X)^9 X^{191/273}(1+F_y)^{164/273}.
\]
This combines its microscopic band with the paid complement. It cannot be read as a pure input-subquadratic recurrence because it still has the explicit \(X^{191/273}\) factor.

If \(F_y\ll_\epsilon y^{\kappa+\epsilon}\), then \(y\asymp X^{1/2}\) and the output exponent is
\[
\Phi(\kappa)=\frac{191+82\kappa}{273}.
\]
In fact
\[
\Phi(\kappa)-\kappa=\frac{191(1-\kappa)}{273}>0
\quad(0\le\kappa<1).
\]
In particular,
\[
\Phi(3/4)=\frac{505}{546}\approx0.9249084249,
\qquad
\Phi(5/6)=\frac{778}{819}\approx0.9499389499.
\]
Both are weaker than their input exponents. Keeping the minimum of the imported seed and this estimate gives the seed, not an improved line. Any assertion that the currently written MHB32 recursion automatically boosts \(7/8\) toward \(1/2\) would be false.

The exact Mellin–Hankel identity itself remains useful:
\[
U(k)=\frac{A_g}{X}\left(\sum c(n)\right)^2
+\frac1{2\pi}\int_{\mathbb R}
C(1-s)^2X^{-s}\zeta(s)G(s)\,dt,\quad s=\tfrac12+it.
\]
The finite \(C\), its complex square, the rank-one term and the complete kernel must remain. A zero-free line at \(7/8\) does not justify replacing \(C(1-s)\) by \(1/\zeta(1-s)\) on the critical line.

## 4. A genuine conditional improvement: the CAP36 cap defect

This section derives a new conditional bound from the **written CAP36 estimate**, rather than claiming an absolute gain for its unknown target.

### 4.1 Exact CAP36 objects and hypotheses

Use the literal cap-three reciprocal completion \(c\) of the Möbius prefix through \(Y\), supported through \(L=Y+J\). Here \(J\) is its integer width. It satisfies
\[
\sum c(n)/n=0,\quad |c(n)|\le3,\quad
\mathcal J(c):=\sum_{k\ge1}\left|\sum_{n\le k}c(n)/n\right|^2\le2F_Y,
\]
and, with \(a=|m(Y)|\),
\[
J\le Ya/2+1.
\]
The symbol \(\mathcal J(c)\) is an energy and is not the width \(J\).

CAP36 uses the same smoothly selected microscopic harmonic observable \(U\) as MHB32. Retain all its observation assumptions, in particular
\[
X\ge8H,\qquad X\le M<2X,\qquad L^2\le8X,\qquad X\ge2HL.
\]
The last condition guarantees that the coefficient-one repair is invisible to this observable. Let
\[
\chi(n)=n^{i\tau},\quad e^{i\tau\log Y}=1,\quad
U_\tau=U(c\chi,c\chi),\quad A_\tau=U(q,q),
\]
where, exactly as in CAP36,
\[
a_\chi=\mathbf1*(\mu\chi),\qquad q=P_L(a_\chi*c),
\qquad (P_Lv)(n)=v(n)\mathbf1_{n\le L}.
\]
This is a **separately source-compressed** arithmetic transform. The proof uses the repair \(\Pi v=v-(\sum_{n\le L}v(n)/n)\delta_1\); the observable is unchanged under that repair when \(X\ge2HL\). The two source cutoffs in its kernel are retained; \(A_\tau\) is not identified with a phase average.

[CAP36, equations (0.1), (4.4), (4.7), (4.8)](https://github.com/GettysburgResearch/riemann/blob/aa725eebf89201fcbefbf7f5e209a22ec318ba5a/standalone/2026-09-25-completion-anchored-phase/PROOF.md) give
\[
\|A_\tau-U_\tau\|^2
\le2^{21}H^4\left[2\kappa(\tau)
\sqrt{\mathcal J(c)D}+D\right]^2,
\]
\[
\kappa(\tau)=\sqrt{1+\tau^2}+|\tau|,\qquad
D=32\tau^2J^4/Y^3.
\]

### 4.2 Insert the conditional pointwise input

The bound on \(m(Y)\) from Section 2 yields
\[
J=O_\epsilon(Y^{\alpha+\epsilon}),\qquad
D=O_\epsilon(\tau^2Y^{4\alpha-3+\epsilon}),
\qquad
\mathcal J(c)=O_\epsilon(Y^{2\alpha-1+\epsilon}).
\]
Using \((a+b)^2\le2a^2+2b^2\),
\[
\|A_\tau-U_\tau\|^2
\ll_\epsilon H^4\left[
\kappa(\tau)^2\tau^2Y^{6\alpha-4+\epsilon}
+\tau^4Y^{8\alpha-6+\epsilon}\right].
\]
For \(|\tau|\le1\), \(\kappa(\tau)\) is bounded, and \(8\alpha-6<6\alpha-4\) because \(\alpha<1\). Consequently, uniformly over the anchored phases in that range,
\[
\boxed{\quad
\|A_\tau-U_\tau\|_{[X,M]}^2
\ll_\epsilon H^4\tau^2Y^{6\alpha-4+\epsilon}.
\quad}
\]

For fixed \(H\):

- The conditional \(7/8\) strip gives \(O_\epsilon(\tau^2Y^{5/4+\epsilon})\).
- The conditional \(11/12\) strip gives \(O_\epsilon(\tau^2Y^{3/2+\epsilon})\).

At an output scale \(X\asymp Y^2\), these are energy exponents \(5/8\) and \(3/4\), respectively. The imported square-step seed is of scale \(Y^{4\alpha-2+\epsilon}\), so this defect bound has a smaller power by \(Y^{2-2\alpha}\). This comparison is between **upper-bound scales**, not a lower bound on the actual native energy or a bound relative to a possibly zero observable.

The first nonzero anchor \(\tau=2\pi/\log Y\), once it is at most one, also contributes the explicit \((\log Y)^{-2}\) factor. This remains a transport-error bound, not an estimate of either \(A_\tau\) or \(U_\tau\).

### 4.3 Why the existing dephasing result cannot finish this transfer

[ADP37](https://github.com/GettysburgResearch/riemann/blob/aa725eebf89201fcbefbf7f5e209a22ec318ba5a/standalone/2026-09-25-anchored-dephasing/PROOF.md) bounds a Fejer average of \(U_\tau\) by \(O_H(\log L)\), once the averaging parameter is at least \(2L^2\log Y\), with the stated alias-separation hypotheses. That sufficient dephasing range includes \(|\tau|\) of order \(L^2\), outside the bounded-\(\tau\) regime above. The full CAP36 expression then carries large \(\tau\) and \(\kappa(\tau)\) factors.

Also, the average is of \(U_\tau\), not \(A_\tau\). Generic extraction of \(U_0\) from that average can lose a power of \(L\): ADP37 proves a nonnative balanced-source counterexample for the actual same harmonic mask. A new **native** concentration or transfer theorem is required.

Thus this combined deduction really reduces one completion/transport cost. It does not bound the principal phase, the unmasked complement, or the complete Newton recurrence.

## 5. A precise route that would yield a dramatic improvement

The concrete target is the NRC32 coarse covariance inequality in [REPO_COMPARISON.md](REPO_COMPARISON.md):
\[
S_Y\le C(\log(2Y))^A(1+F_Y)^{2-\delta},
\qquad\delta>0.
\]
Together with \(F_{(Y+1)^2-1}-F_Y=S_Y+D_Y\), \(0\le D_Y<5/6\), it would give a strict contraction of polynomial energy exponents. If \(F_Y\ll Y^{\kappa+\epsilon}\), the nontrivial output exponent is at most \((1-\delta/2)\kappa\), up to arbitrary small losses, for \(0<\delta<1\). One may always replace a larger \(\delta\) by a smaller one in this range.

A rigorous iteration uses the square ladder, monotonicity, and the logarithmic factor. If
\(Y_{j+1}=(Y_j+1)^2-1\), then
\(\log Y_j\asymp2^j\); the recurrence for
\(\log(1+F_{Y_j})\) has multiplier \(2-\delta<2\) and an additive \(O(j)\) term. Dividing by \(\log Y_j\) gives a limit zero. Monotonicity fills the intervals between ladder values. This gives subpower \(F_X\), which feeds the existing native Mellin criterion, subject to its source contract.

Such a full contraction is **open** and is not a corollary of a fixed-shift Chowla assertion. It is also sufficiently strong to work from a crude polynomial seed, so the external strip alone is not the missing ingredient.

A viable combination may instead prove a contraction only for native inputs already satisfying the conditional \(3/4\) envelope and the corresponding cap-width estimate. That would make the external result operationally useful. The intended new mechanism is to copy the upstream method's **arithmetic principle**, not its formula: sum signed preimages with a common kernel, prove a surviving support restriction, and show the new child energy contracts with every endpoint and kernel seminorm paid. No such exact real-integer adapter has been proved in this import.

## 6. Verification performed for this comparison

The source identities and inequalities were read at the exact repository commits linked above. Current remote main and the five PR heads/states were queried. The exponent arithmetic in Sections 2–4 is algebraic; it is not an extrapolation from computation.

No inherited numerical campaign, Lean build, repository-wide validator or independent proof review was rerun by this comparison. Upstream theorem review belongs to the accompanying audit, not to these conditional deductions.
