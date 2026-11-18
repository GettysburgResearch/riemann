# Director scope adjudication: two analytic hypothesis maps

Date: 2026-11-17. These are exact consequences and interface controls relative to primary source theorems. They do not independently certify every upstream analytic input or assert a new best bound.

## Pintz Corollary 4 and the fixed right slab

Source PAPER-ANALYTIC62-013, arXiv2310.04544v1. Independent complete source reading: audits/latest62_analytic2_fullreads.md. Separate reconstruction: prefix_formula62_pintz_bgstb_slab.md. I read the exact source statements and relevant proof range and independently checked the exponent gap, finite-threshold mesh and charged-pair conclusion.

The usable source statement is N(1−η,T)≪_(η,ε)T^(f(η)+ε), f(η)=η/(1−4η), for each fixed0<η<1/4. Its power improves on2η only for η<1/8; equality at1/8 gives no saving with the arbitrary exponent loss. The source introduction's printed max range differs from the proof's min range; no application here uses the larger printed range, and no new error finding is promoted from that discrepancy.

For fixed0<d≤1/16 put I=[7/8+d,1−d], L=logT and Δ_d=min_(η∈[d,1/8−d]) [2η−f(η)]>0. Then, counting zero multiplicities,

    H_I(T)=Σ_(0<γ≤T,β∈I) T^(2β−1)/[1+L²(β−1/2)²]
          ≪_(d,ε) T^(1−Δ_d+ε)/L².

For d=1/16 the slab is one closed line and the direct density estimate applies; for d>1/16 it is empty. A fixed finite horizontal mesh, independent ofT, avoids assuming uniformity of the implicit constant at a moving threshold. Each cell [a,b] in η uses the inclusive count at1−b and the maximum weight T^(−2a); choosing its width≤ε/4 preserves the gap. This proves the bound for both slab boundaries. The BGSTB far-pair charging lemma then bounds only pairs whose right-hand maximizer is charged into I by O(L H_I), not every pair incident to a zero in I. Outside-slab pairs remain. At the7/8 endpoint a synthetic positive count T^(1/4)log²T meets every fixed-ε source exponent but can give H~T. Spreading copies across height cells preserves a unit-window logarithmic bound. This is an inference countermodel, not actual zeta zeros.

## Dong–Wang–Wang–Zhang inverse theorem

Source PAPER-ANALYTIC62-019, arXiv2608.31060v1, Theorem1.1. Complete source reading by latest agent and targeted independent review witness62_dong_inverse_phase.md. I checked the original theorem, the exact trigger, moment extraction, open-disk geometry and algebraic VK inversion. The source proof's constants remain existential.

Let Q=logT, y=logx, sqrt(Q)≤y≤Q/2, T≤|t|≤2T. The trigger is the one specific unweighted sum |Σ_(n≤x)n^(it)|=x/N with1≤N≤y^(1/100). One center1+iφ with |φ−t|≤cN works for every cN^6≤L≤y/2, giving at leastL/360 zero copies in the open disk of radius LQ/y². For k>0 and1<=N0<=y^(1/100), a lower2k moment normalized by a probability measure on the permitted t-set, strictly above(x/N0)^(2k), supplies a pointwise witness withN<N0; an upper moment or a moment of a different polynomial does not. The triangle bound ensuresN≥1. The twist center is shared across radii although an auxiliary proof frequency may vary.

The disk with radius≤1/2 excludes the critical line, including tangency because it is open. Larger radii may meet the line but do not isolate a line zero or its order. Thus the result cannot by itself supply the exact critical-line evaluation needed for finite phase annihilation. A ball evaluation of the finite sum with the explicit Lipschitz error dΣlogn can certify its trigger, but numerical values ofc,T0 and a nonempty L range are still needed for a finite theorem application.

Combining a separate high-height Vinogradov–Korobov zero-free width c1 Q^(−2/3)(logQ)^(−1/3) with radius chosen strictly within it rules the trigger out if

    y≥C Q^(250/291)(logQ)^(50/291),   y≤Q/2,

since y^(97/50) must dominate Q^(5/3)(logQ)^(1/3) to allow L≥cN^6. This is an asymptotic source-dependent consequence, not an explicit threshold or new best exponential-sum bound. At the allowed length x=sqrtT the source's uniform Lemma5.1 bound already excludes the trigger on high blocks, including blocks containing actual line zeros. Hence a line zero does not force the trigger at every permitted length. The next precise step for a numerical application is to makec,T0 effective; for a phase projection it would additionally need genuine line-zero location and vanishing-order information.
