# Independent exact calculation of the first four sine-Gram moments

Date: 2026-11-17. Researcher/reviewer: li_advocate. Root independently obtained the repeated-index contributions and identified the all-distinct integral as the remaining check. I independently derived the permutation-integral classification below before seeing any other proof of that integral. No novelty or arithmetic higher-moment claim.

## Model and analytic justification

Let k(t)=sin(πt)/(πt), χ=1_[−1/2,1/2], τ=χ*χ=(1−|ξ|)_+, and let X be the unit-intensity determinantal sine process. Let G_R=(k(x−y)) for x,y∈X∩[0,R]. We calculate

    m_j=lim_{R→∞}(1/R)ETrG_R^j,    j=1,2,3,4.

Existence and absolute integrability of each trace-partition term were independently proved by the connected-Eulerian-graph/spanning-tree Hölder argument in `sine_gram_moment_existence_third_round3.md`. Thus all finite determinant expansions and Fubini manipulations here act on absolutely integrable graph products, rather than relying on cancellation of divergent pieces.

Fourier cycle-convolution identities below can be justified by replacing k(t) with k(t)e^{−επt²}, applying ordinary L¹ Fourier convolution, and taking ε↓0. The Gaussian-regularized products are dominated by the same integrable absolute graph products. On the Fourier side the interval indicators are smoothed by an approximate identity and the indicated compact overlap/convolution formulas converge. This avoids treating an informal delta constraint as an unproved interchange of nonabsolutely convergent integrals.

## Elementary integrals

Parseval and interval convolution give

    ∫k²=1,
    ∫k⁴=∫τ²=2/3,
    ∫k⁶=11/20,
    J3=∫cycle_of_3_edges k(edge)²=∫τ³=1/2,
    J4=∫cycle_of_4_edges k(edge)²=∫τ⁴=2/5.

For the sixth-power integral, put b3=χ*χ*χ. On |ξ|≤1/2,

    b3(ξ)=3/4−ξ²,

and on1/2≤|ξ|≤3/2,

    b3(ξ)=.5(3/2−|ξ|)².

Hence

    H=∫_[−1/2,1/2] b3(ξ)²dξ=9/20,
    ∫b3²=9/20+1/10=11/20.

These rational integrals are independently checked by the standard-library Fraction script accompanying this review.

## Third-order determinant cycle and the star term

For three distinct points, write a=k(x), b=k(y), c=k(x−y). The density is

    ρ3(0,x,y)=1−a²−b²−c²+2abc.

The triangle cycle integral is

    T=∫abc ρ3 dxdy
      =1−3(2/3)+2(1/2)=0.

Here the base projection cycle contributes1, each one-edge cubing term contributes2/3, and the fully squared cycle contributes1/2. In contrast, the opposite-repeat star is

    B=∫a²b²ρ3 dxdy
      =1−2(2/3)−1/2+2(9/20)=1/15.

The H=9/20 term follows by Fourier transformation of ∫k(x)^3k(y)^3k(x−y) dxdy, which becomes∫_band b3².

## The missing all-distinct four-cycle integral

Set x1=0 and define

    A4=∫_(R³) k12 k23 k34 k41 ρ4(x1,x2,x3,x4) dx2dx3dx4,
    kij=k(x_i−x_j).

Expand ρ4=det(kij)=sum_{σ∈S4}sgn(σ)product_i k_{i,σ(i)}. Fixed points contribute1. Because k is even, each permutation term depends only on the undirected multigraph obtained by adjoining its nonloop edges to the base four-cycle. Parallel edges retain their multiplicity.

The exact integral table is:

| Permutation class | Number | Sign | Integral for each |
|---|---:|---:|---:|
| identity |1|+|1|
| transpositions |6|−|2/3|
| three-cycles with one fixed point |8|+|1/2|
| adjacent-pair double transpositions |2|+|9/20|
| crossing double transposition |1|+|11/30|
| base four-cycle or its reverse |2|−|2/5|
| other four-cycles |4|−|11/30|

Here are explicit verifications of every entry, rather than just their labels.

