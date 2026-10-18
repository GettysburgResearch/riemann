# The exact all-moment target that reaches one half

Status: PROPOSED complete elementary sufficiency and estimate-model calculations.
The needed arithmetic upper bound is OPEN. This file neither proves RH nor
announces another numerical zero-free boundary. Its purpose is to distinguish a
cofinal native moment theorem from all-order numerator or averaged theorems.

## 1. A sublinear excess suffices; uniform constants in the order do not

Fix a number field F, fixed exterior primes S, and a real c. Use the SAME
principal native Gaussian source

 S_F(X)=sum_(I outside S) mu_F(I) W_c(NI/X),
 W_c(y)=y^(-c)exp[-(log y)^2/4]/(2sqrt(pi)).             (1)

Suppose a family moment M_(2k)(X,H) contains this principal row with weight
at least one. No other row is needed for the following implication. Assume
there is a sequence of FIXED orders k_j tending to infinity, row exponents
h_j>=0, and excesses e_j>=0 such that, for every eta>0,

 M_(2k_j)(X,X^h_j) <<_(j,eta) X^(h_j+k_j+e_j+eta),    (2)
 liminf_j (h_j+e_j)/k_j=0.                            (3)

The definitions and S,c must be consistent across j; an arbitrary different
principal source or excluded set at each order is not licensed by this statement.
Constants and starting scales may depend arbitrarily on j. The row height is
also allowed to be at least two or enlarged by a fixed factor when h_j=0.

**Theorem.** Conditions (2)--(3) imply that every nontrivial zero of zeta_F
lies on Re(s)=1/2. In particular fixed h and any bounded excess e_j<=C suffice;
more generally e_j=o(k_j) suffices with h_j=o(k_j).

**Proof.** Nonnegativity of the complete row sum, not a cancellation or
independence assertion, gives

 |S_F(X)|^(2k_j) <= M_(2k_j)(X,X^h_j).

Given delta>0, choose ONE j for which (h_j+e_j)/(2k_j)<delta/2, then one
fixed eta>0 with eta/(2k_j)<delta/2. Take the 2k_j-th root of (2), keeping
its constant. This proves |S_F(X)|<<_delta X^(1/2+delta). Extend its constant
over the finite initial interval, using absolute convergence of (1).
There is no limit interchange involving k and X, and no uniform-in-k estimate.

For Re(s)>1, absolute Fubini and y=NI/X give

 integral_0^infinity S_F(X) X^(-s) dX/X
    = exp[(s-c)^2]/zeta_F^S(s).                       (4)

Indeed integral_0^infinity W_c(y)y^s dy/y=exp[(s-c)^2], by completing the
square in log y. Ideal counting proves absolute convergence. At X tending
to zero the original sum is flat: for every B>1, |S_F(X)|<=C_B X^B, using
W_c(NI/X)<=C_B(X/NI)^B. At infinity the just-proved growth bound, with delta
chosen below Re(s)-1/2, proves locally uniform absolute convergence of the
left side of (4) throughout Re(s)>1/2. It is holomorphic there, with all
logarithmic derivatives justified by the same margins.

The right side continues meromorphically by the known continuation of
zeta_F. The identity theorem and the NONZERO entire Gaussian transform show
that zeta_F^S has no zeros there. Its pole at one gives a zero, not a pole,
of the reciprocal. Removed Euler factors have zeros only at Re(s)=0, so the
same right-half nonvanishing holds for zeta_F. Its functional equation and
complex conjugation reflect nontrivial zeros across Re(s)=1/2, proving the
claim. No simplicity assumption is used. QED.

For F=Q(omega), zeta_F=zeta L(s,chi_-3), and both factors are holomorphic
away from their stated pole at one. A zero of ordinary zeta in the right
critical half-strip would therefore be a zero of zeta_F. Thus this one
fixed field would already suffice for ordinary RH. This is not a claim
that a family of finite-order numerator moments supplies (2).

The useful quantitative target can be written plainly as

  M_(2k)(X,X^h) <<_(k,eta) X^(h+k+C+eta)
       for an UNBOUNDED sequence of fixed k,             (OPEN-C)

where C and h are fixed. Perfect diagonal order is stronger than necessary.
The present native theorem instead has e_k(h)~k. It does not prove OPEN-C.

## 2. Exact product vectors: where native signs have to be used

For nonnegative W and native v(I)=mu_F(I), define the complete capped
product coefficient c_(k,X)(J) as in NATIVE_ALL_MOMENTS. Write Omega_F(J)
for the number of its prime-ideal factors with multiplicity. Every nonzero
summand in that coefficient has exactly the same sign. Thus EXACTLY

 c_(k,X)(J)=(-1)^Omega_F(J) b_(k,X)(J),  b_(k,X)(J)>=0. (5)

This follows because all I_j must be squarefree and their total number of
prime factors is Omega_F(J). No cancellation has been gained by convolving
inside a single product ideal. Equal rational norms need not be identified
for (5); it is an ideal identity over any fixed field.

Let G_H(J,L)=sum_(Nm<=H) chi_hat_m(J) conjugate(chi_hat_m(L)). Then the
COMPLETE native moment is the finite quadratic form

 M_(2k)=sum_(J,L) (-1)^(Omega_F(J)+Omega_F(L))
                   b_(k,X)(J)b_(k,X)(L) G_H(J,L).     (6)

