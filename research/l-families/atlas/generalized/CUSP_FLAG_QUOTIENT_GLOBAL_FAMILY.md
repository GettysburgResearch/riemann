# Cusp-flag quotient: the level-one global family

Status: PROPOSED THEOREM WITH CLASSICAL INPUTS; frozen-SHA independent review
is required. This is a new five-file packet, not a change to its reviewed parent.

Scope: every fixed even weight k with d=dim S_k(SL(2,Z))>=2; the canonical
first-Fourier-coefficient quotient of its full Rankin--Selberg period matrix.
Meromorphy, reflection, real-half-line positivity, nonzero endpoint residues,
failure of constant full diagonalization, and an ordinary-frequency obstruction.
There is NO assertion uniform in weight, full block irreducibility, new
automorphic representation, exhaustive novelty, RH, or GRH.

Exact lineage: scientific parent b62dfc6348661992bca659c99de226a1b6b22e14,
independent audit/authoring base 8e9f05211954e0a7aae5e63c9367f1d520d3671d.
The manifest authenticates the parent's five files and that audit by frozen
Git blob and LF-normalized SHA-256. Classical modularity and Eisenstein
continuation are imported, not machine-proved; remote paper bytes are not locked.

What is computed: exact integral echelon bases by two constructions, a third
coefficient-duality calculation, all six residual classes for 2<=d<=24,
and complete bounded rational-frequency prefixes. These are finite replays,
not evidence substituted for the all-weight proof below.

Smallest uncontrolled analytic boundary: additional poles at zeros of the
denominator period determinant. No cancellation/distribution theorem is claimed.

## 1. The source and canonical integral basis

Use q=exp(2*pi*i*z), Gamma=SL(2,Z), and constant-term-one Eisenstein series

    E4=1+240 sum sigma_3(n)q^n,  E6=1-504 sum sigma_5(n)q^n,
    Delta=(E4^3-E6^2)/1728=q product_(n>=1)(1-q^n)^24.

The classical ring/dimension theorem writes uniquely

\[
 k=12d+r,\quad r\in\{0,4,6,8,10,14\},\quad
 M_r=1,E_4,E_6,E_4^2,E_4E_6,E_4^2E_6,                  \tag{CF1}
\]

respectively, with dim S_k=d. Write M_r=E4^a E6^b. The d forms

\[
 g_j=\Delta^jE_4^{3(d-j)}M_r,\qquad 1\le j\le d,
\]

have integral coefficients and leading term q^j. They are independent and
therefore a basis. Unit-pivot elimination gives a unique integral basis f_j
with [q^i]f_j=delta_ij for 1<=i,j<=d. Uniqueness follows because these first
d coefficient functionals are independent. This is the classical Miller
basis; replacing E4^(3(d-j)) by E6^(2(d-j)) gives the same echelon basis.
In particular f_d=Delta^d M_r, without any later elimination changing it.

Let ell(f)=[q]f, W=ker ell=span(f_2,...,f_d), N=d+1, and

    c_n=[q^n]f_1,   b_j(n)=[q^n]f_j  (2<=j<=d).

The source is the entire actual cusp-form space, its specified cusp/q
coordinate, and normalized functional ell, not an arbitrary coefficient array.

## 2. Period, quotient and precise analytic scope

Use dmu=dx dy/y^2 and the sign-identified Gamma_infinity quotient in

\[
 E^*(z,s)=\pi^{-s}\Gamma(s)\zeta(2s)
 \sum_{\gamma\in\Gamma_\infty\backslash\Gamma}
                  \operatorname{Im}(\gamma z)^s.
\]

Its classical meromorphic continuation has exactly the simple poles 0,1,
residues -1/2,+1/2, and reflection E*(z,s)=E*(z,1-s). For real s>1 it is
positive. Cusp decay against its locally uniform moderate growth justifies
meromorphic integration of

\[
 I_{ij}(s)=\int_{\Gamma\backslash\mathbb H}
 y^k\overline{f_i(z)}f_j(z)E^*(z,s)\,d\mu(z).
\]

Writing w=s+k-1, unfolding gives

