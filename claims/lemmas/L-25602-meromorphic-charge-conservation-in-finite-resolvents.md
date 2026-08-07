# L-25602 — Meromorphic charge conservation in finite resolvents

Claim ID: `L-25602`  
Title: A finite geometric inverse may move the reciprocal-zeta principal part between its base and terminal residual, but cannot remove it from both  
Status: **PROPOSED EXACT MEROMORPHIC LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-07  
Issue: #256  
Dependencies: elementary local order calculus; `L-23007`  
Scope: every analytic residual parametrization of a finite inverse-zeta expansion

## 1. General finite resolvent

Let `M(s)` and `R(s)` be meromorphic near one nontrivial zeta zero `rho` and
assume

\[
\boxed{1-R(s)=\zeta(s)M(s).}
\tag{L-25602.1}
\]

For an integer `K>=1`, the geometric identity gives

\[
\boxed{
{1\over\zeta(s)}
=M(s)\sum_{j=0}^{K-1}R(s)^j
+{R(s)^K\over\zeta(s)}.}
\tag{L-25602.2}
\]

Call the first term the finite base packet and the second the terminal
residual.

Let `rho` have multiplicity `m`, so

\[
\zeta(s)=(s-\rho)^m g(s),
\qquad g(\rho)\ne0.
\tag{L-25602.3}
\]

## 2. Holomorphic base forces the full pole into the residual

Assume `M` is holomorphic at `rho`. Then

\[
1-R(s)=O((s-\rho)^m),
\]

and hence

\[
R(s)=1+O((s-\rho)^m).
\tag{L-25602.4}
\]

For every finite `K`,

\[
R(s)^K=1+O((s-\rho)^m).
\]

Multiplying the Laurent expansion of `1/zeta` by this factor changes only its
holomorphic part. Therefore

\[
\boxed{
\operatorname{PP}_{\rho}
{R^K\over\zeta}
=
\operatorname{PP}_{\rho}{1\over\zeta}.}
\tag{L-25602.5}
\]

This recovers and generalizes the standard finite-Möbius statement of
`L-23007`.

## 3. Killing the residual pole forces the pole into the base

Assume now that `R` is holomorphic near `rho` and that the residual
`R^K/zeta` is holomorphic there.  If `R(rho)\ne0`, the residual has the same
order-`m` pole as `1/zeta`, a contradiction.  Thus

\[
R(\rho)=0.
\tag{L-25602.6}
\]

Equation (L-25602.1) then gives

\[
1-R(\rho)=1,
\]

so `zeta M` is nonzero at `rho`. Consequently

\[
\boxed{
M(s)
={1-R(s)\over\zeta(s)}
}
\tag{L-25602.7}
\]

has a pole of exact order `m` at `rho`, with the same principal part as
`1/zeta` up to multiplication by the holomorphic unit `1-R`.

Thus a construction which makes the top residual reciprocal-free necessarily
places the reciprocal-zeta singularity in its depth-zero/base row.

## 4. Local order identity

Write `ord_rho f` for the local order, positive for a zero and negative for a
pole.  Equation (L-25602.1) gives the exact balance

\[
\boxed{
\operatorname{ord}_\rho M
=
\operatorname{ord}_\rho(1-R)-m.}
\tag{L-25602.8}
\]

If `r=ord_rho R>0`, then

\[
\operatorname{ord}_\rho(R^K/\zeta)=Kr-m,
\tag{L-25602.9}
\]

while `ord_rho(1-R)=0`, so `ord_rho M=-m`.  If `R(rho)\ne0`, then the residual
order is `-m`.  These are the two basic locations of the conserved charge.

## 5. Complete-tail control

Let

\[
a_V(n)=
\begin{cases}
1,&n=1\text{ or }n>V,\\
0,&2\le n\le V,
\end{cases}
\]

with Dirichlet series

\[
A_V(s)=1+\sum_{n>V}n^{-s}.
\]

Put

\[
R_V^{\rm tail}(s)=1-A_V(s)=-\sum_{n>V}n^{-s},
\]

\[
M_V^{\rm tail}(s)={A_V(s)\over\zeta(s)}.
\tag{L-25602.10}
\]

Then `1-R_tail=zeta M_tail`, and `R_tail` has arithmetic coefficients supported
strictly above `V`.  Its `K`-fold residual is coefficientwise absent through
`V^K`, while

\[
R_{\rm tail}(\rho)=0
\]

at every nontrivial zero.  Hence the terminal residual is holomorphic for
`K>=1` to the extent dictated by (L-25602.9), but the base
`M_tail=A_V/zeta` carries the complete reciprocal-zeta pole.

This example compresses the **terminal factorization dimension** without
weakening the analytic obstruction.

## 6. Consequence for boundary-charge proposals

Neither of the following proves a vanishing RH exponent:

1. a standard finite inverse with holomorphic base and a top residual having
   bounded incidence;
2. a complete-tail inverse with reciprocal-free top residual and a singular
   depth-zero base.

A valid proof must estimate the component carrying the conserved principal
part.  In the fixed-ratio scalar projection this component is the Mertens shell
of PRs #229/#234.

Therefore a charge count is meaningful only after the proof object states
where the reciprocal-zeta principal part lives and proves a source-specific
coercive estimate for that component.

## 7. Proof boundary

Closed exactly here:

- the finite geometric identity;
- full-principal-part retention for holomorphic bases;
- transfer of the pole to the base when the residual is killed;
- the local-order conservation law;
- the complete-tail control example.

Not closed:

- any estimate for the charged component;
- fixed-ratio shell coercivity;
- RH.
