# Independent review: the native theta-source off-central-zero corollary

Verdict: **PASS** on the exact corollary text identified below. This is a
source-bound check of an inference from accepted FI and MP, not a new
divisor search, effective estimate, or re-review of their primary imports.
No scientific source or release-tree file was modified.

## 1. Review target and frozen inputs

Review branch base:
dde680d50358fb6d269485b1b8f61f23ba6b221e.

The root corollary was read directly, without copying it into this branch:

research/l-families/atlas/generalized/NATIVE_THETA_SOURCE_OFFCENTRAL_ZERO_COROLLARY.md

Its reviewed UTF-8 content has **3438 LF-normalized bytes** and SHA256

f76b711355dbdb1b07c172a8e2b5b02a20051338e2badf4816722cc8a5438501.

It was uncommitted when read, so this hash, not a fabricated science commit,
identifies the reviewed text. The verdict transfers only to identical
LF-normalized content. The four complete frozen notes below were read and
their literal Git-blob and LF-SHA identities recomputed with replace objects
disabled. All paths are relative to research/l-families/atlas/generalized/.

| Note | Commit | Git blob | LF SHA256 |
|---|---|---|---|
| CUSP_WEIGHT24_FIXED_DIVISOR_INFINITY.md | ec5bdd9b02ea68bddfcf34ac40a85d283faf64cf | ba8dd0d08aface85ef346106b158636177a88979 | d8737b8551ddd71249b799a1a2ebd61cb2c0ad01bc15ca7954cb36fe73d2f26f |
| CUSP_WEIGHT24_FIXED_DIVISOR_INFINITY_AUDIT_EC5BDD9B.md | 0f29fd2d687c57402a14723dde2bc2b7e74fa317 | 91c1896791ef94b6f1f753fa48bc48eb7e91df7b | 0e86da5a218b066a7d46aa5336d35817ce0c7ad4c8da89a12797e23eed309655 |
| CUSP_MATRIX_PERIOD_POSITIVITY.md | fdd349dcf6ba1b104e27866ae66b4c89752d5f05 | c901150a44e981ed2ef548d8b123d4e6e99f2c27 | fabb13f35e0f6a45ddbc3b5f54f0376e9c0aec5d75b44ae9b4ae10cf17136c0c |
| CUSP_MATRIX_PERIOD_POSITIVITY_REVIEW_FDD349DC.md | 8b2bb44f3b82059b6e3721aba9b2cff2a70fd7d0 | f49d2f8896de45d03e9fa81cd3ed5e9fb0c9ab70 | d4340708d1e349e52f5138d55624c1b5ced53edee06f66660a4143f1fb97d335 |

The accepted reviews remain separate evidence. This short check does not
claim another machine proof of FI's automorphic/value-theorem hypotheses,
nor a fresh replay of the two full scientific suites.

## 2. Literal period normalization and protected divisors

FI1--FI8 retain the actual weight-24 coefficient basis

    g=Delta E4^3-696 Delta^2,   b=Delta^2,
    f_+=g+alpha_+ b,           f_-=g+alpha_- b,
    alpha_+/-=540+/-12 sqrt(144169),   delta=24 sqrt(144169).

Thus delta^2=83041344 and b=(f_+-f_-)/delta. With the conjugate-linear
first slot, the real basis-change matrix has determinant -delta. Both
cross periods agree by their real-coefficient Dirichlet expansions,
then by meromorphic continuation; this is not a claim of pointwise
Hermitian positivity at nonreal s. FI7 supplies the full eigenbasis matrix

    A(s) [[Z(s)S_+(s), C(s)], [C(s), Z(s)S_-(s)]],
    A(s)=pi^(-s)Gamma(s)(4pi)^(-s-23)Gamma(s+23).

No cross entry is discarded. Congruence and the formula for b give exactly

    I_s(b,b)=A(s)H(s)/delta^2,
    det I_(g,b)(s)=A(s)^2 N(s)/delta^2,
    Q_1(s)=A(s)N(s)/H(s),

