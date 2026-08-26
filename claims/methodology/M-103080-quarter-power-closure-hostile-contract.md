# M-103080 — Hostile contract for the quarter-power Boolean closure

A reviewer must reconstruct the following in this order.

1. Verify the Boolean Vaughan identity for an arbitrary cutoff, not only
   `U=Y^(1/6)`.
2. Re-derive the squarefree lattice estimate
   `L_sf(Z)=O(Z^(-1/4))` from the fixed zero-moment derivative kernel.
3. Check that the complete Type-I bound is
   `O(Y^o(1) V W^(-1/4))` and remains Hilbert-valued under every owner
   projection.
4. Verify that the owner-product blocks are disjoint before the block-dependent
   cutoff is chosen.
5. Check the strict floor inequality
   `(V+1)^4>2Y/A`.
6. Verify that every balanced core contains two disjoint factors larger than
   `V`, and that they remain in the physical square core after the owner pair
   is removed.
7. Use the support direction correctly:
   `K_L(X/N)!=0` implies `N<=X`, not `N<=8X`.
8. Reconstruct the exact cutoff-transfer identity
   `B_U-B_V=T_V-T_U`.
9. Verify that the old BCI row is controlled before taking its negative part.
10. Rebuild the inherited chain from BCI through the fixed Mellin--Landau
    detector.

Immediate falsifiers:

```text
choosing V after observing an individual term;
using an owner fibre twice;
dropping the equal-pair normalization;
assuming the Type-I estimate stays power-saving at quarter power;
using a moving Mellin detector;
forgetting a stopped/source-boundary term;
promoting the replay into a proof of RH.
```

The theorem claims a subpower endpoint bound, not a power saving. That is
sufficient for the frozen consumer.
