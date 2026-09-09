# The minimal positive-end-only cubic graphs, decoded

```text
Status: every "exact" statement below was computed in integer/rational
        arithmetic AND independently recomputed by an adversarial
        verification wave (21 verifier agents, one per exact claim:
        20 confirmed, 1 "ambiguous" solely over the family NAMES,
        with the members themselves exactly re-certified); float
        statements are labelled. Workflow transcript: session
        workflows run wf_05c1d915-38d.
Inputs: graphs/witness16.json (adjacency + exact charpolys of the two
        primary n=16 witnesses, census16 idx 708/709).
RH status: unproved; unaddressed. rh_established: false.
```

## What the two witnesses are (exact)

Both are the Hamiltonian cycle `0-1-...-15-0` plus 8 chords, and both
decompose as a **capped ladder**: a diamond (K4 minus an edge) on
`{0,1,2,3}`, a two-rail corridor with nested rungs, and a far cap.

- **Witness 709** = diamond + rungs `(4,15),(5,14),(6,13),(7,12)` +
  a SECOND diamond on `{8,9,10,11}`: the symmetric
  diamond-ladder-diamond chain. 4 triangles (two disjoint
  shared-edge pairs), `|Aut| = 16` (including an end-swap
  automorphism), and a strikingly clean spectrum
  (float-labelled: contains `0, ±1 (triple), √3−1, −2, −(1+√3)`;
  `λ_min = −(1+√3)`, `λ_2 ≈ 2.8422`).
- **Witness 708** = the same diamond + 3-rung ladder, but the far cap
  is an asymmetric 6-vertex block with a single triangle `(9,10,11)`:
  3 triangles, `|Aut| = 4` (Klein four), `λ_2 ≈ 2.8312` — a breach
  margin over `2√2` of only `2.8e-3` (float-labelled; the breach
  itself is Sturm-certified exact).
- The two graphs differ by a SINGLE 2-switch of chords
  (`{7-10, 8-12}` vs `{7-12, 8-10}`), are non-isomorphic (distinct
  exact charpolys), and are non-cospectral.

## Why every earlier search missed them (exact)

Both have minimum edge cut 2 — but realized by FOUR (708) / FIVE
(709) PARALLEL 2-edge cross-sections of the ladder corridor, not by a
single neck between two dense clusters. The 774-dumbbell search
scanned exactly the single-neck shape; the witnesses' bottleneck is a
CORRIDOR. The λ_2 eigenvector localizes as a two-cluster sign pattern
across the corridor (float-labelled), i.e. the expansion failure is
the corridor's, while the diamond caps keep λ_min shallow.

## The capped-ladder families and the transitional window (exact)

Parametrize (names local to this note; "P/Q" have no prior meaning in
the repo): `P(k)` = diamond + k-rung ladder + diamond (n = 2k+8;
witness 709 = P(4)); `Q(k)` = diamond + k-rung ladder + the 6-vertex
one-triangle cap (n = 2k+10; witness 708 = Q(3)). Exact Sturm
certification of members (same cut-and-guard method as the census):

```text
P(3), Q(2)   (n = 14): RAMANUJAN            (consistent with census14)
P(4), Q(3)   (n = 16): positive-end-only    (the witnesses)
P(5), Q(4)   (n = 18): positive-end-only    (two non-isomorphic n=18
                                             examples, exact charpolys
                                             in the workflow record)
Q(5)         (n = 20): positive-end-only
P(6), P(7), Q(6) (n = 20, 22, 22): BOTH-END (2 untempered squares)
```

**The reading:** in these families the positive-end-only property is a
FINITE TRANSITIONAL WINDOW. As the corridor lengthens, λ_2 crosses
2√2 first (n = 16), and the corridor's near-bipartiteness drives
λ_min below −2√2 a few steps later (n = 20-22), after which the
breach is two-sided. Contrast GP(n, 2) (gp24_certificate.json), whose
block structure bounds λ_min ≥ −√5 for ALL n: there the positive-only
property, once entered at n = 24, appears permanent. Two DIFFERENT
mechanisms produce positive-end-only graphs: a transient window in
near-bipartite corridor families, and a permanent regime in
λ_min-bounded families. The negative-end law at small order
(O-108006) now has its precise boundary story: at n ≤ 14 only the
near-bipartite direction can break; at n = 16 the corridor mechanism
opens the expansion direction, three spectra thread the window; by
n = 20-22 the same corridors break both ends at once.