* Identity: successive projection convolutions k*k=k reduce the base cycle to k(0)=1.
* Transpositions: for adjacent transposition(12), the edge12 is cubed and the complementary three-edge path convolves to k12, giving∫k⁴=2/3. For opposite transposition(13), integrate the two degree-two intermediate vertices, again obtaining∫k⁴. Rotation/reflection covers all six.
* Three-cycles: the vertex fixed by σ has degree two. Integrating it collapses its two k edges to their projection convolution, leaving a triangle with all three edges squared. Its integral is∫τ³=1/2. All eight permutations have this graph form.
* Noncrossing double transpositions(12)(34) and(14)(23): the union is a four-cycle with alternating kernels k³,k,k³,k. Its integral is∫b3²χ²=∫_band b3²=9/20.
* Base four-cycle(1234) and its reverse: every base edge is squared, giving∫τ⁴=2/5.
* Crossing double transposition(13)(24): the base cycle has both diagonals doubled. Write the Fourier variables for the two doubled-diagonal pairs as differences z1,z2; each has convolution weight τ(z). Kirchhoff conservation along the base cycle makes its four edge frequencies, up to a common translation t,

      t, t+z1, t+z1+z2, t+z2.

  Their span is exactly |z1|+|z2|, so the available common interval length is(1−|z1|−|z2|)_+. Therefore its integral is

      ∫τ(z1)τ(z2)(1−|z1|−|z2|)_+ dz1dz2
      =4∫_{u,v≥0,u+v≤1}(1−u)(1−v)(1−u−v)dudv
      =4(1/12+1/120)=11/30.

* Other four-cycles: take representative σ=(1243). Its union with the baseC4 has doubled edges12 and34, and single edges23,41,24,13. Swapping labels2 and3 maps this multigraph to the crossing-double-transposition graph, with doubled diagonals13 and24 and four single base-cycle edges. Thus its integral is the same11/30. The other three non-base four-cycles belong to the same multigraph-isomorphism class. The exact script enumerates all24 permutations and checks this classification.

It follows exactly that

    A4=1−6(2/3)+8(1/2)+2(9/20)+11/30
          −2(2/5)−4(11/30)=0.                         (A4)

This is a projection/DPP graph-integral identity. It is not obtained by assuming the desired fourth moment.

### Independent autocorrelation check of11/30

The parent adjudicator independently derived the crossing integral without the cycle-flow parameterization. Put y=x3−x1, v=x4−x2, x=x2−x1, f=k², and A_y(x)=k(x)k(y−x). Then

    Icross=∫ f(y)f(v)∫A_y(x)A_y(x+v)dxdvdy.

The Fourier transform in x is, for |ξ|≤1,

    Ahat_y(ξ)=e^{−πiξy}ell sinc(ell y),
    ell=1−|ξ|,

and zero otherwise. This follows by convolving two interval indicators: the overlap has length ell and center−ξ/2. Autocorrelation Plancherel and fhat(ξ)=ell give

    Icross=∫_{−1}^1 ell³∫ f(y)sinc(ell y)²dydξ.

For0<ell≤1, triangular Fourier overlap gives

    ∫f(y)sinc(ell y)²dy
      =(2/ell)∫_0^ell(1−ξ)(1−ξ/ell)dξ
      =1−ell/3.

Therefore Icross=2∫_0^1 ell³(1−ell/3)dell=11/30. Initial Fubini is justified by the absolute graph integrability already proved; the subsequent transformed integrands are nonnegative. This independent derivation checks the delicate crossing constant and its normalization.

## Trace-partition sum

For the third moment, there are one all-equal partition, three two-point partitions, and one all-distinct partition:

    m3=1+3(∫k²−∫k⁴)+T=1+1+0=2.

For the fourth moment the15 set partitions divide as follows:

* one all-equal partition: contribution1;
* seven two-point partitions: six have kernel k² and one alternating partition has kernel k⁴; their total is6(1−2/3)+(2/3−11/20)=127/60;
* six three-point partitions: four adjacent-repeat patterns give T=0, two opposite-repeat patterns give B=1/15; total2/15;
* one all-distinct partition: A4=0 by the independent calculation above.

Thus

    m1=1,
    m2=1+(1−2/3)=4/3,
    m3=2,
    m4=1+127/60+2/15+0=13/4.

The source-specific model values used in AF2026 §7.2(f) are therefore independently reconstructed. In particular84m3−16m4=116 for this random model. This calculation does not prove that any prime-side zeta compression has these third/fourth moments, which remains the explicit arithmetic condition in the clipped-HS bridge.

## Status and reproducibility

The exact code is `experiments/code/sine_gram_fourth_exact_round3.py`; results are in `experiments/results/sine_gram_fourth_exact_round3.json`. It checks rational polynomial integrals, all24 permutation classes and signs, graph isomorphisms for the mixed four-cycles, the zero all-distinct sum, all15 trace partitions, and the resulting moments. The analytic Fourier/graph justification is the proof above, not inferred from finite numerical experiments. The parent independently confirmed the table and zero sum, including an alternative crossing-integral derivation.

Parent adjudication subsequently confirmed the table and zero sum, with the independent autocorrelation derivation above. The source model moment values are checked; their arithmetic realization for zeta remains conditional.
