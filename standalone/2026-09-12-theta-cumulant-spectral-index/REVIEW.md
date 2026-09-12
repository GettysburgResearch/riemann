# Independent-review request

This is NOT a complete RH proof. The purpose of review is to check the component
claims and the finite source certificate. OPEN-CSI is not assigned to reviewers
as an omitted routine lemma.

## Load-bearing proof checks

1. The actual normalization is mu_(2k)=integral t^(2k)phi/Xi(0), WITHOUT variance
standardization. Reconstruct F(v)=Xi(sqrt(v))/Xi(0), the genus-zero product,
q_n=(-1)^(n+1)kappa_(2n)/(2(2n-1)!), and the Newton signs. No quadratic entire
factor or missing multiplicity may be inserted or dropped.
2. Check CSI1 for an INFINITE possible nonreal divisor. The outer interpolation
set includes every node outside a radius, not just the selected exceptions.
The omitted tail is bounded in ABSOLUTE value and may contain complex nodes.
Verify (7)--(10) and the distinction between analytic multiplicity and inertia.
3. Check that the positive cyclic space is explicitly CONDITIONAL. Its spectral
weights are m lambda, so cyclic eigenvalues are simple even at a multiple Xi
zero. The full multiplicity is in the logarithmic-derivative residue. Do not
replace the stated resolvent identity by det(I-vA)=F or a bounded similarity to
#834's nonnormal operator.
4. In CSI2, check the monomial shift, cyclicity, and the special last moment
k=2n-1. The finite positive rational resolvent is not necessarily an entire
partition function: its integrated pole weights need not be integers.
5. The only proposed RH conclusion is conditional on OPEN-CSI at EVERY degree.
No finite principal-matrix sign, closure of a smaller test family, or generic
positivity of w substitutes for that assertion.

## Computer-assisted finite claim

Reconstruct the source polynomials through order64 by a second method; the tests
use formal exponential composition. Check midpoint Taylor Peano remainder,
L1 derivative bounds, both complete tail constants, normalized moment division,
Newton recurrence versus ordinary cumulants, diagonal scaling200^k, and interval
LDL positivity. A large-argument exponential is bounded as an ENTIRE derivative
before rounding, to avoid underflow magnification. All128 cells, all eight
retained terms and all infinite tails must remain.

The output encloses moments through36 and certifies two9x9 forms. It does not
find zero locations, prove a new high-height zero-free region, certify a finite
Ising realization through36, or establish all-order positivity.

## Relation to other work

#842 supplies the ten-moment graph and local directions. #854 already reaches
twelve moments and proves a specific first-order coupling failure and a global
independent-spin obstruction. No stronger finite graph is claimed here.
#839 supplies the antecedent full complex-tail positivity criterion and #841
the shifted moment formulation and original4x4 certificate. #858 has the antecedent finite-exceptional-index argument; its thresholds and
number of exceptional roots are not used as uniform inputs for xi. #834 gives
the trace-coordinate motivation, but the whole-source argument is rederived
without assuming its determinant theorem or any bounded symmetrizing metric.

The classical origin of these mechanisms must remain credited. Review should
not promote this source-specific synthesis into a novel general moment criterion
or an unconditional proof of the displayed open inequality.
