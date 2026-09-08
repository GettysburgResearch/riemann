# OEC26 — Abel continuation, two failed upper bounds, and the exact endpoint

Status: PROPOSED COMPONENT PROOFS; the unconditional entropy estimate and RH
remain unproved. This records the attempted completion rather than leaving it
to an independent reviewer to invent. Notation is that of PROOF.md.

<a id="1"></a>

## 1. A second construction: average the logarithm, not the Euler product

Let 1/2<=b<1 and epsilon>0. Suppose the NONNEGATIVE moment

    integral_2^infinity E_b(X)X^(-1-epsilon)dX < infinity.       (1)

Define the finite, entire-in-s discrepancy transform

    C_X(s)=sum_(p<=X)p^(-s)-integral_2^X x^(-s)dx/log x,

and its Abel average

    T_epsilon(s)=epsilon integral_2^infinity
                       C_X(s)X^(-1-epsilon)dX.                 (2)

**Theorem OEC26.T5.** Under (1), (2) is holomorphic on Re s>b. On that domain,
with w=s+epsilon, the explicitly constructed analytic function

    J_epsilon(s)=T_epsilon(s)+a_*(w)+V_infinity(w),
    a_*(w)=-gamma-log(log2)+Ein((w-1)log2),
    V_infinity(w)=sum_(p,k>=2)p^(-kw)/k,

satisfies

    exp(J_epsilon(s))=(w-1)zeta(w).                            (3)

Thus (1) proves nonvanishing of zeta on Re w>b+epsilon. Its removable value
at w=1 is 1. Requiring (1) for every epsilon>0 proves nonvanishing on Re w>b.
In particular this gives a second proof of the Abel-moment implication to RH
at b=1/2, without taking a limit of zero-free functions.

### Convergence and branch details

The Schwarz formula from PROOF.md implies on every compact K in Re z>0

    |h_X(z)|<=C_(b,K)[1+E_b(X)].                               (4)

To see this without bounding an arbitrary harmonic conjugate, subtract its
value at z=1. The integral kernel is

    1/(z-it)-1/(1-it).

On K its modulus is at most a constant times (1+t^2)^(-1): the numerator is
1-z and both denominators grow linearly in t, while finite t are handled by
Re z bounded below. Equation (8) of PROOF.md pays the full absolute logarithm.
The value h_X(1) is real and uniformly bounded. This proves (4).

For a compact subset of Re s>b, V_X(s) is uniformly bounded in X because
2Re s>1. Formula (25) of PROOF.md therefore bounds C_X(s) by C_K(1+E_b(X)).
Condition (1) gives locally uniform absolute convergence in (2). Morera's
theorem (or differentiation on smaller compact sets) makes it holomorphic.
No a priori analytic logarithm of actual zeta in this domain was used.

First work in Re s>1, where absolute integration permits interchange in (2).
The weight is NOT normalized to mass one: its total mass is 2^(-epsilon).
For each p>=2,

    epsilon integral_p^infinity X^(-1-epsilon)dX=p^(-epsilon).

The identical factor appears in the continuous term, so

    T_epsilon(s)=sum_p p^(-w)-E1((w-1)log2).                   (5)

All prime-2 endpoint mass is included. By the elementary E1/Ein relation,

    a_*(w)-E1((w-1)log2)=log(w-1)

in Re w>1. Adding the full higher-prime-power series in (5) therefore gives
log[(w-1)zeta(w)] in that initial half-plane. Exponentiation proves (3) there.
Both sides of (3) are analytic throughout Re s>b, since (w-1) cancels zeta's
only pole. The identity theorem gives (3) everywhere, proving zero-freeness.
This continuation does not continue an arbitrarily chosen logarithm through
a hypothetical zero; the zero-free exponential is constructed first from (1).

<a id="2"></a>

## 2. Why this is a real weakening, and not an RH proof

OE26 required a sublogarithmic boundary cost on shifted lines to use a generic
normal-family propagation theorem. The additional arithmetic horizon in the
logarithmic DERIVATIVE now proves that a single subpower subsequence at b=1/2
suffices. The all-cutoff lower bound in PROOF.md is what permits that subsequence;
(1) alone gives an averaged variant, not a pointwise monotonicity theorem.

For example, a prospective bound

    E_(1/2)(X)<=exp(sqrt(log X))

would meet the new criterion, even though it is much larger than log X. No
such bound is established. Enlarging the class of sufficient estimates is
not the same as proving that the actual arithmetic belongs to that class.
The new criterion is still equivalent to RH.

