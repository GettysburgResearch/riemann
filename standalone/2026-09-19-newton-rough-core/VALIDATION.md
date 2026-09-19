# Validation and publication boundaries

## Executed environment

Linux, Python 3.13.5. Accepting code uses only the standard library. It uses
integer arithmetic, exact `Fraction` source algebra, and outward dyadic
intervals with 112 fractional bits. Positive logarithms are reduced to atanh
series with argument in [0,1/3], using the complete explicit geometric tail.
No binary64 value participates in acceptance.

## Final accepting commands

```
python -S -B check.py --check result.json
python -S -O -B check.py --check result.json
python -S -B -m unittest -v test_check.py
python -S -O -B -m unittest -v test_check.py
```

Both reconstructions reproduce the same canonical result. Both nine-method
suites pass. Each suite includes ONE actual copied-CLI, resealed-result refusal
in a temporary directory, not a claimed suite of many subprocess mutations.
Other controls are exact in-process tests. The final clean archive and
add-only patch replay scopes are recorded in the outer DELIVERY.md.

Canonical result SHA-256:

```
cd4a5bb8d46fed6ef24f1b7010e8635ff832092c75f324abac6af6d983b276d7
```

## Concrete accepting coverage

The main reconstruction checks 4096 trial-factorization versus sieve values;
16384 parity-partition equivalences; full native product-fibre bounds for
cutoffs 1 through 40; exact Newton reconstruction and all product-balance
relations at the declared native cutoffs; complete finite grouped-energy
panels at Y=5,15,31,63; and the complete nonzero-collar energy identity at Y=95.
The Y=95 grouped energies themselves are not interval-certified here.

The tests distinguish squarefree parity core from radical; retain every
product beyond B; reject an invalid inclusive square endpoint; reject a fake
native divisor-inverse relation; certify a positive same-core off-diagonal;
certify failure of monotonicity under prime-bank enlargement; and certify
positive cross-block covariance for a cap-three fake source. The Y=128 fake
lower-bound check covers every one of 2049 integer indices in [2048,4096].
The infinite G(2,4) sign control includes its entire tail analytically.
The nine-method suite also reconstructs complete native Newton prefixes at
Y=1,...,24, and checks interval/log/harmonic arithmetic and copied-CLI refusal.
Overlapping examples are not independent theorem counts.

## Numerical independence and review

The primitive Möbius sieve, trial factorization, source convolution and
harmonic/centered formulas are distinct calculation paths, but they are in
one author's packet. The two Python modes use the same arithmetic code.
Neither provides independent mathematical referee acceptance. The optional
NumPy scout is ordinary floating exploration, not a second rigorous backend.

No earlier packet's producer or certificate campaign was rerun. No full
Riemann checkout, source-tree validator, Lean build, Windows/native browser
test, remote CI, new zero-free region, all-scale covariance bound, or RH proof
was executed or obtained. The written infinite estimates require review
independently of the finite arithmetic.

## Publication

GitHub reads succeeded, including a closing read of the #848 branch at
`9e4375952c87835c2f4f2cca10a996009e74a435`. Tool discovery exposed 48 read-only
GitHub actions and no write function. The plugin directory found the already
installed GitHub integration, but no additional write tool became available.
No `gh` executable or configured GH/GITHUB token was present; GitHub DNS did
not resolve in the container. No credential search or access-control bypass
was attempted.

This authoring pass did NOT publish a commit, create a PR, or comment on #902.
The archive carries a tested add-only patch, a suggested PR body and a
publication brief. A publisher must record its actual remote SHA/URL rather
than represent this document as a push receipt.
