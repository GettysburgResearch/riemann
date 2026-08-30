# L-32705 — The balanced parity-paired Selberg reserve tends to one

Claim ID: `L-32705`  
Title: On every fixed balanced carry cone, the complete parity-paired generalized Selberg forcing is `O_eta(n log^2 n)` while the paired Kummer energy is `Omega_eta(n^2)`  
Status: **PROPOSED COMPLETE QUANTITATIVE THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-09  
Dependencies: corrected `L-32704/R-32702`; PR #334 `L-32405`  
Scope: source-coupled balanced interior reserve; endpoint/collar routing and physical block recurrence remain separate

## 1. Statement

Use the paired generalized-prime and Selberg rows of `L-32704`:

\[
P_\pm(n,j)=\sum_d\Lambda_\pm(d)\chi_{n,d}(j),
\qquad
S_\pm(n,j)=\sum_dC_\pm(d)\chi_{n,d}(j).
\]

Fix

\[
0<\eta\le\frac12
\]

and assume

\[
\eta n\le j\le(1-\eta)n.
\tag{L-32705.1}
\]

Then there is a constant `C_eta` such that, for every sufficiently large `n`,

\[
\boxed{
S_+(n,j)+S_-(n,j)
\le C_\eta n\log^2(2n),}
\tag{L-32705.2}
\]

whereas

\[
\boxed{
P_+(n,j)^2+P_-(n,j)^2
\ge\frac{\eta^2\log^22}{2}\,n^2.}
\tag{L-32705.3}
\]

Consequently

\[
\boxed{
\frac{S_+(n,j)+S_-(n,j)}
 {P_+(n,j)^2+P_-(n,j)^2}
\le
C_\eta'\frac{\log^2(2n)}n
\longrightarrow0.}
\tag{L-32705.4}
\]

Equivalently, the surviving Kummer-square reserve on every fixed balanced cone tends to the full paired current energy.

## 2. Lower bound for the paired current

By parity orthogonalization in `L-32704`,

\[
\frac{P_+^2+P_-^2}{2}
=(O+E)^2+R^2,
\]

with `O,E,R>=0`. Hence

\[
P_+^2+P_-^2\ge2O^2.
\tag{L-32705.5}
\]

By symmetry take `j<=n/2`. The odd Kummer profile satisfies

\[
O
=\log\operatorname{odd}\binom nj
\ge j\log\frac nj-\log n
\]

by Kummer's binary-carry bound. Under (L-32705.1),

\[
j\log\frac nj\ge\eta n\log2.
\]

Thus, for all sufficiently large `n`,

\[
O\ge\frac{\eta\log2}{2}n.
\tag{L-32705.6}
\]

Substitution into (L-32705.5) gives (L-32705.3).

## 3. Odd-prime forcing

`L-32704.26` gives

\[
0\le S_{\rm odd}\le j\log^2n\le n\log^2n.
\tag{L-32705.7}
\]

This is already one power of `n` below the current energy.

## 4. Pure-dyadic forcing

Write the even dyadic destination as `4^r` and let

\[
\mathcal C_r
:=\frac{C_{\rm ev}(4^r)}{(\log2)^2}.
\]

The proof of PR #334 `L-32405` gives, for every `r>=4`,

\[
\mathcal C_r<11r4^r.
\tag{L-32705.8}
\]

The first three coefficients are fixed constants. Therefore, if `R=floor(log_4 n)`,

\[
\begin{aligned}
S_{\rm dyad}
&\le C_0
 +11(\log2)^2\sum_{r=4}^{R}r4^r\\
&\le C_0
 +\frac{44}{3}(\log2)^2 Rn.
\end{aligned}
\tag{L-32705.9}
\]

Hence

\[
\boxed{S_{\rm dyad}=O(n\log(2n)).}
\tag{L-32705.10}
\]

uniformly over every row.

## 5. Mixed current-row divisor boundary

The exact mixed decomposition of `L-32704` is

\[
M=M_<+M_\partial.
\]

For the current-row boundary,

\[
M_\partial
=2\sum_{r\ge1}D_{2r}c_r
 \log\operatorname{odd}(N_r-J_r).
\]

Use the crude but source-complete bound

\[
\log\operatorname{odd}(N_r-J_r)\le\log n.
\]

For `a=4^r`,

\[
D_{2r}=(\sqrt a+1)^2\log2
\le\frac94a\log2.
\]

Therefore

\[
E=\sum_rD_{2r}c_r
\le\frac94\log2\sum_{4^r\le n}4^r
\le3n\log2,
\tag{L-32705.11}
\]

and hence

\[
\boxed{M_\partial\le6n(\log2)\log n.}
\tag{L-32705.12}
\]

No use of the much larger bound `M_partial<=2OE` is needed on the balanced cone.

## 6. Strict four-adic mixed descendants

`L-32704.30` gives

\[
M_<
\le\frac94j
 \log\frac{2en}{j}\,\log j.
\]

Under `j>=eta n`,

\[
\log\frac{2en}{j}
\le\log\frac{2e}{\eta},
\qquad
\log j\le\log n.
\]

Thus

\[
\boxed{
M_<
\le
\frac94\log\frac{2e}{\eta}\,n\log n.}
\tag{L-32705.13}
\]

Again the mixed term is one full power below the current energy.

## 7. Completion

Since

\[
\frac{S_++S_-}{2}
=S_{\rm odd}+S_{\rm dyad}+M_<+M_\partial,
\]

combining (L-32705.7), (L-32705.10), (L-32705.12), and (L-32705.13) gives (L-32705.2).

Division by (L-32705.3) proves (L-32705.4).

In particular, for every fixed `eta`, there is `n_eta` such that on every balanced row above `n_eta`,

\[
\boxed{
S_++S_-
\le\frac12(P_+^2+P_-^2),}
\tag{L-32705.14}
\]

and in fact the factor `1/2` can be replaced by any prescribed positive constant once the finite threshold is enlarged.

## 8. Consequence for the live reflected route

The mixed source block left open on PR #334 is not merely nonnegative cofinally. In the balanced interior its entire linear Selberg forcing is asymptotically negligible compared with the source-matched paired Kummer square.

Thus a future physical two-frequency proof does **not** need to manufacture a delicate current-scale arithmetic reserve inside the balanced cone. The available carry reserve tends to one. The remaining work is sharply localized to:

```text
physical independent-frequency source binding;
finite synthesis shifts;
endpoint/collar rows;
strict-delay / neutral-principal recurrence.
```

This is consistent with the exact endpoint and principal-mode firewalls elsewhere in the repository.

## 9. Proof boundary

Closed here:

- an asymptotically full source-coupled paired Kummer reserve on every fixed balanced cone;
- explicit one-power separation `forcing=O_eta(n log^2 n)` versus `energy=Omega_eta(n^2)`.

Open:

- physical normal-block conversion using this reserve;
- endpoint/collar charge routing;
- the resulting delayed recurrence;
- RH.
