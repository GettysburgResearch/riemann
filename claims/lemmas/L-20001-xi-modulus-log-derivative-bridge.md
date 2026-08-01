# L-20001 — Exact bridge between direct-xi modulus and xi-log-derivative hierarchies

Claim ID: `L-20001`  
Title: The value-only passivity rows are the differential shadow of horizontal completed-xi modulus  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-09-i`  
Created: 2026-08-01  
Dependencies: standard completed-xi normalization; the definitions used in `L-3903` and `L-7501`–`L-7503`  
Scope: exact algebraic relationship between the finite interfaces of PRs #67/#68/#71 and #76  
Related counterexample candidates: none

> This is a new proposed connection found during the pre-publication review. It
> does not repair, promote, or retroactively verify any parent claim.

## Definitions

Use

\[
 \xi(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),
 \qquad
 F(s)=\frac{\xi'(s)}{\xi(s)}.
\]

For fixed real `T`, let

\[
 H_T(x^2)=
 \left|\xi\!\left(\frac12+x+iT\right)\right|^2,
 \qquad x\ge0,
\]

as in `L-7501`, and put

\[
 G_T(u)=\log H_T(u)
\]

wherever `H_T(u)>0`. For `x>0`, write

\[
 R_T(x)=
 \operatorname{Re}F\!\left(\frac12+x+iT\right),
 \qquad u=x^2.
\]

## Exact differential identity

At every `x>0` for which the displayed xi value is nonzero,

\[
 \boxed{
 G_T'(x^2)=\frac{R_T(x)}{x}.}
 \tag{1}
\]

Equivalently,

\[
 \boxed{
 R_T(x)=xG_T'(x^2).}
 \tag{2}
\]

### Proof

Differentiating with respect to `x` gives

\[
 \frac{d}{dx}
 \log\left|\xi\!\left(\frac12+x+iT\right)\right|^2
 =F\!\left(\frac12+x+iT\right)
  +\overline{F\!\left(\frac12+x+iT\right)}
 =2R_T(x).
\]

On the other hand, the chain rule gives

\[
 \frac{d}{dx}G_T(x^2)=2xG_T'(x^2).
\]

Equating the two expressions proves (1)–(2). ∎

## Under RH: one Stieltjes function and two Bernstein functions

Under RH, the genus-zero factorization from `L-7501` gives

\[
 H_T(u)=C_Tu^{m_T}
 \prod_j\left(1+\frac{u}{a_j}\right)^{m_j},
 \qquad a_j=(T-\gamma_j)^2>0.
\]

Therefore

\[
 \boxed{
 G_T'(u)=\frac{m_T}{u}+
 \sum_j\frac{m_j}{u+a_j}}
 \tag{3}
\]

is a Stieltjes function and is completely monotone. Moreover,

\[
 \boxed{
 J_T(u):=uG_T'(u)
 =m_T+
 \sum_jm_j\frac{u}{u+a_j}}
 \tag{4}
\]

is a Bernstein function, because

\[
 J_T'(u)=
 \sum_jm_j\frac{a_j}{(u+a_j)^2}
\]

is completely monotone.

Using (1)–(2), the two value-only objects in `L-3903` are exactly

\[
 \frac{R_T(x)}x=G_T'(u),
 \qquad
 xR_T(x)=J_T(u).
 \tag{5}
\]

## Exact identification of the `A` and `B` rows

For `0<x_1<x_2`, put `u_i=x_i^2` and `D=u_2-u_1`. The `L-3903` two-channel rows become

\[
 \boxed{
 A=
 \frac{R_T(x_1)/x_1-R_T(x_2)/x_2}{D}
 =-[u_1,u_2]G_T'.}
 \tag{6}
\]

Since `G_T'` is decreasing under RH, `A>=0`.

Likewise,

\[
 \boxed{
 B=
 \frac{x_2R_T(x_2)-x_1R_T(x_1)}{D}
 =[u_1,u_2]J_T.}
 \tag{7}
\]

