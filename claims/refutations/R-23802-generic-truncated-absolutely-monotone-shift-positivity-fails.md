# R-23802 — Generic truncated absolutely-monotone shift positivity fails

Claim ID: `R-23802`  
Status: `PROPOSED EXACT REFUTATION OF A GENERIC SURROGATE`  
Scope: boundary mechanism for the Gamma–carry / prime-shift route  
Depends on: `L-23805`  
RH status: **unproved**

Define

\[
h_0(t)=\left(e^t-\frac78e^{t/2}-\frac3{16}t e^{t/2}\right)\mathbf 1_{t\ge0}.
\]

On the open half-line every classical derivative is positive:

\[
h_0^{(k)}(t)
=e^{t/2}\left[e^{t/2}-2^{-k}\left(\frac78+\frac3{16}t+\frac{3k}{8}\right)\right]>0
\qquad(t>0,k\ge0).
\]

It is therefore tempting to claim that arbitrary positive backward shifts preserve positivity:

\[
\prod_j(I-\tau_{a_j})h_0(t)\ge0.
\]

That statement is false because truncation at the origin creates a genuine boundary term.

Take

\[
a=\log\frac54,\qquad b=\log\frac43,\qquad t=\log\frac32.
\]

Then

\[
t-a=\log\frac65,
\qquad
t-b=\log\frac98,
\qquad
t-a-b=\log\frac9{10}<0.
\]

Hence

\[
((I-\tau_a)(I-\tau_b)h_0)(t)
=f(3/2)-f(6/5)-f(9/8),
\]

where

\[
f(x)=x-\frac78\sqrt x-\frac3{16}\sqrt x\log x,
\qquad x\ge1.
\]

Elementary rational enclosures for the three square roots and the logarithms give

\[
-0.042298438672
< f(3/2)-f(6/5)-f(9/8)
< -0.042298438668.
\]

Thus

\[
\boxed{((I-\tau_a)(I-\tau_b)h_0)(t)<0.}
\]

## Consequence

No proof of the prime-shift theorem may use only:

- absolute monotonicity of `h_0` on `(0,infinity)`;
- generic B-spline positivity for arbitrary shifts;
- a boundary-free divided-difference identity.

The surviving route must use the arithmetic structure of the actual shifts `log p` and the Möbius inclusion–exclusion boundary charges.

This refutes only the generic surrogate. It does **not** refute the actual prime-log product or Gamma–carry factor positivity.