\[
 I_k(s)=A_k(s)\zeta(2s)D(w),\quad
 D_{ij}(w)=\sum_{n\ge1}a_i(n)a_j(n)n^{-w},
\]
\[
 A_k(s)=\pi^{-s}\Gamma(s)(4\pi)^{-s-k+1}\Gamma(s+k-1).
                                                               \tag{CF2}
\]

The real coefficient basis makes D symmetric. The original period remains
sesquilinear, conjugate-linear in its first input. For Re(s)>1 absolute
convergence of diagonal series follows by Tonelli from the positive unfolded
integral, and cross convergence follows by Cauchy--Schwarz.

Let I_W,D_W denote the restrictions to W. Define

\[
 Q_k=\frac{\det I_k}{\det I_W}=A_k\zeta(2s)F_k,\quad
 F_k=B-C^tD_W^{-1}C,\quad
 B=\sum c_n^2n^{-w},\quad C_j=\sum_{n\ge N}c_nb_j(n)n^{-w}.
                                                               \tag{CF3}
\]

The determinant denominator is not identically zero: the period is positive
definite for real s>1. Thus the quotient is meromorphic. A constant adapted
basis change has matrix [[1,0],[t,T]], T invertible, and acts by Hermitian
congruence. Both determinants acquire |det T|^2. This proves canonicity
relative to the specified source/ell, including complex adapted changes.

For real sigma>1 completion of squares gives

    Q_k(sigma)=min_{ell(f)=1} I_sigma(f,f)>0,

with unique minimizer f_1 plus W-coordinates -I_W^(-1)I_(W,1).
This is not a definition by minimization at nonreal s. Entrywise reflection
gives Q_k(s)=Q_k(1-s), NOT a bare reflection equation for D or F_k.

Let G be the Petersson Gram. The period residue matrix is +/-G/2; G and
G_W are positive definite. Determinant orders d and d-1 give exactly

\[
 \operatorname{Res}_{s=1}Q_k=\frac{\det G}{2\det G_W}>0,
 \qquad \operatorname{Res}_{s=0}Q_k=-\frac{\det G}{2\det G_W}. \tag{CF4}
\]

Away from these endpoints, poles can occur only at zeros of det I_W.
Locally their order is max(ord(det I_W)-ord(det I_k),0); numerator zeros
may cancel them. No existence or cancellation claim is made. Removing A_k
adds no poles since 1/A_k is entire; dividing further by zeta(2s) may add
poles. Reflection and Schwarz conjugation preserve the completed divisor.

## 3. All-weight nonvanishing of the first omitted coefficient

This proof, rather than a finite search, removes the condition c_N!=0.
Put K=24(d+1) and P(q)=product(1-q^n)^(-K)=sum p_m q^m. All p_m are positive.
The weakly holomorphic form

    H=Delta^(-d-1) M_(14-r)

has weight 2-k. Therefore f_1 H has weight two, is holomorphic on the upper
half-plane, and has a possible pole only at the cusp. Its invariant
differential descends holomorphically at elliptic points to the compact
modular curve; the sole possible residue is at the cusp, so it is zero.
Equivalently every such weight-two form is a derivative of a polynomial in j.
Consequently its constant Fourier coefficient vanishes. The echelon gap
leaves precisely two contributing terms, giving

\[
 c_N=-[q^d]\big(M_{14-r}P\big).                            \tag{CF5}
\]

This is a special case of classical coefficient duality, not a new duality
claim. Here is an elementary uniform-in-d sign argument for this particular
coefficient; it is not a uniform-in-weight analytic inverse estimate.
The logarithmic derivative of P gives

\[
 m p_m=K\sum_{h=1}^m\sigma_1(h)p_{m-h},\qquad
 p_{u-1}\le(u/K)p_u.
\]

For 1<=m<=d, repeated use of the second inequality implies
p_(m-h)/p_(m-1)<=(d/K)^(h-1). Since sigma_1(h)<=h^2 and d/K<1/24,

\[
 \frac{p_m}{p_{m-1}}
 \le\frac Km\sum_{h\ge1}h^2 24^{-(h-1)}
 =\frac Km\frac{14400}{12167}<\frac65\frac Km.             \tag{CF6}
\]

