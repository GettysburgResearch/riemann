# Canonical cusp-flag quotient: uncancelled off-central real zeros

Status: PROPOSED SOURCE-SPECIFIC ANALYTIC THEOREM; independent frozen-SHA
review required. This is a new five-file packet, not an edit to its parents.
The conclusion concerns the ACTUAL canonical first-q-coefficient quotient.
There exists an onset k_0; this packet does NOT certify k_0=6144 or any other
numerical onset. No zeta/RH counterexample or new automorphic family is claimed.

Frozen sources: the complete five-file CF family at
b69c854d9e3dd1db7b82d95fe6f032fe47d5306b and the complete five-file CZ release
at a12d0fbc9b17a29f4eb3aa7f984877ffd4c5e717. The latter preserves CZ's
scientific argument, correcting a control character in a displayed fraction.
All ten literal Git objects are authenticated; none is modified here.

## 1. The result and the newly paid native condition

Let k=12d and use the same real Miller basis of S_k(SL(2,Z)), the same
q=exp(2*pi*i*z), and the exact first-coefficient functional ell(f)=[q]f.
Let W=ker ell, I_k(s) be CF2's full completed period matrix, I_W its
restriction, G the Petersson Gram, and
\[
 Q_k(s)=\frac{\det I_k(s)}{\det I_W(s)},\qquad
 h_d=\Delta E_4^{3d-3},\quad \ell(h_d)=1,\quad
 \sigma_k=1-\frac{18}{k}.                                  \tag{UQ1}
\]
The vector h_d is CF's g_1, not Miller f_d. Write
G(f)=integral_F y^k|f(z)|^2 dmu, with dmu=dx*dy/y^2.

**Theorem.** There is an integer k_0 such that for every multiple k=12d>=k_0:

1. I_W(s) is negative definite for EVERY real s in [sigma_k,1).
2. I_(h_d)(sigma_k)>0 and Q_k(sigma_k)>0.
3. Q_k has a real zero s_k in (sigma_k,1), and an equal-order reflected
   zero 1-s_k in (0,18/k). At least one such pair has odd zero order.
   Both are genuine, uncancelled zeros, not poles or formal parent zeros.

Increase k_0 if necessary so k_0>72, hence sigma_k>3/4 and both intervals
are off the central point. The denominator is nonzero on both intervals.
At any of these zeros the full matrix has corank one and its nullvector
is not in W. No simplicity, uniqueness, numerical location, or optimal onset
is asserted. The canonical observable (I_k(s)^(-1))_(11)=1/Q_k(s) has a
genuine pole there, interpreted meromorphically.

The load-bearing improvement over CZ is a bound uniform over ALL of W.
It is not the assertion that a single positive vector lies outside W.
CZ's eventual positive W witnesses at s=1/2 are compatible with negativity
on the much smaller interval near 1 used here.

## 2. A uniform Parseval moment bound for the actual flag

Let f(z)=sum_(n>=N) a_n exp(2*pi*i*n*z) be ANY nonzero cusp form of weight
k>=2 whose first N-1 coefficients vanish. The actual W has N=2. No bound
on the individual coefficients, no finite prefix approximation, and no
hypothetical freedom to choose them will be used.

The standard fundamental domain F has y>=a=sqrt(3)/2 and contains the
whole cusp rectangle |x|<=1/2, y>=1. On that rectangle Parseval gives
\[
 \int_{-1/2}^{1/2}|f(x+iy)|^2dx
     =\sum_{n\ge N}|a_n|^2e^{-4\pi ny}.                    \tag{UQ2}
\]
Fourier convergence for y>=1 and then Tonelli justify every positive sum
and integral. For c>0 and m=k-2>=0 set
\[
 J_m(c)=\int_1^\infty y^m e^{-cy}dy.
\]
Integration by parts, with the boundary term retained, gives
\[
 J_{m+1}(c)=\frac{e^{-c}}c+\frac{m+1}{c}J_m(c),\qquad
 J_m(c)\ge\frac{e^{-c}}c.
\]
Consequently J_(m+1)/J_m<=1+(m+1)/c. Apply this termwise at c=4*pi*n.
On F below y=1 the function max(1,y) is exactly one. Combining the two
parts of the SAME Petersson integral therefore proves
\[
 \boxed{\int_F \max(1,y)y^k|f|^2d\mu
       \le \left(1+\frac{k-1}{4\pi N}\right)G(f).}         \tag{UQ3}
\]
The bound is homogeneous and uniform over the entire indicated subspace.
In particular it holds simultaneously for every f in W with N=2.

