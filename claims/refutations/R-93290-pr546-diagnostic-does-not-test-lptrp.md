# R-93290 — PR #546's retained row scan does not test `LPTRP_23`

Claim ID: `R-93290`  
Status: **EXACT STATEMENT-TO-USE CORRECTION**  
Created: 2026-08-18  
Frozen target: PR #546 at `f920202ea15c577bf05fa58370bdc3d8313868cd`  
RH status: **unproved**

## 1. The two different coefficient sequences

PR #546 defines the full-row diagnostic coefficients by

\[
 b_2(n)=\mathbf1_{n=1}-\mu(n)
 +2\mathbf1_{2\mid n}\mu(n/2)
 -\mathbf1_{3\mid n}\mu(n/3),
\tag{R-93290.1}
\]

and

\[
\begin{aligned}
3b_3(n)={}&\mathbf1_{n=1}-\mu(n)
-\mathbf1_{2\mid n}\mu(n/2)\\
&+5\mathbf1_{3\mid n}\mu(n/3)
-3\mathbf1_{4\mid n}\mu(n/4).
\end{aligned}
\tag{R-93290.2}
\]

Its `row_scan` routine accumulates these coefficients with the ordinary Möbius
function.

The conclusion-producing theorem `LPTRP_23`, however, concerns the
large-prime-filtered Möbius function

\[
 \mu_{>3}(n)=
 \begin{cases}
 \mu(n),&(n,6)=1,\\
 0,&(n,6)>1,
 \end{cases}
\tag{R-93290.3}
\]

and therefore the different coefficients

\[
\boxed{
 a_2(n)=\mathbf1_{n\in\langle2,3\rangle}
 -\mu_{>3}(n)+2\mu_{>3}(n/2)-\mu_{>3}(n/3),
}
\tag{R-93290.4}
\]

and

\[
\boxed{
\begin{aligned}
 a_3^\sharp(n)={}&\mathbf1_{n\in\langle2,3\rangle}
 -\mu_{>3}(n)-\mu_{>3}(n/2)\\
 &+5\mu_{>3}(n/3)-3\mu_{>3}(n/4),
\end{aligned}}
\tag{R-93290.5}
\]

where a nonintegral argument contributes zero and
`a_3^sharp=3 a_3`.

Thus the full-row scan through `300000` is not evidence for the stated
large-prime producer. PR #546 correctly labels the scan diagnostic, but the
quantity scanned is not the quantity consumed.

## 2. Integer endpoints are also insufficient by themselves

For any coefficient sequence `a`, put

\[
 C_a(X)=\sum_{n\le X}\frac{a(n)}{\sqrt n}\log\frac Xn.
\tag{R-93290.6}
\]

Checking only `C_a(N)>=0` at integers does not by itself prove positivity for
real `X`: the row may descend between two activation knots. The exact missing
coordinate is the prefix derivative

\[
 A_a(N)=\sum_{n\le N}\frac{a(n)}{\sqrt n}.
\tag{R-93290.7}
\]

`L-93290` supplies the exact activation identity, and `T-93290` certifies the
actual filtered prefixes rather than only integer row values.

```text
PR #546 full-row scan                         diagnostic / correct scope
PR #546 scan as evidence for LPTRP_23         invalid statement-to-use step
integer row scan without prefix derivatives   insufficient for real X
actual filtered all-real finite theorem       supplied by T-93290
Riemann Hypothesis                            unproved
```
