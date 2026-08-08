# O-30501 — Corrected full-problem target after the terminal-boundary obstruction

Claim ID: `O-30501`  
Status: **RESEARCH SYNTHESIS — exact new direction, no RH claim**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08

## 1. What the obstruction means

The first boundary is macroscopically large in the divisor-source norm but is
created as the difference of two structured flows:

```text
positive analytic central flow
minus
positive finite central flow.
```

Taking its atomic norm separately destroys precisely the cancellation needed
for the sharp constant four.

This is the same failure pattern as:

- the monotone positive-part cover;
- the prime-only queue;
- fixed Abel positivity;
- rowwise absolute values in reflected packets.

## 2. Correct next object

Let \(d_{\rm an}\) be the positive analytic-bank flow and \(d_{\rm fin}\) the
positive finite central flow on the same stopped-power layer. The boundary
source is the carry image of

\[
d_{\rm fin}-d_{\rm an}.
\]

The load-bearing quantity is therefore not

\[
\|\sigma\|_{\rm at},
\]

but the negative capacity after **joint cycle optimization**:

\[
\boxed{
\inf_z
\mathcal N_\omega
\bigl(
d_{\rm fin}-d_{\rm an}+C_\eta z
\bigr).
}
\tag{O-30501.1}
\]

At the first critical stage, \(d_{\rm fin}\) is nonnegative and its residual is
decreasing. Thus the linear source lower bound does not imply linear optimized
debt.

## 3. New proof programme

A valid continuation should emit the two flows themselves and solve their
difference in the explicit Pascal-cycle basis of PR #272:

```text
stopped-power analytic tree;
finite endpoint tree;
their exact shared-edge cancellation;
remaining noncanonical cycle coordinates;
capacity-weighted negative part.
```

The first two central stages are already nonnegative. The source ledger should
start only after those complete positive stages have been removed.

This is a finite constructive theorem, not a source-norm estimate and not an
RH-equivalent scalar restatement.
