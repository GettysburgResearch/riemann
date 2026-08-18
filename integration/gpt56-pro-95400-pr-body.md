## Purpose

Continue Q4 only from PR #573 and attack its finite odd-core cross correlation
without modifying or importing the carry sibling.

**RH remains unproved.** The requested full FOCC proof was attempted through
Type I/II, dispersion, large sieve, pretentious distance, Mellin
almost-orthogonality, positive-kernel completion, square functions and
logarithmic Sobolev methods. No complete proof survived. This successor proves
all exact reductions and source-blind sectors that did survive and isolates one
strictly smaller separated coprime Type-II gate.

## Freeze

```text
base PR:      #573
base branch:  research/gpt56-pro/95310-q4-finite-odd-core-preconditioner
base SHA:     0865242eb9dc0ed6094afc8a87a52b974c6f1307
head branch:  research/gpt56-pro/95400-q4-focc-annular-typeii-hardening
publication:  one add-only Q4 successor commit
carry route:  frozen / absent
```

## Main advances

1. `L-95400`: a safe three-factor scale filter annihilates the complete cubic
   small-`x` tail, producing a factor-1024 annulus with ten exact
   `Q(sqrt(2))` kernel bands. Its inverse has coefficient mass `64/21`, and
   its Mellin zeros lie only on `Re z=-1,-2,-3`.
2. `L-95401`: exact dyadic-band, ratio and gcd decomposition; all active ratios
   are below 1024. The diagonal is `O(log^2 X)`, and polylog-width
   near-diagonal and large-gcd sectors are closed absolutely.
3. `L-95402`: source-faithful Type I/II, coprime common-divisor, Mellin and
   log-Fourier normal forms, with the `J1` boundary retained.
4. `R-95400`: generic PSD/diagonal completion, fixed-window large sieve,
   fibrewise square functions and prime-cube log-Sobolev arguments cannot
   prove FOCC.
5. `T-95400`: FOCC is equivalent to `SACF`, one separated small-gcd coprime
   Type-II correlation on the ten exact bands. `SACF` remains open and
   RH-bearing.

## Replay

```bash
cd experiments/X-95400-q4-focc-annular
python3 verify.py --scan-limit 100000 --output /tmp/x95400.json
cmp /tmp/x95400.json results/verification.json
sha256sum -c SHA256SUMS
cd ../..
sha256sum -c integration/gpt56-pro-95400-content-sha256.txt
```

Expected:

```text
PASS_X_95400_Q4_FOCC_ANNULAR_HARDENING
```

The floating endpoint scan is discovery only.

## Exact boundary

```text
safe annularization                     CLOSED
exact kernels / activation geometry     CLOSED
diagonal / near / large-gcd sectors     CLOSED
Type I/II and Mellin rewrites           CLOSED
source-blind shortcuts                  REFUTED
SACF / FOCC / OCHD                      OPEN / RH-BEARING
Riemann Hypothesis                      UNPROVEN
```
