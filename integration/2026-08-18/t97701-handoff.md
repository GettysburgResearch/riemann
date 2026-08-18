# T-97701 handoff

This packet corrects a publication failure in the PR #590 conversation.  The
announced C4MBI67 materials were not present at the live PR head or in the old
T-97700 archive.

```text
frozen base PR:        #590
frozen base head:      4f1283c67f0d4a4b504badd4c4113ba227521162
new branch:            research/gpt56-pro/97701-c4mbi67-publication-recovery
old ZIP digest:        bf79073d4dbc482a1ff634a06ec4cd8d2f5a6ff3181c209fca86aec96b3ff640
old ZIP disposition:   superseded; not reused as the publication artifact
```

The exact new frontier is

```text
BLPTE67(X) <=> C4MBI67(X) <=> annular scalar A_X>=0.
```

The equivalence, four-band identity and prime-Möbius ownership are proved.  The
C4MBI67 sign and RH remain open.

## Final artifact freeze

```text
ZIP:  riemann-t97701-c4mbi67-publication-recovery-final-20260818.zip
PDF:  t97701-c4mbi67-critical-core-final-20260818.pdf
PDF SHA: 0825f3949f4100c78d1723e2a5c81c6ba451ee65243801cca9d0ea598d6ad21d
TeX:  t97701-c4mbi67-critical-core-final-20260818.tex
TeX SHA: aae5191bf9c07a1526d1570e8d722bfd9596555775b84bd6c0fe52d2687830ed
```

The non-self-referential ZIP checksum is stored only in the external outer
artifact ledger. The final Git tree must have no `.publish/` subtree, no
temporary publication workflow, and no placeholder PDF.
