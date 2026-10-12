# Complete inverse-square Hankel mechanism: independent operator assessment

Status: exact analytic criterion and synthetic obstruction; submitted for review.
Scope: complete native Xi moments at every order, not a finite census and not
an estimate for the generalized Eisenstein/Chowla moments.
Dependencies: complete paired Xi genus-zero product after the parity square,
absolute sum of inverse-square roots, and Xi(iy)>0 for real y.
What was run: exact rational countermodel controls in the companion checker.
Smallest remaining gap toward RH: prove all the native Hankel forms positive.

## H1. Exact moment representation and pole normalization

Write the complete native Xi roots as+-r,Re(r)>0, with integer multiplicities m_r,
including both conjugate representatives when r is nonreal. Put
p_k=sum_r m_r r^(-2k),k>=1,x_r=r^-2. Absolute convergence of sum m_r|r|^-2
implies compact complex node support: B=sup|x_r|<infinity and
|p_(n+1)|<=A B^n,A=sum m_r|r|^-2. The p_k are real by complete conjugation.
For the parity-square entire function Psi(z)=Xi(sqrt(z))/Xi(0), order1/2<1,
the complete genus-zero product gives

F(z)=sum_(n>=0)p_(n+1)z^n=-Psi'(z)/Psi(z)
    =sum_r m_r x_r/(1-z x_r).

The series is locally normally convergent off the complete root-square set.
Every pole z=r² has residue -m_r. The map r->r² is injective onRe(r)>0;
coincident roots simply add their positive integer multiplicities. Thus no
nonreal pole can disappear through signed cancellation or a dropped exponential.

## H2. All Hankel forms alone imply real roots for the actual source

Suppose every real finite polynomial f(X)=sum c_i X^i satisfies
L(f²)=sum c_i c_j p_(i+j+1)>=0. Give real polynomials their semidefinite
inner product L(fg), quotient the nullspace and complete. Multiplication T byX
is symmetric. Nullspace invariance follows directly from Cauchy--Schwarz:
if L(f²)=0 then L(f X²f)=0, hence L((Xf)²)=0.

For a fixed polynomial f define a_n=L(X^(2n)f²)=||T^n f||².
Cauchy--Schwarz gives a_n²<=a_(n-1)a_(n+1). On the other hand

a_n<=A B^(2n)(sum_i|c_i|B^i)².

If a0=0 then a1=0. If a0>0 and a1>B²a0, log-convexity forces
all successive ratios >=a1/a0>B² and hence a_n>=a0(a1/a0)^n,
contradicting the geometric upper bound. Therefore ||Tf||<=B||f||.
T extends to a bounded selfadjoint operator on the completion. The spectral
measure of the constant vector represents L on[-B,B]. Its generating transform
int_[−B,B] dmu(x)/(1-zx) is analytic for every nonreal z. Equality near zero
with the complete meromorphic F extends by analytic continuation on the common
connected nonreal domains. Any actual nonreal root square r² would produce a
nonzero pole in F there, contradicting analyticity of the measure transform.
Thus every actual r² is real. The actual source has Xi(iy)>0 for real y,
so no r can be purely imaginary. All actual r are real, which is RH.

Conversely, under RH the complete moments are the moments of the positive
measure sum m_r r^-2 delta_(r^-2), and every Hankel form is nonnegative.
This proves the exact criterion

RH iff every finite matrix (p_(i+j+1))_(0<=i,j<=N) is positive semidefinite,
for every integer N>=0, using the COMPLETE native actual-Xi moments.

No finite collection of such matrices proves this all-order condition.

## H3. Optional Stieltjes localizers

If a known source bound gives |r|>=R^-1/2, the additional all-order forms
L(X f²)>=0 andL((R-X)f²)>=0 make0<=T<=R directly, so the spectral
measure is supported on[0,R]. This supplies another complete-source proof.
Under RH these localizers hold. These all-order conditions are stronger than
scalar p_k>=0 and must not be replaced by individual positive moments.

## H4. Exact countermodel with the classical vertical-strip geometry

Take an even real polynomial with root representatives15,100+i/2,100-i/2,
each multiplicity1. Its roots all satisfy |Im r|<=1/2 and|Re r|>14.
Nevertheless it has nonreal roots. For every integer k>=1,

p_k=225^-k+2Re((100+i/2)^(-2k))
   >=225^-k-2(40001/4)^-k>0,

since2*(900/40001)^k<1. Thus even cofinal positivity of these scalar
inverse-square moments does not imply real roots in this geometry.

Let x=(100+i/2)^-2=a+ib andx0=1/225. There is a real rational quadratic
P(X)=(X-x0)(A+B X) withP(x)=i(100+i/2), by real-linear interpolation
at the nonreal x. It hasP(x0)=0. Consequently

L(P²)=x0P(x0)²+xP(x)²+conjugate(xP(x)²)=-2.

The explicit coefficients and exact native-form Hankel contraction are
recorded by `check_native_hankel_countermodel.py`. This is a synthetic
obstruction to a proposed inference, not a counterexample to actual Xi.

The useful source gate for further work is therefore positivity of complete
quadratic moment combinations, not increasing the list of scalar moment signs.
