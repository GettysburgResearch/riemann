# L-99280 — Exact compact Hall and normalized component-profile certificate

Claim ID: `L-99280`  
Status: **PROVED EXACT DIRECTED FINITE THEOREM**  
Created: 2026-08-20  
Depends on: the displayed component-row formula of PR #620  
RH status: **not assumed**

## 1. Target Hall prefixes

For \(1\le t\le x<67\), put

\[
A_t=\sum_{n\le t}\frac{\mu(n)}n,
\qquad
B_t=\sum_{n\le t}\frac{\mu(n)}{\sqrt n},
\]

and

\[
H_t(x)=4\sqrt x\,A_t-3B_t.
\]

On each active threshold interval, `H_t` is affine in `sqrt(x)`. Hence its
minimum is at \(x=t\) when \(A_t\ge0\), and at \(x=67\) when \(A_t<0\).

The exact rational interval replay checks every threshold and proves

\[
\boxed{
H_t(x)>\frac7{20}
\qquad(1\le t\le x<67).
}
\tag{L-99280.1}
\]

The minimum is at `t=13`, `x=67`, with the directed enclosure

\[
0.35931766059850017
<
H_{13}(67)
<
0.35931766059850018.
\tag{L-99280.2}
\]

Thus the nested-neighbourhood Hall flow exists with strict reserve.

## 2. Normalized component profiles

Fix \(j\ge2\). On an activation cell \(N\le Y<N+1\), the canonical component
row has the form

\[
Q_Y(j)=a_{j,N}\log Y-b_{j,N},
\tag{L-99280.3}
\]

where

\[
\begin{aligned}
a_{j,N}
={}&
\frac{j+1}{j-1}\frac1{\sqrt j}
-\mathbf1_{N\ge j+1}
 \frac{(j+1)(j-2)}{j(j-1)}\frac1{\sqrt{j+1}}\\
&+\frac2{j(j-1)}
  \sum_{m=j+2}^{N}\frac1{\sqrt m},
\end{aligned}
\tag{L-99280.4}
\]

and \(b_{j,N}\) is the same linear combination with
\(m^{-1/2}\) replaced by \(m^{-1/2}\log m\).

Set

\[
T(Y)=4\sqrt Y-3,
\qquad
\rho_j(Y)=\frac{Q_Y(j)}{T(Y)}.
\]

A direct differentiation gives

\[
\rho_j'(Y)
=
\frac{
a_{j,N}T(Y)/Y-2Q_Y(j)/\sqrt Y
}{
T(Y)^2
}.
\tag{L-99280.5}
\]

Put \(u=\sqrt Y\) and

\[
M_{j,N}(u)
=
a_{j,N}(4u-3)-2uQ_{u^2}(j).
\]

Then

\[
\boxed{
\frac{d}{du}M_{j,N}(u)=-2Q_{u^2}(j)\le0.
}
\tag{L-99280.6}
\]

Therefore it is enough to check the right endpoint \(Y=N+1-\) of each cell.
The exact rational interval replay checks all

\[
\sum_{j=2}^{66}(67-j)=2145
\]

cells and proves

\[
\boxed{
M_{j,N}(\sqrt{N+1})>\frac1{10}.
}
\tag{L-99280.7}
\]

The minimum occurs at `(j,N)=(65,66)` and satisfies

\[
0.11192276814695241
<
M_{65,66}(\sqrt{67})
<
0.11192276814695242.
\tag{L-99280.8}
\]

There is no adverse activation atom because each newly activated logarithmic
term vanishes at activation. Hence

\[
\boxed{
Y_2\ge Y_1
\Longrightarrow
\rho_j(Y_2)\ge\rho_j(Y_1)
\quad(1\le Y_1,Y_2<67).
}
\tag{L-99280.9}
\]

## 3. Common-flow consequence

If `e<=o`, then `x/e>=x/o`; therefore (L-99280.9) gives

\[
\rho_j(x/e)\ge\rho_j(x/o)
\]

for every component row. The target Hall flow from Section 1 consequently
produces a coefficientwise nonnegative Hall bonus in every row, using one and
the same source coupling.

The theorem does not authorize a causal operation on the derivative fibre
`p_s`. Causal recursion is applied only after endpoint integration, to the
endpoint-nested canonical packet.
