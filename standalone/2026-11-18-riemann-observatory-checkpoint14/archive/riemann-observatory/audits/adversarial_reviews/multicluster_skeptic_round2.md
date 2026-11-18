# Independent round-two review: bounded multi-root clusters

Reviewer: li_advocate. Date:2026-11-17. Before receiving the equivalence agent's draft, I independently reconstructed the divided-difference basis, exact finite Gram problem, uniform quadrature convergence, and compactness proof of a positive limiting Gram lower bound. The equivalence agent subsequently supplied an explicit small-interval lower bound, which I independently checked below. No publication novelty is claimed.

## Precise theorem and limiting functional

Fix integer m≥2 and finite C≥0. Let L=N+m, N≥0, and let c=(c_1,…,c_m)∈[−C,C]^m. Form a degree-m polynomial P with roots exp(ic_j/L), counted with actual multiplicity (its nonzero scalar normalization is irrelevant). Let E_N(c/L) be the minimum squared unweighted circle H² error ||1−PA||² over degree≤N polynomials A.

For j=0,…,m−1 define

h_j(x;c)=j! i^(−j) [c_1,…,c_(j+1)]_t exp(itx),

where brackets are divided differences in the frequency variable t and repeated nodes are interpreted by Hermite derivatives. Define

H(c)_(ij)=∫_0^1 h_i(x;c) overline(h_j(x;c)) dx,
F_m(c)=e_0*H(c)^(−1)e_0.

Then H is positive definite for every c, F_m is continuous across every collision, and there exists K_(m,C)<∞ such that

sup_(c∈[−C,C]^m) |L E_N(c/L)−F_m(c)|≤K_(m,C)/L

for every N≥0. For sufficiently large L no phase aliases occur and the proof is the stable Gram formula. For the finitely many smaller L, the theorem refers to the actual polynomial P and its true multiplicities, not a rank-deficient frequency-value matrix.

Equivalently, F_m(c) is the squared minimum L²([0,1]) norm of a complex density u satisfying, at each distinct node a with multiplicity r,

∫_0^1 u(x)e^(iax)dx=1,
∫_0^1 u(x)(ix)^q e^(iax)dx=0, 1≤q<r.

This is a finite interpolation/jet variational problem, not a claim about ζ zeros or arithmetic approximants.

## Basis, collisions, and finite exactness

The Hermite–Genocchi formula gives

h_j(x)=x^j E[exp(ix ∑_(ell=1)^(j+1) T_ell c_ell)],

where T is uniform on the j-simplex (Dirichlet(1,…,1)); for j=0 this is the single node. Consequently h_j=x^j+O(Cx^(j+1)), |h_j|≤1, and |h'_j|≤j+C on[0,1]. The basis depends continuously, indeed analytically symmetrically in each prefix, on all frequency nodes even when arbitrarily many nodes collide. The Taylor derivatives at x=0 form a triangular matrix with diagonal j!, so the functions h_0,…,h_(m−1) are linearly independent. This already proves pointwise positive definiteness; continuity and compactness of the node cube give a uniform positive lower eigenvalue.

For large enough L>C/π, different frequencies in[−C,C] cannot differ by a nonzero multiple of2πL. Then the actual repeated roots are exactly repeated c nodes. A residual R(z)=∑_(k=0)^L r_k z^k belongs to1−P·{degree≤N} precisely when R at each root has value1 and all required derivatives vanish. Differentiating R(exp(it/L)) uses (i/L)^q(z d/dz)^q; the conversion to ordinary root derivatives is triangular with nonzero diagonal. Thus the constraints are exactly the confluent interpolation conditions in t. Applying normalized divided differences to the constant target1 gives

∑_(k=0)^L r_k h_j(k/L)=δ_(j0).

Let H_L(c)=(1/(L+1))∑_(k=0)^L h(k/L)h(k/L)*. These rows are independent when L≥m and there are no phase aliases; equivalently the Hermite evaluation matrix on degree≤L polynomials has full row rank. Minimum norm linear algebra gives

