# T-99826 — Fixed-shell Hardy–Carleson closure contract

Claim ID: `T-99826`  
Status: **EXACT CONCLUSION REDUCTION; SIGNED SHELL ESTIMATE OPEN**  
Created: 2026-08-20  
Base: PR #665 / `T99820`  
RH status: **unproved**

The canonical factor-67 scalar admits a fixed, zero-safe compactification

\[
G(X)=\sum_{X/536\le n\le X}
 \frac{\beta(n)}{\sqrt n}\widetilde K(X/n),
\]

where `\widetilde K` is a fixed continuous kernel supported in `[1,536]`.
Its coefficient diagonal is uniformly bounded.

For every `X`, let `N_X` be the least active source integer and define

\[
Q_X
=
\int_{\mathbb R}
\left|
 \sum_nd_X(n)n^{1-i\gamma}
\right|^2
\frac{d\gamma}{\pi(1+\gamma^2)}.
\]

Then

\[
|G(X)|\le N_X^{-1}\sqrt{Q_X},
\]

and the right side is exactly the square root of a nested suffix-tail energy.
Consequently the single sufficient closure theorem is

\[
\boxed{
\int_1^X N_t^{-1}\sqrt{Q_t}\,\frac{dt}{t}=X^{o(1)}.
}
\tag{T-99826.1}
\]

Under (T-99826.1), `G_-` has subpower logarithmic mass. The Mellin multiplier
in `L-99824` is zero-free throughout the conclusion strip, so Landau excludes
every zeta zero with real part greater than one half; the functional equation
gives RH.

The diagonal part of (T-99826.1) is uniformly bounded. The sole open term is
the signed off-diagonal correlation of nested squarefree shell tails.

```text
fixed ratio-536 compact packet        PROVED EXACT
zero-safe conclusion multiplier       PROVED EXACT
uniform coefficient diagonal          PROVED EXACT
support-shifted point evaluation       PROVED EXACT
Hardy suffix-square identity           PROVED EXACT
signed shell Hardy-Carleson estimate   OPEN / RH-BEARING
Riemann Hypothesis                     UNPROVED
```
