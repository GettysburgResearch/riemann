# Finite boundary defect bounds counting curvature without semiboundedness

Research date: 2026-11-17. This is a source-grounded comparison plus an independently reconstructed auxiliary proposition. No literature novelty is asserted. The proposition concerns self-adjoint operators, not locations of Riemann zeros.

## What the primary source actually establishes

The downloaded source is Berkolaiko–Cox–Latushkin–Sukhtaiev, *The Duistermaat index and eigenvalue interlacing for self-adjoint extensions of a symmetric operator*, arXiv:2311.06701v4, revised 11 September 2025. Its arXiv landing page records the journal version as *Journal of Spectral Theory* 16 (2026), 1–49, DOI 10.4171/jst/590. We inspected the v4 preprint, whose numbering is used below; a journal/preprint line-by-line comparison was not performed.

**Theorem 1.1, pp. 2–3**, assumes S closed, densely defined, **bounded from below**, symmetric, with finite equal deficiency indices (n,n), and a boundary triplet. For self-adjoint extensions H1,H2 represented by Lagrangian planes L1,L2, and the Friedrichs plane F, its counting shift below the essential spectrum lies between −σ− and σ+, where

    σ−=ι(L1,L2,F),    σ+=ι(L2,L1,F),
    σ−+σ+=n−dim(L1∩L2)≤n.

Therefore in the semibounded compact-resolvent case the *same fixed* shift function has range length at most n, not merely absolute magnitude at most n. The fixed range is what gives a 3n, rather than a 6n, curvature estimate.

**Theorem 1.2, p. 4**, retains the assumptions of Theorem 1.1 and gives the difference of half-open interval counts by an endpoint Duistermaat-index difference, for [a,b] disjoint from essential spectrum. The proof is in §5, p. 19. It does not require unique continuation because common missing eigenvalues cancel between the two extensions. The source discusses a possible generalization beyond its stated hypotheses in §1.3, p. 5; that discussion is not itself a theorem.

**Theorem 6.2 and proof, pp. 22–24**, explain the finite-rank resolvent mechanism. In particular (S*−λ)D(λ)=0 puts the resolvent difference in the defect space, and the boundary-triplet computation gives rank D(λ)=n−dim(L1∩L2). The source then chooses a real anchor below both spectra to prove its interlacing theorem. Such a lower anchor does not exist in general for operators unbounded in both directions.

Accordingly one must **not directly cite Theorem 1.1 as a theorem for arbitrary two-sided spectra**. The proposition below removes the lower-bound assumption by treating both branches of a real resolvent reciprocally. Its proof uses only compact-resolvent spectral theory, the resolvent identity and a finite-rank inertia argument; no global count from −∞ is introduced.

Dancis–Davis1987, DOI10.1016/0024-3795(87)90106-6, was bibliographically verified against the publisher/Crossref and an author bibliography. The publisher labels it open archive, but the PDF and text-mining API routes returned403 in this environment. No full mathematical text was obtained, so it is not represented as substantively read or audited. The modern arXiv source supplies the actual source reading in this task.

## Independently reconstructed proposition

Let S be a closed densely defined symmetric operator on a Hilbert space H, with finite equal deficiency indices (d,d). Let H0,H1 be self-adjoint extensions of this **same** S on this **same** H. Assume one, hence both, extensions has compact resolvent. Neither S nor the extensions need be bounded above or below.

There is a real c in ρ(H0)∩ρ(H1). Set

    Rj=(Hj−c)⁻¹,       F=R1−R0,
    p=n+(F),           m=n−(F),       r=p+m=rank F.

Then r≤d. Define the anchored relative count by finite windows:

    ξ(x)= N_H1((c,x])−N_H0((c,x])                  if x>c,
    ξ(c)=0,
    ξ(x)=−N_H1((x,c])+N_H0((x,c])                 if x<c.

Every count on the right is finite. For **every real x**, with multiplicities and the displayed endpoint conventions,

    −m ≤ ξ(x) ≤ p.

Thus the range length is at most r≤d. Moreover, for arbitrary finite u<v,

    ξ(v)−ξ(u)=N_H1((u,v])−N_H0((u,v]).

For K>0 define

    Δ_H(K)=N_H((2K,4K])−2N_H((K,2K]).

Equivalently, Δ_H=N_H((0,4K])−3N_H((0,2K])+2N_H((0,K]). Then

    |Δ_H1(K)−Δ_H0(K)| ≤ 3r ≤ 3d.

The constant3 is sharp even for genuine first-order differential boundary extensions with d=1 and spectra unbounded in both directions. Direct sums give sharpness for every finite d.