All pairs remain. This exact representation suggests a source-specific
restricted quadratic-form estimate, rather than another coefficient-uniform
large sieve. For the HARD PREFIX test W=1_(0,1], a sufficient (not proved)
strengthening, uniformly in EVERY X,H>=2 at each fixed order, is

 |sum_J c_(k,X)(J)chi_hat_m(J)|^2 summed over m
       <<_(k,eta) H X^(C+eta) sum_J |c_(k,X)(J)|^2,   (OPEN-R)

with fixed C>=0 along unbounded fixed k. The elementary divisor bound gives
sum_J |c_(k,X)(J)|^2<<_(k,eta) X^(k+eta). Thus the hard-prefix moment would
be << H X^(k+C+2eta), with the SAME H valid at every shorter or longer scale.

Here is the required Gaussian transfer rather than a silent test substitution.
At fixed X,H, absolute ideal counting and Gaussian decay justify

 A_m,Gaussian(X)=-integral_0^infinity A_m,prefix(tX) W_c'(t) dt.

Minkowski in the full row l_(2k) norm applies at that SAME H. The prefix bound
gives a factor t^((k+C+2eta)/(2k)); its integral against |W_c'(t)| is finite,
as are all fixed-power derivative moments of this logarithmic Gaussian.
Prefix scales below one vanish; scales between one and two have a uniform O(H)
moment and are covered by enlarging the constant. Consequently the Gaussian
moment has the same power H X^(k+C+2eta). Set H=X^h and rename eta to obtain
OPEN-C. A prefix estimate known ONLY on H=X^h would not, by itself, justify
this same-height argument; the all-H coverage in OPEN-R is an explicit obligation.

A common unrestricted positive coefficient array does not satisfy a bound
of this strength: its principal row alone can have size X^(2k).

OPEN-R is stated as a sufficient signed estimate on the ACTUAL capped
Möbius product vectors. It is not claimed weaker than RH in any logical
sense, nor proved by Gram positivity. It displays the precise point at which
the DF operator estimate used in the native theorem loses the source signs.

## 3. Why the positive numerator/residue architecture does not go to one half

This paragraph concerns ONLY the following specified upper-estimate model:
symmetric short scales X=Y=Z^a, 0<a<=1/2, the same w=1,z=1/6 principal
residue, the two-term reflected bound, and the full good Poisson class
bounded by numerator moments plus a reciprocal supremum. It is not a lower
bound for the true arithmetic average and not a no-go theorem for RH.

The model's theta growth exponent is a/2, and the true principal Mellin
shift is b(a)=5/6-a/3. Even after the recovered correction-domain extension,
the full good class uses x=Re(xi)>1/2 and x+y>1, y=Re(w)>0. At its top
frequency U=Z^(1-a), the physical exponent is

 E=x-1+a(y-1/2)+(1-a)m(y),                            (7)

where m(y) is the first-numerator-mean exponent on a full U-member family.
The second-mean bounds used in the repository give m(y)=1 for y>=1/2 and
m(y)=3/2-y for y<=1/2 (away from endpoint poles), up to arbitrary losses.
ALL_NUMERATOR_MOMENTS adds no better full-family exponent: (3) there always
has K>=1+r(1-2y)_+, so Holder gives at least these same model costs.
For y>1, the absolutely convergent numerator also has m(y)=1 and cannot
improve the following minimization.

If y>=1/2, use x>1/2 in (7) to get E>=1/2-a. If 0<y<=1/2, use x>1-y and
m(y)>=3/2-y; subtraction of 1/2-a gives (1-a)(1-2y)>=0. Therefore

 b(a)+max(a/2,E) >= b(a)+max(a/2,1/2-a) >= 8/9.       (8)

For a>=1/3, the last quantity is at least 5/6+a/6>=8/9. For a<=1/3 it is
at least 4/3-4a/3>=8/9. No endpoint is asserted attainable. Exceptional
classes and tails can only worsen this particular set of bounds.

Equation (8) DOES NOT establish a zero-free region with boundary 8/9. It
says that supplying arbitrarily many of THESE numerator moments does not
make the already chosen positive/residue estimate converge to 1/2. This
calculation is intentionally kept separate from the successful all-order
inequalities and from any claim about a different physical projection.

## 4. A distinct critical target already present in the latest work

The live-read #974 component DIAGONAL_FINITE_PART.md, frozen at
89c37b6707cb77fc5a86143ea98d8756759fdcbc, does change the projection. At
z=1/2 and transverse coordinate v=xi+w-1 it proves that the bare normal
residue is explicit and cancels the target zeros, while the normalized
FIRST FINITE PART is - (zeta_F^S)'/zeta_F^S. Its pole at a target zero has
residue minus the multiplicity. The physical monomial is exactly

  Z^(-1/2)(Z/Y)^xi Y^v.

The extra log Y from the finite part multiplies a known residue and is
removable. The full physical finite-part projection and all tails remain
unestimated. This theorem is CREDITED TO #974, not rediscovered or proved
by the present numerical checks. The #962 free-z source supplies a second
existing critical-scale alternative with an invertible harmless numerator.

These suggest the substantive continuation: prove a native signed estimate
such as OPEN-R/OPEN-C, or estimate that full first finite part before a
positive norm-product loss. The all-order calculation above clarifies why
another numerator exponent optimization, without this change, is inadequate.
No such remaining arithmetic estimate is claimed established in this packet.
