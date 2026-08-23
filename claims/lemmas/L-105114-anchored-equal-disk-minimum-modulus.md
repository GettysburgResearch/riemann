# L-105114 - Anchored equal-disk minimum-modulus transfer

Claim ID: L-105114

Status: **PROPOSED EXACT FINITE ANALYTIC LEMMA; XI COFINAL SCALE OPEN**

Created: 2026-08-23

Depends on: elementary Jensen, Borel-Caratheodory, and finite Blaschke
factorization; L-105113 only for the downstream rectangle interface

RH status: **unproved**

## 1. Scale-invariant statement

Let \(f\) be holomorphic in a neighborhood of
\(\overline D(a,r_3)\), let \(f(a)\ne0\), and suppose

\[
0<r_1<r_2<r_3.
\tag{L-105114.1}
\]

Put

\[
A_f=
\log\left(
\frac{\max_{|z-a|=r_3}|f(z)|}{|f(a)|}
\right)\ge0,
\qquad
\beta=\log\frac{r_3}{r_2}>0.
\tag{L-105114.2}
\]

Let \(z_1,\ldots,z_n\) be the zeros of \(f\) in \(D(a,r_2)\),
listed with multiplicity. For \(0<\varepsilon\le1\), define the nominal
equal-disk cover

\[
Z_{f,\varepsilon}
=\bigcup_{j=1}^n D(z_j,\varepsilon r_2).
\tag{L-105114.3}
\]

Then Jensen's formula gives

\[
\boxed{
n\le\frac{A_f}{\beta},
\qquad
\sum_{j=1}^n\operatorname{rad}D(z_j,\varepsilon r_2)
\le\frac{\varepsilon r_2 A_f}{\beta}.
}
\tag{L-105114.4}
\]

Repeated disks caused by multiplicity only overcount the geometric union.
For every \(z\in\overline D(a,r_1)\setminus Z_{f,\varepsilon}\),

\[
\boxed{
\log\left|\frac{f(z)}{f(a)}\right|
\ge-
\left(
\frac{2r_1}{r_2-r_1}
+\frac{\log(2/\varepsilon)}{\beta}
\right)A_f.
}
\tag{L-105114.5}
\]

Both sides are invariant under \(f\mapsto cf\), and every coefficient is
invariant under simultaneous dilation of \(z-a,r_1,r_2,r_3\).

## 2. Proof

Translate \(a\) to zero and normalize

\[
h(w)=\frac{f(a+w)}{f(a)},
\qquad h(0)=1.
\tag{L-105114.6}
\]

Write \(\zeta_j=z_j-a\). For any zero-free radius
\(r_2<\rho<r_3\), Jensen's formula and maximum modulus give

\[
\begin{aligned}
n\log\frac{\rho}{r_2}
&\le
\sum_{|\zeta_j|<r_2}\log\frac{\rho}{|\zeta_j|}\\
&\le
\frac1{2\pi}\int_0^{2\pi}
\log|h(\rho e^{i\theta})|\,d\theta
\le A_f.
\end{aligned}
\tag{L-105114.7}
\]

Letting \(\rho\uparrow r_3\) proves the zero-count and nominal-radius
assertions in (L-105114.4), including when the outer circle contains a
zero.

Since \(h(0)=1\), none of the \(\zeta_j\) is zero. Define

\[
\phi(w)=
\prod_{j=1}^n
\left(
\frac{-r_2}{\zeta_j}
\frac{r_2(w-\zeta_j)}{r_2^2-\overline{\zeta_j}w}
\right),
\qquad
\psi(w)=\frac{h(w)}{\phi(w)}.
\tag{L-105114.8}
\]

The function \(\psi\) is holomorphic and zero-free in \(D(0,r_2)\), and
\(\phi(0)=\psi(0)=1\). On \(|w|=r_2\),

\[
|\phi(w)|=\prod_{j=1}^n\frac{r_2}{|\zeta_j|}.
\tag{L-105114.9}
\]

A holomorphic logarithm \(g=\log\psi\) therefore has \(g(0)=0\) and

\[
\sup_{|w|<r_2}\Re g(w)\le A_f.
\tag{L-105114.10}
\]

Apply Borel-Caratheodory on radius \(\rho<r_2\), then let
\(\rho\uparrow r_2\). For \(|w|\le r_1\),

\[
\log|\psi(w)|=\Re g(w)
\ge-\frac{2r_1}{r_2-r_1}A_f.
\tag{L-105114.11}
\]

If \(w\notin Z_{f,\varepsilon}-a\), then
\(|w-\zeta_j|\ge\varepsilon r_2\). Also
\(|\zeta_j|<r_2\), \(|w|\le r_1<r_2\), and hence each factor in
(L-105114.8) satisfies

