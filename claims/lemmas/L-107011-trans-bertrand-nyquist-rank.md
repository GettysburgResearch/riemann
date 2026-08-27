# L-107011 — The native beta criterion has one trans-Bertrand Nyquist schedule

Claim ID: `L-107011`  
Status: **PROVED EXACT SAMPLING AND DIAGONALIZATION THEOREM**  
Created: 2026-08-27  
Depends on: `L-107010`; `L-107001`  
RH status: **not assumed**

Let \(B=B_{r,\mathrm{Ber}}\) and let \(S_B\) be its fixed support length.
For \(X\ge2\), put

\[
 P_X=\log X+S_B+1,
 \qquad
 t_{k,X}=\frac{2\pi k}{P_X}.
\]

Exactly as in `L-107001`, zero extension to an interval of length \(P_X\)
gives

\[
 \boxed{
 \mathcal E_{r,\mathrm{Ber}}(X)
 =
 \frac1{P_X}
 \sum_{k\in\mathbf Z}
 \left|
 \widehat B(it_{k,X})
 \sum_{n\le X}\frac{\beta(n)}{n^{1/2+it_{k,X}}}
 \right|^2.
 }
 \tag{L-107011.1}
\]

## 1. Every fixed Bertrand depth

Fix \(m\ge0\) and \(A>0\). The functions \(W_m\) are slowly varying and obey

\[
 W_m(CyW_m(y))\ll_{C,m}W_m(y).
 \tag{L-107011.2}
\]

Indeed \(L_1(CyW_m(y))\le 2L_1(y)\) for large \(y\), and every further
softened logarithm changes by only an \(m\)-dependent additive constant.

The slowly varying Fourier envelope also has a summable tail. On the dyadic
block \([2^jT,2^{j+1}T]\),

\[
 W_m(2^{j+1}T)
 \ll_m
 (1+j)^{m+2}W_m(T).
\]

Therefore dyadic summation gives

\[
 \int_T^\infty
 \exp\{-c_mt/W_m(t)\}\,dt
 \ll_m
 W_m(T)\exp\{-c'_mT/W_m(T)\}.
 \tag{L-107011.3}
\]

Choose

\[
 T_{A,m}(X)
 =
 C_{A,m}\log(eX)W_m(\log(eX)).
 \tag{L-107011.4}
\]

For a sufficiently large fixed constant \(C_{A,m}\), the envelope from
`L-107010`, the tail estimate above, and
\(|D_X(t)|\le4\sqrt X\) give

\[
 \boxed{
 \frac1{P_X}
 \sum_{|t_{k,X}|>T_{A,m}(X)}
 \left|\widehat B(it_{k,X})D_X(t_{k,X})\right|^2
 =
 O_A(X^{-A}).
 }
 \tag{L-107011.5}
\]

No Möbius cancellation is used.

The retained number of samples is

\[
 \boxed{
 M_{A,m}(X)
 =
 O_{A,m}\left(
 (\log X)^2W_m(\log X)
 \right).
 }
 \tag{L-107011.6}
\]

For \(m=0\), this recovers the
\((\log X)^2(\log\log X)^2\) rank of `T-107000`. For \(m=1\), it improves to

\[
 O_A\left(
 (\log X)^2
 \log\log X\,
 [\log_3 X]^2
 \right),
\]

and every further fixed depth gives the next Bertrand improvement.

## 2. One diagonal schedule for the same detector

The detector \(B\) does not depend on \(m\). For each integer \(q\ge1\), let
\(C_{A,q}\) include every fixed threshold and implied constant in the
fixed-\(q\) tail theorem.

Since \(W_q(x)=o(W_j(x))\) for every \(j<q\), one may choose increasing
thresholds \(X_q\) so that, for all \(X\ge X_q\),

\[
 C_{A,q}W_q(\log X)
 \le
 \frac1q W_j(\log X)
 \qquad(0\le j<q).
 \tag{L-107011.7}
\]

The thresholds are also chosen large enough to absorb the fixed-\(q\)
tail constant into \(X^{-A}\).

Set

\[
 q(X)=\max\{q:X\ge X_q\}
\]

and define the deterministic truncation with depth \(q(X)\). Then \(q(X)\)
tends to infinity, the discarded tail is \(O_A(X^{-A})\), and the rank has
the form

\[
 \boxed{
 M_A(X)
 =
 O_A\left((\log X)^2\Lambda_A(X)\right),
 }
 \tag{L-107011.8}
\]

where

\[
 \boxed{
 \Lambda_A(X)
 =
 o(W_m(\log X))
 \quad\text{for every fixed }m.
 }
 \tag{L-107011.9}
\]

This is one fixed detector and one deterministic schedule. The schedule
depends only on \(A,X\) and the precomputed analytic constants; it does not
depend on zeta zeros or on the source values.

By `R-107010`, the factor \(\Lambda_A(X)\) cannot remain bounded when the
exterior is deleted solely by the trivial beta bound. Replacing it by its
monotone majorant if necessary, one may therefore record

\[
 \Lambda_A(X)\longrightarrow\infty
\]

while retaining (L-107011.9).

## 3. Arithmetic frontier

Define the retained feature vector exactly as in `L-107001`, using the
diagonal sample set. Then

\[
 \boxed{
 \mathrm{RH}
 \Longleftrightarrow
 \left\|
 \sum_{n\le X}\frac{\beta(n)}{\sqrt n}\mathbf v_X(n)
 \right\|^2
 =
 X^{o(1)}.
 }
 \tag{L-107011.10}
\]

The feature dimension is trans-Bertrand-close to quadratic, but the
arithmetic statement is still the same native `NBV107000` gate.
