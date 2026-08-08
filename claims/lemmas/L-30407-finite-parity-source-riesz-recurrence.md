# L-30407 — Exact finite parity-source Möbius–Riesz recurrence

Claim ID: `L-30407`  
Title: The correctly inverted finite parity boundary is the current critical Möbius–Riesz state minus a strict dyadic child with coefficient `1-eta(1/2)`, plus one explicit half-pole mode  
Status: **PROPOSED COMPLETE EXACT SOURCE THEOREM — INDEPENDENT REVIEW REQUESTED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Dependencies: `L-30405`; elementary Dirichlet eta and finite multiple-Möbius inversion  
Scope: exact finite parity source; no norm contraction or RH conclusion

## 1. Parity load and finite source

Fix `N>=4` and put

\[
Q=\left\lfloor{N+1\over2}\right\rfloor.
\tag{L-30407.1}
\]

For a complex parameter with `Re(s)>0`, define the alternating parity load

\[
\boxed{
P_{N,s}(q)=
\sum_{rq>N}{(-1)^r\over(rq)^s}
\qquad(2\le q\le Q).}
\tag{L-30407.2}
\]

The tail converges by Dirichlet's test, locally uniformly on compact subsets of
`Re(s)>0`.

Its unique finite divisor source on `2<=m<=Q` is

\[
\boxed{
\sigma_{N,s}(m)
=\sum_{d\le Q/m}\mu(d)P_{N,s}(md).}
\tag{L-30407.3}
\]

All sums in (L-30407.3) are finite.

## 2. Critical Möbius–Riesz state

For real `y>=0`, set

\[
\boxed{
M_s(y)=\sum_{d\le y}{\mu(d)\over d^s}.}
\tag{L-30407.4}
\]

The floor convention is understood. At `s=1/2`, this is the critical
Möbius–Riesz state

\[
M_{1/2}(y)=\sum_{d\le y}{\mu(d)\over\sqrt d}.
\tag{L-30407.5}
\]

Also put

\[
\eta(s)=\sum_{r\ge1}{(-1)^{r-1}\over r^s}
=(1-2^{1-s})\zeta(s).
\tag{L-30407.6}
\]

## 3. Exact formula in the absolute-convergence half-plane

Assume first `Re(s)>1` and

\[
2\le m\le\left\lfloor{N\over2}\right\rfloor.
\tag{L-30407.7}
\]

The infinite multiple-Möbius transform of `P_(N,s)` is zero at such `m`, by
`L-30405.19`. Therefore the finite source is minus the omitted `d>Q/m` part.

For

\[
{Q\over m}<d\le{N\over m},
\]

one has `N/(md) in [1,2)`, so the alternating tail begins at `r=2` and equals

\[
(md)^{-s}[1-\eta(s)].
\tag{L-30407.8}
\]

For `d>N/m`, the tail begins at `r=1` and equals

\[
-(md)^{-s}\eta(s).
\tag{L-30407.9}
\]

Hence

\[
\begin{aligned}
\sigma_{N,s}(m)
=-m^{-s}\Bigg(&[1-\eta(s)]
 [M_s(N/m)-M_s(Q/m)]\\
&-\eta(s)[\zeta(s)^{-1}-M_s(N/m)]\Bigg).
\end{aligned}
\tag{L-30407.10}
\]

Using

\[
{\eta(s)\over\zeta(s)}=1-2^{1-s},
\]

this simplifies to

\[
\boxed{
\sigma_{N,s}(m)
={1\over m^s}
\left[
-M_s(N/m)
+[1-\eta(s)]M_s(Q/m)
+1-2^{1-s}
\right].}
\tag{L-30407.11}
\]

## 4. Continuation to the critical exponent

The left side of (L-30407.11) is a finite sum of alternating tails and is
holomorphic on `Re(s)>0`. The right side consists only of finite Dirichlet
polynomials and the entire eta function. Therefore the identity theorem
continues (L-30407.11) to all `Re(s)>0`.

At `s=1/2`, write

\[
\boxed{
\rho_2=1-\eta(1/2).}
\tag{L-30407.12}
\]

The alternating-series bounds give

\[
0<\eta(1/2)<1,
\qquad
\boxed{0<\rho_2<1.}
\tag{L-30407.13}
\]

Thus the exact critical source is

\[
\boxed{
\sigma_{N,1/2}(m)
={1\over\sqrt m}
\left[
-M_{1/2}(N/m)
+\rho_2M_{1/2}(Q/m)
+1-\sqrt2
\right]}
\tag{L-30407.14}
\]

for every `2<=m<=floor(N/2)`.

## 5. Source-coordinate interpretation

Define the current-scale state

\[
\boxed{
\mathfrak M_N(m)
={1\over\sqrt m}M_{1/2}(N/m).}
\tag{L-30407.15}
\]

Then (L-30407.14) is the strict dyadic source recurrence

\[
\boxed{
\sigma_{N,1/2}(m)
=-\mathfrak M_N(m)
+\rho_2\mathfrak M_Q(m)
+(1-\sqrt2)m^{-1/2}.}
\tag{L-30407.16}
\]

The coefficient multiplying the child state is the absolute constant

\[
\rho_2=1-\eta(1/2)<1.
\]

The final term is a pure half-pole lattice mode. It is not a second arithmetic
state.

Equation (L-30407.16) is the precise finite-source version of the analytic
parity collapse in `L-30405`. It identifies the discrepancy between finite and
analytically regularized inversion without an unspecified remainder.

## 6. Exceptional top coordinate

When `N` is odd, `Q=(N+1)/2` is the one source coordinate strictly above `N/2`.
It is exactly the collar coordinate already isolated in `L-30405.7`. Removing
that one atom leaves (L-30407.14) on the complete remaining source range.

No growing endpoint family is omitted.

## 7. Consequence for the terminal proof graph

The exact large terminal source is not arbitrary. After the shift and collar
channels are removed, it has the form

```text
-current Möbius–Riesz state
+ rho_2 * half-scale Möbius–Riesz state
+ half-pole null mode,

0<rho_2<1.
```

Therefore any physical norm or signed carry functional which:

1. treats the half-pole mode in its declared null quotient;
2. retains the signs in (L-30407.16); and
3. exports the source coordinate `mathfrak M_N` without taking total variation

will inherit a genuine factor-`rho_2` dyadic contraction.

The absolute adjacent-tree norm fails precisely because it replaces the signed
difference in (L-30407.16) by the sum of the magnitudes of its three terms.

## 8. What remains to complete RH

Equation (L-30407.16) is a source recurrence, not yet a norm recurrence. A full
proof still has to construct one exact source-compatible physical or carry
functional `E_N` for which

\[
E_N
\le \rho_2 E_Q+N^{o(1)}
\]

follows from (L-30407.16) without losing the sign to Cauchy or total variation.

This theorem does not assign that missing implication to a reviewer. It proves
the complete coefficient identity and states accurately that the compatible
norm theorem remains unproved.

## 9. Proof boundary

Proved exactly here:

- the finite parity-source formula for `Re(s)>1`;
- analytic continuation to `Re(s)>0`;
- the critical source recurrence;
- the strict coefficient `0<rho_2<1`;
- isolation of the only exceptional collar coordinate;
- identification of the precise cancellation destroyed by the absolute norm.

Not proved here:

- a source-compatible norm recurrence;
- Cycle Debt, WSTS, or RH.
