# Coprime infinite-height products with finite corrected physical capture

Status: PROPOSED SYNTHETIC ANALYTIC COUNTEREXAMPLE; independent exact-SHA review required.
Scope: one explicit, nonnative, pure-meromorphic Blaschke pair. RH remains open.
Frozen parents: HC at 90e8dff3d184cbfe59974969ca89615856c33c51 and
LP at 36eddbbf065959f535ca4a7b08455d489ed4bd18. No parent proof is modified.
The finite controls do not machine-certify the infinite-dimensional proof.

## 1. Statement, normalization, and compatible source

Use boundary measure dx and the unitary Fourier convention
\[
 f(z)=(2\pi)^{-1/2}\int_0^\infty h(t)e^{izt}\,dt.
\]
All projections below use this same realization of H^2(C+) as L^2(0,infinity).
Inner products and Gram matrices are conjugate-linear in the first argument.
Set, for n>=1,
\[
 a_n=16\,2^n,\quad \delta_n=2^{-n},\quad
 b_n=a_n+i,\quad u_n=a_n+i(1+\delta_n),                    \tag{CP1}
\]
and let B,U be the pure Blaschke products with these simple zero sets.
For specificity choose factors (1-z/c)/(1-z/bar c), equal to one at z=0.
Write
\[
 P=P_{K_B},\quad K_B=H^2\ominus BH^2,\quad
 P_U=P_{UH^2}=M_U M_U^*,\qquad
 C_I(B,U)=\|\Pi_I P_U P\|_{\mathcal S_2}^2.                \tag{CP2}
\]
Here I is any measurable subset of [0,infinity); traces may initially be infinite.

**Theorem.** B and U extend meromorphically across every finite real point,
have no nonconstant common inner divisor, and BOTH unweighted zero-height
sums are infinite. Nevertheless
\[
 \boxed{\|P_U P\|_{\mathcal S_2}^2<1/9,\qquad
           0\le C_I(B,U)<1/9\quad\hbox{for every }I.}      \tag{CP3}
\]
In contrast, for every positive-measure I in [0,infinity),
\[
 \boxed{\operatorname{tr}(\Pi_I P\Pi_I)=\infty.}           \tag{CP4}
\]
In particular this holds on every interval [A,D] with 0<=A<D<infinity.

Let B_N retain b_1,...,b_N, and P_N=P_(K_(B_N)). With U FIXED at its
infinite product, for every N>=1,
\[
 \boxed{0\le C_I(B,U)-C_I(B_N,U)
  \le\|P_U(P-P_N)\|_{\mathcal S_2}^2
  \le 4^{-N}(2/9+2N/243).}                               \tag{CP5}
\]
Thus the corrected source converges in Hilbert--Schmidt norm, uniformly
over output sets I, in this one fixed configuration. This is not a bound
by the omitted height, which is infinite for every N.

The literal compatible synthetic data may be taken as O=1, numerator N_src=U,
denominator D_src=B, and remainder R_src=U-B. There is no common inner
cancellation in U/B; its reduced Blaschke denominator is B. None of these
objects is the native Xi numerator or denominator.

## 2. Products and their disjoint divisors

The real parts tend to infinity geometrically, and all heights lie in [1,3/2].
For either c_n=b_n or c_n=u_n,
sum 1/|c_n|<infinity and sum Im(c_n)/(1+|c_n|^2)<infinity.
The numerator and denominator genus-zero products defining the specified
factors therefore converge locally normally; their quotient is meromorphic
on C and holomorphic in C+. Equivalently the factors are the usual
unimodularly normalized Blaschke factors, with the displayed Blaschke sum
finite; their product is PURE, with no added singular or exponential factor.
It is inner, with exactly the stated zeros and their reflected lower poles.
There is no finite real accumulation, and no real zero or pole.

Different indices have different real parts, while u_n differs in height
from b_n. Hence the zero divisors are disjoint. Any common inner divisor
of two pure products must itself be a Blaschke product supported on their
common zeros, so it is constant. Both height sums diverge since every height
is at least one. Every origin-centered disk |z|<=R retains a finite initial
prefix of the b_n (possibly empty), since |b_n| increases strictly.

## 3. A literal Riesz basis, with bounded inverses justified

The normalized Hardy kernel at b_n has inverse transform
\[
 e_n(t)=\sqrt2\,e^{-(1+ia_n)t},\quad
 G_{mn}=\langle e_m,e_n\rangle
       ={2\over 2+i(a_n-a_m)}.                           \tag{CP6}
\]
It belongs to K_B since evaluation at a zero annihilates BH^2.
For m!=n,
\[
 |G_{mn}|\le {1\over8|2^n-2^m|}.
\]
For a fixed n the lower-index reciprocal sum is at most
(n-1)/2^(n-1)<=1 (zero at n=1); the upper-index sum is at most
sum_(m>n) 2^(-(m-1))=2^(1-n)<=1. Thus
\[
 \sup_n\sum_{m\ne n}|G_{mn}|\le1/4,\qquad
             (3/4)I\le G\le(5/4)I.                       \tag{CP7}
\]
For finite vectors this follows directly by 2|x_m x_n|<=|x_m|^2+|x_n|^2;
extension by density gives the bounded self-adjoint Gram operator on ell^2.

