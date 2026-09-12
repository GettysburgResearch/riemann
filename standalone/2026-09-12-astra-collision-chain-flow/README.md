# Collision–chain–flow: three source-specific RH continuations

**Proposed component research, not an RH proof. Independent mathematical and
implementation review required.** Date: 12 September 2026.

One add-only packet on main `f99d9e3908dde4865377c75d9ca051c1f545bf4f`.
Nothing in main, another research packet, canonical acceptance, formal sources,
workflows or repository settings is changed.

## Results

**Arithmetic — a sharp scale, not a signed-covariance bound.** The diagonal of
the latest crossing completion has matching upper/lower order (log Y)^4. The
new lower bound uses actual squarefree coprime product collisions and a complete
Euler-product argument. A bounded positive covariance-to-diagonal ratio on
unbounded native crossings is sufficient for the inherited full RH consumer;
nonpositive covariance is not necessary. That upper bound remains open.
Read ARITHMETIC.md.

**Ising — a genuinely infinite connected six-moment construction.** A new
four-group head and the growth-calibrated logarithmic harmonic tail admit an
exact six-moment native theta realization at q=0, certified by a full-source,
full-infinite-tail contraction. Analytic continuation in q supplies connected
ferromagnetic chains at every sufficiently small q>0, retaining the exact theta
moments 2,4,6 and all three real-field growth coefficients. No explicit positive
q radius is certified. A strictly negative eighth-moment error proves this
neighborhood is still not theta. Read ISING.md and NUMERICS.md.

**Gamma — an explicit source score and complete fixed-step zero current.** A
mean-preserving gamma-shape interpolation joins consecutive centered integer
stages. A positive homogeneous-polynomial series gives a tail-complete score
without a digamma evaluation. The finite-exception endpoint argument extends
uniformly over each fixed step, giving an exact weighted-zero balance including
multiplicities, births, collisions and real-axis crossings. Its signed
production is not proved dissipative. Read GAMMA.md.

## New work was incorporated, not silently repeated

The arithmetic input is the NEW crossing packet on #848, not the older balanced
Newton head originally ranked. #863 and #864 rule out inappropriate small-block
and complete-Bernstein shortcuts. #869 opened during this pass with a joint
three-route continuation and a Bessel-anchor gamma balance. #871 also opened
during this pass, establishing the connected growth-calibrated chain framework.
Its contribution is explicitly credited; the new Ising result here is the
six-moment calibrated extension at small q, not the framework itself. The
exact SHAs, paths and reading scopes are in SOURCES.json.

No claim of external novelty or of independent acceptance of those proposed
predecessor results is made. END_TO_END.md identifies every remaining global
premise and the complete conditional ending.

## Reproduce

From this directory, using Python 3.11 or later and only its standard library:

    python -B check.py --check results.json
    python -O -B check.py --check results.json
    python -B test_checks.py --partition unit
    python -O -B test_checks.py --partition unit

Repeat with --partition source, cli-a, cli-b, and integrity. The default command
runs all seven methods together; the recorded complete executions used the
five named partitions.

The complete accepting commands reconstruct the native theta source, all chain
root/tail bounds, every finite arithmetic control, and all gamma finite algebra
and positive-score panels. --emit is a producer, not an acceptance command.
Tests and their actual execution scope are recorded in VALIDATION.md. No full
repository checkout/build, Lean proof, remote CI or independent referee review
is claimed.

## Publication status

This author session could read GitHub but could not publish: no GitHub write
action was exposed and direct Git failed DNS. The delivery includes a ready
add-only patch, source archive, PR body and publication script for ONE PR.
**No branch, commit, or PR is claimed created by this session. In particular,
existing PR #869 is not attributed to this session.**
