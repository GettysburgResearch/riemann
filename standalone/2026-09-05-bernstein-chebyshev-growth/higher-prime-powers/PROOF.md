# Higher prime powers have only one boundary term and a finite-energy remainder

Status: PROPOSED complete analytic proofs; independent review required.
The all-epsilon inequality for the original coefficients and RH remain unproved.
Scope: the literal von Mangoldt source; every integer degree N >= 1; the
parent's fixed scale v=2 and s(w)=(2-w)/(1+w). No fitted or moving scale.
Exact parent: PR #792 at a895f734fc4243dbe81e1a0c5a17cf978a744962,
`standalone/2026-09-05-bernstein-chebyshev-growth/arithmetic-laguerre/PROOF.md`.
What was run: finite exact algebra in `verify_exact.py`; see VALIDATION.md.
Smallest remaining gap: a subexponential estimate for the prime-only sequence
Pcal_N in Section 5. No such estimate is proved here.
Local labels HP-1 through HP-6 apply only to this directory.

## 1. Statement and exact arithmetic conventions

Write L_N=L_N^(0) for the ordinary Laguerre polynomial and retain

    L_N^(-1)(t)=L_N(t)-L_(N-1)(t),     N>=1.

The parent's complete prime-power sum and discrepancy are

    P_N = sum_(p prime) sum_(r>=1)
              (log p)/p^(2r) L_N^(-1)(3r log p),
    I_N = (-1)^N 3*2^(N-1),
    E_N = P_N-I_N.

Each is an absolutely convergent sum at every fixed finite degree. The
higher-power portion is the LITERAL subseries

    Q_N = sum_p sum_(r>=2) (log p)/p^(2r) L_N^(-1)(3r log p).

The coefficient at p^r is log p, not r log p. In particular no prime-power
multiplicity is discarded by replacing the n notation with (p,r).

**HP-1 (higher-power finite-energy theorem).** There is a real sequence
q=(q_N)_(N>=1) in l^2 such that

    Q_N = (2/3)(-1)^N + q_N,                       every N>=1.  (1)

More explicitly, let theta(x)=sum_(p<=x) log p, Delta_theta(x)=theta(x)-x, and

    K^2 = 6 integral_1^infinity |Delta_theta(x)|^2 dx/x^3,
    C3  = sum_p (log p) p^(-3/2)/(1-p^(-1/2)).

Then K is finite by the classical quantitative prime number theorem,
C3<20 by an elementary estimate, and

    ||q||_(l^2) <= K+C3.                                      (2)

Consequently Q_N=(2/3)(-1)^N+o(1) and |Q_N|<=2/3+K+C3 uniformly
in N. No rate for o(1), numerical value for K, or pointwise asymptotic
error such as O(1/N) is claimed.

This is an unconditional theorem in the ordinary sense of using the
classical prime number theorem. It uses neither RH nor a verified zero
prefix. Existence of a critical-line zero is used ONLY for HP-6 below.

The stronger assertion that the whole prime residual has finite l^2 energy
is false, even under RH; Section 6 proves the distinction.

## 2. Prime squares: a source-normalized Laguerre estimate

Set

    Q_(2,N)=sum_p (log p)/p^4 L_N^(-1)(6 log p),
    I_(2,N)=integral_1^infinity x^-4 L_N^(-1)(6 log x) dx.

Finite integration of the polynomial gives

    I_(2,N)=(2/3)(-1)^N.                                     (3)

Indeed, with y=log x, each y^j integrates to j!/3^(j+1), so the
binomial sum is -6(3-6)^(N-1)/3^(N+1).

Let phi_n(t)=exp(-t/2)L_n(t). They are orthonormal in L^2(0,infinity),
with integral phi_n phi_m=delta_nm. This is the alpha=0 specialization
of classical Laguerre orthogonality; no completeness assertion is needed
for the Bessel bound used here. Define

    D2(t)=Delta_theta(exp(t/6))/exp(t/6),
    a_n=integral_0^infinity D2(t) phi_n(t) dt.                  (4)

