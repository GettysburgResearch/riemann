# Validation, source identity, and review scope

**Disposition:** proposed standalone mathematics. These records support
the stated scoped deductions; they are not an RH certificate, a formal
proof, an external expert endorsement, or acceptance into the integrated
record.

## 1. Frozen mathematical sources

| File | SHA256 |
|---|---|
| EULER_TRACE_RESONANCE.md | c8931a93f3fc47805143ab4074ca4e315656a87e58abd5e0e7ba59c03079fb10 |
| RESONANT_SHORT_TRACE.md | 1c043c4650e72d9c78daef4111a3a2485c6f5d285a1ca2afee62283c9286a70f |
| SHORT_FACTOR_NONSMALLNESS.md | 0af49f68a90bc19253e6543abd2e8d8af295a2bb133c5ebb59686e516655a935 |
| HORIZON_NECKLACE_FACTORIZATION.md | a6aa7ab8925eac3f1f514b6e4138baa87735e3902fa3c5a78679480c7cf925ab |
| CONJUGATE_PAIR_CONDUCTOR_SIEVE.md | 220d767a03ed6c61b8e5a3ea34b48a0a2adae92607047fbfa0bb96e5be876ef2 |
| CONDUCTOR_COROLLARIES.md | 49d471154fbfb2b8589742a70343f9abfa8e407172648b73f33a14d5f3e3031d |
| PRIME_DEGREE_COHERENCE.md | 2290ce3d8d24f832259b3d701607beb125ceb5111f86b39d82be200eea1c27fb |

The packet's [manifest](MANIFEST.json) records file sizes, SHA256 values
and Git blob identities. [PROVENANCE.json](PROVENANCE.json) separately
binds every copied external repository source to its immutable commit,
source path and original Git blob. All eleven source transports were
checked against those Git blob identities, including the final newline.

The mathematical content is frozen in one Git commit before the final
publication receipts. [PUBLICATION_RECEIPTS.md](PUBLICATION_RECEIPTS.md)
records that exact commit and the subsequent read-back. A later receipt
commit does not change the reviewed mathematics. The manifest excludes
itself and the publication-receipt file to avoid a circular self-hash.

## 2. Authorship and independent reconstruction

The agents belong to the same team and can share the same model. Their
fresh derivations and adversarial checks provide useful scrutiny, but
their agreement is not external certification. The reports explicitly
disclose development overlap.

| Mathematical object | Authoring lane | Review evidence |
|---|---|---|
| Original Euler trace refutation | Extraction | [Native reconstruction](reviews/resonance_native.md), [bilinear reconstruction](reviews/resonance_bilinear.md), [root reconstruction](reviews/root_reconstruction.md) |
| Short-factor analytic lemma | Extraction | The same native, bilinear and root reconstructions; extraction's own contribution is not counted as an independent review |
| Subcritical CT1 composition | Root, with earlier extraction input | [Native review](reviews/resonance_native.md), [bilinear review](reviews/resonance_bilinear.md), and [extraction review](reviews/resonance_extraction_initial.md) with [final update](reviews/resonance_extraction_update.md) |
| Necklace/horizon representation | Root; native suggested the smooth plateau and authored its finite diagnostic | [Extraction review](reviews/necklace_extraction.md) and [native review with overlap disclosed](reviews/necklace_native.md) |
| General-order pair sieve and native accounting | Bilinear | [Extraction review](reviews/conjugate_pair_initial.md), [final update](reviews/conjugate_pair_update.md), and [root reconstruction](reviews/root_reconstruction.md) |
| Conductor corollaries and the bound-envelope limit | Bilinear | [Extraction review](reviews/conductor_corollaries.md) and root reconstruction |
| Signed distinct-prime sector, deformation and rooting | Native | [Bilinear review](reviews/prime_degree_bilinear.md) and root reconstruction |
| Packet summary | Root | [README scope audit](reviews/readme_scope.md) |

These reviews reconstruct the written proofs and identify their named
analytic inputs. They do not reprove the full external large sieve,
prime ideal theorem, or every earlier repository branch.

### Corrections made during the reviews

The history directory preserves the earlier conductor, CT1 and native
drafts relevant to initial review hashes.

- **Conductor:** the final proof explicitly applies Cauchy to two
  coefficient vectors produced by Mellin separation; specifies the
  primitive background associate before coefficient zero extension;
  distinguishes all locally primitive powers at orders three, four and
  six; and fixes a compact smooth radial row majorant.
- **Necklace:** the general ideal-coefficient theorem is distinguished
  from the Eisenstein element-row trace, whose two-dimensional lattice
  gives the factor \(H\). The same-side pair description retains the
  fixed \(\nu^2\) twist, rather than calling the complete character
  cubic.
- **Native prime sector:** the final prose refers to the proved
  all-distinct restriction, not an undefined graph-connected selector.
  The prime-rooting unit-companion identification with the untwisted
  prime polynomial is restricted to \(\nu=1\).
- **CT1:** malformed inline delimiters were repaired, fixed-\(Y\) row
  absolute convergence was written out, and the separate P13 refutation
  was cross-referenced. Its theorem did not change.
- **README:** the trivial datum in both refutations and the prime
  lower bound, the nonnegative norm test, the \(\delta\) range, and
  the general-order field condition were made explicit.

A historical verdict is not silently reused for changed text. The
updated reports bind the final hashes displayed above.

## 3. Exact finite diagnostics

All three principal diagnostics use Python's standard library only.
Their arithmetic consists of integers, exact rational numbers, exact
finite-field powers and exact arithmetic in the indicated quadratic
field. There is no floating-point acceptance margin, interval
rounding claim, or numerical passage to an asymptotic theorem.
Acceptance uses explicit exceptions, so it is unchanged by
\(\mathtt{python\ -O}\).

