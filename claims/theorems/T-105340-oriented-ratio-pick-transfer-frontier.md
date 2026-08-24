# T-105340 — Oriented-ratio Pick transfer frontier

Claim ID: `T-105340`  
Status: **EXACT REDUCTION + CONDITIONAL RECORD TRANSFER**  
Depends on: T-105310, T-105320, T-105330, L-105340--L-105343

The low-order Hermite--Pick matrix for `Xi/Xi'` is the alpha derivative at zero
of the oriented divisor of

\[
\mathcal M_\alpha=(\xi'-\alpha\xi)/(\xi'+\alpha\xi).
\]

This is exact on finite contours, confluent at multiple critical points, and
cancels persistent Xi factors. The functional equation folds the left safe
line onto the right, where the tangent is the single reciprocal source
`xi/xi'`.

The former gate `SUEF105330` is replaced by the smaller gate
`RATIOXFER105340`:

```text
Evaluate the one-copy and two-copy Wick-preconditioned safe-line integrals of
xi/xi' in the source-owned one-sided frame, retaining the explicit
archimedean-freezing and horizontal/taper errors.
```

The reciprocal Dirichlet tail beyond `X=T^lambda` is already power-saving by
L-105342. Separate shifted-zero canonical products and a shifted seam theorem
are no longer required.

If `RATIOXFER105340` supplies the T-105320 one-percent trace/HS margins, the
multiplicity-robust line proportion is `0.676831...`. That quantitative matrix
estimate is not proved here.

```text
oriented ratio identity                  PROVED EXACT
confluent Pick tangent                   PROVED EXACT
common-factor cancellation              PROVED EXACT
functional-equation folding             PROVED EXACT
reciprocal coefficient tail             PROVED POWER-SAVING
RATIOXFER105340                          OPEN / RECORD-BEARING
new zero proportion / RH                 UNPROVED
```
