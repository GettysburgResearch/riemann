# X-3601 — Exact continuous packets and the confluent Legendre carrier hierarchy

Experiment ID: `X-3601`  
Agent: `gpt56-04-d`  
Issue: #36  
Status: exact formulas and high-precision controls; empirical complete-prime discovery  
Date: 2026-07-25

## Questions

1. What are the correct off-lattice Gram, prime, pole, and archimedean blocks?
2. Can clustered continuous sinc carriers be represented without a nearly
   singular generalized Gram matrix?
3. How efficiently can a smooth hierarchy reproduce the low piecewise-carrier
   basin from PR #44?
4. Can a future exact piecewise finalist be compressed with a rigorous
   representation-energy ledger?

## Mathematical result

L-3601 derives every exact continuous sinc-packet block from the compact box
transform. The finite prime matrix retains the endpoint phases that disappear
only on the integer lattice; the test suite explicitly rejects the naive
fractional-index divided difference.

L-3602 replaces a close carrier cluster by normalized Legendre envelopes on the
compact Fourier interval. The spectral basis functions are

```text
Phi_n,T(z) = sqrt((2n+1)*Delta) * spherical_bessel_j_n(pi*Delta*(z-T)).
```

Their Gram matrix is exactly the identity. A shifted-overlap recurrence produces
all degree-`N` prime kernels in `O(N^2)` operations per prime power.

L-3603 proves that the carrier is a unitary gauge in the full envelope space.
Carrier scans remain useful finite-dimensional preconditioners, but they do not
enlarge the continuum witness class.

L-3604 gives an exact rational projection ledger from any Gaussian-dyadic
D-0801 cell vector into the Legendre hierarchy. It computes the exact captured
energy and exact omitted `L^2` tail at every requested degree. This is designed
to consume the finalist emitted by the cloud-directed PR #64 run.

## Files

- `packet_blocks.py` — public validation interface;
- `legendre_kernel.py` — independent shifted-Legendre recurrence and carrier
  kernel;
- `off_lattice.py` — independent sinc Gram, frequency, compact archimedean,
  pole, lattice, and fractional-adversary formulas;
- `legendre_prime_matrix.cpp` — complete finite prime-power discovery producer;
- `analyze.py` — symmetric eigensolve, residual, and compact result exporter;
- `project_piecewise.py` — standard-library exact rational compression ledger;
- `tests/test_packet_blocks.py` — nine algebraic/numerical formula controls;
- `tests/test_project_piecewise.py` — five exact projection controls;
- `results/summary.json` — retained degree ladders;
- `results/tests.txt` — 14-test transcript.

## Build and reproduce

```bash
g++ -O3 -std=c++17 legendre_prime_matrix.cpp \
  -lquadmath -o legendre_prime_matrix

./legendre_prime_matrix \
  10000000 4709203636353.65 12 matrix.json

python analyze.py matrix.json --output analysis.json

PYTHONPATH=. python -m unittest discover -s tests -v
```

The C++ arguments are:

```text
cutoff carrier maximum_legendre_degree output
```

Dimension equals `degree+1`.

When a dyadic piecewise finalist is available:

```bash
python project_piecewise.py finalist.json \
  --max-degree 32 \
  --output finalist-legendre-energy.json
```

The resulting energy ledger uses only integers and `fractions.Fraction`. It does
not transfer the Weil sign; a compressed packet must still be evaluated
directly.

## Retained complete-prime result

At `T=4709203636353.65`:

| cutoff | dimension | complete terms | leading value |
|---:|---:|---:|---:|
| `10^7` | 5 | 665,134 | `+0.03762842178460375` |
| `10^7` | 9 | 665,134 | `+0.03078117008809567` |
| `10^7` | 13 | 665,134 | `+0.02894569108367382` |
| `10^7` | 17 | 665,134 | `+0.02861094133528108` |
| `10^7` | 21 | 665,134 | `+0.02843496091166272` |
| `10^8` | 5 | 5,762,859 | `+0.01055049694092198` |
| `10^8` | 9 | 5,762,859 | `+0.00734955574210520` |
| `10^8` | 13 | 5,762,859 | `+0.00700360683739740` |
| `10^8` | 17 | 5,762,859 | `+0.00695074871143398` |

No negative occurred.

The final row is within approximately `3.07657e-4` of PR #44's 1,024-cell value
at the same cutoff and carrier. It uses 17 coordinates and an exact identity
Gram matrix.

## Formula and exact-arithmetic controls

The 14 tests check:

1. overlap identity at support shift zero;
2. vanishing at full support shift;
3. exact transpose parity;
4. the `O(N^2)` recurrence against independent quadrature;
5. real symmetry of the carrier kernel;
6. scalar Fejer recovery;
7. real-axis Legendre--Bessel basis and support orthogonality;
8. continuous frequency kernel against direct compact-support integration;
9. integer-lattice sign congruence and a strict fractional-index adversary;
10. exact degree-zero capture of constant piecewise vectors;
11. exact projection scale invariance;
12. rational, monotone captured-energy ledgers for complex dyadic vectors;
13. zero-vector rejection;
14. invalid-degree rejection.

## Numerical classification

### Exact or algebraic

- prime and prime-power enumeration as integers;
- formulas L-3601--L-3604;
- compact-support overlap recurrence as an algebraic identity;
- identity Gram theorem;
- lattice and fractional endpoint-phase identities;
- piecewise-to-Legendre captured energies and tails.

### Empirical

- binary128 logarithm/product/remainder;
- long-double trigonometry and compensated accumulation;
- long-double overlap recurrence;
- binary64 eigensolving;
- replacement of the exact archimedean and pole matrices by the leading scalar.

The displayed positive values prove nothing outside the finite numerical cells.
A future negative must be reevaluated with directed balls for every matrix block
and frozen to exact dyadic coefficients.

## Main negative result

A single low-degree confluent center at the old X-0602 separated-packet height
near `3e12` did not reproduce its `0.242` packet basin; degree 8 gave a much
larger positive value. This is consistent with X-0602 using a genuinely broad
carrier window rather than a close cluster. The next geometry should therefore
use two or more separated confluent centers, not merely increase one local
degree.

## Suggested continuation

First apply L-3604 to the cloud PR #64 finalist. Then implement the M-3601
block-confluent hierarchy with two separated centers. Use small identity-Gram
Legendre blocks locally and the exact L-3601 cross-cluster Gram. Optimize the
center separation and local degrees, then directly reevaluate only the strongest
finite packet with Arb.
