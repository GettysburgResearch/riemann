# Q4 FOCC annular Type-II hardening packet

**Scientific status: FOCC, OCHD and RH remain unproved.**


---

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


---

# L-95401 — Exact band, ratio and gcd decomposition closes the diagonal, near-diagonal and large-gcd sectors

Claim ID: `L-95401`  
Status: **PROPOSED COMPLETE ELEMENTARY DECOMPOSITION/BOUND THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-18  
Depends on: `L-95400`; PR #573 exact six-band source  
Scope: exact pair geometry and source-blind closed sectors; no separated coprime cancellation

## 1. Annular packet and FOCC square

Put

\[
G_X(m)
=
\frac{(\log m)J_0(m/X)+(\log2)J_1(m/X)}{\sqrt m}.
\tag{L-95401.1}
\]

Then

\[
\mathcal A(X)
=
\sum_{X/1024<m\le X\atop m\ \mathrm{odd}}
\mu(m)G_X(m).
\tag{L-95401.2}
\]

Write

\[
\mathcal D_A(X)=\sum_mG_X(m)^2
\]

and

\[
\boxed{
\mathcal X_A(X)
=2\sum_{m<n}\mu(m)\mu(n)G_X(m)G_X(n).
}
\tag{L-95401.3}
\]

Thus

\[
\boxed{
|\mathcal A(X)|^2=\mathcal D_A(X)+\mathcal X_A(X).
}
\tag{L-95401.4}
\]

Only odd squarefree cores contribute.

## 2. Exact dyadic activation geometry

Define the ten bands

\[
I_j(X)=\left(X2^{-j-1},X2^{-j}\right],
\qquad 0\le j\le9.
\tag{L-95401.5}
\]

On each band, `J_0,J_1` are fixed cubic polynomials with coefficients in `Q(sqrt(2))`. If

\[
m\in I_i(X),\qquad n\in I_j(X),\qquad m<n,
\]

then necessarily `i>=j` and

\[
\boxed{
1<\frac nm<2^{i-j+1}\le1024.
}
\tag{L-95401.6}
\]

Thus every surviving pair has bounded multiplicative ratio. The full correlation is the finite direct sum of the 55 band pairs

\[
0\le j\le i\le9.
\]

No tail or unbounded ratio remains.

## 3. Uniform annular bounds

PR #573 gives the safe bounds

\[
|K_0(x)|<512,
\qquad
|K_1(x)|<512.
\]

The absolute coefficient mass of the scale filter is

\[
1+\frac78+\frac7{32}+\frac1{64}=\frac{135}{64}.
\]

Therefore

\[
|J_0(x)|,|J_1(x)|<1080.
\tag{L-95401.7}
\]

On the annulus, `m>X/1024`, so

\[
\boxed{
|G_X(m)|
\le
34560\frac{\log(2X)}{\sqrt X}.
}
\tag{L-95401.8}
\]

Consequently

\[
\boxed{
\mathcal D_A(X)
\le
34560^2\log^2(2X).
}
\tag{L-95401.9}
\]

The annularizer improves the parent diagonal from `O(log^3 X)` to
`O(log^2 X)`.

## 4. Near-diagonal sector

For `H>=1`, define

\[
\mathcal N_H(X)
=
2\sum_{0<n-m\le H}
\mu(m)\mu(n)G_X(m)G_X(n).
\]

There are at most `XH` ordered pairs before imposing oddness or squarefreeness. Hence

\[
\boxed{
|\mathcal N_H(X)|
\le
2\cdot34560^2 H\log^2(2X).
}
\tag{L-95401.10}
\]

Thus every polylogarithmic-width near diagonal is already polylogarithmic without using Möbius cancellation.

## 5. Large-gcd sector

For `H>=2`, define

\[
\mathcal G_H(X)
=
2\sum_{m<n\atop (m,n)\ge X/H}
\mu(m)\mu(n)G_X(m)G_X(n).
\]

The number of such pairs is at most

\[
\sum_{d\ge X/H}
\left\lfloor\frac Xd\right\rfloor^2
\le
X^2\sum_{d\ge X/H}\frac1{d^2}
\le2XH.
\]

Therefore

\[
\boxed{
|\mathcal G_H(X)|
\le
4\cdot34560^2H\log^2(2X).
}
\tag{L-95401.11}
\]

Every polylogarithmic large-gcd sector is also closed source-blindly.

