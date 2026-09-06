# Sources, classical tools and external-reading boundary

## Pinned primary source code and repository mathematics

`SOURCES.tsv` is the controlling list of exact inspected commits, paths, blobs and
ranges. GitHub connector responses at those refs supplied the text. The packet
does not contain a local full checkout or claim an original-producer replay.
The optional `checks/verify_source_checkout.py` can compare these identities
against a local authenticated checkout; it does not prove the source mathematics.

Mathlib at `51e6992efd06126df61a496bebf8f49482a4e129`,
`Mathlib/NumberTheory/LSeries/RiemannZeta.lean`, lines 1-145, provides the
completed entire function, the exact meromorphic identity, differentiability
and reflection. Its *declaration body* controls over the inconsistent overview
comment. No current-master definition is substituted for this source.

The local Zeta23 bridge imports its actual seam, multiplicity, reflection and
Weil theorems and explicitly receives GammaFacts for RvM. Those transitive
upstream proofs were not all read or built. No claim is made to have eliminated
all external inputs merely because local code contains no explicit custom axiom.

## Classical analytic ingredients

The new arguments use the identity theorem, Taylor expansion, dominated and
monotone convergence, Tonelli, local analytic factorization, Hadamard factorization,
Plancherel, Dirichlet sine expansion, Riesz representation and compact spectral
theory at the scopes explicitly stated in the proof notes. These are classical
tools, not new results attributed to this repository. Landau's particular
positive-transform argument is reconstructed in full rather than cited as an
unexamined black box.

Primary reference checks during this pass:

- NIST Digital Library of Mathematical Functions, §1.10 (analytic continuation,
  Taylor expansions and entire-function products): https://dlmf.nist.gov/1.10
- DLMF §25.4 (xi and zeta reflection conventions): https://dlmf.nist.gov/25.4
- DLMF §5.5, especially 5.5.4 and 5.5.8 (digamma reflection and duplication):
  https://dlmf.nist.gov/5.5
- DLMF §5.7 (digamma partial-fraction series): https://dlmf.nist.gov/5.7

These reference checks support the named standard identities, not the
repository-specific conclusions. No original research-paper PDF, zero-verification
payload, historical large numerical certificate or upstream kernel build was
newly authenticated in C4. No external novelty or current-record claim is made.
