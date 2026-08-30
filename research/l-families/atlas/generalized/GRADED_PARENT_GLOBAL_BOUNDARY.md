# From formal graded parents to global analytic boundaries

Status: proposed reviewable mathematics; classical theorem applications and
native deductions, with exact finite controls. Independent frozen-SHA review
is required. No novelty, automorphy or RH claim.

Programme: #764 generalized L-objects.
Claims: GLO764.GRADED_GLOBAL_BOUNDARY_V1,
GLO764.GRADED_DIMENSION_GROWTH_V1, and
GLO764.GRADED_CENTER_COMPLETION_PRICE_V1.

Mathematical parent: the finite-graded classification and its independent
audit at e2f469142cd55086e74751293877ab533001e786. Both remain unchanged.
The companion manifest identifies the exact Git blobs and LF hashes.

## 1. The actual global scalar model

For integers n>=1 and k>=0, let d_n(r) be the coefficient of r^(-s) in
zeta(s)^n, and set
\[
 D_{n,k}(s)=\sum_{r\ge1}\frac{d_n(r)^k}{r^s}.
\tag{GB1}
\]
The coefficients are positive integers; k=0 means the constant power one.
At every prime, d_n(p^j)=binomial(j+n-1,n-1). This is the identity-Satake
specialization of the parent's universal local object, not a statement about
an arbitrary family of nonidentity Frobenius matrices.

Write a=n-1 and d=ka+1. The parent proves
\[
 F_{n,k}(T)=\sum_{j\ge0}\binom{j+a}{a}^kT^j
          =\frac{H_{n,k}(T)}{(1-T)^d}.
\tag{GB2}
\]
For n,k>=2 the integer polynomial H has constant term one, degree
q=(k-1)a, and q distinct simple negative roots. In particular,
\[
 H(T)=\prod_{i=1}^q(1+B_iT),\qquad B_i>0\ \hbox{distinct},\qquad
 \sum_iB_i=h_1=n^k-d.
\tag{GB3}
\]
These all-order root and degree results have a native proof in the frozen
parent. They are not inferred from the finite census below.

The local series is analytic for |T|<1. For any fixed sigma_0>1,
F(p^(-sigma))-1=O_(n,k,sigma_0)(p^(-sigma)) uniformly in sigma>=sigma_0.
This follows directly by bounding its polynomially growing coefficients at
p^(-sigma)<=2^(-sigma_0). Positivity and the convergent sum over primes give
absolute convergence of (GB1) for Re s>1, locally uniform there, and
\[
 D_{n,k}(s)=\zeta(s)^d\prod_p H_{n,k}(p^{-s}).
\tag{GB4}
\]
This does not say D is zero-free on that half-plane. Numerator Euler factors
can vanish there. Real D(sigma)>0 for sigma>1, so its ordinary real logarithm
is unambiguous.

## 2. Exact meromorphy classification

The elementary exceptions are
\[
 n=1\ \hbox{or}\ k=0:\ D=\zeta(s),\qquad
 k=1:\ D=\zeta(s)^n,\qquad
 (n,k)=(2,2):\ D=\frac{\zeta(s)^4}{\zeta(2s)}.
\tag{GB5}
\]
The last identity uses H_(2,2)=1+T and
(1+T)/(1-T)^3=(1-T^2)/(1-T)^4.

For every other pair n,k>=2, the line Re s=0 is a meromorphic natural
boundary of D: no point on that line has a neighborhood admitting meromorphic
continuation from the right. Nevertheless D continues meromorphically to
Re s>0.

Here is the exact external theorem used. Estermann's integer-polynomial
theorem applies to h(0)=1 and h(T)=product_i(1-alpha_i T) in Z[T].
It gives continuation of product_p h(p^(-s)) to Re s>0, and makes every
point of Re s=0 a meromorphic natural boundary unless all |alpha_i|=1.
The precise one-variable statement is reproduced in Delabarre, Section 1.2,
printed p.227; no hypothesis from his later multivariable theorem is imported.

