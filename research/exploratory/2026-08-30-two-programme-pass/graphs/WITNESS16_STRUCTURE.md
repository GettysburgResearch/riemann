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

## Open

Whether idx 706 (the third n=16 positive-only spectrum, barely
untempered, adjacency re-derivable from the census enumeration) is a
member or a 2-switch neighbor of these families; whether P/Q-type
windows exist for other cap choices; and a proof of the GP(n,2)
permanence (λ_2 monotonicity in n along the family).
```
