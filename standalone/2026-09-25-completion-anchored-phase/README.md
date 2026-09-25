# CAP36 — completion-anchored phase transport

**Proposed component mathematics. No full covariance bound or RH proof.**

Read [PROOF.md](PROOF.md) for the exact observable, quantifiers and proofs;
[VALIDATION.md](VALIDATION.md) for actual replay coverage and limitations;
[SOURCES.md](SOURCES.md) for frozen source dependencies.

This pass resolves a *specified compressed* version of the transfer defect left
by RLC35. An early reciprocal-balance repair is invisible to the microscopic
observable when X>=2HL, and is bounded in the correct reciprocal metric.
Compressing each source factor through L before tensoring makes the arithmetic
defect exactly (1-n^(i tau))(c(n)-mu(n)) on the short completion interval.
Anchoring exp(i tau log Y)=1 yields a small-width norm estimate.

For the cap-three native source and |tau|<=1, the complete comparison error on
X<=k<=M<2X satisfies

```
||A_tau-U_tau||^2 <= 2^39 H^4 tau^2 (J/Y) F_Y^2,
```

where J is completion width, F_Y is the previous reciprocal-Mobius energy,
X>=max(8H,2HL), and L^2<=8X. The exact sharper bound is in PROOF.md (0.1).
All selected frequencies and their cross terms are retained. This bounds a
DIFFERENCE of two quantities, not either unknown quantity separately.
The equivalent bound involving Y^(-1/3) has F_Y exponent 7/3; it is not a
subquadratic Newton recurrence.

The transformed kernel has separate factor cutoffs. It cannot replace the
uncompressed Hankel adapter without a leakage term. A nonzero exact leakage
control is included. The next target is an independent bound for the
transformed kernel, or a justified coercivity mechanism using these phase
relations. Neither is supplied here.

## Replay

Python 3, standard library only:

```sh
python -I -S -B check.py --check receipt.json --output replay.json
python -I -S -B -O check.py --check receipt.json --output replay_optimized.json
cmp receipt.json replay.json
cmp receipt.json replay_optimized.json
python -I -S -B test_replay.py
python -I -S -B -O test_replay.py
sha256sum -c SHA256SUMS
```

The actual execution used two four-method groups per test mode after long
combined commands were interrupted. All eight methods completed in both modes.
See VALIDATION.md for commands and the distinction between finite rational
controls and the analytic real-phase/harmonic statements.
