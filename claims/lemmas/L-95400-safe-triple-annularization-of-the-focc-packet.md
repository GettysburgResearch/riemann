# L-95400 — A safe three-factor scale filter annularizes the complete FOCC packet

Claim ID: `L-95400`  
Status: **PROPOSED COMPLETE EXACT ARITHMETIC/KERNEL THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-18  
Frozen parent: PR #573 at `0865242eb9dc0ed6094afc8a87a52b974c6f1307`  
Scope: exact Q4 kernel and scale reduction; no Möbius cancellation estimate and no RH conclusion

## 1. Frozen six-band packet

Retain the centered Q4 cubic

\[
W(x)=
\begin{cases}
5x-63x^2+170x^3,&0\le x\le\tfrac14,\\[2mm]
(-x+3x^2-2x^3)/3,&\tfrac14\le x\le1,\\
0,&x>1,
\end{cases}
\]

and the exact coefficient vectors

\[
A=(1,1,-8,-8,16,16),
\qquad
B=(0,-1,-8,0,32,16).
\]

Put

\[
K_0(x)=\sum_{r=0}^{5}A_r2^{-r/2}W(2^rx),
\qquad
K_1(x)=\sum_{r=0}^{5}B_r2^{-r/2}W(2^rx).
\]

For odd squarefree cores, PR #573's preconditioned observation is

\[
\mathcal C_e(X)
=
\sum_{\substack{m\le X\\m\ \mathrm{odd}}}
\frac{\mu(m)}{\sqrt m}
\left[(\log m)K_0(m/X)+(\log2)K_1(m/X)\right].
\tag{L-95400.1}
\]

## 2. Safe scale filter

Let `S` denote endpoint halving,

\[
(SF)(X)=F(X/2),
\]

and define

\[
\boxed{
Q(S)=
(I-\tfrac12S)(I-\tfrac14S)(I-\tfrac18S)
=I-\tfrac78S+\tfrac7{32}S^2-\tfrac1{64}S^3.
}
\tag{L-95400.2}
\]

Its Mellin multiplier is

\[
\boxed{
q(z)=
(1-2^{-z-1})(1-2^{-z-2})(1-2^{-z-3}).
}
\tag{L-95400.3}
\]

Every zero of `q` lies on one of the lines

\[
\Re z=-1,-2,-3.
\]

Thus the filter cannot cancel a conclusion-producing pole in `Re z>0`.

Define the filtered kernels

\[
\boxed{
J_\nu(x)
=K_\nu(x)-\frac78K_\nu(2x)
+\frac7{32}K_\nu(4x)
-\frac1{64}K_\nu(8x),
\qquad \nu=0,1.
}
\tag{L-95400.4}
\]

## 3. Exact compact support

On `0<=x<=2^-7`, every active term in `K_0,K_1` lies in the low cubic branch of `W`. Hence each `K_nu` is a polynomial combination of `x,x^2,x^3` there.

For a monomial `x^k`, endpoint halving acts by

\[
S[x^k]=2^kx^k.
\]

The factor `I-2^-k S` annihilates `x^k`. Since `Q` contains the three factors for `k=1,2,3`, applying (L-95400.4) annihilates the complete common cubic tail once all four arguments `x,2x,4x,8x` lie below `2^-7`. Therefore

\[
\boxed{
J_0(x)=J_1(x)=0
\quad(0\le x\le2^{-10}).
}
\tag{L-95400.5}
\]

They also vanish for `x>1`. The resulting observation

\[
\boxed{
\mathcal A(X):=Q(S)\mathcal C_e(X)
=
\sum_{\substack{X/1024<m\le X\\m\ \mathrm{odd}}}
\frac{\mu(m)}{\sqrt m}
\left[(\log m)J_0(m/X)+(\log2)J_1(m/X)\right]
}
\tag{L-95400.6}
\]

is supported on one fixed factor-1024 annulus.

The complete ten-band piecewise-cubic coefficients of `J_0,J_1`, in exact `Q(sqrt(2))` arithmetic, are deposited in

```text
experiments/X-95400-q4-focc-annular/certificates/exact_kernels.json
```

with activation bands

\[
2^{-j-1}<x\le2^{-j},
\qquad 0\le j\le9.
\]

## 4. Stable inverse

Every factor in `Q(S)` is invertible on endpoint sequences because its scale coefficient is strictly below one. Explicitly,

\[
\boxed{
Q(S)^{-1}
=
\prod_{k=1}^{3}
\sum_{j\ge0}2^{-kj}S^j.
}
\tag{L-95400.7}
\]

At any finite endpoint the expansion terminates. Its total absolute coefficient mass is

\[
\boxed{
\prod_{k=1}^{3}(1-2^{-k})^{-1}
=\frac{64}{21}.
}
\tag{L-95400.8}
\]

Consequently

\[
\mathcal A(X)=O(\log^C(2X))
\quad\Longleftrightarrow\quad
\mathcal C_e(X)=O(\log^C(2X))
\]

up to a fixed change of constant, uniformly over real or integer endpoints.

## 5. Mellin structure

For `Re z` initially large,

\[
\widehat K_0(z)
=\mathcal A_2(2^{-z-1/2})\widehat W(z),
\qquad
\widehat K_1(z)
=\mathcal B_2(2^{-z-1/2})\widehat W(z),
\tag{L-95400.9}
\]

where

\[
\mathcal A_2(t)=(1+t)(1-4t^2)^2,
\]

\[
\mathcal B_2(t)=-t(1-4t^2)(1+8t+4t^2),
\]

and

\[
\widehat W(z)
=(1-4^{1-z})\frac{z-1}{3(z+1)(z+2)(z+3)}.
\tag{L-95400.10}
\]

The annular kernels satisfy

\[
\boxed{
\widehat J_\nu(z)=q(z)\widehat K_\nu(z).
}
\tag{L-95400.11}
\]

Their logarithmic-coordinate forms are compactly supported in

\[
0\le u\le10\log2.
\]

Their Fourier transforms are therefore entire functions of exponential type, not compactly frequency supported. This distinction is load bearing in the large-sieve audit.

## 6. Boundary

```text
safe triple scale filter                  EXACT
factor-1024 annularization                EXACT
all ten exact Q(sqrt2) kernel bands       DEPOSITED
stable inverse, l1 mass 64/21             EXACT
Mellin multiplier and pole preservation   EXACT
Möbius cancellation on the annulus        OPEN / RH-BEARING
Riemann Hypothesis                        UNPROVEN
```
