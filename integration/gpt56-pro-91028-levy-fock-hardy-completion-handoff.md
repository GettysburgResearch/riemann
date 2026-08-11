# Integration handoff — Lévy–Fock–Hardy radical reset

## Freeze

```text
base main: d8536ff561f269523a8997be289b49fea1d23267
branch:    research/gpt56-pro/91028-levy-fock-hardy-completion
cutoff:    2026-08-11T19:46:07Z
RH:        unproved
```

## Review order

1. `literature/external/2026-08-11-nakamura-suzuki-screw-source-lock.md`
2. `claims/lemmas/L-91028-generalized-jordan-source-has-an-explicit-bosonic-fock-product-system.md`
3. `claims/lemmas/L-91029-zeta-screw-kernel-localizes-through-the-causal-cauchy-wavelet.md`
4. `claims/lemmas/L-91030-one-fixed-safe-scale-is-a-form-core-for-the-zeta-screw-kernel.md`
5. `claims/theorems/T-91006-rh-is-one-fixed-safe-scale-levy-hardy-gram-positivity.md`
6. `claims/lemmas/L-91031-boundary-jordan-channel-has-an-explicit-poisson-chaos-complement.md`
7. `claims/refutations/R-91006-diagonal-cauchy-gates-cannot-replace-the-fixed-scale-levy-gram.md`
8. `experiments/X-91028-levy-fock-hardy-completion/`
9. `reports/gpt56-pro/2026-08-11-levy-fock-hardy-radical-reset.md`
10. parent main claims `L-91014`–`L-91026`.

## Exact new objects

```text
one-particle vector:
  v_(a,s)(tau,n)=1_[0,a](tau) n^(-s-tau)
  in L2(2 Lambda(n) d tau)

Fock kernel:
  <Exp(v_(a,s)),Exp(v_(a,t))>=Q_a(s+conj(t))

scale product:
  v_(a+b,s)=v_(a,s) direct-sum v_(b,s+a)

boundary Levy measure:
  sum_(prime powers n)
  [Lambda(n)/log n](1-n^(-2a))n^(-c) delta_(log n)

causal analyzer:
  Psi_a(u)=sqrt(378)a^3 u(u+i sqrt(alpha)a)(u+i sqrt(beta)a)
           /[(u+ia)^2(u+2ia)^2(u+4ia)^2]

fixed-scale tests:
  Fourier(f_(a,x)^epsilon)(lambda)
  =lambda Psi_a^epsilon(lambda-x)

bridge:
  Fourier(b_a)=Psi_a/u-conj(Psi_a)/u

new complete kernel:
  K_(a0)(i,j)=<G_(g_zeta) F_i,F_j>
```

## Proposed theorem boundary

The local stack proposes, subject to independent review,

```text
RH
<=>
K_(a0) is PSD on every finite rational carrier/orientation packet
```

for **one arbitrary fixed** `a0>1/2`.

The most review-sensitive joint is the weighted Hardy–Wiener form-core theorem:

```text
span{causal modulated derivatives,
     anti-causal modulated derivatives,
     one bridge}
=
complete weighted mean-zero screw space.
```

The distributional half-line argument and bridge integrals should be checked
cold, including Fourier signs, boundary atoms at zero and the weighted-space
continuity estimate.

## Exact finite replay

```bash
cd experiments/X-91028-levy-fock-hardy-completion
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

Expected:

```text
PASS_LEVY_FOCK_HARDY_COMPLETION
```

The replay proves finite identities and synthetic controls only.

## Integration classification

```text
Nakamura–Suzuki screw/ID criterion                IMPORTED PUBLISHED
Jordan source bosonic Fock realization            PROPOSED COMPLETE EXACT
compound-Poisson boundary channel                 PROPOSED COMPLETE EXACT
causal screw localization                         PROPOSED COMPLETE EXACT
admissibility constant                            EXACT
one-fixed-scale form core                         PROPOSED COMPLETE / REVIEW PRIORITY
one-fixed-scale RH criterion                      PROPOSED COMPLETE / RH-EQUIVALENT
diagonal-only closure                             REFUTED EXACTLY
conservative completed Fock/Hardy colligation     OPEN / RH-EQUIVALENT
Riemann Hypothesis                                UNPROVED
```

Do not merge as a proof claim.  Preserve upstream/local separation: none of
these local additions is part of the Anthropic Zeta23 Lean formalization.