E_N(c/L)=(1/(L+1))e_0*H_L(c)^(−1)e_0.

No inverse of a nearly colliding raw Vandermonde is used in this formulation.

## Explicit positive lower bound independently checked

Let T_m=trace(Hilbert_m^(−1)), with Hilbert_m(i,j)=1/(i+j+1),0≤i,j<m. It is an explicit positive integer, for example

T_m=∑_(j=0)^(m−1)(2j+1)binom(m+j,m−j−1)^2 binom(2j,j)^2.

Put s=1/[1+2C sqrt(mT_m)] and δ=s^(2m−1)/(4T_m).

For arbitrary coefficients a_j set b_j=a_js^j. On x=st,

∑a_jh_j(st)=∑b_jt^j+error,

and |error|≤Cs∑|b_j|≤Cs sqrt(m)||b||_2 uniformly in t∈[0,1]. The polynomial has L² norm at least||b||_2/sqrt(T_m), because λ_min(Hilbert_m)≥1/T_m. The chosen s makes the error at most half this bound. Changing variables dx=s dt and using ||b||_2≥s^(m−1)||a||_2 yields

a*H(c)a≥s^(2m−1)||a||²/(4T_m)=δ||a||².

This independently validates the equivalence agent's proposed explicit δ. It is conservative but remains positive at every collision, without any minimum root-gap assumption.

## Uniform remainder with an explicit finite constant

Each Gram entry has Lipschitz constant at most2D, D=m−1+C. The normalized endpoint quadrature bound |average−integral|≤Lipschitz/L therefore gives

||H_L−H||_op≤A/L, A=2mD.

If L≥2A/δ then λ_min(H_L)≥δ/2 and

||H_L^(−1)−H^(−1)||≤2A/(δ²L).

Consequently

|L E_N−F_m|≤[2A/δ²+2/δ]/L.

To cover every finite L choose

L_0=max(m, ceil(C/π)+1, ceil(2A/δ)).

For m≤L<L_0 use0≤E_N≤1 and0≤F_m≤1/δ, giving

L|L E_N−F_m|≤L_0²+L_0/δ.

Thus one explicit valid constant is

K_(m,C)=max(2A/δ²+2/δ, L_0²+L_0/δ).

The estimates are uniform over frequency tuples depending on L, including gaps that close arbitrarily fast or exact collisions. Constants are not claimed sharp or computationally practical.

## Adversarial cases and scope

1. **Finite phase aliases:** if c_j−c_k=2πLq≠0, distinct c nodes represent the same polynomial root. The divided-difference frequency matrix then misses the extra derivative condition and may be singular. Its pseudoinverse must not be substituted for the true repeated-root problem. Aliases are absent for L>C/π and the finite-L part above uses E_N directly, so they do not refute fixed-(m,C) uniform convergence.
2. **Very fast collisions:** numerical raw divided differences become unstable, but the simplex representation and the analytic h_j basis remain regular. There is no gap-dependent constant in the proof. This addresses mathematical uniformity, not automatic numerical stability of a naive implementation.
3. **Growing m:** fixed m is essential. At a complete collision c_1=…=c_m=a, h_j=x^j e^(iax), the Gram is Hilbert_m, and F_m=m². The exact polynomial minimum is1−(L)_falling m/(L+1)_rising m. For fixed m its expansion is

L E_N=m²−m²(m²+1)/(2L)+O_m(L^(−2)).

Therefore any such K_(m,0) must be at least m²(m²+1)/2 asymptotically; no constant independent of m works. More strongly, if m²/L→t>0, then E_N→1−exp(−t), whereas F_m/L→t. Thus even relative agreement fails in this growing-m regime. The theorem supplies no uniform result for unbounded m.
4. **Ordering and common shifts:** the basis depends on a prefix ordering, but its optimizer value is independent of the ordering because it imposes the same confluent interpolation conditions. Adding a common frequency shift multiplies every h_j by the same unit-modulus exponential, leaving H and F_m unchanged.
5. **Exact all-collision consistency:** for fixed m, the m² constant agrees with the all-m polynomial optimum established in `proposals/independent_campaigns/multiplicity_general.md`. It supplies an independent limiting check, not a source audit.

