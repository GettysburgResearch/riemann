# L-102743 — Free labelled Wick second-chaos energy is polylogarithmic

Claim ID: `L-102743`  
Status: **PROVED UNCONDITIONALLY; PHYSICAL RESTRICTION OPEN**  
Created: 2026-08-23  
Depends on: `L-102742`; standard complex Khintchine inequality  
RH status: **not assumed**

Work on a finite horizon `Y` and retain one independent unit-circle variable
`z_l` for every labelled prime coordinate. Put

\[
 r_\ell=p_\ell^{-1/2},
 \qquad
 L(z)=\sum_\ell r_\ell z_\ell,
 \qquad
 V_Y=\sum_\ell r_\ell^2.
\]

The second labelled copy of `67` contributes one additional `1/67`. Hence

\[
 V_Y=\log\log(3Y)+O(1).
 \tag{L-102743.1}
\]

For `0<=t<=1`, let

\[
 W_t(z)=L(z)e^{-tL(z)/2}.
\]

## 1. Exact free second-chaos norm

The labelled convolution square has Hardy norm

\[
 \|W_t^2\|_{H^2}^2
 =\mathbb E\left[|L|^4e^{-2t\Re L}\right].
 \tag{L-102743.2}
\]

By Cauchy--Schwarz,

\[
 \mathbb E[|L|^4e^{-2t\Re L}]
 \le
 \left(\mathbb E|L|^8\right)^{1/2}
 \left(\mathbb E e^{-4t\Re L}\right)^{1/2}.
\]

The complex Khintchine inequality gives

\[
 \mathbb E|L|^8\le4!\,V_Y^4.
\]

Independence and `I_0(x)<=e^{x^2/4}` give

\[
\begin{aligned}
 \mathbb E e^{-4t\Re L}
 &=\prod_\ell I_0(4tr_\ell)\\
 &\le\exp(4t^2V_Y).
\end{aligned}
\]

Consequently, uniformly for `0<=t<=1`,

\[
 \boxed{
 \|W_t^2\|_{H^2}^2
 \le\sqrt{24}\,V_Y^2e^{2V_Y}
 \ll(\log(2Y))^C.
 }
 \tag{L-102743.3}
\]

The squared gauge `S` and Wick renormalizer `R` have polylogarithmic labelled
operator norm. Therefore the complete hard term

\[
 RS\int_0^1(1-t)W_t^2dt
\]

also has polylogarithmic **free labelled** energy.

## 2. Same-product factor-pair collapse

After labelled convolution but before distinct-product observation, one
physical integer `n` receives only factor-pair and duplicate-`67`
representations. Cauchy--Schwarz gives

\[
 |c(n)|^2
 \le C\tau(n)
 \sum_{de=n}|c_-(d)|^2|c_+(e)|^2.
\]

Since `tau(n)=Y^{o(1)}` uniformly for `n<=Y`, (L-102743.3) implies

\[
 \boxed{
 \sum_{n\le Y}|c(n)|^2=Y^{o(1)}
 }
 \tag{L-102743.4}
\]

for the same-product collapsed Wick second chaos. This is the chaos-gauge
counterpart of `L-102702` and `L-102604`.

## 3. Exact remaining loss

Equations (L-102743.3)--(L-102743.4) close:

```text
free labelled Fock energy;
Wick renormalizer and squared gauge;
root and complete first chaos;
same-product factor-pair multiplicity;
duplicate labelled owner multiplicity.
```

They do not control the restriction from independent prime phases to the single
physical logarithmic translation variable. The remaining term is exclusively
the overlap of **distinct integer products** inside the fixed ratio-eight
outer-ray window.

This physical restriction is named `WNC102743` in `T-102800`.