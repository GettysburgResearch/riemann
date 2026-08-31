# One certified central top class completes the marked source resolution

This is a new theorem-guided validation implication. It does not report
a successful degree-seven computation. It does not amend the older
full-kernel contracts, their bounds or tests. In particular, validating
the witness described below is not an execution of the old776-vector
kernel census or the old775-column global rank calculation.

The object is the same characteristic-zero marked Chow module

    V=Q^3, W=Sym^3(V), S=Sym(W), m=S_{>0},
    R=direct_sum_j (Sym^j V) tensor (Sym^j V) tensor (Sym^j V).

The ten variables of S act by the literal symmetric orbit sums. All
modules, maps, coordinates and torus weights below refer to that source.

## Frozen dependencies and their separate roles

All paths in this table are relative to
research/l-families/atlas/generalized/segre-hadamard-source/.

| Role | Commit | File | Git blob |
| --- | --- | --- | --- |
| Source finiteness, Cohen--Macaulay and canonical-module conventions | a895f47628b0bc7c7ee5e0392df2f79c24166f92 | MATHEMATICS.md | bbd847461b4955a93b4533fa687cdd8724e2347c |
| Complete source Tor theorem | 08147ccecfe684af76a8417861fcccda61abe601 | TERNARY_CUBE_TOR_CHARACTERS.md | f8edf2aac25e96434f77e1fc1681b8f22c609071 |
| Full weight/character certificate | 08147ccecfe684af76a8417861fcccda61abe601 | tor_characters.verification.json | 4ea01d1d6fbb0383e31f03f060a8511dd3c7a1e4 |
| Globally exact marked first presentation | 4c635b2ee8d7cf6caa41efde2d2e0c7baea1b787 | TERNARY_CUBE_PRESENTATION.md | ff8bcf95ef425ac976718d8037cedc6a5374ee4e |
| Certified D2 and degree-five D3 data | 742d68b6d3c37191589b0e6463bc122af6d90f76 | resolution_stage5.cache.json | 3f1689a7388de3b4cf3f33e3cc7057d51a94118b |
| Accepted complete degree-six discovery | d3bda0446a379ce0bd8dfe4024f0184451adb1d5 | row_restricted_grade6.discovery.json | b9131081876be381c43237ea42c5695767bd73ae |
| Previous global exactness implication | 423a25c35996ec5bf2c4dfaac6594d31f89f1081 | GLOBAL_EXACTNESS_FROM_CERTIFIED_KERNELS.md | 79e3792aad018275ba90353e470f1fa234bd76d5 |
| Original full-census contract | 423a25c35996ec5bf2c4dfaac6594d31f89f1081 | TERNARY_CUBE_FULL_RESOLUTION.md | daa8d3f42701dbc6ba5a22c18782e4568bec22cf |

The accepted degree-six proof object is
82804857869343db3371d42b7aa64bd5a71cecde7f02269a6df7ff05afb25d5c.
Acceptance of that discovery is distinct from execution of every older
test suite. An implementation of this new contract must authenticate
the consumed frozen maps and their source chains; a numerical dimension
printed in a payload does not independently prove the premises below.

## Required source premises

The frozen first presentation is globally exact and minimal:

    F1 --D1--> F0 --> R --> 0,
    F0=S+17S(-1)+11S(-2), F1=20S(-2)+65S(-3).

The certified degree-four and degree-five source kernels and the
independent Tor2 support prove that the actual marked map

    D2: F2=65S(-4)+20S(-5) --> F1

is a globally exact minimal cover of K1=ker(D1). This is the preceding
step of the423a25 proof:65 first kernel generators, actual old rank639
in degree five, full kernel dimension659 and20 new quotient classes.
This premise must be established before identifying the next quotient
with Tor3; compositions equal to zero alone do not establish it.

Put K2=ker(D2). Dimension shifting through those exact minimal covers
gives

    K2/mK2 = Tor3^S(R,Q).

The independent source Tor theorem, obtained from actual low-degree
Koszul homology and canonical-module duality, says that this quotient
has precisely11 generators in degree five,17 in degree six and one in
degree seven. The degree-seven summand is det(V)^7, with its sole torus
weight omega=(7,7,7). All other internal degrees and degree-seven weights
have zero quotient. Projective dimension three also gives Tor4=0.
These facts are not inferred from an Euler numerator or from the matrix
that is about to be constructed.