\[
\left|
\frac{-r_2}{\zeta_j}
\frac{r_2(w-\zeta_j)}{r_2^2-\overline{\zeta_j}w}
\right|
\ge\frac{\varepsilon}{2}.
\tag{L-105114.12}
\]

Consequently

\[
\log|\phi(w)|\ge-n\log(2/\varepsilon)
\ge-\frac{A_f}{\beta}\log(2/\varepsilon).
\tag{L-105114.13}
\]

Adding (L-105114.11) and (L-105114.13) proves
(L-105114.5). No asymptotic or numerical minimum-modulus input is used.

## 3. Standard-radius form

At

\[
r_1=R,
\qquad r_2=2R,
\qquad r_3=2eR,
\tag{L-105114.14}
\]

one has \(\beta=1\), and the ledger becomes

\[
n\le A_f,
\qquad
S_f\le2\varepsilon R A_f,
\tag{L-105114.15}
\]

\[
\boxed{
|f(z)|\ge |f(a)|
\exp\left(-[2+\log(2/\varepsilon)]A_f\right)
}
\tag{L-105114.16}
\]

on \(\overline D(a,R)\) outside the zero disks.

## 4. Simultaneous three-function and raw-quotient forms

Apply the lemma to finitely many functions \(g_j\) sharing the same
anchor and radii, with possibly different \(\varepsilon_j\). The union of
their nominal covers has total radius at most

\[
S_J\le
\frac{r_2}{\beta}
\sum_{j\in J}\varepsilon_jA_j,
\qquad
A_j=
\log\left(
\frac{\max_{|z-a|=r_3}|g_j(z)|}{|g_j(a)|}
\right).
\tag{L-105114.17}
\]

The projection lemma in the companion report therefore selects a common
symmetric rectangle whenever the complete candidate boundary family lies
in \(\overline D(a,r_1)\) (for example,
\(\overline\Omega_{T_1,\eta_1}\subset\overline D(a,r_1)\)) and

\[
\boxed{
2S_J<\min(\Delta_T,\Delta_\eta).
}
\tag{L-105114.18}
\]

For

\[
F=g_0,
\qquad F'=g_1,
\qquad F''=g_2,
\tag{L-105114.19}
\]

the direct raw quotients need lower bounds only for \(g_1,g_2\). Thus
the simultaneous uncancelled factorwise certificate uses
\(J=\{1,2\}\), not \(J=\{0,1,2\}\); the first carrier alone uses
\(J=\{1\}\). This is not a minimality claim after separately
authenticating common-zero or numerator cancellations. Boundary zeros of
\(F\) remain harmless. Put

\[
B_j=
\left(
\frac{2r_1}{r_2-r_1}
+\frac{\log(2/\varepsilon_j)}{\beta}
\right)A_j.
\tag{L-105114.20}
\]

On a selected raw-safe boundary inside \(D(a,r_1)\),

\[
\boxed{
\left|\frac{F}{F'}\right|
\le
\frac{|F(a)|}{|F'(a)|}e^{A_0+B_1}.
}
\tag{L-105114.21}
\]

\[
\boxed{
\left|\frac{F^2}{F'F''}\right|
\le
\frac{|F(a)|^2}{|F'(a)F''(a)|}
e^{2A_0+B_1+B_2}.
}
\tag{L-105114.22}
\]

If a log-derivative route also requires \(F\ne0\), add \(j=0\) to the
exceptional union. That larger cover is not charged to the raw route.

## 5. Xi specialization and exact boundary

The residue programme uses the \(t\)-plane normalization

\[
\Xi_t(z)=\xi\left(\tfrac12+iz\right),
\qquad
g_j=\Xi_t^{(k-1+j)},
\quad j=0,1,2.
\tag{L-105114.23}
\]

A common anchor must satisfy

\[
g_0(a)g_1(a)g_2(a)\ne0.
\tag{L-105114.24}
\]

The origin is not a general common anchor: \(\Xi_t\) is even, so every odd
derivative vanishes there. The finite theorem is therefore conditional
on authenticated off-center anchor values and the three finite growth
loads \(A_j\).

Under only a classical fixed-\(k\) upper load
\(A_j=O_k(R\log R)\), a uniform choice guaranteed to fit a fixed-width
collar is \(\varepsilon=O(1/(R^2\log R))\). Equations (L-105114.20)--
(L-105114.22) then permit reciprocal-margin losses of size
\(\exp(O_k(R(\log R)^2))\). No current selector estimate absorbs that
loss at the residue-moment scale.

Thus this lemma closes the normalized finite analytic transfer. It does
not authenticate Xi anchors or growth, construct actual-pole manifests,
bound selector cost, prove a cofinal edge estimate, prove RCMV104530, or
prove RH.
