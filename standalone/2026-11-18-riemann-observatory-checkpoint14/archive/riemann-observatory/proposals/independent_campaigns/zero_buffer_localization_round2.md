# Candidate simplification: the limiting matrix proof needs no growing zero buffer

Status: independently proposed after original-source trace reconstruction; director adjudication accepted at scoped conditional-reconstruction level; see audits/adversarial_reviews/director_round3_adjudication.md. This is a proof-dependency/hypothesis weakening, not a new zero proportion, a proof of RH, or a claim of literature novelty.

## Source and precise objective

AF arXiv2608.13637v2 uses I'=[T−sqrt(T),2T+sqrt(T)) and proves ||E||_1=O(T^(-1/2)) in Proposition4.3. Its Theorem5.7 then transfers the prime-side Hilbert–Schmidt norm to the finite zero-side matrix. TheoremA, §6 pp11–12, uses the transferred Hilbert–Schmidt square, trace, counts and Lemma3.2. The printed proof contains no use of Lemma3.4's Weyl bound. The objective here is to determine the weaker tail estimate actually sufficient for that chain.

Take exactly the original real even C² compact window phi, with uniformly bounded supremum, a=||phi||²/L bounded below, and the same critical sampling h=2pi/L. Keep the same d=floor(T/h) sample grid. Let G_0 be the finite zero-side matrix formed using only zeros with Re gamma in I=[T,2T), counted with multiplicity. Let E_0 be the sum over all other nontrivial zeros. Set A=aL² and v_z=(hat(phi)(z−alpha_k))_{0<=k<d}.

**Claim under review:**

||E_0||_1=O(sqrt(X)),

trG_0=N(I)+O(sqrt(X)).

In particular, at X=T/(2pi), ||E_0||_HS=o(sqrt(N(I))) even though ||E_0|| need not be o(1). Consequently the same limiting simple-critical and distinct-zero constants follow from the original prime-side second moment and finite matrix inequality, with a weaker O(1/sqrt(logT)) convergence loss.

## Tail argument

For a complex vector v, ||vv^T||_1=||v||_2²: write vv^T=v(conjugate(v))^*, and a rank-one operator xy* has sole singular value||x||||y||. Hence

||E_0||_1 <= A^(-1) sum_{r outside I} m_z ||v_z||_2².

1. For exterior zeros at distance D<1 from I, there are O(L) of them. Fourier-series Parseval and |Im z|<=1/2 give

sum_{k in Z}|hat(phi)(z−alpha_k)|²
 =L integral phi(u)² exp(−2 Im(z)u)du
 <=C L exp(L/2).

The normalized contribution per zero is therefore O(sqrt(X)/L); the entire unit strips cost O(sqrt(X)).

2. For D>=1, the real-part decay |hat(phi)(z−alpha)|²<=C sqrt(X)|Re z−alpha|^(−4) and grid comparison give normalized finite mass O(sqrt(X)/(L D³)). The global multiplicity bound N(t,t+1)=O(log(|t|+3)) implies

sum_{r outside I,D>=1}m_z D^(-3)=O(logT)=O(L).

This remains true for negative or arbitrarily large ordinates: the shell sum is bounded by C sum_{j>=1}log(T+j+3)/j³=O(logT). Thus all distant excluded zeros cost O(sqrt(X)). The same bounds prove absolute nuclear-norm convergence of the infinite rank-one sum; termwise regrouping is justified.

The trace estimate is the independently reconstructed trace-localization lemma at U=0: interior complement tails and unit endpoint strips have the same O(sqrt(X)) total. The grid-floor endpoint is handled by D−h>=D/2 for interior D>=1; no false assertion that alpha_d lies outside I is needed.

## Why this weaker tail is enough

Write H=G_0+E_0 for the full prime-side matrix. Suppose the prime-side work establishes

||H||_HS²=R(psi)N+O(N logL/L), N~TL.

Then ||H||_HS=O(sqrt(N)) and ||E_0||_HS<=||E_0||_1=O(sqrt(T)). Therefore

| ||G_0||_HS²−||H||_HS² |
 <=2||H||_HS||E_0||_HS+||E_0||_HS²
 =O(T sqrt(L))=O(N/sqrt(L)).

No small operator norm is required for this inequality. It follows that ||G_0||_HS²=(R(psi)+O(L^(-1/2)))N.

