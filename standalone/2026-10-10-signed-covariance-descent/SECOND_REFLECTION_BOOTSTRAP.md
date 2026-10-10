# A shifted Gauss variable after exact cube summation

**Status:** proposed source-conditional analytic theorem. The exact
standard-face object defined below continues to a larger tube by
extracting the dominant squarefree prime factor. The cube sum is
retained throughout. A separate mean-square corollary uses the new
spectral lemma identified explicitly in Section 6. Neither assertion
is the requested fourth or generalized moment estimate.

**Authorship:** signed_series_bootstrap, with the dominant-prime
factorization suggested independently by root. Independent review is
to be recorded against the frozen content.

**Exact sources:** PR #920 mathematical source
`6aceafc1729ca0962eb12519b407b69c3b5a4d5f`, specifically
`DEFORMED_GAUSS_CONTINUATION.md`, equations (1.3), (1.5), and Lemma 2.1;
`HIGHER_ANGULAR_SECOND_MOMENT.md`, Sections 1–3; and
`POST_REFLECTION_EULER_CONTINUATION.md`, equations (3.3), (3.5), and
(4.1). These statements retain the October 5 `paper2.tex` theta
interfaces imported from OpenAI/math
`adc7f1241b42e322a6451854ab7e4b4c146bf78a`.

The finite-ray reunion proved in [FINITE_RAY_REUNION.md](FINITE_RAY_REUNION.md)
motivates the object in Section 1. Its identification with the complete
three-cusp sum additionally requires the explicit coefficient adapter
described in Section 7. The standard-face theorem does not assume that
all three cusp sequences are equal to the infinity-cusp sequence.

## 1. The exact standard-face object

Use `O=Z[omega]`, the primary-generator convention, and the fixed bad
set S of the cited sources. Let k be squarefree and prime to S and put
`Q=Nk`. All products and varying indices below omit the primes dividing
kS. Character values at these excluded primes are retained as zeros;
no power of a character is turned into one there.

Fix finite ray characters eta, rho and varrho, supported on a fixed
bad modulus, with

\[
\kappa=\eta\rho^3,
\qquad \varrho^3=\overline\rho^{\,3}
\quad\hbox{on the good primary elements.}
\tag{1.1}
\]

The second equality is an explicit hypothesis of the standard-face
theorem. It is the cube-character interface needed to apply the theorem
to a finite decomposition of the actual reflected cusp coefficients.

Put

\[
\begin{gathered}
t=1-s,\qquad u=v-s,\qquad w=v-3s+\tfrac32,\\
a_k(n)=\gamma_2(n)\overline{\alpha(n)}\varrho(n)\chi_k(n),\\
c_k(b)=\overline{\alpha(b)}^{\,3}\varrho(b)^3\chi_k(b)^3,
\qquad \chi^-_k=\eta\overline\alpha^{\,3}\chi_k^3.
\end{gathered}
\tag{1.2}
\]

For a good prime p with q=Np, define

\[
x_p=\chi^-_k(p)q^{-w},\qquad
K_p=\kappa(p)q^{1-v},\qquad
y_p=c_k(p)q^{-(3t-1/2)}.
\tag{1.3}
\]

The relation (1.1), including the square of the quadratic row value,
gives the exact identity

\[
\boxed{K_py_p=x_p.}
\tag{1.4}
\]

Define the standard-face series

\[
\begin{aligned}
\mathcal Z_k(s,v;\varrho)
={}&\frac1{L_{S,k}(w,\chi^-_k)}
\sum_{(n,kS)=1}^{*}\sum_{(b,kS)=1}
\frac{a_k(n)c_k(b)(Nb)^{1/2}}
     {(Nn)^t(Nb)^{3t}}\\
&\hspace{12mm}\cdot
\prod_{p\mid nb}\left(1+\frac{K_p}{1-x_p}\right).
\end{aligned}
\tag{1.5}
\]

The n sum is squarefree; b is unrestricted among good primary
elements. In particular n and b may have common prime factors.
Equation (1.5) is initially an absolutely convergent series, for
example on

\[
\Re v<1,\qquad \Re u>1.
\tag{1.6}
\]

Indeed t=u+1-v has real part greater than one, w has real part
greater than one, and the local divisor multiplier costs at most
`N(nb)^(1-Re(v)+epsilon)`. A sharper separate n,b majorant gives
the same assertion. The region (1.6) also lies in the original
absolute reflected domain `Re(s)<Re(v)-1`.

## 2. Summing all cubes before extracting the squarefree factor

For fixed n and a good prime p, the local b sum is

