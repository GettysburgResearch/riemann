# A positive theta-derived source with an added off-real quartet

Status: proposed exact analytic counterexample; independent review pending.
Scope: a modified source, not actual xi. It tests which source-class properties
are sufficient for derivative descent. No RH conclusion is asserted.
Dependencies: the correctly normalized theta Fourier identity and even smooth
source from `reviews/D-pass3/PROOFS_AND_REPAIRS.md#R16`; the established zero
strip and entire growth of xi; elementary integration by parts and an exact
polynomial positivity certificate.

## 1. The construction preserves the known strip and a finite zero census

Use `Xi(z)=xi(1/2+iz)`. For any `R>=10` and `0<d<1/2`, put

\[
Q_{R,d}(z)=((z-R)^2+d^2)((z+R)^2+d^2)
 =z^4+2(d^2-R^2)z^2+(R^2+d^2)^2,
\]

\[
G_{R,d}(z)=\frac{Q_{R,d}(z)}{Q_{R,d}(0)}\Xi(z).
\tag{P1}
\]

This is even real entire, and `G(0)=Xi(0)`. It has the complete zero multiset
of actual Xi together with the four additional zeros

\[
\pm R\pm id.                                      \tag{P2}
\]

If a location already is an Xi zero, its multiplicity increases by one;
there is no cancellation. The known actual-xi zero strip `|Im z|<1/2` is
preserved, without assuming RH. Choosing R above any prescribed verification
height preserves **exactly** its finite zero census. In a box `|Re z|<=T`,
the zero count changes by at most four, with multiplicity. The whole
Riemann–von Mangoldt asymptotic, including its linear term and logarithmic
error scale, is therefore preserved. Polynomial multiplication also
preserves entire order one and its leading growth; it adds only an
`O(log |z|)` term to logarithmic maximum growth.

The following less immediate fact is the useful obstruction: G still has a
strictly positive smooth theta-derived Fourier source.

## 2. Positivity of the complete Fourier source

Let `Phi_theta` be the even theta density with
`Xi(z)=integral_R Phi_theta(u)exp(izu)du`. Define

\[
\widetilde\Phi_{R,d}(u)
 =\Phi_\theta^{(4)}(u)
  +2(R^2-d^2)\Phi_\theta''(u)
  +(R^2+d^2)^2\Phi_\theta(u).                       \tag{P3}
\]

The inherited Gaussian-weighted derivative decay permits four integrations
by parts on the full real line. Consequently the Fourier transform of (P3)
is `Q_(R,d)(z) Xi(z)` exactly, and division by `Q_(R,d)(0)` gives the source
for G. All boundary terms vanish. The source remains even, smooth and in
the inherited rapidly decreasing Fourier class.

The exact global inequalities

\[
\Phi_\theta''\ge-20\Phi_\theta,
\qquad\Phi_\theta^{(4)}\ge-4000\Phi_\theta          \tag{P4}
\]

give, since `R^2-d^2>0`,

\[
\widetilde\Phi_{R,d}
 \ge\bigl[(R^2+d^2)^2-40(R^2-d^2)-4000\bigr]\Phi_\theta
 \ge(R^4-40R^2-4000)\Phi_\theta
 \ge2000\Phi_\theta>0.                            \tag{P5}
\]

Thus positivity includes the entire source, rather than just an asymptotic
tail or a finite set of sample points.

### Exact atom-level certificate for (P4)

For `u>=0`, write `t=pi n^2 exp(2u)>3`. The nth theta summand is

\[
e^{u/2-t}p_0(t),\qquad p_0(t)=4t^2-6t>0.
\]

Each u derivative replaces p by

\[
\mathcal Dp(t)=2t p'(t)+(1/2-2t)p(t).
\]

The second and fourth derivative polynomials are

\[
\begin{aligned}
p_2(t)&=16t^4-112t^3+165t^2-75t/2,\\
p_4(t)&=64t^6-1056t^5+5176t^4-8512t^3
                         +15465t^2/4-1875t/8.
\end{aligned}
\]

For `t=3+v`, `v>=0`,

\[
p_2(t)+20p_0(t)
 =16v^4+80v^3+101v^2+(33/2)v+9/2>0.                 \tag{P6}
\]

For `p_4+4000p_0`, the Fraction-only checker covers every unit interval
`[j,j+1]`, `j=3,...,9`, by all seven exact degree-six Bernstein coefficients.
Every coefficient is positive; the smallest among these 49 coefficients is
`5339753/120`. Since the Bernstein basis is nonnegative and sums to one,
this is a complete lower certificate on `[3,10]`, not a sample test.

For `t=10+v`, the exact tail polynomial is

\[
\begin{aligned}
p_4(10+v)={}&64v^6+2784v^5+48376v^4+422528v^3\\
 &+(7576425/4)v^2+(30619925/8)v+8129125/4>0.
\end{aligned}                                      \tag{P7}
\]

Equations (P6)–(P7) and the finite Bernstein cover prove (P4) for each atom
and then for their full differentiated sum. Evenness extends it to negative
u. Termwise differentiation and summation are justified by the inherited
local convergence and rapidly decreasing derivative bounds.

## 3. The generic high-order entry mechanism remains available

For fixed R,d, the n=1 term dominates the source tail. Its leading factor in
(P3) is `64 t^6 exp(u/2-t)`, so

\[
(\log\widetilde\Phi_{R,d})'
 =25/2-2\pi e^{2u}+O_{R,d}(e^{-2u}),
\qquad
(\log\widetilde\Phi_{R,d})''
 =-4\pi e^{2u}+O_{R,d}(e^{-2u}).                    \tag{P8}
\]

The only leading difference from the original theta tail is the fixed
linear coefficient `25/2` in place of `9/2`. The repaired saddle proof in
`reviews/A/supplement/REPORT.md#S06` uses that coefficient only inside its
bounded `O(1)` terms. Strict positivity and smoothness make the compact
second-log-derivative bound available. Its local quadratic and exterior
exponential argument therefore applies with constants and starting order
depending on R,d. It gives `mu_r~(log r)/2`, the all-y positive-tilt variance
bound and complete lower-ray high-order entry in `T^2 log r/r ->0`.

The explicit finite-moment certificate in `COMPANION_SECTOR.md` states the
actual inputs to the last inference. This is not an assertion that its
low-order inputs hold.

Consequently positivity of the complete Fourier source, the known zero strip,
the full classical zero-count asymptotic, any fixed verified zero census,
and the generic high-order entry mechanism can coexist with an off-real zero.
One must use a property that binds the **exact arithmetic source**, or an
additional signed transport estimate. The multiplicative factor in (P1)
changes that source, even though many analytic checks survive.

## 4. Verification boundary

`verify_theta_quartet.py` reconstructs the derivative recurrence and verifies
all 49 Bernstein coefficients, the positive tail coefficients, and (P5) by
exact rational arithmetic. It also checks the polynomial multiplier/derivative
signs and synthetic quartet positions algebraically. It does not numerically
locate actual xi zeros or certify a chosen finite verification height.
The Fourier identity, zero strip and source regularity are named classical
inputs; the proof above supplies the new source positivity and obstruction.
