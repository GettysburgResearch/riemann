# L-97681 — Every subcritical even rough stopping depth has the wrong eventual sign

Claim ID: `L-97681`  
Status: **PROVED ASYMPTOTIC THEOREM IN THIS PACKET — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-18  
Depends on: the exact `P_61` annular base asymptotic and the literal least-prime source expansion  
RH status: **not assumed**

Let
\[
b(Y)=a_*\sqrt Y+O(1),\qquad a_*>0,
\tag{L-97681.1}
\]
be the complete grouped annular `P_61` scalar, extended by zero below its first
activation. For a least-prime state `p_0>=67`, define the exact natural
depth-`L` current
\[
C_{L,p_0}(X)=
\sum_{\substack{m\ {\rm squarefree}\\
P^-(m)\ge p_0,\ \omega(m)<L}}
\frac{\mu(m)}{\sqrt m}\,b(X/m).
\tag{L-97681.2}
\]

Suppose `L=L(X)` is even and
\[
L(X)=O(\log\log\log X).
\tag{L-97681.3}
\]
Then, uniformly for fixed `p_0`,
\[
\boxed{
C_{L,p_0}(X)<0
}
\tag{L-97681.4}
\]
for all sufficiently large `X`.

## 1. Critical `1/p` layers

Put
\[
z=z_{p_0}(X)=\sum_{p_0\le p\le X/2}\frac1p
=\log\log X+O_{p_0}(1).
\]
For
\[
E_j(X)=
\sum_{\substack{m\le X/2,\ m\ {\rm squarefree}\\
P^-(m)\ge p_0,\ \omega(m)=j}}\frac1m,
\]
the distinct-tuple expansion and the logarithmic product cutoff give, uniformly
for `j<=L`,
\[
E_j(X)=\frac{z^j}{j!}
\left(1+O\!\left(\frac jz+\frac{j^2}{z^2}\right)\right).
\tag{L-97681.5}
\]

Indeed, collision tuples contribute at most
\[
\binom j2\left(\sum_{p\ge p_0}\frac1{p^2}\right)z^{j-2},
\]
while the omitted products `m>X/2` satisfy
\[
\log(X/2)\,T_j
\le
\left(\sum_{p\le X}\frac{\log p}{p}\right)e_{j-1},
\]
and `e_(j-1)/e_j=(1+o(1))j/z`.

Because `z/L -> infinity`, for all large `X`
\[
\frac{E_{j-1}}{E_j}\le\frac14
\qquad(1\le j<L).
\]
Since `L` is even, `L-1` is odd, and therefore
\[
\boxed{
\sum_{j=0}^{L-1}(-1)^jE_j(X)
\le-\frac23E_{L-1}(X)<0.
}
\tag{L-97681.6}
\]

## 2. The bounded base remainder is lower order

Let
\[
W_j(X)=
\sum_{\substack{m\le X/2,\ m\ {\rm squarefree}\\
P^-(m)\ge p_0,\ \omega(m)=j}}\frac1{\sqrt m}.
\]
A prime-by-prime induction using
\[
jW_j(X)
=
\sum_{p\ge p_0}p^{-1/2}W_{j-1}(X/p;p^+)
\]
and the prime number theorem gives an absolute `C>1` such that, uniformly for
`j=O(log log log X)`,
\[
W_j(X)
\ll
\frac{\sqrt X}{\log X}
\frac{(C\log\log X)^{j-1}}{(j-1)!}.
\tag{L-97681.7}
\]
Consequently
\[
\sum_{j<L}W_j(X)
=
o\!\left(\sqrt X\,E_{L-1}(X)\right),
\tag{L-97681.8}
\]
because `C^L=(log log X)^{O(1)}=o(log X)`.

Substituting (L-97681.1) into (L-97681.2), then using
(L-97681.6)--(L-97681.8), gives
\[
C_{L,p_0}(X)
=
a_*\sqrt X\sum_{j<L}(-1)^jE_j(X)
+o(\sqrt X E_{L-1}(X))<0.
\]

## 3. Consequence for the adaptive small-prime split

The depth in PR #578 is the smallest even integer
\[
L_X\ge8\left(1+\sum_{p_0\le p\le(\log X)^{1/4}}\frac1p\right),
\]
so `L_X=O(log log log X)`. Its exact small-prime cube is positive.
Since
\[
C_{L_X,p_0}(X)=\mathcal S_{p_0}(X)+\mathcal L_{p_0}(X)
\]
and the left side is eventually negative, the large-prime complement satisfies
\[
\boxed{
\mathcal L_{p_0}(X)<0
}
\tag{L-97681.9}
\]
eventually.

Thus `LAPBR67` is false. The sign cannot be repaired at any subcritical even
depth; the arithmetic difficulty is forced into the critical product-boundary
regime `L asymp log log X`.
