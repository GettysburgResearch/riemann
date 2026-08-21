# L-103301 — The balanced homotopy increases only nonzero phase energy

Claim ID: `L-103301`  
Status: **PROVED EXACT PHASE THEOREM + SUBPOWER FINITE-EULER GAIN**  
Created: 2026-08-21  
Depends on: `L-103300`; classical Mertens product bounds  
RH status: **not assumed**

Fix one prime, put `a=1/p`, and evaluate the normalized factor of `L-103300`
on the logarithmic character

\[
V_p\mapsto z=e^{-i\theta},
\qquad |z|=1.
\]

Its multiplier is

\[
\boxed{
 m_{a,t}(z)
 =\frac{1-ta z-(1-t)a^2z^2}
 {(1-a)(1+a(1-t))}.
}
\tag{L-103301.1}
\]

Writing `c=cos(theta)`, exact differentiation yields

\[
\boxed{
\partial_t|m_{a,t}(e^{-i\theta})|^2
=
\frac{
2a(1-c)(1-2ac+a^2)(1-a(1-t))
}
{(1-a)^2(1+a(1-t))^3}
\ge0.
}
\tag{L-103301.2}
\]

The derivative vanishes exactly at the neutral phase `theta=0` modulo
`2 pi`; it is strictly positive at every other phase.

At the two endpoints,

\[
 m_{a,0}(z)=\frac{1-a^2z^2}{1-a^2},
\qquad
 m_{a,1}(z)=\frac{1-az}{1-a}.
\]

Since `1-a^2z^2=(1-az)(1+az)`, one gets the exact gain identity

\[
\boxed{
\frac{|m_{a,1}(z)|^2}{|m_{a,0}(z)|^2}
=\frac{(1+a)^2}{|1+az|^2}
\ge1.
}
\tag{L-103301.3}
\]

Moreover

\[
1\le |m_{a,t}(z)|
\le\frac{1+a}{1-a}.
\tag{L-103301.4}
\]

For a finite labelled prime set `Lambda`, the global multiplier is the product
of the local multipliers.  Hence every positive phase weight `w(gamma)` gives
one monotone spectral energy

\[
\mathcal E_{\Lambda,t}(f)
=\int_{\mathbb R}|\widehat f(\gamma)|^2
 \prod_{p\in\Lambda}
 |m_{1/p,t}(e^{-i\gamma\log p})|^2
 w(\gamma)d\gamma,
\tag{L-103301.5}
\]

with

\[
\boxed{
\partial_t\mathcal E_{\Lambda,t}(f)\ge0.
}
\tag{L-103301.6}
\]

The finite total phase gain satisfies

\[
\prod_{p\le Z}
\left(\frac{1+p^{-1}}{1-p^{-1}}\right)^2
\ll (\log Z)^4,
\tag{L-103301.7}
\]

with only an absolute extra factor for the second labelled `67`.  Thus the
entire carrier-normalized homotopy has only polylogarithmic source/phase
amplification.  The remaining loss in the live RH routes cannot be located in
the labelled phase amplitude; it occurs when this amplitude is collapsed onto
one physical multiplicative shell.
