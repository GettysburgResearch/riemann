# Positive boundary energy: a checked alternative, not an RH completion

Date: 2026-09-07. Author continuation of PR #803.
Parent: d1a45dba9c028f52c0f1cdb2c1bc0b2c0d2652c4.
Status: complete proposed COMPONENT arguments; independent review required.
**The requested complete proof of RH has NOT been obtained.**

This pass tests the alternative of minimizing a genuinely positive boundary
energy, rather than the signed functional whose completion Hessian the parent
already proved has rank one. It identifies the complete arithmetic norm,
its exact periodic representation, and the cost imposed by any hypothetical
off-line zero. These are not a proof that the positive norm is small.

The Hardy point-evaluation mechanism is classical Nyman--Beurling mathematics.
PR #804 already uses its delayed version for a different, integrated source
and target 1/s^2. Here the target is 1/s and the source is exactly the finite
completion class in #803. No novelty is claimed for the general mechanism.
The two finite certificates below test this normalization, not any global sign.

## 1. Literal coefficients and the actual positive norm

Let Y>=2 be an integer and let p(s)=sum_(n<=N) a_n n^(-s) be a finite REAL
Dirichlet polynomial with

    a_n=mu(n) for n<Y,             sum_n a_n/n=p(1)=0.       (1)

The additional condition p'(1)=1 is used by the annular contour construction,
but is not needed in the norm and interpolation theorems below. Define

    A_p(x)=sum_n a_n floor(x/n),
    u_p(x)=1-A_p(x),                       x>=1,
    E(p)=integral_1^infinity |u_p(x)|^2 dx/x^2.              (2)

The arithmetic divisor identity gives A_p(x)=1 for 1<=x<Y. The endpoint Y
need not agree; it has measure zero. Balance gives

    A_p(x)=-sum_n a_n {x/n},
    |u_p(x)|<=1+sum_n |a_n|=:B_p.                          (3)

Consequently

    0<E(p)<=B_p^2/Y<infinity.                              (4)

Strictness is justified in section 4; no zero theorem is used to establish
finiteness. Every floor term, including nonsquarefree correction indices,
is retained.

For Re s>1, absolute convergence and the integral of a floor give

    integral_1^infinity u_p(x)x^(-s-1)dx
         =[1-zeta(s)p(s)]/s.                              (5)

The left side is analytic for Re s>0 by (3), and the apparent pole at s=1
on the right is removed by p(1)=0. The identity theorem extends (5) to
Re s>0. This argument uses no zero-free region.

Put t=log x, L=log Y and

    r_p(t)=exp(-t/2)u_p(exp t),                 t>=0.

Then r_p is in L2, vanishes a.e. on [0,L), and its Laplace transform is

    R_p(z)=[1-zeta(z+1/2)p(z+1/2)]/(z+1/2),  Re z>0.       (6)

Fourier Plancherel, with transform integral exp(-itw)r(t)dt and inverse
factor 1/(2pi), therefore proves the EXACT positive boundary identity

    E(p)=(1/(2pi))integral_R
            |1-zeta(1/2+it)p(1/2+it)|^2/(1/4+t^2)dt.      (7)

This is a modulus square. It is not the parent's signed integral containing
p(s)^2, and no equality between those two functionals is asserted.

### 1.1 The unconditional upper bound actually obtained

For the parent's distinguished bounded two-block completion p_Y, its explicit
coefficients are the Mobius prefix and corrections a*n/Y at Y<=n<2Y and
2b*n/Y at index 2n, with |a|<6, |b|<5. Thus

    sum |p_Y[n]| < (Y-1)+(3Y-1)(|a|+2|b|)/2 <25Y-9.

Equations (3)--(4) give the honest all-Y upper bound

    E(p_Y)<625Y.                                         (8)

The prefix, jet and coefficient bounds are imported from the pinned BMC
paper. No subpower improvement to (8) is supplied here. In particular the
coefficient estimate sum |p_Y[n]|^2/n=O(log Y) is NOT a bound for (7).

## 2. What one hypothetical zero forces, for EVERY completion

Suppose rho=beta+i gamma is a nontrivial zero with beta>1/2. Put

    z0=rho-1/2,              a=Re z0=beta-1/2>0.

Since p is an entire finite polynomial, (6) gives R_p(z0)=1/rho. Applying
Cauchy--Schwarz on the actual delayed support, not on the whole half-line,

    1/|rho|^2
       <= E(p) integral_L^infinity exp(-2at)dt
       = E(p) exp(-2aL)/(2a).

Hence, simultaneously for ALL finite completions satisfying (1),

    E(p)>=(2beta-1)Y^(2beta-1)/|rho|^2.                    (9)

