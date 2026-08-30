# Actual cusp periods: off-central real zeros of the full determinant

Status: PROPOSED SOURCE-SPECIFIC THEOREM; independent frozen-SHA review required.
This packet adds five files and changes no parent. Its conclusion concerns the
FULL period determinant, not an uncancelled zero of the first-coefficient flag
quotient. It is not a zeta/RH counterexample, a new automorphic representation,
or a general theorem about every proposed Riemann structure.

The source is CF1--CF4 of the level-one family at
b69c854d9e3dd1db7b82d95fe6f032fe47d5306b. The manifest also pins EF's analytic
context at a27781310ded92125ef16d97d78db4d97cec4c1b and the authoring-base note
at 24bfc73fc9aa3ba115902340affa8727dfa18970. No signed counting law is needed
below. Seven frozen blobs and the four non-fixture artifacts are authenticated.
Remote primary-source bytes are not authenticated.

## 1. Precise result and unchanged source

Let k=12d, d>=512, and let I_k(s) be the full CF period matrix on
S_k(SL(2,Z)), in its real integral Miller basis. Put
\[
 h_d=\Delta E_4^{3d-3},\qquad
 I_h(s)=\int_{\mathcal F}y^k|h(z)|^2E^*(z,s)\,\frac{dx\,dy}{y^2}.
                                                               \tag{CZ1}
\]
The witness h_d is CF1's g_1, NOT Miller f_d: the latter equals Delta^d
in this residual class. We have [q]h_d=1, where q=exp(2*pi*i*z).
We prove
\[
 I_{h_d}(1/2)>0\quad(k=12d>=6144).                         \tag{CZ2}
\]
Consequently det I_k has a zero s_k in (1/2,1), and a reflected zero
1-s_k in (0,1/2), of the same positive multiplicity. The determinant is
not identically zero. No simplicity, uniqueness, sharp onset, location
estimate, or determinant sign change is asserted.

For W=ker([q]) and Q_k=det I_k/det I_W, cancellation remains open. In
particular CZ2 does NOT assert a net zero or pole of Q_k at either point.

## 2. Eisenstein normalization, derived rather than switched

Use exactly CF2's sign-identified primitive sum:
\[
 E^*(z,s)=\pi^{-s}\Gamma(s)\zeta(2s)
 \sum_{\Gamma_\infty\backslash SL_2(\mathbb Z)}\Im(\gamma z)^s.
                                                               \tag{CZ3}
\]
For Re(s)>1, decomposing a nonzero lattice pair into its positive gcd
gives the equivalent half-lattice Mellin formula
\[
 E^*(z,s)=\frac12\int_0^\infty t^{s-1}
 \sum_{(m,n)\ne(0,0)}e^{-\pi t|mz+n|^2/y}\,dt.             \tag{CZ4}
\]
This fixes all factors of two. Poisson summation in n for m!=0 gives
sqrt(y/t) times the sum over ell of
exp(-pi*y*(m^2*t+ell^2/t))*exp(2*pi*i*m*ell*x).
The m=0 terms give Lambda(2s)y^s; the ell=0 terms give
Lambda(2s-1)y^(1-s), where Lambda(u)=pi^(-u/2)Gamma(u/2)zeta(u).
For m*ell!=0 the Mellin integral is
\[
 \int_0^\infty t^{s-3/2}e^{-\pi y(m^2t+\ell^2/t)}dt
 =2|\ell/m|^{s-1/2}K_{s-1/2}(2\pi|m\ell|y).
\]
Its factor 2 cancels the 1/2 in CZ4. For each n>0 there are two
same-sign divisor pairs m*ell=n. Joining positive and negative Fourier
frequencies then gives
\[
 E^*(z,s)=\Lambda(2s)y^s+\Lambda(2s-1)y^{1-s}
 +4\sqrt y\sum_{n\ge1} n^{s-1/2}\sigma_{1-2s}(n)
 K_{s-1/2}(2\pi ny)\cos(2\pi nx).                         \tag{CZ5}
\]
The Fourier sum converges locally normally near s=1/2 for y bounded
below by a positive number; exponential Bessel decay dominates the
divisor factors and their locally bounded parameter derivatives.
The classical continuation therefore makes this equality valid there.

