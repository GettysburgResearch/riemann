# L-26201 — Dyadic boundary exponential B-spline

Claim ID: `L-26201`  
Title: The exact carry Green function admits a positive compact dyadic B-spline filter and an aligned inverse-zeta source with positive Selberg data  
Status: **PROPOSED EXACT LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-02-r`  
Created: 2026-08-08  
Dependencies: retained algebra of `L-23601/L-23602`; elementary Laplace and Dirichlet convolution  
Scope: exact boundary filter and source identities; no asymptotic energy estimate

## 1. The causal Green function behind the carry profile

Put

\[
 q(t)=\left(4e^{t/2}-4-2t\right)\mathbf 1_{t\ge0}.
 \tag{L-26201.1}
\]

Then

\[
 q(0)=q'(0)=0,
 \qquad q(t)\ge0,
 \tag{L-26201.2}
\]

and

\[
 \boxed{
 \widehat q(z)=\int_0^\infty q(t)e^{-zt}dt
 =\frac1{z^2(z-\frac12)}.}
 \tag{L-26201.3}
\]

The logarithmic carry Green kernel is

\[
 h(t)=\left(8e^{t/2}-7-\frac32t\right)\mathbf 1_{t\ge0}.
 \tag{L-26201.4}
\]

Because the first two boundary traces of `q` vanish, ordinary distributional
differentiation introduces no boundary delta and

\[
 \boxed{
 h=(\partial_t+\tfrac12)(\partial_t+\tfrac32)q.}
 \tag{L-26201.5}
\]

Thus the failed Hankel profile is a second differential image of a positive
causal Green function.

## 2. A positive compact exponential B-spline

Let

\[
 L=\log2,
 \qquad
 (\tau f)(t)=f(t-L),
 \tag{L-26201.6}
\]

with every causal function extended by zero to the negative half-line. Define

\[
 \chi_0(t)=\mathbf1_{[0,L]}(t),
 \qquad
 \chi_{1/2}(t)=e^{t/2}\mathbf1_{[0,L]}(t).
 \tag{L-26201.7}
\]

Their transforms are

\[
 \widehat\chi_0(z)=\frac{1-2^{-z}}z,
 \qquad
 \widehat\chi_{1/2}(z)
 =\frac{1-\sqrt2\,2^{-z}}{z-\frac12}.
 \tag{L-26201.8}
\]

Set

\[
 \boxed{
 \mathcal B_0
 =(I-\sqrt2\,\tau)(I-\tau)^2q.}
 \tag{L-26201.9}
\]

Equations (L-26201.3) and (L-26201.8) give

\[
 \boxed{
 \mathcal B_0
 =\chi_0*\chi_0*\chi_{1/2}.}
 \tag{L-26201.10}
\]

Consequently

\[
 \boxed{
 \mathcal B_0(t)\ge0,
 \qquad
 \operatorname{supp}\mathcal B_0=[0,3L].}
 \tag{L-26201.11}
\]

This is genuine convolution positivity. It does not invoke positivity of a
Hankel kernel `f(x+y)`.

The complete hierarchy is

\[
 \boxed{
 \mathcal B_R
 =\chi_0^{*(R+2)}*\chi_{1/2}^{*(R+1)}
 \ge0,
 \qquad R\ge0.}
 \tag{L-26201.12}
\]

It is supported on `[0,(2R+3)L]` and has transform

\[
 \boxed{
 \widehat{\mathcal B_R}(z)
 =\frac{(1-2^{-z})^{R+2}
        (1-\sqrt2\,2^{-z})^{R+1}}
       {z^{R+2}(z-\frac12)^{R+1}}.}
 \tag{L-26201.13}
\]

## 3. Exact source alignment

Use the zeta coordinate

\[
 s=z+\frac12,
 \qquad x=2^{-s}.
 \tag{L-26201.14}
\]

Define

\[
 \boxed{
 R_R(x)=(1-\sqrt2x)^{R+2}(1-2x)^{R+1}}
 \tag{L-26201.15}
\]

and the multiplicative coefficient sequence `b_R` by

\[
 \boxed{
 B_R(s):=\sum_{n\ge1}\frac{b_R(n)}{n^s}
 =\frac{R_R(2^{-s})}{\zeta(s)}.}
 \tag{L-26201.16}
\]

Let `q_R` be the positive causal convolution kernel with transform

\[
 \widehat q_R(z)=\frac1{z^{R+2}(z-\frac12)^{R+1}}.
 \tag{L-26201.17}
\]

Then the same function has two exact source representations:

\[
 \boxed{
 U_R(t)
 =\sum_{n\ge1}\frac{\mu(n)}{\sqrt n}
   \mathcal B_R(t-\log n)
 =\sum_{n\ge1}\frac{b_R(n)}{\sqrt n}
   q_R(t-\log n).}
 \tag{L-26201.18}
\]

Every sum is finite at fixed `t` in the first representation. The equality is
an identity of Laplace transforms.

For `R=0`,

\[
 R_0(x)=(1-2x)(1-\sqrt2x)^2
 =1-(2+2\sqrt2)x+(2+4\sqrt2)x^2-4x^3,
 \tag{L-26201.19}
\]

so

\[
\begin{aligned}
 b_0(n)={}&\mu(n)
 -(2+2\sqrt2)\mathbf1_{2\mid n}\mu(n/2)\\
 &+(2+4\sqrt2)\mathbf1_{4\mid n}\mu(n/4)
 -4\mathbf1_{8\mid n}\mu(n/8).
\end{aligned}
 \tag{L-26201.20}
\]

## 4. Positive inverse and positive generalized prime data

The inverse Dirichlet series is

\[
 A_R(s)=\frac{\zeta(s)}{R_R(2^{-s})}.
 \tag{L-26201.21}
\]

At every odd prime it has the ordinary positive geometric Euler factor. At the
prime `2` its local factor is

\[
 \boxed{
 \frac1{(1-x)(1-\sqrt2x)^{R+2}(1-2x)^{R+1}},}
 \tag{L-26201.22}
\]

whose Taylor coefficients are all nonnegative. Therefore every Dirichlet
coefficient of `A_R` is nonnegative.

If

\[
 -\frac{A_R'}{A_R}(s)
 =\sum_{n\ge1}\frac{\Lambda_R(n)}{n^s},
 \tag{L-26201.23}
\]

then `Lambda_R` is supported on prime powers and is nonnegative. Explicitly,
for `k>=1`,

\[
 \boxed{
 \Lambda_R(2^k)
 =\left[1+(R+2)2^{k/2}+(R+1)2^k\right]\log2,}
 \tag{L-26201.24}
\]

while `Lambda_R(p^k)=log p` at odd prime powers.

Hence the generalized Selberg coefficient identity

\[
 \boxed{
 b_R*(a_R\log^2)
 =\Lambda_R\log+\Lambda_R*\Lambda_R}
 \tag{L-26201.25}
\]

has coefficientwise nonnegative forcing on its right side.

## 5. A bounded digital dual

Let

\[
 \varepsilon(n)=(-1)^{n+1}.
 \tag{L-26201.26}
\]

Its Dirichlet series is the eta function

\[
 \sum_{n\ge1}\frac{\varepsilon(n)}{n^s}
 =(1-2^{1-s})\zeta(s).
 \tag{L-26201.27}
\]

Therefore

\[
 \boxed{
 \varepsilon*b_R=d_R,}
 \tag{L-26201.28}
\]

where `d_R` is supported on the finite set of powers of two occurring in

\[
 \boxed{
 D_R(x)=(1-2x)R_R(x).}
 \tag{L-26201.29}
\]

For `R=0`,

\[
 D_0(x)
 =1-(4+2\sqrt2)x+(6+8\sqrt2)x^2
  -(8+8\sqrt2)x^3+8x^4.
 \tag{L-26201.30}
\]

The cumulative digital coefficient is bounded and nonnegative:

\[
 \boxed{
 \sum_{n\le N}\varepsilon(n)
 =\begin{cases}1,&N\text{ odd},\\0,&N\text{ even}.
 \end{cases}}
 \tag{L-26201.31}
\]

Thus the aligned source has simultaneously:

```text
positive compact boundary B-spline;
positive inverse coefficients;
positive generalized Selberg forcing;
finite dyadic forcing;
bounded digital endpoint partial sums.
```

## 6. Safe-zero and carry interfaces

Every zero of `R_R(2^{-s})` lies on `Re(s)=1/2` or `Re(s)=1`.
Consequently the multiplier cannot cancel a hypothetical zeta zero in

\[
 \frac12<\Re s<1.
 \tag{L-26201.32}
\]

The boundary-spline signal `U_R` is therefore a genuine RH detector.

For `R=0`, let

\[
 g(t)=\mathfrak C(e^t)
 =\sum_{n\ge1}\frac{\mu(n)}{\sqrt n}h(t-\log n).
 \tag{L-26201.33}
\]

Equations (L-26201.5), (L-26201.9), and commutation of constant-coefficient
differential and translation operators give

\[
 \boxed{
 (I-\sqrt2\tau)(I-\tau)^2g
 =(\partial_t+\tfrac12)(\partial_t+\tfrac32)U_0.}
 \tag{L-26201.34}
\]

Thus the new state is an exact boundary-spline integration of the retained
carry profile, not an unrelated RH-equivalent transform.

## 7. Proof boundary

Closed exactly:

- the positive compact exponential B-spline;
- the high-order hierarchy;
- the dual source representations;
- the positive inverse and generalized prime coefficients;
- the finite eta convolution and digital endpoint ledger;
- noncancellation of open-strip zeta zeros;
- the differential bridge to the exact carry profile.

Not proved here:

- a subexponential energy bound for `U_R`;
- the source-specific reflected recurrence estimate of `L-26203`;
- RH.
