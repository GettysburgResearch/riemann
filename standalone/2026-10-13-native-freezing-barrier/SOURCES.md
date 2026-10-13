# Sources, credit, and inherited boundaries

## Repository sources actually inspected

- **PR #936**, `eb8d23decc003d36ded287dc98868308192cc889`,
  [PROOF.md](https://github.com/GettysburgResearch/riemann/blob/eb8d23decc003d36ded287dc98868308192cc889/standalone/2026-10-13-rough-conductor-localization/PROOF.md).
  This is the parent result. Its exact mask-preserving projection, log-square
  upper theorem, and real rough-block remainder are retained. Its lower
  example permits arbitrary aligned phases and an uncontrolled-height CRT
  row. The new lower argument instead keeps native mu_K, a fixed compact
  test, and rows 1 and b^6 inside the specified physical box.
  The inspected proof is 15,711 bytes, Git blob
  `4eeab473b82c55af37bc5e12dc7505a386badc2f`, SHA-256
  `748bd3af30d8de546160dc1e85c2859c8ef93735eb9c5ea46b6ab17faca45787`.
- **PR #937**, `9f3250198a9b0551f42eb73dfd74a265c2a66854`,
  [PRIME_FREEZING.md](https://github.com/GettysburgResearch/riemann/blob/9f3250198a9b0551f42eb73dfd74a265c2a66854/standalone/2026-10-13-prime-freezing-and-noise/PRIME_FREEZING.md).
  Its full proof note was read. It proves the growing deterministic-prime
  sign model and an exact signed freezing flux, and already gives a
  sharpness example for an enlarged coefficient class. These are credited,
  not reproved as new. Its sign model uses roots of order two, whereas #936
  uses sixth-root phase multiplication. The conditional-mean lower argument
  in this packet would apply to either mean-zero randomization. We state
  it for the precise #936 model, without importing the sibling upper proof.
- **PR #931**, mathematical source
  `3968d1b7135900e6130412f58a39bc67e73d4ecb`, and **PR #933**,
  `988f4571bf9ffec65cd73ccb092301550c054ae0`: their prior descriptions and
  the supplied conversation account identify the finite Euler resonance,
  trace obstructions, and sixth-power extraction mechanisms. They are
  comparison/credit sources, not un-replayed analytic hypotheses here.
  The new Mellin identity keeps a genuine smooth norm filter, and extracts
  a physical-scale witness instead of bounding an unfiltered trace.
- **PR #935**, `a7a7fad2c5fa1929c7e04570cde4188e3191b071`: inspected at
  PR-description scope. Its logarithmic Mobius--Liouville square-divisor
  transfer is distinct from this packet's first-prime dilation cost.
  No theorem from its proof note is silently used.

The repository's AGENTS.md was fetched at the parent ref. The new packet
changes neither the integrated status nor any inherited proof file. The
latest PR search was checked before writing; this is not a comprehensive
historical priority audit. No claim of global novelty for classical finite
Euler/Mellin arguments is made.

## Classical analytic input

The sole prime-distribution input is the classical fixed-modulus theorem

    #{p<=x : p=1 mod 3} ~ x/(2 log x).

It supplies pi_K(x)~x/log x and at least c T/log T split primes in [T/2,T].
Only modulus 3 is used: no conductor-uniform, short-interval, or GRH version
is assumed. The deductions of the prime-ideal weighted sums are written
in SMOOTH_MOBIUS_RESONANCE.md.

A primary modern proof is D. Koukoulopoulos, *Pretentious multiplicative
functions and the prime number theorem for arithmetic progressions*,
Compositio Mathematica 149 (2013), 1129--1149,
[arXiv:1203.0596v3](https://arxiv.org/abs/1203.0596v3),
DOI `10.1112/S0010437X12000802`. Its bibliographic record was checked online;
its full proof is not independently reconstructed here. The exact classical
fixed-modulus statement was also checked in the official
[NIST DLMF 27.11](https://dlmf.nist.gov/27.11), final paragraph.

The surrounding random-multiplicative literature is context, not an input:
A. J. Harper, *Moments of random multiplicative functions, II: High moments*,
[arXiv:1804.04114](https://arxiv.org/abs/1804.04114), and R. Angelo--M. W. Xu,
*Oscillations of random multiplicative functions under initial bias*,
[arXiv:2411.14447](https://arxiv.org/abs/2411.14447). The latter concerns a
completely multiplicative sign/positivity problem. Its log-square scale is
not by itself a theorem about the native sextic moment studied here.

## Exact arithmetic reuse

`checks/eisenstein_source.py` is an unchanged copy of #936's
`checks/check_rough_projection.py`: 13,240 bytes, Git blob
`64d21a7f400f5bf5654fd67735743ff1befab067`, SHA-256
`c82b016a86bcfba2105558db3fec5cbc60a564b6354d94b0cc367ad1a3879833`.
The new checker authenticates that blob before using its integer/cyclotomic
arithmetic. Reuse of that arithmetic is not counted as a new theorem.
