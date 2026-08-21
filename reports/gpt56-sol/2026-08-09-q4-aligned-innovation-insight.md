# Q4 aligned innovation scope correction

The first version of this note was wrong and is superseded by the corrected `L-32305`.

The exact aligned compact-current row is

\[
\begin{aligned}
\mathcal L_{4n,4j}(q_\circ)
={}&\psi(4n)-\psi(4j)-\psi(4k)\\
&-4[\psi(n)-\psi(j)-\psi(k)]-4\log4,
\end{aligned}
\]

not a binomial-factorial ratio. The error was substituting Kummer's carry identity for `Lambda` into an additive defect of the Chebyshev prefix `psi`.

Thus the actual innovation retains a genuine radix-four Chebyshev fluctuation and remains RH-bearing. No `O(log n)` scalar innovation theorem is claimed.

The correction is pushed immediately; the SHARP outer-seven-eighths theorem is unaffected.
