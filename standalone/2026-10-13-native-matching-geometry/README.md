# Native matching geometry: sharp reference scales and uniform physical errors

**PROPOSED component mathematics. Not a proof of the full generalized moment or
RH. No new native moment power saving or zero-free boundary. Not pushed in this
session; see PUBLISHING.md. Independent mathematical review remains required.**

Base: PR #942 at `377f548cab8759399aca80ed3188c495667d562a`.
Read [PROOF.md](PROOF.md), particularly Sections 3--5, then the limits in
Section 7. All earlier repository files are left unchanged by the supplied patch.

## Results

For the original squarefree Eisenstein columns, a fixed nonzero nonnegative
compact continuous/smooth test W, every fixed k, and unitary multiplicative
column phases, the complete masked independent-residue principal reference has

    B_(2k)(D) asymp D^k (log(2+D))^((k-1)^2).

This includes sixth-power aliases at k>=6. The lower bound works for arbitrary
unitary prime phases, not just phases in mu_6: selected squarefree products near
the top of the support have isolated charge blocks, so their contribution
cannot be cancelled by a different sixth-power product.

For actual nonzero physical rows, the principal portion has

    P_sharp(D,H) = (2pi/sqrt(3)) H B_(2k)(D)
                    + O(sqrt(H) D^k (log(2+D))^((k-1)^2)),

and for a fixed Schwartz profile Phi,

    P_Phi(D,H) = c_Phi H B_(2k)(D)
                    + O(D^k (log(2+D))^((k-1)^2) (log(2H))^(k^2)).

There is no D^epsilon in these errors. With c_Phi>0 the relative errors are
O(H^(-1/2)) and O((log(2H))^(k^2)/H), uniformly in D. Constants depend on k, W
and the fixed excluded set for the lower bound; no growing-order uniformity is
claimed. The exact band-limited conclusions of #942 are preserved, not replaced.

The key aggregate divisor bound retains

    F_theta(Q)=product_(p|Q)(1+(Np)^(-theta))

instead of replacing it by tau(Q). A dyadic graph count prices its coefficient
cost by zeta_K(1+theta)^(k^2). Choosing theta>0 in terms of H, and paying that
entire cost, yields the smooth error. The zero row and every neutral mask remain.

## Graph interpretation and a sharper signed-sector upper bound

For a graph G of allowed exact multiplicity-two prime incidences on the 2k
slots, let d_G be the nullity of its unsigned incidence matrix. With no singleton
primes and arbitrary higher incidences, the absolute count is

    O_G(D^k (log(2+D))^d_G).

If G admits a strictly positive fractional perfect matching, that logarithmic
order is attained in fixed annular ideal boxes. The mechanism is the dimension
of a matching polytope, not a new independence claim for the physical rows.

| Order | Principal: K_(k,k) | No singletons: K_(2k) |
|---|---:|---:|
| 4 | D^2 log D | D^2 (log D)^2 |
| 6 | D^3 (log D)^4 | D^3 (log D)^9 |
| 8 | D^4 (log D)^9 | D^4 (log D)^20 |

Multiplying the no-singleton absolute count by the actual row
mass proves a bound for that complete SIGNED physical sector by domination.
No sign is assigned to its individual nonprincipal terms. This is sharper in
logarithms, not a larger controlled sector than #940's smooth-singleton theorem.

## Classical credit

The logarithmic powers themselves and the random multiplicative/Birkhoff
connection are classical: Harper--Nikeghbali--Radziwill (2015), Theorems 3--4,
and independently Heap--Lindqvist (2015). This packet proves a mask- and
alias-preserving adaptation and its physical error bounds. It does not claim a
new random multiplicative moment theorem or the leading asymptotic constant.
See SOURCES.md for exact source and reading scopes.

## What was actually tested

The standard-library checker passes 165,577 explicit finite predicates including
setup checks. Ordinary and optimized Python produce byte-identical results.
It checks 1,099 finite graphs, integer matching fibers, 17,846 principal local
patterns, literal masks on complete small column windows, and four specific
false substitutions. These are not independent asymptotic cases.

The additional calibration uses every good squarefree ideal in hard windows
D/2<Nn<=D for D=64,...,2048 (six dyadic scales). It encloses the independent
fourth reference with rational dyadic endpoints and computes exact sharp
principal sums at two heights. It does NOT recompute the full physical moment
or its nonprincipal remainder. The fixed hard diagnostic window differs from
the theorem's stated continuous test.

    python -I -S -B verify.py > replay.json
    python -I -S -B -O verify.py > replay.optimized.json
    cmp replay.json results.json
    cmp replay.optimized.json results.json
    python -I -S -B calibrate.py > replay.calibration.json
    cmp replay.calibration.json calibration.json

The arithmetic helper is an unchanged, hash-authenticated #942 census source.
Proof and diagnostics have one author; there is no independent review, remote
CI, formal proof build or full-repository validation. Read VALIDATION.md.

## Still unpaid

The long-radical nonprincipal sum with genuinely large singleton products needs
a new signed bound. Matching geometry estimates neither that sum nor the full
near-linear-row moment. Small principal calibration errors must not be used as
bounds for the nonprincipal remainder.
