# L-90017 — A zero-safe radix-three quartic filter annularizes the endpoint to factor 81

Claim ID: `L-90017` (provisional range; branch-qualified)  
Title: Adding one unit-circle zero to the critical-annular filter reduces the exact arithmetic window to `[N,81N]`, retains every off-line zero, and admits an exact phase-blind norm certificate  
Status: **PROPOSED COMPLETE EXACT ANNULARIZATION/NORM LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Date: 2026-08-10  
Depends on: `L-90004`, `L-90015`, `L-90016`  
Scope: exact finite filter, pole audit, and unit-circle norm certificate; no unconditional endpoint sign

## 1. The quartic filter

Put

\[
\boxed{
 P_3(y)=(1-y)^2(1-y/\sqrt3)(1+y).
}
\tag{L-90017.1}
\]

Its coefficient expansion is

\[
\boxed{
\begin{aligned}
 P_3(y)
={}&1-(1+1/\sqrt3)y+(-1+1/\sqrt3)y^2\\
&+(1+1/\sqrt3)y^3-(1/\sqrt3)y^4.
\end{aligned}}
\tag{L-90017.2}
\]

Define

\[
\boxed{
\begin{aligned}
 \mathcal U_3(X)
={}&A(X)-(1+1/\sqrt3)A(X/3)\\
&+(-1+1/\sqrt3)A(X/9)\\
&+(1+1/\sqrt3)A(X/27)
 -(1/\sqrt3)A(X/81).
\end{aligned}}
\tag{L-90017.3}
\]

The factors in (L-90017.1) give

\[
 P_3(1)=P_3'(1)=0,
 \qquad
 P_3(\sqrt3)=0.
\tag{L-90017.4}
\]

Thus the two logarithmic scale modes and the critical `X^{-1/2}` seed mode all cancel exactly.

## 2. Exact factor-81 support

For every integer `m<=X/81`, the same expansion as in `L-90015` gives

\[
 b_{X/3^j}(m)
 =2\sqrt m\left(\log{X\over m}-j\log3-2\right)
 +{4m\,3^{j/2}\over\sqrt X}.
\]

Equations (L-90017.4) therefore imply

\[
 \sum_{j=0}^4 [y^j]P_3(y)\,b_{X/3^j}(m)=0.
\tag{L-90017.5}
\]

The prime ramp has only the constant and linear-in-`j` modes, so it also cancels for every prime `p<=X/81`. Consequently

\[
\boxed{
 \mathcal U_3(X)
 \text{ has exact radical/ramp support in }
 (X/81,X].
}
\tag{L-90017.6}
\]

At `X=81N`, multiplication by `3` gives the pure integer-scale expression

\[
\boxed{
\begin{aligned}
 \mathcal V_3(81N)
={}&3A_{81N}-(3+\sqrt3)A_{27N}\\
&+(-3+\sqrt3)A_{9N}\\
&+(3+\sqrt3)A_{3N}-\sqrt3 A_N.
\end{aligned}}
\tag{L-90017.7}
\]

It uses only the annulus `N<m<=81N` in radical-switching coordinates.

## 3. Transform and zero safety

Scaling gives

\[
\boxed{
 \widehat{\mathcal U_3}(z)
 =P_3(3^{-z})\widehat A(z).
}
\tag{L-90017.8}
\]

The roots of `P_3` are

\[
 1\quad\text{(double)},
 \qquad -1,
 \qquad \sqrt3.
\]

If `rho` is a hypothetical off-line zero and `z_rho=rho-1/2`, then

\[
 |3^{-z_\rho}|<1.
\]

Every filter root has modulus at least one, so

\[
\boxed{P_3(3^{-z_\rho})\ne0.}
\tag{L-90017.9}
\]

Hence every off-line pole survives. The extra root `-1` can annihilate only a mode already on the critical line; it creates no RH-converse blind spot.

## 4. Exact unit-circle norm certificate

Let `y=e^{it}` and `x=cos t`. Direct multiplication gives

\[
\boxed{
 |P_3(e^{it})|^2
 =8(1-x)^2(1+x)
 \left({4\over3}-{2x\over\sqrt3}\right).
}
\tag{L-90017.10}
\]

Put

\[
 H(x)=18-|P_3(e^{it})|^2.
\]

Expanded in `Q(sqrt(3))[x]`,

\[
\begin{aligned}
H(x)={}&{22\over3}
 +\left({32\over3}+{16\sqrt3\over3}\right)x\\
&+\left({32\over3}-{16\sqrt3\over3}\right)x^2\\
&+\left(-{32\over3}-{16\sqrt3\over3}\right)x^3
 +{16\sqrt3\over3}x^4.
\end{aligned}
\tag{L-90017.11}
\]

Subdivide `[-1,1]` into the four half-unit intervals. On each interval, convert (L-90017.11) exactly to the degree-four Bernstein basis. Using the rational enclosure

\[
 {1732050807568877\over10^{15}}
 <\sqrt3<
 {1732050807568878\over10^{15}},
\]

every Bernstein coefficient has positive lower endpoint; the global minimum certificate is

\[
 {1183566530771777\over7036886020193280}>{1\over6}.
\]

Therefore

\[
\boxed{
 \max_{|y|=1}|P_3(y)|^2<18,
 \qquad
 \max_{|y|=1}|P_3(y)|<\sqrt{18}.
}
\tag{L-90017.12}
\]

This is an exact algebraic certificate, not a floating maximum search.

## 5. Prime-power moat and certified RH margin

Near the origin,

\[
 P_3(3^{-z})
 =2(1-1/\sqrt3)(\log3)^2z^2+O(z^3).
\]

Combining with the third-order prime-square pole of `Ahat`, the filtered moat is

\[
\boxed{
 C_3
 =(1+\zeta(1/2))(1-1/\sqrt3)(\log3)^2
 =-0.2348344907443489\ldots .
}
\tag{L-90017.13}
\]

Under RH, with

\[
 \Sigma_\xi=(\log\xi)''(1/2),
\]

the entire critical-zero series has absolute value at most

\[
\boxed{
 Z_3=\sqrt{18}\,\Sigma_\xi
 =0.1960499542311713\ldots .
}
\tag{L-90017.14}
\]

Thus

\[
\boxed{
 C_3+Z_3
 =-0.0387845365131775\ldots<0.
}
\tag{L-90017.15}
\]

After the integer-friendly factor `3`, the certified margin is

\[
\boxed{
 -3(C_3+Z_3)
 =0.1163536095395325\ldots .
}
\tag{L-90017.16}
\]

## 6. Proof boundary

Closed exactly, subject to review:

1. the quartic filter and moments;
2. exact factor-81 annularization;
3. off-line zero preservation;
4. the exact `Q(sqrt(3))` Bernstein norm certificate;
5. the negative moat and positive phase-blind RH margin.

Still open:

1. unconditional eventual sign of the factor-81 scalar;
2. RH.

Replay: `experiments/X-90017-radix3-quartic/verify.py`.
