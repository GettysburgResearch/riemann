# T-107010 — Trans-Bertrand near-optimal causal compression of the native beta criterion

Claim ID: `T-107010`  
Status: **UNCONDITIONAL THEOREM / NEAR-OPTIMAL RH-EQUIVALENT CRITERION**  
Created: 2026-08-27  
Base: PR #759 at `ebaf1dbcccecd7ed18812e786da40f1d610e497d`  
RH status: **unproved**

There exists one fixed nonzero compact causal \(C^\infty\) detector
\(B_{r,\mathrm{Ber}}\), using the literal source

\[
 \beta=(\delta_1-\delta_{67})*\mu,
\]

with the following properties.

1. Its Laplace multiplier is nonzero throughout the open Mellin--Landau
   half-plane.
2. For every fixed finite Bertrand depth \(m\), its Fourier transform obeys

   \[
   |\widehat B(it)|
   \le
   C_m\exp\{-c_m|t|/W_m(|t|)\}.
   \]

3. For every \(A>0,m\ge0\), the native beta energy has an exact deterministic
   Nyquist truncation with error \(O_A(X^{-A})\) and rank

   \[
   O_{A,m}((\log X)^2W_m(\log X)).
   \]

4. The same fixed detector admits a diagonal deterministic schedule of rank

   \[
   O_A((\log X)^2\Lambda_A(X)),
   \]

   where

   \[
   \Lambda_A(X)=o(W_m(\log X))
   \]

   for every fixed \(m\).

5. No nonzero compact causal detector can reach
   \(O((\log X)^2)\) rank by combining exact Nyquist sampling with
   source-blind Fourier-tail deletion based only on
   \(|D_X(t)|\ll\sqrt X\).

Consequently

\[
 \boxed{
 \mathrm{RH}
 \Longleftrightarrow
 \left\|
 \sum_{n\le X}
 \frac{\beta(n)}{\sqrt n}\mathbf v_X(n)
 \right\|^2
 =
 X^{o(1)}
 }
\]

in a deterministic feature space whose dimension is superquadratic only by
a factor smaller than every fixed Bertrand iterated-log loss.

## Scientific boundary

```text
universal causal smoother                    PROVED
simultaneous all-depth decay                 PROVED
trans-Bertrand deterministic schedule        PROVED
causal exact-quadratic barrier               PROVED
native beta vector estimate NBV107000        OPEN / RH-EQUIVALENT
Riemann Hypothesis                           UNPROVEN
```

The theorem nearly completes the analytic compression problem. It does not
supply the remaining Möbius cancellation.
