# R-7101 — Full-complex Pick midpoint ghosts in the first high-height grid

Claim ID: R-7101  
Title: The promising negative Pick screens in the first high-height grid are precision artifacts  
Status: REFUTED  
Authoring agent: `gpt56-03-f`  
Reviewing agents: none  
Created: 2026-07-25  
Last updated: 2026-07-25  
Dependencies: X-3902 primitive grid artifacts; `L-3903`; `L-7101`  
Scope: exact eight-node same-height Pick matrices in the first X-3902 carrier window  
Related counterexample candidates: none

## Refuted nomination

The first rigorous 128-bit X-3902 grid used the exact horizontal ladder

\[
 x\in\{2^{-17},2^{-15},2^{-13},2^{-11},2^{-10},2^{-9},2^{-7},2^{-5}\}
\]

at 65 exact ordinates. Near rank deficiency, midpoint eigensolves displayed
multiple negative eigenvalues of size roughly `10^-35` through `10^-33`.

The most discussed frozen screen was at

\[
 T=\frac{20225875608342450317715}{2^{32}},
\]

where an eight-point real-vector midpoint screen appeared negative. The original
X-3902 precision ladder later made that exact real direction positive. The user
requested that the verdict be reopened because one-vector positivity does not
prove positivity of the full complex matrix.

## Triple recheck

### 1. The original real direction

The exact integer vector was replayed at 192, 256, 384, and 512 bits. Every
directed interval had a strictly positive lower endpoint and converged after
normalization to approximately

\[
 +6.7369660275844976\times10^{-37}.
\]

This excludes the originally frozen real direction.

### 2. The true full-complex direction

The 512-bit primitive rectangles were intersected exactly. The complete complex
Hermitian midpoint Pick matrix was reconstructed, including the imaginary parts
of `xi'/xi`. Its true complex midpoint minimum eigenvalue is positive,
approximately

\[
 +2.1247974259266701\times10^{-41}.
\]

A Gaussian-rational direction obtained by one high-bit-depth rounding of that
complex eigenvector was contracted by a separately structured exact checker.
The resulting directed interval was strictly positive, with width below
`9e-148` after normalization.

### 3. The entire matrix box

The stronger `L-7101` certificate takes

\[
 \delta=2^{-136}.
\]

Exact Gaussian-rational `LDL^*` elimination proves

\[
 M-\delta I\succ0
\]

for the rational midpoint matrix `M`. The complete primitive rectangle
uncertainty has exact Hermitian row-sum bound

\[
 E<5.758\times10^{-147}<\delta.
\]

Therefore every actual Pick matrix admitted by the 512-bit boxes satisfies

\[
 K\succeq(\delta-E)I\succ0,
\]

with lower margin exceeding approximately

\[
 1.1479\times10^{-41}.
\]

This quantifies over every real or complex vector. The original refutation was
not premature; it was merely weaker than the now-available whole-matrix proof.

## Wider ambiguous-block audit

The 128-bit midpoint scan contained 29 full-complex negative eigenscreens. Fourteen
of the corresponding ordinates already had independently retained 192-bit
primitive rectangles. For each such block, the 128-bit full-complex midpoint
minimum direction was frozen to Gaussian integers at scale `2^256` and replayed
with exact rational contraction.

Results:

```text
blocks replayed                  14
certified positive directions   14
certified negative directions    0
unresolved directions            0
```

The positive normalized values range from about `1.3e-38` to `1.0e-34`. The
complete row ledger and verification hashes are retained in

```text
experiments/X-3904-complex-pick-recheck/results/
  complex-batch-192-summary.json
```

## Strongest newly discovered midpoint negative

A full-complex reconstruction found an additional 128-bit midpoint screen at

\[
 T=\frac{20225875608341108140435}{2^{32}}
   =T_0-\frac{15}{32},
\]

with displayed midpoint minimum eigenvalue

\[
 -2.626429492911995\times10^{-33}.
\]

A Gaussian-integer direction was frozen at scale `2^256`. Contraction against
the original 128-bit rectangles was unresolved because their width was about
`10^-30`, much larger than the midpoint sign.

A genuinely different ordinary-high-precision implementation, based on mpmath's
Riemann--Siegel assembly, then evaluated all eight exact points and the same
frozen vector:

```text
50 digits:  normalized fixed form  +1.1392326588e-33
60 digits:  normalized fixed form  +1.2260274370e-35
70 digits:  normalized fixed form  +1.2260274656e-35
```

At 60 and 70 digits the independently recomputed complete matrix minimum also
stabilizes positive near

\[
 +1.2259907375\times10^{-35},
\]

while the second eigenvalue remains around `4.16e-26`. Thus this nomination is
also a cancellation ghost. Because this second implementation is not directed,
the verdict is an empirical refutation of the numerical nomination, not a
proof-grade positive matrix certificate.

## Infrastructure audit

New FLINT workflows failed before publishing a first job step or artifact on
2026-07-25. Rerunning an unchanged previously successful FLINT workflow failed
in the same pre-step manner. No mathematical or code conclusion is drawn from
those failures. All rigorous statements above use previously successful,
immutable artifacts; the new `j=-15` result is explicitly labeled ordinary
high precision.

## Exact conclusion

The previously promising Pick candidate does not survive rederivation,
full-complex reconstruction, vector freezing, higher precision, or complete
matrix-box analysis. No negative directed interval remains and no `Z-####`
identifier is allocated.

The finite-table result does not support RH outside the declared point sets.
It instead shows that further optimization on this same-height eight-node table
is low value. A genuine continuation must enlarge the primitive feature space:
new ordinates, adaptive horizontal nodes, cross-height complex packets, or direct
`xi'/xi` jets.

## Adversarial audit

- The complex contraction uses both real and imaginary primitive rectangles.
- The exact vector is frozen before precision escalation.
- The whole-matrix proof uses exact pivots, not a rounded eigenvalue.
- The uncertainty bound covers every admitted primitive rectangle value.
- The fourteen-block audit does not claim whole-matrix positivity at those
  fourteen heights; it certifies only the frozen directions.
- The `j=-15` independent replay is not called a directed certificate.
- Parent normalization and the Pick implication retain their repository status.

## Suggested next attack

Do not spend another search pass refining the same closed point table. The two
live finite-witness offenses are:

1. cross-height complex Pick packets that retain vertical phase information;
2. the complete directed `4,118,082,969`-term D-0801 carrier certificate with
   the recovered 96-bit vector and exact correction moat.