For d>=2, K/d<=36 and K/(d-1)<=72. Thus

    p_d<44 p_(d-1),   p_(d-1)<87 p_(d-2),
    p_d<3828 p_(d-2).

For r=4 or 8 the complementary series is E10 or E6, whose nonconstant
coefficients are negative and whose q coefficients are -264 or -504.
Their first negative term already exceeds p_d in magnitude. For r=0 the
complement is E14=1-24 sum sigma_13(n)q^n; its q^2 coefficient -196632
exceeds p_d/p_(d-2). Hence [q^d](M_(14-r)P)<0 in these three cases.
For r=6,10,14 the complement is E8,E4,1, with nonnegative coefficients,
so that coefficient is positive. We have proved for EVERY d>=2:

\[
 c_N>0\ (r=0,4,8),\qquad c_N<0\ (r=6,10,14).              \tag{CF7}
\]

## 4. Analytic inverse and honest frequency words

Fix one weight throughout this section. The cusp bound |f(z)|y^(k/2)=O(1)
and Fourier extraction at y=1/n give a_i(n)=O_k(n^(k/2)). Consequently all
following absolute majorants converge sufficiently far right. Set

\[
 D_W=\operatorname{diag}(2^{-w},\ldots,d^{-w})+R(w),\quad
 S(w)=\operatorname{diag}(2^{w/2},\ldots,d^{w/2}),
 \quad H(w)=SRS,\quad x(w)=SC.
\]

Then D_W=S^(-1)(1+H)S^(-1). The entrywise absolute majorant for H at
sigma=Re(w) has entries sum_(n>=N)|b_i(n)b_j(n)|(n/sqrt(ij))^(-sigma).
Each ratio is >=N/d>1. Dominated convergence from any abscissa of absolute
convergence makes its maximum row sum tend to zero as sigma tends to infinity.
Choose W0(k) with that row sum eta<1. The absolute majorants for x also
converge there, since n/sqrt(j)>1. Thus

\[
 F_k=B-x^t\sum_{h\ge0}(-H)^h x                             \tag{CF8}
\]

converges normally and absolutely on Re(w)>=W0(k). For example, the sum
of absolute scalar terms is at most (d-1)||x_abs||_infinity^2/(1-eta).
The transpose is appropriate to the real coefficient basis and analytic
continuation in w; it does not conjugate w. No common W0 for varying k is claimed.

Expanding an h-th correction word gives

\[
 \rho=\frac{n_0\cdots n_{h+1}}{j_0\cdots j_h},\qquad
 n_i\ge N,\quad 2\le j_i\le d,\qquad
 \rho\ge\frac{N^2}{d}(N/d)^h.                             \tag{CF9}
\]

Its signed coefficient is (-1)^(h+1) times
c_(n0)c_(n_(h+1)) b_(j0)(n0)b_(jh)(n_(h+1))
product_(i=1..h) b_(j_(i-1))(n_i)b_(ji)(n_i).
Absolute convergence legitimizes all Cauchy products and regrouping.
Below any cutoff CF9 bounds h. For fixed h each integer n_i is bounded;
indeed rho>=n_i(N/d)^(h+1)>n_i. The j_i already have finite ranges.
Thus the rational support is locally finite, not merely a formal series.

## 5. First fractional frequency, with both exceptions retained

The top coefficient is explicitly

\[
 b_d(N)=[q]M_r-24d,
 \qquad [q]M_r=0,240,-504,480,-264,-24.                    \tag{CF10}
\]

For d>=2 it vanishes EXACTLY at (d,r)=(10,4),(20,8), i.e. k=124,248.
At every other weight CF9 has equality only for h=0, n0=n1=N, j0=d.
Hence the first correction is the unique nonzero term

\[
 \rho_* = N^2/d=d+2+1/d,\qquad
 [\rho_*^{-w}]F_k=-c_N^2b_d(N)^2<0.                       \tag{CF11}
\]

All smaller frequencies come from B and are integers; rho_* is not an integer.

At an exceptional weight f_d=q^d+v q^(d+2)+..., with v=-27000,-54000.
Indeed [q^2](Delta/q)^d=288d^2-36d, so using [q]M_r=24d gives
v=[q^2]M_r-288d^2-36d, where [q^2]E4=2160 and [q^2]E4^2=61920.
With j=E4^3/Delta=q^(-1)+744+196884q+..., uniqueness of echelon form yields

    f_(d-1)=f_d(j-744),
    b_(d-1)(N)=196884+v=169884,142884,

