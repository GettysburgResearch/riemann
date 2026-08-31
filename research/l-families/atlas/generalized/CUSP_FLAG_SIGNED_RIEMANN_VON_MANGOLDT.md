# Cusp-flag quotient: a signed Riemann--von Mangoldt law

Status: PROPOSED SOURCE-SPECIFIC THEOREM; independent exact-SHA review required.
Fixed even level-one weight k, d=dim S_k>=2, canonical full Miller basis and
unchanged first-coefficient flag/completion. No RH, critical-line density,
finite-pole, uncancelled-pole, positivity or novelty assertion is made.

Scientific inputs: CF1--CF4 at the metadata-only family release
b69c854d9e3dd1db7b82d95fe6f032fe47d5306b, and the direct theta/growth proof
EF5--EF11 at a27781310ded92125ef16d97d78db4d97cec4c1b. All ten parent
files are authenticated; none is modified. This proof does NOT infer a
counting asymptotic merely from EF's global O(R log R) count bound.

## 1. The theorem and the two determinants

Write I_d=I_k and I_(d-1)=I_W, where W=span(f_2,...,f_d). The symbol r below
means ONLY one of these two specified ranks, not an arbitrary rank-r minor.
Set w=s+k-1, P=d!, and retain
\[
 A(s)=\pi^{-s}(4\pi)^{-s-k+1}\Gamma(s)\Gamma(s+k-1),\qquad
 Q(s)=\frac{\det I_d(s)}{\det I_{d-1}(s)}.                 \tag{RV1}
\]
For T>0 define
\[
 N_r^+(T)=\sum_{0<\Im\rho\le T}\operatorname{ord}_\rho\det I_r,
 \qquad
 N_Q^+(T)=\sum_{0<\Im\rho\le T}\operatorname{ord}_\rho Q.   \tag{RV2}
\]
All real parts are included; the relevant divisors are confined to a
fixed vertical strip. The determinants have poles only at REAL 0 and 1.
Consequently N_r^+ counts their upper-half-plane zeros positively, with
multiplicity. N_Q^+ is instead the NET signed zero-minus-pole count.
Common determinant zeros cancel exactly, including at the height cutoff.

**Theorem.** For each fixed source and every real T>=2,
\[
 N_r^+(T)=\frac{2r}{\pi}T\log\frac{T}{2\pi e}
              -\frac{T}{\pi}\log(d!)+O_k(\log(T+2)),       \tag{RV3}
\]
and therefore
\[
 \boxed{N_Q^+(T)=\frac2\pi T\log\frac{T}{2\pi e}
                           +O_k(\log(T+2)).}             \tag{RV4}
\]
The convention includes zeros at height T. Constants depend on the fixed
weight and actual source; no uniformity in k or numerical error constant
is certified. The unsigned number of net divisor points, with absolute
multiplicity, in a unit height window is O_k(log(T+2)).
That local upper bound is NOT an unsigned global asymptotic for Q.

The essential arithmetic input to the conductor cancellation is that BOTH
determinants have leading product P=d!, with coefficient one. Using (d-1)!
for the W determinant would give an erroneous linear term in (RV4).

## 2. Native Cauchy--Binet and the exact leading product

CF2 gives
\[
 I_r(s)=A(s)M_r(s),\quad M_r(s)=\zeta(2s)D_r(w),\quad
 D_r(w)=\sum_{n\ge1}v_r(n)v_r(n)^t n^{-w},                 \tag{RV5}
\]
where v_d(n)=(a_1(n),...,a_d(n))^t and
v_(d-1)(n)=(a_2(n),...,a_d(n))^t. These are actual integral Miller
coefficients, not independent variables. The transpose uses the real
coefficient basis and does not conjugate s.

For a finite cutoff L, Cauchy--Binet gives
\[
 \det D_{r,L}(w)=
 \sum_{1\le n_1<\cdots<n_r\le L}
 \det[v_r(n_1)\ \cdots\ v_r(n_r)]^2
                       (n_1\cdots n_r)^{-w}.             \tag{RV6}
\]
To pass to infinity, first take w real in the half-plane of absolute entry
convergence supplied by CF2 (Re s>1 suffices). The nonnegative right side
increases to a finite limit because the left determinant converges.
The same series is then absolutely and normally convergent in every
closed farther-right half-plane. Thus (RV6) is a genuine analytic expansion,
not merely a formal determinant calculation.

For the full matrix, n_j>=j, so n_1...n_d>=d!. Equality has exactly the tuple
(1,...,d), whose coefficient matrix is the identity by CF1. For W, v_(d-1)(1)=0.
Any nonzero minor therefore has n_j>=j+1. Its product is >=2...d=d!, with
equality only at (2,...,d), again an identity matrix. Both leading
coefficients are ONE. All omitted products are strictly larger than P.

