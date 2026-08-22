# L-105201 — Uniform high-derivative critical-residue rigidity

Claim ID: `L-105201`  
Status: **PROPOSED UNCONDITIONAL ASYMPTOTIC THEOREM; exact derivation from L-105200**  
Created: 2026-08-23  
Depends on: `L-105200`; PR #720 `L-104522--L-104524`  
RH status: **not assumed**

## 1. Natural common box

Fix `eta,C,H` as in `L-105200`. Put

\[
a_N^*=\max_{\eta N-2\le r\le N+2}a_r,
\qquad
T_N={C\over a_N^*}.
\tag{L-105201.1}
\]

Then

\[
T_N\asymp_{\eta,C}\sqrt{N/\log N}.
\tag{L-105201.2}
\]

For every integer

\[
\eta N+1\le m\le N-1,
\]

write

\[
F_m=\Xi^{(m)},
\qquad
\kappa_m={M_{m-1}\over M_{m+1}}.
\tag{L-105201.3}
\]

## 2. Real-rootedness on the natural window

For all sufficiently large `N`, every zero of `F_m` in

\[
|\Re z|\le T_N,
\qquad
|\Im z|\le H
\]

is real and simple, simultaneously for all `m` in the displayed band.
Moreover, each zero is paired with exactly one model zero

\[
x_{j,m}
={\bigl(j+\tfrac12-\tfrac m2\bigr)\pi\over w_m}
\]

and

\[
\boxed{
\sup_{|x_{j,m}|\le T_N+1/w_m}
 w_m|c_{j,m}-x_{j,m}|
\longrightarrow0.
}
\tag{L-105201.4}
\]

For every regular `0<T<=T_N`,

\[
\boxed{
R_m(T):=\#\{c\in(-T,T):F_m(c)=0\}
={2w_mT\over\pi}+O(1),
}
\tag{L-105201.5}
\]

uniformly in the band.

### Proof

Use the model (L-105200.9). Around every trigonometric zero take a disk of
radius `rho/w_m`, with one fixed `0<rho<pi/4`. On its boundary the cosine
factor has a fixed positive lower bound, while the normalized error tends to
zero uniformly. Rouché gives one zero in every disk. On the complement,

\[
|\cos(x+iy)|^2=\cos^2x+\sinh^2y
\]

excludes further zeros exactly as in `L-104504`; the zero-free Gaussian factor
causes no change. Conjugation symmetry makes every one-zero disk contain a real
zero. Shrinking `rho` after `N` gives (L-105201.4), and counting model cells
gives (L-105201.5).

## 3. Uniform residue rigidity

For every real zero `c` of `F_m` in `(-T_N,T_N)`, define

\[
\rho_{m,c}
={F_{m-1}(c)\over F_{m+1}(c)}.
\tag{L-105201.6}
\]

Then

\[
\boxed{
\sup_{\substack{\eta N+1\le m\le N-1\\
 F_m(c)=0,\ |c|<T_N}}
\left|
{\rho_{m,c}\over-\kappa_m}-1
\right|
\longrightarrow0.
}
\tag{L-105201.7}
\]

In particular, all these residues are negative for sufficiently large `N`.
Thus every high-band critical point in the natural box is a Rolle-generating
extremum, not a wrong extremum.

### Proof

Put

\[
\theta_r(x)=w_rx+{r\pi\over2}.
\]

At a zero `c` of `F_m`, (L-105200.9) gives

\[
\theta_m(c)=\left(j+{1\over2}\right)\pi+o(1)
\tag{L-105201.8}
\]

uniformly. By (L-105200.5) and `|c|<=T_N`,

\[
(w_{m\pm1}-w_m)c=o(1).
\tag{L-105201.9}
\]

Hence

\[
\theta_{m-1}(c)=j\pi+o(1),
\qquad
\theta_{m+1}(c)=(j+1)\pi+o(1).
\tag{L-105201.10}
\]

The adjacent Gaussian widths satisfy

\[
(a_{m\pm1}^2-a_m^2)c^2=o(1)
\tag{L-105201.11}
\]

uniformly, by (L-105200.4), adjacent comparability, and
`a_m^2c^2=O(1)`. Applying (L-105200.9) at orders `m-1` and `m+1` therefore gives

\[
F_{m-1}(c)
=2M_{m-1}e^{-a_m^2c^2/2}(-1)^j(1+o(1)),
\]

\[
F_{m+1}(c)
=-2M_{m+1}e^{-a_m^2c^2/2}(-1)^j(1+o(1)).
\]

Their quotient is (L-105201.7).

## 4. Native residue scale

The concentration theorem also gives

\[
{M_{m+1}\over M_m}
=\int u\,d\nu_m(u)
=w_m+O(a_m),
\]

and the same formula one order below. Therefore

\[
\boxed{
\kappa_mw_m^2\longrightarrow1
}
\tag{L-105201.12}
\]

uniformly in the band. Since `w_m=(1/2)log m+O(loglog m)`, the common residue
scale is

\[
\boxed{
\kappa_m={4+o(1)\over(\log m)^2}.
}
\tag{L-105201.13}
\]

## 5. Exact coherence identity

For any finite family of negative residues write

\[
-\rho_j=\kappa a_j,
\qquad a_j>0.
\]

Then the residue coherence of `L-104522` is exactly

\[
\boxed{
\mathfrak C
={\bar a^2\over \overline{a^2}}
=1-{\operatorname{Var}(a)\over\overline{a^2}}.
}
\tag{L-105201.14}
\]

Thus uniform residue rigidity controls coherence at second order; it does not
merely control the sign count.

## 6. Firewall

Real-zero location alone is not enough for (L-105201.7). If

\[
f_C(x)={x^3\over3}-x+C,
\]

then

\[
f_C'(x)=x^2-1
\]

has the same two simple real zeros for every `C`, while

\[
{f_C(1)\over f_C''(1)}={C-2/3\over2},
\qquad
{f_C(-1)\over f_C''(-1)}=-{C+2/3\over2}.
\]

Changing only the integration constant changes the residue signs and
coherence. The canonical positive-frequency companion and the simultaneous
adjacent-order Gaussian approximation are therefore load-bearing.
