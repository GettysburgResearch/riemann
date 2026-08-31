# 6. Precise next lemmas for the non-primary targets

## Target B — stronger Mellin criterion

**New firewall from Target F.** The continuum radial transport is
strictly totally positive for every positive radial source. This
property is therefore universal and insufficient as an Xi selector.

The remaining meaningful total-positivity question is at the
**logarithmic Mellin source level**, not the radial continuum limit.

**Next lemma B1.** For a reciprocal density \(c(t)\), characterize when
\(x\mapsto e^{x/2}c(e^x)\) is PF\(_\infty\), and determine the zero
class of its bilateral Laplace transform after the endpoint-pole
subtraction required by completion.

**Stop condition.** A condition fails as an RH-facing criterion as soon
as one proper theta-source counterexample from #766 satisfies it while
retaining its certified off-central real zero. Do not replace the
source quotient by a post-Mellin Schur complement.

## Target C — growing divisor depth

The current fixed-\(J\) proof contains an explicit deep-component ratio
of the form

\[
C_J k^{J+1}
\left(\frac{A_{J+1}}{A_J}\right)^{1/2}
=
C_J k^{J+1}
\left(\frac{J}{J+1}\right)^{(k-1)/2}.
\tag{C.1}
\]

With the displayed echelon constants growing at least exponentially in
\(J\), the current estimates naturally require roughly

\[
J^2\log k=o(k),
\tag{C.2}
\]

suggesting a first attainable regime
\(J=o(\sqrt{k/\log k})\), not yet \(o(k/\log k)\).

**Next lemma C1.** Reprove every fixed-depth estimate with explicit
\(J\)-dependence and show that the Schur-complement error is
\(o(A_J)\) uniformly for \(J=o(\sqrt{k/\log k})\).

**Next lemma C2.** Derive a scaled Jacobi/continued-fraction recurrence
for the nested Schur complements before attempting a larger regime.

**Stop condition.** If the Fourier-projection reserve
\((A_{J+1}/A_J)^{1/2}\) no longer dominates the echelon and inverse
constants, the present proof architecture has stopped; finite data
must not be extrapolated past that point.

The \(j\le k/96\) proper theta-source theorem does not solve C because
it changes the source quotient with \(j\).

## Target D — Hecke support

**Next lemma D1.** Replace the coefficientwise \(d_4\) estimate in the
\(X\)-moment by a full Petersson/Kuznetsov quadratic-form bound uniform
over an arbitrary selected Hecke subset.

A reduction from \(O(r\log^5k)\) to \(O(r\log k)\) would align the
zero-free scale with the cusp-concentration obstruction.

**Stop condition.** Average cancellation over the whole Hecke basis is
not enough: the theorem must survive adversarial subsets. If the proof
uses a basis rotation not induced by Hecke lines, it no longer addresses
the stated support problem.

## Target E — Xi transport

**Next lemma E1.** For the declared quadratic model, solve the contour
optimization exactly:

\[
\max_{\Gamma\in\mathcal C}
\left[
\min_{w\in\Gamma}|P(w)|
-
\max_{w\in\Gamma}|F(w)-P(w)|
\right].
\]

The admissible contour class and error majorant must be fixed globally
for all 26 points. This is a finite robust-optimization theorem, not a
precision campaign.

**Stop condition.** If the optimum is nonpositive for an unresolved
point under the frozen jet box, that is a no-go theorem for the declared
model. It is not a no-go theorem for transport itself.

## Target H — derivative certificate

**Next lemma H2.** Extend the existing interval evaluator to the tuple

\[
(\Lambda,\Lambda_s,\Lambda_{ss},\Lambda_x,\Lambda_y)
\]

with one common truncation and tail budget.

For an off-line branch, certify (H.3). For a candidate wall point,
certify the double-zero system and the transverse ratio in (H.6).

**Stop condition.** A winding-one box proves simplicity only at the
off-line zero. It does not certify a wall or a crossing direction.

---

# 7. Separation of evidence classes

## Local finite certificates

* #765: 40 fifth-companion zeros; 8/26 frozen panel transports.
* #770: rank 20 on every integer \(450\le H\le2^{48}\); exact local
  inverse certificates for the full-support rows.
* #781: one real sign-change bracket; two winding-one complex
  rectangles; exact finite graph corpora.

## Analytic theorems proved in this packet

1. The Pick-kernel negative index equals the number of distinct
   upper-half-plane zeros for real polynomials and genus-at-most-one
   real entire functions.
2. Algebraic multiplicity is invisible after companion cancellation;
   \((z^2+1)^m\) is the sharp counterexample.
3. The literal Xi source has the explicit \(E^{-1}\) and \(E^{-2}\)
   correction polynomials (F.3)–(F.4).
4. The first source correction is inward-monotone, exactly
   total-positive in the continuum model, and not a semigroup cocycle.
5. The odd-order floor rule produces a larger oscillatory
   \(O(\delta)\) correction.
6. The 64 full-support rows have explicit lower and upper frame bounds.
7. The source tensor decoder has condition number at most 3 beyond
   (G.10).
8. Pure-prime alias collapse is the one-dimensional determinant
   representation \(\Lambda^2U_i\).
9. Winding one implies a simple Epstein zero and a local analytic
   branch; an off-line symmetry pair can meet the critical line only
   on the multiple-zero discriminant.

## RH-facing speculation, not established

* No off-axis Xi zero is proved.
* No Pick-kernel negative eigenvalue for Xi is certified.
* No positive-source or total-positivity property proves critical-line
  purity.
* No growing-depth divisor ladder is proved.
* No exact Hecke support threshold is proved.
* No Xi transport exists at the 18 unresolved points under a stronger
  model merely because the frozen quadratic criterion fails.
* No Epstein wall component, crossing direction, or connected-island
  theorem is yet certified.
* RH and GRH remain unproved.

---

# 8. Recommended stop-go order for the next pass

1. **Accept Target A after independent sign/convention review.**
   The load-bearing identity is (A.1); test it on \(f(z)=z\) and on
   \((z^2+1)^m\). Stop immediately if the denominator convention
   changes the kernel sign.

2. **For Target F, authenticate the weighted expansion before adding
   numerics.** Check (F.4), then check the exact cocycle witness
   \(-25/(8\pi)\). Do not call the \(E^{-1}\) term the first correction
   of the rounded family unless (F.16) is removed.

3. **For Target G, record the frame theorem separately from rank.**
   The only imported constants are \(B\) and \(L_3\). Recompute
   \(H_{\mathrm{cond}}\) exactly and bind the three local source
   matrices. The decoder is invertible postprocessing, not a source
   projector.

4. **For H, differentiate the existing certified representation.**
   Do not launch a new moduli atlas. A single derivative-certified
   branch box and a single candidate discriminant box are the next
   theorem-sized objects.

5. **Do not merge evidence classes.** Finite transport panels,
   positive Mellin sources, radial total positivity, graph phase
   diagrams, and Epstein zeros are separate mathematical objects and
   support no RH conclusion by analogy.
