# Validation and independent-review boundary

Status: proposed mathematical component proofs, not independent acceptance.
The all-set, all-depth and countable-state arguments are paper proofs. The code
below is a bounded algebra/finite-source certificate, not a proof of RH or a
machine proof of those analytic arguments.

## Executed mathematics

Both commands reconstruct the identical JSON (ordinary and optimized Python):

    python -I -S -B check.py --check result.json
    python -I -S -B -O check.py --check result.json

Acceptance uses only the Python standard library, integers and Fraction.
There is no floating calculation, zeta/gamma/zero oracle, imported producer,
parent code execution or numerical quadrature in the checker.

The bounded coverage is explicit:

- 256 prime-factor versions of sum_(d|n)Lambda(d)=log n, with 255 primality
  classifications independently compared against trial factorization.
- 54 directed rational logarithm enclosures through the primes <=256, including
  the lower coefficient minorants; log2 endpoints are separately checked.
- 10,062 finite descendant/omega comparisons, over initial intervals N<=80.
  Repeated subcases at different N are counted as comparisons, not theorems.
- Twelve finite divisor-closed sets, 48 signed rational test vectors and 133
  exact positive grounded LDL pivots. These are controls, not all-N evidence.
- One actual full N=32 prime-power inverse quadratic: all 65 edges, all ten
  prime bases and 31 exact positive LDL pivots for K_minus-M/384. The finite
  floor is independently established, so this finite inverse enclosure does
  not require accepting the general gap theorem. All original metric factors
  and off-diagonal terms are retained.
- 136 finite coherent-channel checks distinguish its sign from the gap on
  its complement. These algebraic controls are not actual-xi counterexamples.

For the actual inverse the exact rational interval is stored in result.json.
It proves 0.7444806194657 < b^T K^(-1)b < 0.7444806194659. The final residual
budget is less than 10^(-13), and every logarithm is enclosed before the
matrix or residual arithmetic. The lower endpoint comes from the variational
trial; the upper endpoint adds the COMPLETE inverse residual budget.

## Directed logarithm contract

For rational x>=1, write x=2^k r with 1<=r<2. For z=(r-1)/(r+1), sum 80 terms
of 2 sum_(j>=0)z^(2j+1)/(2j+1). The complete positive remainder is at most
2 z^161/[161(1-z^2)]. The same series evaluates log2 at z=1/3. Rational
endpoints are converted OUTWARD to the fixed denominator 2^160. Every later
interval product is a rational scalar multiplication with floor/ceiling;
the result certificate contains the exact endpoints, not rounded displays.

## Exploration excluded from evidence

Non-directed NumPy/SciPy eigenvalue reconnaissance looked at full graphs up
to N=4096 and the prime-removal subtrees. It suggested trying a spectral gap,
but proves no gap, and its values are not used by the theorem or checker.
A non-directed solve at N=32 selected the displayed rational trial rounded
to denominator 10^8. Directed replay, not the floating objective, certifies it.
No uniform positive absolute-constant spectral gap is claimed or refuted.

The paper proof uses a sharper prime-weighted tree argument, not an
extrapolation from these finite spectra. All required arithmetic estimates
are re-proved with their constants. General path comparison, Markov-form
and Schur-complement methods are classical; the limited literature search
is not an exhaustive novelty audit.

## Actual CLI rejection and package checks

In EACH Python mode, test_rejections.py first runs a pristine validator and
mathematical checker, then rejects six altered results and four altered
packages. The result changes include a false RH flag, false inverse endpoint,
changed fixed trial, Boolean/float count aliases and duplicate JSON keys.
Modified results are resealed so their rejection is by reconstruction, not
just a hash mismatch. Package changes include altered proof, resealed extra
file, missing claim ledger and a symlink. Symlink tests execute on Linux;
no Windows execution is claimed.

The exact eleven-file inventory and ten checksum entries are validated.
The complete final packet is also applied as an add-only patch in a temporary
Git fixture, preserving an unrelated sentinel, and rechecked after ZIP
extraction. This is not a full repository checkout or remote CI run. The
remote commit/receipt authenticates the published bytes; a mutable local
checksum file alone is not an independent trust root.

No Lean, Comparator, full repository suite, parent mathematical campaign,
actual critical prime-energy bound or independent referee acceptance is
claimed. No previous source or reviewed claim is modified by this packet.
