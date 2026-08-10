# L-90207 — A fixed binary–ternary producer resonance survives with a certified nonzero numerator

Claim ID: `L-90207`  
Status: **PROPOSED COMPLETE ANALYTIC/CERTIFIED LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-10  
Depends on: `L-90204`, `L-90205`, `L-90206`; the exact sparse hitting trace of `L-32301`; elementary Rouché bounds and the alternating eta continuation of zeta  
Scope: one fixed producer coordinate `n=2`; no RH claim

## 1. The fixed sparse producer

Take threshold `n=2`.  The transition window is `{2,3}`.  The true hitting
trace of `L-32301` is

\[
 h_2(2)=1,
 \qquad
 h_2(3)=\frac23.
\tag{L-90207.1}
\]

Indeed the four children of `3` are `1,2,1,2`, and the size-biased kernel gives
`Q(3,2)=2/3`.

For the endpoint-independent combined trace put

\[
 G(m)=m h_2(m),
 \qquad
 a(m)=G(m)-G(m-1).
\tag{L-90207.2}
\]

Then

\[
 G(2)=2,
 \qquad
 G(3)=2,
 \qquad
 G(4)=4,
\]

so

\[
 \boxed{a(2)=2,\qquad a(3)=0,\qquad a(4)=2.}
\tag{L-90207.3}
\]

By `L-90205`, for every `m>=5`,

\[
 \boxed{
 a(m)=\frac12a(\lceil m/2\rceil)
      +\frac12a(\tau_3(m)),
 }
\tag{L-90207.4}
\]

and therefore

\[
 \boxed{|a(m)|\le2\qquad(m\ge1).}
\tag{L-90207.5}
\]

The corresponding Liouville/Möbius endpoint functional is exactly

\[
 \boxed{
 F(X):=\mathcal F_{-1}(X)=2A_X(2),
 }
\tag{L-90207.6}
\]

where `A_X(2)` is the explicit binary–ternary producer coefficient of
`L-23811`.

## 2. Continued transform

Let

\[
 \mathcal A(u)=\sum_{m\ge1}a(m)m^{-u}
\]

in its initial half-plane.  `L-90205` continues it to `Re u>0` as

\[
 \boxed{
 \mathcal A(u)=\frac{N(u)}{\Delta(u)},
 }
\tag{L-90207.7}
\]

where

\[
 \Delta(u)
 =1-\frac12\left(2^{1-u}+3^{-u}+(3/2)^{-u}\right)
\tag{L-90207.8}
\]

and

\[
 N(u)=\mathcal B(u)+\frac12\mathcal R_2(u)+\frac12\mathcal R_3(u)
\tag{L-90207.9}
\]

is analytic for `Re u>0`.

Combining `L-90204` and `L-90205`, with `u=s+1/2`, gives

\[
 \boxed{
 \widehat F(s)
 =\frac{\mathcal A(s+1/2)}{s^2\zeta(s+1/2)}
 }
\tag{L-90207.10}
\]

as a meromorphic-continuation identity on the common continued domain.

## 3. A concrete characteristic zero

Define

\[
\begin{aligned}
 u_c={}&0.9493558206795862115934860845258463866962847857058568\\
 &+45.675805472436769923338551374209625113229166906532517\,i
\end{aligned}
\tag{L-90207.11}
\]

and let

\[
 r=10^{-10}.
\]

The retained verifier evaluates the elementary exponential polynomial with
50-digit interval arithmetic and obtains

\[
 |\Delta(u_c)|<7.42\times10^{-16},
\tag{L-90207.12}
\]

\[
 |\Delta'(u_c)|>0.6722029956,
\tag{L-90207.13}
\]

while throughout `|u-u_c|<=r`,

\[
 |\Delta''(u)|<0.518.
\tag{L-90207.14}
\]

On `|w|=r`, Taylor's theorem therefore gives

\[
 |\Delta(u_c)+E(w)|
 <7.5\times10^{-16}+\frac{0.518}{2}r^2
 <|\Delta'(u_c)|r.
\]

Rouché's theorem gives exactly one zero `u_*` in the disk:

\[
 \boxed{
 \Delta(u_*)=0,
 \qquad
 |u_*-u_c|<10^{-10}.
 }
\tag{L-90207.15}
\]

The same derivative bounds show that this zero is simple.  In particular,

\[
 \boxed{
 \Re u_*>0.9493558205795862.
 }
\tag{L-90207.16}
\]

## 4. The producer numerator does not cancel the zero

For this trace the finite renewal defect is determined by (L-90207.3).  Evaluate
`N(u_c)` by truncating the absolutely convergent correction series
`R_2,R_3` at `M=50,000`.  The 60-digit finite evaluation is

\[
\begin{aligned}
 \mathcal B_M(u_c)
 &=0.3027793825356794789-0.3105219001053443282i,\\
 \mathcal R_{2,M}(u_c)
 &=-0.1687985661620446348+0.4900426141085744973i,\\
 \mathcal R_{3,M}(u_c)
 &=-0.4066168930888125615+0.1390807231763036806i,
\end{aligned}
\]

hence

\[
 \boxed{
 N_M(u_c)
 =0.01507165291025088075
 +0.004039768537094760747i,
 }
\tag{L-90207.17}
\]

and

\[
 |N_M(u_c)|>0.01560366.
\tag{L-90207.18}
\]

The bound `|a(m)|<=2` makes the infinite tail elementary.  If
`\sigma=\Re u` and `U=|u|`, the mean-value theorem gives

\[
 |\mathcal R_{2,>M}(u)|
 \le2U\sum_{m>M}m^{-\sigma-1},
\]

