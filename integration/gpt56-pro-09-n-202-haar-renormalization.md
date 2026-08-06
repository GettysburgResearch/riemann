# Integration handoff — Haar renormalization criterion

Stack on PR #202. Keep every new claim `PROPOSED` until independently reviewed.

Recommended review order:

1. `claims/theorems/T-20201-single-haar-renormalization-rh-criterion.md`
2. `claims/lemmas/L-20201-exact-haar-prime-formula.md`
3. `claims/theorems/T-20202-real-axis-complete-monotonicity-rh-criterion.md`
4. `experiments/X-20201-haar-renormalization/verify.py`
5. methodology, observation, and report

Load-bearing checks:

- sign and factor in `D=4Psi-Psi(2t)`;
- the transform factor `2/z^2`;
- multiplicity in the dyadic pole cancellation;
- Landau abscissa argument with an epsilon-dependent one-sign correction;
- exact finite prime weights and positive Lerch factorization;
- Laplace uniqueness and Stieltjes moment determinacy.

No merge should describe this as a proof of RH. The serious path is the all-order Stieltjes/Hankel factorization or the cofinal arithmetic defect inequality.
