# X-97400 — Repaired P61 scalar bias and source-interface firewalls

The proof-producing computation has two parts.

## Directed P61 bias producer

```bash
./build_and_replay.sh
```

`src/certify.cpp` uses MPFR 256-bit RNDD/RNDU primitive enclosures and outward
`long double` interval operations. It checks:

- every integer endpoint through `1,000,000`;
- all-real interpolation between integer hinge breakpoints;
- the complete compact asymptotic remainder on `2<=Y<=16`;
- every one of the `262,144` divisors of `P_61`;
- every tail activation interval `x in [2d_i,2d_{i+1})`;
- the exact negative `1/40` witness at `x=184`;
- the repaired `1/42` lower bias and `1/8` upper bias.

The full run takes roughly 25 seconds on the publication host. No large
Target--Lorenz sweep is invoked.

## Exact interface replay

`verify_interfaces.py` checks with rational arithmetic:

- same-channel versus swapped-channel source restriction;
- the one-prime root coefficient mismatch;
- the PR #566 reserve/current countermodel;
- the critical `1/42`, `1/6`, `<1/8` contraction arithmetic.

The replay does not prove a source-complete global rough recursion or RH.
