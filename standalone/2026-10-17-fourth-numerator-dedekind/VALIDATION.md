# Validation and review boundaries

Status: same-author proposed proofs and finite diagnostics. No independent
mathematical reviewer, formal proof assistant, full-repository validator,
remote CI or upstream analytic reconstruction is claimed.

## Executed checks

`python verify.py` and `python -O verify.py` reproduce CHECKS.json byte-for-byte.
`python verify.py --details` emits every density parameter and full quadratic
class exponent, so the 27-class certificate can be inspected independently.
Every inequality in e is checked by rational Bernstein coefficients on the
entire interval 0<e<=10^(-6), not on a numerical grid.

The report contains 2,262 explicit finite predicates. Its groups distinguish:
- 520 density monomial bounds (10 norm and 10 height checks per threshold);
- 671 contour-domain inequalities, including repeated shared vertices;
- complete partition, every class budget, both principal terms and both tails;
- 364 finite polynomial-power and 364 sixth-power/mask identities;
- moment exponent, critical-weight, support and reciprocal-disk bookkeeping.

The phase fixtures use the two finite fields F_7 and F_13 with sextic
characters defined by primitive generators 3 and 2. All 91 residues modulo
7*13 are included, with literal zero values. Initial monomials have exponent
sets {0,1,2,6,7} and {0,1,2}; powers one through four are checked. These are
finite character-product fixtures with integer coefficients, NOT all native
number-field ideals below a cap, NOT the AFE coefficients, and NOT L-values.
Their job is to detect the false loss of sixth-power masks or shared primes.

Eight separately executed corrupted optimized processes fail:
old second-moment pricing in the fourth-moment classes; squarefree-only
columns; erased sixth-power masks; extra coprimality between c and d; counting
at the upper zero threshold; retaining the old Mellin shift; omitting the last
exceptional class; and using a zero gap at the large-frequency cutoff.
MUTATIONS.json records exit status and the actual last error for each process.

No finite predicate estimates an actual infinite numerator moment or proves
that the CT/DF/BGL assumptions hold. No numerical L-value or zero census,
fitted asymptotic, floating exponent acceptance, or positivity extrapolation
is part of this validation.

## Reproduction

From this directory:

    python verify.py > /tmp/checks.json
    cmp CHECKS.json /tmp/checks.json
    python -O verify.py > /tmp/checks-opt.json
    cmp CHECKS.json /tmp/checks-opt.json
    python verify.py --details > /tmp/class-certificates.json

Each `python -O verify.py --mutation NAME` for a name printed by `--help`
MUST exit nonzero. A failed mutation process is not an independent proof test.
The checker uses explicit exceptions and therefore remains active under -O.

MANIFEST.json binds the exact file bytes and Git blob identities. Its hashes
are not mathematical certificates. The downloadable ZIP is checked against
these files; publication is checked by GitHub blob/tree read-back rather than
a claim of a successfully network-cloned local worktree.

## Priority analytic audit

1. NUMERATOR_MOMENTS S6: BOTH indices must be sixth-power-free with the actual
   generator/twist conventions, not merely squarefree.
2. Complete AFE, conductor Mellin separation, both dual parts, and the exact
   c*d^6 decomposition without an added coprimality condition.
3. The moment height exponent must be fixable before the final epsilon loss.
4. The M<1 reconstruction in the pinned parent #965, including all local and
   powerful auxiliary sums and subunit effective lengths.
5. The new 27-class lower-count/upper-contour comparison, principal shift
   15/22, and all horizontal/large-frequency tails.

A defect in any load-bearing analytic step invalidates the proposed 10/11
consequence even if all finite checks and byte hashes pass. The new result is
not promoted into main or the integrated scientific-status record.
