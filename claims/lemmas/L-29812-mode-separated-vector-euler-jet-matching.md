# L-29812 — Mode-separated vector matching for interleaved Euler jets

Claim ID: `L-29812`  
Title: At an even start, every vector-valued interleaved Euler jet splits into a coefficientwise positive parity source plus a smooth Hausdorff alternating source admitting the exact two-sided matching of `L-29810`  
Status: **PROPOSED COMPLETE EXACT SOURCE-DECOMPOSITION LEMMA**  
Authoring agent: `gpt56-02-r`  
Created: 2026-08-08  
Dependencies: `L-29809`, `L-29810`; positive integration  
Scope: exact vector coefficient matching; signed balanced Pascal/debt realization remains separate

## 1. Vector Euler jet

Use the interleaved sequence of `L-29809` and let the starting index `N=2K` be
even.  The node-labeled `m`th jet is

\[
 \boxed{
 V_{N,m}
 =\sum_{r=0}^{m}(-1)^r{m\choose r}a_{N+r}e_{N+r}.}
\tag{L-29812.1}
\]

The two-mode Laplace formula is

\[
 a_{N+r}
 ={1\over\Gamma(s)}\int_0^\infty t^{s-1}
 \left[
  \alpha z^{N+r}+\beta(-z)^{N+r}
 \right]dt,
\tag{L-29812.2}
\]

where `z=e^(-qt)`, `alpha=(e^t+1)/2`, and `beta=(e^t-1)/2`.

## 2. Smooth and parity source decomposition

Since `N` is even,

\[
 (-1)^r(-z)^{N+r}=z^{N+r}.
\]

Substituting (L-29812.2) into (L-29812.1) gives the exact split

\[
 \boxed{V_{N,m}=V_{N,m}^{\rm sm}+V_{N,m}^{\rm par},}
\tag{L-29812.3}
\]

with

\[
\boxed{
\begin{aligned}
V_{N,m}^{\rm sm}
={1\over\Gamma(s)}\int_0^\infty&t^{s-1}\alpha z^N
 \sum_{r=0}^{m}(-1)^r{m\choose r}z^re_{N+r}\,dt,
\end{aligned}}
\tag{L-29812.4}
\]

and

\[
\boxed{
\begin{aligned}
V_{N,m}^{\rm par}
={1\over\Gamma(s)}\int_0^\infty&t^{s-1}\beta z^N
 \sum_{r=0}^{m}{m\choose r}z^re_{N+r}\,dt.
\end{aligned}}
\tag{L-29812.5}
\]

Every coefficient of the parity source (L-29812.5) is nonnegative. It produces
no source-sign debt.

## 3. The smooth mode is exactly Hausdorff

Define

\[
 b_n={1\over\Gamma(s)}\int_0^\infty
 t^{s-1}\alpha(t)z^n\,dt.
\tag{L-29812.6}
\]

Under the change of variable `y=z=e^(-qt)`, this is a Hausdorff moment sequence
on `[0,1]`:

\[
 b_n=\int_{[0,1]}y^n\,d\nu_{q,s}(y)
\tag{L-29812.7}
\]

for a positive measure `nu_(q,s)`.  Consequently

\[
 V_{N,m}^{\rm sm}
 =\sum_{r=0}^{m}(-1)^r{m\choose r}b_{N+r}e_{N+r}
\tag{L-29812.8}
\]

is exactly the source class of `L-29810`.

There exist nonnegative adjacent matching amounts `t_r` and nonnegative even
residuals `rho_r` satisfying

\[
\boxed{
V_{N,m}^{\rm sm}
 =\sum_{r\ {
text{ even}}}\rho_re_{N+r}
 +\sum_{r=0}^{m-1}t_r(-1)^r
  (e_{N+r}-e_{N+r+1}).}
\tag{L-29812.9}
\]

Every negative smooth-mode demand is paid, and

\[
 \sum_{r\ {
text{ even}}}\rho_r=\Delta^mb_N\ge0.
\tag{L-29812.10}
\]

## 4. Full source decomposition

Combining (L-29812.5) and (L-29812.9),

\[
\boxed{
\begin{aligned}
V_{N,m}
={}&V_{N,m}^{\rm par}
 +\sum_{r\ {
text{ even}}}\rho_re_{N+r}\\
&+\sum_{r=0}^{m-1}t_r(-1)^r
  (e_{N+r}-e_{N+r+1}).
\end{aligned}}
\tag{L-29812.11}
\]

Thus all source signs have been reduced to adjacent dipoles. There is no
unmatched higher-order alternating node family.

The scalar residual of (L-29812.11) is

\[
 \Delta^ma_N
 =\Delta^mb_N
 +\sum_{r=0}^{m}{m\choose r}
  {1\over\Gamma(s)}\int_0^\infty
  t^{s-1}\beta z^{N+r}dt,
\]

in agreement with `L-29809.6`.

## 5. Positive superpositions

The decomposition is preserved under every nonnegative superposition over
exponents, stopped endpoints, Taylor channels, and Peano parameters:

1. the parity source remains coefficientwise positive;
2. the integrated smooth weights remain Hausdorff;
3. the weighted Hall inequalities remain valid after integration;
4. finite max-flow supplies one matching for the total smooth source.

Hence the theorem applies to the corrected scalar Euler bank of `L-29809` after
complete common-destination recombination.

## 6. Carry realization boundary

For even `r`, the adjacent dipole

\[
 e_{N+r}-e_{N+r+1}
\]

has the nonnegative central-to-sibling Pascal realization already used in
`L-28302`.

For odd `r`, the reverse dipole

\[
 e_{N+r+1}-e_{N+r}
\]

cannot be a standalone nonnegative carry flow by `R-29805`. It must be retained
as a signed adjacent-tree commutator or recombined with additional positive
source columns.

Therefore (L-29812.11) reduces the complete vector source problem to one
explicit scalar debt ledger:

\[
 \boxed{
 \mathcal D_{N,m}^{\leftarrow}
 =\sum_{\substack{0\le r<m\\r\ {
text{ odd}}}}
 t_r\,\mathcal N_\omega(E_{N+r}),}
\tag{L-29812.12}
\]

where `E_n=T_(n+1)-T_n` is the sparse adjacent-tree commutator of PR #272.

A completed DCD proof must show that the sum of (L-29812.12) over every emitted
jet and exact Euler remainder, after common-destination recombination, is
polylogarithmic and is paired with the lower-flow odd leakage in the same
metric.

## 7. Proof boundary

Proved here:

- exact smooth/parity splitting of the node-labeled jet;
- coefficientwise positivity of the entire parity mode;
- Hausdorff structure of the complete smooth mode;
- exact two-sided matching of all smooth negative demands;
- reduction of every remaining sign to a reverse adjacent dipole.

Open:

- the all-source bound for `mathcal D^leftarrow`;
- exact recombination with PR #272's lower-flow odd leakage;
- DCD;
- RH.
