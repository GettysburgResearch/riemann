# Independent checker receipt: joint reflected blocks

**Reviewer:** \(\texttt{/root/amplification}\).

**Date:** 2026-10-10.

**Verdict:** PASS for the declared finite diagnostics. The checker was inspected and independently replayed in ordinary and optimized Python. Both outputs equal the author's frozen result byte for byte. This receipt supplements the separate full mathematical review; it makes no analytic inference from finite tests.

## Exact identities

| Object | SHA-256 |
| --- | --- |
| attack3_theta_check.py | f156b99c452f514b0bcf0ae4913d8becb24a64612746d06a5e0143ccb8027266 |
| Author's attack3_theta_results.json | 19ec6c46f7bcda904b4f3efb549d731c780b203f448a6125774dbb39bc0870bb |
| Independent attack3_amp_theta_normal.json | 19ec6c46f7bcda904b4f3efb549d731c780b203f448a6125774dbb39bc0870bb |
| Independent attack3_amp_theta_optimized.json | 19ec6c46f7bcda904b4f3efb549d731c780b203f448a6125774dbb39bc0870bb |
| Associated mathematical note, attack3_theta.md | c75be63f43de6efb0d9f820da008f256afc53351fdbfe38870f9e97207955bd5 |
| Separate analytic review, attack3_theta_review_amp.md | cca571ec0ab061e2197b435b6568a97868f5b5f1e9ee91fa65e25455197a320b |

The checker computes its own source hash from its source bytes. The associated mathematical note is separately bound here; the executable does not itself authenticate or prove that note.

## Replay

The commands executed were:

~~~sh
python attack3_theta_check.py --output attack3_amp_theta_normal.json
python -O attack3_theta_check.py --output attack3_amp_theta_optimized.json
cmp attack3_amp_theta_normal.json attack3_amp_theta_optimized.json
cmp attack3_amp_theta_normal.json attack3_theta_results.json
~~~

Both Python processes exited successfully and reported 302,676 exact predicates. Both byte comparisons passed. All acceptance gates use explicit exceptions rather than Python assertions, so optimization cannot disable them. No author source or result file was changed.

## Primitive arithmetic inspection

The ring operations use \(\omega^2+\omega+1=0\), with

\[
(a+b\omega)(c+d\omega)=(ac-bd)+(ad+bc-bd)\omega,
\qquad N(a+b\omega)=a^2-ab+b^2.
\]

The primitive sixth root is \(1+\omega\), correctly represented by the pair \((1,1)\). The six roots produced from it are distinct and have the expected order. The four selected primary generators and residue embeddings are:

| Norm | Generator coefficients \((a,b)\) | Residue of \(\omega\) |
| --- | --- | --- |
| 7 | \((-2,-3)\) | 4 |
| 13 | \((1,-3)\) | 9 |
| 19 | \((-2,3)\) | 7 |
| 31 | \((-5,-6)\) | 25 |

I independently checked that each generator has the indicated prime norm, is one modulo three, and vanishes under its stated embedding. The embedding satisfies the minimal polynomial of \(\omega\). The local sextic value is calculated by the finite-field power \(r^{(q-1)/6}\), then lifted to the corresponding exact sixth root in the ring. This is a primitive finite residue calculation, not a table of desired character signs.

Zero is retained before reducing a character exponent modulo six. In particular, a sixth or principal power still vanishes at a nonunit. The ring convention is consistent throughout; no primitive-sixth-root basis is accidentally substituted into the Eisenstein multiplication formula.

## Coverage and what was recomputed

The 16 ideal masks enumerate precisely all squarefree products of the four selected prime ideals. The 65,536 ordered \((k,g,e,n)\) tuples are all tuples of these masks. They are not all rows below any norm bound.

The complete category counts include:

| Predicate family | Count |
| --- | ---: |
| Primitive field and root checks | 94 |
| Local multiplicativity in the four complete residue fields | 1,540 |
| Principal powers at all local residues | 70 |
| Multiplicativity on the selected norm-91 CRT panel | 8,281 |
| Zero extension on that CRT panel | 91 |
| Common-divisor kernel identity | 65,536 |
| Moving-mask identity | 65,536 |
| Row-divisor phase factorization | 160,000 |
| Complete signed gcd sums, two coefficient panels | 32 |
| Coprime product-column sums, two coefficient panels | 32 |
| Local all-row majorants | 350 |
| Local prime-summability exponent guards | 350 |
| Valuation gates for the \(j=4\) loss | 350 |
| Activity at valuations one and two | 350 |

The remaining 64 predicates cover incidence enumeration, symbolic exponent dimensions and expansions, normalizer ratios, selected long-dual examples, endpoint obstructions, and mutation witnesses. The total is 302,676.

The norm-91 CRT panel uses the two selected prime ideals of norms 7 and 13. Integer residues modulo 91 cover their product residue field completely, by the ordinary CRT. This is not an enumeration of every residue in \(\mathcal O_K/(91)\).

The common-divisor full-sum check has a second enumeration using four states at each prime: neither, \(g\) only, \(n\) only, or common. It verifies that those states cover the 256 ordered \((g,n)\) pairs, and compares the resulting signed sums with direct triple sums. The coprime product coefficients are assembled independently of the row. The two separate coefficient panels include sixth-root phases, Möbius signs, and fixed zero masks.

The normalizer tests use exact squared ratios, avoiding square-root approximations. The six-monomial expansions use rational exponent vectors. The local all-row panel covers valuations 1 through 30, both squarefree-overlap states, all allowed active choices, and five fixed rational values of \(\eta<1/3\). It also checks that the valuation-two \(j=4\) envelope has exponent \(-1\) at the endpoint, while an inactive valuation-three branch has exponent \(-2\).

These local exponent guards test the stated amplitude envelopes. They do not directly evaluate every reflected theta coefficient or prove convergence at all prime ideals. The general convergence argument was reviewed separately in the mathematical receipt.

The mutation controls exhibit an actual difference after dropping the common-divisor row zero, dropping the moving \(e\)-mask, or replacing a repeated product by its radical. These are substantive normalization checks.

## Scope

The executable does not verify either analytic large sieve, theta reflection or support, infinite Euler-product convergence, angular reciprocal bounds, all prime ideals or row valuations, an infinite moment, or RH. The three long-dual parameter examples do not replace the proof over the full interval of \(\theta\). Those boundaries are accurately stated in the source and result.

**Signed:** \(\texttt{/root/amplification}\), independent checker reviewer, 2026-10-10.
