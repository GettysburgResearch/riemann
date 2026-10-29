# The sixth-order box count and the tracker source interface

**Status.** Source-level comparison and exact scalar calculation. The rectangular sieve and buffered detector needed for the box estimate are source-qualified replays, not independently established here. No improved tracker bound follows. The marked detector may admit stronger inputs than those considered below.

The [fourth-moment box calculation](../2026-10-29-fourth-moment-cyclic-box/README.md) treats sextic labels `u=A B⁵` with A,B good squarefree and coprime and `NA≤NB`. In the tracker the physical size variable is the row norm `Y≈Nu`, not the conductor scale `X≈N(AB)`. Since `NA≤NB`,

    (N A N B)³ ≤ (N A)(N B)⁵ = N u.

Thus all such labels with `Nu≤Y`, even after summing all boxes, number `≪_ε Y^(1/3+ε)` by ideal-divisor counting. The optimized n=6 box at σ=4/5 has `NA≈X^(1/15)`, `NB≈X^(14/15)` and `Nu≈X^(71/15)`, so it has at most `Y^(15/71+ε)` labels by counting alone. These are sparse subfamilies in the tracker's row ordering; their improved zero-density estimates do not give a count of all physical sixth-free rows.

A general good sixth-free row has a unique ideal valuation decomposition

    (u)=A B⁵ C² D³ E⁴,

where A,B,C,D,E are pairwise coprime squarefree ideals. In particular the source [`physical_source_amplitude_count`](https://github.com/GTimG/QuasiRiemannTracker/blob/e5a82f72d8ff39a3cc1ad044e6acd727e77a3fc4/submissions/2026-10-29-arvi-density/src/Submissions/arvi_density/ReturnD/PhysicalDirect/PhysicalSourceCount.lean) quantifies over arbitrary `Finset FreeRow` and then filters by the physical prime-slot amplitude; it does not restrict C,D,E to one or require `NA≤NB`. The initial [selected source count](https://github.com/GTimG/QuasiRiemannTracker/blob/e5a82f72d8ff39a3cc1ad044e6acd727e77a3fc4/submissions/2026-10-29-arvi-density/src/Submissions/arvi_density/ReturnD/PhysicalDirect/SourceCountInitial.lean) requires the actual rowwise detector fibers and marked moment hypotheses. Hence a box theorem cannot simply be substituted as a `CountScheme` face for this source.

Fixing `C,D,E` makes their character product a common column twist, and in an arbitrary-coefficient rectangular sieve that twist is a modulus-at-most-one coefficient multiplier, with original zeros. Also the number of possible powerful parts `C²D³E⁴` of norm at most T is `≪T^(1/2+ε)`. These observations suggest a dyadic route, but they do not prove the tracker input. A completed route must control the physical marked slot and detector/profile estimates **uniformly for the moving twist** `χ_(C²D³E⁴)`, sum all powerful-part dyads, and use the actual total conductor and row scale in the detector. The source's currently stated fixed-ray twist is not a uniform theorem for a good conductor that grows with Y. Even after this, a count for unmarked zeros has to match the tracker's amplitude-selected bins and the normalization of δ and p.

There is an independent scalar obstruction to the naive unmarked replacement. The reverse orientation includes the dense squarefree subfamily B=C=D=E=1, A arbitrary, where conductor and row scales agree. At the tracker's fixed-face bottleneck `(δ,p)=(223/500,1/2)`, the sixth-order rectangular exponent has `c=1/6` and

    E(x)=max{1,1/6+x,5/6+x/3},   δ=223/500.

Even granting the source-qualified inverse-second and ordinary-fourth moments, their full-cutoff scalar relaxation is minimized at

    t=3000/2831,   R_unmarked=12803/16986≈0.7537383728.     (1)

For `L=2t/3`, the decreasing third face of `E(x)−δx` at L equals the increasing second face at t. If r≥L the inverse witness is bounded by this R; if r<L then the full ordinary interval has `2m∈[L,1]`, so the fourth moment gives the same bound. Conversely the feasible scalar witnesses `(r,m)=(t,0)` and `(2t/3,t/3)` give the matching lower envelope; this is a statement about these majorants, not actual zeros. The tracker's source129 **amplitude-selected** C count at the same point is

    R_selected=137478360780643/225606975000000
              ≈0.6093710568.                                 (2)

Thus the unmarked relaxation is larger by `30735481372499889/212897782075000000≈0.144367316`. Filtering a row family by amplitude can only reduce its count, so (1) remains a valid but weaker upper bound for that subset; it does not provide the count improvement required at the existing return bottleneck. The comparison does not rule out a new genuinely marked fourth-moment estimate, a different count face, or a different endpoint argument. The physical source theorem, selected moments, finite common profile, detector height, and conductor-to-row transport all remain separate obligations.

**Independent reviews.** Families and High_match checked the row-norm sparsity, optimized box scaling, pinned physical-source quantifiers, scalar witness calculation and exact selected-count comparison. The moving-twist and marked-source interfaces remain open.
