# Direct polynomial-inequality attempt: the complete origin boundary

Status: **PROPOSED component proofs; the requested all-degree inequality is
NOT proved.** This is an unsuccessful direct proof attempt with quantitative
boundary constructions. It is not another claimed completion of RH.

Parent: PR845, `b9ccd03a681a73e91fb7bbfb7a3b97766fe8285e`,
`standalone/2026-09-10-astra-safe-source-kernel/PROOF.md`, AC28-7.
All prior files and mathematical statuses remain unchanged.

The parent already proves the zero-exclusion implication, impossibility of
eta=0, and a sharper multiplicity-dependent necessary cost. We do NOT claim
those conclusions as new. Here they are reconstructed directly with cutoff
functions and actual approximating odd polynomials, without the parent's
holomorphic feature-map or Blaschke continuation argument. The additional
content is the quantitative graph realization and a complete pole/remainder
calculation. No broad novelty claim is made for Euler summation, polynomial
density, approximate spectral modes, or convolution estimates.

## 0. Exactly the requested inequality

For every complex odd polynomial p put

    Q_p(t) = sum_(n>=1, n odd) p(t/n)/n,
    A p(t) = t Q_p'(t),                    0<=t<=1,
    E p(t) = Q_p(1)-sum_(n>=3, n odd) p(t/n)/n, 1<=t<=3.

All norms of p and A p below are on (0,1); the norm of E p is on (1,3).
The requested statement, still OPEN, is

    for every eta>0 there exists finite C_eta such that
    ||E p||^2 <= eta ||p||^2 + 4 C_eta ||A p||^2          (Q)

for EVERY degree and EVERY coefficient vector, with the SAME C_eta.
We establish no such upper bound for general positive eta.

Set Z(s)=(1-2^(-s))zeta(s), and a_s=(s-1)Z(s).
All complex powers of positive real numbers use their real logarithm.
No inverse zeta or assumption on zeros is needed in Sections 1--3.

## 1. AC29-1: the actual polynomial test domain has a controlled C1 completion

Let D={f in C1([0,1];C): f(0)=0}. Define Q_f on [0,1] and E f as above;
E uses f only at arguments <=1. The series for Q_f and Q_f' converge uniformly:
|f(t/n)|<=||f'||_infinity t/n.

If f,g in D and ||f'-g'||_infinity<=d, then

    ||f-g|| <= d/sqrt(3),
    ||A f-A g|| <= 5d/(4sqrt(3)),
    ||E f-E g|| <= 2sqrt(2)d.                           (1.1)

Indeed |f(u)-g(u)|<=d u and Z(2)<5/4. The latter follows, without a
transcendental computation, from

    Z(2) <=1+1/9+1/25+1/49+1/14 <5/4.

The last inequality uses the decreasing-integral bound for the odd tail
starting at 7. Thus |A(f-g)(t)|<=d Z(2)t, and
|E(f-g)(t)|<=d[Z(2)+t(Z(2)-1)]<2d for 1<=t<=3.

Every f in D is a C1 limit of ODD polynomials. One explicit construction is

    h(x)=f'(sqrt(x)),
    h_N(x)=sum_(j=0)^N h(j/N) binom(N,j)x^j(1-x)^(N-j),
    p_N(t)=integral_0^t h_N(u^2)du.                     (1.2)

Bernstein approximation gives h_N->h uniformly. For completeness, its
probabilistic formula is h_N(x)=E h(S_N/N), with S_N binomial(N,x).
Uniform continuity and Var(S_N/N)<=1/(4N) show uniformly that

    |h_N(x)-h(x)| <= omega_h(delta)+||h||_infinity/(2N delta^2).

First choose delta and then N. This proof applies to complex h by absolute
values. Equation (1.2) is an odd polynomial and p_N'->f' uniformly.

It follows from (1.1) that for EACH fixed eta,C, (Q) on all odd polynomials
is EQUIVALENT to (Q) on D. Every strict smooth violation consequently has a
finite odd-polynomial violation. This is a proved density statement in all
three required quantities, not just L2 density and not a finite-degree bound.

## 2. AC29-2: smoothed odd Euler summation, including its full derivative error

Define the fixed cutoff

    chi(v)=0                          v<=1,
           3(v-1)^2-2(v-1)^3          1<v<2,
           1                          v>=2.

It is C1 and piecewise C2, 0<=chi<=1, |chi'|<=3/2, |chi''|<=6 a.e.
For s with 0<beta=Re s<1 and v>0 put

    S_s(v)=sum_(n odd) n^(-s) chi(v/n),
    c_s=(1/2) integral_0^infinity y^(-s)chi(1/y)dy.

S_s(v) is a FINITE sum; c_s converges at both ends. Then exactly

    S_s(v)=c_s v^(1-s)+Z(s)+R_s(v),                    (2.1)

