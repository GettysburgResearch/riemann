# Dong–Wang–Wang–Zhang and the finite phase certificates

17 November 2026. Follow-up to the full reading of all 19 pages of arXiv:2608.31060v1. This audit reconstructs the pointwise input and asks what it can certify in the finite Nyman–Beurling projection. The phase comparison uses the [reviewed finite projection](adversarial_reviews/director_finite_lower_round8.md) and the [exact phase regularization](../proposals/independent_campaigns/latest62_phase_regularization.md). It does not claim an effective numerical zero search.

## What the inverse theorem uses

Write \(Q=\log T,\ y=\log x,\ S(x,t)=\sum_{n\le x}n^{it}\). Theorem 1.1 takes \(T\le |t|\le2T\), \(\sqrt Q\le y\le Q/2\), and a single actual value \(|S(x,t)|=x/N\) with \(1\le N\le y^{1/100}\), beyond an absolute threshold. It gives one center \(\phi=t-t_0\) with \(|\phi-t|\le cN\); for all \(cN^6\le L\le y/2\) there are at least \(L/360\) zero copies in
\[
 \{|s-(1+i\phi)|<LQ/y^2\}.
\]
The center is the twist from (2.4) and is shared across radii. The frequency used to prove the zero count can vary with \(L\). No root derivative, inverse of a root derivative, simplicity, RH or GRH enters this implication.

The actual input has coefficients all equal to one and a prescribed phase \(t\log n\) from one real \(t\). It is converted into a pretentious twist and a local Hölder bound for the normalized sums \(S(e^v,t-t_0)/e^v\). The Fourier identity (3.6) then uses the Dirichlet series of this same multiplicative twist. The pole contribution \(2\pi(1+i(t-t_0))^{-1}\exp((\lambda+i(t-t_0))^2/(2\mathcal T))\) is necessary in that identity and negligible at \(\mathcal T=\lambda/y\). The normalized Gaussian error is \(O((\lambda y)^{-1/6})\). Since the lower input is \(1/N\), the condition \(\lambda y\gg N^6\) absorbs this error. The resulting spectral input is a large pointwise \(|\zeta(1-\lambda+iu)|\), of size at least an absolute constant times \(\lambda^{-1}(\lambda y)^{1/3}e^{\lambda y/2}\), with \(u\) near \(-\phi\). Hadamard comparison across \(\Re s=1\) turns this into a positive weighted zero sum, and the far contribution is subtracted without a root-by-root derivative estimate.

There is a second sufficient route inside the proof. For \(\lambda=L/(40y)\), if one has independently established
\[
 \sum_\rho \frac{\lambda}{|1+\lambda+i(\phi+\xi)-\rho|^2}\ge y/4,
 \qquad |\xi|\le 2\lambda\sqrt{Q/y},
\]
with \(T\le|t|\le2T,\ |\phi-t|=o(T)\), \(cN^6\le L\le y/2\) as above, the final far/near comparison applies directly. The positive sum can also be forced by a vetted lower bound for the ordinary zeta modulus on the left line through (3.3). A small or large reciprocal on the critical line has a different sign and/or location: the proof uses a lower bound for the numerator modulus on \(1-\lambda\), and the companion value on \(1+\lambda\) is bounded **above**. Thus no bound for \(1/\zeta\) by itself or for a reciprocal approximation norm is the needed spectral input.

## Compatible input and a finite enclosure rule

For fixed \(x\), a local **lower** moment over an interval \(I\subset[T,2T]\) gives a valid existential input. If \(0<|I|<\infty,\ k>0\) and
\[
 |I|^{-1}\int_I |S(x,t)|^{2k}\,dt>(x/N_0)^{2k}
\]
for \(1\le N_0\le y^{1/100}\), there is a \(t\in I\) with \(N=x/|S(x,t)|<N_0\). Choose a single \(L\ge cN_0^6\) with \(L\le y/2\). The theorem forces its disk centered within \(cN_0\) of that unknown \(t\), and hence within the vertical enlargement of \(I\). Strictness gives an open set of witnessing ordinates by continuity. The same argument works for any lower moment of the exact same sum with a probability measure supported in the permitted height block. An upper moment cannot establish this premise. A lower moment for \(|\zeta|\), \(|1/\zeta|\) or a polynomial with Möbius coefficients has no substitution in the theorem. It would first need a quantitative comparison to \(S\) or a separate pointwise lower bound for the specific left-line modulus.

The sum itself is finitely checkable. At a rationally specified \(t_\circ\), enclose each \(\exp(it_\circ\log n)\) by complex interval arithmetic. If a certified approximation \(C_\circ\) has \(|S(x,t_\circ)-C_\circ|\le e_\circ\) and \(|t-t_\circ|\le d\), then
\[
 |S(x,t)|\ \ge\ |C_\circ|-e_\circ-d\sum_{n\le x}\log n .
\]
There is no derivative of zeta in this test. If the lower bound is at least \(x/N_0\), and an interval of heights verifies \(T\le|t|\le2T\), the conclusion can be enclosed in a single explicit disk centered at \(1+it_\circ\) of radius \(LQ/y^2+cN_0+d\), or more usefully in the union of disks with radii \(LQ/y^2\) and centers along that certified vertical interval. The latter retains the precise real-part bound. This is an interface to a derivative-free *existence region*, not an isolated root interval. The paper gives absolute thresholds and constants rather than numerical \(c,T_0\). A fully effective finite certificate needs verified explicit upper bounds for those constants, or a direct certified adaptation of the analytic inequalities on the chosen input. A large finite sum certified numerically alone does not verify the required onset or nonempty \(L\)-range.

