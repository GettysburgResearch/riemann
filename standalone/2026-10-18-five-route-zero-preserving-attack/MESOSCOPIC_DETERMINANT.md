# Mesoscopic mass: the same primitive determinant with a much shorter heat window

Status: PROPOSED complete component deductions, awaiting independent review.
No centered prime-error bound or improved zeta strip is proved. The point
is a larger regularization regime with an explicit paid error, not an
identification of positive matrix eigenvalues with Riemann zeros.

Source: #1000, commit 6c4d5309d64978b420c2b897977d6db2ea01ce03,
POSITIVE_DETERMINANT.md. Its matrix construction and exact cyclotomic
identity are credited. The extension below redoes the parameter-uniform
comparison rather than substituting a growing parameter in its c<=1 theorem.

## 1. Preserve the exact integer and its complete matrix

Let P_n be the rational orthogonal projector onto primitive nth Fourier
modes of the n-cycle, L_n=2I-S_n-S_n^T, and

    H_n(t)=I-P_n+P_n(L_n+tI),
    H_N(t)=direct_sum_(2<=n<=N) H_n(t) repeated (N-n) times,
    V_N(t)=(1/2)log det H_N(t).

Every complementary mode has eigenvalue 1; primitive eigenvalues are
 t+4sin^2(pi a/n), gcd(a,n)=1. At zero mass,

    V_N(0)=C(N)=sum_(n<=N)(N-n)Lambda(n)=log A_N,
    A_N=product_(p^j<=N)p^(N-p^j).

Retain ALL prime powers and the complete (N-n) multiplicities. Empty
sums at N=2 have determinant 1. For N>=3 the matrices are nonempty.

Set

    f(u)=log[sinh(u/2)/(u/2)],
    F(v)=integral_0^1(1-y)f(vy)dy,
    B(b)=sum_(m>=1)mu(m)F(b/m)/m.                       (1)

For b>=0 this is an absolutely convergent explicit series, with tail
at m>K at most b^2/(576K^2). It also has the positive representation

    B(b)=sum_(a>=1)phi(a)/a
         integral_0^1(1-y)log[1+(by/(2pi a))^2]dy.       (2)

These are the same functions as in #1000, not a new counterterm.

## 2. Uniform comparison for EVERY mass, with the correct parameter

### Theorem D1

For every N>=2 and every b>=0,

 |V_N(2(cosh(b/N)-1))-C(N)-N^2 B(b)|
     <=b^2 [H_N^harm/72+1/(24N)+1/576],               (3)

where H_N^harm=sum_(m<=N)1/m. Equivalently, for EVERY t>=0, let

    b_N(t)=N arcosh(1+t/2).

Then (3) holds with V_N(t) and b=b_N(t). In particular the matrix can
have rational mass t while the EXACT counterterm uses b_N(t).

Proof. The full cyclotomic divisor identity gives, with h=b/N,

 V_N(2(cosh h-1))-C(N)
   =sum_(n=2)^N (N-n)sum_(d|n)mu(n/d)f(hd).             (4)

