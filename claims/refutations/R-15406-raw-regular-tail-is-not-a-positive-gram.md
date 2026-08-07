# R-15406 — The raw regular tail is not a positive Gram

Claim ID: `R-15406`  
Title: The proposed identity `A_reg ghat ↔ positive Volterra-tail Gram` fails before one Green integration  
Status: `PROPOSED`  
Authoring agent: `gpt56-05-l`  
Created: 2026-08-01  
Dependencies: `L-15429`; elementary positive-kernel Cauchy--Schwarz  
Scope: correction of the requested regular metric identity  
Related counterexample candidates: none

## Boundary expansion

Use the notation of `L-15429`. The regular arithmetic factor has the finite
positive boundary value

\[
 \boxed{
 A_\omega^{\rm reg}(0)
 =c_\omega\left[
 \gamma-{\zeta'(1+2\omega)\over\zeta(1+2\omega)}
 \right]>0.}
 \tag{R-15406.1}
\]

Indeed `gamma>0` and `zeta'(s)<0` for real `s>1`.

Since

\[
 \widehat g_\omega(u_0+q)
 ={B_\omega(0)\over2\omega}q+O(q^2),
 \tag{R-15406.2}
\]

we obtain

\[
 \boxed{
 T_\omega^{\rm raw}(q)
 =d_\omega q+O(q^2),
 \qquad
 d_\omega={B_\omega(0)\over2\omega}
 A_\omega^{\rm reg}(0)>0.}
 \tag{R-15406.3}
\]

Thus the raw regular tail is nonzero and tends to zero through positive values
as `q downarrow 0`.

## Positive-kernel contradiction

Suppose the Hankel kernel

\[
 K_\omega(z,w)
 =T_\omega^{\rm raw}
  \left({z+\bar w\over2}\right)
 \tag{R-15406.4}
\]

were positive semidefinite on the right half-plane.

Fix a real `y>0` with `T_raw(y/2)>0`, and let `x downarrow 0`. Positivity of the
`2 x 2` Gram at the real points `x,y` would imply

\[
 \left|
 T_\omega^{\rm raw}\left({x+y\over2}\right)
 \right|^2
 \le
 T_\omega^{\rm raw}(x)
 T_\omega^{\rm raw}(y).
 \tag{R-15406.5}
\]

The right side tends to zero by (R-15406.3), while the left side tends to

\[
 \left|T_\omega^{\rm raw}(y/2)\right|^2>0,
 \]

a contradiction.

Therefore

\[
 \boxed{
 A_\omega^{\rm reg}(u)\widehat g_\omega(u)
 \text{ is not an ordinary positive Hankel Gram}.}
 \tag{R-15406.6}
\]

This is unconditional and does not depend on RH.

## Exact model showing the cross term

The rational model

\[
 A(q)={1\over q}+1,
 \qquad
 \widehat g(q)={q\over q+1}
 \tag{R-15406.7}
\]

has

\[
 E(q)={1\over q+1},
 \qquad
 T^{\rm raw}(q)={q\over q+1},
 \qquad
 E(q)+T^{\rm raw}(q)=1.
 \tag{R-15406.8}
\]

The raw-tail kernel is indefinite. For the real points

\[
 x={1\over100},
 \qquad y=1,
 \]

its determinant is

\[
 {1\over101}{1\over2}
 -\left({101\over301}\right)^2<0.
 \tag{R-15406.9}
\]

But the moving endpoint cross term

\[
 E(q)-E(0)=-{q\over q+1}
 \]

cancels it exactly, leaving the positive constant kernel one. This is the
finite control in `X-15413`.

## Corrected target

The first candidate for a positive regular tail is not `T_raw`, but the
one-Green kernel

\[
 G_\omega^{\rm reg}(q)
 ={T_\omega^{\rm raw}(q)\over q}
 =\widehat{m_\omega'}(q).
 \tag{R-15406.10}
\]

Its positivity is exactly the smoothed Jordan inequality in `L-15430`. The
moving endpoint Gram `E_omega`, including its boundary--tail cross block, must
be retained simultaneously.

## Consequence for the requested proof

The raw identity requested in Issue #180 cannot be proved because it is false.
Any successful physical metric theorem must:

1. apply the Mellin primitive trace before claiming positivity;
2. retain the complete moving endpoint Gram, not only the singular constant;
3. prove positivity of the one-Green regular density or an equivalent joint
   augmented Schur inequality.
