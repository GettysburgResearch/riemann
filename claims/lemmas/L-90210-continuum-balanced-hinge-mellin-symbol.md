# L-90210 — The broad quarter-balanced hinge occupation has an explicit reciprocal-zeta Mellin symbol with no deterministic cancellation

Claim ID: `L-90210`  
Status: **PROPOSED COMPLETE CONTINUUM ANALYTIC LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-10  
Depends on: continuum child law and characteristic of `L-90209`; elementary Möbius/Mellin calculus  
Scope: the scale-invariant continuum model associated to the ordered balanced policy; finite-policy convergence is not asserted here and RH is not proved

## 1. Continuum square-root hinge source

For `x>=1`, define

\[
 u(x)=\sum_{k\le x}\mu(k)
 \left(\sqrt{\frac{x}{k}}-1\right).
\tag{L-90210.1}
\]

This is the scale profile of the multiples-Möbius primitive for the hinge

\[
 h_T(q)=q^{-1/2}-T^{-1/2}
\]

under `x=T/n`.

On every open integer cell,

\[
 u'(x)=\frac1{2\sqrt x}
 \sum_{k\le x}\frac{\mu(k)}{\sqrt k}.
\]

Put

\[
 \boxed{
 g(x)=xu'(x)
 =\frac{\sqrt x}{2}
 \sum_{k\le x}\frac{\mu(k)}{\sqrt k}.
 }
\tag{L-90210.2}
\]

This is the continuum size-weighted source corresponding to `nr_n`.

## 2. Broad-policy Green operator

The continuum child law of `L-90209` is

\[
 p(v)=4v\mathbf1_{1/4\le v\le3/4}.
\]

The transpose occupation operator acting on scale profiles is

\[
 \boxed{
 (\mathcal Km)(x)
 =4\int_{4/3}^{4}m(x/t)t^{-2}\,dt
 =\frac4x\int_{x/4}^{3x/4}m(y)\,dy,
 }
\tag{L-90210.3}
\]

with the convention `m(y)=0` for `y<1`.

The associated Green occupation is the solution of

\[
 \boxed{m=g+\mathcal Km.}
\tag{L-90210.4}
\]

This equation is the scale-invariant continuum model of the finite recurrence
`L-90209.5`; this lemma studies the continuum equation itself and does not use a
finite-to-continuum error estimate.

## 3. Mellin transform of the arithmetic source

For `Re s>1`, finite switching gives

\[
\begin{aligned}
 \widehat g(s)
 &=\int_1^\infty g(x)x^{-s-1}\,dx\\
 &=\frac12\sum_{k\ge1}\frac{\mu(k)}{\sqrt k}
   \int_k^\infty x^{-s-1/2}\,dx\\
 &=\boxed{
 \frac1{2(s-1/2)\zeta(s)}.
 }
\end{aligned}
\tag{L-90210.5}
\]

Thus the square-root hinge source exposes `1/zeta(s)` with one Riesz factor.

## 4. Mellin multiplier of the broad Green operator

For any function in the initial convergence class, scaling `x=ty` gives

\[
 \widehat{\mathcal Km}(s)
 =\kappa(s)\widehat m(s),
\tag{L-90210.6}
\]

where

\[
 \boxed{
 \kappa(s)
 =4\int_{4/3}^{4}t^{-s-2}\,dt
 =\frac4{s+1}
 \left[\left(\frac34\right)^{s+1}
       -\left(\frac14\right)^{s+1}\right].
 }
\tag{L-90210.7}
\]

This is exactly

\[
 \kappa(s)=\phi(s-1)
\]

for the selected-child Mellin moment `phi` of `L-90209`.

Put

\[
 \Delta_{\rm bal}(s)=1-\kappa(s).
\tag{L-90210.8}
\]

Then (L-90210.4) gives the exact continuum symbol

\[
 \boxed{
 \widehat m(s)
 =\frac{1}
 {2(s-1/2)\zeta(s)\Delta_{\rm bal}(s)}.
 }
\tag{L-90210.9}
\]

initially for `Re s>1`, and then by meromorphic continuation.

## 5. Real-axis geometry and the positive main pole

For real `s`, because `0<V<1`,

\[
 \kappa(s)=\mathbb E[V^{s-1}]
\]

is strictly decreasing. Hence

\[
 \Delta_{\rm bal}(s)
 \begin{cases}
 <0,&s<1,\\
 =0,&s=1,\\
 >0,&s>1.
 \end{cases}
\tag{L-90210.10}
\]

