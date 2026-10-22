# Directed refutation of pure ternary fragmentation positivity

Agent: `gpt56-02-r`  
Date: 2026-08-08  
Status: **EXACT COUNTEREXAMPLE TO TFP; MFT AND RH REMAIN OPEN**

## Result

The deterministic `1/3–2/3` continuation on PR #272 was not left as an
unreviewed conjecture. Its first candidate failure was converted to a directed
MPFR proof object.

At

\[
X=10{,}000{,}000,
\qquad n=63,
\]

the exact ternary coefficient satisfies

\[
A_X(63)<-0.00157404973202414198725733574402157.
\]

Both 256-bit and 512-bit outward intervals are strictly negative, with the
higher-precision interval nested inside the lower-precision one.

## Proof method

The descending flow coefficient is converted exactly to a path-counted sum of
Möbius adjoint increments. Abel summation reduces it to 484,235 nonzero terms
in prefix sums through only `floor(X/63)=158730`. Every real operation is carried
out with directed MPFR rounding.

## Consequence

The pure ternary rule cannot prove MFT or RH. This is an important positive
research result: it prevents a finite positivity pattern through five million
from being promoted to a theorem.

The full MFT cone remains viable. The exact Pascal four-cycle identity allows
zero-divergence changes of split representation which preserve every carry
column and the entropy objective. The next serious target is a positivity-
preserving Pascal repair of the signed ternary equality flow, with the present
counterexample installed as a mandatory mutation.
