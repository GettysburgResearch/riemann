# X-99250 — Directed factor-67 SHARP Harnack certificate

This experiment authenticates the finite theorem in `L-99252` and the exact
algebraic/interface checks used by `T-99250`.

## Fast replay

```bash
python3 verify.py
```

The fast verifier independently checks:

- the compact SHARP Hall base on `[1,67)`;
- the binding wrong-target failure at `t=13`, `x=67`;
- the Radon–Nikodym child ratios and normalized-profile order;
- the local coefficient formula `(1,-2,1)` through 200,000;
- the SHARP and factor-67 Mellin multipliers;
- producer/transcript hashes and fail-closed status flags;
- the exact directed interval at the retained minimizer `x=201^-`.

## Full producer replay

```bash
./replay.sh --full
```

Full mode compiles `src/scan_sharp_h67.cpp`, scans every half-open integer cell
from `67` through `10^8`, and requires byte-identical stdout against
`results/sharp_h67_exact_1e8.txt`.

The producer uses a segmented radical sieve and `unsigned __int128` correction
checks. Long-double square-root values are guesses only; integer inequalities
move every guess to the unique accepted directed integer before it is used.

## Coverage semantics

On `[N,N+1)`, the defect is

```text
4 sqrt(x) A_beta(N) - 3 B_beta(N).
```

It is monotone on the cell. The producer encloses both:

```text
x=N       after activation of beta(N),
x=(N+1)- before activation of beta(N+1).
```

Thus the retained theorem covers every real

```text
67 <= x < 100000001.
```

## Scientific boundary

The retained JSON deliberately records

```text
global_tail_proved=false
rh_established=false
```

The scan is a finite proof object, not an extrapolation to the unbounded tail.
