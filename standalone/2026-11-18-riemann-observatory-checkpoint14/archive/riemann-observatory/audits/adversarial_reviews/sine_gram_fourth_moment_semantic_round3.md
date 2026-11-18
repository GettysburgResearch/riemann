# Independent sine-Gram third and fourth expected moments

Reviewer: semantic_skeptic. Date: 17 November 2026. Reconstructed from DPP correlations and Fourier box geometry before reading the other new moment derivations. No stochastic simulation, numerical quadrature or formal build is used. This is a pure-model calculation, not an arithmetic/prime moment theorem or a novelty claim.

**Conclusion:** for the stationary unit-intensity sine DPP and its finite sinc Gram matrix,

lim_(R->infinity)(1/R) E Tr G_R³=2,

lim_(R->infinity)(1/R) E Tr G_R⁴=13/4.

The delicate all-distinct four-cycle term is exactly0. Its24 determinant terms reduce to11/10-3V, where an independently evaluated Fourier overlap integral gives V=11/30.

## 1. Primary convention and normalization

Let k(t)=sin(pi t)/(pi t), k(0)=1, and X be the stationary sine DPP with correlation densities

rho_l(y1,...,yl)=det[k(yi-yj)].

Let X_R=X intersect[0,R], G_R=(k(x-y))_(x,y in X_R), and

mu_R=(1/R) E sum_(j=1..N_R)delta_(lambda_j(G_R)), N_R=#X_R.

This is expected normalization by interval length, **not** expectation of normalization by the random N_R. Since rho1=1, E N_R=R, so mu_R is a probability measure and its first moment is exactly1.

Actual primary passages inspected for this review: Soshnikov, arXiv math/0002099v4, printed p3 Definition2/Eq1.5 (factorial correlation convention), p8 Definition3/Eq1.20 (determinantal correlations), and p28 Eq2.35 (the displayed unit-intensity sine kernel). These are selected passages of the accessed source, not a substantive reading of its entire66 pages. The preprint/source identity and private-cache SHA are recorded under PAPER-SG001. No assertion that this paper states the present third/fourth Gram-moment formulas is made.

The factorial convention gives, for ordered distinct tuples,

E sum_(distinct y1,...,yl in X_R)F(y)=integral_[0,R]^l F(y)rho_l(y)dy.

There is no1/l! here. In the trace expansion, positions with equal points are first grouped into a set partition; order its blocks canonically by least element, then assign distinct points to those labeled blocks. This counts each trace tuple exactly once. An unordered-point convention would require a compensating factorial, but is not the convention used here.

## 2. Finite windows converge to anchored whole-line integrals

For a trace word of length m and a coincidence partition pi with l blocks, let F_pi be the product of k along the quotient cyclic word, with loops equal to k(0)=1. The expected normalized trace is the sum over partitions of

(1/R)integral_[0,R]^l F_pi(y)rho_l(y)dy.

Writing y_i=y_1+t_i and t_1=0 gives this exactly as

integral_R^(l-1) w_R(t)F_pi(0,t)rho_l(0,t)dt,

w_R(t)=[1-(max_i t_i-min_i t_i)/R]_+.

Here0<=w_R<=1 and w_R->1 at every fixed t. The kernel matrix is positive semidefinite with diagonal1, so0<=rho_l<=1. Thus an integrable majorant is |F_pi|.

All required trace graphs for m<=4 have absolutely integrable products. For two vertices the products are k² or k⁴. For a three-cycle, put a=|k|: its integral is bounded by ||a||_(3/2)^3 using Young and Holder. For a four-cycle it is ||a*a||_2²<=||a||_(4/3)^4. These are finite because |k(t)|<=min(1,C/|t|), hence k belongs to every L^p with p>1. A doubled two-spoke graph has integral of |k(x)|²|k(y)|², also finite. Consequently dominated convergence applies partition by partition.

Furthermore each determinant term adds factors of magnitude<=1 to the same trace product. Every individual term in the finite determinant expansion is therefore absolutely integrable. The Fourier contractions below and all finite determinant summations are justified; no conditional interchange of divergent sinc integrals is used.

## 3. Exact Fourier integrals

Use Fourier transform fhat(xi)=integral f(t)exp(-2pi i t xi)dt and B=1_[-1/2,1/2], so khat=B. Projection contraction gives

integral k(t-a)k(t-b)dt=k(a-b),

an L2 inner-product identity. Put T(xi)=(1-|xi|)_+, the transform of k². The transform of k³ is

B3(xi)=3/4-xi², |xi|<=1/2,

B3(xi)=(1/2)(3/2-|xi|)²,1/2<=|xi|<=3/2,

and0 outside. This follows by integrating the triangular function over a unit box.

The needed values are

I2=integral k²=1,

I4=integral k⁴=integral T²=2/3,

I6=integral k⁶=integral B3²=9/20+1/10=11/20,

J=integral_R² k(x)²k(y)²k(x-y)² dxdy=integral T³=1/2,

L=integral_R² k(x)³k(y)³k(x-y)dxdy
 =integral_[-1/2,1/2]B3(xi)²dxi=9/20,

U=integral_(four-cycle)product_edges k²=integral T⁴=2/5.

These are elementary polynomial integrals, with all Fourier normalizations explicit. Projection/Parseval calculations are in L2; no claim that k itself is L1 is needed.

### The complete K4 graph with one doubled matching

Let

V=integral_R³ k(u)²k(x-y)²k(x)k(x-u)k(y)k(y-u) dxdydu.