**HP-2 (exact square correction and contraction).**

    Q_(2,N)-(2/3)(-1)^N = (2a_N+a_(N-1))/3,       N>=1,        (5)
    sum_(N>=1) |Q_(2,N)-(2/3)(-1)^N|^2 <= K^2.               (6)

### Proof

The Stieltjes expression for the left side of (5) is

    integral_[1,infinity) x^-4 L_N^(-1)(6 log x) dDelta_theta(x).

The lower boundary term is zero because L_N^(-1)(0)=0 for N>=1,
even though Delta_theta(1)=-1. The upper boundary vanishes because
Delta_theta(x)=O(x log x) already suffices at fixed degree. The exact
identity

    -d/dx [x^-4 L_N^(-1)(6 log x)]
        = x^-5 [4L_N(6 log x)+2L_(N-1)(6 log x)]

follows from (L_N^(-1))'=-L_(N-1). Thus integration by parts and t=6 log x
produce (5), with the factor 1/3 and both signs as displayed.

The imported classical estimate for pi(x)-li(x), followed by ordinary
partial summation, gives

    Delta_theta(x)=O(x/(log x)^2)                  as x->infinity.

Only this weak consequence is needed. To make the input explicit, use
pi(x)-li(x)=O(x exp(-c sqrt(log x))) and

    theta(x)=pi(x)log x-integral_2^x pi(y)dy/y.

The main term has derivative one; its integration constant is harmless.
Multiplication by log x and the integrated error are both absorbed in
O(x/(log x)^2). This proves D2 in L^2, with ||D2||_2=K. For example, an
input |Delta_theta(x)|<=C x/(log x)^2 for x>=x0 gives a squared tail norm
at most 2C^2/(log x0)^3, in addition to the finite initial integral. No
values of C or x0 are newly certified in this packet.

Bessel now gives sum_(n>=0)|a_n|^2<=K^2. The two sequence maps
(a_n)_(n>=0) -> (a_N)_(N>=1) and -> (a_(N-1))_(N>=1) have operator
norm at most one. Their convex combination (2a_N+a_(N-1))/3 therefore
has norm at most K. This proves (6).

For clarity, this is control of the ORIGINAL square contribution, not a
replacement by its continuous average. Formula (5) retains its entire
signed discrepancy from that average.

### The degree-zero endpoint and an analytic form

Although the theorem concerns N>=1, the constant coefficient is not
silently set to zero. If A(z)=sum_(n>=0)a_n z^n, direct integration at N=0
gives Q_(2,0)-1/3=1+(2/3)a_0. Hence, initially near w=0 and then on the disk,

    sum_p (log p)p^(-2s(w)) - 1/(2s(w)-1)
       = 1 + (2-w) A(-w)/3.                                  (7)

The right side belongs to H^2 of the unit disk. Here H^2 means an analytic
function with square-summable Taylor coefficients. Formula (7) is also a
check on the endpoint constant; deleting the leading 1 is incorrect.

## 3. Cubes and higher: exact analytic atom norms

The following identity controls the infinite source without estimating
separate derivatives or summing absolute values of the Laguerre polynomial.
For x>=1 put

    f_x(w)=x^(-s(w)),   s(w)=1/2+(3/2)(1-w)/(1+w).

For tau>=0 the function

    B_tau(w)=exp[-(tau/2)(1-w)/(1+w)]

is analytic on the unit disk, has modulus at most one there, and boundary
modulus one away from w=-1. Its H^2 norm is one. For tau,sigma>=0,

    <B_tau,B_sigma>_(H^2)=exp(-|tau-sigma|/2).                 (8)

One can check these assertions directly: use Parseval on circles r<1,
let r increase to one by dominated convergence, and note that on the unit
circle B_tau times conjugate(B_sigma) equals B_(tau-sigma) if tau>=sigma,
or its conjugate otherwise. Its mean is its real value at zero. No
zero-set or positivity premise about xi enters this argument.