where, with C_o(x)=floor((x+1)/2) for x>=0 and d_o(x)=C_o(x)-x/2,

    R_s(v)=integral_0^infinity d_o(x)x^(-s-1)
             [s(chi(v/x)-1)+(v/x)chi'(v/x)] dx.         (2.2)

Use the constants

    K0(s)=2^(beta-1)(|s|+3)/beta,
    K1(s)=2^(beta-1)(3|s+1|+24)/beta,
    K(s)=|s-1|K0(s)+K1(s).

The COMPLETE remainder bounds are

    |R_s(v)| <= K0(s)v^(-beta),
    |v R_s'(v)| <= K1(s)v^(-beta).                     (2.3)

They include the unbounded x region; no sampled or finite tail is substituted.

### Proof

We have |d_o(x)|<=1/2, and d_o(x)=-x/2 on (0,1). Elementary Euler summation
and analytic continuation give the absolutely convergent formula

    Z(s)=s integral_0^infinity d_o(x)x^(-s-1)dx,
                          0<Re s<1.                   (2.4)

One direct verification splits at 1: the first piece is s/[2(s-1)], and the
remaining discrepancy integral is holomorphic for Re s>0. For Re s>1 it is
the usual Euler remainder for the odd Dirichlet series. This proves (2.4)
by continuation across s=1, which is excluded in the displayed strip.

Write dC_o=dx/2+dd_o in the finite smoothed sum. The dx/2 term is
c_s v^(1-s). Subtract the uncut discrepancy contribution (2.4) and integrate
by parts. Both boundary terms vanish: at zero they are O(x^(1-beta)), and
at infinity they are O(x^(-beta)). This gives (2.2).

The integrand is zero for x<v/2. Bounding |(v/x)chi'|<=3 and integrating
x^(-beta-1) from v/2 to infinity gives the first inequality in (2.3).
Differentiation under the integral, justified locally in v by the bounded
piecewise derivatives and an integrable dominating function, gives

    v R_s'(v)=integral d_o(x)x^(-s-1)
              [(s+1)(v/x)chi'(v/x)+(v/x)^2 chi''(v/x)]dx.

The bracket is supported on v/2<=x<=v and bounded by 3|s+1|+24. This proves
the second bound. Endpoint values of chi'' affect no integral. QED.

Euler summation is classical; see DLMF 25.2.8. Formula (2.2) is written out
so that the precise cutoff and all endpoint/derivative terms can be checked.

## 3. AC29-3: singular power modes are realized in the actual polynomial graph

For 0<epsilon<1/2 define on positive t

    f_(s,epsilon)(t)=t^(s-1)chi(t/epsilon).

Its restriction to [0,1] is in D, and it vanishes on [0,epsilon]. Using
(2.1), for every t>0,

    Q_f(t)=c_s epsilon^(s-1)+Z(s)t^(s-1)
                                      +t^(s-1)R_s(t/epsilon). (3.1)

The possibly large first term is CONSTANT IN t. It cancels EXACTLY in both
A f=tQ_f' and E f=Q_f(1)-Q_f(t)+f(t), rather than being bounded separately.
The second identity may use the written extension above 1, but its left side
uses only the original values on [0,1]. No extension choice changes E.

Put

    e_s(t)=Z(s)+(1-Z(s))t^(s-1),      1<=t<=3.

If 1/2<beta<1, then

    ||f_(s,epsilon)-t^(s-1)||^2
       <= (2epsilon)^(2beta-1)/(2beta-1),
    ||A f_(s,epsilon)-a_s t^(s-1)||^2
       <= [|a_s|^2/(2beta-1)+K(s)^2]epsilon^(2beta-1),
    ||E f_(s,epsilon)-e_s|| <=2sqrt(2)K0(s)epsilon^beta. (3.2)

### Proof

The first difference is supported below 2epsilon and has magnitude at most
t^(beta-1). On t<epsilon, A f=0, so the second squared error integrates to
|a_s|^2 epsilon^(2beta-1)/(2beta-1). On epsilon<=t<=1, differentiate (3.1):

    A f-a_s t^(s-1)
       =t^(s-1)[(s-1)R_s(t/epsilon)+(t/epsilon)R_s'(t/epsilon)].

Its magnitude is at most K(s)epsilon^beta/t. Its squared integral is at most
K(s)^2 epsilon^(2beta-1). Finally on [1,3], f=t^(s-1), and the remaining
error is R_s(1/epsilon)-t^(s-1)R_s(t/epsilon). Its magnitude is at most
K0(s)epsilon^beta(1+1/t). This proves (3.2). QED.

Apply (1.2) to each cutoff and take an appropriate diagonal sequence. There
are actual odd polynomials p_j with the three simultaneous limits

    p_j -> t^(s-1)       in L2(0,1),
    A p_j -> a_s t^(s-1) in L2(0,1),
    E p_j -> e_s         in L2(1,3).                    (3.3)

We claim a limit of graph triples, not closability of an otherwise undefined
operator and not that the singular power has an ordinarily convergent Q sum.
Polynomial degrees may grow without a stated quantitative upper bound.

### Direct off-critical obstruction; conditional on such a zero

If Z(s)=0 with 1/2<beta<1, (3.3) becomes a nonzero limiting p, zero limiting
A p, and limiting E p=t^(s-1). Thus for EVERY finite C and

    0<=eta<3^(2beta-1)-1,                               (3.4)

some finite odd polynomial violates (Q). Indeed the limiting gap is

    [3^(2beta-1)-1-eta]/(2beta-1)>0.

This constructs the witness via (1.2), rather than just inferring its
existence from an analytic Gram-continuation theorem. No off-critical zero
is asserted to exist. The conclusion is an alternative proof of the parent's
zero-exclusion implication, not an unconditional new zero-free region.

In particular, any attempt to prove (Q) by simply discarding t close to zero
would discard precisely the graph modes it has to control.

## 4. AC29-4: actual polynomial failure at eta=0, with a direct critical family

Let s=1/2+i gamma be ANY critical-line zero. Existence of at least one is a
classical imported theorem; neither its coordinates nor simplicity are used.
Z(s)=0 because 1-2^(-s) is nonzero here. Keep K0=K0(s), K=K(s).
For R>=1 put

    F_R(t)=(1/R) integral_R^(2R) f_(s,exp(-u))(t)du.     (4.1)

This is in D and vanishes near zero. Its norms obey

    R-log2 <= ||F_R||^2 <=2R,
    ||A F_R||^2 <=4K^2/R,
    ||E F_R-t^(s-1)|| <=2sqrt(2)K0 exp(-R/2).           (4.2)

### Proof

With y=-log t and beta=1/2, the first norm is the integral over y>=0 of
W_R(y)^2, where

    W_R(y)=(1/R)integral_R^(2R)chi(exp(u-y))du.

It is one on 0<=y<=R-log2, between zero and one elsewhere, and zero for
y>=2R. This proves the first bounds.

At the root a_s=0. For each u, A f_(s,exp(-u)) is zero at y>u. At y<=u,
(2.3) and (3.1) give

    |exp(-y/2) A f_(s,exp(-u))(exp(-y))|
       <= K exp(-(u-y)/2).

The factor exp(-y/2) is the EXACT isometry from L2(dt) to L2(dy). The average
is bounded by convolution of 1_[R,2R]/R with the one-sided exponential
kernel, whose L1 norm is 2. Young's inequality gives 2K/sqrt(R), proving
the second bound. This uses the entire y tail and does not assume the errors
from different cutoffs are orthogonal. The third bound follows by averaging
the E error in (3.2), whose pointwise proof remains valid at beta=1/2.

Let ell=log3 and choose

    R0=max(1, 2 log(4sqrt(2)K0/sqrt(ell))).

For R>=R0, ||E F_R||^2>=ell/4. Therefore for any fixed finite C, choosing
R>max(R0,64 C K^2/ell) gives a strict violation of

    ||E f||^2 <=4 C ||A f||^2.

By AC29-1 this violation transfers to a FINITE ODD POLYNOMIAL. Consequently
no degree-independent bound with eta=0 exists for the actual arithmetic
operator. The parent already proves that conclusion by a different argument.

### Necessary cost for positive eta, not a refutation of (Q)

If (Q) holds, insert R=ell/(16eta), for eta sufficiently small that R>=R0.
Equations (4.2) then force

    C_eta >= ell^2/(2048 K^2 eta).                     (4.3)

This is a coarse LOWER bound. The parent's multiplicity-aware bound is
stronger. No upper bound for C_eta has been obtained. Normalizing F_R by
sqrt(R) makes both A-output and E-output tend to zero; this construction
therefore does NOT contradict the positive-eta compactness target.

## 5. What the direct attempt did and did not establish

The direct attempt was to use the convergent positive dilation series and
its unweighted derivative estimate to obtain (Q). The derivative estimate
has the wrong weight. The exact boundary calculation above shows why: the
pole term is harmless after cancellation, but a_s t^(s-1) remains, and its
vanishing is exactly the zero issue. Removing the cutoff before estimating
that graph component would assume the conclusion.

For each fixed polynomial degree, the best nonnegative constant is finite:
A is injective because it multiplies the coefficient of t^(2k-1) by the
positive number (2k-1)Z(2k). Compactness of a finite-dimensional unit sphere
then suffices. It supplies NO bound uniform in degree. The best constants
at eta=0 tend to infinity by Section 4, despite long initially positive
finite matrix tests.

The exact positive-eta all-degree inequality remains OPEN. We have not
proved it false, proved RH, proved necessity of this particular condition
under RH, found an upper bound uniform in degree, or resolved the parent's
shell compactness targets. The completed results are domain control,
full Euler-remainder estimates, and explicit boundary witness mechanisms.
Independent review should not be asked to fill the missing upper bound.
