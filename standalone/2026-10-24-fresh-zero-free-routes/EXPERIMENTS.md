# Exact finite checks and exploratory sextic rectangles

Status: exact finite algebra and explicitly bounded exploratory sums. No analytic mean estimate or zero-free boundary is certified.

## The finite sextic object

`sextic_interpolation_experiment.py` works in `Z[omega]`, with `omega^2+omega+1=0`. It enumerates the unique generators congruent to 1 modulo 3, and excludes the primes above 2 and 3. Columns are squarefree ideals of norm in `[D,2D)`; physical rows are sixth-power-free ideals of norm in `[U,2U)`.

For the elementary sextic symbol `(u/n)_6`, extended by zero whenever `u` and `n` share a prime ideal, it builds

\[
V(z;u)=D^{-1/2}\sum_{D\le Nn<2D}\mu^2(n)z^{\omega(n)}(u/n)_6.
\]

This is one fixed untwisted symbol convention with sharp annuli. It is not a replay of every ray convention, moving puncture, smooth profile, height, or growing parameter in the analytic consumer.

The arithmetic uses exact Eisenstein pairs, exact finite-field exponentiation at split and inert primes, and exact rational polynomial evaluation. NumPy is used only for bounded integer arrays. The script checks an integer size bound before quadratic contractions; the declared cases are far below fixed-width overflow. Display columns ending in `_float` are ordinary numerical displays of exact rational values, not directed-rounding certificates.

Writing the row sums as `A(z)+B(z) omega`, the energy is exactly `A(z)^2-A(z)B(z)+B(z)^2` for real `z`. The script records the complete energy polynomial, its genuine diagonal, and the signed difference. It reconstructs that difference at `z=-1` by exact Lagrange interpolation from `2d+1` points of `[1/4,3/4]`, where `d` is the largest column prime-factor count. Direct accumulation at `z=1` and `z=-1` is checked separately against the energy polynomial.

Every row/column collision zero stays in both the full moment and its diagonal. These are exact finite checks of the proposed continuation interface. They do not prove the continuum mean hypothesis needed as `U,D` grow.

## Recorded rectangles

| U | D | Physical rows | Squarefree columns | Maximum omega | Mobius moment divided by U (ordinary display) |
|---:|---:|---:|---:|---:|---:|
| 64 | 128 | 19 | 37 | 2 | 0.1083984375 |
| 128 | 256 | 39 | 74 | 2 | 0.0626525879 |
| 256 | 512 | 80 | 139 | 3 | 0.0785522461 |
| 512 | 1024 | 150 | 294 | 3 | 0.0859317780 |
| 256 | 4096 | 80 | 1,145 | 3 | 0.0746498108 |
| 400 | 8000 | 124 | 2,252 | 4 | 0.0817825000 |
| 576 | 13824 | 175 | 3,898 | 4 | 0.0822487662 |
| 1600 | 64000 | 484 | 18,061 | 4 | 0.0912967188 |
| 2500 | 125000 | 762 | 35,284 | 5 | 0.0889572768 |

The report also contains the values at `z=1/4,1/2,3/4,1,2`. At the largest rectangle the centered Mobius moment divided by `U` is `0.0080824032`; the unmarked full moment divided by `U` is `0.0706962080`, with centered value `-0.0101786656`. These signs illustrate why recording the complete centered polynomial matters. They do not resolve its asymptotic size.

The local arithmetic checks reconstruct all 88 primary ideals through norm 300 and verify 7,500 multiplicative symbol identities at 12 split/inert prime ideals, including products with natural zeros. The character sums at all nine rectangles are recomputed by the script rather than read from the stored JSON.

## Other finite checkers

| Script | What it checks | What it does not establish |
|---|---|---|
| `arithmetic/check_continuation.py` | 561 interpolation monomials, 33 coefficient masses, 33 Chebyshev costs, 561 integer-node countermodel values, 38 density identities, the `5/48` deficit | A fractional analytic moment, useful effective Baire constants, or a zero-free region |
| `family/check_log_transport.py` | 1,536 logarithmic coefficients; 2,560 rough-splitting coefficients; 3,280 character products, including 918 nonunit products; rejection of eight incomplete prime-only identities | A signed joint prime/inverse mean, or absorption away from the specified envelope maximum |
| `spectral/check_polynomial_identities.py` | Complete rational polynomial identities and positivity certificates for the explicit theta perturbation, plus exact quartet and variance formulas | A numerical theta quadrature, complete operator approximation, spectral selection, or RH |

The source-specific infinite arguments are written in the corresponding notes. Their validity does not follow merely from these finite checks passing.

## Reproduction

From the repository root, use the packet path in place of `PACKET` below. The first three scripts need only the Python standard library; the sextic experiment additionally needs NumPy.

```bash
python3 -I PACKET/arithmetic/check_continuation.py
python3 -O -I PACKET/arithmetic/check_continuation.py
python3 -I PACKET/family/check_log_transport.py
python3 -O -I PACKET/family/check_log_transport.py
python3 -I PACKET/spectral/check_polynomial_identities.py
python3 -O -I PACKET/spectral/check_polynomial_identities.py
python3 -I PACKET/sextic_interpolation_experiment.py --output /tmp/sextic-replay.json
```

The publication review records which outputs were independently reproduced and checks the source/output hashes. Stored JSON is an output, not the primitive input to any claimed analytic theorem.
