# Hecke-selected sources versus fixed-depth cusp concentration

Status: PROPOSED SOURCE-SPECIFIC THEOREM; exact-SHA independent review required.
Authoring base: 070751bf7e96c1dbd6d4b3cfbb05dc70f5a2aa22 (DL).
DL's independent acceptance is pinned at c29ae6f3d134e076fa41aef9ae39920478f16ac0.
This is a new five-file packet. No parent source or programme front is changed.
The all-weight assertions below import classical Hecke/Deligne/Rankin--Selberg
theorems and the stated symmetric-square lower bound. The finite checker does
not prove those imports, evaluate a period, or certify a numerical zero.

Arithmetic taxonomy: MIXED: EXACT_RATIONAL / CERTIFIED_INTEGER_COVERAGE.
All finite coefficient, rational-inequality, and coverage controls use exact
integers and reduced rational numbers; rounding: none. The analytic integrals,
limits, and imported theorems are not machine-certified by this finite replay.
This metadata release preserves scientific source eaa8e8263bb34b8b669f911580c9dd9e55766ba2.

## 1. Source, normalization, and the two different rank scales

Use the EXACT CF/DL space V_k=S_k(SL(2,Z)), q=exp(2*pi*i*z), standard domain
F, dmu=dxdy/y^2, and Petersson form G(u,v)=integral_F y^k bar(u)v dmu.
Thus the first input is conjugate-linear. Put X(z)=max(1,Im(z)). The period is

    I_s(u,v)=integral_F y^k bar(u)v E*(z,s)dmu,
    E*(z,s)=pi^(-s)Gamma(s)zeta(2s) sum_(Gamma_infinity\Gamma) Im(gamma z)^s.

Signs +/-I are identified in this Eisenstein sum. Its residues at0,1 are
-1/2,+1/2 and I_s=I_(1-s). Write

    A_n(k)=Gamma(k-1)/(4*pi*n)^(k-1),
    A_k(s)=pi^(-s)Gamma(s)(4*pi)^(-s-k+1)Gamma(s+k-1).

The notation A_n(k) and A_k(s) has different arguments, as in the parent.
Let B_k be the Petersson-ORTHONORMAL simultaneous Hecke eigenbasis. Its lines
are canonical; choosing phases has no effect below. For each line let f be
the representative with a_f(1)=1, set e_f=f/sqrt(G(f)), and write

    a_f(n)=lambda_f(n)n^((k-1)/2),  |lambda_f(n)|<=tau(n),
    L_f=L(1,sym^2 f)>0.

The Hecke coefficients are real at level one. Hecke selection means a subset
S_k of these eigenlines, not an arbitrary rotated orthonormal basis. Write
V(S_k)=span{e_f:f in S_k}, r_k=|S_k|. Selection may vary with k.

We prove two SEPARATE scales, uniformly over such selections:

* If a unit vector in V(S_k) has at least delta>0 of its Petersson mass in
  y>=eta*k (fixed eta>0), then r_k >>_(eta) delta*k/log k. In particular the
  actual fixed-depth DL determinant-nullvectors need >>_J k/log k Hecke lines.
* If r_k=o(k/log^5 k), the entire restricted period on V(S_k), and every
  restriction inside that space, is nondegenerate at s=1-c/k uniformly for
  c in any fixed compact subset of Re(c)>0. The same holds by reflection.

The stronger cusp-support threshold does NOT replace the weaker zero-free
operator threshold. No numerical sufficient-weight threshold is claimed.
All depths J, cusp constants eta, and compact c sets are FIXED before k grows.
No assertion is made about a codimension-fixed Hecke flag in V_k: its rank
is about k/12, outside both small-rank hypotheses. Changing to a Hecke basis
of the FULL space cannot remove DL's basis-invariant determinant zeros.

## 2. Classical inputs and exact diagonal period

The primary imports are stated here so their scope is not hidden in a norm:

(a) The level-one normalized Hecke eigenbasis and Deligne bound above; see
Iwaniec--Luo--Sarnak (ILS), section2, (2.14)--(2.20), pp71--72.
(b) The ordinary symmetric-square Euler product, continuation and completion;
Holowinsky--Soundararajan (HS), section2, (2.1), p1523.
(c) Uniformly over level-one holomorphic eigenforms of weight k,

    L_f >= c_*/log k                                           (HC1)

