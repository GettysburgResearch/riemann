# The central zero-heat trace and an exact reciprocal-xi subordinator

Date: 2026-09-12. Proposed continuation of PR #842 at
`aa281cc871637f287ff91457e5608b5b5f694c25`.

**PROPOSED COMPONENT PROOFS. Independent mathematical and code review required.
RH, complete monotonicity of the zero-heat trace, the unweighted cumulant-Hankel
sign, and the original pair-Ising realization remain UNPROVED.**

This packet establishes a different positive object: an exact nonnegative
infinitely divisible random variable with a reciprocal-xi Laplace transform.
It is not the theta random variable, an Ising magnetization, or a positive
spectral measure on zeta-zero locations. Positivity and monotonicity of its
Levy kernel are proved at all positive times, including the entire unknown
zero tail. The stronger Stieltjes/Thorin property remains the RH-bearing step.

The heat-trace, Laplace, Bernstein, Hadamard, Poisson and gamma-convolution
mechanisms are classical. The repository's PR #379 already gives an ALL-CENTER
first-Hermite heat criterion. Reciprocal-xi/Wald/van-Dantzig constructions have
prior literature. No external novelty or priority claim is made here. The
contribution offered for review is the fixed-source, explicit all-time sign
estimate, its probabilistic consequences and the exact distinction between
factorial-weighted and unweighted cumulant positivity.

## 1. Source, divisor, and the only imported numerical theorem

Keep the literal full-line convention

    Xi(z)=xi(1/2+iz)=integral_R phi(x) exp(izx) dx,
    phi(x)=sum_(n>=1) exp(x/2)(4Q_n^2-6Q_n) exp(-Q_n),
    Q_n=pi n^2 exp(2x),  Z=Xi(0)>0,  w=phi/Z.

The completion xi is entire, with xi(0)=xi(1)=1/2. Jacobi inversion makes
phi even. Termwise positivity is used ONLY for x>=0; evenness supplies the
other half-line. The locally differentiated series has double-exponential
tails. Put M(h)=integral exp(hx)w(x)dx=xi(1/2+h)/xi(1/2).

We import Platt--Trudgian [PT], Theorem 1, ONLY for its consequence

    every nontrivial zeta zero beta+i gamma with 0<gamma<=30
    has beta=1/2.                                            (LC)

The theorem is published and unconditional, with rigorous interval/Turing
verification through much greater height. Its numerical campaign is NOT rerun
here. No claim about zeros above 30 is imported. Section 8 independently
reconstructs Xi(14)>0 and Xi(15)<0 from the literal theta integral. Thus there
is at least one REAL Xi zero gamma_0 in (14,15). No uniqueness, simplicity,
first-zero status, or completeness of the low census follows from that sign
check alone. Completeness in (LC) is a separate external dependency.

For every nontrivial zeta zero rho=beta+i gamma with gamma>0, put

    z_rho=(rho-1/2)/i=gamma-i(beta-1/2),    a_rho=z_rho^2.

Sum over all these rho, with analytic multiplicities. Equivalently take one
member of each +/- pair of Xi zeros, retaining both conjugate members for an
off-line quartet. The strip theorem gives |Im z_rho|<1/2. By (LC), all
Re(a_rho)>0: low nodes are positive, and high nodes have real part at least
gamma^2-1/4. Xi(0)>0 and discreteness give a strictly positive minimum of
Re(a_rho). Real-axis nontrivial zeta zeros are absent since M(h)>0 for real h.

The even entire function

    F(v)=Xi(sqrt(v))/Z

is defined by its power series, without a square-root branch. The source
bound phi(x)<=C exp(C|x|-c exp(2|x|)) gives
log max_(|z|<=R)|Xi(z)|=O(R log(R+2)). For example substitute u=exp(2x)
in the absolute half-line integral and bound it by a gamma integral.
Hadamard factorization, or the corresponding zero count and product theorem,
therefore gives

    F(v)=product_(gamma>0)(1-v/a_rho),
    sum_(gamma>0) |a_rho|^-1 < infinity.                     (1)

