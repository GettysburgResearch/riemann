# Mechanism firewalls and scope boundaries

Status: **PROVED OR IMPORTED NO-GO STATEMENTS WHERE IDENTIFIED; NO RH CLAIM.**

This note collects the shortcuts that were tested and rejected during the review.  Any future proof of the E–Widder inequality must explicitly survive these firewalls.

## 1. Positive scalar source is insufficient

PR #766 constructs actual positive theta-source quotients with reflection, positive Mellin kernels and source-defined minimum-energy universal properties, yet with off-central real zero pairs.  Therefore the implication

```text
positive theta source
+ functional equation
+ natural quotient
+ scalar Mellin positivity
    -> critical-line zeros
```

is false.

The Architecture-E source theorem must be the two-variable positive-definiteness of `A_Phi`, not pointwise positivity of `Phi`, `H_xi`, or any one-variable Mellin transform.

## 2. Local Xi asymptotics are not arithmetic selectors

The actual-Xi high-derivative, odd-current, Bessel and radial-semigroup limits are real and useful.  The #765 compact-perturbation firewall shows that the following package can coexist with a nonreal zero:

```text
positive smooth Fourier kernel;
exact Xi tail outside a compact set;
local saddle concentration;
high-derivative Gaussian/Bessel asymptotics;
radial heat limits.
```

Thus a proof cannot discard the exponentially small global interference term on the ground that all algebraic-order local asymptotics are positive.

## 3. Sparse transport cannot supply cofinal completeness

A dyadic panel with `O(j)` nodes of weight about `2^{-j}` has total mass comparable to

\[
 \sum_jj2^{-j}<\infty.
\]

Even perfect transport on every such sparse panel cannot by itself produce the divergent or complete family required to eliminate every negative direction.  A cofinal argument needs a dense transport theorem and a uniform Bessel/frame estimate, not more isolated sparse successes.

## 4. Pointwise Wigner positivity is impossible

For

\[
 H_\xi(d)=
 \Phi\left(\frac{\xi-d}{2}\right)
 \Phi\left(\frac{\xi+d}{2}\right),
\]

define the Wigner transform

\[
 W_\Phi(\xi,x)=\int_{\mathbb R}H_\xi(d)e^{ixd}\,dd.
\]

The diagonal Hermite sign can be written as a globally weighted integral of `W_Phi`.  It is tempting to demand `W_Phi>=0` pointwise.  Hudson's theorem rules this out for a non-Gaussian pure state: an everywhere nonnegative pure-state Wigner distribution must be Gaussian, while the Riemann theta kernel has non-Gaussian double-exponential tails.

The sign must arise after nonlocal weighted integration.  Pointwise phase-space positivity is not a viable target.

## 5. Non-isometric compression does not preserve contraction

A common Volterra shortcut has the form

```text
||K|| <= 1
and
C E = I
therefore
||C K E|| <= 1.
```

This is false without an isometric or compatible weighted structure.  Take

