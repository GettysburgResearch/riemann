# L-20803 — A shifted-lattice source notch suppresses every fixed off-line mode after the full graph metric

Claim ID: `L-20803`  
Title: An explicit rational numerator lattice gives a source-normalized growing packet with a nonempty metric/support-averaging exponent wedge  
Status: `PROVED FINITE ALGEBRA AND METRIC-ADAPTED FIXED-MODE ASYMPTOTIC; SCHUR RESIDUAL STILL OPEN`  
Authoring agent: `gpt56-03-s`  
Created: 2026-08-01  
Dependencies: `D-0001`; `L-20801`; elementary partial fractions; fixed-shift gamma-ratio bounds  
Scope: the source direction in the square-support packet; fixed and slowly growing zero ordinates  
Related counterexample candidates: none

## 1. Explicit shifted numerator

Fix

\[
 \frac12<\vartheta<1
 \tag{L-20803.1}
\]

and an integer `r>=1`. Define

\[
 \boxed{
 R_{r,\vartheta}(x)
 =\prod_{j=1}^{r}
   {x-(j-\vartheta)^2\over x-j^2}.}
 \tag{L-20803.2}
\]

The zeros strictly interlace the positive poles. Hence the partial-fraction
residues are positive and there are unique positive numbers
`u_0,...,u_r` such that

\[
 \boxed{
 R_{r,\vartheta}(x)
 =u_0+2\sum_{n=1}^{r}u_n{x\over x-n^2},
 \qquad
 u_0+2\sum_{n=1}^{r}u_n=1.}
 \tag{L-20803.3}
\]

The last identity follows by taking `x` to infinity. Explicitly,

\[
 u_0=\left[
 {\Gamma(r+1-\vartheta)
  \over\Gamma(1-\vartheta)\Gamma(r+1)}
 \right]^2,
 \tag{L-20803.4}
\]

and, for `1<=n<=r`,

\[
\boxed{
\begin{aligned}
 u_n={\sin(\pi\vartheta)\over\pi}
 &{\Gamma(n+\vartheta)\over\Gamma(n+1-\vartheta)}\\
 &\times{\Gamma(r-n+1-\vartheta)\over\Gamma(r-n+1)}
 {\Gamma(r+n+1-\vartheta)\over\Gamma(r+n+1)}.
\end{aligned}}
 \tag{L-20803.5}
\]

For rational `vartheta`, the product/residue definition shows directly that
all `u_n` are rational, even though (L-20803.4)--(L-20803.5) use gamma notation.

Put the vector into the normalized even D-0001 basis:

\[
 v_{r,\vartheta,0}=u_0,
 \qquad
 v_{r,\vartheta,n}=\sqrt2u_n\quad(1\le n\le r),
 \tag{L-20803.6}
\]

and pad it by zeros in every larger packet. For the source functional

\[
 \ell_N(v)=v_0+\sqrt2\sum_{n=1}^{N}v_n,
 \tag{L-20803.7}
\]

one has the exact normalization

\[
 \boxed{\ell_N(v_{r,\vartheta})=1.}
 \tag{L-20803.8}
\]

The corresponding real trigonometric profile is

\[
 T_{r,\vartheta}(t)
 =u_0+2\sum_{n=1}^{r}u_n\cos(2\pi nt),
 \qquad T_{r,\vartheta}(0)=1.
 \tag{L-20803.9}
\]

## 2. Exact D-0001 response

Let

\[
 L=\log c,
 \qquad
 \mu={Lz\over2\pi}.
 \tag{L-20803.10}
\]

The finite D-0001/Guinand--Weil response of an even packet is

\[
 g_{v,L}(z)
 ={L\over\pi^2}\sin^2(\pi\mu)
 \left(\sum_{n=-r}^{r}{u_n\over n-\mu}\right)^2.
 \tag{L-20803.11}
\]

Evenness and (L-20803.3) give

\[
 \sum_{n=-r}^{r}{u_n\over n-\mu}
 =-{R_{r,\vartheta}(\mu^2)\over\mu}.
 \tag{L-20803.12}
\]

Moreover

