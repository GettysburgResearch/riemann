# L-95311 — The finite odd-core packet has polylogarithmic diagonal energy

Claim ID: `L-95311`  
Status: **PROPOSED COMPLETE UNCONDITIONAL ENERGY THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-17  
Depends on: `L-95310`; the exact Q4 cubic of PR #531

Define

\[
K_0(x)
=
\sum_{r=0}^{5}
A_r2^{-r/2}W(2^rx),
\tag{L-95311.1}
\]

and

\[
K_1(x)
=
\sum_{r=0}^{5}
B_r2^{-r/2}W(2^rx).
\tag{L-95311.2}
\]

Then the preconditioned critical observation is exactly

\[
\boxed{
\mathcal C_e(X)
=
\sum_{\substack{m\le X\\m\ {\rm odd}}}
\frac{\mu(m)}{\sqrt m}
\left[
(\log m)K_0(m/X)
+
(\log2)K_1(m/X)
\right].
}
\tag{L-95311.3}
\]

Only odd squarefree \(m\) contribute.

## Diagonal estimate

The safe pointwise Q4 bound

\[
|W(x)|\le32
\qquad(0\le x\le1)
\]

and the coefficient sums

\[
\sum_{r=0}^{5}|A_r|2^{-r/2}<16,
\qquad
\sum_{r=0}^{5}|B_r|2^{-r/2}<16
\]

give

\[
|K_0(x)|<512,
\qquad
|K_1(x)|<512.
\tag{L-95311.4}
\]

For

\[
F_{m,X}
=
\frac{
(\log m)K_0(m/X)
+
(\log2)K_1(m/X)
}{\sqrt m},
\]

one therefore has

\[
|F_{m,X}|
\le
512\frac{\log(2m)}{\sqrt m}.
\]

Consequently

\[
\boxed{
\sum_{\substack{m\le X\\m\ {\rm odd}}}
|F_{m,X}|^2
\le
2^{18}
(1+\log(2X))^3.
}
\tag{L-95311.5}
\]

Thus every same-core diagonal and the complete Rademacher-randomized model are
already polylogarithmic:

\[
\boxed{
\mathbb E_\varepsilon
\left|
\sum_m\varepsilon_mF_{m,X}
\right|^2
=
\sum_m|F_{m,X}|^2
=
O(\log^3X).
}
\tag{L-95311.6}
\]

No prime number theorem, zero table or RH input is used.

## Exact surviving correlation

Write

\[
|\mathcal C_e(X)|^2
=
\mathcal D(X)+\mathcal X(X),
\]

where

\[
\mathcal D(X)=\sum_m|F_{m,X}|^2
\]

and

\[
\boxed{
\mathcal X(X)
=
2\sum_{m<n}
\mu(m)\mu(n)F_{m,X}F_{n,X}.
}
\tag{L-95311.7}
\]

The diagonal \(\mathcal D\) is closed by (L-95311.5). The entire deterministic
OCHD obstruction is the distinct odd-core cross correlation
\(\mathcal X(X)\).
