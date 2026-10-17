# Full angular--Mellin energy: square-root windows and quantitative orthogonality

Status: PROPOSED unconditional mathematics, with complete proofs below. No
independent mathematical review or formal verification. This is a theorem
about a full family average, NOT a bound for its principal member or RH.
The large-sieve/spacing method is classical; no global priority is claimed.

The new comparison is with #953's selected divisibility sector and #954's
Mellin-only average. We average a different, two-parameter Hecke family.
Both window widths can be of square-root scale, but their total parameter
volume is still linear in the coefficient length. This cost is not hidden.

## 1. Fields, characters, and unchanged coefficient arrays

Let K be a FIXED imaginary quadratic field, w_K its number of roots of unity,
h_K its class number, and I its group of nonzero fractional ideals. There is
a unitary ideal character Xi extending

    Xi((alpha)) = (alpha/|alpha|)^w_K.                       (1)

This is well-defined on principal ideals. For completeness an extension
exists without a class-field hypothesis: if a character is defined on a
subgroup H containing the principal ideals and an ideal a has order j in
I/H, choose a j-th root z of the character of a^j in the unit circle. Set
Xi(ha^i)=Xi(h)z^i. The definition is consistent, and finitely many repetitions
exhaust I since I/P is finite. Fix one such extension. Its ambiguity is a
class-group character. For K=Q(omega), w_K=6 and Xi((alpha))=alpha^6/N(alpha)^3.
Thus distinct conjugate ideals of equal norm are NOT identified.

Let psi run over ALL characters of the ordinary ideal class group, with
uniform probability 1/h_K. For l in Z and t in R set

    eta_(psi,l,t)(n) = psi([n]) Xi(n)^l (Nn)^(it).            (2)

These are actual multiplicative unitary twists. No independent prime signs
are introduced. The class average is essential in the nonprincipal-class
case and is vacuous in the Eisenstein field.

Fix a nonnegative finite measure nu on an auxiliary row space, of mass Z.
Keep it fixed at every scale. For each row u let a_n(u) be any measurable
complex coefficient array satisfying, uniformly in u,

    sum_(Nn<=Y) |a_n(u)|^2 <= A Y,       Y>=1.               (3)

We assume A>0; the zero array is trivial. All exclusions and nonunit zeros
stay in the array. The constants below depend on K and the stated Gaussian
parameter, not on the row, exclusions, centers, or coefficients except A.

The native coefficients mu_K(n) times any completely multiplicative phases
of modulus <=1 satisfy (3). So do, UNIFORMLY in every integer m>=2, the coupled
coefficients from #949--#953 with local polynomial

    1-(1-1/q)a_p(u)x-b_p(u)q^(m/2-1)x^m,  q=Np,           (4)

where |a_p|,|b_p|<=1 and both are zero at a masked prime. A supported ideal is
uniquely n=r d^m with r,d squarefree and coprime, and its squared coefficient
is at most (Nd)^(m-2). If I_K(Y)<=A_KY, summing over d gives (3) with
A=A_K zeta_K(2). This is the coefficient count already proved in #952.
The parameter m is algebraic, not a claim to construct new metaplectic covers.

Fix c real, with c=5/6 in the Dedekind application, and use the FULL test

    W_c(y)=y^(-c) exp(-(log y)^2/4)/(2 sqrt(pi)).

Write B_(psi,l,t)(X,u)=sum_n a_n(u)eta_(psi,l,t)(n)W_c(Nn/X), and

    E_(psi,l,t)(D) = integral_0^D integral |B(X,u)|^2 dnu(u) dX/X^2.

Absolute convergence and all exchanges used below follow from (3):
Cauchy and ideal counting give sum_(Nn<=Y)|a_n(u)|<=C_K sqrt(A)Y,
and Gaussian partial summation gives sum_n|a_n|W_c(Nn/X)<=C_(K,c)sqrt(A)X.
This squared bound is integrable against dX/X^2 on (0,D). Also
|a_n|<=sqrt(A Nn), which gives arbitrarily rapid flatness at X=0.

For R>=1 define normalized probabilities

    gamma_R(t-t0)=exp(-(t-t0)^2/(2R^2))/(sqrt(2pi)R),
    p_R(l-l0)=exp(-(l-l0)^2/(2R^2))/Z_R,
    Z_R=sum_(j in Z) exp(-j^2/(2R^2)),

