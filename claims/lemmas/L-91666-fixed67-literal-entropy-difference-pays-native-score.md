# L-91666 — The fixed-67 literal entropy difference pays the full native score difference

Claim ID: `L-91666`  
Status: **PROVED ANALYTIC + DIRECTED FINITE THEOREM**  
Created: 2026-08-14  
Supersedes: the index-only file `L-91664`  
RH status: **unproved; this is one load-bearing score lemma**

## 1. Statement

For real `Y>=1`, put

\[
 E(Y)=\sum_{2\le m\le Y}
 \frac{\log m}{\sqrt m}\log\frac Ym,
 \qquad E(Y)=0\quad(1\le Y<2).
\tag{L-91666.1}
\]

Then, for every real `Y>=67`,

\[
\boxed{
 E(Y)-E(Y/67)
 \ge 5\left(\sqrt Y-\sqrt{Y/67}\right).
}
\tag{L-91666.2}
\]

The inequality is strict. At the first endpoint,

\[
\boxed{
 E(67)-5(\sqrt{67}-1)
 =3.2764007195549669\ldots>3.
}
\tag{L-91666.3}
\]

Thus the exact component-row difference `Q_Y-Q_(Y/67)` pays the complete
row-budgeted native score difference with coefficient one.

## 2. Cell derivative

Let

\[
 f(m)=\frac{\log m}{\sqrt m},
 \qquad
 A(N)=\sum_{2\le m\le N}f(m),
\tag{L-91666.4}
\]

and define

\[
 F(Y)=E(Y)-E(Y/67)
 -5\left(\sqrt Y-\sqrt{Y/67}\right).
\tag{L-91666.5}
\]

On an open cell `N<Y<N+1`, put `M=floor(N/67)`. Entering summands have
zero logarithmic value, so `F` is continuous at every integer and every child
activation. Direct differentiation gives

\[
\boxed{
 F'(Y)=\frac{A(N)-A(M)}Y
 -\frac5{2\sqrt Y}\left(1-\frac1{\sqrt{67}}\right).
}
\tag{L-91666.6}
\]

Consequently, on this cell it is enough to prove

\[
 A(N)-A(M)>
 \frac52\left(1-67^{-1/2}\right)\sqrt{N+1}.
\tag{L-91666.7}
\]

## 3. Complete finite corridor

The companion exact checker verifies (L-91666.7) for every

\[
 67\le N\le468.
\]

It uses only integer arithmetic, directed decimal square-root intervals, and
positive-tail atanh bounds for logarithms. There are `402` cells. The smallest
directed margin is attained at `N=67` and satisfies

\[
\boxed{
 A(67)-A(1)
 -\frac52(1-67^{-1/2})\sqrt{68}
 >22.1747542920858>22.
}
\tag{L-91666.8}
\]

The same replay gives the directed base (L-91666.3). Therefore `F` is strictly
increasing on `[67,469]` and positive there.

## 4. Analytic tail

Assume `Y>=469`, and put

\[
 N=\lfloor Y\rfloor,
 \qquad M=\lfloor Y/67\rfloor.
\]

Then `M+1>=8`. The function

\[
 f(x)=\frac{\log x}{\sqrt x}
\]

is decreasing for `x>=e^2`, hence on `[M+1,N+1]`. Therefore

\[
 A(N)-A(M)
 \ge\int_{M+1}^{N+1}\frac{\log x}{\sqrt x}\,dx.
\tag{L-91666.9}
\]

Let

\[
 P(x)=2\sqrt x\log x-4\sqrt x,
 \qquad P'(x)=\frac{\log x}{\sqrt x}.
\tag{L-91666.10}
\]

Since `N+1>Y`, `M+1<=Y/67+1`, and `P` is increasing for `x>1`,

\[
 A(N)-A(M)
 \ge P(Y)-P(Y/67+1).
\tag{L-91666.11}
\]

Put

\[
 c=\frac52(1-67^{-1/2}),
 \qquad
 G(Y)=P(Y)-P(Y/67+1)-c\sqrt Y.
\tag{L-91666.12}
\]

The directed base is

\[
\boxed{G(469)>131.798262054325>100.}
\tag{L-91666.13}
\]

Moreover

\[
\begin{aligned}
 \sqrt Y\,G'(Y)
 &\ge
 \log Y-67^{-1/2}\log(Y/67+1)-\frac c2\\
 &\ge
 (1-67^{-1/2})(\log Y-5/4)>0
 \qquad(Y\ge469).
\end{aligned}
\tag{L-91666.14}
\]

Thus `G` is positive and increasing. Equations (L-91666.6),
(L-91666.11), and (L-91666.12) give `F'(Y)>0` on the complete analytic tail.
Together with Section 3 this proves (L-91666.2).

## 5. Packet consequence

Let a positive source atom at quotient `Y` carry component row `Q_Y` and
row-budgeted declared score `5 sqrt(Y)-3`. The current same-index row difference

\[
 Q_Y-Q_{Y/67}
\]

has literal entropy `E(Y)-E(Y/67)`. Hence (L-91666.2) proves

\[
\boxed{
 \operatorname{Score}(Q_Y-Q_{Y/67})
 \ge [5\sqrt Y-3]-[5\sqrt{Y/67}-3].
}
\tag{L-91666.15}
\]

Multiplication by every nonnegative survival/hazard row coefficient preserves
the inequality. The recursive child is therefore inherited with coefficient
one; no source-mass fraction is substituted for a signed deficit.

## 6. Replay boundary

The retained verifier checks:

```text
F(67)>3;
all 402 derivative cells 67<=N<=468;
G(469)>100 and the analytic-tail derivative condition;
exact causal coefficient cancellation;
native Mobius response convolution;
ordinary and radix-four replacement algebra.
```

It does not replay the expensive Hall, source-tree, outer mismatch, collar,
omission, or port certificates and does not establish RH.
