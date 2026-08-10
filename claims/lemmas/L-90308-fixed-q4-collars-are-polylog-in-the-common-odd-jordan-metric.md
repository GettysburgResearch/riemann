# L-90308 — Fixed Q4 collars are polylogarithmic in the common odd-Jordan metric

Claim ID: `L-90308`  
Title: For the common odd-Jordan Q4 carrier of `L-90307`, every fixed-child endpoint collar of the base, zero-bare input, and compact output has first current `O(log n)` and second current `O(log^2 n)`, hence contributes only polynomial forcing in logarithmic block scale  
Status: **PROPOSED COMPLETE EXACT/ARITHMETIC LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-10  
Dependencies: `L-90307`; PR #341 `L-34005`; elementary structure of `Lambda_odd` and `C_odd`  
Scope: finite endpoint/cut collars in the odd-Jordan metric; no interior recurrence or RH conclusion

## 1. Three source types

Retain the paths of `L-90307` at `tau=0`:

\[
g=B_0=\mu,
\qquad
h=(\varepsilon-\delta_4)*\mu,
\qquad
c=(\varepsilon-4\delta_4)*\mu.
\tag{L-90308.1}
\]

Their divisor-prefix sources are exactly

\[
\boxed{
\mathbf1*g=\varepsilon,
\quad
\mathbf1*h=\varepsilon-\delta_4,
\quad
\mathbf1*c=\varepsilon-4\delta_4.
}
\tag{L-90308.2}
\]

Hence all three bare carry fields are uniformly bounded, and the `h` field vanishes identically once both children are at least four.

## 2. Odd first and second Jordan currents

Let

\[
\Lambda_o=\Lambda_{\rm odd},
\qquad
C_o=\Lambda_o\log+\Lambda_o*\Lambda_o.
\tag{L-90308.3}
\]

For a source `b` among `g,h,c`, its odd-Jordan jets are

\[
q_b=b*\Lambda_o,
\qquad
t_b=b*C_o.
\tag{L-90308.4}
\]

Convolving once with `1` and using (L-90308.2) gives

\[
\boxed{
\begin{aligned}
\mathbf1*q_g&=\Lambda_o,
&\mathbf1*t_g&=C_o,\\
\mathbf1*q_h&=(\varepsilon-\delta_4)*\Lambda_o,
&\mathbf1*t_h&=(\varepsilon-\delta_4)*C_o,\\
\mathbf1*q_c&=(\varepsilon-4\delta_4)*\Lambda_o,
&\mathbf1*t_c&=(\varepsilon-4\delta_4)*C_o.
\end{aligned}}
\tag{L-90308.5}
\]

## 3. Pointwise coefficient bounds

Elementary von Mangoldt support gives

\[
\boxed{|\Lambda_o(m)|\le\log(2m).}
\tag{L-90308.6}
\]

Moreover

\[
\boxed{|C_o(m)|\ll\log^2(2m).}
\tag{L-90308.7}
\]

To see this, the term `Lambda_o(m) log m` is immediate. For the convolution term, a nonzero summand

\[
\Lambda_o(d)\Lambda_o(m/d)
\]

requires both `d` and `m/d` to be odd prime powers. Thus `m` has at most two odd prime factors. If it has two distinct prime factors there are at most two ordered nonzero decompositions; if `m=p^k`, there are `k-1` decompositions and

\[
(k-1)(\log p)^2\le (\log m)^2.
\]

This proves (L-90308.7) with an absolute constant.

Applying the fixed filters `epsilon-delta_4` or `epsilon-4delta_4` preserves the same bounds.

## 4. Fixed-child prefix/carry localization

For any arithmetic sequence `f`, put `a=1*f`. For a split `n=r+(n-r)` with fixed positive integer `r`, the exact prefix/carry identity is

\[
\boxed{
\mathcal L_{n,r}(f)
=\sum_{j=0}^{r-1}a(n-j)-\sum_{m=1}^r a(m).
}
\tag{L-90308.8]

(The closing bracket in the tag is typographical only.)

Therefore for every fixed `r` and every `b in {g,h,c}`,

\[
\boxed{
|\mathcal L_{n,r}(q_b)|\ll_r\log(2n),
}
\tag{L-90308.9}
\]

and

\[
\boxed{
|\mathcal L_{n,r}(t_b)|\ll_r\log^2(2n).
}
\tag{L-90308.10}
\]

The reflected child `n-r` has the same bounds.

Thus every endpoint jet needed by the Q2/Q4 fixed-filter source/state dictionary is local after one prefix convolution.

## 5. Curvature collars are polynomial in block scale

On a logarithmic parent block

\[
e^J\le n<e^{J+1},
\]

one has for fixed `r`

\[
|Q_b(n,r)|\ll_r 1+J,
\qquad
|T_b(n,r)|\ll_r (1+J)^2,
\tag{L-90308.11}
\]

while the bare coordinate `Y_b(n,r)` is `O_r(1)`.

Hence the scalar source curvature

\[
Q_b(n,r)^2-Y_b(n,r)T_b(n,r)
\]

is

\[
\boxed{O_r((1+J)^2).}
\tag{L-90308.12}
\]

Any fixed finite family of endpoint rows, finite Toeplitz collars, or finite dyadic filter delays therefore contributes at most

\[
\boxed{O((1+J)^A)}
\tag{L-90308.13}
\]

for a fixed absolute exponent `A` after the standard block normalization.

This includes the adverse compact-source contacts `r=1,2,3` already isolated on PR #341, but the statement is uniform for every fixed collar width.

## 6. No moving-filter derivative gauge is needed

The point of using the common odd-Jordan metric is that the Q2/Q4 transfer filters are parameter-independent (`L-90307`). Therefore the only finite-width forcing is geometric truncation/collar forcing of the form estimated above.

The full `s`-derivative decomposition of PR #345 remains useful as a separate bridge, but it is not needed inside the odd-Jordan recurrence. In particular one need not pay a same-scale derivative gauge merely to transport curvature through the all-pass state.

## 7. Proof boundary

Closed exactly here:

1. explicit prefix sources for the three common Q4 states;
2. exact odd-current and odd-second-current prefix formulas;
3. pointwise `Lambda_odd=O(log n)` and `C_odd=O(log^2 n)`;
4. fixed-child localization;
5. first-current `O(log n)` and second-current `O(log^2 n)` endpoint bounds;
6. polynomial finite-collar curvature forcing in logarithmic scale.

Still open:

1. the complete balanced-interior coefficient-one recurrence in this common metric;
2. exact accounting of the lower-order negative spectral mass inside that recurrence;
3. RH.