# O-32401 — The critical source is a neutral mode, not a contractive mode

Claim ID: `O-32401`  
Status: **PROPOSED SYNTHESIS / SCOPE FIREWALL**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: PR #302 `L-28014`; PR #323 `R-32201`; `L-32401/L-32402`

## 1. What the newest branches jointly show

Two recent exact calculations change the right proof target.

PR #302 `L-28014` factors the complete shifted central analytic resolvent as

```text
(I-C)^(-1)=(I-K)^(-1)(I-U)^(-1),
```

where the shifted-lattice dressing `K` is a strict contraction on the declared
critical power-log jet bank. The noncontractive core is the reciprocal-eta / local
Euler source carried by `(I-U)^(-1)`.

PR #323 gives the complementary spectral firewall. At every critical-line zeta
zero the eta transfer has a neutral multiplier. Hence a translation-invariant
norm containing the actual zeta oscillatory mode cannot make the complete
source transfer strictly contractive without also suppressing legitimate
critical-line modes.

`L-32402` shows the same phenomenon survives the whole real local-Euler homotopy:
finite dyadic Euler factors do not cancel any off-line zeta pole.

## 2. Correct recurrence shape

The correct all-scale theorem should therefore have the form

```text
principal RH-bearing source:
    coefficient-one delayed recurrence;

analytic / lattice / endpoint dressing:
    strict contraction or polylog forcing.
```

A model scalar inequality is

\[
 \boxed{
 E(J)
 \le C(1+J)^A
   +\sup_{u\le J-\delta}E(u),
 \qquad\delta>0.
 }
\tag{O-32401.1}
\]

No coefficient `<1` is required on the principal mode. Iterating (O-32401.1)
only `O(J/delta)` times gives

\[
 \boxed{E(J)=O((1+J)^{A+1}),}
\tag{O-32401.2}
\]

which is already subexponential and therefore sufficient for every pole-energy
criterion in the current dyadic source programme.

This recurrence is compatible with neutral critical-line oscillations and still
excludes every mode with positive horizontal exponent.

## 3. Why this matters for current proposals

A proposed proof should be rejected if it seeks a strict contraction of the
complete reciprocal-zeta/eta state in a norm that contains the critical
oscillatory modes. Strict contraction is appropriate only after the principal
source has been split off.

Conversely, a coefficient-one delay should not be dismissed as too weak. It is
already sufficient to turn a polynomial forcing term into a polynomial global
energy bound.

The most source-complete current candidate for the neutral principal state is
the atomized two-contact field of `L-28011`, now diagonalized exactly by
`L-32401`. Its transverse logarithmic Selberg sector has the explicit positive
source matching of `L-28009/L-28010`; endpoint energy has the finite absorption
of `L-28015`; shifted-lattice dressing is controlled by `L-28014`.

Thus the live missing theorem is no longer naturally a strict `theta<1`
contraction. It is a coefficient-one lower-scale recurrence for the Brownian
tail charge of `L-32401`, with every transverse term paid by the already proved
strict reserves.

## 4. Status boundary

This observation changes the target architecture; it does not prove the
coefficient-one recurrence. RH remains unproved.