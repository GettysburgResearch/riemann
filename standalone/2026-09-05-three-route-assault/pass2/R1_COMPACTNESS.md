# Route 1, pass 2: compatible matrices are unnecessary

Status: PROPOSED THEOREMS, complete proofs below; independent review required.
Scope: positive finite-rank determinant approximants, escape of trace, constructive two-coefficient completion, and finite zero-exclusion certificates. RH is not assumed in the forward theorems and is not proved.
Parent: PR #793 at 7275b956b278051504da4befeb3b37924f83fd58; the Route-1 proof and its marked-mode obstruction remain unchanged.
Smallest open step: produce positive finite-rank approximants to the *actual* invariant xi coefficients at unbounded accuracy. No such producer is supplied here.

The improvement is an elimination of a proposed extra task: one does NOT need compatible compressions or projective consistency of the finite matrices. Uniform trace control and coefficient convergence suffice. This is a constructive specialization of classical type-I Laguerre-Polya compactness, not an external novelty claim.

## A1. Trace-compactness with the exact escape term

Let K_n be positive semidefinite matrices of arbitrary finite sizes, with tr K_n <= C. Put p_n(u)=det(I+u K_n), and suppose each Taylor coefficient of p_n converges to the corresponding coefficient of an entire f with f(0)=1. Then there are nonnegative numbers lambda_j with sum lambda_j <= C and gamma >= 0 such that

    f(u) = exp(gamma u) product_j (1+u lambda_j),
    gamma + sum_j lambda_j = f'(0).

No relation between the spaces carrying K_n is required. If log f(x)=o(x) on the positive real axis, then gamma=0. In particular this holds if f has entire order less than one.

### Proof

Arrange the eigenvalues lambda_(n,j) decreasingly and pad by zeros. They obey 0 <= lambda_(n,j) <= C/j. Diagonal subsequence extraction gives lambda_(n,j) -> lambda_j for every fixed j, and Fatou gives sum lambda_j <= C. Traces converge to c=f'(0), by coefficient convergence.

For |u|<=R and J>=2CR, all terms with j>J satisfy |u lambda_(n,j)|<=1/2. The principal logarithm power series gives

    |log(1+u lambda)-u lambda| <= |u|^2 lambda^2,
    sum_(j>J) lambda_(n,j)^2 <= C^2/(J+1).

Consequently the tail product differs, in logarithmic coordinates, from exp(u sum_(j>J)lambda_(n,j)) by at most R^2 C^2/(J+1), uniformly in n. First take n to infinity at fixed J, then J to infinity. The limit is exp((c-sum lambda_j)u) product_j(1+u lambda_j). The product converges locally uniformly. The extracted gamma=c-sum lambda_j is nonnegative.

Also e_k(lambda_(n,*)) <= C^k/k!, by expansion of (sum lambda)^k. Thus the p_n are locally uniformly bounded by exp(C|u|), their coefficient limit is f, and the preceding limit is f itself, not a different subsequential function. For x>=0 every product factor is at least one, so log f(x)>=gamma x. The stated sublinear positive-axis growth forces gamma=0. QED.

When gamma=0, the sorted eigenvalue vectors of the chosen subsequence actually converge in l1. Indeed their coordinatewise limits have the same total mass c as their convergent traces; choose a finite prefix carrying all but an arbitrary small part of c, and bound both remaining positive tails. Hence the diagonal matrices converge in trace norm after this freely chosen spectral identification. This is a *conclusion*, not a compatibility assumption.

## A2. Why escape must be accounted for

The matrices K_n=(c/n)I_n have trace c and p_n(u)=(1+cu/n)^n -> exp(cu). Every individual ordered eigenvalue tends to zero. Without the positive-axis growth condition all trace can escape, and no positive trace-class determinant can equal exp(cu) when c>0: its zero-free determinant would have no positive eigenvalues and would be identically one.

It is therefore incorrect to deduce trace-norm compactness from a trace bound alone. A1 uses the actual xi growth to rule out precisely this missing term.

## A3. Application to the theta target

Use the actual normalization

    f(u)=xi(1/2+sqrt(u+1/4))/xi(1),   xi(1)=1/2.

The functional equation makes this entire in u. The standard split-theta formula is

    f(u)=1+4u integral_0^infty e^(tau/2) psi(e^(2tau))
                         cosh(tau sqrt(u+1/4)) d tau,
    psi(t)=sum_(m>=1) exp(-pi m^2 t).

It gives positive Taylor coefficients and log f(x)=O(sqrt(x) log(x+2)) for x>=1. One can obtain this bound by setting r=sqrt(x+1/4), bounding the theta tail by C exp(-pi exp(2tau)), and substituting t=exp(2tau), leaving a gamma integral of parameter O(r). Thus A1 applies without a new growth or projective-consistency hypothesis.

