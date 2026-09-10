# The mollified compression: multiplicative weights on the Alpöge–Furman certificate

```text
Status:            PROVED EXACT (T-109300 weighted rank–trace certificate with off-line defect,
                   T-109301 its RH form, L-109302 expansion in the weight parameter,
                   L-109304 order-two identity for the direct-sum family, L-109308 placement of RH
                   in Bui–Heath-Brown); PROVED MODULO CITED INPUTS (T-109305 ceiling 0.6819 for every
                   unconditional trace-moment certificate, T-109307 transfer to Dirichlet L-functions);
                   NUMERICAL RECORD (X-109303); REDUCTION, NOT A THEOREM (R-109306).
                   No unconditional proportion above 2/3 is proved here. RH remains unproved.
Scope:             the unconditional "70 percent" (19/27) for zeta and for every primitive Dirichlet
                   L-function; Alpöge–Furman arXiv:2608.13637v2 and Bui–Heath-Brown arXiv:1302.5018.
Exact sources or dependencies:
                   Alpöge–Furman Lemma 3.2 (rank–trace), the Poisson–Gabor lemma (§2.3), §6 (bandwidth-one
                   ceiling, Lean-certified at the cited tag); Bui–Heath-Brown Lemmas 1–2 and (8);
                   Montgomery (1973); Rudnick–Sarnak (1996); Odlyzko's zeros 1..18816 with zeta'(rho).
What was actually run:
                   scripts/weighted.py, scripts/expansion.py, scripts/hybrid.py on zeros 1000..18816,
                   6000..18816, 12000..18816 (outputs/*.log). RH-numerics only: the certificates are
                   evaluated on the true zeros, which are simple and on the line at these heights.
Smallest remaining gap:
                   the four mollified pair-correlation functionals Lambda_1, Lambda_2, Lambda_2',
                   (Lambda_3, Lambda_4 upper bounds) of L-109302 have no proved asymptotics;
                   unconditionally, the off-line mollified moments S_1^off, S_2^off of R-109306.
```

## Result in one paragraph

Bui–Heath-Brown's 19/27 uses RH exactly once, to identify the contour-computable second moment
`Σ_ρ Bζ'(ρ)Bζ'(1−ρ)` with `Σ_ρ |Bζ'(ρ)|²`. Alpöge–Furman's 2/3 avoids the identification by
compressing Weil's form to a bandwidth-one Gabor family and charging off-line pairs through the
positive index. Theorem 1 (T-109300) combines them: multiply the Gabor family by
`h = 1 + εBζ'`. Because `Bζ'` vanishes at multiple zeros, the multiple zeros keep weight one while
the simple zeros are re-weighted, and the rank–trace lemma gives, exactly and unconditionally,

```text
s_1 ≥ 2 tr W_h − ‖W_h‖²_HS − 2 Σ_{off-line ρ} m_ρ (1 − h(ρ)h(1−ρ)).
```

Under RH the defect term vanishes (Theorem 2) and the certificate is
`2Σ|h(ρ)|² − Σ|h(ρ)|²|h(ρ')|² sinc²(L(γ−γ')/2)`. On Odlyzko's zeros at heights `10^4` it certifies
`0.742–0.745` for the Bui–Heath-Brown mollifier (`θ = 0.45`) against `0.695` for the unweighted
Alpöge–Furman matrix at the same heights, uniformly over three windows, and the small-`ε`
expansion (Proposition 3) attributes the gain to two stable ratios, `X ≈ 0.210·L·N` and
`Y ≈ 4.17·L²·N`, giving `4X²/Y ≈ 0.042` in addition to the finite-height base; projected to the
limit this is `≈ 0.71 > 19/27` under RH, pending the asymptotics of four pair-correlation-weighted
mollified moments (the exact list is in Proposition 3). Unconditionally two things block 70%:
every certificate built from trace moments of bandlimited compressions is bounded by `0.6819`
(Proposition 6, from the Alpöge–Furman ceiling and the Rudnick–Sarnak range), and the weighted
certificate's off-line defect is controlled only by the mollified first and second moments over
off-line zeros (R-109306), which no current zero-density estimate reaches. The adjoined
(direct-sum) family, the other natural hybrid, gains nothing: its order-`ε²` coefficient is
`S_2 − S_2^{pc}`, negative for every mollified weight tested (Proposition 5). Everything transfers
verbatim to primitive Dirichlet `L`-functions (Proposition 7); the family average is already at
`0.811` by Alpöge–Furman's Remark on Dirichlet averaging (§6.3).

Read `PROOF.md`.

## Replay

```bash
cd standalone/2026-09-02-seventy-percent-mollified-compression/scripts
python3 weighted.py 6000     # ~1 minute: certificate values vs eps, three weight families
python3 expansion.py 6000    # ~20 s: the functionals Lambda_k, X, Y, predicted vs exact gain
python3 hybrid.py 6000       # ~1 minute: direct-sum family, sign of S2 - S2pc
```

All arithmetic is double precision on Odlyzko's zeros (`outputs/zetaprime_first18816.txt`, with
`ζ'(ρ)` from mpmath at 20 digits); the theorems do not depend on it.
