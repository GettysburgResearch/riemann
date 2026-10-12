# Arithmetic and negative-mass research packet

Status: **PROPOSED mathematics**, with finite exact arithmetic checks and
independent internal proof review during the October 10 wave. These objects
have not been integrated into the reviewed baseline. RH remains open.

Scope: one literal critical SHARP detector, one sufficient global
supercritical-power threshold, and the classical fixed-zero-free-half-plane
adapter. Inherited source identities and verdicts are preserved.

The concrete positive result is a lower global SHARP threshold:

\[
 H_m(x)>0\quad(x\ge1,\ m\ge1.737).
\]

[SQUAREFREE_STITCH.md](SQUAREFREE_STITCH.md) gives the squarefree weighted
prefix refinement and seven certified exponent slabs proving this bound.
[HORIZON_STITCH.md](HORIZON_STITCH.md) gives the complete finite-horizon/tail
stitch proof and five directed Arb certificates covering all real endpoints
and powers in the remaining interval. [POWER_THRESHOLD.md](POWER_THRESHOLD.md)
gives the full labelled-prime proof of the static threshold 1.80206853774,
the exact threshold bracket, all interval-error contracts, and an explicit
eventual-positive horizon for every fixed 1<m<2. The latter horizon escapes
to infinity near m=1, so it does not supply the critical estimate.

[NEGATIVE_MASS.md](NEGATIVE_MASS.md) derives a quantitative zero-free strip
from polynomial logarithmic negative mass and an explicit pole-driven
Omega constant for a rightmost off-line zero of arbitrary multiplicity.
It also shows that the normalized quadratic SHARP primitive already has
unconditional global bounded variation and a positive limit. Those facts
do not control the critically weighted negative variation.

[ZERO_FREE_MERTENS.md](ZERO_FREE_MERTENS.md) reconstructs the growth and
Perron adapter, with a finite-rectangle logarithm interpolation proof. Its
consequence for the fixed detector is

\[
 \limsup_{Y\to\infty}\frac{\log(1+N_F(Y))}{\log Y}
       =\sup_\rho\Re\rho-\frac12.
\]

The proof does not require the supremum to be attained. A zero-free theorem
imported from another paper supplies only its declared theta; this packet
does not reprove or independently approve that paper.

Reproduce from this directory with Python 3.10 or newer:

```sh
python3 -B verify_power_threshold.py --output /tmp/power-normal.json
python3 -B -O verify_power_threshold.py --output /tmp/power-optimized.json
diff -u /tmp/power-normal.json /tmp/power-optimized.json
python3 -B test_threshold.py
python3 -B -O test_threshold.py
```

The rational checker and its six independent controls use only the Python
standard library. The checker uses exact rational directed enclosures; the
analytic infinite-series tail bounds are proved in the manuscript.
An optional independent replay uses python-flint 0.9.0 and Arb directed
balls:

```sh
python3 -B check_threshold_arb.py --output /tmp/power-arb.json
python3 -B verify_horizon_stitch.py --output /tmp/horizon-normal.json
python3 -B -O verify_horizon_stitch.py --output /tmp/horizon-optimized.json
diff -u /tmp/horizon-normal.json /tmp/horizon-optimized.json
python3 -B verify_squarefree_stitch.py --output /tmp/squarefree-normal.json
python3 -B -O verify_squarefree_stitch.py --output /tmp/squarefree-optimized.json
diff -u /tmp/squarefree-normal.json /tmp/squarefree-optimized.json
```

The actual execution receipt and retained output are in `EXECUTION.json`
and `results/`. Source hashes bind the finite checks. Ordinary decimal
reconnaissance was used only to choose the bracket, never for acceptance.

The remaining mathematics is the native critical negative-mass estimate,
or a theorem that lowers a uniform sufficient exponent all the way to one.
No finite positive scan, pairing-threshold improvement, or fixed-power
tail theorem is asserted to provide that estimate.
