# BNR26: balanced arithmetic Newton renormalization

**PROPOSED component theorems and an OPEN nonlinear estimate. RH is not proved.**
Date: 2026-09-10. Author: Astra. Base: `f99d9e3908dde4865377c75d9ca051c1f545bf4f`.

This is a new attack on the literal growing arithmetic prefix, not another
late-tail optimization. The short-source Newton identity is classical. It is
also used in PR805's different odd-integer, endpoint-smoothed normalization.
The proposed contribution is its coupling to a canonical compact TWO-moment
completion, an exact joint energy/mean renormalization, and a sufficient
subquadratic-gain programme with a precise generic countermodel.

The nonlinear arithmetic upper bound in Section 5 is NOT established. The
positive identities do not make it automatic. All components require independent
review; no priority is claimed for convolution inversion, projection, or the
classical hyperbola decomposition. See SOURCE_LOCK.json and RESEARCH_PLAN.md.

## 0. One physical source space

All arithmetic functions are on ALL positive integers, with ordinary Dirichlet
convolution `(a*c)(n)=sum_(d|n) a(d)c(n/d)`. Let `1(n)=1`, let `delta` be its
convolution identity, and let mu be the ordinary Mobius function: `1*mu=delta`.
A superscript 2 below means convolution square only when written `a*a`.

For a finite real source a set

    P_a(s)=sum_n a_n n^(-s),  A_a(x)=sum_(n<=x) a_n,
    h_a(t)=e^(-t/2) A_a(e^t), t>=0,
    J(a)=integral_1^infinity A_a(x)^2 dx/x^2.

Every support term and the whole terminal tail are included. Finite summation
and integration give

    J(a)=sum_(k>=1) A_a(k)^2/[k(k+1)]
        =sum_(m,n) a_m a_n/max(m,n).                       (0.1)

For an infinite arithmetic source we use J only after establishing the actual
cumulative function is locally square integrable and its entire norm finite.
No positive divisor kernel is substituted for (0.1).

For Y>=1 integral, write b=Y+1 and

    M(k)=sum_(n<=k) mu(n),
    E_Y=sum_(k=1)^Y M(k)^2/[k(k+1)],
    u_Y=sum_(k=1)^Y M(k)/[k(k+1)]
       =sum_(n<=Y)mu(n)/n - M(Y)/b.                       (0.2)

E is the immutable prefix energy in PR836. The signed mean u is a separate
coordinate; small energy is not permission to delete it. Define

    A_Y=E_Y+2b u_Y^2.                                    (0.3)

A_Y is a scalar, not the cumulative function A_a(x). In this packet it is
the norm of the canonical balanced state defined next.

## 1. BNR26-1: two moments, exact compact minimization, and the price

Put M=M(Y), m=sum_(n<=Y)mu(n)/n. Define c=c^(Y) by

    c_n=mu(n) for 1<=n<=Y,
    c_b=M-2b m,   c_(2b)=2b m-2M,
    c_n=0 at all other n>Y.                              (1.1)

Both boundary coefficients are rational and determined by the KNOWN prefix.
Exactly,

    sum_n c_n=0,   sum_n c_n/n=P_c(1)=0.                  (1.2)

Its cumulative function is M(k) for integer k<=Y, is `-2b u_Y` on
`b<=k<2b`, and is zero for k>=2b. Thus

    J(c)=E_Y+2b u_Y^2=A_Y.                               (1.3)

### Exact optimum

Among finite real a preserving EVERY coefficient through Y, supported at
indices <=2b, and satisfying both conditions (1.2), c is the unique minimizer
of J. For every such a,

    J(a)=A_Y+J(a-c).                                     (1.4)

Indeed summation by parts, using zero total, gives
`P_a(1)=sum_(k<2b) A_a(k)/[k(k+1)]`. The unknown tail cells b,...,2b-1 have
weight sum `1/b-1/(2b)=1/(2b)`. Their weighted mean must equal -u_Y.
Cauchy--Schwarz makes their energy at least `2b u_Y^2`, with equality exactly
for the constant cumulative tail `-2b u_Y`. Equality determines every coefficient.
The source difference has zero weighted tail mean; it is orthogonal to this
constant tail and to the unchanged prefix. This proves (1.4).

