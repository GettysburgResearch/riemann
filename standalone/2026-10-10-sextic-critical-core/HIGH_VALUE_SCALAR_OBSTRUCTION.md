# High-value amplification: a squarefree-row gain and the all-row obstruction

Status: a proved consequence of the preceding packet's Gram theorem and imported second moment, together with a precise obstruction for their collected scalar upper bounds. No full near-linear-row moment improvement is claimed. The artificial distribution below is not an actual sextic or Möbius counterexample.

Baseline: PR 913, head `6498d6cc2eded03159c7332b25fd224ad07f89c1`. Dependencies are the reviewed `SEXTIC_GRAM_BOUND.md`, including its Bombieri–Halasz–Montgomery consequence; the exact finite incidence identities and divisor coefficient bounds; the imported all-row second moment; and, only where explicitly used, the uniform pointwise estimate from a common zero-free half-plane. No frozen note is modified.

## 1. Amplify before using the Gram theorem

Retain the literal polynomial

\[
A_u(D)=\sum_{(n,S)=1}\mu_K(n)\nu(n)\chi_n(u)W(Nn/D).
\]

Fix an integer \(m\ge1\), and restrict the row set in this section to squarefree primary \(u\) with \(Nu\asymp H\), outside the fixed bad primes. On each fixed ray class, reciprocity and multiplication give

\[
A_u(D)^m=\sum_n c_m(n)\chi_u(n),\qquad
Nn\asymp D^m,\qquad
\sum_n|c_m(n)|^2\ll D^{m+\epsilon}.
\tag{1.1}
\]

The columns \(n\) here need not be squarefree. Their coefficients are the actual finite product convolution, with the fixed reciprocity factor included. The fixed-order ideal divisor bound and counting the supported factor tuples prove the energy estimate. Every nonunit zero is retained by multiplicativity. The Gram theorem's physical inner index is unrestricted, which is precisely what permits (1.1).

Let \(R(V)\) count a subset of such rows on which \(|A_u(D)|\ge V\). Use a fixed nonnegative smooth majorant for the coefficient support in (1.1), at physical scale \(L=D^m\). The row Gram theorem has

\[
G(H,L)=HL+H^2L^{1/3}.
\]

The BHM inequality is

\[
R(V)V^{2m}\ll D^{m+\epsilon}
       \bigl(D^m+\sqrt{R(V)G(H,D^m)}\bigr).
\]

Solving the resulting quadratic inequality in \(\sqrt R\) yields

\[
\boxed{
R(V)\ll (DH)^\epsilon
\left[
\frac{D^{2m}}{V^{2m}}
+\frac{H D^{3m}+H^2D^{7m/3}}{V^{4m}}
\right].}
\tag{1.2}
\]

Fixed ray splits, units, bad squarefree factors and dyadic row annuli cost only fixed constants or logarithms. Thus the resulting moment bound below covers every squarefree element row, including its finite bad-prime possibilities. It does not cover nonsquarefree rows by assertion.

## 2. A genuine squarefree-row fourth-moment bound

Assume the imported all-row second moment at the polynomial scale being used:

\[
\sum_{0<Nu\le H}|A_u(D)|^2\ll D^\epsilon HD.
\tag{2.1}
\]

Use (1.2) with \(m=2\). Below an amplitude threshold \(T\), (2.1) contributes at most \(D^\epsilon HDT^2\). Above \(T\), integrate the counting bound against \(4V^3\,dV\), using the elementary maximum \(|A_u(D)|\ll D\). The \(V^{-4}\) term costs a logarithm; the \(V^{-8}\) terms give

\[
\sum_{\substack{0<Nu\le H\\u\ \mathrm{squarefree}}}|A_u(D)|^4
\ll (DH)^\epsilon\left[
HDT^2+D^4+(HD^6+H^2D^{14/3})T^{-4}\right].
\]

Set \(T^6=D^5+HD^{11/3}\). If this exceeds the elementary maximum, the low-amplitude estimate alone is still valid. In all cases,

\[
\boxed{
\sum_{\substack{0<Nu\le H\\u\ \mathrm{squarefree}}}|A_u(D)|^4
\ll (DH)^\epsilon
\left[D^4+HD^{8/3}+H^{4/3}D^{20/9}\right].}
\tag{2.2}
\]