The result in fact applies to any pair of compact-resolvent self-adjoint operators for which F at one common real anchor has finite rank r, without requiring a common S. The common-extension hypothesis is used to deduce r≤d and to interpret the cost as boundary dimension.

## 1. Why compactness and a real anchor are available

At w=i, write Rj(i)=(Hj−i)⁻¹ and D(i)=R1(i)−R0(i). Since Hj⊂S*,

    (S*−i)D(i)=0,

so ran D(i)⊂ker(S*−i) and rank D(i)≤d by the definition of the deficiency index. Thus compactness of one Rj(i) implies compactness of the other.

A compact-resolvent self-adjoint operator has isolated real eigenvalues of finite multiplicity and no finite accumulation point. The union of the two spectra is discrete locally and countable; some real c avoids both spectra. This is only a **single common resolvent point** requirement. It is not a common lower spectral bound.

For completeness, the resolvent identity gives, at any common z and w,

    D(z)=[I+(z−w)R1(z)] D(w) [I+(z−w)R0(z)].

To check the possibly noncommuting factors, observe

    [I+(z−w)R1(z)]R1(w)=R1(z),
    R0(w)[I+(z−w)R0(z)]=R0(z),

and expand: the two cross terms (z−w)R1(z)R0(z) cancel. The outer factors are invertible, with inverses I+(w−z)Rj(w). Therefore rank D(c)=rank D(i)≤d. At a real c both Rj are bounded compact self-adjoint, so F is finite-rank self-adjoint and its inertia p,m is well defined.

This proof does not assume that dim ker(S*−c)=d at a real point and does not need an unproved real-defect-space extension of a nonreal formula. The needed finite rank is transported directly from i.

## 2. Inertia controls both nonzero tails of compact operators

Let C0,C1 be bounded compact self-adjoint operators, C1−C0=F, with p positive and m negative eigenvalues of F. For t>0, one has

    −m ≤ N_C1([t,∞))−N_C0([t,∞)) ≤ p.                 (A)

Here only finite upper tails are counted. To prove the upper bound first for strict tails, let E1 be the spectral subspace of C1 for (t,∞). On E1 every nonzero v satisfies <C1v,v>>t||v||². Intersect E1 with ker F+, losing at most p dimensions. On this intersection C0=C1+F− in the quadratic-form sense, so <C0v,v>>t||v||². Projection onto C0's spectral subspace for (t,∞) is injective on that intersection: a nonzero vector orthogonal to that subspace would have <C0v,v>≤t||v||². Consequently

    N_C1((t,∞))−p≤N_C0((t,∞)).

Swap 0 and1 to get the lower bound, since the positive inertia of −F is m. Passing through thresholds increasing to t from below supplies [t,∞). All relevant counts are finite because t>0.

Apply this strict-tail argument to −C0,−C1 at threshold −t when t<0. Since −F has inertia (m,p), it gives

    −p ≤ N_C1((−∞,t))−N_C0((−∞,t)) ≤ m.              (B)

The reversal of p,m in (B) is essential. It will be canceled by the minus sign in the relative count below the anchor.

## 3. The reciprocal map gives the same range on both sides

The spectral theorem maps every Hj eigenvalue λ to (λ−c)⁻¹ for Rj.

If x>c, set t=(x−c)⁻¹>0. Then exactly

    N_Hj((c,x])=N_Rj([t,∞)).

Equation(A) yields ξ(x)∈[−m,p].

If x<c, set t=(x−c)⁻¹<0. The reciprocal function is decreasing on the negative branch, and the half-open conventions give exactly

    N_Hj((x,c])=N_Rj((−∞,t)).

There is no eigenvalue at c. Equation(B) controls the difference of these negative resolvent tails in [−p,m]. The **minus sign in ξ** reverses that interval, giving once again ξ(x)∈[−m,p]. At c, ξ(c)=0 lies in the same interval; both counts vanish near c because c is a common resolvent point.

This treats both branches with one fixed pair (p,m). Estimating them independently by |ξ|≤d and then discarding their common range would unnecessarily lose a factor2.

The ξ function is right-continuous with jumps equal to the difference of spectral multiplicities. Additivity of finite half-open counts proves the interval-difference identity. No absolute count N((−∞,x]) is defined for the two-sided limiting operators. Changing the common anchor merely adds an integer constant to ξ; neither its range length nor the three-height expression changes.

## 4. Three-height cancellation and sharpness

The interval-difference identity gives

    Δ_H1−Δ_H0 = ξ(4K)−3ξ(2K)+2ξ(K).

