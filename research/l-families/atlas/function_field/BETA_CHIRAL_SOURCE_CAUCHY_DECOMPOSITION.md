# T-108008 — The literal beta source splits into an exact diagonal and two signed cusp channels

Status: **exact Cauchy transfer of the assembled beta Perron source through the
finite Chebyshev spectrum, exact primitive-pair formula before every source
norm, exact beta-square diagonal Euler product, proof that the diagonal is not
amplified by the cubic cusp, exact first-edge two-channel decomposition, and
exact signed Chebyshev cell-current coordinates, and a binding correction of the directed primitive-pair orientation sign in T-108006; no RH-sized off-diagonal
correlation estimate, no payment of the outer Fourier tails, no new zero-free
region, and no proof of RH.**

Bounded replay:
[`beta_chiral_source_cauchy_decomposition.py`](beta_chiral_source_cauchy_decomposition.py).
Canonical output:
[`beta_chiral_source_cauchy_decomposition.json`](beta_chiral_source_cauchy_decomposition.json).

This packet continues T-108006 at exact head
`bbfb9761c2b4bb37e35342e8d9279895f8d44be0`.  The source-locked T-108006
front door uses beta-pair evenness to replace the symmetric T-108004 cusp
inside the assembled integral by one directed chiral branch.  T-108008
authenticates that reduction, corrects the sign of its prose-level primitive-pair orientation under the stated Fourier convention, and supplies the literal primitive-pair, diagonal/off-diagonal, and multiplicative-cell coordinates.  T-108004 found the
complete geometric multiplier on the local window

\[
 t=\tau N^{1/3},
 \qquad
 v=N^{1/3}\log(m/k),
\]

and its exact cubic carrier

\[
 |v|^{-1/2}e^{-\lambda|v|/2}e^{i|v|^3/3}.
\]

The missing issue was how the *literal* reciprocal-zeta/beta source enters
that carrier before any absolute value is taken.  The answer is an exact
Cauchy transfer and an exact diagonal/off-diagonal split.

## 0. Outcome

Let \(K\in L^2(\mathbb R)\) be real and compactly supported, put

\[
 R=\widetilde K*K,
 \qquad
 R_z(x)=R(x)e^{-z|x|/2},
 \qquad \Re z>1,
\tag{0.1}
\]

and use

\[
 \widehat f(t)=\int_{\mathbb R}f(x)e^{-itx}\,dx.
\tag{0.2}
\]

For

\[
 s={1+z\over2},
 \qquad
 B_\beta(w)={1-67^{-w}\over\zeta(w)},
 \qquad
 F_z(t)=B_\beta(s-it)B_\beta(s+it),
\tag{0.3}
\]

define the assembled Perron source pairing

\[
 \mathfrak E_K(z)
 ={1\over2\pi}\int_{\mathbb R}\widehat{R_z}(t)F_z(t)\,dt.
\tag{0.4}
\]

Put

\[
 P_z(u)={1\over2\pi}{z\over u^2+z^2/4},
 \qquad
 (\mathcal P_zF)(\xi)=\int_{\mathbb R}P_z(t-\xi)F(t)\,dt.
\tag{0.5}
\]

### Theorem T-108008

The geometric tilt transfers exactly to the unsquared source:

\[
 \boxed{
 \widehat{R_z}(t)
 =\int_{\mathbb R}P_z(t-\xi)|\widehat K(\xi)|^2\,d\xi,}
\tag{0.6}
\]

and therefore

\[
 \boxed{
 \mathfrak E_K(z)
 ={1\over2\pi}\int_{\mathbb R}
 |\widehat K(\xi)|^2(\mathcal P_zF_z)(\xi)\,d\xi.}
\tag{0.7}
\]

The transferred source is the literal signed primitive-pair sum

\[
 \boxed{
 (\mathcal P_zF_z)(\xi)
 =\sum_{m,k\ge1}
 {\beta(m)\beta(k)\over\sqrt{mk}\,\max(m,k)^z}
 e^{i\xi\log(m/k)}.}
\tag{0.8}
\]

