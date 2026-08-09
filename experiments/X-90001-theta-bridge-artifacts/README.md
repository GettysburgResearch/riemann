# X-90001 — theta-bridge validation artifacts (session 2026-08-08/09)

Rerunnable scripts backing `claims/theorems/T-90001-theta-bridge-equivalence.md`.
What each authenticates (none is a proof; they validate stated identities/bounds numerically):

- `validator.py` — exact decomposition T^s(z)=Phi_s+E_s vs raw definitions, all z, X=500..2e5 (Deriver-1 normal form).
- `d2_validator.py` — independent kernel-route decomposition (Deriver-2 normal form).
- `xcheck.py` — reconciliation of the two normal forms (regroup identity to 4.6e-11), if present.
- `xmellin.py` / `wsts_converse.py` — Mellin/Landau consumer checks; radical bridge V=V1-V2 to 1.6e-11 at X=1e6.
- `wsts_verify.py`, `wsts_verify2.py` — Prop-1 bridge + moat + floor numerics (uncond-status agent).
- `kernel_profile.py` — band-resolved kernel-difference constants (log 2 envelope).
- `moat_adv.py`, `moat_grid.py` — adversarial re-derivation of the Moat chain: symbolic J' identity, knot continuity, global closed form for H, 4M-point H_c<=0 grids (c in {1/3,0.4,1/2}).
- `adv_item4.py` — adversarial check of the consumer: Ehat identity, Ehat(1)=0, pole residues.

Environment: python3 + numpy + sympy + mpmath. SHA256SUMS covers all files.
