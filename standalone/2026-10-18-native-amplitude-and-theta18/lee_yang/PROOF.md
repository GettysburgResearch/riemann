# A connected ferromagnetic realization of the original theta moments through degree 18

Status: **proposed computer-assisted finite theorem. Independent review of the
frozen source and replay is required. RH is not proved.**

The result below reaches a new moment target: every moment of the original
theta law through degree 18 is realized by an actual connected, zero-field,
ferromagnetic Ising measure. The construction has 281 vertices and 280 positive
edges. It is a new model and root certificate, not an extrapolation of the
degree 16 certificate in PR #974. Its moment 20 differs strictly from the target.
No unbounded-order construction or target-reaching extension theorem is asserted.

The inherited directed arithmetic is the same implementation as
[PR #886 at d998605c0718e332ac503baf078704b862f8250e](https://github.com/GettysburgResearch/riemann/tree/d998605c0718e332ac503baf078704b862f8250e/standalone/2026-09-13-astra-theta-degree-sixteen),
with one additional trailing newline in the local copy. Removing exactly
that final newline gives the source Git blob
`712bb0f0114cbba85e8082c3130ebf09b53e8936`. The authenticated local file has
6,534 bytes and the source file has 6,533 bytes; there is no implementation
change. Both identities are recorded in `SOURCES.json`.
The six-index source replay was used through degree 18 in
[PR #974 at 89c37b6707cb77fc5a86143ea98d8756759fdcbc](https://github.com/GettysburgResearch/riemann/tree/89c37b6707cb77fc5a86143ea98d8756759fdcbc/standalone/2026-10-17-three-route-continuation/lee_yang).
Here it is extended explicitly through degree 20, with every remainder
included. The arithmetic implementation is inherited; the chain moment
recurrence, root, and independent finite enumeration are new.

## 1. Source normalization and statement

For real t≥0, define

$$
\Phi(t)=\sum_{n\ge 1}
 \left(4q_n^2e^{9t/2}-6q_ne^{5t/2}\right) e^{-q_ne^{2t}},
\qquad q_n=\pi n^2,
$$

and extend evenly. We use the classical theta Fourier representation with
the normalization

$$
\Xi(z)=\int_{\mathbb R}\Phi(t) e^{izt}\,dt,
\qquad
\frac{\Xi(z)}{\Xi(0)}
 =\frac{\xi(1/2+iz)}{\xi(1/2)}.
$$

Each summand is positive for t≥0 because q_ne^{2t}>3/2. Set

$$
 Z=\int_{\mathbb R}\Phi(t)\,dt,\qquad
 \rho_\theta(dt)=Z^{-1}\Phi(t)\,dt,\qquad
 v=\mathbb E_{\rho_\theta}T^2,\qquad T_*=T/\sqrt v.
$$

The complete source has every exponential moment. The replay in Section 4
encloses its moments through 20, including normalization, and proves
1/25<v<1/20. Let c_n be the cumulants of a fair sign and put

$$
 s_r=\kappa_{2r}(T_*)/c_{2r},\qquad 1\le r\le 10.
$$

All these denominators are nonzero integers; c_18=209865342976 and
c_20=−29088885112832. Cumulants are the formal derivatives at zero of
the logarithm of a moment generating series with constant term 1. No
logarithm across unknown zeros of Xi is used.

### Theorem T18C

There is a zero-field ferromagnetic Ising measure on a tree with 281 vertices
and 280 edges, together with a nonnegative weighted spin observable Y, such that

$$
 \mathbb E Y^{2r}=\mathbb E T_*^{2r}\quad(1\le r\le 9),
 \qquad \mathbb E Y^{2r+1}=0\quad(r\ge 0).
 \tag{1}
$$

Every edge has a finite, strictly positive coupling satisfying

$$
 10^{-9}<J_e<1/4.\tag{2}
$$

All 280 observed spins have strictly positive weights. One auxiliary hub
has observable weight 0. The characteristic function of Y is entire and
has no nonreal zeros. Its support is contained in (−10,10).

For the first two weighted core spins, designated U_0,U_1 below,

$$
 \frac 1{60}<\operatorname{Cov}(U_0,U_1)<\frac{17}{1000}.\tag{3}
$$

The next standardized moment has a strict nonzero discrepancy:

$$
 \frac{45}{100}
 <\mathbb E Y^{20}-\mathbb E T_*^{20}
 <\frac{451}{1000}.\tag{4}
$$

The root is unique in the specified nine-coordinate cube of radius 10^-30
about the rational center in `chain_parameters.json`, with its other 20
coordinates fixed. This is uniqueness in that cube only. The observable
X=√vY therefore realizes every original, unstandardized theta moment
through degree 18, and its characteristic function also has only real zeros.
In this rescaling, multiply only the observable weights by √v and keep
every coupling fixed. In particular, the relation q_leaf=ηa defines the
standardized construction; it is not recomputed from the rescaled weights.

## 2. The full connected Ising measure

The parameters are

$$
 z=(a_0,a_1,w_0,\ldots,w_{13},q_0,\ldots,q_{12})\in\mathbb R^{29}.
$$

Take a hub ε, 256 leaves of type 0, 10 leaves of type 1, and a chain of 14 core
spins σ_0,…,σ_13. Every leaf is joined to the hub; the hub is joined to
σ_0; consecutive core spins are joined. Thus the graph has
1+256+10+14=281 vertices and 256+10+1+13=280 edges, and is connected and acyclic.

Write η=1/1000. The edge correlations tanh J_e are:

| Edge type | Correlation | Number of edges |
|---|---:|---:|
| Hub to type 0 leaf | ηa_0 |256|
| Hub to type 1 leaf | ηa_1 |10|
| Hub to σ_0 | η |1|
| σ_0 to σ_1 | q_0=0.22713565209564776 |1|
| σ_i to σ_{i+1},1≤i≤12 | q_i=1/100000000 |12|

The decimal in this table is an exact terminating rational. All these
correlations belong strictly to (0,1) throughout the certified cube. Thus
J_e=atanh q_e is a finite, strictly positive coupling. The full probability
of a spin configuration s is

$$
 \mathbb P(s)=2^{-281}\prod_{e=ij}(1+q_es_is_j).\tag{5}
$$

For a tree, this expression is normalized: choose the hub spin uniformly
and independently choose every edge product s_is_j with mean q_e, then
recover each spin along the unique path from the hub. This bijection
between spins and the hub/edge variables proves normalization and proves
that (5) is the usual Gibbs law proportional to exp(Σ_eJ_es_is_j).
It includes every one of the 2^281 configurations.

The observable is

$$
 Y=a_0\sum_{\ell=1}^{256}\sigma_{0\ell}
    +a_1\sum_{\ell=1}^{10}\sigma_{1\ell}
    +\sum_{i=0}^{13}w_i\sigma_i.\tag{6}
$$

The auxiliary hub has weight 0. It remains a vertex with all its incident
couplings. At the rational center, a_0≈0.02332769758,
a_1≈0.10895361771, w_0≈0.47912675565, and w_1≈0.15481470662.
The complete exact center is the parameter file, not these approximations.

The first core pair satisfies Eσ_0=Eσ_1=0 and Eσ_0σ_1=q_0, since the
edge products in the tree description are independent and the hub is fair.
Therefore, for U_i=w_iσ_i,

$$
 \operatorname{Cov}(U_0,U_1)=w_0w_1q_0.\tag{7}
$$

The checker proves (3) directly on the whole parameter cube. It also proves
256a_0+10a_1+Σ_i w_i<10 and the positivity of every observed weight there.
For 0<q<1,

$$
 q<\operatorname{atanh}q\le\frac q{1-q^2}.
$$

The rational checks q>10^-9 and q/(1−q²)<1/4 for every edge type establish (2).

### The exact conditional chain recurrence

Let τ_i=σ_iσ_{i+1}. Conditional on σ_0=1, the τ_i are independent signs
with means q_i. Set recursively

$$
 A_{13}=w_{13},\qquad A_i=w_i+\tau_i A_{i+1}.
$$

Then A_0 has exactly the distribution of the core observable given σ_0=1.
The variable τ_i is independent of A_{i+1}. Its n-th raw moments obey

$$
 G_{13,n}=w_{13}^n,\qquad
 G_{i,n}=\sum_{k=0}^n\binom nk w_i^{n-k}G_{i+1,k}
 \begin{cases}1&k\text{ even},\\q_i&k\text{ odd}.\end{cases}
 \tag{8}
$$

Conditional on ε=1, σ_0 has mean η and is independent of the subsequent
edge products. Hence the conditional core raw moment of order n is
G_0,n for n even and ηG_0,n for n odd. A single leaf of type j contributes
conditional moment a_j^n for n even and ηa_j^{n+1} for n odd.

All leaves and the core are independent given ε. Add their conditional
cumulants, counting the leaf types 256 and 10 times; invert the cumulant
recursion to recover the conditional moments. The hub is a fair sign and
changing it negates the observable in distribution. The unconditional even
moments are the conditional even moments, and the unconditional odd moments
are zero. This proves that the finite recurrence computes the complete
measure (5), without a state cutoff or an independence substitution.

## 3. Exact moment equations and contraction proof

For a raw moment list M_0=1, define its cumulants recursively by

$$
 K_n=M_n-\sum_{j=1}^{n-1}\binom{n-1}{j-1}K_jM_{n-j}.\tag{9}
$$

The inverse identity is

$$
 M_n=\sum_{j=1}^n\binom{n-1}{j-1}K_jM_{n-j}.\tag{10}
$$

Apply (9) to the conditional components in Section 2, sum the cumulants with
the stated integer multiplicities, apply (10), set odd raw moments to zero,
and apply (9) again. Denote the resulting unconditional cumulant of order 2r
divided by c_2r by B_r(z). Every B_r is a polynomial over the rationals in
the 29 parameters. `chain_exact.py` implements (8)–(10); automatic forward
differentiation in `tree_core.py` evaluates the Jacobian by the same exact
polynomial operations. The equations to be solved are

$$
 F_r(z)=B_r(z)-s_r=0,\qquad 1\le r\le 9.\tag{11}
$$

The unknown source constants s_r are enclosed by full theta replay, not
read from a saved moment or solver receipt. Identities(9) and (10) are
triangular, so solving (11) gives all the moment equalities in(1).

Use the active coordinate list(2,13,0,10,1,11,5,3,7), in that order,
and let c be the exact terminating-rational center. Let B be the closed
cube of radius r_0=10^-30 in these nine coordinates, with the other 20 fixed.
The checker first computes the exact rational 9×9 Jacobian J_0=DB(c) in
the active coordinates. It computes its rational inverse R and explicitly
verifies both RJ_0=I and J_0R=I.

The directed interval evaluation then produces rational upper bounds

$$
 \beta\ge\|RF(c)\|_\infty,\qquad
 L\ge\sup_{z\in B}\|I-RDB(z)\|_\infty.
$$

The strict acceptance predicates are

$$
 L<10^{-3},\qquad \beta<r_0/1000,\qquad
 r_0-\beta-Lr_0>99r_0/100.\tag{12}
$$

The accepted receipt has β<2.843·10^-41 and L<4.312·10^-12. These
diagnostic bounds are much smaller than the strict predicates (12); the
acceptance calculation uses exact rational and integer interval bounds.

For the actual theta constants, the Newton map z↦z−RF(z) thus maps B
strictly inside itself and is a strict contraction. Banach's fixed point
theorem yields a unique fixed point in B. Since R is invertible, the fixed
point solves(11). Every positive parameter, coupling, covariance, and
support assertion was checked on B itself, so it holds at this root.

The source extension through 20 enables a separate exact diagnostic.
The checker encloses both c_20(B_10(z)−s_10) and the direct raw difference
M_20(z)−E T_*^20 throughout B. Each lies strictly in(45/100,451/1000).
At the root they are equal because all lower cumulants agree. This proves (4)
and records precisely the finite endpoint of the construction.

### Independent finite enumeration

`chain_controls.py` directly enumerates every one of the 128 configurations
of a seven-vertex tree: a hub, two leaves, and a four-spin core chain with
unequal positive weights and unequal positive edge correlations. It uses
the exact Gibbs product (5) and compares every rational raw moment of
orders 0 through 20 with(8)–(10). It verifies total mass 1 and all odd moments 0.
It also deletes a positive core edge and verifies that the variance changes,
rejecting that erroneous graph. This independent finite enumeration checks
the conditioning, repeated leaves, core orientation, and observable weights.
It does not replace the full-source replay or the contraction argument.

## 4. Complete theta replay through 20

For n=1,…,6, integrate the n-th theta summand to

$$
 U_n=(2,3/2,1,3/4,1/2,3/8)_n.
$$

Use cells of width 1/16, midpoint c, and half-width h=1/32. There are
(32,24,16,12,8,6) cells,98 in total. On each cell, expand the source summand
in(t−c)/hthrough degree D=120 and integrate its product with t^j at the
polynomial level for every j=0,2,…,20. The even full-line factor 2 is kept.
The source code pays the following three remainders for every such j.

### Taylor remainder

On the complex circle|t−c|=1/8, one has|Im t|≤1/8, so Re e^(2t)>0
and|exp(−q_ne^(2t))|≤1. Every center lies below 2; hence Re t<17/8.
For all six explicit indices, q_n<144. With e<3, the prefactor is bounded by

$$
 4\cdot 144^2\cdot 3^{10}+6\cdot 144\cdot 3^6<10^{11}.
$$

Cauchy's coefficient estimate therefore bounds the discarded series on
each real cell by 10^11·4^−121/(1−1/4). Each real t belongs to[0,2], so
t^j≤2^j. The sum of full-line integration lengths is 2Σ_nU_n=49/4<16.
The complete two-sided Taylor error is at most

$$
 E_j=\frac{16\cdot 10^{11}\cdot 2^j}{4^{121}(3/4)}.\tag{13}
$$

Nothing in this argument stops at 18: it applies to j=20 with the explicitly
included factor 2^20. The explicit index range is six throughout.

### Six time tails

For t=U+u, put q=πn², E=e^(2U), and λ=2 qE−9/2. The checker verifies
λ>0 for every explicit index. Dropping the negative prefactor term and using
e^(2u)≥1+2u bounds the full-line tail by

$$
 T_{n,j}=8q^2e^{9U/2-qE}
 \sum_{k=0}^j\binom jk U^{j-k}\frac{k!}{\lambda^{k+1}}.\tag{14}
$$

This is the integral of the binomial expansion of(U+u)^j against
the resulting exponential majorant. All six tails are included.

### All omitted theta indices

At U=0, the same estimate gives
8π²n^4e^(−πn²) j!/(2πn²−9/2)^(j+1). For n≥7 the ratio of consecutive
numerators is at most(8/7)^4e^(−15π)<1/2, while the denominator increases.
The full omitted-index tail is therefore bounded by

$$
 N_j=\frac{16\pi^2\,7^4e^{-49\pi}j!}{(98\pi-9/2)^{j+1}}.\tag{15}
$$

The Taylor error(13) is subtracted from the lower polynomial integral and
added to its upper endpoint. By positivity, the time and index tails(14)
and (15) are added only to the upper endpoint. None of these tails is set
to zero. Normalize by the enclosed positive mass, divide by the appropriate
power of the enclosed variance, and use(9) to get s_1,…,s_10.

### Directed arithmetic and source authentication

Every interval endpoint is an integer divided by 2^320. Addition is exact
at this scale; multiplication and division use integer floor and ceiling.
The inherited square-root routine uses integer square root with an upward
correction. Only integers, rational Fraction values, and these intervals
are used for acceptance. Decimal and NumPy scouts are not imported by the
checker or trusted as targets or roots.

The pi enclosure uses Machin's identity and 96-term alternating arctangent
series, including the first omitted term. The exponential enclosure scales
a nonnegative argument into[0,1/8], uses 96 positive Taylor terms and the
geometric bound starting with term 97, and then squares outward. Negative
arguments use outward reciprocals. Cell coefficients and integrations use
the same directed operations. `certify_chain.py` authenticates the unchanged
`pr886_primitive.py` by SHA-256
`2eba75b7fc82617342c20f6a06270462b6d82f1e7162f66847c029e7e5a9fa55`.

## 5. The real-zero conclusion

The imported result is the finite zero-field ferromagnetic Lee–Yang theorem
with arbitrary nonnegative real observable weights. A precise statement is
Newman and Wu, *Constants of de Bruijn–Newman type in analytic number theory
and statistical physics*,
[arXiv:1901.06596v2, Section 2.5, equation(21) and the following display](https://arxiv.org/html/1901.06596v2#S2.SS5).
It applies to every finite ferromagnetic Gibbs measure with J_ij≥0 and
observable weights λ_i≥0; unequal and irrational weights are allowed.

The version with strictly positive weights already suffices to justify
the auxiliary hub. Give the hub weight δ>0 while leaving the graph and all
couplings fixed. For each δ the characteristic function has no zero in
either open half-plane. As δ decreases to 0, the finite configuration sums
converge uniformly on every compact subset of the complex plane to the
characteristic function of (6). The limit is entire and equals 1 at 0, so
it cannot be identically zero in either half-plane. Hurwitz's theorem
therefore leaves both half-planes zero free. All zeros of the limit are
real. Multiplication of the observable by the positive scalar√v preserves
this conclusion for the unstandardized X.

This proves the real-zero conclusion for the constructed finite-spin law.
The theorem identifies its moments with the theta law only through 18,
and (4) certifies that the functions already differ at order 20. The theorem
does not identify the characteristic function with Xi/Z.

## 6. Reproduction and remaining mathematical gap

From the final packet directory, run standard Python 3:

```sh
sha256sum --check SHA256SUMS
python3 certify_chain.py --check chain_certificate.json
```

The checker regenerates the complete original-theta moments and all tails,
recomputes the exact rational center Jacobian and both inverse identities,
encloses the whole-box Jacobian, verifies every strict acceptance predicate,
runs the exact finite enumeration, and compares the complete receipt.
The rational center file is input to a proof; it is never accepted merely
because an optimizer produced it. Stored source and scout JSON files are
not input to acceptance.

The route to RH still needs ferromagnetic real-zero laws reaching the
original theta targets at unbounded moment orders, with the uniform
convergence and source-identification hypotheses of the all-order consumer.
T18C closes the specific degree 18 finite target left open by the previous
degree 16 work. It supplies no extension rule at arbitrary order and no
estimate controlling the next positive discrepancy. These are distinct,
explicitly open requirements.