Multiplicity is included in sums/products throughout. There is no unknown
exponential factor because F has order at most 1/2<1 and F(0)=1.
These are classical entire-xi facts, not consequences of RH or a finite table.

Define the CENTRAL zero heat trace

    H(t)=sum_(gamma>0) exp(-t a_rho),    t>0.                 (2)

Conjugation makes H real. The series and all fixed derivatives converge
absolutely and locally uniformly in t>0. This is heat on the ZERO locations,
not the de Bruijn heat deformation of the theta density. No individual term
at an unknown nonreal node is asserted nonnegative.

## 2. A crude whole-source zero count, sufficient for complete tails

The source has the elementary envelope

    0<phi(x)<256 exp(-x^2),    x in R.                       (3)

For x>=0, Q=pi n^2 exp(2x) satisfies
x^2+x/2 <=(3/2)exp(2x)<=Q/2. Therefore
exp(x^2)phi_n(x)<=4Q^2 exp(-Q/2)<=256 exp(-Q/4).
Sum exp(-3n^2/4)<sum 2^-n=1, using exp(3/4)>2, and reflect.

On [0,1/8], 3<Q_1<5: use 3<pi<16/5 and exp(1/4)<3/2.
Thus phi(x)>18/243, since exp(5)<3^5. Integration on both half-lines gives
Z>1/54. Gaussian integration now yields

    |F(v)|<= (256 sqrt(pi)/Z) exp(|v|/4)
           <2^15 exp(|v|/4).                               (4)

For N_F(r), the number of zeros in |v|<=r with multiplicity, Jensen at radius
2r gives N_F(r)<=15+r/(2log2)<15+r. Boundaries follow by radius limits.
If N(T) counts all gamma in (0,T], then |a_rho|=gamma^2+(beta-1/2)^2, so

    N(T)<=15+T^2+1/4 <=2T^2,    T>=4.                      (5)

This deliberately rough bound counts the FULL unknown divisor. It is not the
usual sharper Riemann--von Mangoldt estimate and requires no numerical count.

For A>=4, Stieltjes integration of (5), with the nonpositive lower-endpoint
term -N(A)g(A) retained or discarded only in the upper bound, gives

 sum_(gamma>A) exp(-t gamma^2)
       <= B0(t,A):=2(A^2+1/t)exp(-t A^2).                  (6)

If t(A^2+1/4)>=1, g(u)=(u^2+1/4)exp(-t u^2) is decreasing on [A,infinity).
Using -g'(u)<=2tu(u^2+1/4)exp(-t u^2) gives

 sum_(gamma>A)(gamma^2+1/4)exp(-t gamma^2)
 <= B1(t,A):=2 exp(-t A^2)
       [A^4+2A^2/t+2/t^2+(A^2+1/t)/4].                   (7)

In particular, |exp(-t a_rho)|<=exp(t/4-t gamma^2), and
|a_rho exp(-t a_rho)|<=(gamma^2+1/4)exp(t/4-t gamma^2).
Equations (6)--(7) cover every remaining zero and multiplicity, whether or
not its real part is 1/2.

## 3. HTP1: strict central heat positivity and monotonicity for ALL time

**Theorem.** With the fixed source and imported (LC), for EVERY t>0,

    H(t) > (1/2) exp(-225t),
    -H'(t) > 98 exp(-225t).                               (8)

Since (LC) is an established finite verification, these are unconditional
number-theoretic assertions at the proposed-proof scope, not consequences of
the unproved global RH. The certificate supports the elementary constants
and anchor sign; it is not a machine proof of this infinite theorem.

### 3.1 Small times, 0<t<=1/32

