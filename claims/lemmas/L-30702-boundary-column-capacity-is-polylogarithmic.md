# L-30702 — The coherent stopped boundary has only polylogarithmic column-capacity mass

Claim ID: `L-30702`  
Title: Although its ordinary divisor-source atomic norm is linear, the complete stopped boundary has `O(log^2 X)` mass in the natural carry-column metric  
Status: **PROPOSED COMPLETE ELEMENTARY LEMMA**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-08  
Issue: #307  
Dependencies: `R-30701`  
Scope: one complete first boundary; no all-generation flow construction

## 1. Alternating-pair bounds

Retain

\[
p(x)=x^{-1/2},
\qquad
w_X(x)=x^{-1/2}\log(X/x)\mathbf1_{x\le X}.
\]

Both functions are nonnegative and decreasing on their positive support. For
fixed `q`, the interlacing points satisfy

\[
2kq-1<(2k+1)q<2(k+1)q-1.
\]

Consequently the finite paired sum

\[
(\mathcal C_Xw_X)(q)
=\sum_{k\ge1}
[w_X(2kq-1)-w_X((2k+1)q)]
\]

is nonnegative and bounded by its first positive term:

\[
0\le(\mathcal C_Xw_X)(q)\le w_X(2q-1).
\tag{L-30702.1}
\]

The same alternating-series argument gives

\[
0\le(\mathcal Cp)(q)\le p(2q-1).
\tag{L-30702.2}
\]

## 2. Pointwise boundary bound

For `2q-1<=X`, put

\[
L_X(q)=\log\frac{X}{2q-1}.
\]

The boundary is

\[
P_X(q)=(\mathcal C_Xw_X)(q)-L_X(q)(\mathcal Cp)(q).
\]

Equations (L-30702.1)--(L-30702.2) imply

\[
\begin{aligned}
|P_X(q)|
&\le w_X(2q-1)+L_X(q)p(2q-1)\\
&=2L_X(q)(2q-1)^{-1/2}.
\end{aligned}
\]

Since `2q-1>=q` and `X/(2q-1)<=X/q`,

\[
\boxed{
|P_X(q)|
\le2q^{-1/2}\log\frac Xq.
}
\tag{L-30702.3}
\]

## 3. Carry-column capacity norm

The column capacity normalization is `q^(-1/2)`. Therefore

\[
\begin{aligned}
\sum_{2\le q\le(X+1)/2}
\frac{|P_X(q)|}{\sqrt q}
&\le2\sum_{2\le q\le X}
\frac1q\log\frac Xq\\
&\le2\int_1^X\frac1t\log\frac Xt\,dt
+2\log X.
\end{aligned}
\]

The integral is `(log X)^2/2`. Hence

\[
\boxed{
\sum_q\frac{|P_X(q)|}{\sqrt q}
\le(\log X)^2+2\log X.
}
\tag{L-30702.4}
\]

Thus the same coherent boundary satisfies the sharp coordinate contrast

\[
\boxed{
\begin{array}{rcl}
\text{ordinary divisor atomic norm}&=&\Omega(X),\\
\text{carry-column capacity mass}&=&O(\log^2X).
\end{array}}
\tag{L-30702.5}
\]

## 4. Interpretation

The linear lower bound in `R-30701` is not evidence that the boundary itself is
macroscopic in the proof-facing carry metric. It proves that the atom-by-atom
map

\[
\sigma\longmapsto\sum_m\sigma_mE_{m-1}
\]

is the wrong coordinate for this recombined source.

Any successful repair should preserve the complete boundary until it is placed
in the Pascal-cycle or another coherent carry-flow coordinate. Taking the
ordinary divisor-source total variation first loses a factor of order `X`.

Equation (L-30702.4) does not itself construct a flow. It identifies the scale
which a correct cycle-optimized transference theorem is allowed to spend.

## 5. Proof boundary

Proved exactly:

1. the alternating-pair bounds;
2. the pointwise critical boundary estimate;
3. the polylogarithmic column-capacity mass.

Open:

1. a right inverse from this coherent boundary class to balanced flows with
   comparable negative capacity;
2. the all-generation recurrence;
3. RH.