\[
\begin{aligned}
R_{r,\vartheta}(\mu^2)
={}&{\Gamma(r+1-\vartheta-\mu)
       \Gamma(r+1-\vartheta+\mu)
       \Gamma(1-\mu)\Gamma(1+\mu)
     \over
     \Gamma(1-\vartheta-\mu)
       \Gamma(1-\vartheta+\mu)
       \Gamma(r+1-\mu)\Gamma(r+1+\mu)}.
\end{aligned}
 \tag{L-20803.13}
\]

Using

\[
 \Gamma(1-\mu)\Gamma(1+\mu)
 ={\pi\mu\over\sin\pi\mu},
 \tag{L-20803.14}
\]

the sine singularities cancel exactly. Thus

\[
\boxed{
 g_{r,\vartheta,L}(z)
 =L\left[
 {\Gamma(r+1-\vartheta-\mu)
  \Gamma(r+1-\vartheta+\mu)
  \over
  \Gamma(1-\vartheta-\mu)
  \Gamma(1-\vartheta+\mu)
  \Gamma(r+1-\mu)
  \Gamma(r+1+\mu)}
 \right]^2.}
 \tag{L-20803.15}
\]

This identity is entire in `z`; apparent gamma poles are removable. It is the
full factorial ledger of the growing notch, not a fixed-order Watson expansion.

## 3. Coefficient metric

The production coefficient metric of the padded vector is

\[
 \|v_{r,\vartheta}\|^2
 =u_0^2+2\sum_{n=1}^{r}u_n^2.
 \tag{L-20803.16}
\]

Fixed-shift gamma quotient bounds applied to (L-20803.5) give, uniformly for
`0<=k<r`,

\[
 u_{r-k}\le C_\vartheta
 r^{\vartheta-1}(k+1)^{-\vartheta}.
 \tag{L-20803.17}
\]

Since `2 vartheta>1`, the endpoint square sum is convergent. The remaining
indices are smaller, and therefore

\[
 \boxed{
 \|v_{r,\vartheta}\|^2
 \le C_\vartheta r^{2\vartheta-2}.}
 \tag{L-20803.18}
\]

At square level `(N,c)=(M,M^2)`, the source Riesz norm is

\[
 g_M=1+2M.
 \tag{L-20803.19}
\]

The affine trial satisfying `ell x=g_M` is `x_M=g_Mv`. Its exact triangular
source-graph metric cost is bounded by

\[
\boxed{
 \Lambda_M^{\rm notch}
 :=1+{\|x_M\|^2\over g_M}
 =1+g_M\|v\|^2
 \le C_\vartheta M r^{2\vartheta-2}.}
 \tag{L-20803.20}
\]

Thus the factorial numerator does not hide an exponential coefficient cost.
For `vartheta>1/2` the cost is the explicit endpoint power in
(L-20803.20).

## 4. Uniform fixed-mode bound

Let `z=a+ib` lie in a fixed compact subset of

\[
 |b|\le\frac12.
 \tag{L-20803.21}
\]

More generally, allow `|z|<=H_M` provided

\[
 H_M\log M=o(\sqrt r).
 \tag{L-20803.22}
\]

Uniform Stirling estimates in (L-20803.15) give

\[
\begin{aligned}
 |g_{r,\vartheta,2\log M}(z)|
 \le{}&C_\vartheta(\log M)
 r^{-4\vartheta}
 (1+|z|\log M)^{4\vartheta-2}\\
 &\times M^{2|b|}
 \exp\!\left(
  C_\vartheta{|z|^2(\log M)^2\over r}
 \right).
\end{aligned}
 \tag{L-20803.23}
\]

The exponential is `1+o(1)` under (L-20803.22). A zero of multiplicity `m`
contributes at most a fixed multiple of `m g_M |g|` to the normalized quadratic
on `x_M`. Combining this with (L-20803.20) yields

\[
\boxed{
\begin{aligned}
 \Lambda_M^{\rm notch}\,arepsilon_{M,z}
 \le{}&C_{\vartheta,z}
 (\log M)^{4\vartheta-1}
 M^{2+2|b|}
 r^{-2\vartheta-2}.
\end{aligned}}
 \tag{L-20803.24}
\]

