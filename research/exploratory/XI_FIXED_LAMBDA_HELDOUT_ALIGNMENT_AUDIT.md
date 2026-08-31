# Independent review: held-out fixed-lambda Xi alignment

Verdict: **PASS**, with the finite/conditional/cofinal boundaries below.
Science: `64165b8c805d182dbc43f2e5855e64a86cf1aaf9`.
Independent review protocol frozen BEFORE its numerical runs at
`57d26725a5783a6715124eb82dd9cc8c516eca03`.

The reviewer read the entire theorem note, producer, 44-test module and
manifest. All five scientific files remain unchanged. Review arithmetic
is in a separate worktree, and no author module is imported or executed
by the resident independent evaluator.

## 1. What was independently reproduced

The evaluator authenticates the scientific fixture, four artifact hashes,
canonical payload, 24 recursively reached historical source files, and all
44 native FLINT binaries and runtime versions. It reuses only the reviewer's
own previously frozen independent evaluator, with its exact Git blob checked:

- review commit `26201b3a7de6293ea47621f06b45dd9837521a20`;
- `xi_fixed_lambda_joint_independent_review.py`;
- Git blob `35f8baf0486625490f3fb9afe998956f75fe5280`.

This route evaluates reflected xi using exponential log-Gamma, takes its
series in a unit s-variable, and applies the i^j chain rule afterward.
The author uses the direct Gamma product and z-variable series. Both routes
still trust the SAME FLINT special-function implementation; this is not a
second-library or formal-verification claim.

The independently preregistered complete boundary panel passed unchanged:

| box center | precision | complete arcs | Taylor terms | root count |
| ---: | ---: | ---: | ---: | ---: |
| 256 | 384 bits | 832 | 36 | 8 |
| 512 | 384 bits | 832 | 36 | 9 |
| 1024 | 1152 bits | 3328 | 52 | 9 |

All original box edges were retained. The successful author subdivisions
were halved in length, yielding 4992 independently enclosed arcs. Every
convex image hull excludes zero and includes its polygon endpoints. The
independent polygon winding algorithm counts quadrant changes, not the
author's ray crossings, and reversal gives the negative winding. Each
refined image overlaps the corresponding author enclosure. The report
stores the ordered convex-hull stream hashes, not a second large fixture.

At 384 bits in normal Python and 512 bits in optimized Python, the evaluator
also reproduced:

- all 40 simple R5 root-disc proofs with the full 2^-120 radii;
- all six noncommon guards on each full root rectangle;
- 1080 point/rectangle/reflected-rectangle derivative overlaps per run;
- all 1600 normalized Hardy Gram entries, including every old/new cross term;
- every node's actual raw-value weighted alignment, all four nested prefixes,
  all four strict finite Bessel ceilings, and all positive increment floors.

The ONE parameter lambda64 is independently reconstructed by differentiating
the paired log-Gamma phase; its interval overlaps the authenticated frozen
FC lambda. The earlier fourteen-node boundary census is inherited from the
exact prior independent FC review, while all fourteen nodes themselves are
rebuilt here alongside the twenty-six new nodes.

The first new raw modulus is rigorously below 0.054. Thus the earlier
fourteen-node lower pattern >1/4 does NOT survive this held-out extension.
No alternative window, parameter, or favorable subset was substituted.

## 2. Analytic and coverage audit

For a boundary arc of half-length h, the scalar Xi enclosure on the outer
radius-1/4 square pays the radius-1/8 derivative Cauchy bound. Consequently
the F=Xi^(5)-i lambda Xi^(6) coefficient tail is bounded by

    M_Xi (5! 8^5 + lambda 6! 8^6) (8h)^N / (1-8h).

This exact geometric tail and the full convex polygon homotopy justify the
argument principle, not endpoint samples alone. The author retains the two
failed 1024-box tiers before the successful tier. Their failure is an
insufficient zero-exclusion enclosure, NOT a certified boundary zero.

Each root-disc inequality

    (A+M2 r^2/2) 2^50 < D r

is a strict directed-ball/Rational Rouché certificate. The disjoint discs
lie wholly inside their boxes, and their counts equal the independent
boundary counts. Hence they exhaust all zeros of R5 in those boxes, with
multiplicity paid. The zeros counted are companion R5 zeros, not a census
of the nontrivial zeros of Xi itself. All scouting outcomes are retained,
but the independent proof does not use the Newton scouts as coverage.

The normalized Gram convention is correctly

    G_ij=2 sqrt(y_i y_j)/(y_i+y_j+i(x_j-x_i)), G_ii=1.

The maximum absolute row sum bounds its norm. All finite ceilings are strict
upward rational roundings; full-square raw values enter |Theta0(b)|^2 y/x.
Neither this weighted sum nor its increment is asserted to be a physical
trace. The weights do not replace the physical Hardy metric.

## 3. Critical-jet transport lemma HA3

I independently rederived the source-exact Taylor estimate with g=f^(5),
g'(t)=0, a=g(t), c=g''(t), ac<0 and q=-a/(lambda c)>0.
On |w|<=2q the error relative to L=a-i lambda c w is bounded by

    2|c|q^2+M3(4q^3/3+2lambda q^2)=Delta |a|.

On |w-iq|=2Delta q the linear modulus is 2Delta|a|. Since Delta>0
and Delta<1/2, the circle lies inside the assumed Taylor disk and strictly
in the upper half-plane. Rouché gives one simple root. The same estimate
makes g nonzero on the whole disk; at an R5 zero, C5=2g is nonzero.

The optional ratio hypothesis |f/(lambda f')|<=eta<1 correctly gives
nonvanishing of R0,C0 and the raw modulus floor (1-eta)/(1+eta).
The stated height and horizontal-offset asymptotics are conditional
consequences of the explicit derivative hypotheses, not assertions that
those hypotheses have been established for Xi. The density-to-divergence
corollary follows by partial summation of 1/(t log^2 t). Its pairwise
disjointness and eventual density hypotheses are indispensable.

Even those hypothetical conclusions do not pay the uniform Bessel premise
of the older LB3 criterion. The later independently reviewed occupancy
packet may replace that premise by a crowding-weighted criterion, but no
such cofinal crowding/alignment theorem is being imported into HA silently.

## 4. Replay evidence and limitations

The scientific fixture LF SHA256 is
`eb6464cc2eed61f8aecf2eff6e2f36a5ee5f850252237f0f95bd9b0e4e51b206`;
payload `1822457a5144ae0753d529be83884e42298191e85b32c646cc364cd2687ef570`.
The independent boundary, 384-bit and 512-bit reports are resident beside
this note. They bind the same final reviewer script hash.

Separately delegated immutable detached-source replays completed all 44
tests in normal Python (929.329s) and optimized Python (937.860s), both
producer checks (453.656s / 457.281s), and four exact LF fixture/manifest
emits. Those runs are source-producer replays, not independent algorithms.
Their strict source, type/cap, resealed-erasure and primitive-zero-jet
attacks were inspected in the complete test module. Ruff and full-base
whitespace checks passed; the frozen science was not modified.

One reviewer plumbing correction preceded the numerical acceptance runs:
the HA top-level fixture does not repeat lambda_enclosure, so that reference
was corrected to the already authenticated historical FC fixture. No
scientific value, boundary, precision panel, or acceptance threshold changed.

No uniform infinite Bessel bound, cofinal alignment divergence, global
component-innerness theorem, physical Hilbert--Schmidt infinity, outer-metric
identification, or RH result follows from this finite packet. The fixed-width
dyadic-window survey is explicitly not a cofinal census.
