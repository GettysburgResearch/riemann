# L-26213 — Exact common weighted embedding for every annular bank observation

Claim ID: `L-26213`  
Title: Multiplicative source convolution, normalized physical translation, and carry potentials commute exactly in one weighted sequence Hilbert space  
Status: **PROPOSED COMPLETE EXACT LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Depends on: PR #268 `L-26802/L-26804`; `L-26210`--`L-26212`  
Scope: exact common-metric source embedding; no bank-observation upper bound, reserve estimate, or RH conclusion

## 1. The compact opposite-parity window

Retain

\[
h_\omega(t)=e^{-t/2}
\left[
\mathbf1_{[0,\log2)}(t)
-\frac12\mathbf1_{[\log2,\log4)}(t)
\right]
\]

and the integer potential

\[
g_m(r)=\mathbf1_{m\le r<2m}-\frac12\mathbf1_{2m\le r<4m}.
\]

For a finitely supported coefficient sequence `x`, put

\[
\alpha_x=\sum_m\frac{x_m}{\sqrt m}\delta_{\log m},
\qquad
Q_x=h_\omega*\alpha_x,
\]

and

\[
F_x(r)=\sum_mx_mg_m(r).
\]

PR #268 proves, for almost every `log r<=t<log(r+1)`,

\[
Q_x(t)=e^{-t/2}F_x(r),
\]

and hence

\[
\boxed{
\|Q_x\|_2^2
=\sum_{r\ge1}\frac{|F_x(r)|^2}{r(r+1)}.
}
\tag{L-26213.1}
\]

Define the fixed weighted Hilbert space

\[
\mathscr H_w
=\ell^2\!\left(\mathbb N,{1\over r(r+1)}\right).
\]

## 2. Multiplicative convolution intertwines exactly

Let `a` be any finitely supported arithmetic sequence and define

\[
(a*x)(q)=\sum_{dm=q}a(d)x(m).
\]

Let

\[
\mathcal A_a
=\sum_d\frac{a(d)}{\sqrt d}\tau_{\log d}.
\]

Then normalized physical translation gives the exact source identity

\[
\boxed{
\mathcal A_aQ_x=Q_{a*x}.
}
\tag{L-26213.2]

The corresponding potential has the exact formula

\[
\boxed{
F_{a*x}(r)
=\sum_da(d)F_x\!\left(\left\lfloor{r\over d}\right\rfloor\right).
}
\tag{L-26213.3]

Indeed

\[
g_{dm}(r)=g_m\!\left(\left\lfloor{r\over d}\right\rfloor\right)
\]

for every positive integer `d,m,r`.

Combining (L-26213.1)--(L-26213.3), every multiplicative prefix observation has the exact common-metric norm

\[
\boxed{
\|\mathcal A_aQ_x\|_2^2
=\sum_{r\ge1}{1\over r(r+1)}
\left|
\sum_da(d)F_x\!\left(\left\lfloor{r\over d}\right\rfloor\right)
\right|^2.
}
\tag{L-26213.4]

No annulus-dependent metric is introduced.

## 3. Exact dilation scaling

For

\[
(D_dF)(r)=F(\lfloor r/d\rfloor),
\]

telescoping the weights over one `d`-block gives

\[
\sum_{r=dk}^{d(k+1)-1}{1\over r(r+1)}
={1\over d}\,{1\over k(k+1)}.
\]

Therefore

\[
\boxed{
\|D_dF\|_{\mathscr H_w}^2
={1\over d}\|F\|_{\mathscr H_w}^2.
}
\tag{L-26213.5]

This is the exact critical square-root scaling already built into the normalized translation coefficient `d^{-1/2}`.

## 4. One common oversupport carry row

Assume

\[
x_m=0\quad\text{unless}\quad M\le m<2M
\]

and

\[
a(d)=0\quad(d\ge R).
\]

Then `a*x` is supported below `2MR`, and

\[
\operatorname{supp}F_{a*x}\subset[M,8MR).
\]

Set

\[
U=8MR,
\qquad
N=2U-1=16MR-1.
\]

For `1<=j<U`,

\[
F_{a*x}(N)=F_{a*x}(N-j)=0,
\]

so

\[
(\mathcal S_NF_{a*x})(j)=-F_{a*x}(j).
\]

Consequently

\[
\boxed{
\|\mathcal A_aQ_x\|_2^2
=\sum_{j=1}^{U-1}
{ |(\mathcal S_NF_{a*x})(j)|^2\over j(j+1)}.
}
\tag{L-26213.6]

Every bank prefix `a=a_Y` with `Y<=R` therefore lives in the **same** row `N`, the same lower-half coordinate set, and the same weight `1/[j(j+1)]`. Smaller supports are represented by zeros, not by changing the metric.

All source collisions and all within-observation cross terms are already included in `a*x` before the norm is taken.

## 5. Application to the critical digital bank

Take

\[
a_Y(n)=c_2(n)\mathbf1_{n<Y},
\qquad
c_2(n)=1-v_2(n),
\]

and take the RH-sensitive annular coefficient

\[
x_m=\Lambda_\omega(m)\mathbf1_{M\le m<2M}.
\]

Then every strict-prefix observation in `L-26210/L-26211` is exactly

\[
Q_{a_Y*x}
\]

and is represented by (L-26213.6) in one common weighted carry Hilbert space.

Moreover its carry source is

\[
\omega_2*(a_Y*x),
\]

so the distinction between the RH-sensitive feature and the positive-inverse feature is retained algebraically. No substitution of `P_n` for `W_n` occurs.

This closes the **existence of a common annular bank embedding** which was left conditional in `L-26212`.

## 6. What remains quantitative

The exact common embedding does not imply an upper estimate for the observations. A full theorem must still:

1. decompose `omega_2*(a_Y*x)` into its finite generalized-prime current term and signed strict-delay tail;
2. retain quotient cells `2,3,4` and every reflected cross term;
3. route the proper-divisor Selberg defect and endpoint collars;
4. prove a subexponential current-versus-lower-scale inequality.

The common metric is now explicit; the remaining problem is a source-specific estimate inside that metric.

## 7. Proof boundary

Closed exactly, subject to review:

- physical/source convolution intertwining;
- the integer-potential formula;
- the common weighted Hilbert space;
- exact normalized dilation scaling;
- one common oversupport carry row for every finite bank observation;
- source-faithful embedding of the critical digital bank.

Open:

- quantitative observation domination;
- the transition/collar recurrence;
- RH.