To check the noncyclotomic hypothesis, one can use h_1>q from the parent.
For later quantitative purposes we record the stronger bound
\[
 h_1\ge2q,\qquad A=\max_i B_i>2.
\tag{GB6}
\]
Indeed h_1-2q=(a+1)^k-(3k-2)a-1. For a>=2, its k=2 value is a(a-2)>=0.
For a=1 start at k=3, where it is zero. Its increment in k is
a((a+1)^k-3)>0 in both ranges. Equality occurs only at (n,k)=(3,2),(2,3).
Here q>=2, and distinctness makes the maximum strictly greater than the
average, hence A>2. Estermann now applies to H with alpha_i=-B_i.

Multiplying by zeta(s)^d cannot remove a natural boundary: any hypothetical
meromorphic germ of D can be divided by this nonzero meromorphic germ.
The same argument excludes rescue by any nonzero meromorphic multiplier
defined at the boundary point. This is an imported classical theorem
application, not a new natural-boundary theorem.

## 3. The meromorphic exception still fails ordinary completion

For D_(2,2), meromorphy alone does not supply an ordinary functional equation.
In fact D_(2,2) has infinitely many poles in 0<Re s<1/2, and is holomorphic
in 1/2<Re s<1.

For a proof requiring no RH, zero-density theorem, or multiplicity estimate,
let Z be the set of distinct zeta zeros in 0<Re rho<1, and put
\[
 E=\{\rho\in Z:\zeta(\rho/2)\ne0\}.
\tag{GB7}
\]
Every zero reaches E after finitely many successive halvings. Otherwise
zeros would approach zero, contradicting zeta(0)=-1/2. If E were finite,
every rho in Z would be 2^j alpha for some alpha in E. But
2^j Re alpha<1 permits only finitely many j for each such alpha. This would
make Z finite, contradicting its known infinitude. Thus E is infinite.

For each rho in E, the denominator zeta(2s) vanishes at s=rho/2 while the
numerator zeta(s)^4 is nonzero. The pole order equals the multiplicity of
rho. Conversely zeta(2s) is nonzero when Re s>1/2, and the numerator has no
pole in the open right half of the critical strip. This proves the claimed
asymmetry. It does not assert that every scaled zeta zero is uncancelled.

Let M be any nonzero meromorphic function with only finitely many zeros and
poles in 0<Re s<1. Then F=M D_(2,2) still has infinitely many left-strip
poles and at most finitely many right-strip poles. It cannot obey
\[
 F(s)=\eta\,\overline{F(1-\bar s)},\qquad \eta\ne0,
\tag{GB8}
\]
as a meromorphic identity: reflection pairs these poles bijectively.
The plain equation F(s)=eta F(1-s) is excluded for the same reason.

In particular this excludes every ordinary finite-gamma completion
\[
 M(s)=e^{cs+c_0}R(s)\prod_{\nu=1}^N
                    \Gamma(a_\nu s+b_\nu)^{e_\nu},
\tag{GB9}
\]
with N finite, R a nonzero rational function, integer e_nu, real nonzero
a_nu and arbitrary complex b_nu. Standard positive slopes are included.
Gamma divisor points are (-b_nu-j)/a_nu, j>=0; only finitely many lie in
the bounded real-part strip. Rational and exponential factors preserve
this property.

Unlike the natural-boundary assertion, this no-rescue conclusion does NOT
cover arbitrary meromorphic multipliers. Multiplication by the arithmetic
factor zeta(2s), followed by the ordinary gamma factor, produces the completed
fourth power of zeta. That multiplier has the excluded infinite cancellation.

Thus, within the unmodified scalar family (GB1), ordinary same-center
finite-gamma completion is possible exactly in the elementary chambers
n=1 or k in {0,1}. They are powers of the usual completed zeta function.
For a nonexceptional pair, reflection together with the known continuation
on Re s>0 would extend the completed function across Re s=0, contradicting
Section 2.
No assertion is made about alternative dual Euler products or a different
notion of completion.

## 4. Exponential growth of the formal graded dimensions

