# T-15117 — Correct coupled window/readout target-preservation criterion

Claim ID: `T-15117`  
Status: **PROVED COMPOSITION THEOREM; TWO WINDOW-BODY ESTIMATES OPEN**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-01  
Dependencies: `L-15139`, `L-15140`, `T-15116`  
Scope: replace the impossible readout-only proof by an exact body-plus-tail schedule

## 1. Explicit schedule

Assume the spectral hypotheses of `L-15139` with exponent `a>1/4`.  Choose

\[
 N(M)=\left\lceil
 (2^M\beta_M)^{1/(a-1/4)}
 \right\rceil,
\tag{T-15117.1}
\]

so every `S_4` readout tail used below is at most `2^-M`.

Let

\[
 b_M=\|C_M\|_4,
\]

and define the complete-window raw pullback body error

\[
 r_M(r)=
 \sup_{|w|\le r}|g_M^{\rm lin}(w)-g_{A,M}(w)|.
\tag{T-15117.2}
\]

## 2. Uniform comparison bounds

Suppose, along the windows,

\[
 \sup_M
 \bigl(\|\widetilde R_M\|_4+
       \|R_M\|_4\bigr)
 \le B<\infty,
\tag{T-15117.3}
\]

and

\[
 \|A_M\|_2,\|K_M\|_2\le C.
\tag{T-15117.4}
\]

The finite-readout maps inherit the same bounds up to the explicit compression
tails.

## 3. Necessary and sufficient body conditions for this schedule

For the schedule (T-15117.1),

\[
 \boxed{
 \|C_{M,N(M)}\|_4
 \le b_M+2^{-M},}
\tag{T-15117.5}
\]

and also

\[
 \boxed{
 \|C_{M,N(M)}\|_4
 \ge b_M-2^{-M}.}
\tag{T-15117.6}
\]

Therefore

\[
 \|C_{M,N(M)}\|_4\to0
 \iff b_M\to0.
\tag{T-15117.7}
\]

Likewise, for every `r<1/C`, there is an explicit constant `D_(B,C)(r)` such
that

\[
 \boxed{
 |\rho_{M,N(M)}(r)-r_M(r)|
 \le D_{B,C}(r)2^{-M}.}
\tag{T-15117.8}
\]

Hence

\[
 \rho_{M,N(M)}(r)\to0
 \iff r_M(r)\to0.
\tag{T-15117.9}
\]

## 4. Target-preservation conclusion

If the two genuine window-body estimates

\[
 \boxed{b_M\to0,}
\tag{T-15117.10}
\]

and

\[
 \boxed{r_M(r)\to0\quad\text{for every }r<1/C}
\tag{T-15117.11}
\]

hold, then the coupled schedule proves

\[
 \|C_{M,N(M)}\|_4\to0,
 \qquad
 \rho_{M,N(M)}(r)\to0.
\]

The estimates of `T-15116` then give local convergence of the Ward determinant
ledger to the original Guinand--Weil ledger.  If the latter tends to the
centered completed-zeta logarithmic derivative and the same finite operators
converge in `S_2` to a self-adjoint `K`, the determinant identity and RH follow.

## 5. Quartic first gate

Before attempting all orders it is necessary to prove

\[
 \boxed{
 a_{4,M}^{\rm lin}\to\tau_4,
 \quad
 \operatorname{Tr}(A_{M,N(M)}^4)\to\tau_4,
 \quad
 \operatorname{Tr}(K_{M,N(M)}^4)\to\tau_4.}
\tag{T-15117.12}
\]

The difference of the latter two is bounded by

\[
 4C^3\|A_{M,N(M)}-K_{M,N(M)}\|_2,
\]

and the finite-jet factorization gives

\[
 \|A-K\|_2
 \le B\|C_{M,N(M)}\|_4.
\tag{T-15117.13}
\]

Thus the quartic ladder can falsify the proposed small-jet route before an
all-orders calculation: a persistent directed lower bound on the realized jet
or on `|Tr A^4-Tr K^4|` rules it out.

## 6. Exact status

The coupled `N(M)` schedule and every readout-tail estimate are now explicit.
The unsolved content is no longer a choice of readout growth.  It is exactly the
pair of complete-window body limits (T-15117.10)--(T-15117.11), beginning with
the realized quartic jet of `L-15140` and the raw quartic pullback.
