# Price a below-diagonal moment in the simplified quasi-RH architecture

Status: proposed conditional adapter; the new moment input below is OPEN.
Scope: the literal ideal Mobius/sextic family of the frozen October 5 paper,
for each fixed finite-order Hecke character and every fixed smooth profile.
RH remains open. This deduction does not assert a new source moment bound.
Exact source: OpenAI `math` commit
`fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`, `qrh11-12.tex`, especially
the family and prime-sixth extraction at source lines 215--276. The paper's
proved mean square has H=D^(1+vartheta), vartheta>0; it cannot be evaluated
below D by changing a parameter without a new proof.
What ran: the accompanying exact rational pricing checker. It checks the
scalar adapter, not the arithmetic estimate or any L-function theorem.
Smallest remaining gap: a source-faithful mean-square estimate below the
row/column diagonal with penalty exponent strictly less than one half.

## 1. Keep the actual family and state the unpaid input

Let K=Q(sqrt(-3)). S contains the ideal primes above 2 and 3 and those
dividing the fixed conductor of nu. All columns are nonzero integral ideals
coprime to S, counted once, using their unique primary generator. Write

    A_u(D)=sum_n mu_K(n) nu(n) chi_n(u) W(Nn/D),

where W belongs to C_c^infinity((0,infinity);C), nu is fixed and finite order,
and chi_n is the actual sextic symbol extended by zero at common factors.
Rows are nonzero elements u in O_K, with their actual unit multiplicities.

**OPEN-RMS(kappa,h).** For a fixed 0<=kappa<=1/2 and 0<h<1, every such
nu,W and every epsilon>0 satisfy, for every D>=2 and H=D^h,

    sum_{0<Nu<=H} |A_u(D)|^2
        <<_{nu,W,h,kappa,epsilon} D^(1+epsilon) H (D/H)^kappa.       (R1)

The requirement covers all fixed smooth profiles. It is neither an
arbitrary-coefficient large sieve nor a growing-conductor or height-uniform
claim. The coefficient mu_K nu and the sextic symbols may not be replaced.

## 2. Prime-sixth replicas pay the exact two costs

Put Y=H^(1/6). For each primary prime p, Y/2<Np<=Y, outside the fixed S,
the literal identity chi_n(p^6)=1_{p does not divide n} gives

    A_(p^6)(D)=A_1(D)+O_W(D/Y).                                  (R2)

Indeed only multiples of p differ; their number in the fixed norm support
is O_W(D/Np), and both coefficient moduli are at most one. The prime ideal
theorem supplies asymptotically Y/logY distinct primary primes. Their sixth
powers are distinct nonzero rows with norm at most H. Fixed excluded primes
affect only finitely many choices. Summing the square triangle inequality
over these rows and applying (R1) yields

    |A_1(D)|^2 << D^(1+kappa+epsilon) H^(5/6-kappa)
                         +D^2 H^(-1/3).                         (R3)

Absorb the prime logarithm into epsilon, with h fixed. The resulting
summatory exponent is

    theta(kappa,h)=max((1+kappa+h*(5/6-kappa))/2, 1-h/6).          (R4)

The first function increases and the second decreases in h throughout
0<=kappa<=1/2. Their unique intersection gives the exact optimum

    h*=6(1-kappa)/(7-6kappa),
    theta*=(6-5kappa)/(7-6kappa).                                 (R5)

In particular an RMS penalty kappa=2/5 at h=18/23 would give the strict
zero-free half-plane Re(s)>20/23=0.86956521739..., conditional on R1.
The boundary kappa=1/2 gives 7/8; every smaller kappa gives a smaller bound.
Even an unpenalized below-diagonal moment (kappa=0) stops at 6/7 in this
prime-sixth extraction. This adapter alone cannot reach the critical line.

## 3. Direct smooth Mellin continuation retains every zero height

Suppose R3 gives A_1(D)<<D^(theta+epsilon) for every fixed W and epsilon.
For Re(s)>1, absolute interchange and D=Nn/t give

    integral_0^infinity A_1(D) D^(-s-1) dD
      = W_hat(s) C_S(s)/L_K(s,nu),
    W_hat(s)=integral_0^infinity W(t)t^(s-1)dt,
    C_S(s)=product_(p in S)(1-nu(p)(Np)^(-s))^(-1).               (R6)

Conductor-prime factors equal one under the zero extension. Every remaining
finite Euler factor is holomorphic and nonzero in Re(s)>0. The left side
is holomorphic in Re(s)>theta: it vanishes for sufficiently small D because
W has compact support away from zero, and its large-D integral converges
locally uniformly after choosing epsilon below the compact real-part gap.

If L_K had a zero rho with Re(rho)>theta, choose a nonnegative smooth
profile supported in a sufficiently narrow positive interval that
|Im(rho)*log(t/t0)|<pi/3 there. After a fixed phase rotation, the real part
of W_hat(rho) is strictly positive. Thus the right side of R6 has a
nonremovable pole at rho, contradicting the left side's holomorphy. This
argument handles any finite zero height and any multiplicity; it requires
no uniformity as rho or W varies. Principal poles create reciprocal zeros
and do not obstruct the adapter.

For the trivial nu, L_K(s,1)=zeta(s)L(s,chi_-3); hence its zero-free
half-plane implies the same for zeta. More generally the norm pullback of
a fixed Dirichlet character has L_K equal to the corresponding two
Dirichlet factors, up to nonvanishing finite local factors. Each remains
within the explicitly fixed finite-order arithmetic class.

## 4. Source barrier and a mechanism to investigate

The frozen proof's positive dual energy starts with dual height approximately
D^2/H. When H<D and the cube divisor is small, the required positive gap
between this dual height and the canonical width reverses. The cube-divisor
cutoff falls below one and leaves a same-scale child, so its contraction
argument cannot simply be reused. The completed dual diagonal bound by
itself gives a below-diagonal penalty of size D/H, not R1 with kappa<1/2.

There is a possible source-specific improvement before that positive
majorant: retain the signed mu(f) in the initial Poisson sum. The exact
divisor identity

    sum_(f|c) mu(f) 1_{(c/f,k)=1}=mu(c) 1_{c|k}

holds for squarefree c and collapses its artificial diagonal. A separately
reviewed source derivation is needed to bind its original normalizations;
off-diagonal terms remain unpaid. This identity neither proves R1 nor
permits a generic coefficient replacement. It identifies a precise place
where source signs may have been lost by a nonnegative energy bound.
