# Cusp-flag quotient: finite-order divisor and explicit formula

Status: PROPOSED SOURCE-SPECIFIC THEOREM; exact-SHA independent review required.
Scope: each FIXED even level-one weight k with d=dim S_k>=2, the full canonical
Miller basis and first-coefficient flag of CF1, and the unchanged completion.
RH remains unsolved. This is a classical explicit-formula construction for
the actual quotient, not a new abstract Poisson--Newton theorem.

Scientific parent: CF1--CF12 at 43ecb4ac3f2487ee944b6bb6bef72e1ad92f2678;
its metadata-only release b69c854d9e3dd1db7b82d95fe6f032fe47d5306b supplies
the five frozen family files. PS1/PS8 at 1483ff25e9100276ac7064ba7d7d696b45afb9ea
is normalization context. None of those files is changed.

What is replayed: complete logarithmic-frequency prefixes derived from six
authenticated complete parent prefixes, formal log/exp reconstruction,
independent zeta prime-power corrections, and exact completion/divisor algebra.
No period, zero, high derivative, gamma value, or analytic limit is sampled.
Smallest remaining quantitative boundary: numerical bounds for the actual
growth constants/Jensen anchors and any useful signed-divisor cancellation;
no zero distribution or positive Weil functional is supplied.

## 1. The native object and theorem

Keep the parent's real integral Miller basis f_1,...,f_d, ell(f)=[q]f,
W=ker ell, N=d+1, w=s+k-1, and
\[
 I_{ij}(s)=\int_{\mathcal F}y^k\overline{f_i(z)}f_j(z)E^*(z,s)\,d\mu,
 \quad Q_k(s)=\frac{\det I_k(s)}{\det I_W(s)}.
\]
Here dmu=dx dy/y^2 and F is the standard SL(2,Z) fundamental domain, with
|x|<=1/2 and y>=a=sqrt(3)/2. With the exact parent normalization,
\[
 Q_k(s)=A_k(s)\mathcal L_k(s+k-1),\quad
 A_k(s)=\pi^{-s}(4\pi)^{-s-k+1}\Gamma(s)\Gamma(s+k-1),        \tag{EF1}
\]
and mathcal L_k(w)=zeta(2w-2k+2)mathcal F_k(w).
The original period is sesquilinear in its form arguments, but meromorphic
in s. No conjugation of s occurs.

**Theorem.** Put J(s)=s(s-1)I(s). Its entries are entire and satisfy
log^+ max_(|s|<=R)|J_ij(s)|=O_k(R log(R+2)). Both determinants det J and
det J_W are nonzero entire functions with the same growth scale. Thus
Q_k and mathcal L_k are meromorphic of Nevanlinna order at most one, and
\[
 \sum_{|\rho|\le R}|\operatorname{ord}_\rho Q_k|
 +\sum_{|\rho|\le R}|\operatorname{ord}_\rho\mathcal L_k|
       =O_k(R\log(R+2)).                                  \tag{EF2}
\]
The two sums use their own stated s and w coordinates. Orders are NET
multiplicities: positive for zeros, negative for poles, after all cancellations.
The constants depend on this fixed weight/source. This is an upper bound,
not an asymptotic zero-count formula or a numerical certificate.

The net divisor of Q_k lies in some finite vertical strip. The divisor of
mathcal L_k need only be left-located: gamma trivial-zero ladders prevent
silently assigning the same strip to it.

Write, on a sufficiently right half-plane,
\[
 -\log\mathcal L_k(w)=\sum_{\lambda\in\Lambda_k}b_\lambda e^{-\lambda w}.
                                                                    \tag{EF3}
\]
All equal frequencies are combined. Lambda_k is a locally finite subset of
(0,infinity), and lambda=log rho for positive rational rho>1. The expansion
and its logarithmic derivative converge absolutely farther right.

For every phi in C_c^\infty((0,infinity)), the actual completed quotient obeys
\[
 \boxed{\begin{aligned}
 \sum_{\rho\in\operatorname{div}Q_k}\nu_\rho
       \int_0^\infty e^{\rho t}\phi(t)\,dt
  ={}&\sum_{\lambda\in\Lambda_k}
       \lambda\,b_\lambda\,e^{-(k-1)\lambda}\phi(\lambda)\\
    &-\int_0^\infty
       \frac{1+e^{-(k-1)t}}{1-e^{-t}}\phi(t)\,dt .
 \end{aligned}}                                                   \tag{EF4}
\]
The lambda multiplier in the atomic mass is essential. The left TEST
PAIRING is absolutely convergent; its exponential series is not asserted
to converge pointwise. The atomic sum is finite on this compact support.
The excluded origin can carry a normalization-dependent delta distribution;
(EF4) does not discard it for tests that meet zero.