\[
 C=\begin{pmatrix}M&0\\0&1\end{pmatrix},
 \qquad
 E=C^{-1},
 \qquad
 K=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

Then `CE=I` and `||K||=1`, but

\[
 CKE=
 \begin{pmatrix}
 0&M\\
 M^{-1}&0
 \end{pmatrix},
 \qquad
 \|CKE\|=M.
\]

In the actual Architecture-E lift, the missing weighted contraction defect expands to the original signed source/Hermite quadratic form.  Proving the weighted contraction is therefore equivalent to the target, not a consequence of the pointwise scalar multiplier bound.

## 6. `PF_infinity` is not closed under positive addition

For `nu>0` and `alpha>0`, define

\[
 f_\alpha(x)=e^{-\nu x-\alpha e^{-x}}.
\]

Its bilateral Laplace transform is

\[
 \mathcal Bf_\alpha(s)
 =\Gamma(s+\nu)\alpha^{-(s+\nu)}.
\]

Each `f_alpha` is a classical Pólya-frequency kernel of infinite order.  But for distinct positive `alpha,beta`,

\[
 \mathcal B(f_\alpha+f_\beta)(s)
 =\Gamma(s+\nu)
 \left[
  \alpha^{-(s+\nu)}+\beta^{-(s+\nu)}
 \right],
\]

and the bracket vanishes at

\[
 s+\nu=\frac{(2m+1)\pi i}{\log(\beta/\alpha)}.
\]

The sum therefore has nonreal transform zeros and is not `PF_infinity`.

Consequently modewise total positivity of theta atoms cannot be summed term by term to obtain total positivity of the arithmetic theta kernel.  The coupled arithmetic sum is precisely where the zeta factor and its zero divisor enter.

## 7. Source quotient and gauge operations can lose powers

The #770 results show that:

- ordered-word quotienting changes the diagonal by factorial factors;
- principal recombination can amplify the diagonal by a horizon power;
- ratio-mask gauge inversion has a cofinal `H^{1/12-o(1)}` lower bound;
- a fixed finite physical minor can remain nonsingular for huge finite ranges while becoming singular at infinite horizon.

Therefore an estimate after quotient/gauge inversion does not automatically pull back to the source metric.  The complete connection, labels and source norm must be retained.

The E–Widder formula avoids this problem: the von Mangoldt source is inserted directly into an absolutely convergent scalar form before any nonorthogonal quotient.

## 8. Self-duality is not purity

The Segre/Chow resolutions on #769 and #781 explain reciprocal numerators and functional-equation symmetry through Gorenstein duality.  A reciprocal characteristic polynomial can still have eigenvalues off the critical circle.  The deformation-spectrum theorem makes the separation exact:

```text
reciprocal pairing          automatic;
temperedness / purity       separate inequality.
```

Euler-characteristic or Tor cancellation cannot replace a positive polarization on actual cohomology.

## 9. Arithmetic moduli are not wall-protected by default

The Epstein packets on #781 provide arithmetic completed theta objects with certified off-critical real and complex zeros.  Hence arithmetic origin, theta representation, a functional equation and connected deformation data do not isolate a critical-line chamber.

A wall architecture requires a new invariant absent from the Epstein counterexamples.  Topology alone is insufficient.

## 10. Negative index counts locations, not multiplicity

For a nonreal conjugate pair, the Hermite kernel has a `(1,1)` feature block.  Multiplicity scales that block but does not add linearly independent Cauchy features.  Therefore

\[
 \operatorname{sq}_{-}(\mathcal B_X)
\]

counts distinct upper-half-plane zero locations, not algebraic multiplicity.  Any theorem claiming a multiplicity-weighted equality is false without a confluent feature enlargement and a correspondingly different reduced quotient.

## 11. Low finite order does not imply all order

The repository has accepted or proposed low-order results:

- scalar monotonicity and concavity;
- safe Pick positivity through finite order three;
- finite Loewner and Hausdorff moment identities;
- terminal-scale and small-scale positivity.

The Stieltjes conclusion is an all-order matrix/differential statement.  The first unsupported Widder rung already introduces a third derivative,

\[
 -D_u^3[u^2q(u)]\ge0,
\]

which is not controlled by the known first- and second-derivative signs.  Finite order cannot be promoted by induction without a new recurrence preserving the correct sign and source metric.

## 12. Direct absolute Euler summation stops before the detection annulus

The older safe-line square-root generating transform is absolutely Eulerian only inside the disk `|w|<3/4`.  An off-line zero at horizontal depth `y` creates a pole at

\[
 w=1-y^2\in(3/4,1).
\]

Thus the direct generating-function Euler sum becomes nonabsolute exactly before the RH-detecting annulus.  Crossing that annulus is not a routine dominated-convergence argument.

The E–Widder coordinate removes this particular obstruction by evaluating every fixed derivative order at `s>1`; it does not remove the sign problem.

## 13. Absolute prime envelopes destroy the mechanism

The filters

\[
 \mathcal L_k(u,\log n)
\]

need not have one sign.  Replacing them by absolute values gives a substantially stronger statement and erases cancellations between prime-power translations.  The #765 and #770 firewalls both indicate that the sign-bearing remainder can be much smaller than the absolute source mass.

Any proof of `(EW)` must assemble signed prime structure before estimation.

## 14. Renaming an equivalent condition is not progress

After the closure theorem, the following are equivalent:

```text
A_Phi is PSD;
K_0 is PSD;
Hermite–Bezout kernel is PSD;
companion has zero negative squares;
safe Pick kernel is PSD at all orders;
q is Stieltjes;
all E–Widder inequalities hold;
prime-shift operator is accretive;
RH.
```

A claimed proof that passes from one line to another without proving new arithmetic input is circular, even if the intermediate language is de Branges, canonical systems, purity, total positivity, conservative scattering or operator monotonicity.

## 15. Required shape of a genuine completion

A noncircular completion must supply at least one of the following directly from the retained source:

1. a source-local Gram factorization of `A_Phi`;
2. a positive Stieltjes measure for `q` constructed without the zero set;
3. a source-compatible factorization `T+T^*=V^*V` of the prime-shift operator;
4. an all-order recurrence proving the E–Widder inequalities with no loss at the critical mode;
5. a polarized cohomological realization whose purity theorem evaluates to the same source form.

The proof must also explain why the mechanism fails for the native positive-source counterexamples of #766 and the Epstein counterexamples of #781.

## 16. Stop conditions for future passes

A proposed completion must be rejected or demoted if it does any of the following:

- assumes raw companion innerness or source/Hermite positivity;
- proves only pointwise entry positivity;
- sums modewise `PF_infinity` certificates;
- uses a non-isometric compression without a metric intertwiner;
- infers purity from reciprocity alone;
- extrapolates finite-order positivity to all orders;
- replaces the signed prime sum by an absolute envelope;
- crosses the Euler annulus by an unjustified interchange;
- imports the zero measure in the construction of the allegedly arithmetic Stieltjes measure.

These are mechanism boundaries, not reasons to abandon the programme.  They specify what the next proof must genuinely add.
