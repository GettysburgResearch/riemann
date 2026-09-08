# A signed prime-tail defect on a nonescaping, bounded-norm sequence

Status: PROPOSED COMPLETE COMPONENT PROOF; independent review required.
RH and full-source matrix positivity remain UNPROVED.
Local label: ASTRA-QC-07. Same exact source/metric as PROOF.md.
Dependencies: QC1/QC4; the parent's unconditional rational-test explicit
formula and trace bound ||Gamma_0||<1/2. No zero prefix or PNT is used.
No external priority claim. Limits below are explicitly ITERATED, not a
uniform assertion about arbitrary simultaneous cutoff schedules.

## 1. A completely predetermined sequence

Let r>=1, m=r+2, d=r^2, and let Pi_r be the ORIGINAL-L2 projection onto
E_(m,d) from PROOF.md. Define

    f(t)=exp(-t)1_[1/2,infinity)(t),
    f_r=Pi_r f,    epsilon_r=||f_r-f||_2.

QC1 at c=1 proves f_r->f in L2, so epsilon_r->0. These are bounded-norm,
NONESCAPING tests, unlike the earlier d=o(m^2) families. Every f_r is a
finite real exponential polynomial and has integral zero, whereas

    b:=integral f=exp(-1/2),   ||f||^2=1/(2e).

The coefficient vector of f_r is explicitly source-independent. In the
basis u_j, j=m,...,m+d, with exact G from QC14, let

    v_j=2^(-j)[sum_(l=0)^(j-2) 1/l!-1/(j-1)!],
    theta_r=v^t G^(-1)v.

Elementary incomplete Gamma integration gives <u_j,f>=e^-1 v_j, hence

    f_r=sum_j [e^-1 G^(-1)v]_j u_j,
    epsilon_r^2=e^-2(e/2-theta_r).                         (ED1)

All v, G, and theta_r are rational. Thus any requested error threshold can
be checked with rational arithmetic and an elementary series enclosure of
e; no zeta zeros, primes, or xi evaluations enter this projection error.
Convergence guarantees eventual success of such a search, but no practical
size bound or universal explicit first r is supplied.

## 2. Complete explicit formula and convergence of its continuous part

For a real test h put R_h(A)=Laplace(h)(A),

    g_h(x)=R_h(x^2+1/4)^2,
    G(h)=int_R g_h(x)Omega(x)dx,
    P(h)=sum_(n>=2) Lambda(n)n^(-1/2) ghat_h(log n),
    Q(h)=<h,Gamma_0 h>.

The full formula is

    4pi Q(h)=4pi R_h(0)^2+G(h)-2P(h).                       (ED2)

It applies to each finite f_r. For the limit f it also applies directly:

    R_f(A)=exp(-(A+1)/2)/(A+1),
    g_f(x)=exp(-(x^2+5/4))/(x^2+5/4)^2.                    (ED3)

The last even function is analytic in |Im x|<sqrt(5)/2, so a Fourier contour
strictly above height 1/2 gives absolute convergence of the prime series.
All finite rational tests have the same open pole-free strip. Absolute
convergence is asserted for EACH fixed test, not uniformly in r.

For A=x^2+1/4>0, Cauchy-Schwarz in time gives

    |R_(f_r)(A)-R_f(A)|<=epsilon_r/sqrt(2A),
    |g_(f_r)(x)-g_f(x)|<=epsilon_r ||f||/A<epsilon_r/A.      (ED4)

We used ||f_r||<=||f||. Since integral_R A^-1 dx=2pi<8, this proves
L1 convergence of g and UNIFORM convergence of their Fourier transforms
on the real frequency axis. Moreover |Omega(x)|<=8+log(1+|x|), and

    int_R |Omega(x)|/(x^2+1/4)dx<76.                       (ED5)

One elementary proof of the Omega bound uses its increasing digamma
partial-fraction series, Omega(0)>-8, and the Euler--Maclaurin estimate
|digamma(z)-log z|<=1/Re z at Re z=1/4. For ED5, the constant 8 costs
16pi<64. Bound the remaining logarithm by 1 on |x|<=1 (cost <8), and
by 1+log|x| outside (cost 2 integral_1^infinity(1+log x)/x^2 dx=4).
Thus |G(f_r)-G(f)|<76 epsilon_r.

The trace-class source bound gives

    |Q(f_r)-Q(f)|
      <=||Gamma_0||(||f_r||+||f||)epsilon_r<epsilon_r.       (ED6)

No positivity of Gamma_0 is used.

## 3. The exact endpoint defect in the full prime sum

Subtract ED2 for f from ED2 for f_r, retaining R_(f_r)(0)=0 and R_f(0)^2=1/e.
Then exactly

    P(f_r)-P(f)+2pi/e
       =[G(f_r)-G(f)]/2-2pi[Q(f_r)-Q(f)].                 (ED7)