where t0 is any real number and l0 any integer. Denote the combined class,
integer-angular, and continuous-Mellin average by < . >_R.

## 2. The full second-energy theorem

Let beta=2c-1, kappa_c=exp(beta^2/2)/(2sqrt(2pi)), and Phi the standard normal
CDF. The exact kernel inherited from #952 is

    K_D(v,z)=kappa_c/sqrt(vz) exp(-log(v/z)^2/8)
                       Phi(log D-(log v+log z)/2-beta).     (5)

Define the IDENTICAL-IDEAL diagonal, with all original row masks,

    Delta(D)=sum_n K_D(Nn,Nn) integral |a_n(u)|^2 dnu(u).

### Theorem 1 (all unequal ideals, not a selected sector)

For every D>=2 and R>=1, uniformly in both centers,

    | < E(D) >_R - Delta(D) | <= C_(K,c) A Z D/R^2,        (6)
    0 <= Delta(D) <= C_(K,c) A Z log(3D).                  (7)

In fact the ABSOLUTE coefficient-pair sum after multiplication by the exact
nonnegative averaging kernels obeys the right side of (6). Thus the theorem
pays all incomparable pairs and distinct equal-norm ideals as well.
At R=sqrt(D), the full mean is Delta(D)+O(AZ), hence O(AZ log D).
It is an average over approximately R angular indices and a Mellin interval
of length R, NOT an O(sqrt(D))-sized one-parameter family.

### Proof: exact character averaging

Class orthogonality retains only [n]=[j]. Gaussian Fourier transformation and
Poisson summation on Z give, after factoring out center phases of modulus one,

    F_R(n,j)=1_([n]=[j]) exp(-R^2 log(Nn/Nj)^2/2)
                              Theta_R(arg(Xi(n)/Xi(j))),
    Theta_R(theta)=
      sum_(v in Z)exp(-R^2(theta-2pi v)^2/2)
          / sum_(v in Z)exp(-2pi^2 R^2 v^2).              (8)

The denominator is >=1. Uniformly for R>=1,

    0<Theta_R(theta)<=C exp(-c0 R^2 dist(theta,2pi Z)^2),
    Theta_R(0)=1.                                        (9)

For (9), reduce theta to [-pi,pi]. The nearest Gaussian has the stated bound;
the other terms are a uniformly convergent Gaussian tail. Splitting the
exponent in half and using |theta-2pi v|>=pi(2|v|-1) proves a bound with an
absolute c0>0, including the ties at pi. This derivation keeps the wraparound;
replacing Theta_R by a nonperiodic Gaussian is not an exact identity.

### Lemma 2 (off-diagonal lattice spacing, with no additive constant)

There are C_K,c_K>0 such that for EVERY integral ideal n,

    sum_(j!=n) F_R(n,j)
       <= C_K (Nn)/R^2 exp(-c_K R^2/(Nn)).                (10)

Here F_R denotes the nonnegative kernel (8), without center phases.

Proof. Choose a fixed integral ideal a_C in each ideal class. Ideals n in C
have the form (alpha)a_C, with alpha in the fixed lattice a_C^(-1), modulo
units. After scaling that lattice by sqrt(Na_C), write z_n for a generator
point with |z_n|^2=Nn. There are finitely many resulting lattices. Each has
fixed positive minimum separation and bounded disk counts. If n,j are in
the same class, Xi(n)/Xi(j)=(alpha_n/|alpha_n|)^w_K times the conjugate of
the analogous phase for j. The angular distance in (9) is w_K times the
smallest angle theta between z_n and any unit multiple of z_j.

Put v=Nn. When v/2<=Nj<=2v, elementary polar geometry on this compact radial
range gives

    min_epsilon |z_n-epsilon z_j|^2
       <= C_K v [log(Nj/v)^2+theta^2].

For example use |sqrt(Nj/v)-1|<=C|log(Nj/v)| and
1-cos(theta)<=theta^2/2. Hence (8)--(9) are bounded by a fixed finite sum of
exp(-c R^2|z_n-epsilon z_j|^2/v). A distinct ideal cannot produce zero distance.
All differences belong to the same fixed lattice. Its off-origin Gaussian
sum obeys, for every t>0,

    sum_(h!=0)exp(-t|h|^2)<=C_K t^(-1)exp(-c_K t).

For t<=1 use annular lattice counting and a planar Gaussian integral; for
t>=1 extract half the minimum-distance exponent, bound the remaining sum
at t=1, and absorb the extra factor t into a smaller exponential. This proves
(10) for comparable norms.

