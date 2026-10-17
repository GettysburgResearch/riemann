# Higher numerator moments on the actual sixth-free family

Status: PROPOSED source-qualified component proof. Independent mathematical
review is required. The fixed-order large sieve and complete approximate
functional equation below are imported analytic inputs. This is NOT a bound
for reciprocal L-functions or for the native inverse-Mobius moments.

## 1. Exact input and indexing

Fix the field F, S, deep ray modulus and finite list of S-unit twists in
#965, commit d58e3282a9379b6ae165681bc2e21e4f9fd18c26. That source identifies
CT's Poisson characters with psi chi_a, where a ranges over SIXTH-POWER-FREE
exterior ideals, ordered by their FULL norm. At each good prime, a positive
exponent 1,...,5 gives the prescribed nonprincipal local residue character.
Original character values are zero at nonunits. The fixed twist psi is
unitary of finite order. Angular theta characters are not included here.

The load-bearing DF sieve contract, at this exact indexing, is

 sum_{Na<=U}^{6-free} |sum_{Nc<=V}^{6-free} z_c chi_a(c)|^2
  <<_eta (UV)^eta [U+V+U^(5/6)V^(1/3)+U^(1/3)V^(5/6)] sum_c |z_c|^2. (S6)

This is de Faveri's Theorem 1.1 as specified in #965 SOURCES and the detector
formula in PROOF (27). The same finite ray-class decomposition and generator
choices are retained. A fixed psi multiplies the column coefficients, not the
row counting measure. Permitted row subsets can be retained by positivity.
A merely squarefree-indexed sieve is NOT enough for the present proof.

We also import the standard complete AFE for these finite-order Hecke
L-functions, including its dual, root numbers, original finite Euler omissions,
and rapid Mellin-weight decay. The conductor is <=C Na. The finitely many
archimedean types and S data are fixed. In particular, for Na~U and height t,
its two Dirichlet polynomials can be cut at

 L=U^(1/2+delta)(2+|t|)^C_F

with an arbitrarily small inverse power of U error and a fixed polynomial
height factor; delta>0 is chosen after the desired final norm loss. An AFE
cutoff of exactly sqrt(U) with its infinite tail deleted is not used.

The underlying primitive character agrees with the exterior character away
from S. A sixth-free exterior prime has nontrivial local exponent, so it is
not a neutral sixth-power omission of a primitive conductor. Extra factors
at S have fixed size and are handled before the argument by their finite
Euler polynomials. There are only finitely many resulting test families.

## 2. The moment bound

For every fixed integer r>=1 and every eta>0,

 sum_{Na<=U}^{6-free} |L_F^S(1/2+it,psi chi_a)|^(2r)
  <<_{F,S,psi,r,eta} U^(kappa_r+eta) (2+|t|)^C_{F,S,r},          (1)

where the height exponent can be fixed for 0<eta<=1, and

 kappa_r=max(1,r/2,5/6+r/6,1/3+5r/12).                          (2)

Thus kappa_1=1, kappa_2=7/6, kappa_3=19/12, and kappa_r=r/2
for r>=4. The numerical application needs r=2, namely the fourth moment
U^(7/6+eta). No uniformity in an unbounded moment order is asserted.

### 2.1 AFE and conductor separation

It suffices to treat one dyadic row range. The principal u=1 and any finitely
many bounded indices are handled separately by fixed-function polynomial
height bounds, so their AFE polar terms are not silently omitted. For the
nonprincipal ranges write the AFE as A_a+epsilon_a B_a
with |epsilon_a|=1, after the fixed local factors. The inequality
|A+epsilon B|^(2r)<=2^(2r-1)(|A|^(2r)+|B|^(2r)) keeps both parts.
Its truncation error is harmless using elementary polynomial bounds and
choosing the fixed tail order large enough in terms of r.

Separate each AFE weight by its Mellin integral on a small positive real
line. A conductor factor has the form Q_a^(s/2); its imaginary part is a row
phase, and its absolute value is bounded by U^delta times a fixed height
factor. The gamma/Mellin weights have integrable decay, with a seminorm
polynomial in 2+|t|. Minkowski is applied outside the row L2 norm. Taking r
copies only changes the fixed seminorm and the arbitrarily small norm loss.

Consequently the r-th power of either AFE piece reduces to polynomials

 P_a = sum_{Nn<=L^r} b_n chi_a(n),
 |b_n| <= C (Nn)^(-1/2) d_r(n) U^delta (2+|t|)^C,             (3)

with row-INDEPENDENT b_n at each fixed Mellin parameter. The finitely many
fixed twists and unitary n^(-it) factors remain in b_n. No root number is
moved inside a column in a row-dependent way. The complete divisor profile
d_r bounds the actual ordered factorization sum; it is not substituted for
its signed or complex values in the sieve itself. The dual AFE is treated
with conjugate characters, to which the same sieve applies.