## 6. Exact gcd/common-divisor coordinates

For a surviving odd-squarefree pair, write

\[
d=(m,n),
\qquad
m=da,
\qquad
n=db.
\]

Then

\[
a,b,d\ \text{are odd squarefree and pairwise coprime},
\]

and

\[
\boxed{
\mu(m)\mu(n)=\mu(a)\mu(b).
}
\tag{L-95401.12}
\]

The common divisor carries no Möbius sign. The activation constraints become

\[
\frac{X}{1024a}<d\le\frac Xa,
\qquad
\frac{X}{1024b}<d\le\frac Xb.
\tag{L-95401.13}
\]

For `a<b`, a nonempty interval forces

\[
\boxed{b<1024a.}
\tag{L-95401.14}
\]

The remaining correlation is therefore an exact finite-ratio coprime Type-II form in `(a,b)`, averaged over a sign-free common divisor `d`.

## 7. Small reduced-variable Type I sector

In the gcd coordinates of Section 6, restrict first to `a<=H`.  For fixed
`a<b<1024a`, the number of admissible common divisors is at most `X/b`.
Using (L-95401.8), the absolute contribution is bounded by

\[
2\cdot34560^2\log^2(2X)
\sum_{a\le H}
\sum_{a<b<1024a}\frac1b.
\]

The inner harmonic interval has uniformly bounded mass, so

\[
\boxed{
|\mathcal T_{a\le H}(X)|
\ll H\log^2(2X).
}
\tag{L-95401.15}
\]

Thus every polylogarithmic small-`a` Type I sector is also closed without
Möbius cancellation.

## 8. Final balanced separated small-gcd core

Fix

\[
H=(\log(2X))^B
\]

for any fixed `B`. By (L-95401.10) and (L-95401.11), the only nontrivial sector is

\[
\boxed{
\begin{gathered}
X/1024<m<n\le X,\\
n-m>H,\\
(m,n)<X/H.
\end{gathered}
}
\tag{L-95401.16}
\]

Equivalently, in gcd coordinates,

\[
\boxed{
\begin{gathered}
(a,b)=1,
\quad H<a<b<1024a,\\
d<X/H,
\quad d(b-a)>H,\\
(a,d)=(b,d)=1,
\end{gathered}
}
\tag{L-95401.17}
\]

with all three variables odd squarefree.

This is the exact balanced separated small-gcd annular core. No same-core, near-diagonal, high-common-divisor, remote-ratio or inactive-band term remains.

## 9. Boundary

```text
ten exact activation bands                 CLOSED
all ratios                                 <=1024 EXACT
annular diagonal                           O(log^2 X)
polylog near diagonal                      CLOSED ABSOLUTELY
polylog large-gcd sector                   CLOSED ABSOLUTELY
polylog small-a Type I sector               CLOSED ABSOLUTELY
common-divisor sign cancellation           EXACT
separated small-gcd coprime core           OPEN / RH-BEARING
Riemann Hypothesis                         UNPROVEN
```


---

# L-95402 — Exact Type I/II, Mellin and frequency normal forms for annular FOCC

Claim ID: `L-95402`  
Status: **PROPOSED COMPLETE EXACT REWRITING THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-18  
Depends on: `L-95400/L-95401`  
Scope: source-faithful arithmetic normal forms; no claimed estimate for the final Type-II form

## 1. The logarithmic and boundary channels

Write

\[
\mathcal A(X)=\mathcal A_0(X)+(\log2)\mathcal A_1(X),
\]

where

\[
\mathcal A_0(X)
=
\sum_m\frac{\mu(m)\log m}{\sqrt m}J_0(m/X),
\tag{L-95402.1}
\]

and

\[
\mathcal A_1(X)
=
\sum_m\frac{\mu(m)}{\sqrt m}J_1(m/X).
\tag{L-95402.2}
\]

All sums are over odd squarefree `m` in the factor-1024 annulus.

## 2. Exact prime-divisor expansion

For every squarefree `m>1`,

\[
\boxed{
\mu(m)\log m
=-\sum_{p\mid m}(\log p)\mu(m/p).
}
\tag{L-95402.3}
\]

Consequently

\[
\boxed{
\mathcal A_0(X)
=-
\sum_{p\ \mathrm{odd}}
\frac{\log p}{\sqrt p}
\sum_{d\ \mathrm{odd\ squarefree}\atop(d,p)=1}
\frac{\mu(d)}{\sqrt d}
J_0(pd/X).
}
\tag{L-95402.4}
\]

