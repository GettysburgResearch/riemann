# Independent round-two reconstruction: fixed weighted Selberg errors

Reviewer: li_advocate. Date:2026-11-17. Status: the proposed extension holds for every fixed integer q≥1; a sharper explicit local remainder is available. These are elementary consequences of the existing fixed-profile argument; no historical or publication novelty is claimed. The q=1 qualitative necessary-simplicity statement is prior work of Wei–Wu2022, Proposition1.9.

## Definitions and result

For integers N≥2 put b_(n,N)=μ(n)(1−log n/log N), V_N(s)=∑_(n≤N)b_(n,N)n^(−s), C_N=∑_(n≤N)b_(n,N). On Re(s)=1/2 define

d_(q,N)²=(1/(2π))∫_R |1−ζ(1/2+it)V_N(1/2+it)|²/|1/2+it|^(2q) dt.

This is the full, prescribed-array error, not the infimum over coefficient choices or a truncated-height integral. For every fixed integer q≥1,

d_(q,N) ≥ |C_N+2|/sqrt(N) − [4π²/(3^q sqrt(5))]N^(−5/2).             (W1)

Consequences:

* d_(q,N)→0 along the full sequence implies RH and simplicity of every nontrivial zero.
* If a critical-line zero ρ has multiplicity m≥2, then

limsup_(N→∞) d_(q,N)/(log N)^(m−2) ≥ m/[|ρ|²|ζ^(m)(ρ)|].             (W2)

In particular a double zero gives limsup d_(q,N)≥2/[|ρ|²|ζ″(ρ)|]>0; multiplicity m≥3 gives limsup d_(q,N)=∞.
* If a nontrivial zero has Re(ρ)>1/2, then limsup d_(q,N)=∞. By functional symmetry, any failure of RH supplies such a zero.

All these constants are independent of q for fixed q; this does not assert uniform control for q varying with N. The local error bound in(W1) is explicit in q.

## Hilbert space, Mellin convention, and integration operator

Use H=L²((0,∞),du/u²) and M f(s)=∫_0^∞ f(u)u^(−s−1)du on Re(s)=1/2. Substitution u=e^x gives the usual Fourier transform of e^(−x/2)f(e^x), so Plancherel has normalization1/(2π).

Define I f(u)=∫_0^u f(v)dv/v. The integral is well defined for every finite u and f∈H, because its absolute value is at most sqrt(u)||f||_(H;(0,u)). In logarithmic coordinates I is convolution by exp(−x/2)1_(x≥0), an L¹ kernel of norm2. Thus I:H→H is bounded with norm at most2, and M(If)(s)=Mf(s)/s in the L² boundary sense. For the concrete functions below the classical integral also converges absolutely in0<Re(s)<1 and Fubini verifies the identity directly. The lower integration endpoint0 is fixed; no arbitrary constant of integration may be added. Iterating gives the multiplier s^(−(q−1)).

Let χ(s)=2^s π^(s−1)sin(πs/2)Γ(1−s), so ζ(s)=χ(s)ζ(1−s) and |χ|=1 on the critical line. The boundary map

(U_q F)(s)=χ(s)[(1−s)/s]^q F(1−s)

is a unitary involution: reflection preserves the boundary measure, both factors have modulus1, and χ(s)χ(1−s)=1. Integer powers require no branch convention.

Set W_N(u)=∑_(n≤N)b_(n,N){nu}/n and g(u)=−sin(2πu)/π. Both lie in H: they are O(u) near0 and bounded at infinity. The convergent fractional-part and sine–Gamma Mellin integrals give

M W_N(s)=−ζ(s)V_N(1−s)/s,
M g(s)=−χ(s)/s.

Apply U_q to F_(q,N)(s)=[1−ζ(s)V_N(s)]/s^q. Direct substitution gives

U_q F_(q,N)(s)=[χ(s)−ζ(s)V_N(1−s)]/s^q
             =M[I^(q−1)(W_N−g)](s).

Consequently the exact identity is

d_(q,N)=||I^(q−1)(W_N−g)||_H.                                    (W3)

It also proves finite norm for every N,q. Boundedness ||I||≤2 gives d_(q,N)≤2^(q−1)d_(1,N), but its inverse is unbounded; small weighted error cannot simply be converted back to small q=1 error.

## The shrinking interval survives every fixed integration

For0<u<1/N, {nu}=nu for every n≤N, so W_N(u)=u C_N. Since I(u)=u, the same identity holds for I^(q−1)W_N on that interval; the operator only uses values at v≤u.

Taylor's global remainder bound gives |g(u)+2u|≤(4π²/3)u³ for u≥0. The positive integral operator preserves pointwise majorants and I(u³)=u³/3, hence

|I^(q−1)g(u)+2u|≤(4π²/3^q)u³.

The H norm of (C_N+2)u on(0,1/N) is |C_N+2|/sqrt(N), and that of the error majorant is [4π²/(3^q sqrt5)]N^(−5/2). Restrict(W3) to this interval and use the reverse triangle inequality to prove(W1). No limit interchange, conditional sum, or assumption about ζ zeros is needed for this step.

For q=2 specifically, I g(u)=−Si(2πu)/π=−2u+(4π²/9)u³+O(u⁵). Thus the stronger |s|^(−4) weighting still preserves the same leading small-u obstruction; it does not remove multiplicity constraints for this fixed array.

## Full-sequence Mellin pole argument and quantitative constants

