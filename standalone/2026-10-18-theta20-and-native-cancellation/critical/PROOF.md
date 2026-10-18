# One fixed shift is a bounded bridge to the complete native source

Status: PROPOSED complete component proofs; independent review required.
Scope: exact source identities and all finite-horizon critical Lp norms, not
a new arithmetic upper estimate and not an RH proof. All infinite Gaussian
tails and all ideal factorizations are retained. The additional arithmetic
results in ARITHMETIC.md concern the ordinary integer source only.

## 1. Literal sources and norms

Fix a number field F, a finite set S of prime ideals, and real c. Ideals are
nonzero integral ideals outside S; equal norms do not identify ideals. Put
Z(s)=zeta_F^S(s), with residue kappa at one, and

    W_c(y)=y^(-c) exp[-(log y)^2/4]/(2 sqrt(pi)),
    A(X)=sum_I mu_F(I) W_c(NI/X),
    a_h(I)=sum_(DE=I) mu_F(D)(NE)^(-h),
    S_h(X)=sum_I a_h(I) W_c(NI/X), h>0.

Here A is the unchanged native Mobius Gaussian. The coefficient a_h is the
specified deformation from #980/#991, not a new notation for mu_F. Common
prime factors in D,E remain. Every source converges absolutely for each X>0,
locally uniformly together with its X derivatives: fixed-field ideal counting
and Gaussian decay dominate every fixed divisor or logarithmic power.

For 1<=p<infinity define the all-past critical norm

    N_p(f;T) = (integral_0^T |f(X)/sqrt(X)|^p dX/X)^(1/p),

and use the essential supremum for p=infinity. For every finite T these
norms of the displayed sources are finite. Gaussian flatness at X=0 is part
of that assertion. Replacing the lower endpoint 0 by 2 changes a root norm
by a fixed finite quantity, independent of T.

## 2. An exact two-sided causal dilation identity

### Theorem 1

For every fixed h>1/2, every 1<=p<=infinity and every T>0,

    N_p(S_h;T) <= Z(h+1/2) N_p(A;T),
    N_p(A;T) <= [Z(h+1/2)/Z(2h+1)] N_p(S_h;T).          (1)

The SAME constants work for every p and T. No zero-free theorem is used.
There is no shift tending to zero, moment-order loss or growing logarithmic
amplification. This is a bounded projection between these precise complete
sources, not a projection of the full physical CT operator.

Proof. Absolute Gaussian convergence permits Dirichlet convolution in the
literal source sums and gives

    S_h(X)=sum_E (NE)^(-h) A(X/NE),
    A(X)=sum_E mu_F(E)(NE)^(-h) S_h(X/NE).                (2)

The second identity follows because the Dirichlet inverse of I -> (NI)^(-h)
is I -> mu_F(I)(NI)^(-h). It includes every prime power. On dividing by
sqrt(X), a dilation coefficient becomes (NE)^(-h-1/2). For a finite partial
sum, Minkowski and Y=X/NE show that the norm of each term on (0,T) is at most
its absolute coefficient times N_p(A;T), or N_p(S_h;T), respectively; the
actual upper endpoint is T/NE<=T. The absolutely summable coefficients allow
the finite sums to converge in Lp; for p=infinity the same argument is the
uniform triangle inequality. Finally

    sum_E (NE)^(-h-1/2)=Z(h+1/2),
    sum_E |mu_F(E)|(NE)^(-h-1/2)=Z(h+1/2)/Z(2h+1).

These Euler products are in their absolute half-plane. This proves (1).
The hypothesis h>1/2 is exactly what makes this absolute dilation argument
summable. No impossibility result for h<=1/2 is asserted. QED.

### Ordinary zeta specialization

For F=Q and S empty, one can take the single shift h=1. Then

    a(n)=a_1(n)=n^(-1) product_(p|n)(1-p), a(1)=1,
    a(p^j)=-(p-1)/p^j, j>=1.                            (3)

In particular |a(n)|<=1, and all prime powers remain. Formula (1) becomes

    N_p(S_1;T) <= zeta(3/2) N_p(A;T),
    N_p(A;T) <= [zeta(3/2)/zeta(3)] N_p(S_1;T).         (4)

These are fixed small constants, not asymptotic powers of T.

## 3. The complete continuum is a bounded, explicit correction

When h>1/2 and Z(1-h) is finite and nonzero, put

    k_h=-kappa/[h Z(1-h)],
    J_h(X)=integral_1^infinity y^(-h) W_c(y/X) dy,
    B_h(X)=[W_c(1/X)-S_h(X)]/h-k_h J_h(X),
    R_h(X)=W_c(1/X)-h k_h J_h(X).

Thus S_h=-h B_h+R_h EXACTLY. This is the complete one-sided continuum,

    J_h(X)=(1/2) X^(1-h) exp[(1-h-c)^2]
                    erfc[-(log X+2(1-h-c))/2].          (5)

It is not replaced by its large-X exponential. Every N_p(R_h;infinity) is
finite, uniformly bounded over 1<=p<=infinity after the fixed h,c are chosen.
At infinity J_h=O(X^(1-h)); at zero the one-sided Gaussian makes it flat to
every power. The unit Gaussian has the same flatness at both endpoints.
A bounded function in L1 has Lp norm at most max(L1,Linfinity), proving the
uniform-in-p assertion for these critical normalized functions.

