# Third reconstruction: fixed logarithmic Möbius mollifier requires simple zeros

Reviewer: history/spectral agent. Date2026-11-17. Independent derivation below was produced from the parent-supplied claim and definitions, before reading the other agents' proof or Wei–Wu's proof. Parent subsequently reported the established prior result in Wei–Wu2022 Proposition1.9; no novelty claim is made. This is a scoped reconstruction, not a claim of error in an earlier paper.

## Exact definitions and norm

For N≥2 integer put

    a_(n,N)=μ(n)(1−logn/logN), 1≤n≤N,
    V_N(s)=∑_(n≤N)a_(n,N)n^(−s),
    d_N²=(1/(2π))∫_R |1−ζ(1/2+it)V_N(1/2+it)|²/(1/4+t²)dt.

Let

    W_N(u)=∑_(n≤N)(a_(n,N)/n){nu},
    g(u)=−sin(2πu)/π,
    Ψ(x)=∑_(n≤x)μ(n)log(x/n).

The measure in the real-variable Hilbert space is du/u² on(0,∞). Distinguish d_N from its square throughout.

## Direct unitary identity: no external local-limit theorem is needed for necessity

Use M h(s)=∫_0∞h(u)u^(−s−1)du. OnRe s=1/2, Mellin–Plancherel is unitary from L²(du/u²) to L²(dt/(2π)). For0<Re s<1,

    M{nu}(s)=−n^sζ(s)/s,
    M W_N(s)=−ζ(s)V_N(1−s)/s.

The fractional-part identity is the standard convergent Mellin representation of the analytically continued zeta function; the finite sum causes no interchange difficulty. Every W_N is O(u) near0 and bounded at∞, so belongs to the stated Hilbert space.

The sine Mellin integral gives

    M g(s)=(2π)^s Γ(−s)sin(πs/2)/π=−χ(s)/s,

where χ(s)=2^sπ^(s−1)sin(πs/2)Γ(1−s) and ζ(s)=χ(s)ζ(1−s). Both integral formulas converge on0<Re s<1. Thus

    M(W_N−g)(s)=χ(s)[1−ζ(1−s)V_N(1−s)]/s.

ForRe s=1/2, |χ(s)|=1 and |s|=|1−s|. Reflection t↦−t and Plancherel give the exact identity

    d_N=||W_N−g||_(du/u²).

Also ||g||²=1 by ∫_0∞sin²(au)/u²du=πa/2 for a>0. A separate theorem asserting local convergence W_N→g is useful for other arguments but is unnecessary for this necessary condition.

## Escape through the shrinking interval

If0<u<1/N, then{nu}=nu for every n≤N, hence

    W_N(u)=u C_N, C_N=∑_(n≤N)a_(n,N)=Ψ(N)/logN.

Therefore

    |C_N|/sqrtN=||W_N||_(0,1/N;du/u²)
                ≤d_N+||g||_(0,1/N;du/u²)
                ≤d_N+2/sqrtN,

using |sin(2πu)|≤2πu. Consequently d_N→0 implies Ψ(N)=o(sqrtN logN). This extends from integers to all realx because for N≤x<N+1,

    Ψ(x)−Ψ(N)=M(N)log(x/N), M(N)=∑_(n≤N)μ(n),

whose absolute value is≤1 by |M(N)|≤N and log(1+1/N)≤1/N. No unproved bound on the Mertens function was inserted.

## Mellin–Abelian obstruction to multiple zeros

ForRe s>1, absolute convergence and direct integration give

    F(s)=∫_1∞ Ψ(x)x^(−s−1)dx=1/[s²ζ(s)].

If Ψ(x)=o(sqrtx logx), the integral defines an analytic function onRe s>1/2. The identity continues there away from the removable behavior at s=1; it rules out any zero ofζ inRe s>1/2. By the functional equation this yields RH.

Letρ=1/2+iγ be any zero on the critical line and put s=ρ+ε, ε>0. With v=logx,

    F(ρ+ε)=∫_0∞ [e^(−v/2)Ψ(e^v)] e^(−εv−iγv)dv.

