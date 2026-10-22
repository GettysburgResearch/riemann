# R-32704 — The Q=4 PNT prefix cancellation belongs to `c_4=1*q_4`, not to `q_4`

Claim ID: `R-32704`  
Status: **EXACT SOURCE-TYPING CORRECTION; THE CORRECTED PHYSICAL THEOREM IS REPAIRED IN `L-32708`**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-09  
Dependencies: PR #325 `R-32403/L-32407`; elementary Dirichlet convolution  
Scope: corrects the uncorrected version of the Q=4 current-prefix argument; no RH conclusion

## 1. The two coefficient sequences

Retain the Q=4 inverse source and generalized-prime sequence

\[
 b_4=\mu*e_4,
 \qquad
 q_4=b_4*\Lambda_4,
\]

with

\[
 e_4(1)=1,
 \qquad
 e_4(4^r)=-3\quad(r\ge1).
\]

Then

\[
 \boxed{
 c_4:=\mathbf1*q_4=e_4*\Lambda_4.
 }
\tag{R-32704.1}
\]

The two sequences are not equal.

## 2. Prefix summation is not Dirichlet convolution by `1`

For any arithmetic function `f`,

\[
 (\mathbf1*f)(n)=\sum_{d\mid n}f(d)
\]

is a divisor sum, whereas

\[
 \sum_{m\le x}f(m)
\]

is an ordinary prefix sum. Summing the divisor convolution gives

\[
 \boxed{
 \sum_{n\le x}(\mathbf1*f)(n)
 =\sum_{d\le x}f(d)\left\lfloor\frac xd\right\rfloor,
 }
\tag{R-32704.2}
\]

not the ordinary prefix of `f`.

Therefore the identity

\[
\Psi_4(x)-3\sum_{r\ge1}\Psi_4(x/4^r)
\]

cannot be the ordinary prefix of `q_4` merely from `1*q_4=e_4*Lambda_4`.

## 3. Minimal exact witness

At the first Q-adic collision:

\[
\Lambda_4(2)=\log2,
\qquad
\Lambda_4(3)=\log3,
\qquad
\Lambda_4(4)=7\log2.
\]

Also `b_4(2)=-1`, so

\[
q_4(2)=\log2,
\qquad
q_4(3)=\log3,
\qquad
q_4(4)=6\log2.
\]

Hence

\[
 \boxed{
 \sum_{m\le4}q_4(m)=7\log2+\log3.
 }
\tag{R-32704.3}
\]

On the other hand

\[
c_4=e_4*\Lambda_4
\]

gives

\[
c_4(2)=\log2,
\quad c_4(3)=\log3,
\quad c_4(4)=7\log2,
\]

and therefore

\[
 \boxed{
 \sum_{m\le4}c_4(m)=8\log2+\log3.
 }
\tag{R-32704.4}
\]

The two prefixes differ by exactly `log 2`.

## 4. What the PNT cancellation actually proves

Because `c_4=e_4*Lambda_4`, its ordinary prefix is legitimately

\[
 \boxed{
 G_4(x):=\sum_{n\le x}c_4(n)
 =\Psi_4(x)-3\sum_{r\ge1}\Psi_4(x/4^r).
 }
\tag{R-32704.5}
\]

This is precisely the coefficient of the **correct interval-kernel physical field** in PR #325 `R-32403/L-32407`.

Thus the cancellation argument based on

\[
3\sum_{r\ge1}4^{-r}=1
\]

is not lost. It must simply be attached to `c_4` rather than to `q_4`.

`L-32708` records the repaired PNT theorem and the resulting vanishing physical-current/reserve ratio in the correct coordinate.

## 5. Disposition

```text
prefix q4 = Psi4 - 3 sum Psi4(. / 4^r)     FALSE
prefix c4 = Psi4 - 3 sum Psi4(. / 4^r)     EXACT
uncorrected q4 PNT argument                 SOURCE-TYPE ERROR
correct interval-kernel physical field      RETAINED
corrected PNT cancellation for c4           REPAIRED IN L-32708
RH                                           UNPROVED
```