\[
\begin{cases}
\displaystyle
1+\left(1+\frac K{1-x}\right)\frac y{1-y}
=\frac1{(1-x)(1-y)},&p\nmid n,\\[7pt]
\displaystyle
\frac{1+K/(1-x)}{1-y}
=\frac{1-x+K}{(1-x)(1-y)},&p\mid n.
\end{cases}
\tag{2.1}
\]

The first equality uses Ky=x. It includes every valuation of b,
including those for which p also divides n. Multiplying (2.1) over
the good primes cancels exactly the displayed reciprocal L-function
in (1.5). Thus

\[
\boxed{
\mathcal Z_k(s,v;\varrho)
=L_{S,k}(3t-\tfrac12,c_k)
\sum_n^*\frac{a_k(n)}{(Nn)^t}
                  \prod_{p\mid n}(1-x_p+K_p).}
\tag{2.2}
\]

At a deleted prime the two original sums omit every positive
valuation, so its factor in (2.1)–(2.2) is one. This is not an
identity obtained by extending (1.4) through a nonunit.

Now extract K at every squarefree prime of n:

\[
1-x_p+K_p=K_p(1+h_p),\qquad
h_p=K_p^{-1}-y_p.
\tag{2.3}
\]

Set

\[
\widetilde a_k(n)=\kappa(n)a_k(n),
\qquad h(d)=\prod_{p\mid d}h_p\quad(d\text{ squarefree}).
\tag{2.4}
\]

Since `(Nn)^(-t) product K_p = kappa(n)(Nn)^(-u)`,
equation (2.2) becomes

\[
\mathcal Z_k(s,v;\varrho)
=L_{S,k}(3t-\tfrac12,c_k)
\sum_n^*\frac{\widetilde a_k(n)}{(Nn)^u}
                                  \prod_{p\mid n}(1+h_p).
\tag{2.5}
\]

The relevant Gauss variable is therefore u=v-s, rather than t=1-s.
This change is made only after the full cube sum in (2.1).

## 3. The exact conditioned Gauss representation

For squarefree d prime to kS put

\[
G_{k,d}(u)
=\sum_m^*\frac{\widetilde a_k(m)\chi_m(d)^4}{(Nm)^u}.
\tag{3.1}
\]

The character in (3.1) enforces `(m,d)=1`. The Gauss CRT identity
from the source gives

\[
\widetilde a_k(dm)
=\widetilde a_k(d)\widetilde a_k(m)\chi_m(d)^4
\qquad ((d,m)=1).
\tag{3.2}
\]

Expanding the finite product in (2.5) and writing n=dm now gives

\[
\boxed{
\mathcal Z_k(s,v;\varrho)
=L_{S,k}(3t-\tfrac12,c_k)
\sum_d^*\frac{\widetilde a_k(d)h(d)}{(Nd)^u}
                                      G_{k,d}(u).}
\tag{3.3}
\]

This is initially proved by absolutely convergent rearrangement on
(1.6). It preserves the moving d mask both in the inner squarefree
series and in its cube completion.

### Lemma 3.1: the available individual Gauss bound

Write a=Re(u)>1/2. On closed real strips, with a fixed positive
distance from 1/2, for every epsilon>0 one has

\[
\boxed{
|G_{k,d}(u)|
\ll Q^{\max(0,1-a)+\epsilon}
       (Nd)^{\max(0,(1-a)/2)+\epsilon}
       (2+|\Im u|)^M.}
\tag{3.4}
\]

The constants are uniform in the moving k,d. The exponent M is
finite and depends only on the strip, epsilon and fixed ray data.

When the source writes its row symbol as `chi_n(k)` rather than
`chi_k(n)`, primary sextic reciprocity supplies a fixed supplementary
ray character in n after k is split into its finitely many bad residue
classes. Absorb that character into `kappa varrho` for the application
of the source bound. Its cube is retained in (3.5), so this convention
change does not alter the completed object. The same finite partition
is used when applying the row mean in Section 6.

**Proof.** The completed series is exactly

\[
\mathcal T_{k,d}(u)
=G_{k,d}(u)
L_{S,kd}\!\left(3u-\tfrac12,
     (\kappa\varrho)^3\overline\alpha^{\,3}\chi_k^3\right).
\tag{3.5}
\]

The twist `chi_m(d)^4` contributes its twelfth power on the cube
variable, so it contributes the mask at d to this L-function. The
twist has canonical angular parameter zero and uses the minus first
horizontal derivative. At good k primes the local exponent is 1;
at d primes it is 4. Thus the exact reflected factors have moduli at
most one at k and
`q^(-1/2)|-1+q 1_(p|ell)|` at d.

