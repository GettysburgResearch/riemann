# Independent review of AF2026 §7.2(d),(f): Christoffel mass versus one-sided mass

Reviewer: li_advocate. Date: 2026-11-17. This reconstruction was completed without reading the analytic agent's counterexample or draft. No main theorem of AF2026 is characterized as false.

## Primary source, exact scope, and context

PAPER-A004: Alpöge–Furman, arXiv2608.13637v2, 19 August2026. Actual source `sources/analytic/2608.13637.pdf/.txt`; printed p13 visually inspected, including §7.2(d),(f). Also read §1, Lemmas3.1–3.4, Proposition4.1's statement, and the §6 index regrouping to understand the claimed application. No new whole-work reading or global technical-audit classification is claimed.

The matrix G̃ is explicitly real symmetric/Hermitian, rather than positive semidefinite: off-line pairs contribute signature(1,1) blocks. The introduction normalizes d~N and tr G̃~N. On p13, observations(d)–(f) are expressly introduced as **informal**. Part(d) says that known normalized moments through2m give the sharp lower bound n_+(G̃)/d=at least1−Λ_m(0), with Λ called the Christoffel function of the moment sequence. No separate variational definition of Λ is supplied in that paragraph. Part(f) gives sine-Gram moments

    (y0,y1,y2,y3,y4)=(1,1,4/3,2,13/4),

and Λ2(0)=5/36, then the conditional13/18 simple-on-line proportion.

The literal interpretation using the ordinary minimum-square Christoffel function is false for general Hermitian moment sequences. A positive-root/Stieltjes qualification repairs it. The specific displayed sine-moment certificate is independently valid without requiring actual G̃ to be positive semidefinite.

## 1. What the ordinary Christoffel function always proves

For a probability measure μ onR with moments through2m, define

    λ_m(0)=min { ∫ p(x)^2 dμ(x) : p real, deg p≤m, p(0)=1 }.

With a positive definite moment Hankel matrix H_m=(y_{i+j})_{0≤i,j≤m}, this is1/(H_m^{-1})_{00}. It depends only on the truncated moment vector. For every feasible p,

    μ({0}) ≤ ∫p²dμ,

so μ({0})≤λ_m(0). Thus1−λ_m(0) is always a lower bound for μ(R\{0}), i.e. the normalized **rank** of a Hermitian matrix. It does not automatically bound μ((0,∞)), its positive index.

For m=1 with y1>0, the minimizer is p(x)=1−(y1/y2)x and is≥1 on x≤0. Hence q=1−p² is a one-sided indicator minorant, giving μ((0,∞))≥y1²/y2=1−λ1(0). The sign of y1 is already an important qualification; positive mean alone does not make the same reasoning valid for m≥2.

## 2. Exact eight-dimensional counterexample with positive mean and nonsingular moments

Take

    G=diag(−1,−1,−1,2,2,2,2,3),    d=8.

Its normalized moments are

    y=(1,1,7/2,7,37/2),     n_+(G)/d=5/8.

The Hankel matrix is

    H2=[[1,1,7/2],[1,7/2,7],[7/2,7,37/2]].

Its leading principal minors are1,5/2,27/8, all strictly positive. Minimization gives

    p(x)=1+8x/21−x²/3,
    ∫xp dμ=∫x²p dμ=0,
    λ2(0)=∫p²dμ=3/14.

Consequently the proposed ordinary-function positive-index lower bound would be

    n_+(G)/d ≥ 1−3/14=11/14,

whereas5/8<11/14, with exact gap9/56. This witness has positive normalized trace1 and a positive definite moment matrix; neither a zero-mean convention nor singular-Christoffel ambiguity explains it away. Its kernel polynomial has roots

    r_±=(4±sqrt163)/7,

one negative and one positive. In particular p(−1)=2/7, so q(−1)=1−p(−1)²=45/49>0; the tempting polynomial q=1−p² fails the required q≤0 on the negative half-line.

