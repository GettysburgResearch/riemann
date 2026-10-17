# A self-restricted zero detector: exponent 5/7 at three quarters

Status: PROPOSED source-qualified component proof. Independent mathematical
review required. No CT theta theorem, quasi-RH statement, RH/GRH, or native
critical moment is a premise of this document. The deep input is DF's actual
sixth-order sieve, together with classical Hecke analytic theory.

The shifted Mellin detector overlaps #971's SHIFTED_DETECTOR.md and is credited.
The new ingredient is applying the hereditary moment bounds to BOTH the
numerator and mollifier on the exceptional set itself, before eliminating its
unknown cardinality. Moving the line alone is not claimed new.

## 1. Retain one zero per exceptional character

Keep the full sixth-free norm family and finite S-twists of HEREDITARY_MOMENTS.
Let E consist of nonprincipal rows a with Na<=U having a zero beta+i gamma,
beta>=sigma and |gamma|<=T. Put R=|E|. This counts CHARACTERS/indices, not the
number of all zeros with multiplicities. Fix 1/2<=theta<sigma<1 and 1<=A<=B.

Set M_A(s,chi)=sum_(Nd<=A) mu_F(d)chi(d)(Nd)^(-s), and
c_A(n)=sum_(d|n,Nd<=A)mu_F(d). Complete ideal convolution gives c_A(1)=1,
c_A(n)=0 for 1<Nn<=A, and |c_A(n)|<<_eta(Nn)^eta.
For a chosen zero rho=beta+i gamma of a row,

 sum_n c_A(n)chi(n)(Nn)^(-rho) exp(-Nn/B)
  = (1/(2pi i)) integral_(2) L(rho+z,chi)M_A(rho+z,chi)
                                            Gamma(z)B^z dz. (1)

Shift to Re z=theta-beta. It lies strictly between -1 and 0 with fixed
margins. The crossed Gamma residue at z=0 is ZERO because L(rho)=0. The
nonprincipal L is entire; there are no other crossed poles. Gamma decay
and fixed-strip polynomial bounds justify the horizontal limits. Thus
one has either a substantial L*M_A integral on Re s=theta or a substantial
Dirichlet-polynomial tail on A<Nn<=B U^delta.

For completeness, the maxima in this dichotomy have the following costs.
For the first integral its Gamma majorant decays exponentially in the
height displacement. The possible gamma lie in an interval of length O(T).
Subharmonic disk means control rowwise maxima by integrated |L M_A| on
nearby real/imaginary points. Neighboring strips change the exponents by
O(delta), using (4) and the finite explicit endpoint formulas; choose the
fixed disk radius after prescribing the loss. Positive row sums are taken
before Holder, and the SAME E is retained at every integration point. The
height cost is a fixed polynomial in 2+T, not a power of R or U.

For the tail, exponential truncation costs an arbitrary inverse U power.
Partial summation at real part sigma leaves dyadic PREFIX maxima; ordering
ideals by norm with ties fixed and binary interval decomposition costs only
logarithms. Sobolev on unit height intervals uses |P|^2+|P'|^2, with derivatives
inserting log Nn. The full-column version of DF's sieve, with coefficients
of size V^eta on n~V, gives V K(U,V). Binary disjointness at each level retains
the total square coefficient mass. The resulting tail contribution is

 Q_sigma(U,A,B)=B^(2-2sigma)+U A^(1-2sigma)
  +sup_(A<=V<=B)[U^(1/3)V^(11/6-2sigma)
                         +U^(5/6)V^(4/3-2sigma)].          (2)

The small enlargement B U^delta is paid by an arbitrary power loss, not
silently dropped. One could initially restrict to finite sums and height
intervals, then pass to the limits with these bounds.

These arguments establish the usable subset detector

 R << U^eta(2+T)^C [B^(theta-sigma) sum_E |L(theta+it) M_A(theta+it)|
                      + Q_sigma(U,A,B)],                 (3)

where a common-height supremum/integral of polynomially bounded length is
understood on the first mean, with the preceding disk/height costs included.
It is NOT the literal printed BGL (5.3), which uses theta=1/2; this gives the
changed-line and rowwise-maximal justification. The harmless negligible
rowwise errors sum to O(U^-1) by selecting the truncation order first.

## 2. The unknown R must stay inside both moments

