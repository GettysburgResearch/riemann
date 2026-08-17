# Q4 FOCC annular Type-II hardening

Scientific status: **FOCC, OCHD and RH remain unproved.**

Frozen base: PR #573 at `0865242eb9dc0ed6094afc8a87a52b974c6f1307`.
The carry sibling is frozen and not imported.

## 1. Exact parent packet

Let

\[
W(x)=\begin{cases}
5x-63x^2+170x^3,&0\le x\le1/4,\\
(-x+3x^2-2x^3)/3,&1/4\le x\le1,\\
0,&x>1,
\end{cases}
\]

and

\[
A=(1,1,-8,-8,16,16),\qquad B=(0,-1,-8,0,32,16).
\]

Define

\[
K_0(x)=\sum_{r=0}^5A_r2^{-r/2}W(2^rx),\qquad
K_1(x)=\sum_{r=0}^5B_r2^{-r/2}W(2^rx).
\]

PR #573's critical packet is

\[
\mathcal C_e(X)=
\sum_{m\le X\atop m\text{ odd}}
\frac{\mu(m)}{\sqrt m}
[(\log m)K_0(m/X)+(\log2)K_1(m/X)].
\]

Only odd squarefree `m` contribute.

## 2. Safe annularization

Let `(SF)(X)=F(X/2)` and

\[
Q(S)=(I-S/2)(I-S/4)(I-S/8)
=I-7S/8+7S^2/32-S^3/64.
\]

Put

\[
J_\nu(x)=K_\nu(x)-\frac78K_\nu(2x)
+\frac7{32}K_\nu(4x)-\frac1{64}K_\nu(8x).
\]

Below `x=2^-7`, every active term of `K_0,K_1` lies in the common cubic branch.
For `k=1,2,3`, endpoint halving acts on `x^k` by `2^k`; the factor
`I-2^-k S` annihilates it. Hence

\[
J_0(x)=J_1(x)=0\qquad(0\le x\le2^{-10}).
\]

Therefore

\[
\mathcal A(X):=Q(S)\mathcal C_e(X)
=
\sum_{X/1024<m\le X\atop m\text{ odd}}
\frac{\mu(m)}{\sqrt m}
[(\log m)J_0(m/X)+(\log2)J_1(m/X)].
\]

The ten active intervals are `(2^(-j-1),2^-j]`, `0<=j<=9`; on each,
`J_0,J_1` are explicit cubics over `Q(sqrt(2))`. The companion generator
`exact_kernels.py` emits every coefficient exactly.

The inverse is

\[
Q(S)^{-1}=\prod_{k=1}^3\sum_{j\ge0}2^{-kj}S^j,
\]

with total coefficient mass

\[
\prod_{k=1}^3(1-2^{-k})^{-1}=64/21.
\]

Thus a polylog bound for `mathcal A` is equivalent to one for `mathcal C_e`.
The Mellin multiplier

\[
q(z)=\prod_{k=1}^3(1-2^{-z-k})
\]

has zeros only on `Re z=-1,-2,-3`, so no conclusion-producing pole is
cancelled.

## 3. Exact pair geometry

Put

\[
G_X(m)=\frac{(\log m)J_0(m/X)+(\log2)J_1(m/X)}{\sqrt m}.
\]

Then

\[
|\mathcal A(X)|^2=\mathcal D_A(X)+\mathcal X_A(X),
\]

where

\[
\mathcal D_A=\sum_mG_X(m)^2,
\qquad
\mathcal X_A=2\sum_{m<n}\mu(m)\mu(n)G_X(m)G_X(n).
\]

The parent bounds and the filter mass give

\[
|J_0|,|J_1|<1080,
\qquad
|G_X(m)|\le34560\frac{\log(2X)}{\sqrt X},
\]

so

\[
\mathcal D_A(X)\le34560^2\log^2(2X).
\]

If `m` and `n` lie in dyadic bands `I_i,I_j` and `m<n`, then

\[
1<n/m<2^{i-j+1}\le1024.
\]

Thus all 55 band pairs have bounded ratio.

For `H>=1`, the pairs with `0<n-m<=H` contribute at most

\[
2\cdot34560^2H\log^2(2X).
\]

For `H>=2`, the pairs with `(m,n)>=X/H` contribute at most

\[
4\cdot34560^2H\log^2(2X).
\]

Write `m=da,n=db`, with `d=(m,n)`. Since `m,n` are odd squarefree,
`a,b,d` are pairwise coprime odd squarefree integers and

\[
\mu(m)\mu(n)=\mu(a)\mu(b).
\]

The common divisor is sign free. Activation forces

\[
a<b<1024a.
\]