Fix a nonexceptional pair n,k>=2. Order B_1=A>B_2>...>B_q>0 and put
beta=max(1,B_2)<A. The parent's unique formal graded factorization has integer
dimensions w_m defined by
\[
 F(T)=\prod_{m\ge1}(1-T^m)^{-w_m},\qquad
 b_m=m[T^m]\log F(T)=d+(-1)^{m+1}\sum_iB_i^m,
\]
\[
 mw_m=\sum_{r\mid m}\mu(r)b_{m/r}.
\tag{GB10}
\]
Integrality is supplied by the integer formal Euler transform; it does not
follow merely from positivity of the B_i. For m>1 the d terms cancel.
Separate r=1 and bound every proper divisor exponent m/r by m/2 to obtain
\[
 w_m=\frac{(-1)^{m+1}A^m}{m}
 +O_{n,k}\left(\frac{\beta^m+\tau(m)A^{m/2}}m\right).
\tag{GB11}
\]
All constants are for this fixed pair; no uniform n,k estimate is asserted.
Since tau(m)<=m, the error is o(A^m/m). Consequently every sufficiently
large grade has nonzero dimension, eventually positive for odd m and
negative for even m. Nonzero dimension implies a nonzero virtual class;
positive dimension does not establish effectivity of that class.

With logarithms normalized by their Taylor series on |T|<1, the local
graded logarithm is absolutely convergent exactly when |T|<1/A. At
|T|=1/A its absolute terms are asymptotic to 1/m. This is a convergence
boundary for this expansion, not a natural boundary of the rational F.
Ordered convergence on that circle holds except at T=-1/A, by separating
the geometric harmonic main term in (GB11) from an absolutely summable
remainder. At T=-1/A the real logarithm tends to minus infinity and the
partial products tend to the actual zero of F.

For real sigma>1, log zeta(m sigma)=2^(-m sigma)+O_sigma(3^(-m sigma)).
The remainder estimate follows, for large m, from the absolutely convergent
Dirichlet series and its logarithm; finitely many initial m do not matter.
Therefore
\[
 |w_m\log\zeta(m\sigma)|
 \sim\frac{(A\,2^{-\sigma})^m}{m}.
\tag{GB12}
\]
The ordered global graded logarithm sum_m w_m log zeta(m sigma) converges
absolutely exactly for sigma>sigma_*=log(A)/log(2)>1. Below sigma_*, but
still above one, its terms fail to approach zero. This can happen while
the original positive Dirichlet series is absolutely convergent.

At the real endpoint sigma=sigma_* the series instead converges CONDITIONALLY:
its main term is (-1)^(m+1)/m and its remainder is absolutely summable.
It equals log D(sigma_*). To justify the value, for sigma>sigma_* absolute
convergence permits interchanging grades and primes. On a closed short
interval starting at sigma_*, the remainders converge uniformly absolutely;
the alternating main series converges uniformly from above, with tail at
most 1/(M+1). Taking sigma down to the endpoint gives the identity by
continuity of D on the real half-line.

No logarithm on all of Re s>1 is asserted. In fact, at
s=sigma_*+(2l+1)pi i/log(2), l integer, the prime-two numerator has its
simple zero -1/A; every other prime factor is nonzero because its argument
has modulus below 1/A. Thus D has zeros inside Re s>1.

The exact held-out pair H_(2,3)=H_(3,2)=1+4T+T^2 has A=2+sqrt(3).
The inequalities sqrt(8)<A<4 show that the unmodified graded zeta product
fails its term test at sigma=3/2, but converges absolutely at sigma=2.
The ordinary Dirichlet series converges absolutely at both values.

## 5. Constructive control: the price of centering the grades

Let Lambda_zeta(s)=pi^(-s/2)Gamma(s/2)zeta(s), with its usual meromorphic
reflection equation. An affine graded argument g_d(s)=ds+c preserves the
same center exactly when
\[
 g_d(1-s)=1-g_d(s),\qquad c=(1-d)/2.
\tag{GB13}
\]
Hence the modified object
\[
 D^{\rm cent}_{2,2}(s)=\frac{\zeta(s)^4}{\zeta(2s-1/2)},\qquad
 \Lambda^{\rm cent}_{2,2}(s)
 =\frac{\Lambda_\zeta(s)^4}{\Lambda_\zeta(2s-1/2)}
\tag{GB14}
\]
does have a same-center meromorphic functional equation. Its gamma multiplier
is pi^(-s-1/4) Gamma(s/2)^4/Gamma(s-1/4), an ordinary finite quotient.

