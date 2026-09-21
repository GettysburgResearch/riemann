# PET26: a signed prime-extension estimate with its prime-power cost paid

**Proposed component proofs; independent review required. No new bound for
PCR26's full product covariance, no all-scale Newton gain, and no RH proof.**

This is an additive continuation of #903 at
`519252721d8b4e4c70c0fd1f21d8c9465242b338`, which includes both BCP26 and
SBC26. Their different finite partitions are preserved, not conflated.
The elementary starting identity is classical logarithmic differentiation of
Dirichlet convolution. No novelty claim is made for it, for the PNT, for
Schur's test, or for Newton inversion. The contribution proposed here is the
following explicit signed observable, its completed proof and finite constants,
and its interface to the existing cutoff-boundary programme.

## 1. The observable: keep a prime and ALL its composite multiples together

Set b=Y+1>=2, a=log b, B=b^2-1. Put M(x)=sum_(n<=x)mu(n), and M(x)=0 for x<1.
Define the inherited physical energies

$$E=\int_1^b M(x)^2\frac{dx}{x^2},\qquad
 I=\int_b^{b^2}M(x)^2\frac{dx}{x^2}.$$

Define the signed prime-extension covariance

$$\boxed{\mathcal P_Y=\sum_{p<b^2}(\log p)
       \int_b^{b^2}M(x)M(x/p)\frac{dx}{x^2}.} \tag{1}$$

The sum is over primes and is finite. It is NOT a sum of positive parts,
NOT BCP26's prime-pivot Gram, NOT PCR26's distinct-product covariance, and
NOT the rough-squareclass covariance. It is a precisely specified new
observable of the SAME native output M. No transfer between those individual
covariance decompositions has been proved.

Let Lambda(p^j)=log p, j>=1, and Lambda(n)=0 otherwise. Dirichlet convolution
is denoted *. Set Df(n)=f(n)log n. The classical identities

$$1*\mu=\delta,\quad D1=1*\Lambda,\quad
 D(f*g)=Df*g+f*Dg$$

imply

$$D\mu+\Lambda*\mu=0. \tag{2}$$

Summation by parts gives the exact native identity, for every x>=1,

$$\sum_{p^j\le x}(\log p)M(x/p^j)
   =-\log x\,M(x)+\int_1^x M(u)\frac{du}{u}. \tag{3}$$

The negative term in (3) is arithmetic cancellation between primes and
composites, not cancellation of an artificially balanced vector.

## 2. Infinite prime-power tails collapse to a finite repeated-prime pattern

Write Lambda_1(p)=log p and zero otherwise; Lambda_H=Lambda-Lambda_1.
Let mu_(p)(n)=mu(n)1_(p does not divide n). Then

$$\boxed{\Lambda_H*\mu
       =\sum_p(\log p)\,\delta_{p^2}*\mu_{(p)}.} \tag{4}$$

Proof: the local factor of mu is 1-T, whereas the p-part of Lambda_H/log p
is T^2/(1-T). Their product is T^2. All operations are coefficientwise
finite formal Dirichlet operations. Alternatively, for n=p^j m, p not
 dividing m, sum_(k=2)^j mu(n/p^k) is mu(m) for j=2 and zero for j>=3.
If m is not squarefree it is zero as well. Thus the coefficient on the
right is supported on numbers with exactly one repeated prime, to exponent
two, and all other prime exponents at most one. QED.

In particular

$$\sum_p\log p\,M(x/p)
 =-\log x\,M(x)+\int_1^xM(u)\frac{du}{u}
  -\sum_p\log p\,M_{(p)}(x/p^2). \tag{5}$$

This cancels the entire prime-power tail BEFORE estimating it. For the
uniform estimate below it is also useful to retain its positive causal
operator representation; both realizations are checked independently.

## 3. Exact finite constants

For q=p^j, j>=2, put w_q=(log p)/sqrt(q). Define

$$A(s)=\sum_{p^j\le e^s,\ j\ge2}w_{p^j},\qquad A(s)=0\ (s<0).$$

On the square stage define

$$L_b=\frac12\sup_{0\le t\le a}\{A(t)+A(a-t)\},$$

$$U_b=\sup_{0\le v\le a}\sum_{e^v\le p^j\le be^v,\ j\ge2}w_{p^j}. \tag{6}$$

Both use finite sums with q<=b^2. Closed endpoints may increase the Schur
bound at an isolated point; that is safe, not an omitted endpoint correction.
The suprema are finite step maxima. In rational r=exp(t) coordinates it
suffices to test r=1,b,q,b/q for L_b, retaining only r in [1,b], and
r=1,b,q,q/b for U_b, again retaining only r in [1,b]. Ordering these points
uses rational comparisons, not logarithm rounding.