It is enough to construct positive finite K_n whose determinant coefficients converge to the theta coefficients. Their first coefficients are their traces, so convergence of the first coefficient already supplies the eventual trace bound. A1 yields f(u)=det(I+uK) for a positive trace-class diagonal K. Every zero of f is then negative real, and for a nontrivial zeta zero rho=beta+i gamma_0,

    Im(rho(rho-1))=(2 beta-1) gamma_0.

Since gamma_0 is nonzero, beta=1/2. This is a *conditional closure theorem*. The missing arithmetic positivity/approximation producer remains the RH-bearing problem.

The diagonal spectral identification in A1 is not a source-defined canonical Hilbert operator. It proves existence of an unmarked positive scalar realization; any additional functorial or canonical-source requirement remains a separate research objective.

## A4. Exact finite matching is not an artificial stronger endpoint

Suppose f is already a positive determinant with infinitely many distinct positive eigenvalues. Then for each fixed N there exists a finite positive matrix whose first N determinant coefficients agree with f exactly.

Choose N distinct positive eigenvalues t_1,...,t_N. For a long finite spectral truncation containing them, adjust these N values so that the first N power sums equal the full power sums. The Jacobian of (sum_j t_j^k)_(k=1,...,N) in the chosen variables is [k t_j^(k-1)], an invertible Vandermonde matrix. The missing tail moments tend to zero. The inverse function theorem therefore supplies small adjustments, preserving positivity, for every sufficiently long truncation. Newton's identities then give exact determinant-coefficient matching.

For invariant xi under RH, infinitely many distinct positive reciprocal spectral values are available, so exact finite matching is equivalent to the positive determinant endpoint. This reverse implication is *conditional on RH*, not a way to manufacture the approximants without it.

## A5. A concrete two-coefficient construction

Let the desired first coefficients be 1,C,a_2 with C>0, and set p_2=C^2-2a_2. There is a finite nonnegative spectrum realizing them exactly if and only if

    0 < p_2 <= C^2.

The necessity is p_2=sum lambda_j^2 and C=sum lambda_j. For 0<p_2<C^2 choose any integer r>=ceil(C^2/p_2), r>=2, and put

    d=sqrt((r p_2-C^2)/(r-1)),
    x=(C-d)/r,
    y=(C+(r-1)d)/r.

The spectrum consisting of r-1 copies of x and one copy of y is nonnegative, has sum C, square sum p_2, and second elementary symmetric sum a_2. For p_2=C^2 use the rank-one spectrum (C). The case p_2=0,C>0 is the forbidden pure-escape boundary, not a finite realization.

This is a finite algorithm on supplied coefficients, not a proof of the actual xi second-order sign or of higher-order feasibility. It supplies an exact acceptance test for the first nontrivial scalar completion. The companion R1_XI_MINIMAL_RANK.md executes this on actual xi and then supplies an exact minimal-rank-32 completion through degree three.

## A6. Finite, source-side zero-exclusion certificates

Let P(u)=det(I+uK), K>=0 finite, tr K<=C. Suppose the coefficients of P and f differ by at most epsilon_k through degree N. For S>R>0, Cauchy's estimate and the positive determinant coefficient bound give, on |u|<=R,

    |f(u)-P(u)| <= E_N(R,S),
    E_N = sum_(k=0)^N epsilon_k R^k
          + M_f(S) (R/S)^(N+1)/(1-R/S)
          + exp(CR) (CR)^(N+1)/(N+1)!.

Here M_f(S)=max_(|u|=S)|f(u)|. For actual xi, positivity of its coefficients gives M_f(S)<=f(S), which is the explicit theta integral above. Thus no zero table is required to bound the remainder.

Fix 0<theta<=pi/2. On |u|<=R, |arg u|<=pi-theta (with u=0 included),

    |P(u)| >= exp(-2RC(1+|log(sin theta)|)).

To prove this, split eigenvalues at 1/(2R). There are at most 2RC large eigenvalues, and each corresponding factor has modulus at least sin theta. For the small ones, |1+u lambda| >= 1-R lambda >= exp(-2R lambda). Multiply the bounds.

If E_N is strictly smaller than this lower bound, f has no zero in the stated compact sector. This is a finite, checkable sufficient certificate; unlike the all-rank endpoint, it can use one approximate finite matrix and an actual source tail bound. No such new xi certificate is claimed as executed in this pass.

## A7. Remaining attack and mandatory tests

The next source construction may use unrelated finite matrix sizes and may aim only at convergent coefficients. It must preserve the scalar theta coefficients, not the natural marked occupation marginals refuted in pass 1. The checker tests escape, Newton identities, the two-coefficient construction, and finite coefficient bounds. It does not establish xi positivity or infinite-order feasibility.
