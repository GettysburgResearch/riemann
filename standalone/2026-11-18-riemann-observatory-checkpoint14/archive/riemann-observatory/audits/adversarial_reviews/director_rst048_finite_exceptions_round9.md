# Director adjudication: finite off-line exceptions and excess approximation rates

17 November 2026. Accepted scoped reconstruction of RST048 v2 Theorem6, (90)–(101), under the hypothesis that its multiset Z+ of right off-line nontrivial zeros is finite. Exact source SHA256: 57a65d19bc9914db42dfc2869850cc02e959b87699099abeb40525085600681b. I read the original §9 and the two independent complete reconstructions rst048_thm6_advocate63.md and rst048_thm6_skeptic63.md, including their distinct lower-bound routes, then independently checked the projection, scalar minimization and contour interfaces. RST001 v2 and RST004 v1 are now separate versioned bibliography records. The earlier fixed-Laurent localization qualification is retained. No whole-paper Level2/3 or priority claim follows.

## 1. The limiting target is a discrete projection

Use H=L²(dt/(2π)) on Re s=1/2, E=1/s, and let S be the Mellin image of integer-cell steps in L²([1,∞),dx/x²). Put V_N=span{ζ(s)(n^(−s)−n^(−1))/s:2≤n≤N}, V=closure union V_N, u=P_VE and D∞²=‖E−u‖². An anchored length-N polynomial gives exactly V_N, so

    d_N²=D∞²+dist(u,V_N)².

Under the finite-exception hypothesis the right-zero jets are independent on S and V is their common kernel. For independence, a relation tested against n^(−s)/s and summed with n^(−w) gives distinct highest-order poles at w=1−ρ. For synthesis, choose finite Dirichlet polynomials spanning the finite jet space. If P vanishes to all required orders, P/ζ is holomorphic on Re s>1/2. Smooth Dirichlet cutoffs of(P/ζ)(s+ε), anchored at1, converge first at fixed ε>0 by a retained-right shift and subpower reciprocal bounds. Then let ε↓0. The critical-line factors in the paired Hadamard product have modulus ratio≤1; each finite off-line factor is bounded uniformly for ε below half its horizontal distance. The gamma quotient grows by only a small power. Dominated convergence and the vanishing anchor prove P/s∈V. Correcting a dense finite-polynomial family by the fixed spanning polynomials yields the full kernel identity.

Thus S⊖V is a finite span of step-projected reproducing jets. It is not the continuous Hardy-space Blaschke complement. In particular replacing u by a scalar Blaschke product divided by s changes the discrete target. The latter nonconstant rational numerator has an asymptotic expansion in1/s incompatible with the exponentially small correction of any integer-step Mellin transform after its first cell.

## 2. The unrestricted norm has an extra scalar penalty

Write H0=ζ/s−1/(s−1). It is the Hardy transform of −{x} on x≥1. The boundary vector1/(s−1) is orthogonal to that Hardy space and has squared norm1. Set h_S=P_SH0, κ=‖H0−h_S‖² and Π=P_(S⊖V). For c=A(1), the full residual splits exactly into the finite V_N approximation, this outside-Hardy vector, the nonstep part and Π. Define

    u_c=P_V(E−c h_S),
    F(c)=(1+κ)|c|²+‖Π(E−c h_S)‖²,
    Λ=1+κ+‖Π h_S‖²>0.

Let c* uniquely minimize F, put u*=u_(c*) and Δ∞²=F(c*). Then

    Δ_N²−Δ∞²=min_c{Λ|c−c*|²+dist(u_c,V_N)²}.

The scalar is allowed because the ordinary first coefficient makes the pair(V_N coefficient vector,c) free at the same length N. If Z+ is nonempty, both baselines are positive. For D∞ this follows from a continuous right-zero evaluation of E; F(c)=0 would require c=0 and ΠE=0, which is impossible. The theorem estimates excess over these baselines, not convergence of the original distances to zero.

## 3. The precise limits

The accepted statements are

    lim_N (log N)(d_N²−D∞²)=Σ_(Reρ=1/2, distinct) mρ²|u(ρ)|²,
    lim_N (log N)(Δ_N²−Δ∞²)=Σ_(Reρ=1/2, distinct) mρ²|u*(ρ)|².

The targets already contain1/s, so no further factor1/|ρ|² belongs in these sums. If Z+ is empty, u=u*=E, c*=0, and these reduce to Theorem1. The finite exceptional configuration and all its multiplicities are fixed before N→∞.

## 4. Why the upper argument extends

Step-projected right-zero jet representers have cell size O(n^(1−β)log^j n) and successive differences O(n^(−β)log^j n); h_S has differences O(n^(-2)). Hence W=sU for U=u or u* and all fixed derivatives are bounded on Re s≥1−β_min+ε. Choose δ with4δ<β_min−1/2. On the left line a=1/2−δ, G=W/ζ has only critical-line poles to its right: right exceptions cancel and reflected exceptions are to its left.

At high height finite exceptions leave a zero-free fixed right half-strip. Borel–Carathéodory and three circles for logζ give subpower ζ and1/ζ on retained lines and ζ'/ζ(1/2+η+it)=o(log|t|). The completed logarithmic derivative then gives a positive critical-line Poisson sum equal to(1/2+o(1))log|t|, up to negligible finite exceptions. Integrating over a padded fixed cell with η≤D/3 bounds the cluster size by(2D/π+o(1))log|t|<D log|t|. This independently supplies the needed count and avoids importing an unproved exact finite-exception version of the source RH error term(8).

Both full contour identities retain the upward left edge. Their combination gives ζ(J0−JN)/logN, of norm O(1/logN); the strip residue carries W(s) times the full indicator. The previously reconstructed delayed-cluster bounds, telescoping connectors and ordinary integer quadrature keep their strict negative exponents. They apply to every subset of clusters. Fixed Laurent terms of reduced order contribute only O(1/logN) in norm; the top term supplies m²|U(ρ)|² after the local optimal profile. Fixed replacements precede N→∞ and tail exhaustion. The anchor is O(1/logN) in the full weighted norm and changes no leading constant. No growing inverse-zero-derivative or inverse-Gram bound is assumed.

## 5. Matching lower bounds and a moving scalar

The already reconstructed paper47 compact Mellin tests apply directly to U−v_N, with arbitrary bounded v_N∈V_N. Their limiting normalized Gram is the confluent Hilbert block. The target's cell growth gives local uniform convergence of compact Mellin tests to U and its derivatives across the critical line; its normalized higher-jet targets vanish, leaving U(ρ) in the zeroth slot. The first inverse Hilbert entry is m². This gives the fixed finite-zero lower bound and then exhaustion. The advocate's independent Burnol-vector transfer gives the same result. No subtraction of exceptional representers from the test vectors is needed.

For the unrestricted minimum, the upper bound at fixed c* makes the excess O(1/logN); the exact positive scalar penalty forces c_N−c*=O((logN)^(-1/2)). The targets u_(c_N) lie in a bounded two-dimensional family. Their compact pairings therefore converge to those of u*, and discarding the nonnegative scalar penalty gives the matching lower bound. This avoids an unjustified uniform-in-c upper construction.

The finite-exception assumption remains an unresolved arithmetic hypothesis. The reconstruction does not establish that any such off-line configuration actually occurs or that the exceptional set is empty. Its usable content is the exact discrete projection geometry and the two conditional excess-rate formulas.
