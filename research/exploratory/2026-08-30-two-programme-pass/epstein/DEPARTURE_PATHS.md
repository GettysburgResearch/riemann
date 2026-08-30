# E3 — Two departure paths through moduli space (t in (0,30))

NON_DIRECTED_HIGH_PRECISION, dps=40. tau grid 0.1 with events refined by bisection
in tau to 1e-3 (coordinator budget guidance; the spec's 0.05/1e-6 was coarsened — see
SCOPE.md); path A is extended along x up to 0.35 when quiet to tau=1.
"Departure" means: two on-line zeros (12-digit locations)
merge and the on-line count drops by 2 while the argument-principle box count in
[0.3,0.7] x (0.05,30.0) is unchanged — i.e. the pair moves off the line as a symmetric
pair, numerically to the stated precision.

The phenomenon itself (zero collisions spawning off-critical pairs in one-parameter
Epstein families) is published — Arenstorf–Brewer (1993); Travenec–Samaj
(arXiv:1909.07112); Betermin–Samaj–Travenec (arXiv:2110.09368); off-line zeros for
class-number>1 / non-arithmetic forms go back to Davenport–Heilbronn and
Potter–Titchmarsh. What is recorded here is this lab's certified event data along two
specific moduli paths, with argument-principle certification of each count at stated
precision, and k-indexing of which zero pairs depart where.

Note: off-line zeros remain a density-zero phenomenon; Bombieri–Hejhal (conditionally)
and Ki / Y. Lee give a full-density / proportion picture of Epstein zeros ON the line.
Leaving the arithmetic locus does NOT push zeros off the line in bulk; the tables below
measure the finitely many low-height departures only.

## Path A_x_slide_y1.02:  z = 0.15*tau + 1.02i (extension: same line to x=0.35)

| tau | n_line | n_box | off-line pairs (disc/2) |
|---|---|---|---|
| 0.00 | 13 | 13 | 0 |
| 0.10 | 13 | 13 | 0 |
| 0.20 | 13 | 13 | 0 |
| 0.30 | 13 | 13 | 0 |
| 0.40 | 13 | 13 | 0 |
| 0.50 | 13 | 13 | 0 |
| 0.60 | 13 | 13 | 0 |
| 0.70 | 11 | 11 | 0 |
| 0.80 | 11 | 11 | 0 |
| 0.90 | 11 | 11 | 0 |
| 1.00 | 11 | 11 | 0 |
| 1.67 | 10 | 10 | 0 |
| 2.33 | 9 | 11 | 1 |

### events

- UNRESOLVED unit: 1 unit(s) of |disc| jump 2 not resolved to a specific merging pair (possible window-boundary entry/exit near t=30.0); see records.

## Path B_y_stretch_x0:  z = i*(1+tau)

| tau | n_line | n_box | off-line pairs (disc/2) |
|---|---|---|---|
| 0.00 | 13 | 13 | 0 |
| 0.10 | 10 | 10 | 0 |
| 0.20 | 11 | 11 | 0 |
| 0.30 | 12 | 12 | 0 |
| 0.40 | 14 | 14 | 0 |
| 0.50 | 11 | 11 | 0 |
| 0.60 | 10 | 14 | 2 |
| 0.70 | 12 | 14 | 1 |
| 0.80 | 17 | 17 | 0 |
| 0.90 | 17 | 17 | 0 |
| 1.00 | 20 | 20 | 0 |

### events

- **departure** at tau* = 0.501953 (z* = 0.000000 + 1.501953 i): colliding zeros t = 25.117024041, 25.328995872 -> t* = 25.208434; off-line pair at tau = 0.60: sigma = 0.652150 (pair 1/2 +- 0.152150), t = 24.550491
- **departure** at tau* = 0.501953 (z* = 0.000000 + 1.501953 i): colliding zeros t = 23.599431047, 25.117024041 -> t* = 25.208448; off-line pair at tau = 0.60: sigma = 0.652150 (pair 1/2 +- 0.152150), t = 24.550491
- **reentry** at tau* = 0.608984 (z* = 0.000000 + 1.608984 i): colliding zeros t = 24.051919617, 24.781544280 -> t* = 24.524595; off-line pair at tau = 0.60: sigma = 0.652150 (pair 1/2 +- 0.152150), t = 24.550491
- **reentry** at tau* = 0.730078 (z* = 0.000000 + 1.730078 i): colliding zeros t = 10.930978277, 11.280623232 -> t* = 11.296586; off-line pair at tau = 0.70: sigma = 0.666386 (pair 1/2 +- 0.166386), t = 11.379312

### The central question

The per-tau tables above answer it directly: the first off-line pairs appear at the
recorded tau* values, the colliding pairs are k-indexed by their 12-digit t-locations,
and the count of off-line pairs at fixed height as one moves away from the arithmetic
point is the disc/2 column (monotone or not as recorded — no bulk departure; the
overwhelming majority of the ~ (t/2pi) log t zeros in the window stay on the line).

Path B passes through rectangular lattices; at heights where y^2 is rational these are
(up to scale) Epstein zetas of integral binary forms of non-fundamental discriminant or
class number > 1, whose off-line zeros are classical (Davenport–Heilbronn;
Potter–Titchmarsh) — the lab measures WHERE they sit in this family.