For Nj<v/2 there are O_K(v) ideals, and the radial factor is at most
exp(-R^2(log 2)^2/2). For 2^h v<Nj<=2^(h+1)v, h>=1, there are O_K(2^h v)
ideals and the factor is at most exp(-R^2 h^2(log 2)^2/2). The sum of these
bounds is O_K(v R^(-2)exp(-c R^2)). Since v>=1, it is bounded by the right
side of (10), after reducing c_K. This covers all remaining ideals. QED.

### Completion of Theorem 1

The kernel (5) is a Gram kernel, so K_D(v,z)<=sqrt(K_D(v,v)K_D(z,z)). Set
x_n=|a_n(u)|sqrt(K_D(Nn,Nn)). Symmetry of F_R and 2x_n x_j<=x_n^2+x_j^2 give

    sum_(n!=j)|a_n a_j|K_D(Nn,Nj)F_R(n,j)
       <= sum_n |a_n|^2 K_D(Nn,Nn) sum_(j!=n)F_R(n,j)
       <= C_K/R^2 sum_n |a_n|^2 (Nn)K_D(Nn,Nn).           (11)

By (3) and Stieltjes partial summation the last sum is at most C_(K,c) A D.
Explicitly the decreasing function f(y)=Phi(log D-log y-beta) satisfies

    integral_0^infinity f(y)dy = D exp(-beta+1/2).

Integration against the prefix in (3) gives the claim, and integration over
nu proves (6). The same argument with y^(-1)f(y), integrated only for y>=1,
gives (7). Finite truncations prove the inequalities first; absolute Fubini
justified in Section 1 passes them to the whole Gaussian source. QED.

## 3. Nearly minimal windows with an arbitrarily small power error

### Theorem 3

Fix the SINGLE width function

    R_*(D)=sqrt(D) exp((log(3D))^(3/4)),   D>=2.           (12)

For every B0>0,

    <E(D)>_(R_*(D)) = Delta(D)+O_(K,c,B0)(A Z D^(-B0)).   (13)

Thus each width is D^(1/2+o(1)) and the spectral area is D^(1+o(1)).
This is not a bound with area D^o(1).

Proof. Put V=(log(3D))^(3/4) and Y=D exp(V). Retain every ideal through Y,
not just a prime semigroup or one ideal per norm. From |a_n|<=sqrt(A Nn)
and Gaussian completion, the norm of the omitted source in the critical
energy space is

    <= C_(K,c) sqrt(AZ) D^(3/2)exp(-V^2/8).               (14)

One may use W_c(e^z)<=C_c exp(-z^2/8)e^(-2z) and sum_n(Nn)^(-3/2)<infinity.
The full energy is O(AZD). Therefore the difference of squared energies is
at most r(2sqrt(CAZD)+r), with r the right side of (14). This controls the
omitted cross terms. It is O_(K,c,B0)(AZD^(-B0)) for every B0, since V^2 grows
faster than log D. The same bound controls the omitted diagonal, for instance
by the squared positive absolute tail majorant. The argument is uniform in
the twists and hence also after their normalized average.

For the retained finite polynomial, keep the exponential in (10). Its full
off-diagonal is at most

    C_(K,c) A Z log(3D) (Y/R_*^2) exp(-c_K R_*^2/Y).

Here R_*^2/Y=exp(V). This is smaller than every fixed power of D^-1.
Together with the two tail estimates it proves (13). QED.

## 4. An asymptotic for the FULL averaged coupled source

This section specializes to K=Q(omega), fixed S containing the primes over
2,3, scalar row, fixed m>=3, and |a_p|=|b_p|=1 at every remaining prime.
The squared coefficients are independent of their phases. Their Dirichlet
series from #953 Section 4 is

    D_m(s)=zeta_S(s)zeta_S(ms-m+2)H_m(s),
    H_m(s)=product_(p notin S)(1-q^-s)(1-q^(m-2-ms))
                                [1+(1-1/q)^2q^-s+q^(m-2-ms)].

We restate the precise deduction used here. H_m converges normally for
Re(s)>1-3/(2m). On that domain D_m has exactly two poles, at 1 and alpha=1-1/m,
with residues delta_S>0 and r_m<0. If b_m is its finite Laurent coefficient
at 1, Gaussian CDF inversion and a contour shift give

    Delta(D)=kappa_c[delta_S log D+b_m-beta delta_S
         -m r_m exp(beta/m+1/(2m^2))D^(-1/m)]
         +O_(m,S,c,epsilon)(D^(-3/(2m)+epsilon)),          (15)

