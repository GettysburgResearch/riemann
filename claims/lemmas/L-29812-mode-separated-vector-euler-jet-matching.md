# L-29812 — Mode-separated vector matching for interleaved Euler jets

Claim ID: `L-29812`  
Title: At an even start, every vector-valued interleaved Euler jet splits into a coefficientwise positive parity source plus a smooth Hausdorff alternating source admitting the exact two-sided matching of `L-29810`  
Status: **PROPOSED COMPLETE EXACT SOURCE-DECOMPOSITION LEMMA**  
Authoring agent: `gpt56-02-r`  
Created: 2026-08-08  
Dependencies: `L-29809`, `L-29810`; positive integration  
Scope: exact formal vector coefficient matching; actual arithmetic source binding is treated by `L-29816`

## 1. Vector Euler jet

Use the interleaved sequence of `L-29809` and let the starting index `N=2K` be
even. The node-labeled `m`th jet is

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

Substituting (L-29812.2) into (L-29812.1) gives

\[
 \boxed{V_{N,m}=V_{N,m}^{\rm sm}+V_{N,m}^{\rm par},}
\tag{L-29812.3}
\]

where

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

Every coefficient of the parity source is nonnegative.

## 3. The smooth mode is Hausdorff

Define

\[
 b_n={1\over\Gamma(s)}\int_0^\infty
 t^{s-1}\alpha(t)z^n\,dt.
\tag{L-29812.6}
\]

Under `y=z=e^(-qt)`, this has the Hausdorff representation

\[
 b_n=\int_{[0,1]}y^n\,d\nu_{q,s}(y)
\tag{L-29812.7}
\]

for a positive measure `nu_(q,s)`. Consequently

\[
 V_{N,m}^{\rm sm}
 =\sum_{r=0}^{m}(-1)^r{m\choose r}b_{N+r}e_{N+r}
\tag{L-29812.8}
\]

is the source class of `L-29810`.

There are nonnegative adjacent matching amounts `t_r` and nonnegative
residuals `rho_r` on the even levels such that

\[
\boxed{
V_{N,m}^{\rm sm}
 =\sum_{r\equiv0\,(2)}\rho_re_{N+r}
 +\sum_{r=0}^{m-1}t_r(-1)^r
  (e_{N+r}-e_{N+r+1}).}
\tag{L-29812.9}
\]

Every negative smooth-mode demand is paid, and

\[
 \sum_{r\equiv0\,(2)}\rho_r=\Delta^mb_N\ge0.
\tag{L-29812.10}
\]

## 4. Full formal source decomposition

Combining the smooth matching and the parity source,

\[
\boxed{
\begin{aligned}
V_{N,m}
={}&V_{N,m}^{\rm par}
 +\sum_{r\equiv0\,(2)}\rho_re_{N+r}\\
&+\sum_{r=0}^{m-1}t_r(-1)^r
  (e_{N+r}-e_{N+r+1}).
\end{aligned}}
\tag{L-29812.11}
\]

Thus every formal source sign is reduced to an adjacent dipole.

The scalar residual agrees with `L-29809.6`:

\[
 \Delta^ma_N
 =\Delta^mb_N
 +\sum_{r=0}^{m}{m\choose r}
  {1\over\Gamma(s)}\int_0^\infty
  t^{s-1}\beta z^{N+r}dt.
\]

## 5. Positive superpositions

The decomposition is preserved under nonnegative superposition over exponents,
stopped endpoints, Taylor channels, and Peano parameters:

1. the parity source remains coefficientwise positive;
2. the integrated smooth weights remain Hausdorff;
3. weighted Hall inequalities remain valid after integration;
4. finite max-flow supplies a matching for the total smooth source.

## 6. Carry realization boundary

For even `r`, the formal adjacent dipole has the forward orientation. For odd
`r`, it has the reverse orientation. `R-29805` proves that a reverse divisor
dipole cannot be a standalone nonnegative carry flow.

Moreover, withdrawn `L-29815` shows that one may not multiply the unscaled
Pascal sibling by a common arithmetic destination: noncoprime chains break that
tensorization.

Therefore (L-29812.11) is a coefficient/source decomposition, not by itself an
actual carry-flow construction. `L-29816` supplies the correct proof-facing
route: retain the complete target on actual carry columns, perform the exact
multiples-Möbius decoder, and realize the resulting node divergence with
adjacent-tree commutators.

## 7. Proof boundary

Proved here:

- exact smooth/parity splitting;
- coefficientwise positivity of the parity mode;
- Hausdorff structure of the smooth mode;
- exact two-sided matching of every smooth negative demand;
- reduction of formal signs to adjacent dipoles.

Not proved here:

- tensorized arithmetic source-to-carry binding;
- all-generation boundary norm;
- DCD;
- RH.
