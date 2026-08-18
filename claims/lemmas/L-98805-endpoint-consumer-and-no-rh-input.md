# L-98805 — The native deficit enters the one-sided endpoint consumer without an RH-strength premise

Claim ID: `L-98805`
Status: **PROPOSED COMPLETE DEPENDENCY COMPILATION / NO-RH-INPUT AUDIT**
Depends on: `L-98804`; frozen `T-91313`; endpoint/WSTS, prime-square and Mellin-Landau chain
RH status: **conclusion only**

For every ordinarily feasible row `d`, finite summation gives

\[
 \mathcal H(d)=\sum_q\Lambda(q)\Gamma_q(d)
 \le\sum_q\Lambda(q)w_X(q)=P_\Lambda(X).
\]

Hence the native prime-power gap satisfies

\[
\boxed{
 F_\Lambda(X)
 \le J_\Lambda(X)-\mathcal H(d_X)
 =\Delta_X(d_X).
}
\]

By `L-98804`, the right side is `O(1)`, and therefore

\[
 F_\Lambda(X)=o(\log^2X).
\]

The frozen endpoint theorem converts this one-sided estimate, together with the
prime-square moat, into eventual prime-endpoint negativity.  The frozen
Mellin-Landau and functional-equation chain then excludes zeros with real part
greater than one half.  Reflection gives the opposite side.

The new producer uses none of the following as an input:

```text
RH or GRH;
CPBD or a balanced Type-II estimate;
M(X)=O(X^(1/2+eps));
a fixed zero-free strip;
a power-saving PNT remainder;
J_Lambda(X)-4sqrt(X)=O(log X);
a source-blind large-sieve or coherence bound.
```

The only zeta-zero argument appears after the explicit native-deficit producer
has been constructed.
