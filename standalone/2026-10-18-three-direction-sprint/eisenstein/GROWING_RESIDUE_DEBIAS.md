# A growing family of legal residue-cancelling probes

**PROPOSED source-qualified theorem.** This strengthens the scalar tail
counterterm to a growing set of arithmetic divisibility constraints. It
annihilates the complete polar functionals for squarefree numerator labels
in that range. The continuous primitive remainder and the full mixed
covariance remain unproved; no new zeta boundary is asserted.

All ideals are good integral ideals of `E=Q(omega)`, with the same fixed
finite bad set and primary convention as `TAIL_DEBIASED_MOLLIFIER.md`.
Write `q_a=Na`, and

    v(a)=product_(p|a) q_p^2/(q_p^2+q_p-1),
    f(a)=product_(p|a) 1/(q_p+1)                 (a squarefree).

Let V be smooth, equal to one on `[0,1]`, and zero on `[2,infinity)`.
Let W be nonnegative, smooth, nonzero, and supported in `(2,3)`.
Assume a fixed `1/2<beta<1` such that the fixed-field zeta reciprocal
has no poles on `Re s>beta` and has polynomial vertical bounds on every
closed half-plane `Re s>=beta+epsilon`. The working source bound allows
`beta=7/8`; no stronger zero-free input is used here. Equivalently one
may import the smoothed Mobius estimate (4) below as the precise input.

## 1. Exact construction and its resource

Fix `eta>0` and `1<=G<=D^(1/2-eta)`. For all sufficiently large D there
are real coefficients `xi_g`, indexed by ALL good squarefree `q_g<=G`,
including the unit, for which

    b_D(a)=mu(a)V(q_a/D)
          +mu(a)^2/v(a) W(q_a/D) sum_(g|a,q_g<=G) xi_g       (1)

satisfies the exact simultaneous identities

    F_g := sum_(g|a) b_D(a)v(a)/q_a = 0
                     (g squarefree, q_g<=G).                 (2)

It retains `b_D(a)=mu(a)` for `q_a<=D`, hence retains the complete unit
convolution on products of norm at most D. Every multiplier defined by
these coefficients is a finite Dirichlet polynomial. In particular it
cannot cancel a zero of the L-function it multiplies. The usual
principal-pole regularization, when needed, remains a separate part of
that detector interface.

For every prescribed positive epsilon the coefficients can be chosen
with

    (sum_g f(g)|xi_g|^2)^(1/2)
         << D^(beta-1+epsilon) G^(1-beta+epsilon),
    sum_g |xi_g|/sqrt(q_g)
         << D^(beta-1+epsilon) G^(3/2-beta+epsilon).            (3)

The pointwise tail coefficient in (1) is bounded by the second resource
in (3), times a prescribed subpower of D. These are complete sums over
the growing index set, not a fixed-label assertion.

### The prefix response

Let `Z_g=sum_(g|a) mu(a)V(q_a/D)v(a)/q_a`. Uniformly for squarefree g,

    |Z_g| << D^(beta-1+epsilon) q_g^(-beta+epsilon).           (4)

Indeed write `a=g c`, `(c,g)=1`. The Dirichlet series of `mu(c)v(c)`
with this mask is `zeta_E^S(s)^(-1)` times an Euler product absolutely
convergent for `Re s>0`, times
`product_(p|g)(1-v(p)q_p^(-s))^(-1)`. On `Re s>=beta+epsilon`
the last product is `O_epsilon(q_g^epsilon)`. Smooth Mellin inversion
at length `D/q_g` proves (4). The possible pole of the Mellin transform
of V at zero is cancelled by the zero of the zeta reciprocal at one.
All supported-prime factors are fixed. This proves (4) from the stated
zero-free/vertical input; it is not an additional cancellation hypothesis.

### The response matrix

The tail response matrix is exactly

    B_(g,h)=sum_([g,h]|a) mu(a)^2 W(q_a/D)/q_a.

The elementary ideal count and the squarefree sieve give, uniformly for
squarefree `l` of norm at most D,

    sum_(l|a) mu(a)^2 W(q_a/D)/q_a
       = c_W f(l)+O_epsilon(D^(-1/2)q_l^(-1/2)(Dq_l)^epsilon), (5)