Write gamma for Euler's constant. The zeta Laurent expansion and
Gamma duplication give
\[
 \Lambda(1+\epsilon)=\epsilon^{-1}+c+O(\epsilon),\quad
 \Lambda(\epsilon)=-\epsilon^{-1}+c+O(\epsilon),\quad
 c=(\gamma-\log(4\pi))/2.
\]
For example psi(1/2)=-gamma-2log2 gives the first constant; reflection
Lambda(u)=Lambda(1-u) gives the second. Taking the cancelling limit in
CZ5 yields the actual central value
\[
 E^*(x+iy,1/2)=\sqrt y(\log y+\gamma-\log(4\pi))
 +4\sqrt y\sum_{n\ge1}\tau(n)K_0(2\pi ny)\cos(2\pi nx).
                                                               \tag{CZ6}
\]

Normalization discrepancy retained explicitly: Zagier's scanned equation
(14), printed p.278, displays 2*sqrt(y) in its cosine sum, although its
equations (4)--(6) fix CZ3--CZ4. Under those definitions this is a factor-two
discrepancy. CZ4's calculation above, not that printed coefficient, is
load-bearing here. Venkatesh's independent equation (10.6), printed p.1068,
has 4*sqrt(y), with equation (10.5) fixing the same completion. That printed
cosine has y where the periodic coordinate must be x; CZ4 derives the phase
as m*ell*x explicitly. No source is silently renormalized or edited.

## 3. Uniform elementary bounds on the whole fundamental domain

Take the standard domain F: |x|<=1/2, |z|>=1, and put
a=sqrt(3)/2, r=exp(-2*pi*y). Thus y>=a. The elementary inequalities
3<pi<4, 0<gamma<1, 2<e<3 will suffice. For reproducible finite
reductions, positive exponential Taylor sums give
\[
 \sum_{n=0}^6\frac{5^n}{n!}>100,\qquad
 \sum_{n=0}^4\frac{3^n}{n!}>16,\qquad
 \sum_{n=0}^4\frac{4^n}{n!}>32.                            \tag{CZ7}
\]
The estimate e<3 follows by comparing 1/n! for n>=2 with 2^(-(n-1)),
with strict inequality for n>=3. Also sqrt(3)>5/3, so pi*sqrt(3)>5;
CZ7 implies r<1/100 throughout F. These are rigorous envelopes, not
floating evaluations of pi, gamma, exponentials or periods.

From K_0(t)=integral_0^infinity exp(-t*cosh u)du and cosh u>=1+u^2/2,
\[
 K_0(t)\le e^{-t}\sqrt{\pi/(2t)}.
\]
The divisor pairing bound tau(n)<=2sqrt(n), including square n, gives
the following bound for the entire nonconstant term in CZ6:
\[
 |\mathcal R(x,y)|\le4\frac{r}{1-r}<4/99<1.              \tag{CZ8}
\]
Every bound here is uniform in x, with no cancellation of Fourier terms.

Since sigma_3(n)<=n^4, let
\[
 C(r)=\frac{1+11r+11r^2+r^3}{(1-r)^5},\qquad
 \sum_{n\ge1}n^4r^n=rC(r).
\]
The identity follows by applying (r*d/dr)^4 to (1-r)^(-1).
All coefficients in C's power series are positive, hence C is increasing
on [0,1). Exact rational substitution gives C(1/100)<2 and
240*(1/100)*C(1/100)<3. Therefore on F
\[
 |E_4|<4,\qquad |E_4-1|\le480r.                          \tag{CZ9}
\]
Delta's product and log(1+u)<=u give
\[
 |\Delta|\le r\exp(24r/(1-r))<e/100<1.
\]
For the lower bound use |1-q^n|>=1-r^n and the elementary finite-product
inequality product(1-u_i)>=1-sum u_i, 0<=u_i<=1. Apply it to 24 copies
of each r^n and take decreasing limits of positive products. It gives
\[
 |\Delta/q|\ge\prod_{n\ge1}(1-r^n)^{24}
 \ge1-24r/(1-r)>25/33>1/2.                              \tag{CZ10}
\]

