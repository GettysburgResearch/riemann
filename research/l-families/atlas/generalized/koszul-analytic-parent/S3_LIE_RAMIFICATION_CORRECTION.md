# The actual S3 Lie parent has ramified PBW factors with branching

Status: proposed exact local-source theorem, using the canonical graded
modules of [MATHEMATICS.md](MATHEMATICS.md) and the actual S3 cover of
[S3_RAMIFICATION_AND_GRADED_FAMILY.md](S3_RAMIFICATION_AND_GRADED_FAMILY.md).
This is a companion to the global arithmetic Lie completion. It concerns
the exponentially growing modules M_n, not the polynomial-growth Segre
grades R_n. The construction, PBW identity and finite-cover formalism are
classical inputs; no external priority or arithmetic RH claim is made.

The point of the calculation is that taking inertia invariants of each
Lie-parent module does not produce the averaged Hilbert series of the
original invariant Segre algebra. The actual Artin local factors must use
the former operation. Their difference is already visible in degree two,
and it persists as fractional local monodromy.

## 1. Source-defined local factors

Write s for a transposition and c for a three-cycle. The frozen source has

    F_e(z)=(1+2z)/(1-z)^4,
    F_s(z)=(1-z^2)^(-2),       F_c(z)=(1-z^3)^(-1).

Let M_n be the degree-n dual homotopy-Lie module, with its actual S3 action,
and put epsilon_n=(-1)^(n+1). These modules are defined before their scalar
series. Equivariant PBW gives

    F_h(z)=product_(n>=1) det(1-z^n h | M_n)^(-epsilon_n).       (1.1)

For an inertia subgroup I and a Frobenius lift phi normalizing I, define

    S_(I,phi)(z)
       =product_(n>=1) det(1-z^n phi | M_n^I)^(-epsilon_n).     (1.2)

This is the actual signed Artin local product, evaluated with one grading
variable. At a closed point of degree d, its argument is z^d. Since
dim M_n is asymptotic to 2^n/n, all determinant logarithms in (1.1)--(1.2)
converge absolutely for |z|<1/2. The displayed products are nonzero there.
The invariants in (1.2) are taken grade by grade on the full source; no
inertia-invariant input substitution is made.

The fact that M_n is the dual of a Lie grade causes no problem: finite-group
invariants commute with duality, and (1.2) uses its specified representation.
No Lie bracket on the dual spaces themselves is asserted.

## 2. Transposition inertia gives a dyadic equation

Put S_2=S_(<s>,1). On M_n, let a_n and b_n be the +1 and -1 multiplicities
of s. If D(z)=product(1-z^n)^(-epsilon_n b_n), then

    F_e(z)=S_2(z)D(z),
    F_s(z)=S_2(z)D(z^2)/D(z).

Eliminating D gives the exact germ identity

    S_2(z)^2 / S_2(z^2) = F_s(z) F_e(z) / F_e(z^2).          (2.1)

The normalizer of a transposition subgroup in S3 is that subgroup itself.
Consequently the finite ramified Frobenius acts trivially on M_n^I, even
when a chosen lift is s. Thus S_2 is the required finite-branch local
factor for this source, rather than merely an identity-Frobenius example.

At z=-1/2, the factors S_2(z^2), F_s(z), and F_e(z^2) are analytic and
nonzero. F_e has a simple zero there. Equation (2.1) therefore continues
the source germ to a slit neighborhood in the form

    S_2(z)=(1+2z)^(1/2) U_2(z),                             (2.2)

where U_2 is analytic and nonzero. The branch is selected by continuation
from the initial disk. This is not a meromorphic local germ at -1/2.

## 3. Three-cycle inertia gives a triadic equation

Put S_3=S_(<c>,1). The two nontrivial c-eigenspaces have equal dimensions
in every M_n: a transposition interchanges them. Let B(z) be the product
associated with either such eigenspace. Then

    F_e(z)=S_3(z)B(z)^2,
    F_c(z)=S_3(z)B(z^3)/B(z).

Hence

    S_3(z)^3 / S_3(z^3) = F_c(z)^2 F_e(z) / F_e(z^3).       (3.1)