This is a constrained extension of PR836's causal projection, NOT a free
cancellation of early energy. With only P_a(1)=0 and unrestricted later support,
that packet's optimum is `F_Y=E_Y+b u_Y^2`; compact support and zero total here
pay the additional `b u_Y^2`. Both costs remain in all subsequent estimates.

## 2. BNR26-2: exact prefix squaring and invariance under late completion

For ANY finite c agreeing with mu through Y, not necessarily (1.1), define

    e=delta-1*c,   N(c)=2c-1*c*c.                         (2.1)

These operations are locally finite coefficientwise, even though N(c) need
not have finite support. The exact ring identity is

    mu-N(c)=mu*e*e.                                     (2.2)

Proof: `c=mu*(delta-e)`. Expanding `2c-1*c*c` gives
`mu*(delta-e*e)`. Since e(n)=0 for n<b, its convolution square vanishes below
b^2. Therefore, with B=b^2-1,

    N(c)(n)=mu(n) for EVERY 1<=n<=B,                     (2.3)
    mu(b^2)-N(c)(b^2)=e(b)^2.                            (2.4)

The endpoint in (2.4) is not silently included. It can fail, and does fail in
small accepting controls. For Y=1, balanced c is `(c_1,c_2,c_4)=(1,-3,2)`;
N(c)(4)=-4 while mu(4)=0.

### Why balancing the input does not change the reconstructed arithmetic

If d is any finite alteration supported at n>=b, then exactly

    N(c+d)-N(c)=2e*d-1*d*d.                              (2.5)

Both terms vanish below b^2. Thus tail choices can enforce (1.2) WITHOUT
altering any output coefficient in (2.3). This is an exact support statement,
not a small-error assertion or a probabilistic resampling of the Mobius signs.

### The actual recursive map

Discard N(c) only after retaining its ENTIRE prefix through B, and apply the
explicit rule (1.1) at scale B to that prefix. The result is exactly c^(B).
Starting with the seed mu(1)=1 gives the cutoff ladder

    Y_0=1, Y_(j+1)=(Y_j+1)^2-1:
    1, 3, 15, 255, 65535, ... .                          (2.6)

No future Mobius value, zero, or inverse-zeta oracle enters this recursion.
Its arithmetic complexity is not claimed better than established methods.
Huxley--Watt equations (1.5)--(1.10), with Vaughan/Linnik/Heath-Brown antecedents,
are credited for short-source inversion. PR805 already uses a balanced Newton
hierarchy on odd integers. Neither earlier identity supplies the norm gain
proposed below, and neither is refuted by this change of normalization.

## 3. BNR26-3: every quadratic raw stage has a legitimate whole norm

Now take the balanced compact c in (1.1), set v=N(c), and let V(x) be its
actual cumulative function. Complete finite rearrangement gives

    V(x)=2 A_c(x)-sum_(r,s) c_r c_s floor(x/(rs)).        (3.1)

For x>=2b, the first term is zero. The linear floor part also vanishes:

    sum_(r,s) c_r c_s x/(rs)=x (sum c_r/r)^2=0.

Let `psi(t)={t}-1/2`, with psi(INTEGER)=-1/2. Since `(sum c_r)^2=0`, the
constant part vanishes too. In fact for ALL real x>=1,

    V(x)=2 A_c(x)+sum_(r,s)c_r c_s psi(x/(rs)).            (3.2)

In particular, with L1c=sum |c_r|,

    |V(x)| <= (L1c)^2/2 for x>=2b,
    integral_X^infinity V(x)^2 dx/x^2 <= (L1c)^4/(4X),
                                      X>=2b.            (3.3)

Thus each quadratic stage is an ordinary global L2 source, despite its
infinite coefficient support. This tail bound does NOT assert that its norm
is small uniformly as Y grows. Higher Newton powers are not assigned the
same domain conclusion without a separate proof.

On Re s>1, finite Dirichlet algebra gives

    P_v(s)=2P_c(s)-zeta(s)P_c(s)^2.                      (3.4)

The Mellin representation `P_v(s)=s integral_1^infinity V(x)x^(-s-1)dx`
continues analytically to Re s>0 by (3.3). At s=1 the right side of (3.4)
vanishes: P_c(1)=0 and zeta has only a simple pole there. Hence

    integral_1^infinity V(x) dx/x^2=0.                   (3.5)

