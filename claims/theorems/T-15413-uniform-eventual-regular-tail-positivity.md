# T-15413 — Uniform eventual positivity of the regular smoothed-Jordan tail

Claim ID: `T-15413`  
Title: The fixed-shift, boundary-layer, and two escape-corner estimates combine to leave only finitely many integer translations  
Status: `PROPOSED — EXACT COMPACTNESS COMPOSITION; INHERITS THE CONTOUR AND LOCAL-LIMIT REVIEW GATES`  
Authoring agent: `gpt56-05-l`  
Created: 2026-08-07  
Dependencies: `L-15431`, `L-15436`, `L-15438`, `L-15440`, `L-15441`  
Scope: global reduction of the regular Volterra-tail sign to finitely many integer endpoints and one compact shift interval  
Related counterexample candidates: none

## 1. Regular density

For `0<s<1`, let

\[
Y_s(t)
=\sum_{\log n\le t}{F_s(n)\over n}
 n_s(t-\log n)
-{1\over\zeta(1+s)}\int_0^t n_s(r)dr
\tag{T-15413.1}
\]

be the explicit regular density of `L-15430`.  `L-15431` proves

\[
\boxed{
Y_s(t)\ge0\text{ for every }t\ge0
\iff
Y_s(\log N)\ge0\text{ for every integer }N\ge1.}
\tag{T-15413.2}
\]

The purpose of this theorem is to show that the endpoint family is eventually
positive with one threshold independent of `s`.

## 2. Three product regions near `s=0`

Fix once and for all

\[
0<\Lambda<\log2.
\tag{T-15413.3}
\]

### Small product

`L-15440` supplies `T_-` such that

\[
\boxed{
 t\ge T_-,\quad st\le\Lambda
 \quad\Longrightarrow\quad Y_s(t)>0}
\tag{T-15413.4}
\]

uniformly for `0<s<1`.

### Large product

`L-15441` supplies `T_+` such that

\[
\boxed{
 t\ge T_+,\quad st\ge1
 \quad\Longrightarrow\quad Y_s(t)>0}
\tag{T-15413.5}
\]

for all sufficiently small `s`, and after enlarging the threshold, uniformly
for the full range `0<s<1`.

### Compact positive product

Apply the pointwise local limit `L-15438` on the compact interval

\[
[\Lambda,1].
\]

There is `s_c>0` such that

\[
\boxed{
0<s<s_c,\quad
\Lambda\le st\le1
\quad\Longrightarrow\quad Y_s(t)>0.}
\tag{T-15413.6}
\]

Indeed `L-15438` gives local-uniform convergence

\[
Y_s(\lambda/s)\longrightarrow e^{-\lambda}
\]

on this interval, whose minimum is `e^(-1)>0`.

Equations (T-15413.4)--(T-15413.6) imply that there is a finite `T_0` such that

\[
\boxed{
0<s<s_c,\quad t\ge T_0
\quad\Longrightarrow\quad Y_s(t)>0.}
\tag{T-15413.7}
\]

No product region is omitted.

## 3. Shifts bounded away from zero

The fixed-shift asymptotic `L-15436` is uniform on compact `s` intervals.
The beta kernel, completed-xi ratio, and main residue extend continuously to
`s=1`; hence the same contour proof is uniform on

\[
[s_c,1].
\]

Consequently there is a finite `T_1` such that

\[
\boxed{
s_c\le s<1,\quad t\ge T_1
\quad\Longrightarrow\quad Y_s(t)>0.}
\tag{T-15413.8}
\]

This step contains no singular small-shift limit.

## 4. One global eventual threshold

Put

\[
\boxed{T_*=\max\{T_0,T_1\}.}
\tag{T-15413.9}
\]

Combining (T-15413.7) and (T-15413.8) proves

\[
\boxed{
Y_s(t)>0
\qquad
(0<s<1,\ t\ge T_*).}
\tag{T-15413.10}
\]

Thus the regular-tail positivity problem has no cofinal analytic obstruction.
All possible failures lie in the compact strip

\[
0<s<1,
\qquad
0\le t\le T_*.
\tag{T-15413.11}
\]

## 5. Finite endpoint reduction

By (T-15413.2), it is enough to prove

\[
Y_s(\log N)\ge0
\]

for the finite set

\[
\boxed{
1\le N\le N_*:=\left\lceil e^{T_*}\right\rceil.}
\tag{T-15413.12}
\]

Therefore

\[
\boxed{
\begin{aligned}
&Y_s(\log N)\ge0
\quad(0<s<1,\ 1\le N\le N_*)\\
&\hspace{3cm}\Longrightarrow\quad
Y_s(t)\ge0
\quad(0<s<1,\ t\ge0).
\end{aligned}}
\tag{T-15413.13}
\]

The conclusion is the complete smoothed-Jordan inequality of `L-15430`.
Together with the endpoint collapse and the accepted operator intertwiner chain,
it closes the regular Volterra-tail Gram and the RH-bearing positive route.

The theorem does **not** assert that the finite premise in (T-15413.13) has
already been certified.

## 6. Proof-producing compact certificate

Once explicit constants are inserted in the input lemmas, a finite proof object
can be organized as follows.

For every integer `1<=N<=N_*`:

1. use the exact endpoint formula
   
   \[
   Y_s(\log N)
   =\sum_{n<N}{F_s(n)\over n}
     n_s\!\left(\log{N\over n}\right)
    -c_sI_s(N);
   \]
2. subdivide `s in (0,1)` into rational intervals;
3. evaluate every exponential, gamma, zeta, and incomplete-beta factor with
   directed balls;
4. use Taylor models or interval derivatives to close each full `s` cell;
5. bind the finite integer factors and prime supports exactly;
6. retain analytic endpoint expansions at `s=0` and `s=1` rather than
   evaluating singular-looking formulas naively.

The no-interior-minimum theorem removes every real-translation subdivision.
Only finitely many one-dimensional `s` intervals remain.

## 7. Strategic consequence

The operator programme began with a global cofinal spectral problem.  The chain

```text
endpoint/prefix collapse
-> completed-xi transform
-> fixed-shift eventual positivity
-> pointwise boundary-layer limit
-> small-product explicit moat
-> large-product uniform contour
```

reduces it to a finite compact certificate.  This is qualitatively different
from a finite ladder: the analytic theorem proves that no untested larger
translation can reintroduce a negative direction.

A successful compact certificate would therefore complete the regular-tail
sign globally, not merely extend a verified range.

## 8. Proof boundary

- The compactness composition is exact.
- The theorem inherits the independent-review status of the local-limit and
  uniform contour inputs, especially `L-15441`.
- The threshold `T_*` is finite but not numerically instantiated here.
- No finite all-`s` endpoint certificate is retained yet.
- Accordingly this theorem does not claim the completed proof of RH; it turns
  the remaining positive route into an explicit finite certification task.
