# A concrete complement estimate after removing low-radical Gauss profiles

**Status.** This is an elementary reduction to an unproved operator estimate. It combines the [moving-twist projection bound](moving-twist-overlap.md) with the [all-row growing-rank obstruction](../2026-10-29-gauss-growing-rank/README.md); all quoted analytical inputs remain source-qualified. No complement estimate or zero-free region is claimed.

Let T_(Y,P) be the full good natural-row sextic operator at row norm scale Y and squarefree source norm scale P=Y^(6/5), with fixed ray sector and zero masks. For δ>0 fixed, let V be the span of the coefficient vectors v_(P,h) of the moving-twist note, indexed by distinct good sixth-power-free h with N rad(h)≤P^(25/72−δ), and by one fixed smooth source norm profile. Let Π be its orthogonal projection. That note proves, for the fixed smooth Möbius vector m and after a sufficiently small fixed height budget,

    ||T_(Y,P) Πm||² ≪ Y^(1−12δ/5+ε).                             (1)

A sufficient additional statement is the full-space **complement estimate**

    ||T_(Y,P)(I−Π)||² ≪ Y^(1+ε)                                  (2)

for every ε>0, with constants uniform in Y and the stated fixed data. If (2) holds, then ||m||²≪1 and the triangle inequality give

    ||T_(Y,P)m||² ≪ Y^(1+ε).                                      (3)

This remains true after restricting the rows to any subset, because row restriction does not increase the norm. A bound only for the single vector `(I−Π)m` is a weaker sufficient input. In either form, applying it to a physical detector would still require its actual prime products, masks, profiles and cumulative height range to lie in the proved class; (3) alone does not imply a zero-free theorem.

There is no proof of (2) in the cited source. Xu–Sang's profile comparison is a centered estimate inside a prescribed finite-dimensional radial-profile family, not an estimate on the whole orthogonal complement of V. Proposition 3.1 gives individual Gauss-image norms with explicit moving-support error, not a diagonalization or control of arbitrary linear combinations and all other source vectors. The local factor Ω and the Möbius overlaps do not supply such control. In fact, for the source's explicit centered scale-comparison profile at this target, the proof of Xu–Sang Lemma 5.1 gives a squared norm O((YP)^ε[Y(1+(P²/Y)^(1/12))+P]) after converting its 1/P normalization to an ℓ²-scale coefficient vector. At P=Y^(6/5), that available upper bound is O(Y^(6/5+ε)); even for this individual centered direction it does not prove a Y-sized estimate. An upper bound of that size is not a lower bound and does not disprove (2).

At balanced row and source scales, the separate all-row growing-rank result shows at least Y^(5/42−ε) eigenvalues of size at least Y^(8/7−ε); consequently no projection of smaller rank can yield a Y-sized complement bound there. Our span has potentially ≪H^(1+ε), with H=P^(25/72−δ), which is much larger than that lower bound at the *different* target scale P=Y^(6/5). The existing lower-bound computation therefore neither disproves (2) at the target scale nor proves that the chosen span captures the obstructing eigenspace. In particular, the individual h=p⁵ tests whose images are large need not themselves be eigenvectors, and the balanced-scale result cannot simply be transferred to the longer source interval.
