# Bourgain refinement and complete masked input-frequency removal

**PROPOSED complete deductions. No new zeta boundary is claimed.**
This addendum preserves the previously reviewed compression files and
credits the new source packet from PR #1003, exact commit
`669b6a01f4d4858ae1ef806b07547be95c08c935`:
`standalone/2026-10-18-theta26-and-critical-family/arithmetic/NATIVE_FREQUENCY_TAIL.md`.
That source proves high-frequency removal for the full unmasked native
input. Here it is extended to every fixed annular original denominator
and core mask, using the exact coefficients already proved in
`MASKED_COMPRESSION.md`. The companion source's
`LOW_FREQUENCY_ATTACK.md` is an explicit generic-coefficient obstruction;
none of the deductions below supplies the missing Mobius contraction.

## 1. Named direct zeta input

Bourgain's published Theorem 5 in
[arXiv:1408.5794v2](https://arxiv.org/pdf/1408.5794v2), PDF page 2,
gives the direct critical-line bound

    |zeta(1/2+it)| <<_delta (1+|t|)^(13/84+delta).        (1)

The primary theorem was read directly for this addendum. Its exponent
is used as an explicit imported published result, not a reciprocal
bound. It improves the classical Weyl input used in the frozen flux
proof, without changing that proof's exact transport or masks.

## 2. Exact masked spectral amplitude

Use any fixed annular original mask |omega_(j,q)|<=1 on 2<=q<=Y^2,
including the original moving denominator cutoff and the prefix-adaptive
core mask. On that one physical annulus the coefficients are fixed.
The finite exact inversion in `MASKED_COMPRESSION.md` gives

    V_j(x)=sum_(d<=Y^2) alpha_(j,d) R(x/d),
    alpha_(j,d)=sum_(q<=Y^2,d|q) mu(q/d)omega_(j,q)C_Y(q),
    |alpha_(j,d)| <<_epsilon Y^epsilon/d.                (2)

Every original old product and every shared-prime term is included.
For example the last bound follows from
`|C_Y(q)|<<_epsilon Y^epsilon/q` and the harmonic sum over multiples
of d. The bound is uniform over all the fixed annular contractions;
it does not assert that those contractions have small low-frequency
output.

Put r(u)=e^(u/2)R(e^u). Its exact Fourier multiplier, with kernel
`exp(-itu)`, is `zeta(1/2+it)/(-1/2+it)`. Therefore

    a_j(u)=e^(u/2)V_j(e^u),
    ahat_j(t)=zeta(1/2+it)/(-1/2+it) * P_j(t),
    P_j(t)=sum_(d<=Y^2)alpha_(j,d)sqrt(d)d^(-it).        (3)

No multiplicative factorization of P_j is assumed. Its coefficient
square mass is `sum_d d|alpha_(j,d)|^2<<_epsilon Y^epsilon`.
The elementary finite-polynomial mean-value argument in #1003,
Section 2, thus gives

    integral_T^(2T)|P_j(t)|^2 dt
            <<_epsilon (T+Y^2)Y^epsilon, T>=1.          (4)

One can also prove (4) directly by the Gram off-diagonal bound
`2/|log(d/e)|<=2Y^2/|d-e|`, followed by the harmonic row sum. The
additional logarithm is absorbed into the prescribed subpower.

Equations (1), (3), (4) and a convergent dyadic sum prove

    integral_(|t|>T)|ahat_j(t)|^2 dt
       <<_epsilon (YT)^epsilon T^(-71/42)(T+Y^2).       (5)

At T=Y^(84/71), this is `O_epsilon(Y^epsilon)` for every epsilon>0.
The small preliminary losses are chosen before the final epsilon.

## 3. Physical windows and coherent retained energy

Decompose a_j into input frequencies |t|<=T and |t|>T BEFORE restricting
to its original physical log-annulus J_j. Multiplication by 1_(J_j)
is an L2 contraction. The actual annuli have disjoint interiors, and
there are O(log Y) of them. Hence (5) gives

    sum_j ||1_(J_j) a_(j,>Y^(84/71))||_2^2
                           <<_epsilon Y^epsilon.       (6)

Under x=e^u this is exactly the continuous dx energy of the discarded
input-frequency pieces on the complete strict square-step windows.
The reverse triangle inequality compares the complete masked source
and its retained low-input-frequency source with root error
`O_epsilon(Y^epsilon)`. It retains all their coherent cross terms.
No claim is made that multiplication by a physical indicator preserves
Fourier support: the final restricted low-input-frequency function
need not be bandlimited. Nor is the frequency-truncated output a unit
step function; (6) is a continuous norm statement on the literal cells,
as in the native exact consumer.

Thus the actual already-masked source, and not just the unmasked
`G_Y^2` multiplier, has a completely paid high-input-frequency sector.
The remaining bounded-frequency range still requires its arithmetic
estimate. The generic packet in #1003's LOW_FREQUENCY_ATTACK shows why
support, balance and multiplier bounds alone cannot replace that use
of the literal Mobius coefficients.

For these rough masks the coefficients in (2) sum to zero, since
`sum_(d|q)mu(q/d)=0` for q>=2. The ORIGINAL V_j is consequently
constant on every unit cell: between its integer harmonic jumps its
derivative is `-sum_d alpha_(j,d)/x=0`. Its continuous cell energy is
therefore its original discrete energy. This does not turn either
frequency piece separately into a step function.

## 4. Improved compression exponents

The exact flux theorem in `FLUX_COMPRESSION.md` states, for targets
of norm D=X^2, maximum target coefficient A/D and gap G,

    ||W||_(L2(dx))^2
       << A^2 D^(-1+2theta) G^(2-2theta),               (7)

with small powers understood. Use (1), so theta=13/84+delta.
For the balanced compression gap G=X^(7/10+eta), the exponent of X
in (7), before the freely small eta,delta, is

    -2+4*(13/84)+(7/10)*(2-2*(13/84))=-83/420<0.

The complete balanced error remains subpower; it already had no
positive energy floor. For the square compression gap
G=X^(6/5+eta), the corresponding exponent is

    -2+4*(13/84)+(6/5)*(2-2*(13/84))=68/105.            (8)

Choosing eta,delta in terms of the desired final epsilon improves the
ENTIRE already-masked square-compression error energy to

    Y^(68/105+epsilon).                                (9)

All low-product and upper-corner treatments are unchanged. This is an
improvement of the error term in the frozen `SQUARE_COMPRESSION.md`,
not a bound for its still open signed one-dimensional main amplitude.
It applies directly to that FULL, unremoved square-root source. The
optional additional removal of roots r<=T_root in that file costs
`Y^epsilon*T_root^4/Y` in energy. Its former example
T_root=Y^(5/12) would therefore retain a Y^(2/3) cost. To keep the
improved (9), retune this OPTIONAL cutoff to
`T_root<=Y^(173/420)`, since `4*(173/420)-1=68/105`, or use that
file's actual coefficient-mass budget instead. No new core projection
is applied to the reference squares.
If that complete main amplitude obeys a legal recurrence resource
`Y^a(1+F_Y)^p`, p<2, the pinned native all-prefix consumer now gives

    kappa <= max(a/(2-p),34/105).

The alternative square route's error-only zero-boundary floor is
therefore 139/210, rather than 2/3. The balanced route retains its
zero-loss error reduction. Neither statement proves a recurrence or
an improved boundary without the respective complete main estimate.
