# X-91403 — Review controls and aggregate regeneration

This small exact replay checks:

- the omitted causal sources `85,86,87` in the historical support formula;
- the mode-dependent score mismatch in the reviewed one-branch identification;
- the failure of source-mass fractions to scale signed packet loss;
- the exact aggregate recanonicalization identity of `L-91410` on rational controls.

The replay is finite algebra only. It does not certify the finite producer, packet normalization, or RH.
