# A new attack: arithmetic coercivity across multiplicative shells

**PROPOSED component results; independent review pending. RH remains unproved.**
This packet changes direction from PR837's signed-kernel spectral identities.
The new target is a uniform compactness estimate for an explicit triangular
integer matrix carrying ALL finite divisor equations. No source coefficient
is selected to avoid a difficult direction.

Start with [PROOF.md](PROOF.md), especially Sections 1, 3 and 4.
[ATTACK_PLAN.md](ATTACK_PLAN.md) separates the proposed global mechanism from
the finite test programme. [VALIDATION.md](VALIDATION.md) states actual checks.

## The exact bridge

For odd X>=3, vectors are indexed by 1,3,...,X-2. Put v_(-1)=0 and

    (B_X v)_n = sum_(d|n) d(v_d-v_(d-2)).

The first column of its inverse is the literal harmonic odd-Mobius sequence
m(n)=sum_(k<=n, k odd)mu(k)/k. More generally,

    B_X^(-1)(n,d)=m(n/d)/d.

The COMPLETE inverse trace is

    2 ||B_X^(-1)||_HS^2 = sum_(d<X, d odd) E(X/d)/d,
    E(X)=integral_1^X m(t)^2 dt.

Consequently

    E(X)/2 <= ||B_X^(-1)||_op^2
           <= (sum_(d<X, d odd)1/d) E(X)/2.

Thus a uniform inverse estimate for arbitrary forcing costs only a logarithmic
factor beyond the original source energy. Subpower inverse growth is exactly
RH-equivalent; the reverse implication retains the classical RH-to-Mertens
input. This is a proved adapter, not a source-to-operator assumption.

Arithmetic matrix routes are not new in general: Bordelles--Cloitre (2009)
already give an RH criterion using smallest singular values. See SOURCES.json.
We make no comprehensive novelty claim for this specific normalization.

## Why the shell decomposition offers a different mechanism

Split X=3A at A=3^r. No odd integer below 3A has a proper divisor in [A,3A).
This makes the entire new-shell diagonal block exactly invertible:

               [ B_A   0  ]                 [ V_A     0 ]
    B_(3A) =   [ C_A  K_A ],    B_(3A)^(-1)=[ L_AV_A  J_A ],

where V_A=B_A^(-1), J_A(n,k)=1_(k<=n)/k and L_A=-J_AC_A. No coupling is removed.
Uniformly, ||J_A||_op^2<=2/3. Old forcing supported on d>=A/q also has a
uniform new-shell output bound <2q^2 for every fixed q>=1. The remaining
sector has d/A tending to zero.

The proposed all-source target is:

    for every eta>0, some finite C_eta works at EVERY A=3^r:
    ||L_A x||^2 <= eta||x||^2+C_eta||B_A x||^2.

**This target is OPEN.** The conditional theorem proves that it implies RH:
the complete block inverse gives

    kappa(3A)<=max((1+2eta)kappa(A)+2C_eta,4/3),
    kappa(A)=||B_A^(-1)||_op^2.

Arbitrarily small eta then gives subpower growth. Equivalently, the OPEN
assertion says bounded vectors with vanishing divisor-equation residual
cannot produce a nonvanishing new-shell output. Finite-dimensionality and
coordinatewise convergence do not supply its uniformity.

## Positive finite tests and essential counterexamples

Exact rational certificates prove the proposed all-vector inequality with
C=1, eta=1/10 and 1/100 at A=3,9,27,81. These are complete matrix inequalities
at eight fixed parameter pairs, not sampled-vector evidence or an all-scale
estimate. Another seven specified matrices satisfy B_X^*B_X>I/4.

A classical critical-line-zero argument proves that NO fixed positive
coercivity gap can persist for all X. The conjectured subpower loss permits
this degeneration. Separately, an explicit nonnegative multiplicative CONTROL
kernel has the same diagonal, determinant, eigenvalues, exact divisor inversion
and fresh-shell stability, but its required C_eta grows exponentially in the
shell number. It is not the zeta source. This refutes a generic matrix proof,
not the native compactness target.

## Review and replay

    python -B check.py --check results.json --self-test
    python -O -B check.py --check results.json --self-test
    python -OO -B check.py --check results.json --self-test

The inverse is reconstructed by both triangular elimination and independent
trial-factorized Mobius sums. Positive definiteness is checked by integer
Bareiss determinants and separate rational LDL elimination. Ten resealed
corruptions are rejected in each self-test. All are same-author implementation
controls, not an independent mathematical review or proof of the open target.
No full-checkout repository validation is claimed.

The new contribution is the exact full-source matrix/shell architecture,
its positive controlled sectors, a precise sufficient compactness theorem,
and honest failure controls. The missing uniform estimate is not disguised
as an established lemma, and no RH proof is claimed.
