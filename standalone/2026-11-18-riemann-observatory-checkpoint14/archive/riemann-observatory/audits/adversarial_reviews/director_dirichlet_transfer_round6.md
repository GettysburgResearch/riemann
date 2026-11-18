# Adaptive approximation for one fixed primitive Dirichlet character

The director independently reconstructed the transfer below, read the complete proponent proof and two independent adversarial audits, and inspected de Roton's original French definitions and Theorem2 on printedpp419–420. The matching lower bound is a published input whose exact application is checked; this is not a whole-paper audit of its proof. The upper construction adapts the independently reconstructed RST048v2 main argument. Its fixed-character publication priority remains unassessed. No generalized RH is proved.

## Exact theorem

Fix a primitive Dirichlet characterχ. Assume GRH for Lχ(s)=L(s,χ). With arbitrary complex coefficients and

    Δ_(N,χ)²=inf_{A(s)=Σ_{n≤N}a_n n^(-s)}
       (2π)^(-1)∫_R |1−Lχ(1/2+it)A(1/2+it)|²/(1/4+t²)dt,

one has

    lim_N (logN)Δ_(N,χ)²
      =Σ_{distinct nontrivialzerosρ ofLχ}mρ²/|ρ|².       (A)

All signed ordinates are used, without assuming they occur in± pairs. A central zero, if any, is included once with contribution4m². The sum converges. All constants may depend onχ. There is no conductor-uniform estimate, effective convergence rate, prescribed reciprocal-coefficient asymptotic or anchoring constraint. The conductor1 principal case is the source zeta theorem; belowχ is nonprincipal.

## 1. Analytic inputs follow from this character's GRH

Lχ is entire, with a zero-free simply connected half-plane Re s>1/2 under GRH and classical boundary nonvanishing. Its Euler logarithm fixes an analytic branch there. A crude fixed-strip polynomial bound and Borel–Carathéodory give |logLχ|≪χ,η log(2+|t|) on any smaller right strip. An inner disk about2+it has bounded Euler logarithm. Hadamard three-circles on intermediate disks improves the bound to Oχ,η(log(2+|t|)^θ),θ<1, at each fixed offsetη>0; Cauchy on a slightly smaller disk gives Lχ′/Lχ=o(log|t|). This proves both Lχ and1/Lχ are subpower on fixed right strips. The primitive functional equation and interpolation give |Lχ(σ+it)|≪χ,ε(2+|t|)^(max(1/2−σ,0)+ε) on fixed bounded strips and reciprocal subpower on a fixed left line1/2−δ. Compact heights there are nonzero. No assumption about ζ's RH is needed for a nonprincipalχ.

The completion Λχ(s)=(q/π)^((s+κ)/2)Γ((s+κ)/2)Lχ(s) obeys Λχ(s)=εχ overline{Λχ(1−bar s)}. This is symmetry across Re s=1/2 at the *same* ordinate. For Ξχ(w)=Λχ(1/2+w), e^(-i argεχ/2)Ξχ(it) is real. At a regular point of this axis, its logarithmic derivative has real part0. In the genus-one Hadamard expansion, the central factor contributesm0/w and the compensated noncentral summands have imaginary values on this axis. Their normal convergence therefore sets the real exponential constant to0. Foru>0,

    Re Ξχ′(u+it)/Ξχ(u+it)
       =Σ_γ mγ u/[u²+(t−γ)²].

For fixedη>0 the left side is(1/2)log(q|t|/(2π))+oχ,η(log|t|) by Stirling and the fixed-offset logarithmic derivative. To count zeros in[T−h,T+h], integrate this nonnegative sum over[T−h−κ0,T+h+κ0]. Each counted zero contributes at least2atan(κ0/η); the integral is(h+κ0+o(1))log|T|. Let height tend to infinity first, thenη→0 andκ0→0. Thus the fixed-window count is at most(h/π+o(1))log|T| at either sign ofT. This proves exactly the tiny fixed-window coefficient required by the adaptive proof. A separate explicit-formula/Beurling–Selberg proof in the proponent note gives the same bound with a fixed bandwidth error that can be chosen small enough. There is no shrinking-window claim.

Good-height selection averages Σγlog(1+η²/(t−γ)²) on each fixed interval. Its integral2πη and unit-window counts give the same small reciprocal exponent as the zeta argument, after choosingη relative to the fixed interval width. The gamma ratio has the favorable negative sign in the inverse's horizontal defect. Select the positive and negative mesh heights independently. The cell containing a central zero is an ordinary finite exception. With sourceD=e=10^-4,δ=10^-6, the resulting contour bound isCχT_C^e and k_C≤DlogT_C eventually; no conjugation symmetry of the ordinate set is used.

## 2. A retained left edge handles the different pole structure

PutF=1/Lχ andL=logN. Its reciprocal Dirichlet coefficients are μ(n)χ(n), bounded by1 in modulus. On the upward linea=1/2−δ define J0 andJN as source(94), with numeratorsF(z) andF(z)e^(L(z−s)). Cauchy and Perron give

    F′=Σ_CR_C′−J0,
    LV_N=LF+F′+Σ_CB_C+JN,
    V_N=Σ_{n≤N}μ(n)χ(n)n^(-s)(1−logn/L).

