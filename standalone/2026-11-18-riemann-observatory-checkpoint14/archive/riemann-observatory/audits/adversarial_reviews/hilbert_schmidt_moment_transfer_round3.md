# Independent reconstruction: weak spectral transfer and clipped finite-moment certificates

Date: 2026-11-17. Reviewer/proposer: li_advocate. Root independently proposed the weak-law connection; this review reconstructs it and adds a finite-prefix clipping lemma. Classical matrix facts are proved below rather than attributed to an unread original paper. No novelty, arithmetic moment estimate, or RH claim.

## 1. Hoffman–Wielandt in the precise Hermitian setting

Let F,G be Hermitian matrices on the same d-dimensional space, with eigenvalues α1≤...≤αd and β1≤...≤βd. Then

    sum_i(α_i−β_i)^2 ≤||F−G||HS².                      (HW)

To check the needed trace inequality, write TrFG=sum_{i,j}α_iβ_j p_{ij}, where p_{ij}=|<u_i,v_j>|² is doubly stochastic. A doubly stochastic averaging cannot increase the pairing of two sorted real sequences: summation by parts reduces this to the fact that weights r_j∈[0,1] summing to d−k maximize sum_j r_jβ_j by placing weight1 on the largest d−k entries. Hence TrFG≤sum_i α_iβ_i. Expanding the squared Hilbert–Schmidt norm proves(HW). This argument includes negative eigenvalues and does not require positive semidefinite matrices or commuting matrices.

For any globally Lipschitz h:R→R,

    |d^{-1}Trh(F)−d^{-1}Trh(G)|
      ≤Lip(h)d^{-1}sum_i|α_i−β_i|
      ≤Lip(h)||F−G||HS/sqrtd.                          (BL)

Therefore ||F_T−G_T||HS=o(sqrtd_T) transfers weak empirical spectral convergence between F_T and G_T. Bounded Lipschitz functions determine weak convergence. Equal dimensions and the normalized Hilbert–Schmidt rate are essential; an unnormalized o(1) or a statement about unrelated compressions is not being substituted.

## 2. What it does not transfer

Higher moments need not be close. Set d=k^6, F=I_d and G=I_d−diag(k²,0,...,0). Then

    ||F−G||HS/sqrtd=1/k→0,

but the normalized fourth-moment difference is

    d^{-1}(TrG^4−TrF^4)=k²−4+6/k²−4/k^4→∞.

The single outlier has mass1/d, so both empirical laws still converge weakly toδ1. This exact witness explains why a proof should transfer weak laws or bounded certificates, rather than silently transfer all polynomial traces.

## 3. A stronger finite-prefix certificate transfer

Let q be a real polynomial satisfying the pointwise one-sided inequalities

    q(x)≤0 for x≤0,    q(x)≤1 for x>0.                 (C)

Set h(x)=max(q(x),−1). Then:

* h≥q;
* both q and the constant−1 minorize1_{(0,∞)}, so h also minorizes it;
* h is bounded between−1 and1;
* h is globally Lipschitz. Indeed q is globally bounded above; if nonconstant it has even degree and negative leading coefficient, so {q≥−1} is compact and its derivative is bounded there. Outside that set h is constant. Constant q is immediate.

Functional calculus and(BL) now give the exact finite-dimensional inequality

    n_+(G)/d ≥Trh(G)/d
             ≥Trq(F)/d−Lip(h)||F−G||HS/sqrtd.          (CT)

Only the moments of **F** through degq occur on the right. No moment transfer for G, operator-norm-small error, spectral cutoff, or limiting law is needed for this finite certificate.

If F_T's fixed moment prefix gives Trq(F_T)/d_T→L(q), and the normalized Hilbert–Schmidt error tends to0, then liminf n_+(G_T)/d_T≥L(q). The degree and q are fixed before taking the T limit. This is useful for moment-SDP certificates as well as minimum-square certificates satisfying the one-sided sign condition.

## 4. An explicit robust fourth-moment certificate

Take the source-specific polynomial from the independent AF review,

    p(x)=1−7x/4+2x²/3,
    q(x)=1−p(x)²
        =(7/2)x−(211/48)x²+(7/3)x³−(4/9)x^4.

It satisfies(C), since p(x)≥1 for x≤0. For h=max(q,−1), one may take the explicit global Lipschitz constant6, using the parent’s independently derived sharpening below.

Here are exact bounds. The minimum of p is−19/128, so p never reaches−sqrt2. Also

    p(−1/4)=71/48>sqrt2,    p(3)=7/4>sqrt2.

Since p is decreasing to its vertex and then increasing, the active set {q≥−1}, equivalently |p|≤sqrt2, lies in[−1/4,3]. On that interval |p'|≤9/4. Where h is nonconstant,

    |h'|=|q'|=2|p p'|≤(9/2)sqrt2<7.

