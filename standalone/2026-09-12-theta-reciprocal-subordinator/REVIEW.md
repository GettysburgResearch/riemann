# Independent review request

This is a request to reconstruct the component arguments, not to supply an
omitted RH theorem. All statements retain proposed status until reviewed.

## Highest-risk mathematical points

1. **Counting convention and complement.** H sums one member of each +/- Xi
   pair, retaining both members of a conjugate nonreal pair and all analytic
   multiplicities. Check N(T)<=2T^2 from the F(v) Jensen bound, the lower endpoint
   in Abel summation, and both B0/B1 envelopes. The external census is only
   through30, but it MUST be complete; two numerical signs alone are insufficient.
2. **Two time ranges.** Re(a exp(-ta))=exp(-t Re a)[Re a cos(t Im a)+Im a sin(t Im a)].
   Check that all small-band terms are positive, and that the four rational
   budgets cover whole time intervals via monotonicity rather than sampling.
3. **Exact prime formula.** Check the factor two from the +/- divisor, the
   completion poles, gamma normalizer, Gaussian inverse Laplace scaling16t,
   and Fubini at the canceled u=0 endpoint. The pole and prime pieces separately
   have only the stated initial Laplace half-line; the full sum is continued.
4. **Probability construction.** Verify Levy integrability from the complete
   divisor, the Poisson small-jump construction, self-decomposability via
   H(t)-H(t/c), and shape/RATE conventions in the gamma split. S_tau is not the
   original theta random variable.
5. **The remaining property.** Complete monotonicity of H is NOT proved. The
   Stieltjes characterization would exclude nonreal poles of A'/A; ordinary
   Bernstein/infinite divisibility does not. Check the exact -8 synthetic
   cumulant witness and factorial-index conventions before using the positive
   infinite towers. PR379's all-center quantifier is not discharged at one center.

## Finite numerical review

The code evaluates the literal n=1,...,4 theta terms at4097 Simpson nodes on
[0,2], uses an integrated fourth-derivative Peano bound, and pays every omitted
index and the whole physical tail. Check Machin truncation signs, outward integer
rounding, exponential underflow enclosures, interval inputs, cosine half-angle
recursion, and both endpoint weights. The displayed decimals do not replace
the stored primitive reconstruction. Normal/optimized and two-mesh comparisons
are same-author/same-backend checks, not independent implementation review.

## Inputs that remain imported or unreviewed

The Platt--Trudgian published theorem is used but not re-proved or rerun. The
classical entire-xi product, Jensen, Bernstein representation and Laplace
uniqueness have their ordinary hypotheses stated. No theorem is imported from
the related reciprocal-xi preprint discussed for historical orientation.

The original cumulant-index, finite-jet and ferromagnetic manuscripts are not
newly accepted by this continuation. The new proof does not depend on an
existing unweighted numerical Hankel certificate, an Ising fit, a spectrum of
the old nonnormal theta operator, or a global phase/zero-confinement claim.

## Smallest failure that would invalidate the main new conclusion

A wrong whole-tail bound or an incomplete low-height centrality premise would
invalidate HTP1, and consequently the positive Levy interpretation. A wrong
factorial-to-cumulant normalization would invalidate HTP4. Failure to prove
complete monotonicity DOES NOT invalidate these narrower results: that stronger
statement is explicitly open. A hypothetical off-line zero is compatible with
the positive/decreasing central trace, as the mechanism explains.