Set v=1/t>=32 and A=v. Write a=A_rho+i B_rho, where
A_rho=gamma^2-(beta-1/2)^2>0 and |B_rho|<=gamma.
For gamma<=1/t we have |tB_rho|<=1. Hence

 Re exp(-ta)=exp(-tA_rho)cos(tB_rho)>0,
 Re[a exp(-ta)]=exp(-tA_rho)
       [A_rho cos(tB_rho)+B_rho sin(tB_rho)]>0.            (9)

The real anchor contributes more than exp(-225t) to H and more than
196 exp(-225t) to -H'. Use the absolute tail bounds, not a positivity
assumption, outside gamma<=A. Its H-to-anchor ratio is at most

    2(v^2+v) exp[-v+901/(4v)]
       <=2112 exp(-24)<2112/2^24<1/2.                    (10)

For -H' the corresponding ratio is at most

 [2(v^4+2v^3+(9/4)v^2+v/4)/196] exp[-v+901/(4v)]
       <2232848/(196*2^24)<1/2.                          (11)

Each monomial v^j exp[-v+901/(4v)], j<=4, decreases for v>=32;
its logarithmic derivative is j/v-1-901/(4v^2)<0. At v=32 the exponent is
less than -24. Thus the bounds cover the WHOLE small-time interval, not a grid.

### 3.2 Large times, t>=1/32

All nodes with gamma<=30 are central by (LC) and contribute nonnegatively to
both sums. For gamma>30 apply (6)--(7). The relative errors are bounded by

    2(900+1/t) exp[-2699t/4] <1864/2^21<1/2,              (12)

and

 (2/196)[30^4+2*30^2/t+2/t^2+(30^2+1/t)/4]
       exp[-2699t/4] <1739762/(196*2^21)<1/2.             (13)

All factors decrease with t and the exponent at t=1/32 is less than -21.
Subtracting the tails from the anchor proves (8).

The low zeros were NOT used to decide a global functional without a complement
argument: (6)--(13) are that complement argument. This theorem controls only
the fixed CENTER ZERO. It does not prove the all-center first-Hermite condition
in PR #379, or signs of all higher derivatives at this center.

## 4. HTP2: the same H has an exact all-prime-power formula

Let gamma_E be Euler's constant, and Lambda the von Mangoldt function. For t>0,

 H(t)=exp(t/4)-(gamma_E+log pi)/(4sqrt(pi t))
    +(1/(4sqrt(pi t))) integral_0^infinity
        [exp(-u)-exp(-u/4-u^2/(16t))]/[1-exp(-u)] du
    -(1/(2sqrt(pi t))) sum_(n>=2) Lambda(n)/sqrt(n)
                                      exp[-(log n)^2/(4t)]. (14)

Every prime POWER occurs. The integral's two terms must be kept together near
u=0. This is a scalar special case of the classical explicit-formula mechanism;
we derive its exact normalization without importing a local operator identity.

Put A(s)=F(-s)=xi(1/2+sqrt(s))/xi(1/2), defined as an entire function of s via
its series. It is positive for real s>=0. Define Psi(s)=log A(s) there. For
r=sqrt(s)>1/2, the ordinary completion identity and absolutely convergent Euler
logarithmic derivative give

 Psi'(s)=1/(s-1/4)-(log pi)/(4sqrt(s))
       +psi(1/4+sqrt(s)/2)/(4sqrt(s))
       -(1/(2sqrt(s))) sum_(n>=2) Lambda(n)/sqrt(n)
                                           exp(-sqrt(s)log n).       (15)

Here psi is digamma. Use the elementary Gaussian Laplace identity

 integral_0^infinity exp(-st-b^2/(4t))dt/sqrt(pi t)
                         =exp(-b sqrt(s))/sqrt(s), b>=0, s>0,        (16)

and DLMF 5.9.16,

 psi(z)=-gamma_E+integral_0^infinity
                      [exp(-u)-exp(-zu)]/[1-exp(-u)]du.

