# R-99610 — Coefficient-only owner quadratic variation is blind on the squarefree sector

Claim ID: `R-99610`  
Status: **PROVED EXACT METHOD FIREWALL**  
Created: 2026-08-20  
Depends on: `L-99610`  
RH status: **not assumed**

Let `n` be squarefree and `67` not divide `n`.  Then

\[
g_{67}(n)=1,\qquad f_{67}(n)=\mu(n)\in\{-1,1\}.
\]

Every owner divisor in (L-99610.8) is a prime `q|n`, and

\[
f_{67}(n/q)=-f_{67}(n).
\]

Therefore

\[
M_{t+1}=(-1)^{t+1}f_{67}(N_t/q)
       =(-1)^tf_{67}(N_t)=M_t
\]

at every step of the owner chain.  The entire coefficient martingale quadratic
variation is exactly zero:

\[
\boxed{\sum_t(M_{t+1}-M_t)^2=0.}
\tag{R-99610.1}
\]

Nevertheless the SHARP boundary contribution

\[
\frac{\mu(n)}{\sqrt n}T(x/n)
\]

is nonzero and is negative for odd `omega(n)`.  Thus no estimate depending only
on the quadratic variation of `f_67` can control the conclusion-facing sign.
This binds the earlier owner-martingale programme at its coefficient-only
scope.

The repair is not to discard the owner chain.  It is to carry the scale
coordinate `x/N_t`; its increments remain nonzero even when parity is
deterministic.  That exact repair is `L-99611`.