Every activation remains literal through the factor `J_0(pd/X)`.

Choose the symmetric threshold

\[
U=\sqrt X.
\]

Then

\[
\mathcal A_0=\mathcal T_I+\mathcal T_{II},
\]

where

\[
\mathcal T_I
=-
\sum_{p\le U}
\frac{\log p}{\sqrt p}
\sum_{d\atop(d,p)=1}
\frac{\mu(d)}{\sqrt d}J_0(pd/X),
\tag{L-95402.5}
\]

and

\[
\boxed{
\mathcal T_{II}
=-
\sum_{p>U}
\frac{\log p}{\sqrt p}
\sum_{d<U}
\frac{\mu(d)}{\sqrt d}J_0(pd/X).
}
\tag{L-95402.6}
\]

In the second form, coprimality is automatic because `p>d`. The activation requires

\[
X/1024<pd\le X.
\]

Thus the large-prime part is an exact bilinear form with both variables at most `sqrt(X)` after the reciprocal change `p approximately X/d`; it is not an all-integer surrogate.

The `J_1` boundary channel has no `log m` factor and remains as the explicit lower-order reciprocal-zeta state (L-95402.2). It may not be deleted.

## 3. Mellin transform

Put

\[
M_{\mathrm{odd}}(s)
=
\sum_{m\ \mathrm{odd}}\frac{\mu(m)}{m^s}
=
\frac1{(1-2^{-s})\zeta(s)}.
\tag{L-95402.7}
\]

For `Re z` initially large, Mellin interchange gives

\[
\boxed{
\int_1^\infty\mathcal A(X)X^{-z-1}\,dX
=
-\widehat J_0(z)M_{\mathrm{odd}}'(z+\tfrac12)
+(\log2)\widehat J_1(z)M_{\mathrm{odd}}(z+\tfrac12).
}
\tag{L-95402.8}
\]

By `L-95400`,

\[
\widehat J_\nu(z)=q(z)\widehat K_\nu(z),
\]

where `q` has zeros only on `Re z=-1,-2,-3`. The finite Q4 factors do not cancel a pole coming from a zero

\[
\rho=z+\tfrac12,
\qquad \Re\rho>\tfrac12.
\]

Thus a polylogarithmic bound for `mathcal A` is conclusion-producing rather than a routine smoothing consequence.

## 4. Log-Fourier representation

Put

\[
\varphi_{\nu}(u)=J_\nu(e^{-u}),
\qquad 0\le u\le10\log2.
\]

Then

\[
\widehat J_\nu(\sigma+it)
=
\int_0^{10\log2}
\varphi_\nu(u)e^{-(\sigma+it)u}\,du.
\tag{L-95402.9}
\]

The transform is entire of exponential type `10 log 2`. It is not compactly supported in `t`.

For a dyadic annular Dirichlet polynomial

\[
P(t)=\sum_{X/1024<m\le X}c_m m^{-it},
\]

the elementary Hilbert-inequality expansion gives

\[
\boxed{
\int_{-T}^{T}|P(t)|^2dt
\le
(2T+C X)\sum_m|c_m|^2
}
\tag{L-95402.10}
\]

with an absolute constant `C`. Indeed

\[
|\log(m/n)|\ge\frac{|m-n|}{X}
\]

on the annulus, and the off-diagonal integral kernel is bounded by

\[
\frac2{|\log(m/n)|}
\le
\frac{2X}{|m-n|}.
\]

Hilbert's inequality completes the estimate.

At any fixed Mellin window `T=polylog(X)`, the `CX` term remains. Mellin compactness therefore supplies no source-blind polylogarithmic pointwise estimate.

## 5. Ratio form of the square

The annular square has the exact ratio-kernel form

\[
\mathcal X_A(X)
=
2\sum_{m<n}
\mu(m)\mu(n)
\frac{\Gamma_X(m/X)\Gamma_X(n/X)}{\sqrt{mn}},
\tag{L-95402.11}
\]

where

\[
\Gamma_X(x)
=(\log X+\log x)J_0(x)+(\log2)J_1(x).
\]

After `m=da,n=db`, this becomes