On a<=y<=32, |log y|<4: a>1/2 and log32<4 by CZ7. Also
|gamma-log(4*pi)|<3 because 4*pi<16<e^3. With sqrt(y)<6 and CZ8,
\[
 |E^*(z,1/2)|<43\quad(y\le32).                           \tag{CZ11}
\]
For y>=32, log y+gamma-log(4*pi)>log2>1/2; the last inequality follows
by integrating 1/t>1/2 on 1<t<2. Since sqrt(y)>5 and CZ8<1,
\[
 E^*(z,1/2)>1\quad(y\ge32).                              \tag{CZ12}
\]
Finally area(F)<=1/a<2 by containment in the strip y>=a.

## 4. Compact negative mass and a positive cusp slab

For h_d from CZ1 and k=12d, CZ9--CZ10 give on y<=32
\[
 y^k|h_d|^2\le32^k4^{6d-6}\le64^k.
\]
Using CZ11 and area(F)<2, all possibly negative mass is bounded below
by -86*64^k, and hence by -100*64^k. CZ12 says the rest is positive.

Put L=k/(4*pi) and integrate only the unit-width slab
|x|<=1/2, L<=y<=L+1. For k>=6144, L>k/16>=384>32, so this rectangle
is wholly inside F. On it r<=exp(-k/2). For every real k>=24 the function
k*exp(-k/2) is decreasing. CZ7 gives e^12>16^4=65536 and hence
240*24*e^(-12)<1/2. In particular 480*e^(-k/2)<1 and
\[
 |E_4|^{6d-6}\ge(1-480e^{-k/2})^{k/2-6}
 \ge1-240k e^{-k/2}>1/2.                                 \tag{CZ13}
\]
Here the exponent is a nonnegative integer, so Bernoulli's inequality
applies; replacing k/2-6 by k/2 only weakens the lower bound.
By CZ10, |h_d|^2>e^(-4*pi*y)/8 throughout this same slab. Combining
CZ12 with dmu=dx*dy/y^2 and integrating a pointwise lower bound gives
\[
 I_{h_d}(1/2)>
 \frac18 L^{k-2}e^{-k-4\pi}-100\,64^k.                    \tag{CZ14}
\]
The integral is finite by cusp decay, and no unweighted measure has
replaced the native y^k*dmu. Both lower bounds are simultaneous for all x.

## 5. The all-weight threshold, not a finite sample

Using pi<4 and e<3 in the positive term of CZ14 gives
\[
 \frac18 L^{k-2}e^{-k-4\pi}
 >\frac{32}{k^2 3^{16}}\left(\frac{k}{48}\right)^k.
\]
Thus strict positivity follows from
\[
 \left(\frac{k}{3072}\right)^k>rac{25}{8}3^{16}k^2.
                                                               \tag{CZ15}
\]
For EVERY integer k>=6144, the left side is at least 2^k. The sequence
2^k/k^2 is strictly increasing for integers k>=3, because
\[
 2k^2-(k+1)^2=k^2-2k-1>0;
\]
the polynomial is positive at 3 and has successive difference 2k-1>0.
At k=6144, use 25/8<2^2, 3^16<2^26 and 6144^2<2^26. The right side
of CZ15 is therefore <2^54, while 2^6144>2^54. Monotonicity then proves
CZ15 for every integer k>=6144, not only a tested list. Restricting to
multiples of 12 proves CZ2. The elementary threshold is deliberately
conservative; no claim of first onset or failure at lower weight is made.

