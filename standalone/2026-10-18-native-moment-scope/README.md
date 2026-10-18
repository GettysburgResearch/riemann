# Native all-moment sharpening and the exact remaining target

Status: **PROPOSED mathematics; independent review required.** No new
zero-free half-plane or RH proof is claimed. This is a separately labeled
continuation of #976 at `bf845aa1d9d06b0ce62440edc5726de997a888db`.

## What improves

The latest packet proves an all-order theta theorem and identifies an open
native Möbius moment target. This continuation advances the native side:

1. **An exact source adapter.** Every repeated row a b^6 is a literal Euler
   deletion of the a row. Its Gaussian equals a complete smooth-ideal
   convolution of that same native source; the finite inverse is explicit.
   The average of the resulting Euler-mask mass over Nb<=B costs O(B),
   with an explicit convergent Euler-product constant and no B^epsilon loss.
2. **The full target's exact strength.** #976's stated growing-family target
   is equivalent to GRH for every primitive Hecke member represented by
   that fixed family. A logarithmically growing second-moment target has
   the same strength. The claim is not extended to arbitrary Hecke families.
3. **A target confined to the principal sector.** All principal b^6 rows,
   with their original masks and repetitions retained, need only field RH.
   Their natural row count is H^(1/6) at original height H. The exact native
   all-order growth abscissa equals the corresponding rightmost-zero
   supremum, both for the full family and for the principal sector.
4. **An explicit high-order native bound from a named external input.** Taking
   CT v2's printed 31/32 finite-order Hecke theorem as an explicit input gives
   `sum_(Nu<=D^h)|A_u(D)|^(2k) << D^(h+31k/16+epsilon)`.
   At h=1,k=32 this improves #976's displayed S6 exponent from 385/6 to 63,
   a power gain of 7/6 in the complete native 64th moment. It recovers its
   input boundary, and is not an independent proof or improvement of it.

Read [PROOF.md](PROOF.md) for the exact statements and complete deductions,
and [ANALYTIC_ADAPTER.md](ANALYTIC_ADAPTER.md) for the conductor-uniform
reciprocal lemma. The unconditional identities, mask-average lemma and
abscissa classification do not assume CT's zero-free theorem. The last
numerical-exponent corollary explicitly does.

## The latest theta source was checked directly

Fresh direct access to Cureton–Thorner's versioned primary TeX source
succeeded. [CT_INTERFACE_REVIEW.md](CT_INTERFACE_REVIEW.md) maps its actual
reflection, profile bounds, local beta branches, masks and quadratic sieve
to #976's adopted interface. No transcription mismatch was found in those
contracts. [CT_SOURCE_AUDIT.json](CT_SOURCE_AUDIT.json) pins the exact source
bytes and formula spans. This is a partial source-interface review; the
deep upstream metaplectic proof is not thereby independently reconstructed.

## Reproduction

From this directory, with Python 3.12 (standard library only):

```sh
python verify.py
python -O verify.py
python -m unittest -v test_exact
python verify.py --column-cap 4096 --row-cap 512
python verify_manifest.py
```

The extended exact check covers ALL 2,474 Eisenstein integral ideals through
norm 4,096, including 1,241 exterior source columns, and ALL 157 exterior
masking ideals through norm 512. Individual HNF ideals are compared with an
independent rational Euler recurrence. Conjugate ideals, inert and ramified
primes, shared primes, all powers and literal nonunit zeros are retained.
These are finite algebra checks, not an analytic certification.

The separate directed Gaussian experiment needs `python-flint==0.9.0`:

```sh
python -m pip install -r requirements-interval.txt
python gaussian.py --output ../reproduced-native-principal-gaussian.json
python replay_gaussian.py
python -m unittest -v test_gaussian
```

The deposited [GAUSSIAN.json](GAUSSIAN.json) encloses the actual tau=1,c=4
native Gaussian at D=1,2,...,1024 along the powers of two, over EVERY
principal masking ideal Nb<=64. It computes all norm coefficients through
4,194,304 and adds a directed bound for the complete infinite upper tail.
The replay doubles that cutoff and raises precision from 256 to 384 bits.
Individual-ideal low-scale sums are a separate source check. Deliberately
omitting the tail, removing both conjugate primes instead of one, or losing
a conjugate row in BOTH producer and replay is rejected by those distinct
gates. See [GAUSSIAN_CONTRACT.md](GAUSSIAN_CONTRACT.md).

There is also an explicit full sextic Kummer-family replay, including the
nonprincipal rows and their complex phases. It uses every actual ideal
u with Nu<=64, rather than just the principal b^6 sector. Its source and
generator convention are specified in [EISENSTEIN_FAMILY.md](EISENSTEIN_FAMILY.md).

```sh
python verify_kummer.py
python gaussian_native.py --output ../reproduced-native-full-gaussian.json
python gaussian_native.py --replay NATIVE_GAUSSIAN.json
```

The values and moments concern these explicitly specified finite experiments.
They supply no all-scale evidence for either open critical estimate.
[VALIDATION.md](VALIDATION.md) records the exact executed scope and limits;
[SOURCES.md](SOURCES.md) separates fresh reads, adopted inputs and novelty.

For the combined finite reproduction use `python replay.py --intervals`.
An optional `--ct-source <downloaded-TeX>` authenticates the primary input.
Five isolated Lean lemmas also check the finite mask algebra and fixed-order
quantifiers; [FORMAL.md](FORMAL.md) states exactly what was typechecked.
