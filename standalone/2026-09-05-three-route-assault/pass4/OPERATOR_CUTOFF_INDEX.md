# Every finite arithmetic prime cutoff has infinitely many negative directions

Status: PROPOSED COMPLETE COMPONENT PROOFS; independent review required. The full arithmetic operator's positivity and RH remain OPEN.
Scope: the literal kernel of PR #792/HL-1, with all gamma terms retained and an arbitrary finite prime-power cutoff; the common Hardy family from PR #793/pass2. No hypothetical zero, zero census, or RH input.
Local labels OC-1 through OC-3. This is an obstruction for one explicit approximation scheme, not a counterexample to full-source positivity.

## 1. Keep the arithmetic source exactly

Set a=3/4, b=3/2, c_j=2j+1/2 and

    C=(1-gamma_E-log(2pi))/3, alpha_j=1/(c_j^2-b^2).

For finite X>=2, define the continuous even kernel

    W_X(x)= (1/2) exp(|x|/2)+C exp(-b|x|)
       +sum_(j>=1) alpha_j exp(-c_j|x|)
       -(1/3)sum_(2<=n<=X) Lambda(n)/sqrt(n)
          [exp(-b|x-log n|)+exp(-b|x+log n|)],               (OC1)

and, on L2(0,infinity),

    T_X(t,u)=b exp(-a(t+u)) W_X(t-u).

This is the precise finite-prime truncation of the independent arithmetic construction in #792, BRIDGE.md, HL-1. In particular it is NOT an exact finite-dimensional compression of the full operator.

T_X is self-adjoint and trace class. The decaying gamma kernels are positive trace-class after damping, with trace one before multiplication by alpha_j; sum alpha_j<infinity. The growing kernel decomposes into one rank-one operator minus a positive trace-class Volterra Gram operator. Each finite prime shift is a bounded shift of the base exponential kernel plus a rank-one endpoint term. These explicit decompositions are supplied in the pinned source. They use no zero distribution; the only infinite sum here is the absolutely summable gamma sum.

## 2. OC-1: negative index is infinite for every finite X

For EVERY finite X>=2,

    number of negative eigenvalues of T_X, with multiplicity, is infinite. (OC2)

The same conclusion holds if the positive gamma sum is additionally truncated while C and the completion term are retained unchanged.

### Exact negative residual at the origin

Write

    W_X(x)=cosh(x/2)+R_X(x).

The identity exp(|x|/2)=2cosh(x/2)-exp(-|x|/2) shows that R_X is continuous and decays exponentially as |x| tends to infinity, for fixed X. Since

    sum_(j>=1) alpha_j=1/6+log(2)/3,

we get the exact value

    R_X(0)=-D_X,
    D_X=(gamma_E+log pi+2P_X(2))/3>0.                      (OC3)

In the notation of PRIME_TAIL_TRANSITION.md this is also

    R_X(0)=2(m_0(X)-1/2).

The moment obstruction and this operator obstruction are caused by the same unmatched completion pole.

For x>=log X, the finite prime term is a constant multiple of exp(-bx). Thus for a finite explicit M_X,

    |R_X(x)|<=M_X exp(-x/2), x>=log X.

For example one can take

    M_X=1/2+|C|+sum alpha_j
              +(1/3)sum_(2<=n<=X) Lambda(n)(n+n^-2).

### Arbitrarily large negative subspaces

Choose a spacing D>log X so large that

    2M_X exp(-D/2)/(1-exp(-D/2))<D_X/2.

For any integer K>=3, use points t_i=1+iD, 0<=i<K. The residual matrix [R_X(t_i-t_j)] has diagonal -D_X and absolute off-diagonal row sums less than D_X/2. It is therefore bounded above by -(D_X/2)I.

The matrix [cosh((t_i-t_j)/2)] is

    v v^T-w w^T,
    v_i=cosh(t_i/2), w_i=sinh(t_i/2),

and has rank at most two. On the simultaneous null space of v^T and w^T, of dimension at least K-2, the full W_X matrix is strictly negative.

To pass from point matrices to the L2 operator, take compactly supported, unit-integral continuous bumps phi_(i,epsilon) near t_i and set f_i(t)=exp(at)phi_(i,epsilon)(t). Their quadratic-form matrix for T_X tends to b[W_X(t_i-t_j)] by continuity. For each finite K choose epsilon small enough that the strict negative subspace persists. All f_i belong to L2 and have disjoint supports. Their large norms do not affect inertia; no uniform normalized eigenvalue gap is asserted.

Thus T_X has at least K-2 negative eigenvalues for every K. Compact self-adjoint spectral theory proves OC2. Truncating the gamma sum makes R_X(0) more negative and retains decay, so the same proof applies. QED.

## 3. OC-2: the omitted ACTUAL primes cancel the growing mode

Let W be the full arithmetic kernel, with the entire prime-power sum. Then, unconditionally,

    W(x)=o(exp(x/2)),
    W(x)-W_X(x) ~ -(1/2)exp(x/2) as x->infinity, fixed X.  (OC4)

This is only cancellation of the deterministic pole at s=1. It does not rule out an exp(delta*x) contribution for 0<delta<1/2 and therefore does not prove RH.

Proof. Let Y=exp x. The prime contribution in OC1 with its positive sign before subtraction is exactly

    (1/3){exp(-3x/2)[sum_(n<=Y) Lambda(n)n + sum_(n>=2) Lambda(n)n^-2]
             +exp(3x/2)sum_(n>Y) Lambda(n)n^-2}.            (OC5)

Classical PNT and partial summation give

    sum_(n<=Y)Lambda(n)n ~ Y^2/2,
    sum_(n>Y)Lambda(n)n^-2 ~ 1/Y.

After division by exp(x/2), the three contributions in OC5 tend respectively to 1/6, zero, and 1/3. The total is 1/2, exactly cancelling the growing completion term. The gamma terms decay. Every fixed truncated sum decays for x>log X, so W_X(x)~exp(x/2)/2. This proves OC4. QED.

This is an actual prime-source cancellation theorem, but at the classical PNT scale, not at the missing critical scale.

## 4. OC-3: trace-norm convergence does not repair the sign argument

The source-built prime-atom estimate in pinned #792/HL-1 gives

    ||T-T_X||_1 <= (4/3)X^-1/4(4log X+19) ->0,             (OC6)

with the gamma series retained. Hence this is an example where arithmetic truncations converge in trace norm but EVERY truncation has infinite negative index. The conclusion concerns T_X only; whether T itself is positive is still the RH-equivalent open theorem.

There is no contradiction with compactness: the diagonal operators with entries 2^-j for j<=K and -2^-j for j>K converge in trace norm to diag(2^-j), while each approximant has infinitely many negative eigenvalues.

In particular, the proof plan

    retain finitely many prime atoms -> prove that operator PSD -> take the limit

cannot work for OC1. Exact compressions P_N T P_N of the FULL source are different objects and are not refuted. An analytically balanced completion or a tail bound in the original quadratic form must enter before a positivity claim.

The remaining full-source arithmetic sign is not supplied by OC4 or OC6. Norm convergence and cancellation of the single s=1 pole do not exclude the smaller exponential modes associated with hypothetical exceptional zeros.
