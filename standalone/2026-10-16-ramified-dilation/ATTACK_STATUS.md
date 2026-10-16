# The remaining signed estimate after the local split

Status: research assessment; all new component proofs are proposed.
No independent mathematical review, native moment bound, or RH conclusion.

## The exact surviving row

With the definitions of RAMIFIED_DILATION.md, the unestimated arithmetic is

    U_s(n;Z)=sum_(b^6 | (n), (b,s)=1)
          h(b)(Nb)^3 g_s(-n/delta_b^6)
          B_(n/delta_b^6)(Z/(Nb)^6).

B is the ACTUAL forward theta row. It is not a substituted native Mobius
polynomial, a randomized reference, or the scalar geometric completion.
The coefficients h(b) keep their signs/phases. The theta row index, the
shorter scale, common theta-column factors and the full Gaussian expansion
stay inside the sum.

The common-prime a part is now an explicit operator on U_s. Its active
shells are disjoint; its neutral shells have an explicit overlapping
budget. At the raywise critical fourth energy it loses no power of the
row cap, column scale or denominator norm. This resolves the local
Gauss-mask obstacle, subject to the explicit source-data interface.
It does not bound U_s.

## What a useful next theorem must actually say

A next estimate can target U_s jointly in the row n and denominator s,
with the real theta coefficients and the prescribed tests. It must retain
the simultaneous scale change

    (row norm cap T, column Z) -> (T/(Nb)^6, Z/(Nb)^6).

The outer Y is fixed. The old special curve X=Z^alpha, Y=Z^beta is not
preserved. The needed aggregate estimate must pay its own raywise maximal
or scale-dependent coefficients. An averaged bound at a single common
scale cannot be replaced by a sum of separate denominator-wise suprema.

For example Theorem 4 legitimately gives, for nonnegative weights w_s,

    sum_s w_s E^*_4[C_s](Q_s X,Z)
        <= exp(32 [F:Q]) sum_s w_s E^*_4[U_s](Q_s X,Z).

It does NOT bound the right side. Nor has a complete implication from
this row-energy estimate to the scalar critical Gaussian estimate been
proved here: the actual probe pairing and its comparison residual must
still be treated. The inherited scalar target remains

    Ghat(Z) = O_epsilon(Z^(1/2+epsilon)), for every epsilon>0.

The native alternative remains the complete signed injection-minus-
compensation bound in #950/#951. These are substantial arithmetic
obligations, not bookkeeping suppressed by the new notation.

## Direct closure attempt and its precise failure

The local operation was first tested as a possible dissipative filter.
There IS exact cancellation/orthogonality in its active common-prime
supports, but the resulting operator has norm at least one. More precisely,
the hard-ball test and a one-row source U_m0(Z)=Z^(1/2+1/p) attain the
active energy budget asymptotically. The identity a=1 term alone prevents
any universal T^(-delta) gain.

At p<6, the full positive Minkowski budget is already convergent under
the critical joint-ray input. This confirms that a bounded operator is
not the missing arithmetic theorem. Reapplying it to the unknown source
would return its exponent, not improve it. The exact support split is
useful because it removes common-prime ambiguity WITHOUT estimating away
the remaining coprime signed sum.

## Relation to recent work

#950 supplied the exact simultaneous pre-Poisson dilation and warned that
common primes, moving rows and the infinite principal Gaussian tail could
not be deleted. This packet supplies a divided-row kernel and its local
Gauss support/energy analysis. It does not add another scalar Euler factor.

#951's live ATTACK_STATUS explains that Holder/Young leaves unknown
partially restored U moments. The current calculation does not assume
those moments are controlled. Its primitive row U_s is a different object;
identifying the two without a source-faithful adapter would be invalid.

The #944 conductor-divisor window concerns a Hermitian tuple's character
conductor. The present active/neutral split concerns a denominator's Gauss
character. Their terminology is similar but they are not interchangeable.
A genuine combination requires writing both local characters in the same
joint sum; no global conductor-window estimate is imported here.

## Assessment

The gain is a rigorous local part of the requested joint arithmetic
operation and a sharper description of where a power saving CANNOT come
from. It is not evidence that the remaining full proof is close, and it
is not an improvement of a zeta zero-free exponent. The next nontrivial
advance must estimate the actual surviving signed coprime theta pairing
or the compensated native flux, not another universal norm comparison.
