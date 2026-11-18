# Director adjudication: finite lattice certificates and the constant-term constraint

17 November 2026. I independently checked the algebra, finite convex geometry, exact escape witness and interval interpretation after reading the two source-based proofs and the independent reviews. Evidence: audits/latest62_inverse_adjacent_lattice.md; audits/adversarial_reviews/finite_moment63_review.md; augmented_moment63_review.md; prefix_moment63_cli_review.md. The general discrete moment and positive cubature results are credited to Infusino–Kuna–Lebowitz–Speer and Bayer–Teichmann. These are scoped ordinary proofs and an exact arithmetic implementation, not whole-paper audits, actual zeta coefficient enclosures or a priority claim.

## 1. Exact data and finite certificates

Let μ_m=m(m−1), a_m=μ_m²W_m for m≥2, and ν=Σa_m δ_(μ_m). All a_m are nonnegative. The first M nonconstant Taylor coefficients of the already reconstructed prefix profile determine the moments y_j=∫x^j dν for 0≤j<M by the invertible triangular map. The constant C(0) is separate. These are true limiting Taylor data, never derivatives of a finite-N staircase. Their arithmetic interpretation requires the earlier RH-conditional fixed-prefix theorem; the following positive-measure statements do not.

For M≥1 define P_M(x)=∏_(j=2)^M(x−μ_j), with empty product1, and

    D_M=P_M(μ_(M+1))=(M−1)!(2M)!/(M+1)!.

This polynomial is zero on the first M−1 lattice nodes and positive and increasing on the tail. Therefore

    0≤Σ_(m>M) a_m≤R_M/D_M,   R_M=∫P_M dν.

For M=1 this is the exact identity Σ_(m≥2)a_m=y_0=C'(0). If R_M=0, all multiple support lies among m=2,…,M; Vandermonde recovers its weights, and C(0) recovers W_1. Positive tail bounds alone give no maximum multiplicity. The single-polynomial bound is sharp globally, attained by distributions supported through μ_(M+1).