For fixed u put h_u(x)=k(x)k(x-u). Its Fourier transform is obtained by overlapping two unit boxes. For |xi|<=1, let ell=1-|xi|. The overlap is an interval of length ell and midpoint xi/2, giving

hhat_u(xi)=exp(-pi i u xi)ell*sinc(ell u).

It is0 for |xi|>1. The k(x-y)² factor is the Fourier multiplier T(xi)=ell, so Parseval yields

V=integral_[-1,1]ell³[integral_R k(u)²sinc(ell u)²du]dxi.

For0<ell<=1, another triangular-overlap calculation gives

integral k(u)²sinc(ell u)²du
 =(1/ell)integral_[-ell,ell](1-|t|)(1-|t|/ell)dt
 =1-ell/3.

The ell=0 value follows by dominated convergence, although it is immaterial after multiplying by ell³. Hence

V=2 integral_0^1 ell³(1-ell/3)dell=11/30.

This is an exact Fourier/box-polytope evaluation. The original graph integral is absolutely integrable by the four-cycle majorant. The transformed integrand is nonnegative, so the last interchanges can also use Tonelli.

## 4. Three-vertex determinant integrals

Write a=k(x), b=k(y), c=k(x-y). Then

rho3=1-a²-b²-c²+2abc.

For the triangular trace product define

A=integral_R² abc*rho3 dxdy.

Projection contraction gives integral abc=1 and integral a³bc=I4; the three squared-edge insertions are equivalent by relabeling. Thus

A=1-3I4+2J=0.

For the doubled-spoke product define

Bstar=integral_R² a²b²*rho3 dxdy.

Expanding the determinant gives

Bstar=1-2I4-J+2L=1/15.

In particular an all-distinct trace-cycle integral can vanish through signed sinc cancellation even though the DPP density is nonnegative. No positivity of each trace product has been assumed.

## 5. Third-moment coincidence accounting

There are five partitions of the three cyclic positions:

| Number/type | Multiplicity | Anchored limit for each |
|---|---:|---:|
| all points equal |1|1|
| one repeated point and one other point |3|I2-I4=1/3|
| three distinct points |1|A=0|

Therefore the third expected per-length moment tends to1+3/3=2. The same accounting at order2 gives1+(I2-I4)=4/3.

## 6. All24 determinant terms for the distinct fourth cycle

Let C be the anchored integral of k12 k23 k34 k41 times rho4. Expand the determinant by permutations. The cycle type and its position relative to the trace cycle give:

| Permutation class | Count | Sign | Graph integral |
|---|---:|---:|---:|
| identity |1|+|1|
| single transposition, adjacent trace endpoints |4|-|I4=2/3|
| single transposition, opposite trace endpoints |2|-|I4=2/3|
| two adjacent transpositions |2|+|L=9/20|
| two opposite transpositions |1|+|V=11/30|
| a3-cycle |8|+|J=1/2|
| the trace4-cycle or its inverse |2|-|U=2/5|
| another4-cycle |4|-|V=11/30|

For a single transposition, contracting the remaining two- or three-edge paths leaves k⁴. Two adjacent transpositions give a four-cycle with alternating edge powers3,1,3,1, whose Fourier integral is L. A3-cycle lets the unused vertex contract to the third squared triangle edge, giving J. Two opposite transpositions and the four nontrace Hamiltonian cycles all produce the same complete K4 graph with a doubled matching, V. The trace cycle or inverse gives the square of every trace edge, U.

The counts sum to24. Therefore

C=1-6I4+2L+V+8J-2U-4V
 =11/10-3V=0.

This cancellation has been independently derived rather than inferred from the desired final moment.

## 7. All15 coincidence partitions at fourth order

The quotient trace words give the complete table:

| Type | Multiplicity | Anchored limit for each |
|---|---:|---:|
| one point, AAAA |1|1|
| two points, two transitions |6|I2-I4=1/3|
| two points, alternating ABAB |1|I4-I6=7/60|
| three points, adjacent repeated position |4|A=0|
| three points, opposite repeated position ABAC |2|Bstar=1/15|
| four distinct points |1|C=0|

The6 two-transition partitions comprise four3+1 partitions and two adjacent2+2 partitions. The third2+2 partition is alternating. Of the six3-block partitions, four repeat neighboring cyclic positions and two repeat opposite positions. Thus every partition is accounted for exactly once.

It follows that

lim(1/R)E TrG_R⁴
 =1+6(I2-I4)+(I4-I6)+4A+2Bstar+C
 =1+2+7/60+2/15=13/4.

## 8. Reproduction and limits of the conclusion

`experiments/code/sine_gram_fourth_moment_semantic_round3.py` independently enumerates the coincidence partitions and all24 determinant permutations, and evaluates the Fourier-polynomial integrals by exact Fraction integration. Its output, including every permutation and sign, is `experiments/results/sine_gram_fourth_moment_semantic_round3.json`. This verifies finite algebra/combinatorics; the analytic graph reductions and dominated convergence are proved above, not inferred from the program.

The proved pure-model prefix is(1,4/3,2,13/4), so the model combination84m3-16m4 is116. This does **not** establish that the prime-side zeta matrix has these moments, an almost-sure spectral limit, a random-N-normalized moment limit, or any new zero proportion. Those are separate statements with separate hypotheses. This review maps to the existing pure-model moment claim SG310 and introduces no duplicate theorem ID.

Classification: **Independently checked with no issue found in the inspected portion.**
