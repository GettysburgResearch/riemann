# Native smooth Mobius resonance and sharp small-prime dilation costs

Status: PROPOSED reviewable mathematics. Complete proofs are supplied below,
with the classical prime number theorem in the fixed progressions modulo 3
as a named input. No new native moment upper bound, zero-free half-plane,
independent review, or RH proof is claimed.

Scope: K=Q(omega), omega^2+omega+1=0; integral ideals; a fixed finite excluded
prime-ideal set S containing the primes over 2 and 3. Prime-ideal norms,
including both conjugate split ideals and inert ideals, are retained. W is
one fixed nonzero, nonnegative function in C_c^infinity((0,infinity)), with
support contained in [a,b], 0<a<b. The twist in this note is the trivial
finite-order twist. No moving coefficient vector or moving test is chosen.

Classical credit: finite Euler multiplication, Mellin inversion/uniqueness,
Rankin bounds, and dilation multipliers are standard. The intended addition
is their use to obtain a sharp maximal smooth-Mobius exponent with native
coefficients, and the physical partial-moment consequence in the companion
note. The exponential finite-product mechanism is related to, but concerns
a different norm-filtered object from, the trace obstructions in #931/#933.
See SOURCES.md for inspected sources and the limits of the comparison.

## 1. Two finite objects and one exact identity

Let B_y={p not in S : Np<=y}, let P_y be the product of its prime ideals,
and define

    E_y(s) = product_(p in B_y) (1-(Np)^(-s)),
    M_y(D;W) = sum_(d | P_y) mu_K(d) W(Nd/D).                 (1.1)

M_y is the genuine squarefree y-smooth Mobius sum, with every ideal of the
specified support included. It is not a positive smooth-number count or a
prime-only selector. Its coefficients are fixed by mu_K, not adjusted to
align any row. Equal rational norms are summed with their full multiplicity.
For each fixed y the sum is finite, and M_y(D)=0 unless

    1/b <= D <= NP_y/a.

Put W_hat(s)=integral_0^infinity W(x) x^s dx/x. A change of variable D=Nd/x,
term by term in the finite sum, gives the entire-function identity

    integral_0^infinity M_y(D;W) D^(-s) dD/D = W_hat(s) E_y(s).  (1.2)

No unfiltered infinite Euler product, contour shift, or removal of a
physical norm test occurs in this identity. For every fixed real sigma,
W_hat(sigma)>0. Consequently, for any t_y->0,

    |W_hat(sigma+i t_y)| >= c_(W,sigma)>0                     (1.3)

for all sufficiently large y. Only this local nonvanishing is needed;
there is no claim that an arbitrary compact test is globally zero-free.

The elementary ideal count I_K(x)=O_K(x) gives

    |M_y(D;W)| <= C_(K,W) D                                  (1.4)

uniformly in y whenever M_y(D) can be nonzero. The fixed exclusions do not
increase this bound.

## 2. A slowly varying frequency almost maximizes the finite Euler product

We use the classical PNT in the fixed progression 1 modulo 3. Split
rational primes have two prime ideals of norm p; inert primes have one of
norm p^2. Thus, after any fixed exclusions,

    pi_K(y) ~ y/log y.

For each fixed 0<sigma<1, partial summation gives

    S_sigma(y) := sum_(p in B_y) (Np)^(-sigma)
       ~ y^(1-sigma) / ((1-sigma) log y),
    sum_(p in B_y) (Np)^(-2sigma) = o(S_sigma(y)).             (2.1)

For the second assertion, the cases 2sigma<1, =1, and >1 give respectively
O(y^(1-2sigma)), O(log y), and O(1), any of which suffices. Chebyshev bounds
or the ideal count give these upper bounds; no zero-free region is used.

### Theorem 2.1 (low-frequency resonance)

For fixed 0<sigma<1 and t_y=pi/log y,

    log |E_y(sigma+i t_y)|
       = (1+o(1)) S_sigma(y)
       = (1+o(1)) y^(1-sigma)/((1-sigma) log y).              (2.2)