The Laplace transform in t of (14) is (15) for s>1/4. All interchanges have
absolute control. For the prime term use Tonelli and r>1/2. For the gamma
integral at u<1, split its numerator into exp(-u)-exp(-u/4) and
exp(-u/4)[1-exp(-u^2/(16t))]. Divide by 1-exp(-u)>=u/2.
The first part is bounded uniformly; integrating the second against
exp(-st)t^-1/2 gives a constant times [1-exp(-u sqrt(s)/2)]/u, bounded as
u tends to zero. At u>=1 both transformed terms decay exponentially.
The pole term's initial Laplace domain is s>1/4, not all s>0 separately.

On the other hand, (1) gives Psi'(s)=sum 1/(s+a_rho). All Re(a_rho)>0 and
sum 1/Re(a_rho)<infinity, the latter by (1) and the high-strip geometry.
Thus (2) has this Laplace transform for s>=0. Uniqueness for weighted L1
Laplace transforms and continuity in t identify (14) with (2) at every t>0.
The full signed cancellation in (14) is retained; none of its individual
terms is asserted to be the Levy kernel on its own.

A completely explicit arithmetic truncation bound is available. If N is an
integer with a=log N>=2 and a>t, then Lambda(n)<=log n and monotonicity give

 sum_(n>N) Lambda(n)/sqrt(n) exp[-(log n)^2/(4t)]
 <=2t[1+t/(a-t)] exp[t/4-(a-t)^2/(4t)].                    (17)

Indeed compare with the integral of log(x)x^-1/2 exp[-log^2(x)/(4t)] from N,
then put v=log x and complete the square. Its integral is
exp(t/4)[2t exp(-(a-t)^2/(4t))+t integral_a^infinity exp(-(v-t)^2/(4t))dv].
The Gaussian tail is at most 2t exp(-(a-t)^2/(4t))/(a-t). This proves (17).
The formula is practical at some scales and badly cancellation-conditioned at
others; no all-scale fast numerical algorithm is asserted.

## 5. HTP3: construct the EXACT reciprocal-xi random process

For s>=0, the product and complete integral above yield

 Psi'(s)=integral_0^infinity exp(-st)H(t)dt,
 Psi(s)=integral_0^infinity [1-exp(-st)]H(t)dt/t.           (18)

The first integral is absolutely convergent even at s=0 because
sum 1/Re(a_rho)<infinity. More generally every integral of t^k|H(t)| is finite;
use sum k!/[Re(a_rho)]^(k+1), or a fixed positive lower bound for Re(a_rho).
Since H>0, the measure H(t)dt/t is a Levy measure on (0,infinity): its
integral against min(1,t) is finite. There is neither drift nor killing in (18).

For any tau>=0 construct independent Poisson jump sums in the intervals
(2^(-j-1),2^(-j)], j>=0, and (1,infinity), with intensity

    tau H(t)dt/t.

Each interval has finite intensity. The expected sum of small jumps is finite,
so their nonnegative sum exists almost surely; the large-jump intensity is
finite. The elementary compound-Poisson formula and bounded convergence give

 E exp(-s S_tau)=exp(-tau Psi(s))
              =[xi(1/2)/xi(1/2+sqrt(s))]^tau,
                           s>=0, tau>=0.                 (19)

Using Poisson measures with an additional time coordinate constructs all tau
on one space with stationary independent increments. Thus S is a driftless
subordinator, meaning an increasing Levy process, with mean

    E S_tau=tau Psi'(0)=tau q_1=tau Var_w(U)/2.             (20)

This is an exact probability realization of the RECIPROCAL transformed xi.
It is NOT a realization of the theta density as an Ising magnetization, and
NOT a claim that the theta characteristic function itself is infinitely divisible.
No high zero is assumed central in constructing this probability law. Formula
(14), rather than a supplied zero list, also defines its intensity.

### Self-decomposability and an explicit gamma component

For every 0<c<1,

 Psi(s)-Psi(cs)=integral_0^infinity (1-exp(-st))
                           [H(t)-H(t/c)]dt/t.