Let Ψ(x)=∑_(n≤x)μ(n)log(x/n). At integers N, Ψ(N)=C_N log N. For N≤x<N+1 the difference is log(x/N)∑_(n≤N)μ(n)=O(1), so full-sequence bounds transfer to real x.

For Re(s)>1, absolute convergence gives

∫_1^∞ Ψ(x)x^(−s−1)dx=1/[s²ζ(s)].                                (W4)

If limsup d_(q,N)<∞, then(W1) gives Ψ(x)=O(sqrt(x)log x). The integral therefore extends analytically to Re(s)>1/2, forcing zero-freeness there and hence RH. This proves the off-line-zero limsup-divergence conclusion.

If d_(q,N)→0, one obtains Ψ=o(sqrt(x)log x). At a critical-line zero ρ of multiplicity≥2, split the Mellin integral at a large fixed A to obtain

ε²∫_1^∞ Ψ(x)x^(−ρ−ε−1)dx→0 as ε↓0.

Indeed the tail is bounded by an arbitrary small constant times ε²∫_1^∞log x·x^(−ε−1)dx, which equals that constant. The initial finite integral vanishes after multiplication by ε². But(W4) has a nonzero pole coefficient at such a zero, a contradiction. This proves necessary simplicity for full convergence.

More generally, if D=limsup d_(q,N)/(log N)^(m−2)<∞, then |Ψ(x)|≤(D+o(1))sqrt(x)(log x)^(m−1). Analytic continuation again excludes off-line zeros. Multiplying(W4) at s=ρ+ε by ε^m yields a pole coefficient of modulus m!/[|ρ|²|ζ^(m)(ρ)|], while the absolute integral is bounded in the limit by D(m−1)!, because

ε^m∫_1^∞(log x)^(m−1)x^(−ε−1)dx=(m−1)!.

This proves(W2), with the infinite-D case automatic. The statement for m≥3 follows since the logarithmic denominator diverges.

## Subsequence quantifier: RH survives, simplicity is not established by this method

The shrinking-interval argument alone controls Ψ only at the selected N if d_(q,N)→0 along a subsequence. It does **not** supply the full real-x little-o estimate needed to exclude multiple boundary zeros. Therefore the simplicity statement above must not be rewritten with liminf d_(q,N)=0 on the basis of this proof.

One can nevertheless show that liminf d_(q,N)=0 forces RH, separately. Define the analytic Hardy function

A_(q,N)(s)=(s−1)[1−ζ(s)V_N(s)]/s^(q+1), Re(s)>1/2.

The ζ pole at1 is canceled, and its boundary norm is exactly d_(q,N), since |s−1|=|s| there. To check H² membership without relying on boundary norms alone, write

φ(s)=(s−1)ζ(s)/s²=1/s−[(s−1)/s]J(s),
J(s)=∫_1^∞{x}x^(−s−1)dx.

The integral represents a Laplace transform of the bounded function {exp(t)}1_(t≥0). On Re(s)≥1/2 its H² norm is finite by Fourier–Plancherel, and it is bounded in modulus by1/Re(s). The factor(s−1)/s is bounded by1 in this half-plane. Hence φ∈H²∩H∞. Now A_(q,N)=(s−1)/s^(q+1)−φ(s)V_N(s)/s^(q−1) lies in H² for every fixed integer q≥1, since V_N and1/s are bounded analytic multipliers there.

At a zero ρ=β+iγ with β>1/2, A_(q,N)(ρ)=(ρ−1)/ρ^(q+1), independent of N. The H² point-evaluation inequality gives the finite-N bound

d_(q,N)≥sqrt(2β−1)|ρ−1|/|ρ|^(q+1)>0.

Thus even a vanishing subsequence excludes off-line zeros. This does not prove or disprove a corresponding subsequence simplicity statement; that question is left open by the inspected argument. Bounded full-sequence errors are stronger and force the limsup conclusions already proved.

## Source anchoring and prior-art limits

Inspected primary source: Fei Wei and Dongsheng Wu, *A characterization of the zero-free region of the Riemann zeta function and its applications*, Expositiones Mathematicae40(4) (2022),961–993, DOI10.1016/j.exmath.2022.07.004. Local source `sources/selberg_round2/zero_free_2022.pdf`; authoritative author/institute copy https://bimsa.net/doc/publication/1424.pdf. Specifically inspected pp.6–7 Problem1, Proposition1.9 and Theorem1.10; pp.27–29 Proposition1.9 proof and Remark5.8. This is a targeted proof inspection, not an audit of every theorem in the work.

Conrey–Myerson, arXiv:math/0002254v1, pp.2–3 Proposition1 and the W_N definition, supplies the fractional-part norm context; this review inspected those passages. Ehm, arXiv:2405.06349v2, p.1 equations(1)–(2) and following fixed-coefficient discussion, explicitly studies q=1,2. That passage distinguishes an optimized criterion before discussing a fixed Selberg array. The result above shows that q=2 full fixed-array convergence also entails simplicity, so stronger height downweighting alone cannot evade that necessary condition. This is not a verified mathematical error in Ehm's paper and does not refute its arbitrary-coefficient weighted criterion.

Focused primary-source web searches covered weighted Selberg/Nyman/simple-zero formulations and the exact Wei–Wu title on2026-11-17. They located the q=1 source but did not establish exhaustive priority for the all-q corollary. No novelty claim is made. The weighted extension is an independently checked reusable consequence of the same argument, pending a complete literature search.
