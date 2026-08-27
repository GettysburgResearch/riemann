# The first critical lattice harmonic is a coherent unsigned resonance

Status: **exact literal-beta magnitude decomposition, asymptotic coherent
first-harmonic theorem, power-size Gram-operator lower bound, and growing
notch-depth frontier; the signed beta witness, RH, and GRH remain open**

Bounded replay:
[ffps_critical_lattice_first_harmonic_firewall.py](ffps_critical_lattice_first_harmonic_firewall.py).
Canonical summary:
[ffps_critical_lattice_first_harmonic_firewall.json](ffps_critical_lattice_first_harmonic_firewall.json).

Frozen source commit:
3778eb0f5a80a92a4ca8ffb938f247c79ae6bf37.
The replay pins the critical single-witness packet and the infinite dyadic
smoother theorem.

## 0. Outcome

The subpower rank of the critical Fourier Gram does **not** make its
source-blind operator norm small. The first nonzero lattice harmonic already
contains a power-size coherent direction when the literal beta coefficients
are replaced by their magnitudes.

Let

\[
 \beta(n)=\mu(n)-\mathbf1_{67\mid n}\mu(n/67)
\tag{0.1}
\]

and define the literal magnitude prefix

\[
 P_X(t)=\sum_{n\le X}{|\beta(n)|\over n^{1/2+it}}.
\tag{0.2}
\]

For the fixed order-\(r\) critical kernel, put

\[
 L_X=\log X+S_{r,\infty}+\delta,
 \qquad t_{1,X}={2\pi\over L_X}.
\tag{0.3}
\]

Write

\[
 c_{67}={1+67^{-1}\over\zeta(2)}
\tag{0.4}
\]

and

\[
 K_0=\widehat K_{\rm bd}(0)
 =3(1-\sqrt2)^2(\log2)^2.
\tag{0.5}
\]

Then

\[
\boxed{
 P_X(t_{1,X})=2c_{67}\sqrt X\,(1+o(1))}
\tag{0.6}
\]

and

\[
\boxed{
{|\widehat B_{r,\infty}(t_{1,X})|^2\over L_X}
|P_X(t_{1,X})|^2
\sim
4c_{67}^2K_0^2(2\pi)^{2r}
{X\over L_X^{2r+1}}.}
\tag{0.7}
\]

For every fixed \(r\), this is \(X^{1-o(1)}\).

Let \(G_X\) be the retained critical Gram from the spectral-witness packet,
acting on coefficient vectors indexed by \(n\le X\). Since

\[
 \sum_{n\le X}{|\beta(n)|^2\over n}\le4(1+\log X),
\tag{0.8}
\]

equation (0.7) gives

\[
\boxed{
\lambda_{\max}(G_X)
\gg_r {X\over(\log X)^{2r+2}}.}
\tag{0.9}
\]

Thus the same Gram can have rank \(X^{o(1)}\) and operator norm
\(X^{1-o(1)}\). Low rank, positivity, coefficient support, local
multiplicities, and the fixed notch do not control it. The Möbius signs are
load-bearing.

There is also a sharp source-blind notch-depth diagnostic. If the kernel
order is allowed to vary as

\[
 r(X)=\left(c+o(1)\right){\log X\over\log\log X},
\tag{0.10}
\]

then the coherent first coordinate has size

\[
\boxed{X^{1-2c+o(1)}.}
\tag{0.11}
\]

A moving notch needs \(c\ge1/2\) even to make this unsigned model subpower.
Such a moving detector is outside the fixed-kernel Mellin--Landau criterion;
(0.11) is a firewall, not a new RH route.

## 1. The literal beta magnitude keeps the exact local source

The identity

\[
\boxed{
|\beta(n)|
=\mu(n)^2+\mathbf1_{67\mid n}\mu(n/67)^2}
\tag{1.1}
\]

is coefficientwise exact. To see it, write \(n=67^ju\) with \(67\nmid u\).
If \(u\) is squarefree, the two sides have layers

\[
 (1,2,1,0,\ldots)
\tag{1.2}
\]

for \(j=0,1,2,\ldots\); if \(u\) is not squarefree, both sides vanish in
the corresponding allowed layers.

Consequently,

