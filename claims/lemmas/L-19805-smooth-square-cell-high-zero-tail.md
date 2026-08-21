# L-19805 — Smooth square-cell averages have a subpolynomial complete high-zero tail

Claim ID: `L-19805`  
Title: Positive smoothing inside one critical square cell suppresses every zero above height proportional to the square-root scale  
Status: `PROPOSED — COMPLETE OSCILLATORY-TAIL ESTIMATE`  
Authoring agent: `gpt56-pro-09-i`  
Created: 2026-08-01  
Depends on: `L-19804`; Nakamura--Suzuki's zero expansion; the unconditional Riemann--von Mangoldt count

## 1. Smooth cell average

Fix a nonnegative function

\[
w\in C_c^\infty(0,1),
\qquad
\int_0^1w(u)du=1.
\tag{L-19805.1}
\]

For `n>=1`, put

\[
x_n(u)=n^2+(2n+1)u
\tag{L-19805.2}
\]

and define

\[
\boxed{
\mathscr A_n(w)
 =\int_0^1w(u)\Psi(\log x_n(u))du.}
\tag{L-19805.3}
\]

This is a positive average over the square cell `[n^2,(n+1)^2]`, so
`L-19804` gives

\[
RH
\iff
\mathscr A_n(w)\ge0
\text{ eventually}.
\tag{L-19805.4}
\]

## 2. Zero-side filter

For a centered zero `gamma`, define

\[
\boxed{
J_{n,w}(\gamma)
 =\int_0^1w(u)x_n(u)^{-i\gamma}du.}
\tag{L-19805.5}
\]

Averaging Nakamura--Suzuki's absolutely convergent expansion gives

\[
\boxed{
\mathscr A_n(w)
 =\sum_\gamma m_\gamma
 \frac{1-J_{n,w}(\gamma)}{\gamma^2}.}
\tag{L-19805.6}
\]

No RH assumption enters this identity.

Write

\[
\gamma=a+ib,
\qquad |b|\le\frac12.
\tag{L-19805.7}
\]

The ordinary zero ordinate is `-a`, while `b` is its horizontal displacement
from the critical line.

## 3. Nonstationary filter bound

For every integer `M>=0`, there is a constant `C_(w,M)` such that

\[
\boxed{
|J_{n,w}(a+ib)|
 \le C_{w,M}
 n^{2b_+}
 \left(1+\frac{|a|}{n}\right)^{-M},}
\tag{L-19805.8}
\]

where `b_+=max(b,0)`. In particular, uniformly over the complete critical strip,

\[
\boxed{
|J_{n,w}(\gamma)|
 \le C_{w,M}n
 \left(1+\frac{|a|}{n}\right)^{-M}.}
\tag{L-19805.9}
\]

### Proof

The phase is

\[
\phi_n(u)=\log x_n(u),
\qquad
\phi_n'(u)=\frac{2n+1}{x_n(u)}\asymp n^{-1}
\tag{L-19805.10}
\]

uniformly on `[0,1]`. There is no stationary point. Factor

\[
x_n(u)^{-i\gamma}=x_n(u)^b e^{-ia\phi_n(u)}.
\]

For `|a|<=n`, the absolute-value bound gives

\[
|J_{n,w}(\gamma)|\le C_w n^{2b_+}.
\]

For `|a|>n`, integrate by parts with

\[
e^{-ia\phi_n(u)}
 ={1\over-ia\phi_n'(u)}
 {d\over du}e^{-ia\phi_n(u)}.
\tag{L-19805.11}
\]

All boundary terms vanish because `w` is compactly supported in `(0,1)`.
Each application costs at most `C_w n/|a|`; derivatives of
`x_n(u)^b`, `1/phi_n'(u)=x_n(u)/(2n+1)`, and the fixed bump are bounded by the
same declared scale. Repeating `M` times proves (L-19805.8).

## 4. Complete high-zero tail

Fix `A>0` and let the high set consist of centered zeros with

\[
|\Re\gamma|=|a|\ge An.
\tag{L-19805.12}
\]

For every `M>=2`, the unconditional zero count

\[
N(T+1)-N(T)\ll\log(T+2)
\tag{L-19805.13}
\]

and (L-19805.9) give

\[
\begin{aligned}
\sum_{|a|\ge An}
 m_\gamma { |J_{n,w}(\gamma)|\over|\gamma|^2}
&\ll_{w,M}
 n^{M+1}
 \sum_{k\ge An}{\log(k+2)\over k^{M+2}}\\
&\ll_{w,M,A}\log(n+2).
\end{aligned}
\tag{L-19805.14}
\]

Also

\[
\sum_{|a|\ge An}{m_\gamma\over|\gamma|^2}
 \ll_A{\log(n+2)\over n}.
\tag{L-19805.15}
\]

Therefore the complete high-zero contribution to (L-19805.6) obeys

\[
\boxed{
\left|
\sum_{|\Re\gamma|\ge An}
 m_\gamma{1-J_{n,w}(\gamma)\over\gamma^2}
\right|
 \le C_{w,M,A}\log(n+2).}
\tag{L-19805.16}
\]

This estimate is unconditional and includes every hypothetical off-line zero.
The worst possible horizontal factor `n` is exactly offset by the `1/gamma^2`
zero weight and the arbitrarily high nonstationary decay.

## 5. Consequence at the RH scale

Since

\[
\log n=n^{o(1)},
\]

the complete zero tail above height `An` is already negligible for the
subpolynomial criterion. Thus the RH-bearing part of the smooth square-cell
average is confined to the finite moving block

\[
\boxed{
|\Re\gamma|<An.}
\tag{L-19805.17}
\]

No unselected high-zero absolute budget larger than `O(log n)` is needed.

This gives a proof-producing finite phase-band architecture:

1. retain the finite zero block through height proportional to `n` if a zero-side
   certificate is desired;
2. bound every remaining zero, on or off the line, by (L-19805.16);
3. independently evaluate the equivalent finite prime-power average through
   `(n+1)^2`;
4. compare the two directed intervals.

An unbounded verified-zero census is still not a proof requirement for the
prime-side criterion. The zero-side formulation is a finite diagnostic and
cross-check.

## 6. Fixed off-line zeros are not suppressed

For every fixed centered zero `gamma`,

\[
J_{n,w}(\gamma)
 =n^{-2i\gamma}(1+o(1))
\tag{L-19805.18}
\]

because `x_n(u)/n^2->1` uniformly. Hence a fixed off-line zero with `b>0`
retains magnitude `n^(2b)` and is not smoothed away. The averaging removes only
zeros whose ordinate is large relative to the cell's square-root scale.

This is consistent with `L-19802`: the rightmost horizontal displacement still
controls the exact negative growth exponent.

## 7. Proof boundary

- The nonstationary filter and high-zero tail estimates are unconditional.
- The `O(log n)` tail is subpolynomial but does not determine the sign of the
  finite moving zero block.
- A finite critical-line verification through height `An` closes only that
  finite level, not the cofinal sequence.
- The lemma materially simplifies proof production but does not prove the
  averaged inequalities or RH.