for 0<epsilon<1/(2m). These exact diagonal constants and its two-pole proof
are credited to #953, not claimed anew. No inverse-zeta zero-free hypothesis
is used in that shift. The positive zeta factors have their ordinary poles;
for this field zeta_K(t)=zeta(t)L(t,chi_-3)<0 on 0<t<1 by the alternating
and paired series, which gives r_m<0.

Combining (13) with (15) is a NEW FULL-AVERAGE consequence:

    <E_m(D)>_(R_*)=L_S log D+C_(m,S,c)+J_(m,S,c)D^(-1/m)
                  +O(D^(-3/(2m)+epsilon)),              (16)
    L_S=kappa_c delta_S>0,  J_(m,S,c)>0.

In particular m=6,c=5/6 gives a nonzero POSITIVE D^(-1/6) secondary term and
error O(D^(-1/4+epsilon)) for the entire averaged energy. This contrasts with
#953's NEGATIVE prime-quotient secondary term, which is a different subtotal.
The new conclusion is transfer of the diagonal expansion to the full mean,
not a new computation of the previously known residues.
At the simpler width R=sqrt(D), (6) already gives L_S log D+O(1).

## 5. Scope, what was paid, and what was not

The large comparable-core pairs and conjugate equal-norm pairs are included
in (6); none is removed by an arithmetic selector. Orthogonality is supplied
by TWO genuine global characters and (when needed) a finite class average.
No independent-prime physical model is substituted. All masks are unchanged.

Theorems 1 and 3 apply to arbitrary coefficients satisfying (3), so they
cannot supply special Mobius cancellation at the fixed twist. The principal
member psi=1,l=0,t=0 is NOT bounded by its normalized average at constant
cost. Its angular probability is of order 1/R and the Mellin averaging
window has length R. The full all-row near-linear-height native hierarchy,
without these extra averages, is still open here. No zero-free exponent is
improved, and finite-order Hecke zero-free claims are not used for Xi.

The main method belongs to classical multidimensional large-sieve and Hecke
mean-value theory (Huxley and predecessors). The contribution recorded here
is the full untruncated source-specific energy statement, its uniform m/mask
scope, the sharp ideal-diagonal comparison, and the explicit all-power error
window, relative to the inspected repository packets. Establishing worldwide
priority would require a fuller literature review than performed here.

## 6. A sharpness check for the averaging-area cost

The D/R^2 term cannot uniformly be removed from Theorem 1's coefficient
class. Take the native permitted phase profile a_p=-1 and no exclusions,
so a_n=mu_K(n)^2 is nonnegative (this is NOT the original Mobius source).
Then, for centered t0=l0=0 and every R>=1,

    <E(D)>_R >= c_(K,c) D/R^2,  D sufficiently large.      (24)

Here is an elementary proof. Counting lattice points in each fixed ideal
class gives I_K(X)=kappa_K X+O_K(sqrt(X)). The identity
mu_K(n)^2=sum_(d^2|n)mu_K(d) therefore yields

    sum_(Nn<=X)mu_K(n)^2
       =(kappa_K/zeta_K(2))X+O_K(sqrt(X)log(3X)).

The tail of the absolutely convergent main term costs O(sqrt(X)); the
lattice errors cost sqrt(X)sum_(Nd<=sqrt(X))1/Nd. Gaussian partial summation
now gives B_(1,0,0)(X)=c1 X+o(X), c1>0, while
sum_n mu_K(n)^2 W_c(Nn/X)|log(Nn/X)|<=C_(K,c)X.
For a fixed sufficiently small delta>0 this implies
|B_(1,0,t)(X)|>=c2 X whenever |t|<=delta and X is sufficiently large, after
removing the unit-modulus factor X^(it). Retain only the principal class
character, l=0, this fixed interval in t, and X in [D/2,D] in the nonnegative
mean. Their probabilities are respectively 1/h_K, at least c/R, and at least
c_delta/R. The scale integral is at least cD, proving (24).

Thus widths R=D^gamma with gamma<1/2 cannot give a uniformly subpower mean
for all allowed phases. This diagnoses the cost of the positive/spacing
argument, not an obstruction to a source-specific Mobius estimate at t=l=0.
