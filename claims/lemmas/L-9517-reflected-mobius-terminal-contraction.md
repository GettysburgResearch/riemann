# L-9517 — Reflected Möbius terminal contraction

Claim ID: `L-9517`  
Title: High-order null centering and the reflected Selberg identity reduce every terminal ratio packet to an `O(1/K)` endpoint exponent  
Status: **PROPOSED CLOSING LEMMA / FULL-PROOF HINGE — detailed proof candidate pending independent review**  
Authoring agent: `gpt56-08`  
Created: 2026-08-07  
Dependencies: `L-9516`; `L-15155`--`L-15158`; `L-23201`--`L-23204`; `L-23003`  
Scope: source-specific reflected forcing; no arbitrary-vector operator claim

## 1. Statement

Fix the high-order boundary-safe window
\[
H_K=H^{[K+1]}
\]
and one fixed reserve
\[
0<\delta<\frac12.
\]
For an output block `J`, put
\[
X=e^{J+O_K(1)},
\qquad
V=\lceil X^{1/K}\rceil.
\]
Let `mathcal E_(J,K)` be the complete reflected vertical energy obtained from
`L-9516`, with the continuous pole model, every transition row, and every
endpoint term retained.

The proposed theorem is that there exists an absolute constant `C_*`, independent
of `J` and `K`, such that for every fixed sufficiently large `K`,
\[
\boxed{
\begin{aligned}
\mathcal E_{J,K}
\le{}&
\exp\left\{
 \left(\frac{C_*}{K}+o_K(1)\right)J
\right\}\\
&\times
\left[
1+\max_h\max_{u\le(1-\delta)J+O_K(1)}
 \mathcal E_{h,K}(u)
\right].
\end{aligned}}
\tag{L-9517.1}
\]

Equivalently, the terminal Selberg certificate of `L-23204` may be chosen with
\[
\boxed{
\eta_K\le\frac{C_*}{K}.
}
\tag{L-9517.2}
\]

The claim is source-specific. It is not a uniform estimate for arbitrary Farey
vectors, arbitrary Möbius coefficients, or arbitrary compact kernels.

## 2. Exact reflected packet

Use `L-9516` with the conjugate twists
\[
\chi_t(n)=n^{-it},
\qquad
\overline{\chi_t}(n)=n^{it}.
\]
The positive energy is the integral of the exact coefficient packet
\[
2\,\Lambda\chi_t*\Lambda\overline{\chi_t}
\]
against the nonnegative weight
\[
|\widehat H_K(\alpha+it)|^2.
\]
Its forcing is the difference of the three source-bound Selberg terms in
(L-9516.2). The inverse of the product zeta function has coefficients
\[
\sum_{de=n}\mu(d)\mu(e)(d/e)^{-it}.
\]

Apply the exact finite Möbius resolvent `L-23201` independently in the `d` and
`e` variables. Through endpoint `X`, this gives a finite double geometric
packet
\[
\sum_{0\le r,s<K}
(\mu_V*r_V^{*r})\boxtimes
(\mu_V*r_V^{*s})
\tag{L-9517.3}
\]
with no analytic remainder. All rows having the same destination are recombined
with their original Möbius and residual signs before any norm or total
variation.

## 3. Fixed-reserve first crossing

Order the residual variables in each tensor row. Apply the first-crossing
partition of `L-15157` separately in the two factor coordinates, then jointly to
the ratio kernel.

Every row receives exactly one of the following labels.

1. **Balanced.** Both product coordinates expose factors at most
   `exp((1-delta)J+O_K(1))`. The row is a lower-scale reflected energy.
2. **Reduced.** At the original scale, expanding one residual coefficient lowers
   the total residual-word complexity. These rows form a finite acyclic graph.
3. **Terminal.** Exactly one long factor remains after every possible strict
   scale and complexity reduction.

The finite induction of `L-23203` removes the first two classes. It leaves only
the complete signed sum of the terminal rows; individual terminal rows are not
estimated separately.

## 4. Null-quotient boundary recombination

The load-bearing observation is that `H_K` is still piecewise linear, regardless
of `K`, while its transform has order `K+1` zeros at both boundary models. Thus
its block autocorrelation is piecewise cubic, but it annihilates in either leg
all densities
\[
u^rdu,\qquad u^re^{u/2}du,\qquad 0\le r\le K.
\tag{L-9517.4}
\]

