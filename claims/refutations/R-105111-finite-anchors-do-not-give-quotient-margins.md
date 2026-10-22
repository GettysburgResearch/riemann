# R-105111 — Finite anchors do not give quotient margins

Claim ID: R-105111

Status: **PROPOSED EXACT REFUTATION**

Created: 2026-08-23

Depends on: R-105110; L-105111

RH status: **unproved**

## Refuted inference

The following implication is false:

> A finite collection of first/product denominator anchor values, together
> with a complete stable first critical-point manifest, fixed target residue,
> parity, and bounded first optimal selector, gives a quantitative edge lower
> margin between the anchors.

## Exact counterfamily

For a finite \(S\subset(0,\infty)\), let

\[
Q_S(z)=z^2\prod_{s\in S}(z^2-s^2),
\qquad
L_C(z)=z e^{-CQ_S(z)^2},
\tag{R-105111.1}
\]

and

\[
F_C(z)=
\exp\!\left(\int_0^zL_C(w)\,dw\right),
\qquad C>0.
\tag{R-105111.2}
\]

Then \(F_C\) is real, even, entire, and zero-free, and
\(F_C'/F_C=L_C\).  Hence \(F_C'\) has exactly the one global simple zero
\(0\).  Its first target residue and optimal selector are fixed:

\[
\operatorname{Res}_{0}\frac{F_C}{F_C'}=1,
\qquad
W_{1,C,*}=1,
\qquad
\tau_{1,C}=1.
\tag{R-105111.3}
\]

At every \(s\in S\),

\[
L_C(s)=s,
\qquad
L_C'(s)=1,
\qquad
A_C(s)=s^2+1.
\tag{R-105111.4}
\]

Thus both \(G_1=L\) and \(G_{12}=LA\) have \(C\)-independent anchor values.
At every real nonsample \(\zeta\ne0\), however,

\[
L_C(\zeta)\to0,
\qquad
A_C(\zeta)\to0
\tag{R-105111.5}
\]

provided \(Q_S(\zeta)\ne0\).

For

\[
S=\{1/2,1\},
\qquad E=[1/2,1],
\qquad \zeta=3/4,
\tag{R-105111.6}
\]

the fixed endpoint data are

\[
\begin{array}{c|cc}
z&1/2&1\\
\hline
G_1(z)&1/2&1\\
G_{12}(z)&5/8&2,
\end{array}
\tag{R-105111.7}
\]

but

\[
Q_S(3/4)^2=\frac{99225}{16777216}>0,
\tag{R-105111.8}
\]

so both denominator values at \(3/4\) collapse as \(C\to\infty\).

The inference fails because center/anchor data carry no derivative or Taylor
tail control between samples.  L-105111's disk slack supplies exactly that
missing information.

## What is not refuted

The anchored log-drop identity remains exact.  For \(G_1\), its
drop/variation debt grows with \(C\).  For \(G_{12}\), either \(A_C\)
acquires a zero on the edge, making the product margin zero directly, or its
drop/variation pays the collapse on any zero-free parameter range.  The
disk-cover theorem also remains valid: any cover that certifies the
collapsing region must pay growing derivative bounds or lose positive slack.

Only the first derivative-event manifest is fixed.  No stable second
manifest is claimed.  The family varies with \(C\), has infinite order, and
is not Xi or a fixed-function cofinal model.  No Xi margin, RCMV104530, or RH
conclusion follows.