\[
\boxed{
2\sum_{a<b<1024a\atop(a,b)=1}
\mu(a)\mu(b)
\sum_{d\in\mathcal I_X(a,b)\atop(d,ab)=1}
\frac{
\Gamma_X(da/X)\Gamma_X(db/X)
}{d\sqrt{ab}},
}
\tag{L-95402.12}
\]

where `d,a,b` are odd squarefree and `mathcal I_X(a,b)` is the exact intersection of the two activation intervals from `L-95401`.

The inner common-divisor kernel is sign free. The only arithmetic signs left are the coprime parity character `mu(a)mu(b)`.

Because `(a,b)=1`, one may also put `k=ab`. Then

\[
\mu(a)\mu(b)=\mu(k),
\]

and the complete balanced Type-II core becomes the single-sign product form

\[
\boxed{
2\sum_{k\ \mathrm{odd\ squarefree}}\mu(k)
\sum_{a\mid k\atop a<k/a<1024a}
\sum_{d\in\mathcal I_X(a,k/a)\atop(d,k)=1}
\frac{
\Gamma_X(da/X)\Gamma_X(dk/(aX))
}{d\sqrt{k}}.
}
\tag{L-95402.13}
\]

The divisor-pair weight is explicit and finite. This reparametrization
collapses the two coprime signs to one Möbius sign but does not remove the
reciprocal-zeta obstruction.

## 6. Pretentious and dispersion boundary

The Type I/II and gcd rewritings preserve all six Q4 bands, but they do not remove the reciprocal-zeta source. Any estimate that replaces `mu` by absolute values loses a factor of order `sqrt(X)`. Any estimate depending only on the modulus-one character, local support, or the diagonal square is ruled out by `R-95400`.

A successful dispersion theorem must therefore estimate the complete coprime Type-II form (L-95402.12), including the `J_1` boundary and all band cross terms, at square-root strength. Standard zero-free-region or pretentious first-moment bounds do not reach that scale.

## 7. Boundary

```text
source-faithful Type I/II split             EXACT
large-prime bilinear form                   EXACT
J1 boundary retained                       EXACT
Mellin transform and pole audit             EXACT
log-Fourier entire/exponential type         EXACT
fixed-window large-sieve loss O(X)          EXACT
coprime finite-ratio dispersion estimate    OPEN / RH-BEARING
Riemann Hypothesis                          UNPROVEN
```


---

# R-95400 — Source-blind positive-kernel, square-function, Mellin and log-Sobolev shortcuts do not prove FOCC

Claim ID: `R-95400`  
Status: **PROPOSED COMPLETE EXACT SCOPE FIREWALL — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-18  
Depends on: `L-95400`–`L-95402`; PR #573 top-band firewall  
Scope: rejects generic inferences; does not refute arithmetic FOCC

## 1. Top-band sign mutation survives annularization

On

\[
\frac23\le x\le\frac34,
\]

all terms `K_nu(2^h x)` with `h>=1` vanish. Hence

\[
J_0(x)=K_0(x)=W(x),
\qquad
J_1(x)=0.
\tag{R-95400.1}
\]

Moreover

\[
W(x)=\frac{x(1-x)(2x-1)}3\ge\frac2{81}.
\tag{R-95400.2}
\]

Replace the actual Möbius signs temporarily by `+1` on odd squarefree cores in

\[
2X/3\le m\le3X/4.
\]

Every activation interval, same-core diagonal, passive fibre identity, kernel coefficient and local Sobolev norm remains unchanged. But the annular critical output is

\[
\gg
\sum_{2X/3\le m\le3X/4\atop m\ \mathrm{odd\ squarefree}}
\frac{\log m}{\sqrt m}
\gg\sqrt X\log X.
\tag{R-95400.3}
\]

The diagonal is only `O(log^2 X)`. Therefore none of the following data can imply FOCC without using the actual global Möbius signs:

```text
finite band support;
pointwise kernel bounds;
passive fibre energy;
same-core diagonal;
local activation geometry;
gcd counts;
modulus-one source labels.
```

## 2. Diagonal positive-kernel completion costs the number of active cores

Let `g=(G_X(m))` over the nonzero active cores. The source-blind matrix behind the desired inequality is

\[
\lambda\operatorname{diag}(g_m^2)-gg^T.
\]

On the support of `g`, congruence by `diag(|g_m|)^{-1}` gives

\[
\lambda I-\sigma\sigma^T,
\qquad
\sigma_m=\operatorname{sgn}(g_m).
\]

