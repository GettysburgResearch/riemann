# L-99131 — Two fixed row kernels and the primitive-scalar positive lift

Claim ID: `L-99131`  
Status: **PROVED EXACT FACTORIZATION THEOREM**  
Created: 2026-08-19  
Depends on: `L-99130`; the literal dictionaries of PR #611  
RH status: **not assumed**

Retain the exact sharp-row dictionaries

\[
Q_2(s)=\zeta(s)-1+2\,2^{-s}-3^{-s},
\tag{L-99131.1}
\]

\[
Q_3^\sharp(s)=\zeta(s)-1-2^{-s}+5\,3^{-s}-3\,4^{-s}.
\tag{L-99131.2}
\]

The moving-cutoff rows are

\[
A_{2,z}=M_zQ_2,
\qquad
A_{3,z}^\sharp=M_zQ_3^\sharp.
\tag{L-99131.3}
\]

With `x=2^{-s}` and `y=3^{-s}`, define

\[
\boxed{
K_2(s)={2(1-2x+y)\over(1-x)(2-x)},
}
\tag{L-99131.4}
\]

\[
\boxed{
K_3(s)={2(1+x+3x^2-5y)\over(1-x)(2-x)}.
}
\tag{L-99131.5}
\]

Then exact algebra gives

\[
\boxed{A_{2,z}=R_z-K_2B_z,}
\qquad
\boxed{A_{3,z}^\sharp=R_z-K_3B_z.}
\tag{L-99131.6}
\]

The two future-prime tails are therefore two fixed observations of one signed
profile against one positive reservoir.

The unique physical `5:3` scalar is `5A_2+A_3^sharp`; its numerator collapses:

\[
5Q_2+Q_3^\sharp
=6\zeta-3(1-x)(2-x).
\tag{L-99131.7}
\]

Consequently

\[
\boxed{
5A_{2,z}+A_{3,z}^\sharp=6(R_z-B_z).
}
\tag{L-99131.8}
\]

At the `p>3` root (`z=5`), let

\[
B_\diamond=(1-x)(1-x/2)\zeta^{-1},
\qquad
C_\diamond=1-B_\diamond.
\]

Because

\[
M_5={\zeta^{-1}\over(1-x)(1-y)},
\]

(L-99131.8) becomes the positive `2,3`-smooth lift

\[
\boxed{
5A_{2,5}+A_{3,5}^\sharp
={6C_\diamond\over(1-2^{-s})(1-3^{-s})}.
}
\tag{L-99131.9}
\]

Thus the FPCB23 scalar and the primitive-prefix carrier of PR #624 are the same
source after a positive finite-Euler inverse.

The component kernels are genuinely signed:

\[
K_2(2)=-1/2,
\qquad
K_3(3)=-5.
\tag{L-99131.10}
\]

Therefore scalar positivity cannot be promoted to two-row positivity without a
source-sensitive envelope theorem.
