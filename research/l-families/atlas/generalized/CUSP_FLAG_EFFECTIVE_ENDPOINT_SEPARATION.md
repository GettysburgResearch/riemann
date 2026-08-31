# Cusp-flag quotient: effective endpoint separation and zero scale

Status: PROPOSED SOURCE-SPECIFIC ANALYTIC THEOREM; independent frozen-SHA
review required. Exactly five new files; the UQ and CZ parents are unchanged.
This is the actual canonical first-q-coefficient quotient, not a generic flag,
a model coefficient array, an eigenvalue sample, or a zeta/RH counterexample.

The complete UQ packet at bcd3ad5ff0c42e7b205663b68a010e2dbde6d941 and CZ
release at a12d0fbc9b17a29f4eb3aa7f984877ffd4c5e717 are frozen inputs.
All ten blobs are authenticated. The definitions of the source, Eisenstein
completion and Petersson measure are exactly theirs.

## 1. Statements with distinct effective and asymptotic quantifiers

Let k=12d, h=h_d=Delta E4^(3d-3)=CF's g_1, ell=[q], W=ker ell, and
G(f)=integral_F y^(k-2)|f|^2 dx dy. Let I(s), I_W(s) and
Q_k(s)=det I(s)/det I_W(s) be the native completed periods and quotient.
Write G_h=G(h)>0, and Lambda(u)=pi^(-u/2)Gamma(u/2)zeta(u).

**Effective theorem.** For EVERY multiple k=12d>=K=2^16=65536:
\[
 I_s(f,f)\le(-k/144+60)G(f)<0
 \quad(0\ne f\in W,\ 1-18/k\le s<1),                     \tag{EP1}
\]
and
\[
 I_{1-18/k}(h,h)/G_h
 \ge {773\over72000}k-{2019\over100}>0.                  \tag{EP2}
\]
Consequently Q_k has an uncancelled odd-order real-zero pair in
(1-18/k,1) and (0,18/k). The first admissible weight covered is 65544.
This is a conservative SUFFICIENT onset, not an optimal onset, nor a claim
about failure below it. It does NOT inherit CZ's different 6144 threshold.

