# Relative arithmetic boundary representations

A research packet from 25 September 2026 responding to the request for a genuinely structural Riemann research pivot.

Start with **RESEARCH.md**. It contains all definitions, component proofs, the scope of the repository reading, limitations, and a concrete comparison-theorem objective.

The strongest quantitative result here is a warning about a tempting auxiliary model: the full finite-prime completion through y=1,000,000 has energy **greater than 10^33**, although the exact same source's native head energy is enclosed between **1.6633047261 and 1.6633056308**. An analytic resonant-interval proof and exact integer/dyadic/rational computations support this comparison. It is not a counterexample to RH and is not a native upper-bound improvement.

The constructive pieces are full residue-channel source restoration, a half-density real-dilation comparison, an exact first-exit cocycle, and a positive mixed-boundary Gram kernel with exact gcd/lcm support. These are components of a proposed relative arithmetic Fourier theory, not a completed cohomology or RH proof.

## Reproduce

Python 3.10 or later, standard library only:

```sh
python -I -S -B check.py --output replay.json
python -I -S -B completion_certificate.py --check completion_receipt.json
python -I -S -B -O check.py --output replay_optimized.json
python -I -S -B -O completion_certificate.py --check completion_receipt.json
```

`check.py` exercises finite algebra with integers, rational numbers, and exact cyclotomic quotient rings. `completion_certificate.py` reconstructs the million-scale analytic lower-bound inputs and native-energy enclosure, and includes a small full-prime-completion scout with up to 2^20 divisors.

For the million-scale certificate without the optional small-divisor scout:

```sh
python -I -S -B completion_certificate.py --skip-small --output quick_receipt.json
```

That output has a deliberately different empty scout field; do not compare it with the full stored receipt.

The written analytic arguments are not certified by a proof assistant. See VALIDATION.md and SOURCES.md. No remote repository changes were made.
