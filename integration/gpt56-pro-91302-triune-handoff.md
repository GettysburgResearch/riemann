# Integration handoff — T-91302 Triune Adelic Scattering Completion

## Branch

```text
research/gpt56-pro/91302-triune-adelic-scattering
```

## Frozen base

```text
main @ b837c12199dd407116f604ce6c938039d1a76da4
```

The proposal depends conceptually on draft PRs #400, #401, and #402 and on the
phase-locked adelic theta-wavelet packet. Integration should preserve those
exact provenances rather than silently treating their open claims as main-line
theorems.

## Review order

1. `L-91307` — common kernel equivalences.
2. `L-91310` §2 — new log-odds Sturm–Liouville identity.
3. `L-91308` — local port and canonical construction.
4. `L-91309` — source/output spaces and AOT.
5. `T-91302` — full implication chain.
6. `R-91302` — mandatory controls.
7. experiment and checksums.
8. full report.

## Promotion status

```text
full unconditional proposal: YES
full proof of RH:             NO
ready for hostile review:     YES
ready for theorem promotion:  NO
```

## Exact remaining theorem

Prove `AOT_a` for every `a` in one predetermined sequence tending to zero:

\[
\frac{
1-\Theta_a(z)\overline{\Theta_a(w)}
}{
-i(z-\bar w)
}
=
\langle q_{a,w},q_{a,z}\rangle_{\theta,\beta,\mathrm{Pois},2}.
\]

The right side must use the explicit source-ordered vector declared by the
proposal; an abstract square root of the left side is forbidden.
