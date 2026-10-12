# Bounded independent review of rapid collision decay and exact short transport

Status: complete analytic read ACCEPT for RD1–RD4 and SC2–SC5, with the
literal source factorization and tube identities explicitly identified below.
Scope: arbitrary polynomial suppression of one exact Mellin-tube component
of a norm-filtered source representation. Neither the complement nor the
complete signed moment is bounded here.
Exact sources in `../../literature/`: `SUBCRITICAL_RAPID_COLLISION_DECAY.md`,
SHA256 `a41b84b54f0e4052e6700887bad5cd82552ab452744f29c1b5f70e68cbf0735e`;
`SHORT_POLYNOMIAL_COLLISION_TRANSPORT.md`, SHA256
`c538719277b1e7de70a7e3f872fb2720668bd43ca57c9cffff6ff29b6766d5ac`;
`PRIME_SLOT_CANCELLATION.md`, SHA256
`d37ad696b46c7dda15a7faf314c46cda2d7d67e25ac8d3288c7f138aac373c13`;
and `PRIME_SLOT_SUBCRITICAL_TUBE.md`, SHA256
`5aca641b5c58e8d2efaf643c660d98cb5970235478bd9e0622e1d6014c4a1c28`.
The source field, actual character/nonunit conventions, incidence and smooth
weights remain those literal fixed upstream interfaces. Main integration of
those interfaces is attributed to the owning source reviewer.
What was actually run: complete mathematical read of RD, SC and the relevant
P/ST factorization/tube sections; no new finite coefficient or residue-symbol
checker, large source sum or Mellin integral computation.
Smallest remaining gap: the complementary independent-frequency trace.

## Positive Euler product and complete multiplicity

For a fixed number field, fixed FINITE forbidden-prime set S and fixed
`0<alpha<1`, the fixed-S ideal count gives `A_Y>>Y^(1-alpha)`. Expanding
its mth power groups all ordered m-tuples into product ideals of norm at
most `Y^m`, each with every prime factor norm at most Y. The restricted
factorization multiplicity is at most the complete `d_m`.

Its elementary subpower bound is valid for arbitrary prime powers. The local
binomial factor is at most `m^e` for e>=1, since assigning e labeled items
to m boxes dominates the number of weak compositions. Large primes pay
this by their delta norm power. At each of the finitely many small primes,
the local polynomial in e divided by that exponential has finite supremum.
Multiplying the finite constants gives the complete ideal divisor bound.

The finite reciprocal Euler product Z_Y contains every product ideal in
the expansion with positive coefficient one. Thus
`A_Y^m<=C Y^(m delta) Z_Y`. With `delta=(1-alpha)/2` and arbitrarily large
FIXED m, its inverse decays faster than each fixed power of Y. The constants
depend on field, S, alpha and requested power; no uniformity as alpha tends
to one or S grows with Y is inferred. Moving row/incidence prime deletions
are separately paid by the stated subpower norm weight.

The P/ST local factors retain actual multiplicative characters, conjugate
slots and zero values at nonunits. On the stated independent-frequency tube
the positive pair floor is literal, and its logarithmic quadratic error is
summable at `4sigma>1`; the cubic remainder is absolutely convergent at
`3sigma>1`. The rapid positive-product estimate therefore transports to
that tube, uniformly in its unrestricted central frequency and with all
moving deletions/rows retained. It does not apply to independent frequencies
outside that region or to the individual reciprocal factors.

## Exact norm-filtered truncation

The local collision series has coefficient `1-number_of_active_slots` at
each multivariate exponent, including coefficient one at zero. Its coordinate
exponents are all nonnegative. With finite Y and sigma>0, each geometric
series and their finite product converge absolutely, uniformly in all
imaginary parts at that fixed real contour. No infinite reciprocal-L product
or contour crossing is used.

The short T_i is exactly B_i's ideal-coefficient truncation to norm<=Y;
character nonunit zeros and excluded S/Q primes remain. Every collision
coefficient multiplies its column by an ideal of norm at least one. Hence
a removed B_i term of norm>Y cannot affect ANY final coefficient whose
i-th column norm is <=Y. This argument is at the ideal level, not merely
at numerical norms, so different prime ideals with equal norm are preserved.

The source norm test kills every column beyond `Y/Nc_i<=Y`. Complete
coefficient agreement therefore proves the filtered identity SC4 exactly.
Absolute series convergence and rapid vertical Mellin decay justify every
termwise inversion for each fixed finite Y. The two integrands can differ
pointwise and their separate tube integrals need not match; only their
complete norm-filtered integrals have the asserted exact identity.

## Tube and incidence coverage

Absolute ideal counting bounds each short polynomial by `C Y^(1-sigma)`,
uniformly in t and moving exclusions. Every physical scale costs at most
`D^sigma`, and D is comparable to Y, giving the complete product cost
`C Y^r`. Fixed smooth Mellin transforms are absolutely integrable with
polynomial frequency weights.

The RD6 row weight is paid by the full Schwartz lattice sum
`sum_(u!=0)|Phi(u/sqrt H)|(1+Nu/H)^epsilon0=O(H)` in the source's two real
dimensions. This retains the noncompact spatial row tail. Combined with
arbitrary fixed-power collision decay it bounds the exact short-representation
tube component per eligible allocation by `O_A(H Y^(r-A))`.

Every eligible shared-prime mask has `NQ<=Y^k`. Its primes can be assigned
to only a fixed finite number m of source subsets. For a squarefree mask
that assignment count is at most `d_m(Q)`. Summing the complete masks and
choosing the divisor exponent `delta=epsilon/k` gives
`O_epsilon(Y^(k+epsilon))` eligible allocations. Exterior literal source
factors have modulus at most one. Arbitrarily large A consequently pays
the entire incidence sum at every requested fixed power, as stated in SC7.

Verdict: ACCEPT for the exact filtered transport and negligible tube within
these interfaces. This review authenticates no new full source moment,
critical-sector cutoff bound, complementary trace contract, zero-free
boundary or RH result. The owner's finite coefficient controls have their
separate runtime/source reviewer and are not claimed as run here.
