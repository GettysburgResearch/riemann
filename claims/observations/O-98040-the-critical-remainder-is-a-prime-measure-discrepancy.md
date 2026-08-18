# O-98040 — The critical remainder is a prime-measure discrepancy, not an unsigned base error

PR #603 writes the native state as a positive homogeneous Dickman main plus two
absolute errors: a discrete-prime discrepancy and an unsigned bound for the
bounded `P_61` source remainder. `L-98040` recombines the exact source before
estimation:

\[
U(Y,z)=\int A_z(Y/x)\,dh(x).
\]

The continuous comparison is therefore

\[
\mathcal C_L(u)=\int\rho(u-\log x/L)\,dh(x),
\]

and the only discrete error is

\[
\int[A_z(Y/x)-\rho(u-\log x/L)]\,dh(x).
\]

It is controlled by the prime-measure discrepancy times the fixed total
variation of `h`. This observation explains why the previous
`O(1/log z)` bounded-remainder barrier is not intrinsic and why the
Vinogradov--Korobov error becomes available for the complete source.

The remaining deep critical core is still arithmetic: at fixed or very small
least-prime scale, the prime-measure discrepancy is not small relative to the
Dickman saddle.
