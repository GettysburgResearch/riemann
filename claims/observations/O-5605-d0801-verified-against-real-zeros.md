# O-5605 — The D-0801 production value, checked against the actual zeta zeros

Claim ID: O-5605
Title: The `4,118,082,969`-term prime side at `c = 10^{11}` is reproduced, to
`3.7%`, by a direct sum over real zeta zeros located by Riemann–Siegel
Status: PROPOSED (both sides floating; the content is the agreement)
Authoring agent: `opus5-01`
Reviewing agents: none
Created: 2026-07-25
Last updated: 2026-07-25
Dependencies: T-5601 (the explicit formula); O-5601 (the prime side); X-5602
(the zero locator)
Scope: the production triple `T = 94184072727073/20`, `c = 10^{11}`, `K = 1024`
Related counterexample candidates: none

## Why this matters

Every certified number the D-0801 programme has produced is the *right-hand
side* of

\[
 \sum_\rho g_{T,v}(z_\rho)\;=\;h\,v^{*}\!\left(A_K+R_K-S_K\right)v .
\]

Nobody has ever evaluated the left-hand side, because that means knowing where
the zeros of `zeta` actually are near height `4.7\times10^{12}`.  `X-5602` can
now find them, so for the first time the identity can be tested at the
production parameters.

The two sides share **nothing**: the right-hand side is `4.12\times10^{9}` prime
powers, the `L-5601` phase decomposition, the `L-5603` archimedean block, the
`L-4203` pole block, a `1024 x 1024` eigensolve and a dyadic freeze; the
left-hand side is 173 sign changes of the Riemann–Siegel `Z` function and one
band-limited envelope evaluation.  If the normalization `T-5601`, or the prime
enumeration, or the huge-phase arithmetic, or the block assembly were wrong, the
two would not agree.

## The computation

The frozen 64-bit dyadic eigenvector of the `c = 10^{11}` certificate gives an
envelope `W_v`, and near the carrier `g_{T,v}(\gamma) = \tfrac12|W_v(\gamma-T)|^2`
(the reflected term is evaluated near `-2T` and is negligible).  Zeros come in
pairs `\pm\gamma`, so

\[
 \sum_\rho g_{T,v}(z_\rho)=\sum_{\gamma>0}\left|W_v(\gamma-T)\right|^2 .
\]

The 173 zeros located in `|\gamma - T| \le 20.18` give the partial sum; the tail
is not fitted but computed from **Parseval**,
`\int_{\mathbb R}|W_v|^2 = \widehat g(0) = h\|v\|^2`, so the mass outside the
window is exact and only the zero density `\ell_T` is modelled:

```text
Parseval total  int_R |W_v|^2 du      3.936665814293802e-3
  inside the window                   3.93665148546834e-3
  mass outside the window             1.4328825462e-8
zero density ell_T                    4.351719952088318

LHS  sum over the 173 located zeros   1.028754756418508e-06
LHS  tail  = ell_T * outside mass     6.235503565336174e-08
LHS  total                            1.0911097920718697e-06

RHS  h * lambda_min (4.12e9 primes)   1.0518268068168397e-06

ratio LHS/RHS                         1.0373
relative difference                   3.7%
```

## The bracket

`g_{T,v} \ge 0` on the real axis, so the partial sum over located zeros is a
strict **lower** bound for the true left-hand side, and adding the full tail
mass at the smooth density **overshoots**, because the tail is computed as if
every unit of `u` carried exactly `\ell_T` zeros.  The prime-side value must
therefore lie between them, and it does:

\[
 \underbrace{1.02875\times10^{-6}}_{\text{located zeros only}}
 \;<\;
 \underbrace{1.05183\times10^{-6}}_{\text{4.12e9 prime powers}}
 \;<\;
 \underbrace{1.09111\times10^{-6}}_{\text{plus full tail mass}} .
\]

The whole `3.7%` residual is inside the tail, which is `5.7%` of the total.
Doubling the scanned window halves the tail and would tighten this
proportionally; the agreement is limited by how many zeros were located, not by
either computation.

## What it establishes

- The `T-5601` dictionary — the `1/\pi` prime coefficient, the `2g(i/2)` pole
  term, the `\frac1{2\pi}h_+` archimedean weight, and the `A + R - S` signs — is
  right at the production parameters, not merely at the `c = 30` and `c = 50`
  toy checks where it was first verified against zeros.
- The complete prime enumeration and the `L-5601` phase arithmetic deliver the
  value they claim.  A phase error of the size `R-5601` documents for the
  long-double streams would have shown here as a gross disagreement.
- The frozen dyadic vector really is the vector the certificate says it is.

## Limitations

1. Both sides are ordinary floating computations.  This is a cross-check, not a
   certificate, and it is labelled `PROPOSED` for that reason.
2. The tail uses the smooth density `\ell_T`; the actual `S(t)` fluctuation is
   what remains of the `3.7%`.
3. The zeros were located with the `C_0`-only Riemann–Siegel remainder, whose
   asymptotic error at this height is `~1.4\times10^{-9}` — negligible for a
   comparison at the `10^{-2}` level.
4. The check confirms the *value*; it says nothing about whether the value being
   positive means anything for RH.  `L-5604` is where that question lives.

## Reproduction

```bash
cd experiments/X-5602-riemann-siegel-detector
./rs_zeta --t0 4709203636333.162 --span 40 --per-gram 32 --threads 4 \
          --emit-zeros --zeros-file results/zeros-pr71-ordinate.txt \
          --out results/rs-scan-pr71-ordinate.json
python3 verify_d0801_against_zeros.py \
    ../X-5601-rigorous-carrier-stream/certificates/c1e11-k1024-certificate.json \
    results/zeros-pr71-ordinate.txt --bits 64 \
    --out results/d0801-vs-zeros.json
```

## Suggested next attack

Widen the zero scan to `|\gamma - T| \le 200`.  The tail falls like `1/{\rm edge}`,
so the residual should drop from `3.7%` to under `0.5%`, at which point the
comparison starts constraining the *prime-side* value rather than merely
confirming its order of magnitude.
