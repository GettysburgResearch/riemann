# Integrated pole-cancelled smoothing and a finite operator bound

22 October 2026. Status: exact analytic identity and finite polynomial
operator estimate; the continued primitive operator estimate remains
unproved. No improved inverse moment or zero-free boundary follows.

Source: rStation paper 10, v2, Sections 2--8, snapshot SHA256
`525c899dd4dd5cb0ed15db43f63fb6e25cc140f98358e9d41ddfe897f5a23a7a`.
Download provenance is recorded in `SOURCE_MANIFEST.json`.
The canonical online location is
<https://rstation.ai/problems/riemann_hypothesis/papers/10>.

## 1. A finite dyadic operator that really saves label length

Over the Eisenstein field, retain good ideal representatives and all
zero extensions. Let rows `n` be unrestricted good ideals with `Nn<=X`,
and let labels `R` be any distinct sixth-power-free good ideals with
`NR<=K`. On squarefree good moduli `Nc~L`, let `|b_c|<=C L^(-1/2-eta)`.
Define

\[
 T_L(n,R)=\sum_{c\ {\rm sf},\ Nc\asymp L}
                   b_c\chi_c(n)\chi_c(R).
 \tag{1}
\]

Either common orientation is allowed. Fixed ray restrictions and common
punctures are retained by diagonal masks and fixed block decompositions.
This is an operator on arbitrary label coefficient vectors.

Write

\[
 \Psi_6(V,L)=V+L+V^{5/6}L^{1/3}+V^{1/3}L^{5/6},
\]

and

\[
 \Psi_{\rm all}(X,L)=X+LX^{1/6}
                  +X^{5/6}L^{1/3}+X^{1/3}L^{5/6}.
\]

The source's sextic sieve and matrix multiplication give

\[
 \boxed{\quad
 \|T_L\|^2\ll_\epsilon (XKL)^\epsilon
 L^{-1-2\eta}\Psi_{\rm all}(X,L)\Psi_6(K,L).
 \quad} \tag{2}
\]

**Proof.** Factor the matrix as the character matrix from moduli `c` to
rows `n`, the diagonal multiplier `b_c`, and the transposed character
matrix from labels `R` to `c`. The first squared operator norm is bounded
by `Psi_all`; the second is bounded by `Psi_6(K,L)`. To obtain the first
bound, write `n=n0 d^6` uniquely, with `n0` sixth-power-free. For each
fixed `d`, its exact natural zero is the column mask `(c,d)=1`; row blocks
are orthogonal. Sum the source sieve bounds over `Nd<=X^(1/6)`:
the four contributions are respectively `O(X)`, `O(L X^(1/6))`,
`O(X^(5/6)L^(1/3))`, and `O(X^(1/3)L^(5/6))`. The sums in the first,
third, and fourth terms converge with weights `(Nd)^(-6)`, `(Nd)^(-5)`,
and `(Nd)^(-2)`. This proves (2). No average over label coefficients has
replaced the operator norm. QED.

In particular, if

\[
                    2\le K\le X^{1/3},\qquad
                       K\le L\le\sqrt{XK},
\]

then

\[
             \|T_L\|^2\ll_\epsilon (XK)^\epsilon X K^{1/6}.
 \tag{3}
\]

Indeed `Psi_all(X,L) << X+X^(5/6)L^(1/3)` in this range, and
`Psi_6(K,L) << L+K^(1/3)L^(5/6)`. After division by `L`, the four
products are bounded by `X K^(1/6)`: the last one is at most
`X^(11/12)K^(5/12) <= X K^(1/6)` because `K^3<=X`.

The lower bound `L>=K` matters. For the full set of permitted labels,
the modulus-one contribution alone is the all-ones matrix, with squared
operator norm comparable to `XK`.
Thus evaluating (2) only at the natural functional-equation length is
not a proof of an operator bound for the entire smoothed primitive
Dirichlet series.

## 2. Integrated smoothing cancels all sufficiently short moduli

Let `w` be a fixed smooth function supported in `[a0,b0]` with `a0>0`, and
put

\[
 \widehat w(s)=\int_0^\infty w(x)x^{s-1}\,dx,
 \quad\theta=7/6,\quad u=1+\eta+it,
 \quad0<\eta<1/12.
\]

For one fixed numerator `r`, write

\[
 H_r(u)=\sum_{(c,r)=1}\frac{\nu(c)g_6(r,c)}{(Nc)^u}
\]

in its initial absolute half-plane and then use the source's primitive
continuation on `Re u>1`. Its possible pole there at `theta` is at most
simple. Define

\[
 \mathcal E_U[H_r]=\frac1{2\pi i}
   \int_{(1+\eta)}H_r(u)\widehat w(u-1/2)U^{u-1}\,du.
 \tag{4}
\]

