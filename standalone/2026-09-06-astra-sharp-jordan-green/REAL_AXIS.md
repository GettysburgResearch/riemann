# A real-axis prime-deletion margin supplied by one prime

Status: **PROPOSED COMPLETE PROOF; REVIEW PENDING**.
This closes the inequality explicitly left open in PR #440, L-91412.17,
on a larger interval. It is not used to prove the sharper density theorem in
PROOF.md; the two proofs provide complementary checks of the research pivot.

## Theorem JGC26.T3

For every real 0<s<=1,

\[
 M_s=\sum_p\frac{\log p}{p^s(p-1)},\quad c_s=1/\zeta(1+s)
\]

satisfy

\[
 \boxed{s^2M_s-c_s>\frac{13}{900}s^2c_s>
                      \frac{13}{1800}s^3.}
\tag{A1}
\]

The series converges absolutely. The previous open interval 0<s<5/12 is
included. No PNT, zero-location theorem, or finite prime truncation is used.

## 1. Keep the extra prime-power reserve

Let L_s=-zeta'(1+s)/zeta(1+s). Absolute Euler expansion gives

\[
 M_s-L_s=\sum_{p,k\ge2}(\log p)
               [p^{-s-k}-p^{-(1+s)k}]\ge0.
\]

Retain all k>=2 for the ONE prime p=2. Writing t=2^(-s), this yields

\[
 M_s-L_s\ge (\log2)\frac{t(1-t)}{2-t}.
\tag{A2}
\]

For 0<s<=1, t>=1/2, t/(2-t)>=1/3 and the concavity of 1-2^(-s) gives
1-t>=s/2. Since zeta(1+s)>1/s,

\[
 \boxed{\zeta(1+s)(M_s-L_s)>\frac{\log2}{6}>1/9.}
\tag{A3}
\]

Discarding the extra prime-power reserve would miss this fixed positive term.

## 2. Pay the Euler-summation defect without a numerical zeta evaluation

Set g(s)=zeta(1+s)-1/s and P(s)=(s+1)(s+2)(s+3).
Euler--Maclaurin through B_4, obtained by integration by parts of periodic
Bernoulli polynomials, gives

\[
 g(s)=\tfrac12+(s+1)/12-P(s)/720+R(s),
\]

\[
 R(s)=-\frac{P(s)(s+4)}{24}
       \int_1^\infty\widetilde B_4(x)x^{-s-5}dx.
\tag{A4}
\]

Here B_4(v)=v^2(1-v)^2-1/30 on [0,1], periodically extended, and
|B_4|<=1/30: its maximum is 7/240 and its minimum is -1/30.
The displayed remainder and its derivative are absolutely convergent for
0<=s<=1; differentiation is justified by the integrable logarithmic envelope.
Explicit integration of x^(-s-5) and (log x)x^(-s-5) gives

\[
 |R'(s)|\le P'(s)/720+P(s)/(360(s+4)).
\]

The derivative of -P/720 cancels the first upper term. Since P(s)/(s+4)
is increasing on [0,1] with endpoint 24/5,

\[
 g'(s)\le\frac1{12}+\frac1{75}=\frac{29}{300}.
\tag{A5}
\]

The monotonicity follows either by differentiation with a positive numerator
or by writing P/(s+4)=s^2+2s+3-6/(s+4).
Thus

\[
 -\zeta'(1+s)\ge1/s^2-29/300.
\tag{A6}
\]

## 3. Combine the signs before dividing

Equations (A3) and (A6) imply

\[
 \zeta(1+s)M_s
 >1/s^2-29/300+1/9=1/s^2+13/900.
\]

Multiply by s^2 c_s. The elementary upper integral bound for zeta gives
c_s>s/(1+s)>=s/2, proving (A1).

## What this does and does not transfer

The zero-child transport and overshoot estimate in the frozen L-91412 remain
separate source formulas. This theorem pays their infinite real-axis mean
margin; it does not independently verify every coefficient in that packet,
and its margin alone would still require a finite-prime tail/overshoot
comparison to prove all knots. PROOF.md bypasses that loss and proves all
knots and intervening times directly. Neither theorem proves the critical
Xi-source intertwiner.

External input: the classical Euler--Maclaurin formula, e.g. NIST DLMF
25.11(iii). The exact remainder is written explicitly above rather than an
asymptotic series being treated as a global identity. See SOURCES.tsv and
EXTERNAL_INPUTS.md. All original analytic inequalities are reproduced in
this note; numerical reconnaissance is not a premise.