No source norm or channelwise absolute value appears in (0.8).  Pairing
\((m,k)\) with \((k,m)\) gives the exact directed form

\[
 \boxed{
 (\mathcal P_zF_z)(\xi)
 =D_\beta(z)
 +2\sum_{m>k}
 {\beta(m)\beta(k)\over\sqrt{mk}\,m^z}
 \cos\!\left(\xi\log{m\over k}\right).}
\tag{0.8a}
\]

This is the primitive-pair version of the T-108006 beta-even chiral
reduction: one orientation is retained, but only after the reflected pair has
been assembled exactly.

### Binding sign correction to T-108006

T-108006 correctly proves that the directed profile has the Fourier
representation

\[
 \mathcal D(\lambda,\tau)
 ={1\over2\pi}\int_{v<0}H^{\leftarrow}_\lambda(v)e^{i\tau v}\,dv.
\tag{0.8b}
\]

The assembled beta source uses the phase

\[
 e^{i\tau L_{m,k}},
 \qquad L_{m,k}=N^{1/3}\log(m/k).
\tag{0.8c}
\]

Consequently the \(\tau\)-integration evaluates the carrier at
\(v=-L_{m,k}\), not at \(v=L_{m,k}\):

\[
 \int_{\mathbb R}\mathcal D(\lambda,\tau)
 e^{i\tau L_{m,k}}\,d\tau
 =H^{\leftarrow}_\lambda(-L_{m,k}).
\tag{0.8d}
\]

Since the carrier is supported on \(v<0\), the directed \(z+2it\) face
selects

\[
 \boxed{L_{m,k}>0,\qquad m>k.}
\tag{0.8e}
\]

Thus the formulas and one-sided carrier in T-108006 remain correct, but its
prose identification “\(v<0\), equivalently \(m<k\)” reverses the source
lag sign under the Fourier convention it states.  Equation (0.8a) uses the
correct \(m>k\) orientation.  Choosing the reflected directed face would,
of course, exchange the two orders without changing the assembled integral.

For the unit-height Chebyshev step \(K_N\), with nodes

\[
 y_j={1-\cos(j\pi/N)\over2}
\]

and derivative masses

\[
 q_j=(-1)^ja_j,
 \qquad a_0=a_N=1,
 \qquad a_j=2\ (0<j<N),
\]

write

\[
 Q_N(\xi)=\sum_{j=0}^Nq_je^{-i\xi y_j}.
\tag{0.9}
\]

Then

\[
 \widehat K_N(\xi)={Q_N(\xi)\over i\xi}
\]

with a removable value at zero, and hence

\[
 \boxed{
 \mathfrak E_{K_N}(z)
 ={1\over2\pi}\int_{\mathbb R}
 {|Q_N(\xi)|^2\over\xi^2}
 (\mathcal P_zF_z)(\xi)\,d\xi.}
\tag{0.10}
\]

This is the requested insertion of the exact finite difference spectrum into
the literal beta source **before** squaring the arithmetic channels.

## 1. Proof of the Cauchy transfer

The Fourier transform of the bilateral exponential is

\[
 \int_{\mathbb R}e^{-z|x|/2}e^{-iux}\,dx
 ={z\over u^2+z^2/4},
 \qquad \Re z>0.
\tag{1.1}
\]

Since \(\widehat R(\xi)=|\widehat K(\xi)|^2\), the product-convolution rule
proves (0.6).  For \(\Re z>1\), both beta Dirichlet series are absolutely
convergent, \(P_z\in L^1\), and \(|\widehat K|^2\in L^1\).  Fubini therefore
proves (0.7).

Termwise,

\[
 F_z(t)=\sum_{m,k\ge1}
 \beta(m)\beta(k)(mk)^{-s}e^{it\log(m/k)}.
\tag{1.2}
\]

The Cauchy kernel acts diagonally on exponentials:

\[
 \int_{\mathbb R}P_z(t-\xi)e^{itx}\,dt
 =e^{-z|x|/2}e^{i\xi x}.
\tag{1.3}
\]

Finally,

