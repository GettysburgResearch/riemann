# Cyclic color phases collapse the Witt entropy barrier

Status: **exact root-of-unity local adapter, content-necklace
specialization, grouped normal convergence on
\(|u|<c^{-1/c}\), and exponential critical-normalized decay when
\(q^c>c^2\); no optimal-radius or natural-boundary claim, native cyclic
mask/sheaf realization, number-field transfer, RH, or GRH result**

Bounded replay:
[function_field_cyclic_color_witt_resonance.py](function_field_cyclic_color_witt_resonance.py).
Canonical summary:
[function_field_cyclic_color_witt_resonance.json](function_field_cyclic_color_witt_resonance.json).

Frozen source: the complete multicolor Witt theorem at commit
**2d4e06ccc65b337f05410219f366323c40a4a8d5**. The producer pins its
complete quartet by Git blob ID and checks the imported working-tree
producer before executing it.

## 0. Outcome

Let \(q\) be a prime power, \(c\ge2\), and
\(\omega=e^{2\pi i/c}\). Give the \(c\) mutually exclusive colors the
complete cyclic phase set

\[
 \mathbf z_{\rm cyc}=(1,\omega,\ldots,\omega^{c-1}).
\tag{0.1}
\]

The phase power sums are

\[
\boxed{
 p_d:=\sum_{j=0}^{c-1}\omega^{jd}
 =
 \begin{cases}
 c,&c\mid d,\\
 0,&c\nmid d.
 \end{cases}}
\tag{0.2}
\]

Consequently the native local factor at an irreducible \(P\) is

\[
 1-u^{\deg P}p_{\deg P}
 =
 \begin{cases}
 1-cu^{\deg P},&c\mid\deg P,\\
 1,&c\nmid\deg P.
 \end{cases}
\tag{0.3}
\]

Thus the cyclic specialization of the complete color series is exactly

\[
\boxed{
 F^{\rm cyc}_{q,c}(u)
 =\prod_{\substack{P\\c\mid\deg P}}
  (1-cu^{\deg P}).}
\tag{0.4}
\]

This sparse Euler adapter is only the first cancellation. The stronger
fact is that the content-refined Witt product can be grouped by word
length and continued normally on every closed disk

\[
\boxed{|u|\le r<c^{-1/c}.}
\tag{0.5}
\]

Therefore, for every \(n\ge0\),

\[
\boxed{
 |[u^n]F^{\rm cyc}_{q,c}(u)|
 \le C_{q,c,r}r^{-n}.}
\tag{0.6}
\]

A critical radius

\[
 q^{-1/2}<r<c^{-1/c}
\tag{0.7}
\]

exists exactly when

\[
\boxed{
 q>c^{2/c}
 \quad\Longleftrightarrow\quad
 q^c>c^2.}
\tag{0.8}
\]

In that regime,

\[
\boxed{
 q^{-n/2}|[u^n]F^{\rm cyc}_{q,c}(u)|
 \le C_{q,c,r}(r\sqrt q)^{-n},}
\tag{0.9}
\]

so the complete cyclic shell decays exponentially after critical
normalization.

This replaces the uniform color-square condition \(q>c^2\) by a
phase-coherent threshold:

| colors \(c\) | uniform phase-torus disk | cyclic disk | cyclic critical condition |
|---:|---:|---:|---:|
| \(2\) | \(1/2\) | \(2^{-1/2}\) | \(q>2\) |
| \(3\) | \(1/3\) | \(3^{-1/3}\) | \(q^3>9\) |
| \(4\) | \(1/4\) | \(4^{-1/4}\) | \(q>2\) |
| \(c\ge5\) | \(1/c\) | \(c^{-1/c}\) | every integer \(q\ge2\) |

The last row uses \(c^{2/c}<2\) for \(c\ge5\). This is a theorem about one
exact phase fiber. It does not improve the phase-uniform radius and does
not say that \(c^{-1/c}\) is optimal.