An exact polynomial version explains the finite replay:
\[
 J_m(c)=e^{-c}c^{-m-1}P_m(c),\qquad
 P_m(c)=\sum_{j=0}^m\frac{m!}{j!}c^j.
\]
Then P_(m+1)=(m+1)P_m+c^(m+1), and
(c+m+1)P_m-P_(m+1)=c(P_m-c^m) has nonnegative coefficients.
The written induction proves this for all m; checking small polynomials
does not replace UQ2--UQ3 or its all-W quantifier.

## 3. Uniform Eisenstein expansion near the pole

Use the exact CF/CZ completion, not an uncompleted Eisenstein series.
Put Lambda(u)=pi^(-u/2)Gamma(u/2)zeta(u). The directly derived Fourier
normalization CZ3--CZ5 gives for 3/4<=sigma<1
\[
 E^*(z,\sigma)=C(\sigma)y^\sigma+D(\sigma)y^{1-\sigma}
                     +R_\sigma(z),\quad
 C(\sigma)=\Lambda(2\sigma),\quad D(\sigma)=\Lambda(2\sigma-1).
                                                               \tag{UQ4}
\]
The cosine coefficient is 4*sqrt(y), as derived from the half-lattice
Mellin formula in CZ, not the inconsistent printed factor in Zagier's
equation (14). No normalization or source identity is changed here.

For real 0<=nu<=1/2 and t>0 the integral
K_nu(t)=integral_0^infinity exp(-t*cosh u)cosh(nu*u)du gives
K_nu(t)<=K_(1/2)(t)=sqrt(pi/(2t))*exp(-t).
CZ's elementary geometry gives r=exp(-2*pi*y)<1/100 on F.
Since n^(sigma-1)<=1 and sigma_(1-2sigma)(n)<=tau(n)<=n,
\[
 |R_\sigma(z)|
 \le2\sum_{n\ge1}n r^n
 =\frac{2r}{(1-r)^2}<1                                   \tag{UQ5}
\]
uniformly over z in F and sigma in [3/4,1).
There is no Fourier cancellation or compact-only remainder estimate.

For epsilon=1-sigma tending to zero through positive reals, the classical
simple pole of Lambda at 1 and its regular value at 2 give
\[
 C(1-\epsilon)=\frac{\pi}{6}+O(\epsilon),\qquad
 D(1-\epsilon)=-\frac1{2\epsilon}+O(1).                   \tag{UQ6}
\]
More explicitly, there exist fixed epsilon_0>0 and constants C_1,C_2
such that these two remainder bounds hold for 0<epsilon<=epsilon_0.
They depend only on this fixed Eisenstein function, not on k or f.
Shrink epsilon_0 so D(1-epsilon)<0 and C(1-epsilon)>0 there.
Since a^epsilon=1+O(epsilon), also
\[
 D(1-\epsilon)a^\epsilon=-\frac1{2\epsilon}+O(1)           \tag{UQ7}
\]
uniformly on that punctured interval. This retains the part of F with y<1:
replacing y^epsilon by 1 everywhere would have the wrong justification.

## 4. Negativity on the complete denominator space

For real sigma in [3/4,1), y^sigma<=max(1,y); also y^epsilon>=a^epsilon.
Because D is negative, UQ4--UQ7 and the all-W estimate UQ3 imply
\[
 \frac{I_f(1-\epsilon)}{G(f)}
 \le C(1-\epsilon)\left(1+\frac{k-1}{8\pi}\right)
            +D(1-\epsilon)a^\epsilon+1
 \le\frac{k}{48}-\frac1{2\epsilon}+O(1)                  \tag{UQ8}
\]
for EVERY nonzero f in W, uniformly for 0<epsilon<=18/k and all sufficiently
large k. The O(1) is uniform in k, epsilon AND f: the C error contributes
O(epsilon*k)=O(1), while UQ7 and UQ5 have absolute bounded errors.
Therefore throughout this entire interval
\[
 \boxed{I_f(1-\epsilon)/G(f)\le-\frac{k}{144}+O(1)<0.}     \tag{UQ9}
\]
Choosing k beyond one fixed threshold proves negative definiteness of
I_W(s) on [sigma_k,1), not just at a selected endpoint or for selected
basis vectors. In particular det I_W has no real zeros there.
All W coefficients and cross terms are covered by UQ2's positive Parseval
sum; no diagonalization of the period family was assumed.

## 5. Uniform normalized concentration of the actual g_1 witness

Define, for 0<=beta<=1,
\[
 M_k(\beta)=\int_F y^{k-2+\beta}|h_d(z)|^2dx\,dy,\qquad
 A_k(\beta)=\int_0^\infty y^{k-2+\beta}e^{-4\pi y}dy
 =\frac{\Gamma(k-1+\beta)}{(4\pi)^{k-1+\beta}}.             \tag{UQ10}
\]
Here M_k(0)=G(h_d)>0; A_k is only a scalar comparison integral, not a
replacement source matrix or a changed completion.

