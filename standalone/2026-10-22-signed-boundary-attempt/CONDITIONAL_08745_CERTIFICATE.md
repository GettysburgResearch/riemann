# An exact conditional scalar certificate for 0.8745

22 October 2026. **Status: proved scalar implication under an unproved
high-conductor moment hypothesis and the inherited analytic interfaces.**

The rational scalar target is

\[
                         B_{\rm target}=\frac{1749}{2000}=0.8745.
\]

This is **not an achieved zero-free boundary**. The high-conductor
hypothesis `HC(1/100,2/25)` in `RADICAL_STRATIFICATION.md` remains
unproved. This note supplies a complete finite scalar consumer of its
improved inverse exponent, subject to the matching-field qualification
below. It strengthens the earlier infinitesimal sensitivity calculation
to one explicit positive value of the inverse-range gain.

## 1. Inputs, conclusion, and family scope

The frozen repository input is commit
`64cb43c038d1828a478cb97cbc32e435e111d2d2`, especially
`scalar/TANGENT_CERTIFICATE.md` and
`mixed/CONDITIONAL_BOUNDARY_SENSITIVITY.md`. The primary comparison
formulas are Liu, [arXiv:2610.26835v1](https://arxiv.org/html/2610.26835v1),
(13.16), (14.3), (14.8), Remark 14.1, Proposition 14.6 and Lemma 14.7,
printed pages 101--102 and 107--116. The upstream analytic estimates are
retained as source-dependent inputs.

The scalar premise is that the common bound `beta<=7/8` and all source
detector, moment, numerator, contour, and continuation interfaces hold in
one matching family, with the improved full inverse exponent

\[
 e_{\rm new}(r)=\max\left\{1,\frac16+\frac{33}{40}r\right\}.
 \tag{1}
\]

**Conditional scalar implication.** Replacing the old inverse exponent
by (1), and making no other analytic improvement, permits the explicit
source comparison step with endpoint `1749/2000`. All endpoint and side
inequalities have strict rational margins on their continuous domains.

The radical-stratification note deduces (1) from
`HC(1/100,2/25)` over the Eisenstein field `E=Q(sqrt(-3))`, with its
full support, natural zeros, growing punctures, and specified
fixed-seminorm uniformity. For a family-wide conclusion its hypothesis
must cover every fixed coefficient ray character and finite sector used
by the comparison; one unrelated character would not suffice.

The analytic families must be matched explicitly. Liu's Section 14
comparison is assembled over a fixed cyclotomic field `F` containing
`mu_12`, whereas the original radical-stratification note is over `E`.
The scalar formulas are field independent; this does not identify the
two analytic families. Two separate notes in this packet supply the
relevant interfaces:

- `MATCHING_FIELD_RADICAL_REDUCTION.md` proves the low-conductor and
  amplification reduction in Liu's exterior-ideal and finite-unit
  conventions. Its conclusion requires the corresponding unproved
  `HC_F`, not merely `HC(E)`.
- `EISENSTEIN_CONDITIONAL_ASSEMBLY.md` checks the direct Eisenstein
  assembly in Xu--Sang, arXiv:2610.15291v2, including its generic
  row-count numerator input, endpoint conditions and continuation.
  With that source's stated analytic inputs and `HC(E)` retained,
  it supplies the conditional Eisenstein and Dirichlet conclusion.

This note proves the finite conditional **scalar target**. Combining it
with the appropriate matched assembly gives the corresponding conditional
family theorem; no `HC` premise or unconditional zero-free improvement
is supplied by the scalar algebra. No all-field conclusion is inferred
from a hypothesis over just `E` or one cyclotomic field.

## 2. Rational parameters

Take

\[
 \kappa=\frac34,\qquad \ell=\frac{253}{1500},\qquad
 b=\frac7{100},\qquad \eta=\frac1{100},\qquad
 \nu_0=\frac56\eta=\frac1{120}.
 \tag{2}
\]

The source parameters become

\[
 \begin{gathered}
 l_x=\frac{571}{1500},\qquad l_y=\frac{169}{375},\qquad
 h=\frac{197}{250},\qquad c_\kappa=\frac49,\\
 C_0=-\frac14+\frac b6+\frac{5\ell}{4}=-\frac{11}{400},\qquad
 V=\ell+c_\kappa(h/4-l_y/2)=\frac{2107}{13500},\\
 B(\ell)=\frac{11}{12}-\frac\ell4=\frac{1749}{2000}.
 \end{gathered}
 \tag{3}
\]

We use the already available boundary `7/8`, hence the fixed
`kappa=3/4`, throughout. No self-consistency root or limiting iteration
is needed for this conditional step.

## 3. The new detector count, including its flat part

Put

\[
 D=3-\frac{17}{9}x,\quad
 P=(2-\tfrac89x)(1-x),\quad
 q=\frac{\delta P}{D},\quad L=\frac56-\delta,
 \qquad 0\le x\le\frac12.
\]

The unchanged short count and the sloping part of the new long count are

\[
 R_{\rm short}(t)=1-\delta+q(3/2-t),\qquad
 R_{\rm long}(t)=\frac16+(L-\nu_0)t.
\]

Their exact intersection is

\[
 \begin{split}
 t_\eta&=\frac{L+3q/2}{L+q-\nu_0},\\
 R_\eta&=1-\delta+
           \frac{q(L-3\nu_0)}{2(L+q-\nu_0)},\\
 J_\eta&=(L-\nu_0)D+\delta P.
 \end{split}
 \tag{4}
\]

We use (4) only on

\[
                     \frac18\le\delta\le\frac45.
 \tag{5}
\]

This is a licensed continuous domain, not an extrapolation from the old
critical point. Here `D>=37/18`, `P>=7/9`, and `q>0`.
Moreover

\[
 L-\nu_0\ge\frac1{40}>0,\qquad
 L-3\nu_0\ge\frac1{120}>0.
 \tag{6}
\]

Thus the intersection denominator and the long-count slope are positive,
`t_eta<3/2`, and `R_eta>1-delta`.

The flat part in (1) ends at `r=100/99`. It cannot be omitted. Directly,

\[
 (1-\eta)(L+3q/2)-(L+q-\nu_0)
       =\eta\delta+(1/2-3\eta/2)q
       =\frac\delta{100}+\frac{97q}{200}>0.
 \tag{7}
\]

Consequently `t_eta>100/99`. For `1<=r<=100/99`, the inverse
count is `1-delta r<=1-delta<R_eta`. For
`100/99<=r<=t_eta`, its sloping exponent is increasing by (6),
and its endpoint is precisely `R_eta`. The endpoint strip
`1-epsilon_c<=r<1`, or the strip where the other detector length is
near one-half, is covered by the old `1-delta` bounds with their
arbitrarily small losses. Interior short scales use the unchanged M1/M2
crossing, not that endpoint-strip bound.

The short-detector crossing retains `1<t_eta<3/2`. The actual formulas
from Section 13.4, printed page 101, specialize at `kappa=3/4` to

\[
 r_* = \frac{(2-8x/9)t-5x/9}{D},\qquad
 m_* = t-r_* = \frac{(1-x)t+5x/9}{D}.
 \tag{7a}
\]

Both increase in `t`. At `t=3/2` they equal `1` and `1/2`.
At `t=1`, their derivatives in `x` are `-5/(9D^2)` and
`5/(9D^2)`, respectively. Hence throughout `1<=t<=3/2` they
obey `23/37<=r_*<=1` and `1/3<=m_*<=1/2`. The required prime lengths obey
`z_M<=(1-r_*)/2<=7/37<1/5` and
`z_S<=(1-2m_*)/(6kappa)<=2/27<1/5`; also
`2r_*-1>=9/37>0`. Thus the source capacities and their strict
length margins remain available; the short M1/M2 argument has not been
changed. Relative to the old count `R_0`,

\[
 R_0-R_\eta=
 \frac{\nu_0q(2L+3q)}{2(L+q)(L+q-\nu_0)}>0.
 \tag{8}
\]

Together with `2D-3P=2x(2+c_kappa-3c_kappa x)>=0`, this gives

\[
                1-\delta<R_\eta<R_0\le1-2\delta/3.
 \tag{9}
\]

The inherited numerator-supply conditions are therefore preserved. The
row-scale monotonicity also persists: `R_eta>=1-delta>=1/6` on
(5), so the same positive lower slope from Lemma 14.5 is available.

## 4. One polynomial identity proves the whole new endpoint rectangle

The modified endpoint is

\[
 E_\eta=C_0+\frac\delta2+\delta xV
                         -\frac{3h}{4}(1-R_\eta).
 \tag{10}
\]

Let `y=1/2-x`. Then

\[
 D=\frac{37}{18}+\frac{17}{9}y,\qquad
 P=\frac79+2y+\frac89y^2.
\]

Direct coefficientwise rational arithmetic gives

\[
              -2J_\eta E_\eta=A(y)\delta^2+B(y)\delta+C(y),
 \tag{11}
\]

where

\[
\begin{split}
A(y)&=\frac{103649}{243000}+\frac{15917}{20250}y
             +\frac{11807}{20250}y^2+\frac{8428}{30375}y^3,\\
B(y)&=-\frac{1289117}{3240000}-\frac{61493}{162000}y
             +\frac{89647}{810000}y^2,\\
C(y)&=\frac{4477}{48000}+\frac{2057}{24000}y.
\end{split}
\tag{12}
\]

All coefficients of `A` are positive. More decisively, all coefficients
of its discriminant complement are positive:

\[
\begin{split}
4AC-B^2={}&\frac{8709023111}{10497600000000}
 +\frac{36066648779}{262440000000}y
 +\frac{188515131683}{437400000000}y^2\\
 &+\frac{25419430511}{65610000000}y^3
 +\frac{54374440991}{656100000000}y^4.
\end{split}
\tag{13}
\]

The identity

\[
 4A(A\delta^2+B\delta+C)=(2A\delta+B)^2+(4AC-B^2)
 \tag{14}
\]

now proves positivity for every real `delta` and every `y>=0`.
There is no sampling in either variable. On the actual interval
`0<=y<=1/2`, positivity of the coefficients and `A(1/2)=1` imply
`A<=1`. Also `P<=2D/3<D` and `D<=3`, so

\[
 0<J_\eta=(5/6-\nu_0)D+\delta(P-D)\le\frac{99}{40}.
\]

Equations (11)--(14) therefore give the explicit uniform bound

\[
 -E_\eta\ge\frac{8709023111}{207852480000000}
                      >\frac1{25000}
 \qquad\left(\frac18\le\delta\le\frac45,
                         \ 0\le x\le\frac12\right).
 \tag{15}
\]

## 5. The high-delta branch, small classes, and all side conditions

Use the original count on `3/4<=delta<=5/6`. This overlaps (5),
so buffered detector partitions can use either estimate in a genuine
open overlap. If a single Lipschitz count is preferred, interpolate
between the two upper exponents within the overlap; the endpoint is
affine in the count and both endpoint bounds are strict there.

Let `J_0` and `E_0` be the source expressions, and put
`z=delta-3/4`. The exact old numerator becomes

\[
 -2J_0 E_0=A(y)z^2+L_1(y)z+L_0(y),
 \tag{16}
\]

with the same positive `A` as in (12), and

\[
\begin{split}
L_1(y)&=\frac{336631}{1458000}+\frac{565453}{729000}y
       +\frac{178067}{182250}y^2+\frac{4214}{10125}y^3,\\
L_0(y)&=\frac{106721}{3888000}+\frac{54961}{243000}y
       +\frac{393479}{972000}y^2+\frac{2107}{13500}y^3.
\end{split}
\tag{17}
\]

Every coefficient is positive. Since `0<J_0<=5/2`, this proves

\[
                    -E_0\ge\frac{106721}{19440000}
                               >\frac1{25000}
 \tag{18}
\]

on the entire old high-delta branch. In the actual comparison from
`beta<=7/8`, Proposition 14.6 only needs bins with `delta<=3/4`;
(16)--(18) also certify the larger formal source rectangle without using
the improved inverse branch beyond its licensed range.

For `0<delta<1/8`, retain the old small-delta estimate. The floor,
small rows, far rows, and principal rows are also treated by the source
estimates. Every strict side condition in Remark 14.1 is verified below.
The right column is the exact positive margin by which the required
inequality holds.

| Requirement | Positive margin |
|---|---:|
| `b>0` | `7/100` |
| `ell>1/6` | `1/500` |
| `ell<1/5` | `47/1500` |
| `kappa>7497/10000` | `3/10000` |
| `B>437/500` | `1/2000` |
| `lx>ell` | `53/250` |
| `ly-ell>11b/6` | `461/3000` |
| `6 kappa ell>3/4` | `9/1000` |
| `ell/h<1/(6 kappa)` | `29/3546` |
| `ell/h>21/100` | `239/59100` |
| `ly>h/2` | `17/300` |
| `ly<1/2` | `37/750` |
| `C0<-1/250` | `47/2000` |
| `C0+Asm/8<-1/250` | `13231/28368000` |
| `C0+(1/2+3ell/2)/50<-1/100` | `61/25000` |
| `13h/75-ly/2+1/50<-1/20` | `703/37500` |

Here `Asm` is exactly the quantity in Remark 14.1. The allowed upper
endpoint `kappa=3/4` is an equality, as in the inherited `7/8` step.

For example choose `r0=1/25000` and the row-extension buffer
`zeta=1/10^7`. Then
`2 zeta<min(r0/2,1/1000)` and `ell/(h+zeta)>21/100` hold exactly.
Thus a positive fixed allowance remains for all subsequent small
discretization and analytic losses. No asymptotic assertion in the
parameter `eta` is used.

## 6. Closing the conditional comparison

The full scalar domain is now covered:

- `0<delta<1/8`: the old small-delta endpoint with the strict margins
  above;
- `1/8<=delta<=4/5`: the new detector count (4), including the flat
  inverse branch, and the uniform bound (15);
- `3/4<=delta<=5/6`: the original count and (18);
- the source floor, small-row, far-row, and principal regimes: their
  unchanged estimates with the listed side margins.

The numerator resource is unchanged. Equations (8)--(9) preserve its
required row-count and length bounds. The source row-scale monotonicity
and contour assembly therefore retain a strict positive saving, provided
the analytic hypotheses stated in Section 1 are supplied. The
continuation in Lemma 14.7 then gives the conditional target in (3).

The target is strictly below the inherited limiting bracket:

\[
 \frac{1749}{2000}
  <\frac{1+749773294079928/10^{15}}2<B_\flat.
\]

The gap from the inherited numerical boundary is about `0.000386647`.
This is the impact of the **unproved** `HC` input, not an attained
improvement. As a negative control, the old endpoint at these same
rational parameters and `delta=47/100,x=1/2` is

\[
             E_0=\frac{27399077}{16218900000}>0.
 \tag{19}
\]

Thus the certificate really uses the new inverse estimate; it does not
relabel an improvement already supplied by the old envelope.

## 7. Reproduction and verification scope

Run

```sh
python -I -S -B verify_conditional_08745.py
```

The standard-library checker constructs (11) from the primitive endpoint
formula, verifies all polynomial identities and positive coefficients,
checks the licensed range and flat cutoff identities, checks every side
margin, and records (19). Its output is
`CONDITIONAL_08745_CHECKS.json`. All acceptance values are exact rational
numbers; optimization, plots, floating-point values, and finite grids
play no part in acceptance.

The checker does not prove the high-conductor raw inverse moment, the
upstream analytic estimates, or a zero-free theorem. Those distinctions
are retained explicitly in its machine-readable output.
