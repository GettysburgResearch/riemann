# Newton rough-core covariance: a proved sector bound, not the missing RH gain

**Status:** proposed component proofs with complete arguments and finite
outward-rounded checks; independent mathematical review required.
**RH and the native scale-to-scale gain remain unproved.**

This executes the direction chosen in [issue #902](https://github.com/GettysburgResearch/riemann/issues/902)
against PR #848 at `9e4375952c87835c2f4f2cca10a996009e74a435`.
It does not pursue the marginal simple-zero proportion result.

## What is actually added

The earlier PCR26 packet controls the diagonal after coalescing equal products
in the arithmetic Newton square. This packet controls a much larger sector:
**every pair of products whose prime-valuation parity differs only at primes
in a prescribed small bank, with arbitrary square factors allowed.**

For the literal truncated Möbius source the complete absolute budget is

```
832 H_Y H_(Y^2)^4 product_(p in S) (1+2/sqrt(p))^2.
```

For the actual cap-three completion, valid at every cutoff, it is

```
1458 H_L^6 H_(L^2)^4 product_(p in S) (1+2/sqrt(p))^2, L<=2Y.
```

Thus the within-block sector is subpower even when S contains every prime
up to `(log L)^2`. These are upper estimates for whole families of actual
off-diagonal terms, not a finite scan or just another RH equivalence.
The fifth-logarithmic native estimate and tenth-logarithmic completed estimate
apply to different sources; they are not interchangeable.

All product coefficients, products above the observation endpoint, the new
annulus, and the completion collar remain in the exact update. The remaining
cross-block covariance is explicitly unpaid. The sector bound also holds for
certain fake sources, and an explicit uniformly capped family makes the
unpaid term of quadratic size. Therefore the estimate does not supply the
source-specific gain by itself.

Read [PROOF.md](PROOF.md), especially Sections 2-6, then the fake-family test
in Section 8. The main ingredients used from #848 are its existing innovation
isometry, clipped completion, harmonic kernel, and Newton prefix theorem.
They are credited, not claimed as new. No global mathematical priority is
asserted for the new combination of elementary estimates.

## Run the accepting finite reconstruction

From this directory, using Python 3.10 or later:

```sh
python -S -B check.py --check result.json
python -S -O -B check.py --check result.json
python -S -B -m unittest -v test_check.py
```

No third-party numerical package, network, repository-relative import, or
zero table is used in acceptance. Normal and optimized runs share one
implementation and author, not independent mathematical review.

The checker reconstructs actual coefficients and exact rational source
relations, then uses outward integer intervals for finite grouped energies.
It covers native full annuli at Y=5,15,31,63; a separate exact native Newton
prefix and nonzero collar at Y=95; a fake-source annulus at Y=15; and every
index in the Y=128 fake family's specified large-output interval.
The infinite-k sector bounds are proved in the manuscript, not by extrapolating
those calculations.

The optional `scout.py` uses NumPy/binary64 and writes `scout.json`. It is
exploration only. The larger Y=95 and Y=127 grouped panels there are not
interval-certified. See [EXPERIMENTS.md](EXPERIMENTS.md) and
[VALIDATION.md](VALIDATION.md) for exact scope.

## Where the attempted full gain stopped

Writing the full update in the existing reciprocal-sum norm leaves

```
F_B-F_Y = 4 T_Y + D_S + C_S - 4 <m_c,Q>,  B=(Y+1)^2-1.
```

This packet bounds D_S uniformly, and keeps T_Y and the mixed term. It does
not establish a subpower native bound for C_S or the desired exponent gain.
The source-specific divisor-inverse relations must enter that next estimate;
a large prime in a parity difference is not in itself a cancellation theorem.

## Publication boundary

The authoring session could read the connected GitHub repository, but its
48 exposed GitHub actions were read-only. Discovery found no write action;
no authenticated CLI or token was available and direct GitHub DNS did not
resolve. The complete packet and an add-only patch were produced locally.
**There is no new remote commit or PR receipt in this archive.** A separate
publisher must append its actual receipt after publication.
