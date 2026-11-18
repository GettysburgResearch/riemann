# Independent replay with Platt's original program

This archive uses the unmodified program published by David Platt with the earlier verification. Its Arb 2.23 and FLINT 2.9 implementation runs separately from the modern FLINT 3.6.0 producer. It evaluates its own scaled completed zeta samples, searches sign changes and stationary points, and runs its own Turing count. Its parameter header permits heights from $10^{10}$ through $3.01\times10^{12}$. The source is pinned to commit d918aa093a304819a0f7d1c27bfaf67c8c0f0602. [Original repository](https://github.com/djplatt/arb_zeta/tree/d918aa093a304819a0f7d1c27bfaf67c8c0f0602) · [Parameter table](https://github.com/djplatt/arb_zeta/blob/d918aa093a304819a0f7d1c27bfaf67c8c0f0602/parameters.h) · [Turing checks](https://github.com/djplatt/arb_zeta/blob/d918aa093a304819a0f7d1c27bfaf67c8c0f0602/turing.c)

From this directory on Debian amd64 with gcc, git, dpkg-deb, GMP development headers and the MPFR runtime, build in a separate workspace. The builder fetches exact source and checks SHA-256 for all seven historical development and runtime packages before local extraction.

```sh
python build_original.py /tmp/riemann-legacy
python run_original.py --binary /tmp/riemann-legacy/platt-original/arb_zeta \
  --library-dir /tmp/riemann-legacy/old-libs/usr/lib/x86_64-linux-gnu \
  --until 3000175356164 --runs /tmp/riemann-legacy/runs
python check_runs.py --runs /tmp/riemann-legacy/runs --check-chains
python check_error_reserve.py
```

The executed historical binary had SHA-256 `9aa12c66e9d3c4078c408d1aa7f330fe843d0653e6558845afbac6af2ee6b691`. The optional modern endpoint check uses python-flint 0.9.0. With no arguments the checker audits the archived raw stdout transcripts in [runs](runs).

The program can return process status zero after a failed search. The checker therefore requires one original regional outcome for each requested iteration, in order, with the exact stated height boundaries. It counts a region only after the program reports that its sign search obtained exactly its Turing upper-minus-lower count. It checks that repeated endpoint counts agree and that all counts are nondecreasing in physical height. The reported frontier includes only the union of successful intervals continuously connected to the historical height. Failed searches stay visible. The runner automatically retries gaps on shifted exact dyadic grids and archives each raw result. Parallel lanes may cover separate ranges before they meet.

The [error-reserve calculation](error-reserve.md) checks the original interpolation path and its Fourier allowances at the heights in this archive, including the unused DC-bin allowance which pays the sinc truncation. The historical run returns regional counts. Individual root brackets are available in the modern producer's archive.

The optional `--check-chains` partitions successful regions into chains having exactly matching height boundaries. It checks both endpoint counts of every chain with generic zeta_nzeros. Within a chain, historical sign changes occur in disjoint open intervals and the total number found equals the modern full-strip count difference. Thus this stronger crosscheck verifies exhaustion independently of the internal historical Turing estimates. The builder also verifies every Taylor bucket residual at every archived precision.

To replay a fixed inventory after new runs have been added, select a checkpoint explicitly. For example, `python check_runs.py --snapshot checkpoint-half-million.json --check-chains` reads and hashes precisely the listed raw transcripts and recomputes their chain endpoint counts. Produce a new inventory with `python check_runs.py --check-chains --write-snapshot checkpoint-name.json`.
