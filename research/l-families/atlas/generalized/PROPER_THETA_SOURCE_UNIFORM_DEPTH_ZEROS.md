# Effective growing-depth real zeros of proper native theta quotients

This is a uniform strengthening of the accepted fixed-depth and
effective-first-depth corollaries. It concerns different native source
quotients at different depths, all formed BEFORE Mellin observation.

## 1. Exact inputs and claim

The source spaces, quotient completion and central criterion are those of
[TQ](PROPER_THETA_SOURCE_REAL_ZERO_COROLLARY.md), science
`0d1f90323c8d61abefee077b7bcaa4c024596a55`, independently reviewed at
`31e5ca265cc3be43cff30962041d93a2be4d8ee2`.
The elementary Gamma and exponential bounds are also proved in
[E96](PROPER_THETA_SOURCE_EFFECTIVE_WEIGHT96.md), science
`6e47a4b2604668eb88b977c9182f5a04a214638a`, reviewed at
`43c36f4c462bb008d7fb744ca52768d2591b1822`.

The NEW arithmetic input here is the FULL off-diagonal Petersson formula,
not HC20's diagonal estimate alone:
[Iwaniec--Luo--Sarnak, Section 2, (2.1)--(2.3), (2.7)--(2.9),
Proposition 2.1, printed pp68--69](https://www.numdam.org/article/PMIHES_2000__91__55_0.pdf).
Those pages were read visually in the original PDF, including the
Fourier and Petersson normalizations. Only this unconditional formula is
used; no RH-dependent result elsewhere in that paper is imported.

**Theorem.** For EVERY integer j>=1 and EVERY even integer k>=96j, the
actual proper theta-source quotient associated with

    V_(k,j)={f in S_k : a_f(1)=...=a_f(j-1)=0},
    W_(k,j)={f in V_(k,j) : a_f(j)=0}

has positive central value L_(k,j)(1/2)>0 and a reflected sign-changing
real zero pair in (0,1/2) and (1/2,1). Its entire pole-cleared completion
s(s-1)L_(k,j)(s) retains that pair.

Thus the permitted depth grows linearly with weight. The theorem is not
an assertion of many distinct pairs in ONE fixed quotient: each j labels
a different source quotient. There is no optimality, simplicity,
uniqueness, weight24 result or12j/k location law.

## 2. Source-normalized coefficient Gram matrix

Put nu=k-1 and

    A_m=Gamma(nu)/(4*pi*m)^nu.

Let P_m be the ordinary holomorphic Poincare series reproducing the
m-th coefficient, with HC's sign-identified cusp stabilizer. In our
conjugate-linear-FIRST Petersson convention,

    G(P_m,f)=A_m a_f(m).

Set v_m=P_m/sqrt(A_m), for1<=m<=j, and let

    K_mn=G(v_m,v_n).                                          (U1)

This is an actual Hermitian Gram matrix. ILS uses the opposite linearity
convention. Translating its (2.3),(2.7) gives K_mn=Delta_(k,1)(n,m).
At level one with trivial character, the Kloosterman sum is real
(pair a unit with its negative) and symmetric in m,n
(replace a unit by its inverse); i^k is real for even k.
Consequently the Petersson matrix is real symmetric and this is also
Delta_(k,1)(m,n). Thus the exact formula in our convention is

    K_mn=delta_mn+2*pi*i^k sum_(c>=1) S(m,n;c)/c
                              *J_nu(4*pi*sqrt(m*n)/c).         (U2)

Equivalently the raw Poincare coefficient factor (m/n)^(nu/2)
cancels sqrt(A_m/A_n) after applying the reproducing identity.
The coefficient values are not identified with vectors in an unweighted
Euclidean metric. The A_m normalizations and conjugations are essential.

## 3. Complete growing-block control

The defining Bessel series gives, for real x>0,

    |J_nu(x)| <= (x/2)^nu/nu! * exp(x^2/[4(nu+1)]).

Every term is bounded using (nu+r)!>=nu!*(nu+1)^r; this is an infinite
series estimate, not a finite Bessel sample. Also |S(m,n;c)|<=c and
sum_(c>=1)c^(-nu)<=2 for nu>=3. Since m,n<=j, U2 therefore gives

    max_(m,n<=j) |K_mn-delta_mn|
      <=4*pi*(2*pi*j)^nu/nu! * exp(4*pi^2*j^2/k).              (U3)

For any vector u, the absolute quadratic error is bounded by the maximum
entry error times (sum|u_m|)^2, hence by j times that error times ||u||^2.
In particular, with

    delta=||K-I||_op,

the right side of U3 multiplied by j bounds delta. This pays the whole
growing block, not merely each diagonal entry.

The assumption k>=96j gives nu>=95j. We retain the growth of the
exponential factor: it is less than e^j<3^j, NOT uniformly less than e.
The elementary integral estimate for log(nu!) gives
nu!>(nu/e)^nu>(nu/3)^nu. Using 4*pi<13,2*pi<7 and21/95<1/4, we obtain

    delta <13*j*3^j*(21*j/nu)^nu
          <=13*j*3^j*(21/95)^nu
           <13*j*4^(j-nu)
          <=13*j*4^(-94*j)<1/1000.                            (U4)

For the last inequality, 13000<4^94 is an exact integer base case.
The sequence j*4^(-94j) has successive ratio at most2/4^94<1.
Thus U4 holds for ALL permitted j,k, not a tested finite range.

It follows that K is positive definite and its eigenvalues lie between
1-delta and1+delta. In particular the first j coefficient functionals
are independent.

## 4. Simultaneous coefficient constraints and the physical vacuum

The actual quotient vacuum minimizes G[f] subject to

    a_f(m)=0 (m<j),             a_f(j)=1.

In the normalized coefficient frame these are
G(v_m,f)=c_m, with c=sqrt(A_j)*e_j. The least-norm lift lies in the
span of the v_m. Writing it as sum v_m alpha_m gives K alpha=c,
and its squared norm is c* K^(-1)c. Therefore

    G_(Q,j)=A_j*(K^(-1))_jj <= A_j/(1-delta).                  (U5)

A vector perpendicular to this span leaves all constraints unchanged
and only increases the norm, so this minimizes over the WHOLE cusp
space. For j>1 this is NOT the diagonal formula A_j/a_(P_j)(j):
all earlier coefficient constraints are enforced simultaneously.

The level-one dimension formula gives
dim S_k>=floor(k/12)-1>=8j-1>=j+1.
Together with coefficient independence this makes
dim V=dim S_k-j+1 and dim W=dim S_k-j>=1.
Thus every quotient in the theorem is genuinely proper.

## 5. A uniform lower bound for the native source ratio

TQ's all-lift cusp/Poisson bound, valid at every depth, gives

    H_(Q,j)(t)>=J_(k,j)/sqrt(t),
    J_(k,j)=integral_1^infinity y^(nu-1/2) exp(-4*pi*j*y) dy.

It did not require fixed j or a fixed minimizing lift. Only TQ's old
asymptotic evaluation was fixed-depth; we replace that evaluation here.

As in E96, the omitted interval (0,1) is less than1/(nu+1/2), so

    J_(k,j)/A_j >
      Gamma(nu+1/2)/[sqrt(4*pi*j)*Gamma(nu)]
      -1/[(nu+1/2)A_j].                                      (U6)

The factorial bound and nu>=95j yield

    A_j=nu!/[nu*(4*pi*j)^nu]
        >(nu/(39j))^nu/nu
        >=(95/39)^nu/nu >2^nu/nu >1000.                       (U7)

The last sequence increases for integers nu>=95 and
2^95>95000. Hence the subtracted amount in U6 is less than1/1000,
uniformly in BOTH variables.

Integral Cauchy--Schwarz gives
Gamma(nu+1/2)/Gamma(nu)>=nu/sqrt(nu+1/2).
The square of the remaining lower bound contains

    nu^2/[j*(nu+1/2)]
      >=95^2*j/(95j+1/2)
      >=95^2/(95+1/2).                                       (U8)

The first step uses monotonicity in nu and nu>=95j; the second uses j>=1.
The rational inequality95^2/[(191/2)*(88/7)]>(137/50)^2 and4*pi<88/7
therefore give, uniformly,

    J_(k,j)/A_j >137/50-1/1000=2739/1000.                     (U9)

Combining U4,U5,U9 gives

    R_(k,j)=J_(k,j)/G_(Q,j)
            >=(1-delta)*J_(k,j)/A_j
             >2736261/1000000>273/100>e.                      (U10)

The complete exponential-series bound for e is E96's
163/60+7/4320<273/100. No asymptotic estimate or unknown weight threshold
remains anywhere in U4--U10.

## 6. Completed zero conclusion and exact scope

TQ's source-exact criterion gives

    L_(k,j)(1/2)/G_(Q,j)>=2R_(k,j)(log R_(k,j)-1)>0.

The positive residue at one gives negative divergence from its left.
Real analyticity with no interior poles and reflection supply the
asserted off-central real pair, with odd multiplicity for at least one
such reflected pair. Pole clearing does not remove the zeros.

This is uniform for j<=k/96. It says nothing about depths near the full
dimension, such as j approximately k/12, and supplies no12j/k zero
location or an all-zero census. The number96 is a sufficient constant,
not an optimized or minimal one. It does not establish Hecke-stable
source selection, an Euler product, a new automorphic representation,
RH or GRH.

The argument is a late analytic synthesis of the actual theta-source
bound, the FULL normalized coefficient Gram and elementary estimates.
It is not a numerical atlas or a new computational module. The existing
37-module replay denominator is unchanged; independent frozen-source
review must separately authenticate the off-diagonal normalization,
growing-block norm, simultaneous constraints and uniform estimates.
