# ATC29 execution and boundaries

## Accepting calculations performed

The final default report was generated with `python -S -B check.py --write
results.json`, then completely reconstructed and compared with BOTH

```
python -S -B check.py --check results.json
python -O -S -B check.py --check results.json
```

Both return identical canonical SHA256:
`331e41e255c9ed05ba64185340e1d13811f7577a4f46fd161ea14d0aadfe8a81`.

Both `python -S -B test_check.py` and `python -O -S -B test_check.py` passed all
14 methods, zero errors/failures/skips on this Linux host. The symlink refusal
was actually executed. Future hosts lacking symlink permission explicitly skip
that one case rather than report an unexecuted success.

Each suite runs an actual bounded CLI write, pristine check, and changed-report
refusal. That is ONE real mutated-report subprocess per suite, not a campaign
of independent full default-corpus corruption replays. Other type, source-hash,
coverage, constant, correction and scope controls run in-process. CLI children
retain the parent's optimization setting. They use a separately labeled quick
campaign, not the default report.

## Coverage

Default periodic algebra: all 47 denominators q=2,...,48, 38,023 complete cyclic
partial-sum comparisons and 282 directed whole-tail checks. The regression suite
also compares finite exact tail sums with the complete remainder envelope.
These are finite checks of identities used in the infinite written argument.

Default complete native panels: Y=31,63,95,127. Each retains every observation
cell in Y<k<=floor(5Y/4), with all exact source and product coefficients needed
for that reconstruction. Independent scaled-integer Newton products are compared
with both sieve and trial-factorization values. For every composite amplitude,
its activation tail is evaluated from the complete finite harmonic/log formula;
all future dyadic correction blocks are summed until the correction is exactly
zero. Largest auxiliary harmonic argument: 4,194,303. No Mobius computation at
that auxiliary height is claimed.

The high/semiprime/other-high covariance ledger retains its complete mixed term.
At three declared points per panel the full direct high spectral sum is checked
against complementary evaluation. At other points, complementary evaluation is
used, not a second independent exhaustive spectral sum. All tail formulas retain
prime-power logarithms until valid cancellation.

Default larger panels: Y=4095,16383,65535. The accepting local output is computed
from the short-source integer Newton convolution, with its capped-completion
restoration. Two separate finite Mobius methods (prime-sign sieve and
smallest-prime recurrence) check every reconstructed coefficient. These checking
methods DO compute the future local source; they do not supply the short-source
producer with those values. The largest native endpoint is 81,918. Summing the
seven panels' reconstructed coefficient counts gives 107,906 comparisons with
overlap; it is NOT that many distinct new integers or whole square-stage cells.

The large panels compare the chosen semiprime packet with ALL other spectral
modes, not exclusively the high ones. At Y=65535 there are 1,491 primes and
1,110,795 distinct semiprime denominators in the packet. Its exact common-mode
formula is used, not enumeration of one million oscillatory columns.

## Arithmetic and source identity

No ordinary floating-point value, transcendental oracle, numerical zeta value,
rounded mesh cutoff or Fourier quadrature enters acceptance. Exact Fraction
algebra constructs the small source and amplitudes. Authoritative interval
endpoints are integer multiples of 2^-112, with outward division/product/square
rules. Logarithms use the inherited exact atanh series and its complete tail.
The cutoff uses an integer eleventh root. Exact integer harmonic quotients and
prime-power constants are retained.

`ncg28_primitives.py` is a hash-authenticated byte-for-byte predecessor copy.
Agreement between two arithmetic constructions written by the same author is
not independent mathematical review; sharing this backend is explicitly recorded.
The copied module's previous main/default campaign is not invoked by ATC29.

## Development record

An initial default report was generated before adding the labeled quick mode
and selecting the short-source output (rather than its agreeing native checking
value) as the authoritative large-panel interval. It was replaced and every
final accepting/test command above rerun. No initial report is represented as
the final source-bound receipt. Ordinary binary64 exploration informed which
finite examples to inspect, but its script and values are excluded from the
accepting packet. No interrupted numerical run is counted as a success.
An editorial Section 3 transport mismatch was detected by the Git blob hash
and reconciled before publication; no numerical formula or code changed.

## Packaging and what this does not validate

The delivery archive is checked by fresh extraction, SHA256SUMS, both final
reconstructions and both 14-method suites. A separate add-only temporary Git
fixture authenticates the payload subtree and patch application while preserving
an unrelated sentinel. Actual publication SHA/ref and remote tree readback belong
to the PR/issue receipt, not to a predicted commit written into this file.

This is not a full authenticated Riemann checkout or whole-repository validator.
No earlier full DSE27/RCB26/NSR26/NCG28 campaign replay, Lean build, remote CI,
Windows/macOS execution, independent analytic review, new zero-free region,
unbounded high-composite upper estimate, or RH proof is claimed. In particular,
the finite tests do not prove the infinite activation estimate or PNT asymptotic.
