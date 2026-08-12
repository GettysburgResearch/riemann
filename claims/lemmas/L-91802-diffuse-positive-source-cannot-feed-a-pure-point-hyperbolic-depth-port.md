# L-91802 — A diffuse positive source cannot feed a pure-point hyperbolic depth port

Claim ID: `L-91802`  
Status: **PROVED EXACT OPERATOR-VALUED LEBESGUE-DECOMPOSITION THEOREM**  
Created: 2026-08-13  
Depends on: none beyond elementary positive operator-valued measure theory  
RH status: **unproved**

## 1. Positive kernel-valued measures

Let `X` be a measurable space and let

\[
 \mathsf A,\mathsf C,\mathsf S,\mathsf H,\mathsf E
\]

be countably additive positive operator-valued measures on `X`, acting on a
common finite packet coefficient space.  Equivalently, every scalar
polarization

\[
 I\longmapsto
 \langle \mathsf A(I)v,v\rangle
\]

is a finite positive measure, and similarly for the other letters.

Assume the interval-local source identity

\[
\boxed{
 \mathsf A(I)
 =\mathsf C(I)+\mathsf S(I)+\mathsf H(I)+\mathsf E(I)
}
\tag{L-91802.1}
\]

for every measurable `I subset X`.

## 2. Absolute continuity passes to every positive output

From positivity and (L-91802.1),

\[
 0\preceq\mathsf H(I)\preceq\mathsf A(I)
\]

for every `I`.  Therefore

\[
\boxed{
 \mathsf H\ll\mathsf A.
}
\tag{L-91802.2}
\]

Indeed, if `A(I)=0`, then for every vector `v`,

\[
 0\le\langle\mathsf H(I)v,v\rangle
 \le\langle\mathsf A(I)v,v\rangle=0,
\]

so `H(I)=0` by polarization.

Consequently, if

\[
 \mathsf A\ll m
\]

for a non-atomic scalar measure `m`, then

\[
\boxed{
 \mathsf H\ll m.
}
\tag{L-91802.3}
\]

## 3. Diffuse-versus-pure-point exclusion

Suppose now that `m` is non-atomic and `H` is pure point:

\[
 \mathsf H
 =\sum_{x\in\mathcal P}
  H_x\,\delta_x,
 \qquad H_x\succeq0.
\]

For every `x in P`,

\[
 \mathsf A(\{x\})=0
\]

and hence

\[
 0\preceq H_x
 =\mathsf H(\{x\})
 \preceq\mathsf A(\{x\})=0.
\]

Thus

\[
\boxed{
 H_x=0\quad(x\in\mathcal P),
 \qquad
 \mathsf H=0.
}
\tag{L-91802.4}
\]

This is the operator-valued form of uniqueness in the Lebesgue decomposition
of a positive measure.

## 4. Approximate local form

Let `x0` be a proposed atom and let `I_h downarrow {x0}` be shrinking
neighbourhoods.  Suppose

\[
 0\preceq H_{x_0}
 \preceq\mathsf A(I_h)+R_h,
\]

where `R_h` is Hermitian and

\[
 \|\mathsf A(I_h)\|\longrightarrow0,
 \qquad
 \|R_h\|\longrightarrow0.
\]

Then

\[
\boxed{H_{x_0}=0.}
\tag{L-91802.5}
\]

Indeed

\[
 \|H_{x_0}\|
 \le\|\mathsf A(I_h)\|+\|R_h\|
\]

for every `h`.

If `A` has a locally bounded density, `||A(I_h)||=O(|I_h|)`.  Hence any
interval-local defect `o(1)` is enough to remove the atom.  No carrier-height
rate such as `o(Y^-2)` is required.

## 5. Kernel formulation

The theorem applies packetwise to positive kernels.  If

\[
 A_I(x,y)=C_I(x,y)+S_I(x,y)+H_I(x,y)+E_I(x,y)
\]

and every finite matrix of every term is positive, then the same conclusion
holds after passing through the minimal Kolmogorov decompositions.

No global square root of the full target kernel is used.  The conclusion is
local in the radial Borel algebra.

## 6. Exact boundary

```text
positive interval-local identity              ASSUMPTION
absolute continuity inherited by outputs      EXACT
pure-point output under diffuse source         ZERO EXACTLY
approximate shrinking-interval version         EXACT
application to zeta radial source lock         OPEN / RH-BEARING
Riemann Hypothesis                             UNPROVED
```