This uses the actual Möbius coefficients through (2.1), and the actual product convolution in (1.1). It is stronger than the old uniform-pointwise interpolation on this row subset for a nonempty intermediate range. Specifically, if \(\beta>5/6\) and the previously proved uniform estimate \(|A_u(D)|\ll D^{\beta+\epsilon}\) is available, then every exponent in (2.2) is strictly below \(h+1+2\beta\), for \(H=D^h\), provided

\[
3-2\beta<h<6\beta-\frac{11}{3}.
\tag{2.3}
\]

This interval is nonempty exactly when \(\beta>5/6\). With the earlier conditional value \(\beta=139999/160000\), its endpoints are

\[
\frac{100001}{80000}=1.2500125,
\qquad
\frac{379991}{240000}=1.583295833\ldots.
\]

At the desired near-linear scale \(1<h\le1.1\), the \(D^4\) term already exceeds the old full fourth-moment upper bound. Thus (2.2) gives no near-linear improvement even before the missing nonsquarefree rows are restored. It must not be published as a full-moment bound.

## 3. What the scalar data permit near the target scale

Here is a quantitative obstruction to obtaining an improvement merely by optimizing the collected scalar norm bounds. Let

\[
\frac12<\beta<1,\qquad
1\le h\le\min\left\{\frac{11}{10},3-2\beta\right\},
\qquad H=D^h.
\]

On an abstract set of available squarefree rows of norm comparable to \(H\), assign amplitude

\[
V_*=D^\beta
\quad\hbox{to}\quad
R_*\asymp D^{h+1-2\beta}
\quad\hbox{rows},
\]

and assign zero elsewhere. There are enough squarefree rows because \(h+1-2\beta<h\). This is only an assignment of numbers to row labels; no claim is made that one fixed Möbius polynomial, or even one common coefficient vector, realizes it.

Its moments are

\[
R_*V_*^{2m}\asymp D^{h+1+2(m-1)\beta}.
\tag{3.1}
\]

In particular it saturates the imported second-moment size and every higher bound obtained by multiplying that second moment by the uniform maximum. It is compatible with each of the following scalar constraints:

1. **Row count and maximum:** \(R_*\le H\) and \(V_*=D^\beta\).
2. **All the classical squarefree-row moment majorants:** the available coefficient-energy reduction gives an upper bound proportional to
   \[
   HD^m+D^{2m}+H^{2/3}D^{5m/3}.
   \]
   For \(m=1\), its first term covers (3.1). For every \(m\ge2\), its \(D^{2m}\) term alone covers it, since
   \[
   2m-[h+1+2(m-1)\beta]
   =2(m-1)(1-\beta)+1-h\ge3-2\beta-h\ge0.
   \]
   The ordinary primitive-character alternative, with majorant \(D^{2m}+H^2D^m\), is compatible for the same reason.
3. **Every fixed-order amplified Gram high-value bound (1.2):** for \(m\ge2\), its first term at \(V_*\) is already at least \(R_*\), by the same inequality. For \(m=1\), the term \(HD^3/V_*^4\) is at least \(R_*\), since its exponent exceeds \(h+1-2\beta\) by \(2-2\beta>0\).

The distribution can be placed entirely in the valuation block \(a_1\asymp H\), with all the other layers and the sixth-power base equal to one. Therefore a scalar refinement that only decomposes into the existing conductor/valuation blocks does not eliminate this example. No exceptional sixth-power row is needed to exhibit this limitation.

For the conditional \(\beta=139999/160000\), the entire intended interval \(1<h\le1.1\) satisfies these inequalities. Consequently the listed scalar constraints alone cannot imply any fixed power improvement over

\[
HD^{1+2(k-1)\beta}
\]

for any fixed \(k\ge2\). This is an obstruction to an implication from a specified list of upper bounds, not an obstruction to the actual number-theoretic moment theorem.

## 4. What additional information would escape the obstruction

A useful new estimate must prohibit the amplitude/count pair
\(V_*=D^\beta\), \(R_*=D^{h+1-2\beta}\) on the genuinely squarefree conductor block. Examples would be a strict improvement of the high-value count at that scale, or a signed balanced-coefficient estimate that cannot be reduced to coefficient mass and the current Gram row norms. Merely applying the same Gram bound to higher powers, interpolating more scalar moments, or deleting exceptional rows does not supply that information.

The complementary reflection calculation in `REFLECTION_SCALAR_AUDIT.md` retains an exact angular weight and quadratic cross-symbol after cancellation. It identifies a possible source of the additional coupled arithmetic information, without asserting that it has already supplied the missing estimate.
