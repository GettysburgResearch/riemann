# Heat-Hankel synthesis: source-only matrices and quantitative capture

**RH and the full arithmetic matrix inequality remain UNPROVED.** Complete
component proofs are proposed for independent mathematical and code review.
No external novelty, referee acceptance, or formal-proof claim is made.

Base: PR #790 at `634d9a8ec4b0819442e601686a109ff7015b7b0b`.
New files are confined to `heat-hankel-pass5/`. Predecessors are unchanged.

This pass steps back from enlarging scalar derivative ranges. It combines
#793's infinite-background Hardy interpolation with #792's distinction
between a controlled diagonal and the full signed arithmetic form. Read
`CROSS_REVIEW.md` for the exact heads, proof texts read, and limitations.

## Main component theorems

Let `A=rho(1-rho)`, with all upper-half-plane nontrivial zeros and their
multiplicities, `S(t)=sum_A exp(-At)`, and `h=X'/X` in the parent invariant
normalization. Define on `L2(0,infinity)`

    Gamma_tau(s,t)=S(tau+s+t), tau>=0.

This Hankel operator is trace class without assuming RH. It is specified
from literal Euler/gamma data through the divided differences of the safe
positive-axis function h (and a stated thermal transform for tau>0).

**Exact inertia.** The number of negative eigenvalues of Gamma_tau is the
number of distinct off-line zeta quartets, at every finite tau>=0. Zero
multiplicities are retained as weights, not counted as independent vectors.
The argument treats the full infinite background without assuming spacing.

**Source-only finite capture.** For k>=1, use the predetermined real space

    V_(k,J)=span{t^r exp(-2^j t): 0<=j<=J, 0<=r<2k}.

If P is the true L2 orthogonal projection and tau>0, choose the least J>=0
with `tau*2^J>=2k`. Then

    ||Gamma_tau-P Gamma_tau P||_1 < 3^-k,
    dimension = 2k(J+1) = O_tau(k log(k+2)).

At tau=0 set J=4k. This uses ONLY derivatives of h at positive dyadic nodes:

    ||Gamma_0-P Gamma_0 P||_1
       < 3^-k+(10+5k/2)4^-k,
    dimension = 2k(4k+1).

These are indefinite finite approximations with a proved error, NOT proved
positive approximations. No unknown zero enters the nodes, metric, or error.
No universal first detection rank is claimed.

**Correct metric and negative mass.** The raw Gram is exactly

    G_((j,r),(l,s))=(r+s)!/(2^j+2^l)^(r+s+1).

The source form Q consists of confluent divided differences of h_tau. The
orthogonal compression is `M=G^-1/2 Q G^-1/2`. An explicitly orthonormal
rational-Laplace basis and safe derivative compiler are supplied. If
`nu=Tr(Gamma_tau)_-`, `nu_k=Tr(M)_-`, and epsilon is the error above, then

    nu_k <= nu <= nu_k+epsilon.

Every exceptional quartet must therefore appear in a finite member of this
fixed hierarchy. The full-sign problem is now the arithmetic PSD of Q, not
an additional conjecture about cofinal capture or a zero-chosen metric.

## What is actually proved about positivity

Put `H=h(0)=1+gamma_E/2-log(4pi)/2`. The source budget gives unconditionally

    Tr Gamma_0=H/2,
    ||Gamma_0||_1 <= H/[2(1-H)],
    0<=Tr(Gamma_0)_- <= H^2/[4(1-H)].

The upper bound is not zero. The proposed final equality
`||Gamma_0||_1=H/2`, equivalently PSD of all the finite Q matrices, remains
RH-equivalent and open. An exact positive-heat countercontrol has a 3x3
entrywise-positive matrix with determinant `-2/15625`, so positive heat alone
does not close this gap.

## Reading and validation

Read `PROOF.md`, then `CROSS_REVIEW.md`, and `VALIDATION.md` before reusing a
claim. The finite checker uses only Fraction and Gaussian-rational algebra:

    python verify.py --check result.json
    python -O verify.py --check result.json
    python rejection_tests.py
    sha256sum -c SHA256SUMS

It reconstructs confluent projection norms, finite-source divided differences,
raw and orthonormal metrics, partial-fraction compilers, finite inertia and
the negative test. It does not evaluate an actual-xi matrix, prove the
infinite interpolation or trace-norm estimates by machine, or prove RH.
