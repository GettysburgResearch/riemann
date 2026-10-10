# Independent review of the subset-product incidence bound

Reviewer: `/root/audit_formalization`, an independent analysis agent in this research pass. Date: 2026-10-10.

**Verdict:** the new deductions pass this scoped mathematical review, conditional on the stated imported sieve and, where used, the uniform pointwise/native-second-moment inputs. No mathematical revision is requested. This is an agent source-and-proof review, not journal peer review, a Lean proof, or an independent reconstruction of every imported analytic theorem.

## Exact reviewed artifact

- File: `balanced/SUBSET_PRODUCT_INCIDENCE.md` in the research authoring directory; the publication may copy these exact bytes to its packet root.
- Size: 19,942 bytes.
- SHA-256: `9d62a79c0074c7506d273ff7203807e4efd054bfdf0b85baddf340304da4f3de`.

The review binds the entire note at this hash, including its stated limits. I read all seven sections and checked the displayed deductions against the pinned interfaces named in the note. Published source packets were not edited. The earlier all-row squarefree-column sieve is retained as an input; its whole proof is not rerun here.

## 1. Whole physical product, including collisions

Lemma 2.1 correctly uses the unique shared-prime incidence decomposition before the squarefree-column sieve. Once all shared ideals are fixed, the remaining singleton product is squarefree and its coefficient is independent of the row. Its squared coefficient mass is bounded by its product length times a fixed-order divisor loss. The exterior repeated-prime character factors have modulus at most one, including their nonunit zeros.

The three norm-level shared-ideal exponents are respectively \(|I|/2\), \(|I|\), and \(5|I|/6\). Only the first, at pair incidences, is harmonic. All other displayed sums converge or have a fixed finite horizon. Thus the full product estimate
\[
HP_J+H^{1/6}P_J^2+H^{2/3}P_J^{5/3}
\]
follows by Minkowski with a small-power loss. A squarefree-column theorem is not being applied directly to a product with repeated primes. Bounded nonempty scales below one are correctly included by the fixed support lower bounds.

## 2. Critical forward correction and moving masks

The local factors in (3.2) are the correct forward correction from independent inverse polynomials to the pairwise-coprime, masked core. At a good prime away from the mask, the coefficient of a nonconstant monomial is one minus its support size; at a mask prime it is one. Complete multiplicativity with zero extension gives the finite identity (3.3), even when a row prime divides one of the correction indices.

Lemma 3.1 does not claim absolute convergence at several critical weights \(1/2\). The finite horizon permits a shift by any fixed \(\delta>0\), at cost at most \(Z^\delta\). After the shift, every good-prime mixed term has total exponent greater than one. The moving mask costs \((NC)^\eta\), uniformly for polynomially bounded \(NC\). Choosing both margins in terms of the final epsilon proves the claimed small-power bound. No inverse factor with denominator \(1-k/\sqrt{Np}\) appears, so no unmentioned small-prime enlargement is needed.

## 3. Subset estimate and quantifiers

For a fixed subset \(J\), applying the whole-product estimate on \(J\) and the pointwise bound on its complement gives the three norm monomials in (4.2). Their correction weights are \(1/2,1,5/6\) on \(J\), and \(b\) outside it. Each is at least \(1/2\), so the finite-horizon lemma applies to all three with the same moving mask. Squaring gives exactly
\[
HP\left(\frac{P}{P_J}\right)^{2b-1}
\left[1+\frac{P_J}{H^{5/6}}+
\left(\frac{P_J^2}{H}\right)^{1/3}\right]
\]
up to the stated small-power loss.

Two necessary quantifiers are present: the physical row range remains fixed throughout every shortening, and the subset \(J\) is chosen for the original rectangle and held fixed within its convolution proof. The note does not substitute a theorem known only on the curve \(H=Y^h\). The new subset estimate needs the uniform pointwise input when \(J\) is proper. The optional native one-axis estimate additionally needs (NM2), in its original allowed height range. The whole-set choice needs neither of those extra inputs.

## 4. Exact sixth-moment example

The pair-incidence triangle at \(h=21/20\), \(b=7/8\) has three singleton scales \(D^{7/12}\), total product \(D^{7/4}\), and two-axis product \(D^{7/6}\). I recomputed the exponents:

- Native one-axis loss: \(7/8\).
- Whole classical loss: \(\max(0,7/8,49/60)=7/8\).
- Two-axis classical loss: \(\max(0,7/24,77/180)=77/180\).
- Remaining pointwise axis: \(7/16\).
- New loss: \(623/720\), a saving of \(7/720\) against both former displayed estimates.

Summing all three shared-ideal dyads costs \(D^{5/4}\) at squared-norm level; multiplying by singleton product \(D^{7/4}\) gives the correct \(D^3\) normalization. The claimed bound is therefore for an actual full incidence portion, not one frozen shared tuple. Full common gcd one is compatible with the construction. The comparison is between proved upper estimates; the note correctly makes no lower-bound claim about the true norm.

For the perturbed optional \(b\), the new/native gap is positive exactly under the stated sufficient condition \(2b-1>11/15\). The example does not attain the diagonal sixth-moment target.

## 5. Aggregation and signed residual

The selector in Theorem 6.1 depends on complete shared-incidence blocks. It does not truncate individual singleton sums, so the core theorem remains applicable. The sum of square roots of the product lengths is bounded by \(D^{k/2}\) times harmonic pair-incidence logarithms. This proves the threshold-uniform bound \(HD^k L\), with its stated small-power loss.

The residual construction uses the sharp-row triangle inequality before smoothing the full residual squared norm. That order is important: the selected part only needs its sharp-row estimate, while the residual is expanded under the smooth nonnegative majorant. The imported positive conductor accounting survives the restricted tuple domain, and the remaining Hermitian term is real. Its lower bound by minus the controlled part follows from positivity of the residual norm. No monotonicity of a signed sum under restriction is presumed.

Integrating the pointwise upper inequality gives excess \(\max(\lambda,e)\), provided the stated one-sided signed integral bound holds at all dyadic scales with every required epsilon loss. The zero-free expression in (6.5) remains conditional on this open arithmetic estimate and on the fixed-detector extraction interface. It is not a new zero-free theorem.

## 6. Limitations retained

The all-order finite optimization is algebraically correct. For the top-scale balanced core \(x=1\), \(1<h\le11/10\), \(b=7/8\), every proper multi-axis alternative has the displayed nonnegative additional loss relative to the native one-axis choice. Thus the new argument genuinely enlarges some controlled incidence strata, but does not automatically improve the hardest balanced core or the full moment. It proves neither the required signed average nor the cofinal moment hierarchy.

No numerical experiment, build, kernel proof, or external publication review is claimed by this report. The review is bound to the source bytes above; later edits require renewed assessment of the changed claims.