where `c_W>0` is fixed. To see the uniform error, write `a=l c`, expand
squarefreeness of c by squares prime to l, and expand `(c,l)=1` over
divisors of l. The ideal counting error is
`O(sqrt(D/q_l)log(2D) sum_(e|l)q_e^(-1/2))` before harmonic smoothing.
Its main local factor is `1/(q_p+1)`. Partial summation gives (5).
Since `q_[g,h]<=G^2<D`, this covers the whole matrix.

The main matrix has the exact positive factorization

    f([g,h])=f(g)f(h) sum_(d|g,d|h) q_d.                     (6)

Its diagonal is f(g). After diagonal normalization, its least eigenvalue
is at least `C_epsilon G^(-epsilon)`. Here is a direct proof rather than
an assumed conditioning estimate. Set

    y_d=sqrt(q_d) sum_(d|g) f(g)xi_g.

The quadratic form in (6) is `sum_d|y_d|^2`. Divisor Mobius inversion
on the downward-closed squarefree set `q_g<=G` gives

    f(g)xi_g=sum_(g|d) mu(d/g)y_d/sqrt(q_d).

Cauchy with weights `q_(d/g)^(-1-epsilon)`, followed by the convergent
ideal series at `1+epsilon`, yields

    sum_g f(g)|xi_g|^2 <<_epsilon G^epsilon sum_d|y_d|^2.

The remaining sum over g dividing d is divisor-bounded; all small powers
may be chosen before the prescribed final epsilon.

After the same diagonal normalization the error in (5) is bounded by
`D^(-1/2)q_(g,h)^(1/2)G^epsilon` entrywise. The elementary Schur bound

    sum_(q_h<=G) sqrt(q_(g,h))
       <= sum_(d|g) sqrt(q_d) #{h:d|h,q_h<=G}
       << G sum_(d|g)q_d^(-1/2) <<_epsilon G q_g^epsilon

shows that its norm is `O(D^(-1/2)G^(1+epsilon))`. It is smaller than
the main least eigenvalue in the stated range. Thus B is invertible.
Solve `B xi=-Z`; this proves (2). The normalized inverse bound, (4),
and `f(g)^(-1)<<_epsilon q_g^(1+epsilon)` give

    ||xi||_f << G^epsilon (sum_g |Z_g|^2/f(g))^(1/2)
             << D^(beta-1+epsilon)G^(1-beta+epsilon).

Cauchy over the `O(G)` labels proves the second inequality in (3).
For the pointwise assertion, Cauchy over divisors of a uses
`sum_(g|a,q_g<=G)f(g)^(-1)<<G^(1+epsilon)q_a^epsilon`.

## 2. Analytic price of the complete tail

Use the SAME common row character, fixed finite twists, height profiles,
and all original zero extensions as in the pinned zero-slot TWO-PLAIN
source input of `TAIL_DEBIASED_MOLLIFIER.md`. Let `S_psi(N)` be its plain
factor, with any bounded polynomial length, and let `T_psi(D)` denote
the normalized polynomial contributed by the tail in (1). Then

    sum_rows |T_psi(D) S_psi(N)|^2
       << U^(1+epsilon) D^(2beta-2+epsilon)G^(3-2beta+epsilon)
                                                (1+height)^C. (7)

This bound is for the COMPLETE tail and its actual shared-prime masks.
It does not require inverse second moments at length D.

For each squarefree g, extract `a=g c`. Its term is
`psi(g)/(sqrt(q_g)v(g))` times the squarefree positive tail at length
`D/q_g`, with the input mask `(c,g)=1`. The unmasked positive tail has
the exact `L(s,psi)/L(2s,psi^2)` representation and absolutely convergent
correction already proved in the companion file. Adding this mask
multiplies its local series by
`product_(p|g)(1+v(p)^(-1)psi(p)q_p^(-s))^(-1)`.
At `Re s=1/2` its complete absolute coefficient mass is `O(g^epsilon)`;
the good primes have norm at least seven, so each geometric expansion
converges. Zero character values cause no division. Its remaining square
index has harmonic mass `O(log(2D))` at polynomially bounded lengths.
Minkowski and the zero-slot TWO-PLAIN estimate therefore bound each
g-term's joint root norm by `U^(1/2+epsilon)q_g^(-1/2+epsilon)`.
Summing with (3), BEFORE discarding any common mask or tail, proves (7).

