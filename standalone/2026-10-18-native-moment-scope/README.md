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
   Its sharp order dependence is also identified: for fixed 0<sigma<1,
   `log C_sigma(r) ~ [sigma/(1-sigma)] * (sigma r/log r)^(1/sigma)`.
   This saves logarithmic factors in the stated growing-order transfer,
   when the native source envelope is supplied. The fixed-order mean has
   an exact leading constant; large masks have a sharp logarithmic tail,
   with the lower bound's family-size range explicit. See
   [MASK_ASYMPTOTICS.md](MASK_ASYMPTOTICS.md).
2. **The full target's exact strength.** #976's stated growing-family target
   is equivalent to GRH for every primitive Hecke member represented by
   that fixed family. A logarithmically growing second-moment target has
   the same strength. The claim is not extended to arbitrary Hecke families.
3. **A target confined to the principal sector.** All principal b^6 rows,
   with their original masks and repetitions retained, need only field RH.
   Their natural row count is H^(1/6) at original height H. The exact native
   all-order growth abscissa equals the corresponding rightmost-zero
   supremum. More strongly, the complete principal FIRST ABSOLUTE moment at
   ANY positive polynomial replica height already has field-RH strength,
   by a finite prime-replica bootstrap. Any one fixed positive moment order
   suffices. At each fixed even order its growth exponent
   is exactly b0+2k Theta_F. The full family has the separate finite-order
   enclosure in PROOF.md (20b).
4. **An explicit high-order native bound from a named external input.** Taking
   CT v2's printed 31/32 finite-order Hecke theorem as an explicit input gives
   `sum_(Nu<=D^h)|A_u(D)|^(2k) << D^(h+31k/16+epsilon)`.
   At h=1,k=32 this improves #976's displayed S6 exponent from 385/6 to 63,
   a power gain of 7/6 in the complete native 64th moment. It recovers its
   input boundary, and is not an independent proof or improvement of it.
   PROOF.md §10 then mixes the primary DF zero-density theorem with that
   CT envelope, for the exact untwisted DF sextic family. It further gives
   `D^(h+61k/32+epsilon) + D^(108h/485+31k/16+epsilon)`.
   At h=1,k=32 the exponent is 30178/485, a gain of 5657/2910 over #976's
   displayed S6 exponent. For each fixed k>=280h it also gives
   `D^(h/6+31k/16+epsilon)`, retaining the natural replica height cost.
   Both imported inputs, every partial core height and the finite-height
   contour argument are explicit; every exceptional core is retained.
5. **An explicit exceptional-core count.** If R flat cores are omitted at
   height H, their full sixth-power replicas occupy at most
   `O(H^(1/6) R^(5/6))` rows. A single fixed core has asymptotically a
   positive constant times H^(1/6) replicas. PROOF.md §9 quantifies the
   remaining distinction from #984's good-family and capped inverse-L
   moments, and states the maximal native premise that would permit a
   deterministic transfer with the exceptional contribution retained.
   A second adapter gives the exact weighted vertical reciprocal moment
   sufficient for that transfer, with the contour hypothesis explicit.
   The cofinal native criterion also tolerates deletion of
   `o(D^(h/6)/log D)` actual full rows; core exceptions have a different cost.
   No analytic input from that proposal is used.

Read [PROOF.md](PROOF.md) for the exact statements and complete deductions,
and [ANALYTIC_ADAPTER.md](ANALYTIC_ADAPTER.md) for the conductor-uniform
reciprocal lemma. The unconditional identities, mask-average lemma and
abscissa classification do not assume CT's zero-free theorem. The numerical
native bounds in PROOF.md §§8,10 explicitly assume that theorem; §10 also
adopts the separately stated primary DF zero-density estimate.

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

The deposited [GAUSSIAN.json](GAUSSIAN.json) encloses the actual tau=1,c=0
native Gaussian at D=1,2,...,4096 along the powers of two, over EVERY
principal masking ideal Nb<=64. It computes all norm coefficients through
16,777,216 and adds a directed bound for the complete infinite upper tail.
An explicit S-deleted ideal-count envelope and exact Stieltjes boundary
count sharpen that tail. The coarser bounds remain as fallbacks; a wrong
inert-prime density or an overstated boundary count is rejected.
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
Six isolated Lean lemmas also check the finite mask algebra, fixed-order
quantifiers and geometric exponent bootstrap; [FORMAL.md](FORMAL.md)
states exactly what was typechecked.
