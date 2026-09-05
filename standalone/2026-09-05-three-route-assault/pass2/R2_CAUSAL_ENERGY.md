# Route 2, pass 2: causal energy, explicit diagonal, and one-zero blow-up

Status: PROPOSED THEOREMS with complete arguments; independent review required.
Scope: the actual 67-free Mobius source, a fixed [1,2] frequency band, all positive damping parameters, and individual zero multiplicities. No new Mobius cancellation estimate is proved.
Parent: PR #793 at 7275b956b278051504da4befeb3b37924f83fd58, Route-2 fixed-band and causal transport note.
Smallest open step: a one-sided bound for the complete signed off-diagonal uniformly in the log-time horizon at every positive damping.

This pass removes the maximal-prefix operator from the final formulation, derives the complete arithmetic kernel, and quantifies the contribution of any single off-line zero without assuming it is rightmost or simple. It also identifies the causal/anti-causal error that invalidates a tempting reciprocal-zeta line-integral shortcut.

## B1. Fixed definitions

Put q=67, mu_q(n)=mu(n)1_(q does not divide n), and

    B_t(x)=sum_(n<=exp x) mu_q(n)n^(-1/2-it),   x>=0,
    J_sigma(L)=integral_0^L exp(-2 sigma x) integral_1^2 |B_t(x)|^2 dt dx,
    J_sigma=lim_(L->infty)J_sigma(L) in [0,infty].

The frequency interval is fixed before introducing any hypothetical zero. For sigma>1/2, |B_t(x)|<=2 exp(x/2) gives J_sigma<=4/(2 sigma-1). This is the paid absolute-convergence region, not a critical estimate.

## B2. Exact arithmetic form and the fully paid diagonal

Define k(v)=integral_1^2 exp(-itv)dt = exp(-3iv/2)sinc(v/2). Finite expansion and integration give

    J_sigma(L)=(1/(2sigma)) sum_(m,n<=exp L)
      mu_q(m)mu_q(n)/sqrt(mn) k(log(m/n))
      [max(m,n)^(-2sigma)-exp(-2sigma L)].

The matrix kernel is positive semidefinite because it is the original integral of squared prefix sums. Its complete sum is real, although individual k terms are complex. The diagonal is

    D_sigma(L)=(1/(2sigma)) sum_(n<=exp L)
      mu_q(n)^2/n [n^(-2sigma)-exp(-2sigma L)],
    D_sigma= zeta(1+2sigma)/[2sigma zeta(2+4sigma)(1+q^(-1-2sigma))].

For every sigma>0, D_sigma(L) increases to this finite value. The Euler factor follows from sum mu(n)^2 n^(-s)=zeta(s)/zeta(2s) and removal of the local factor 1+q^(-s). In particular

    D_sigma ~ 1/[4 zeta(2)(1+1/q) sigma^2] as sigma->0+.

Let C_sigma(L)=J_sigma(L)-D_sigma(L) be the FULL signed off-diagonal, including both orientations. Then

    J_sigma<infty  iff  sup_(L>=0) C_sigma(L)<infty.

Indeed J_sigma(L) is increasing and D_sigma(L)<=D_sigma. Only an upper bound on the signed C is needed. Estimating the sum of absolute off-diagonal terms is an unnecessary stronger target. C itself is not claimed monotone.

## B3. All-positive-damping finiteness is exactly the RH endpoint

The following are equivalent:

    (i) J_sigma<infty for every sigma>0;
    (ii) sup_L C_sigma(L)<infty for every sigma>0;
    (iii) RH.

It is enough to test any predetermined sequence sigma_j decreasing to zero.

### Forward proof, with causality retained

If J_sigma is finite, then for almost every t in [1,2], exp(-sigma x)B_t(x) belongs to L2(0,infty). Its Laplace transform is holomorphic for Re s>sigma by Cauchy-Schwarz. On Re s>1/2 it equals the absolutely convergent expression

    L[B_t](s)=D_q(s+1/2+it)/s,
    D_q(w)=1/[zeta(w)(1-q^(-w))].

Meromorphic uniqueness gives the same expression throughout Re s>sigma and requires that it have no pole there. A nontrivial zero rho with Re rho>1/2+sigma would give a nonremovable pole at s=rho-1/2-it; the finite Euler factor is nonzero at rho. Thus no such zero exists. Applying this for sigma_j->0 and using reflection proves RH.

Conversely the classical RH-to-Mertens bound gives sum_(n<=X)mu(n)/sqrt n=O_epsilon(X^epsilon). The exact finite-Euler inverse and fixed-band Abel transport from pass 1 give B_t(x)=O_epsilon((1+x)exp(epsilon x)) uniformly for 1<=t<=2. Taking epsilon<sigma proves J_sigma<infty. This direction imports the classical RH/Mertens implication; no such bound is asserted unconditionally.

