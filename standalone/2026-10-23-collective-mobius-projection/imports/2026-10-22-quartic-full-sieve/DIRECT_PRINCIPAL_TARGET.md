# A substantial-bound target that bypasses the detector floor

Status: exact conditional implication, not an established moment improvement.
Scope: the Riemann zeta function, through the principal Eisenstein inverse.
Dependencies: the exact sixth-power puncture identity in
`standalone/2026-10-20-boundary-iteration/mixed/MARKED_CANONICAL_MEAN.md`,
Sections 2--3, and the ordinary prime-ideal theorem in a fixed ray class.
What was run: symbolic exponent calculation and a direct analytic proof.
Smallest remaining gap: the full unrestricted-row inverse moment hypothesis
(R), with its common smooth-profile uniformity.

Let E be the Eisenstein field and let S be the fixed finite set of omitted
prime ideals. Every ideal in the sums below is coprime to S. For a fixed
smooth annular W put

    M_u(D;W) = sum_n mu_E(n) chi_n(u)^(-1) (Nn)^(-1/2) W(Nn/D),

where character values at common primes are literally zero. Fix 0<a<=1.
Assume that for every epsilon>0, uniformly for H >= D^a and D>=2,

    sum_(0<Nu<=H) |M_u(D;W)|^2 <<_(epsilon,W) (HD)^epsilon H.       (R)

The hypothesis is required for every fixed smooth annular profile W, with
dependence through finitely many smooth seminorms and common uniformity on
compact families with a fixed supporting annulus. All nonzero physical rows
occur in (R), including sixth powers. This includes the fixed smooth Euler
derivatives and the profiles x^(1/2)W(x) and x^(-s)W(x) used below. A strict
margin H>=D^(a+eta), for every eta>0, gives the same open half-plane.

Then

    zeta(s) != 0 whenever Re(s) > 1/2 + 5a/12.                    (Z)

This avoids the balanced low-side comparison entirely. It does not claim
(R) for any a<1.

## Proof

Choose H=D^a (or its slightly inflated version) and amplifier primes p in a
fixed good annulus Np~A=H^(1/6), so that N(p^6)<=cH. There are
A^(1-o(1)) such primes. The exact Euler deletion identity is

    M_1(D;W) = M_(p^6)(D;W)
               - (Np)^(-1/2) M_(p^6)(D/Np;W).                   (1)

It follows by writing n=pm in the terms excluded by the natural zero at p;
mu_E(pm)=-mu_E(m) on (p,m)=1. No unrestricted value at a nonunit is used.

Square (1), sum over p, and bound the first term by (R). The second length
D/Np lies within a fixed constant multiple of D/A. To handle its dependence
on p, set F_p(t)=M_(p^6)(D/(At);W), for t in the common fixed compact
interval containing every Np/A. Then

    t d/dt F_p(t) = M_(p^6)(D/(At); xW'(x)).

One-dimensional Sobolev bounds the sum of supremum squares of F_p by the
integral of the sums of squares of these two fixed profiles. At each t, the
rows p^6 are injective and are a subset of the rows in (R), at one common
column length D/(At). Since that length is at most a fixed multiple of D/A,
the same H is admissible after a harmless fixed enlargement. The extra
coefficient (Np)^(-1) is O(A^(-1)). Consequently

    |M_1(D;W)|^2 << D^epsilon H/A
                  = D^(5a/6+epsilon).                          (2)

With W replaced by x^(1/2)W(x), (2) gives the unnormalized smoothed Mobius
bound D^(1/2+5a/12+epsilon). A smooth dyadic partition of unity therefore
continues the Dirichlet series 1/zeta_E^S(s) normally to every compact subset
of Re(s)>1/2+5a/12; the profile x^(-s)W(x) has bounded relevant seminorms
on each compact set. In Re(s)>1 the continued sum is the usual reciprocal.
Here the exact incomplete Euler product is

    zeta_E^S(s) = zeta_E(s) product_(p in S) (1-(Np)^(-s)).

The finite product is holomorphic and nonzero for Re(s)>0. Analytic
continuation gives zeta_E^S(s)F(s)=1 away from the pole at one, so
zeta_E^S, and therefore zeta_E, has no zero in the stated half-plane. Finally
zeta_E(s)=zeta(s)L(s,chi_{-3}); L(s,chi_{-3}) is holomorphic there, so a zeta
zero there would be a zeta_E zero. This proves (Z).

## Significant targets

| Full physical row scale | Resulting zeta boundary if (R) is proved |
|---|---|
| H >= D^(21/25) | Re(s)>17/20 = 0.85 |
| H >= D^(18/25) | Re(s)>4/5 = 0.8 |
| H >= D^(3/5) | Re(s)>3/4 = 0.75 |

In contrast, the current imported bound H+H^(1/6)D^(5/6) has no raw
row-volume range below H~D. Its value at H=D^(21/25) is
D^(73/75), while the desired (R) is D^(21/25); the required full-moment
saving is D^(2/15). This is a substantial analytic target, not a decimal
optimization. (The exponent calculation is 1/6*(21/25)+5/6=73/75.)

The principal sixth-power construction is inherited mathematics; the
purpose here is to calibrate a concrete 0.85 target while avoiding the
current detector architecture's separate low-side floor. No novelty of
the amplification argument is claimed.