The kernel is nonnegative because H decreases. It satisfies the same Levy
integrability test. Hence for each tau there is a nonnegative independent
Y_(tau,c) such that S_tau has the distribution of c S'_tau+Y_(tau,c), where
S'_tau is an independent copy. This proves self-decomposability, rather than
assuming it from the closed expression (19).

Moreover (8) gives the independent decomposition

    S_tau =_law Gamma(shape=tau/2, RATE=225) + R_tau,       (21)

where R_tau>=0 is infinitely divisible. Subtract (1/2)exp(-225t)/t from the
Levy density, and use Frullani's formula. No self-decomposability of R_tau is
asserted.

The reciprocal real-axis function is consequently a characteristic function:

 xi(1/2)/xi(1/2+x)=E exp(-x^2 S_1),    x in R.             (22)

Evenness around 1/2 handles x<0. It is the characteristic function of a
centered Gaussian mixture with conditional variance 2S_1, and of the symmetric
Levy process obtained by Brownian subordination. This classical construction
does not imply imaginary-axis zeros for M(h), and is not a new Lee--Yang theorem.

## 6. HTP4: scalar cumulant signs and factorial-weighted positivity at ALL orders

Let the native q_n have exactly the parent's normalization

 q_n=(-1)^(n+1)kappa_(2n)(w)/[2(2n-1)!]=sum a_rho^(-n).

Equation (18) and its derivatives give

 q_n=1/(n-1)! integral_0^infinity t^(n-1)H(t)dt
                      >1/(2*225^n),    n>=1.             (23)

Thus the alternating signs of ALL even cumulants hold at once. This is not an
extrapolation of the previous list of moments through 36. It is a consequence
of the all-time trace estimate and its complete complement bound.

For EVERY degree d the two matrices

 Ghat_d=((i+j)! q_(i+j+1))_(0<=i,j<=d),
 Hhat_d=((i+j+1)! q_(i+j+2))_(0<=i,j<=d)                   (24)

are strictly positive definite. They are precisely the Gram matrices of the
monomials in L2(H(t)dt) and L2(t H(t)dt). Nonzero polynomials cannot vanish
almost everywhere under these strictly positive densities. No assumption on
zeros being simple is made.

The parent's native target is INSTEAD

    H_d=(q_(i+j+2))_(0<=i,j<=d)>=0 for every d.             (25)

Removing the factorials is not a congruence or a positivity-preserving Schur
operation. The two-by-two reciprocal-factorial matrix

    [1,1/2; 1/2,1/6]

has determinant -1/12. Therefore (24) must not be substituted for (25).
All scalar entries may be positive while a polynomial quadratic form is negative.

## 7. The exact remaining step, and an explicit test of the attempted finish

The appropriate stronger property is

    (-1)^k H^(k)(t)>=0 for EVERY k>=0 and t>0.             (CM)

Only k=0 and k=1 have been proved in Section 3. Bernstein's classical
representation theorem identifies (CM) with H being a Laplace transform of a
positive measure on [0,infinity). This is also equivalent, here, to Psi' being
a Stieltjes function:

    Psi'(s)=integral_[0,infinity) dnu(x)/(s+x).             (26)

There is no constant term because Psi'(s)->0 as s->infinity, by dominated
convergence in the absolutely summable divisor series. A term proportional to
1/s is excluded by finiteness at zero. Tonelli transfers the Laplace/Stieltjes
representations in either direction; uniqueness identifies the density H.
The positive measure need not have finite total mass, but its integral
against 1/(1+x) is finite. These details matter for the whole infinite spectrum.

For the ACTUAL source,

    RH <=> (CM) <=> Psi' is Stieltjes.                     (27)