\[
 (mk)^{-s}e^{-z|\log(m/k)|/2}
 ={1\over\sqrt{mk}\,\max(m,k)^z},
\tag{1.4}
\]

which proves (0.8).  Substitution into (0.7), followed by Fourier inversion,
recovers the max-weighted beta Gram form exactly.

## 2. The diagonal is explicit and does not carry the cusp height

Split (0.8) into \(m=k\) and \(m\ne k\):

\[
 (\mathcal P_zF_z)(\xi)=D_\beta(z)+O_\beta(z,\xi),
\tag{2.1}
\]

where

\[
 \boxed{
 D_\beta(z)=\sum_{n\ge1}{\beta(n)^2\over n^{1+z}}.}
\tag{2.2}
\]

The diagonal is independent of \(\xi\).  Since \(\mathcal P_z1=1\) and the
unit-height Chebyshev step satisfies \(\|K_N\|_2^2=1\), its complete
contribution to (0.10) is simply

\[
 \boxed{\mathfrak E_{K_N}^{\rm diag}(z)=D_\beta(z).}
\tag{2.3}
\]

Thus the pointwise \(N^{1/3}\) cusp height found in T-108002/T-108004 does
not amplify the diagonal.  All genuinely new cusp arithmetic is
off-diagonal.

The exceptional-prime local states are

\[
 \beta(67^0m)=\mu(m),
 \qquad
 \beta(67m)=-2\mu(m),
 \qquad
 \beta(67^2m)=\mu(m)
\]

for squarefree \(m\) coprime to \(67\).  Consequently, with \(w=1+z\) and
\(x=67^{-w}\),

\[
 \boxed{
 D_\beta(z)
 ={1+4x+x^2\over1+x}
 {\zeta(w)\over\zeta(2w)}.}
\tag{2.4}
\]

Equation (2.4) is an exact meromorphic diagonal subtraction, not an estimate.

## 3. The first edge has exactly two source channels

The Cauchy kernel has the exact partial fraction

\[
 P_z(u)={1\over2\pi i}
 \left({1\over u-iz/2}-{1\over u+iz/2}\right).
\tag{3.1}
\]

At the first finite edge put

\[
 z_N=4iN+\sigma,
 \qquad \sigma=\lambda N^{1/3}>0.
\tag{3.2}
\]

Then

\[
 \boxed{
 P_{z_N}(t-\xi)
 ={1\over2\pi i}
 \left[
 {1\over t-\xi+2N-i\sigma/2}
 -{1\over t-\xi-2N+i\sigma/2}
 \right].}
\tag{3.3}
\]

The first Chebyshev spectral packets lie at \(\xi\simeq+2N\) and
\(\xi\simeq-2N\).  Formula (3.3) carries both of them to the same local
source window \(t=\tau N^{1/3}\).  These are the two chiral contributions
whose geometric sum is the T-108004 cusp \(\mathcal C(\lambda,\tau)\).
They must be assembled against the beta source before any absolute value.
At the integrated level, the beta source is even:

\[
 F_z(-t)=F_z(t).
\tag{3.3a}
\]

Consequently the T-108004 symmetric split obeys

\[
 \boxed{
 \int_{\mathbb R}{J_N(z+2it)+J_N(z-2it)\over2}F_z(t)\,dt
 =\int_{\mathbb R}J_N(z+2it)F_z(t)\,dt.}
\tag{3.3b}
\]

The change of variables \(t\mapsto-t\) proves (3.3b).  This is the exact
one-directed-chirality front door recorded in T-108006; (0.8a) is its
literal primitive-pair realization.

This also identifies the exact object on which a signed estimate must act:

\[
 \boxed{
 {1\over2\pi}\int {|Q_N(\xi)|^2\over\xi^2}
 O_\beta(z_N,\xi)\,d\xi,}
\tag{3.4}
\]

or, equivalently, the off-diagonal part of (0.8) against the cubic lag
carrier of T-108004.

## 4. Exact signed multiplicative-cell coordinates

The same source has a second exact coordinate that keeps every short
multiplicative interval signed.  For a sharp cap \(X\), define