Consequently (1) also gives, simultaneously for all finite horizons,

    N_p(A;T) <= [Z(h+1/2)/Z(2h+1)]
                            [h N_p(B_h;T)+N_p(R_h;infinity)],
    h N_p(B_h;T) <= Z(h+1/2)N_p(A;T)+N_p(R_h;infinity). (6)

For ordinary zeta h=1 is legal because zeta(0)=-1/2, and k_1=2. Thus B_1
includes the exact correction 2 J_1, whose limiting size is constant and
whose critical norm is finite. For a general field or S, h=1 can fail the
nonzero-value condition. The raw-source theorem (1) needs no such condition.
One universally available centered choice is h=3/2: the functional equation
and the Euler half-plane imply Z(-1/2)!=0; no gamma or finite-S Euler factor
has a zero or pole there. This fixed-field assertion does not make a claim
about zeros inside the critical strip.

For a check on the full continuum normalization, set v=c-1/2 and b=h-1/2>0.
Gaussian integration (equivalently Mellin Plancherel on Re s=1/2) yields

    N_2(J_h;infinity)^2
       = exp(2v^2+2b^2) erfc(sqrt(2)b)/(2b),
    N_2(W_c(1/X);infinity)^2=exp(2v^2)/(2 sqrt(2 pi)),
    <W_c(1/X),J_h>_critical=b N_2(J_h;infinity)^2.       (7)

For example, the Mellin transforms are exp[(s-c)^2] and
exp[(s-c)^2]/(s+h-1). Their products reduce (7) to the Gaussian integral
of 1/(b^2+t^2); evaluation follows by writing its reciprocal as a Laplace
integral and completing the square. All functions are in the stated L2
space, so this computation does not invoke an unknown zeta boundary value.

## 4. A single SMALL shift also detects every zero, globally

The fixed-shift average in #991 gives a valid direct local pole test. It is
not necessary for the qualitative global implication below. A numerator
can cancel a particular denominator zero at one shift, but it cannot cancel
an entire forward chain of zeros of a zeta function.

### Theorem 2

Fix ANY h>0 for which Z(1-h) is finite and nonzero, and define B_h as above.
Then the condition

    integral_2^T |B_h(X)|^2 dX/X^2 <<_epsilon T^epsilon
                         for every epsilon>0           (8)

is equivalent to the Riemann hypothesis for zeta_F. The estimate (8) is not
proved here. For h>1/2, (6) is the stronger quantitative native-source bridge.

Proof of sufficiency. The full Gaussian sources are flat at zero. Cauchy on
each dyad [R,2R], using (8), gives local normal convergence of the Mellin
integral on Re s>1/2, together with any fixed logarithmic derivatives. On
Re s>1 its exact value is

    exp[(s-c)^2] ((1-Z(s+h)/Z(s))/h-k_h/(s+h-1)).        (9)

The stipulated k_h cancels the full shifted numerator pole at 1-h. Let rho
be a zero of Z in Re s>1/2. It is not 1-h by the hypothesis on that value.
Holomorphy of (9) implies that Z(rho+h)=0 of at least the same multiplicity:
otherwise the quotient would retain a pole (a numerator pole would also
contradict holomorphy). Apply the same argument at rho+h, and continue.
After finitely many steps the real part exceeds one, where Z has no zeros.
This contradiction excludes every such rho without assuming a rightmost,
simple or separated zero. The functional equation proves field RH.

Proof of necessity. Assume field RH, choose a fixed line sigma=1/2+eta, and
move the full Gaussian Mellin contour to it. The denominator is zero-free
there; standard fixed-field reciprocal bounds in that half-plane and the
Gaussian control the entire vertical tail. Choose eta so sigma!=1-h when
needed. The explicit subtraction cancels that pole during the movement.
Thus B_h(X)=O_eta(X^(1/2+eta)). Integrating and then taking eta<epsilon/2
gives (8). This is the classical RH-assuming Gaussian contour argument; it
is not an unconditional reciprocal estimate. QED.

For F=Q, S empty this is ordinary RH. For a general field it is field RH,
a stronger statement in general; no converse from ordinary RH is asserted.

## 5. What this advances and the exact remaining estimate

#991 pays a logarithmic endpoint extraction cost for its small-shift average.
Theorem 1 supplies an exact bounded transfer from ONE fixed shift directly to
the complete unchanged native source, with all constants independent of the
horizon and moment order. Theorem 2 shows why isolated numerator cancellation
does not obstruct a one-shift global criterion. Neither conclusion uses CT,
de Faveri, a family mean, an exceptional set, or a cap on reciprocal values.

Theorem 1 does NOT bound either side at critical size. ARITHMETIC.md takes
the next step for the actual integer coefficients (3): it derives the full
quadratic kernel, proves its logarithmic diagonal, applies a published signed
correlation theorem to every fixed additive band, and computes the whole
infinite divisibility sector. The remaining nondivisibility correlations
still need a critical upper bound. No physical theta-to-native projection
or new fixed-member zero-free region has been established.
