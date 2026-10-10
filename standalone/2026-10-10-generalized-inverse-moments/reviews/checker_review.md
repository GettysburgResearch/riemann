# Independent review and replay of the generalized-moment algebra checker

Reviewer: theta-closure subagent, 2026-10-10.

Verdict: PASS for the stated finite algebra and actual two-prime character fixtures. No required code correction was identified. This is not validation of a short-row analytic moment theorem.

## Frozen source and replay

Reviewed source:

`standalone/2026-10-10-generalized-inverse-moments/checks/verify_algebra.py`

SHA256:

`362694b6c2257392c49e333b804d8767e56a3d34e172b5b0fc746efd96c337e8`

Independent command, from the repository root:

```sh
python -O standalone/2026-10-10-generalized-inverse-moments/checks/verify_algebra.py --output /workspace/scratch/5b23d9b20a3a/theta-review-algebra.json
```

The process exited with code 0 and reported `PASS`, exact integer arithmetic in `Z[zeta_6]`, and 32,473 explicit predicates. Optimized Python was deliberately used: the checks raise exceptions and do not depend on `assert` statements.

The independently generated result was compared byte-for-byte with the authored `results/algebra.json` using `cmp`; exit status was 0. Both files have SHA256

`0dfd3fdd97a991bbb7acd4719a55618d08de5712ec729a9f489bcda76041fd47`.

Predicate counts:

| Category | Count |
|---|---:|
| Actual character embedding/state checks | 5 |
| Hypergraph polynomial identities | 80 |
| Actual row identities | 7,280 |
| Complete residue moments | 80 |
| Adversarial zero-mask checks | 2 |
| Multinomial local inverses | 5,004 |
| Euler corrections | 5,004 |
| Inverse corrections | 5,004 |
| Two-way corrections | 5,004 |
| Nonnegative inverse coefficients | 5,004 |
| Logarithmic leading coefficients | 6 |

## Why the character fixtures are native arithmetic

The two residue embeddings are the prime ideals

\[
 \mathfrak p_7=(7,\omega-4),\qquad
 \mathfrak p_{13}=(13,\omega-9),
 \qquad \omega^2+\omega+1=0.
\]

The chosen images satisfy the defining polynomial in their finite fields. Each quotient is the actual field `F_p`. The element `zeta_6=1+omega` maps to a primitive sixth root, and the character is obtained from the defining residue formula `u^((p-1)/6)`, with an explicit zero at `p|u`. Thus these are sextic residue symbols at actual split prime ideals, not arbitrary assignments of roots of unity.

The integer residues `0,...,90` give a complete set of representatives for the product quotient: their images cover `F_7 x F_13` by the ordinary Chinese remainder theorem, and that quotient has cardinality 91. These rows are complete residue representatives, not a norm ball.

The exact arithmetic basis is consistent: `zeta_6^2=zeta_6-1`, so multiplication of `a+b zeta_6` and `c+d zeta_6` is `(ac-bd)+(ad+bc+bd) zeta_6`, exactly the implemented rule. Its squared complex modulus is `a^2+ab+b^2`, exactly the implemented norm.

The signs `nu(p_7)=nu(p_13)=-1` are compatible with the genuine fixed Hecke twist `nu_5=chi_5 composed with N`, where `chi_5` is the real quadratic Dirichlet character modulo 5: both 7 and 13 are quadratic nonresidues modulo 5. Their product has twist `+1`. The checker supplies these two local signs directly; it does not compute the entire global Hecke character or its conductor. That is sufficient for these finite column fixtures.

## Independent assembly and collision handling

The direct side builds the product by polynomial multiplication of the four squarefree ideal choices `1,p_7,p_13,p_7 p_13`. The regrouped side instead enumerates repeated incidence sets and then independently allocates unused primes to no singleton factor or exactly one singleton factor. Each support and dilation is evaluated on the resulting original ideal norm. This is a meaningful check of the incidence decomposition, rather than a comparison of two serializations of one expansion.

The character exponent representation distinguishes absent exponent zero from every positive multiple of six. The latter is encoded by six and evaluates to zero at a local nonunit. Exponents add using this convention, so `chi^6`, `chi^12`, and their conjugates retain the coprimality mask. Two explicit negative fixtures reject the incorrect constant-one replacement.

For the complete moment calculation, character conjugation permutes the seven states `0,1,...,6` injectively. The dictionary comprehension constructing the conjugate therefore cannot silently overwrite collisions. The coefficients in these fixtures are real integers, so no coefficient conjugation is missing. Polynomial multiplication then groups the genuine sixth-power collisions. Complete local summation contributes `p` for an absent prime, `p-1` for an active sixth-power mask, and zero for each nonprincipal local power. The independent field evaluation and this orthogonality calculation agree in all 80 panels, including orders above six.

## Local Euler-series checks

For each factor count `r=1,...,6`, all nonnegative multiindices of total degree at most eight are covered: 5,004 multiindices in total. The series `1-sum z_i`, `product(1-z_i)`, its multinomial inverse, and the two correction factors are assembled from separate explicit coefficient formulas. Every convolution contributing to a tested coefficient remains within the same total-degree truncation, so no unavailable higher-degree coefficient is silently treated as zero in a way that could affect the check.

The signs and normalizations agree with the proofs. In particular the local correction coefficient is `1-|supp(e)|`, and the inverse coefficient is the full inclusion-exclusion multinomial expression. Their degree-two absolute mass is exactly `binom(r,2)`.

## Limits of this evidence

The replay covers two split prime ideals, four squarefree column ideals, moment orders one through eight, five finite scale fixtures, two real local twist choices, and finite total degree eight for the Euler identities. The weight fixtures are deliberately not smooth. It does not test arbitrary complex smooth tests, other prime ideals or inert primes, unbounded moment order, norm-ball asymptotics, any uniform implied constant, the Mertens estimate, theta reflection, or off-diagonal cancellation at the requested short row length. The complete residue identity is exact finite orthogonality; it is not a short-row moment bound.

These limitations match the source file and JSON scope statements. The finite replay supports the local algebra and implementation; the all-order statements rest on the written proofs, and the desired analytic fourth and generalized moments remain open.
