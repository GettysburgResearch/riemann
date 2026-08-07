# T-23002 — The first critical Farey cell is already RH-equivalent

Claim ID: `T-23002`  
Title: Square-root control of one fixed-ratio Mertens increment, equivalently the first Farey cluster, is equivalent to the Riemann Hypothesis  
Status: **PROPOSED REDUCTION — ESTIMATE OPEN**  
Authoring agent: `gpt56-pro-09-o`  
Created: 2026-08-07  
Dependencies: `L-23003`; the classical Littlewood/Mertens criterion  
Scope: full Riemann Hypothesis

## 1. The scalar increment

Define

\[
 \Delta_{2/3}M(D)
 =M(D)-M(2D/3),
\]

where the second argument is rounded down.

Then the following are equivalent:

1. RH;
2. for every `epsilon>0`,
   \[
   \boxed{
   \Delta_{2/3}M(D)
   =O_\varepsilon(D^{1/2+\varepsilon});}
   \tag{T-23002.1}
   \]
3. for every `epsilon>0`, the first reduced-Farey cell of `L-23003` obeys
   \[
   \boxed{
   B_{D,1}=O_\varepsilon(D^{1/2+\varepsilon}).}
   \tag{T-23002.2}
   \]

## 2. RH implies the increment bound

The classical Mertens formulation of RH gives

\[
 M(x)=O_\varepsilon(x^{1/2+\varepsilon})
\]

for every `epsilon>0`.  Subtracting the two values at `D` and `2D/3` proves
(T-23002.1).  Equation (T-23002.2) then follows from the exact identity

\[
 B_{D,1}
 =\left(\frac{i}{2\pi}+\frac1{2\pi^2}\right)
 \Delta_{2/3}M(D).
\]

## 3. The increment bound implies RH

Fix `D` and choose `J` so that `(2/3)^J D` is bounded.  The geometric
resolution

\[
 M(D)
 =M((2/3)^JD)
 +\sum_{j=0}^{J-1}
 \Delta_{2/3}M((2/3)^jD)
\]

and (T-23002.1) give

\[
 |M(D)|
 \ll_\varepsilon
 1+D^{1/2+\varepsilon}
 \sum_{j\ge0}(2/3)^{j(1/2+\varepsilon)}
 \ll_\varepsilon D^{1/2+\varepsilon}.
\]

The Mertens criterion gives RH.

## 4. Implication for the repository-wide proof candidate

`L-23002` was formulated as a signed near-resonance transport estimate.  The
present theorem shows that its very first coherent cell already contains an
RH-equivalent scalar.  Therefore a purported completion must do one of two
things:

1. prove (T-23002.1) directly; or
2. prove an exact endpoint/adjacent-cell identity whose net effect implies
   (T-23002.1).

A generic local-to-Bohr operator estimate cannot accomplish this: PR #231 gives
an explicit `sqrt(D)` lower bound for the corresponding cluster-operator row.
The signs and divisor coupling of the actual Möbius vector are load bearing.

## 5. Status boundary

This theorem is an equivalence and a review gate, not a proof of the estimate.
It sharpens the remaining task but does not establish RH.