where H=Z(S_++S_-)-2C and N=Z^2 S_+S_--C^2. The zeta(2s) multiplier
has already been incorporated by FI6--FI7; adding another would be wrong.
The two gamma functions and the nonzero exponential factors show that
A is holomorphic and nowhere zero on Re s>1.

FI3 and Section5 prove more than unsigned numerator/denominator counts.
The protected pole disks contain an H zero while N is nonzero throughout;
the protected zero disks contain an N zero while H is nonzero throughout.
Therefore the former give
genuine zeros of I_s(b,b), and the latter genuine zeros of det I_(g,b).
At each point the corresponding zero multiplicity is unchanged by A and
delta. Separate distinct-point lower bounds c_P T and c_Z T transfer in
each fixed substrip 1<sigma_1<sigma_2<=1+eta. No assertion that every zero
is protected, or that the zeros are simple, is needed.

## 3. The actual scalar source is a restriction, not a proper quotient

Apply MP1--MP12 to the genuine one-dimensional cusp space V=C b with W=0.
Its Petersson vacuum is G_b>0, and its positive source is

    B_b(t)=1/2 integral y^24 |b(z)|^2 [Theta_z(t)-1] dmu(z).

MP6 gives C_0=B_b exactly. Consequently its completed observation is the
literal original period L_0(s)=I_s(b,b), not a fitted scalar factor or a
Schur quotient of the two-dimensional source.

For precision about the word reciprocal, B_b obeys MP4's AFFINE law.
The vacuum-restored H_b(t)=G_b+2B_b(t) obeys the homogeneous law
H_b(t)=t^(-1)H_b(1/t). The vacuum has not been discarded. B_b(t)>0 for
every t>0 because the nonzero lattice sum and |b|^2 give a positive
integral. Smoothness is also justified locally: for t>=t0>0 and any
fixed derivative order j, each differentiated Gaussian is bounded by
a constant times exp(-pi t0 a/2), where a is its nonnegative lattice
energy. MP1's cusp-integrability bound at t0/2 then permits termwise
differentiation and integration. No finite theta cutoff is used.

MP13 gives the positive scalar Mellin feature kernel
L_0(z+conjugate(w)) for Re z,Re w>1/2. MP12 gives

    L_0(s)=G_b/[2s(s-1)]
             + integral_1^infinity [t^(s-1)+t^(-s)]B_b(t)dt.

Hence s(s-1)L_0(s) is entire with reflection s -> 1-s and retains every
above zero in Re s>1. Reflection yields off-central zeros in Re s<0.
For the full two-dimensional source W=0, the analogous determinant
statement follows in the same way; multiplying its matrix by s(s-1)
does not remove these zeros either.

The statement is compatible with strict positivity on the REAL half-line
s>1: FI's zeros lie at nonreal points in a vertical substrip. Positive
kernel structure is not pointwise positivity at every complex argument.

## 4. Accepted inference and limits

The reviewed scalar corollary is native: b=Delta^2 is an actual cusp form.
It is not a Hecke eigenline. Indeed a_1(b)=0 and a_2(b)=1; simultaneous
Hecke eigenform identities a_1(T_n b)=a_n(b) would make all coefficients
zero if a_1 were zero.

Restriction to C b BEFORE completion must not be confused with MP's
proper source quotient for V=S_24 and dim W=1. This corollary does not
settle the zeros of that different construction. Nor is a determinant
zero an eigenvalue-by-eigenvalue matrix-zero classification.

The near-1 width eta, counting constants, onset and individual ordinates
remain noneffective as in FI. There is no zero simplicity, complete
census, scalar Euler product, preferred Hecke flag, new automorphic lift,
RH counterexample, or general scattering-normalization conclusion.
The verified conclusion is exactly that positive reciprocal theta-source
structure plus actual modular-period origin does not, by itself, force
critical-line zeros, even for a scalar unquotiented source.

This resident review contains no new scientific computation or source
edit. Source identities, the target content hash, control-character scan
and review-only whitespace delta were checked before freezing.
