# Coherent quadratic place Euler source: the leading pole disappears, the elliptic scale survives

Status: proposed exact theorem for the already constructed S3 times C2
function-field cover. This is the full place-Euler product of the
coherent graded algebra R_n tensor chi^n. It is different from the
polynomial-growth product over finite cohomological grades, from the
fixed module R_n tensor chi, and from the ordinary exponential Lie
Fredholm parent. No new curve, automorphic representation, number-field
L-function or RH theorem is claimed.

The classical mechanisms are equivariant Koszul/PBW extraction, actual
finite-cover cohomology and Weil weights. The source-specific conclusion
is exact: the quadratic operation removes the main Q^n coefficient term
of the untwisted place Euler source, but the same elliptic denominator
P_E(z^2) gives the sharp remaining scale Q^(n/4).

## 1. Fix the actual coherent source before forming local factors

Use the frozen generic cubic cover

    x^3+A x+B=u^2,  char(F_Q)>3,
    A!=0,  -4A^3-27B^2!=0.

Its S3 Galois closure Z has genus three. Adjoin w^2=u, whose quadratic
character is chi. The joint cover Ztilde is geometrically connected
with group S3 times C2 and genus nine, as established in the
[actual ramified twist packet](RAMIFIED_TWISTED_GLOBAL_COMPLETION.md).
The quadratic cover is branched at u=0 and infinity; the cubic cover
is unramified at zero. The joint cover, rather than a table of signs,
is the source of every chi value and inertia projector below.

Let V be the two-dimensional standard representation and W the
three-dimensional permutation representation of S3. The actual algebra is

    A_n=Sym^n(V) tensor Sym^n(W) tensor chi^n
       =Sym^n(V tensor chi) tensor Sym^n(W).

Multiplication sends A_i tensor A_j to A_(i+j); it is the diagonal
colour/degree subalgebra of the two-colour construction. Its Koszul
Lie grades are exactly M_n tensor chi^n. This follows functorially from
the homogeneous grading, not by twisting each independent finite
cohomological factor by an arbitrarily chosen sign.

At every closed place v take full joint inertia invariants:

    F_(v,chi)(t)=sum_(n>=0) tr(phi_v | A_n^(I_v)) t^n,
    E_chi(z)=product_v F_(v,chi)(z^(deg v)).               (1.1)

At a good place with source Frobenius (h,epsilon), epsilon=+1 or -1,
the factor is F_h(epsilon t), where

    F_e(t)=(1+2t)/(1-t)^4,
    F_s(t)=(1-t^2)^(-2), F_c(t)=(1-t^3)^(-1).

Every factor has constant term one. This is why the coherent operation
defines a normalized Euler germ; simply multiplying every coefficient,
including grade zero, by a fixed chi(v) would be a different and generally
unnormalized operation.

## 2. The full ramified local factors

Write F_C2=(F_e+F_s)/2 and F_C3=(F_e+2F_c)/3. At an old finite
transposition branch place, chi is unramified and the factor is
F_C2(epsilon t), with its actual source sign epsilon.

At the new place u=0, inertia is the central quadratic involution.
Only even grades survive. If h_0 is the actual S3 Frobenius there,
the factor is the even part (F_(h_0)(t)+F_(h_0)(-t))/2. In s=t^2,
the three possibilities are

    h_0=e: (1+14s+9s^2)/(1-s)^4,
    h_0=s: 1/(1-s)^2,
    h_0=c: 1/(1-s^3).                                  (2.1)

At infinity the joint inertia is cyclic of order six and contains the
central quadratic involution. Again only even grades survive. For
Q=1 modulo 3 the local series is the even part of F_C3, namely

    (1+3s+10s^2+7s^3+3s^4)/((1-s)^4(1+s+s^2));          (2.2)

for Q=2 modulo 3 it is F_s(t)=1/(1-s)^2. No choice of the quadratic
Frobenius lift affects the surviving even grades. These are full
joint-inertia invariants, not invariants of V and W formed separately.

All these local functions are rational with no poles in |t|<1.
They are derived from the actual source; no ramification factors have
been selected to cancel an unwanted global pole.

## 3. Unit-disk continuation and its exact natural boundary

Apply the finite-group criterion in the
[source-corrected Segre theorem](S3_SEGRE_EULER_MEROMORPHIC_BOUNDARY.md)
to this actual joint cover and algebra. The finite extraction uses
the genuine compact-support factors

    product_(1<=n<=N) L_U(M_n tensor chi^n,z^n)^((-1)^(n+1)),            (3.1)

where U removes every branch point of the joint cover. The good local
remainder is 1+O(t^(N+1)); all exponents are integral. The finite bad
factors in Section 2 are kept exactly. Thus (1.1), initially convergent
near zero, has single-valued meromorphic continuation to |z|<1.
This does not extend the ideal domain of an infinite Lie operator.

The identity good factor still has the zero -1/2. The genus-nine
regular-cover count gives

    pi_split(d)=Q^d/(12d)+O(Q^(d/2))>0

for every sufficiently large d. At a completely split degree-d place,
the zeros z^d=-1/2 survive: finite cohomological weight circles have
radii 1, Q^(-1/(2n)) or Q^(-1/n), none equal to 2^(-1/d) for odd Q.
Other local factors have no poles inside the unit disk. These zeros
accumulate at every point of |z|=1, proving a meromorphic natural boundary.

The same argument excludes a nonzero rational prefactor in a reciprocal
identity E_chi(z)=R(z)E_chi(1/(Qz)) on 1/Q<|z|<1. Exterior definitions
of different functions are not excluded. In z=Q^(-s), the continuation
domain is Re(s)>0 and its boundary is Re(s)=0.