One can first truncate the Mellin integrals, apply the stated bounds, and
then pass to their absolutely integrable tails. Height exponents are bounded
on the real Mellin strips 0<delta<=1; constants may depend on delta. This
makes C_{F,S,r} independent of the later arbitrarily small norm loss. This
point is necessary when zero-free rectangles are fixed before those losses.

### 2.2 The exact sixth-power removal, including masks

Write uniquely n=c d^6, where c is sixth-power-free. NO coprimality condition
between c and d is imposed. Complete multiplicativity with zero values gives

 chi_a(c d^6)=chi_a(c) 1_{(a,d)=1}.                           (4)

For example, a prime exponent 7 belongs to BOTH c and d; deleting this case
would change the AFE. If a prime dividing d divides a, the entire term is
zero even when the exponent of that prime in c is zero.

For fixed d, use the row subset (a,d)=1 and apply (S6) at
V=L^r/(Nd)^6, omitting d for which V<1. The original coefficients b_cd^6
obey, after rescaling delta,

 sum_{Nc<=V}^{6-free} |b_{c d^6}|^2
  << U^eta (2+|t|)^C (Nd)^(-6+eta).                          (5)

Indeed d_r(c d^6)<<_{r,epsilon}(Nc (Nd)^6)^epsilon, and
sum_{Nc<=V}1/Nc<<_F log(2V), by fixed-field ideal counting.
This bound is uniform in the actual coefficient phases and the moving d.
It does not replace (4) by unmasked character periodicity.

Let K(U,V) denote the bracket in (S6). It is increasing in V. Minkowski
across d, followed by (5), now gives

 ||P_a||_{ell2(a)}
  << U^eta (2+|t|)^C K(U,L^r)^(1/2)
       sum_d (Nd)^(-3+eta)
  << U^eta (2+|t|)^C K(U,L^r)^(1/2).                         (6)

The last sum converges for sufficiently small eta. It includes ideals with
prime factors shared with c. Fixed exterior restrictions can only reduce
this positive summation. In particular the AFE's nonsquarefree columns are
NOT discarded, and the number of powerful rows is NOT paid separately.
The sixth-free ROW sieve is essential to avoid that extra loss.

Since L^r<=U^(r/2+small loss)(2+|t|)^C, the four terms of K give precisely
(2) after squaring (6). Integrate the Mellin parameters, add both AFE pieces,
and sum dyadic row ranges. This proves (1) from the declared inputs.

## 3. A bound on any zero-selected subset

If C(U) is ANY subset of the actual rows a~U, including their finite S-unit
labels, with #C(U)<<U^nu, Holder gives

 sum_{a in C(U)} |L_F^S(1/2+it,psi chi_a)|
  << U^((1-1/(2r))*nu+kappa_r/(2r)+eta)(2+|t|)^C.             (7)

The subset may depend on the zeros of a denominator L-function. In using
(7), take the reciprocal and correction-factor suprema BEFORE Holder.
There is no independence assumption and no moment of inverse L-values.

At r=2 the exponent is

                 3nu/4+7/24.                               (8)

The second-moment exponent was (nu+1)/2. Equation (8) is strictly smaller
for nu<5/6. At nu=2/3 it saves exactly 1/24 in the exponent of U. It is
worse at nu=1, so the complete good class must retain its second-moment
estimate. Replacing every class indiscriminately by (8) is invalid.

For completeness, the best displayed Holder envelope over all r>=1 is

 min((nu+1)/2, 3nu/4+7/24, 7nu/8+1/4), 0<=nu<=1.            (9)

The r=3 line lies between r=2 and r=4; their common crossing is nu=1/3.
For r>=4, increasing r only increases (1-1/(2r))*nu+1/4.
These are statements about this sufficient envelope, not optimal lower
bounds for actual numerator means.

## 4. Credit and limits

Using an AFE, powering a Dirichlet polynomial, removing fixed-order powers,
and applying a large sieve are classical methods. No global priority claim
is made for (1). The claimed repository contribution is the explicit
all-sixth-free, zero-mask-preserving numerator adapter and its use to move
the actual CT detector beyond #965's 91/100 proposal.

The moment in (1) concerns L in the NUMERATOR of that detector. It is not
sum_u |sum mu_F(n) chi_n(u) W(Nn/D)|^(2r). The latter inverse-polynomial
moment, its 17/24 target, and the full RH programme remain open.

The most important independent review is to verify that the cited DF
Theorem really supplies (S6) on BOTH sixth-free indices for these generator
choices, and then review the complete AFE separation and (4)--(6). If any
of these contracts fails, the proposed zero-free composition fails as well.