This changes the local object: its prime factor is
(1-sqrt(p)T^2)/(1-T)^4, not (1-T^2)/(1-T)^4. Its coefficient at p^2 is
10-sqrt(p), whereas the original D_(2,2) coefficient is nine. In particular,
for every 0<epsilon<1/4,
|10-sqrt(p)|/(p^2)^epsilon tends to infinity over primes. The usual
coefficient Ramanujan bound is lost. More generally centering grade d
replaces T^d by p^((d-1)/2)T^d.

This is an explicit completed meromorphic toy and an exact local price,
not a Selberg-class member, an automorphic construction, or a rescue of the
unchanged parent. Infinite arithmetic poles and negative virtual grades
are not ruled out by its functional equation alone.

## 6. Computation and provenance boundary

The companion producer replays the full rectangle 1<=n<=5, 0<=k<=5,
through grade 24. It checks finite-difference numerators and a vanishing
tail, direct divisor-power coefficients, Newton sums against Euler logarithms,
Mobius inversion against independent triangular factor elimination, all
exception identities, the strengthened first-coefficient inequality,
the quadratic exact control, and grade-center affine identities.
Synthetic halving forests and pole-order controls check the combinatorial
logic; they are not actual zeta zero samples.

Supported maxima are n,k<=5 and grade<=32. Exact integers/rationals have
explicit type, size and work-budget guards. The manifest authenticates the
frozen proof and review, with unchanged current bytes; artifact hashes bind
the note, producer, tests and manifest. Fixture acceptance requires complete
typed canonical-JSON equality to a source-authenticated rebuild.

No floating roots, logarithms, zeta values, prime samples, or fitted
asymptotics are used. Arithmetic is exact integer/rational, with algebraic
roots and logarithmic thresholds represented symbolically. The computation
does not prove Estermann, the infinite halving lemma, meromorphic continuation,
or convergence thresholds; those have the written/imported proofs above.

    python -B research/l-families/atlas/generalized/graded_parent_global_boundary.py --check
    python -B -O research/l-families/atlas/generalized/graded_parent_global_boundary.py --check
    python -B -m unittest discover -s tests -p test_graded_parent_global_boundary.py
    python -B -O -m unittest discover -s tests -p test_graded_parent_global_boundary.py

The smallest load-bearing failures would be a wrong frozen root theorem,
a misapplied one-variable Estermann hypothesis, or an invalid infinite
halving argument. Finite agreement alone cannot discharge them.

## 7. Established sources and research meaning

Estermann's 1928 theorem is the source of the natural-boundary result:
[original publication](https://academic.oup.com/plms/article/s2-27/1/435/1579152),
DOI 10.1112/plms/s2-27.1.435. The exact applicable statement was checked in
[Delabarre, Section 1.2, p.227](https://www.numdam.org/item/10.24033/bsmf.2647.pdf).
Only that one-variable theorem is imported.

Dahlquist, *On the analytic continuation of Eulerian products*, Arkiv for
Matematik 1 (1952), 533--554, Section 1.2 p.534 and Lemma 2.1 pp.536--537,
already explains why an unmodified infinite zeta product can fail and why
small primes must be separated:
[primary paper](https://archive.ymsc.tsinghua.edu.cn/pacm_download/116/6867-11512_2007_Article_BF02591361.pdf),
[publisher record](https://doi.org/10.1007/BF02591361).
The formal-product warning is not new.

The standard zeta facts used in Section 3 are recorded in
[DLMF 25.10](https://dlmf.nist.gov/25.10),
[DLMF 25.6.1](https://dlmf.nist.gov/25.6.E1), and
[DLMF 25.2](https://dlmf.nist.gov/25.2); gamma divisor facts in
[DLMF 5.2](https://dlmf.nist.gov/5.2); the completed zeta reflection in
[DLMF 25.4](https://dlmf.nist.gov/25.4).

The programme gain is a precise distinction between a formal graded parent,
global meromorphy, ordinary completion, and a changed centered-grade model.
These are useful design constraints and constructive controls. They do not
establish unexplored priority or supply a new genuine arithmetic L-function.
