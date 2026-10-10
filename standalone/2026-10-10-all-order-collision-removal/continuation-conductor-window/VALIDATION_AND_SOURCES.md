# Source, validation and claim boundaries

## Frozen source and preservation

This is an add-only continuation of GettysburgResearch/riemann PR #916:

- parent commit: `f5c089e33ccce4eae4307d4f6475b9977485cb78`;
- parent root tree: `dee1aae18bee482aae953729441604ac6d480bb9`;
- branch: `research/all-order-collision-removal-20261010`;
- relevant parent proof: `standalone/2026-10-10-all-order-collision-removal/continuation-integrated-window/INTEGRATED_CRITERION.md`, blob `34928b0d8531e8cbe8764edbabb188bcb72d5ff1`;
- parent sieve audit: `continuation-integrated-window/OPTIMAL_SIEVE_AUDIT.md`, blob `28ca6619f658b27791033a06776455a364018ea6`.

The parent was read live through the GitHub connector. Its branch head was confirmed, rather than inferred from the earlier chat. Main, sibling branches, accepted status and all predecessor files are outside this edit.

The new covariance-sector estimate does NOT assume the imported quasi-Riemann theorem, a new large sieve, or any adjacent analytic packet. Its proof explicitly supplies the finite Gauss norm, the lattice Fourier estimate, common-prime mask accounting, balanced tuple count and weighted integration. The final zero-free implication uses the parent's integrated norm comparison and replica/Mellin implication with their stated fixed-prime cutoff.

## Adjacent work and literature inspected

PR #919 at `9b04a887e171b3104a66cf57296ce5b0b2920d78` already studies signed conductor frontiers in original moment variables. Its PR metadata were read, not its complete mathematical packet. Its results are not silently imported into this proof, and elementary conductor removal is not claimed as a new general idea.

PR #922 at `f71a9bc6ac3ce59a3c19d7e842a3fa082ecfbe32` and PR #923 at `1a1152008706f7e24fa1efe4990588f8f99c5d8d` were checked at metadata level to avoid confusing their short-row/all-cusp results with an established solution of the long-row covariance. No adapter from those packets is assumed here.

Alexandre de Faveri, *Optimal large sieve for fixed order characters*, arXiv:2610.04045v1, Theorem 1.1 and introduction, was checked online at https://arxiv.org/html/2610.04045v1. This confirms the newer external sieve used in the parent's audit. It is NOT an input to the new theorem. Its proof was not independently reconstructed. Finite Fourier orthogonality, Poisson summation, fixed-order divisor bounds and unit orthogonality in the new argument are classical, not discoveries claimed by this packet.

## Exact arithmetic diagnostic

`arithmetic_probe.py` uses only the Python standard library. The retained command is

    python -I -S -B arithmetic_probe.py --D 96 --H 96 --write actual.json > actual.stdout

The complete output is 445-plus lines of exact integer and rational data, including every dyadic conductor band. It is reproduced rather than treated as a precomputed source. Its exact SHA-256, source SHA-256, primitive inventory SHA-256, selected fractions and check counts are in `verification_record.json`.

The primitive source is O=Z[omega], norm a^2-ab+b^2. All primary ideals of norm <=96 avoiding 2 and 3 are enumerated, factored, and reconstructed. Residue symbols are computed using quotient-lattice modular powering. An independent F_p embedding or F_p[omega] calculation verifies each prime symbol. Original zero values are never replaced by unit phases.

The row set is ALL nonzero Eisenstein elements with norm <192. Norm 192 itself has row weight zero. Its size is 684. There are 27 squarefree input ideals, 21 good prime ideals, and 153 product columns after exact support pruning. This very small range has input factor depth at most two. The window is 1_(1/2,1] and the integrated scale weight is X^(-3)dX/X (sigma=3/4 for the fourth moment). It is NOT the smooth W_* window in the zero-free application.

At integer intervals [m,m+1), all box coefficients are constant. With L=lcm(1,...,D)^3, the scale weights have common denominator 3L and numerators L/m^3-L/(m+1)^3. Row weights have denominator (2H)^8. All phases are represented in Z[rho], rho=exp(pi*i/3), and every covariance sum is exact. The real contribution of a conjugate pair whose kernel is x+y rho is 2x+y. No floating-point arithmetic occurs in the checker.

The direct squared row sums are compared with independent ordered coprime-pair enumeration and with the full product-column covariance decomposition. The same reconstruction is performed for the top scale interval [48,96], not just the cumulative integral. Common-prime masks and radial six-block zeros are checked over the actual row set.

Normal and optimized executions each pass **3,522,979 explicit finite predicates**, and their stdout files agree byte for byte. Most counts are repeated primitive/row identity checks; they are not millions of independent analytic lemmas. Three deliberately false changes are rejected: replacing a zero residue value by one, forging the covariance by one integer unit, and discarding the nonzero off-diagonal. A separately changed output fraction is rejected by complete regeneration with exit 1 and message `REJECT: complete primitive reconstruction mismatch`.

Twenty-eight additional exact SymPy polynomial checks verify that every partial derivative of total order <=6 of (1-(x*x+y*y)/2)^8 is divisible by (1-(x*x+y*y)/2)^(8-order). This audits the boundary vanishing used in the Fourier proof. SymPy is not needed by the delivered arithmetic checker.

## Meaning and limitations of the measurements

The retained cumulative signed/diagonal ratio is about 0.0009720531. On the top scale interval it is about 0.2248192451. Printed decimals are ordinary presentations of the exact stored fractions, not interval certificates or asymptotic estimates. Short scales, especially the unit contribution, dominate the cumulative quantity. The small cumulative ratio must not be advertised as numerical evidence for the required growing-scale exponent.

Some conductor bands have negative signed contributions. This illustrates why exact signed data are retained; it does not prove that the still-unbounded high-conductor sum cancels adequately. The proof's absolute band bound has unspecified fixed constants and is established analytically, not fitted to these samples.

## Review and acceptance status

The author checked the finite Gauss normalization, primitive conductor, nonunit mask, support lower endpoint, three integral regimes, delta losses, replica weight and use of positivity. No independent mathematical reviewer, external human review, Lean build, full upstream proof reconstruction or global theorem certification was available or performed in this pass.

The result is a proposed complete component proof. The smallest missing arithmetic theorem for a better zero-free region is (6.3) of `ROW_SMOOTHING_AND_CONDUCTOR.md`, after the proved low-conductor and unit-block removals. The high-conductor moment bound, 17/24, generalized diagonal hierarchy and RH remain open in this packet.