Proof. Because Np>=7, the power-series expansion of log(1-z), taking real
parts, is uniform for z=(Np)^(-sigma-i t_y). It yields

    log |E_y(sigma+i t_y)|
      = -sum_(p in B_y) (Np)^(-sigma) cos(t_y log Np)
        + O_sigma(sum_(p in B_y) (Np)^(-2sigma)).             (2.3)

For any fixed 0<eta<1, the sum over Np<=y^(1-eta) is o(S_sigma(y)), by
(2.1) or partial summation. On the remaining primes, t_y log Np lies in
[pi(1-eta),pi], so its cosine differs from -1 by at most 1-cos(pi eta).
First let y tend to infinity with eta fixed, and then let eta decrease to
zero. The weighted cosine average tends to -1. Equation (2.1) absorbs the
quadratic remainder and proves (2.2). QED.

The frequency t_y tends to zero. A bound that only excludes very large
vertical frequencies cannot remove this resonance. The product is finite
and entire; the large value is not a pole or a zeta zero.

## 3. Sharp maximal exponent for the actual smooth Mobius sum

### Theorem 3.1 (native smooth-sum witnesses)

Fix A>1 and 0<alpha<1-1/A. For every sufficiently large real y, there is
D>=exp(y^(1/A)) such that

    |M_y(D;W)| > D^alpha.                                    (3.1)

In particular y<=(log D)^A, and the scales D obtained in this way are
unbounded. The same fixed W and the same actual Mobius coefficients work
throughout.

Proof. Choose a fixed sigma with alpha<sigma<1-1/A, and write
D_0=exp(y^(1/A)). Suppose instead |M_y(D)|<=D^alpha for every D>=D_0.
The absolute value of (1.2), split at D_0, is at most

    C_(W,sigma) D_0^(1-sigma)
          + D_0^(alpha-sigma)/(sigma-alpha).                 (3.2)

The first term follows from (1.4), including the vanishing below 1/b.
The second is the convergent integral of D^(alpha-sigma) over [D_0,infinity).
But (1.3) and Theorem 2.1 give a lower bound of

    exp(c_sigma y^(1-sigma)/log y)

for the same quantity, once y is large. Since 1-sigma>1/A, this exceeds
(3.2), whose logarithm is O(y^(1/A)). This contradiction proves (3.1).
All integrals are of finite y-smooth sums; no asymptotic assertion about
an infinite Mobius Dirichlet series has been substituted. QED.

### Theorem 3.2 (localized witnesses)

In Theorem 3.1, given any fixed eta>0, D can be chosen to satisfy

    exp(y^(1/A)) <= D <= exp(y^(1/A+eta)).                    (3.3)

Proof. In addition choose 0<tau<sigma<1-1/A such that sigma>alpha and
1-tau<1/A+eta. This is possible by taking tau and sigma sufficiently close
to 1-1/A from below. The positive Rankin bound, valid for every D>0, is

    |M_y(D)| <= C_W (bD)^tau
                     product_(p in B_y)(1+(Np)^(-tau))
               <= C_(W,tau) D^tau exp(C_tau y^(1-tau)).       (3.4)

Set D_1=exp(y^(1/A+eta)). The integral of |M_y(D)|D^(-sigma) above D_1
is at most

    C exp(C_tau y^(1-tau) - (sigma-tau)y^(1/A+eta)),

which tends to zero. If (3.1) failed on [D_0,D_1], the middle integral
would have the second bound in (3.2), and the lower integral would have
the first. The same resonance contradiction applies. QED.

### Corollary 3.3 (sharp maximal logarithmic-power exponent)

For every fixed A>1,

    limsup_(D->infinity)
      log(1 + sup_(2<=y<=(log D)^A) |M_y(D;W)|) / log D
       = 1-1/A.                                             (3.5)

For the upper bound choose any tau with 1-1/A<tau<1 and use (3.4).
Uniformly in the permitted y, its extra logarithm is
O((log D)^(A(1-tau)))=o(log D). Then let tau decrease to 1-1/A.
The lower bound follows from Theorem 3.1 with alpha increasing to 1-1/A.