The same weighted-tail Cauchy--Schwarz argument as in Section 1, now for the
infinite cumulative source after B, yields

    F_B=E_B+(B+1)u_B^2 <= J(v),
    A_B=E_B+2(B+1)u_B^2 <= 2J(v).                        (3.6)

So recompletion is justified in the physical norm with an absolute factor
two. It is not an iteration of one fixed controller's full-line residual.
PR812's fixed-controller obstruction remains operative for its own class.

## 4. BNR26-4: the literal joint energy/mean update

For b<=k<b^2, (2.3) says V(k)=M(k). Define quantities computed solely from c:

    I_Y=sum_(k=b)^(b^2-1) V(k)^2/[k(k+1)],
    L_Y=sum_(k=b)^(b^2-1) V(k)/[k(k+1)].                  (4.1)

Then exactly

    E_B=E_Y+I_Y,   u_B=u_Y+L_Y,
    A_B=E_Y+I_Y+2b^2(u_Y+L_Y)^2.                        (4.2)

For k>=2b, V(k) is the centered hyperbola quadratic form in (3.2), with BOTH
rank-one terms removed. On the collar b<=k<2b, keep `2A_c(k)=-4b u_Y`.
Removing that collar changes the actual scalar. I_Y is nonnegative; L_Y is
signed and is not independently assumed to cancel u_Y.

### Integer discontinuities matter

Let psi0 be the midpoint Fourier sawtooth: psi0(t)=psi(t) off the integers,
psi0(integer)=0. Then the exact relation is

    sum c_r c_s psi(k/(rs))
      =sum c_r c_s psi0(k/(rs))
        -(1/2) sum_(rs|k)c_r c_s.                       (4.3)

An argument using a symmetric Fourier series must retain this divisor-boundary
term. It is not zero merely because both moments in (1.2) vanish. The checker
reconstructs all these endpoint terms in the declared finite corpus.

The Huxley--Watt decomposition `floor(x/rs)=x/(rs)-1/2-psi(x/rs)` is classical.
Here (1.2), (2.5), and (4.2) place it in one exact, repeatedly recompleted
full-energy source. They do not prove cancellation of the centered form.

## 5. BNR26-5: an explicit full-proof target, including vanishing gains

The principal OPEN target is a source-specific nonlinear estimate on the
canonical states, not an operator bound for arbitrary balanced vectors.
One concrete sufficient form is, on all sufficiently late stages of (2.6),

    1+A_B <= 2(1+A_Y)^(3/2).                             (G)

The finite pilot tests (G) only at 66 declared Y. It does not prove any
unbounded-scale instance. The constants in (G) are a proposed target, not a
claimed sharp law or a fit accepted as a theorem.

### Conditional conclusion for a fixed gain

More generally suppose fixed C>=1,K>=0 and 0<delta<1 give

    1+A_B <= C (log b)^K (1+A_Y)^(2-delta)               (5.1)

at every sufficiently late ladder stage (increase C to absorb finitely many
initial exceptions). Let t_j=log(Y_j+1)=2^j log2 and
F_j=log(1+A_(Y_j)). Then

    F_(j+1) <= (2-delta) F_j+O(j+1).

Solving this scalar recurrence gives `F_j=O((2-delta)^j)`. Thus, writing
`theta=log_2(2-delta)<1`,

    E_(Y_j) <= A_(Y_j) <= exp(O(t_j^theta)).              (5.2)

The constants may depend on the claimed gain. Monotonicity of E and
`t_(j+1)=2t_j` extend (5.2), with adjusted constants, to every large cutoff.
This gives E_X=X^o(1). For (G), theta=log_2(3/2).

### A uniform positive gap is not necessary

Suppose instead `0<=delta_j<=1`, `C_j>=1`, and eventually

    1+A_(Y_(j+1)) <= C_j(1+A_(Y_j))^(2-delta_j),
    sum_j delta_j=infinity,
    sum_j 2^(-j)log C_j <infinity.                       (5.3)

Then also E_X=X^o(1). Divide the logarithmic recurrence by 2^(j+1):

    f_(j+1) <= (1-delta_j/2) f_j + 2^(-j-1)log C_j.