The norm bound in PROOF.md contains C_sigma=2+2/sigma^2. Setting sigma=0
would be invalid. No such limit is used: for a hypothetical zero at depth d,
one FIXED 0<sigma<d is enough. The resulting admissible vectors are in the
source domain at alpha=b+sigma, not silently in the domain at b itself.
Excluding every right-of-line zero would then give the domain completeness
from the preceding Hardy factorization, but that exclusion is not proved here.

<a id="3"></a>

## 3. Attempt 1: estimate the arithmetic discrepancy with known PNT input

All the remaining growth in (4) comes from

    C_X(s)=integral_[2-,X] x^(-s)/log x d(theta(x)-x).

The endpoints, the real continuum subtraction, and all prime powers in V_X
are fixed before estimating. Integrating by parts on the logarithmic coordinate
u=log x gives a boundary term plus transforms of

    f_L(u)=exp(-bu)[theta(exp u)-exp u]/u,
                               log2<=u<=L=log X,

multiplied by b+iy, and the analogous f_L/u term. Cauchy-Schwarz against the
Cauchy frequency weight and Plancherel bound their weighted L1 contribution
by constants times the endpoint size, ||f_L||_2 and ||f_L/u||_2.

The classical unconditional PNT remainder

    |theta(x)-x|<=C x exp(-c sqrt(log x))

therefore gives, for each fixed 0<b<1,

    E_b(X)<=C_b[1+X^(1-b)exp(-c_b sqrt(log X))].               (6)

For b=1/2, the higher-prime-power contribution is at most O(1+log X), which
can be absorbed into (6). The full high-frequency tail is treated using the
finite-product bound, exactly as in PROOF.md. Alternatively the weighted
L2 argument treats the linear discrepancy at all frequencies at once.
Split the u-integral at L/2 to verify the exponential remainder in (6): the
first half loses a fixed exponential in L; on the second half use
sqrt(u)>=sqrt(L/2). Constants exist but are not numerically certified here.
This is a restatement/application of a classical-scale estimate, not a new
fixed-power saving or a new zero-free region.

At b=1/2, (6) is still X^(1/2-o(1)), not X^o(1). Insert (6) into the Abel
moment (1). It pays epsilon>=1-b, including equality because
integral exp(-c sqrt L)dL converges. The resulting domain is only Re w>1,
where the Euler product already supplies zero-freeness. It does NOT pay the
moments for every epsilon>0. No complete RH path follows from (6).

<a id="4"></a>

## 4. Attempt 2: use a signed logarithmic mean or causal passivity

The signed boundary mean is exactly h_X(1), uniformly bounded. But

    (1/pi) integral |U_X|/(1+y^2)=2E_b(X)-h_X(1).

A bounded signed mean leaves the positive logarithmic cost uncontrolled.
This is not a zeta-specific obstruction: h_A(z)=A exp(-Lz) has signed mean
A exp(-L) at z=1. Its positive boundary mean is at least A/4: use
(cos t)_+=(|cos t|+cos t)/2, |cos t|>=cos^2 t, and the exact Cauchy-weighted
means of cos(Ly) and cos^2(Ly), namely exp(-L) and (1+exp(-2L))/2.
Taking A=exp(L/2) makes the signed mean tend to zero while the positive cost
diverges. This is a synthetic analytic log, not the actual Euler source.
For the actual causal quantity, (8) of PROOF.md makes the missing absolute
control explicit rather than hiding it.

Likewise the entropy-to-Hardy theorem is an UPPER bound for the norm of q_X
in terms of E_b(X). Positivity of a source Gram or its stored energy gives
no reverse bound on E_b. Reversing that implication would simply assume the
new target. The full signed forcing in (14), particularly the continuous
part and the complete prime jump part, must be estimated together.

These two attempts do not produce the needed upper estimate. No generic
impossibility of a different arithmetic argument is asserted.

<a id="5"></a>

## 5. Exact final obligation and status

One sufficient end-to-end statement is now

    there exist X_j->infinity with
    log(1+E_(1/2)(X_j))/log X_j ->0.                           (7)

If (7) were proved, PROOF.md excludes every off-line zero with full
multiplicity; reflection gives RH. The source domain is then full and the
previous critical convolution becomes the claimed full-domain isometry.
This completes the deduction AFTER (7), not a proof of (7).

The constructions, norm bounds, power obstruction, conditional converse and
Abel continuation are supplied in full. The assertion (7), the minimum-phase
upper defect estimate, and unconditional RH remain unproved. A new entropy
integral, a finite source identity, or an isolated numerical cutoff is not
reported as their completion. The next proof task is genuinely arithmetic:
control the positive part of the compensated prime logarithm on one unbounded
subsequence, or prove all its positive Mellin moments finite.