In particular, with `beta=7/8` and

    G=D^(1/5-eta),

the root coefficient resource is `D^(-5eta/8+epsilon)`. The complete
correction costs only `U^(1+epsilon)` and its pointwise coefficients are
subpower. This applies even at the native full inverse cutoff
`D=U^(3/2)`: then `G=U^(3/10-3eta/2)`. No inverse row-size estimate at
that long cutoff is being imported. The count-union argument in
`TAIL_ROW_COUNTS.md` applies to this row-size correction with the same
profile qualifications. If instead `D=U,G=U^(3/10)`, (7) costs
`U^(9/8+epsilon)` and pointwise coefficients cost `U^(1/16+epsilon)`;
the unchanged-count conclusion is NOT asserted for that choice.

## 3. The actual squarefree-label polar functional

This section uses the exact fixed-form cusp and residue normalization
of rStation paper8/v1, Sections2--7 (pinned in NOTES.md). Write
`rho_prim(m)=w(m)rho_full(m)`, where
`w(m)=product_(p|m) q_p/(q_p+1)`. For every squarefree good R, consider
the global product-profile functional

    sum_a b_D(a) sum_(a|n) rho_prim(nR) Phi(q_n/X).            (8)

Its full polar term is

    C_[R] Z_S X^(5/6) q_R^(-1/6) v(R) Phihat(5/6)
       * sum_(g|R) c(g) F_g,
    c(g)=product_(p|g)(v(p)^(-1)-1)
        =product_(p|g)(q_p^(-1)-q_p^(-2)).                   (9)

`C_[R]` may depend on the fixed finite ray sector of R and the fixed
section/filter, but not on a. Thus (2) annihilates (9) for EVERY
squarefree `q_R<=G`, at once, for every admitted product profile.

Here is why no nonlocal character of a is hidden in (9). Change variables
`m=nR`; the progression modulus is `aR`. Since a and R are squarefree,
its prime valuations are at most two. In the finite cusp-constant
calculation for a progression, reduce every fraction to its primitive
denominator r dividing aR. For r not the unit, the character `chi_r`
on its unit group is nonprincipal: its local exponents are one or two,
never six. Its sum over that group is zero. Only r=1 supplies a constant,
with density `1/(q_a q_R)`. A fixed numerator ray filter changes its
cusp constant through the ray class of R, independently of a.

This constant-term argument DOES NOT use the false identity
`g(n,r)=g(1,r)bar chi_r(n)` for nonsquarefree r. In particular,
`g(1,p^2)=0` can coexist with nonzero `g(n,p^2)` at nonunit n. The
nonconstant Fourier transform and its errors must keep those terms.

For the primitive density expand `w=1*h`, with
`h(p)=-1/(q_p+1)` and h zero on higher prime powers. The progression
modulus becomes `[aR,d]`, still with valuations at most two. Its polar
density, including ALL shared primes, is

    sum_d h(d)/q_[aR,d]
       =Z_S v(rad(aR))/(q_a q_R).                           (10)

At a prime already in aR the factor is `(1+h(p))/q_p^e`; at any other
prime it is `1+h(p)/q_p`. These prove (10) directly. The same summable
density transfer as paper8 Section7 applies for each fixed R; its
constants for nonpolar errors are not asserted uniform in growing R.
Finally

    v(rad(aR))=v(a)v(R)/v((a,R)),
    v((a,R))^(-1)=sum_(g|a,g|R)c(g).

Together with the `q_R^(5/6)` change of product scale these identities
give (9).

This proves exact cancellation of a WHOLE growing squarefree-label
polar space with an affordable zero-preserving finite detector. It is
not an estimate for the corresponding continuous space. We do not
import paper8's squarefree-modulus Fourier error for aR: the modulus
can have exponent two. Quantitative nonconstant transforms for these
growing labels, and stability through subsequent twisted/reflected
children, are the remaining gates. A further character factor
`chi_a(Q)^k` or a separate outer Mellin height would require a new
functional; neither is silently declared cancelled by (2).

The finite checker accompanying this file verifies complete arithmetic
response matrices, their exact solutions and low-prefix invariants.
It supplies no evidence for a new global analytic covariance estimate.
