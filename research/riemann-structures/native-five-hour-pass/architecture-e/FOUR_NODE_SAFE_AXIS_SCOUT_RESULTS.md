# Four-node safe-axis scout result

Status: BOUNDED POSITIVE RECONNAISSANCE; independently replayed and frozen;
no continuum theorem.

The first registered run was stopped at the 120-second wall cap before it
created an artifact. It had redundantly recomputed the same scalar F values
for every packet. No panel outcome from that run was observed or accepted.
A precision-keyed scalar cache was added without changing the grid, formulas,
precision, finalist rule, source pins or scientific caps.

The unchanged campaign then completed in 28.188 seconds. It evaluated all
1,911 registered packets and returned 'POSITIVE_ON_REGISTERED_GRID'.
All 24 smallest generalized eigenvalues agreed between 100- and 200-digit
calculations to the registered 60-digit tolerance. The smallest was

    1.0365420586722290844298541592742852462139135063e-11

at the 2^-32 fourfold near-confluent endpoint panel

    (1/2, 1/2+2^-32, 1/2+2^-31, 1/2+3*2^-32).

The same near-endpoint family occupied the smallest four entries. The
smallest separated primary-grid packet was '(1/2,9/16,3/4,1)', with value
about '9.1195731e-11'. Thus this grid points to the fully confluent endpoint
jet as the hard chamber, not to the high-axis or mixed-node regions.

The registered high control and source-basis full-confluence control at256
were positive. Artifact size is 6,261,041 bytes, within the8MiB cap. Final
proof SHA-256:

    eebb53b7eb22107b9949a3e70545a97e7b08ff8d504bdde23bae56766a99032a

The fresh full check passed in 32.328 seconds and the optimized full check
passed in 33.719 seconds. All 12 compact hostile/source controls passed in
ordinary Python (0.211 s) and optimized Python (0.230 s). Ruff passed before
the final write.

This is finite numerical reconnaissance. It supplies no interval enclosure
between grid packets and no proof that the limiting endpoint jet is positive.
In particular, the positive values must not be promoted to four-node safe-axis
positivity or RH.

The root reviewer independently reran the complete 1,911-packet check in
ordinary and optimized Python and all 12 hostile tests in both modes.  The
four runs passed with the same typed artifact and final proof hash.