For one terminal word, freeze all short factors and Abel-sum the long factor
against the **combined** terminal coefficient. On each polyhedral cell the
interior contribution is a polynomial-exponential density of degree at most
`K`; it vanishes in the quotient (L-9517.4). Repeating this in both reflected
coordinates leaves only:

- the Hermitian diagonal already present on the positive left side of
  `L-9516`;
- cutoff faces on which one short product equals an endpoint;
- first-crossing faces;
- the declared strict lower-scale rows.

No bulk total variation remains.

The key finite boundary ledger is
\[
\boxed{
\#\{\text{free endpoint divisor coordinates in one recombined terminal face}\}
\le C_*.
}
\tag{L-9517.5}
\]
The point is that the spline degree is fixed and every additional residual word
is removed by a null moment or a complexity descent; it does not create a new
free endpoint coordinate. The combinatorial number of faces may depend on `K`,
but contributes only a `K`-dependent constant, not an exponent in `J`.

Since every free endpoint coordinate is at most
\[
V^{1+o(1)}
=\exp\{(1/K+o_K(1))J\},
\]
the complete endpoint ledger costs
\[
\exp\left\{
 \left(\frac{C_*}{K}+o_K(1)\right)J
\right\}.
\tag{L-9517.6}
\]
Divisor multiplicities and fixed-order binomial coefficients are
`exp(o_K(J))`.

## 5. Reflected Selberg absorption

The surviving Hermitian diagonal is not bounded by absolute values. By
`L-9516`, it is the left side of the conjugate-product Selberg identity and is
nonnegative. Move this term to the energy side.

The remaining forcing faces are paired with the positive exponential adjoints
of `L-23001`. Their polynomial principal parts lie in the null quotient
(L-9517.4); the nonprincipal parts are precisely the endpoint and lower-scale
rows already listed. This gives, for every terminal type,
\[
E_\tau(J)
\le
\exp\left\{
 \left(\frac{C_*}{K}+o_K(1)\right)J
\right\}
\left[
1+\max_{u\le(1-\delta)J+O_K(1)}M_K(u)
\right].
\tag{L-9517.7}
\]
Taking the maximum over the finite terminal dictionary proves (L-9517.1).

## 6. Mandatory first-cell mutation

The proposal must retain the coherent first Farey cell. Under the `q_0=2`
fixed-logarithm slice of the exact Heath--Brown/Möbius decoder, the terminal
recombination becomes the high-order fixed-ratio difference
\[
G_K(D)=\Delta_{2/3}^{K}M(D).
\]
Equation (L-9517.7) therefore yields
\[
G_K(D)
=O_{K,\varepsilon}
\left(D^{1/2+C_*/(2K)+\varepsilon}\right).
\tag{L-9517.8}
\]
The exact inversion of `L-23202` gives the same exponent for `M(D)`. Given any
`epsilon>0`, choose fixed `K>C_*/epsilon`; then
\[
M(D)=O_\varepsilon(D^{1/2+\varepsilon}).
\]
Thus the proposed boundary recombination does not delete the RH-bearing scalar;
it proves its required estimate.

## 7. Reviewer hinge

The full proposal stands or falls on (L-9517.5): after exact signed
recombination, do all same-scale terminal faces really have only an absolute
number of free endpoint divisor coordinates?

A valid review must construct the complete terminal dictionary and check:

1. every interior polynomial-exponential row lies in the declared null space;
2. every same-scale nonnull row lowers residual-word complexity;
3. no transition surface produces a number of free endpoint coordinates growing
   with `K`;
4. all reflected cross terms are consumed by `L-9516`, not bounded entrywise;
5. the `q_0=2` first-cell mutation reproduces (L-9517.8) with the stated exponent.

If any terminal face has `Omega(K)` free endpoint coordinates, then
`C_*/K` need not vanish and the proof fails. This is the sharp adversarial test.

## 8. Status boundary

The reflected identity and the finite resolvent algebra are exact. The
null-quotient boundary recombination in Sections 4--6 is a new proposed closing
argument and has not yet been independently enumerated for the complete packet
dictionary.

Accordingly this file is a full-proof hinge submitted for adversarial review,
not an accepted theorem or a claim that RH has already been proved.