The proof of PR #920's conditioned-theta Lemma 2.1 applies with
these local data: changing exponent 3 at k to exponent 1 changes
the dual character from sextic to quadratic, and changing the plus
derivative to the minus derivative changes only a unit phase.
The dual absolute majorant at `Re(u)=-eta` gives
`Q^(1+2eta)(Nd)^(1/2+2eta+epsilon)`. Interpolation with the
absolute defining line to the right of one gives
`Q^(1-a+epsilon)(Nd)^((1-a)/2+epsilon)` for 0<=a<=1.
To the right of one use the absolute defining series.

For a>1/2 the L-function in (3.5) is in its absolute Euler
half-plane, since `3a-1/2>1`. Its reciprocal is bounded uniformly
even with the moving k,d omissions: the product of the absolute
values of its reciprocal local factors is at most
`product_p(1+(Np)^(-3a+1/2))`. Thus division in (3.5) introduces
no extra conductor power or zero-free assumption. The fixed-strip
vertical bounds follow from the same Mellin and interpolation
argument. This proves (3.4). QED.

## 4. A new normally convergent tube

### Theorem 4.1

The series (1.5) has a holomorphic continuation to the connected
tube

\[
\boxed{
\mathfrak N=\{(s,v):
  \Re(v-s)>\tfrac12,\quad \Re v<1,\quad
  \Re v-3\Re s>1\}.}
\tag{4.1}
\]

On every closed real subregion with bounded real coordinates and
strict margins in (4.1),

\[
|\mathcal Z_k(s,v;\varrho)|
\ll Q^{\max(0,1-\Re(v-s))+\epsilon}
          (2+|\Im s|+|\Im v|)^M.
\tag{4.2}
\]

The representation is the normally convergent d sum (3.3).

**Proof.** Put a=Re(u), tau=Re(v), and delta=1-tau>0. Conditions
(4.1) say a>1/2, tau<1, and `3a-2tau>1`. They imply
`Re(s)=tau-a<0` and `Re(w)=3a-2tau+3/2>5/2`.
Also `Re(t)=a+delta>1`: for a<1, the last inequality in (4.1)
gives `a-tau>(1-a)/2>0`, and for a>=1 use tau<1.

From (2.3),

\[
|h_p|\le q^{-\delta}+q^{-3\Re(t)+1/2}
\ll q^{-\delta},
\qquad
|h(d)|\ll_\epsilon (Nd)^{-\delta+\epsilon}.
\tag{4.3}
\]

The second term is smaller than the first because
`3Re(t)-1/2-delta=3a+2delta-1/2>1`.
The squarefree product in (4.3) uses the usual fixed-small-prime
argument. It is uniform in the imaginary parts.

For 1/2<a<1, Lemma 3.1 bounds a d summand by

\[
Q^{1-a+\epsilon}(2+|\Im u|)^M
(Nd)^{-a-\delta+(1-a)/2+2\epsilon}.
\tag{4.4}
\]

The ideal norm sum converges when

\[
\tfrac32a+\delta>\tfrac32,
\quad\hbox{equivalently}\quad 3a-2\tau>1.
\tag{4.5}
\]

Choose epsilon smaller than the strict margin. For a>=1 the
corresponding condition is `a+delta>1`, already true. A small
neighborhood of a=1 is treated using the uniform strip bound in
Lemma 3.1 and the same positive margin.

The remaining cube L-function in (3.3) is in its absolute
half-plane, because Re(t)>1. It has a uniform Euler bound,
including the row mask. Hence (3.3) converges locally normally,
is holomorphic, and obeys (4.2). The domain (4.1) is an intersection
of open real half-spaces and contains the initial region (1.6).
The equality there proves continuation of the same function. QED.

For `1/4<Re(v)<1`, the effective upper boundary is

\[
\boxed{\Re(s)<\frac{\Re(v)-1}{3}.}
\tag{4.6}
\]

This is strictly to the right of the old absolute dual-theta
condition `Re(s)<Re(v)-1`. For example `(s,v)=(-1/20,9/10)`
lies inside (4.1), whereas the old condition would require
`Re(s)<-1/10`.

## 5. Why simply repeating the same theta reflection is different

The previous section changes the Gauss variable after the complete
cube summation. It should be distinguished from applying the same
theta involution twice to the unsummed divisor projection.

At a good prime let delta_p(m)=1_(p|m). Its normalized finite
Fourier coefficient is 1/q at every additive frequency. Equivalently
`delta_p=1-chi_p^0`, where the source defines chi_p^0 as the unit
indicator, not as the constant function one.

