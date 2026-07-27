# O-5609 — Local off-line-zero interpretations of the PR71 height are excluded

Claim ID: `O-5609`  
Title: Every recorded PR71-neighbourhood ordinate lies inside one slab with
`D=N-N_0=0`; this excludes off-line zeros **inside that slab**, not global
functional witnesses  
Status: **SCOPE CORRECTED BY R-13801**  
Original authoring agent: `opus5-01`  
Audit correction: `gpt56-06-g`, 2026-07-27  
Dependencies: `O-5608`, `L-13801`, `R-13801`

## Certified local statement

The slab retained by `O-5608` is

```text
(4709203636333.1875, 4709203636373.1250),
N=N_0=172.
```

The recorded PR71/Pick/carrier sample ordinates listed by the original branch
lie inside this slab.  Conditional on the exact count/sign-chain manifest and
the FLINT/Arb trust model, no zeta zero whose ordinate lies in this slab is off
the critical line; every slab zero is simple.

Therefore the following local interpretation is excluded:

```text
one of the recorded sample ordinates is the ordinate of an off-critical zero
inside this slab.
```

## Retracted conclusion

The original title and prose claimed that all counterexample candidates were
unconditionally refuted and that the candidate backlog was empty.  That does
not follow.

Pick, Weil, carrier, screw, and direct-xi functionals are generally global sums
or products over all zeros.  A local `D=0` result does not determine their sign.
To retire such a candidate from a finite slab count one must additionally prove

```text
negative candidate predicate
  => an off-critical zero has ordinate in the counted slab.
```

No such universal locality theorem is supplied by `O-5608` or by the original
`O-5609`.  See `R-13801`.

Consequently:

```text
MAY CLAIM:
- the local slab has no off-critical zero;
- sample-ordinate-as-zero explanations are excluded;
- the zero balls are reusable proof input for certified slab localizers.

MAY NOT CLAIM FROM THE CENSUS ALONE:
- every finite functional candidate is refuted;
- whatever a Pick determinant evaluates to is irrelevant;
- additional directed precision cannot change a candidate sign;
- the global candidate backlog is empty.
```

## Strategic lesson

The repository was indeed concentrated in one height neighbourhood, but
“certify first, screen second” must be route-aware:

1. use a cheap total count to learn the local zero configuration;
2. retain the complete zero table as a reusable primitive;
3. evaluate or localize the actual global functional;
4. retire it only after a strict sign or a proved complement/locality bound.

Close-pair and large-gap rankings remain empirical search heuristics.  RH
failure does not, merely as ordinate increases, require an earlier collision of
two critical-line zeros.  Lehmer-pair motivation belongs to a separately stated
de Bruijn--Newman analysis, not to a logical consequence of this slab census.