Exactly as above,

    S_3(z)=(1+2z)^(1/3) U_3(z)                             (3.2)

on a slit neighborhood of -1/2, with U_3 analytic and nonzero. This is
the infinity factor when Q is 1 modulo 3.

When Q is 2 modulo 3 the actual infinity Frobenius has transposition
coset. Write S_(3,s)=S_(<c>,s). Each standard S3 summand contributes one
+1 and one -1 eigenvalue to s, but has no <c>-invariants. Thus

    F_s(z)=S_(3,s)(z) B(z^2),
    S_(3,s)(z)=F_s(z) [S_3(z^2)/F_e(z^2)]^(1/2).            (3.3)

The square-root branch in (3.3) is the germ with value one at zero.
This factor is regular at z=-1/2. Its first fractional singularities
occur at z^2=-1/2, where its local exponent is (1/3-1)/2=-1/3.
The Frobenius coset is therefore load-bearing for the analytic boundary,
as well as for the finite local traces.

## 4. The discrepancy is visible before any limiting operation

The source has

    M_1 = 1 + sgn + 2 std,
    M_2 = 1 + std.

These identities follow either from the already constructed low-degree
modules or from equivariant PBW through degree two; the replay checks them
against the frozen source. They give the following exact comparison:

| Inertia and Frobenius | Actual Lie-parent product through z^2 | Averaged Segre Hilbert series through z^2 |
|---|---|---|
| <s>, identity on invariants | 1+3z+4z^2 | (F_e+F_s)/2 = 1+3z+10z^2+... |
| <c>, identity on invariants | 1+2z+2z^2 | (F_e+2F_c)/3 = 1+2z+6z^2+... |
| <c>, transposition coset | 1+0z+0z^2 | F_s = 1+0z+2z^2+... |

The two constructions agree in degree one and differ in degree two. An
invariant Koszul complex remains exact, but its full tensor terms must be
retained. Replacing that complex by the PBW product of the invariant Lie
pieces is another operation. Neither exactness of the original complex nor
the unramified scalar identity (1.1) identifies the two columns above.

## 5. Explicit propagation of the local branch points

For d=2,3, let F_(c_d) mean F_s or F_c. Solving (2.1) or (3.1) at zero
gives

    log S_d(z)
      = (1/d) log F_e(z)
        + (d-1) sum_(j>=0) d^(-j-1) log F_(c_d)(z^(d^j))
        - (d-1) sum_(j>=1) d^(-j-1) log F_e(z^(d^j)).       (5.1)

Initially this is an identity on |z|<1/2. It follows by iterating the
functional equation; the remainder d^(-J)log S_d(z^(d^J)) tends to zero.
On every compact subset of |z|<1, all sufficiently late terms in (5.1)
converge normally. The finitely many earlier logarithms may be continued
along paths avoiding their zeros and poles.

At any root of 1+2z^(d^j), exactly one indicated F_e term vanishes: the
different j have different radii. The F_(c_d) have no zeros or poles inside
the unit circle. The local exponents are therefore

    1/d                    for j=0,
    -(d-1)/d^(j+1)         for j>=1.                       (5.2)

All are nonintegral. Their reduced denominators are unbounded, so no fixed
finite-degree branched cover of the disk can make S_d meromorphic at all
these points: a local ramification degree must be divisible by the reduced
denominator to make the exponent integral. The branch points accumulate
densely on |z|=1. This records a precise obstruction to finite ramified
repair; it is not a claim that S_d is a single-valued meromorphic function
throughout the punctured unit disk.

## 6. Relation to the global arithmetic construction

At unramified points the local parent is F_Frob(z^deg). At the finite
branches and infinity the correct factors are (2.1), (3.1), or (3.3).
These corrections are derived from actual inertia and Frobenius on M_n.
They are not fitted scalar multipliers designed to restore a preferred
functional equation.

The companion global theorem constructs the finite cohomology groups of
these same M_n, proves the sharp operator domains, and determines which
local branching survives global recombination. Local branching alone would
not prove a global obstruction, since different factors can cancel. The
global nonintegral exponent is checked separately from actual source point
counts. No passage from this function-field construction to the complete
native number-field family is asserted.
