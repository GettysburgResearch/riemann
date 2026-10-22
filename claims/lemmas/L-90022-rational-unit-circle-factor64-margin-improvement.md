# L-90022 — A rational unit-circle dressing strengthens the factor-64 margin

Claim ID: `L-90022` (provisional range; branch-qualified)  
Title: Replacing the primitive-third-root dressing by `1+3y/4+y^2` preserves exact factor-64 support and zero safety while improving the phase-blind RH margin by a factor greater than two  
Status: **PROPOSED COMPLETE EXACT ANNULARIZATION/NORM LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Date: 2026-08-10  
Depends on: `L-90019`, `L-90020`  
Scope: improved factor-64 member; no claim of optimality within all degree-six zero-safe filters

## 1. Improved factor

Define

\[
\boxed{
 P_{64}^*(y)
 =(1-y)^2(1-y/\sqrt2)(1+y)
 \left(1+{3\over4}y+y^2\right).
}
\tag{L-90022.1}
\]

The quadratic roots satisfy

\[
 y^2+{3\over4}y+1=0,
\]

so their product is one and their discriminant is negative. Both roots lie exactly on the unit circle.

The coefficient expansion is

\[
\boxed{
\begin{aligned}
P_{64}^*(y)={}&1-\left({1\over4}+{1\over\sqrt2}\right)y
 +\left(-{3\over4}+{1\over4\sqrt2}\right)y^2\\
&+\left(-{3\over4}+{3\over4\sqrt2}\right)y^3
 +\left(-{1\over4}+{3\over4\sqrt2}\right)y^4\\
&+\left(1+{1\over4\sqrt2}\right)y^5
 -{1\over\sqrt2}y^6.
\end{aligned}}
\tag{L-90022.2}
\]

As before,

\[
 P_{64}^*(1)=(P_{64}^*)'(1)=P_{64}^*(\sqrt2)=0.
\tag{L-90022.3}

Thus every radical/ramp coordinate below `X/64` cancels exactly.

## 2. Zero safety

The filter roots are

```text
1 (double), sqrt(2), -1,
and the two roots of y^2+3y/4+1.
```

Every root has modulus at least one. Hence for a hypothetical off-line zero `rho`,

\[
 |2^{-(\rho-1/2)}|<1
 \quad\Longrightarrow\quad
 P_{64}^*(2^{-(\rho-1/2)})\ne0.
\tag{L-90022.4}

No RH-converse pole is lost.

## 3. Exact unit-circle norm certificate

For `y=e^{it}` and `x=cos t`,

\[
 \left|1+{3\over4}y+y^2\right|
 =\left|2x+{3\over4}\right|.
\]

Therefore

\[
\boxed{
 |P_{64}^*(e^{it})|^2
 =8(1-x)^2(1+x)
 \left({3\over2}-\sqrt2x\right)
 \left(2x+{3\over4}\right)^2.
}
\tag{L-90022.5}

Put

\[
 H_{64}^*(x)=11-|P_{64}^*(e^{it})|^2.
\]

Expanded in `Q(sqrt(2))[x]`,

\[
\boxed{
\begin{aligned}
H_{64}^*(x)={}&{17\over4}
 +\left(-{117\over4}+{9\sqrt2\over2}\right)x\\
&+\left(-{21\over4}+{39\sqrt2\over2}\right)x^2\\
&+\left({309\over4}+{7\sqrt2\over2}\right)x^3\\
&+\left(12-{103\sqrt2\over2}\right)x^4\\
&+(-48-8\sqrt2)x^5+32\sqrt2x^6.
\end{aligned}}
\tag{L-90022.6}

The retained verifier subdivides `[-1,1]` into 1,024 rational intervals and converts (L-90022.6) exactly to degree-six Bernstein form over the rational enclosure of `sqrt(2)`. Every lower endpoint is positive. Hence

\[
\boxed{
 \max_{|y|=1}|P_{64}^*(y)|^2<11.
}
\tag{L-90022.7}

## 4. Improved RH margin

At `y=1`, the two dressing factors contribute

\[
 (1+1)\left(1+{3\over4}+1\right)={11\over2}.
\]

Thus the filtered prime-square moat is

\[
\boxed{
 C_{64}^*
 ={11\over4}(1+\zeta(1/2))
 (1-1/\sqrt2)(\log2)^2<-0.178.
}
\tag{L-90022.8}

Under RH, (L-90022.7) gives the complete critical-zero bound

\[
\boxed{
 Z_{64}^*<\sqrt{11}(\log\xi)''(1/2)<0.154.
}
\tag{L-90022.9}

Consequently

\[
\boxed{
 C_{64}^*+Z_{64}^*<-0.024.
}
\tag{L-90022.10}

After the integer-friendly scaling by `4sqrt(2)`, the certified margin exceeds `0.13`.

## 5. Aligned integer expression

Multiplying the coefficients by `4sqrt(2)` gives

\[
\boxed{
\begin{aligned}
 \mathcal V_{64}^*(64N)={}&4\sqrt2 A_{64N}
 -(4+\sqrt2)A_{32N}\\
 &+(1-3\sqrt2)A_{16N}
 +(3-3\sqrt2)A_{8N}\\
 &+(3-\sqrt2)A_{4N}
 +(1+4\sqrt2)A_{2N}-4A_N.
\end{aligned}}
\tag{L-90022.11}

The arithmetic support remains exactly `[N,64N]`.

## 6. Comparison with the cyclotomic witness

The cyclotomic member of `L-90019` has the simpler factor `1+y+y^2` and is sufficient to attain the minimal annulus. The rational member (L-90022.1) has the same degree, support, and zero-safety, but its exact norm bound improves from `4` to `sqrt(11)` while sacrificing only a small part of the deterministic moat.

Thus:

```text
L-90019: simplest minimality witness;
L-90022: preferred factor-64 proof target.
```

## 7. Proof boundary

Closed exactly, subject to review:

1. rational unit-circle root geometry;
2. exact factor-64 annularization;
3. zero safety;
4. exact `Q(sqrt(2))` Bernstein norm bound;
5. improved fixed RH-side margin;
6. aligned integer expression.

Still open:

1. unconditional sign of the improved factor-64 scalar;
2. optimality among all zero-safe degree-six dressings;
3. RH.

Replay: `experiments/X-90019-factor64-rational/verify.py`.
