# L-23805 — Continuum carry symbol and the sharp mass eight

Claim ID: `L-23805`  
Title: The scaled carry operator has an explicit zeta Mellin symbol, and its exact inverse has first mass equal to eight  
Status: **PROPOSED EXACT CONTINUUM LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-07  
Issue: #238  
Scope: continuum geometry and proof firewall; no positivity theorem

## 1. Scaled carry kernel

For `x>=1`, put

\[
\boxed{
K(x)={\lfloor x\rfloor\,[\lfloor x\rfloor+1-x]\over x}.}
\tag{L-23805.1}
\]

If `n/q -> x` while `n,q -> infinity`, the exact finite carry coefficient

\[
\beta_{nq}
={\lfloor n/q\rfloor\,[q-1-(n\bmod q)]\over n+1}
\]

converges to `K(x)`. Thus, under the scaling

\[
n=Xs,
\qquad q=Xt,
\qquad d_X(n)=X^{-3/2}f(s),
\]

the carry equations tend to

\[
\boxed{
(Tf)(t)=\int_t^1 f(s)K(s/t)\,ds
=t^{-1/2}\log(1/t).}
\tag{L-23805.2}
\]

The normalization `X^(-3/2)` is forced by the desired entropy scale:

\[
\sum_n n d_X(n)
\sim \sqrt X\int_0^1s f(s)\,ds.
\]

## 2. Mellin transform of the carry kernel

For `Re p>2`, intervalwise integration on `[k,k+1]` gives

\[
\begin{aligned}
I(p)
&:=\int_1^\infty K(x)x^{-p}\,dx\\
&=\sum_{k\ge1}\int_k^{k+1}
 \left({k(k+1)\over x}-k\right)x^{-p}\,dx.
\end{aligned}
\tag{L-23805.3}
\]

The two resulting series telescope, yielding

\[
\boxed{
I(p)={p-2\over p(p-1)}\,\zeta(p-1).}
\tag{L-23805.4}
\]

The apparent singularity at `p=2` is removable and

\[
\boxed{I(2)=\frac12.}
\tag{L-23805.5}
\]

Equation (L-23805.4) continues meromorphically wherever its right side does.
It explains why reciprocal zeta appears when the carry matrix is inverted: it
is already present in the continuum symbol, not introduced by a particular
finite elimination order.

## 3. Exact inverse Mellin transform

Let

\[
F(p)=\int_0^1 f(s)s^{p-1}\,ds.
\tag{L-23805.6}
\]

For `Re z` large enough, Fubini and the substitution `x=s/t` give

\[
\int_0^1 (Tf)(t)t^{z-1}\,dt
=I(z+1)F(z+1).
\tag{L-23805.7}
\]

The target in (L-23805.2) has Mellin transform

\[
\int_0^1t^{z-3/2}\log(1/t)\,dt
={1\over(z-1/2)^2}.
\tag{L-23805.8}
\]

Writing `p=z+1`, the unique formal inverse therefore has

\[
\boxed{
F(p)
={p(p-1)
 \over
 (p-2)\zeta(p-1)(p-3/2)^2}.}
\tag{L-23805.9}
\]

This is the continuum version of the finite Möbius decoder in `L-23803`.

## 4. The sharp mass is eight

At `p=2`,

\[
(p-2)\zeta(p-1)\longrightarrow1.
\]

Consequently (L-23805.9) gives the exact value

\[
\boxed{
F(2)=\int_0^1s f(s)\,ds=8.}
\tag{L-23805.10}
\]

Thus the coefficient `8` in the carry mass theorem is not fitted from prime
data or entropy asymptotics. It is the exact first moment of the inverse carry
operator. Since `G_n~n/2`, it produces the required prime-ramp constant `4`.

## 5. Explicit Möbius/Riesz profile

For `Re p>2`, expand

\[
{1\over\zeta(p-1)}
=\sum_{m\ge1}{\mu(m)\over m^{p-1}}.
\]

The rational factor in (L-23805.9) has the partial fraction decomposition

\[
{p(p-1)\over(p-2)(p-3/2)^2}
={8\over p-2}-{7\over p-3/2}
-{3/2\over(p-3/2)^2}.
\tag{L-23805.11}
\]

Let

\[
r(s)=8s^{-2}-7s^{-3/2}
-{3\over2}s^{-3/2}\log(1/s),
\qquad0<s\le1.
\tag{L-23805.12}
\]

Formal inverse Mellin transformation gives the finite-at-each-point profile

\[
\boxed{
 f(s)=\sum_{m\le1/s}\mu(m)m\,r(ms).}
\tag{L-23805.13}
\]

This formula makes the arithmetic obstruction explicit. The individual Riesz
components need not be positive; any successful positivity or near-packing
argument must group the complete Möbius family before discarding signs.

## 6. Consequence for proof design

The continuum operator supplies three exact facts:

1. the only sharp mass capable of paying the archimedean screw term is `8`;
2. the inverse contains `1/zeta`, so a coefficientwise positivity proof is
   expected to be RH-bearing;
3. a nonnegative **packing** may nevertheless be easier than positivity of the
   exact inverse, because it may leave a subpolynomial residual and need only
   recover the first mass.

This motivates the canonical greedy packing theorem in `T-23802` rather than
full Carry Saturation.

## 7. Proof boundary

Closed here:

- the scaled carry kernel;
- its Mellin symbol;
- the inverse multiplier;
- the exact sharp mass `8`;
- the explicit Möbius/Riesz inverse profile.

Open:

- positivity of the continuum inverse;
- a finite nonnegative packing with mass `8 sqrt(X)-X^(o(1))`;
- RH.