Since f_x=x^(-1/2)B_(3 log x), (8) proves

    <f_x,f_y>_(H^2) = min(x,y)/max(x,y)^2.                     (9)

Subtracting the constant coefficients f_x(0)=x^-2 gives the positive kernel

    K0(x,y) = min(x,y)/max(x,y)^2 - 1/(x^2 y^2)
            = [min(x,y)^3-1]/(x^2 y^2)
            = integral_1^infinity
                  1_(u<=x^3) 1_(u<=y^3) du/(x^2 y^2).        (10)

**HP-3 (finite-source Gram identity).** For arbitrary complex weights
c_j and x_j>=1, if F(w)=sum_j c_j f_(x_j)(w)=sum_N F_N w^N, then

    sum_(N>=1)|F_N|^2
      =sum_(i,j)c_i conjugate(c_j) K0(x_i,x_j)
      =integral_1^infinity |sum_(j:x_j^3>=u)c_j/x_j^2|^2 du.   (11)

All three expressions retain cross terms. The rational kernel at rational
x_j admits exact finite replay even though the original coefficients
contain logarithms. Replacing those logarithms by arbitrary rational
weights is used only for algebraic test fixtures, never as prime data.

**HP-4 (the entire exponent-at-least-three source is in H^2).** The actual
series

    C(w)=sum_p sum_(r>=3)(log p) p^(-r s(w))

converges in H^2, since

    sum_p sum_(r>=3)(log p)||f_(p^r)||_(H^2) = C3 < infinity.

Its nonconstant coefficients are (-1)^N Q_(>=3,N), where
Q_(>=3,N) is the literal r>=3 part of Q_N. Thus

    ||(Q_(>=3,N))_(N>=1)||_(l^2) <= C3.                       (12)

The H^2 sum agrees with the original Dirichlet series on the disk: the
latter is normally convergent for Re s>1/3, and every compact disk maps
strictly inside Re s>1/2. The coefficient identity follows from the finite
Laguerre generating identity and continuity of coefficient evaluation.
There is no interchange of a conditionally convergent arithmetic series.

For a simple numerical ceiling not depending on primes, bound

    C3 <= [1/(1-2^(-1/2))] sum_(n>=2)(log n)n^(-3/2) < 20.

The factor in brackets is below 4. The summand is decreasing for x>=2
because log 2>2/3, and its sum is at most

    (log 2)/(2sqrt 2) + 2(log 2+2)/sqrt 2 < 5.

Use log 2<1 and sqrt 2>7/5 for the last strict bound. The lower inequality
log 2>2/3 follows by strict Jensen applied to 1/x on [1,2].

Adding (6) and (12) proves HP-1, including the l^2 bound (2).

### A false termwise continuum shortcut

For a fixed exponent r>=2 the continuum moment is

    I_(r,N)=integral_1^infinity x^(-2r)L_N^(-1)(3r log x)dx
           =(-1)^N [3r/(2r-1)^2]
                      [(r+1)/(2r-1)]^(N-1).                  (13)

For EACH fixed N>=1 all these moments have the same sign, and

    |I_(r,N)| >= [3/(4r)] 2^(-(N-1)).

Therefore sum_(r>=3) I_(r,N) diverges. The actual prime-power sum does not.
Approximating every power separately by an integral starting at x=1 and
then summing the main terms would be invalid. We subtract the square
continuum ONLY, and retain cubes and higher as a single convergent source.

## 4. What the theorem says in generating-function language

The full higher-power Dirichlet series

    Q(s)=sum_p sum_(r>=2)(log p)p^(-rs)

is normally convergent for Re s>1/2. HP-1, with its finite degree-zero
coefficient, is equivalent to

    Q(s(w)) = (1+w)/(3(1-w)) + R(w),       R in H^2.           (14)

The rational term is exactly 1/(2s(w)-1); it arises from the square
continuum. R is the sum of the square error (7) and C(w). In particular
this statement proves a specific source-defined boundary regularity,
not merely absence of interior poles.