## 1. Content-necklace specialization

For a nonzero content vector
\(\mathbf a=(a_0,\ldots,a_{c-1})\), let \(M(\mathbf a)\) be the primitive
necklace multiplicity from the frozen multicolor theorem. At length \(k\)
define the content-necklace polynomial

\[
 S_k(\mathbf z)
 =\sum_{|\mathbf a|=k}M(\mathbf a)\mathbf z^{\mathbf a}.
\tag{1.1}
\]

Multivariate Möbius inversion gives the exact Witt polynomial identity

\[
\boxed{
 S_k(\mathbf z)
 ={1\over k}\sum_{d\mid k}\mu(d)
 \left(\sum_{j=0}^{c-1}z_j^d\right)^{k/d}.}
\tag{1.2}
\]

For a positive integer \(\ell\), set

\[
 g_\ell=(c,\ell),
 \qquad
 h_\ell={c\over g_\ell}.
\tag{1.3}
\]

At \(\mathbf z=\mathbf z_{\rm cyc}^{\,\ell}\), the inner power sum in
(1.2) is nonzero only if \(c\mid\ell d\), equivalently
\(h_\ell\mid d\). Hence

\[
\boxed{
 |S_k(\mathbf z_{\rm cyc}^{\,\ell})|
 \le{\tau(k)\over k}\,c^{k/h_\ell}.}
\tag{1.4}
\]

Terms with no eligible divisor simply vanish. The bound is deliberately
one-sided; cancellation among the surviving Möbius terms can improve it.

## 2. Grouped normal convergence

Group the exact multicolor Witt product by content length:

\[
 F^{\rm cyc}_{q,c}(u)
 =\prod_{k\ge1}G_k(u),
 \qquad
 G_k(u)=
 \prod_{|\mathbf a|=k}
 \left(
  1-qu^k\omega^{\sum_jja_j}
 \right)^{M(\mathbf a)}.
\tag{2.1}
\]

Fix \(r<c^{-1/c}\) and put

\[
 \theta=rc^{1/c}<1.
\tag{2.2}
\]

Choose \(K\) so large that \(qr^K<1/2\). The finitely many factors
\(G_k\) with \(k<K\) are polynomials and cause no analytic obstruction.
For \(k\ge K\), the principal logarithm expands absolutely:

\[
 \log G_k(u)
 =-\sum_{\ell\ge1}{q^\ell u^{k\ell}\over\ell}
 S_k(\mathbf z_{\rm cyc}^{\,\ell}).
\tag{2.3}
\]

Because \(g_\ell\le\ell\),

\[
 h_\ell\ell={c\ell\over g_\ell}\ge c.
\tag{2.4}
\]

Combining (1.4) and (2.4) gives, on \(|u|\le r\),

\[
\begin{aligned}
 |u|^{k\ell}
 |S_k(\mathbf z_{\rm cyc}^{\,\ell})|
 &\le{\tau(k)\over k}
 r^{k\ell}c^{k/h_\ell}\\
 &\le{\tau(k)\over k}\theta^{k\ell}.
\end{aligned}
\tag{2.5}
\]

After increasing \(K\) so that \(q\theta^K<1/2\), the double logarithmic
tail is dominated by

\[
 \sum_{k\ge K}{\tau(k)\over k}
 \sum_{\ell\ge1}{(q\theta^k)^\ell\over\ell},
\tag{2.6}
\]

which converges. The convergence is normal on every disk in (0.5).
Exponentiating the tail and restoring the finite polynomial head proves
(0.5). Cauchy's formula proves (0.6).

This regrouping matters. Taking absolute values content by content forgets
the root-of-unity interference and recovers only the smaller disk
\(|u|<1/c\).

## 3. Exact cyclic threshold

The overlap (0.7) is equivalent to

\[
 q^{-1/2}<c^{-1/c}.
\tag{3.1}
\]

