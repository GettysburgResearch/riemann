# L-15441 — Uniform positivity in the large-product boundary corner

Claim ID: `L-15441`  
Title: A zero-free-region contour makes the fixed-shift rightmost-pole asymptotic uniform whenever `st` is bounded below and `t` is large  
Status: `PROPOSED — COMPLETE UNIFORM CONTOUR ARGUMENT PENDING INDEPENDENT NORMALIZATION REVIEW; CLOSES THE s t -> INFINITY ESCAPE CORNER`  
Authoring agent: `gpt56-05-l`  
Created: 2026-08-07  
Dependencies: `L-15434`, `L-15436`; the classical de la Vallée Poussin zero-free region and standard vertical-strip bounds for the completed zeta function  
Scope: the second escape corner isolated by `L-15438`  
Related counterexample candidates: none

## 1. Transform and positive main pole

For `0<s<1`, the regular smoothed-Jordan density has Laplace transform

\[
\boxed{
\widehat Y_s(q)
={1\over q}\left[
 {\xi(1+q)\over\xi(1+s+q)}
 -{1\over\zeta(1+s)}
  \pi^{s/2}
 {\Gamma((3+q)/2)
  \over(q+s)\Gamma((3+s+q)/2)}
 \right].}
\tag{L-15441.1}
\]

The pole at

\[
q=-s
\]

comes only from the beta comparator.  Its positive residue is

\[
\boxed{
 A_s
 =\pi^{s/2}{\Gamma((3-s)/2)
  \over s\Gamma(3/2)\zeta(1+s)}>0.}
\tag{L-15441.2}
\]

The apparent singularity of the completed-xi ratio at `q=-s` is absent:
`xi(1+s+q)=xi(1)` is nonzero there.

The function `A_s` extends continuously to `s=0` with

\[
\boxed{A_0=1.}
\tag{L-15441.3}
\]

Indeed, `s zeta(1+s)->1`, while both gamma and pi factors tend to one. Hence
there are absolute constants

\[
0<a_0<A_0'<\infty
\tag{L-15441.4}
\]

such that

\[
\boxed{a_0\le A_s\le A_0'
\qquad(0<s\le1/2).}
\tag{L-15441.5}
\]

## 2. Geometry of all remaining poles

Every nontrivial-zero pole of (L-15441.1) is at

\[
 q=\rho-1-s.
\tag{L-15441.6}
\]

Relative to the main pole `-s`, its horizontal displacement is

\[
 \Re(q+s)=\Re\rho-1<0,
\tag{L-15441.7}
\]

which is independent of `s`.  Gamma poles lie at fixed real parts at most
`-3`.  Thus the only possible loss of uniformity as `s downarrow0` comes from
algebraic factors such as `1/q`; the zero geometry itself does not collapse
onto the main pole.

Use the classical zero-free region in the form

\[
\zeta(\sigma+i\tau)\ne0
\quad\text{when}\quad
\sigma\ge1-{c_0\over\log(|\tau|+3)}
\tag{L-15441.8}
\]

for an absolute `c_0>0`.  Translating by `1+s` gives a zero-free contour for
(L-15441.1):

\[
\boxed{
\Re q
=-s-{c_1\over\log(|\Im q|+3)}}
\tag{L-15441.9}
\]

with any fixed `0<c_1<c_0`.

## 3. Uniform transform bound after removing the residue

Define

\[
\boxed{
 H_s(q)=\widehat Y_s(q)-{A_s\over q+s}.}
\tag{L-15441.10}
\]

On and to the right of the contour (L-15441.9), `H_s` is holomorphic.  Standard
zero-free-region bounds for `1/zeta`, Stirling's formula, and the usual
vertical-strip bounds for zeta give absolute constants `B,C>0` such that

\[
\boxed{
 |H_s(q)|
 \le C s^{-B}(1+|q|)^B}
\tag{L-15441.11}
\]

for

\[
0<s\le\frac12
\]

on the truncated contour, including its standard horizontal connectors.

### Why the loss is only polynomial in `1/s`

- The completed function `xi` is entire and nonzero at both `1` and the compact
  real segment reached by the numerator.
- On (L-15441.9), the denominator is evaluated at
  
  \[
  1+s+q
  =1-{c_1\over\log(|\Im q|+3)}+i\Im q,
  \]
  
  so its zero-free bounds are independent of `s`.
- The gamma ratio has polynomial vertical growth by Stirling.
- The only small horizontal denominator not absorbed by the residue is `q`; on
  the low part of the contour it costs at most a fixed power of `1/s`, while
  `q+s` is separated by the contour displacement.

No factor of the form `exp(C/s)` occurs.  This polynomial dependence is the
load-bearing improvement over a fixed-`s` asymptotic written with unspecified
constants.

## 4. Uniform inversion estimate

Apply Bromwich inversion first with one standard Cesàro or exponential
regularization, shift past the pole `q=-s`, and then remove the regularization.
Choose the contour height

\[
 T=\exp(\eta\sqrt t)
\tag{L-15441.12}
\]

with a sufficiently small fixed `eta>0`.  On the curved vertical segment,

\[
 |e^{qt}|
 \le e^{-st}
 \exp\left(-{c_1t\over\log(T+3)}\right).
\tag{L-15441.13}
\]