Under reflection, the zero additive frequency therefore carries
coefficient 1/q. At nonzero additive frequencies the source's active
exponent-zero calculation gives an exponent-four character, a fixed
unit phase, and norm factor `q^(1/2-2t)` in the t-variable.
The minus sign relative to the unit-indicator calculation is retained.

The unsummed post-reflection local factor is

\[
A_p+B_p\delta_p(m),\qquad
A_p=1-\frac{u_p}{D_p},\quad B_p=\frac{q u_p}{D_p},
\tag{5.1}
\]

with `u_p=zeta(p)q^(-v)` and `D_p=1-x_p+z_p` as in PR #920.
Its inactive coefficient after another reflection is exactly

\[
\boxed{A_p+B_p/q=1.}
\tag{5.2}
\]

The active coefficient has norm power

\[
q^{3/2-2t-v}=q^{1-w-s},\qquad t=1-s,
\tag{5.3}
\]

and the same D_p denominator. This is precisely the norm power of
the original conditioned divisor coefficient. The exact Gauss and
angular phases are restored by the same finite transform and theta
involution; (5.2) already shows that it is not a new independent
reflection on the divisor variable. An inferred second Weyl
reflection cannot be justified merely by renaming this operation.

The useful operation in Sections 2–4 is instead the identity
`1-x+K=K(1+K^(-1)-y)` after Ky=x has cancelled the full cube
denominator. That is what replaces t by u=v-s.

## 6. Mean-square consequence of a spectral Gauss bound

This section is an implication from an explicitly separate analytic
input. For a real a0<1 suppose that, for every fixed a>a0 and every
squarefree d, the literal family (3.1) satisfies

\[
\boxed{
\left(\sum_{k\sim Q}^{*}|G_{k,d}(u)|^2\right)^{1/2}
\ll Q^{1/2+\epsilon}(Nd)^{(1-a)/2+\epsilon}
                (2+|\Im u|)^M,
\qquad a=\Re u<1.}
\tag{6.1}
\]

The norm sum includes the exact `(k,d)=1` zeros, or equivalently
restricts to that set. All constants must be uniform in Q,d and in
the finite ray characters used. A fixed-row constant does not
constitute (6.1).

### Proposition 6.1

Assuming (6.1), the new chamber with a0<Re(u)<1 satisfies

\[
\boxed{
\left(\sum_{k\sim Q}^{*}
|\mathcal Z_k(s,v;\varrho)|^2\right)^{1/2}
\ll Q^{1/2+\epsilon}
(2+|\Im s|+|\Im v|)^M.}
\tag{6.2}
\]

**Proof.** Apply Minkowski to the normally convergent d sum (3.3).
The k-dependent coefficient tilde-a_k(d) is a contraction, and
(4.3) is uniform in k. The exterior cube L-function is uniformly
bounded in k. For a given d the required norm is therefore at most

\[
Q^{1/2+\epsilon}(2+|\Im u|)^M
(Nd)^{-a-\delta+(1-a)/2+2\epsilon}.
\]

The same strict inequality (4.5) makes this summable. This proves
(6.2), initially for finite d sums and then for their norm limit.
No independence between the row and divisor coefficients is assumed.
QED.

The companion [SPECTRAL_ROW_MEAN.md](SPECTRAL_ROW_MEAN.md) supplies
(6.1) for a0=5/8. Its proof and independent review are separate
from the algebra and deterministic continuation above.

The balanced Mellin scalar after removing the reflected row
conductor is `D^(v-2s)`. In the new variable this exponent is

\[
\Re(v-2s)=2a-\tau.
\tag{6.3}
\]

The chamber says `tau<(3a-1)/2`. Thus the infimum allowed by
(6.1) and this proof is

\[
\inf(2a-\tau)=\frac{1+a_0}{2}.
\tag{6.4}
\]

For a0=5/8 this is 13/16, approached from above at

\[
u\longrightarrow\tfrac58^+,
\qquad v\longrightarrow\tfrac7{16},
\qquad s\longrightarrow-\tfrac3{16}.
\tag{6.5}
\]

The inequalities are strict; no endpoint assertion is made. The
limiting s is also to the right of the first standalone
first-derivative kernel pole at s=-1/3.

An actual completed covariance bound must retain its original
normalization, outer coefficients, row ranges, smooth transforms,
and all finite-ray components before using (6.2)–(6.5). The power
13/16 is a balanced scalar exponent for this analytic argument,
not a zeta zero-free exponent or a proved generalized moment.

## 7. Interface with the full reflected object

