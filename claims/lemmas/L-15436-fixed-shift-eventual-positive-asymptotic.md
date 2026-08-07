# L-15436 — Fixed-shift regular density has a positive rightmost-pole asymptotic

Claim ID: `L-15436`  
Title: For every fixed `0<s<1`, the completed smoothed-Jordan density is eventually positive and asymptotic to an explicit positive multiple of `e^{-st}`  
Status: `PROPOSED — COMPLETE CONTOUR/Tauberian CONSEQUENCE OF THE CLASSICAL ZERO-FREE LINE`  
Authoring agent: `gpt56-05-l`  
Created: 2026-08-07  
Dependencies: `L-15434`; the classical zero-free theorem `zeta(z) != 0` on `Re z=1`; a standard de la Vallée Poussin contour or equivalent effective PNT remainder  
Scope: fixed `s`, and uniformly on compact subintervals of `(0,1)`; no uniform claim as `s downarrow 0`  
Related counterexample candidates: none

## 1. Transform and candidate main pole

Recall from `L-15434` that

\[
\widehat Y_s(q)
={1\over q}\left[
 {\xi(1+q)\over\xi(1+s+q)}
 -{1\over\zeta(1+s)}
  \pi^{s/2}
 {\Gamma((3+q)/2)
  \over(q+s)\Gamma((3+s+q)/2)}
 \right].
\tag{L-15436.1}
\]

At

\[
q=-s,
\tag{L-15436.2}
\]

the completed-xi ratio is regular:

\[
{1\over q}{\xi(1+q)\over\xi(1+s+q)}
\Big|_{q=-s}
=-{1\over s}{\xi(1-s)\over\xi(1)}.
\tag{L-15436.3}
\]

The beta comparator has a simple pole.  Its contribution to the residue of
`widehat Y_s` is

\[
\boxed{
A_s
={\pi^{s/2}\Gamma((3-s)/2)
  \over
  s\Gamma(3/2)\zeta(1+s)}>0.}
\tag{L-15436.4}
\]

Thus `q=-s` is a positive candidate rightmost pole.

## 2. Every nontrivial-zero pole lies strictly to the left

The remaining nonarchimedean poles in (L-15436.1) arise from zeros `rho` of
`xi(1+s+q)`, namely

\[
q=\rho-1-s.
\tag{L-15436.5}
\]

Every nontrivial zero satisfies

\[
0<\operatorname{Re}\rho<1.
\tag{L-15436.6}
\]

Consequently

\[
\boxed{
\operatorname{Re}(\rho-1-s)<-s.}
\tag{L-15436.7}
\]

The gamma poles are at `q=-3-2k`, also strictly to the left of `-s` for
`0<s<1`.  Hence `q=-s` is the unique finite singularity with maximal real part.

The inequality is strict for each zero but not separated by one uniform
constant, because zeros may approach the line `Re rho=1` at increasing height.
The classical zero-free region supplies the contour separation needed below.

## 3. Asymptotic theorem

For every fixed `0<s<1`,

\[
\boxed{
Y_s(t)=A_s e^{-st}+o_s(e^{-st})
\qquad(t\to\infty).}
\tag{L-15436.8}
\]

More quantitatively, the standard de la Vallée Poussin zero-free region and
Stirling bounds give constants `c_s,C_s>0` such that one may take

\[
\boxed{
Y_s(t)
=A_s e^{-st}
+O_s\!\left(e^{-st-c_s\sqrt t}(1+t)^{C_s}\right).}
\tag{L-15436.9}
\]

The constants can be chosen uniformly for

\[
s\in[s_0,s_1]
\tag{L-15436.10}
\]

whenever

\[
0<s_0<s_1<1.
\]

### Proof outline

Begin with Bromwich inversion on `Re q=b>0`, first after one harmless
exponential or Cesaro regularization.  Shift the contour toward `Re q=-s`.
Equation (L-15436.4) supplies the residue.

For `|Im q|=T`, choose the usual zero-free contour on which

\[
\operatorname{Re}(1+s+q)
\ge
1-{c\over\log(T+3)}.
\tag{L-15436.11}
\]

The classical zero-free theorem bounds the reciprocal zeta factor there by a
power of `log(T+3)`.  Stirling's formula gives

\[
{\Gamma((3+q)/2)\over\Gamma((3+s+q)/2)}
\ll_s (1+|q|)^{-s/2}.
\tag{L-15436.12}
\]

Standard convexity bounds control the numerator zeta/xi factor.  The shifted
vertical integral is therefore bounded by

\[
e^{-st}
\exp\!\left(-{ct\over\log(T+3)}\right)
(1+T)^{O_s(1)},
\tag{L-15436.13}
\]

while the truncated horizontal and inversion tails are controlled by the same
gamma smoothing.  Taking

\[
\log T\asymp\sqrt t
\tag{L-15436.14}
\]

gives (L-15436.9).  Compact `s`-uniformity follows because all gamma and
numerator-strip constants are uniform away from `s=0` and `s=1`.

Equivalently, one may apply the same zero-free contour to the Mellin transform
of the beta-smoothed summatory function.  The smoothing in `n_s` is precisely
what makes the rightmost-pole extraction proof-facing.

## 4. Eventual positivity

Since `A_s>0`, (L-15436.8) gives

\[
\boxed{
\exists T_s<\infty:
\qquad
Y_s(t)>0
\quad(t\ge T_s).}
\tag{L-15436.15}
\]

Uniformly on every compact `s`-interval as in (L-15436.10), there is one
`T_(s0,s1)` such that

\[
\boxed{
Y_s(t)>0
\quad
(s_0\le s\le s_1,\ t\ge T_{s_0,s_1}).}
\tag{L-15436.16}
\]

By the no-interior-minimum theorem `L-15431`, the same conclusion can be checked
on integer endpoints:

\[
Y_s(\log N)>0
\]

for every sufficiently large `N`, at each fixed `s`.

## 5. Where a counterexample would have to escape

Suppose a sequence satisfies

\[
Y_{s_j}(t_j)<0,
\qquad t_j\to\infty.
\tag{L-15436.17}
\]

Then (L-15436.16) forces

\[
\boxed{s_j\to0.}
\tag{L-15436.18}
\]

Thus the full two-parameter sign problem does **not** contain an independent
large-translation obstruction at any fixed horizontal shift.  Every possible
failure is pushed into the singular boundary layer

\[
s\downarrow0,
\qquad
t\to\infty.
\tag{L-15436.19}
\]

This is a global structural reduction, not a finite numerical statement.  It
also explains the observed asymptotic

\[
Y_s(\log N)\sim A_sN^{-s}.
\tag{L-15436.20}
\]

## 6. Proof boundary

- The pole location and coefficient are exact.
- Eventual positivity uses only the classical zero-free line/region, not RH.
- The quantitative error is a standard contour consequence and should be
  independently checked with the repository's exact completed-xi
  normalization before promotion from `PROPOSED`.
- No bound uniform as `s downarrow0` is claimed.
- The remaining RH-bearing regime is the joint singular limit
  `s downarrow0`, `t to infinity`; this lemma does not close that boundary
  layer or prove RH.