Under RH take nu=sum m_rho delta_(gamma_rho^2). Conversely a Stieltjes function
is holomorphic on C minus the nonpositive real axis. The actual meromorphic
continuation Psi'(s)=A'(s)/A(s) has a nonzero positive-integer residue at each
s=-a_rho. Any nonreal a_rho would be a nonreal pole. Equality on the positive
axis analytically continues on the connected slit domain with the isolated
poles removed, contradicting such a pole. The map z->z^2 is injective on the
chosen Re z>0 half of the Xi divisor, so distinct nodes cannot cancel residues.
All real a_rho are positive, by the source's real-axis positivity. This proves
the converse without a rightmost-zero, eigenvector-completeness or simplicity
assumption. In probability terminology (26) is the missing gamma-convolution /
Thorin property of (19), not ordinary infinite divisibility.

The following exact spectral control shows why the proposed immediate finish
'positive and decreasing H, hence Stieltjes' is false. Set

 H_*(t)=2exp(-t)+2exp(-2t)cos t.

It is positive for t>0. For 0<t<=1, cos t and sin t are positive, so H_*'<0.
For t>=1,

    -H_*'(t)>=2exp(-t)[1-sqrt(5)exp(-t)]>0,

because e>sqrt(5). Yet its resolvent is

 Psi_*'(s)=2/(s+1)+1/(s+2-i)+1/(s+2+i),                   (28)

which has nonreal poles and cannot be Stieltjes. It defines a perfectly valid
self-decomposable positive random variable through the same Poisson construction.
Its reciprocal entire polynomial is

    A_*(s)=(1+s)^2[(s+2)^2+1]/5.

Thus even INTEGER residue multiplicities do not repair the implication.
For q_n^*=2+2Re[(2+i)^(-n)] all entries are positive. Nevertheless with
P(x)=(x-1)(35x-13), lambda=(2-i)/5 satisfies lambda P(lambda)=2i, and

    sum_(i,j) P_i P_j q^*_(i+j+2)=-8.                     (29)

The real node at 1 is annihilated. This is a SYNTHETIC spectral example, not
the theta law, not an Ising model, and not an asserted zeta zero. It isolates
the exact failed inference between the two kinds of positivity.

### Where the direct arithmetic attempt stops

In (14), the pole term is positive, the prime-power sum is subtracted, and
the combined gamma integral has a signed numerator. Section 3 proves their
combined sign and first-time monotonicity using strip geometry and a complete
tail bound. Differentiating (14) further introduces higher Hermite factors
in log n / sqrt(t), with both signs. Their arithmetic cancellation is not
estimated here at unbounded derivative order. Positivity of the original
theta density or of the constructed Levy density cannot replace that estimate.

The probabilistic realization is therefore COMPLETE for the weaker positive
class, but its Stieltjes upgrade is OPEN and is precisely RH-strength. The
original pair-Ising and unweighted Hankel targets also remain open. This is
not an end-to-end RH proof with a routine final check delegated to reviewers.

## 8. Native finite certificate and its scope

check.py uses standard-library integers/Fractions and outward dyadics of unit
2^-192. Its interval design is adapted from the uploaded CSI intervals.py,
but no old numerical moment receipt is an input. Machin's pi formula uses
96 alternating terms of arctan(1/5) and arctan(1/239), with the next omitted
term. Exponential evaluation reduces the input to modulus <=1/8, uses degree
48 and remainder 2/(8^49*49!), and squares with outward rounding. For x<=-192,
exp(x)<=2^-192. For negative interval inputs, the 1-Lipschitz bound pays input
width. Cosines at modulus <=32 are reduced by 32, approximated through degree
64 with remainder 1/66!, and doubled five times. Each operation encloses the
full real value; no binary64 arithmetic or special-function oracle is used.

The first four literal theta terms on [0,2] are integrated at ALL 4097 nodes
of a 4096-cell composite Simpson rule. For the derivative polynomials

 P_0(Q)=4Q^2-6Q,
 P_(j+1)=2Q P_j'+(1/2-2Q)P_j,

the first-four-term L1 derivative bounds on [0,2] are

 B_j=6 sum_k |[Q^k]P_j|(k-1)!,
 (B_0,...,B_4)=(60,366,3135,71463/2,2044911/4).