This is exactly the source's actual adjoint contour remainder. It is
not the value of `H_r` at one height.

For any fixed `Y>0`, use the source's pole-cancelling smoothing

\[
 P_r(u;Y)=\sum_{(c,r)=1}\frac{\nu(c)g_6(r,c)}{(Nc)^u}
             e^{-Nc/Y}\left(1+\frac{Nc/Y}{u-\theta}\right).
 \tag{5}
\]

Termwise Mellin inversion gives the exact identity

\[
 \begin{split}
 \mathcal E_U[P_r]
   =U^{-1/2}\sum_{(c,r)=1}
      \frac{\nu(c)g_6(r,c)}{\sqrt{Nc}}e^{-Nc/Y}
       \left[
          w(x)-\frac{Nc}{Y}x^{-2/3}
                    \int_0^x w(t)t^{-1/3}\,dt
       \right],\qquad x=\frac{Nc}{U}.
 \end{split}
 \tag{6}
\]

To check the sign and support, on the line `Re u<theta` one has

\[
 \frac1{2\pi i}\int_{(1+\eta)}
     \frac{\widehat w(u-1/2)x^{-u}}{u-\theta}\,du
       =-x^{-\theta}\int_0^x w(t)t^{-1/3}\,dt.
 \tag{7}
\]

This follows either by Mellin convolution or from the elementary Mellin
transform of `-x^(-2/3) 1_(x>=1)`. Equation (7), divided by the central
factor `x^(-1/2)`, is precisely the second term in (6).

Both terms in the square brackets vanish identically when `Nc<a0 U`.
Consequently, if `Y<=U^(1-delta)` with fixed `delta>0`, the entire
right side of (6) is smaller than every negative power of `U`, uniformly
in polynomially bounded numerator and matrix lengths. For a direct
absolute bound use `|g_6(r,c)|<=Nc`, polynomial ideal counting, and
`e^(-Nc/Y)<=e^(-a0 U/(2Y))e^(-Nc/(2Y))` on the remaining support. The
same calculation holds for the completed full series, grouping its
convolution variable `m=c d^6` before applying (6).

This cancellation explains why the short-modulus objection to a bound
for `H_r(u)` does not by itself obstruct a bound for the actual `E`.
The Mellin integral must be kept intact until that cancellation occurs.

## 3. A licensed completed shift and its exact change of scales

The source supplies continuation and reflection for the **completed
full finite vector**, `Z_r(u)=zeta_S(6u-5)D_r(u)`. Define the completed
primitive component

\[
                \mathscr H_r(u)=\zeta_S(6u-5)H_r(u).
\]

It too has no pole other than a possible simple theta pole in the strip
`Re u>=1-eta`. To justify this statement, reduce every numerator
valuation modulo six while retaining its modulus exclusion, and apply
the source's finite local inversions (3.3)--(3.4), with all ray
interchanges. After multiplying them by the common factor
`zeta_S(6u-5)`, they express `mathscr H_r` as a finite sum of completed
full components with finite Euler denominators
`1-nu(p)^6(Np)^(5-6u)`. Their zeros have real part `5/6`, so none occurs
in this strip, since `1-eta>11/12`. The full components have the asserted
regularity by source Section 2; the same inversions also preserve their
polynomial vertical growth for each fixed numerator. This reasoning
uses the full finite vector, not a scalar functional equation for `H`.

Consequently pole-cancelled smoothing gives the licensed identity

\[
 \mathscr H_r(u)=\mathscr P_r(u;Y)
 -\frac1{2\pi i}\int_{(-2\eta)}
 \mathscr H_r(u+z)\Gamma(z)
       \left(1+\frac z{u-\theta}\right)Y^z\,dz,
 \qquad \Re u=1+\eta.
 \tag{8}
\]

Its completed smoothed convolution is exactly

\[
 \mathscr P_r(u;Y)=\sum_{\substack{c,d\ {\rm good}\\(c,r)=1}}
     \frac{\nu(c)g_6(r,c)}{(Nc)^u}(Nd)^{5-6u}
      F_u\!\left(\frac{Nc(Nd)^6}{Y}\right),
 \qquad F_u(x)=e^{-x}\left(1+\frac{x}{u-\theta}\right).
 \tag{8a}
\]

Start the defining Mellin integral on `Re z=2`, where the series is
absolutely convergent, and shift to `Re z=-2eta`. Its residue at zero
is `mathscr H_r(u)`; the factor `1+z/(u-theta)` cancels its only other
possible crossed pole. The next pole of `Gamma(z)` is at `z=-1`, to
the left of the new contour. This proves (8). Formula (6) applies to
(8a) after grouping its actual index `m=c d^6` and its coefficient
`nu(c)g_6(r,c)(Nd)^5`.

