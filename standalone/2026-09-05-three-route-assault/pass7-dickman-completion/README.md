# Seventh continuation: horizon-faithful Dickman completion

**RH IS NOT PROVED.** Complete proposed component proofs are supplied; independent mathematical review remains required. All three routes remain active. This packet does not promote finite checks into an infinite sign theorem.

Parent scientific source: PR #793 at `8eee76d79a5a608f5d6b89c9205cc7bba637f66a`.
Scope: ordinary primes and the literal 67-free Mobius source, causal norms, collective omitted-prime corrections, and the exact balanced-source connection.
Start with [PROOF.md](PROOF.md), then [SOURCES_AND_REVIEW.md](SOURCES_AND_REVIEW.md).

## Constructive result

For L=log X, multiply the genuine finite Euler product by the single-valued entire factor

    C_X(s)=exp(gamma)(s-1)L exp(-Ein((s-1)L)).

This is the classical Dickman correction, not a new special function. In the original causal coordinate it is I minus convolution with

    k_(X,a)(x)=L^-1 exp((1-a)x)[-rho'(x/L)], x>=L,

where rho is the positive Dickman function. The correction preserves the exact full Mobius source for EVERY x<L. It removes the entire continuous omitted-prime contribution rather than one local Euler term.

On Re(s)=1, the full causal L2 error of the corrected product is

    O(exp(-c sqrt(log X)))

for some c>0. All frequencies are included. This is a PNT-level norm theorem, not an RH-strength theorem. The constants are not numerically certified.

## Two sharper raw-error theorems

For F_X(x)=exp(-x)M_X(exp x), F(x)=exp(-x)M_67(exp x),

    (log X)[F_X(log X+y)-F(log X+y)] -> g(y) in L2,
    g(y)=sum_(n<=exp y)mu_67(n)/n-exp(-y)M_67(exp y).

The raw norm error is asymptotic to ||g||_2/log X. Moreover

    ||F_X||_2^2=||F||_2^2+||g||_2^2/(log X)^2+o((log X)^-2).

After subtracting that translated first profile, the residual rescaled on x=(log X)u converges in L2 to (67/66)omega'(u), where omega is Buchstab's function and its jump at u=1 is excluded from omega'. The residual norm has exact order (log X)^(-3/2). The universal squared norm lies between 7/24 and 19/24.

These are aggregate signed-source limits, not diagonal estimates or random-prime models.

## Connection to the other routes and the unresolved step

Differentiating log C_X gives exactly X^(1-s)/(s-1). Thus the same completion gives the balanced gamma-plus-prime logarithmic derivative used by the moment and Hardy routes. All powers of p<=X are retained; the difference from a hard prime-power cutoff is stated and bounded explicitly.

At a=1 the correction is bounded by 2, but is not a contraction. At every fixed a<1 its exponentially tilted kernel has growing norm. Neither Dickman positivity nor the safe-line norm theorem supplies the collective signed estimate in Re(s)>1/2. Local boundedness of the corrected products throughout that half-plane remains the open RH-equivalent endpoint.

No moment-matrix PSD, Hardy positivity, new signed Mertens power saving, or zero-free region is claimed.

## Replays

With the unchanged parent sibling present:

```sh
python verify.py --check RESULTS.json --manifest
python -O verify.py --check RESULTS.json --manifest
python verify.py --self-test
python -O verify.py --self-test
```

The exact suite reconstructs 2242 bounded integer/rational controls. Twelve unit/rejection tests pass in both modes. The parent proof is authenticated by its literal SHA-256 before use; no parent code is executed. The optional regression uses 50-digit mpmath at nine fixed arithmetic points and is NOT a proof dependency.

The finite checker does not machine-prove PNT, Plancherel, the Dickman/Buchstab transform identities, infinite-frequency bounds, or asymptotic limits. No previous broad suite, Lean build, remote CI run, or independent referee review is claimed. The publication receipt belongs in the PR conversation, outside the immutable source files.