Consequently

    |P(f_r)-P(f)+2pi/e|<46 epsilon_r,
    lim_(r->infinity) P(f_r)=P(f)-2pi/e.                   (ED8)

Every individual prime-power summand converges to the corresponding
summand for f, by ED4. The SUM converges to a DIFFERENT value. The missing
mass is exactly the endpoint term; it cannot be hidden in an unspecified
uniformity error. There is no contradiction with dominated convergence:
no summable domination uniform in r has been proved or is valid here.

Let P_>X(h) mean the entire tail over prime powers n>X. For every fixed
integer X, its finite complementary sum converges. Hence

    lim_r P_>X(f_r)=P_>X(f)-2pi/e,
    lim_(X->infinity) lim_(r->infinity) P_>X(f_r)=-2pi/e.    (ED9)

In the other order the limit is zero, since each fixed-r series converges
absolutely. ED9 is a signed prime-tail theorem on bounded-norm tests that
converge to a fixed nonzero function. It is not the previous escaping-test
mechanism, and it is not an estimate of the unknown negative part of Gamma_0.

## 4. Explicit finite error budget

For all r>=1 and integers X>=2 the following bound is valid:

    |P_>X(f_r)+2pi/e|
      <=64(log X+3)/sqrt X
           +[50+16sqrt X log X]epsilon_r.                 (ED10)

Here is a complete tail proof. Shift the Fourier contour for ED3 to x-i.
Since

    |(x-i)^2+5/4|>=x^2+1/4,
    Re[(x-i)^2+5/4]=x^2+1/4,

we have int_R |g_f(x-i)|dx<=16sqrt(pi)<32, and therefore
|ghat_f(ell)|<=32exp(-ell) for ell>=0. The polynomial denominator has no
pole in the intervening strip and the Gaussian pays its vertical ends.
Integral comparison with Lambda(n)<=log n gives

    sum_(n>X) Lambda(n)n^(-3/2)
      <=X^-1/2(2log X+4+2log2)
      <2X^-1/2(log X+3).

This proves |P_>X(f)|<64(log X+3)/sqrt X. For the finite complementary sum,
ED4 gives Fourier error <8epsilon_r, and the same elementary comparison
gives sum_(n<=X)Lambda(n)/sqrt n<=2sqrt X log X. Its error is at most
16sqrt X log X epsilon_r. Combine these bounds with ED7/ED8; replacing
46 by 50 yields ED10. No zero census, PNT error, or sum of unknown residues
is input to this estimate.

For a concrete rational sufficient test, choose X=10^8. Using log10<3,

    |P_>10^8(f_r)+2pi/e|
       <108/625+3,840,050 epsilon_r.                       (ED11)

Thus any r for which the exact ED1 enclosure proves epsilon_r<=10^-7
satisfies P_>10^8(f_r)<-1, because the right side of ED11 is below one
and 2pi/e>2. Existence of such r is proved by QC1; this pass does NOT
claim to have computed that r or evaluated this huge prime sum. The statement
is a computable sufficient condition, not an executed large certificate.

## 5. Bilinear matrix form of the same limit

Fix a finite real packet f_i(t)=exp(-p_i t)1_[a,infinity)(t), p_i>0, a>0.
Use any predetermined d_r/r^2->1/(2a) and project each f_i to E_(r+2,d_r).
Define the prime matrix by g_ij=R_i(x^2+1/4)R_j(x^2+1/4) and the same Fourier
sum. The estimates in Section 2 polarize, and the direct limiting explicit
formula applies because all poles are outside the critical strip.
With b_i=exp(-a p_i)/p_i,

    lim_X lim_r [P_>X(f_(r,i),f_(r,j))]_(ij)
                      =-2pi b b^t.                       (ED12)

Convergence here is entrywise and therefore in every finite-dimensional
matrix norm. The correction has rank one, is negative semidefinite, and
vanishes on coefficient vectors orthogonal to b. It is NOT negative definite
on all signed combinations. There is no assertion uniform in an unbounded
packet size, or in arbitrary simultaneous X=X_r limits.

## 6. Where the final sign still stands

ED7 removes a concrete missing arithmetic term from an attempted limit
argument. It does not make the limiting full form positive. After restoring
the endpoint, the remaining expression is exactly <f,Gamma_0 f>, and arbitrary
signed packets remain the RH-bearing inequality. ED12 by itself pays nothing
on the b-orthogonal coefficient subspace. The correct finite-source target
on the square-width schedule is still QC17, not the sign of the endpoint
defect or of individual real-exponential tests.

The complete finite geometric and constant checks are recorded separately.
No actual infinite prime sum or actual high-order xi matrix was evaluated.