If `N_X` entries are active, the eigenvalues are

\[
\lambda\quad(N_X-1\text{ times}),
\qquad
\lambda-N_X\quad(1\text{ time}).
\]

Thus

\[
\boxed{
\lambda\operatorname{diag}(g_m^2)-gg^T\succeq0
\Longleftrightarrow
\lambda\ge N_X.
}
\tag{R-95400.4}
\]

Since `N_X` is of order `X`, a source-blind diagonal Schur completion pays the macroscopic factor that FOCC is designed to avoid.

## 3. Fixed-window Mellin almost-orthogonality loses `X`

The exact mean-square estimate (L-95402.10) contains the term

\[
CX\sum|c_m|^2.
\]

The logarithmic frequencies `log m` on a length-`X` annulus have minimum spacing of order `1/X`. Compact support of the log kernel makes its Fourier transform entire, not frequency compact. A fixed or polylogarithmic Mellin window therefore cannot turn the diagonal into a pointwise bound.

## 4. Prime-cube log-Sobolev normalization barrier

For a finite set of odd primes `P`, extend the annular function by zero to the Boolean prime cube:

\[
f(S)=G_X\left(\prod_{p\in S}p\right).
\]

The Möbius sum is the unnormalized top Walsh coefficient

\[
\sum_{S\subseteq P}(-1)^{|S|}f(S)
=2^{|P|}\widehat f(P).
\]

Parseval, Bonami hypercontractivity and the cube log-Sobolev inequality control the normalized coefficient `widehat f(P)`, but returning to the arithmetic sum introduces the factor `2^{|P|}`. The support probability is itself exponentially small, and the resulting source-blind bound is no stronger than the absolute annular mass. A closing inequality must use arithmetic organization beyond the uniform prime cube.

## 5. Near-diagonal and large-gcd closure does not propagate

`L-95401` closes pairs with

\[
|m-n|\le\log^B X
\]

or

\[
(m,n)\ge X/\log^B X.
\]

There is no monotone or positivity argument extending these estimates to separated coprime pairs. The sign-free common-divisor average in (L-95402.12) leaves the full character `mu(a)mu(b)` on the ratio variables.

## 6. What remains logically possible

This firewall does not refute:

```text
a source-specific coprime dispersion theorem;
a coefficient-one reflected/Jordan reserve;
a nonlocal arithmetic Carleson embedding;
an exact Type-II Bellman recurrence;
a direct proof of the annular Möbius sum.
```

It forbids presenting local passivity, diagonal energy, generic positive kernels, fixed-window large sieve, or Boolean hypercontractivity as such a theorem.


---

# T-95400 — Annular separated-coprime FOCC is the exact remaining Q4 gate

Claim ID: `T-95400`  
Status: **COMPLETE EQUIVALENCE/CONDITIONAL COMPOSITION — FOCC NOT PROVED**  
Created: 2026-08-18  
Depends on: `L-95400`–`L-95402`, `R-95400`; PR #573; frozen centered-cubic Mellin consumer  
RH status: **UNPROVEN**

## 1. Annular FOCC

Let

\[
\mathcal A(X)=\sum_m\mu(m)G_X(m),
\qquad
\mathcal D_A(X)=\sum_mG_X(m)^2,
\]

and

\[
\mathcal X_A(X)=\mathcal A(X)^2-\mathcal D_A(X).
\]

By `L-95401`,

\[
\mathcal D_A(X)=O(\log^2X).
\tag{T-95400.1}
\]

Therefore the following are equivalent, up to a fixed change of logarithmic exponent:

