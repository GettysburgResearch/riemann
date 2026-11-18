# A single signed moment inequality sufficient for incremental progress

Status: conditional reformulation of THM-F012; no estimate of the new analytic input is proved. Source setting: AF arXiv2608.13637v2 §7.2(f), flat bandwidth-one window, withd/N->1 and the usual finite zero-count interface. This is about classical zeta, not generalized RH.

Suppose a Hermitian matrix familyG_T has normalized momentsm_k(T)=tr(G_T^k)/d_T withm1->1 andm2->4/3. Let

D_T=84m3(T)−16m4(T).

For the globally valid one-sided certificatep(x)=1−7x/4+2x²/3,

L_T(p²)=1−(7/2)m1+(211/48)m2−(7/3)m3+(4/9)m4

=(121−D_T)/36+o(1).

Thus THM-F012 givesn_+(G_T)/d_T>=1−L_T(p²). If the source's count constraints n_+<=s1+s2+pairs andN>=s1+2s2+2pairs hold, then

liminf s1/N >= [liminf D_T−103]/18.

The statement can be expressed safely as a uniform eventual bound: ifD_T>=D0−o(1), then the right side is(D0−103)/18. This avoids silently assuming separate limits form3,m4. No separate boundedness of those moments is used by this fixed linear combination; positivity ofL_T(p²) itself forcesD_T<=121+o(1).

## Precise targets

- D0>115 improves the flat two-thirds baseline.
- For any target proportionkappa0, D0>103+18kappa0 suffices to exceed it.
- To exceed the source Knausgård simple-critical value1669159/2478195, the exact threshold isD0>31699883/275355, approximately115.1236876. This comparison treats that preprint's result as its stated value, not an independently completed proof audit by this track.
- The proposed sine-process valuesm3=2,m4=13/4 giveD0=116 and hence13/18, as in the source's conditional extension.

The useful missing lemma is therefore an eventual lower bound for84trG_T³−16trG_T⁴, normalized byd_T, at the chosen explicit threshold. Proving separate moment asymptotics would suffice, but is stronger than this particular certificate requires.

## Why the reformulation is not yet an easier theorem

The quartic term has a negative coefficient inD. Rare large spectral outliers can destroy the bound while contributing little to lower moments. Even positive Gram matrices with unit diagonal and fixed first/second moments can have such tails; mere positivity or RH-style real spectra does not supply the inequality. Close clusters and multiplicities are material risks. The prime-side expansions oftrG³ andtrG⁴ involve higher correlations beyond the already available pair-correlation input. No cancellation of those difficult terms has been demonstrated here.

A concrete next analytic step is to expand the single signed combination before estimating its summands, keeping exact smoothing and support, and determine whether any off-diagonal prime correlation terms cancel or have a usable sign. Failure should be documented by an explicit surviving correlation term or an allowed Gram countermodel. A numerical test on zero data would be exploratory only; it cannot establish this eventual bound.

The existing source-specific polynomial arithmetic is independently checked, but this frontier formulation has no claimed historical novelty and no new unconditional zero-proportion conclusion.

## Stronger prime-matrix version through clipped Lipschitz transfer

The following independently reviewed refinement avoids assuming that the unbuffered zero-side matrix inherits higher moments. LetF_T be the full prime-side Hermitian matrix,G0_T the finite zero-side matrix without a buffer,d their common dimension,r=d/N andrho=||F−G0||_HS/sqrt(d). Define

p(x)=1−7x/4+2x²/3, q(x)=1−p(x)², h(x)=max(q(x),−1).

Then q<=h<=1_{x>0}, andh is globally6-Lipschitz. Indeed the active derivative satisfies|q'|²=(32/3)p²(p+19/128)<=211/6<36. Finite Hoffman–Wielandt/Cauchy–Schwarz gives

n_+(G0)/d >= trq(F)/d−6rho.

The finite source block counts therefore yield the exact inequality

s1/N >=2r[trq(F)/d−6rho]−1.

Writingm_k^F=trF^k/d andD_F=84m3^F−16m4^F,

trq(F)/d=(7/2)m1^F−(211/48)m2^F+(7/3)m3^F−(4/9)m4^F.

Thus under r->1,rho->0,m1^F->1,m2^F->4/3 andliminfD_F>=D0, the same conditional conclusion is

liminf s1/N >=(D0−103)/18.

Here D_F,notD_G0,is the required prime-side quantity. No higher-moment transfer toG0, vanishing operator norm, limiting spectral law or zero-atom theorem is used. The no-buffer estimateO(sqrtT) already makesrho->0; the classical zero-free sharpening is optional for a better rate.

This version also needs only the zero-side block-rank/index/count geometry, not its trace normalization. The finite perturbation core was actually checked locally inLean(THM-F014); the global clipping construction andLip6 have independent ordinary proofs in audits/adversarial_reviews/zero_buffer_clipped_moment_third_round3.md and hilbert_schmidt_moment_transfer_round3.md. The arithmetic D_F input remains completely unproved by this argument.