When R<=sqrt(U), a density exponent 1/2 already suffices. Otherwise apply
Holder on E, not on the entire family:

 sum_E |L M_A| <= R^(1/4) (sum_E |L|^4)^(1/4)
                                      (sum_E |M_A|^2)^(1/2). (4)

Define S=U^(2-2theta)R^(2theta-1), L0=U^(13/6-2theta), and
M_c,d=U^d A^c for

 (c,d)=(2-2theta,0), (4/3-2theta,5/6), (11/6-2theta,1/3).

The hereditary estimates bound (4), apart from height/loss factors, by

 R^(1/4)(S+L0)^(1/4)(S+sum M_c,d)^(1/2).                  (5)

Split its two roots using positivity. There are EIGHT terms: SS, L0S,
and three each of SM and L0M. The powers of R are respectively
3theta/2-1/2, theta-1/4, theta/2, and 1/4, all strictly below one.
Consequently they can be eliminated without first replacing R by U.

If R<=C sum_j U^(d_j)R^(alpha_j)+C U^q with finitely many alpha_j<1,
then one summand is at least R divided by the number of summands. Hence
R<<sum_j U^(d_j/(1-alpha_j))+U^q, with losses renamed. This elementary
finite argument is the only self-consistency elimination used here.

For A=U^a,B=U^b, define g_H as the maximum of the following FIFTEEN
rational expressions (theta,sigma,a,b fixed):

 SS:  1+(theta-sigma)b / ((3/2)(1-theta));
 L0S: [37/24-3theta/2+(theta-sigma)b]/(5/4-theta);
 SM:  [(1-theta+d)/2+ca/2+(theta-sigma)b]/(1-theta/2),
 L0M: 13/18-2theta/3+2d/3+2ca/3+(4/3)(theta-sigma)b,
       for each of the THREE (c,d) above;
 tail: (2-2sigma)b, 1+(1-2sigma)a,
       1/3+(11/6-2sigma)v, 5/6+(4/3-2sigma)v, for v=a,b;
 small-R: 1/2.                                             (6)

There are 2+6+6+1=15 terms. It follows that

 #E(U,sigma,T) << U^(g_H+eta)(2+T)^C.                       (7)

For every prescribed positive final loss a sufficiently small fixed rho>0
therefore gives #E(U,sigma,4U^rho)<<U^(g_H+loss). A finite list of rational
parameter choices admits one rho. No uniformity in growing order, moving
thresholds or an unbounded number of strata is assumed.

## 3. A clean new exponent

Take sigma=3/4, theta=7/12, a=5/7 and b=8/7. Substitution in ALL FIFTEEN
terms of (6) gives maximum 5/7. Thus the proposed unconditional deduction is

 # {a: Na<=U, a sixth-free, L has a zero Re s>=3/4,
                           |Im s|<=4U^rho}
               <<_epsilon U^(5/7+epsilon).                 (8)

Here rho is suitably small and fixed after epsilon and the field data.
One can see the active balancing directly. The long-numerator/short-mollifier term in (3)
has size U^(10/21)R^(1/3), giving R<<U^(5/7). The dominant long/mollifier
term has size U^(15/28)R^(1/4), giving the SAME exponent. The two mixed
sieve tail endpoints have exponent 5/7 as well. No exceptional class is
counted at a threshold to its right.

Compared with #966's 43/60, the exponent gain is 1/420. Compared with the
concurrently recovered #971's 395/552, it is 5/3864. The old DF exponent
8/11 exceeds 5/7 by 1/77. These comparisons concern the norm exponent at
a common sufficiently small polynomial height, not matching optimal T
exponents or a worldwide zero-density record.

## 4. Inputs used in the full composition

For each row of strata.tsv labelled H, the exact verifier evaluates all
fifteen expressions (6). For a row labelled DF it uses the older complete
ten-term detector, retaining the second numerator mean:

 (1+d+ca)/2+(1/2-sigma)b,
       (c,d)=(1,0),(0,1),(1/3,5/6),(5/6,1/3),
 together with all SIX tail terms in (6).                  (9)

This is DF Section 9's displayed detector calculation at fixed norm powers.
Some high-sigma rows use (9) rather than (6), because imposing the small-R
floor 1/2 needlessly weakens an already rarer class. Every rational choice
is verified individually; no optimizer or claimed formula-validity range
is an analytic premise. The selected density (8) is independent of CT.
COMPOSITION.md additionally depends on CT and the explicitly adopted
short-support/local-domain arguments. Neither statement proves RH.