The sector `a<=H` also costs only `O(H log^2 X)` absolutely, because for fixed
`a,b` there are at most `X/b` admissible common divisors and
`sum_(a<b<1024a)1/b=O(1)`.

With `H=log^B(2X)`, the sole remaining pairs satisfy

\[
H<a<b<1024a,
\quad(a,b)=1,
\quad d<X/H,
\quad d(b-a)>H,
\]

with `(d,ab)=1` and all variables odd squarefree.

## 4. Type I/II and product forms

For squarefree `m>1`,

\[
\mu(m)\log m=-\sum_{p\mid m}(\log p)\mu(m/p).
\]

Hence the log channel is exactly

\[
-\sum_{p\text{ odd}}\frac{\log p}{\sqrt p}
\sum_{d\text{ odd squarefree}\atop(d,p)=1}
\frac{\mu(d)}{\sqrt d}J_0(pd/X).
\]

Splitting at `p=sqrt(X)` gives a literal Type I/II decomposition. In the
large-prime part, `d<sqrt(X)` and coprimality is automatic. The `J_1` boundary
channel remains explicit.

The gcd form is

\[
2\sum_{a<b<1024a\atop(a,b)=1}\mu(a)\mu(b)
\sum_{d\in\mathcal I_X(a,b)\atop(d,ab)=1}
\frac{\Gamma_X(da/X)\Gamma_X(db/X)}{d\sqrt{ab}}.
\]

Since `(a,b)=1`, setting `k=ab` converts the two signs to one `mu(k)` and a
finite divisor-pair weight. It does not remove reciprocal-zeta cancellation.

## 5. Mellin and large-sieve audit

Let

\[
M_{odd}(s)=\frac1{(1-2^{-s})\zeta(s)}.
\]

Then

\[
\int_1^\infty\mathcal A(X)X^{-z-1}dX
=-\widehat J_0(z)M_{odd}'(z+1/2)
+(\log2)\widehat J_1(z)M_{odd}(z+1/2).
\]

The exact factors are

\[
\widehat K_0(z)=(1+t)(1-4t^2)^2\widehat W(z),
\]

\[
\widehat K_1(z)=-t(1-4t^2)(1+8t+4t^2)\widehat W(z),
\quad t=2^{-z-1/2},
\]

and `widehat J_nu=q widehat K_nu`. Every off-line zeta pole survives.

In log coordinates, `J_nu(e^-u)` is supported in `0<=u<=10log2`, so its
Fourier transform is entire of exponential type, not frequency compact.
For a length-`X` annular Dirichlet polynomial,

\[
\int_{-T}^T|\sum c_m m^{-it}|^2dt
\le(2T+CX)\sum|c_m|^2.
\]

The `CX` term follows from frequency spacing `asymp1/X` and Hilbert's
inequality. A fixed or polylogarithmic Mellin window therefore cannot prove
FOCC.

## 6. Exact shortcut firewalls

A source-blind diagonal completion of `gg^T` requires a multiplier equal to
the number of active cores: after congruence, `lambda diag(g^2)-gg^T` becomes
`lambda I-ss^T`, whose final eigenvalue is `lambda-N`.

On `2/3<=x<=3/4`, `J_0=W>=2/81` and `J_1=0`. Replacing the actual Möbius signs
by `+1` on odd squarefree cores in this band leaves every local/passive/diagonal
quantity unchanged but produces output `gg sqrt(X)log X`. Thus local support,
diagonal energy, passive fibres, generic PSD, square functions, and prime-cube
log-Sobolev estimates cannot prove the deterministic bound.

## 7. Correct final theorem

Let `SACF` denote the balanced separated coprime correlation above, with
`H=log^B(2X)`. The closed sectors give

\[
\mathcal X_A(X)=\mathcal S_H(X)+O_B(\log^{B+2}(2X)).
\]

Because `mathcal D_A=O(log^2 X)`, a polylog bound for `SACF` is equivalent to a
polylog bound for `mathcal A`, hence for the PR #573 packet. The safe Mellin
multipliers preserve every pole in `Re z>0`, so

\[
SACF\Longrightarrow FOCC\Longrightarrow OCHD\Longrightarrow RH.
\]

This packet does **not** prove SACF or FOCC. The surviving theorem is a balanced,
separated, small-gcd, coprime Type-II Möbius correlation on ten exact Q4 bands.

```text
safe annularization                    PROVED EXACT
exact band/ratio/gcd geometry          PROVED EXACT
diagonal/near/large-gcd/small-Type-I   PROVED POLYLOG
Type I/II and Mellin normal forms      PROVED EXACT
source-blind shortcuts                 REFUTED AT CLAIMED SCOPE
SACF / FOCC / OCHD                     OPEN / RH-BEARING
Riemann Hypothesis                     UNPROVEN
```
