# Exact-commit assembly review: proposed R=4.72 region

Reviewed23 October2026 at commit
`4ac216d015778604c030494ce9f998283dda6dc9`, directory
`standalone/2026-10-23-shifted-logistic-region` in the publication checkout.
The reviewed files were read directly from Git objects. I also created a
separate Git archive and authenticated all87 manifest components among
its93 files. No reviewed file was changed.

Manifest SHA256:
`ec9e6b9a54e583a77e4a18a131930b2fe0d6a4412b2c777cc1a87d81fb336b6a`.
Assembled PROOF.md SHA256:
`eb935cfc115a3ed6df5d8e3e4c494d60d55c10347e5a641303819806edc7f291`.
The accompanying `ASSEMBLY_472_INTEGRITY.json` records the other top-level
hashes and the archive check.

## Authorship and review scope

I authored the new shifted Ford component and earlier global wrappers,
and co-developed its main mechanism with the root. My review of those
parts is an author/coauthor consistency check, not an independent proof
review. The separate type-agent report in this exact packet binds the
same shifted-component hash and independently audits its interfaces.
My inspection of the assembled low/high composition, root Euler tail,
manifest, and launcher is separate from their authorship. No human or
external peer review is claimed.

## Findings

No new assembly-interface gap was found in the stated source-dependent
claim. In particular:

- The two detectors use the same minimizing zero B, not two unrelated
  zero-free parameters. The Littlewood input confines any violating
  zero to a finite height range; outside it B>=Astar. Thus one violating
  zero with B<Astar makes the global minimum occur among finitely many
  zeros. The finite verification excludes the prefix, and nonvanishing
  on Re s=1 makes the selected B positive.
- The lower rectangle is correctly enlarged in A while its lower
  log-height becomes28.7. This preserves eta<.0075, sigma>.99, the
  previous cutoff-correction envelope A/l^2<.21/28^2, and every fixed
  error budget. The separate frequency cutoffs and separate alpha_0,
  alpha_1 in the transform correction are retained.
- The lower certificate and higher endpoint both include52. Their
  strict positive margins contradict the necessary inequalities on
  the two complementary height ranges. The high proof retains the
  full shifted Revers envelope, so it does not misuse the simplified
  envelope whose domain began at log-height60.
- The .55 real-center gain, .255 high prime gain, .31 low signed
  archimedean gain, and1.26 low prime gain are used in their respective
  detector normalizations. They are not added twice or transported
  across kernels without their stated factors.
- The Euler upper bounds have the correct omitted-tail exponents and
  denominators. Their source hashes, and the independent review hashes,
  match the archived manifest. The ordinary/optimized launcher runs
  explicit reconstruction checkers rather than accepting stored JSON.
- README, SOURCES and PROOF distinguish this classical-form result
  from a smaller fixed half-plane boundary and from RH. Revers remains
  an identified preprint input. No priority or external-certification
  claim is inferred from the exact arithmetic.

## What was and was not run

The exact Git-archive integrity audit passed all87 component hashes.
I read the ten-checker launcher and verified that its listed scripts
are authenticated components and execute in an isolated temporary copy.
I previously ran the new shifted endpoint normally and with `-O`, with
byte-identical JSON, and independently read the Euler reconstruction.
At the root's request I did not duplicate the entire ten-checker replay
in this assembly review; the root is running that separate replay.

The imported finite RH computation, published Littlewood region,
corrected Ford identity, and Revers estimate were not reproved by this
audit. The finite arithmetic is not a global formal certificate. The
remaining status is a source-dependent research theorem candidate with
internal reviews, awaiting the repository's integration and external
mathematical scrutiny. The reviewed bytes may be used for that review;
this receipt does not authorize a different later mathematical head.