## 6. Whitened inertia, the actual determinant, and reflection

CF2's meromorphic integration has only simple entry poles at 0 and 1.
For real s in (0,1), E*(z,s) is real, so I_k(s) is Hermitian; in the
fixed real coefficient basis it is real symmetric. Entries are analytic,
and therefore continuous, on this interval and at s=1/2. CF4 gives
\[
 I_k(s)=\frac{G}{2(s-1)}+H_k(s),                           \tag{CZ16}
\]
where G is the positive definite Petersson Gram and H_k is holomorphic
near 1. For this fixed k, whiten by the CONSTANT positive square root
G^(-1/2). The whitened matrix is Id/(2(s-1))+G^(-1/2)H_k(s)G^(-1/2).
The latter term has bounded operator norm on a small real neighborhood
of 1. Thus the whitened matrix, and by congruence I_k(s), is negative
definite for real s<1 sufficiently close to 1.

At s=1/2 the nonzero vector representing h_d has positive quadratic
value by CZ2, so the largest eigenvalue of I_k(1/2) is positive. Choose
s_1<1 close enough that all eigenvalues are negative. On [1/2,s_1],
the largest eigenvalue is continuous: for Hermitian matrices A,B the
Rayleigh supremum gives |lambda_max(A)-lambda_max(B)|<=||A-B||.
The intermediate value theorem supplies s_k strictly between these
endpoints with lambda_max(I_k(s_k))=0. Hence det I_k(s_k)=0.
The determinant is not identically zero because I_k(s) is positive
definite for real s>1. Its zero order is therefore finite and positive.

Entrywise E*(z,s)=E*(z,1-s) implies I_k(s)=I_k(1-s), not just an
equality of signs. Substituting the analytic Taylor series at s_k
shows det I_k(1-s_k)=0 of exactly the same order. The two zeros are
distinct and off the central point. This argument does not assume
simple eigenvalue branches or a sign change of the determinant.

## 7. A native W witness and the precise uncancelled boundary

The property [q]h_d=1 does not make CZ2 a minimization or positivity
statement for Q at s=1/2. CF3's positive Schur minimization was proved
only for real s>1. Indefinite restrictions cannot be treated that way.

Indeed fix any integer j>=2 and let d>=j grow. The ACTUAL form
\[
 h_{d,j}=\Delta^j E_4^{3(d-j)}\in W
\]
has leading term q^j. The compact estimate remains -100*64^k because
|Delta|<1 and 4^(6(d-j))<=2^k. Put L_j=k/(4*pi*j). For sufficiently
large k at this fixed j, L_j>=32 and
240*k*exp(-k/(2j))<1/2. Repeating CZ13--CZ14, now using
|Delta/q|^(2j)>2^(-2j), gives
\[
 I_{h_{d,j}}(1/2)>
 2^{-2j-1}\left(\frac{k}{4\pi j}\right)^{k-2}
 e^{-k-4\pi j}-100\,64^k>0                               \tag{CZ17}
\]
eventually. The final dominance follows by taking logs of the ratio:
it is k*log(k)-O_j(k)-2*log(k), which tends to infinity. The preceding
small-error condition follows from k*exp(-k/(2j))->0. These elementary
limits are part of the written proof, not outputs of finite sampling.
Thus W itself has a positive central direction eventually and, by
the same whitened argument using G_W, det I_W also has off-central
real zeros. No common threshold with CZ2 is asserted for all j, nor
are the full and minor zero locations asserted equal or different.