Both sides are positive, so raising to the power \(2c\) gives the exact
integer comparison \(q^c>c^2\). Once a radius in (0.7) is fixed, (0.9)
follows immediately from (0.6).

The threshold is surprisingly permissive:

\[
\begin{array}{c|c|c}
c&q\text{ at the first prime-power control}&q^c-c^2\\ \hline
2&3&5\\
3&3&18\\
4&3&65\\
5&2&7.
\end{array}
\tag{3.2}
\]

At \(c=3,q=2\), the exact comparison fails:
\(2^3-3^2=-1\). The packet infers neither decay nor failure there.

## 4. Relevance to cyclic-mask design

The multicolor phase-torus theorem measures worst-case coherent entropy.
The present theorem shows that a cyclic Fourier fiber can erase most of
that entropy before any norm is taken:

\[
\text{uniform colors: }c^k
\quad\leadsto\quad
\text{cyclic grouped scale: }c^{k/c}.
\tag{4.1}
\]

This is directly suggestive for the ternary physical-mask programme.
A genuine arithmetic adapter with three cyclic Kummer modes should be
assembled in its Fourier fiber before applying a positive energy estimate.
If it realizes (0.1) with the complete cubic phase set, its formal color
tax is governed by \(q^3>9\), not \(q>9\).

That conditional sentence is load-bearing. The native FFPS source also has
owner labels, Boolean incidences, diagonals, Artin--Schreier pieces, and
varying closed-place degrees. This packet does not prove that those
components form the mutually exclusive local color model, nor that a
cohomological pushforward preserves the cyclic grouping.

No number-field estimate follows. The grouped continuation uses the exact
polynomial Witt identity.

## 5. Claim ledger

| statement | grade |
|---|---|
| cyclic root-of-unity adapter (0.2)--(0.4) | **PROVED EXACT** |
| content-necklace identity (1.2) | **PROVED EXACT** |
| cyclic bound (1.4) | **PROVED** |
| grouped continuation to \(|u|<c^{-1/c}\) | **PROVED BY NORMAL CONVERGENCE** |
| critical decay for \(q^c>c^2\) | **PROVED** |
| optimality or natural boundary at \(c^{-1/c}\) | **NOT CLAIMED** |
| native cyclic-mask or sheaf realization | **NOT INCLUDED** |
| number-field transfer | **NOT INFERRED** |
| RH or GRH | **NOT PROVED** |

No external novelty claim is made without a dedicated literature
comparison.

## 6. Bounded replay

The replay accepts formal integer \(q\ge2\); the field-theoretic theorem
requires \(q\) to be a prime power. It substitutes the cyclic phases in
the complete direct Euler and content-Witt dictionaries and reduces
exactly in the cyclotomic quotient:

- \(c=2,q=3\), through total degree seven;
- \(c=3,q=3\), through total degree five.

Both dictionaries collapse to the sparse Euler adapter (0.4). The tests
also verify the content-necklace specialization for \(c=2,3,4\), the exact
integer threshold, and the \(c=3,q=2\) non-overlap control.

There is no finite-field element, finite-field polynomial, irreducible,
curve, point, floating-point, random, or zeta-zero enumeration.

~~~text
python -B research/l-families/atlas/function_field/function_field_cyclic_color_witt_resonance.py --check
python -B -O research/l-families/atlas/function_field/function_field_cyclic_color_witt_resonance.py --check
python -B -m unittest tests.test_function_field_cyclic_color_witt_resonance
python -B -O -m unittest tests.test_function_field_cyclic_color_witt_resonance
python -B -m ruff check research/l-families/atlas/function_field/function_field_cyclic_color_witt_resonance.py tests/test_function_field_cyclic_color_witt_resonance.py
python -B -m ruff format --check research/l-families/atlas/function_field/function_field_cyclic_color_witt_resonance.py tests/test_function_field_cyclic_color_witt_resonance.py
~~~