Every fixed initial term is killed by the divergent accumulated gain.
The summable forcing tail is arbitrarily small, uniformly in later j.
Splitting the finite early part from that tail proves f_j->0. Monotonicity
again extends the conclusion from the ladder to all cutoffs. For instance,
a gain of order 1/(j+1) and polynomial-in-j logarithmic losses would suffice.
No such arithmetic sequence of gains is supplied here.

### Complete implication to RH, without the earlier factorial consumer as a premise

If E_X=X^o(1), set for Re s>1/2

    F(s)=integral_1^infinity M(x)x^(-s-1)dx.              (5.4)

For each closed smaller half-plane Re s>=sigma>1/2 choose epsilon<2sigma-1.
Cauchy--Schwarz on each dyadic interval gives

    integral_(2^j)^(2^(j+1)) |M(x)|x^(-sigma-1)dx
      <= [integral M(x)^2 dx/x^2]^(1/2)
         [integral x^(-2sigma)dx]^(1/2)
      =O(2^(j(epsilon/2+1/2-sigma))).                   (5.5)

The energy integral through an integer endpoint is bounded by the corresponding
E, so the series is uniformly summable on compact subsets. Inserting powers
of log x proves differentiation is legitimate as well. F is holomorphic in
Re s>1/2. For Re s>1, ordinary absolute Mobius inversion gives
`s F(s)=sum mu(n)n^(-s)=1/zeta(s)`.

The identity theorem, applied to the holomorphic product after cancelling the
pole at 1, therefore gives

    (s-1) zeta(s) s F(s)=s-1, Re s>1/2.                 (5.6)

A nontrivial zero rho in that half-plane would make the left side zero and
the right side rho-1 nonzero. This is impossible. The functional equation
reflects any left-of-line nontrivial zero to that half-plane. Thus RH follows.
No finite zero list, simplicity, PNT error bound or random signs are involved.

The entire unproved step is (5.1) or (5.3) FOR THE LITERAL CANONICAL SOURCES.
Neither well-definedness of the map nor its exact coefficient reproduction
establishes that step. No converse claiming these particular gain laws follow
from RH is asserted.

## 6. BNR26-6: double balance alone cannot deliver subquadratic gain

An exact non-Mobius control prevents a generic shortcut. For each EVEN b>=16
let the fake prefix be a_1=1, a_2=...=a_(b-1)=0. Its balanced compact completion
is

    c_1=1, c_b=1-2b, c_(2b)=2b-2,
    J(c)=2b-3+1/b <=2b.                                 (6.1)

It satisfies BOTH (1.2). For b^2/2<=k<b^2, all products of two late indices
are outside the floor sum, and A_c(k)=0. Thus

    V(k)=-k-2(1-2b)floor(k/b)-2(2b-2)floor(k/(2b)).       (6.2)

Set t=floor(k/b). If t is even, V=-k+2bt; if t is odd,
V=-k+2b(t+1)-2. Both are at least k-2b, hence at least k/2 since k>=4b.
Consequently

    sum_(k=b^2/2)^(b^2-1) V(k)^2/[k(k+1)]
        >= b^2/16 >= J(c)^2/64.                         (6.3)

For any fixed delta>0, no estimate by a fixed constant times a power of log b
and `(1+J(c))^(2-delta)` holds on this entire balanced class. The power-two
barrier survives the exact removal of both explicit rank-one modes.

These fake prefixes fail the inverse relations `sum_(d|n)c_d=delta_(n=1)`
inside the prefix. They are NOT counterexamples to (G), to (5.1) on actual
mu, or to RH. The missing proof must exploit that literal arithmetic, rather
than only moment cancellation, a positive norm, or small continuum kernels.

## 7. What this attempt supplies and what it does not

Supplied: a unique canonical compact state and its full cost; exact prefix
squaring invariant under late source choices; a legitimate whole quadratic
stage and certified tail; a two-coordinate immutable-prefix update; a full
conditional RH argument allowing nonuniform gains; and a generic quadratic
countermodel. These are proposed component proofs, not a completed RH proof.

Not supplied: a native unbounded subquadratic gain, a uniformly bounded
full-line controller, a new zero-free region, or a proof that generic balanced
source inequalities transfer to mu. The separate finite pilot is a falsifiable
starting point, not statistical justification for (G). The boundary between
the exact renormalization and its unknown energy growth is explicit.
