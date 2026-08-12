# L-91329 — An integrated fractional-column top omission closes the real terminal annulus

Claim ID: `L-91329`  
Status: **PROPOSED COMPLETE EXACT FRACTIONAL TERMINAL THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-12  
Depends on: `L-91110/L-91111/L-91114`, `L-91324-fractional-column-green-identity-and-continuous-reset.md`  
Responds to: the real-column terminal gap identified in PR #405  
RH status: **unproved**

## 1. Why the integer pointwise estimate is insufficient

The integer-column proof in `L-91115` gives a uniform pointwise lower bound for the endpoint derivative. For a noninteger column, a breakpoint may enter fractionally and its pointwise derivative can tend to zero at the switch. Thus the integer lower bound cannot simply be reused.

The terminal argument only needs the response integrated over a fixed omitted endpoint interval. That integrated quantity has a uniform lower bound.

## 2. Fractional switching formula

For a finite seed `F`, put

\[
 A_F(n)=\frac{F(n)}{n-1}.
\]

For real `q>0`, let

\[
 k_j=\lfloor jq\rfloor,
 \qquad
 \vartheta_j=\{jq\}.
\]

The fractional Green identity of `L-91324` is

\[
 \overline v_q(F)=
 \sum_{j\ge1}
 \left[
 F(k_j)-F(k_j+1)
 +2\vartheta_j
  (A_F(k_j)-A_F(k_j+1))
 \right].
\tag{L-91329.1}
\]

## 3. Endpoint derivative

For real endpoint `s`, define

\[
 F_s(n)=\partial_sb_s(n)
 =\left(\frac{2\sqrt n}{s}
 -\frac{2n}{s^{3/2}}\right)\mathbf1_{n\le s}.
\tag{L-91329.2}
\]

For `1<x\le s`, the continuous extension

\[
 \frac{F_s(x)}{x-1}
 =\frac2{s^{3/2}}
  \frac{\sqrt{sx}-x}{x-1}
\]

is nonincreasing in `x`, because its derivative has numerator

\[
 1-\frac{\sqrt s(x+1)}{2\sqrt x}\le0.
\tag{L-91329.3}
\]

Hence every fractional correction in (L-91329.1) is nonnegative whenever both adjacent nodes are active. The partially active final breakpoint is also nonnegative.

For a fully active breakpoint `k=floor(jq)`,

\[
\begin{aligned}
 F_s(k)-F_s(k+1)
 &=\frac2{s^{3/2}}
 \left[1-\frac{\sqrt s}{\sqrt k+\sqrt{k+1}}\right]\\
 &\ge s^{-3/2}
 \left[2-\sqrt{\frac sk}\right].
\end{aligned}
\tag{L-91329.4}
\]

## 4. Uniform integrated derivative floor

Assume

\[
 q\ge100,
 \qquad
 q+1\le s<4q.
\]

We distinguish the number of full breakpoints.

- If only the first breakpoint is full, then either `s<2q` or the second is only partially active. In both cases
  \[
  \frac{s}{k_1}<\frac{2q+1}{q-1}<\frac94,
  \]
  so (L-91329.4) contributes more than `1/2`.

- If the first two are full and the third is absent or partial, then
  \[
  \frac{s}{k_1}<\frac{3q+1}{q-1}<\frac{49}{16},
  \qquad
  \frac{s}{k_2}<\frac{3q+1}{2q-1}<\frac{25}{16}.
  \]
  Their combined lower contribution exceeds `1`.

- If the first three are full, then
  \[
  \frac{s}{k_1}<\frac{4q}{q-1}<\left(\frac{21}{10}\right)^2,
  \]
  \[
  \frac{s}{k_2}<\frac{4q}{2q-1}<\left(\frac32\right)^2,
  \]
  \[
  \frac{s}{k_3}<\frac{4q}{3q-1}<\left(\frac65\right)^2.
  \]
  Their combined contribution exceeds `6-21/10-3/2-6/5>1`.

Thus in every case

\[
 \boxed{
 \partial_s\overline v_q(b_s)
 =\overline v_q(F_s)
 \ge\frac12s^{-3/2}.
 }
\tag{L-91329.5}
\]

This is an integrated-terminal replacement for the false uniform pointwise import from the integer-column theorem.

## 5. Fixed top omission

Let

\[
 W=200000,
 \qquad
 S_X=X-W-2.
\]

Omit the continuum endpoint interval

\[
 [S_X,X-1].
\]

For sufficiently large `X`, the equality endpoint density on this interval is

\[
 L(X/s)=2\sqrt{X/s}-1\ge1.
\]

If

\[
 X/4<q<X-W,
\]

then the subinterval

\[
 [\max(S_X,q+1),X-1]
\]

has length at least `W-2`, lies in `q+1<=s<4q`, and satisfies `s<=X`. Therefore

\[
 \boxed{
 \overline v_q(Q^{\rm top}_{X,\rm cont})
 \ge\frac{W-2}{2}X^{-3/2}
 =99999X^{-3/2}.
 }
\tag{L-91329.6}
\]

## 6. Quantization and signed-error ledger

The top-packet B-spline collar has adjacent-difference constant `C=32`. The fractional ordinary-response bound of `L-91324` gives, for `q>X/4`,

\[
 |\overline v_q(C_X^{\rm top})|
 <89\cdot32\cdot8\,X^{-3/2}
 =22784X^{-3/2}.
\tag{L-91329.7}
\]

Hence the quantized omission removes at least

\[
 (99999-22784)X^{-3/2}
 =77215X^{-3/2}.
\tag{L-91329.8}
\]

The complete remaining fractional mismatch-plus-collar overfill in `L-91324` is bounded by

\[
 28836X^{-3/2}.
\]

Thus the strict terminal margin is

\[
 \boxed{77215-28836=48379.}
\tag{L-91329.9}
\]

For `q>=X-W`, every retained endpoint index is at most `X-W`, so the retained response vanishes by triangularity.

Therefore the complete terminal annulus is feasible for every real column.

## 7. Score cost

The omitted endpoint width is fixed. Its exact entropy cost is

\[
 O(WX^{-1/2}\log^2(2X))=O(1)
\]

per reset generation. The repair does not change the coefficient-one score target.

## 8. Verification and status

The companion Fraction-only replay checks every rational case bound and the complete coefficient ledger. Retained verdict:

```text
PASS_INTEGRATED_FRACTIONAL_TOP_OMISSION
```

```text
integer pointwise derivative bound at real q       FALSE AS AN IMPORT
fractional Green identity                           EXACT
integrated derivative floor 1/2                     PROPOSED COMPLETE EXACT
fixed real-column omission margin 48379             EXACT LEDGER
continuous terminal annulus                         PROPOSED COMPLETE
rough all-generation state projection               OPEN / RH-BEARING
Riemann Hypothesis                                  UNPROVEN
```
