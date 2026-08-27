# L-105604 — The differential microscope is the scale derivative of normalized shifted-zero flow

Claim ID: `L-105604`  
Status: **PROVED EXACT INFINITESIMAL ORIENTED-PHASE IDENTITY**  
Created: 2026-08-24  
Depends on: `L-105340`, `L-105416`, `L-105444`, `L-105602`  
RH status: **not assumed**

## 1. Scale-normalized shifted companion

Let `F` be a real entire function and put

\[
m={F\over F'}.
\]

For `h>0` and real deformation parameter `alpha`, define

\[
\boxed{
E_{\alpha,h}(z)
=F'(z)-{\alpha\over h}F(z).
}
\tag{L-105604.1}
\]

On the real axis define the height-`h` all-pass boundary value

\[
\boxed{
\Theta_{\alpha,h}(x)
={E_{\alpha,h}(x+ih)
 \over
 E_{\alpha,h}(x-ih)}.
}
\tag{L-105604.2}
\]

For real `alpha`, reality of `F` gives `|Theta_(alpha,h)(x)|=1` whenever the
denominator is nonzero.

The companion depends on `h` through `alpha/h`. This dependence is deliberate
and load bearing below. It also means that finite nonzero-`alpha` quotients at
two heights are not shell maps of one common entire function.

## 2. Exact phase velocity

Differentiate at `alpha=0`. Since

\[
\left.\partial_\alpha
\log E_{\alpha,h}(z)
\right|_0
=-{1\over h}m(z),
\]

and `m(x-ih)=overline(m(x+ih))`, one obtains

\[
\boxed{
\mathcal V_F(x,h)
:=
\left.\partial_\alpha
\arg\Theta_{\alpha,h}(x)
\right|_0
=-{2\over h}\operatorname{Im}m(x+ih).
}
\tag{L-105604.3}
\]

The factor `1/h` in (L-105604.1) makes the phase velocity dimensionless and
turns an affine Herglotz carrier into an `h`-independent phase velocity.

## 3. Differential microscope identity

The base-zero differential microscope is

\[
\mathcal C_F(x,h)
={1\over2}
\left[
 h\Re m'(x+ih)-\Im m(x+ih)
\right].
\]

Cauchy--Riemann gives

\[
\partial_h\Im m(x+ih)=\Re m'(x+ih).
\]

Differentiating (L-105604.3),

\[
\boxed{
\partial_h\mathcal V_F(x,h)
=-{4\over h^2}\mathcal C_F(x,h).
}
\tag{L-105604.4}
\]

Equivalently,

\[
\boxed{
\mathcal C_F(x,h)
=-{h^2\over4}
\partial_h
\left.
\partial_\alpha
\arg\Theta_{\alpha,h}(x)
\right|_0.
}
\tag{L-105604.5}
\]

Thus the differential microscope is literally the scale derivative of one
normalized infinitesimal shifted-zero phase flow.

## 4. Integrated scale ledger

For `0<h_1<h_2` in a pole-free vertical segment,

\[
\boxed{
\mathcal V_F(x,h_2)-\mathcal V_F(x,h_1)
=-4\int_{h_1}^{h_2}
{\mathcal C_F(x,h)\over h^2}\,dh.
}
\tag{L-105604.6}
\]

Therefore

\[
\boxed{
\mathcal C_F(x,h)\le0\text{ for every }h
\quad\Longleftrightarrow\quad
\mathcal V_F(x,h)
\text{ is nondecreasing in }h.
}
\tag{L-105604.7}
\]

This is the oriented-zero-flow version of the monotonicity of
`Im m(x+ih)/h` in `L-105444`.

## 5. Infinitesimal relation to shell winding

Let

\[
\mathcal A_{\alpha;h_1,h_2}(x)
={\Theta_{\alpha,h_2}(x)
 \over
 \Theta_{\alpha,h_1}(x)}.
\]

Then

\[
\boxed{
\left.\partial_\alpha
\arg\mathcal A_{\alpha;h_1,h_2}(x)
\right|_0
=-4\int_{h_1}^{h_2}
{\mathcal C_F(x,h)\over h^2}\,dh.
}
\tag{L-105604.8}
\]

At `alpha=0`, the companion is the common entire function `F'`, independent of
`h`, so

\[
\mathcal A_{0;h_1,h_2}
={F'(x+ih_2)F'(x-ih_1)
 \over
 F'(x-ih_2)F'(x+ih_1)}
\]

is exactly the height-shell all-pass map of `L-105602` for `F'`.

For `alpha!=0`, however, `E_(alpha,h)` varies with height. Therefore
(L-105604.8) is an **infinitesimal tangent identity at alpha zero**, not a
claim that the finite deformed quotient counts one shell. This firewall is
essential.

The legitimate conclusion is that pointwise phase variance and shell winding
meet at the first variation of the same circle-valued shell construction.

## 6. Zero-motion calibration

Let `c` be a simple real zero of `F'`, with residue

\[
\rho_c={F(c)\over F''(c)}.
\]

The zero branch of `E_(alpha,h)` through `c` satisfies

\[
\boxed{
{dc_\alpha\over d\alpha}\bigg|_0
={\rho_c\over h}.
}
\tag{L-105604.9}
\]

Thus the same normalization which produces the dimensionless phase velocity
also prices one critical residue in units of the physical height. The
fine-scale limit `h C_F(c,h)->rho_c` is consistent with this zero motion.

## 7. Xi implication

For `F=Xi`, proving

\[
\partial_h\mathcal V_F(x,h)\ge0
\qquad(x\in\mathbb R,\ h>0)
\]

is exactly `DM105444(0,0)` and hence RH. The existing oriented-ratio and
one-sided-Hardy programmes estimate the `alpha` phase velocity. The remaining
problem is to retain its monotonicity in physical height after the complete
source/error transfer.

## 8. Scope

No monotonicity estimate is proved here. The identity does not replace the
`H^(1/2)` shell gate: a phase velocity can be nonmonotone through narrow slips
whose topological cost is visible only after integrating in the spatial
variable. The finite deformed family at `alpha!=0` is not assigned a shell
count. RH remains unproved.