Also
\[
 \zeta(2s)^r
 =\sum_{\ell_1,\ldots,\ell_r\ge1}
       (\ell_1\cdots\ell_r)^{2k-2}
       ((\ell_1\cdots\ell_r)^2)^{-w}.                    \tag{RV7}
\]
Its leading product is one with coefficient one, and all coefficients
are nonnegative. Combining (RV6)--(RV7) proves that
\[
 F_r(s):=P^{s+k-1}\det M_r(s)
       =1+\sum_{\eta>1}c_{r,\eta}\eta^{-(s+k-1)},
       \qquad c_{r,\eta}\ge0,                            \tag{RV8}
\]
on a right half-plane. The rational frequencies have the form integer/P,
so are locally finite and bounded away from one. Equal frequencies are
combined. Absolute domination at one fixed abscissa gives
\[
 \sup_{\Re s\ge c}|F_r(s)-1|\longrightarrow0
                         \quad(c\longrightarrow\infty). \tag{RV9}
\]
Choose one real c>2 sufficiently large for BOTH ranks that the supremum
in (RV9) is <1/2. Their logarithms there have uniformly bounded principal
imaginary parts and continue from positive values on the real axis.

## 3. Pole clearing, functional equation and polynomial strip growth

Put
\[
 U_r(s)=[s(s-1)]^r\det I_r(s)=\det J_r(s).
\]
EF8--EF9 prove that U_r is nonzero entire, real type, and
log^+ max_(|s|<=R)|U_r(s)|=O_k(R log(R+2)). Entrywise reflection gives
\[
 U_r(1-s)=U_r(s),\qquad
 U_r(\bar s)=\overline{U_r(s)}.                           \tag{RV10}
\]
The nonzero Petersson residue matrices in CF4 show that det I_r has
EXACT pole order r at 0 and 1 and no other poles. In particular U_r(0)
and U_r(1) are nonzero; the clearing factors introduce no endpoint zeros.

Since 1/A is entire, F_r has at most a pole of order r at 1. At zero the
order-r pole of det I_r cancels the order-r gamma pole of A^r. Thus
\[
 H_r(s)=(s-1)^r F_r(s)
       =P^{s+k-1}U_r(s)/(s^r A(s)^r)                     \tag{RV11}
\]
is entire of order at most one. Thus a global exp(O_k(1+R^(3/2)))
upper bound is sufficient without importing a sharper reciprocal-gamma
growth estimate. Here 1/(sA(s)) is entire:
the zero of 1/A at zero cancels the apparent division by s.
These assertions concern the continued function, not values at poles.

The exact reflection multiplier is
\[
 F_r(s)=P^{2s-1}
           \left(\frac{A(1-s)}{A(s)}\right)^rF_r(1-s).
                                                                  \tag{RV12}
\]
There is no bare reflection for M_r. For fixed real sigma, Stirling yields
\[
 \left|\frac{A(1-\sigma-it)}{A(\sigma+it)}\right|
  =(4\pi^2)^{2\sigma-1}|t|^{\,2-4\sigma}
                                      (1+O_{k,\sigma}(|t|^{-1})).
                                                                  \tag{RV13}
\]
The two gamma shifts cancel out of the power 2-4sigma. This controls the
left line sigma=1-C from the right line sigma=C, for every fixed C>=c.
On the latter F_r is bounded; on the former it is
O_(k,C)((1+|t|)^(r(4C-2))). Compact low-height segments are handled using
the entire H_r rather than dividing pointwise by a singular multiplier.

Here is the required strip argument in full. On both edges of
1-C<=Re s<=C, H_r is bounded by C_0(1+|t|)^B for some integer B>=0;
one may take any integer B>=r(4C-1), increasing C_0 if needed.
Choose a real D>C+1, so -D is outside this strip. Then
h(s)=H_r(s)/(s+D)^B is holomorphic on the closed strip and uniformly
bounded by some C_1 on its two vertical edges. Its interior growth is
exp(O_(k,C)(1+|t|^(3/2))). For epsilon>0, multiply by exp(epsilon s^2).
On horizontal edges at heights +/-R the modulus tends to zero as R tends
to infinity, because -epsilon R^2 dominates O(R^(3/2)). On the vertical
edges it is <=C_1 exp(epsilon max(C^2,(1-C)^2)). The maximum principle,
first R->infinity and then epsilon->0, gives |h|<=C_1 throughout.
Consequently
\[
 |F_r(\sigma+it)|\ll_{k,C}(1+|t|)^{B}
 \quad(1-C\le\sigma\le C,\ |t|\ge1).                     \tag{RV14}
\]
No polynomial strip bound was inferred from order alone; the boundary
bounds from the exact native reflection were indispensable. The same
argument applies on any larger fixed strip needed by the disks below.