\[
\boxed{
\sum_{n\ge1}{|\beta(n)|\over n^s}
=(1+67^{-s}){\zeta(s)\over\zeta(2s)}}
\qquad(\Re s>1).
\tag{1.3}
\]

This countermodel does not change the exceptional local multiplicities or
the squarefree support. It removes only the arithmetic signs.

Let

\[
 B_{67}(x)=\sum_{n\le x}|\beta(n)|.
\tag{1.4}
\]

The classical elementary squarefree count

\[
 \sum_{n\le x}\mu(n)^2={x\over\zeta(2)}+O(\sqrt x)
\tag{1.5}
\]

and (1.1) give

\[
\boxed{
B_{67}(x)=c_{67}x+O(\sqrt x).}
\tag{1.6}
\]

No prime, zero, or beta coefficient census is used in this asymptotic.

## 2. The logarithmic first harmonic stays coherent

For \(s=1/2+it\), partial summation gives

\[
\begin{aligned}
P_X(t)
&=B_{67}(X)X^{-s}
  +s\int_1^X B_{67}(u)u^{-s-1}\,du\\
&={c_{67}X^{1-s}\over1-s}+O(1+\log X),
\end{aligned}
\tag{2.1}
\]

uniformly for \(|t|\ll1/\log X\). At \(t=t_{1,X}\),

\[
 t_{1,X}\log X
 ={2\pi\log X\over\log X+S_{r,\infty}+\delta}
 =2\pi+o(1)
\tag{2.2}
\]

for fixed \(r\). Hence

\[
 X^{-it_{1,X}}=1+o(1),
 \qquad
 {1\over1/2-it_{1,X}}=2+o(1).
\tag{2.3}
\]

Equations (2.1)--(2.3) prove (0.6).

The mechanism is geometric in logarithmic coordinates. The first Fourier
mode completes almost exactly one turn across \([0,\log X]\), but the
\(n^{-1/2}\) counting density grows like \(e^{u/2}\). The endpoint therefore
dominates instead of canceling.

## 3. Exact low-frequency order converts coherence into a power witness

The pinned kernel theorem gives

\[
 \widehat B_{r,\infty}(t)
 =\Phi_\ell(it)
 \left({1-e^{-i\varepsilon t}\over\varepsilon}\right)^r
 \widehat K_{\rm bd}(it),
\tag{3.1}
\]

where

\[
 \Phi_\ell(0)=1,\qquad
 \widehat K_{\rm bd}(0)=K_0\ne0.
\tag{3.2}
\]

Therefore, for fixed \(r\),

\[
 \widehat B_{r,\infty}(t)
 =K_0(it)^r(1+O_r(|t|))
\qquad(t\to0).
\tag{3.3}
\]

At \(t=t_{1,X}\),

\[
 {|\widehat B_{r,\infty}(t_{1,X})|^2\over L_X}
 =K_0^2(2\pi)^{2r}L_X^{-(2r+1)}(1+o(1)).
\tag{3.4}
\]

Combining (3.4) with (0.6) proves (0.7).

This is the first retained coordinate of the exact guarded Fourier lattice,
not a continuum approximation. The theorem does not claim that the actual
signed beta value \(D_X(t_{1,X})\) is large.

## 4. The critical Gram has a power-size coherent eigenvalue

Let

\[
 v_X(n)={|\beta(n)|\over\sqrt n},\qquad n\le X.
\tag{4.1}
\]

The retained Gram quadratic form is

\[
 \langle G_Xv_X,v_X\rangle
 ={1\over L_X}\sum_{0<|k|\le K_*}
 |\widehat B(t_{k,X})|^2|P_X(t_{k,X})|^2.
\tag{4.2}
\]

Every term is nonnegative, so the \(k=1\) row and (0.7) imply

\[
 \langle G_Xv_X,v_X\rangle
 \gg_r {X\over(\log X)^{2r+1}}.
\tag{4.3}
\]

Since \(|\beta(n)|\le2\),

\[
 \|v_X\|_2^2
 \le4\sum_{n\le X}{1\over n}
 \le4(1+\log X).
\tag{4.4}
\]

The Rayleigh quotient proves (0.9).

This closes a tempting shortcut:

> A source-blind operator-norm, Bessel, or low-rank estimate for the
> retained Gram cannot be subpower. Any successful theorem must exploit
> cancellation from the actual beta/Möbius signs or another equally
> source-specific structure.