Because the coefficients sum to zero, subtract −m from all three ξ values. They now lie in [0,r]. The sum of positive coefficients is3 and the negative coefficient has magnitude3, so the expression lies in [−3r,3r]. All endpoints are already covered by(A),(B); no generic-position or zero-eigenvalue exclusion is needed.

To see sharpness within actual extension theory, take H=L²(0,2π), S=−i d/dx on H0¹(0,2π), and

    Hθ f=−if′,
    D(Hθ)={f∈H¹(0,2π): f(2π)=exp(2πiθ)f(0)}.

Integration by parts makes these domains self-adjoint. The minimal S has deficiency(1,1): the equations S*f=±if have one-dimensional solution spaces generated by exp(∓x). Every Hθ has compact resolvent by the compact H¹→L² embedding and has spectrum {n+θ:n∈Z}.

Choose θ1=3/20, θ0=2/5 and K=3/10. The positive counts at K,2K,4K are respectively (1,1,2) for Hθ1 and (0,1,1) for Hθ0. Therefore

    Δ_Hθ1=1,      Δ_Hθ0=−2,      Δ_Hθ1−Δ_Hθ0=3.

For the two distinct phases the common domain intersection is exactly H0¹, so these really are extensions of the same minimal S. They are unbounded in both spectral directions. Finite direct sums yield3d.

## 5. What this says about realizable energy-dependent boundary models

A boundary evaluation can be unbounded as an operator on the ambient L² space, so the previous bounded block-coupling proof cannot simply be reused. The proposition instead applies when the proposed model supplies **one fixed self-adjoint extension**, and a reference extension, of a common closed densely defined S with finite deficiency d and compact resolvent. Its boundary coefficients may be large. Eliminating internal variables may make a scattering formula depend on energy; that dependence does not defeat the estimate if the full fixed-domain realization satisfies the hypotheses.

Conversely, writing down an arbitrary unitary matrix S(k) for each real k does not establish any such realization. An energy-dependent domain condition alone need not define a single linear self-adjoint operator. A model must identify the full Hilbert space, operator/domain, common symmetric restriction, deficiency indices, and compactness. Finite auxiliary degrees live in the full space and cannot be omitted when checking those hypotheses.

If the full reference operator is H0=A⊕D with an M-dimensional Hermitian auxiliary block D, and H1 shares the stipulated common S with **that full reference**, then additivity gives

    |Δ_H1−Δ_A| ≤ 3d+2M.

Indeed an eigenvalue of D contributes either0,−2 or1 to Δ_D, so |Δ_D|≤2M. This is bookkeeping under the stated full-space realization, not an assertion that arbitrary auxiliary elimination automatically gives finite defect d or that d=M.

The theorem compares the **same two operators at all three heights**. One may let their parameters vary with the external family index K, provided each comparison fixes them across K,2K,4K and uses its own actual deficiency/rank. Essential spectrum is excluded by compact resolvent; no claim about counts through continuous spectrum is made.

If the physical spectral parameter is g(k), use g(K),g(2K),g(4K) as the three ordered energy endpoints. The proof works for any ordered triple with coefficients2,−3,1; a common monotone change of spectral parameter adds no factor. Confusing wave number k with energy k² is unnecessary and can be avoided explicitly.

For the director's first-order E-channel reference graph with |Δ_H0(K)|<3E, a boundary model in this common-extension class satisfies

    |Δ_H1(K)|<3E+3d.

Consequently, matching classical zeta zero counts at all three heights with errors≤εK K forces the same curvature-type cost, now with E+d, whenever the reference graph estimate and target Riemann–von Mangoldt normalization have been established. This is a conditional model-cost consequence, not a result about zeta zero locations. No claim that d is automatically equal to a chosen number of auxiliary states is made.

## Review status and reproducibility

The parent independently checked the two reciprocal branches, fixed range [−m,p], half-open endpoint conventions, 3r cancellation and common-real-anchor existence before this write-up. The finite-rank transport identity and sharp differential example were then supplied separately. This is an independent reconstruction with parent review; a separate third reconstruction is not claimed here.

Exact rational sharpness/count checks: `python experiments/code/extension_interlacing_round2.py`. Results: `experiments/results/extension_interlacing_round2.json`. These finite checks supplement the abstract proof, not replace it.

Primary source limitations: no full-paper L1 reading of the 35-page modern preprint, no audit of every Duistermaat-index/SGA-like prerequisite, no Dancis–Davis full-text audit, and no proof that an arbitrary proposed S(k) belongs to the realizable class. The complete source-access/reading scope is in `logs/extensions_round2.md` and `papers/spectral_extension_round2_records.jsonl`.