respectively. These are genuinely nonzero; the vanished top pivot is NOT
silently replaced in the source. It is retained as zero in the same D_W.
For every nonzero word endpoint, j<d forces n/sqrt(j)>=N/sqrt(d-1), and
j=d forces n>=N+1. For d>=3,

    N^2/(d-1)<(N+1)^2/d,

since the cross-multiplied difference is d^2-d-4>0. Each internal word
factor n/sqrt(ij)>=N/d>1. Thus every nonzero exceptional correction obeys

\[
 \rho\ge\frac{N^2}{d-1}(N/d)^h.                           \tag{CF12}
\]

Equality occurs only for h=0, n0=n1=N, j0=d-1. The first fractional terms are

| Weight | d | Frequency | Coefficient in w coordinates |
|---|---:|---:|---|
| 124 | 10 | 121/9 | -(274199916600352164708 * 169884)^2 |
| 248 | 20 | 441/19 | -(56759176303803625378304458445779330578 * 142884)^2 |

The displayed c_N values are exact finite computations; their nonvanishing
already follows without computation from CF7.

For every weight, multiplication by
zeta(2s)=sum_(a>=1) a^(2k-2)(a^2)^(-w) leaves the first fractional coefficient
unchanged. For a>=2 a contributing lower F_k frequency would precede the first
fractional frequency and hence be an integer. Multiplying it by a^2 cannot
give a noninteger. The completed support remains locally finite and absolutely
convergent on a sufficiently right half-plane.

Uniqueness follows by subtracting two absolute generalized series, selecting
the least nonzero frequency, multiplying by its w-th power, and letting real
w tend to infinity. Domination at a fixed convergence abscissa justifies the
limit. The union with ordinary integer frequencies is still locally finite.
Thus F_k and L_k=zeta(2s)F_k have NO absolutely convergent ordinary Dirichlet
series in s on a right half-plane. The shift w=s+k-1 only rescales coefficients.
This excludes normalized ordinary-prime Euler products whose expansion into
integer frequencies converges absolutely. It excludes neither generalized
prime/norm systems nor merely formal, conditional, or engineered products.
Changing the completion or multiplying by arbitrary factors changes the object.

## 6. Constant full diagonalization is impossible

If one fixed invertible complex C diagonalized I_k(s) by congruence for all s,
ordinary Dirichlet uniqueness would make every transformed coefficient vector
have at most one nonzero coordinate. The vectors for n=1,...,d are the standard
coordinate vectors. Each row of C must therefore have just one nonzero entry;
invertibility forces their columns distinct, so C is monomial. But the vector
at N has both c_N and b_d(N) nonzero, or c_N and b_(d-1)(N) at the two exceptions.
A monomial map preserves this support size, a contradiction.
This excludes full diagonalization by one constant congruence, NOT every
nontrivial block decomposition, parameter-dependent diagonalization, or every
possible representation of the scalar. Nor can Q_k be a constant linear
combination of the period entries: division by A_k zeta(2s) would give an
ordinary Dirichlet series for F_k.

## 7. Bounded replay and source/search boundary

The producer constructs both integral bases through q^(d+2) for all 138 pairs
2<=d<=24 and the six r values. It compares complete coefficient arrays, then
records their canonical digest and leading data. Delta's product is checked
against (E4^3-E6^2)/1728; the two bases use E4^3 and E6^2 respectively.
The independent colored-partition recurrence checks CF5 and the sign bounds.
Every row retains b_d(N), including both zeros.

For example, all six residual classes at d=3 give first frequency 16/3:

| Weight | c_4 | b_3(4) |
|---|---:|---:|
| 36 | 57093088 | -72 |
| 40 | 19291168 | 168 |
| 42 | -9436928 | -576 |
| 44 | 3953248 | 408 |
| 46 | -1515968 | -336 |
| 50 | -161408 | -96 |

The coefficient is minus the square of the product in each row. For weight
36 this is -16897873695195856896. Further examples in the fixture include
weight 48 (d=4, first frequency 25/4) and weight 60 (d=5, first frequency 36/5).

