# T97910 factor-67 product-boundary publication provenance

## Exact lineage

The source packet named PR #590 at scientific head
`223f11259b3e7134f78d6492795e6e94caca8be3`. Publication instead branches from
the then-current PR #590 head
`4f1283c67f0d4a4b504badd4c4113ba227521162` so the repository retains its
complete archival lineage.

The intervening commits are archival-only:

```text
395485cea8381cc431ee54d8c588af63de356d57  add repository archival PDF for T97700
4f1283c67f0d4a4b504badd4c4113ba227521162  add one-shot T97700 PDF publisher
```

The scientific input remains frozen at `223f11259...`; neither intervening
commit changes a scientific claim, experiment, result, or proof object.

## Route split and collision-only re-identification

The supplied deterministic archive contains two independent routes. This PR
publishes only its seven-file factor-67 route. The Q4 route belongs on the PR
#580 lineage and is intentionally absent here.

The live repository already uses `T-97900` and related `97900` identifiers.
Therefore this route is re-identified mechanically and consistently:

```text
L-97900 -> L-97910
L-97901 -> L-97911
L-97902 -> L-97912
T-97900 -> T-97910
X-97900 -> X-97910
```

Paths, internal references, equation tags, schema, verdict, retained result,
and proof-object hash follow the new IDs. The verifier's retained JSON write is
also pinned to UTF-8 with LF newlines so replay is byte-stable on Windows and
POSIX. These are publication-only changes; the mathematical prose is otherwise
unchanged.

## Relationship to adjacent routes

PR #596 and PR #598 are alternative open localizations of the factor-67
boundary. They neither establish `ESBLP67` nor `AFPBR67`. Conversely, the two
localizations in T-97910 do not establish their open `CPSL67`/`NCBI67`
conditions. All are compatible with, and do not revive, the prior refutation of
`LAPBR67`.

## Scientific status

```text
complete near-critical small-prime cube       PROVED IN CLAIM PROSE
expanded terminal largest-prime strip         PROVED IN CLAIM PROSE
positive Euler-main localization              PROVED IN CLAIM PROSE
ESBLP67                                       OPEN / RH-BEARING
AFPBR67                                       OPEN / RH-BEARING
LAPBR67                                       REFUTED; NOT REVIVED
Riemann Hypothesis                            UNPROVED
```

The finite replay checks algebraic identities and sanity models. It does not
machine-prove the PNT/Mertens asymptotics, either remaining gate, or RH.