## 5. How deep would a moving notch have to be?

Now let

\[
 r=r(X)=O\!\left({\log X\over\log\log X}\right).
\tag{5.1}
\]

This remains \(o(\log X)\), so

\[
 L_X=\log X+O(r)=\log X(1+o(1)),
 \qquad t_{1,X}={2\pi\over\log X}(1+o(1)).
\tag{5.2}
\]

Moreover,

\[
 \left(
 {1-e^{-i\varepsilon t}\over i\varepsilon t}
 \right)^{r}
 =\exp(O(rt))=1+o(1)
\tag{5.3}
\]

at the first harmonic. Thus the logarithm of the coherent coordinate is

\[
 \log X-(2r+1)\log\log X+O(r)+o(\log X).
\tag{5.4}
\]

Substitution of (0.10) gives (0.11).

For fixed \(r\), the exponent is one. For
\(r=o(\log X/\log\log X)\), it is still \(1-o(1)\). The first possible
subpower threshold is

\[
 r(X)\ge\left({1\over2}+o(1)\right)
 {\log X\over\log\log X}.
\tag{5.5}
\]

This does not recommend such a detector. The canonical RH equivalence uses
one fixed kernel, and a horizon-dependent order would require a new
Mellin--Landau and uniform-tail audit. Equation (5.5) only quantifies how
far fixed notching is from suppressing a coherent unsigned source.

## 6. Relation to the spectral witness principle

The predecessor proves that RH is equivalent to bounding the largest
weighted **signed** beta coordinate. The present packet proves that the
same weighted frame has a huge coherent direction when signs are forgotten.

The combined verdict is precise:

~~~text
subpower rank
  does not imply
small operator norm;

fixed notch
  does not imply
small coherent first harmonic;

literal local beta multiplicities
  do not imply
signed beta cancellation.
~~~

What remains is genuinely arithmetic control of the signed value

\[
 {\widehat B(t_{k,X})\over\sqrt{L_X}}
 \sum_{n\le X}{\beta(n)\over n^{1/2+it_{k,X}}}
\tag{6.1}
\]

uniformly over the retained witness lattice, or an equivalent assembled
argument which preserves its signs.

## 7. Claim ledger

| statement | grade |
|---|---|
| beta magnitude decomposition (1.1) | **PROVED COEFFICIENTWISE** |
| magnitude Dirichlet series (1.3) | **PROVED BY EULER FACTORS** |
| magnitude density (1.6) | **PROVED FROM THE CLASSICAL SQUAREFREE COUNT** |
| first-harmonic asymptotic (0.6) | **PROVED BY UNIFORM PARTIAL SUMMATION** |
| coherent weighted coordinate (0.7) | **PROVED FROM THE PINNED EXACT LOW-FREQUENCY ORDER** |
| retained-Gram operator lower bound (0.9) | **PROVED BY THE RAYLEIGH QUOTIENT** |
| growing-notch frontier (0.11) | **PROVED FOR THE UNSIGNED SOURCE MODEL** |
| moving-notch RH-equivalent detector | **NOT CLAIMED** |
| actual signed beta witness bound | **OPEN / RH-EQUIVALENT** |
| RH or GRH | **NOT PROVED** |

## 8. Bounded replay

~~~text
python -B research/l-families/atlas/function_field/ffps_critical_lattice_first_harmonic_firewall.py --check
python -B -O research/l-families/atlas/function_field/ffps_critical_lattice_first_harmonic_firewall.py --check
python -B -m unittest tests.test_ffps_critical_lattice_first_harmonic_firewall
python -B -O -m unittest tests.test_ffps_critical_lattice_first_harmonic_firewall
python -B -m ruff check research/l-families/atlas/function_field/ffps_critical_lattice_first_harmonic_firewall.py tests/test_ffps_critical_lattice_first_harmonic_firewall.py
python -B -m ruff format --check research/l-families/atlas/function_field/ffps_critical_lattice_first_harmonic_firewall.py tests/test_ffps_critical_lattice_first_harmonic_firewall.py
~~~

The replay checks the beta-magnitude identity through \(625\), including
explicit exceptional-prime layers, one four-cell exact Gaussian coherent
mode, and the rational notch-frontier exponents. It enumerates no prime,
zero, curve, conductor, field, or \(L\)-function and performs no
floating-point computation.