Finally, the accepted lower D3 columns must give all of K2_5 and K2_6:
eleven degree-five vectors, and110 actual variable multiples of them
together with17 new degree-six vectors spanning the full127-dimensional
degree-six kernel. Their complete weights and polynomial compositions
are retained. Denote these vectors by z_1,...,z_11 and y_1,...,y_17.

## The exact old subspace in degree seven

There are no K2 components below degree five. Indeed otherwise a least
nonzero degree would give a nonzero class of K2/mK2 below its known Tor
support. The accepted lower columns therefore imply

    (mK2)_7 = sum_i S_2 z_i + sum_j S_1 y_j.                 (1)

This equality uses actual generation through degree six, not the
independence of a counted list of old columns. All55 degree-two monomials
and all10 degree-one variables must be included. Thus the global old
list has11*55+17*10=775 entries, but its global rank need not be computed
for this new theorem.

Every column is torus homogeneous. Weight spaces form a direct sum, so
the central part of(1) is exactly

    O_omega = span of ALL x^alpha z_i and x^beta y_j
              of total weight omega,
              |alpha|=2, |beta|=1.                          (2)

Columns of other weights cannot contribute to a linear combination
lying in this central weight space. In particular, selecting the entire
central-weight old list loses no possible old expression for a central
vector. Selecting an arbitrary subset of that list would be insufficient.

## The one new computational obligation

Construct a vector v in the original coordinates of (F2)_7,omega and
certify BOTH of the following:

1. D2 v=0 in every original target row, equivalently as a complete
   polynomial vector in F1. Checking only selected elimination rows,
   a numerical residual or an alternating dimension is insufficient.
2. v is outside the complete old central span O_omega in(2).

For the second assertion, an exact rank increase of the old list upon
adjoining v is sufficient. Alternatively, supply an exact linear
functional on the original central domain that annihilates every old
column and has nonzero value on v. Such a dual witness requires neither
a complete basis of the central kernel nor a rank calculation in other
weights. All coefficients, degrees, torus weights and original column
addresses remain part of the certificate.

The first assertion places v in K2; the second makes its image nonzero
in (K2/mK2)_7,omega by(1)--(2). This quotient is independently known to
be one-dimensional. Therefore v supplies its entire basis. Its entry
degrees are positive automatically from internal degree seven and the
degree-four/five generators of F2; the lower columns retain their
already certified minimality.

Nothing in this argument requires all776 degree-seven kernel vectors,
or even the complete central kernel, to be computed. If a row-restricted
kernel routine is used to find v, its full-row validation still must
certify assertion1; the restriction itself is not a replacement for it.

## Global surjectivity, then injectivity

Let D3 have the actual29 columns z_i,y_j,v, with domain

    F3=11S(-5)+17S(-6)+S(-7).

Their classes now form a basis of every degree of K2/mK2. Since K2 is a
finitely generated graded S-module bounded below, graded Nakayama gives
image(D3)=K2 in every internal degree. This is a minimal free cover:
the induced map F3/mF3 --> K2/mK2 is an isomorphism.

Only after this surjectivity is proved put K3=ker(D3). Dimension shifting
through the now-exact preceding sequence identifies

    K3/mK3 = Tor1^S(K2,Q) = Tor4^S(R,Q) = 0.

The module K3 is finitely generated because S is Noetherian. Another
application of graded Nakayama gives K3=0. Thus

    0 --> F3 --D3--> F2 --D2--> F1 --D1--> F0 --> R --> 0

is the complete minimal marked resolution. No injectivity of an
unverified map was assumed, and the Tor identification at each stage
uses only covers already proved exact.

## What is deduced, and what remains unmeasured

After the preceding witness succeeds, injectivity of D3 implies that
the775 old degree-seven multiples are independent and that the full
degree-seven kernel has dimension

    11*dim(S_2)+17*dim(S_1)+1 = 605+170+1 = 776.

These are then algebraic consequences of the independently supported
global theorem and the new actual witness. They are not measurements
of a performed775-column global elimination or a776-vector kernel
census. A report must keep these statuses distinct.

Failure to find or certify v leaves this new obligation open. It does
not refute the classical Tor theorem, establish a missing higher
generator, or turn an interrupted old run into a completed one. The
result, when certified, is one marked resolution; no GL3-equivariant
choice of the marked lifts, finite superdeterminant interpretation,
arithmetic Frobenius assertion or RH consequence is supplied here.
