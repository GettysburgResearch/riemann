# T-98101 — A single polylogarithmic Stieltjes correlation is sufficient for the native scalar

Claim ID: `T-98101`  
Status: **UNCONDITIONAL REDUCTION; STIELTJES SIGN OPEN**  
Created: 2026-08-18  
Depends on: `L-98103`, `T-98100`  
RH status: **unproved**

Fix `epsilon>0`, set

\[
Z=(\log\log\log X)^2,
\qquad
Y=(\log X)^{4+\epsilon},
\]

and define

\[
\mathcal J_\epsilon(X)
=
\int_2^Y S_Z(X/y)\,dU_Z(y).
\tag{T-98101.1}
\]

Let `mathcal B_epsilon(X)` be the explicit debt in `T-98100.1`. The exact
summation identity and the two endpoint/bulk estimates give

\[
\boxed{
|U_{\rm full}(X)-\mathcal J_\epsilon(X)|
\le2\mathcal B_\epsilon(X),
\qquad
\mathcal B_\epsilon(X)=o(1/\log X).
}
\tag{T-98101.2}

Define **Polylogarithmic Stieltjes Transport 67 (`PLST67`)** by

\[
\boxed{
\mathcal J_\epsilon(X)
\ge2\mathcal B_\epsilon(X)
}
\tag{T-98101.3}

for one fixed `epsilon>0` and every sufficiently large real `X`. Then

\[
\boxed{
\mathrm{PLST}_{67}
\Longrightarrow
U_{\rm full}(X)\ge0\text{ eventually}
\Longrightarrow
\mathrm{GPC}_{67}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-98101.4}

The open theorem is now one signed correlation on a one-dimensional child
interval of polylogarithmic length. The two factors are:

```text
S_Z(X/y):  long-scale rough reciprocal-Mobius prefix;
dU_Z(y):   exact complete-cube child innovation.
```

Neither factor may be replaced by its modulus. The child innovation is a signed
bounded-variation measure, and the rough prefix does not have a proved uniform
sign. Their common-source pairing is the conclusion-producing object.

At finite `X`, `U_Z` has finitely many activation knots on `[2,Y]`; therefore
`mathcal J_epsilon` is an exact finite sum of elementary logarithmic integrals
against a step prefix. A strict negative value supplies a replayable separator
consisting of

```text
root endpoint X;
slow cutoff Z;
child window [2,Y];
rough-prefix jump products;
active base-kernel cells;
directed scalar interval.
```

## Boundary

```text
exact Stieltjes identity                   PROVED
child window <= log^(4+epsilon) X         PROVED
endpoint and bulk debt o(1/log X)         PROVED
PLST67                                    OPEN / RH-BEARING
GPC67                                     OPEN / IMPLIED BY PLST67
Riemann Hypothesis                        UNPROVEN
```