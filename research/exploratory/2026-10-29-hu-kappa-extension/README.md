# Parameter extension of Hu's paired moment: an induction audit

**Status:** Proposed conditional source adaptation, **not** a standalone proof of the moment and **not** a zero-free-region theorem. The parameter inequalities below are proved. Applying them to Hu's complete induction requires the κ-independent source interfaces itemized below, including all coefficient, mask, exceptional-row and profile controls; those have not been independently replayed.

**Sources:** Hu, [*A seven-eighths zero-free half-plane for unitary Weil L-functions*](https://hexagonmath.org/2610.00216v1), Theorem 4.2, §§4.6–4.8, Proposition 4.14; OpenAI, [*The quasi-Riemann hypothesis*](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf), Lemma 18.1 and its proof; Xu–Sang, [arXiv:2610.15291v2](https://arxiv.org/abs/2610.15291v2), Lemma 2.1 and Appendix A. Xu–Sang carry this κ-range audit out for the OpenAI source; Hu's moment includes a fixed genuinely unitary background and has an additional source-matching burden.

## Proposed extension, with precise imports

Fix Hu's field `K` containing `mu_12`, fixed infinity-type orbit, arithmetic data and source coefficient classes. Suppose the following Hu §4 proof ingredients hold with their displayed quantifiers uniformly on the compact parameter range `13/18<=kappa<=1`:

1. the unrestricted zero-slot moment and common-profile/finite-seminorm bounds;
2. the uncentered two-transform induction, child width decrease, terminal controls, exceptional-row cancellation, original masks and coefficient identities, including the fixed unitary background on every child;
3. for each positive slot, the prime estimate (4.38) with exponent `kappa`, whenever every finite-order Hecke L-function over `K` has no zeros to the right of `(1+kappa)/2` (and absolute counting at `kappa=1`);
4. the centered comparison and its reflected profile with the same scale and loss relation as OpenAI (18.15), and the finite-depth, loss, height and mesh order described in Hu Proposition 4.14.

Then Hu's paired moment conclusion (4.4)–(4.5) holds for every `13/18<=kappa<=1`, with its same zero-free premise when `kappa<1`, same finite exceptional family, fixed unitary background and source masks, and a mesh uniform on that compact κ-range before the number of slots. In particular, `kappa=29991/40000` is inside the range. The paired moment needed in a second stage is obtained only if the stated finite-order zero-free ceiling `(1+kappa)/2` is itself available in exactly the required all-character scope.

These imports are stronger than merely citing Hu Theorem 4.2, whose printed hypothesis starts at `3/4`; in particular this note does not silently extend that theorem.

## Exact parameter audit

Write `M` for effective row width, `z>=0` for total live slot length, and `A=n1+n2+z`. The source capacity is

    A+(6kappa-1)z <= M,       A>=z.

On `13/18<=kappa<=1` this gives

    kappa z <= M/6,        z <= 3M/13.

The first inequality, not the old auxiliary bound `z<=2M/9`, is what pays the small-width terminal exponent in OpenAI (18.13) and Hu's corresponding width-floor argument.

For the same-band centered comparison suppose `A>5M/6`. Then

    (6kappa-1)z < M/6,       6kappa-1 >= 10/3,       z<M/20.

Hence both comparison lengths `M/4` and `A-z-M/4` are positive and at least `M/4`. The source's reflected comparison relation gives

    A_comp <= 3M/2-A+2z+xi < 23M/30+xi,
    A_comp+(6kappa-1)z <= 5M/2-2A+2z+xi < 14M/15+xi.

The former lies at least `M/15` below the source uncentered cutoff `5M/6`; the latter lies at least `M/15` below the capacity `M`, before `xi`. For widths above a fixed positive floor, choose `xi` below the corresponding fixed fraction of that floor. These bounds and the comparison-length margins are uniform in κ on the entire compact interval.

For a child let `F=(A_act-M_act+(6kappa-1)z_act)_+`. Removing a whole slot of width `s` decreases the left side of the capacity condition by exactly `6kappa s`, and its prime estimate costs exponent `kappa s`. A greedy prefix whose total removed width first reaches `F/(6kappa)` overshoots by at most the slot mesh `eta`; the accumulated cost is at most

    kappa [F/(6kappa)+eta] <= F/6+eta.

If the prefix exhausts the live slots before reaching the requested width, invoke the unrestricted zero-slot moment; it would be invalid to assert that a nonzero-slot child then satisfies the capacity condition. Hu's source width-gain estimate `F/6<=Delta_child+O(xi)` is a separate import. This is the only reason the clipping cost is paid by the child width drop.

Finally, for all admissible κ one has `0<=6kappa-1<=5`, so the source's aggregate support-error estimate remains

    |Delta M| + |Delta A| + 5|Delta z|.

The prime-line shift from `(1+kappa)/2` by any fixed `e>0` changes the **squared** slot exponent by `2ez`; all lengths lie in prescribed bounded ranges, so this can be put into a previously fixed loss uniformly over κ. The line lies a fixed positive distance to the right of 1/2 throughout the interval. When `kappa=1`, the source uses absolute prime counting instead. The finite target and its height/conductor are handled in Hu's stipulated order, not absorbed into an unquantified exponent.

## What the audit does and does not establish

These calculations reproduce the parameter-dependent part of Xu–Sang Appendix A and show that the numerical thresholds appearing in the OpenAI centered proof do not prevent the smaller κ. Inspection of Hu §4 finds the same affine capacity, slot cost, width-drop and aggregate-support forms; the source's infinite-type background is maintained through his coefficient identities, not approximated by finite-order characters.

The unresolved proof obligation is an explicit traversal of Hu's two-transform and exceptional-terminal proofs with the enlarged compact κ interval, checking that every imported lemma and each constant/mesh quantifier is truly independent of the old lower endpoint. In particular one must establish that the finite-character prime estimate applies to every live slot and derivative after all masks and twists, that all centered comparisons preserve the two independent physical profiles and the fixed unitary background, and that no source dependency is used only in its original `3/4` range. If any such lemma has an additional κ-dependent assumption, the audit above does not repair it. No claim is made that this work has verified those imports or proved their extension.

**What was done:** checked Hu's displayed κ occurrences, OpenAI Lemma 18.1 proof's parameter-dependent inequalities and Xu–Sang Appendix A; proved the elementary inequalities shown above. No Lean build or full theta/moment proof replay was performed.
