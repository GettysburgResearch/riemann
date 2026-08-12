# Integration handoff — compressed delay and completed-source correction

## Freeze

```text
cutoff UTC:       2026-08-12T13:49:47Z
main:             b837c12199dd407116f604ce6c938039d1a76da4
parent PR #400:   7dc9fec9eb5fab4ee9340ddbc5a52e36a6ab617e
continuation:     research/gpt56-pro/91306-covariant-tail-hankel-completion
RH:               unproved
```

## Read after the earlier PR #404 packet

1. `claims/refutations/R-91011-arbitrary-delays-do-not-automatically-preserve-the-suzuki-model-space-factorization.md`
2. `claims/lemmas/L-91316-suzuki-model-space-tangent-factors-through-a-fisher-hankel-gram.md`
3. `claims/lemmas/L-91401-positive-delays-have-an-explicit-model-space-julia-colligation.md`
4. `literature/external/2015-nakamura-complete-riemann-zeta-distribution-source-lock.md`
5. `claims/refutations/R-91402-completed-xi-fisher-law-is-not-a-positive-poisson-source.md`
6. corrected experiment, report, and this handoff.

## Lifecycle corrections

Read these earlier claims only through the corrections above:

```text
L-91307  raw-delay statement corrected by R-91011/L-91401;
T-91301  delay placement uses compressed Julia colligation;
L-91313  Fisher/model-space factorization remains exact on resident vectors;
T-91302  common Poisson/Fisher source claim withdrawn by R-91402.
```

The phrase

```text
prime Poisson-Fock output -> completed Fisher-Hardy output
```

is not currently a single proved source isometry. What is proved is a pair of
compatible explicit realizations:

```text
prime Poisson score -> prime tail-Hankel Julia output;
completed xi Fisher score -> completed model-space tangent.
```

## Exact new theorem

For the positive Hardy delay semigroup,

```text
S_tau|K_Theta
 =T_tau + M_Theta R_tau
```

orthogonally, with

```text
T_(tau+sigma)=T_tau T_sigma,
R_(tau+sigma)=R_tau T_sigma+S_tau R_sigma,
T_tau* T_tau+R_tau* R_tau=I.
```

Every mixed-delay cross term is preserved. The bridge has the same explicit
resident/leakage boundary decomposition.

## Exact new firewall

For every safe `a>1/2`, the completed law

```text
xi(1/2+a-it)/xi(1/2+a)
```

is quasi-infinitely divisible but not infinitely divisible by Nakamura's
published theorem. It therefore cannot equal a positive Poisson/Levy source.

## Preferred next attack

Construct the renormalized common-source wave operator

```text
prime Poisson/Julia
 + gamma/pole/theta
 -- W_a -->
completed Fisher-Hankel
 + positive environment.
```

Highest-value order:

1. work first on one finite prime cutoff and one finite delay packet;
2. apply the completed gamma/theta counterterm before taking the source norm;
3. prove the visible block is exactly `A_a` and its prime block exactly
   `H_(beta_a)`;
4. prove cutoff-uniform graph-norm bounds;
5. pass the prime cutoff;
6. adjoin the reflected orientation and bridge;
7. identify the coefficient-one defect with the delayed screw/Weil Gram.

This aligns with PR #403's Julia/Wick/Green production target. Do not attempt a
direct critical Euler-product Hilbert vector or a positive Levy-measure
identification of the completed xi law.
