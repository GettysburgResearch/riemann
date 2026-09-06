# X-21502 — Triangular terminal-prime energy reconnaissance

This discovery-only experiment evaluates the real `L-21501` window on the
complete von Mangoldt manifest through `10^7`.

## Build and run

```bash
g++ -O3 -std=c++17 -Wall -Wextra recon.cpp -o recon
./recon > results/recon-1e7.json
```

The implementation:

1. sieves every prime through `10^7`;
2. enumerates every prime power once with weight `log(p)/sqrt(p^k)`;
3. represents the piecewise-linear signal by exact slope-change events;
4. integrates the square of each linear piece analytically in long double;
5. accumulates the single-atom diagonal independently;
6. reports total, diagonal, and off-diagonal unit-block energies.

Blocks `j=2,...,16` are complete because their required prime powers lie below
the declared cutoff. Later blocks are not reported.

## Digests

```text
source
fd904f4adc306c9ee59077d0ce596ebc92dc70fee549921b483208fa83386c54

retained result
9ee9138eb426f4cdd23425776bc057a0e7d4b2141904416509918854dc3a69db
```

## Classification

```text
LONG_DOUBLE_RECONNAISSANCE
```

This is not a directed certificate. The striking cancellation is preserved to
motivate a global Selberg/dispersion proof, not to infer RH from a finite
ladder.