\[
 G_{N,X}(u)=\sum_{m\le X}{\beta(m)\over\sqrt m}
 K_N(u-\log m).
\tag{4.1}
\]

If

\[
 A_X(v)=\sum_{\substack{m\le X\\\log m\le v}}
 {\beta(m)\over\sqrt m},
\tag{4.2}
\]

then the jump representation gives

\[
 \boxed{
 G_{N,X}(u)=\sum_{j=0}^Nq_jA_X(u-y_j).}
\tag{4.3}
\]

Equivalently, cell by cell,

\[
 \boxed{
 G_{N,X}(u)=
 \sum_{j=0}^{N-1}(-1)^j
 \sum_{\substack{m\le X\\
 e^{u-y_{j+1}}<m\le e^{u-y_j}}}
 {\beta(m)\over\sqrt m}.}
\tag{4.4}
\]

Thus the beta energy is the integral of the square of one *assembled signed
cell current*; it is not the sum of the absolute energies of the cells.

Writing \(G^\mu\) for the same field with \(\mu\) in place of \(\beta\),
the exceptional scale obeys

\[
 \boxed{
 G^\beta_{N,X}(u)
 =G^\mu_{N,X}(u)
 -67^{-1/2}G^\mu_{N,\lfloor X/67\rfloor}(u-\log67).}
\tag{4.5}
\]

Equation (4.5) retains the cross-scale sign before squaring.  As established
by the duplicate-67 firewall, it is a coordinate identity rather than an
asymptotic contraction by itself.

## 5. What has and has not been closed

T-108004 exposed the local cubic geometry and T-108006 selected the directed chiral source branch. T-108008 fixes the source-lag sign in the interpretation of that branch and now inserts the literal
source into that geometry and removes the complete diagonal exactly.  The
remaining RH-bearing term is no longer an unspecified beta norm.  It is the
signed off-diagonal primitive-pair correlation in (3.4), with:

- the \(+2N\) and \(-2N\) Cauchy channels assembled;
- the three exceptional-prime local states assembled;
- the diagonal Euler product subtracted;
- the cubic phase retained;
- no channelwise absolute value.

The next named gate is therefore

```text
BETACHIRALOFFDIAG108010

Subtract D_beta(z) exactly.  On t=tau*N^(1/3), prove a signed bound for the
complete off-diagonal source after the +2N and -2N Cauchy channels and all
exceptional-prime local states have been assembled.  Equivalently, estimate
primitive pairs m != k against

  |v|^(-1/2) exp(-lambda*|v|/2+i|v|^3/3),
  v=N^(1/3) log(m/k),

and then pay the outer-tau ranges.  No absolute value may be inserted before
this assembly.
```

No such RH-sized bound is asserted in this packet.

## 6. Replay ledger

The retained producer:

1. authenticates the T-108006 chiral source front door, the T-108004 carrier, and the assembled Perron predecessor;
2. checks the duplicate-67 scale relation at nine finite Dirichlet rows;
3. verifies, with exact rational arithmetic, the direct-step, jump-prefix,
   and alternating-cell forms on every cell of a nontrivial fixture;
4. checks the Cauchy partial fraction;
5. checks an explicit diagonal/off-diagonal transferred source;
6. checks the exceptional beta-square Euler factor exactly;
7. checks the two first-edge pole channels.

```text
PASS_T108008_BETA_CHIRAL_SOURCE_CAUCHY_DECOMPOSITION

T-108006 chiral source front door             AUTHENTICATED
primitive-pair orientation sign                CORRECTED (m>k for z+2it)
beta-pair oriented reduction                  PROVED
exact Cauchy transfer                         PROVED
finite jump spectrum before source norm       PROVED
signed Chebyshev cell-current identity         PROVED
exceptional 67 cross-scale field identity      PROVED
exact beta-square diagonal Euler product       PROVED
diagonal cusp amplification absent             PROVED
first-edge two Cauchy channels                 PROVED
signed off-diagonal cusp estimate              OPEN
outer-frequency tails                          OPEN
direct lambda=0, tau!=0 finite boundary        OPEN
new zero-free half-plane                       NOT PROVED
RH                                             UNPROVED
```