**Asymptotic theorem.** Fix a nonempty compact real interval
J contained in (0,24). Put s=1-c/k, c in J, and L=log(k/(4*pi)).
For every fixed integer M>=0, uniformly over c in J and ALL f in W,
\[
 |I_s(h,f)|\le C_{J,M}k^{-M}\sqrt{G_hG(f)}.                \tag{EP3}
\]
There are thresholds depending on J,M; they are not asserted equal to K.
With B_0=(gamma-log(4*pi))/2,
\[
\begin{split}
 {Q_k(1-c/k)\over G_h}
 ={}&k\left({1\over24}-{1\over2c}\right)
 -\left({c\over24}+{1\over2}\right)L\\
 &+B_0-{1\over24}-{c\Lambda'(2)\over2\pi}
 +O_J(\log^2 k/k).                                      \tag{EP4}
\end{split}
\]
In particular there exists an uncancelled real-zero pair with
\[
 1-s_k={12\over k}+{288\log k+O(1)\over k^2}.             \tag{EP5}
\]
More precisely put C_12=B_0-1/24-6Lambda'(2)/pi. Such zeros can be chosen with
\[
 k(1-s_k)=12+{288L-288C_{12}\over k}
                  +O(\log^2 k/k^2).                    \tag{EP6}
\]
Every sequence of real zeros whose c=k(1-s) remains in a fixed compact
subset of (0,24) obeys EP6. No uniqueness, simplicity, derivative asymptotic,
global zero census, or exclusion of zeros escaping c->0 or c->24 is claimed.
In particular the effective theorem does not assign an effective error
constant or onset to the finer asymptotic location.

## 2. Native inputs retained, including normalization

On the standard domain F, y>=a=sqrt(3)/2, and for 3/4<=s<1 the exact
CZ half-lattice expansion is
\[
 E^*(z,s)=C(s)y^s+D(s)y^{1-s}+R_s(z),\quad
 C(s)=\Lambda(2s),\quad D(s)=\Lambda(2s-1),\quad
 |R_s(z)|\le {2r\over(1-r)^2}<1,\ r=e^{-2\pi y}<1/100.    \tag{EP7}
\]
The sharper last bound is UQ5: CZ's cosine coefficient is 4sqrt(y), and
K_nu<=K_(1/2) gives exactly the factor 2 displayed here. The printed
normalization discrepancy documented in CZ is not silently reintroduced.

UQ2--UQ3, by Parseval above y=1 and integration by parts, prove for ANY
cusp form beginning at q^N, N>=1,
\[
 \int_F\max(1,y)y^{k-2}|f|^2dxdy
 \le\left(1+{k-1\over4\pi N}\right)G(f).                 \tag{EP8}
\]
This applies to ALL of W with N=2 and to h with N=1, not just basis vectors.
We also retain |Delta|<1, |E4|<4 and |E4-1|<=480r on F.

## 3. Explicit completed-zeta bounds: no special-function sampling

Set F(u)=pi^(-u/2)Gamma(u/2). The Euler integral and its differentiated
version give, for 0<x<=1,
\[
 \Gamma(x)\le1/x+1/e,\qquad
 |\Gamma'(x)|\le1/x^2+2/e.                               \tag{EP9}
\]
Indeed split at t=1; on the lower part discard e^(-t), while on the upper
part use t^(x-1)<=1 and log t<=t. Since e>2, pi<4 and log pi<2:

- For u in [1/2,1], x=u/2 is in [1/4,1/2]; Gamma<5,
  |Gamma'|<17, hence F<5 and |F'|<(17+2*5)/2<14.
- For u in [3/2,2], x is in [3/4,1]; Gamma<2,
  |Gamma'|<3, hence F<2 and |F'|<(3+2*2)/2<4.

For real u>0, u!=1, Euler summation gives
\[
 \zeta(u)={u\over u-1}
 -u\int_1^\infty\{t\}t^{-u-1}dt
 ={1\over u-1}+H(u),\qquad 0\le H(u)\le1.                \tag{EP10}
\]
For completeness the first equality follows for u>1 by writing
zeta(u)=u integral_1^infinity floor(t)t^(-u-1)dt and splitting
floor(t)=t-{t}; the fractional-part integral converges holomorphically
for Re(u)>0 and so continues the identity there. Its real bound follows
from 0<=u integral {t}t^(-u-1)dt<=1.

Since F(1)=1, EP9--EP10 prove, for 0<epsilon<=1/4,
\[
 \left|\Lambda(1-2\epsilon)+{1\over2\epsilon}\right|
 \le14+5=19.                                            \tag{EP11}
\]
On u in [3/2,2], zeta(u)<=1+integral_1^infinity t^(-3/2)dt=3, and
\[
 |\zeta'(u)|
 \le\sum_{n\ge2}{\log n\over n^{3/2}}
 \le\int_1^\infty{\log(t+1)\over t^{3/2}}dt
 \le2\log2+4<6.
\]
The middle inequality holds termwise on [n-1,n], and log(t+1)<=log2+log t.
Thus |Lambda'|<=4*3+2*6=24 on this full interval, whence
\[
 |\Lambda(2-2\epsilon)-\pi/6|\le48\epsilon.               \tag{EP12}
\]
The constants 19 and 48 are explicit integral inequalities, not numerically
estimated Laurent coefficients.

## 4. Effective negativity for the complete canonical denominator

Now k>=K and 0<epsilon<=18/k. EP11 makes D(1-epsilon)<0.
Also a^epsilon>=1-epsilon because log a>-1; since a<1, EP11 implies
\[
 D(1-\epsilon)a^\epsilon\le-{1\over2\epsilon}+19+1/2.
\]
Apply EP7--EP8 as in UQ8:
\[
 {I_{1-\epsilon}(f,f)\over G(f)}
 \le(\pi/6+48\epsilon)\left(1+{k-1\over8\pi}\right)
       -{1\over2\epsilon}+19+1/2+1
 \le{k\over48}-{1\over2\epsilon}+60.                     \tag{EP13}
\]
Here the positive error is less than
2/3+1+36+19+1/2+1<60:
48epsilon<1, and 6epsilon(k-1)/pi<2epsilon*k<=36.
Since 1/(2epsilon)>=k/36 and K>8640, EP13 proves EP1.
Every inequality is uniform in epsilon and the entire vector f in W.

## 5. An all-weight quantitative mass comparison

Define the same comparison integrals as UQ10:
\[
 M_k(\beta)=\int_Fy^{k-2+\beta}|h|^2dxdy,\quad
 A_k(\beta)={\Gamma(k-1+\beta)\over(4\pi)^{k-1+\beta}},
 \quad0\le\beta\le1.                                    \tag{EP14}
\]
With Y=log k, r<=k^(-6) above Y, UQ12 gives
\[
 1-u\le |h/q|^2\le(1-u)^{-1},\quad
 u={48r\over1-r}+240kr\le289k^{-5}<1/1000.                \tag{EP15}
\]
The low h mass is <=(2Y)^k and the low comparison mass <=Y^k.
Writing X=k/(4*pi), the comparison integral on [X,X+1] is at least
X^(k-2)e^(-k-4*pi), uniformly in beta. Thus BOTH low-piece ratios are <B(k),
where
\[
 B(k)=3^{16}k^2\left({96\log k\over k}\right)^k
                                                <1/1000. \tag{EP16}
\]
Here 8*pi*e<96 and e^(4*pi)/(16*pi^2)<3^16.
The last inequality holds for EVERY integer k>=K, not only k=K:
log k/k decreases there, and
96 log K/K<96*16/65536=3/128<1/32.
Also k^2<=2^k for all integers k>=4: it holds at 4 and the ratio
2^k/k^2 is increasing for k>=3, since 2k^2-(k+1)^2=k^2-2k-1>0.
Consequently B(k)<3^16*2^(-4k)<2^(26-4k)<=2^(-10)<1/1000.
These are symbolic exponent inequalities; constructing 2^(4K) is unnecessary.
Similarly 289K^(-5)<1/1000 implies EP15 for every k>=K.

Combining the high and low pieces, with the whole x period present above Y,
proves the simultaneous comparison
\[
 {998\over1000}\le {M_k(\beta)\over A_k(\beta)}
       \le {1003\over1000}\quad(0\le\beta\le1,\ k\ge K).   \tag{EP17}
\]
Indeed the lower bound is (1-u)(1-B)>=1-u-B, and the upper bound is
(1-u)^(-1)+B<=1+2u+B. In particular the ratio of the lower to the upper
constant is 998/1003>99/100.

## 6. Jensen bounds and the explicit positive endpoint

Take epsilon=18/k. We have
18 log k/k<=18 log K/K<288/65536<1/200.
The probability density proportional to y^(k-1)e^(-4*pi*y) is Gamma with
shape k and rate 4*pi; its mean is k/(4*pi). Since y^(-epsilon) is convex,
Jensen and the elementary Gamma recurrence give
\[
 {A_k(1-\epsilon)\over A_k(0)}
 \ge {k-1\over4\pi}\left({k\over4\pi}\right)^{-\epsilon}.
\]
This is not a saddle approximation. Since k-1>=(999/1000)k,
k^(-epsilon)>=1-epsilon log k>199/200, and 4*pi>1, EP17 gives
\[
 {M_k(1-\epsilon)\over G_h}
 \ge {99\over100}{999\over1000}{199\over200}{k\over4\pi}
 >{49\over50}{k\over4\pi}.                               \tag{EP18}
\]

For the upper moment, Jensen for the concave function t^epsilon, applied
to the ACTUAL probability measure y^(k-2)|h|^2/G_h, and EP8 with N=1 give
\[
 {M_k(\epsilon)\over G_h}
 \le\left(1+{k-1\over4\pi}\right)^\epsilon
 \le k^\epsilon<e^{1/200}\le{200\over199}<{101\over100}.    \tag{EP19}
\]
Using max(1,y) first makes this step valid also below y=1.
Now 48epsilon=864/k<pi/120, so C(1-epsilon)>=(19/20)(pi/6).
Meanwhile D>=-k/36-19 and D<0. With EP7 and EP18--EP19,
\[
 {I_{1-18/k}(h,h)\over G_h}
 \ge {19\over20}{49\over50}{k\over24}
       -{101\over100}\left({k\over36}+19\right)-1
 ={773\over72000}k-{2019\over100}>0.                     \tag{EP20}
\]
The final positive affine function is increasing and positive already at K;
it is a uniform elementary threshold proof, not a list of period samples.

EP1 makes I_W invertible along the full interval. In the adapted basis
(h,f_2,...,f_d), the real Schur identity gives Q>=I(h,h)>0 at its left end.
The unchanged CF4 residue is positive, so Q(s)<0 sufficiently near 1
for each fixed k. Continuity, analyticity and denominator nonvanishing give
an odd-order uncancelled zero; entrywise reflection gives its equal-order mate.
This repeats only the now-effective conclusion of UQ18, not an indefinite
positive-form minimization. Corank one and nonzero ell on the nullvector
follow exactly as in UQ section7.

## 7. Uniform actual Schur decoupling: the previously missing bound

Fix J=[c_-,c_+] contained in (0,24). Constants in this section may depend
on J and a fixed requested decay order M, never on the dimension or f in W.
Repeating EP13 with epsilon<=c_+/k replaces its numerical error60 by an
O_J(1) error: the coefficient error is O(epsilon*k)=O_J(1), and EP11's
remaining error is absolute. Thus for all sufficiently large k,
\[
 I_{1-c/k}(f,f)\le-\kappa_J kG(f),\qquad
 \kappa_J={1\over2}\left({1\over2c_+}-{1\over48}\right)>0. \tag{EP21}
\]
This compact-c statement is not asserted uniformly as c approaches 0 or 24.

Choose a FIXED positive integer A and split at Y=A log k. Set
r_Y=k^(-2*pi*A). Product telescoping, not a modulus-only argument, proves
\[
 \delta_Y=\sup_{y\ge Y,x}|h/q-1|=O_A(kr_Y).               \tag{EP22}
\]
In detail, for any finite product,
|product(1+z_j)-1|<=product(1+|z_j|)-1<=exp(sum|z_j|)-1.
Apply this to 24 copies of -q^n and k/4-3 copies of E4-1.
Their absolute sums are <=24r/(1-r)+120kr. Pass to the convergent infinite
Delta product, then use exp(v)-1<=2v for small positive v. This controls
the complex ratio itself; |h/q| near one alone would NOT suffice.

Write P_s(y)=C(s)y^s+D(s)y^(1-s). Uniformly for c in J,
|P_s(y)|<=C_J k max(1,y), while EP7 gives |R_s(z)|<=C r_Y above Y.
For every f in W and every y>=Y, the source Fourier gap gives exactly
\[
 \int_{-1/2}^{1/2}\overline q\,f(x+iy)\,dx=0.             \tag{EP23}
\]
Therefore the P_s part of the high integral I_s(h,f) may replace h by h-q.
EP8, Cauchy--Schwarz with positive weight max(1,y), EP22 and
A_k(1)/G_h=O(k) yield its bound
\[
 C_J k^2\delta_Y\sqrt{G_hG(f)}.
\]
Here the error's weighted norm squared is <=delta_Y^2 A_k(1);
the W weighted norm squared is O(kG(f)), uniformly over ALL W.
The high R part is <=C r_Y sqrt(G_hG(f)).
On the low region |E*|<=C_J kY and UQ13--UQ14 with Y=A log k give
\[
 {G(h; y\le Y)\over G_h}
 \le \ell_A(k)\ll_A k^2
       \left({8\pi e A\log k\over k}\right)^k,
\]
which decreases faster than every inverse fixed power of k. Thus
\[
 {|I_s(h,f)|\over\sqrt{G_hG(f)}}
 \ll_{J,A}k^2\delta_Y+r_Y+kY\sqrt{\ell_A(k)}
 =O_{J,A}(k^{3-2\pi A})+\hbox{superpolynomial remainder}. \tag{EP24}
\]
For each fixed M choose A>(M+3)/6, using pi>3. This proves EP3.
A depends on M but not k; no uniform assertion in growing M is being made.

Let b be the cross functional in W and D=I_W. Its dual Petersson norm
satisfies b^*G_W^(-1)b<=C_(J,M)^2 k^(-2M)G_h by EP3.
EP21 implies (-D)^(-1)<=1/(kappa_J*k) G_W^(-1), so
\[
 0\le Q_k(1-c/k)-I_{1-c/k}(h,h)
 \le {C_{J,M}^2\over\kappa_J}k^{-2M-1}G_h.               \tag{EP25}
\]
This is a coordinate-free bound on the actual source functional and inverse.
There is no dimension factor, free-coefficient replacement, or norm change.
The raw witness and the canonical quotient are thereby equal to arbitrary
fixed algebraic precision after division by G_h.

## 8. Uniform expansion and the location constant

The same high/low split with A chosen sufficiently large gives
M_k(beta)=A_k(beta)(1+O_N(k^(-N))) uniformly 0<=beta<=1 for every fixed N.
It also makes integral R_s|h|^2/G_h=O_N(k^(-N)) uniformly c in J:
above Y use EP7, below Y use the low h mass. This is stronger than merely
using |R|<1 when a second-order location is wanted.

Put epsilon=c/k. The positive-real digamma estimate
psi(x)=log x+O(1/x), uniform on [k-1,k+1], gives
\[
 {\Gamma(k-1+\epsilon)\over\Gamma(k-1)}
 =\exp(\epsilon\log k+O_J(k^{-2})),
\]
\[
 {\Gamma(k-\epsilon)\over\Gamma(k-1)}
 =(k-1)\exp(-\epsilon\log k+O_J(k^{-2})).
\]
These follow by integrating psi over intervals of length epsilon;
a generic uniform Gamma-ratio error O(1/k) alone is too coarse here.
Consequently
\[
 {M_k(\epsilon)\over G_h}
 =1+{cL\over k}+O_J(\log^2 k/k^2),\qquad
 {M_k(1-\epsilon)\over G_h}
 ={k-1-cL\over4\pi}+O_J(\log^2 k/k).                     \tag{EP26}
\]
The native Laurent expansions from CZ and regular Taylor expansion at 2 give
\[
 C(1-c/k)=\pi/6-{2c\Lambda'(2)\over k}+O_J(k^{-2}),\quad
 D(1-c/k)=-{k\over2c}+B_0+O_J(k^{-1}).                   \tag{EP27}
\]
Multiplying EP26--EP27, retaining the -1/(4*pi) term, proves EP4 for I(h,h).
EP25 transfers it to the actual canonical Q without a hidden Schur constant.

To justify the zero statement, use any fixed interval J around 12 contained
in (0,24). The leading function f(c)=1/24-1/(2c) has a simple zero at 12
and f'(12)=1/288. Uniform EP4 gives opposite signs at fixed points on its
two sides for sufficiently large k; EP21 excludes denominator zeros between
them. Thus there is an uncancelled real zero there.
At any zero staying in J, EP4 first forces c=12+O(log k/k).
Taylor expansion then gives, uniformly at such zeros,
\[
 0={k\over288}(c-12)-L+C_{12}+O(\log^2 k/k),
\]
proving EP6 and EP5. More generally if c stays in any fixed compact subset
of (0,24), the leading equation first forces c->12, so the same conclusion
applies. Reflection preserves the order, and sign change ensures an odd-order
choice. No derivative bound or Rouche argument is used to claim uniqueness.

## 9. Exact replay and classical boundaries

The finite producer checks rational integral-envelope constants, the affine
sign margins and all-integer monotonicity certificates, Gamma-Jensen factors,
symbolic exponent budgets and the exact coefficients 12 and 288.
It independently constructs actual Delta^j E4^(k/4-3j) q-prefixes by finite
binomial convolution at the first covered weights, and compares overlapping
prefixes with the frozen UQ source. It does NOT sample periods, zeros, special
functions, logarithms or exponentials. The all-weight/analytic proofs remain
the written arguments, not conclusions obtained from these finite models.

Arithmetic taxonomy is MIXED, with CERTIFIED_INTEGER_COVERAGE and
EXACT_RATIONAL; no rounding. Strict bool/int separation, 4096-bit rational
caps, q order<=8, numerical control weight<=2^20, fixed decay-order controls
<=32, a 2,000,000-unit charged work cap and 2,000,000-byte/20,000-node JSON
caps fail closed. Complete typed reconstruction authenticates all ten source
blobs, four artifact hashes and the canonical payload seal, in normal and -O
Python. The theorem's unbounded quantifiers are not bounded by machine caps.

The mechanisms are classical Euler summation, Gamma integrals, Jensen,
Parseval, elementary concentration and Schur algebra. Additional primary
reference formulas checked are
[DLMF25.11.5](https://dlmf.nist.gov/25.11.E5),
[DLMF5.9.19](https://dlmf.nist.gov/5.9.E19), and
[DLMF5.11.2](https://dlmf.nist.gov/5.11.E2).
EP9--EP12 give their required bounds directly; remote bytes are not
authenticated. All modular/Eisenstein normalization references remain pinned
through CZ and UQ. No new abstract asymptotic theory, novel automorphic family,
exhaustive novelty search, zeta/RH counterexample, or global zero classification
is asserted.

Release gates: named tests and producer --check in normal and -O Python,
both emission modes in both modes, Ruff, fresh exact-SHA replay and the complete
authoring-base-to-head whitespace check. Independent analytic review is required.
