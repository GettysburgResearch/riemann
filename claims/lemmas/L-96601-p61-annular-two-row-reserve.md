# L-96601 — The complete P61 logarithmic annulus has a uniform two-row reserve

Claim ID: `L-96601`  
Status: **PROVED FINITE/DIRECTED + ANALYTIC CERTIFICATE**  
Created: 2026-08-17  
Depends on: `L-96600`

Let

\[
 P=P_{61}=\prod_{p\le61}p,
 \qquad
 A_x(j)=Q_x(j)-Q_{x/4}(j),
\]

and define the complete finite-Euler annular rows

\[
 E_j(x)=\sum_{d\mid P}\frac{\mu(d)}{\sqrt d}A_{x/d}(j),
 \qquad j=2,3.
 \tag{L-96601.1}
\]

Then

\[
\boxed{
\begin{array}{ll}
0\le E_2(x)<5/2,&0\le E_3(x)<1,\qquad 1\le x<67,\\[2mm]
E_2(x)>7/5,&E_3(x)>1/2,\qquad x\ge67.
\end{array}}
\tag{L-96601.2}
\]

## Exact reduction

Write `q_j=C_j*1+h_j`, with

\[
 C_2=1,
 \quad h_2(1)=-1,
 \quad h_2(2)=2,
 \quad h_2(3)=-1,
\]

and

\[
 C_3=1/3,
 \quad h_3(1)=h_3(2)=-1/3,
 \quad h_3(3)=5/3,
 \quad h_3(4)=-1.
\]

Put

\[
 \Phi(x)=\sum_{d\mid P}\frac{\mu(d)}{\sqrt d}H_x(d),
\]

\[
 A_P(x)=\sum_{\substack{d\mid P\\d\le x}}\frac{\mu(d)}d,
 \quad
 B_P(x)=\sum_{\substack{d\mid P\\d\le x}}\frac{\mu(d)}{\sqrt d},
 \quad
 N_P(x)=\#\{d\mid P:d\le x\}.
\]

Finite rearrangement gives

\[
 E_j(x)=
 C_j\sum_{d\mid P}\frac{\mu(d)}{\sqrt d}K(x/d)
 +\sum_a\frac{h_j(a)}{\sqrt a}\Phi(x/a).
 \tag{L-96601.3}
\]

The exact activation sweep over `d` and `4d`, `d|P`, proves

\[
 \boxed{|\Phi(x)|<3/2\qquad(x>0).}
 \tag{L-96601.4}
\]

Using `L-96600`,

\[
\begin{aligned}
 E_j(x)\ge{}&2C_j\sqrt x\,A_P(x)
 +C_j\kappa_4B_P(x)
 -\frac{C_jN_P(x)}{6\sqrt x}\\
 &-\frac32\sum_a\frac{|h_j(a)|}{\sqrt a}.
\end{aligned}
\tag{L-96601.5}
\]

A second exact divisor-event sweep proves `A_P(x)>1/100` for `x>=67` and,
for every event `x>=2000`, gives the directed lower bounds

\[
 E_2(x)>6,
 \qquad E_3(x)>3/5.
\]

Between divisor events the right side of (L-96601.5) is increasing, so the event
check covers the entire tail. The compact interval `1<=x<=2000` is checked in
the original row formula. Since every row is affine in `log x` between integer
knots, integer endpoints exhaust the compact real interval.

The retained proof object checks all `262144` divisors and `524288` annular
activation events. The minimum compact margins occur near `x=104` and `x=102`,
not at the analytic splice.