For a disk wholly to the right of the critical line, one must choose \(L<y^2/(2Q)\). Since \(y\le Q/2\), this is stricter than \(L\le y/2\), and is available exactly when \(cN^6<y^2/(2Q)\). In particular the theorem's lower length \(y=\sqrt Q\) need not admit a near-one disk at all. For a fixed \(0<r<1/2\), taking \(L=r y^2/Q\) gives real parts strictly greater than \(1-r\), if \(N^6\le r y^2/(cQ)\). These are local zero copies. They need not have distinct ordinates.

## Incompatibility tests for the phase lower bound

The cutoff phase projection requires a known actual \(\rho=1/2+i\gamma\) and chooses zeroth evaluation at that precise point. For higher jets it needs the certified vanishing order. Exact location need not be represented by digits if the isolating interval plus validated existence and appropriate remainder bounds suffices, as in the finite Hardy-sign certificates. The vanishing on the approximation space is along the specified critical-line evaluation. A zero count in an open two-dimensional disk does not provide that functional.

- When \(LQ/y^2\le1/2\), the entire open disk lies strictly to the right of the critical line. Its zeros cannot be fed to the current critical-line phase formula. In this range the conclusion, if triggered, is evidence of off-line zeros.
- When \(LQ/y^2>1/2\), the disk may meet the line, but a count there does not establish that any zero lies on the line, or its ordinate or vanishing order. Adding RH would turn any known zero in the disk into a line zero but would make a narrower-disk witness impossible. Quantitative isolating and location bounds would still be needed for a finite projection.
- The finite phase lower bound has the converse problem. A reviewed critical-root test can succeed even when the arithmetic large-value antecedent fails at every \(t\) on the block. Take \(x=\sqrt T\), an allowed upper endpoint of Theorem 1.1. Lemma 5.1 gives \(|S(\sqrt T,t)|/\sqrt T\ll T^{-1/13}=o((\log\sqrt T)^{-1/100})\) uniformly for \(T\le |t|\le2T\). There are arbitrarily high critical-line zeros, so blocks containing genuine critical-root witnesses still have no qualifying \(S(\sqrt T,t)\). This rejects a blanket reverse implication from a phase zero to a pointwise large sum at an allowed test length; it does not test other lengths. The exact Sobolev filter frontier, moreover, has the same value for every measurable unitary multiplier by Plancherel, including the identity. Consequently its constant contains no information about a specific arithmetic large sum.

A right-half-plane zero potentially supports a different finite lower certificate via the ordinary Hardy reproducing kernel, if an actual interior root is separately validated. That would be an off-axis obstruction using a different functional and would require the appropriate pole-removed Hardy space. It is not the existing critical-line phase or multiplicity formula.

## A zero-free-region corollary of the inverse direction

This is an exact parameter transfer, not a claim about a best bound for these partial sums. Suppose the usual high-height Vinogradov–Korobov region supplies zero-free width at least \(C Q^{-2/3}(\log Q)^{-1/3}\) for \(|\Im s|\asymp T\), with a fixed \(C>0\). Choose \(r=c_1Q^{-2/3}(\log Q)^{-1/3}\) with fixed \(0<c_1<C\), absorbing the bounded changes between \(\log |\Im s|\) and \(Q\). Take \(L=r y^2/Q\). The \(L\)-range is nonempty for all possible large-value inputs \(N\le y^{1/100}\) as soon as \(r y^2/Q\ge c y^{6/100}\). Equivalently it suffices, with a suitable constant, that
\[
 y\ \ge C_1 Q^{250/291}(\log Q)^{50/291},\qquad y\le Q/2.
\]
Indeed \(2-6/100=97/50\) and inversion gives exponents \((5/3)(50/97)\) and \((1/3)(50/97)\). The disk cannot contain a zero, so \(|S(x,t)|< x/(\log x)^{1/100}\) uniformly there for sufficiently large \(T\). A classical width of order \(1/Q\) instead gives \(L=O(y^2/Q^2)=O(1)\), insufficient for an unbounded \(N\)-range. This illustrates why the theorem’s radius and the sixth-power threshold both matter. The zero-free input is separate and applies only near 1, and this corollary gives no upper count for full blocks of zeros.

## Dependencies and outstanding verification

The main external analytic inputs are Granville–Soundararajan’s Halász comparison and Lipschitz estimates (their older paper Lemma 7.1 and Theorems 2b, 4), their inverse-theorem template for large character sums, Euler–Maclaurin, the standard completed-zeta Hadamard product and functional equation, and van der Corput/Kusmin–Landau for the long-length addendum. The shifted pole and Gaussian localization are supplied in the Dong paper rather than suppressed by reference to the character case. The pointwise forcing theorem is unconditional in its stated asymptotic ranges. No numerical threshold or validated conversion to critical jets was produced. The proposed subexponential-length corollary and the finite hypothesis map are ready for independent review.

- [Dong–Wang–Wang–Zhang, arXiv:2608.31060v1](https://arxiv.org/pdf/2608.31060v1)
- [Granville–Soundararajan, large-character-sum inverse theorem](https://arxiv.org/abs/1501.01804)
- [Granville–Soundararajan, multiplicative mean values](https://arxiv.org/abs/math/9911246)
- [Explicit Vinogradov–Korobov example](https://arxiv.org/abs/2306.10680v1)
