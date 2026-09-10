# SSQ26 validation and the limits of the evidence

The mathematical statements are proposed component proofs. No code execution
is an independent proof of Brun--Titchmarsh, Cramer's conditional theorem,
Hardy uniqueness, or a global ordinary-prime energy upper bound.

## Exact finite reconstruction

The final check is Python standard-library-only and uses no `assert` for
acceptance. It reconstructs seven groups:

1. Seven rational frequency checks of the stable adapter and inverse.
2. Five finite weighted projection/variance controls.
3. 127 exact square-cell geometry/control cases, n=2,...,128.
4. The integer sieve through 16384 checked against independent trial division
   over the same entire range; 1900 primes are present. This is finite source
   authentication, not a count of analytic theorems.
5. 126 square-cell prime counts checked against directed logarithmic BT
   inequalities. The infinite BT theorem is imported, not proved by these.
6. Six full finite endpoint-sample energy prefixes M=4,8,16,32,64,128,
   comprising the 126 summands n=2,...,127. These are different prefixes
   of one computation, not six independent implementations.
7. Eight exact signed discrete work/endpoint identities on synthetic data.

The directed primitive arithmetic uses 160-bit dyadic intervals. Logarithms
are reduced to [1,2] and evaluated by 72 atanh terms with the complete geometric
remainder. For x=n^2, Li_2(x) is evaluated as

    log(log(x)/log(2))
       +sum_(k=1)^128 [log(x)^k-log(2)^k]/(k k!) + remainder.

All n<=128 satisfy log(n^2)<10. The nonnegative remainder is bounded by

    10^129/[129*129!*(1-10/130)].

All multiplication, division, logs, power series, and squared discrepancies
are rounded outward using integer floor/ceiling. No library Ei/li/log, floating
quadrature, zeta or gamma call is used. Every prime up to the declared finite
cutoff is reconstructed. No infinite coarse tail is set to zero or included
in the reported sample prefix.

The final result SHA256 is
`e7a80214068439ae01bb3714825634dd821480117d6ac1f478546725d2edbe06`.
Normal and optimized isolated Python runs agree byte-for-byte with result.json.
The output's `rh_proved` and `global_coarse_tail_certified` fields are false.

## Real command-line rejection controls

In each Python mode, the pristine byte validator and mathematical checker pass.
Six altered retained results are rejected by a complete fresh check: false RH,
false global tail, float alias, missing prefix, false directed endpoint, and
duplicate JSON. Four altered packages are rejected by the actual byte validator:
changed proof, removed file, extra file, and a symlink substituted for a payload.
Thus there are twelve result refusals and eight package refusals across the two
modes, plus four pristine controls. The symlink controls ran on Linux; no native
Windows behavior is claimed. The two mode summaries are byte-identical.

A checksum is integrity relative to the manifest, not an external mathematical
signature. Altering and reauthoring both mathematics and manifest is outside
that guarantee. The check command reconstructs its numerical records instead
of merely accepting internally consistent JSON.

## Source and publication boundary

The parent proof was read in full and its length, SHA256 and Git blob matched
its frozen source. Parent mathematical checkers, historical experiments and
formal builds were NOT rerun. The new proof imports only the coarse classical
interval BT upper bound for its unconditional local theorem. Yamada's stronger
numerical constant and computational certificate are not used.

Non-directed mpmath reconnaissance (35 digits) evaluated the six finite sample
prefixes to choose readable display brackets. Those values are not evidence;
the directed primitive reconstruction independently certifies the fixed brackets.
No actual infinite energy, growing-cutoff convergence or entropy is evaluated.

The packet has twelve files, with eleven checksum entries. An add-only patch
and ZIP are provided. The patch is tested by applying it to a fresh temporary
Git repository with an unrelated sentinel, checking every resulting byte, and
replaying both modes. This is not a full Riemann checkout or remote CI run.
No external novelty, independent referee acceptance, Lean/comparator result,
new zero-free region, or RH proof is claimed.

## Reproduce

    python -I -S -B validate.py
    python -I -S -B check.py --check result.json
    python -I -S -B -O check.py --check result.json
    python -I -S -B test_rejections.py
    python -I -S -B test_rejections.py --optimized

With a parent checkout available, additionally run

    python -I -S -B validate.py --parent-root /path/to/parent/checkout