The l^2 norm controls both signs of the real coefficient sequence. It does
not assert that its entries are nonnegative, eventually have one sign,
or obey an effective decay rate. In particular it is not a statement
about the signs of the unresolved r=1 source.

## 5. Return to the original c_N(2) without losing the completed terms

Define the PRIME-ONLY corrected coefficient

    Pcal_N = (-1)^N sum_p (log p)/p^2 L_N^(-1)(3 log p)
               -3*2^(N-1)+2/3,                    N>=1.      (15)

All sums are defined from ordinary primes and converge at fixed degree.
The parent's exact normalization is

    d_N = A_N -(3/8)(-1)^N E_N,
    A_N = (-1)^N(9/32) sum_(ell>=2) ell^-2
                                  (1-3/(2ell))^(N-1).

Its AL-3 estimate gives A in l^2; explicitly A_N=O(1/N). Substituting
HP-1, with all signs retained, gives the exact statement

**HP-5 (prime-only source modulo a finite-energy remainder).**

    d_N = -(3/8)Pcal_N + r_N,                                (16)
    r_N = A_N -(3/8)(-1)^N q_N,
    ||r||_(l^2) <= ||A||_(l^2) +(3/8)(K+C3).                  (17)

The parent's polynomial-cost return remains

    |c_N(2)| <= (8/9)sqrt(2N+1) max_(0<=j<=N)|d_j|.           (18)

Thus all higher prime powers and the entire archimedean contribution have
been controlled independently of degree. The remaining all-epsilon bound
can be placed on Pcal_N alone. Conversely RH gives bounded d_N by its
positive spectral Chebyshev representation, and hence bounded Pcal_N by
(16). Consequently

    RH <=> Pcal_N is bounded
       <=> Pcal_N has the all-epsilon subexponential upper bound.  (19)

The equivalences follow from the parent's complete endpoint proof; they
are NOT a proof of any one condition in (19). No new criterion is claimed
as an external novelty. The substantive additional result is the proved
finite-energy estimate (1)--(2) for a literal infinite arithmetic subsource.

The condition still required is

    for every epsilon>0 there is C_epsilon<infinity such that
    |Pcal_N| <= C_epsilon exp(epsilon N), every N>=1.           (20)

This pass does not obtain (20).

## 6. The attempted Hilbert-space extension fails for a precise reason

After HP-1 it is natural to try the same Bessel estimate on the remaining
prime source. It does NOT just leave an unverified constant. The needed
square-integrability condition is false.

**HP-6 (critical-line boundary energy cannot be removed).** Neither
(d_N)_(N>=1) nor (Pcal_N)_(N>=1) belongs to l^2. Moreover

    integral_1^infinity
       |theta(x)-x+sqrt x|^2 dx/x^2 = infinity.                (21)

These assertions are unconditional and compatible with RH. They do not
contradict boundedness or subexponential growth of the sequences.

### Coefficient proof, retaining multiplicity