## 4. Four actual grades determine the first poles

The untwisted S3 Lie multiplicities in (trivial,sign,standard) order are

    M_1=(1,1,2), M_2=(1,0,1), M_3=(0,0,1), M_4=(0,1,1).

Odd grades acquire chi and even grades do not. The actual fixed-chi
source has no proper H^0 or H^2, so its proper L-functions are
polynomials. Denote the joint-cover anti-invariant numerator by P_-,
the twisted standard numerator by P_(E,chi), and retain the untwisted
elliptic numerators P_D and P_E. The proper factors in (3.1) through
grade four, apart from compact-support boundary factors on |z|=1, are

    n=1: P_-(z),
    n=2: (1-z^2)(1-Qz^2)/P_E(z^2),
    n=3: P_(E,chi)(z^3),
    n=4: 1/(P_D(z^4) P_E(z^4)).                         (4.1)

Here P_- has degree twelve and P_(E,chi) degree four. Their reciprocal
roots have modulus sqrt(Q), by the actual curve cohomology. Their
definition and weights do not depend on reconstructing all polynomial
coefficients from the small-field replay.

With N=3, the remainder converges for |z|<Q^(-1/4). There is no pole
in that disk: in particular the untwisted pole at 1/Q is gone.
The disappearance comes from twisting away the first grade's trivial
H^2 constituent, not from subtracting the untwisted leading term by hand.

Write E_chi(z)=sum_(n>=0) c_n z^n. Cauchy's estimate therefore gives

    c_n=O_(Q,eta)((Q^(1/4)+eta)^n) for every eta>0.        (4.2)

For the untwisted source, the corresponding statement is
a_n=A_Q Q^n+O((Q^(1/4)+eta)^n), with A_Q>0. These are source-specific
coefficient statements, not estimates for arbitrary Euler products.

There is also an exact arithmetic interpretation of the cancellation.
Every untwisted S3 local series above has nonnegative integer coefficients.
For an effective base divisor D, let a(D) be the product of its untwisted
local coefficients. At places other than zero and infinity, the coherent
source multiplies the degree-n local coefficient by the actual chi(v)^n.
At zero and infinity it retains only even local grades. Thus c_n is the
sum of a(D) over degree-n effective divisors, with these prescribed signs
and parity restrictions, whereas a_n is the unrestricted nonnegative sum.
In particular |c_n|<=a_n. The much sharper bound (4.2) is cancellation in
this specified arithmetic source sum. The finite parity restrictions
alone would not remove the untwisted pole, since their local ratios are
positive at z=1/Q; the nontrivial quadratic source is essential.

## 5. The elliptic poles cannot be canceled at the new ramification

Take N=4 and a radius between Q^(-1/4) and Q^(-1/5). Equation (4.1)
has possible poles on the first circle exactly at roots of P_E(z^2).
The other finite cohomological factors have different weight radii;
in particular M_4 has no trivial constituent. It remains to exclude
zeros of the good and bad Euler remainder at such a root z_0.

Write z_0^2=alpha^(-1), where alpha is an elliptic Q-Weil number.
Every conjugate of z_0 has modulus Q^(-1/4). The good-place numerator
zeros are +1/2 or -1/2, so no positive power of z_0 is one of them.
At each old finite branch place, the numerator of F_C2(epsilon t)
has algebraic-unit roots, just as 1+t+3t^2+t^3 does. No power of z_0
is an algebraic unit, by the norm argument in the untwisted theorem.

The new local numerators in (2.1)--(2.2) require a different check.
For a local argument t=z_0^d, put s=t^2=alpha^(-d). If
1+14s+9s^2 vanished, the algebraic integer beta=alpha^d would satisfy

    beta^2+14 beta+9=0.

If the numerator in (2.2) vanished, it would satisfy

    beta^4+3 beta^3+10 beta^2+7 beta+3=0.                 (5.1)

The monic integral minimal polynomial of beta would divide the relevant
monic polynomial over Z. Its nonzero constant term has absolute value
|Norm(beta)|, a positive power of the characteristic prime p: every
conjugate of beta has modulus Q^(d/2). It cannot divide 9 or 3 when
p>3. Both alternatives are impossible. The remaining new local factors
have constant numerator one. Thus all actual local factors are finite
and nonzero at z_0, including the new ramification. The normally
convergent tail is also nonzero there.

Consequently the first poles are exactly the roots of P_E(z^2), with
their algebraic multiplicities. The power-series radius formula yields

    limsup_(n->infinity) |c_n|^(1/n)=Q^(1/4).             (5.2)

No fixed sign, single oscillation, or generic simplicity of those poles
is assumed. Equation (5.2) explains why the coherent twist removes the
leading main term but does not remove the second Lie grade's elliptic
scale. The global unit-circle natural boundary is later than this first
Taylor-series singularity; meromorphic continuation and Taylor radius
are distinct claims.

## 6. Bounded replay and limits

The replay is to authenticate the existing joint source, actual quadratic
values and the frozen untwisted finite-extraction packet. It should compare
the complete degree-two closed-place Euler source with the appropriate
finite cohomological factors and actual bad corrections; test chi^n
on the first four Lie grades; and derive all even local series in
(2.1)--(2.2) from their invariant source. The reciprocal-polynomial
constant terms 9 and 3 are exact arithmetic controls, not a sampled
absence-of-zeros test.

All new primitive fields remain of order at most 49. Reconstructed
prefixes are not promoted to complete higher-degree Frobenius polynomials.
The continuation, all-degree split places, noncancellation and sharp
limsup are proved above, not inferred from finite coefficient agreement.
Execution, independent reading and the exact scientific freeze are
recorded separately after validation.
