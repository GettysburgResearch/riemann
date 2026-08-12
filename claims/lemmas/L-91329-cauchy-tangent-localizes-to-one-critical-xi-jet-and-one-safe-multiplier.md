# L-91329 — The Cauchy tangent localizes to one critical xi jet and one common safe logarithmic-derivative multiplier

Claim ID: `L-91329`  
Status: **PROVED EXACT CRITICAL-JET LOCALIZATION OF THE PHYSICAL MODEL-SPACE TANGENT**  
Created: 2026-08-13  
Depends on: `L-91327`, `L-91328`, the functional equation and conjugation symmetry of `xi`  
Sharpens: the Toeplitz-resolvent block in `L-91327`  
RH status: **unproved**

## 1. One analytic safe logarithmic derivative

Fix `a>1/2` and put

\[
 \sigma=\frac12+a>1.
 \tag{L-91329.1}
\]

Define, on the upper half-plane,

\[
 \boxed{
 D_a(z)
 =a\frac{\xi'}\xi(\sigma-iz).
 }
 \tag{L-91329.2}
\]

If `z in C_+`, then

\[
 \operatorname{Re}(\sigma-iz)
 =\sigma+\operatorname{Im}z>1.
\]

Thus `D_a` is analytic throughout `C_+`; its zeta logarithmic derivative is
represented there by an absolutely convergent Dirichlet series. On the real
boundary,

\[
 \ell_a(t)
 =a\partial_a\log\Theta_a(t)
 =\overline{D_a(t)}-D_a(t).
 \tag{L-91329.3}
\]

Although `D_a(t)=O(log(2+|t|))`, equation (L-91328.3) shows that the difference
in (L-91329.3) is uniformly bounded.

## 2. The Toeplitz resolvent has an exact divided-difference formula

Let

\[
 T_{\ell_a}f=P_+(\ell_af).
\]

For the ordinary upper-Hardy kernel

\[
 \kappa_w(z)=\frac1{z-\overline w},
 \qquad w\in\mathbb C_+,
\]

the analytic-multiplier adjoint identity gives

\[
 P_+(\overline{D_a}\,\kappa_w)
 =\overline{D_a(w)}\kappa_w.
 \tag{L-91329.4}
\]

Therefore

\[
 \boxed{
 T_{\ell_a}\kappa_w
 =\left(\overline{D_a(w)}-D_a(z)\right)\kappa_w(z).
 }
 \tag{L-91329.5}
\]

Differentiating in `bar w` gives

\[
 \boxed{
 T_{\ell_a}\kappa_w^{[1]}
 =\overline{D_a'(w)}\kappa_w
  +\left(\overline{D_a(w)}-D_a(z)\right)
   \kappa_w^{[1]}.
 }
 \tag{L-91329.6}
\]

The Riesz projection in the Toeplitz columns of `L-91327` has disappeared.
Only multiplication by the single safe analytic function `D_a` remains.

The formulas are valid on the kernel-jet core because
`D_a(t)\kappa_w(t)` and `D_a(t)\kappa_w^[1](t)` lie in `L2`; this follows from
the logarithmic growth of `D_a`.

## 3. Exact cancellation inside the model-space tangent

Write

\[
 \Theta_a(z)
 =\frac{\xi(\sigma+iz)}{\xi(\sigma-iz)}.
 \tag{L-91329.7}
\]

For `w in C_+`, define the finite anti-holomorphic coefficients

\[
 \boxed{
 B_a(w)
 =\overline{\Theta_a(w)}
 =\frac{\xi(\sigma-i\overline w)}
        {\xi(\sigma+i\overline w)},
 }
 \tag{L-91329.8}
\]

\[
 \boxed{
 A_a(w)
 =a\frac{\xi'(\sigma-i\overline w)}
        {\xi(\sigma+i\overline w)}.
 }
 \tag{L-91329.9}
\]

The denominator in both formulas lies in `Re(s)>1`, so these coefficients are
finite even when the numerator of `B_a` vanishes. Where the reflected
logarithmic derivative is finite,

\[
 A_a(w)=B_a(w)D_a(\overline w),
\]

and (L-91329.9) is its canonical entire continuation through reflected zeros.

Let

\[
 \mathcal A_a=M_{a\partial_a\Theta_a}^*P_{K_{\Theta_a}}.
\]

Combining `L-91327.23` with (L-91329.5), and using

\[
 a\partial_a\Theta_a
 =\Theta_a(D_a^\#-D_a),
 \qquad
 D_a^\#(z)=\overline{D_a(\overline z)},
\]

gives the exact cancellation

\[
 \boxed{
 \mathcal A_ak_w^{\Theta_a}(z)
 =\left(A_a(w)-B_a(w)D_a(z)\right)\kappa_w(z).
 }
 \tag{L-91329.10}
\]

No reciprocal xi value and no singular reflected logarithmic derivative
appears separately.

For the first confluent jet, put `lambda=bar w` and define

\[
 B_a^\flat(\lambda)
 =\frac{\xi(\sigma-i\lambda)}
        {\xi(\sigma+i\lambda)},
 \qquad
 A_a^\flat(\lambda)
 =a\frac{\xi'(\sigma-i\lambda)}
        {\xi(\sigma+i\lambda)}.
 \tag{L-91329.11}
\]

Then

\[
\boxed{
\begin{aligned}
 \mathcal A_ak_w^{\Theta_a,[1]}(z)
 ={}&\left(
  (A_a^\flat)'(\overline w)
  -(B_a^\flat)'(\overline w)D_a(z)
 \right)\kappa_w(z)\\
 &+\left(
  A_a(w)-B_a(w)D_a(z)
 \right)\kappa_w^{[1]}(z).
\end{aligned}}
 \tag{L-91329.12}
\]

Thus every physical tangent column is a linear combination of

```text
kappa_w, kappa_w^[1],
D_a kappa_w, D_a kappa_w^[1],
```

with finite scalar coefficients.

## 4. Reflection moves all but one physical node to the safe half-plane

For the Cauchy nodes

\[
 w_{x,r}=x+ira,
 \qquad r\in\{1,2,4\},
 \tag{L-91329.13}
\]

the functional equation gives

\[
 \boxed{
 B_a(w_{x,r})
 =\frac{
  \xi(\frac12+(r-1)a+ix)
 }{
  \xi(\frac12+(r+1)a+ix)
 }.
 }
 \tag{L-91329.14}
\]

Differentiating the functional equation gives

\[
 \boxed{
 A_a(w_{x,r})
 =-a\frac{
  \xi'(\frac12+(r-1)a+ix)
 }{
  \xi(\frac12+(r+1)a+ix)
 }.
 }
 \tag{L-91329.15}
\]

The confluent coefficients are obtained by differentiating the two safe-
denominator quotients. Explicitly, with

\[
 u_r=\frac12+(r-1)a+ix,
 \qquad
 v_r=\frac12+(r+1)a+ix,
\]

one has

\[
 \boxed{
 (B_a^\flat)'(x-ira)
 =i\frac{\xi'(u_r)\xi(v_r)-\xi(u_r)\xi'(v_r)}
         {\xi(v_r)^2},
 }
 \tag{L-91329.16}
\]

and

\[
 \boxed{
 (A_a^\flat)'(x-ira)
 =-ai\frac{\xi''(u_r)\xi(v_r)-\xi'(u_r)\xi'(v_r)}
          {\xi(v_r)^2}.
 }
 \tag{L-91329.17}
\]

Now:

```text
r=1: u_1=1/2+ix,       v_1=1/2+2a+ix;
r=2: u_2=1/2+a+ix,     v_2=1/2+3a+ix;
r=4: u_4=1/2+3a+ix,    v_4=1/2+5a+ix.
```

Because `a>1/2`, every `u_r,v_r` for `r=2,4` lies in `Re(s)>1`. The only
non-safe scalar data in the entire six-coordinate physical Cauchy block are
therefore

\[
 \boxed{
 \xi(\tfrac12+ix),
 \quad
 \xi'(\tfrac12+ix),
 \quad
 \xi''(\tfrac12+ix),
 }
 \tag{L-91329.18}
\]

coming from the simple/double pole block at height `a`. Their denominators are
all on the very safe line `Re(s)=1/2+2a>3/2`.

This is a localization statement, not a sign theorem. Critical-line values of
an entire function still encode the full zero set.

## 5. Finite output matrix with one critical confluent block

For every finite carrier packet, substitute (L-91329.10)--(L-91329.17) into
the finite matrix `G_a^out(W)` of `L-91327.26`. Every entry is then an ordinary
`H2` inner product among the common safe multiplier columns

```text
kappa_w, kappa_w^[1],
D_a kappa_w, D_a kappa_w^[1]
```

with:

```text
safe xi/xi' data at r=2,4;
one critical xi/xi'/xi'' block at r=1;
exact triangular delay coefficients;
exact Cauchy partial-fraction coefficients.
```

Thus the RH-bearing source domination can be presented as one finite confluent
block comparison in which the only critical-line scalar channel is explicit.
No unsafe logarithmic derivative, principal value, or reciprocal-zero
singularity is hidden in the formula.

The reflected Hardy orientation gives the conjugate critical block. The
canonical bridge appends one explicit rational row and column.

## 6. Exact boundary

```text
safe analytic multiplier D_a on C_+                         EXACT
Toeplitz kernel columns as divided differences              EXACT
cancellation of reflected logarithmic-derivative poles      EXACT
physical simple/double tangent columns                      EXACT
r=2 and r=4 scalar data entirely in Re(s)>1                  EXACT
only r=1 uses critical xi, xi', xi''                         EXACT
finite delayed output block with one critical confluent row EXACT
completed source domination of that block                   OPEN / RH-BEARING
mixed orientation and bridge arithmetic rows                OPEN
Riemann Hypothesis                                           UNPROVED
```
