# Independent review of the analytic interface and global conclusion

**Reviewer:** the field-audit agent, independently of the boundary author.  
**Result:** PASS for the stated import-dependent corollary.  
**Reviewed claim:** AMPLIFIED-BOUNDARY-87488666-20261018.

This review checks the application of the specified source statements,
their quantifiers, and the new proof's numerical coverage. It does not
independently prove the upstream cubic-theta, reflection, detector, or
Hecke moment theorems. It is not a certification of an unconditional
resolution of the quasi-Riemann hypothesis or RH.

## 1. Exact reviewed files

The paths are relative to the research packet root.

| File | SHA-256 |
|---|---|
| correlated/UNIFORM_BOUNDARY.md | 61149bdf31f4e12541da5d7543a2cb0311fd93878f1c5e034e2e1b0e4a24a385 |
| correlated/certify_boundary.py | 79a1519c18ed8f8caf014acc4637147f1eb1c6e1f2f73cad227cf6160694afbf |
| correlated/rational_polynomial.py | e9d3966ae6ace7e3bcab042e739e548e7389ba1ace0172aeb1243ce62f350133 |
| correlated/certificate.json | c3cbac1ea1b98e1227757189c3958b616235ab69701fe69e51d710e8d1145d2f |

The source version consulted directly was Yuanda Xu and Hejian Sang,
*Amplified moments and a refinement of the quasi-Riemann hypothesis*,
[arXiv:2610.15291v2, October 15, 2026](https://arxiv.org/html/2610.15291v2):
Section 2, Propositions 3.1, 4.1, 5.1 and 6.1, Section 6.2, Sections
7–8, and Appendices B, C, E, F and G. The upstream source was also read
where the natural character presentations and buffered polynomial
estimates mattered.

## 2. The source allows a new parameter tuple

The decisive source statement is Lemma 8.1. It concerns any tuple
admissible under Section 6.2 whose moment parameter is licensed by the
preceding family bound. It is not restricted to the two examples in
Section 7. Proposition 6.1 likewise has a general admissible-tuple
statement. Consequently a new tuple can be supplied by an exact
certificate without claiming a new analytic moment estimate.

The reviewed proof uses

$$
\kappa=\frac{29991}{40000},\qquad
\frac{1+\kappa}{2}=\frac{69991}{80000}.
$$

The right-hand side is the source's first-stage family conclusion. It
is established before the proposed new tuple is applied. In particular,
neither $0.87488666$ nor an ordinary-zeta-only hypothesis is used to
license this $\kappa$. The full auxiliary Hecke family remains in the
licensing argument.

## 3. Coverage of every numerical premise

I compared the predicates in the checker with the complete admissibility
list in source Section 6.2. The coverage is complete:

| Premise group | Independent scope check |
|---|---|
| Geometry | Both length endpoints, both moment-range endpoints, positive imbalance, the $87/100$ contour boundary, and both low-side scale inequalities are checked. |
| Prime supply | Both capacity comparisons, the supply on the extended row range, and both inequalities on $l_y$ are checked. |
| Positive reserve | Positivity and upper bounds for $g_*$ and $2r$, together with $g-2r>g_*$, are checked. |
| Intermediate endpoint | The completed-square certificate covers $0\leq\delta\leq5/6$, $0\leq x\leq1/2$, containing the required rectangle starting at $\delta=1/8$. |
| Other rows | Both endpoints of the small-$\delta$ maximum, the detector-floor bound, and the small-row bound are checked separately. |
| External license | The preceding-stage equality is checked separately from numerical admissibility. |

The variable $r$ in the proof is the positive row-range extension called
$\zeta$ in the source and receipt. This renaming is consistent.

The denominator argument includes the two endpoint cases
$\delta=0,5/6$: $D,P>0$ and
$J=(5/6-\delta)D+\delta P$ imply $J>0$ throughout. Thus clearing
$J$ does not reverse an inequality or omit a singular boundary.

I read the rational polynomial implementation. Its coefficients expand
the stated expression $Q=-8J(E+g)$, and its complete-square identity
uses $4AC-B_q^2$, with the correct sign. Positivity of its coefficients
on $y\geq0$ supplies a continuum proof, rather than a sampled maximum.
The separate independent polynomial reconstruction in the packet is
additional evidence; this review does not relabel a replay of the
author's checker as that independent reconstruction.

## 4. Complete remainder and height scope

The inference uses the full conclusion of Proposition 6.1, not just its
endpoint expression. Under its hypotheses, the same normalized probe
has the direct bound and the complete remainder bound, with a positive
exponent saving common to the targets. The source's treatment includes
the small rows, detector floor, distant rows, principal residue errors,
and local main/error expansion.

I checked the features that prevent an incorrect finite-height reading:

* The physical character presentations retain their original zeros at
  ramified primes. The numerator need not equal the detector's fixed
  twist; the averaged-numerator statement does not require that
  identification.
* Appendix B controls the primitive approximate-functional-equation
  profiles and fixed-prime restorations. It treats row-dependent
  conductors without turning them into arbitrary arithmetic coefficients.
* Appendix C leaves exterior reciprocal integrals on globally valid
  contours. Its interior moves preserve the buffered height interval
  and one cumulative frequency allowance.
* Appendix F fixes the common losses and finite prime-slot system before
  taking the large parameter to infinity. Target-dependent seminorm and
  height orders are fixed before selecting the height exponent, and
  the exterior tail order is chosen afterwards. Constants and thresholds
  may depend on the target; the final positive saving does not.

Those are declared analytic imports of this corollary. The new exact
certificate neither supplies nor independently authenticates them.

## 5. Why the quantifiers imply all heights and conductors

Here is an explicit check of the logical conclusion. Let $\beta_*$ be
the full-family supremum, and suppose
$\Delta=\beta_*-B_\dagger>0$. The applicable source statements give,
for every fixed target and the same probe,

$$
|J_\eta(Z)|\ll_\eta
 Z^{C_b(\beta_*)-3\Delta/4},\qquad
|J_\eta(Z)-f_\eta(Z)|\ll_\eta
 Z^{C_b(\beta_*)-\rho},
$$

with $\rho>0$ independent of the target. Hence $f_\eta$ has a common
positive power saving. Taking a smaller common saving
$0<\epsilon_*<\Delta$ keeps
$\beta_*-\epsilon_*>B_\dagger>87/100$.

Its Mellin transform is holomorphic to the right of
$\beta_*-\epsilon_*$: the power saving controls the large-$Z$ end,
and the defining Gaussian integral gives arbitrarily rapid decay at
the small-$Z$ end. On the initial absolute line the transform is

$$
e^{(s-5/6)^2}\frac{H_\eta(s)}{L_F^S(s,\eta)}.
$$

The Gaussian is never zero, and the source supplies
$|H_\eta(s)-1|\leq1/2$ throughout the requisite half-plane. The
reciprocal therefore continues holomorphically there for each target.
The common $\epsilon_*$ contradicts the defining supremum; no maximum
or specially chosen target attaining $\beta_*$ is required.

This is a half-plane statement for every imaginary part. It does not
assert useful numerical uniform constants or an effective height
threshold. The internal height truncations used to estimate the probe
are not a cutoff in its Mellin continuation conclusion.

For ordinary zeta, the fixed-field identity

$$
\zeta_{\mathbb Q(\sqrt{-3})}(s)=\zeta(s)L(s,\chi_{-3})
$$

has an entire nonprincipal second factor, so a nontrivial zeta zero
persists on the left. Finite deleted Euler factors are nonzero in
$\Re s>0$. A principal pole gives a zero of the reciprocal and does not
invalidate the argument. The same source transfer supplies the more
general Dirichlet conclusion stated in the proof.

## 6. Replay and verdict

Both of the following were run independently in the review session and
returned PASS:

~~~sh
python -B correlated/certify_boundary.py --check correlated/certificate.json
python -B -O correlated/certify_boundary.py --check correlated/certificate.json
~~~

Both returned the receipt hash in Section 1, 21 strict scalar margins,
three inclusive margins, and the exact gain $1/25000000$. Required
comparisons remain active under optimization.

**No missing premise or quantifier error was found in the application
of the declared analytic interface.** The result is the stated
import-dependent global parameter corollary at $0.87488666$, an exact
improvement of $4\cdot10^{-8}$ over the source's stated final boundary.
This review makes no literature-wide priority claim and no claim that
the upstream analytic hypotheses have been independently proved.