Exact standard-library rational checks are saved in `experiments/code/christoffel_independent_round3.py` and `experiments/results/christoffel_independent_round3.json`.

### The correct sharp moment value for this witness

The same moments have a canonical three-atom representation at0,r_−,r_+ with weights

    w0=3/14,
    w_±=11/28 ± 27/(14sqrt163).

All weights are positive and match moments0–4 exactly. Its positive mass is

    w_+=11/28+27/(14sqrt163) ≈0.544,

which is strictly smaller than1−λ=11/14 because the negative canonical node also has positive weight.

This w_+ is the actual sharp infimum over probability measures onR with these moments. Here is an explicit dual proof. Write a=r_−<0 and b=r_+>0, and put

    h=b+b(b−a)/(3b−a)>b,
    q(x)=A x(x−a)²(x−h),
    A=[b(b−a)²(b−h)]^{-1}<0.

Then q(0)=q(a)=0, q(b)=1, q'(b)=0. On x≤0, q≤0 directly from its factors. On x>0,

    q'(x)=A(x−a)[4x²−3(a+h)x+ah].

The bracket has one positive and one negative root because ah<0; its positive root is b. Thus q increases to1 at b and then decreases, so q≤1 on x>0. Therefore q≤1_{(0,∞)} everywhere. Its expectation is w_+, because the canonical quadrature matches degree4 and q equals the indicator at all three nodes. The primal canonical measure and dual polynomial coincide, proving sharpness. This is an elementary moment-problem calculation, not an asserted new result and not a zeta-zero configuration counterexample.

## 3. Exact repair: a positive-root qualification

Suppose H_m is positive definite, the normalized minimizer p_m has full degree m, and it has m distinct real nonzero roots r1,...,rm. The following proof supplies both a repair and a diagnostic.

Stationarity gives L(x p_m h)=0 for every polynomial h of degree≤m−1, where L is the moment functional. Divide a polynomial f of degree≤2m by x p_m to write f=x p_m h+r, deg r≤m. Lagrange interpolation of r at nodes0,r1,...,rm yields a quadrature exact through degree2m. Its weights w_i=L(ell_i²)>0, using H_m positive definiteness and the same exactness; w0=L(p_m²)=λ_m(0).

If all roots r_i are **positive**, then

    p_m(x)=product_i(1−x/r_i) ≥1,    x≤0.

So q=1−p_m² is a globally valid minorant of1_{(0,∞)}, giving μ((0,∞))≥1−λ_m(0) for every measure with those moments. The exact quadrature has all nonzero nodes positive and attains equality. In this case the ordinary Christoffel value really is the sharp one-sided bound.

If any r_i is negative, the same positive quadrature has negative-node mass, hence positive mass strictly below1−λ_m(0). The unrestricted formula fails. Under the displayed full-degree/simple-real-root conditions, positive roots are therefore necessary and sufficient for this particular formula to be a universal sharp positive-mass bound. Degenerate, missing-degree, or multiple-root cases require separate limiting treatment and are not silently covered.

A useful sufficient source of the positive-root property is a nondegenerate **Stieltjes moment sequence**: if the moments have a representing measure supported on[0,∞) with sufficiently many positive support points, p_m is an orthogonal polynomial for the positive measure x dμ, normalized at0. Its roots are positive. The sign-change proof uses orthogonality ∫x p_m h dμ=0 and does not require actual inspected G̃ to be positive semidefinite; only its limiting or exact moment vector must have this additional structure.

### Exact regular-case one-sided replacement, including mixed signs

Under the same full-degree/distinct-real-root hypotheses, the actual sharp positive-mass bound is

    B(y)=sum_{r_i>0} w_i,

where w_i are the positive canonical quadrature weights at0,r1,...,rm. This is the ordinary one-sided CMS form; its upper CDF at0 is w0+sum_{r_i<0}w_i. It is not generally w0 alone.