Put

$$r_b=2(1-b^{-1/4}),\quad s_b=1-b^{-1},$$
$$d_b=\log b-r_b-L_b,\qquad h_b=s_b+U_b. \tag{7}$$

### PET26-1: signed prime-extension bound

For the actual Mobius source, at EVERY cutoff b>=2,

$$\boxed{\mathcal P_Y\le-d_b I+h_b\sqrt{EI}.} \tag{8}$$

When d_b>0 this gives the uniform, one-sided bound

$$\boxed{(\mathcal P_Y)_+\le\frac{h_b^2}{4d_b}\,E.} \tag{9}$$

The finite gate d_b>0 must be checked or established; it is not presumed
at all cutoffs. The reported cutoffs all pass. The theorem below implies
it eventually, without any numerical extrapolation.

## 4. Proof of the finite estimate

Use f(t)=exp(-t/2)M(exp t), zero for t<0, on [0,2a]. Its early and late
restrictions f_0,f_1 have squared norms E,I respectively. A prime-power
dilation becomes w_(p^j) f(t-j log p). Set

$$(Rf)(t)=\int_0^t e^{-(t-u)/2}f(u)\,du,$$
$$(Hf)(t)=\sum_{p^j\le e^t,\ j\ge2}w_{p^j} f(t-j\log p).$$

Equation (3) gives the EXACT energy identity

$$\mathcal P_Y+\langle f_1,Hf\rangle
       =-\int_a^{2a}t f(t)^2dt+\langle f_1,Rf\rangle. \tag{10}$$

Every prime and composite contribution has been retained.

**Late-to-late H.** Translate [a,2a] to [0,a]. For each shift s use
2|g(t)g(t-s)|<=|g(t)|^2+|g(t-s)|^2. After integrating and summing, the
coefficient on |g(t)|^2 is at most [A(t)+A(a-t)]/2. Therefore

$$|\langle f_1,Hf_1\rangle|\le L_b I. \tag{11}$$

**Early-to-late H.** For a fixed late t, the permitted shifts lie in
[t-a,t], an interval of length a. For a fixed early u, they lie in
[a-u,2a-u], also of length a. Each row and column mass is bounded by U_b.
Weighted Cauchy followed by Fubini (the finite atomic version of Schur's
test) gives norm at most U_b. Thus

$$|\langle f_1,Hf_0\rangle|\le U_b\sqrt{EI}. \tag{12}$$

**Late-to-late R.** Its symmetric quadratic kernel is
(1/2)exp(-|t-u|/2). On an interval of length a its row sum is
2-exp(-t/2)-exp(-(a-t)/2), at most 2(1-exp(-a/4))=r_b. Therefore

$$\langle f_1,Rf_1\rangle\le r_b I. \tag{13}$$

**Early-to-late R.** This is a rank-one operator:

$$Rf_0(t)=e^{-(t-a)/2}\int_0^a e^{-(a-u)/2}f_0(u)du.$$

The product of the two factor norms is 1-exp(-a)=s_b. Hence

$$|\langle f_1,Rf_0\rangle|\le s_b\sqrt{EI}. \tag{14}$$

Insert (11)-(14) in (10), and use integral_a^(2a) t f^2>=aI. This proves
(8). For d_b>0 complete the square in sqrt(I):

$$-d_b I+h_b\sqrt{EI}
 =\frac{h_b^2 E}{4d_b}
  -d_b\left(\sqrt I-\frac{h_b\sqrt E}{2d_b}\right)^2.$$

This proves (9). No RH, sign conjecture, independence of primes, or generic
smallness of a Mobius norm is a premise. QED.

## 5. PET26-2: asymptotic constant, without an RH-strength prime error

The classical PNT and partial summation imply

$$\sum_{p\le z}\frac{\log p}{p}=\log z+o(\log z).$$

Also

$$\sum_p\sum_{j\ge3}\frac{\log p}{p^{j/2}}<\infty,$$

by comparison with sum_(n>=2) log(n)/[n^(3/2)(1-1/sqrt(2))]. Consequently

$$A(s)=s/2+o(s). \tag{15}$$

Uniformly for 0<=s<=2a, the error in (15) is o(a): first fix a threshold
beyond which it is at most epsilon*s and then bound the remaining compact
range. The single atomic mass at a closed window endpoint is bounded by
an absolute constant and does not affect this conclusion. It follows that

$$L_b=a/4+o(a),\quad U_b=a/2+o(a),$$
$$d_b=(3/4+o(1))a,\quad h_b=(1/2+o(1))a.$$