Complete word prefixes are replayed for (d,r,cutoff)=(2,0,12),(3,0,10),
(3,14,8),(4,0,10),(10,4,14),(20,8,24). CF9 bounds inverse depth; rho>n_i
shows that q coefficients through floor(cutoff) suffice, including every
unseen tail index. Endpoint states are pruned only when even the minimum
closing index N cannot fit. Zeta square frequencies are added exactly.
Tests independently enumerate ungrouped words and compare all grouped maps.

The public caps are d<=24, q order<=28, cutoff<=28, primitive rational bits<=32,
internal integer/rational bits<=4096, state count<=4096, output support<=1024,
and 20,000,000 charged arithmetic/loop units. Charges precede declared loop
expansions; this is not a count of all interpreter instructions or a wall-clock
bound. Duplicate/nonfinite JSON, type drift (including bool/int and float/int),
missing/extra fields, source drift, artifact digest drift and cap violations
fail closed. Full typed canonical reconstruction is the acceptance rule.
No numerical period, zero, gamma or zeta sampling is performed.

Primary sources and the bounded search performed on 2026-08-31:

- [Duke--Jenkins, On the zeros and coefficients of certain weakly holomorphic
  modular forms](https://www.math.ucla.edu/~wdduke/preprints/serre.pdf),
  equations (2)--(8), Corollary 1 and its weight-two derivative proof: the
  integral canonical basis and coefficient duality used in CF5. This is a
  classical ingredient, not a priority claim for the present construction.
- [Stein, Modular Forms, A Computational Approach, section 2.3](https://wstein.org/books/modform/modform/level_one.html#the-miller-basis),
  Lemma 2.20: Miller's integral echelon basis with the triangular E4/E6/Delta
  construction. The original Miller thesis is cited there through Lang;
  it was not directly inspected here.
- [Miller--Schmid](https://arxiv.org/pdf/math/0605783), introduction (1.7)--(1.14),
  for unfolding. Its introductory omission of the reflected completed pole
  at zero is corrected by the following primary source, as in the parent.
- [Zagier, Eisenstein series and the Riemann zeta-function](https://people.mpim-bonn.mpg.de/zagier/files/scanned/EisensteinRiemannZeta/eisenstein-zeta-978-3-662-00734-1_10.pdf),
  section 1(a)--(c), equations (3)--(17): completed poles, reflection, moderate
  growth and the rapidly decreasing period. These analytic inputs are imported.
- [Anderson--Trapp, Shorted Operators II (1975)](https://doi.org/10.1137/0128007):
  the positive-form/Schur quotient operation is classical. CF3 has its own
  finite-dimensional proof, not an uninspected operator-theorem dependency.
- [Boecherer--Chiera (2008)](https://www.numdam.org/item/AIF_2008__58_3_801_0/):
  adjacent Rankin--Selberg/Petersson continuation and Gram computations, not
  identification of this particular s-dependent flag quotient.

Targeted searches combined Rankin--Selberg with Schur complement, determinant
quotient, quotient metric, Gram matrix and period matrix. They located the
classical operations and adjacent period literature but did not identify an
exact prior match in the inspected results. This is a bounded search, not
an exhaustive literature review or evidence of global novelty. The PDF
workflow was used for the primary coefficient-duality source; no source
PDF was edited or re-exported.

The 35 tests include a separate Delta logarithmic-derivative construction,
independent ungrouped word enumeration, and exact reduction to the frozen
weight-24 parent's frequency fixture. The report charges 6,696,953 of
20,000,000 work units. Replay commands, from the repository root:

```text
python -B -m unittest discover -s tests -p test_cusp_flag_quotient_global_family.py
python -B -O -m unittest discover -s tests -p test_cusp_flag_quotient_global_family.py
python -B research/l-families/atlas/generalized/cusp_flag_quotient_global_family.py --check
python -B -O research/l-families/atlas/generalized/cusp_flag_quotient_global_family.py --check
```

Ruff lint/format and the authoring-base-to-head whitespace check are additional
nonmathematical gates. Passing replay does not certify the classical imports
or analytically prove CF2--CF12.