Classification: independently checked with no issue in the fixed-m, bounded-frequency uniform theorem after specifying actual multiplicities at finite aliases. The explicit Gram lower bound supplied by the equivalence agent survives independent reconstruction. No transfer from this finite exponential-polynomial model to an infinite arithmetic zero set is proved, and fixed-root results such as Burnol's do not by themselves imply this uniform theorem.

`experiments/code/multicluster_skeptic.py` and `experiments/results/multicluster_skeptic.json` provide a separate70-digit numerical stress test, explicitly nonvalidated. It evaluates a complete-homogeneous Taylor representation of the confluent divided differences, so exact repeated nodes and gaps of10^(−35) do not require subtraction of almost equal function values. Six cases with m=2,…,5 and five choices of L were checked. The triple collision gives F=9; a triple with gaps10^(−35) agrees to displayed precision. Two exact double clusters give F≈15.7461032238536; perturbing both double roots by10^(−35) agrees to displayed precision. The exact all-collision finite error was also cross-checked against the all-m product formula. These are reproducibility observations, not certified bounds; all theorem conclusions above rest on the analytic proof.

## Independent addendum: explicit first correction and O(L^(−2)) remainder

The equivalence agent next proposed an endpoint correction. I reconstructed the following argument from its statement before reading its proof. Write G=H(c), κ=e_0*G^(−1)e_0, and

B_end=[h(0)h(0)*+h(1)h(1)*]/2,
β=e_0*G^(−1)B_end G^(−1)e_0.

With D_*=2m(C+m) and M_2=4m(C+m)^2, one has ||H_L−G||≤D_*/L and

H_L=G+(B_end−G)/(L+1)+R_L, ||R_L||≤M_2/(12L²).

To see this exactly, let T_L be the composite trapezoidal average of the matrix-valued function Q(x)=h(x)h(x)*. The normalized full endpoint average is [L T_L+B_end]/(L+1). The operator-norm bound on the trapezoidal error is sup||Q''||/(12L²). The simplex formula gives ||h||≤sqrt(m), ||h'||≤sqrt(m)(C+m), ||h''||≤sqrt(m)(C+m)². Therefore ||Q''||≤2||h''||||h||+2||h'||²≤M_2. These bounds include exact collisions.

Let E=H_L−G and v=G^(−1)e_0. For L≥2D_*/δ the inverse identity

H_L^(−1)=G^(−1)−G^(−1)E G^(−1)+G^(−1)E H_L^(−1)E G^(−1)

gives

F_L:=e_0*H_L^(−1)e_0=κ+(κ−β)/(L+1)+ε_L,
|ε_L|≤[M_2/(12δ²)+2D_*²/δ³]/L².

Here v*Gv=κ and v*(B_end−G)v=β−κ. Multiplying by L/(L+1) yields the exact algebraic relation

L E_N−κ+β/(L+1)=(β−κ)/(L+1)²+[L/(L+1)]ε_L.

Since ||B_end−G||≤2m, |β−κ|≤2m/δ². Thus a valid uniform bound is

|L E_N−κ+β/(L+1)|≤K_2/L²,
K_2=(2m+M_2/12)/δ²+2D_*²/δ³.

For the explicit δ above the threshold also excludes nonzero phase aliases; otherwise impose L>C/π explicitly. This is a large-L uniform statement, not a claim about the raw aliased Gram formula at arbitrary small L.

At complete coalescence, β=(m^4+m²)/2. This agrees with the independently derived exact all-m product expansion already recorded above. The numerical stress-test output now includes β and the L²-scaled corrected remainder, including repeated nodes and gaps10^(−35); it remains explicitly nonvalidated numerical evidence. This corroborates the uniform endpoint correction without claiming novelty or arithmetic transfer.