for an absolute c_*>0. HS section2 (2.2), p1523 states this weight-aspect
form explicitly, with the Goldfeld--Hoffstein--Lieman (GHL) input. GHL p178
also explicitly says its arguments extend to holomorphic forms uniformly
in the weight and that level one has no GL(1)-lift exception. We import
HC1; we do not compute c_* or claim an effective onset for this packet.

The Hecke recurrence at each prime proves the Euler-factor identity

    sum_n lambda_f(n)^2 n^(-s)=zeta(s)L(s,sym^2 f)/zeta(2s).

CF's literal unfolding therefore gives, initially for Re(s)>1 and then
meromorphically,

    I_s(f,f)=A_k(s)zeta(s)L(s,sym^2 f),
    G(f)=2 A_k(1)L_f=(k-1)A_1(k)L_f/(2*pi^2).          (HC2)

The second equality follows by taking the residue at1, which is G(f)/2.
It also agrees with ILS Lemma2.5 (2.36), p74: at level one their
Z(1,f)=L_f/zeta(2), not L_f. Thus no volume or zeta factor is suppressed.
With Gamma_R(u)=pi^(-u/2)Gamma(u/2) and
Lambda(s,zeta)=Gamma_R(s)zeta(s), duplication gives exactly

    I_s(f,f)=2^(-k-1) Lambda(s,zeta) Lambda(s,sym^2 f),
    Lambda(s,sym^2 f)=Gamma_R(s+1)Gamma_R(s+k-1)Gamma_R(s+k)L(s,sym^2 f).

For comparison, HS p1523 also supplies a constant c0>0 and the zero-free
region Re(s)>=1-c0/log(k(1+|Im(s)|)) for L(s,sym^2 f). Hence, for fixed
positive real c and all sufficiently large k, the eigenLINE period at
1-c/k is nonzero and negative: L is positive there by continuity from1,
zeta(s)<0 for0<s<1, and A_k(s)>0. This does not diagonalize a period matrix.
The operator proof in section5 needs only HC1, not this zero-free region.

Indeed for two distinct a1-normalized Hecke forms f,g, the cross unfolding
starts with the nonzero n=1 coefficient1. Ordinary Dirichlet uniqueness
shows I_s(f,g) is NOT identically zero. Their Petersson orthogonality only
makes the cross RESIDUE at1 zero; it does not make the full function zero.

## 3. Complete cusp-tail mass and the Hecke-support bound

Let Q(a,x)=Gamma(a,x)/Gamma(a), with the upper incomplete Gamma integral.
For eta*k>=1, the domain above eta*k is the full width-one cusp rectangle.
Parseval, Tonelli and HC2 give the EXACT formula

    M_eta(e_f):=integral_(F,y>=eta*k) y^k |e_f|^2 dmu
      =2*pi^2/((k-1)L_f) sum_(n>=1) lambda_f(n)^2
                               Q(k-1,4*pi*eta*k*n).    (HC3)

This retains every coefficient. It does not assume polynomial-in-k bounds
on the Fourier coefficients a_f(n). Those coefficients contain n^((k-1)/2).
Let Z have Gamma distribution with shape k-1 and scale1, so Q(k-1,x)=P(Z>=x).
Using tau(n)<=2sqrt(n), floor sums and Tonelli,

    sum_n lambda_f(n)^2 Q(k-1,a*n)
      <=4 E sum_(n<=Z/a) n <=4 E(Z/a)^2,
    a=4*pi*eta*k,  E Z^2=(k-1)k.

Consequently

    M_eta(e_f)<=1/(2*eta^2*k*L_f).                      (HC4)

The harmless bound sum_(n<=u)n<=u^2 is valid also for0<=u<1, when the
sum is zero. All passages are nonnegative monotone limits, so HC4 pays
the complete n tail, including n growing with k.

Compression of multiplication by the cusp indicator is positive. Its norm
on V(S_k) is at most its trace in the orthonormal Hecke basis. Therefore,
for every v in V(S_k) with G(v)=1,

    M_eta(v)<=1/(2*eta^2*k) sum_(f in S_k)1/L_f
              <= r_k log k/(2*eta^2*c_* k).            (HC5)

In particular M_eta(v)>=delta forces

    r_k >=2*eta^2*c_* delta*k/log k.                    (HC6)

This is a support/concentration statement in the ACTUAL Petersson measure.
It is not an inference from an ordinary Euclidean norm of q coefficients.

