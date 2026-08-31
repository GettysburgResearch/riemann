# Independent audit: the all-weight cusp-flag quotient family

Status: PASS WITH FIXED-WEIGHT ANALYTIC AND POLE BOUNDARIES.
Review date: 2026-08-31.
Programme: #764.

## Exact scientific state

Reviewed source: 43ecb4ac3f2487ee944b6bb6bef72e1ad92f2678.
Authoring base: 8e9f05211954e0a7aae5e63c9367f1d520d3671d.
Imported scientific commit: 31e9d161be24165ad0eb9994b16895e884345690.
The five scientific files are unchanged by this audit.

| Artifact | Frozen Git blob |
|---|---|
| CUSP_FLAG_QUOTIENT_GLOBAL_FAMILY.md | 77820c6af8d089d22547db6cda5ba025ed96f84f |
| cusp_flag_quotient_global_family.py | e3d6fd8aff9e5d65a5d9b692623a4978a3ef4170 |
| cusp_flag_quotient_global_family.json | 326efd383cf0972c4f67a4d003d649cd9f7b895f |
| cusp_flag_quotient_global_family.sources.json | 90dc74d185b0b9a42f865a9f9df895ba7cd1c5dd |
| tests/test_cusp_flag_quotient_global_family.py | e1e3b1574e98bcb5776f48f549e250e6fe8b22a6 |

The first four files are in research/l-families/atlas/generalized/.
Fixture LF-normalized SHA-256:
70812297758842c27af5840f0c31e3e738093d9aad930330588b4f8ed1450b57.

Six exact source bindings retain all five files of the weight-24 parent
b62dfc6348661992bca659c99de226a1b6b22e14 and its independent audit at the
authoring base. All six raw Git identities and LF hashes, and four current
artifact hashes, were independently checked. A local cherry-pick is not
a replacement identity for that original reviewed parent.

## The accepted all-weight theorem

The [proof](CUSP_FLAG_QUOTIENT_GLOBAL_FAMILY.md) uses the actual full
level-one cusp-form space at every fixed even weight with dimension d>=2,
its distinguished cusp/q coordinate, and ell(f)=[q]f.
It does not start with arbitrary coefficient vectors.

### Basis and coefficient nonvanishing

The classical dimension/ring theorem gives k=12d+r,
r in {0,4,6,8,10,14}. The forms
Delta^j E4^(3(d-j)) M_r have unit triangular leading coefficients.
Integral elimination therefore gives the unique Miller basis with
[q^i]f_j=delta_ij for 1<=i,j<=d.

Put N=d+1 and P(q)=product(1-q^n)^(-24N).
The weakly holomorphic form Delta^(-N) M_(14-r) has weight 2-k.
Multiplying it by f_1 gives a weight-two differential with no possible
residue except at the cusp; the total-residue theorem makes that residue
zero. The echelon gap then gives exactly

    c_N = -[q^d](M_(14-r) P).

There are two surviving coefficient contributions, not an arbitrary
truncation of a convolution. Holomorphy at elliptic points is retained.

For K=24(d+1), the colored-partition recurrence and
p_(u-1)<=u p_u/K give

    p_m/p_(m-1) <= (K/m) * 14400/12167 < (6/5) K/m,
    p_d < 44 p_(d-1),  p_d < 3828 p_(d-2).

The negative q coefficients of E10 and E6, and the negative q^2 coefficient
of E14, dominate the indicated partition coefficient. The complementary
E8, E4 and 1 have nonnegative coefficients. Thus c_N>0 for r=0,4,8 and
c_N<0 for r=6,10,14, for every d>=2. This is a written all-weight proof,
not extrapolation from the 138 finite cases.