Here is an independent polynomial proof, including the global signs. If all roots are positive, use q=1−p_m² as above. If all are negative, q=0 and the canonical measure already has positive mass0. Otherwise sort r1<...<r_k<0<r_{k+1}<...<r_m. Hermite interpolation gives a unique polynomial q of degree≤2m with

    q(0)=0,
    q(r_i)=0 for i≤k,     q(r_i)=1 for i>k,
    q'(r_i)=0 for every i.

The interpolation is nonsingular: a homogeneous solution would have zeros at0 and double zeros at allm other distinct nodes, hence2m+1 zeros while its degree is at most2m.

The derivative q' already has m distinct zeros at the r_i. Rolle supplies another k−1 zeros between consecutive negative nodes, another m−k−1 between consecutive positive nodes, and one between r_k and0. These total2m−1 distinct zeros, saturating its degree. There are no other critical points, all these zeros are simple, and q' has positive sign on(0,r_{k+1}) because q rises there from0 to1 without a critical point. Alternating the signs across the ordered simple derivative zeros shows that each negative node is a local maximum of value0, each positive node a local maximum of value1, and the intervening critical points are minima. Beyond the outermost nodes the polynomial decreases away from these maxima. Consequently q≤0 on(−∞,0] and q≤1 on[0,∞).

Thus q is globally a minorant of1_{(0,∞)}. Its expectation, determined by the moments through2m, is exactly sum_{r_i>0}w_i, because the canonical quadrature matches those degrees and q agrees with the indicator at every quadrature node. The quadrature itself attains that positive mass. This proves both primal attainment and dual sharpness in the stated regular case, including on the noncompact real line. No unspecified SDP strong-duality theorem is required.

Missing-degree, colliding-root, or semidefinite moment cases remain outside this regular-case proof and should be handled by a separate limiting/degenerate analysis. No novelty is claimed for this reconstructed classical CMS argument.

## 4. The paper's particular sine-moment calculation is valid

For y=(1,1,4/3,2,13/4), exact minimization gives

    p(x)=1−7x/4+2x²/3,
    λ2(0)=5/36.

Its roots are (21±sqrt57)/16, both positive. More directly p(x)≥1 for x≤0 because both nonconstant terms are nonnegative there. Hence

    q(x)=1−p(x)²
        =(7/2)x−(211/48)x²+(7/3)x³−(4/9)x^4

obeys q≤0 for x≤0 and q≤1 for x>0. Thus every Hermitian G with these normalized moments, even an indefinite G, satisfies

    n_+(G)/d ≥ tr q(G)/d =31/36.

For asymptotically matching moments, the right side is31/36+o(1). No general CMS assertion is needed for this calculation.

The value is sharp over moment measures: put a=(21−sqrt57)/16 and b=(21+sqrt57)/16, with weights

    w0=5/36,
    wa=31/72+25/(24sqrt57),
    wb=31/72−25/(24sqrt57).

They are positive, sum to1, and match moments through4. The recurrence on nonzero nodes, whose sum is21/8 and product3/2, checks y2,y3,y4 directly. This measure has positive mass31/36.

