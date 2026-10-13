# Exact-commit nonauthor review: cubic fibers and parity-envelope interfaces

**Verdict: PASS within the finite, conditional, and method-specific scopes stated below.** I found no substantive mathematical blocker in the reviewed material. This verdict does not supply an unproved analytic premise, prove the full generalized moment conjecture, or prove RH.

- Reviewer: automated agent `/root/theta_closure`, a nonauthor of the two notes and the cubic-fiber checker reviewed here.
- Review completed: 2026-10-13 UTC.
- Repository: GettysburgResearch/riemann.
- Exact mathematical source: `c07b9f653b8d0eb82d9f056d935a4ecef6770f56` (PR #930).
- Packet: `standalone/2026-10-12-parity-and-cubic-fibers/`.
- Formal proof scope: all of CUBIC_FIBERS_AND_RIESZ_PRODUCTS.md; PARITY_DAMPED_MOMENTS.md §§7–9, with its supporting definitions, stated hypotheses, and proof interfaces read and checked.
- Executable scope: source inspection and independent normal/optimized replays of the committed cubic-fiber checker. This is not an independent reimplementation or formal proof verification.
- This is an automated-agent review, not human review, merge approval, or integration.

## 1. Authenticated source identities

I fetched the following files through the GitHub connector at the exact commit above, saved their returned UTF-8 contents without adding a newline, and recomputed SHA-256 and Git blob SHA-1 from their bytes. Every reconstructed Git blob agreed with the connector's returned blob identity. Both note hashes agreed with the hashes supplied in the review request.

The Git blob calculation was SHA-1 of the concatenation of the ASCII header “blob ”, the decimal byte length, a NUL byte, and the file bytes.

| Source | Bytes | SHA-256 | Git blob |
|---|---:|---|---|
| [CUBIC_FIBERS_AND_RIESZ_PRODUCTS.md](https://github.com/GettysburgResearch/riemann/blob/c07b9f653b8d0eb82d9f056d935a4ecef6770f56/standalone/2026-10-12-parity-and-cubic-fibers/CUBIC_FIBERS_AND_RIESZ_PRODUCTS.md) | 25,697 | `026d1a3d6f458b872128fa77fbe683a35cc38a799e822d29760dbc566c2bd91e` | `f8824c18f1ba54f0ab863f2a4b0fc92a55bc01e9` |
| [PARITY_DAMPED_MOMENTS.md](https://github.com/GettysburgResearch/riemann/blob/c07b9f653b8d0eb82d9f056d935a4ecef6770f56/standalone/2026-10-12-parity-and-cubic-fibers/PARITY_DAMPED_MOMENTS.md) | 38,285 | `fed521f2865b428e5a0eebd1d6f36ae09cc6d51f513952547ba6087910d0d232` | `dbc13956b5eb5f3b5b2028dc9ebcd81a7c48a8c3` |
| [checks/verify_cubic_fibers.py](https://github.com/GettysburgResearch/riemann/blob/c07b9f653b8d0eb82d9f056d935a4ecef6770f56/standalone/2026-10-12-parity-and-cubic-fibers/checks/verify_cubic_fibers.py) | 23,564 | `3c600e421b0664654830e09429108ff0798db94061d1f5684ccbe6ccde228114` | `a337db59569e4ec14464a0fcea96bea6606d354e` |
| [results/cubic_fibers.json](https://github.com/GettysburgResearch/riemann/blob/c07b9f653b8d0eb82d9f056d935a4ecef6770f56/standalone/2026-10-12-parity-and-cubic-fibers/results/cubic_fibers.json) | 8,538 | `68c4c47d5c1389ec2c63f6546b01ede6a9e25d6b161b996913a3a837c34df64e` | `5724cfbc17d1f082ae2553a571598788c71d4da3` |

These are identities of the mathematical source reviewed, not identities inferred from branch names or a later PR head. I did not edit any of these files.

### Detector dependency

I also freshly fetched and authenticated [SAMPLED_MOMENT_CRITERION.md at 086bf0560c0c2679a1fe41418f583d2c5ca743c3](https://github.com/GettysburgResearch/riemann/blob/086bf0560c0c2679a1fe41418f583d2c5ca743c3/standalone/2026-10-10-mobius-overlaps-and-sampled-moments/SAMPLED_MOMENT_CRITERION.md). It has 28,877 bytes, SHA-256 `18bf2fdad438eb21ae3318eba7d42e9c03803b2dd1abc4d8f6448fb3b04499de`, and Git blob `ccb083b8bfd2e3c015c9a8aad5b27ba2754243a4`. I read its nonvanishing Mellin-detector construction in Proposition 2.1 and its extraction argument in §6.

I also read the locally available causal-inverse argument cited from [SCALE_AVERAGED_CRITERION.md at 6b4723042b3d250024eef45cb1924f88f28e902c](https://github.com/GettysburgResearch/riemann/blob/6b4723042b3d250024eef45cb1924f88f28e902c/standalone/2026-10-10-oscillating-overlaps-and-averaged-moments/SCALE_AVERAGED_CRITERION.md), including the moving-cutoff conditions. That file was not freshly fetched and authenticated in this review. Its causal-inverse theorem remains a named imported premise; the present review checks that the invocation uses the required positive exponent, fixed moment order, and growing cutoff.

## 2. Full cubic-fiber proof review

### 2.1 Exact character and residue-class identities

I reconstructed the factorization into the quadratic and cubic characters, including their literal zero values at nonunits. In the note's notation,
\[
\chi_{\mathfrak n}(u a^3)
 =\chi_{\mathfrak n}(u)Q_{\mathfrak n}(a),
\]
while the cubic component of the transformed row equals the original cubic component times the coprimality indicator for \(a\) and \(\mathfrak n\). The identity does not require coprimality of \(a\) and \(u\). The auxiliary mask cannot be omitted.

On complete unit residue classes modulo the product of the good primes in the finite column support, the local quadratic signs are independent and fair. The nonnegative Riesz density
\[
\prod_{\mathfrak p}(1+N\mathfrak p^{-t}Q_{\mathfrak p}(a))
\]
has mean one and realizes the stated positively biased sign law. The \(t=0\) specialization selects the all-plus quadratic signs. The opposite sign convention in the companion parity note is reconciled by the substitution \(e_{\mathfrak p}=-z_{\mathfrak p}\), together with the explicit Möbius coefficient.

I checked the distinction between the cube map on elements and its use after choosing ideal generators. The finite multiplicity and unit phases are retained. No argument silently replaces cube multiplication by sixth-power multiplication.

The elementary lattice completion is appropriately scoped. A residue class modulo an Eisenstein ideal of norm \(N\mathfrak f\) has counting error
\[
O(1+\sqrt{B/N\mathfrak f})
\]
in a norm ball of radius parameter \(B\), uniformly in the residue class. Summing this bound against a nonnegative periodic function produces a relative error controlled by
\[
\sqrt{N\mathfrak f/B}+N\mathfrak f/B.
\]
Thus this completion argument gives a complete-residue comparison when \(B\) is sufficiently larger than \(N\mathfrak f\). After multiplication by \(a^3\), it incurs the corresponding cubic row-height cost. This is an explicit limitation of the supplied argument, not a theorem that every specialized completion must incur that cost. In particular, the proof does not replace a short physical norm ball by a complete CRT average.

### 2.2 Full likelihood and the smaller frequency-space norm

For \(0\le s<t\), put \(a_{\mathfrak p}=N\mathfrak p^{-s}\), \(b_{\mathfrak p}=N\mathfrak p^{-t}\), and \(\Delta_{\mathfrak p}=a_{\mathfrak p}-b_{\mathfrak p}\). I independently expanded the finite likelihood ratio under the base law:
\[
L=\prod_{\mathfrak p}
\left(1+\frac{\Delta_{\mathfrak p}
 (z_{\mathfrak p}-b_{\mathfrak p})}{1-b_{\mathfrak p}^{\,2}}\right).
\]
The exact squared norm on the full function space is
\[
\Gamma=\prod_{\mathfrak p}
\left(1+\frac{\Delta_{\mathfrak p}^{\,2}}{1-b_{\mathfrak p}^{\,2}}\right).
\]

The proof correctly obtains a different norm after restriction to the space generated by squarefree monomials of norm at most \(X\). The norm cutoff is divisor closed, so changing from ordinary monomials to centered monomials preserves that space. The squared norm of the projected likelihood is exactly
\[
K_X^2
=\sum_{N\mathfrak r\le X}
 \prod_{\mathfrak p\mid\mathfrak r}
 \frac{\Delta_{\mathfrak p}^{\,2}}{1-b_{\mathfrak p}^{\,2}},
\]
with the finite prime-support restriction understood. Orthogonality gives the formula, and the projected likelihood itself gives equality in the comparison norm on the entire linear space.

The coefficient majorant, fixed divisor bound, and ideal counting yield
\[
K_X^2\ll X^{\max(1-2s,0)+\varepsilon},
\]
with bounded cost for \(s>1/2\). This bound is not inferred by replacing a truncated sum with the full product at the endpoint.

A \(2k\)-th moment has frequencies inside the stated norm envelope \(X=(2D)^{2k}\). The rowwise comparison and Cauchy inequality give
\[
F_{k,s}\le J_H^{1/2}K_X F_{2k,t}^{1/2}.
\]
The input on the right is a \(4k\)-th moment. The proof does not obtain a same-order comparison by renaming this input. If that input satisfies the appropriate diagonal estimate, the loss \(D^{k\max(1-2s,0)+\varepsilon}\) follows.

The exact norm and its extremizer concern the entire finite frequency space. They do not establish the optimal comparison constant on the smaller cone of actual nonnegative Hecke-family moment polynomials. This distinction is explicitly retained.

### 2.3 Prime subsequences and the endpoint \(s=1/2\)

I checked the prime-rich-subsequence argument using the Eisenstein ideal count, the simple pole of \(\zeta_K\), the logarithmic singularity of the prime Dirichlet series, and Mellin inversion against a nonnegative annular weight. A hypothetical uniform power saving in the prime-weighted sum would continue its Mellin transform through the singularity. This supplies arbitrarily large prime-rich scales without inserting a prime number theorem.

It follows that the full product \(\Gamma\) is bounded for \(s>1/2\), diverges at \(s=1/2\) with at most a polylogarithmic bound, and has superpower growth along a subsequence for \(s<1/2\). The finite frequency-space comparison instead has the stated power exponent; products of \(2k\) distinct primes in the annulus give its lower bound. The upper and lower bounds use the same allowed norm cutoff.

The infinite product-law statements also check. Above \(1/2\), forward and reverse likelihoods converge in \(L^2\), with expectation one, giving mutual absolute continuity. At and below \(1/2\), the accumulated squared bias difference diverges. A normalized sum of centered local signs, Chebyshev's inequality, and a subsequence suitable for Borel–Cantelli give disjoint almost-sure limit events for the two laws. The argument includes the degenerate target law at \(s=0\).

Infinite-law singularity at \(s=1/2\) is compatible with a subpower finite comparison cost there. The note does not conflate these claims.

### 2.4 Positive-noise floor and zero extraction

For each fixed \(t>0\), a prime on the column annulus has no proper multiple remaining on that annulus. Consequently its coefficient in the centered expansion is the isolated prime coefficient, without contamination from shorter column terms. A row of norm at most \(D^h\) can be divisible by only a bounded number, depending on fixed \(h\), of these primes. The local variance is at least \(1-D^{-2t}\).

Combining the prime-rich subsequence with orthogonality therefore gives the lower second-moment scale uniformly over the physical rows. Jensen and row counting give
\[
\lambda_{k,h}(t)\ge h+k.
\]
This is a fixed positive-noise assertion. It does not provide a floor at \(t=0\), or a uniform statement for an unspecified sequence \(t=t(D)\).

The expectation identity is
\[
\mathbb E_t\mathcal A_u(D;W)
 =D^{-t}A_u(D;W_t),\qquad W_t(x)=x^{-t}W(x).
\]
I checked the norm shift, Jensen step, replica budget, and Mellin exponent in the zero-extraction argument. Extraction uses the specified universal nonvanishing detector; an arbitrary test function need not have the required nonvanishing Mellin transform. Its shifted transform is nonzero in \(\Re z>t\).

Conditional on the stated extraction machinery, the damped bound with loss \(e\) gives the strict zero-free region
\[
\Re z>\frac12+t+\frac{5h}{12k}+\frac{e}{2k}.
\]
The corresponding lower growth implication for a fixed zero with \(\beta>t\) is
\[
\lambda_{k,h}(t)\ge 2k(\beta-t)+h/6.
\]
The contradiction argument chooses a positive intermediate exponent, and its weighted integral has strictly negative excess exponent. It does not require simultaneous alignment of record scales for different moment orders.

The upper calibration using \(PW_B\),
\[
\lambda_{k,h}(t)
 \le h+k\max(1,2B-2t),
\]
retains the actual conductor-uniform pointwise hypothesis. A supremum of zero real parts is not substituted for that hypothesis. Fixed-test and stronger uniform test-family quantifiers remain distinct. The use of \(h_k=o(k)\) is a sequence of fixed-order exponent statements, not an unproved uniform estimate for \(k\) growing with \(D\). At the threshold \(t=B-1/2\), this calibration returns the same boundary \(B\); it does not by itself improve it.

## 3. Parity note §§7–9 and supporting interfaces

### 3.1 Quantifiers and de-damping

I checked the multiplicative coefficients including their zero masks, the full cubic environment on which the Walsh coefficients depend, and the parity radical of the tuple product. Inactive local factors are treated through vanishing coefficients. The baseline is not silently replaced by the principal complete-residue kernel.

The pointwise premise \(PW_b\) is stated over all allowed shorter column scales with the same physical row range and the stipulated test control. The optional weighted second-moment input is separately named; it is not deduced from the row-weight mass condition alone. The centered coefficient is the appropriate shorter inverse sum with its enlarged coprimality mask and nonempty-support floor.

Jensen's de-damping identity and its weight change are correct. Applying Jensen to the additional-second-moment bound in Theorem 6.3 gives the de-damped excess exponent
\[
2kt+(k-1)(2b-2t-1)_+.
\]
At the threshold \(t=b-1/2\), this equals \((2b-1)k\), including when the additional second-moment input is available. At \(t=0\), it instead equals \((2b-1)(k-1)\). The second-moment input therefore does not save that constant-order portion after threshold de-damping. This paragraph clarifies the wording of this review receipt; the published mathematics and the scoped review verdict are unchanged.

The randomized second-moment equivalence requires identical ambient, shorter-scale, row, and test quantifiers on both sides. The converse implication from all fixed averaged moment orders yields an individual bound at the top column scale by choosing a sufficiently large fixed order. It does not automatically supply all shorter-scale bounds at the same row height.

The generic bounded-coefficient reverse example has the claimed moment exponent \(2k(1-t)\) and undamped value of order \(D^{2k}\), so the reverse power cost is attained in that larger coefficient class. It is not presented as an actual fixed Hecke row.

### 3.2 Integer envelope and the common-spike witness

The equal-scale fixed-product norm inputs are explicitly granted source-qualified estimates. Their normalized exponent envelope is
\[
F_h(j)=\max\{j,\;2j-5h/6,\;5j/3-h/3\},
\qquad j\in\mathbb Z_{\ge1}.
\]
I reconstructed the breakpoints \(h/2\) and \(3h/2\), the real-variable comparison, and the need to maximize over actual integer degrees. The finite list of neighboring integers, together with \(j=1\), suffices because the pieces are affine and the final slope of \(2bj-F_h(j)\) is nonpositive.

With \(a=2b-1\) and
\[
\delta=\max\{a,\sup_{j\ge1}(2bj-F_h(j))\},
\]
the common-spike array with amplitude \(D^b\) and support density \(D^{-\delta}\) satisfies the stipulated pointwise, second-moment, and every fixed integer product-norm constraint. Balanced signs give zero mean. For \(h>1\), the bound \(\delta<h\) allows a literal finite-row realization with the same exponents. The construction does not claim an arithmetic realization of the Hecke family.

Thus any inference using only these specified norm constraints must retain the lower loss
\[
e_k\ge (2b-1)k-\delta.
\]
For \(h_k>1\) and \(h_k=o(k)\), the resulting cofinal lower loss is \(\liminf e_k/k\ge2b-1\). Constants depending on fixed moment order do not remove this exponent obstruction. The upper subset-product comparison agrees with the witness in the stated ranges.

I separately checked the arithmetic at \(b=7/8\), including \(\delta=3/4\) for \(1<h\le7/4\), the change immediately above \(7/4\), and the counting endpoint \(b=1\) with its range \(h\le6/5\). These are statements about the specified integer norm data, not about all exact arithmetic identities and all unequal-scale test families.

### 3.3 Cumulants and resampling

For a fixed even order, the one-block term in the cumulant of the symmetric sparse spike contributes its support density once. Every other nonzero partition contributes at least its square. Hence
\[
\kappa_m=D^{mb}(p+O_m(p^2)).
\]
Rewriting moments in connected terms therefore does not remove this particular spike exponent. The argument does not preclude new estimates exploiting additional arithmetic information.

The complete-residue conditional cancellation is correct: a nonzero uniform sixth root is equivalent to an independent quadratic sign and cubic value. Conditional on the complete cubic data, each active quadratic sign remains fair. At a zero local value the corresponding nonempty coefficient vanishes. This proves the asserted nonempty-Walsh cancellation for complete residue classes. No short physical row weight is inserted into that identity.

For the resampling obstruction, two rows in the norm ball have difference norm at most \(4H\). If they agree modulo every prime except \(\mathfrak p\), and \(N(\mathfrak Q/\mathfrak p)>4H\), divisibility forces them to be equal. The full-residue-coordinate heat-bath move is then the identity on the conditioned physical row set; its Dirichlet form vanishes. This rules out a nontrivial spectral or logarithmic-Sobolev inequality from that particular chain on a nontrivial conditioned distribution. It does not rule out chains on coarser character coordinates.

## 4. Independent executable replay

### 4.1 Commands and byte comparison

The commands below were run from the scratch working directory containing a byte-exact copy of the committed source. Python was version 3.12.14.

```sh
python attack4_theta_review_sources/checks/verify_cubic_fibers.py \
  --note attack4_theta_review_sources/CUBIC_FIBERS_AND_RIESZ_PRODUCTS.md \
  --output attack4_theta_cubic_replay.json

python -O attack4_theta_review_sources/checks/verify_cubic_fibers.py \
  --note attack4_theta_review_sources/CUBIC_FIBERS_AND_RIESZ_PRODUCTS.md \
  --output attack4_theta_cubic_replay_optimized.json
```

Both commands exited with code 0 and reported:

```json
{"report_sha256":"68c4c47d5c1389ec2c63f6546b01ede6a9e25d6b161b996913a3a837c34df64e","status":"PASS","total_predicates":38577}
```

I compared the two generated files and the freshly fetched committed result with direct byte-array equality. All three pairwise comparisons were true. Their common SHA-256 is the committed result hash in §1. A final byte-identity check when sealing this report again found both generated outputs identical to that committed result.

### 4.2 Acceptance conditions and actual scope

I read the checker in full. It uses standard-library exact integer and rational arithmetic. Acceptance conditions are explicit exception-raising checks, so optimization does not disable them. The checker does not read a precomputed PASS result to decide acceptance. It records the executed checker and supplied proof hashes, computes its report, and writes the report after all checks succeed. The explicit note argument avoids any ambiguity in its fallback filename search.

The field fixtures use the split prime fields of orders 7, 13, and 19, with the documented images of the Eisenstein root. Sextic powers are evaluated in those fields; roots are represented by exact Eisenstein pairs with exact multiplication, conjugation, and norm. Literal local zeros are exercised.

The complete CRT fixture enumerates all 1,729 residues modulo \(7\cdot13\cdot19\), including all 1,296 unit classes. Separate Eisenstein-coordinate tests cover the cube identities and their masks. Finite native coefficient arrays include rational weights and a multiplicative sextic phase. They test the stated finite identities; they do not instantiate every parameter of one asymptotic smooth Hecke family.

The checker tests the Riesz identities for several rational biases and fixed moment orders, centered orthogonality, divisor-closed projected likelihoods, exact comparison inequalities, parity-frequency support, order doubling, the isolated-prime variance floor, and exponent algebra. Its adversarial guards reject an omitted auxiliary zero mask, an incorrect cubic row cost, sixth-power substitution, an incorrect Riesz sign, full-product substitution for the truncated cost, a non-divisor-closed basis replacement, contaminated prime coefficients, and an incorrect positive variance floor at zero noise.

| Diagnostic group | Predicates |
|---|---:|
| Adversarial guards | 8 |
| Centered basis | 192 |
| Exponent algebra | 40 |
| Likelihood | 54 |
| Moment frequency | 170 |
| Native CRT | 5,414 |
| Native cube masks | 21,609 |
| Native field setup | 66 |
| Native ring | 2,499 |
| Prime floor | 41 |
| Projection | 600 |
| Riesz native law | 36 |
| Riesz native moment | 7,848 |
| **Total** | **38,577** |

This replay validates the listed finite computations and report reproducibility. It does not numerically establish prime-rich subsequences, infinite-product singularity, an asymptotic moment estimate, \(PW_b\), a zero-free region, or a short-row completion. I did not run or claim an independent audit of the companion parity checker as part of this assigned review.

## 5. Conclusion and remaining scope

The exact source commit passes this nonauthor review in the requested scope. The strongest distinctions relevant to subsequent work survive examination: full and frequency-restricted comparison costs differ; the endpoint finite comparison is compatible with infinite-law singularity; the noise floor requires fixed positive noise; detector and pointwise-bound quantifiers remain explicit; the spike construction obstructs a specified norm-only inference; and complete-residue cancellation does not supply cancellation on short physical rows.

The source-qualified causal, pointwise, and fixed-product analytic inputs remain hypotheses or imported results with their stated scope. This review supplies no estimate for the unresolved signed physical covariance and no upgrade from the method-specific obstruction to an impossibility theorem for the arithmetic family. It does not certify the full generalized \(2k\)-th moment result or RH.

This receipt applies to the exact identities in §1. Mathematical changes require a new review of the changed material.