The parent's exact generating function is

    D(w)=sum_(N>=0)d_Nw^N
        =d_0/2+(3/8)(xi'/xi)(s(w)).                          (22)

Use the classical existence of a nontrivial critical-line zero
rho0=1/2+i gamma0, gamma0!=0, of some finite multiplicity m>=1. This input
is imported; no numerical zero computation is needed. Put

    w0=(2-rho0)/(1+rho0).

Then |w0|=1, w0!=-1, s'(w0)=-3/(1+w0)^2, and the meromorphic function
on the right of (22) has the nonzero residue

    Res_(w=w0) D(w) = -m(1+w0)^2/8.                           (23)

Suppose d were in l^2. The left of (22) would be analytic on the whole
disk and, by the identity theorem for meromorphic functions, agree there
with the right side. Any interior pole would already be a contradiction.
Near w0 there is a punctured neighborhood containing no other poles, so
along rw0 as r increases to 1 the right side grows like a nonzero constant
times (1-r)^(-1). On the other hand Cauchy--Schwarz gives

    |D(rw0)| <= ||(d_N)_(N>=0)||_2 / sqrt(1-r^2).

This is impossible. Thus d is not in l^2. Formula (16) and r in l^2 then
imply that Pcal is not in l^2 either. Simplicity is not assumed. Removing
finitely many boundary poles cannot fix this class of norm: infinitely
many critical-line zeros remain by Hardy's classical theorem.

### Source proof of (21)

For t>=0 set

    D1(t)=[theta(exp(t/3))-exp(t/3)]/exp(t/6).

The same integration by parts as in Section 2, now at exponent r=1,
gives, for every fixed N>=1,

    E_(prime,N)=(1/3)integral_0^infinity
                         D1(t)[2phi_N(t)+phi_(N-1)(t)]dt,

where E_(prime,N) is the prime-only sum minus I_N. The integrals converge
at fixed degree under theta(x)=O(x log x); this is NOT an L^2 assertion.
Also the elementary Laplace integral of Laguerre gives

    integral_0^infinity phi_n(t)dt=2(-1)^n.

Therefore (15) has the exact source form

    Pcal_N = [(-1)^N/3] integral_0^infinity
                       [D1(t)+1][2phi_N(t)+phi_(N-1)(t)]dt.   (24)

If D1+1 were in L^2, the same Bessel/contraction argument as HP-2 would
put Pcal in l^2, contradicting the coefficient proof. Finally

    ||D1+1||_2^2
      =3 integral_1^infinity |theta(x)-x+sqrt x|^2 dx/x^2.

This proves (21). The +sqrt x correction has ALREADY removed the elementary
square bias; the obstruction is not cured by inserting that correction.

## 7. Disposition of the proof attempt

The positive result is global in degree: all prime powers of exponent at
least two contribute exactly (2/3)(-1)^N plus a finite-energy error. The
archimedean terms are also in l^2. The prime-only centered source is now
isolated by an exact equality modulo l^2, with no missing power or main term.

The attempted extension was:

    classical PNT -> square-source L^2 -> Laguerre Bessel bound
       -> attempt the same L^2 bound for the remaining prime source.

The first arrow is proved and sufficient for the higher-power theorem.
The final arrow is refuted by HP-6, including after the square correction.
An argument for (20) must allow the actual boundary poles and their
non-square-summable oscillatory coefficients, while excluding poles inside
the disk. H^2 is the wrong class for the entire source. Bounded coefficients
or a suitable weaker growth estimate remain possible; no source estimate
of that strength is established here.

This is not a new zero-free region, critical-line proportion, zero census,
or completed proof of RH. Passing finite checks does not change that status.

## References and exact trust boundary

1. Parent arithmetic proof AL-1--AL-7 at the commit/path in the header.
   Original GROWTH.md at 81e336a6d62d0963216ae05f809ec4df05447eb8 supplies
   the precise all-epsilon endpoint and spectral Chebyshev convention.
2. NIST DLMF, Table 18.3.1 (Laguerre orthogonality, alpha=0):
   https://dlmf.nist.gov/18.3
3. NIST DLMF 18.12.13 (Laguerre generating function), and its polynomial
   specialization/limit at alpha=-1:
   https://dlmf.nist.gov/18.12
4. NIST DLMF 27.12.5 (classical quantitative PNT):
   https://dlmf.nist.gov/27.12#E5
   Only the derived theta error O(x/log^2 x) is used in HP-1/HP-2.
5. NIST DLMF 25.10(i), including the infinitely-many critical-line zeros
   statement following equation 25.10.2:
   https://dlmf.nist.gov/25.10
   This classical input is used only in HP-6.

All consulted external material was HTML/MathML; no PDF was analyzed.
Classical Hardy-space Parseval, Laguerre and PNT tools are credited rather
than claimed as new. No external priority claim is made for their present
combination. This packet has not received an independent mathematical
review or a Lean formalization.