For simple on-line zeros form P1 as in AF §6, but now only inside I, and Q'=G_0−P1. Let s1 be the number of simple on-line zeros, s2 the number of distinct multiple on-line zeros, and p the number of distinct off-line conjugate pairs. Then

rankP1<=s1, trP1<=s1, n_+(Q')<=s2+p,

s1+2s2+2p<=N.

Lemma3.2 gives s1>=4trG_0−2N−||G_0||²_HS, hence

s1>=(2−R(psi)−O(L^(-1/2)))N.

Its rearranged form gives3s1+4(s2+p)>=4trG_0−||G_0||²_HS. Subtract s1+2s2+2p<=N to get

Nd(I)>=s1+s2+p>=(3−R(psi)−O(L^(-1/2)))N/2.

These are exactly the original limiting constants. Dyadic summation gives the corresponding cumulative liminf forms; the finite initial segment is negligible. This conditional deduction does not independently establish the prime-side asymptotic or claim that all printed quantitative estimates are correct.

## Scope, possible failure modes and next step

The conclusion uses C²-type uniform real-part Fourier decay and bounded-window Parseval; the sharp indicator window without endpoint smoothing does not automatically satisfy the needed tail bound. It uses the true global zero count with multiplicity, not an assumed spacing condition. Its error O(N/sqrt(L)) is weaker than the paper's claimed O(N logL/L), so it cannot simply replace the growing buffer when retaining that sharper rate.

The director and an independently tasked skeptic are checking whether any hidden invocation of E=o(1), of Weyl, or of a buffer-dependent prime-side statement survives in §6. If none does, a reusable next result is an abstract trace/nuclear localization lemma for a conjugation-invariant multiset in a bounded horizontal strip with local multiplicity O(logT). Formalization should target that lemma plus the small-relative-Hilbert–Schmidt transfer, rather than claiming all numerical statements of the prose theorem have been compiled.

## Stronger version using a classical zero-free strip

Independent skeptic source check: BGSTB, arXiv2306.04799v1, §2 p6 (after(2.17)), explicitly states the Vinogradov–Korobov region

beta<=1−delta(t), delta(t)=c/[(log t)^(2/3)(loglog t)^(1/3)], t>=3,

for a suitable c>0. Guth–Maynard, arXiv2405.20552v2 §13.1 pp50–51, uses the same bound and cites Montgomery, Topics in Multiplicative Number Theory, Corollary11.4. This is a classical **external theorem used here**, not a claim that its original proof has been audited by this project. Choose a smaller monotone positive delta if needed so all displayed large-height assertions hold.

For all zero ordinates r in[T/2,3T], the functional equation also gives beta>=delta(3T). Thus |Im gamma|<=1/2−delta(3T). For T large take delta(3T)<=1/4. The Parseval integral has the sharper uniform bound

integral exp(2 eta u)du
 <=2 exp[(1/2−delta(3T))L], |eta|<=1/2−delta(3T),

because the reciprocal of1−2delta is at most2. The Fourier-tail bound gains the identical exponential factor. Repeating both near and distant localization therefore bounds the contribution of these heights by

C sqrt(T) exp[−delta(3T)L].

For all other heights, D=dist(r,I)>=T/2. The global zero-count shell bound gives sum m_r D^(-3)=O(L/T²), hence normalized far errorO(T^(-3/2)). These bounds are valid both for the nuclear tail and the trace remainder (the latter only involves interior zeros and needs no far term). Consequently

||E_0||_1
 <=C sqrt(T) exp[−c' L^(1/3)/(logL)^(1/3)]+O(T^(-3/2))
 =O_A(sqrt(T)L^(−A)) for every fixed A>0.

The same prime-side argument then gives

| ||G_0||_HS²−||H||_HS² |=O_A(N L^(−A))

for every fixed A, after adjusting A between the two estimates. Thus the zero-buffer simplification can preserve the source's prime-sideO(N logL/L) error if one imports this stronger classical zero-free input. The basic version needs only the critical strip and has the weakerO(N/sqrtL) rate. Keep those two hypothesis packages distinct.

This connection is exact: a zero-free strip improves the absolute Fourier sampling mass of off-line zeros exponentially in delta*L; that controls the discarded matrix relative to its sqrt(N) scale. It does not place all zeros on the critical line, improve the limiting proportion, independently verify the prime-side moment, or show any novelty relative to existing literature.
