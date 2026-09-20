# Executed validation and limits

## Accepting arithmetic

The accepting checker uses only Python standard-library integers and Fraction
for sources, products, divisibility, native Newton coefficients, and the whole
prime-power harmonic component. Real transcendental calculations use outward
integer fixed-point intervals with denominator 2^144; the decimal endpoints
in results.json are separately rounded outwards and are only presentations.

Pi is enclosed by 128-term alternating arctangent sums and the Machin identity.
Cosines are evaluated by the degree-97 Taylor polynomial (the odd coefficient
is zero), with the complete 4^98/98! Lagrange remainder. Argument reduction
places the real input in [0,pi]. Interval arithmetic pays rounding at every
operation. Real logarithms are reduced to [1,2), using the 96-term atanh series
and its complete positive tail. The logarithmic sine is evaluated through
(1/2)log(2-2cos). There is no floating FFT, special-function library, quadrature,
zero table, or truncation of an unpaid infinite harmonic tail in acceptance.

A different exact rational arctangent identity is used to check pi; a longer
rational logarithm series checks log 2. Exact special trigonometric values,
angular coefficient-mass bounds, and the complete Ramanujan/log identity are
also checked. These are different calculation paths by the SAME author,
not an independent numerical package or independent mathematical review.

## Complete default finite scope

Defaults: Y=15 and Y=31. There are nine observation blocks, 1,232 covered
cells counting overlap between campaigns, and 2,455 reconstructed coefficient
comparisons counting overlap of their prefixes. The largest native endpoint
is 1,023; the largest source cutoff is 31 and last source index is 32.
The largest possible Fourier denominator is therefore 1,024.

The far mixed-prime calculation includes 34,460 reduced-frequency instances;
the near mixed-prime side has 8,890 instances, counting repeated block
experiments. Of the far instances, 32,482 lie beyond the declared LOCAL
NCG28 denominator-window comparison cutoff. That statistic does not identify
them with the old fixed-source W_high and is not an energy-coverage claim.

All product amplitudes are checked using a separate gcd-threshold formula.
Every reconstructed native coefficient is compared to an independently
computed full Mobius sieve; the source seeds use trial factorization.
The full sieve is a finite cross-check, not an input to the coefficient
producer. Every prime-log coefficient cancels exactly.

The whole prime-power harmonic component is computed rationally on every
block. For the three panels with local source cutoff at most seven, BOTH
mixed-prime angular pieces are evaluated directly by their finite cosine
and logarithm formulae. On the other panels the near component is calculated
by exact complementary algebra after independent full-source reconstruction.
That is not a second independent evaluation of every near Fourier term.
All three energies, all three doubled cross terms, the combined controlled
energy, and its cross term with the remainder are retained.

Canonical results.json SHA256:
`3b6fd0d9a16d91881c56bcf771a0f60ac52a40ce92b877791529b6589c13bc08`.
The report also binds the exact accepting check.py by its SHA256.

## Commands and outcomes

The final default reconstruction and the twelve-method suite pass in normal
and optimized Python with zero skips, failures, or errors:

```
python -S -B check.py --check results.json
python -S -B test_check.py
python -S -O -B check.py --check results.json
python -S -O -B test_check.py
```

The tests include exact prime-threshold algebra, 27 bounded artificial-prefix
controls, block schedules for every Y from 7 through 512, centered single-
frequency identities, exact source-pair versus reduced-frequency dictionaries,
a complete rational tail-norm identity, and native positive and negative
far/near cross terms. Deleting the partial centering constant fails a specific
balanced-source control.

There are four altered-report comparisons and a duplicate-key refusal inside
the Python process. One test additionally runs an actual CLI write, a pristine
CLI replay, and ONE corrupted-report CLI refusal. Do not relabel these as
many complete adversarial numerical campaigns. Parser/domain tests have their
own explicitly bounded scope.

Fresh final archive extraction and a fresh add-only Git fixture were used to
repeat all four commands and the file-hash checks. The patch was checked and
applied in the fresh fixture, preserving an unrelated sentinel. This is a
minimal local Git fixture, NOT a full authenticated Riemann checkout.

## Exploratory work not promoted to evidence

A preliminary NumPy/binary64 scout explored an earlier TWO-channel angular
partition through global Y=63. It helped test the formulas and identify that
the near-zero band remained substantial. The final result uses a different,
THREE-channel partition after proving the separate prime-power bound. No
binary64 value, exploratory Y=63 number, or previous two-channel pilot is an
accepting result or an additional final-campaign run. A small early pilot
JSON was superseded before sealing; results.json is the final complete report.

## Publication and scope

Live GitHub reads confirmed #904 at
`879497b4f11be2618c448efc1fa93f69b4022e4c`, both at entry and closing read.
Write-action discovery returned none; the complete available GitHub action
inventory was read-only. Plugin discovery identified the already connected
GitHub provider, not an additional publishing action. Direct git ls-remote
failed to resolve github.com. No remote commit, PR update, issue comment or
push was performed by this session.

No inherited NCG28/DSE27/RCB26/NSR26 complete campaign was replayed. No full
repository validator, clean cross-platform installation, Windows/macOS test,
Lean build, remote CI, external peer review or unbounded near-zero estimate
is claimed. The infinite inequalities are written mathematics requiring
review, not certified by comparing JSON files.
