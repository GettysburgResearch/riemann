# R-100400 — The normalized cell deficit is not the Mellin–Landau deficit

Claim ID: `R-100400`  
Status: **EXACT NORMALIZATION REFUTATION / REPAIR FIREWALL**  
Created: 2026-08-20  
Base: PR #685 at `4f69b7656f42dcb5ff250d13adc9f88e8d18f315`  
RH status: **unproved**

Let

\[
\mathcal E_2(X)
=
16\frac{1-67^{-3/2}}{\zeta(3/2)}X-\mathfrak H_2(X).
\]

On an integer cell \(N\le X<N+1\), put \(t=\sqrt X\).  The cell formula of
PR #685 has the form

\[
\mathcal E_2(t^2)=P_N(t)=A_Nt^2+B_Nt+C_N.
\]

Therefore

\[
\frac{\mathcal E_2(t^2)}{t^2}
=
A_N+\frac{B_N}{t}+\frac{C_N}{t^2}.
\]

The primitive

\[
-2A_N\log t+\frac{2B_N}{t}+\frac{C_N}{t^2}
\]

differentiates to

\[
-\frac{2}{t}\frac{\mathcal E_2(t^2)}{t^2}.
\]

Consequently it computes

\[
\boxed{
\int [-\mathcal E_2(X)/X]_+\frac{dX}{X},
}
\]

not

\[
\boxed{
\int [-\mathcal E_2(X)]_+\frac{dX}{X}.
}
\]

The correct cell primitive for the unnormalized deficit is

\[
\boxed{
-A_Nt^2-2B_Nt-2C_N\log t,
}
\]

because \(dX/X=2\,dt/t\).

This distinction is conclusion-facing.  Dividing by \(X\) shifts every Mellin
singularity one unit to the left.  A negative-mass estimate for
\(\mathcal E_2(X)/X\) therefore does not preserve the positive-half-plane
reciprocal-zeta poles used by the claimed Landau consumer.

Hence the `CATD100300 -> RH` arrow in PR #685 is invalid as written.  The
corrected route in `L-100400` uses the unnormalized activation-zero envelope and
its proper logarithmic measure.