By (RV9), U_r has no zeros on Re s>=c. Reflection gives the same assertion
on Re s<=1-c. Hence its real zeros are finite in number, and all nonreal
zeros lie in this fixed strip. Neither RH nor any simplicity input is used.

## 4. A fixed-disk Backlund/Jensen argument

Take T sufficiently large, R_1=2c and R_2=4c, and define
\[
 B_{r,T}(z)=\tfrac12(F_r(z+iT)+F_r(z-iT)).
                                                                  \tag{RV15}
\]
For real x this is Re F_r(x+iT). It is holomorphic on the closed disk
|z-c|<=R_2 once T>R_2+2, because the only possible shifted poles
1+/-iT are outside. Its center satisfies B_(r,T)(c)>1/2 by (RV9).
On that disk (RV14), on a suitably larger FIXED strip, gives
max |B_(r,T)|<=C_2(T+2)^B. Jensen with radii R_1,R_2 yields
\[
 \#\{z:B_{r,T}(z)=0,\ |z-c|\le R_1\}
 \le\frac{\log(C_2(T+2)^B)-\log(1/2)}{\log2}
 =O_k(\log(T+2)).                                       \tag{RV16}
\]
Outer-boundary zeros are handled by a limiting radius. The real segment
[1-c,c] lies strictly inside the smaller disk.

If the horizontal line at T avoids zeros of F_r, its real-part zeros split
this segment into at most n+1 intervals. On each interval F_r lies in
one open half-plane, so a continuous argument changes between its endpoints
by at most pi in absolute value. At the separating points F_r is nonzero,
so the argument continues. Thus
\[
 \left|\Delta_{[1-c,c]+iT}\arg F_r\right|
                             =O_k(\log(T+2)).             \tag{RV17}
\]
This bounds NET argument change, not its total variation as a path.
A rotated real-part auxiliary also works; here the right normalization
already supplies a positive real anchor, so no rotation is necessary.

Since U_r=[s(s-1)]^r A(s)^r P^{-s-k+1}F_r,
the polynomial and gamma factors add O_k(log(T+2)) argument change across
this fixed horizontal segment, by uniform Stirling or its logarithmic
derivative. The P factor has constant argument on a horizontal segment.
The same bound therefore holds for U_r, and by real type also at -T.

For later use, apply Jensen directly to F_r on the disk centered at c+iT
with the same radii. Its center modulus exceeds 1/2 and its maximum is
polynomial in T. The whole strip segment with |Im s-T|<=1 is inside the
smaller disk, since sqrt((2c-1)^2+1)<2c. For T large, gamma and clearing
factors have no zeros or poles there. Therefore the number of U_r zeros,
with multiplicity, in that unit window is O_k(log(T+2)). This proves the
local jump bound and, by summing the two ranks, its signed-divisor analogue.

## 5. Argument principle, phase constant and exceptional heights

First take T avoiding the zero ordinates of BOTH determinants. Use the
counterclockwise rectangle with real edges 1-c,c and heights -T,T.
On the right edge choose a continuous logarithm starting with U_r(c)>0,
and let theta_r(T)=arg U_r(c+iT). Real type makes the right-edge argument
change 2theta_r(T). Reflection (RV10) makes the left-edge contribution
equal to the right-edge contribution. The two horizontal contributions
are O_k(log(T+2)) by (RV17). The argument principle gives
\[
 2N_r^+(T)+R_r=\frac{2}{\pi}\theta_r(T)
                               +O_k(\log(T+2)),          \tag{RV18}
\]
where R_r is the finite total multiplicity of real zeros of U_r.
It is a fixed O_k(1) term; no assertion R_r=0 is needed.
Real poles at 0,1 have already been cleared and do not enter N_r^+.

Using logarithms of gamma continued from their positive real values,
Stirling on the fixed right line gives
\[
 \Im\log\Gamma(\alpha+iT)
 =T\log T-T+(\alpha-\tfrac12)\pi/2+O_\alpha(T^{-1}),
\]
and hence
\[
 \Im\log A(c+iT)
       =2T\log\frac{T}{2\pi e}+O_k(1).                  \tag{RV19}
\]
Indeed the exponential completion contributes -T log(4pi^2),
not -T log(2pi). The constant (4pi)^(-k+1) is positive real.
The clearing factor [s(s-1)]^r contributes O_k(1) to the right-edge
argument, and log F_r is uniformly bounded there. Thus
\[
 \theta_r(T)
 =2rT\log\frac{T}{2\pi e}-T\log P+O_k(1).               \tag{RV20}
\]
Equations (RV18)--(RV20) prove (RV3). Its rank difference proves (RV4)
because P is the SAME in both rows and d-(d-1)=1.