## Completion: idx 706 decoded — the classification closes (exact)

The third positive-only spectrum's representative (from the census
reps cache) is the identity 16-cycle plus chords
`(0,2),(1,3),(4,15),(5,14),(6,13),(7,9),(8,11),(10,12)`: the SAME
diamond head `{0,1,2,3}` and the SAME 3-rung corridor as 708/709, with
a THIRD cap variant — two triangles `(7,8,9)` and `(10,11,12)` joined
through the chord `(8,11)` (a two-triangle chain; 4 triangles total,
min cut again 2 via parallel corridor cross-sections; chord distance 3
from each of 708/709, so not a single 2-switch of either).

**Classification (exact, by the exhaustive census):** the three
minimal positive-end-only cubic spectra at n = 16 are precisely the
three DIAMOND-HEADED 3-RUNG CAPPED LADDERS, one per cap variant:

```text
idx 709: cap = diamond            (second K4-minus-edge)
idx 708: cap = one-triangle block
idx 706: cap = two-triangle chain (barely untempered: square within
                                   0.0089 of the threshold 8)
```

One family shape, three caps — the expansion-side breach at minimal
order has exactly one mechanism. (Counts are of SPECTRA: cospectral
mates would merge; each decoded representative is as stated.)

## The complete cap-window table (exact; graphs/cap_windows.json)

The deposited question — do windows exist for other caps? — is now
answered exhaustively: of the 15 chord-matchings on the far 6
positions, 5 are simple-graph-valid, and 4 are distinct up to the
corridor mirror (cap `(0,4),(1,3),(2,5)` is the mirror of 708's cap).
Verdict sequences over corridor length k = 2..7 (n = 2k+10; exact
Sturm; the two GUARD cells are the census's adaptively-resolved
n = 16 spectra):

```text
cap (0,3),(1,5),(2,4)  [708]:  RAM  POS  POS  POS  BOTH BOTH
cap (0,5),(1,3),(2,4)  [709]:  RAM  POS  POS  BOTH BOTH BOTH
cap (0,2),(1,4),(3,5)  [706]:  RAM  POS* POS  POS  BOTH BOTH
                               (*guard cell = idx 706, resolved POS
                                by the adaptive cut, barely)
cap (0,3),(1,4),(2,5) [cross]: NEG  BOTH* BOTH BOTH BOTH BOTH
                               (*guard cell = the census's unique
                                both-end spectrum idx 707)
```

So: EXACTLY the three witness caps have positive-only windows (of
lengths 3, 2, 3 with different offsets), the crossing cap never does
(it enters at the NEGATIVE end at k = 2 — the only diamond-headed
frame member to do so — and goes two-sided immediately after), and
every cap ends BOTH-END as the corridor lengthens. The n = 16 census
rows (3 positive-only + 1 both-end among diamond-headed frames) are
exactly the k = 3 column of this table. The window phenomenon is
therefore CAP-SELECTIVE: the cap decides whether the expansion end
opens before the bipartite end catches up.

## Open — both questions now ANSWERED

Non-diamond heads: the diamond is the ONLY valid 4-vertex head
(parallel-chord exclusion), and the 6-vertex-head atlas
(head_cap_atlas.py + json; O-108517 addendum) shows windows occur for
EXACTLY the window-type x window-type block pairs — including with no
diamond present — while the crossing block at either end kills the
window; the three minimal witnesses re-decompose as 6/6 ladders with
the s709 block common to all three. GP(n,2) permanence — PROVED as
T-108514 (standalone/2026-08-31-gp-positive-family/). Window
finiteness in EVERY capped-ladder family — PROVED as L-108520
(induced 2x15 ladder forces both-end; integer pivot 50 > 49).
```
