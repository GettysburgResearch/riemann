# L-91326 — Logarithmic weighted model projection closes the forced Cauchy domain

Claim ID: `L-91326`  
Status: **PROVED EXACT WEIGHTED-DOMAIN THEOREM, USING THE STANDARD A2 RIESZ-PROJECTION THEOREM**  
Created: 2026-08-13  
Depends on: `L-91323`, `L-91325`  
Closes: forced-delay membership in the corrected reciprocal-xi domain  
RH status: **unproved**

## 1. The logarithmic weight

Put

\[
 L(t)=1+\log(2+|t|),
 \qquad
 \omega(t)=L(t)^2.
 \tag{L-91326.1}
\]

Then

\[
 \boxed{\omega\in A_2(\mathbb R).}
 \tag{L-91326.2}
\]

### Proof

Recall that the `A2` condition is

\[
 \sup_I
 \left(\frac1{|I|}\int_I\omega\right)
 \left(\frac1{|I|}\int_I\omega^{-1}\right)<\infty,
 \tag{L-91326.3}
\]

where the supremum is over finite intervals.

Let `r=|I|` and `d=dist(I,0)`.

If `d>=2r`, then `2+|t|` varies by a bounded multiplicative factor on `I`.
Consequently `L(t)`, and hence `omega(t)`, is comparable to a constant on the
whole interval, uniformly in `I`. The product in (L-91326.3) is therefore
bounded.

If `d<2r`, then `I` is contained in `[-3r,3r]`. Hence

\[
 \frac1r\int_I\omega(t)dt
 \le C L(r)^2.
 \tag{L-91326.4}
\]

For large `r`, split the reciprocal integral at `sqrt(r)`:

\[
\begin{aligned}
 \int_0^{3r}\frac{dt}{L(t)^2}
 &\le \sqrt r
   +\frac{3r}{L(\sqrt r)^2}\\
 &\le C\frac r{L(r)^2}.
\end{aligned}
 \tag{L-91326.5}
\]

The bounded range of `r` is absorbed into the constant. By symmetry and
`I subset [-3r,3r]`, equation (L-91326.5) gives

\[
 \frac1r\int_I\omega(t)^{-1}dt
 \le \frac C{L(r)^2}.
 \tag{L-91326.6}
\]

Multiplying (L-91326.4) and (L-91326.6) proves (L-91326.2).

## 2. Every inner model projection is bounded in the logarithmic weight

By the standard Hunt--Muckenhoupt--Wheeden theorem, the Riesz projection
`P_+` is bounded on `L2(omega dt)`.

Let `Theta` be any inner function on the upper half-plane. On ordinary `L2`,

\[
 P_{K_\Theta}
 =P_+-M_\Theta P_+M_{\overline\Theta}.
 \tag{L-91326.7}
\]

Since `|Theta|=1` almost everywhere, both multiplication operators are
isometries on `L2(omega dt)`. Therefore (L-91326.7) extends uniquely to a
bounded operator there and

\[
 \boxed{
 \|P_{K_\Theta}F\|_{L^2(\omega dt)}
 \le C_\omega\|F\|_{L^2(\omega dt)}.
 }
 \tag{L-91326.8}
\]

The bound is independent of the inner function.

## 3. The safe Suzuki phase tangent has only logarithmic growth

Fix `a>1/2` and put

\[
 \sigma=\frac12+a>1.
\]

On the real boundary, functional symmetry gives

\[
 \Theta_a(t)=\frac{\xi(\sigma+it)}{\xi(\sigma-it)}.
 \tag{L-91326.9}
\]

Thus the logarithmic radial tangent is

