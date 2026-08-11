# R-91003 — Subcritical safe-disc tests are high-carrier blind

Claim ID: `R-91003`  
Status: **PROPOSED COMPLETE ASYMPTOTIC FIREWALL — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: `L-91008`, `T-91003`, the exact off-line pole formula of `T-91001/T-91002`  
RH status: **unproved**

## 1. One off-line pair in the unit-disc generator

Suppose

\[
 \rho=\frac12+y+i\gamma,
 \qquad 0<y<\frac12,
\]

is an off-line zero of multiplicity `m`, and evaluate at its matching centre `x=gamma`.

Put

\[
 w_y=1-y^2\in\left(\frac34,1\right).
\]

Its exact contribution to the unit-disc generator is

\[
 \boxed{
 \mathcal A_{\gamma}^{\rm pair}(w)
 =-\frac{4my^2}
 {w_y^2(w_y-w)}.
 }
\tag{R-91003.1}
\]

Therefore its coefficient contribution is

\[
 \boxed{
 a_k^{\rm pair}(\gamma)
 =-4my^2w_y^{-k-3}.
 }
\tag{R-91003.2}
\]

The pair is invisible to every fixed disc `|w|<=R<3/4`, but it produces exponential coefficient growth at rate `w_y^-1`.

## 2. Competition with the gamma/Catalan background

`L-91008` proves that the universal positive high-carrier background is

\[
 \ell_\gamma c_k,
 \qquad
 c_k\sim\frac1{2\sqrt\pi}k^{-3/2},
 \qquad
 \ell_\gamma=\log(2+|\gamma|).
\tag{R-91003.3}
\]

The target pair can dominate this background only once

\[
 4my^2w_y^{-k-3}
 \gtrsim \ell_\gamma k^{-3/2}.
\tag{R-91003.4}
\]

Equivalently,

\[
 \boxed{
 k\log\frac1{w_y}
 \ge
 \log\ell_\gamma+O(\log k+|\log y|+1).
 }
\tag{R-91003.5}
\]

Thus the natural detecting order for a depth-`y` pair is

\[
 \boxed{
 k_{\rm det}(\gamma,y)
 \sim
 \frac{\log\ell_\gamma}
 {\log(1/(1-y^2))}.
 }
\tag{R-91003.6}
\]

## 3. The universal deepest-pair threshold

As `y` tends to the edge `1/2`,

\[
 w_y\downarrow\frac34,
 \qquad
 \log\frac1{w_y}\uparrow\log\frac43.
\]

Therefore the earliest possible universal detecting order is

\[
 \boxed{
 k_{\rm edge}(\gamma)
 \sim
 \frac{\log\ell_\gamma}{\log(4/3)}
 =3.4760594967\ldots\,\log\log|\gamma|.
 }
\tag{R-91003.7}
\]

`T-91003` proves positivity through every fixed fraction below exactly this scale. The agreement is not accidental: the Cauchy contour approaches the maximal direct-Euler radius `3/4`, and a hypothetical deepest pair has its pole at that same radius.

## 4. Fixed safe-disc Pick packets cannot close RH

For every fixed `R<3/4`, `L-91008` gives

\[
 \frac{\mathcal A_x}{\ell_x}\longrightarrow\Phi
\]

locally uniformly on `|w|<R`, where `Phi` is a strict Stieltjes/Pick function. Consequently every fixed finite Pick, Loewner, Hausdorff, Hankel, or Bernstein packet supported in that disc is eventually strictly positive at high carrier whether or not RH is true.

The same is true for any growing coefficient order satisfying

\[
 k\le
 \left(
 \frac1{\log(4/3)}-\varepsilon
 \right)
 \log\ell_x.
\]

Thus the following strategy is closed:

```text
stay a fixed distance inside |w|=3/4;
prove any fixed finite Pick/Hankel packet positive;
or let the order grow strictly below the edge scale;
conclude RH.
```

All those conclusions are already forced by the universal gamma background.

## 5. What a conclusion-producing argument must do

At least one of the following is necessary:

1. continue the Stieltjes/Pick sign into the annulus `3/4<|w|<1`;
2. control coefficient/Hausdorff order at and beyond
   `log(ell_x)/log(4/3)` with the second-order logarithmic losses included;
3. subtract or neutralize the Catalan gamma background while preserving a positive prime-side structure;
4. use carrier-specific information that rules out the edge pole directly.

The classical zero-free region in `L-91007` proves a small annular holomorphic continuation, but holomorphy alone does not provide any of these sign mechanisms.

## 6. Exact boundary

```text
off-line pair coefficient                       EXACT
pair/background balance                         PROPOSED COMPLETE
universal edge order 1/log(4/3)                 EXACT ASYMPTOTIC
fixed safe-disc Pick/Hankel tests                HIGH-CARRIER BLIND
strictly subcritical growing order               HIGH-CARRIER BLIND
annular Pick sign / critical growing order       OPEN / RH-EQUIVALENT
Riemann Hypothesis                               UNPROVED
```