For 2≤j≤M let ℓ_j=P_M/[(x−μ_j)P'_M(μ_j)], T_j=∫ℓ_j dν and σ_j=sign P'_M(μ_j)=(-1)^(M−j). Exact interpolation and the positive tail give

    0≤σ_j(T_j−a_j)≤R_M/[|P'_M(μ_j)|(μ_(M+1)−μ_j)].

For any fixed node μ_j, let d_j be its distance to the nearest other lattice node: d_2=4 and d_j=2(j−1) for j≥3. Since 1−(x−μ_j)²/d_j² is at most the node indicator on the lattice,

    a_j≥y_0−(y_2−2μ_j y_1+μ_j² y_0)/d_j².

These are signed polynomial functionals, so exact rational coefficient intervals propagate rigorously. Combining a functional with the inverse triangular map before interval evaluation preserves useful cancellations. The sensitivity of the normalized upper R_M/D_M to the last Taylor coefficient is exactly M(M+1)²/binom(2M,M)². Raw inverse-moment amplification is therefore not by itself an error estimate for this particular certificate.

## 2. Including C(0) changes finite-data identifiability

The remaining simple mass is W_1=C(0)−∫g dν, where

    g(x)=4/(sqrt(1+4x)−1)²,   g(μ_m)=1/(m−1)².

For y_0>0 normalize ν to a probability. For n≥1, the feasible augmented data (y_1/y_0,…,y_n/y_0,C(0)/y_0) are exactly

    A_n=conv{(x,…,x^n,g(x)): x=μ_m,m≥2}+R_(≥0)e_c.

The ray represents W_1/y_0. Positive finite-dimensional cubature replaces any representing measure by at most n+2 occupied lattice atoms with the same data. The set has full dimension; it need not be closed.

Every feasible interior datum admits positive mass at any chosen lattice node while preserving all these data, including C(0). Remove a sufficiently small amount of that node's augmented vector, renormalize, and use the open interior ball and finite cubature. One can even plant a small probability with positive weights at every node and exponential tails, then represent the residual finitely. This is an inverse-data ambiguity, not a possible rearrangement of the actual zeros of a fixed zeta function.

At a feasible boundary datum a supporting affine functional has the form h(x)=p(x)+βg(x)≥0 on the lattice, deg p≤n and β≥0. Zero total slack forces h to vanish on every occupied multiple node and βW_1=0. If β=0 there are at most n contacts. If β>0, rationalization gives

    g=x^(-1)+(1/2)x^(-2)+(x^(-2)+4x^(-1))/(2sqrt(1+4x)).

Every derivative has strictly alternating sign, since the factors are completely monotone and x^(-1) makes the sign strict. Hence h^(n+1) never vanishes, and Rolle bounds the contact set by n+1 points. Vandermonde and C(0) uniquely determine the whole profile. The parity refinement in the independent review is also valid: when n is even there are at most n contacts; when n is odd, n+1 contacts require consecutive-node pairs. This follows from the sign of the interpolation remainder for g beyond and between the contacts.

If y_0=0, positivity forces ν=0 and W_1=C(0)≥0; all other moments must vanish. For n=0 with y_0>0, the feasible normalized constant is any c>0 and no such finite-support boundary point exists. Thus the exceptional exact datum C'(0)=0 is not the only possible finite uniqueness certificate, and interior pure moments alone do not decide the augmented problem.

## 3. Escape to infinity is a real feasibility obstruction

For n≥1 the closure of A_n adds a nonnegative ray only in the highest pure moment. Normalize the generators of the cone by 1+x^n+g(x). Their only new limit is the highest-moment unit vector with zero mass; the normalized generator set plus the simple-slack vector is compact on a positive affine slice. Its cone is closed, proving the stated closure formula. At a boundary point, a supporting p+βg has leading coefficient p_n≥0. Complementarity forces the escape to vanish if p_n>0. If p_n=0 there are at most n contact nodes; their masses are fixed by the lower moments, C(0) fixes the simple mass, and the highest moment fixes the unique remaining escape. Exact feasibility means escape zero.

Here is a complete witness. The data

    (y_0,y_1,y_2,C(0))=(1,6,37,1/4)

have interior pure moments but are infeasible augmented data. Strict Jensen for g and mean6 forces ν=δ_6 when ∫g≤1/4, contradicting y_2=37. Nevertheless they belong to the feasible-data closure. For any lattice x>6 put masses

    1/[(x−6)(x−2)] at x,
    1/[4(x−2)] at2,
    the remaining mass at6.

They have exactly y_0=1,y_1=6,y_2=37, while their g cost decreases to1/4 from above as x tends to infinity. The limiting closed-cone representation is δ_6 plus one unit of second-moment escape. All continuous nonnegative dual inequalities can hold at this infeasible point. A numerical positivity/SDP check alone is not a representability certificate. With exact boundary saturation, the contact and escape tests distinguish it.

## 4. Implementation and unresolved arithmetic input

The standard-library Fraction CLI experiments/code/prefix_moment63_certificates.py implements only the proved conditional tail and interpolation certificates, with exact rational or rational interval inputs. It explicitly reports feasibility_checked=false. Its tail status is conditional on a common positive lattice representation. It rejects duplicate JSON keys, invalid Unicode and a proved necessary coefficient inequality; these checks do not solve full feasibility. No actual zeta Taylor coefficients were supplied. The independent review ran 540 feasible controls,18 cutoff/saturation controls,16 malformed/contradictory inputs and three deliberately infeasible examples, with byte-identical saved replays.

The full augmented classifier has not been implemented as a numerical decision procedure. A rigorous higher-moment cap can control finite-lattice truncation; without it an atom can escape in the highest supplied moment. The actual RH profile has very strong multiplicity-weight tails, but effective numerical constants and genuine limiting coefficients are still needed. An arithmetic endpoint estimate, or certified limiting derivatives with a controlled order of limits, remains the essential missing input. These finite certificates do not decide RH or simplicity from finite-N staircase values.