\[
 \ell_a(t)
 =a\partial_a\log\Theta_a(t)
 =a\left[
  \frac{\xi'}\xi(\sigma+it)
  -\frac{\xi'}\xi(\sigma-it)
 \right].
 \tag{L-91326.10}
\]

Using

\[
 \frac{\xi'}\xi(s)
 =\frac1s+\frac1{s-1}
 -\frac12\log\pi
 +\frac12\psi(s/2)
 +\frac{\zeta'}\zeta(s),
 \tag{L-91326.11}
\]

absolute convergence of `zeta'/zeta` on `Re(s)=sigma` and the standard
digamma bound give

\[
 \boxed{
 |\ell_a(t)|\le C_aL(t).
 }
 \tag{L-91326.12}
\]

No zero-free estimate near the critical line is used; the entire argument is
on the fixed safe line `sigma>1`.

## 4. Every forced delayed Cauchy resident vector lies in the corrected domain

For a carrier `x` and delay `tau>=0`, put

\[
 F_{a,x,\tau}(t)
 =e^{-i\tau t}\Psi_a(t-x).
 \tag{L-91326.13}
\]

The rational Cauchy factor has relative degree three, so

\[
 |F_{a,x,\tau}(t)|
 \le C_{a,x}(1+|t|)^{-3}.
 \tag{L-91326.14}
\]

Consequently

\[
 F_{a,x,\tau}\in L^2(\omega dt).
 \tag{L-91326.15}
\]

Let

\[
 r_{a,x,\tau}
 =P_{K_{\Theta_a}}F_{a,x,\tau}.
 \tag{L-91326.16}
\]

By `L-91323`, this is exactly the forced resident vector

\[
 r_{a,x,\tau}
 =T_{\Theta_a,\tau}g_{a,x}
  +B_{\Theta_a,\tau}q_{a,x}.
 \tag{L-91326.17}
\]

Equations (L-91326.8) and (L-91326.15) give

\[
 r_{a,x,\tau}\in L^2(\omega dt).
 \tag{L-91326.18}
\]

Since multiplication by `bar Theta_a` preserves absolute value, (L-91326.12)
gives

\[
\begin{aligned}
 \|\ell_a\mathcal U_{\Theta_a}r_{a,x,\tau}\|_2^2
 &\le C_a^2
   \int_{\mathbb R}\omega(t)|r_{a,x,\tau}(t)|^2dt
 <\infty.
\end{aligned}
 \tag{L-91326.19}
\]

Therefore

\[
 \boxed{
 r_{a,x,\tau}\in\mathcal D_a
 =\{g\in K_{\Theta_a}:
   \ell_a\mathcal U_{\Theta_a}g\in L^2\}.
 }
 \tag{L-91326.20}
\]

Every finite carrier-delay packet belongs to `D_a` by linearity. The conclusion
is locally uniform on compact carrier and delay sets.

## 5. The canonical bridge and reflected orientation also enter the domain

The bridge transform of `L-91321` is

\[
 \widehat b_\eta(t)
 =-\frac{2i\eta t}{\eta^2+t^2}.
 \tag{L-91326.21}
\]

Its positive- and negative-Hardy rational components decay like `1/|t|`, so
each belongs to `L2(omega dt)`. Applying the corresponding model projection
and (L-91326.12) proves that the resident bridge components lie in the same
corrected domain. Reflection preserves the even weight `omega`, so the theorem
holds verbatim for the anti-causal orientation.

This is a domain statement only. It does not sign the mixed-orientation or
bridge arithmetic rows and columns.

## 6. Consequence for the corrected factorization

For every forced delayed Cauchy packet `h`, equation (L-91326.20) makes the
renormalized factorization of `L-91325` legitimate:

\[
 \boxed{
 \mathcal J_ah
 =a\sqrt{2V_a}\,
  \mathfrak T_{\varphi,a}
  \mathcal C_a\mathcal B_ah.
 }
 \tag{L-91326.22}
\]

Moreover

\[
 \mathcal C_a\mathcal B_ah
 =-\frac{\varphi_a\ell_a}{a\sqrt{V_a}}
   \mathcal U_{\Theta_a}h
 \in\operatorname{Dom}(\mathfrak T_{\varphi,a}).
 \tag{L-91326.23}
\]

Thus the corrected endpoint has no remaining form-domain ambiguity on the
actual delayed rational Cauchy and bridge packet. The only load-bearing issue
is the quantitative structured observability estimate through the unbounded
reciprocal-amplitude leg.

## 7. Exact boundary

```text
logarithmic weight omega belongs to A2                  EXACT
Riesz/model projections bounded on L2(omega)            STANDARD THEOREM + EXACT REDUCTION
safe Suzuki logarithmic tangent O(log |t|)              EXACT
all forced delayed rational Cauchy vectors in D_a       PROVED
finite carrier-delay packets in D_a                     PROVED
canonical bridge orientation components in D_a          PROVED
corrected reciprocal-xi factorization on physical core  PROVED
mixed-orientation and bridge arithmetic sign            OPEN
structured reciprocal-xi observability estimate         OPEN / RH-BEARING
Riemann Hypothesis                                      UNPROVED
```