This is conditional on the hypothetical zero, not a statement that one
exists. No simplicity, rightmost-zero, ordinate-independence or finite
zero-verification assumption is used. The denominator is |rho|^2, because
our target is 1/s; the corresponding #804 target is 1/s^2 and has |rho|^4.
The formula is not continued to a=0: boundary point evaluation there does
not have this finite norm.

It follows directly that the following UNPROVED construction would imply RH:
there exist integers Y_j tending to infinity and completions p_j satisfying
(1) such that

    log(1+E(p_j))/log Y_j -> 0.                            (10)

Any one right-of-line zero contradicts (9); reflection handles the left.
Only an unbounded subsequence is needed for this sufficient implication.
No converse or unconditional existence assertion is being smuggled into (10).
This is a classical approximation-type sufficient condition, not evidence
that it is easier than the signed-count target.

## 3. Multiplicities and finite simultaneous constraints

For clarity the exact finite interpolation cost is also given. Shift the
actual function, g_p(t)=r_p(t+L), and write G_p(z)=exp(Lz)R_p(z). Its norm
is still E(p). If rho has multiplicity q, then, for 0<=k<q,

    G_p^(k)(z0)= [d^k/dz^k (exp(Lz)/(z+1/2))]_(z=z0).
                                                               (11)

Define the polynomials in L

    b_k(L)=sum_(ell=0)^k binom(k,ell)L^(k-ell)
                       (-1)^ell ell!/rho^(ell+1),
    P_j(L)=sum_(k=0)^j binom(j,k)(2a)^k b_k(L)/k!.         (12)

The functions

    e_j(t)=sqrt(2a)exp(-conj(z0)t)L_j(2at), j>=0,

are orthonormal in L2(0,infinity), with L_j the ordinary Laguerre polynomial.
For example the Laguerre generating functions give
integral_0^infinity exp(-u)sum_j L_j(u)v^j sum_k L_k(u)w^k du
=1/(1-vw) near (0,0), proving the needed orthogonality coefficientwise.
Expanding each L_j and using (11) gives

    <e_j,g_p>=sqrt(2a)exp(Lz0)P_j(L),        0<=j<q.

Bessel's inequality therefore proves

    E(p)>=2a Y^(2a)sum_(j=0)^(q-1)|P_j(log Y)|^2.          (13)

In particular any such family satisfies

    liminf_(Y->infinity) E(p)/(Y^(2a)(log Y)^(2q-2))
       >= (2a)^(2q-1)/[((q-1)!)^2 |rho|^2].              (14)

The leading coefficient follows directly from (12); this is a lower bound,
not a leading asymptotic for the entire arithmetic norm.

For several distinct hypothetical zeros rho_i with z_i=rho_i-1/2 in the
right half-plane, keep derivative orders 0<=k<q_i. Use the kernels

    k_(i,k)(t)=(-t)^k exp(-conj(z_i)t),
    H_((i,k),(j,l))=(-1)^(k+l)(k+l)!/(z_i+conj(z_j))^(k+l+1),
    v_(i,k)=[d^k/dz^k(exp(Lz)/(z+1/2))]_(z=z_i).

Linear independence of distinct exponential polynomials makes H positive
definite. With inner product conjugate-linear in its first slot,
G_p^(k)(z_i)=<k_(i,k),g_p>. Orthogonal projection gives

    E(p)>=v^* H^(-1) v.                                  (15)

The right side is the exact minimum over L2 functions with these finite
Laplace-jet constraints: the minimizer is the kernel combination with
coefficient vector H^(-1)v. It is NOT asserted to be realizable by an
admissible arithmetic polynomial. Adding more constraints can only increase
the minimum. For real coefficients one can include conjugate nodes; the
minimizer in that conjugation-invariant analytic problem is then real.
No actual zero list or numerical zero parameter is used in the finite checks.

## 4. The full arithmetic energy has an exact finite-period representation

Let Q be any positive integer divisible by every support index of p. Balance
implies A_p(x+Q)=A_p(x), so u_p is periodic and constant on each [j,j+1).
For 1<=r<=Q let

    b_r=1-sum_n a_n floor(r/n),
    omega_(Q,r)=sum_(k>=0)[1/(r+kQ)-1/(r+1+kQ)]>0.

Nonnegativity permits regrouping the ENTIRE integral (2), yielding

    E(p)=sum_(r=1)^Q omega_(Q,r)|b_r|^2.                  (16)

