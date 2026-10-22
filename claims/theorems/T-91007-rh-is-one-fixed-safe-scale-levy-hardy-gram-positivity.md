# T-91007 — Scalar fixed-scale Lévy–Hardy criterion: blocked and superseded

Claim ID: `T-91007`  
Status: **UNPROVEN / ORIGINAL REVERSE IMPLICATION USED FALSE `L-91032`; SUPERSEDED BY `T-91008`**  
Created: 2026-08-11  
Corrected: 2026-08-12  
RH status: **unproved**

## 1. Original proposal

The original packet fixed one `a_0>1/2`, used one causal Cauchy mother, its
anti-causal reflection and one bridge, and proposed

\[
 \mathrm{RH}
 \Longleftrightarrow
 \mathbb K_{a_0}\succeq0
\]

on every finite carrier/orientation/bridge packet.

The forward implication under RH was the zero-side Lévy Gram.  The reverse
implication relied entirely on the claim that the scalar family was dense in
the complete weighted mean-zero screw space.

## 2. Why the proof is invalid

`R-91008` gives an exact hidden jump vector supported beyond an interior zero
of the physical causal mother.  Hence the scalar causal family has more than
the declared one-dimensional half-line defect.  `L-91032` is false as stated,
and positivity on its finite Gram packets does not imply positivity of the
complete screw form.

This is not a minor regularity gap.  The missing directions are explicit
nonzero vectors.

## 3. What survives

The following statements from the original packet remain valid at their
stated or proposed scopes:

```text
under RH the scalar two-orientation kernel is a Lévy Gram;
the scalar recurrence is one causal diagonal;
every fixed-safe-scale entry is absolutely Eulerian;
finite negative matrices would be finite countercertificates;
full carrier polarization is essential.
```

The RH equivalence is not retained for the scalar index set.

## 4. Corrected criterion

`L-91034` introduces a positive delay fibre.  The corrected index set is

\[
 (\{+,-\}\times\mathbb R\times[0,\infty))
 \sqcup\{\star\}.
\]

Subject to independent review of the repaired density theorem, positivity on
every finite delayed packet is equivalent to the full screw positivity and
hence to RH.

The corrected final component is not a full-Fock-to-one-scalar-Hardy map.  By
`L-91035`--`L-91037` it is a completed **first-chaos tangent lift** into the
delayed two-sided Hardy reserve.  Its normative statement is `T-91008`.

## 5. Exact boundary

```text
RH -> scalar fixed-scale Lévy Gram                 RETAINED
scalar Gram -> full screw form                     FALSE PROOF / NOT ESTABLISHED
scalar fixed-scale RH equivalence                  BLOCKED
corrected delayed fixed-scale criterion            PROPOSED COMPLETE in T-91008
completed first-chaos tangent intertwiner          OPEN / RH-EQUIVALENT
Riemann Hypothesis                                 UNPROVED
```
