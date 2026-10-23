# Additional source identity correction

23 October 2026. Additive provenance correction to mathematical assembly
`738e19e0a6a3dd41498b0419e70d9c96f8d988e3`.

The exact Git blob `LABEL_UNIFORM_MOBIUS_RESIDUES.md` in that assembly has
SHA256

    12c765c1fdccec8ebb087b7608b80bb7b2d30114bf664ac1e43a2966b9d8f89d

as correctly recorded in `COMPONENT_MANIFEST.json`. Several frozen prose
references accidentally insert one extra `c` after `12c765c1fdcc`, producing
a 65-character string. This affects references in the primitive continuation,
short-label note, label review, and the earlier source-pin erratum. In all
such references the file name, source bytes, and intended reviewed argument
are the same. The 64-character value above is the corrected identity.

This correction is separate from `SOURCE_PIN_ERRATUM.md`, which corrects
the imported full scalar remainder hash and clarifies the projection notation.
Both corrections apply. No analytic statement or previously frozen source
file is changed. The independent assembly reviewer reproduced this hash
directly from the exact Git archive and compared all manifest components.
