# R-107300 — Full augmentation and independent marked places are invalid closure shortcuts

Claim ID: `R-107300`  
Status: **BINDING TWO-PART STRUCTURAL FIREWALL**  
Created: 2026-08-30  
Depends on: PR #765; `L-107301--L-107302`  
Programme issues: #763, #737, #739  
RH/GRH status: **unproved**

## 1. Independent marked-place products

The native Wick pair lies in one fixed shared \((\ell,\rho)\) conductor fibre.
Giving its two atoms independent marked-place pairs replaces the physical
coefficient relation by a product allocation of strictly larger rank. PR #765
already gives exact finite matrices witnessing this rank tax.

Therefore a \(Z_0\times Z_1\) model is not the native source.

## 2. Full augmentation is not automatically nonconstant

When \(Q\equiv1\pmod4\), the even quadratic Kummer character belongs to
\(\mathscr A_Q\), and its pullback under \(z\mapsto z^2\) is constant.

At \(Q=5\), the augmentation has rank one and is exactly this quadratic
character. Its square pullback is the constant sheaf.

Thus the implication

```text
connected augmentation
  -> no constant constituent after the physical square map
  -> Deligne cancellation
```

is false.

The correct object is the reduced augmentation tensor
\(\mathscr C_{\ell,\rho}^{\rm nr}\), plus the explicit one-coordinate and
two-coordinate quadratic resonance rows in `L-107302.5`.

## 3. Rank-by-rank absolute values remain forbidden

Even after resonance removal, bounding every character constituent
separately and summing absolute values pays the augmentation rank. A valid
global proof must estimate the relative object or its pushed-forward
cohomology coherently.

These firewalls do not refute the shared-conductor programme. They identify
the unique honest local object and the exact residual rows.