The synthesis map T:c -> sum c_n e_n consequently extends boundedly,
is bounded below, and has closed range. Its range is all of K_B:
a Hardy function orthogonal to every e_n vanishes at every b_n; canonical
Hardy factorization makes it divisible by the PURE factor B. A vector
also in K_B must therefore be zero. This proves completeness, not merely
linear independence or an upper frame estimate.
Hence G=T^*T is boundedly invertible on all of ell^2, Q=T G^(-1/2) is an
isometry onto K_B, and
\[
             P=T G^{-1}T^*,\quad \|G^{-1}\|\le4/3.        \tag{CP8}
\]
All finite prefixes and all restricted tail families inherit CP7.

## 4. Correct projection, global trace, and bare divergence

Evaluation of M_U f at b gives M_U^* e_b=bar U(b)e_b. Since M_U is an
isometry,
\[
 P_U e_b=\overline{U(b)}\,U e_b,\qquad
                 \|P_Ue_b\|^2=|U(b)|^2.                 \tag{CP9}
\]
This can also be checked from the Hardy kernel
i/[2pi(z-bar b)], normalized using K_H(b,b)=1/(4pi Im b).
The formula is for P_(UH^2), not for P_(K_U)=1-P_U.

Removing the factor at u_n leaves an inner factor of modulus at most one.
Therefore, with p_n=delta_n^2/(2+delta_n)^2,
\[
 |U(b_n)|^2\le\left|{b_n-u_n\over b_n-\bar u_n}\right|^2
 =p_n<4^{-n}/4,\qquad
             \sum_n |U(b_n)|^2<1/12.                    \tag{CP10}
\]
Tonelli/the orthonormal-coordinate definition of the Hilbert--Schmidt norm
gives ||P_U T||_HS^2=sum_n ||P_Ue_n||^2. Thus P_U T is Hilbert--Schmidt.
Using Q from CP8 now proves
\[
 \|P_U P\|_{\rm HS}^2=\|P_UQ\|_{\rm HS}^2
 =\operatorname{tr}(G^{-1}T^*P_U T)
 \le {4\over3}\sum_n |U(b_n)|^2<1/9.                     \tag{CP11}
\]
The trace identity is legitimate: T^*P_U T=(P_UT)^*(P_UT) is positive
trace class, G^(-1) is bounded, and cyclicity may be applied in this ideal.
No unbounded inverse Gram or formal infinite matrix trace is used.
Contraction by Pi_I proves CP3, even for the entire output half-line.

Conversely CP8 and G^(-1)>=(4/5)I give P>=(4/5)TT^*.
For every positive-measure I, all e_n have the same strictly positive mass
m_I=integral_I 2exp(-2t)dt. Extended positive traces and Tonelli imply
tr(Pi_I P Pi_I)>=(4/5)sum_n m_I=infinity. This proves CP4.
One can instead first use any finite prefix and let its dimension grow;
no infinite trace is subtracted. LP's low-pass theorem agrees with this,
but CP4 also covers shifted bands for THIS construction.

Do not replace P_U by M_U in CP11. The numerator-transmitted quantity
T_I(B,U)=||Pi_I M_U P||_HS^2 is different. Its global version is infinite
because M_U is an isometry and dim K_B=infinity. We make no assertion
about its bounded-band values for this pair.

## 5. Orthogonal-prefix tail: the overlap correction is essential

Put E_N=K_B ominus K_(B_N), and let T_+ synthesize e_n for n>N.
The residual synthesis S_N=(1-P_N)T_+ has range E_N and Riesz bounds
3/4 and 5/4. Indeed, for finite tail coefficients a,
\[
 \|S_Na\|^2=\inf_c\|T_Nc+T_+a\|^2
              \ge(3/4)\|a\|^2,\qquad
 \|S_Na\|^2\le(5/4)\|a\|^2.
\]
The infimum is over the finite prefix coefficients. Density and the
closed-range bound show that its range is E_N. Thus the CP8 argument gives
\[
 \|P_U(P-P_N)\|_{\rm HS}^2
                 \le(4/3)\|P_U S_N\|_{\rm HS}^2.         \tag{CP12}
\]

For n>N and m<=N, CP6 gives |G_mn|<=1/(4*2^n), whence the cross Gram
R_N=T_N^*T_+ satisfies
\[
 \|R_N\|_{\rm HS}^2\le N4^{-N}/48,\qquad
 \|P_NT_+\|^2
 =\|T_NG_N^{-1}R_N\|^2
 \le(4/3)\|R_N\|^2\le N4^{-N}/36.                       \tag{CP13}
\]
Here ||T_NG_N^(-1)||^2=||G_N^(-1)||<=4/3.
The squared Hilbert--Schmidt triangle bound and ideal inequality give
\[
 \begin{split}
 \|P_US_N\|_{\rm HS}^2
 &\le2\|P_UT_+\|_{\rm HS}^2+2\|P_UP_NT_+\|_{\rm HS}^2\\
 &\le2\left({4^{-N}\over12}
         +\|P_UP_N\|_{\rm HS}^2\,{N4^{-N}\over36}\right)\\
 &\le2\,4^{-N}(1/12+N/324).
 \end{split}                                             \tag{CP14}
\]
We used CP10 and ||P_UP_N||_HS^2<=||P_UP||_HS^2<1/9.
Combining CP12--CP14 proves the last bound in CP5.