## 2. A direct theta bound, not an assumed finite-order axiom

Define the unimodular lattice theta series
\[
 \Theta_z(u)=\sum_{m,n\in\mathbb Z}
 \exp\!\left[-\pi u\left(m^2y+\frac{(mx+n)^2}{y}\right)\right].
\]
Zagier's equations (6)--(7), with the sign-identified primitive normalization,
give E*(z,s)=(1/2)int_0^infinity(Theta_z(u)-1)u^(s-1)du initially for Re s>1.
Poisson summation gives Theta_z(1/u)=u Theta_z(u). Splitting at one yields
\[
 E^*(z,s)=\frac1{2s(s-1)}
  +\frac12\int_1^\infty(\Theta_z(u)-1)(u^{s-1}+u^{-s})\,du. \tag{EF5}
\]
In particular the residues are -1/2 at zero and +1/2 at one, as in CF2.

For each fixed cusp form put
C_i=sum_(n>=1)|a_i(n)| exp(-2pi(n-1)a)<infinity.
Absolute convergence of its q series at exp(-2pi a)<1 gives
|f_i(x+iy)|<=C_i exp(-2pi y) for y>=a. No Ramanujan or RH bound is used.

For v>0 and any real shift theta, the Gaussian sum satisfies
sum_n exp(-pi v(n+theta)^2)<=1+v^(-1/2).
One proof uses Poisson summation to maximize the periodic Gaussian at theta=0,
then compares the unshifted tail with its integral. Also
\[
 2\sum_{n\ge1}e^{-\pi v n^2}
       \le\sqrt{2/v}\,e^{-\pi v/2};
\]
split each exponent in half and compare one half-sum with int_0^infinity.
Separating m=0 from m!=0 therefore gives, for u>=1,
\[
 0\le\Theta_z(u)-1
 \le\sqrt{2y/u}\,e^{-\pi u/(2y)}
 +(1+\sqrt{y/u})\sqrt{2/(uy)}\,e^{-\pi uy/2}.               \tag{EF6}
\]

Let H_ij(u)=int_F y^k bar f_i f_j(Theta_z(u)-1)dmu.
Use the containing strip |x|<=1/2,y>=a for absolute upper bounds. In the first
term of (EF6), reserve exp(-2pi y) and use
2pi y+pi u/(2y)>=2pi sqrt(u). In the second, use y>=a and u>=sqrt(u).
It follows explicitly that
\[
 |H_{ij}(u)|\le C_{ij}^H e^{-c\sqrt u},\quad c=\pi a/2,
                                                                  \tag{EF7}
\]
where one valid finite constant is
\[
 C_{ij}^H=\sqrt2 C_iC_j\left[
 \int_a^\infty y^{k-3/2}e^{-2\pi y}dy+
 \int_a^\infty (y^{k-5/2}+y^{k-2})e^{-4\pi y}dy\right].
\]
This controls the entire cusp, including large y where the shortest lattice
vector is small. A uniform exp(-c u) theta bound over F would be false.

The absolute bounds justify pairing (EF5) and Fubini initially on Re s>1;
they also justify locally uniform continuation of its paired integral to
every compact set of s. With G the Petersson Gram,
\[
 J_{ij}(s)=G_{ij}/2+
 \frac{s(s-1)}2\int_1^\infty H_{ij}(u)(u^{s-1}+u^{-s})du.   \tag{EF8}
\]
All entries are therefore entire. Taking C_H=max_ij C_ij^H and
G_0=max_ij |G_ij|, for R>=1 one valid common entry bound is
\[
 E(R)=G_0/2+
 2C_H R(R+1)c^{-2R-2}\Gamma(2R+2).                         \tag{EF9}
\]
Indeed the remaining integral is bounded by
int_1^infinity u^R exp(-c sqrt u)du
<=2c^(-2R-2)Gamma(2R+2). Stirling gives log E(R)=O_k(R log(R+2)).
These constants are defined, not numerically certified in this packet.

The argument works for complex source forms as well: bar f_i f_j is fixed
with respect to s, and the absolute bound uses C_i C_j. A constant complex
basis change is Hermitian congruence, with no anti-holomorphic change of s.
Alternatively, in a fixed Hecke basis the entries are finite constant linear
combinations of classical completed GL2 x GL2 Rankin--Selberg functions.
That observation is compatible with classical vertical-strip bounds, but it
is not needed as a hidden global growth assumption. Q itself is a determinant
quotient, not a finite linear combination or a new automorphic representation.

## 3. Determinants, Jensen anchors, poles and the strip

At s=2, I(2) and I_W(2) are positive definite by CF3. Hence J(2)=2I(2)
has positive determinants, including det J_W(2)>0. Write U=det J,
V=det J_W. Then exactly
\[
 Q_k(s)=\frac{U(s)}{s(s-1)V(s)}.                           \tag{EF10}
\]
Neither U nor V is identically zero. The determinant bound is
|U(s)|<=d! E(R)^d and |V(s)|<=(d-1)! E(R)^(d-1) on |s|<=R.