The zero-side index charge in §6 gives, for its finite block truncation A=P1+Q',

    n_+(A)≤rank P1+n_+(Q')≤s1+s2+p≤(N+s1)/2.

Consequently s1/N≥2(n_+(A)/N)−1. With d~N this yields2·31/36−1=13/18 under the stated fourth-moment hypothesis. If moments are evaluated for A plus an operator-norm-small tail E, a threshold version avoids instability of the raw positive index: q(0)=0 and q is Lipschitz near0, so

    #{lambda(G)>δ}/d ≥ tr q(G)/d−Cδ.

Choose δ→0 with ||E||<δ and apply Lemma3.4 to A. This makes the transfer to the block count robust. This review does not separately verify the source's prime-side HL*(4) hypothesis or the numerical identification of the sine-Gram fourth moment; it verifies the stated implication from those four moment values and the existing index geometry.

## 5. Correct general optimization and SDP certificate

For arbitrary Hermitian moment data y, the sharp moment-class quantity is

    B(y)=inf { μ((0,∞)) : μ≥0, moments0..2m equal y }.

A universal polynomial dual lower bound is

    sup L_y(q),
    deg q≤2m,  q(x)≤0 for x≤0,  q(x)≤1 for x≥0.

This dual is not the unconstrained minimum-square Christoffel problem. Without additional compactness/duality hypotheses, this note asserts weak duality only; the explicit primal/dual witnesses above prove equality in the two inspected examples.

The polynomial constraints have an exact univariate SDP formulation. For t≥0 require

    −q(−t)=z_m(t)^T A z_m(t)+t z_{m−1}(t)^T B z_{m−1}(t),
     1−q(t)=z_m(t)^T C z_m(t)+t z_{m−1}(t)^T D z_{m−1}(t),

with A,B,C,D positive semidefinite, coefficient matching, and z_j=(1,t,...,t^j). The half-line sum-of-squares representation follows by applying real univariate factorization to the nonnegative polynomial p(u²) and separating even/odd square terms. Thus it is exact at the stated degree, rather than an arbitrary relaxation of polynomial nonnegativity. Rational feasible solutions provide independently checkable lower-bound certificates.

## 6. Classical source check and alternative readings

The actual primary text Gilboa–Peled, arXiv1407.2467v2, pp1–2, defines separate extremal functions

    overlineπ(x)=sup μ([−1,x]),
    underlineπ(x)=inf μ([−1,x)),
    λ(x)=sup μ({x}),

for measures on[−1,1] matching a prescribed finite moment vector. It states overlineπ−underlineπ=λ. This is the distinction relevant here: atom mass is the **width** between one-sided CDF extremals, not the upper CDF itself. Their compact-interval λ also includes the support constraint and is not automatically identical to the unrestricted Hankel minimum-square quantity. Only these classical introductory statements were inspected; the differential theorems were not audited, and the paper has a later2015 erratum whose content was not accessed.

Serious alternative interpretations of AF(d) are:

* If Λ was intended as the upper one-sided CDF extremal at0, then1−Λ is the sharp lower positive mass by definition, but that is not the ordinary Christoffel function; a definition and notation repair are needed.
* If the remark was implicitly restricted to the nonnegative sine-Gram/Stieltjes moment sequence used immediately in(f), the positive-root argument supplies the missing qualification. The numerical λ2=5/36 and resulting13/18 are compatible with that reading.
* If it is intended literally for all Hermitian normalized moment sequences, the exact eight-dimensional witness refutes that extension.

Classification: **missing or insufficiently stated hypothesis / source-notation ambiguity in an informal general remark**, supported by an exact counterexample to its unrestricted ordinary-Christoffel interpretation. No conclusion here invalidates TheoremsA/B, §3's rank–trace inequality, or the source-specific conditional13/18 implication.

The further all-moments-to100% sentence requires control of the limit λ_m(0), not just the first four moments. A standard sufficient route is moment determinacy of the nonnegative limiting law plus no atom at0, together with the positive-root quadratures; then their extremal atom weights converge to0 by tightness, moment preservation, and uniqueness. Neither those law properties nor a replacement proof of that all-k sentence was audited here. This is a concrete next source/lemma check, not a claimed counterexample to the sine-Gram law.

## Subsequent independent model checks

The original conditional-moment implication above treated the source sine moments as inputs. They have now been independently reconstructed in `sine_gram_fourth_moment_advocate_archived_round3.md`, including the all-distinct fourth-cycle integral0. The all-moment model-law prerequisites were separately established in `proposals/independent_campaigns/sine_gram_all_moments_round3.md` and THM-SG309: full expected model moment limits, Hamburger determinacy, and no atom at0. This resolves the stated model-law continuation task, while the actual arithmetic prime-side higher-moment asymptotics remain unproved.