The coefficient-duality ingredient is classical.
The root visually inspected the complete relevant pages 1, 2 and 5 of
[Duke--Jenkins](https://www.math.ucla.edu/~wdduke/preprints/serre.pdf):
equations (2)--(8), the integral canonical basis, and Corollary 1's
weight-two derivative argument agree with the normalization used here.
The Miller construction is also stated in
[Stein, Lemma 2.20](https://wstein.org/books/modform/modform/level_one.html#the-miller-basis).
The root's PDF-reading workflow was read-only and kept the original
normalizations visible; no PDF was edited or re-exported.

### Global quotient and analytic continuation

For the same completed Eisenstein series as the reviewed parent,

    I_k(s)=A_k(s) zeta(2s) D(w),  w=s+k-1,
    A_k(s)=pi^(-s) Gamma(s) (4pi)^(-s-k+1) Gamma(s+k-1),
    Q_k(s)=det I_k(s)/det I_W(s)=A_k(s) zeta(2s) F_k(w).

The period has only its classical simple poles at 0 and 1 before taking
the quotient. Real-half-line positive definiteness ensures the denominator
determinant is not identically zero. Adapted complex basis changes multiply
both determinants by the same squared absolute determinant.
Thus Q_k is canonical relative to the declared source and functional.

For real s>1 it is the positive minimum over ell(f)=1. For nonreal s the
definition is meromorphic, not a complex-valued minimization problem.
It obeys Q_k(s)=Q_k(1-s), with nonzero residues

    Res_1 Q_k = det G/(2 det G_W),  Res_0 Q_k = -det G/(2 det G_W).

The remaining poles can occur at zeros of det I_W; their existence,
cancellation and distribution are not established. Removing A_k adds no
poles, since its reciprocal is entire. Removing zeta(2s) may add poles.

The Eisenstein normalization and reflected endpoint pole were checked
against [Zagier, Section 1(a)--(c)](https://people.mpim-bonn.mpg.de/zagier/files/scanned/EisensteinRiemannZeta/eisenstein-zeta-978-3-662-00734-1_10.pdf)
in the parent review and again by the independent family reviewer.
The completed series, not an uncompleted Eisenstein normalization, is used.

### Honest inverse words and the two exceptional weights

For each fixed weight the cusp coefficient bound supplies an absolutely
convergent matrix majorant sufficiently far right.
After diagonal scaling of D_W, every tail ratio is at least (d+1)/d>1.
Its maximum absolute row sum tends to zero; hence the Neumann series,
scalar Cauchy products and regrouping are absolutely normally convergent
on a sufficiently right half-plane depending on the weight.

An h-th correction word has frequency

    rho=(n_0 ... n_(h+1))/(j_0 ... j_h),
    n_i>=N, 2<=j_i<=d, rho>=N^2/d * (N/d)^h.

This bounds depth below any cutoff. Also rho>n_i, so the required q order
and every tail-index range are bounded. The support is locally finite.

Normally the uniquely least correction frequency is N^2/d, with coefficient
-c_N^2 b_d(N)^2<0. Its top pivot vanishes only at weights 124 and 248.
Those zero entries remain in the same source matrix. Direct expansion and
f_(d-1)=f_d(j-744) give:

| Weight | Active pivot | Active b(N) | Least fractional frequency |
|---|---:|---:|---:|
| 124 | 9 | 169884 | 121/9 |
| 248 | 19 | 142884 | 441/19 |

At these weights, nonzero top-pivot endpoints must start at N+1.
The strict comparison N^2/(d-1)<(N+1)^2/d and the internal-word factor
N/d>1 rule out every smaller mixed or deeper word. The negative coefficient
there is again uniquely determined, not inferred from a truncated search.

All smaller frequencies are integers. Multiplication by zeta(2s) only
introduces integer-square frequency factors and cannot cancel this first
noninteger term. Uniqueness of absolutely convergent locally finite
generalized Dirichlet series therefore excludes an ordinary integer-frequency
Dirichlet expansion for both F_k and L_k=zeta(2s)F_k, and excludes ordinary
prime Euler products that expand absolutely into such a series.

The first d coefficient directions force any constant full diagonalizing
congruence to be monomial. The N-th direction has at least two nonzero
coordinates, including at the two exceptions, giving the contradiction.
This is a full-diagonalization obstruction, not a block-irreducibility theorem.

## Independent bounded replay

The root inspected the proof, producer, tests and manifest, authenticated
the complete fixture, and ran all 35 tests normally and under Python -O:
4.430s and 4.337s, both PASS. Both complete producer modes, Ruff lint/format,
and the entire authoring-base-to-source whitespace check passed.

The root separately reconstructed all 138 omitted coefficients using a
negative-binomial colored-partition product and Eisenstein coefficients,
with E6 also recovered through the Ramanujan differential identity.
It independently reconstructed all six complete frequency maps using
ordered ungrouped words, rather than the producer's grouped states.
The respective numbers of closing words were 27, 18, 7, 16, 1 and 1.
The zeta-square completions and both exceptional integer values matched.
This independent reconstruction and all source bindings also passed -O.

A separate reviewer read the complete packet and reported no blocking
findings. In addition to its 35-test/producers replay in both modes, it
reconstructed all 138 complete basis digests through Faber/j elimination,
all colored partitions by a product construction, all six published
frequency maps and nine held-out prefixes. Its exceptional prefixes through
cutoff 28 included 1,291 and 53 nonzero ordered correction words.
It also rejected 128 additional hostile type/schema/frequency/source/
artifact/cap/JSON controls in each mode, without editing the author files
or coordinating with their author.

The producer's declared arithmetic/loop budget is bounded and charged
before its specified expansions. It is not a wall-clock bound or a count
of every interpreter instruction. Numeric controls enforce strict types
and bit/dimension/degree/support caps. Complete typed JSON reconstruction,
source identities and artifact hashes govern acceptance; result checks
do not disappear under Python -O.

Reproduction from the repository root:

~~~text
python -B tests/test_cusp_flag_quotient_global_family.py
python -B -O tests/test_cusp_flag_quotient_global_family.py
python -B research/l-families/atlas/generalized/cusp_flag_quotient_global_family.py --check
python -B -O research/l-families/atlas/generalized/cusp_flag_quotient_global_family.py --check
~~~

## Accepted scope and remaining work

This is an all-weight family by a written proof, with a separate analytic
inverse half-plane for each fixed weight. It is not a uniform-in-weight
limit. Classical modularity, Eisenstein continuation and Petersson theory
are imported; exact finite fixtures do not machine-prove them.

The object is a canonical nonlinear quotient of classical global periods.
No new automorphic representation, full block irreducibility, all-purpose
spectral geometry, generalized-prime impossibility, conditional/formal
Euler-product exclusion, complete pole theorem, exhaustive novelty,
RH or GRH consequence is accepted. Real positivity is not complex
zero-freeness. Any further positive-spectrum or pole-distribution theorem
requires a separate source-bound proof and independent review.