For R>=1 Jensen in the disks centered at TWO with radii R+2 and 2(R+2)
gives the explicit bound
\[
 \sum_{|\rho|\le R}|\operatorname{ord}_\rho Q_k|
 \le 2+\frac{\log\!\left(d!(d-1)!\,E(2R+6)^{2d-1}\right)
                  -\log(U(2)V(2))}{\log2}.               \tag{EF11}
\]
If an outer circle meets a zero, take a limiting radius; the displayed
maximum bound remains valid by continuity. The factor two pays s(s-1).
Common determinant zeros cancel and can only reduce this unsigned bound.
No individual additional pole is declared uncancelled.

Products and quotients of entire functions of order at most one have
meromorphic Nevanlinna order at most one. Equation (EF10) proves this for Q.
Since 1/A_k is entire of order at most one, the same holds for mathcal L.
Its unsigned divisor bound follows from (EF11) plus the two gamma ladders,
which contribute O_k(R), and the fixed coordinate shift. This proves (EF2).
There is no assertion about the maximum modulus of a meromorphic function
on circles through poles.

The parent CF8--CF12 gives a normally absolutely convergent generalized
Dirichlet expansion mathcal L(w)=1+sum_(rho>1)a_rho rho^(-w).
Its absolute nonconstant mass tends to zero uniformly as Re w tends to
infinity. Thus mathcal L, and then Q, have no zeros or poles sufficiently
far right. CF3's exact Q(s)=Q(1-s) gives the corresponding left region.
Consequently the NET divisor of Q lies in a finite vertical strip. This
uses both the right expansion and the source reflection, not a zero census.

## 4. The logarithm and the surviving fractional atom

Choose sigma_0 so far right that
Z(sigma_0)=sum_(rho>1)|a_rho|rho^(-sigma_0)<1.
The branch log mathcal L tending to zero at +infinity is given there by
\[
 -\log(1+h)=\sum_{j\ge1}\frac{(-1)^j}{j}h^j,\quad
 h=\mathcal L-1.                                         \tag{EF12}
\]
The absolute coefficient mass is at most -log(1-Z(sigma_0)).
The additive monoid generated by the log frequencies is locally finite:
its generators have a positive minimum and only finitely many lie below
each cutoff; word length below any cutoff is bounded. Regrouping equal
rational products is therefore legitimate. For epsilon>0,
\[
 \sum_\lambda|\lambda b_\lambda|e^{-(\sigma_0+\epsilon)\lambda}
 \le\frac{-\log(1-Z(\sigma_0))}{e\,\epsilon}.                \tag{EF13}
\]
Thus mathcal L'/mathcal L=sum lambda b_lambda exp(-lambda w);
the sign follows by differentiating MINUS log, not log.

The parent's first fractional frequency rho_* has a_*<0:
rho_*=N^2/d, a_*=-c_N^2 b_d(N)^2, except at k=124,248 where
rho_*=N^2/(d-1), with the retained active pivots 169884,142884.
Every smaller source frequency is an integer. Any product of two or more
nonconstant frequencies equal to rho_* would have all factors smaller than
rho_*, and hence be an integer. This is impossible. Therefore
\[
 b_{\log\rho_*}=-a_*>0,\qquad
 \text{its (EF4) mass}=
 (-a_*)\rho_*^{-(k-1)}\log\rho_*.                         \tag{EF14}
\]
At weight 24 this is
88203653222400 (9/2)^(-23) log(9/2), not a mass at log of an integer.
The rational multiplier is exact; logarithms are symbolic, not evaluated
or represented as rational numbers by the replay.

The atomic side is not claimed positive. The first nonconstant coefficient
of mathcal L is positive (CF1/PS14), so its minus-log coefficient is negative,
whereas (EF14) is positive. No positive Laplace or Weil conclusion follows.

## 5. The distributional bridge and completion term

The count (EF2) implies sum_(rho!=0)|nu_rho|/|rho|^2<infinity.
For phi smooth and supported in [a_0,b_0] subset (0,infinity), two integrations
by parts give
\[
 \int e^{\rho t}\phi(t)dt
  =\rho^{-2}\int e^{\rho t}\phi''(t)dt\quad(\rho\ne0).
\]
The divisor is left-located, so the latter integral is bounded uniformly
in rho. This proves absolute convergence of the divisor TEST PAIRING.
The finitely many small/zero rho are handled separately. Neither a
pointwise sum nor positivity of a spectral measure has been proved.

