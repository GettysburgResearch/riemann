# T-104501 — Original-height high derivative entry closes; one Xi defect gate remains

Claim ID: `T-104501`  
Status: **UNCONDITIONAL HIGH-DERIVATIVE ENTRY + EXACT ONE-GATE RH REDUCTION**  
Created: 2026-08-22  
Depends on: `L-104500--L-104504`  
RH status: **unproved**

`L-104504` proves the formerly open growing-box input: for every fixed height
`T` and every `H>1/2`, some sufficiently high even derivative of Xi has only
simple real zeros in

\[
R_{T,H}=\{z:|\Re z|\le T,\ |\Im z|\le H\}.
\]

Choose such an order `r(T)`.  The exact transport of `L-104501` gives

\[
O_{R_{T,H}}(\Xi)
=
2\sum_{k<r(T)}E_k(T)
+
\sum_{k<r(T)}
\bigl(B_{k,-}(T)+B_{k,+}(T)+W_k(T)-1\bigr).
\tag{T-104501.1}
\]

Define the right side as `C_RP(T)`.  It is automatically a nonnegative even
integer because it equals the number of off-real Xi zeros in the symmetric
rectangle.

Therefore the single remaining theorem

\[
\boxed{
\mathrm{RPCH104501}:\qquad C_{RP}(T)<2
\quad\text{for every sufficiently large }T
}
\tag{T-104501.2}
\]

implies

\[
O_{R_{T,H}}(\Xi)=0.
\]

Letting `T` grow yields RH.

Thus

\[
\boxed{\mathrm{RPCH104501}\Longrightarrow\mathrm{RH}.}
\tag{T-104501.3}
\]

## Exact boundary

```text
factor-two real conservation                 PROVED
complex winding transport                    PROVED
Riccati/Pick dictionary                      PROVED
fixed-scaled high derivative entry           PROVED
fixed original-height high derivative entry  PROVED
RPCH104501 cumulative charge <2              OPEN / RH-BEARING
Riemann Hypothesis                           UNPROVEN
```

The programme is no longer waiting on a growing-order Levinson–Conrey theorem
for the high-derivative base case.  Such estimates may still help with the
remaining charge, but the base case is supplied directly by the positive Xi
Fourier kernel and Laplace concentration.