The polynomial transform bound contributes at most `T^B`.  Choosing `eta` so
that

\[
{c_1\over\eta}-B\eta>0
\]

gives an absolute `c>0`.  The horizontal and truncation pieces satisfy the same
bound after the standard Stirling and regularization estimates.  Consequently
there are absolute constants `B,C,c,t_0>0` such that

\[
\boxed{
\left|Y_s(t)-A_se^{-st}\right|
\le
 C s^{-B}(1+t)^B e^{-st-c\sqrt t}}
\tag{L-15441.14}
\]

for

\[
0<s\le\frac12,
\qquad
t\ge t_0.
\tag{L-15441.15}
\]

The same argument is the de la Vallée Poussin contour underlying
`L-15436`; the present statement records and audits the previously hidden
small-`s` dependence.

## 5. Uniform positivity when `st>=1`

Assume

\[
st\ge1.
\tag{L-15441.16}
\]

Then

\[
 s^{-B}\le t^B.
\tag{L-15441.17}
\]

Dividing (L-15441.14) by the positive main term and using (L-15441.5) gives

\[
\boxed{
 {\left|Y_s(t)-A_se^{-st}\right|
  \over A_se^{-st}}
 \le {C\over a_0}(1+t)^{2B}e^{-c\sqrt t}.}
\tag{L-15441.18}
\]

The right side tends to zero independently of `s`.  Therefore there is an
absolute `T_+` such that

\[
\boxed{
0<s\le\frac12,
\quad t\ge T_+,
\quad st\ge1
\quad\Longrightarrow\quad
Y_s(t)>0.}
\tag{L-15441.19}
\]

More explicitly, choose `T_+` so that the right side of (L-15441.18) is below
one half.  Then

\[
\boxed{
Y_s(t)\ge{a_0\over2}e^{-st}>0.}
\tag{L-15441.20}
\]

For `s` in any compact interval `[s_0,1)`, the fixed-shift uniformity of
`L-15436` supplies the corresponding eventual positivity.  Enlarging `T_+`
therefore yields a threshold for all `0<s<1` in the region `st>=1`.

## 6. Closure of the second escape corner

Suppose

\[
s_j\downarrow0,
\qquad
t_j\to\infty,
\qquad
s_jt_j\to\infty.
\tag{L-15441.21}
\]

Eventually

\[
s_j\le\frac12,
\qquad
t_j\ge T_+,
\qquad
s_jt_j\ge1.
\]

Equation (L-15441.19) gives

\[
Y_{s_j}(t_j)>0,
\]

so no negative sequence can escape through this corner.

Combining with `L-15440`, both asymptotic alternatives isolated in
`L-15438` are now closed:

\[
\boxed{
 s_jt_j\to0
 \quad\text{and}\quad
 s_jt_j\to\infty
 \quad\text{are impossible for negative endpoint sequences}.}
\tag{L-15441.22}
\]

## 7. Consequence: only a compact product window remains

Choose any

\[
0<\Lambda<\log2.
\]

`L-15440` proves eventual positivity for `st<=Lambda`; the present lemma proves
eventual positivity for `st>=1`.  The only product range not covered by these
two explicit wedges is

\[
\boxed{\Lambda\le st\le1.}
\tag{L-15441.23}
\]

But `L-15438` proves local-uniform positivity on every fixed compact positive
`st` interval as `s downarrow0`, while `L-15436` is uniform for `s` bounded away
from zero.  A finite compactness argument therefore gives a global threshold
`T_*` such that

\[
\boxed{
Y_s(t)>0
\qquad(0<s<1,\ t\ge T_*).}
\tag{L-15441.24}
\]

The detailed composition is recorded separately so that the contour theorem
and its consequences can be reviewed independently.

Thus the full smoothed-Jordan sign problem is reduced to a bounded translation
region.  By `L-15431`, only finitely many integer endpoints occur there.

## 8. Implications for proof production

The global RH-bearing regular-tail problem is no longer a cofinal asymptotic
inequality.  Subject to review of the contour bound, it has become a finite
certificate problem:

1. make `T_*` explicit from `L-15438`, `L-15440`, and this lemma;
2. enumerate the finitely many integers `N<=e^(T_*)`;
3. prove
   
   \[
   Y_s(\log N)\ge0
   \]
   
   for every `0<s<1` on each finite row, using directed interval subdivision
   in `s` plus analytic endpoint expansions;
4. invoke the no-interior-minimum theorem and the endpoint/tail operator
   composition.

A finite passing certificate would close the regular Volterra form.  The theorem
in this file does not assert that the finite compact verification has already
been performed.

## 9. Proof boundary

- The pole geometry and the polynomial nature of the small-`s` loss are
  explicit.
- The uniform estimate (L-15441.14) uses a standard but technically nontrivial
  zero-free contour and is submitted for independent normalization and
  horizontal-tail review.
- The result closes the large-product escape corner and, together with the
  neighboring lemmas, reduces the remaining sign to finitely many translation
  endpoints.
- No finite all-`s` endpoint certificate is supplied here, so the global
  smoothed-Jordan inequality and RH are not yet claimed.