For a height containing zeros, take nonexceptional heights decreasing to T.
The divisors are locally finite in a fixed strip, so each positive count
stabilizes to the convention 0<Im rho<=T. Uniform constants in the previous
bounds permit the limit. Alternatively, (RV16)'s direct F_r version bounds
every jump by O_k(log(T+2)). Both approaches apply determinant by determinant;
N_Q itself is not assumed monotone. Enlarging the source-dependent constant
covers the compact range 2<=T<=T_0.

At every nonreal point,
ord Q=ord det I_d-ord det I_(d-1). Subtraction before or after summing
therefore gives the same NET count, even with arbitrarily many common zeros.
We do not infer an uncancelled denominator pole, finiteness of poles,
critical-line concentration, a positive divisor, or an unsigned RH theorem.
The positive leading SIGNED count is compatible with substantial positive
and negative divisor contributions.

## 6. Bounded replay and sources

The producer authenticates ten frozen parent files, then invokes ONLY the
authenticated family Miller constructor from its frozen Git bytes (not a
mutable current import). For dimensions 2,3,4 in all six residual classes
and the exceptional weights 124,248, it compares both exact E4/E6 basis
constructions through q^(d+2) and their complete frozen family digests.

For these twenty sources it forms finite coefficient matrices with columns
1,...,d+1, computes squared-minor Cauchy--Binet coefficients, and independently
compares their weighted sum with a rational Gaussian determinant of the finite
Gram matrix using weights n^(-2). For W its identically zero n=1 column is
explicitly retained/checked before removing it from subset enumeration.
These finite Grams are NOT evaluations of the analytically continued period
at w=2. They are bounded algebra controls; the infinite tail and leading
product theorem are proved in section 2, not numerically discarded.

Typed symbolic ledgers check the two gamma factors, the power of 4pi^2,
the coefficient 2r multiplying T log(T/(2pi e)), and cancellation of the
same formal log(d!) between ranks. No log, gamma, phase, period, zero or
contour integral is numerically evaluated. Separate non-native finite
signed-divisor controls test cutoff inclusion and common cancellation;
they are not samples of actual cusp-flag zeros.

Arithmetic is MIXED: EXACT_RATIONAL and CERTIFIED_INTEGER_COVERAGE,
without rounding. Strict int/bool separation, finite workload/bit/shape
caps, duplicate/nonfinite JSON rejection, LF-normalized source/artifact
hashes, and full typed fixture reconstruction are required. The written
analytic proof is not machine-certified by these controls.
The replay caps dimension at 20, columns at 21, subset enumeration at 4096,
exact rational numerator/denominator sizes at 4096 bits, local charged work
at 5000000 and frozen-constructor charged work at 2000000. Native q order
is exactly d+2<=22. Generic finite Gram exponents are integers 1 through 4;
the recorded native algebra uses 2. JSON/source/artifact bytes are capped
at 2000000; symbolic divisor controls have at most 32 nodes with coordinates
bounded by 32 and multiplicities between 1 and 32. None of these caps
limits the all-fixed-weight written theorem or certifies an analytic limit.

Classical inputs and attribution:

- CF1--CF4 at b69c854d9e3dd1db7b82d95fe6f032fe47d5306b:
  native Miller coefficients, absolute unfolding, poles and exact reflection.
  EF5--EF11 at a27781310ded92125ef16d97d78db4d97cec4c1b:
  actual theta-derived entire growth, not an abstract finite-order assumption.
- [Trudgian, An improved upper bound for the argument of the Riemann
  zeta-function on the critical line II, arXiv:1208.5846v2](https://arxiv.org/pdf/1208.5846v2),
  section 2 equation (2.4), the following real-part crossing argument,
  and section 3 Lemma 1: classical Backlund/Jensen machinery. Relevant
  PDF pages were visually inspected. No zeta-specific numerical constant
  or sharper Backlund reflection estimate is imported here.
- [Tao, 254A Supplement 3, section 4, Theorem 41](https://terrytao.wordpress.com/2014/12/15/254a-supplement-3-the-gamma-function-and-the-functional-equation-optional/):
  classical functional-equation/argument-principle counting framework.
- [Tao, Give yourself an epsilon of room, Exercise 1](https://terrytao.wordpress.com/2009/02/28/tricks-wiki-give-yourself-an-epsilon-of-room/):
  classical maximum-principle strip damping. The exact exp(epsilon s^2)
  argument and its source-specific hypotheses are written in section 3.

Remote reference bytes are not authenticated by the offline replay.
This is a classical counting method applied to this actual quotient,
not a new general Riemann--von Mangoldt theorem or a novelty guarantee.