## B4. Exact reciprocal-line formula: only when the causal norm is finite

Whenever J_sigma<infty, Plancherel gives

    J_sigma=(1/(2pi)) integral_R W_sigma(omega)
                         |D_q(1/2+sigma+i omega)|^2 d omega,
    W_sigma(omega)=integral_1^2 dt/[sigma^2+(omega-t)^2]
      =[arctan((omega-1)/sigma)-arctan((omega-2)/sigma)]/sigma >0.

For rigor, first take a line sigma+epsilon. The causal Laplace transform is its L2 Fourier transform there and agrees with the meromorphic expression. Let epsilon decrease to zero in L2; boundary values agree almost everywhere. Fubini, Tonelli, and omega=t+tau give the displayed positive weight. For sigma>1/2 no additional convergence hypothesis is needed.

One must NOT reverse this identity merely because the right-hand line integral happens to be finite. Such a line need not be the boundary of the causal Hardy function; poles to its right can encode anti-causal data instead.

## B5. Every individual off-line zero forces a quantified singularity

Let rho=beta+i gamma be ANY nontrivial zero with beta>1/2, of multiplicity m>=1. Put delta=beta-1/2 and

    R_rho=m!/[zeta^(m)(rho)(1-q^(-rho))] != 0,
    a_m=binom(2m-2,m-1)/4^(m-1).

Then, allowing J to take the value infinity,

    liminf_(epsilon->0+) epsilon^(2m-1) J_(delta+epsilon)
       >= (a_m/2)|R_rho|^2 W_delta(gamma) >0.

No linear independence of ordinates, rightmost-zero assumption, or simplicity is used. A fully explicit lower bound for the positive weight is

    W_delta(gamma) >= 1/[delta^2+(|gamma|+2)^2].

### Proof

If J_(delta+epsilon) is infinite, its contribution to the claimed lower bound is automatic. Along every subsequence for which it is finite, B4 applies. Restrict the positive omega integral to a fixed small neighborhood of gamma containing no other pole. The Laurent expansion is

    D_q(rho+z)=R_rho z^(-m)+O(|z|^(1-m)).

Set omega=gamma+epsilon v. Dominated convergence on the scaled neighborhood, using a local bound C|z|^(-m), gives its limiting contribution

    (|R_rho|^2 W_delta(gamma)/(2pi))
        integral_R (1+v^2)^(-m)dv.

The integral is pi a_m (by integration by parts, a_1=1 and a_(m+1)/a_m=(2m-1)/(2m)). This proves the liminf for every finite subsequence, hence in the extended sense. Other zeros can make the full norm larger or infinite; no asymptotic equality for the FULL J is claimed. The weight bound follows by replacing each denominator by delta^2+(|gamma|+2)^2. QED.

This quantifies the no-dilution mechanism on the actual Mobius source. A single finite-height exception already obstructs all-positive-damping finiteness. The theorem is a lower bound caused by a hypothetical zero, not an unconditional upper bound excluding that zero.

## B6. Exact causal/anti-causal countercontrol

Take a simple model B(x)=exp(delta x) on x>=0, delta>0. Its causal damped norm is infinite for 0<sigma<=delta. Nevertheless, for every sigma!=delta,

    (1/(2pi)) integral_R |1/(sigma-delta+i omega)|^2 d omega
      =1/[2|sigma-delta|] <infty.

For sigma<delta, this boundary function is the Fourier transform of

    -exp((delta-sigma)x)1_(x<0),

not of exp((delta-sigma)x)1_(x>=0). Thus pointwise finiteness of a reciprocal-zeta vertical moment, detached from holomorphic causal continuation, cannot prove the desired Mobius estimate. The sign and support switch are both load-bearing.

## B7. Where the attempted closure stops

The diagonal is paid for all sigma>0, and the complete signed off-diagonal is now explicitly specified. Absolute summation proves the whole norm finite only for sigma>1/2. Moving a reciprocal-zeta integration line into 0<sigma<=1/2 without controlling crossed poles is circular; B6 gives the precise failure mechanism.

The remaining task is to bound sup_L C_sigma(L) from the literal prime/Mobius source for every positive sigma, or prove a quantitatively uniform exponent improvement that implies it. No instance of a new signed power saving is claimed. This is the same arithmetic endpoint as pass 1, now with a causal positive norm, an exact diagonal subtraction, and a multiplicity-aware individual-pole lower bound that can be compared with an actual proposed upper bound.