We prove, uniformly for beta in [0,1],
\[
 M_k(\beta)=A_k(\beta)(1+O(k^{-5})).                        \tag{UQ11}
\]
Take Y=log k. For sufficiently large k, Y>=1. On y>=Y, CZ9 gives
|E4-1|<=480r, and pi>3 gives r<=k^(-6).
The Delta product with 48 copies, Bernoulli's inequality, and
log(1+t)<=t show, with
\[
 u=48r/(1-r)+240kr,
\]
that
\[
 1-u\le |\Delta/q|^2|E4|^{k/2-6}
       \le e^u\le(1-u)^{-1},\qquad u\le289k^{-5}.          \tag{UQ12}
\]
For large k, u<=1/2; hence the middle expression is 1+O(k^(-5)).
For precision, |Delta/q|^2>=1-48r/(1-r), while
|E4|^(k/2-6)>=(1-480r)^(k/2-6)>=1-240kr.
Both lower factors are nonnegative for large k, so their product is at
least 1-u. The upper logarithm is at most u. Finally
48/(1-r)<49 when r<=1/100. These are bounds on actual complex modular
forms uniform in x, not only on the imaginary axis.

The part with y<=Y is negligible uniformly in beta. CZ gives
|Delta|<1 and |E4|<4 on F, so |h_d|^2<=2^k. Since y>=a,
k-2+beta>=0, Y>=1, and the x width is at most one,
\[
 0\le \int_{F\cap\{y\le Y\}}y^{k-2+\beta}|h_d|^2dx\,dy
          \le(2Y)^k.                                    \tag{UQ13}
\]
The analogous comparison integral over 0<=y<=Y is at most Y^k.
For X=k/(4*pi)>=1, integrating the comparison integrand only over
[X,X+1] gives the beta-uniform lower bound
A_k(beta)>=X^(k-2)*exp(-k-4*pi).
Thus each low-piece ratio is bounded by
\[
 O\left(k^2\left(\frac{8\pi e\log k}{k}\right)^k\right)
          =o(k^{-m})\quad\hbox{for every fixed }m.         \tag{UQ14}
\]
To justify the last limit, eventually (8*pi*e*log k)/k<1/2; then
k^(m+2)*2^(-k) tends to zero, for example by its consecutive-term ratio.
No transcendental samples establish this limit.
For y>=Y the entire horizontal period is present in F, so UQ12 compares
its integral directly with A_k(beta)'s high piece. UQ13--UQ14 prove UQ11.

There is no missing uncontrolled compact contribution of E* at the moving
point sigma_k: on y<=Y, UQ4--UQ6 give |E*(z,sigma_k)|=O(k+Y).
Indeed y^sigma_k<=max(1,Y), y^(18/k)<=max(1,Y^(18/k)) is bounded, and
D(sigma_k)=O(k). Multiplying this estimate by UQ13 is still negligible
compared with k*A_k(0). Equivalently the exact decomposition in UQ4
reduces the full period to the already controlled three integrals.

## 6. The positive endpoint, including its normalized constant

For x=k-1 and beta in [0,1], the positive-real digamma estimate
psi(x+t)=log x+O(1/x), uniformly 0<=t<=1, implies
\[
 \frac{\Gamma(k-1+\beta)}{\Gamma(k-1)}
       =(k-1)^\beta(1+O(1/k)).                            \tag{UQ15}
\]
This follows by integrating psi from x to x+beta and exponentiating a
uniform O(1/k) error, rather than assuming a uniform ratio theorem.
Use UQ11 and UQ15 with epsilon_k=18/k. Since
epsilon_k*log((k-1)/(4*pi))=O(log k/k),
\[
 \frac{M_k(1-\epsilon_k)}{kM_k(0)}
       =\frac1{4\pi}+O(\log k/k),\qquad
 \frac{M_k(\epsilon_k)}{M_k(0)}
       =1+O(\log k/k).                                   \tag{UQ16}
\]
Equation UQ5 bounds the remainder integral in UQ4 by M_k(0).
Combining UQ6 and UQ16, with D(sigma_k)/k=-1/36+O(1/k), proves
\[
 \boxed{\frac{I_{h_d}(\sigma_k)}{kG(h_d)}
       =\frac1{24}-\frac1{36}+O(\log k/k)
       =\frac1{72}+O(\log k/k)>0}                         \tag{UQ17}
\]
eventually. The constants are independent of the growing dimension because
the explicit modular expression h_d and the uniform estimates above were
used throughout. This does not assert a numerical onset.