It is **not** justified to replace `mathscr H` by raw primitive `H` in
(8). Dividing by `zeta_S(6u-5)` on the shifted line samples
`Re(6u-5)=1-6eta`; the source's completed continuation alone gives no
zero-free assertion there. Completion can instead be removed exactly
on the original right-hand line, using its absolutely convergent
reciprocal Euler series:

\[
 \boxed{\quad
 \mathcal E_U[H_r]
    =\sum_{a\ {\rm good}}\frac{\mu(a)}{Na}\,
        \mathcal E_{U/(Na)^6}[\mathscr H_r].
 \quad} \tag{8b}
\]

Indeed `1/zeta_S(6u-5)=sum_a mu(a)(Na)^(5-6u)`, and

\[
       (Na)^{5-6u}U^{u-1}
          =(Na)^{-1}\bigl(U/(Na)^6\bigr)^{u-1}.
\]

At `Re u=1+eta` the absolute coefficient weight before integration is
`(Na)^(-1-6eta)`, which is summable. Polynomial vertical growth and the
rapid decay of `widehat w` justify interchange. No zeta zero-free
assertion is used.

All the scales in (8b) must remain. At scale `U_a=U/(Na)^6`, equation
(6) suppresses the completed polynomial only when its actual index
`m` is below `a0 U_a`. A fixed smoothing length short relative to
`U` need not be short relative to `U_a`. Thus (8b) is an exact
completion-removal interface, not an estimate for its infinite sum.

The polynomial part admits one further exact cancellation. Choosing
`Y_a=Y/(Na)^6` gives

\[
 \sum_{a\ {\rm good}}\frac{\mu(a)}{Na}\,
 \mathcal E_{U/(Na)^6}
       [\mathscr P_r(\,\cdot\,;Y/(Na)^6)]
       =\mathcal E_U[P_r(\,\cdot\,;Y)].
 \tag{8c}
\]

In the completed convolution (8a), put `b=ad`. After applying (6), both
profile arguments depend only on `Nc(Nb)^6`, and the outside coefficient
is `U^(-1/2) nu(c)g_6(r,c)(Nb)^2/sqrt(Nc)` times
`sum_(a|b)mu(a)`. Exponential decay justifies the grouping, and that
divisor sum vanishes unless `b=1`, proving (8c). Thus scaled smoothing
does remove completion from this polynomial part. In the reflected
integral, however, the combined Euler coefficient is
`mu(a)(Na)^(5-6(u+z))`. On `Re(u+z)=1-eta` its absolute weight is
`(Na)^(-1+6eta)`, which is not summable. One cannot move the Euler sum
inside that contour by absolute convergence or obtain the required
operator estimate by summing its absolute weights. The ordering and
signed arithmetic of this remaining sum are substantive analytic data.

## 4. The remaining primitive operator estimate

For squarefree `r`, the exact primitive local inversion is

\[
 H_\nu(r,u)=E_r(u)^{-1}\sum_{d\mid r}
       \mu(d)\nu(d)^2\gamma_2(d)
       \overline{\chi_d(r/d)}^{\,2}
       (Nd)^{3/2-2u}D_\nu(rd^2,u).
 \tag{9}
\]

Here `E_r(u)=prod_(p|r)(1-nu(p)^6 (Np)^(5-6u))`. Multiplying (9) by
`zeta_S(6u-5)` gives the same identity with `H` and `D` replaced by
`mathscr H` and `Z`, respectively, on both lines in (8). All finite ray
interchanges are required for general valuations. At `r=nR`, the
divisors in (9) depend jointly on the row and label. The source's proof
applies divisor Cauchy for each fixed label and then averages its rows;
this gives the Hilbert--Schmidt estimate `X K^(3/2)` after summing labels.
It does not preserve an arbitrary linear combination of labels.

For example, even before the Euler-denominator expansion, the factor
`(Nd)^(3/2-2u)` changes the physical scale `U` to `U/(Nd)^2`, with
outside coefficient `(Nd)^(-1/2)`, while the full-series numerator becomes
`r d^2`. Reflection therefore has the formal dual length
`Nr (Nd)^4/U`, not `Nr/U`. Removing this change by a pointwise bound or
an unlicensed diagonal coefficient substitution would discard the main
new difficulty.

An operator estimate stable under the actual full primitive inversion
must retain the common Mellin profiles, all local changes, and all
scales in (8b). The finite estimate (3) and cancellation (6) do not
provide such an estimate. They do not bound the full complementary
operator or establish the high-conductor inverse moment.