Every factor in this estimate is source-bound: the source scaling `g_M`, the
coefficient metric, and the gamma/factorial normalization have all been
included.

## 5. Nonempty exponent wedge

Choose

\[
 r_M=\lfloor M^\beta\rfloor.
 \tag{L-20803.25}
\]

For a hypothetical fixed off-line zero, `|b|<1/2`. The worst closed-strip power
in (L-20803.24) is

\[
 M^{3-\beta(2\vartheta+2)}.
 \tag{L-20803.26}
\]

Hence

\[
\boxed{
 {3\over2(1+\vartheta)}<\beta<1
 \quad\Longrightarrow\quad
 \Lambda_M^{\rm notch}\varepsilon_{M,z}\longrightarrow0
}
 \tag{L-20803.27}
\]

for every fixed zero with `|Im z|<1/2`. The interval is nonempty precisely
because `vartheta>1/2`.

A concrete rational choice is

\[
 \boxed{
 \vartheta={3\over4},
 \qquad
 \beta={9\over10}.}
 \tag{L-20803.28}
\]

Then

\[
 \Lambda_M^{\rm notch}=O(M^{11/20}),
 \tag{L-20803.29}
\]

and, uniformly even at the formal boundary `|b|=1/2`,

\[
\boxed{
 \Lambda_M^{\rm notch}\varepsilon_{M,z}
 =O_z\!\left((\log M)^2M^{-3/20}\right).}
 \tag{L-20803.30}
\]

The support derivative scale of the finite response packet is `O(r_M)`.
Writing the multiplicative support as `c=M^2`,

\[
 r_M=M^{9/10}
 =o\!\left(\sqrt{c/\log c}\right).
 \tag{L-20803.31}
\]

Thus the same concrete choice lies strictly below the sub-square-root envelope
required by the Hilbert-valued support large sieve. The half-shift
`vartheta=1/2` is critical: its fixed-mode requirement forces `beta>=1` and
leaves no room for a sub-full-degree support packet. Moving the numerator roots
strictly inside each pole cell opens the wedge (L-20803.27).

## 6. A slowly growing fixed-frequency block

The zero-count bound `N(H)=O(H log H)` and (L-20803.23) imply that the complete
block `|z|<=H_M=M^kappa` is suppressed after the same graph metric whenever

\[
\boxed{
 3-\beta(2\vartheta+2)
 +\kappa(4\vartheta-1)<0,}
 \tag{L-20803.32}
\]

with `kappa<beta/2` to retain (L-20803.22). Thus the construction removes not
only each fixed mode separately but a power-growing inner zero block. The
remaining moving/high-frequency block is the proper input to support averaging.

## 7. Exact Schur boundary

The desired source scalar is still the minimum over the complete affine source
class. For the explicit trial `x_M`, put

\[
 r_M^{\rm Sch}=P_WA_{M,M^2}x_M.
 \tag{L-20803.33}
\]

The exact residual-shorting identity is

\[
\boxed{
 {g_M\over\ell_MA_{M,M^2}^{-1}\ell_M^*}
 ={1\over g_M}
 \left[
 \langle A_{M,M^2}x_M,x_M\rangle
 -(r_M^{\rm Sch})^*A_{WW,M}^{-1}r_M^{\rm Sch}
 \right].}
 \tag{L-20803.34}
\]

Equations (L-20803.24)--(L-20803.32) solve the complete fixed-frequency
factorial/metric part of a line-centered perturbation proof. They do **not**
bound the second term of (L-20803.34) by themselves. A proof of the requested
scalar gate must now combine this explicit packet with one joint estimate for
its line-centered trial energy and actual residual, as in `L-15633/L-18512`, or
work directly with the centered-prime resolvent.

## 8. Proof boundary

- The partial fractions, source normalization, gamma response, and metric bound
  are exact.
- The fixed-mode and power-growing-block estimates include all factorial and
  source-graph metric costs.
- The construction supplies a genuine feasible exponent wedge which a fixed or
  half-shift packet does not have.
- It does not assert that raw trial suppression controls a Schur minimum.
- The unresolved quantity is the joint residual in (L-20803.34), not frame
  conditioning or a hidden factorial loss.