The right Cauchy edge vanishes by absolute convergence, while the horizontal edges tend to infinity at fixedN. All trivial zeros are to the left ofa. Using the finite rational identity then gives

    1−LχV_N=Σ_CE_C^(1)+Lχ(J0−JN)/L.

The retained edge has normOχ(1/L), because its kernel is(δ²+(t−y)²)^(-1), both reciprocal and critical-line multiplier are subpower, ande^(L(z−s)) has modulusN^(-δ). This accounts for the entire remainder. Unlikeζ, Lχ has no pole at1, and no anchoring is imposed, so there is no normalization at1 to pay for.

Telescoping all original cells including empties yields two high strips with h+=H+O(D) andh−=−H+O(D). Their indicator is1_{t>h+ or t<h−}. The source positive-kernel and logarithmic connector bounds apply separately, giving squared errors Oχ(H^-1+N^(2δ)L^-2H^(-1+4e)+N^(2δ)H^(-2+4e)). No reflected edge is substituted for an actual one.

## 3. Integer realization and the local constant transfer unchanged

The Newton principal-part and divided-difference proof uses real ordinates after centering, including repeated or zero ordinates. Replacingζ byLχ in the analytic quotient gives the same cancellation of the Cauchy factorial and simplex volume. All character dependence enters one fixed prefactor. The corrected error for any cell subsetB has squared norm≤CχL^-1Σ_{C∈B}(2+|τ_C|)^(-2+1/100).

Delayed profiles, H=N^(1/20),K=N^(3/20), and the collective correction

    Σ_{n≤N} n^(-s−1) Σ_{|τ_C|≤H}h_C(logn)
      [w_(k_C)(logn/L)−(1−logn/L)]

give an actual ordinary integer Dirichlet polynomial. Its squared quadrature errors retain powers−0.1499595 and−0.049958. Coefficients may be complex and may be nonzero at integers sharing ramified primes withq: the infimum permits them. Requiring them to retain the reciprocal coefficient pattern would change the theorem.

For each fixed finite set, expand into individual Laurent terms for the local far estimate, as in the explicit RST048 qualification. Atρ of multiplicitym, the top coefficientm!/Lχ^(m)(ρ) cancels the analytic multiplier atρ; the optimal profile(1−u)^m has local costm²/|ρ|². Lower orders and cross terms vanish at the scaled squared level. Fixed-profile quadrature still involves the regular functionζ(1+s−ρ)−1/(s−ρ), because sampling is over ordinary integers. Its logarithmic growth is unconditional; the multiplier bound now comes from this character's GRH. The use ofζ here does not import RH forζ.

Hold each repaired finite set fixed whileN→∞, control its complementary corrected tail by CχY^(-99/100)/L, and only then exhaust the fixed sets. For every such fixed set the source construction gives a genuine sequence of admissible polynomials. This proves the upper limsup in(A) without uniform growing Laurent constants. Unit-window counts imply convergence ofΣmρ²/|ρ|² by bounding the squared multiplicities in each unit window by the square of its total count.

## 4. Published lower bound in the exact norm

Anne de Roton, *Une approche hilbertienne de l'hypothèse de Riemann généralisée*, BSMF134(2006),417–445, DOI10.24033/bsmf.2516, defines B_F^λ andD(λ) onp419 and gives the multiplicity-squared lower bound in Theorem2 onp420. The inspected29-page primary PDF SHA256 is `6b379ceeead2c10e614bd4be268c9672f0b364fa95799a5474a9479a82f9e445`.

For nonprincipalχ, the pole-residue term vanishes and ψχ(t)=−Σ_{n≤1/t}χ(n). This function is supported on0<t≤1 and bounded byq by period cancellation, hence isL². Its Mellin transform is−Lχ(s)/s, first forRe s>1 and then forRe s>0 by boundedness and continuation. Thus the residual1_(0,1](t)+Σ_{n≤N}a_nψχ(nt) has transform(1−LχA)/s. Mellin–Plancherel has exactlydt/(2π). The continuous scalesα∈[1/N,1] containα=1/n; signs are absorbed in arbitrary complex coefficients. ThereforeD(1/N)≤Δ_(N,χ), with no cutoff power loss or factor2.

Square the nonnegative published lower bound. Under GRH its critical-line zero sum equals the sum in(A). The source theorem says'bande critique' whereas its discussion and jet proof select critical-line zeros; this wording does not affect the present GRH specialization. Nothing here promotes an unproved off-line version or audits every analytic step of the published theorem.

## Evidence, credit and next steps

Full proponent: effective_cluster62_dirichlet_transfer.md. Independent skeptic: ../dirichlet_transplant_skeptic62.md. Further adversarial check: ../latest62_dirichlet_transfer.md. The director independently checked the analytic log branch, centered functional-equation symmetry, central factor, Poisson fixed-window coefficient, retained-edge signs, actual integer support, unchanged quadrature exponents and exact Mellin inclusion. The proponent's39 finite controls test complete-cell signs, asymmetric telescoping and a complex mod5 Mellin example; they are corroboration, not proof of the infinite assertions.

This is a source-based transplantation with classical generalized lower-bound ancestry. A bounded search has not established publication novelty. Next precise work: check the broader prior literature for the same upper theorem; instantiate fixedχ effective constants; determine whether any controlled conductor dependence survives; extend beyond degree1 only after accounting for its gamma degree, coefficient estimates and appropriate complementary-function lower bound. Do not infer a moving-conductor result from a fixed-character proof.
