# L-90019 — A zero-safe radix-two cyclotomic filter annularizes the endpoint to factor 64

Claim ID: `L-90019` (provisional range; branch-qualified)  
Title: The cubic cyclotomic dressing `(1+y)(1+y+y^2)` turns the radix-two critical filter into an exact factor-64 annularizer, retains every off-line zero, and has unit-circle norm below four  
Status: **PROPOSED COMPLETE EXACT ANNULARIZATION/NORM LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Date: 2026-08-10  
Depends on: `L-90004`, `L-90015`, `L-90016`  
Scope: exact factor-64 filter, pole audit, and algebraic norm certificate; no unconditional endpoint sign

## 1. The filter

Put

\[
\boxed{
 P_{64}(y)
 =(1-y)^2(1-y/\sqrt2)(1+y)(1+y+y^2).
}
\tag{L-90019.1}
\]

The product excluding the critical factor simplifies:

\[
 (1-y)^2(1+y)(1+y+y^2)=1-y^2-y^3+y^5.
\]

Therefore

\[
\boxed{
\begin{aligned}
 P_{64}(y)={}&1-{y\over\sqrt2}-y^2
 +\left(-1+{1\over\sqrt2}\right)y^3\\
 &+{y^4\over\sqrt2}+y^5-{y^6\over\sqrt2}.
\end{aligned}}
\tag{L-90019.2}
\]

Define the unscaled filtered endpoint

\[
\boxed{
\begin{aligned}
 \mathcal U_{64}(X)={}&A(X)-{1\over\sqrt2}A(X/2)-A(X/4)\\
 &+\left(-1+{1\over\sqrt2}\right)A(X/8)
 +{1\over\sqrt2}A(X/16)\\
 &+A(X/32)-{1\over\sqrt2}A(X/64).
\end{aligned}}
\tag{L-90019.3}
\]

The factors in (L-90019.1) give

\[
 P_{64}(1)=P_{64}'(1)=0,
 \qquad
 P_{64}(\sqrt2)=0.
\tag{L-90019.4}
\]

Hence the constant/logarithmic scale modes and the critical seed mode all cancel.

## 2. Exact factor-64 support

The proof of `L-90015` applies with radix two and degree six. For every integer `m<=X/64`,

\[
 \sum_{j=0}^6[y^j]P_{64}(y)\,b_{X/2^j}(m)=0,
\]

and for every prime `p<=X/64`,

\[
 \sum_{j=0}^6[y^j]P_{64}(y)\,w_{X/2^j}(p)=0.
\]

Therefore

\[
\boxed{
 \mathcal U_{64}(X)
 \text{ has exact radical/ramp support in }
 (X/64,X].
}
\tag{L-90019.5}
\]

At `X=64N`, multiplication by `sqrt(2)` gives the aligned expression

\[
\boxed{
\begin{aligned}
 \mathcal V_{64}(64N)={}&\sqrt2 A_{64N}-A_{32N}
 -\sqrt2 A_{16N}\\
 &+(1-\sqrt2)A_{8N}+A_{4N}
 +\sqrt2 A_{2N}-A_N.
\end{aligned}}
\tag{L-90019.6}
\]

It uses only radical/ramp data in `[N,64N]`.

## 3. Zero safety

The Mellin multiplier is

\[
\boxed{
 \widehat{\mathcal U_{64}}(z)
 =P_{64}(2^{-z})\widehat A(z).
}
\tag{L-90019.7}
\]

The filter roots are

```text
1, 1, sqrt(2), -1, exp(2 pi i/3), exp(-2 pi i/3).
```

Every root has modulus at least one. If `rho` is a hypothetical off-line zero and `z_rho=rho-1/2`, then

\[
 |2^{-z_\rho}|<1.
\]

Thus

\[
\boxed{P_{64}(2^{-z_\rho})\ne0,}
\tag{L-90019.8}
\]

so every off-line pole survives.

## 4. Exact unit-circle norm certificate

Let `y=e^{it}` and `x=cos t`. The cyclotomic factor gives

\[
 |1+y+y^2|=|1+2x|.
\]

Consequently

\[
\boxed{
 |P_{64}(e^{it})|^2
 =8(1-x)^2(1+x)
 \left({3\over2}-\sqrt2 x\right)(1+2x)^2.
}
\tag{L-90019.9}
\]

Put

\[
 H_{64}(x)=16-|P_{64}(e^{it})|^2.
\]

Expanded in `Q(sqrt(2))[x]`,

\[
\boxed{
\begin{aligned}
H_{64}(x)={}&4+(-36+8\sqrt2)x
 +(12+24\sqrt2)x^2\\
&+(84-8\sqrt2)x^3-56\sqrt2 x^4\\
&-48x^5+32\sqrt2 x^6.
\end{aligned}}
\tag{L-90019.10}
\]

The retained verifier subdivides `[-1,1]` into 64 rational intervals, converts (L-90019.10) exactly to degree-six Bernstein form on each interval, and bounds `sqrt(2)` by the rational enclosure

\[
 {1414213562373095\over10^{15}}
 <\sqrt2<
 {1414213562373096\over10^{15}}.
\]

Every Bernstein lower endpoint is strictly positive. Therefore

\[
\boxed{
 \max_{|y|=1}|P_{64}(y)|^2<16,
 \qquad
 \max_{|y|=1}|P_{64}(y)|<4.
}
\tag{L-90019.11}
\]

This is an exact algebraic certificate, not a floating grid claim.

## 5. Prime-square moat and RH margin

Near the origin,

\[
 P_{64}(2^{-z})
 =6(1-1/\sqrt2)(\log2)^2z^2+O(z^3).
\]

Thus the filtered prime-square moat is

\[
\boxed{
 C_{64}
 =3(1+\zeta(1/2))(1-1/\sqrt2)(\log2)^2
 <-0.194.
}
\tag{L-90019.12}
\]

Under RH the entire critical-zero series is bounded absolutely by

\[
\boxed{
 Z_{64}<4(\log\xi)''(1/2)<0.185.
}
\tag{L-90019.13}
\]

Hence

\[
\boxed{
 C_{64}+Z_{64}<-0.009.
}
\tag{L-90019.14}
\]

After multiplication by `sqrt(2)`, the aligned scalar has an RH-side margin greater than `0.012`.

## 6. Proof boundary

Closed exactly, subject to review:

1. the cyclotomic filter and coefficient expansion;
2. exact factor-64 annularization;
3. off-line zero preservation;
4. the exact `Q(sqrt(2))` Bernstein norm certificate;
5. the strict phase-blind RH margin.

Still open:

1. unconditional eventual sign of the factor-64 scalar;
2. RH.

Replay: `experiments/X-90018-factor64-cyclotomic/verify.py`.
