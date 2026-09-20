# Sources, attribution, and exact reading boundary

> **Publication completed:** the executable companion is now resident in this
> directory. The earlier documentation-only publication is preserved at commit
> `5cd394d5dfe49d153be49e9eaab02e83efdce3f1`. See [PUBLISHER.md](PUBLISHER.md)
> for fresh replay results and the distinction from mathematical acceptance.

## Repository anchors

- Reading/publication starting parent: #904 at
  `d0d7ad05f9d4504e9d752518b34a9fd0609a06f7`.
  Root tree `eac4bbb9a8e9f47472925a521c7e78d69a6eb06f`.
  Branch `research/astra/20260919-divisor-square-mesh`.
- NCL29: `standalone/2026-09-20-native-frequency-localization/` at that head.
  Its complete proof and accepting arithmetic were read from the supplied
  archive; current GitHub contents identities were checked before publication.
  PROOF.md blob: `18dcfef25dd6bf73ce7e5f57a28769fe95bd71fa`.
  check.py blob: `5f4491e8186923ffe6bd101ce04ca4c723920ebf`.
  The latter has SHA256
  `3fb75554bf1750b9e42657e22041d59a7f3d83e54cdb9d36ee209dcf63a449aa`.
- NCG28: #904 at `879497b4f11be2618c448efc1fa93f69b4022e4c`.
  Its exact tail map and centering/source conventions are preserved in NCL29.
  This pass does not rerun its full campaign or use its 4/3 window bound as
  an unproved replacement for MCB31's microscopic estimate.
- DSE27: #904 at `4e8dea7004874d1a9c679b58db1dca1fbb539388`.
  Its original physical E-energy mesh campaign is not rerun or relabeled as F.
- BNR26/NIR26/PCR26: #848, preserved through
  `7de75c02417d5d8db7eafb1ceba364380e72d16a`.
  The innovation isometry, exact Newton prefix, and cap-three completion are
  inherited and rederived at the needed scope in PROOF.md.
- ATC29 at `47a1df32adb48a3a58faa58576fff72ff84d9c4f` was observed in the
  live #904 description. Its activation and native semiprime results received
  body-level reconnaissance only. They are not premises of the new estimates.
- Concurrent ACC29/SFC30, #905 at
  `dfd20b6a778941a3d0c5f671ba840a6b35e4d36e`, likewise received live body-level
  reconnaissance only. Its squarefree completion and sparse cofactor-graph
  estimates are not imported or claimed rediscovered here. MCB31 instead
  retains PCR26's cap-three completion and estimates a dense frequency band.
- AGENTS.md at the reading parent was read. No original manuscript, trusted
  formal source, workflow, main ref or canonical status is changed.

## Arithmetic implementation lineage

`exact.py` is an explicitly credited excerpt of NCL29's `check.py`, retaining
its 144-bit outward integer interval routines and elementary factorization,
Mobius and trigonometric helpers. The module header and imports are adapted
for this standalone packet. It is NOT an independent interval implementation.
The new `check.py` and tests reuse it. Same-author arithmetic agreement and
normal/optimized executions do not constitute external mathematical review.

New source checks use distinct formulas: product convolution versus the gcd
threshold, reduced fractions versus unreduced product fractions, and complete
Newton coefficient reconstruction versus a direct finite Mobius sieve. These
are useful implementation cross-checks, not independent analytic refereeing.

## Classical tools and literature boundary

Dirichlet inversion, short-source Newton identities, finite summation by
parts, Abel summation, finite sine sums, smooth quintic cutoff functions,
Cauchy-Schwarz, Riemann-sum convergence and bounded-overlap accounting are
classical. Their use is not claimed as a discovery.

Relevant primary reference: M. N. Huxley and N. Watt, *Mertens Sums requiring
Fewer Values of the Mobius function*, arXiv:1807.05890 (2018),
https://arxiv.org/abs/1807.05890 . Its public abstract/metadata were checked in
this pass for the classical short-source attribution; no new full-paper audit
or imported deep exponential-sum theorem is claimed.

NCL29 supplies the precise earlier far-sector bound used in Sections 4-5.
The microscopic mixed-derivative estimate and the generic sharpness family
are proved directly here. No theorem about quadratic-character large sieves,
random Mobius signs, zeta-zero statistics or short intervals is imported.
External novelty of this packet-specific composition is NOT established.
