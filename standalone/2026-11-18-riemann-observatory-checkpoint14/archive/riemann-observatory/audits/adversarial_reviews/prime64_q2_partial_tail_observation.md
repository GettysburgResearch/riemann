# Certified \(Q_2\) partial sums and a quartic-tail diagnostic

These checks certify complete finite partials of
\[
 C_{\le Y}=\sum_{\substack{\rho=1/2+i\gamma\\|\gamma|\le Y}}
             \frac{|\zeta'(\rho)|^2|2^{1-\rho}-1|^2}{|\rho|^2}.
\]
They also evaluate, using Arb balls for the exact symbolic coefficients, the quartic main term for the RH-conditional infinite tail. The resulting totals are numerical diagnostics. A numerical error constant for the omitted tail remainder is still needed before treating them as enclosures of \(C_2\). [Quartic derivation](prime64_q2_full_polynomial.md)

For each \(Y\), Arb computes the all-zero positive count at \(Y+2^{-10}\). The run checks that the count is an exact integer and that this many pairwise disjoint, strictly positive ordinate balls lie on the line below \(Y\). At each ball the interval for \(|\zeta'(\rho)|\) is strictly positive, proving that the certified zeros are simple. These checks exhaust the count and exclude a zero at the cutoff. Reflection supplies the negative ordinates. The real midpoint is excluded by the eta-series sign. The partials are therefore unconditional finite certificates. The script stores each interval by outward dyadic endpoints as well as a decimal display.

The incorrect control deletes the oscillating cross term in \(|Q_2|^2=3-2\sqrt2\cos(\gamma\log2)\) and substitutes three times the full untwisted tail polynomial. Its leading tail coefficient is three times the correct one. This makes it a control for the arithmetic factor as well as for the low-order terms.

| Height \(Y\) | Positive count | Certified partial, rounded for display | Partial plus quartic tail model | Partial plus incorrect control |
|---:|---:|---:|---:|---:|
| 100 | 29 | 0.252538016854565 | 0.652217626203123 | 0.827876117116119 |
| 400 | 202 | 0.429482203409325 | 0.653464894674835 | 0.785280768500830 |
| 1000 | 649 | 0.512027298499316 | 0.653461514245364 | 0.749360227092275 |
| 10000 | 10142 | 0.616498752887311 | 0.653393857725111 | 0.685399541864903 |

The partial-plus-quartic values at 400 and 1000 differ by about \(3.38\cdot10^{-6}\); the incorrect control changes by about \(3.59\cdot10^{-2}\) over the same heights. This agreement is a check on the expected numerical scale of the symbolic coefficients. The finite partial at 10000 gives \(C_2>0.61649875288731141829\). Combining it with the previously rigorous unconditional majorant \(5.218866\) for the true tail at 10000 yields \(C_2<5.83537\) for the series. This upper bound does not use the quartic model. [Centered Hardy tail bound, equation (2) with \(Y=10000,J=8\)](prime64_main_term_moments.md)

The 128-bit run through 1000 took about three seconds in this workspace. It uses FLINT 3.6.0 and the existing Python runtime. The 160-bit replay through 10000 took about 99 seconds, and its exact dyadic intervals overlap the 128-bit ones at the three shared heights. The pre-existing height-100 director checks remain unchanged. [Experiment script](../../scripts/prime64_q2_partial_tail_observation.py) · [128-bit results](../../experiments/results/prime64_q2_partial_tail_observation.json) · [160-bit results](../../experiments/results/prime64_q2_partial_tail_observation_y10000.json)
