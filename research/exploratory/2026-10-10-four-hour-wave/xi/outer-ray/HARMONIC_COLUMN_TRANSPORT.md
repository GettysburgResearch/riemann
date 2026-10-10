# A finite companion column from complete-census localization

Status: proposed analytic continuation, pending independent exact-source review.
Scope: actual `Xi(z)=xi(1/2+iz)`, derivative order zero, every real
`1<=lambda<=10`, and the entire closed lower column `|Re z|<=8174`.
This is a finite real-part range, despite its unbounded depth. It does not
assert RH, an all-height sector, or any higher derivative order.
Exact dependencies: [THEOREM.md](THEOREM.md),
[CENSUS_LOCALIZATION.md](CENSUS_LOCALIZATION.md), the complete census and
primitive source qualifications in
[NATIVE_SLAB_CERTIFICATE.md](NATIVE_SLAB_CERTIFICATE.md), and the elementary
theta/Gamma/Jensen bounds in
[COARSE_ZERO_COUNT.md](../../heights/COARSE_ZERO_COUNT.md).
What was actually run: the existing 8,049-bracket native replay establishes
the finite premises at its explicitly imported FLINT historical complete-count
scope. This document gives a separate analytic proof; it does not treat any
Gaussian box receipt as an all-column certificate.
[check_harmonic_constants.py](check_harmonic_constants.py) checks the rational
guards and the finite bracket inequalities used here; its receipt
[harmonic_column_constants.json](harmonic_column_constants.json) explicitly
does not replay primitive zeta values or authenticate this analytic proof.
Smallest remaining gap: independent audit of this newly composed analytic
argument, followed by continuation to unbounded real part.

## 1. Statement and finite source premises

Put

