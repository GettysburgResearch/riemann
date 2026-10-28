# A weaker principal-signal interface

**Status:** Proposed conditional reduction; no new zero-free region is proved.
**Scope:** The scalar principal signal in Proposition 2.1 of the [OpenAI quasi-RH preprint](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf), combined with the proposed [principal Euler-factorization](2026-10-28-principal-factorization.md).
**Inputs:** The source's local identities and the standard Hecke analytic continuation; the optional extension below additionally assumes Boyang Hu's [unitary-Hecke nonvanishing claim](https://hexagonmath.org/2610.00216v1), which has not been independently verified here.
**What was done:** Inspection of the source's Proposition 2.1 and proof, and an algebraic substitution.
**Smallest remaining gap:** Prove the source's low estimate and uniform high remainder for the *same physical probe* at the proposed boundary, including all nonprincipal rows, contours, and error terms. This note supplies none of these estimates.

## Interface

In Proposition 2.1, the hypothesis `sup_{Re s > sigma0}|H_eta(s)-1| <= 1/2` may be replaced by the following two conditions:

1. `H_eta` is holomorphic and zero-free on `Re s > sigma0`;
2. `H_eta` is bounded on `Re s >= 2`.

All other assumptions and quantifiers of Proposition 2.1 remain unchanged. To verify this replacement, the source's proof uses boundedness of `H_eta` only to move the defining contour of the signal to arbitrarily large real parts, which gives rapid decay as `Z` tends to zero. The assumption on `Re s >= 2`, together with the absolutely convergent reciprocal Euler product and Gaussian factor there, suffices for that argument. Once the Mellin transform is constructed on `Re s > beta_* - epsilon_*`, it equals the original `exp((s-5/6)^2) H_eta(s)/L^S(s,eta)` on `Re s>1`. The identity theorem and division by the nonvanishing `H_eta` provide the desired continuation of `1/L^S(s,eta)`. No uniform lower bound on `|H_eta|` is needed for this division: holomorphic nonvanishing suffices. The uniform power saving `epsilon_*` in the other hypotheses remains essential.

## Conditional application to the scalar factor

Assume the local factor identity and factorization in [principal-factorization](2026-10-28-principal-factorization.md), and assume Hu's stated nonvanishing for every unitary Hecke character in `Re v>7/8`. Set

    sigma0 = 31/48,      v = 6s-3.

Then `Re s>sigma0` implies `Re v>7/8`. Because `sigma0>1/2`, one may choose a **single** fixed prime cutoff (uniform in the target character) for which the factor `K_eta` is holomorphic and satisfies `|K_eta-1|<=1/2` on `Re s>=sigma0`. Add the finitely many primes at which the target is ramified to the exceptional set. The Hecke character `psi_eta=conj(alpha)^6 eta^6` is unitary; Hu's claimed rank-one theorem makes its Hecke L-function nonzero on `Re v>7/8`. Its deleted Euler factors are nonzero there. Thus

    H_eta(s) = L^S(6s-3,psi_eta) K_eta(s)

is holomorphic and nonzero for `Re s>31/48`. On `Re s>=2` the original Euler product is uniformly bounded, so the preceding weakened scalar interface is met.

Hu's claim is an external input, not an independently established result here. This does not give the source's stronger closeness estimate `|H_eta-1|<=1/2` on the larger half-plane, and it says nothing about multivariable deformations away from `w=1,z=1/6`, nonprincipal rows, or required uniform remainder bounds. In particular it does not establish a zeta zero-free region, and Hu's proof is itself presented as extending the OpenAI method.
