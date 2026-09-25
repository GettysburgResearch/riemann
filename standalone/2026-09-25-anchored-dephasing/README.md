# ADP37: anchored dephasing and principal-phase concentration

**Proposed component mathematics. Not independently reviewed or integrated. No RH proof or new native principal-phase upper bound.**

Parent: PR #907, CAP36 at `c5ee83dc5f2f5f7ffa2d89b45298923a04e6cf0b`.

## Read

- `PROOF.md`: literal harmonic observable, alias-sensitive Fejer identity, finite dephasing estimate, independent logarithmic averaged bound, actual-harmonic counterexample to generic principal extraction, and precise remaining native concentration problem.
- `SOURCES.md`: classical inputs and exact repository dependencies.
- `VALIDATION.md`: arithmetic, coverage, successful executions, failed development attempts, and limitations.
- `check.py`, `test_replay.py`, `receipt.json`, `SHA256SUMS`: executable primitive replay and authentication records.

## Result

For a native cap-three source through Y, length L, and the SAME smooth microscopic observable of CAP36, put B=L^2 and use phases tau_j=2pi j/log Y with triangular Fejer weights of width K. Under

    X>=8H, B<=8X, YX>=4HB, X<=M<2X,

the phase average obeys

    A_K <=648[1+(B log Y/K)^2] h_(16H)^2(2h_L-1).

This is independent of the previous native energy F_Y. With K>=2B log Y it is logarithmic in L at fixed H. The exact product-collision diagonal is retained before the bound; aliased products are grouped when the separation condition does not apply.

It is an AVERAGED bound, not a principal-member bound. In the same actual centered harmonic kernel there are nonnative, real balanced sources with |c|<=1 whose principal energy is at least 2^(-72)L^2 while their limiting mean is O(log L). Thus generic mean-to-principal coercivity with a subpower loss is false. This does not refute a native Mobius estimate.

The next mathematical obligation is to control concentration at the untwisted phase using literal native arithmetic, not just balance, coefficient caps, or invertibility of source modulation. CAP36's small-frequency transport cannot silently be applied at the order-L^2 frequencies in the guaranteed dephasing window.

## Reproduce

From this directory:

```sh
sha256sum -c SHA256SUMS
python -I -S -B check.py --check receipt.json --output /tmp/adp37-normal.json
python -I -S -B -O check.py --check receipt.json --output /tmp/adp37-optimized.json
cmp receipt.json /tmp/adp37-normal.json
cmp receipt.json /tmp/adp37-optimized.json
python -I -S -B test_replay.py
python -I -S -B -O test_replay.py
```

The full receipt includes directed evaluations of the ACTUAL centered harmonic kernel and actual logarithmic anchored phases at two small native cutoffs, covering their full declared observation blocks. Rational surrogate controls are separately labeled. Neither class of finite checks replaces the universal written proofs.

No main/canonical/workflow changes, independent review, proof-assistant verification, repository-wide validator, or inherited-campaign replay is claimed.