\[
F(z)=\Xi(z),\quad E_\lambda(z)=F(z)-i\lambda F'(z),\quad
W_\lambda(z)=\frac{iE_\lambda(z)}{E_\lambda'(z)}.
\tag{HC1}
\]

The complete census through `R=8192`, as qualified in the native certificate,
proves that all zeros with `|Re z|<=R` are simple and real. There are exactly
8,049 positive zeros there, every bracket lies above 14, and the first bracket
lies below 15. The directed native seed is `F(0)>1/4`. The classical complete
strip is `|Im rho|<=A=1/2`. All remaining zeros, with all multiplicities,
are retained in the complete paired product. These are the premises of the
claim; a list of sign changes without the complete count would not suffice.

Under these premises,

\[
\boxed{E_\lambda(z)\ne0,\quad E_\lambda'(z)\ne0,\quad
\operatorname{Re}W_\lambda(z)>0
\quad (z=T-iy,\ |T|\le8174,\ y\ge0,\ 1\le\lambda\le10).}
\tag{HC2}
\]

The historical finite complete-count verification inside FLINT is imported,
not rerun. The elementary analytic continuation below does not strengthen
that provenance claim.

## 2. A complete uniform count for every polynomial companion

Take nested complete real even genus-zero-in-`z^2` product approximants `P_n`
of (O2)--(O3), normalized by `P_n(0)=F(0)`, and containing whole real pairs
and whole nonreal quartets. Let

\[
f_n(t)=P_n(-it),\quad f(t)=F(-it)=\xi(1/2+t),\quad
E_{n,\lambda}=P_n-i\lambda P_n'.
\tag{HC3}
\]

Every coefficient of `f_n` is nonnegative. A real pair contributes
`1+t^2/gamma^2`. A nonreal conjugate block contributes

\[
1+2\operatorname{Re}(\rho^{-2})t^2+|\rho|^{-4}t^4.
\tag{HC4}
\]

For these blocks `|Re rho|>R>A>=|Im rho|`, so
`Re(rho^(-2))>0`. Multiplicities preserve nonnegative coefficients.
Each new block has constant coefficient one, so nesting makes every
nonnegative coefficient nondecreasing. Local uniform convergence and
convergence of each fixed derivative give coefficientwise convergence to
`f`; hence, for `t>=0`,
`f_n(t)<=f(t)` and `f_n'(t)<=f'(t)`. The same coefficient signs give
`|P_n(z)|<=f_n(|z|)` and `|P_n'(z)|<=f_n'(|z|)`.

The positive theta representation writes
`f(t)=integral Phi(u) cosh(tu) du`, with `Phi(u)>0`, `u>=0`.
For `t,u>=0`,

\[
u\sinh(tu)\le \tfrac12u e^{tu}
\le\tfrac12e^{(t+1)u}\le\cosh((t+1)u),
\tag{HC5}
\]

using `u<=e^u`. Thus `f'(t)<=f(t+1)`; also `f(t)<=f(t+1)`.
For every `1<=lambda<=10` and every radius `L>=0`,

\[
\max_{|z|\le L}|E_{n,\lambda}(z)|
\le f(L)+10f'(L)\le11f(L+1).
\tag{HC6}
\]

Let `N_(n,lambda)(t)` count **all** zeros of `E_(n,lambda)` in the closed
disk `|z|<=t`, with analytic multiplicity. Since
`E_(n,lambda)(0)=F(0)>1/4`, Jensen on radius `2t`, followed by (Z3) with
`s=2t+3/2`, gives

\[
N_{n,\lambda}(t)\log2
\le\log88+(t+7/4)\log(2t+3/2).
\tag{HC7}
\]

An exceptional outer radius is handled by increasing it slightly and
passing down; no inner zero or multiplicity is discarded. For `t>=1024`,
`log t>20/3`, `log88<7`, `log(2t+3/2)<log t+3/2`, so the right side is
strictly less than

\[
\left(\frac{21}{20480}
      +\frac{4103}{4096}\frac{49}{40}\right)t\log t
=\frac{201215}{163840}t\log t
<\frac43t\log t.
\tag{HC8}
\]

Here `603645<655360` is an integer inequality. The elementary bounds
`2/3<log2<1` and `log3<3/2` are established in the cited coarse-count
proof. Since `log2>2/3`, this proves the uniform complete count

\[
N_{n,\lambda}(t)<2t\log t
\qquad(t\ge1024,\ n\ge1,\ 1\le\lambda\le10).
\tag{HC9}
\]

This counts the complete polynomial companion zero set. It is not a new
native count of the zeros of the limiting companion.

## 3. A uniform lower bound on the logarithmic-derivative harmonic function

Set

\[
C=R-A=8191.5,\quad V=R-2A=8191,\quad
q_\lambda=E_\lambda'/E_\lambda,\quad
u_\lambda(x,y)=\operatorname{Im}q_\lambda(x-iy).
\tag{HC10}
\]

Complete-census localization (L8)--(L10) proves `E_lambda` is zero-free
for `|Re z|<C`, `Im z<0`; the real-axis strict Laguerre argument proves
it is also nonzero for `|Re z|<C`, `Im z=0`. Consequently `u_lambda` is
harmonic on a neighborhood of the closed rectangle
`[-V,V] x [0,A]`. The real boundary has `u_lambda>0` by (L11)--(L12).
The outer theorem proves `u_lambda>0` for `y>A`; continuity gives
`u_lambda(x,A)>=0` in this rectangle.

The polynomial companions satisfy the same zero-free lower region
`|Re z|<C`: apply (L2)--(L3) to `P_n` and then
`Re(E_(n,lambda)/P_n)>1`. Their zeros all have imaginary part at least
`-A` by the outer polynomial companion argument. Thus every lower zero
`zeta=alpha+i beta` of a polynomial companion has

\[
-A\le\beta<0,\qquad |\alpha|\ge C.
\tag{HC11}
\]

At `z=x-iy`, `|x|<=V`, `0<y<=A`, an upper or real zero contributes a
nonnegative amount to the imaginary logarithmic derivative. A lower zero
contributes at least

\[
\frac{y+\beta}{(x-\alpha)^2+(y+\beta)^2}
\ge-\frac{A}{(x-\alpha)^2}.
\tag{HC12}
\]

For lower zeros with `|alpha|<=2V`, their modulus is less than `2V+1=16383`.
By (HC9), their total number, including multiplicity, is less than
`2*16384*14=458752`, since `log16383<14`. The separation
`|x-alpha|>=C-V=A` bounds their total negative contribution by `917504`.

For lower zeros with `|alpha|>2V`,
`|x-alpha|>|alpha|/2` and `|zeta|^2<=2alpha^2`. Their total negative
contribution is at most

\[
8A\sum_{|\zeta|>2V}\frac{m_\zeta}{|\zeta|^2}.
\tag{HC13}
\]

Partial summation with the **complete** count (HC9), dropping the negative
endpoint term, gives for `a>=1024`

\[
\sum_{|\zeta|>a}\frac{m_\zeta}{|\zeta|^2}
\le2\int_a^\infty\frac{N_{n,\lambda}(t)}{t^3}\,dt
<\frac{4(\log a+1)}a.
\tag{HC14}
\]

At `a=2V=16382`, this is less than `60/16382<1`. Hence the far negative
contribution is less than 4. Combining both parts proves
`Im(E_(n,lambda)'/E_(n,lambda))>-917508>-2^20` on the rectangle interior.
All fixed polynomial derivatives converge locally uniformly, and the
limiting companion is nonzero here. Their logarithmic derivatives converge;
continuity to the boundary therefore gives

\[
u_\lambda(x,y)\ge-M,\qquad M=2^{20},\qquad
|x|\le V,\quad0\le y\le A.
\tag{HC15}
\]

No unspecified roots were excluded from (HC13)--(HC14).

## 4. An explicit positive bound on the whole real boundary

At real `x` with `|x|<=V` away from a root, write
`q=F'/F=q_P+q_tail`, where `P` contains all 8,049 positive census roots
and their negative partners. Put `D=-q'>0`. All contributions to `D`
are positive by (L11): a nonreal tail root has real part beyond `R`,
so its distance in real part from this interval is greater than
`R-V=1>A`. In particular `D>=D_P=-q_P'`.

The finite product contains exactly 16,098 real roots. Cauchy--Schwarz
on their individual logarithmic-derivative summands gives

\[
q_P(x)^2\le16098\sum_{\alpha\in Z(P)}\frac1{(x-\alpha)^2}
=16098D_P(x)\le16098D(x).
\tag{HC16}
\]

The complete actual-source coarse count gives the remaining sum
`S_tail=sum_(Re rho>R) m_rho/|rho|^2 <28/R`, because
`logR=13log2<13`. The full paired-product derivative therefore obeys

\[
|q_{\rm tail}(x)|
\le\frac{2V S_{\rm tail}}{1-V^2/R^2}
<\frac{56VR}{R^2-V^2}<2^{18}.
\tag{HC17}
\]

The last bound is an exact rational inequality. For example
`V>3R/4` implies `R+V>7R/4`, while `R-V=1`, so the fraction is less
than `32V<32R=2^18`. Consequently

\[
q(x)^2\le2q_P(x)^2+2q_{\rm tail}(x)^2
<32196D(x)+2^{37}.
\tag{HC18}
\]

The first real pair, whose positive root is below 15, contributes at least
`2/(V+15)^2` to `D`. Since `V+15=8206<2^14`, this proves
`D>2^(-27)` everywhere under consideration. Direct algebra gives

\[
u_\lambda(x,0)=\frac{\lambda D(x)}{1+\lambda^2q(x)^2}
>\frac{D(x)}{1+2^{22}D(x)+2^{44}}
>\frac{2^{-27}}{1+2^{-5}+2^{44}}>2^{-72}=:b.
\tag{HC19}
\]

Here `1<=lambda<=10`, `100<2^7` and `32196<2^15` justify the first
strict bound. The function `D/(1+2^22 D+2^44)` is increasing for positive
`D`; the last denominator is less than `2^45`. At a simple real root,
direct substitution into `E_lambda'/E_lambda` gives `u_lambda=1/lambda`.
Thus the same strict bound holds at every root too, proving

\[
u_\lambda(x,0)>b=2^{-72}
\quad(|x|\le V,\ 1\le\lambda\le10).
\tag{HC20}
\]

The finite factor and infinite tail are both complete. This estimate does
not replace the unknown tail by zero or use a midpoint for a census root.

## 5. Harmonic measure suppresses the two distant vertical boundaries

Work in the open rectangle `(-V,V) x (0,A)`. Put
`theta=pi*y/A`, `k=pi/A=2pi`. The affine harmonic function

\[
p(x,y)=1-y/A
\tag{HC21}
\]

has value one on the whole bottom, zero on the top, and lies in `[0,1]`.

Let `h_s` be the harmonic measure of both vertical sides in the finite
rectangle: its side values are one and its top/bottom values zero. The
separated-variable expansion is

\[
h_s(x,y)=\frac4\pi
\sum_{\substack{n\ge1\\n\ {\rm odd}}}
\frac{\cosh(nkx)}{n\cosh(nkV)}\sin(n\theta).
\tag{HC22}
\]

The maximum principle gives `0<=h_s<=1`. This series converges locally
uniformly in the interior and has the stated boundary limits. For
`0<theta<pi`, `|sin(n theta)|<=n sin theta`; also
`cosh(nkx)/cosh(nkV)<=2exp(-nk(V-|x|))`. Therefore

\[
h_s(x,y)\le\frac8\pi\sin\theta\,
\frac{e^{-k(V-|x|)}}{1-e^{-2k(V-|x|)}}.
\tag{HC23}
\]

By (HC15), (HC20), and the nonnegative top value, the harmonic
comparison function
`u_lambda-b*p+(M+b)*h_s` has nonnegative boundary lower limits.
On a vertical side it is at least `-M-b*p+M+b>=0`; on the top it is
nonnegative; on the bottom it is nonnegative by the uniform bound.
At the bottom corners `u_lambda>b` continuously and `p<=1`; at the top
corners `p` tends to zero and `u_lambda` has nonnegative continuous values.
The bounded side harmonic measure is nonnegative. Thus the bounded-domain
maximum principle applies, including the finitely many boundary
discontinuities, and gives

\[
u_\lambda(x,y)\ge b\,p(x,y)-(M+b)h_s(x,y).
\tag{HC24}
\]

Use the slightly larger comparison range
`L=32697/4=8174.25`, which leaves a neighborhood around the claimed endpoints.
For `0<theta<pi`, `sin(theta)=sin(pi-theta)<=pi-theta`; hence

\[
p(x,y)=1-\theta/\pi\ge\frac{\sin\theta}{\pi}
>\tfrac14\sin\theta.
\tag{HC25}
\]

For `|x|<=L`, the denominator in (HC23) is greater than `1/2`, and
`pi>3`; hence

\[
h_s(x,y)<6e^{-2\pi(V-L)}\sin\theta.
\tag{HC26}
\]

Since `M+b<2^21`, the negative term in (HC24) is strictly less than
`2^24 exp(-2pi(V-L)) sin theta`. Its positive term is strictly greater
than `2^(-74) sin theta`. The ratio of these latter bounds is

\[
2^{-98}e^{2\pi(V-L)}
=2^{-98}e^{67\pi/2}
>2^{-98}e^{100}>2^2>1,
\tag{HC27}
\]

using the elementary bounds `3<pi<4` and `e>2` (the upper bound for pi was
used in HC25). Thus
`u_lambda(x,y)>0` for `|x|<=L`, `0<y<A`, uniformly for the entire
parameter interval `1<=lambda<=10`.

## 6. Attach the real boundary and the unbounded outer region

The real boundary is strictly positive by (L11)--(L12). At `y=A` and
`|x|<=8174`, the logarithmic derivative is harmonic across the line,
because `E_lambda` is nonzero in a neighborhood. It is nonnegative there,
strictly positive below by (HC27), and strictly positive above by the
outer theorem. A neighborhood stays inside `|x|<L`. The strong minimum
principle therefore makes its value on the line strictly positive too.
For every `y>A`, the outer theorem is already strict without restricting
`x`. This proves `u_lambda>0` on the entire claimed closed lower column.

Finally, `u_lambda>0` implies `q_lambda!=0` and

\[
\operatorname{Re}W_\lambda
=\operatorname{Re}(i/q_\lambda)
=\frac{\operatorname{Im}q_\lambda}{|q_\lambda|^2}>0.
\tag{HC28}
\]

The companion is zero-free by localization in the whole column, so both
denominators in (HC1) are defined. This proves (HC2). It composes finite
source-qualified census information with complete-tail analytic control;
no finite ladder is promoted to an unbounded real-part claim.
