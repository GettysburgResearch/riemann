# R-96500 - An explicit odd rough history reverses a canonical Target-Lorenz leaf and blocks parity-blind projective gluing

Claim ID: `R-96500`
Status: **PROVED EXACT REFUTATION OF THE PR #550 GLUING ARGUMENT**
Created: 2026-08-17
Replay: `X-96500-parity-covariant-gluing`
RH status: **unproved; full-row nonnegativity is not refuted**

Take

\[
X=67\cdot71\cdot13=61841.
\]

Follow the positive least-prime source path with incoming history `(67)`. At
the next rough prime the terminal parameters are

\[
p=71,\qquad y=13<67.
\]

The incoming history has odd length, so `L-96500/L-96501` reverse the canonical
terminal sign.

For `d|P_61`, define the canonical target atom

\[
t_d=d^{-1/2}\left[T(923/d)-71^{-1/2}T(13/d)\right],
\]

where

\[
T(u)=(4\sqrt u-3)\mathbf1_{u\ge1}.
\]

Let

\[
E_T=\sum_{\mu(d)=1}t_d,
\qquad
O_T=\sum_{\mu(d)=-1}t_d.
\]

Exact 192-bit dyadic rational interval arithmetic over all 239 active divisors
proves

\[
\boxed{E_T-O_T>17.}
\tag{R-96500.1}
\]

The canonical Target-Lorenz map removes even source of target mass `O_T`; it is
therefore oriented from `E` to `O`. After the odd history, actual even capacity
is `O_T` and actual odd demand is `E_T`. A reversed exact-target Hall map would
require

\[
O_T\ge E_T,
\]

contradicting (R-96500.1). Thus the terminal map used in `L-96302` cannot be
installed on this leaf while preserving the complete target datum.

This refutes the claimed projective composition, not the desired inequality
`c_X(j)>=0`. Global cancellation between different histories remains possible.
