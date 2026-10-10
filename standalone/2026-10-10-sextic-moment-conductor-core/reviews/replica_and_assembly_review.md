# Root review: replica averages and final assembly

Reviewer: root research agent. Date: 2026-10-10.

**Verdict: the replica component proofs pass at their stated scope.** This is an independent reading of the replica agent's mathematics, not an external or formal certification. The root agent also reconciled the other independent reviews with the final packet. No full moment estimate or new zero-free region was obtained.

## Exact replica source

The author-frozen replica_extraction_attack.md has SHA-256
223075c86b08344030c1b2368a35e8f28b10b002d0c9884fe867da88428e2871.
The packet's REPLICA_AVERAGES.md has SHA-256
489bac05b84802d9366c8c398fbf300affeb126a05acc66f2b77cd3cc8be8357.
The only change is making the standard normalization c(1)=1 explicit in the completely multiplicative operator datum. It is necessary for the identity term; zeros at other primes remain permitted.

## 1. Moving averaging operator

The annular ideal counts and conditional divisibility limit are correct for each fixed excluded prime set Q. The positive Euler weights have summable prime perturbations O((Np)^(-1-beta)) for every beta > 0.

The essential order of choices was checked: first choose Q using the exact limiting conditional mean of (G_beta - 1)^p; then keep Q fixed while choosing Y0 by summable domination. This proves that the sum of the suprema of the dilation coefficients over Y >= Y0 is small. Bounding only the supremum of their sum would not suffice for an arbitrary moving Y(D).

Weighted Hölder applies for every fixed integer p >= 1, with the p = 1 convention stated in the note. Each dilation is a contraction on (0,X) with measure dD/D because its change of variables uses (0,X/Nd). Jensen bounds the averaged operator, and the Neumann series is a genuine inverse on that same Banach space. No future scales or omitted initial interval enter the argument.

The limiting multiplier's local numerator and denominator are nonzero for Re(s) > 0 and |c(p)| <= 1, and the Euler perturbations are summable. It therefore cannot cancel a reciprocal-L pole in that half-plane. This transports a future average estimate; it does not establish one.

## 2. Rough record replication and omitted rows

Continuity and the positive lower support cutoff justify the record-scale construction. Exact Euler removal bounds the relative lift error by G_beta(v)-1. Elementary ideal counting and Markov's inequality give a positive proportion of sufficiently rough bases with error at most one half.

Distinct ideals give distinct sixth-power elements, since all Eisenstein units have sixth power one. Thus a positive multiple of H^(1/6) distinct permitted rows survive at the record scales. No prime-counting logarithm appears. An arbitrary deleted set of o(H^(1/6)) cannot remove all these rows.

The strict exponent comparison is

\[
2k\beta+h/6 > k+h+e.
\]

This gives the stated boundary 1/2 + 5h/(12k) + e/(2k); choosing a fixed epsilon smaller than the gap yields the contradiction. The Mellin nonvanishing test remains an explicit dependency on PR #912.

## 3. Saturation examples

The first example satisfies the complete prime-removal algebra, including nonunit zeros. Its support on a zero-density set prevents a nonzero finite periodic column representation. That limitation is stated.

For the second example, the refined sieve gives exponents

\[
h+2jB-j,\qquad h/6+2jB,\qquad
2h/3+2jB-j/3.
\]

With B = 1/2 + 5h/(12K) and K >= 3h/2, all three are at most h+j for j <= K. For j >= K the middle exponent dominates. Squarefree density and rough replicas give its matching lower bound at every sufficiently large scale. The elementary density proof uses a convergent square-divisor tail.

The datum nu_B(p) = -(Np)^(B-1) has modulus strictly below one and is not a finite-order Hecke character. This is a counterexample to a bootstrap from the specified weaker hypotheses, not to the native moment target.

## 4. Final assembly

The A2 note is copied byte for byte from the final author source. Its initial review and supplement retain separate frozen scopes. The conductor and interaction notes, both checkers, and their outputs match the independently reviewed hashes.

The overview was corrected to specify 1 < Nf <= F for the nonprincipal conductor sector, the fixed polynomial column bound needed in the diagonal estimate, and that the singleton-core and Poisson problems are separate sufficient residual formulations. Inline math delimiters were repaired. The averaging claim explicitly retains integer p >= 1.

The root agent independently inspected the source initial-Poisson formula and derived the reversible diagonal cancellation. It applies to the entire signed auxiliary sum, not separately to each dyadic f or b block. Positive A2 norm transfer does not automatically transfer a centered covariance estimate: distinct correction triples create cross terms and different auxiliary ideals. These restrictions remain explicit.

No proof file uses a finite numerical check as the proof of an infinite estimate. The packet establishes neither the moving-conductor A2 functional equation nor the required strict signed off-diagonal bound, 17/24 attainment, or RH.
