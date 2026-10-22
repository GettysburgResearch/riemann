# X-19801 — exact square-screw level combiner

This standard-library verifier combines one directed finite-level certificate for

\[
\mathscr S(N)=-g_\zeta(2\log N).
\]

It uses `fractions.Fraction` only. The transcendental interval producer and the proof that the prime-power manifest is complete are external typed gates; the verifier binds their cutoff, count, and SHA-256 and rejects an assumed or incomplete manifest.

The retained synthetic certificate proves

```text
N                         2
cutoff                    4
elementary term           2
prime interval            [9/20,9/20]
linear interval           [-1/2,-2/5]
Lerch interval            [1/10,1/8]
total interval            [23/20,51/40]
verdict                    CERTIFIED_NONNEGATIVE_SQUARE_LEVEL
proof-object SHA-256       b611ca0b4c6b68e45a746ad021ad5a62defe45c18700a464abb12e30f4075b43
```

This is a finite arithmetic regression only. It does not evaluate the Riemann screw function and does not prove any cofinal assertion.
