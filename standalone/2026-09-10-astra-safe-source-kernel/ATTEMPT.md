# Full-problem attempt and remaining obligation

Status: proposed research, not an RH proof or independent acceptance.

## What changed

The parent target compared the actual future output with the complete old
response and the input. Raw future transmission is unbounded, so dropping the
old-response term cannot work. I retained it, tested exact exponential inputs,
and multiplied out the inverse-zeta factors BEFORE taking any norm estimate.

The first odd activation occurs at 3. The source before log3 is therefore
explicit. This converts the full future input into an entire numerator b_r
and makes kernel positivity a global analytic continuation mechanism. The
new forward implication does not need to recover all discrete small forcing
columns from a nonuniform continuum approximation.

The most useful final form is AC28-7: one inequality on (0,1) and (1,3) for
all odd polynomials, with a fixed positive arithmetic dilation measure.
It has no growing cutoff parameter except polynomial degree, and no unknown
zero or reciprocal-zeta singularity in its primitive data. Arbitrary degrees
are necessary; there is no claim that a finite matrix settles RH.

## Attempts made, including failures

1. Finite Euler products seemed a possible source of positive factorizations.
   They fail for EVERY finite prime set: the numerator a_P has an artificial
   zero at z=1/2 because a finite product cannot cancel the pole at s=1.
   The same direct kernel argument detects this obstruction. Four exact
   negative determinant controls are retained.

2. Scalar positive bounds do hold for the true source. AC28-4 proves them on
   the ENTIRE safe real axis at eta=0,C=4. Yet no finite C can give all-order
   positivity at eta=0, by classical critical zeros. Thus the next step must
   be a genuinely polarized inequality, not better scalar estimates.

3. Positive dilation of the derivative gives an unconditional all-degree
   norm-equivalence: ||Q_p'-p'|| <= (4/5)||p'||. This is a valid result but
   uses the unweighted derivative. Weighting by t changes the dilation norm
   from n^(-3/2) to n^(-1/2); the absolute norm sum diverges. I did not use
   the unweighted estimate as a substitute for the missing critical norm.

4. The exact one-pole comparison can pay a boundary-resonance cost C_eta
   proportional to 1/eta through a sum of squares. It is a NONNATIVE model.
   Assigning a sum of such independent modes to the actual arithmetic source
   without a completeness/domain/cross-term theorem would not be a proof.

5. Non-directed mpmath eigenvalue scouting selected the final finite tests.
   Those signs are not used as mathematical certificates. The submitted
   finite evidence is regenerated with directed rational intervals and two
   independently structured source and matrix computations.

## What a complete proposal would have to add

Prove, for the literal operator Q_p and EVERY complex odd polynomial p,

    ||E_p||_(1,3)^2 <= eta||p||_(0,1)^2+C_eta*4||tQ_p'||_(0,1)^2,

with finite C_eta independent of degree, for positive eta tending to zero.
Equivalent acceptable output: a bounded source-faithful contraction S mapping
phi_z to psi_z on a fixed safe interval, or an exact positive Gram/sum-of-
squares factorization at every order. Such a theorem would yield the global
zero-free strip directly by AC28-3 and close RH.

Potential point of leverage, NOT an obtained estimate: isolate the t=0
weighted boundary from the positive dilation operator. The unweighted
Neumann-series inverse is controlled; the weighted prediction must exploit
cancellation between Q_p(1) and the COMPLETE dilation tail on (1,3), rather
than bounding them separately. Uniform estimates for the endpoint and the
tail independently are not asserted. The finite-prime failure requires an
infinite-source-faithful cancellation mechanism, not an uncorrected truncation.

No actual all-degree estimate, uniform factorization, or zero-free-region
improvement was obtained. Q-AC26 and its subpower-defect version remain OPEN;
this new direct sufficient target is also OPEN. The proved links explain
exactly what an eventual positive theorem would buy, not that it has been
found. Earlier proofs, counterexamples, and source-status boundaries remain
unchanged.