## 4. Complete X-moment, with the full low domain retained

Define M_X(v)=integral_F X y^k|v|^2dmu. Below y=1, X=1 and its contribution
for a unit vector is at most1. Above1, Parseval and HC2 now give

    integral_(y>=1) y*y^k |e_f|^2dmu
       =pi/(2L_f) sum_(n>=1) lambda_f(n)^2/n Q(k,4*pi*n). (HC7)

For every n, tau(n)^2<=d_4(n). This follows primewise from
(a+1)^2<=binom(a+3,3), whose difference is a(a-1)(a+1)/6. Thus for u>=1,

    sum_(n<=u) tau(n)^2/n
      <=sum_(n<=u)d_4(n)/n <=H_floor(u)^4<=(1+log u)^4.  (HC8)

The middle bound enlarges abcd<=u to four independent indices<=floor(u).
For u<1 the sum is zero and is bounded by (1+log^+u)^4.
Use now Z of Gamma shape k, set A=1+log k>=1, and note
log^+(Z/(4*pi))<=log k+Z/k. Tonelli and (a+b)^4<=8(a^4+b^4) give

    sum_n tau(n)^2/n Q(k,4*pi*n)
       <=E(1+log^+(Z/(4*pi)))^4
       <=8 A^4+8 E(Z/k)^4 <=8 A^4+192<=200 A^4,
    E(Z/k)^4=k(k+1)(k+2)(k+3)/k^4<=24.                (HC9)

Therefore the concrete full-domain bound is

    M_X(e_f)<=1+100*pi*(1+log k)^4/L_f.                (HC10)

Taking the positive compression's trace proves the uniform all-vector bound

    ||T_X|V(S_k)||_G
      <=r_k+100*pi*(1+log k)^4 sum_(f in S_k)1/L_f
      << r_k log^5 k.                                  (HC11)

Here T_X denotes the positive FORM operator after compression to the finite
space. No claim that multiplication by X preserves holomorphic cusp forms
is made. The constants are independent of which eigenforms were selected.

## 5. Uniform COMPLEX-c Laurent bound and the whole restricted period

Fix a compact K contained in Re(c)>0. Put epsilon=c/k, s=1-epsilon and
y>=sqrt(3)/2. For all sufficiently large k, Re(s) lies in[3/4,1).
LS7--LS10, with the same Fourier normalization, give uniformly on K

    E*(z,s)=C(s)y^s+D(s)y^epsilon+R_s(z),
    C(s)=pi/6+O_K(1/k),  D(s)=-k/(2c)+O_K(1),
    |R_s(z)|<1.                                        (HC12)

LS's complex-order Bessel integral proves the last estimate; it is not
an analytic continuation of a real inequality. Powers of y use real log y.
For y>=1 and Re(epsilon)<=1/2,

    |y^epsilon-1|<=|epsilon| log(y)y^(Re epsilon)
                   <=2|epsilon|y.

For sqrt(3)/2<=y<=1 the analogous difference is O_K(1/k). Also |y^s|<=X
and |y^epsilon|<=X, after a uniform constant below1. Since c stays bounded
and away from0, HC12 consequently proves the POINTWISE, full-domain estimate

    |E*(z,1-c/k)+k/(2c)|<=C_K X(z).                    (HC13)

In particular the k-times-power difference in D(s)y^epsilon is paid; it
is not dropped or estimated only at typical y.
Weighted Cauchy--Schwarz yields for all u,v in V(S_k)

    |I_(1-c/k)(u,v)+kG(u,v)/(2c)|
          <=C_K sqrt(M_X(u)M_X(v)).                    (HC14)

Whiten with the constant original Petersson Gram. HC11--HC14 give in genuine
operator norm, uniformly for c in K,

    G_S^(-1/2) I_S(1-c/k) G_S^(-1/2)/k
        =-Id/(2c)+O_K(r_k log^5 k/k).                  (HC15)

The same bound holds on EVERY subspace of V(S_k), whether Hecke-selected
or not. If r_k=o(k/log^5 k), a Neumann inverse about the scalar -1/(2c)
proves all these restrictions invertible, uniformly on K for large k.
For real c in a fixed positive compact interval they are negative definite.
Their determinants, and determinant ratios for any fixed-in-s internal flag,
have neither zero nor pole there. Reflection gives the left endpoint region.
For a quotient with a prescribed normalized functional, its scalar leading
factor also depends on that functional's Petersson quotient metric; HC15
does NOT assert an unnormalized quotient equals -k/(2c).

