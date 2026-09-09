# What the closing attack did and did not establish

Status: the full RH proof is NOT obtained. The component theorem TRG26 has a
complete proposed proof in PROOF.md and remains subject to independent review.
This note records the attempted composition, not an omitted lemma assigned to
future reviewers. Date: 2026-09-09.

## 1. Why this problem was chosen

The recent sources solve several genuinely different tasks. PR803 now encloses
full native residual norms uniformly over coefficient spaces, but its later
norm-transfer packet also constructs exact balanced variations showing that a
coefficient-uniform divisor-to-physical comparison costs order Y/log Y. PR825
controls the centered graph inverse by O(log log P). PR828 gives the exact
anchored root cost on product reservoirs and notes that this does not determine
the centered all-support gap. The prospective integration #830 preserves these
qualifications rather than making the source norms identical.

I tested the remaining optimistic graph argument: perhaps centering removes all
slow behavior, so the constant gaps of the product models can be used after an
arbitrary divisor-closed cutoff. TRG26 proves this inference false and determines
the sharp centered order. It also supplies a positive replacement: on its actual
union supports only one nonconstant mode deteriorates; after retaining it the
rest has the fixed gap (3/2)log 2.

This is not a changed zeta function. The supports are legitimate examples in the
all-support theorem's own class and retain every allowed arithmetic edge. They
are NOT the ordinary interval supports {1,...,N}. No conclusion about that
narrower family's asymptotic gap is drawn.

## 2. The new reduction is complete for its stated graph

The full graph's first eigenvalue is the unique root of the monotone scalar
function (7). The explicit finite resolvents in (11) reconstruct its eigenvector.
A global sign perturbation of this graph can therefore retain constants and the
slow contrast as two coordinates, with the remaining inverse bounded by 1/g0.
All couplings must still be included in its Schur complement.

That reduction cannot by itself be called a reduction of the Weil form or of the
floor residual. In particular, (i) a positive divisor gap is not an upper bound
for an affine approximation error, (ii) matching divisor identities do not
identify two Hilbert metrics, and (iii) the remaining two-coordinate form is not
positive merely because its eliminated complement is positive.

The root masses in this pass illustrate the danger concretely: counting the
shared root twice would remove the +lambda h correction in (9) and produce a
wrong secular equation. Our bounded algebra tests cover that correction and
also the simultaneous-zero case that naive Dirichlet inversion would lose.

## 3. Exact end-to-end conditional route still available

Let e(x)=pi(x)-Li_2(x), with Li_2(x)=integral_2^x du/log u and e(2-)=0. A
sufficient arithmetic theorem remains

    K=integral_2^infinity e(x)^2 dx/x^2 <infinity.             (OPEN)

Here is the closing implication, to keep its dependence explicit. Assuming K
finite, the function

    C(s)=s integral_2^infinity e(x) x^(-s-1) dx

is analytic for Re s>1/2, by Cauchy--Schwarz applied to e(x)/x and x^(-s),
uniformly on compact subsets. On Re s>1, ordinary partial summation gives

    C(s)=sum_p p^-s-integral_2^infinity x^-s/log x dx.

Put a=log2 and

    B(s)=-gamma_E-log a+Ein((s-1)a)-2log s,
    V(s)=sum_p sum_(k>=2)p^(-ks)/k.

V converges absolutely locally on Re s>1/2. B is analytic there with the
right-half-plane branch of log s and entire Ein. In the Euler half-plane,
exp(B+C+V)=(s-1)zeta(s)/s^2. Analytic uniqueness extends the identity to the
half-plane Re s>1/2. The left side is never zero, and the zeta pole at 1 is
removable in the right side. Thus (OPEN) would imply RH by reflection.

This argument constructs a logarithm from an assumed energy bound; it does not
assume one across hypothetical zeros. The unproved input is K finite. Neither
TRG26's eigenvalue asymptotic nor its full complement inverse establishes K.
The conditional Cramer upper estimate in the earlier cutoff-taper packet cannot
be invoked here without already assuming RH.

Equally, the native-residual route still needs actual growing-prefix completions
with subpower full physical error. A coefficient-uniform graph comparison cannot
supply it, by ANT3/ANT4 in the inspected #803 source. A specially selected
minimizer could behave better; this pass does not bound that minimizer.

## 4. What is and is not new or independently checked

The arithmetic union construction, exact two-reservoir secular equation, the
sharp centered all-support order and the absolute gap after one additional
mode are the new proposed components. The proof rederives its needed box spectrum,
Euler mass bound and squarefree root asymptotic, so its new lower construction
does not rely on accepting an unread analytic statement from another branch.
The matching all-support upper order is a rederivation of the older path method,
with a looser constant, not a separate new theorem claimed for priority.

The latest #803 comparison proof was inspected through its definitions and
uniform upper comparison; the explicit sharp variation and later evidence are
used only at the scope stated in its author PR, not newly accepted here. The
review #827 and integration #830 were read at metadata/orientation level. Their
source qualifications are not additional mathematical hypotheses of TRG26.

No proof or Lean formalization of Navier--Stokes was analyzed in this pass. The
OpenAI research index dated September 8, 2026 confirms an announcement of a
proposed solution; it is not evidence for any assertion about Riemann zeta.

The packet should be sent for review of the graph theorem and its exact scope,
not presented as a completed proof of RH. No new zero-free region, evaluated
intrinsic entropy, or unconditional critical prime-error exponent is claimed.