The value 18 separates two genuine native scales: the first Fourier
frequency gives 1/24, while W's first possible frequency 2 gives 1/48.
The pole contributes -1/36 at epsilon=18/k. No arbitrary flag has replaced
ell, and no finite coefficient census proves the separation.

## 7. Actual noncancellation, corank, and reflected zeros

At sigma_k use the adapted basis (h_d,f_2,...,f_d). It has the same
first-coefficient normalization as the Miller basis, so CF's canonical
quotient is unchanged. Write its real symmetric period matrix as
\[
 I=\begin{pmatrix}a&b^t\\b&D\end{pmatrix},\qquad D=I_W.
\]
By UQ9, D is negative definite. Gaussian elimination by an invertible
constant-at-this-point congruence gives
\[
 Q_k(\sigma_k)=a-b^tD^{-1}b\ge a=I_{h_d}(\sigma_k)>0.      \tag{UQ18}
\]
This is elementary Schur algebra AFTER full-space negativity has been
proved for W. It is not an indefinite minimization principle.

CF4 gives
Q_k(s)=r_k/(s-1)+O_k(1), with
r_k=det G/(2 det G_W)>0. Hence Q_k(s)<0 for real s<1 sufficiently close
to 1, for each fixed k. UQ9 guarantees that Q is analytic and real-valued
on [sigma_k,1), with no denominator zero in the path.
Choose an endpoint before 1 at which Q is negative. Continuity gives a
zero between it and sigma_k. A nonzero analytic real function has finitely
many zeros on this closed subinterval; a sign change forces at least one
of them to have odd order.

At a zero, D remains invertible; block elimination gives rank(I)=d-1,
and any nullvector with first coefficient zero would contradict the
negative definiteness of D. Moreover
ord(det I)=ord(Q), since det D is nonzero: cancellation is impossible.
The cofactor identity (I^(-1))_(11)=det I_W/det I=1/Q holds meromorphically
in the original Miller coordinates, so this canonical observable has a pole.

Entrywise CF reflection I(s)=I(1-s) also applies to I_W. Thus the reflected
denominator is nonzero and Q(1-s)=Q(s) transfers the zero with the same
order to (0,18/k). This is a result about the signed divisor of the actual
quotient, not about zeta's divisor or an assumed RH-type positivity theorem.

## 8. Replay limits and references

The exact producer reconstructs the incomplete-Gamma polynomials and the
nonnegative gap identity by separate coefficient formulas/recurrences;
checks the native first-frequency/pole constants as exact rational symbolic
cancellations; verifies the modular quotient envelope UQ12; and authenticates
actual small Miller W bases plus source-bound high-weight h_d prefixes.
Its finite controls do NOT evaluate periods, Gamma/Bessel functions,
exponentials, eigenvalues, zeros, the onset k_0, or any analytic limit.
No unrelated rational-matrix toy is used to pay the all-W bound.

Arithmetic taxonomy is MIXED: CERTIFIED_INTEGER_COVERAGE and EXACT_RATIONAL,
with no rounding. Rational components are capped at 4096 bits, the finite
Gamma-polynomial degree at 12, numerical control weight at 12288, q order
at 8, JSON/source/artifact bytes at 2,000,000, total JSON nodes at 20,000,
and local charged work at 2,000,000. Authenticated source helpers have
separate capped work accounts. These machine caps do not bound the theorem.
Complete typed schemas, literal frozen hashes, all four artifact seals,
payload digest, duplicate/nonfinite JSON rejection, strict bool/int separation,
and forbidden control-character checks are enforced in normal and -O modes.

The classical inputs are Parseval, Tonelli, integration by parts, the
Eisenstein continuation/residue in CF/CZ, and elementary finite-dimensional
Schur/inertia algebra. The normalizations and the known printed discrepancy
remain documented in the frozen CZ proof, not silently corrected here.
For the additional special-function estimates, primary reference formulas are
[DLMF 10.32.9](https://dlmf.nist.gov/10.32.E9),
[DLMF 10.39.2](https://dlmf.nist.gov/10.39.E2), and
[DLMF 5.11.2 with its positive-real remainder bound](https://dlmf.nist.gov/5.11).
Their exact hypotheses are used only on positive real arguments and bounded
orders. Remote bytes are not authenticated by the offline producer.
No new abstract concentration, Schur, or zero theory is claimed, and the
limited literature check is not an exhaustive novelty search.

Release checks are the named unittest file in normal and -O Python, both
producer --check runs, both --emit-report/--emit-manifest modes, Ruff, and the
complete authoring-base-to-frozen-head whitespace check. Independent analytic
review is necessary before scientific acceptance.