## 6. Native DL nullvectors require growing Hecke support

Fix J>=1 and1<=i<=J. DL gives a simple determinant zero of I|W_i near
c=12J at sufficiently large even weights, where
W_i={a_1=...=a_(i-1)=0}. Its one-dimensional nullspace is an actual source
subspace, not a zero of a surrogate matrix. Work in DL's unit-triangular
chart (h_1,...,h_J,W_(J+1)) and let N=J+1.

DL9--DL10 prove, for eta_J=1/(10000(J+1)),

    G(h_J)=A_J(1+o(1)),
    integral_(y<=eta_J*k) y^k|h_J|^2dmu
                   <=poly_J(k)10^(-k) A_(J+1).         (HC16)

Thus the Petersson-unit h_J tends to full mass in y>=eta_J*k.
Here is the required transfer to the COMPLETE nullvector, including both
eliminated blocks. After eliminating E=I|W_(J+1), call the finite matrix H,
and M={i,...,J-1}. At its determinant zero choose the h_J coefficient1.
The earlier coefficients are EXACTLY

    u=-H_MM^(-1)H_MJ=-A_M^(-1) C_M^(-1)H_MJ,
    |u_m|<=C_J A_J/(k A_m),                            (HC17)

by DL21 and DL24. For an empty M there is no such term. Hence

    ||sum_(m in M)u_m h_m||_G
                 <=C_J A_J/(k sqrt(A_(J-1)))=o(sqrt(A_J)).

Finally the genuine deep component is -E^(-1) applied to the cross functional
of h_J+sum u_mh_m. DL15 and the G-inverse bound in DL16 give

    ||deep component||_G<=C_J k^(J+1)sqrt(A_(J+1))
                                      =o(sqrt(A_J)).   (HC18)

The coefficient sum 1+sum|u_m| is bounded, since A_J/A_m<=1 and J is fixed.
No coordinate norm on the growing deep dimension replaces this dual G norm.
Equations HC16--HC18 show that its unit nullvector v_(i,J,k), with a suitable
phase, satisfies

    ||v_(i,J,k)-h_J/sqrt(G(h_J))||_G ->0,
    M_(eta_J)(v_(i,J,k))->1.                            (HC19)

Cusp-indicator compression is a contraction, so the mass transfer follows
from norm convergence. Apply HC6, for example with delta=1/2 for large k:
every exact Hecke support of v_(i,J,k) has size >>_J k/log k.
Reflection gives the same nullspace at the reflected determinant zero.
For i=1 these are the full period determinant's nullvectors. For i>1 the
nullspace is of the RESTRICTED form on W_i, not necessarily of the full form.
This distinction does not affect HC5, which concerns any vector in V_k.

## 7. Fixed-index coefficient kernels and robust approximation

For fixed j let P_(k,j)=sum_(Gamma_infinity\Gamma) q^j|_k gamma be the
ordinary holomorphic Poincare series, with the SAME sign-identified quotient
and slash factor (c_gamma*z+d_gamma)^(-k). Unfolding gives
G(P_(k,j),f)=A_j a_f(j). Put p_j=a_(P_(k,j))(j), so
G(P_(k,j))=A_j p_j. ILS Proposition2.1 gives

    p_j=1+2*pi*i^k sum_(c>=1) S(j,j;c)/c J_(k-1)(4*pi*j/c).

The crude |S(j,j;c)|<=c and the defining Bessel series imply, for k>=4,

    |p_j-1|<=4*pi*(2*pi*j)^(k-1)/(k-1)!
                         *exp(4*pi^2*j^2/k)->0.        (HC20)

Indeed |J_nu(x)|<=(x/2)^nu/Gamma(nu+1)*exp(x^2/(4(nu+1))), and
sum c^(-(k-1))<=2. Thus p_j>0 for all sufficiently large k.
For the unit coefficient kernel p_(k,j)=P_(k,j)/sqrt(A_j p_j), HC2 gives
the EXACT overlap

    |G(p_(k,j),e_f)|^2
       =2*pi^2*lambda_f(j)^2/((k-1)L_f p_j)
       <<_j log k/k.                                   (HC21)

