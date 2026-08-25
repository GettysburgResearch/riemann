# Standalone proof — F1 dyadic-cell localization and one-Hardy-primitive frontier

## Frozen packet

```text
F1 parent:
  PR #730
  77c4f9e24ead1a89678ffdb975275b914c709d70

Boolean/energy parent:
  PR #719
  4146f81e7237d41e2e4a0cb1737511266683e980

same-half-source/reflection parent:
  PR #751
  98af0db6ec7f77d6333a77a3dac53c4698852f43
```

The classical Riemann Hypothesis is not assumed and is not proved here.

## 1. Fixed current

After source recombination and the inherited repeated-label contraction
ledger, write the derivative-outer current as

\[
H(X)=\sum_na_nK_L(X/n),
\]

where

\[
K_L(y)=
\begin{cases}
8-4\sqrt y,&1\le y<2,\\
-8(1+\sqrt2)+4\sqrt2\sqrt y,&2\le y<4,\\
8\sqrt2-2\sqrt y,&4\le y<8,\\
0,&\text{otherwise}.
\end{cases}
\]

The canonical coefficients are real and finite on each frozen horizon.

## 2. Integer-cell normal form

Fix an integer \(m\) and \(m<X<m+1\).  A summand can change branch only when
\(X\) crosses one of \(n,2n,4n,8n\), all integers.  Hence the active sets are
constant on the cell.  Put

\[
\begin{aligned}
S_0&=\sum_{m/2<n\le m}a_n,
&S_1&=\sum_{m/4<n\le m/2}a_n,
&S_2&=\sum_{m/8<n\le m/4}a_n,\\
T_0&=\sum_{m/2<n\le m}{a_n\over\sqrt n},
&T_1&=\sum_{m/4<n\le m/2}{a_n\over\sqrt n},
&T_2&=\sum_{m/8<n\le m/4}{a_n\over\sqrt n}.
\end{aligned}
\]

Substitution gives

\[
H(X)=A_m+B_m\sqrt X
\]

with

\[
A_m=8S_0-8(1+\sqrt2)S_1+8\sqrt2S_2,
\]

\[
B_m=-4T_0+4\sqrt2T_1-2T_2.
\]

This proves the exact cell localization.

## 3. Cell logarithmic L1 mass

Let \(a=\sqrt m\), \(b=\sqrt{m+1}\).  The substitution \(X=t^2\) gives

\[
\int_m^{m+1}|H(X)|{dX\over X}
=2\int_a^b{|A_m+B_mt|\over t}dt.
\]

An antiderivative away from the sole possible zero is

\[
F_m(t)=A_m\log t+B_mt.
\]

Splitting at \(-A_m/B_m\) when that root lies inside \((a,b)\) gives the
closed formula in `L-105470.7--L-105470.8`.

For an affine function with endpoint values \(u,v\),

\[
{b-a\over4}(|u|+|v|)
\le\int_a^b|q(t)|dt
\le {b-a\over2}(|u|+|v|).
\]

The lower bound follows directly in the opposite-sign case from

\[
\int_0^1|(1-s)u+sv|ds
={|u|^2+|v|^2\over2(|u|+|v|)}
\ge {|u|+|v|\over4},
\]

and the same-sign case is larger.  Since \(1/b\le1/t\le1/a\),

\[
{w_m\over2\sqrt2}(|u|+|v|)
\le\int_m^{m+1}|H(X)|{dX\over X}
\le w_m(|u|+|v|),
\]

where \(w_m=(b-a)/a\) and \(b/a\le\sqrt2\).

## 4. One Hardy primitive

Define

\[
P(x)=\sum_{n\le x}a_n,
\qquad
Q(x)=\sum_{n\le x}{a_n\over\sqrt n},
\qquad
W(x)=2P(x)-\sqrt xQ(x).
\]

Let \((Sf)(x)=f(x/2)\) and

\[
\Delta_2=(I-S)^2(I-\sqrt2S)
=I-(2+\sqrt2)S+(1+2\sqrt2)S^2-\sqrt2S^3.
\]

The constant part of the right cell endpoint is

\[
A_m=8\Delta_2P(m).
\]