One can, by diagonal choices in Theorem 3.2, arrange witness sequences
with y=(log D)^(A+o(1)) and |M_y(D)|>=D^(1-1/A-o(1)). This does NOT assert
the lower bound on the single prescribed curve y=(log D)^A, at every D,
or on any prescribed sequence of D. The uniform range in (3.5) is essential
to the theorem stated here. No saddle-point asymptotic for M_y is claimed.

## 4. The cost of removing small primes is a genuine operator norm

For sigma>0 let B_sigma be the Banach space of measurable functions on
(0,infinity) with norm ||f||_sigma=sup_(D>0) D^(-sigma)|f(D)|. Define

    (T_y f)(D) = sum_(d | P_y) mu_K(d) f(D/Nd),
    (U_y f)(D) = sum_(d supported on B_y) f(D/Nd),             (4.1)

where U_y includes all prime powers. Its sum is absolutely convergent in
B_sigma for every fixed y and sigma>0. Euler convolution gives
T_y U_y=U_y T_y=I, with exchanges justified by these norm majorants.

### Theorem 4.1

In this fixed quadratic field,

    ||T_y||_(B_sigma->B_sigma) = product_(p in B_y)(1+(Np)^(-sigma)),
    ||U_y||_(B_sigma->B_sigma) = product_(p in B_y)(1-(Np)^(-sigma))^(-1).
                                                                    (4.2)

For fixed 0<sigma<1, both logarithms are (1+o(1))S_sigma(y).
Moreover f_y(D)=D^(sigma+i pi/log y), which has norm one and arbitrarily
small logarithmic oscillation frequency, already gives

    log ||T_y f_y||_sigma = (1+o(1))S_sigma(y).               (4.3)

Proof. The upper bounds are the absolute convolution masses. For U_y,
the norm-one function f(D)=D^sigma attains its upper bound exactly.
For T_y, group ideals by their ordinary rational norm n, writing the
coefficient as c_y(n). There is no Mobius sign cancellation inside this
norm fiber: for a split rational prime the possible squarefree ideal
norm exponents are 0,1,2 with signs +,-,+; for an inert rational prime
there are exponents 0,2 with signs +,-. The splitting type is fixed for
each rational prime. Hence all ideals in one norm fiber have the same
Mobius sign. This remains true after fixed exclusions of one or both
conjugate prime ideals. Therefore

    sum_n |c_y(n)| n^(-sigma) = product_(p in B_y)(1+(Np)^(-sigma)).

At D=1 choose f(1/n)=sign(c_y(n))n^(-sigma) for the finite set with
c_y(n) nonzero, and define f elsewhere with norm at most one. This attains
the upper bound. A smooth norm-one interpolant can alternatively be made
at these finitely many separated logarithmic points. This exact norm
argument is specific to the stated field; it is not asserted for every
number field with mixed residue degrees over one rational prime.

Finally T_y f_y(D)=E_y(sigma+i pi/log y)f_y(D). Theorem 2.1 proves (4.3).
Expanding log(1+q^(-sigma)) and -log(1-q^(-sigma)) and using (2.1) proves
the common norm asymptotic. QED.

At the exact critical weight sigma=1/2,

    log ||T_y|| ~ log ||U_y|| ~ 2 sqrt(y)/log y.              (4.4)

Thus these critical-weight operators have subpower cost in D if and only
if sqrt(y)/log y=o(log D), for y(D)->infinity. This statement concerns the
specified operator norm. A moment bound allowing every D^epsilon can use
weights 1/2+delta instead. In particular (4.4) does not contradict #936's
sufficient y=(log D)^(2+o(1)) range or #937's sufficient bias-budget bound.

## 5. Research implication and limits

The previous generic-phase sharpness argument needed a deliberately aligned
coefficient vector or an unconstrained CRT row. Theorem 3.1 instead keeps
the native Mobius coefficients, one fixed compact test, and the principal
row u=1. The companion note amplifies this through actual sixth-power rows
inside H=D^h. This is the extra arithmetic content.

The resonance is produced by truncating which prime phases remain native.
It does not imply a large value of the FULL Mobius sum at the same D.
The omitted rough-prime terms can cancel it. Bounding that signed
recoupling, rather than assuming every intermediate partial randomization
is small, remains the relevant arithmetic problem.