The classical Poisson--Newton formula, with coefficients defined by
MINUS log as in (EF3), now applies to mathcal L: it is nonconstant, has
a half-plane of absolute generalized-Dirichlet convergence, meromorphic
finite order and left-located divisor. In distributions on t>0,
\[
 \sum_{\omega\in\operatorname{div}\mathcal L}
       \operatorname{ord}_\omega\mathcal L\,e^{\omega t}
     =\sum_\lambda \lambda b_\lambda\delta_\lambda .       \tag{EF15}
\]
One can also obtain this from the genus-at-most-one Hadamard products and
the logarithmic derivative: the residual polynomial is constant and its
inverse Laplace transform is supported at zero. Muñoz--Pérez-Marco's
Theorem 3.5 and Corollary 3.6 supply the classical distributional theorem;
we do not claim a new abstract result.

Return to the s coordinate, multiplying (EF15) by exp(-(k-1)t).
The divisor identity from (EF1) adds div A_k, whose gamma poles are
s=-n and s=-(k-1)-n, n>=0, each with multiplicity MINUS one.
The exponential constants in A have no divisor. Consequently their sum is
\[
 W(A_k)(t)=-\sum_{n\ge0}e^{-nt}
           -\sum_{n\ge0}e^{-(k-1+n)t}
         =-\frac{1+e^{-(k-1)t}}{1-e^{-t}},\quad t>0.        \tag{EF16}
\]
Overlapping ladders are counted twice. Addition of signed divisors, including
any cancellation with mathcal L, proves (EF4). This is not a claim that Q
itself has uncancelled gamma poles. In particular its source poles at zero
and one are already included on the left through their net multiplicities.

A compactly supported frequency test sees finitely many logarithmic atoms,
but generally ALL zeros/poles through its exponential transform. A finite
zero census cannot replace that left side without a proved tail estimate.
The formula does not supply such an effective tail, a total charge,
a positive criterion, RH/GRH, or an asymptotic zero distribution.

## 6. Finite controls, source locks and classical inputs

For each authenticated complete parent cutoff C, truncating before taking
-log is valid: every omitted source frequency exceeds C and all other
nonconstant factors exceed one. Terms of logarithmic degree j stop once
rho_min^j>C. The producer computes all products within the cutoff, combines
collisions and verifies exp(-B)=L or F through that entire cutoff.

It also checks -log L-(-log F)=-log zeta(2w-2k+2) independently via ordinary
prime powers with square frequencies p^(2m) and coefficients -p^((2k-2)m)/m.
Tests use a separate additive prime-valuation derivation/recurrence for the
formal logarithm. These are exact finite algebra, not zero computations.
The gamma overlap and endpoint-pole cancellation controls are divisor algebra
only; they do not assign unknown actual determinant zeros.

Arithmetic is MIXED: EXACT_RATIONAL plus CERTIFIED_INTEGER_COVERAGE.
Rational coefficients, frequency products and shifts are exact, with no
rounding; log rho remains a typed symbolic multiplier. Frequency/cutoff input
rationals use at most 32 bits, source/log coefficients and internal rationals
4096 bits, cutoff<=28, support<=512,
log/exp word degree<=16, and a charged work cap of 500000. Limits and theta/
Jensen/Poisson--Newton proofs are not machine-certified by these panels.
Six frozen source objects and all four current note/producer/manifest/test
artifacts are bound by typed identities and LF-normalized hashes. Full
typed fixture reconstruction, duplicate/nonfinite rejection and strict
bool/int separation are acceptance requirements.

Primary inputs inspected, including the relevant displayed PDF formulas:

- [Zagier, Eisenstein series and the Riemann zeta-function](https://people.mpim-bonn.mpg.de/zagier/files/scanned/EisensteinRiemannZeta/eisenstein-zeta-978-3-662-00734-1_10.pdf),
  printed p.277, equations (6)--(7): exactly the theta normalization used
  in (EF5). Cusp decay, the uniform lattice bound and determinant/count
  deductions are written above.
- [Muñoz--Pérez-Marco, Poisson-Newton formulas and Dirichlet series,
  arXiv:1301.6511v2](https://arxiv.org/pdf/1301.6511v2),
  section 2, section 3 equation (6), Theorem 3.5/Corollary 3.6:
  finite-order meromorphic generalized series, signed multiplicities,
  minus-log sign and distributions away from the origin.
- [Cogdell--Piatetski-Shapiro, Remarks on Rankin--Selberg convolutions](https://people.math.osu.edu/cogdell.1/rorsc-www.pdf),
  Theorem 2.3: compatible classical continuation/vertical-strip context,
  not a substitute for the direct bound (EF7)--(EF9).

Remote PDF bytes are not claimed authenticated by the offline replay.
There is no assertion of a new abstract explicit formula, new automorphic
representation, exhaustive novelty, or RH positivity.
