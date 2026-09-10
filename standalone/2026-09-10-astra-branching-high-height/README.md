# BHH26 — every finite branching depth is eventually critical-line simple

**Proposed complete component proofs; independent mathematical review required.
RH and confinement in the remaining bounded windows are NOT proved.**

This add-only continuation starts from PR #857 at
`3f1984867d23b588d09c88a892882411724b174b` and keeps its literal
Gamma(5/2, rate 5/2) shared-uniform branching orbit, reflected Mellin function
H_n, and entire representative E_n.

## Positive theorem

For EVERY finite depth n, an explicitly generated integer T_n has the property

```
H_n(s)=0, 0<=Re(s)<=1, |Im(s)|>=T_n
    ==> Re(s)=1/2 and the zero is simple.
```

The same holds for E_n. Thus each finite depth has only finitely many possible
off-central critical-strip zeros, and infinitely many simple central zeros.
The fixed-depth count is

```
N_n(R) = (R/(2pi)) log[pi R/(30 e 4^n)] + O_n(1).
```

The coefficients, onset and error are NOT uniform in depth. For orientation,
the conservative first cutoffs are 320, 279109, 1788260812445057, and
3097471590717602242860533234898291413963. They are outputs of analytic bounds,
not completed numerical zero censuses.

## Mechanism

A finite distributional derivative of the compact gamma-mixing law consists
of known atoms plus a bounded-variation density. Beta averaging squares only
the diagonal atom coefficients; all mixed terms stay in the density. The
common uniform scale produces an integer recurrence

```
u_(n+1,j)=u_(n,j)^2-2u_(n,j-1)^2, u_(0,0)=1.
```

The leading polynomial P_n(z)=sum u_(n,j)^2 z^j has all roots in |z|<=1/4.
An exact Mellin decomposition retains the WHOLE BV remainder with explicit
O_n(1/|Im s|) value and derivative bounds. The gamma factor then forces a
strictly positive modulus-ratio derivative above T_n, where it is valid to
apply that criterion. The previously certified negative derivative at depth
one and height 23 is unaffected.

This is not a claim that positive coefficients alone give zero-free actual
transforms, that the remainder is zero, or that the leading polynomial is xi.

## Read and replay

Read PROOF.md Sections 2–5, then REVIEW.md, SOURCES.json and VALIDATION.md.

```bash
python -I -S -B check.py --check result.json
python -I -S -B -O check.py --check result.json
python -I -S -B test_check.py
python -I -S -B -O test_check.py
```

The standard-library checker uses integers and exact fractions. It reconstructs
finite derivative-measure identities, full mixed beta moments, uniform-scale
endpoint/interior terms, leading polynomials and threshold arithmetic.
It does not evaluate any zeta function, actual zero, contour, or infinite
operator. It does not machine-prove the all-depth analytic theorem.

## Remaining RH obligation

Parent E_n converges locally uniformly to xi. The new good regions are ABOVE
T_n. To infer RH one still needs bounded-window confinement along unbounded
depths, or another independently proved cofinal zero theorem. The windows
below T_n grow quickly. Finite exceptional counts do not imply zero exceptions.
The needed theorem is not assigned to reviewers as routine work.

Classical beta–gamma, BV, polynomial root and gamma-asymptotic mechanisms are
credited. No external priority claim or independent acceptance is asserted.