This already supplies a global bound7, including transition points. The stronger exact bound6 follows from

    (p')²=(8/3)(p+19/128),
    |q'|²=(32/3)p²(p+19/128)
          ≤(64/3)(sqrt2+19/128)<211/6<36

on the active set. Outside it h is constant; piecewise continuity handles transition points. Thus for arbitrary Hermitian F,G,

    n_+(G)/d ≥ (7/2)m1(F)−(211/48)m2(F)
                 +(7/3)m3(F)−(4/9)m4(F)
                 −6||F−G||HS/sqrtd,

where mj(F)=TrF^j/d.

If the **prime-side** F has limiting moments(1,4/3,2,13/4), the polynomial expression tends to31/36. An exact zero-side block matrix G differing by normalized Hilbert–Schmidt o(1) therefore has liminf n_+(G)/d≥31/36. Under d~N and the zero-side charge s1≥2n_+(G)−N+o(N), this yields13/18. This is a sufficient prime-side moment hypothesis, not an assertion that sourceAF's differently phrased moment hypothesis has already been proved or that its arithmetic moments transfer term by term.

### A single higher-moment combination suffices

Assume only m1(F_T)→1, m2(F_T)→4/3 and define

    D_T=84m3(F_T)−16m4(F_T).

Then Trq(F_T)/d_T=(D_T−85)/36+o(1), so the exact finite-dimensional certificate implies

    n_+(G_T)/d_T ≥(D_T−85)/36
                    −6||F_T−G_T||HS/sqrtd_T+o(1).

If D_T is bounded and d_T~N_T, with normalized Hilbert–Schmidt error tending to0 and the exact-block charge above,

    s1_T/N_T ≥(D_T−103)/18
                −12||F_T−G_T||HS/sqrtd_T+o(1).

The exact prelimit charge keeps the factor d_T/N_T; the simplified asymptotic display uses bounded D_T. Consequently a lower bound liminf D_T>115, together with normalized Hilbert–Schmidt error o(1), would beat the2/3 simple-on-line certificate; the sine input D=116 gives13/18. The exact limits of m3 and m4 separately are unnecessary for this sufficient implication. No bound for this arithmetic D_T is proved here. A matrix with the first two moments asymptotic to these values necessarily has limsup D_T≤121, since q≤1 implies Trq(F_T)/d_T≤1. In particular, the proposed improvement condition itself supplies the boundedness needed in that asymptotic simplification.

## 5. The all-fixed-moments connection

Suppose every fixed prime-side moment of F_T converges to that of a Hamburger-moment-determinate probability measure μ supported on[0,∞), with μ({0})=0. Hamburger determinacy here means uniqueness among positive measures on all ofR, not merely among measures supported on[0,∞), because the approximating F_T may have negative eigenvalues. The sine law’s exponential moment/even Carleman bound supplies this stronger property. Even moments give tightness and uniform integrability of every lower power, so the method of moments gives empirical(F_T)⇒μ. By(HW)/(BL), empirical(G_T)⇒μ whenever ||F_T−G_T||HS=o(sqrtd_T). Portmanteau for the closed set(−∞,0] gives

    limsup d_T^{-1}#{lambda_j(G_T)≤0}≤μ((−∞,0])=0.

Thus n_+(G_T)/d_T→1. The exact block charge then yields s1/N→1. No operator-norm limit is required; rare large eigenvalue outliers are harmless to weak convergence even when they destroy higher-moment comparison.

For the sine-Gram model, `proposals/independent_campaigns/sine_gram_all_moments_round3.md` proves the needed law properties for every weak expected-law subsequential limit, with an explicit external PW² interpolation input. The subsequent THM-SG309 graph/Hölder addendum proves existence/uniqueness of the full expected model moment limit. It does not prove any prime-side higher-moment asymptotic, almost-sure IDS, or convergence rate. A conditional application must specify which law's moments are being matched and the exact window/density normalization.

The finite clipped-certificate argument in§3 is stronger for any fixed available moment prefix: it does not require the complete model law. The all-moments weak-law argument remains a useful independent reconstruction and avoids all growing-degree choices.

## Status

Root's weak-law transfer was independently checked here. The clipping lemma and fourth-moment inequality are newly reconstructed connections within this archive, with no publication novelty claim. Parent and li_skeptic independently challenged and confirmed the clipping directions and normalized Hilbert–Schmidt transfer; the explicit improvement to Lipschitz6 is the parent’s calculation, checked here. The sine-law prerequisites have a durable independent review at `audits/adversarial_reviews/sine_gram_skeptic_round4.md`. No claim about sourceAF's main unconditional theorem is changed by this note.

A degree or Lipschitz constant growing with d requires additional quantitative control and is outside the fixed-certificate result.

Durable independent reviews: `hs_clipped_certificate_skeptic_round4.md`, `zero_buffer_clipped_moment_third_round3.md`, and `zero_buffer_weaklaw_third_round3.md` in this directory. They separately reconstructed the transfer before comparing this proof; the third review’s Hamburger-determinacy scope clarification is incorporated above.
