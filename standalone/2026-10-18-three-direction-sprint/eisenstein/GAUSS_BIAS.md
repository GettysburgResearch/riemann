# A fixed cubic Gauss vector with its polar bias canceled

Status: **PROPOSED consequence of explicitly imported component theorems.**
This is a restricted-vector mean estimate, not a new arbitrary-coefficient
large sieve or a zero-free theorem. It is separate from the complete native
cube-vector overlap in ANGULAR_COEFFICIENTS.md.

Use primary elements of Z[omega], ideal norm N, and the cubic normalized
Gauss sum gtilde_3 in the conventions of [de Faveri--Dunn--Hoffstein,
2607.07911v1, section 2.1](https://arxiv.org/html/2607.07911v1#S2.SS1).
For a fixed real H in C_c^infinity(0,infinity), put

    T_H(a;B)=sum_b^flat gtilde_3(b) conjugate((a/b)_3) H(Nb/B).

The complete sum retains the nonunit zero convention, hence all cases in
which a,b share primes. There is no artificial coprime replacement.
The imported polar evaluation and complete remainder are

    T_H(a;B)=C Hhat(5/6) B^(5/6) conjugate(gtilde_3(a))
                    /(Na)^(1/6) product_(P|a)(1+1/NP)^(-1)+R_H(a;B),
    sum_(Na<=A)^flat |R_H(a;B)|^2 <<_(H,epsilon) (AB)^(1+epsilon). (1)

These are that paper's (2.4)--(2.9); its second-moment input is
[David--de Faveri--Dunn--Stucky, 2410.03048v2, Lemma 6.6](https://arxiv.org/html/2410.03048v2#S6),
and its pointwise evaluation is the specialization of Lemma 6.7 there.
The mean-square remainder (1) is valid for A,B>=1. The lower-bound argument
elsewhere in the former paper imposes B<=A<B^2; that extra range is not
used in the remainder calculation itself.

The published pointwise lemma initially states a nonnegative test profile.
Its signed extension used here is rigorous: choose a nonnegative smooth
envelope E identically one on the compact support of H. With C>=sup|H|,
write H=(H+CE)-CE. Both profiles are nonnegative, smooth and compactly
supported. Apply the two identities and subtract. The polar functional is
linear, the two full remainders subtract, and |R_1-R_2|^2<=2|R_1|^2+2|R_2|^2
pays their constants. The divisor and height terms in the complete
remainder are not dropped. No positivity is used after this extension.

Consequently any fixed signed profile with Hhat(5/6)=0 satisfies the actual
arithmetic mean estimate

    sum_(Na<=A)^flat |T_H(a;B)|^2 <<_(H,epsilon) (AB)^(1+epsilon). (2)

For example choose any nonzero H0 in C_c^infinity(0,infinity) and set

    H=(y partial_y+5/6)H0,  Hhat(s)=(5/6-s)H0hat(s).       (3)

The boundary terms in integration by parts vanish at both endpoints, so
(3) cancels the complete polar term exactly. This is a genuine improvement
over the worst operator estimate for this particular Gauss-shaped vector.
It does not assert that an arbitrary Mobius or reciprocal-L vector belongs
to the same orthogonal subspace.

There is an exact obstruction to the most tempting transfer. For the SAME
radial physical profile W0(x)=H(|x|^2), the elementary Fourier--Mellin
calculation in ../CROSS_ROUTE.md gives

    M_W0(z)=pi^2(2pi)^(-2z) Gamma(z)/Gamma(1-z) Hhat(1-z).

The principal CT scalar is proportional to M_W0(1/6), hence proportional
to Hhat(5/6). Imposing the cancellation in (3) in this same W0 coordinate
therefore kills the target scalar too. This is a rank-one obstruction for
this explicit profile architecture. It does not prohibit another variable,
a joint profile, or cancellation of a different nuisance sector.

GAUSSIAN_FILTER.md records a different-coordinate filter that preserves
the principal scalar and every nontrivial target zero. Applying (2) to that
filter still requires identifying its actual native Gauss-polar component;
the identities in this note do not supply that identification.
