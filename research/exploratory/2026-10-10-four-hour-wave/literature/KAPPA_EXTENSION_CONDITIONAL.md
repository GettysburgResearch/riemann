# A conditional corollary from an enlarged plain-moment parameter range

Status: independently reviewed written source-qualified conditional deduction. No new unconditional result or compiled analytic theorem is asserted.
Scope: finite-order Hecke L-functions over K=Q(sqrt(-3)) and their Dirichlet transfer; strict half-plane Re(s)>0.87495703. RH remains open.
What ran: frozen source comparison, proof-interface inspection, exact rational polynomial certificates, and byte-identical normal/optimized Python replays.
Smallest remaining gap: independently rebuild the imported analytic proofs. The parameter-range adapter received a separate complete Section 18 source review; the coordinator reviewed Sections 4–5 against the frozen Liu and PR #910 transport/Euler interfaces. The imported OpenAI and Liu analytic proofs have not been rebuilt in this wave.

## 1. Statement, dependencies, and prior work

Write S for OpenAI's September 30 manuscript at [fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex). Its SHA-256 is `42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3`. This is byte-identical to the imported S in repository PR #910, commit `670a76c1a3a8f325c43c1755b1cfc24d313a3e3c` (the imported OpenAI commit there is `adc7f1241b42e322a6451854ab7e4b4c146bf78a`). Write L for [Baiying Liu's October 8 manuscript](https://github.com/liubaiying101/Slightly-improved-zero-free-half-planes-for-the-quasi-Riemann-hypothesis/blob/7d10420de90efa2f082a06a342fc7accbd57ab37/Slightly%20improved%20zero-free%20half-planes%20for%20the%20quasi-Riemann%20hypothesis.pdf), frozen at `7d10420de90efa2f082a06a342fc7accbd57ab37`.

**Conditional corollary.** Assume the analytic inputs of S and the imported theorem of L with their exact arithmetic conventions, coefficient classes, masks, all-height bounds and uniformity. Then, subject to the adapters proved below, every finite-order Hecke L-function over K and every Dirichlet L-function has no zero in

    Re(s)>B,  B=87495703/100000000=0.87495703.

The principal pole at s=1 is allowed. This is an implication from imported analytic results, with a new written parameter adapter; it is not an independent verification of those results.

PR #910 already supplies a variable-geometry low estimate, enlarged principal Euler domain, contour transport, and a fixed-kappa=3/4 improvement to 139999/160000. It also identifies the exact geometry ceiling later attained by L. The low-side and Euler adapters used below are credited to that work and L, rather than claimed anew. The added deduction is the enlargement of S's **plain** fourth-moment parameter range, retaining its actual capacity. This is different from PR #910's unproved fourth moment for the standalone inverse-Mobius sum.

The imported dependency ledger is precise:

| Input | Frozen locator | Use |
| --- | --- | --- |
| Imported family bound | L, Theorem 21.1 and Section 26 | beta_* <= B_L=(1507-2sqrt(921))/1653. |
| Kernel, masking, reflection, finite Poisson and centered induction inputs | S, Section 18, `lem:plain` proof; its cited reflection and local transform lemmas | The parameter-free analytic identities and bounds in the plain-moment proof. Their numerical kappa inequalities are replaced explicitly below. |
| Global logarithmic control and ray-prime estimates | S, `lem:logarithmic-control`, `old-eq:3.4`–`old-eq:3.5` | Prime bound for s_kappa=(1+kappa)/2 >= beta_*. |
| Same-character inverse/plain detector | S, `prop:detector-witness` | Saturated pair at common character and height, with unchanged zero extensions. |
| Marked inverse and no-slot amplification | S, `lem:marked`, `lem:inverse-amplification` | Inverse capacities, long counts and zero-capacity handling. |
| General low estimate | PR #910, `GEOMETRY_PERTURBATION.md`, Lemmas 4.1–4.2; L, Section 22 | Compensated rescaling with the positive-part loss retained. |
| General Euler, principal and physical transport interfaces | PR #910, Lemmas 3.1–3.5; L, Sections 17–20 | General positive lengths and boundary >=437/500; finite internal height costs. |
| Continuation and Dirichlet transfer | S, `lem:continuation-criterion`, `prop:hecke-dirichlet-transfer`; L, Proposition 3.1 and Corollary 14.1 | Convert a family-uniform positive exponent margin to the stated zero-free half-plane. |

No theorem for arbitrary row-dependent prime coefficients, growing ray conductors, unmasked rows, or a different physical probe is assumed.

## 2. Extended plain fourth moment

**Lemma.** In S, `lem:plain`, replace the interval 3/4<=kappa<=1 by 13/18<=kappa<=1 and leave every other hypothesis and conclusion unchanged. In particular, for live slots keep

    n_1+n_2+6 kappa z <= M,
    beta_* <= (1+kappa)/2  when kappa<1.

The same finite-ray coefficients, disjoint underlying prime supports, common puncture masks, inducing-character exclusion outside the fixed group Theta, and fixed-slot-count quantifiers are required. The slot mesh is uniform in the enlarged compact interval.

**Proof adapter.** Use S's proof in its stated order. The following enumerates every use of the numerical lower kappa bound in that proof, including the hidden stronger margins in its Lean geometry helpers.

### 2.1 Prime estimate and terminal width

For kappa<1, move the smooth von Mangoldt contour to s_kappa+e, e>0, where s_kappa=(1+kappa)/2. The retained hypothesis s_kappa>=beta_* makes this line strictly zero-free. Its values lie in a fixed compact real range, s_kappa>=31/36, so the global logarithmic-control input applies with the same kind of uniform constants. No zero is assumed absent merely because the new parameter is smaller.

The coefficient expansion is unchanged. If an inducing character psi outside Theta became principal after multiplication by a coefficient character in Theta, then psi belonged to Theta, a contradiction. Prime-power errors, division by log(Py), bounded-scale counting, natural-radical deletion and normalized twist derivatives are as in S. They give

    |Q_omega|^2 <= C Z^(kappa z+epsilon_1) p_j(W)^b (1+|omega|)^h.

The squared normalization exponent is still 2s_kappa-1=kappa. At kappa=1 use absolute counting, exactly as S. Contour displacement costs 2ez, independent of derivative order.

At a terminal width M<=rho, positivity of the plain lengths gives 6kappa z<=M. Thus

    z<=3M/13,  kappa z<=M/6.

S's auxiliary bound z<=2M/9 is replaced by the first bound; its terminal loss uses only the second. The extra positive-slot loss remains at most rho/6. Zero-slot reflection and its padded core are unchanged.

### 2.2 Comparison reflection, including clipped deleted columns

Put lambda=6kappa-1, so 10/3<=lambda<=5. In the comparison region A>=5M/6 and A+lambda z<=M,

    lambda z <= M/6,  z<=M/20.

For the strict region A>5M/6, the inequalities for z are strict. Both comparison lengths are at least M/4 because A-z>=5M/6-M/20>M/2. One reflection has total length at most

    A_comp <= 3M/2-A+2z+xi <=23M/30+xi,
    A_comp+lambda z <=5M/2-2A+2z+xi <=14M/15+xi.

Their required boundaries are 5M/6 and M. Each therefore retains margin M/15 before xi. S already chooses xi<rho/30, so for M>rho a margin at least M/30 remains. Nothing in the comparison calls a live moment with an inadmissible capacity.

The formal deleted-column helpers sometimes retain the stronger constants M/21, 16M/21 and 13M/14. They must be weakened, rather than invoked unchanged. Here is the needed clipped version. Suppose

    0<=short<=M/4,  0<=z<=ell<=M/20,
    lambda ell<=M/6,
    short+max(0,along)+z>5M/6,
    reflected<=max(0,M-along+xi),  xi>=0.

The high inequality forces along>0; otherwise its left side is at most 3M/10. If M-along+xi>=0, then

    reflected+short+z
      < M/6+2short+2z+xi <=23M/30+xi.

Adding lambda z<=M/6 gives reflected+short+6kappa z<=14M/15+xi. If the maximum is zero, reflected<=0 and both upper bounds follow even more strongly from short<=M/4, z<=M/20 and lambda z<=M/6. Hence every scale in the reflected window is admissible when xi<=M/30. The same monotone deletion argument handles the branch already at or below 5M/6. This covers S's actual max-with-zero lengths, rather than reasoning only about formal unclipped scales.

In the frozen formal source the required replacements occur at `Moments/ReflectionRetainedLength.positive_slot_width_drop` and `Energy/ReferenceState`, `ReferenceLowBranchGeometry`, `ReferenceLowWindow`. The current upstream declarations still require 3/4; this note supplies their mathematical adapters. The separate `../xi/formal/LowKappaCapacity.lean` compiles the real comparison and clipped-column inequalities, without formalizing the analytic interfaces that supply their hypotheses.

### 2.3 The two transforms and greedy live-slot removal

All mask-erasure, reflection, finite Poisson, allocation, Gaussian and exceptional-row identities in the remaining proof are independent of the lower kappa bound. Their capacity ledger is affine in lambda. For a natural child, define the actual defect after support and clipping operations as in S,

    F_act=(A_act-M'_act+lambda z_act)_+.

Removing live length d decreases A_act+lambda z_act by (1+lambda)d=6kappa d, while the prime bound costs kappa d in the squared exponent. The cost/defect ratio remains exactly 1/6. Select the first prefix reaching F_act/(6kappa), or remove every slot when its total is smaller. The overshoot is at most one mesh unit, hence

    kappa d <= F_act/6+kappa eta <=F_act/6+eta.

This operation remains well-defined since kappa>=13/18>0. The support and boundary defects are included before this prefix is chosen. There is one prefix per actual child, and no loss proportional to the number of removed slots.

Every affine perturbation in the ledger is still bounded by

    |Delta M|+|Delta A|+5|Delta z|,

because 0<=lambda<=5. Thus the same numerical aggregate Lipschitz constant C_* works after enlarging it for the fixed finite number of operations. Exceptional centered cancellation keeps its formal raw scales and common polynomial-size radical; it does not erase row zeros or apply a supremum to an exceptional centered difference.

### 2.4 Finite induction, mesh and all-height uniformity

Use exactly S's order: all zero-slot width bands first, then positive-slot bands; within a band, the uncentered stage precedes its centered comparison. Every nonterminal child drops nominal width by sigma, and aggregate support errors smaller than sigma/2 leave its earlier band. The depth remains D=2+ceil(2M_max/sigma). Comparison margins proved above prevent same-band cycles.

Choose rho,sigma and padding delta_pad before the slot count, so

    rho+delta_pad+rho/6+3sigma+5sigma/3 <epsilon/4.

Then choose xi,eta,epsilon_0 with S's bounds `old-eq:2.1i`, including xi<rho/30. These comparisons use only the enlarged compact interval, kappa<=1, lambda<=5 and the already established reflection margins. Fix the slot count, arithmetic data and support boxes only afterward. Their aggregate logarithmic widths H_N enter the eventual threshold log Z>=C H_N/xi and constants, not a multiplied exponent loss.

The per-depth envelope remains

    E_d=T_term+(d+1)C_*(eta+xi+epsilon_0).

One terminal loss occurs on a branch. The greedy step contributes one eta; common weighted Fourier measures retain their already extracted counting mass. Uniform Euler derivatives of full-product radial kernels avoid any Z^(Jxi) loss when the required internal derivative order J increases. The prime bound's polynomial twist-height factor is integrated at a fixed finite seminorm order. Reflection acts on at most two plain factors with fixed gamma shape, independently of kappa.

Choose the finite kernel, reflection, prime and terminal height/seminorm orders backward through the finite depth, exactly as the end of S's proof. Increasing those orders changes constants and the eventual threshold, not the exponent budget. The final external tail order lies outside that propagation and is chosen last. S's argument therefore retains its fixed polynomial height cost uniformly in kappa in [13/18,1]. This proves the adapted moment, conditional on the unchanged analytic identities and estimates of S. No stronger moment class has been introduced.

## 3. Actual-capacity detector count

For the corollary fix kappa=149983/200000 and c=1/(6kappa). Then 2/9<c<3/13. The inverse capacity stays z_I(r)=(1-r)/2. The extended plain moment gives z_P(m)=c(1-2m), applied to **two** copies of the plain witness, at the same character/height as the inverse witness. Keep all original physical masks and ray coefficients and the whole-product conjugation used by S.

Let alpha=5/6, delta=2a-1, x=q/delta in [0,1/2]. The ideal inverse and plain savings are

    F_I(r)=x+(1-x)r,
    F_P(r)=2cx+(2-4cx)(t-r).

The plain count decreases in the actual m, since its derivative is -2delta+4cq<=delta(-2+2c)<0. Thus m>=t-r-O(epsilon) permits the stated substitution. Write

    A_x=2-4cx, D_x=3-x-4cx, P_x=A_x(1-x),
    r_*(t)=[A_x t+(2c-1)x]/D_x.

D_x>=5/2-2c>0. The exact crossing geometry is:

    r_*(3/2)=1,
    r_*(1) decreases in x,
    min r_*(1)=(3-2c)/(5-4c)>=23/37,
    1/3 <= t-r_*(t) <=1/2.

For the lower inverse bound the difference is (18c-4)/[37(5-4c)]>=0. For the lower plain length,

    1-r_*(1)-1/3 = x(1-2c)/(3D_x)>=0.

Use the plain moment for r<=r_*(t) and the inverse moment for r>=r_*(t), except at small-capacity neighborhoods. The inverse strict width conditions retain the margin 2r-1>=9/37, after the fixed capacity decrement. Its requested length is at most 7/37. The plain side has m>=1/3-O(epsilon), so its requested length is at most c/3+O(epsilon)<7/37. Thus the same prime-supply hypothesis suffices. No new character-independent or row-dependent coefficient is used.

At zero inverse capacity use S's no-slot sixth-power amplification, uniformly even as r approaches one; at zero plain capacity use the no-slot plain estimate. If r>=1 the original long exponent is unchanged. Hence the common short and long counts are

    R_short(t)=1-delta+delta P_x/D_x (3/2-t),
    L(t)=1-delta+(alpha-delta)(t-1).

Their balance occurs at t=1+delta P_x/(2J), J=(alpha-delta)D_x+delta P_x. Since delta P_x<=J, this t belongs to [1,3/2]. The balanced count is

    R_c=1-delta+(alpha-delta)delta P_x/(2J).

J>0, P_x<=D_x, and 1-delta<=R_c<=1. No `Delta/4` penalty remains: it came from replacing an actual capacity by its kappa=3/4 baseline, whereas the actual chosen capacity is retained here. Mesh and capacity-decrement losses can be made arbitrarily small.

## 4. Geometry, low estimate, Euler domains and exact signal

Choose the fixed rational tuple

    ell=12512891/75000000, b=1542571/12500000,
    lx=(1-b-ell)/2, ly=(1+b-ell)/2,
    h=(1+b+3ell)/2, M=1-ell,
    B=11/12-ell/4=87495703/100000000.

Keep the physical compensated expression, local correction and prime normalizer of S, instantiated at these lengths. Its principal Mellin exponent is

    C(s)=lx/2+s-1+h/6=s-(4+b)/6.

In particular C(B)=lx/2+b/12=750891/4000000. The change in b changes C and must not be hidden by keeping the original constant 11/16.

The source-certified geometry gates are all strict: lx>ell, ly>ell, ly-ell-11b/6>0, 1-3ell>0, ell<1/5, b>0, lx>b+ell, ly<1, ell/h>1/5>7/37, and 5ell>h. Exact values for the operative reserves appear in `kappa-candidate-certificate.json`; they are verified by `check_kappa_candidate.py`.

The shared low adapter from PR #910 and L retains the rescaled subset of length d before estimating it. Its completed row norm is bounded by

    Z^[M'+(5ell-1+d)_+/4+epsilon], M'=M-2d.

The Gram and Cauchy steps give unscaled excess (5ell-1+d)_+/8. Physical tuple counting and compensating rescaling contribute -d, so the total excess is

    -d+(5ell-1+d)_+/8 <=0  (d>=0, ell<1/5).

Thus the same independently defined physical expression has direct bound |J_eta(Z)|<<Z^[C(B)+epsilon]. This is the proved variable-geometry bound of the cited prior work, not a continuity assertion about the whole proof.

B>437/500, so the enlarged principal box of PR #910 and L applies. Its good-prime defect exponents, row-prime boundary estimates and controlled rational denominators give a holomorphic quotient-free full correction. On the principal residue, where division is justified, G_p/H_p=-1+O(Np^[-437/500]). The associated H_eta is holomorphic on Re(s)>437/500 and within 1/2 of one after the same fixed pre-target cutoff. In particular it has no zeros on Re(s)>B.

Choose a fixed even slot count K and equal slot lengths ell/K, with disjoint compact annular windows before arithmetic masks. The fixed-ray prime theorem gives a nonzero eventual normalizer A_T(Z) of size (log Z)^(-K). For any 0<mu<(437/500)ell/K, the exact principal residue is

    H_eta(s) Z^(ell/6) A_T(Z) [1+O(Z^(-mu))].

Every contour uses this same full correction and same excluded set. The principal remainder saves ly/20, h/600 and mu, exactly as the shared interface. Principal targets are permitted because their reciprocal has a zero, rather than a pole, at one. The physical average and signal remain independent of the auxiliary height cutoff.

## 5. All physical row ranges and continuation

Under a contradiction beta_*>B, the prior imported theorem gives beta_*<=B_L. Exact rational isolation of sqrt(921) verifies

    B_L <(1+kappa)/2,  B<B_L.

Thus the extended moment's prime hypothesis is supplied by a **previous** theorem. There is no assumption of the conclusion B and no simultaneous fixed-point bootstrap. The dynamic bin ceiling delta<=2beta_*-1<kappa<alpha is valid; the scalar certificate covers the larger rectangle 0<=delta<=alpha anyway.

At the central row scale the transported high exponent relative to C(B) is

    E=-1/4+b/6+5ell/4+(1/2+ell)delta+ell x delta-h(1-R_c).

Set v=1/2-x and Q=2J(-E). Exact expansion gives Q=A(v)delta^2+D(v)delta+G(v). Every coefficient of A and of Disc(v)=4A(v)G(v)-D(v)^2 is strictly positive, including Disc(0). The complete-square identity gives

    4A Q=(2A delta+D)^2+Disc >0.

Since J<=5/2, A(v)<=A(1/2) on the rectangle, and Disc(v)>=Disc(0), the exact uniform reserve is

    -E >=560828536677742722737/60751889795319776946000000000 >10^(-9).

For 1/2<=d<=h the transported exponent is E+(d-h)(R_c+delta/2-17/50). Its slope is at least 1-delta/2-17/50>=4/25 and at most two. Hence its maximum is at h; extension to h+zeta costs at most 2zeta. The strict reserve permits a fixed positive zeta, chosen below a fixed fraction of 10^(-9) and below 5ell-h, so prime supply remains available.

The lowest class uses delta_0=1/50 and R=1; its reserve is

    -[-1/4+b/6+5ell/4]-(1/2+3ell/2)/50 >0.

Intermediate rows use the unchanged no-prime count R=76/75-2delta/3. Their maximum at d=1/2 is bounded by

    [(225ell+50-75b)delta+78ell-49b-73]/300.

This is affine in delta, and the checker verifies strict negativity at both 1/50 and 5/6. Small rows retain reserve ly/2-13h/75-2/100>0, directly relative to C(beta_*); the checker also verifies it after the conservative cost 7/8-B. Very large rows use the unchanged absolute contour: for fixed zeta>0 the coefficient of its far-right z line is -zeta, so an arbitrarily large fixed saving is available. All principal reserves above are positive.

Choose real contour, amplitude, rounding, moment, normalization and mesh losses within fixed fractions of the minimum of these reserves and the contradiction gap beta_*-B. Choose the mesh before K; then choose K large enough for the actual physical slot lengths (at most 2ell/K in row base) and spike rounding. All these real choices are target-independent. Fix the target and its exact bad-prime set afterward, then fix the finite internal Sobolev/seminorm and height orders from the adapted moment and the shared transport.

The transported estimate therefore has common m>0 and finite target-dependent A_eta,B_eta such that, for every external tail order N,

    |J_eta-f_eta| << Z^[C(beta_*)-m](1+T_1)^A_eta + Z^B_eta T_1^(-N).

Choose T_1=Z^tau_eta with tau_eta>0 below the detector allowances and m/[4(A_eta+1)]. Choose N afterward so B_eta-N tau_eta<C(beta_*)-m/2. Because the external order does not raise a previously fixed internal height degree, this gives |J_eta-f_eta|<<Z^[C(beta_*)-m/2].

The direct bound meets the continuation criterion with sigma_0=B, C(s)=s-(4+b)/6 and, for example, omega_0=(beta_*-B)/2. The principal factor is holomorphic and within 1/2 of one on that half-plane. The family criterion implies beta_*<=B, contradicting beta_*>B without requiring that its supremum is attained. The imported norm-pullback/finite Euler-factor transfer supplies all Dirichlet characters, with principal poles treated as above. This completes the written conditional deduction.

## 6. Review boundary and reproduction

The new mathematical step is a finite proof adapter for the original plain-moment induction. The recorded exact certificate verifies exponent identities, geometry and strict scalar reserves; it cannot authenticate Poisson, reflection, analytic continuation or the imported family theorem. No new source headline is reported as independently proved.

Run the checker with the prepared SymPy environment. All checks use explicit exceptions; normal and `python3 -O -B` output files were byte-identical under `cmp`. The `fourth_moment_extension_verified` field is true with the explicit scope “written proof adapter independently reviewed; imported analysis not rebuilt.” This field records the source review, not a conclusion proved by the scalar checker. `imported_bound_independently_rebuilt` and `rh_proved` remain false. Existing upstream Lean helpers still use the old interval. The separate compiled arithmetic generalization is now `../xi/formal/LowKappaCapacity.lean`: it proves the specific weaker reflection constants in Section 2.2, support-error margins, terminal prime cost and clipped deleted-column bounds, with explicit positive witnesses in the new interval. Its fifteen statements have only foundational axioms in the recorded compiler reports. These statements match the analytic normalization but do not formalize or instantiate its underlying moment, reflection and transport interfaces; their compilation is not a compiled zero-free theorem.
