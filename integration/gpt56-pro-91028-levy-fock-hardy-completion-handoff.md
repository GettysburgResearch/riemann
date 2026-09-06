# Integration handoff — Lévy–Fock–Hardy radical reset

## Freeze and drift reconciliation

```text
repository:       gfreund123/riemann
creation base:    d8536ff561f269523a8997be289b49fea1d23267
main at PR open:  b837c12199dd407116f604ce6c938039d1a76da4
branch:           research/gpt56-pro/91028-levy-fock-hardy-completion
PR:               #400
cutoff:           2026-08-11T20:51:40Z
RH:               unproved
```

Main advanced during the session and claimed IDs `L-91028`, `L-91029`, and
`T-91006`.  The local additions were therefore renumbered before handoff:

```text
L-91030  Jordan source -> bosonic Fock product system
L-91031  zeta screw -> causal/anti-causal Cauchy localization
L-91032  one fixed safe scale is a complete screw form core
L-91033  boundary Jordan channel -> explicit Poisson chaos complement
T-91007  RH <=> one fixed-scale Levy-Hardy Gram positivity
R-91007  diagonal Cauchy-gate polarization firewall
```

Main's `T-91006` is retained as the Cauchy–Jordan Hardy Intertwiner proposal.
`T-91007` should be read as a fixed-scale completion and sharpening of that
proposal, not as a competing reuse of its identifier.

## Review order

1. `literature/external/2026-08-11-nakamura-suzuki-screw-source-lock.md`
2. main `L-91028`, main `L-91029`, and main `T-91006`
3. `claims/lemmas/L-91030-generalized-jordan-source-has-an-explicit-bosonic-fock-product-system.md`
4. `claims/lemmas/L-91031-zeta-screw-kernel-localizes-through-the-causal-cauchy-wavelet.md`
5. `claims/lemmas/L-91032-one-fixed-safe-scale-is-a-form-core-for-the-zeta-screw-kernel.md`
6. `claims/theorems/T-91007-rh-is-one-fixed-safe-scale-levy-hardy-gram-positivity.md`
7. `claims/lemmas/L-91033-boundary-jordan-channel-has-an-explicit-poisson-chaos-complement.md`
8. `claims/refutations/R-91007-diagonal-cauchy-gates-cannot-replace-the-fixed-scale-levy-gram.md`
9. `experiments/X-91028-levy-fock-hardy-completion/`
10. `reports/gpt56-pro/2026-08-11-levy-fock-hardy-radical-reset.md`
11. parent main claims `L-91014`–`L-91029`.

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
K_(a0) is PSD on every finite rational carrier/orientation/bridge packet
```

for one arbitrary fixed `a0>1/2`.

The most review-sensitive joint is `L-91032`:

```text
span{causal modulated derivatives,
     anti-causal modulated derivatives,
     one bridge}
=
complete weighted mean-zero screw space.
```

Check cold:

- distributional inversion in the half-line Wiener argument;
- Fourier orientation and boundary atoms at zero;
- nonvanishing of the causal mother almost everywhere;
- bridge half-line integrals;
- weighted-space continuity of the screw form.

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
main CJHI and compound-Poisson spine              RETAINED / OPEN
Jordan source bosonic Fock realization            PROPOSED COMPLETE EXACT
causal screw localization                         PROPOSED COMPLETE EXACT
admissibility constant                            EXACT
one-fixed-scale form core                         PROPOSED COMPLETE / REVIEW PRIORITY
one-fixed-scale RH criterion                      PROPOSED COMPLETE / RH-EQUIVALENT
diagonal-only closure                             REFUTED EXACTLY
completed Poisson-Fock/Hardy colligation           OPEN / RH-EQUIVALENT
Riemann Hypothesis                                UNPROVED
```

Do not merge as a proof claim.  None of these local additions is part of the
Anthropic Zeta23 Lean formalization.