At any common location s_0 the exact unpaid test is
\[
 \operatorname{ord}_{s_0}Q_k
 =\operatorname{ord}_{s_0}\det I_k
  -\operatorname{ord}_{s_0}\det I_W.                       \tag{CZ18}
\]
Proving det I_W(s_k)!=0 would suffice to retain a zero of Q, but has
not been done. Nor has a relative positive-inertia gap between full
space and W been established. Separate positive vectors on the two
spaces provide no such gap. The full-parent obstruction is therefore
the conclusion; an uncancelled flag obstruction remains a new gate.

## 8. Exact replay, primary inputs, and scope

The producer verifies rational/Taylor envelope reductions in CZ7--CZ15,
including the all-integer induction's base and difference polynomials.
It constructs native q-prefixes of Delta^j*E4^(3(d-j)) at d=2,3,512,513,1024
and j=1,2 through q^8. Its Delta logarithmic-derivative recurrence is
compared with the authenticated frozen family's product/E4-E6 construction.
Tests independently expand E4 powers by the finite binomial formula.
These prefixes verify source identity and finite algebra, NOT positivity
of an analytic period, an eigenvalue calculation, or a zero census.

Arithmetic taxonomy: MIXED, with CERTIFIED_INTEGER_COVERAGE and EXACT_RATIONAL
components. No rounding is used. Pi, gamma, exponentials and integrals remain
symbolic in the analytic argument. Public finite controls cap dimension at
1024, q order at 8, exponents at 3072, rational/integer bits at 4096, source
and JSON bytes at 2,000,000, total JSON nodes at 20,000, and charged work at
2,000,000 units. Source-family
primitive work is separately capped at 100,000. These computational caps do
not restrict the all-d theorem. Schema reconstruction distinguishes bool
from int, rejects duplicates/nonfinite JSON/type drift, and authenticates
literal frozen Git blobs plus LF-normalized SHA-256. All four artifact hashes
and a canonical payload digest are checked. Passing finite replay does not
machine-certify analytic continuation, period bounds, inertia, or CZ17's limit.

Primary references inspected:

- [Zagier, Eisenstein series and the Riemann zeta-function](https://people.mpim-bonn.mpg.de/zagier/files/scanned/EisensteinRiemannZeta/eisenstein-zeta-978-3-662-00734-1_10.pdf),
  section 1, equations (4)--(6), (14)--(17), printed pp.276--278:
  the classical lattice completion, continuation, reflection and Bessel
  representation. The Fourier discrepancy is documented in section 2 above.
- [Venkatesh, Sparse equidistribution problems, period bounds and subconvexity](https://annals.math.princeton.edu/wp-content/uploads/annals-v172-n2-p05-p.pdf),
  equations (10.5)--(10.6), printed pp.1067--1068: independent corroboration
  of the same completion and the coefficient 4. The PDF skill was used for
  read-only visual inspection of normalization; no PDF was changed.
- CF1's classical modular-form ring, product and integral basis inputs are
  retained with the exact source bindings, including its Duke--Jenkins and
  Miller/Stein references. No eigenform, Euler-product, or Hecke-diagonal
  assumption is added to h_d or to the full period matrix.

Cusp localization, positive-residue inertia and the intermediate value
argument are classical mechanisms. The bounded literature check is not an
exhaustive priority search; no novelty of the mechanism or abstract zero
theory is claimed. This is a source-specific test of the existing arithmetic
parent. It makes no claim about Riemann zeta zeros, RH/GRH, every weight,
every minor, a novel automorphic family, or uncancelled Q zeros.

Replay from the repository root:

```text
python -B -m unittest discover -s tests -p test_cusp_period_off_central_real_zeros.py
python -B -O -m unittest discover -s tests -p test_cusp_period_off_central_real_zeros.py
python -B research/l-families/atlas/generalized/cusp_period_off_central_real_zeros.py --check
python -B -O research/l-families/atlas/generalized/cusp_period_off_central_real_zeros.py --check
```

Both emission modes, Ruff, and the complete authoring-base-to-frozen-head
whitespace check are additional release gates. Independent proof review is
required before scientific acceptance.
