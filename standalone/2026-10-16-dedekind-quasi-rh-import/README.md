# Dedekind quasi-Riemann import and research assessment

**Status: external-source import and proposed research assessment.** No new zero-free theorem, native higher-moment estimate, or RH proof is asserted. No independent mathematical review or Lean build was performed in this import.

**Requested source:** Dean Cureton and Jesse Thorner, *A quasi-Riemann hypothesis for Dedekind zeta functions*, [Hexagon 2610.00200v1](https://hexagonmath.org/2610.00200v1).

**Pinned formal source:** [AxiomMath/DedekindZetaZeroFree at `09afbb4ce6570c1615d58509dc197fc9f0956b7d`](https://github.com/AxiomMath/DedekindZetaZeroFree/tree/09afbb4ce6570c1615d58509dc197fc9f0956b7d), dated 13 October 2026. The pinned statement is the zero-free half-plane **Re(s) > 31/32** for every number field and for finite-order Hecke characters, with the appropriate pole exception at one.

## Read first

- [RESEARCH_ASSESSMENT.md](RESEARCH_ASSESSMENT.md): significance, proof mechanism, exact bottlenecks, connections to this repository, and prioritized attacks.
- [SOURCE_MAP.md](SOURCE_MAP.md): statement fidelity, the formal dependency path, copied versus merely inspected files, version and manuscript-access limitations.
- [VALIDATION.md](VALIDATION.md): exactly what was checked and what remains unverified.

## What is imported

Thirteen unchanged upstream files are physically present under `upstream/`: the Challenge and Solution, Dedekind and Hecke entrypoints, cyclotomic descent entrypoint, scale constants, growth argument, exact Euler-correction algebra and recipe, build configuration, comparator configuration, toolchain, and Apache license. Their original Git blob identities, SHA-256 hashes, lengths, and canonical paths are recorded in [UPSTREAM_LOCK.json](UPSTREAM_LOCK.json).

This is a **selected source snapshot, not a self-contained Lean checkout**. The transitive theta and class-field libraries are not duplicated here. [reproduce_upstream.sh](reproduce_upstream.sh) fetches the complete original repository at the exact pin into a new directory; its optional `--build` mode runs the upstream build, comparator, and axiom-print commands. Those network/build commands were not run successfully in this environment.

**Manuscript limitation:** Hexagon's indexed landing record was readable, but the manuscript and source downloads were inaccessible. No PDF or LaTeX manuscript bytes are included or claimed to have been read. The record advertises a v2 dated 14 October 2026; its body was not retrieved. This import preserves the requested v1 citation and pins the separately accessible 13 October formal release, without claiming that release formalizes v2.

## Main assessment

The advance is **generality and reusable proof infrastructure**, not a numerically better Riemann-zeta exponent than the previously imported special-setting bounds. Its promising contributions are the field-general metaplectic/theta construction, an actual reflected second-moment source, and a nonvanishing Mellin certificate. None automatically supplies our missing signed high-moment covariance.

The exact published growth budget contains two almost equal terms. At unchanged scales, improving the reflected estimate alone stops at the comparison-error boundary **1937/2000**, only **1/4000** below 31/32. The inspected numerator product is proved holomorphic and nonzero only above **2/3**. The new [normalization note](RENORMALIZED_CERTIFICATE.md) removes its explicit sixth-power Euler denominator and proves that the remaining product is holomorphic and nonzero above **1/2**. This gives an exact signed-dilation target, not a bound for that target or an improvement to 31/32.

The strongest proposed direction is to bound the explicit renormalized signed probe, keeping the comparison residual together, then test an exact bridge to #946's injection-minus-compensation and #944's conductor window. A higher-order or varying-cover period hierarchy is a second, more speculative route. Both have explicit unproved interfaces in the assessment.

## Local checks

```sh
python checks/check_import.py
python -O checks/check_import.py
```

These verify source identities, the declared theorem/build interface, and rational exponent bookkeeping. They do **not** check Lean proof terms, the transitive axiom footprint, a native moment estimate, or the manuscript.

This packet is added independently on the repository's `main` baseline. Research PRs are cited at immutable commits; none is silently merged or promoted to integrated status.