In particular

$$\boxed{(\mathcal P_Y)_+
       \le(1/12+o(1))(\log b)E.} \tag{16}$$

The o(1) here depends ONLY on the explicit prime-power masses, not on any
hypothesis about E or I. This is an all-scale analytic theorem, not an
extrapolation of the finite negative table. We do NOT claim 1/12 is an
optimal constant for the native source.

A more informative uniform form is

$$\frac{\mathcal P_Y}{\log b}
 \le-(3/4+o(1))I+(1/2+o(1))\sqrt{EI}. \tag{17}$$

For each fixed eta>0, an increment I>=(4/9+eta)E therefore forces negative
prime-extension covariance at all sufficiently large cutoffs. The theorem
does not prove that every native covariance is negative.

## 6. PET26-3: logarithmic defects propagate quadratically through Newton

For any real arithmetic base A with A(1)=1, let nu=A^(-1) for Dirichlet
convolution and Lambda_A=(DA)*nu. Define

$$\mathscr L_A c=Dc+\Lambda_A*c,\qquad
 e=\delta-A*c,\qquad v=2c-A*c*c.$$

Then, exactly at every coefficient,

$$\boxed{\mathscr L_A v=2e*(\mathscr L_A c).} \tag{18}$$

Proof: DA=A*Lambda_A. Expand Dv using the Leibniz rule and collect terms;

$$Dv+\Lambda_A*v
 =2(Dc+\Lambda_A*c)-2A*c*(Dc+\Lambda_A*c).$$

This is (18). If c agrees with nu through Y, both e and L_A c vanish below
b; the defect in (18) vanishes on the ENTIRE reconstructed interval n<b^2.
At the first omitted coefficient it is exactly

$$\mathscr L_Av(b^2)=2e(b)\mathscr L_Ac(b). \tag{19}$$

It need not be zero. The implementation tests this endpoint, not just the
open interval. Arbitrary changes to c after Y are included in the tests.
The proof is formal coefficient algebra and applies to the existing clipped
completion as well as to the truncated source; no whole-line energy is
assigned to an unbalanced infinite Newton output.

For exact testing one can replace D by D_p c(n)=v_p(n)c(n). This is also a
derivation, and every identity has integer/rational coefficients. Summing
these identities with weights log p gives the logarithmic one.

For a NONnative source a, the energy equation (10) has the additional term

$$\int_b^{b^2} A_a(x)D_a(x)\frac{dx}{x^2},\qquad
 D_a(x)=\sum_{n\le x}(Da+\Lambda*a)(n). \tag{20}$$

Dropping (20) is not permitted. The delta-source control violates (8) and
(9) when this term is falsely discarded. Thus the new signed estimate is
not a generic balanced-vector theorem in disguise.

## 7. The actual consumer and the missing side of the estimate

The entire next canonical state remains

$$\mathcal A_B=E+I+2b^2(u_Y+u_{\rm ann})^2,$$
$$u_Y=\int_1^bM(x)\frac{dx}{x^2},\qquad
 u_{\rm ann}=\int_b^{b^2}M(x)\frac{dx}{x^2}. \tag{21}$$

Both signed means are reported and the completed state is reconstructed.
The innovation state is the same formula with b^2 instead of 2b^2. No
comparison of isolated diagonals in different coordinate systems is asserted.

**Crucial limitation:** (9) bounds the POSITIVE part of the new signed
covariance. A large output energy can coexist with a very NEGATIVE value
of P_Y. Therefore (9) is not by itself an upper bound on I, nor a proof of
RH. This direction-of-inequality issue must remain adjacent to the claim.

For an explicit connection, write N_Y=(-P_Y)_+. Equation (8) gives

$$\sqrt I\le
 \frac{h_b\sqrt E+\sqrt{h_b^2E+4d_bN_Y}}{2d_b}\quad(d_b>0). \tag{22}$$

Thus a genuinely new upper estimate on N_Y would have an immediate physical
energy consumer. For example N_Y<=K log(b)(1+E), uniformly along the square
ladder, would give I<=C_K(1+E), hence polylogarithmic physical energy along
that ladder. The existing Mellin/Cauchy-Schwarz continuation argument then
yields RH. NO SUCH NEGATIVE-PART ESTIMATE IS PROVED HERE. This conditional
ending is included to expose what is still required, not advertised as a
new easier RH criterion.

The forward research target is quantitative control of the compensating
prime-extension magnitude, or a proved comparison to the existing harmonic
rough-core blocks. Merely proving a negative sign or inserting the finite
1/12 asymptotic constant at small cutoffs will not suffice.
