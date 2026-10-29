# Audit of the long-source adapter and seed

**Status:** Source and algebra review, not a Lean proof and not a proof of the missing seed. The relevant pinned source files are identified in [the proposal](README.md). No independent verification of their imported analytic dependencies was performed.

In `UniformSlotAmplification.lean`, `uniform_slot_crossing` explicitly assumes `0<=delta<=1`, with the mesh chosen before the finite slot dictionary. The stronger `delta>=1/2` premise appears in the later `squarefree_family_long_to_all` interface and in the reflection/contraction machinery, rather than in the crossing theorem itself. For an assumed long bound `N<=K Z^epsilon (L+B^sigma L^(1-sigma))`, with `0<sigma<=1`, the proposed choice `target=log(B/L)/log Z` for `L<B` yields `B<=Y<=B Z^(mesh+loss)`. Applying the assumption at `Y` and crossing yields the proposed all-source exponent `B^(1-sigma)L^sigma`, with the stated fixed-power and small-loss bookkeeping. The `L>=B` case uses the seed directly. I found no algebraic need for `sigma>=1/2` in this adapter; it remains an uncompiled conditional extension of the source interface.

The seed's actual norm requirement is easier to see than its two-term expression: for **every** `0<sigma<=1` and `L>=B`,

```text
L <= L+B^sigma L^(1-sigma) <= 2L.
```

Thus the seed asks for a nearly linear `O(Z^epsilon L)` operator norm throughout `B<=L<=B^2`. The slope only changes the selection hypothesis; it does not change the requested long-range size. At balance `L=B`, the generic sextic large sieve permits `B^(7/6+epsilon)`, and the desired selection must remove its `B^(1/6)` excess. The unsimplified long-range contribution `L^(5/6)B^(1/3)` exceeds `L` until `L=B^2`; an arbitrary-vector large-sieve estimate alone therefore does not prove the seed.

The proposed small-slope counterexample agrees with the pinned `SelectedSlotData` definitions, which allow finite sets of arbitrary nonzero ideals in each slot and impose an ℓ² coefficient-mass bound, not a prime-only requirement. Pick fixed `w>0` below the early mesh and choose sixth-power slot ideals `J^6` of norm at most `Z^w`; normalized equal weights give squared slot amplitude equal to a fixed positive constant times their number, of order `Z^(w/6)`. At `sigma=1/6`, take the fixed permitted coefficient mass large enough to absorb the density constant. Squarefree row prime ideals of norm in `[B,2B]`, restricted to a common primary residue class modulo 36 by pigeonhole, have cardinality `>>B/log B`. For `B=Z`, source ideals `K^6` with `N K<=B^(1/6)` contribute `>>B^(1/6)` columns; both sets of roots are too short to share a prime with any chosen row. Every matrix entry is one, so the squared operator norm is `>>B^(7/6)/log B`. This contradicts the seed for every `0<sigma<=1/6` after choosing the arbitrary power loss below `1/6`. The width floor and mass must be fixed before letting `Z` tend to infinity; the construction can choose them after the early mesh, as permitted by the interface.

This counterexample uses composite sixth-power **slot** ideals and cannot be transferred to literal prime slots. The unrestricted squared norm lower bound in [Xu–Sang, Theorem 1.1](https://arxiv.org/abs/2610.17675v2) likewise does not prove that its extremizing rows pass the stipulated prime-slot selection. Their [Theorem 1.2](https://arxiv.org/abs/2610.17675v2) concerns a fixed smooth unnormalized prime sum, and does not give the selected operator bound uniformly in all allowed prime-slot data. Their lower-bound branch uses the cited OpenAI zero-slot moment; their structured prime branch also imports the unmarked inverse moment and detector. Neither preprint was independently verified in this audit. No matching proof or counterexample for the literal-prime-slot seed at `sigma=223/500` was located in the targeted literature search.

## A count consequence for genuine prime slots

At balance `B=Z`, a separate conditional calculation controls the **number** of selected rows, though it does not yield the selected operator norm. Suppose one literal slot has width `w>0`, prime-ideal support in a fixed annulus of norm `P=Z^w`, and row-independent coefficients `|a_p|<=C P^(-1/2)`. Let `k>=1` be fixed with `k w<=1/2`. Subject to de Faveri's stated sixth-power-free large sieve, the kth-power expansion and sixth-power removal give

```text
sum_(N u<=Z, squarefree u) |sum_p a_p chi_p(u)|^(2k) << Z^(1+epsilon).   (A2)
```

To see the needed column bound, write the expansion as `sum_c b_c chi_c(u)`. The fixed-order divisor bound gives `|b_c|<<Z^epsilon P^(-k/2)` and `Nc<<P^k`. Split `c=v^6 c0` with `c0` sixth-power-free. For each fixed `v`, ideal counting shows `sum_c0 |b_(v^6 c0)|^2 << Z^epsilon/(Nv)^6`. The sixth-power symbol contributes only a mask `(u,v)=1`; drop that row restriction when applying de Faveri to `c0`. Since `P^k<=Z^(1/2)`, each resulting row norm is at most `Z^(1/2+epsilon)/(Nv)^3`. Minkowski and convergence of `sum_v (Nv)^(-3)` prove (A2), up to rechoosing the arbitrary power loss. All constants may depend on fixed `k`, `w`, the annulus and the field.

If this slot satisfies `|sum_p a_p chi_p(u)|^2>=Z^(sigma w)` on every row of `F`, (A2) gives

```text
|F| << Z^(1-k sigma w+epsilon).                                  (A3)
```

For `k=floor(1/(2w))`, `k w>1/2-w`; at `sigma=223/500` and sufficiently small fixed `w`, this produces a saving greater than `1/6`. Under a positive total-width floor and finitely many slots, one may also obtain an individual slot with slope arbitrarily close to the aggregate slope and width bounded below by a positive constant depending on the number of slots, width floor and allowed slope loss. Indeed the pointwise coefficient bound gives each slot energy at most its width plus `O(1/log Z)`, so slots below a sufficiently small fixed width contribute only a small fraction of the total energy; a zero-width slot contributes `O(1/log Z)`. The lower width bound keeps `k` in a finite range when the slot widths vary, so the fixed-`k` constants may be maximized over that range. Pointwise annular normalization remains an additional assumption beyond PR93's broad ℓ²-only descriptor. The result still falls far short of the seed: the Hilbert–Schmidt estimate for arbitrary `L≈Z` columns is only `O(|F| L)`. A proof must exploit the interaction of selection and source coefficients, not merely the row count.
