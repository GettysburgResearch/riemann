# X-4501 — Exact checker for quantitative witness survival

Experiment ID: X-4501  
Status: exact algebraic synthetic controls; no RH computation  
Agent: `gpt56-06-b`  
Issue: #45  
Date: 2026-07-23  
Related claims: D-4501, L-4501, L-4502, L-4503, M-4501  
Candidate IDs: none

## Research question

Can one tiny standard-library checker verify that a frozen finite witness remains
strictly negative under every realization of a declared uncertainty set, while
failing closed on missing channels, broken dual proofs, excessive radii, or
unresolved logical gates?

X-4501 tests three certificate geometries.

1. `affine-box` — exact support function of independent rational intervals.
2. `affine-polytope-dual` — exact LP weak-duality certificate preserving
   correlation.
3. `pick-disks` — exact fixed-vector contraction of the Pick matrix followed by
   complex-disk support bounds.

The checker proves only quantitative survival inside the declared mathematical
uncertainty set.  It does not prove an RH equivalence theorem, analytic
normalization, or the soundness of a transcendental leaf enclosure.

## Files

- `verify.py` — exact checker using only integers and `fractions.Fraction`.
- `certificates/affine-box-survives.json` — strict independent-box moat.
- `certificates/affine-box-touches-zero.json` — deliberately unresolved control.
- `certificates/affine-polytope-correlation.json` — correlation preserved by an
  exact rational dual multiplier.
- `certificates/pick-disks-survives.json` — exact Pick contraction with small
  independent disks.
- `certificates/pick-disks-too-wide.json` — same midpoint, enlarged disks, sign
  no longer certified.
- `tests/test_verify.py` — committed controls and fail-closed mutations.
- `results/tests.txt` — recorded test run.
- `results/certificate-results.json` — deterministic summary of the committed
  certificates.

## Certificate semantics

### Affine box

For

\[
 q=q_0+\sum_i a_i u_i,
 \qquad
 u_i\in[c_i-r_i,c_i+r_i],
\]

the checker reconstructs

\[
 U=q_0+\sum_i(a_ic_i+|a_i|r_i).
\]

It certifies quantitative survival exactly when `U<0`.

### Correlated polytope

For

\[
 \mathcal U=\{u:Au\le b\},
 \qquad q=q_0+a^Tu,
\]

the producer supplies exact rational `y` with

\[
 y\ge0,
 \qquad A^Ty=a.
\]

The checker verifies the equalities and proves

\[
 q\le q_0+b^Ty.
\]

A rational feasible point is also checked so that the declared uncertainty set
is not accidentally empty.

The committed control uses

\[
 q=-1/10+u_1+u_2,
 \quad -1\le u_i\le1,
 \quad u_1+u_2=0.
\]

The joint dual certificate gives robust upper `-1/10`.  Forgetting the
correlation and using the independent box gives `19/10` and loses the witness.

### Pick disks

For exact points and vector, the checker reconstructs

\[
 c_j=\overline{v_j}\sum_k
 \frac{v_k}{s_j+\overline{s_k}-1}
\]

and checks the identity

\[
 v^*Kv=2\operatorname{Re}\sum_jc_jF_j
\]

against a direct exact matrix contraction on every run.  Given

\[
 F_j\in B(z_j,r_j),
 \qquad M_j^2\ge|c_j|^2,
\]

it verifies

\[
 v^*Kv\le
 2\operatorname{Re}\sum_jc_jz_j+2\sum_jM_jr_j.
\]

The committed exact coefficients are

\[
 c_1=18/13-i/13,
 \qquad |c_1|^2=25/13,
\]

\[
 c_2=-63/208+i/13,
 \qquad |c_2|^2=25/256.
\]

With centers `-1,-1` and radii `1/100`, the exact midpoint is

\[
 -225/104,
\]

the certified uncertainty increment is

\[
 137/4000,
\]

and the robust upper endpoint is

\[
 -110719/52000<0.
\]

Increasing both radii to `1` changes only the uncertainty set, not the midpoint;
the robust upper becomes

\[
 82/65>0,
\]

so the checker correctly refuses certification.

All Pick data are synthetic rational controls.  They are not evaluations of
Riemann `xi`.

## Uncertainty manifest

Every certificate declares the exact set of quantitative channel IDs used by
its score.  The checker rejects:

- a used but undeclared channel;
- a declared but unused channel;
- duplicate channels;
- a quantitative state outside the sound closure set;
- a logical gate marked `BLOCKING` or lacking an evidence locator.

Logical-gate strings are workflow metadata, not proof validation.  The result
`QUANTITATIVE_SURVIVAL_WITH_CLOSED_GATE_MANIFEST` means only that the manifest
claims all gates have approved states; the mathematical gate evidence remains a
separate review or formal-proof obligation.

## Commands

```bash
python -m unittest discover -s tests -v
python -m compileall -q verify.py tests

for certificate in certificates/*.json; do
  python verify.py "$certificate" --allow-not-certified
done
```

## Recorded result

Fifteen tests pass.  The mutation suite rejects:

- hidden and decorative uncertainty channels;
- a blocking logical gate;
- a broken `A^T y=a` dual equality;
- an infeasible polytope anchor;
- a Pick coefficient-magnitude underestimate;
- a point on the critical boundary;
- and a false claimed robust endpoint.

The two deliberately widened controls return `NOT_CERTIFIED`; they are not
parser failures.

## Proof boundary

Exact within X-4501:

- rational parsing and arithmetic;
- affine box support;
- rational LP weak duality checks;
- Pick fixed-vector algebra;
- squared coefficient-magnitude bounds;
- strict final sign comparison;
- uncertainty-manifest set equality.

Not proved by X-4501:

- any RH criterion or equivalence;
- any actual `zeta`, `xi`, prime, contour, or divisor computation;
- soundness of a future Arb/MPFI producer;
- absence of a shared bug between independent implementations;
- correctness of the Python runtime or hardware.

The experiment is proof infrastructure, not evidence for or against RH.

## Suggested next experiment

Use the `pick-disks` schema in Issue #39.  An Arb producer should export exact
rational outer disks for direct `xi'/xi` values at dyadic points.  The X-4501
checker should remain independent and reconstruct only the frozen fixed-vector
functional.  For shared jet or range-reduction errors, replace independent
disks by an affine/polytope certificate rather than widening them separately.
