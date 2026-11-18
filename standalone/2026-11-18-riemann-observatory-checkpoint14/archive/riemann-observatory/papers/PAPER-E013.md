# PAPER-E013 — Partial sums of the Möbius function

Kannan Soundararajan. *Journal für die reine und angewandte Mathematik*631(2009),141–152. DOI https://doi.org/10.1515/CRELLE.2009.044 . Exact title/author/DOI verified with Crossref; pagination verified against the author's Stanford publication profile. Crossref encodes year2009 as its volume and631 as issue; the conventional journal citation is retained here.

Actual mathematical source: https://arxiv.org/pdf/0705.0723v2 , version13February2008,11pages. The current arXiv history listsv1 on5May2007 andv2 on13February2008. The journal text was not compared. Private PDF `sources/soundararajan_round4/sound0705v2.pdf`, SHA256 `9bacaa0c6bbaf687091d8be7b9f0df3e58727339002c9cabcb4de90e33f41fa7`. Metadata and landing-page snapshots are stored alongside it. Accessed17November2026.

**Scope:** all11pages were read substantively, including the proofs and references: whole-work Level1. Theorem/proof architecture and the typical-height lower-bound mechanism were reconstructed in `audits/soundararajan_mobius_round4.md`. Not a whole-paper Level2 audit: the full primary proofs of the Selberg–Beurling majorants, explicit formula and Maier–Montgomery large sieve have not been independently audited here. No new mathematical error is asserted.

## Exact central results

Let M(x)=sum_(n<=x)mu(n). Theorem1 p1 assumes RH and proves, for large x,

|M(x)|≪sqrt(x) exp((logx)^(1/2)(loglogx)^14).

The exponent14 is what this original source states. The later Balazard–deRoton treatment gives refinements of the method with exponent5/2+delta; that stronger bound must not be retrospectively quoted as this paper's Theorem1.

Theorem2 p2: underRH, for largeT,0<=h<=sqrt(T), and(loglogT)^2<=V<=logT/loglogT, the numberR of points T<=t1<...<tR<=2T, separated by at least1, at which

N(t_j+h)−N(t_j−h)−(h/pi)log(t_j/(2pi))>V

is bounded by

R≪T exp[−V log(V/loglogT)+3V loglogV].

Zeros are counted with multiplicity. Endpoint conventions forN at zero ordinates should be kept consistent with the explicit formula; the proof uses interval majorants rather than numerical zero samples.

Definition3 pp2–3 calls t in[T,2T] V-typical when: a smoothed prime Dirichlet polynomial of lengthx=T^(1/V) is bounded in modulus by2V for every sigma>=1/2; every subinterval of(t−1,t+1) of length2piV/logT contains at most3V zero ordinates; and every such subinterval of length2piV/((logV)logT) contains at mostV. All three conditions matter. A zero-count bound alone cannot silently replace the prime-polynomial condition.

Proposition4 p3: underRH, every t in[T,2T] is V-typical forV>=(1/2+o(1))logT/loglogT; for generalV in the above range the number of well-spaced V-atypical points is at mostT exp[−V log(V/loglogT)+4V loglogV], up to an absolute constant.

Proposition5 p3: underRH, at a V-typical t put sigma0=1/2+V/logT. For sigma0<=sigma<=2,

log|zeta(sigma+it)|>=−V loglogV;

for1/2<sigma<=sigma0,

log|zeta(sigma+it)|>=−V log[(sigma0−1/2)/(sigma−1/2)]−8V loglogV.

The lower bound is deliberately height-dependent and only at typical ordinates. Its use on an adaptive contour is not an unconditional uniform reciprocal-zeta estimate.

## Architecture, limitation and reusable questions

Theorem2 uses Selberg band-limited interval majorants, the explicit formula and a high-moment large-sieve inequality for prime Dirichlet polynomials. The maximal usable moment satisfies length^k<=T. Proposition4 packages those bounds into typical/atypical heights. Proposition5 combines a smoothed logarithmic-derivative identity with the local zero counts. The final Perron contour moves rightward at atypical heights; its total contribution balances the reciprocal-zeta cost against their rarity.

The source suggests a stronger Gaussian bound for **all V-atypical points** as a route to a much smaller conditional Mertens bound. This is a proposed input, not a theorem. The precise next task is to identify which improved prime-polynomial and short-interval zero-count estimates can jointly supply that stronger bound over compatible V ranges.

For the growing logarithmic-Riesz campaign, an actionable open interface is to replace its worst-height reciprocal-zeta tail estimate by an averaged estimate derived from this typical/atypical decomposition or newer negative moments. That transfer has not been proved, and the shifted arguments, smoothing scales and full height weights must all be matched. The current archive's growing-array theorem does not require a new improvement of this paper.