This is a kernel/eigenline identity, not a diagonalization of I(s).
Since a_(h_J)(J)=1, G(P_(k,J),h_J)=A_J. Equations HC16 and HC20 make the
normalized h_J converge to p_(k,J) in G norm. Together with HC19 this proves

    ||projection_(V(S_k)) v_(i,J,k)||_G
          <=C_J sqrt(r_k log k/k)+o_J(1).              (HC22)

The little-o term is uniform over S_k, since orthogonal projection is a
contraction. In particular no r_k=o(k/log k) Hecke-selected subspace can
even approximate these unit nullvectors with a nonvanishing projected norm.
The parameter J is fixed; HC20 is not a growing-index estimate here.

## 8. Exact finite controls, source bindings and boundaries

The producer builds the integral q-echelon basis in all six residual classes
for d=2,3,4 by two independent E4/E6 charts and checks Delta by its logarithmic
derivative recurrence. It reconstructs exact T2,T3 matrices and their action
on the COMPLETE retained prefix through q^(d+2), requiring source coefficients
through q^(3(d+2)); the two operators commute. No omitted q tail is used in
these finite algebra checks. At weight24 the canonical basis gives

    T2=[[0,1],[20468736,1080]],
    T3=[[195660,-48],[-982499328,143820]]=195660 Id-48 T2.

The normalized eigenforms are f_1+alpha f_2 with
alpha^2-1080alpha-20468736=0, hence alpha=540+/-12sqrt(144169).
Their cross period has first Dirichlet coefficient1, despite G-orthogonality.
The finite ledger also checks exact floor sums, prime-exponent d4 domination,
integer Gamma moments, the k/log-scale normalization, and trace-versus-diagonal
controls with rational positive matrices. These are identities/finite tests,
not sampling of the all-k estimates or of any Eisenstein integral.

The 32 new tests pass in normal Python and under -O, along with the136 tests
of DL/NP/LS/AW (168 total in each mode). The tests' separate finite-binomial
Delta product and forward echelon construction reconstruct all18 charts;
held-out q coefficients through6d independently check T6=T2*T3. Thirty-five
additional fresh resealed payload/artifact mutations are rejected through
the actual reconstruction in each mode. These are separate from the unit
tests' mocked source-manifest seam controls. Both producer checks and all
four LF-exact fixture/manifest emissions pass, as do Ruff check/format check
and the full-base whitespace check. No source file uses assertions as a guard.

Source commits/blobs/LF hashes and all four nonfixture artifact hashes are
authenticated. Fixture acceptance requires strict typed canonical equality
to the reconstructed result, not merely a resealed payload. Public caps and
an arithmetic/loop work budget are enforced by explicit exceptions under -O.
They are not a sandbox, an interpreter-operation count, or a wall-clock bound.
Primary PDF URLs are source citations; their remote bytes are not authenticated
by the offline Git checker. The PDF workflow checked the printed normalizations.

Primary references actually consulted:

* [Holowinsky--Soundararajan, Mass equidistribution for Hecke eigenforms,
  Annals172 (2010)](https://annals.math.princeton.edu/wp-content/uploads/annals-v172-n2-p18-p.pdf),
  pp1518--1523, especially section2, (2.1)--(2.2), p1523: exact weight-aspect
  symmetric-square normalization, zero-free region, and HC1.
* [Goldfeld--Hoffstein--Lieman, An effective zero-free region,
  Annals140 (1994)](https://www.math.columbia.edu/~goldfeld/EffectiveZeroFreeRegion.pdf),
  pp177--180; p178's explicit holomorphic-weight remark and level-one exception
  exclusion. The current packet does not reprove the GHL/HS theorem.
* [Iwaniec--Luo--Sarnak, Low lying zeros of families of L-functions,
  IHES91 (2000)](https://www.numdam.org/article/PMIHES_2000__91__55_0.pdf),
  section2, Proposition2.1 (p68), (2.14)--(2.20) (p71), and Lemma2.5 (p74).
  Their inner product has the opposite argument convention; the real diagonal
  norm agrees, and the coefficient-kernel identity above uses OUR convention.

This is a source comparison using classical inputs, not a new automorphic
representation, an exhaustive prior-art assertion, critical-line placement,
RH/GRH, global divisor census, uniform depth ladder, or optimal rank threshold.
No tame polynomial Fourier bound for a1-normalized eigenforms is assumed.
No exact finite control supplies a numerical onset for the analytic theorems.