For each m let g_m(x)=(N-mx)f(bx/N) on [0,N/m], extended by zero
elsewhere. Including the endpoint jump of g_m',

    total_variation(dg_m')<=4m f(b/m)<=b^2/(6m).

Indeed f(0)=f'(0)=0, f',f''>=0, and f(u)<=u^2/24 for ALL u>=0,
by the positive sinh product. The two interior absolute contributions
have integrals 2m f(b/m) and m f(b/m); the endpoint contributes the
fourth m f(b/m). The Bernoulli second-variation quadrature inequality
therefore gives

    |sum_(d in Z)g_m(d)-integral_R g_m|<=b^2/(72m).

Its integral is N^2 F(b/m)/m. Summing with |mu(m)|<=1, paying the
entire m>N tail from (1), and subtracting the UNIT contribution
(N-1)f(b/N)<=b^2/(24N), proves (3). No estimate used b<=1. QED.

The old rational-mass formula replaced b=2N asinh(c/(2N)) by c and
paid a c^4 error. That replacement is unnecessary. Retaining the actual
b_N(t) removes that extra cost and permits a growing regularizer.

## 3. A better-conditioned exact target for ANY candidate strip

Fix 1/2<=theta<1. Set

    c_N=ceil(N^((1+theta)/2)), t_N=c_N^2/N^2,
    b_N=2N asinh(c_N/(2N)).                              (5)

Then t_N is rational, 0<t_N<=1, and N^(theta-1)<=t_N. The actual
matrix condition number satisfies, for N>=3,

    cond(H_N(t_N))<=5/t_N<=5N^(1-theta).                (6)

This follows directly from eigenvalues in [t_N,5]; complementary
unit modes remain. Since b_N<=c_N<=2N^((1+theta)/2), (3) proves

    V_N(t_N)=C(N)+N^2 B(b_N)+O(N^(1+theta)log(2N)).      (7)

All constants here can be chosen absolute. In particular:

* theta=1/2 gives condition number O(N^(1/2));
* theta=5/6 gives condition number O(N^(1/6)).

These are condition-number exponents, NOT zeta zero locations. The second
choice is calibrated to a still-unproved 5/6 height target. The earlier
fixed-c construction had only an O(N^2) condition-number guarantee.

The counterterm is now N-dependent, and must be retained exactly. Its
own sharp large-b asymptotic is NOT assumed. In #1000 its Mellin transform
already has target-related poles at rho-1; approximating it by its leading
linear term without a paid error would merely conceal the zeta problem.

### One-sided consumer at the candidate boundary

If, in addition to these proved component identities, one establishes

    V_N(t_N)<=(N-1)^2/2+N^2B(b_N)
                       +O_epsilon(N^(1+theta+epsilon)) (OPEN-D)

for every epsilon>0 and all integers N, then zeta has no nontrivial
zero with real part >theta. This is not an estimate supplied by (7).

To see the implication, transfer (OPEN-D) back to the fixed C(N) using
(7), choosing the harmless logarithmic loss within epsilon. Write
E(x)=C(x)-(x-1)^2/2. Interpolation between consecutive integers changes
an upper bound by at most 1/8. Its Mellin transform is

    integral_1^infinity E(x)x^(-s-2)dx
       =[-zeta'/zeta(s)-1/(s-1)]/[s(s+1)], Re s>1.       (8)

At a nontrivial zero rho its residue is -m_rho/[rho(rho+1)], nonzero.
The expression has no singularity at a real s>0, except the already
removed pole at one. The Landau positivity argument applied to
Kx^(1+theta+epsilon)-E(x), made nonnegative beyond a finite x_0, forces
its convergence abscissa to be at most theta+epsilon: otherwise there
would be a singularity at a real point where (8) continues analytically.
Thus (8) is holomorphic in Re s>theta+epsilon. Its zero residues exclude
zeros there, and epsilon is chosen separately for each point. This is
the same classical one-sided mechanism as #1000, with theta in place
of 1/2. No moving-parameter Mellin transform was used; transfer to the
fixed C occurred FIRST.

### The conditioning gain has a bulk-subtraction tradeoff

The larger mass does NOT make all parts of the problem smaller. In fact

    B(b)/b -> 1/[12 zeta(2)] as b tends to infinity.    (8a)

To prove this without an RH input, note that f(u)/u tends to 1/2 and
0<=f(u)<=u/2. Dominated convergence in the integral gives F(v)/v ->1/12.
In B(b)/b the m-th summand is mu(m)m^(-2)F(b/m)/(b/m), bounded by
1/(12m^2). The absolutely convergent sum gives (8a), using the Euler
identity sum mu(m)/m^2=1/zeta(2).

Thus N^2 B(b_N) has size N^((5+theta)/2), larger than the desired N^2
prime main term. The useful condition-number/heat-window improvement comes
with subtraction of this explicitly defined larger bulk. Its leading
linear asymptotic alone has NOT been shown accurate enough for OPEN-D.
The full B must remain with a controlled evaluation tail; no efficient
large-N algorithm or automatic cancellation of the centered trace is
claimed. This is a tradeoff, not a removal of the arithmetic difficulty.

## 4. The entire long-time heat tail is now inexpensive

Let D_N be the matrix dimension; D_N<=N^3/6. Frullani's identity for
each positive eigenvalue gives

 V_N(t)=(1/2) integral_0^infinity
              [D_N exp(-u)-Tr exp(-uH_N(t))] du/u.       (9)

For 0<t<=1 and T>0 the absolute tail after T is at most

    D_N exp(-tT)/(tT).                                  (10)

Indeed every eigenvalue is at least t; the two positive trace majorants
are at most 2D_N exp(-tu), and integrate 1/u<=1/T.
Taking T=K log N/t_N gives a tail at most

    N^(3-K)/[6K log N],
    T<=K N^(1-theta)log N.                              (11)

For the theta=5/6 target only heat times up to O(N^(1/6)log N) are
needed, with a completely paid inverse-power long-time tail. This is a
real reduction in the spectral window compared with the old small mass.
It is NOT an estimate for the short-time centered trace in (9).

An effective reference operator would still need to match the large
bulk term and leave a signed trace difference that can be bounded at
N^(1+theta+epsilon). The identity reference in (9) proves the formula
but does not accomplish that task. No such arithmetic reference bound
is claimed in this packet.

## 5. Verification boundary

The new checker uses exact cycle/determinant polynomials and directed
rational log, square-root and arctangent enclosures. It evaluates B(b)
using the POSITIVE formula (2), including its entire positive tail;
this is a different finite evaluation of B from #1000's small-c
Bernoulli expansion. Cases have c>1 as well as rational t<=1. These
finite comparisons check the new parameter handling, not the proof for
all N or the missing centered height bound.
