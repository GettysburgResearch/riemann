# L-94002 — One thinning controls every physical column and leaves native deficit below 3457

Claim ID: `L-94002`  
Status: **PROPOSED COMPLETE ON THE FROZEN RETAINED-CELL ESTIMATE — REVIEW REQUIRED**  
Date: 2026-08-16

Retain the notation of `L-94001`. The exact adjacent-cell estimate gives, for every `q>=2`, including `q<K`,

\[
|v_q(E_X^I)|<\frac{57}{2q\sqrt K},
\]

\[
|\mathcal D_4v_q(E_X^I)|<\frac{171}{4q\sqrt K}.
\]

The moving top anchor gives the uniform relative detail bound

\[
\boxed{
\frac{|\mathcal D_4v_q(E_X^I)|}{\Omega_X(q)}
<\frac{23}{\sqrt K}
}
\]

whenever `Omega_X(q)>0`; zero-capacity columns have zero retained response by support.

Choose

\[
\tau_K=\frac{\sqrt K}{\sqrt K+24},
\qquad d_X=\tau_Kd_X^0.
\]

Then

\[
\Xi_{d_X}(q)
\le
\frac{\sqrt K+23}{\sqrt K+24}\Omega_X(q)
<\Omega_X(q)
\]

for every nonzero detail column. Positive radix-four inversion yields

\[
C_{d_X}(q)\le w_X(q)
\qquad(q\ge2).
\]

The exact positive native dual gives

\[
J_\Lambda(X)-\mathcal H(d_X)
=\langle Y_4,\Omega_X-\Xi_{d_X}\rangle.
\]

Using the elementary Chebyshev bound for `J_Lambda`, the sparse `Y_4` support, and the retained-cell total-variation estimate gives, for `X>=10^12`,

```text
one common thinning                  <3456
one signed retained-cell mismatch       <1
------------------------------------------
native deficit                       <3457.
```

No benchmark estimate for `J_Lambda(X)-4sqrt(X)` is used.
