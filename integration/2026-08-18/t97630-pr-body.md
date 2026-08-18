## Purpose and provenance

Publish a collision-free archival reconstruction of the cutoff-239
parity-contractive annular candidate described in the earlier Branch3 digest.
The unavailable original proof-evidence packet has **not** been recovered, and
this draft must not be read as byte-identical or evidentially equivalent to it.

This packet is intentionally distinct from PR #576.

## Exact target

```text
base PR:      #565
base SHA:     339e3367660f40c74795802a6f8170b15e19b13a
head branch:  research/gpt56-pro/97630-corrected-p61-bias-annular-closure
```

## Main statements

```text
PR #565 bias from x>=67                refuted at x=184
smallest surviving integer cutoff      239
F>=0                                   1<=x<239
M/40<=F<=M/8                           x>=239, all real
PR #566 reserve=>current domination    false as an implication
low children                           recombined before observation
high recursive mass                    <1/8
strict hereditary margin               1/960
annular Mellin numerator                zero-safe
T-97630                                reconstructed candidate digest / review
RH                                     unproved
```

## Evidence boundary

The included Python replay checks the `x=184` witness, cutoff constant, formal
recombination/contraction identities, the reserve/current countermodel, Mellin
finite-factor flag, and mutations. The included C++ checks the `x=184` witness
and endpoints `67..238`; despite retaining `FINITE_N=2,500,000`, it does **not**
execute the advertised sweep through 2.5 million and does **not** implement the
analytic tail. Accordingly, the all-real cutoff-239 certificate is a
reconstructed candidate statement, not a fully replayed theorem in this PR.

The first hostile-review target is the literal atomwise source-tree theorem
identifying the proposed current/high-child recursion with the native annular
Möbius scalar.