The exact finite-ray reunion produces a sum of three cusp
coefficient sequences with the divisor multiplier in (1.5). To
apply Theorem 4.1 to the complete function, a sufficient exact
adapter is the following: in each allowed unit/ramified sector,
after the fixed Fourier rays are reunited, the good-part coefficient
is a finite sum of terms

\[
C_{j,\varrho}(k)\sqrt{Nb}\,
\gamma_2(n)\varrho(n)\varrho(b)^3,
\qquad \varrho^3=\overline\rho^{\,3}.
\tag{7.1}
\]

The row factors `chi_k(n)chi_k(b)^3` and angular factors in (1.2)
are outside (7.1). Fixed supplementary cubic characters may be
absorbed into varrho because their cubes are one. The constants,
finite character family, exact masks, and ramified summation bound
must all be supplied by the adapter.

The primary formulas for this task are Dunn–Radziwill,
*Bias in cubic Gauss sums: Patterson's conjecture*,
[arXiv:2109.07463v3](https://arxiv.org/pdf/2109.07463v3), equations
(5.7), (5.13), (5.14), and Appendix A. Their cusp representatives
gamma_10 and gamma_19 are exactly the two nonstandard representatives
used here. Those formulas express their coefficients through
tau_1 and tau_2 and fixed additive phases. The explicit coefficient
adapter is supplied in
[ALL_CUSP_COEFFICIENT_ADAPTER.md](ALL_CUSP_COEFFICIENT_ADAPTER.md),
and the cubic homogeneity of the reunited finite transform is
supplied in [FINITE_RAY_REUNION.md](FINITE_RAY_REUNION.md).
The separate proof of the cube covariance is
[FINITE_CUBE_HOMOGENEITY.md](FINITE_CUBE_HOMOGENEITY.md).

Only after (7.1) is proved may the standard-face bound be summed
over those components. Merely using the old absolute support bound
for d_+ and d_- would not justify replacing them by (3.1).

## 8. Compare the resulting bound for the actual physical completion

Suppose the all-cusp contour composition has been performed with
the original normalization of the physical balanced completion
`mathcal C_(D,D)`. Equations (6.2)–(6.5) then supply the candidate
bound, for squarefree rows,

\[
\sum_{k\sim Q}^{*}|\mathcal C_{D,D}(k)|^2
\ll QD^{13/8+\epsilon}.
\tag{8.1}
\]

The composition, including its original smooth Mellin factors, is
separate from Theorem 4.1. The comparison in this section concerns
the size (8.1) even when that composition is available.

Two existing estimates for the same complete object are

\[
\begin{split}
\sum_{k\sim Q}^{*}|\mathcal C_{D,D}(k)|^2
&\ll D^\epsilon\bigl[Q+D^2+(QD^2)^{2/3}\bigr],\\
\sum_{k\sim Q}^{*}|\mathcal C_{D,D}(k)|^2
&\ll D^\epsilon D(Q+Q^2).
\end{split}
\tag{8.2}
\]

The first is proved by the direct physical product-polynomial
expansion and the squarefree sextic sieve, with its full cubes;
see Section 4 of
[SUPPORT_PRUNED_COVARIANCE.md](SUPPORT_PRUNED_COVARIANCE.md).
The second is the inherited factorwise use of the completed theta
mean square, recorded in PR #915's coupled-completion note.

Put Q=D^h, h>=0, to compare powers. The first expression in (8.2)
has exponent

| Row exponent h | Classical physical exponent |
|---|---|
| 0<=h<=1 | 2 |
| 1<=h<=4 | (2h+4)/3 |
| h>=4 | h |

The new expression has exponent `h+13/8`. It is smaller than
the classical expression only for `h<3/8`. In that range the
factorwise exponent `1+2h` is already smaller; the new expression
would beat that factorwise exponent only for `h>5/8`.

This also follows without a power parametrization. If
`Q<=D^(5/8)`, then `D(Q+Q^2) <= 2QD^(13/8)`.
If `Q>=D^(3/8)`, each of the three classical terms is at most
`QD^(13/8)`, since

\[
D^2\le QD^{13/8},\qquad
\frac{(QD^2)^{2/3}}{QD^{13/8}}
=Q^{-1/3}D^{-7/24}\le1.
\tag{8.3}
\]

These two ranges cover every Q>=1, D>=1. Consequently (8.1)
does not improve the available minimum of the two bounds in
(8.2), at any row scale in powers of D. The new all-cusp
support-pruned estimate can only make that minimum smaller.

The new analytic domain and the conductor mean are useful distinct
theorems. The favorable scalar exponent 13/16 is not, by itself,
a new physical covariance range or a step to the fourth moment
required for the boundary 17/24.