At `s=1`, `1/zeta(s)` has a simple zero and `Delta_bal` has a simple zero, so
the quotient is removable.

At the critical point,

\[
 \kappa(1/2)
 =\frac83\left[\left(\frac34\right)^{3/2}
                -\left(\frac14\right)^{3/2}\right]
 =\sqrt3-\frac13,
\]

and therefore

\[
 \boxed{
 \Delta_{\rm bal}(1/2)=\frac43-\sqrt3<0.
 }
\tag{L-90210.11}
\]

Also `zeta(1/2)<0`: this follows directly from the alternating eta continuation,
because `eta(1/2)>0` while `1-2^{1/2}<0`.

Consequently the pole at `s=1/2` has **positive** residue

\[
 \boxed{
 C_{\rm bal}
 =\frac1{2\zeta(1/2)(4/3-\sqrt3)}>0.
 }
\tag{L-90210.12}
\]

This is the deterministic positive square-root main mode visible in the large
finite hinge occupations.

## 6. Every off-line zeta zero survives

Let `rho` be a nontrivial zeta zero with

\[
 \Re\rho>1/2.
\]

The factor `Delta_bal` is analytic there.  It occurs in the **denominator** of
(L-90210.9), not the numerator.  Therefore it cannot cancel the pole of
`1/zeta(s)` at `rho`; if `Delta_bal(rho)=0`, the singularity can only become
stronger.

Thus

\[
 \boxed{
 \zeta(\rho)=0,\ \Re\rho>1/2
 \quad\Longrightarrow\quad
 \widehat m(s)\text{ is singular at }s=\rho.
 }
\tag{L-90210.13}
\]

This is an important distinction from the frozen first-entrance factorization
of `L-90204`, where a boundary-dependent deterministic numerator could in
principle cancel an arithmetic pole.

## 7. Continuum one-sign criterion implies RH

By `L-90209`, `Delta_bal` has no zeros on `Re s>=1` except the removable
conservation root, and in fact has a strict deterministic gap.  On the positive
real interval `(1/2,1)`, (L-90210.10) shows directly that it is nonzero.  Zeta
has no real zeros there.  Hence the only positive-real singularity of
`widehat m` before `1` is the explicit main pole at `s=1/2`.

Suppose

\[
 m(x)\ge0
\]

for every sufficiently large `x`.  If an off-line zero `rho` existed with
`beta=Re rho>1/2`, (L-90210.13) would give a nonreal singularity to the right of
the main pole.  The abscissa of convergence of the eventually nonnegative
Mellin source would then be at least `beta`; Landau's one-sign theorem would
force a singularity at the positive real point equal to that abscissa.  No such
real singularity exists.  Contradiction.

Therefore

\[
 \boxed{
 m(x)\ge0\text{ eventually}
 \quad\Longrightarrow\quad\mathrm{RH}.
 }
\tag{L-90210.14}
\]

Functional-equation symmetry supplies the other side of the critical line.

This is a continuum criterion, not an unconditional positivity theorem.

## 8. Critical logarithmic target

The same calculation shows why the logarithmic critical target is smoother.
Its multiples-Möbius scale primitive has Mellin transform

\[
 \frac1{(s-1/2)^2\zeta(s)},
\]

and differentiating to the size source gives an additional factor `s`.  Thus
the broad-policy critical occupation has the formal continuum symbol

\[
 \boxed{
 \widehat m_{\log}(s)
 =\frac{s}
 {(s-1/2)^2\zeta(s)\Delta_{\rm bal}(s)}.
 }
\tag{L-90210.15}
\]

The double critical pole produces a positive `sqrt(x) log x` main term, while
nontrivial zeros retain an extra Riesz denominator relative to the hinge
criterion.  This helps explain why direct critical-target reconnaissance is even
more stable numerically than individual hinges.

No sign theorem for (L-90210.15) is claimed.

## 9. Proof boundary

Proved for the continuum model:

1. the exact square-root Möbius source;
2. the broad transpose Green operator;
3. its Mellin multiplier;
4. the exact reciprocal-zeta occupation symbol;
5. positivity of the critical main residue;
6. automatic survival of every hypothetical off-line zeta zero;
7. eventual continuum occupation positivity implies RH;
8. the logarithmic-target symbol.

Still open:

- positivity of the continuum hinge or logarithmic occupation;
- a sufficiently sharp finite-to-continuum theorem for `L-90209.5`;
- finite OBH;
- RH.