The weights sum to one. Equivalently they equal
[digamma((r+1)/Q)-digamma(r/Q)]/Q, but the proof and checker do not need
that special-function implementation. For any integer K>=1 their tails obey

    0< sum_(k>=K)[1/(r+kQ)-1/(r+1+kQ)]
       <1/[Q(r+Q(K-1))].                                 (17)

This follows by comparison with the decreasing function (r+Qt)^(-2) and
integration from K-1. Thus (16) has an elementary complete error budget.
Since b_Q=1, (16) proves E(p)>0 for every finite balanced p.

For fixed support, (16) is a positive quadratic minimization problem on the
balanced coefficient space. Its Hessian is positive definite on nonzero
balanced variations: if all their floor values vanished, the first nonzero
coefficient index would give a nonzero value at that integer. Consequently
adding consistent affine jet/prefix constraints gives a unique finite
minimizer. No dimension-uniform bound on those minima follows. Q can be
extremely large, so (16) is not advertised as an efficient large-scale engine.

### 4.1 Two small, complete checks

Write l=log 2. The polynomial

    p_2(s)=1+(2/l-4)2^(-s)+(4-4/l)4^(-s)

has prefix mu(1), p_2(1)=0 and p_2'(1)=1. Formula (16), Q=4, gives exactly

    E(p_2)=(4-pi)/2 * (1/log2-1),
    189/1000 < E(p_2) <191/1000.                          (18)

For a derivation, the three nonzero cell values are 3-2/l, 2-2/l and 1.
Their weights are pi/8-l/4, 3l/4-pi/8 and 1-pi/8-3l/4. For an explicit
derivation write omega_r=omega_(4,r). The convergent alternating series give
omega_1+omega_2=pi/4, omega_2+omega_3=l/2, and omega_1+omega_3=l.
Together with sum omega_r=1 these yield all the displayed weights. Expansion
then gives (18). This is an admissible Y=2 norm check, not an annular m>=2 certificate.

A second completion keeps the ACTUAL prefix through n=3. Put

    t=(1-l/2-(log3)/3)/l,
    p_4(s)=1-2^(-s)-3^(-s)+(4t-2)4^(-s)+(-8t+8/3)8^(-s).

It has p_4(1)=0 and p_4'(1)=1 exactly, by elementary substitution. Its
period is Q=24, not lcm of unnecessary zero-coefficient indices. The checker
uses (16)--(17), all 24 cells, K=2048 and outward integer rounding to prove

    57/1000 < E(p_4) <59/1000.                            (19)

The infinite tail is included. Neither (18) nor (19) is a numerical boundary
integral, a new zero-free region, an optimized all-Y result or RH evidence.

## 5. Attempted completion and the remaining gap

The intended proof step was to replace the signed low-frequency problem by
a small positive approximation energy. Sections 1 and 4 make that energy
well-defined and finitely certifiable. Section 2 shows exactly what a small
norm would imply. It does NOT provide the small norm.

The only unconditional all-Y bound obtained for the specified p_Y is (8),
which allows fixed positive power growth. It cannot contradict (9), whose
exponent 2beta-1 lies strictly between zero and one. Neither a positive Gram
matrix, a logarithmic coefficient diagonal, the two jet conditions, nor two
small finite energies establishes (10).

The original signed-count theorem likewise remains unproved. Nothing here
bounds how often the parent's low-frequency integral is below -1. It would
be incorrect to submit this manuscript, or the preceding conditional chain,
as a proposed COMPLETE RH proof. A reviewer may verify every component above
and still cannot accept RH: the needed arithmetic upper bound has not been
supplied. No theorem is being left for the referee to invent.

## 6. Dependencies and review boundary

The contour parent at d1a45dba and the BMC parent at ed074bca are pinned in
SOURCES.json. Only BMC's coefficient bounds are used for (8); sections 1--4
otherwise supply their own finite-source and Hilbert proofs. The #804 source
at b556c3f (PROOF.md, section 3) has the earlier delayed integrated-target
bound and multiplicity calculation; this adaptation is not claimed as a new
principle. Baez-Duarte (arXiv:math/0011254) and Burnol
(arXiv:math/0103058) are relevant primary prior art. They are credited for
context, not imported as an unexplained proof of (10).

Classical Fourier Plancherel, analytic continuation of zeta, its functional
symmetry, elementary Mobius inversion and Laguerre orthogonality are the
analytic inputs. The hypothetical-zero conclusions do not import RH,
simplicity, a finite zero table or an all-spectrum numerical certificate.
The checker verifies bounded exact identities and the two finite norm
intervals. It does not machine-prove Plancherel, analytic continuation,
finite interpolation in Hilbert space or any unbounded arithmetic estimate.
