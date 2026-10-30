# Exact-arithmetic quartic prime-row mixed-moment experiment

**Scope.** This is an exploratory finite computation, not evidence for a theorem, a zero-density estimate, or asymptotic cancellation. It tests only quartic prime rows over `Q(i)`, fixed height zero and fixed smooth or sharp annular profiles. In particular it does not model the row-dependent detector zero, the full fourth-free family or the selected large-value rows.

For `X=1000,3000,10000,30000`, enumerate every rational prime `X≤p≤2X`, `p≡1 (mod 8)`, and select one primary Gaussian prime π over p. With `D=X^(10/13)` and `N=X^(5/13)` compute

    M_π=D^(−1/2) Σ_(D<N a<2D) μ(a) χ_π(a) W(Na/D)(Na/D)^(−4/5),
    S_π=N^(−1/2) Σ_(N<N a<2N)      χ_π(a) W(Na/N)(Na/N)^(−4/5).

The sums are over Gaussian ideals coprime to the prime over 2; primary generators are used to compute quartic residue symbols exactly in `F_p`. For p≡1 mod 8, the primary quartic reciprocity sign is 1, which puts this selected ray sector in the natural source orientation. The code lists each Gaussian ideal once modulo units and computes the ideal Möbius function from exact integer factorization of its norm. A separate [arithmetic check](check_arithmetic.py) checks representative Möbius values and quartic reciprocity for all chosen prime pairs up to 500; this is a check, not a proof of the implementation in general. The script uses NumPy and Python integer modular exponentiation, with no floating-point evaluation of residue characters.

[experiment.py](experiment.py) outputs CSV; reproduce the stored [smooth results](smooth.csv) and [sharp-annular results](annular.csv) with

    python check_arithmetic.py
    python experiment.py --scales 1000 3000 10000 30000 --profile smooth --max-rows 0 > smooth.csv
    python experiment.py --scales 1000 3000 10000 --profile annular --max-rows 0 > annular.csv

The smooth profile is `exp(4−1/((x−1)(2−x)))` on `(1,2)` and zero outside; the sharp profile is its annular indicator. The raw CSV includes row counts, lengths, sums, maxima and counts exceeding the unadjusted formal thresholds. Write `E` for the average over the enumerated rows. The two dimensionless diagnostics are

    C = E(|M|²|S|²)/(E|M|² E|S|²),
    H = E(|M|²|S|²)/sqrt(E|M|⁴ E|S|⁴).

| X | rows | C, smooth | H, smooth | C, sharp | H, sharp |
|---:|---:|---:|---:|---:|---:|
| 1000 | 31 | 1.006 | 0.442 | 0.916 | 0.454 |
| 3000 | 85 | 0.937 | 0.540 | 1.150 | 0.556 |
| 10000 | 261 | 1.094 | 0.566 | 1.085 | 0.533 |
| 30000 | 695 | 1.035 | 0.478 | not run | not run |

On these runs, the mixed second moment is of the same rough order as the product of marginal second moments; Cauchy's fourth-moment bound is not close to equality. This suggests a possible **research target**: control the actual mixed moment on this fixed prime-row family with essentially bounded average, uniformly over the required common profiles and heights. No such estimate is established by these numbers. The ordinary annulus has only 5, 9, 15 and 21 ideals, respectively, so the displayed ratios are especially sensitive to the cutoff. The sharp profile is not a substitute for a uniform smooth-profile theorem.

The formal large-value tests `|M|²≥D^(3/5)`, `|S|²≥N^(3/5)` found no simultaneous rows in these runs. The detector inequalities contain unspecified constants and power losses and use zero-dependent profiles, so this is not evidence that a detector class is empty. The prime-row family itself is a thin subset of all natural rows; averages here cannot bound the full family or establish a power saving. Extending the observed behavior would require genuine signed cancellation in off-diagonal quartic character correlations at combined column length `DN=X^(15/13)`, with all ray sectors, masks and heights maintained.

**Independent check.** Other_families reviewed the ideal enumeration, split/inert Möbius rules, primary generators and modular quartic roots, and reran the arithmetic checker and one smooth-profile example. This checks the finite implementation, not an asymptotic estimate.
