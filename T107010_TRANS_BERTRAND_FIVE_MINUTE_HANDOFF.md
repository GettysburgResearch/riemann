# T-107010 — trans-Bertrand causal Nyquist compression

Status: **unconditional near-optimal analytic compression; RH remains unproved**

Parent: PR #759 at `ebaf1dbcccecd7ed18812e786da40f1d610e497d`.

## Result

One fixed compact causal probability smoother is built by interleaving every
finite Bertrand box cascade. Its Fourier transform simultaneously satisfies,
for every fixed depth `m`,

\[
 |\Phi(it)|\le C_m\exp\{-c_m |t|/W_m(|t|)\},
\]

where

\[
 W_m(x)=\prod_{j=1}^m\log_j(e_j+x)\,
        \log_{m+1}(e_{m+1}+x)^2.
\]

The same native beta detector therefore has, for every fixed `m`, an exact
Nyquist truncation of rank

\[
 O_{A,m}\bigl((\log X)^2W_m(\log X)\bigr).
\]

A diagonal choice of depth gives one fixed detector and one deterministic
truncation schedule of rank

\[
 (\log X)^2\Lambda(X),
\]

where `Lambda(X)` is smaller than every fixed Bertrand factor `W_m(log X)`.

## Optimality boundary

A nonzero compact causal detector cannot have an exponentially decaying
Fourier `L2` tail. Hence no source-blind argument using only

\[
 |D_X(t)|\ll\sqrt X
\]

can delete the exterior at `T=O(log X)`. Exact `O(log^2 X)` Nyquist rank is
impossible in this architecture.

The live arithmetic target remains `NBV107000`; low rank still does not imply
cancellation.