Compatible orthonormal bases for P_N and its orthogonal complement give
\[
 C_I(B,U)-C_I(B_N,U)=\|\Pi_I P_U(P-P_N)\|_{\rm HS}^2.
\]
All quantities are finite by CP3; equivalently this is additivity of the
nonnegative ONB squared-norm series on the INPUT subspaces. The rate tends
to zero since N<=2^N. This proves CP5 and Hilbert--Schmidt convergence,
including for geographic disks via Section 2. The fixed U is never
truncated in this theorem. A naked kernel-tail sum is not identified
with the orthogonal source tail.

## 6. Exact finite interface and provenance

For finite controls use unnormalized inverse kernels v_b(t)=exp(-(eta+ia)t),
so every matrix has Gaussian rational entries with no square-root samples.
Let V collect a finite B prefix and W a finite U prefix. Put
G_0=V^*V, D= W^*W, R=W^*V, and J=diag(bar U_M(b_j)).
The producer reconstructs the SAME physical Gram in two ways:
\[
 H_{\rm values}=J^*G_0J,\qquad
 H_{\rm Schur}=G_0-R^*D^{-1}R,\qquad
 C_{\rm finite}=\operatorname{tr}(G_0^{-1}H).              \tag{CP15}
\]
The second route uses P_(U_M H^2)=1-P_(K_(U_M)), not a generic matrix
substitution. It is a full matrix identity before taking its trace.
Finite U_M is used only to test this exact identity; it is not silently
substituted for the fixed infinite U in CP3 or CP5.
Models with M<N deliberately lack some matching numerator factors and
must NOT be assigned CP10's all-node bound.

The finite normalized B-Gram determinant is also rebuilt by
\[
 \det(2G_0)=\prod_{j<k}
 { (a_j-a_k)^2\over (a_j-a_k)^2+4}>0,                     \tag{CP16}
\]
the Cauchy determinant identity; independent tests use permutation/cofactor
and exact complex Gram--Schmidt routes. Row bounds, matching pseudohyperbolic
factors, reciprocal geometric tails, the overlap correction CP13--CP14,
and strict coprimeness are separately checked; band mass is kept symbolic.
No transcendental numerical integration, sampled eigenvalue, or finite
panel is used to prove an infinite limit.

Arithmetic is MIXED: EXACT_RATIONAL and CERTIFIED_INTEGER_COVERAGE.
Gaussian rationals are pairs of Fraction, never Python complex or float.
Public rational components have at most 32 bits; internal components at
most 4096 bits; matrix degree<=4, index<=8, work<=200000, UTF-8 bytes<=2000000.
Complete typed reconstruction, strict bool/int separation, duplicate/nonfinite
JSON rejection, primitive source locks, four artifact locks and a payload
seal are mandatory. These finite controls do not certify complex analysis.

Both complete frozen parent notes were personally read. HC supplies the
correct C-versus-T operator interface and earlier sparse B example; LP
supplies the bare low-pass equivalence and its scope barriers. They are
authenticated by commit, Git blob and LF-normalized SHA-256.

A targeted primary-source literature check read
[Boricheva, arXiv:2203.15372v1](https://arxiv.org/html/2203.15372v1),
the introduction, Section 2.2/Theorem A, and Section 2.4's projection/model
operator formulas. These record the classical reproducing-kernel projection,
Riesz-basis and distance framework. The proofs needed here are written above;
we do not import its compactness criterion as a Hilbert--Schmidt theorem.
The cited paper's P_theta projects onto K_theta; our P_U projects onto its
orthogonal complement U H^2. Remote bytes are not authenticated offline.
No exhaustive novelty search or new abstract Hardy-theory claim is made.

## 7. Exact refutation and remaining native burden

This explicit source refutes the proposed generic implication:
"coprime reduced pure denominator of infinite height plus an infinite-height
pure numerator forces divergent corrected physical capture."
Here the denominator is already reduced, its bare trace diverges on EVERY
positive-length band, yet even the GLOBAL corrected physical trace is <1/9.

It does not decide the actual Xi ratio, its maximal common factor,
the size of its numerator on denominator zeros, Riesz properties of its
kernel family, native outer-normalized jets, physical-T uniformity, total
Pick charge, reverse-Rolle descent, critical-line density, RH, or GRH.
The native missing gate remains a source-specific estimate for P_U P_(K_B);
neither height alone nor coprimeness supplies it.

Smallest result-invalidating burdens: CP9's adjoint/conjugation convention,
CP7--CP8's infinite Riesz completeness, or CP12--CP14's orthogonal-tail
estimate. Each is proved explicitly, with finite exact controls kept separate.