\[
\boxed{
\mathcal X_A(X)=O(\log^C X)
\Longleftrightarrow
\mathcal A(X)=O(\log^{C'}X).
}
\tag{T-95400.2}
\]

The forward implication uses

\[
\mathcal A^2=\mathcal D_A+\mathcal X_A;
\]

the reverse implication is immediate from the same identity.

By the stable inverse in `L-95400`, this is also equivalent to the original preconditioned packet bound for `mathcal C_e`, and hence to PR #573's FOCC statement.

## 2. Separated-coprime formulation

Fix any sufficiently large constant `B`, and put

\[
H=(\log(2X))^B.
\]

Let `mathcal S_H(X)` be the part of `mathcal X_A` with

\[
|m-n|>H,
\qquad
(m,n)<X/H,
\tag{T-95400.3}
\]

and, after writing `m=da,n=db`, with the additional balanced condition

\[
a>H,\qquad b>H.
\]

Then `L-95401` gives

\[
\boxed{
\mathcal X_A(X)
=
\mathcal S_H(X)
+O_B(\log^{B+2}(2X)).
}
\tag{T-95400.4}
\]

In gcd coordinates the remaining form is

\[
\boxed{
2\sum_{a<b<1024a\atop(a,b)=1}
\mu(a)\mu(b)
\sum_{d\in\mathcal I_X(a,b)\atop(d,ab)=1}
\frac{
\Gamma_X(da/X)\Gamma_X(db/X)
}{d\sqrt{ab}},
}
\tag{T-95400.5}
\]

restricted further by

\[
a>H,\qquad b>H,\qquad d<X/H,
\qquad
d(b-a)>H.
\]

Thus FOCC is equivalent to the following one theorem.

> **Separated Annular Coprime FOCC (`SACF`).**  
> For some fixed `A,B`,
> \[
> |\mathcal S_{(\log 2X)^B}(X)|
> \le C(\log 2X)^A
> \]
> for every sufficiently large `X`.

All kernel coefficients, activation domains, ratio constraints and common-divisor weights in SACF are explicit and finite.

## 3. Consumer

The Mellin transform of `mathcal A` is the frozen reciprocal-zeta transform multiplied by the safe factors

\[
(1+2^{-s})^2
\prod_{k=1}^{3}(1-2^{-s-k}).
\]

The first factor comes from PR #573's dyadic preconditioner; the second comes from `L-95400`. None has a zero in `Re s>0`.

Consequently SACF gives a polylogarithmic bound for the original centered-cubic critical observation. The frozen Mellin pole audit then excludes every zeta zero with real part greater than `1/2`, and functional-equation symmetry yields RH:

\[
\boxed{
\mathrm{SACF}
\Longrightarrow
\mathrm{FOCC}
\Longrightarrow
\mathrm{OCHD}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-95400.6}
\]

## 4. Exact scientific result of this pass

The following sectors are now removed from the open theorem:

```text
infinite dyadic depth;
remote ratios;
inactive Q4 bands;
same-core diagonal;
polylog-width near diagonal;
polylog large-gcd pairs;
polylog small-reduced-variable Type I pairs;
source-blind passive/PSD arguments;
fixed-window Mellin almost-orthogonality.
```

The remaining SACF theorem is a genuine separated, small-gcd, coprime Type-II Möbius correlation on ten exact Q4 activation bands.

## 5. Proof boundary

This packet does **not** prove SACF or FOCC. The requested unconditional Q4 closure was attempted through Type I/II, dispersion, large sieve, pretentious distance, Mellin almost-orthogonality, positive-kernel completion, square functions and logarithmic Sobolev inequalities. Every source-blind variant either incurs a power of `X` or reduces to the same reciprocal-zeta cancellation.

```text
safe annularization                      PROVED EXACT
exact band/ratio/gcd geometry            PROVED EXACT
diagonal/near/large-gcd sectors          PROVED POLYLOG
Type I/II and Mellin normal forms        PROVED EXACT
source-blind shortcuts                   REFUTED AT CLAIMED SCOPE
SACF separated coprime Type-II bound     OPEN / RH-BEARING
FOCC                                     OPEN / EQUIVALENT HERE
Riemann Hypothesis                       UNPROVEN
```


---

# M-95400 — Hostile review protocol for the annular FOCC hardening

Review in this order:

1. Freeze PR #573 at `0865242eb9dc0ed6094afc8a87a52b974c6f1307`.
2. Reconstruct `L-95400`, especially the endpoint-halving convention and the support cutoff `2^-10`.
3. Compare every band coefficient against `exact_kernels.json` using exact `Q(sqrt(2))` arithmetic.
4. Check the stable inverse coefficient mass `64/21` and the location of every Mellin zero.
5. Reconstruct the ten-band pair partition and the constants in `L-95401`.
6. Verify the gcd substitution preserves pairwise coprimality and removes the common-divisor sign exactly.
7. Check the Type I/II expansion retains `(d,p)=1`, the literal activation and the `J1` boundary.
8. Treat all numerical signs as reconnaissance only.
9. Treat `SACF` as open.

Immediate rejection conditions:

```text
one nonzero J0/J1 coefficient below x=2^-10;
a missing scale factor in Q(S);
a Mellin zero in Re z>0;
a ratio greater than 1024 in an active pair;
a common-divisor Mobius sign retained after m=da,n=db;
an omitted J1 boundary channel;
a diagonal or randomized estimate promoted to deterministic FOCC;
a fixed-window large-sieve estimate with the CX term deleted;
a source-blind PSD or log-Sobolev argument used after R-95400;
a floating scan represented as SACF, FOCC or RH.
```

The correct final status is:

```text
SACF / FOCC / OCHD / RH: open and conclusion-producing.
```


---

# O-95400 — Annular cross-correlation reconnaissance

Claim ID: `O-95400`  
Status: **FLOATING DISCOVERY ONLY — NON-PROBATIVE**  
Created: 2026-08-18  
Depends on: exact kernels in `X-95400`

The lightweight replay evaluates the exact piecewise formulas in ordinary double precision at selected integer endpoints. Representative values for

\[
\mathcal A(X),
\qquad
\mathcal D_A(X),
\qquad
\mathcal X_A(X)=\mathcal A(X)^2-\mathcal D_A(X)
\]

are:

```text
X=       256   A=  1.9060461908   D=  4.8548052343   Xcorr= -1.2217931527
X=     1,000   A=  0.3212714358   D=  8.9887748156   Xcorr= -8.8855594801
X=    10,000   A= -0.1120869776   D= 22.5595378563   Xcorr=-22.5469743657
X=   100,000   A= -0.4926485529   D= 44.5929654588   Xcorr=-44.3502628622
```

The observed negativity suggests the stronger inequality

\[
|\mathcal A(X)|^2\le\mathcal D_A(X)
\]

may be worth testing. No proof is supplied, and `R-95400` shows that no source-blind matrix argument can establish it.

The retained result records the scan separately from exact algebra. No finite scan is used in `T-95400`.


---

# Q4 FOCC attack: safe annularization and the separated coprime Type-II frontier

## Executive conclusion

The requested FOCC proof was attacked through all of the proposed coordinates. No complete unconditional proof survived the interface audit, so RH is not claimed.

The pass nevertheless produces a substantial exact reduction:

1. a safe three-factor scale filter kills the entire cubic small-`x` tail;
2. the Q4 packet becomes one factor-1024 annulus with ten exact `Q(sqrt(2))` bands;
3. the diagonal improves to `O(log^2 X)`;
4. every polylog-width near-diagonal and large-gcd sector is closed absolutely;
5. every remaining pair has bounded ratio and admits an exact pairwise-coprime `m=da,n=db` form;
6. the source-faithful Type I/II, Mellin and log-Fourier forms are explicit;
7. generic PSD, square-function, Mellin-window and log-Sobolev closures are ruled out.

The sole remaining theorem is the separated small-gcd coprime Type-II estimate `SACF`.

## Why the standard attacks did not close

### Type I/II

The log-weighted channel has an exact prime-divisor expansion, but the large-prime piece retains a bilinear Möbius sum at critical square-root normalization. Absolute values cost `sqrt(X)`.

### Dispersion and gcd

Common divisors are sign free and large gcd is harmless. After removing them, the full sign character remains on two coprime ratio variables. No local positivity follows.

### Large sieve / Mellin almost orthogonality

Logarithmic frequencies on a length-`X` annulus have spacing `1/X`; a fixed Mellin window retains an `O(X)` loss. Compact log support gives an entire Fourier transform, not compact frequency support.

### Pretentious distance

Nonpretentious first-moment bounds do not reach the critical square-root scale. The exact Mellin transform still contains `1/zeta(s+1/2)`.

### Positive-kernel completion

A diagonal Schur completion of the rank-one cross kernel requires a factor equal to the number of active cores. This reproduces the macroscopic wall.

### Square functions / log Sobolev

The Möbius source is a top parity character on the prime cube. Uniform-cube normalization introduces an exponential denormalization factor; the arithmetic support and global signs remain essential.

## Exact final chain

```text
SACF
 -> annular FOCC
 -> stable inverse to PR #573 packet
 -> OCHD critical centered-cubic bound
 -> frozen Mellin pole exclusion
 -> RH.
```

`SACF` is open and RH-bearing.

## Scientific status

```text
new exact reduction: yes
complete FOCC proof: no
complete unconditional RH proof: no
Riemann Hypothesis: unproved
```