and

\[
 |\mathcal R_{3,>M}(u)|
 \le5U\sum_{m>M}m^{-\sigma-1}.
\]

Thus, throughout the root disk,

\[
 \boxed{
 |N(u)-N_M(u)|
 \le3.5\,U\,M^{-\sigma}/\sigma
 <0.005827.
 }
\tag{L-90207.19}
\]

A separate derivative estimate for the same difference kernels gives

\[
 \sup_{|u-u_c|\le r}|N'(u)|<812,
\tag{L-90207.20}
\]

so moving from `u_c` to the exact root costs less than `8.2e-8`.  Reserving an
additional `10^{-6}` for the finite transcendental evaluation still leaves

\[
 \boxed{
 |N(u_*)|>0.0097.
 }
\tag{L-90207.21}
\]

Therefore the characteristic zero is **not** canceled by the sparse producer
boundary condition, and `mathcal A(u)` has a simple pole at `u_*`.

## 5. Zeta does not cancel the pole

For `Re u>0`, use

\[
 \eta(u)=(1-2^{1-u})\zeta(u),
\tag{L-90207.22}
\]

where

\[
 \eta(u)=\sum_{n\ge1}(-1)^{n-1}n^{-u}.
\]

At `u_c`, the first `10,000` terms give

\[
 \eta_{10000}(u_c)
 =0.03164454350108357613
 +0.6208399553862113213i,
\]

so

\[
 |\eta_{10000}(u_c)|>0.6216459.
\tag{L-90207.23}
\]

Pairing consecutive terms and using the mean-value theorem gives the infinite
tail bound

\[
 |\eta(u)-\eta_{10000}(u)|
 \le |u|\,10000^{-\Re u}/\Re u
 <0.007673
\tag{L-90207.24}
\]

throughout the root disk.  The disk variation of the finite part is below
`1.2e-8`.  Hence

\[
 \boxed{|\eta(u_*)|>0.6139.}
\tag{L-90207.25}
\]

Also

\[
 |1-2^{1-u_*}|>0.2503.
\tag{L-90207.26}
\]

Consequently

\[
 \boxed{\zeta(u_*)\ne0.}
\tag{L-90207.27}
\]

The universal factor `s^{-2}` is also nonzero at

\[
 s_*=u_*-\frac12.
\]

Combining Sections 3--5:

\[
 \boxed{
 \widehat F(s)
 \text{ has a genuine nonreal pole at }
 s_*=u_*-\frac12,
 }
\tag{L-90207.28}
\]

with

\[
 \boxed{
 \Re s_*>0.4493558205795862.
 }
\tag{L-90207.29}
\]

## 6. Real-axis audit

For real `u>1/2`, `Delta'(u)>0`, so `Delta` has exactly one real zero, at
`u=1`.  Zeta has no real zeros on `(1/2,1)` and is positive for `u>1`.
At `u=1`, `mathcal A(u)` has at most a simple pole because `Delta'(1)>0`, while
`1/zeta(u)` has a simple zero.  Hence the product in (L-90207.10) is removable
there.

Therefore

\[
 \boxed{
 \widehat F(s)
 \text{ is holomorphic at every real }s>0.
 }
\tag{L-90207.30}
\]

The only positive-half-plane singularity certified here is nonreal.

## 7. Integer interpolation

The transform formulas use the natural real endpoint.  The producer theorem is
stated at integer endpoints.  Put

\[
 F^\#(x)=F(\lfloor x\rfloor).
\]

Since

\[
 F(X)=\sum_{q\le X}(a*\mu)(q)q^{-1/2}\log(X/q),
\tag{L-90207.31}
\]

and `|a(m)|<=2`, one has

\[
 |(a*\mu)(q)|\le2\tau(q).
\tag{L-90207.32}
\]

For `N<=x<N+1`, the support is unchanged, and

\[
 F(x)-F(N)
 =\log(x/N)\sum_{q\le N}\frac{(a*\mu)(q)}{\sqrt q}.
\]

Using

\[
 \sum_{q\le N}\frac{\tau(q)}{\sqrt q}
 =\sum_{ab\le N}(ab)^{-1/2}
 \le2\sqrt N(1+\log N),
\]

we obtain

\[
 \boxed{
 |F(x)-F^\#(x)|
 \le4\frac{1+\log N}{\sqrt N}.
 }
\tag{L-90207.33}
\]

Thus the Mellin transforms of `F` and `F#` differ by a function holomorphic for
`Re s>-1/2`.  In particular the pole (L-90207.28) survives unchanged for the
integer-step interpolation.

A crude absolute estimate from (L-90207.31) gives

\[
 F^\#(x)=O(\sqrt x\log^2(2x)),
\tag{L-90207.34}
\]

so its Mellin transform has finite abscissa of convergence at most `1/2`.

## 8. Assurance boundary

The infinite estimates, Rouché argument, recurrence, and interpolation bounds
are analytic.  The retained `X-90204` artifact evaluates only the finite
transcendental quantities with 60--80 digits and uses very large safety margins;
`Delta(u_c)` and `Delta'(u_c)` are additionally checked with interval arithmetic.
The numerator noncancellation margin after all analytic tails is greater than
`9e-3`.

Proved/certified here:

- one simple characteristic root in a radius `1e-10` disk;
- noncancellation by the actual `n=2` sparse producer trace;
- noncancellation by zeta;
- a genuine nonreal pole with real part greater than `0.44935582057` after the critical shift;
- holomorphy of the continued transform on the positive real axis;
- transfer of the pole to integer endpoints.

The oscillation consequence is stated separately in `T-90204`.