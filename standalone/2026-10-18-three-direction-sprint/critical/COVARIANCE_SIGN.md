# A complete directed sign change in the actual mixed covariance

Status: **finite primitive-source certificate, not an asymptotic bound.**
This tests the original signed fourth-order covariance directly. It does
not climb a moment ladder, estimate its limiting exponent, or prove an
improved zero-free region. It rules out an exact universal one-sign
identity for the displayed admissible profiles and parameters. It does
not refute a statement restricted to all sufficiently large scales.

Work in Z[omega], omega^2+omega+1=0, with every good integral ideal
represented by its generator a+b omega congruent to1 modulo3. Use the
literal sextic symbol chi_A(u)=(u/A)_6, with its original zero extension.
Let W(x)=exp(4-1/((x-1)(2-x))) on 1<x<2 and zero elsewhere. This is one
fixed smooth compact profile. Put U=D=1024,N=32 and

    M_t(u)=sum_d mu(d) (Nd)^(-1/2-it) W(Nd/D) chi_d(u),
    S_t(u)=sum_n       (Nn)^(-1/2-it) W(Nn/N) chi_n(u).

The physical rows are EVERY good sixth-free u in U<Nu<2U, with weight
w_u=W(Nu/U). The missing boundary values have zero weight. The powers
of n and all shared primes are retained. These profiles have the same
central normalization as D^(-1/2),N^(-1/2) after absorbing x^(-1/2)
into their fixed smooth input profiles. The common height is t.

Expand E_t=sum_u w_u |M_t(u)S_t(u)|^2 in the ORIGINAL four inputs.
Let E_D be its entire d1=d2 strip, E_N its entire n1=n2 strip, and E_DN
their intersection. Exact inclusion-exclusion gives

    C_diff=E_t-E_D-E_N+E_DN,

the complete sum with d1!=d2 AND n1!=n2. After collapsing A_i=d_i n_i,
the good primitive pair conductor is

    C(A1,A2)=product_(p: ord_p A1-ord_p A2 !=0 mod6) Np.

Common primes with equal character exponent remain zero-only row masks;
they do not disappear from the character evaluations. Let C_high be the
complete part of C_diff with C(A1,A2)>U^(9/8). The directed certificate
gives the strict enclosures

    -0.013092 < C_high(t=0)  < -0.013090,
     0.018834 < C_high(t=10) <  0.018836.

Thus this actual remainder has both signs as the legal common height
changes. An absolute or one-sided size estimate allowing positive values
is still required. No sign assumption is inserted into the zero-free
consumer on the strength of a numerical trend at height zero.

## Complete primitive coverage and arithmetic contract

`covariance_sign_check.py` enumerates EVERY good ideal through norm 2048
in primary generators. An independent enumeration of all omega-stable
Hermite normal form lattices checks the inventory bijectively. Exact
prime ideal division authenticates every factorization and Mobius value.
Finite-field exponentiation gives every prime sextic character as an
integer phase code, including the nonunit code. Multiplication builds
all composite symbols; every collapsed-product representation is checked
against the original two input phase arrays.

The full input has 294 inverse terms, nine plain terms, 2,646 original
pairs and 2,514 collapsed products on 312 complete physical rows. The
good pair conductors are assembled in an exact int64 matrix with an
explicit no-overflow gate. Division prime by prime implements their
exact valuation formula. The threshold is the integer 2,435, determined
by C^8<=U^9. No floating logarithm selects or excludes a pair. Each
selected upper-triangular conductor is additionally checked by direct
integer prime-valuation multiplication.

There are 13,818 upper-triangular selected pairs. Their row kernels are
computed by exact integer phase counts at each row norm, followed by
outward Arb/acb multiplication by the actual profile weights. The full
E_t and both COMPLETE strips are computed directly from the actual
polynomials at every row. Their complement is exact subtraction of the
whole low-conductor sector, so no high-conductor pair is omitted.

For each low-conductor pair, its coefficient is the collapsed outer
product minus the original same-d and same-n record products, plus their
intersection. This keeps the full coherent cross terms, even when
different factorizations give the same collapsed product. Off-diagonal
conjugate pairs contribute twice their real part. The diagonal is retained.

All character arithmetic, inventories, zero masks, phase bins and
conductor gates are exact integers. All transcendental values, products
and sums use python-flint0.9.0 Arb/acb at 192-bit outward precision.
NumPy is used ONLY for exact bounded integer arrays, finite indices and
integer phase counts; no NumPy floating or BLAS result enters a sign.
The saved record binds the raw producer source and exact character and
conductor streams. Every strict sign gate remains active under Python-O.

To reconstruct the primitive computation, with python-flint0.9.0 in
the supplied dependency directory and NumPy installed, run

    python covariance_sign_check.py --dependency-dir PATH --check COVARIANCE_SIGN_CHECKS.json
    python -O covariance_sign_check.py --dependency-dir PATH --check COVARIANCE_SIGN_CHECKS.json

`--check` first reruns ALL primitive calculations, then compares the
complete record. It does not accept the saved signs as input evidence.
This certificate is distinct from the earlier ordinary-floating scouts;
those scouts suggested the test but are not its proof.