The bracket is o(v). Givenη>0, outside a finite interval it has modulus≤ηv, so

    limsup_(ε↓0) ε²|F(ρ+ε)|≤η,

because ε²∫_0∞v e^(−εv)dv=1 and the fixed compact part tends0. Lettingη↓0 gives ε²F(ρ+ε)→0. A zero of multiplicitym has

    F(ρ+ε)~m!/[ρ²ζ^(m)(ρ)]·ε^(−m).

For m=2 the scaled limit is nonzero; for m>2 its modulus diverges. Both contradict the Abelian limit. Thus all critical zeros must be simple.

## Quantitative version

Suppose D=limsup_N d_N<∞. The shrinking-interval bound gives

    A=limsup_(x→∞)|Ψ(x)|/(sqrtx logx)≤D.

The same Abelian argument, with an eventual bound(A+η)v in place ofo(v), gives

    limsup_(ε↓0)ε²|F(ρ+ε)|≤A≤D.

Analyticity inRe s>1/2 still follows from Ψ(x)=O(sqrtx logx), so this argument also forces RH if D is finite. In particular, ifρ is a double zero,

    limsup_N d_N ≥ 2/(|ρ|²|ζ″(ρ)|).

Ifρ has multiplicitym≥3, the Laurent expansion contradicts any finiteD, so limsup_N d_N=∞. These are necessary conditions for this fixed array and this full norm. They are not conclusions about the infimum over all possible mollifier coefficients or about truncated t-integrals.

## Adversarial checks and limits

- The factor s² belongs to the Mellin transform oflog(x/n), not the ordinary unsmoothed Mertens sum.
- The shrinking interval is(0,1/N), not(0,N); its mass is C_N²/N.
- The integer-to-real extension uses only |M(N)|≤N.
- A double pole cannot be hidden by oscillation e^(−iγv): its radial Laurent limit is nonzero.
- We used the exact Mellin image ofg and the functional equation, so did not assume an external weak/local convergence theorem to conclude strong convergence.
- RH plus simplicity is necessary; no sufficient condition from those two assertions alone is established here.
- Allγ andρ normalizations are classical ζ(s), not doubled xi zero ordinates.

Finding class: independently checked with no issue found in the reconstructed implication. Established prior art was reported before publication of this note; primary proof comparison is appended below after reading the source. No error claim concerning a published author follows.

## Primary-source comparison after saving the independent derivation

Actual full PDF was obtained from https://bimsa.net/doc/publication/1424.pdf and the relevant source portions were read: Fei Wei and Dongsheng Wu, *A Characterization of the Zero-Free Region of the Riemann Zeta Function and Its Applications*, Proposition1.9, printedp7, and its proof printedpp27–28 (plus the definition of(1.6) onp6). This is a partial source reading, not a whole-paper audit or an added full-reading count.

The original statement explicitly says convergence of the fixed Selberg sequence in(1.6) implies RH and simple zeros. Problem1 asks for the converse under RH alone; the following discussion explicitly notes that a positive answer would force RH⇒simplicity. Theorem1.10(2) also states that boundedness of(1.6) implies RH. Thus the qualitative necessary-simplicity conclusion and the boundedness⇒RH part are established prior art, not discoveries of this archive.

The primary proof uses the fractional-part function g_N(t)=∑a_(n,N){1/(nt)}, a unitary transform and the shrinking interval(0,1/N) to deduce ∑a_(n,N)=o(sqrtN); its F(x)=∫_1^xM(t)/t dt equals ourΨ(x). Its inequality(5.10) and radial double-pole contradiction agree with the independent Mellin–Abelian reconstruction. Our explicit targetg=−sin(2πu)/π and exact direct Mellin norm identity avoid leaving that unitary transform implicit. The quantitative limsup statements above were not stated in the inspected Proposition1.9 proof; they are elementary scoped extensions of the same estimates, with no novelty claim and no assertion of a comprehensive literature search.

Verdict after source comparison: no discrepancy found in the inspected necessary implication. No basis for characterizing the earlier introductory sentence in another paper as a mathematical error; conventions, historical context and later open-problem status need to remain distinct.