Since `J_T` is increasing under RH, `B>=0`.

More generally, the complete-Bernstein divided-difference row in `L-3903` is
exactly

\[
 \boxed{
 (-1)^{n-1}[u_0,\ldots,u_n]J_T,}
 \tag{8}
\]

and its sign follows immediately from (4).

Thus the scalar, `A`, `B`, and higher value-only rows are not independent
mysteries: they are differential consequences of the same horizontal modulus
function used by `L-7501`–`L-7503`.

## Integral bridge and witness transfer

On every interval with positive modulus,

\[
 \boxed{
 G_T(v)-G_T(u)
 =\int_u^v
 \frac{R_T(\sqrt t)}{\sqrt t}\,dt.}
 \tag{9}
\]

Consequently:

1. scalar passivity `R_T(x)>=0` for all `x>0` implies direct-modulus
   monotonicity;
2. a strict direct-modulus reversal on a zero-free interval forces
   `R_T(x)<0` at some interior point;
3. by continuity, a strict scalar violation then persists at nearby exact
   rational or dyadic points.

This is an existential transfer, not a procedure for locating the interior
point from endpoint intervals alone.

## Pick-diagonal bridge and the real/complex boundary

For the same-height Pick matrix

\[
 K_{jk}=
 \frac{F(s_j)+\overline{F(s_k)}}{x_j+x_k},
 \qquad
 s_j=\frac12+x_j+iT,
\]

the diagonal is

\[
 \boxed{
 K_{jj}=\frac{R_T(x_j)}{x_j}=G_T'(u_j).}
 \tag{10}
\]

For a real vector, the imaginary skew-Hermitian data cancel in the quadratic
form, explaining why the value-only contractions of PR #67 can be reconstructed
from `Re F` alone. A genuinely complex Pick direction depends on the imaginary
primitive rectangles as well; those are the separate finite closures supplied
by PRs #68 and #71.

This distinction prevents the real/value-only feasible anchor from being
misdescribed as closure of the full complex Pick cone.

## Computational consequence

A single directed horizontal table can support two independently conditioned
certificate families:

- direct completed-xi modulus products and differences;
- xi-log-derivative scalar, Bernstein, and real-Pick rows.

The exact bridge suggests a cross-check at each point:

1. evaluate direct completed xi at nearby horizontal nodes;
2. evaluate `xi'/xi` at the center;
3. compare a directed finite-difference enclosure of `log |xi|^2` with the
   directed rectangle for `2 Re(xi'/xi)`.

This does not replace either proof producer, but it provides a normalization and
horizontal-coordinate audit using different special-function outputs.

## Analytic and dependency audit

- Equations (1)–(2) are unconditional wherever the sampled xi value is nonzero.
- Under RH, every `x>0` is zero-free at fixed real `T`, so the identities hold on
  the full positive half-line.
- Equations (3)–(8) import the canonical-product statement of `L-7501`.
- The bridge does not prove the arbitrary-height Pick theorem, a directed
  special-function enclosure, or RH.
- A finite positive table remains finite; no global conclusion is obtained by
  numerical differentiation or integration.

## Gap audit

1. Interval finite differences of a logarithm can be much wider than direct
   derivative balls and require a strictly positive modulus lower endpoint.
2. A modulus rectangle containing zero cannot be logged.
3. The mean-value transfer from a modulus reversal to a scalar violation is
   existential; it does not identify an exact point without an additional
   localization argument.
4. The real-vector Pick restriction must not be conflated with the complete
   complex matrix.
5. This proposed bridge cannot be cited to retroactively verify the frozen
   versions of PR #67 or PR #76.

## Suggested review and experiment

1. Independently verify the chain-rule normalization and the factors of `x` and
   `2`.
2. On a modest directed control table, enclose both sides of (9) and require
   overlap.
3. Re-document PR #67 as the real/differential shadow of PR #76, while keeping
   PRs #68/#71 as the full-complex closures.
