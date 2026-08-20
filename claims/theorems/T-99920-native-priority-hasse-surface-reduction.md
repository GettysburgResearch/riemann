# T-99920 — Native priority-Hasse surface reduction

Claim ID: `T-99920`  
Status: **UNCONDITIONAL REDUCTION + CONDITIONAL RH THEOREM; ONE ARITHMETIC GATE OPEN**  
Created: 2026-08-20  
Frozen base: PR #667 at `7c044d232198265974dd8f4a530b98c6653dba55`  
RH status: **unproved**

Let

\[
B(X)=\frac{(\mathcal S_{67}h)(X)}{\sqrt X}
=\sum_{n\le X}\frac{\beta(n)}n\Phi_{67}(X/n),
\qquad
\beta=(\varepsilon-\delta_{67})*\mu.
\]

Represent the source by one Boolean label of activity `1/p` for every prime `p!=67` and two labelled copies of `67`, each of activity `1/67`.  At each finite endpoint only finitely many labels are active.

`L-99920` constructs a canonical odd-to-even Hasse flow which exactly matches the complete weighted Euler cube.  `L-99921` truncates this flow by the physical box potential and proves

\[
\boxed{[-B(X)]_+\le\mathcal U_X,}
\tag{T-99920.1}
\]

where

\[
\mathcal U_X
=\sum_i
\sum_{\substack{A\subseteq\{i+1,\ldots,k\}\\|A|\ {m odd}}}
\lambda_iw(A)
[\Phi_X(P_A)-\Phi_X(p_iP_A)].
\tag{T-99920.2}
\]

Equivalently,

\[
\boxed{
[-(\mathcal S_{67}h)(X)]_+
\le\sqrt X\,\mathcal U_X.
}
\tag{T-99920.3}
\]

`L-99922` gives the exact product-boundary coarea

\[
\mathcal U_X
=\int\mathcal C_X(t)\,d\nu_X(t),
\]

so every loss is owned by the first prime whose literal native Hasse edge crosses an activation threshold.

Define the remaining theorem

\[
\boxed{
\mathrm{UPBF67}(Y):
\quad
\int_2^Y\sqrt X\,\mathcal U_X\frac{dX}{X}
=Y^{o(1)}.
}
\tag{T-99920.4}
\]

If `UPBF67` holds, (T-99920.3) gives subpower logarithmic negative mass for the zero-free factor-67 box.  The specialized Mellin-Landau theorem on the frozen base then implies RH.  Hence

\[
\boxed{\mathrm{UPBF67}\Longrightarrow\mathrm{RH}.}
\tag{T-99920.5}
\]

`L-99923` additionally identifies the Cauchy-Poisson/GPMOC square with an exact coefficient-tail coarea.  Thus the Hasse and Hardy formulations share the same multiplicative boundary geometry.

## Exact status

```text
native 1/p duplicate-67 source               PROVED EXACT
complete weighted Hasse matching             PROVED EXACT
activation-truncated feasible flow            PROVED EXACT
arbitrary min-cut <= upward priority flux      PROVED EXACT
product-boundary Stieltjes coarea              PROVED EXACT
Poisson Gram = coefficient-tail square         PROVED EXACT
UPBF67 surface-flux estimate                   OPEN / RH-BEARING
Riemann Hypothesis                             UNPROVED
```

This packet does not claim `UPBF67` or RH.