With \(R(x)=\sqrt xQ(x)\), rescaling
\(\sqrt mQ(m/2^j)=2^{j/2}R(m/2^j)\) gives

\[
B_m\sqrt m=-4\Delta_2R(m).
\]

Therefore

\[
H(m+)=4\Delta_2(2P-R)(m)=4\Delta_2W(m).
\]

## 5. Endpoint jump

The four jumps of \(K_L\) are

\[
4,
\quad-4(2+\sqrt2),
\quad4(1+2\sqrt2),
\quad-4\sqrt2
\]

at \(1,2,4,8\).  Hence

\[
H(m+)-H(m-)=4E(m),
\]

where

\[
E(m)=a_m-(2+\sqrt2)\mathbf1_{2\mid m}a_{m/2}
 +(1+2\sqrt2)\mathbf1_{4\mid m}a_{m/4}
 -\sqrt2\mathbf1_{8\mid m}a_{m/8}.
\]

Thus

\[
H((m+1)-)=4(\Delta_2W(m+1)-E(m+1)).
\]

## 6. Global continuous/discrete comparison

Set

\[
\begin{aligned}
V_M&=\int_M^{2M}|H(X)|{dX\over X},\\
G_M&=\sum_{m=M}^{2M-1}w_m
 (|\Delta_2W(m)|+|\Delta_2W(m+1)|),\\
J_M&=\sum_{m=M}^{2M-1}w_m|E(m+1)|.
\end{aligned}
\]

The two-endpoint inequality and the preceding endpoint identities give

\[
\sqrt2(G_M-J_M)\le V_M\le4(G_M+J_M).
\]

Moreover

\[
{1\over(1+\sqrt2)m}\le w_m\le{1\over2m},
\]

so

\[
G_M\asymp\sum_{m=M}^{2M}{|\Delta_2W(m)|\over m}.
\]

## 7. The jump ledger is closed

The frozen source energy gives

\[
\sum_{M/8<n\le2M}|a_n|^2=M^{o(1)}.
\]

Each dyadic term in \(J_M\) is at most a fixed constant times

\[
\sum_{n\asymp M/2^j}{|a_n|\over n}.
\]

Cauchy--Schwarz gives

\[
\sum_{n\asymp M/2^j}{|a_n|\over n}
\le
\left(\sum|a_n|^2\right)^{1/2}
\left(\sum n^{-2}\right)^{1/2}
=M^{-1/2+o(1)}.
\]

There are only four scales, so

\[
J_M=M^{-1/2+o(1)}.
\]

The function jumps themselves are not measure atoms in the original
logarithmic L1 observation.  The estimate only pays the conversion from the
left endpoint to the right-continuous sample.

## 8. Final equivalence

Define

\[
\mathrm{F1HARDY}_{105470}:
\qquad
\sum_{m=M}^{2M}{|\Delta_2W(m)|\over m}=M^{o(1)}.
\]

The preceding inequalities prove

```text
F1HARDY105470
  <=> logarithmic L1 mass of H_K is subpower
  <=> F1VAR105460
  <=> REFSIG106150
  <=> SFSC106150
  -> WKSFSC106150
  -> BCI102990
  -> RH.
```

The first three equivalences are at the same frozen source and boundary
convention; inherited closed fields are removable in both directions by the
triangle inequality.

## 9. Duality and firewall

Since \(\Delta_2W(m)=H(m+)/4\), weighted `l1` duality gives

\[
\sum_{m=M}^{2M}{|\Delta_2W(m)|\over m}
=
\sup_{|\varepsilon_m|\le1}
\left|
\sum_na_n{1\over4}
\sum_{m=M}^{2M}{\varepsilon_m\over m}K_L(m/n)
\right|.
\]

This is one scalar source-correlation family.

Finally, on any cell and at any prescribed interior point \(X_0\), the allowed
affine function

\[
q(X)=\sqrt X-\sqrt{X_0}
\]

vanishes at \(X_0\) but has strictly positive logarithmic L1 mass.  Therefore
one sample per cell cannot replace the two-endpoint/Hardy gate.

`F1HARDY105470`, `BCI102990`, and RH remain unproved.