For f(x)=sum_(n<=4)phi_n(x)cos(zx), its fourth-derivative L1 bound is
C_z=sum_(j=0)^4 binom(4,j)|z|^(4-j)B_j. The two-cell Simpson Peano kernel has
supremum h^4/72, so the DOUBLE half-line integration error is <=2h^4 C_z/72.
Both endpoint nodes retain their correct weights.

For the complete omitted source, substitution Q=pi n^2 exp(2x) gives

 2 integral_a^infinity phi_n(x)dx
       <=4(Q_0^2+2Q_0+2)exp(-Q_0), Q_0=pi n^2 exp(2a).

Consecutive majorants have ratio <1/2 in the tails used here. All n>=5 over
x>=0 cost at most 8(75^2+150+2)exp(-75); all n>=1 over x>2 cost at most
8(150^2+300+2)exp(-150), using pi exp(4)>150. The latter overcounts beyond
the first four indices, harmlessly. Both are widened using directed exp bounds.
Cosine modulus is at most one, so this pays the complete complex-sign tail of
the REAL Fourier evaluations used for the anchor.

The resulting fresh enclosures, rounded outward for this display, are

 Xi(0) in (0.497120777381093745, 0.497120778995534475),
 Xi(14) in (0.000201274673576665, 0.000201314214893850),
 Xi(15) in (-0.000705721431786749,-0.000705674485856346).

No heat trace is numerically truncated to a list of zeros. The checker also
reconstructs (10)--(13)'s four exact rational budgets, the spectral witness (29),
and the inverse-factorial determinant. The independent analytic imports are
listed below. Normal/optimized execution is the SAME arithmetic implementation,
not independent mathematical acceptance.

## 9. Sources, overlaps, and review limits

[P] PR #842 at aa281cc871637f287ff91457e5608b5b5f694c25; earlier CSI packet
at 4558dce9cb981a2e8c0e3e058b21a5b17f6a1cf5, path
standalone/2026-09-12-theta-cumulant-spectral-index/. The native theta and q_n
normalizations are retained. Its unweighted 9x9 certificates are NOT enlarged
by (24), and its old numerical integration was not rerun. New anchor integration
is reconstructed here. The prior finite-jet perturbations are not native sources.

[H] PR #379 at 589f1c05ccaf248cf08c87fefa7d5ab6d2380708: metadata/body inspected.
It already formulates zero-heat monotonicity at EVERY real center. No theorem
from its uninspected full proof is imported; our fixed-center proof and (14)
are reconstructed directly. All-center positivity is not inferred from (8).

[PT] D. Platt and T. Trudgian, The Riemann hypothesis is true up to 3*10^12,
Bull. London Math. Soc. 53 (2021), 792--797; arXiv:2004.09765v1, Theorem 1.
https://arxiv.org/abs/2004.09765
The theorem statement, scope and Turing completeness explanation were read in
parsed text and the PDF page image. Only (LC) is imported. The original entire
numerical verification is not rerun or independently re-audited.

[D] NIST DLMF 5.9.16, digamma integral, and classical Gaussian Laplace identity.
https://dlmf.nist.gov/5.9.E16
Hadamard/Jensen, Laplace uniqueness, Bernstein's representation theorem and
Poisson construction are classical. Their roles are explicit above; the new
claim does not depend on a nonstandard variant of any of these theorems.

[R] N. Polson, Riemann, Thorin, van Dantzig Pairs, Wald Couples and Hadamard
Factorisation, arXiv:1804.10043. Related reciprocal-xi literature, inspected
in selected statements/page images only. No asserted GGC completion or RH
conclusion from that manuscript is imported, and no comprehensive validity
review is claimed. Equations (18)--(29) distinguish ordinary infinite divisibility
from the strictly stronger property needed here and are independently derived.

Recent #870/#871/#874--#876 received the reading scopes recorded in SOURCES.json.
Their protected windows, model growth matches and positive response operators
are not silently promoted to global zero confinement or source identification.