The root researcher ran both modes from the copied repository sources
and compared each report pair byte-for-byte. The native report was
rerun after its final prose scope correction; the checker itself was
unchanged.

### 3.1 Conjugate-pair arithmetic and exponent accounting

Producer: [check_conjugate_pair.py](check_conjugate_pair.py).

It reconstructs sextic residue values at the split Eisenstein prime
ideals of norms \(7,13,19\), including zero values. Its declared finite
grid covers:

- 111,132 conjugate-pair identities and 111,132 reflected recombination
  identities;
- 8,064 common-divisor mask identities;
- actual nonunit cases and deliberate wrong-power, deleted-mask and
  restored-nonunit controls;
- 88 Poisson monomial substitutions and 66 AFE substitutions at orders
  \(3\) through \(24\);
- the exact rational feasible fourth-tuple comparison and all four
  cleared-denominator sector conditions.

The proof for all \(n\ge3\) is the symbolic argument in the manuscript.
Sampling those orders is not its justification.

Reports: [ordinary](checks/conjugate_pair.json) and
[optimized](checks/conjugate_pair.optimized.json), identical SHA256

\[
\mathtt{2618f1a052b20e2c5c72a5238f254e2210f8b6db45f72a3fa3a0a3c6e5824c2e}.
\]

### 3.2 Signed partition, prime masks and rooting

Producer: [check_prime_degree.py](check_prime_degree.py).

It checks 57 exact complex vectors for the partition identity, 171
instances of the explicit collision inequality, 150 finite-field
sixth-power masks, 31 formal prime-rooting coefficient cases, and
10,368 exact rational threshold comparisons. It includes deliberate
incorrect partition coefficients, zero restoration and rooting signs.

Reports: [ordinary](checks/prime_degree.json) and
[optimized](checks/prime_degree.optimized.json), identical SHA256

\[
\mathtt{45f5bbd0b008252a65b7b6ecf2ec2e61ef8e148f0cff33bff4ddf473cbd9dc3c}.
\]

These checks do not establish the prime ideal theorem, the asymptotic
signed lower bound, the Dedekind zeta continuation, or the moment
limsup. Those are deductions in the written proof from named inputs.

### 3.3 Primitive necklaces and physical coefficient rectangles

Producer: [check_necklace_horizons.py](check_necklace_horizons.py).

It independently enumerates 1,183 primitive cyclic-word orbits, checks
16 local remainder cases, and compares the full coefficient reunion
on seven physical rectangles. The rectangles include unequal horizons,
separate prime-ideal labels with equal norm seven, literal zero slots,
and signed phases. The checker catches:

- a cutoff too small to preserve the physical coefficients;
- one copy in place of the required two at a three-distinct-letter
  monomial;
- a spurious imprimitive one-letter factor;
- replacement of a principal nonunit zero by one.

The finite coefficient algebra is more general than the selected
native row phases. Its finite phase cases are not claimed as a full
arithmetic row census.

Reports: [ordinary](checks/necklace_horizons.json) and
[optimized](checks/necklace_horizons.optimized.json), identical SHA256

\[
\mathtt{9f8a8b6352c85a956bd6ea74fd66f9a1da866135296bb7edfbbe51cb5c62ce10}.
\]

The normal convergence and all-horizon transport are proved in the
manuscript. They are not inferred from these rectangles.

## 4. Reproduction commands

Run from this packet's directory:

~~~sh
python check_conjugate_pair.py --proof CONJUGATE_PAIR_CONDUCTOR_SIEVE.md --report checks/conjugate_pair.json
python -O check_conjugate_pair.py --proof CONJUGATE_PAIR_CONDUCTOR_SIEVE.md --report checks/conjugate_pair.optimized.json
python check_prime_degree.py --proof PRIME_DEGREE_COHERENCE.md --report checks/prime_degree.json
python -O check_prime_degree.py --proof PRIME_DEGREE_COHERENCE.md --report checks/prime_degree.optimized.json
python check_necklace_horizons.py --proof HORIZON_NECKLACE_FACTORIZATION.md --report checks/necklace_horizons.json
python -O check_necklace_horizons.py --proof HORIZON_NECKLACE_FACTORIZATION.md --report checks/necklace_horizons.optimized.json
python verify_packet.py
~~~

The integrity verifier checks the manifest, copied source identities,
report/proof/producer bindings, and byte equality of the paired reports.
Its optional \(\mathtt{--replay}\) mode reruns the three diagnostics
into temporary files and compares their exact bytes with the recorded
reports. It is a transport and finite-diagnostic verifier, not an
analytic proof checker.

## 5. Smallest failure points and boundaries

- The Euler refutation would fail if the chosen fixed cross-pair mask
  were not legal or if any row could be negative. Both are proved from
  the exact source allocation and local factors.
- The CT1 refutation additionally needs simultaneous non-smallness of
  the actual product on the opposite-cluster interval. The elementary
  interpolation lemma supplies that exact statement.
- The necklace repair needs absolute coefficient convergence after
  degree \(J\), and the fact that an oversized column cannot be made
  smaller by another factor. Both are proved with nonnegative
  coordinate exponents and all masks retained.
- The conductor extension needs the primitive squarefree root-number
  split and correct reflected orientation before positive norms.
  These are its load-bearing imported interfaces, not finite
  numerical assertions.
- The signed prime lower bound needs the whole row-summed partition
  error, rather than a positive-row lower bound for an indefinite
  quantity. The explicit U-statistic inequality supplies it.

No native moment estimate is inferred from a random model, a finite
prime sample, a larger unfiltered trace, an absolute conductor mean,
or an exact representation alone. The target remains the complete
signed native prime/composite cancellation with the original norm
tests and source uniformity.
