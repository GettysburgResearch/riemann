# L-97810 — The root scalar is the zero Lorenz hinge and needs only a root Bellman budget

Claim ID: `L-97810`  
Status: **PROVED EXACT FINITE/ALGEBRAIC REDUCTION**  
Created: 2026-08-18  
Depends on: PR #590 `L-97700/L-97701`; compared with PR #591 `L-97700`  
RH status: **not assumed**

Retain PR #590's exact largest-prime identity

\[
 U_{\rm full}(X)=U_Z(X)-\mathfrak I_Z(X)-\mathfrak T_Z(X),
\tag{L-97810.1}
\]

where `Z=(log X)^(1/4)`, the complete small-prime cube `U_Z` is positive,
`mathfrak I_Z=o(U_Z)` is the terminal Type-I range, and `mathfrak T_Z` is the
largest-prime-owned signed Type-II term.

Define the **root-only balanced large-prime estimate** `RBLPTE67` by

\[
 \boxed{
 \mathfrak T_Z(X)\le U_Z(X)-\mathfrak I_Z(X)
 }
\tag{L-97810.2}
\]

for every sufficiently large root endpoint `X`.

Then (L-97810.2) is exactly equivalent to

\[
 \boxed{U_{\rm full}(X)\ge0}
\tag{L-97810.3}
\]

at that endpoint.  No state-wise inequality is logically required for the
Mellin consumer: eventual root positivity for every real `X` is enough.

## Zero-hinge identification

For the completed paired source `(E,O)`, let the source capacities, target
coordinates and nonnegative scalar coordinates be `(a_i,t_i,r_i)`.  The
forward Lorenz dual slack is

\[
 D^+(\lambda)=\lambda T_O+
 \sum_{i\in E}a_i(r_i-\lambda t_i)_+-R_O.
\]

At `lambda=0`, all `r_i>=0`, and therefore

\[
 \boxed{D^+(0)=R_E-R_O.}
\tag{L-97810.4}
\]

After the common root normalization, `R_E-R_O=U_full(X)`.  Thus the scalar
route is exactly the **zero-hinge slice** of the completed Lorenz problem.
Consequently

\[
 \mathrm{CPSL67}\Longrightarrow\mathrm{RBLPTE67},
\tag{L-97810.5}
\]

but the converse is not a formal implication.

## Exact strictness countermodel

Take one even atom `(a,t,r)=(1,1,1)` and one odd atom `(1,2,1/2)`.  Then

\[
 D^+(0)=1-\frac12=\frac12>0,
\]

so the scalar is positive.  But the odd target demand is `2`, while total even
target capacity is `1`; completed Lorenz feasibility fails, and
`D^+(lambda)->-infinity` as `lambda->-infinity`.

Hence all-hinge `CPSL67` and state-wise `BLPTE67` are stronger than the exact
root scalar obligation.  They remain useful sufficient mechanisms, but they
should not be advertised as the minimal theorem needed by Mellin--Landau.
