# L-104548 — Windowed p-variation and critical-moment transfer

Claim ID: `L-104548`  
Status: **PROVED EXACT REDUCTION**  
Created: 2026-08-24  
Depends on: `L-104543`, `L-104546`  
RH status: **not assumed**

Let `f` be real `C^2` on a regular compact interval `I=[a,b]`, with simple
nonzero critical values. For `p>=1`, define

\[
D_{p,I}
=
\sum_{f'(c)=0}
\varepsilon_c|f(c)|^p,
\tag{L-104548.1}
\]

\[
B_{p,I}
=
\sum_{f'(c)=0}|f(c)|^{2p},
\qquad
R_I=\#\{c\in I:f'(c)=0\}.
\tag{L-104548.2}
\]

Here `epsilon_c=+1` at a good extremum and `-1` at a wrong one.

## 1. Exact source-visible numerator

Apply the total-variation identity to

\[
F_p(t)=\operatorname{sgn}(f(t))|f(t)|^p.
\]

Its critical points and good/wrong orientations agree with those of `f`, and

\[
|F_p'(t)|=p|f(t)|^{p-1}|f'(t)|.
\]

Therefore

\[
\boxed{
\begin{aligned}
2D_{p,I}
={}&
p\int_a^b|f|^{p-1}|f'|\,dt\\
&+
\operatorname{sgn}f'(a)\operatorname{sgn}f(a)|f(a)|^p\\
&-
\operatorname{sgn}f'(b)\operatorname{sgn}f(b)|f(b)|^p.
\end{aligned}
}
\tag{L-104548.3}
\]

The signed first moment is thus an explicit positive p-variation plus two
endpoint terms. It is not an unknown orientation sum.

## 2. Exact count bound

If `G_I` is the number of good critical points, Cauchy--Schwarz gives

\[
(D_{p,I})_+
\le
\sum_{c\in G_I}|f(c)|^p
\le
\sqrt{G_I B_{p,I}}.
\]

Hence

\[
\boxed{
G_I\ge\frac{(D_{p,I})_+^2}{B_{p,I}},
}
\tag{L-104548.4}
\]

and

\[
\boxed{
\frac{G_I-W_I}{R_I}
\ge
2\frac{(D_{p,I})_+^2}{R_IB_{p,I}}-1.
}
\tag{L-104548.5}
\]

## 3. Xi gate

For `f=Xi''`, choose regular windows covering density one of Conrey's real
`Xi'''` zeros.

Define:

```text
PVAR104600 — p-variation / critical-moment coherence

For some fixed p>=1 and eta>0, prove on those windows

  (D_p,I)_+^2 / [R_I B_p,I] >= (1+eta)/2 + o(1),

where D_p,I is evaluated by the explicit variation formula (L-104548.3).
```

Then

\[
\boxed{
\mathrm{PVAR104600}
\Longrightarrow
\alpha_2\ge\eta\alpha_3
>
0.9873\,\eta.
}
\tag{L-104548.6}
\]

The denominator `B_p,I` is a positive critical-value moment and admits the
thin-strip marked-logarithmic-derivative contour of `L-104544` with marker
`f^{2p}` (or a holomorphic regularization when `p` is not integral).

This route replaces the tautological phase lower bound by one explicit
positive variation and one positive marked moment.
