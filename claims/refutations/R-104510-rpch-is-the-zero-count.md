# R-104510 — The cumulative RPCH charge is the off-real zero count

Claim ID: `R-104510`  
Status: **PROVED EXACT SCOPE CORRECTION**  
Created: 2026-08-22  
Depends on: `L-104501`, `T-104501`  
RH status: **unproved**

Fix a conjugation-symmetric rectangle `Omega` and a derivative order `r` for
which the hypotheses of `L-104501` hold. Its exact identity is

\[
O_\Omega(F_0)
=
O_\Omega(F_r)
+
2\sum_{k<r}E_k
+
\sum_{k<r}(B_k+W_k-1).
\tag{R-104510.1}
\]

If the high derivative has no off-real zero in the rectangle, then

\[
\boxed{
2\sum_{k<r}E_k
+
\sum_{k<r}(B_k+W_k-1)
=
O_\Omega(F_0).
}
\tag{R-104510.2}
\]

Thus `RPCH104501`, which asks that the left side be less than two, is exactly

\[
O_\Omega(\Xi)<2.
\]

Because the off-real zero count is an even nonnegative integer, this is
equivalent to the desired zero-free conclusion in the rectangle. The RPCH
statement is therefore a valid RH-equivalent detector, but not an independent
estimate or a completed middle arrow.

## Binding consequence

The summands in (R-104510.2) may have cancellation. Bounding the wrong-extremum
and winding pieces independently can only strengthen the problem and can
destroy the exact boundary transport.

The successor programme must locate the *last derivative level at which a
lower-half-plane index is present* and control the one event at which that
index disappears. This is done by the Hermite–Biehler companion in
`L-104510--L-104515`.
