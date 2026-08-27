# The complete function-field divisor wavelet has an exact Witt factorization

Status: **exact all-\(q\) squarefree divisor-orientation identity, exact
content-refined Witt factorization, and exponential critical normalization
decay for every \(q\ge5\); no growing sieve/core theorem, maximal-height
wavelet estimate, number-field WAVEPRIMCAR, RH, or GRH result**

Bounded replay:
[function_field_divisor_wavelet_witt_factorization.py](function_field_divisor_wavelet_witt_factorization.py).
Canonical summary:
[function_field_divisor_wavelet_witt_factorization.json](function_field_divisor_wavelet_witt_factorization.json).

Frozen source: commit
`fad8ce2c4ce8633c5bb67356e6765800eac3d440`. The producer pins the
Markdown and replay blobs of the `BASEWAVE = PRIMCAR` identity and the
literal function-field beta/evaluation adapter.

## 0. Outcome

Let \(q\) be a prime power and let \(\mathcal M_q\) be the monic
polynomials in \(\mathbf F_q[T]\). For a monic squarefree \(N\), define its
complete divisor-orientation character

\[
 \Omega_z(N)
 =\mu(N)\sum_{A\mid N}z^{\,2\deg A-\deg N},
 \qquad z\in\mathbf C^\times.
\tag{0.1}
\]

If \(N=\prod_P P\), then

\[
 \boxed{
 \Omega_z(N)
 =\prod_{P\mid N}
   -\bigl(z^{\deg P}+z^{-\deg P}\bigr).}
\tag{0.2}
\]

Consequently its complete degree generating function is

\[
\boxed{
 F_q(u,z)
 :=\sum_{\substack{N\in\mathcal M_q\\N\ {\rm squarefree}}}
   \Omega_z(N)u^{\deg N}
 =\prod_P
  \left(1-(uz)^{\deg P}-(u/z)^{\deg P}\right).}
\tag{0.3}
\]

This is the exact function-field counterpart of the coherent divisor
Fourier wavelet

\[
 \mu(N)\sum_{A\mid N}
 e^{it(2\log A-\log N)}
\]

appearing before the near-square kernel and height truncation in the
integer `WAVEPRIMCAR` route.

For \(a,b\ge0\), \(a+b>0\), put

\[
\boxed{
 M(a,b)
 ={1\over a+b}
 \sum_{d\mid\gcd(a,b)}
 \mu(d){(a+b)/d\choose a/d}.}
\tag{0.4}
\]

This is the nonnegative integer counting primitive binary necklaces with
content \((a,b)\). The multivariate Witt identity gives the second exact
factorization

\[
\boxed{
 F_q(u,z)
 =\prod_{\substack{a,b\ge0\\a+b>0}}
 \left(1-q\,u^{a+b}z^{a-b}\right)^{M(a,b)}.}
\tag{0.5}
\]

The two length-one necklaces give

\[
 (1-quz)(1-qu/z).
\tag{0.6}
\]

These are the two universal affine-zeta modes. Every remaining factor has
total necklace length at least two. Formula (0.5) is not a numerical fit
and does not enumerate irreducible polynomials: it follows by applying the
polynomial zeta identity

\[
 \prod_P(1-v^{\deg P})=1-qv
\tag{0.7}
\]

to every factor in the formal Witt decomposition of \(1-X-Y\).

The factorization has a strong analytic consequence. Uniformly for
\(|z|=1\), the product in (0.5) converges normally on every closed disk

\[
 |u|\le r<\frac12.
\tag{0.8}
\]

Thus it analytically continues (0.3) from its original Euler-product disk
to \(|u|<1/2\). Cauchy's estimate gives, for every \(r<1/2\),

\[
\boxed{
 \sup_{|z|=1}
 \left|[u^n]F_q(u,z)\right|
 \le C_{q,r}r^{-n}.}
\tag{0.9}
\]

After the critical function-field normalization, this becomes

\[
\boxed{
 q^{-n/2}
 \sup_{|z|=1}
 \left|[u^n]F_q(u,z)\right|
 \le C_{q,r}(r\sqrt q)^{-n}.}
\tag{0.10}
\]

For every \(q\ge5\), choose

\[
 q^{-1/2}<r<1/2.
\]

Then the right side decays exponentially. Hence the complete coherent
divisor-orientation shell is not merely of square-root size in those
function fields: after critical normalization it is exponentially small,
uniformly in the Fourier phase.

This resolves one literal function-field shadow of the integer wavelet's
zero-frequency divisor-loss channel. It does **not** prove the integer
gate. The exact cancellation uses all monic squarefree \(N\) of one
degree, all divisor colors, and the full polynomial Euler algebra before
any norm. A growing coprimality sieve, fixed core \(u\), exceptional
`67`-channels, interval endpoint, or maximal-height cutoff can break the
factorization and remains outside the theorem.

## 1. The divisor orientation is a two-color Euler product

For one irreducible factor \(P\mid N\), a divisor \(A\mid N\) has two
choices:

- put \(P\) in \(A\), contributing \(z^{\deg P}\);
- put \(P\) in \(N/A\), contributing \(z^{-\deg P}\).

The squarefree Möbius sign contributes \(-1\) for the selected prime. This
proves (0.2). Summing over the absent/selected states of every irreducible
gives (0.3).

Equivalently, set

\[
 X=uz,\qquad Y=u/z.
\tag{1.1}
\]

The local factor is simply

\[
 1-X^{\deg P}-Y^{\deg P}.
\tag{1.2}
\]

The point of retaining both colors coherently is visible here. Taking
absolute values before the local state sum replaces (1.2) by a positive
divisor-loss factor and destroys the algebra below.

## 2. Content-refined Witt identity

The formal identity

\[
\boxed{
 1-X-Y
 =\prod_{\substack{a,b\ge0\\a+b>0}}
  (1-X^aY^b)^{M(a,b)}}
\tag{2.1}
\]

is the two-letter Witt identity. A short coefficient proof is enough for
the present use. Take negative logarithms. The left side gives

\[
 -\log(1-X-Y)
 =\sum_{k\ge1}{(X+Y)^k\over k}.
\tag{2.2}
\]

The right side gives

\[
 \sum_{a,b}M(a,b)
 \sum_{\ell\ge1}{X^{a\ell}Y^{b\ell}\over\ell}.
\tag{2.3}
\]

Comparing the coefficient of \(X^rY^s\) and applying Möbius inversion on
\(\gcd(r,s)\) yields exactly (0.4). This also proves integrality by the
primitive-necklace interpretation. In particular,

\[
 \sum_{a+b=k}M(a,b)
 ={1\over k}\sum_{d\mid k}\mu(d)2^{k/d}
 =:L_k(2),
\tag{2.4}
\]

the number of binary Lyndon words of length \(k\). The first values are

\[
 2,1,2,3,6,9,18,30.
\tag{2.5}
\]

Apply (2.1) to \(X^{\deg P},Y^{\deg P}\) in every local factor (1.2).
As a formal power series in \(u\), every coefficient involves only
finitely many pairs \((a,b)\) and prime degrees, so the factors may be
reordered:

\[
\begin{aligned}
 F_q(u,z)
 &=\prod_P\prod_{a,b}
   \left(1-
    \bigl(u^{a+b}z^{a-b}\bigr)^{\deg P}
   \right)^{M(a,b)}\\
 &=\prod_{a,b}
   \left[
    \prod_P
    \left(1-
     \bigl(u^{a+b}z^{a-b}\bigr)^{\deg P}
    \right)
   \right]^{M(a,b)}.
\end{aligned}
\tag{2.6}
\]

Equation (0.7) turns the inner bracket into
\(1-q\,u^{a+b}z^{a-b}\), proving (0.5).

## 3. The analytic radius and the critical phase transition

Fix \(r<1/2\) and \(|z|=1\). Group the tail of (0.5) by
\(k=a+b\). Its total exponent at length \(k\) is \(L_k(2)\), and

\[
 0\le L_k(2)\le {2^k\over k}.
\tag{3.1}
\]

For all sufficiently large \(k\), \(q r^k\le1/2\), so

\[
 \sum_{a+b=k}
 M(a,b)
 \left|\log(1-q u^kz^{a-b})\right|
 \ll_q L_k(2)r^k
 \ll { (2r)^k\over k}.
\tag{3.2}
\]

The last series converges. Finitely many shorter factors are polynomials,
so zeros among them cause no singularity. This proves normal convergence,
uniformly in \(|z|=1\), and hence (0.8).

Cauchy's coefficient formula on \(|u|=r\) proves (0.9). Multiplying by
\(q^{-n/2}\) proves (0.10). The interval
\(q^{-1/2}<r<1/2\) is nonempty exactly when \(q>4\). This proves the
exponential critical decay for every prime power \(q\ge5\).

For \(q=3\), (0.9) still gives the uniform unnormalized
\((2+o(1))^n\) upper exponent, but it does not imply decay after
\(3^{-n/2}\) normalization. No \(q=3\) critical-decay claim is made.
The method's threshold is recorded rather than hidden.

## 4. Fixed degree-lattice kernels

Let \(\kappa_n:\mathbf Z\to\mathbf C\) have finite support, and define

\[
 S_n(\kappa_n)
 =\sum_{\substack{N\ {\rm monic\ squarefree}\\\deg N=n}}
  \mu(N)\sum_{A\mid N}
  \kappa_n(2\deg A-n).
\tag{4.1}
\]

Write its Fourier polynomial as

\[
 \widehat\kappa_n(\theta)
 =\sum_j\kappa_n(j)e^{-ij\theta}.
\tag{4.2}
\]

Fourier inversion and (0.1) give

\[
 S_n(\kappa_n)
 ={1\over2\pi}\int_0^{2\pi}
  \widehat\kappa_n(\theta)
  [u^n]F_q(u,e^{i\theta})\,d\theta.
\tag{4.3}
\]

Therefore

\[
\boxed{
 |S_n(\kappa_n)|
 \le C_{q,r}r^{-n}
 {1\over2\pi}\int_0^{2\pi}
 |\widehat\kappa_n(\theta)|\,d\theta.}
\tag{4.4}
\]

The elementary bound

\[
 {1\over2\pi}\int_0^{2\pi}
 |\widehat\kappa_n(\theta)|\,d\theta
 \le\sum_j|\kappa_n(j)|
\tag{4.5}
\]

shows that a uniformly \(\ell^1\)-bounded kernel family has uniformly
bounded Fourier algebra norm. This includes a fixed finitely supported
sampled log-ratio kernel. More generally, any horizon-dependent kernel
whose Fourier algebra norm is subexponential retains the same exponential
coefficient exponent. A rescaled sharp cutoff can have logarithmically
growing Fourier norm; that is still subexponential, but uniform boundedness
is not asserted for every use of the word “compact.” This covers the
complete degree-shell analogue of a fixed near-square autocorrelation
window.

It does not cover every predicate in `WAVEPRIMCAR`. In particular, a
coprimality sieve or a fixed nontrivial core changes local factors, while a
maximal endpoint supremum prevents the complete degree-shell assembly used
in (4.3).

## 5. What this says about the integer moonshot

The theorem isolates a mechanism rather than transferring a bound:

~~~text
coherently sum all divisor orientations
  -> two-color local factor 1-X^deg(P)-Y^deg(P)
  -> content-refined Witt decomposition
  -> one polynomial-zeta zero for every primitive color word
  -> analytic continuation to |u|<1/2
  -> exponential critical decay for q>=5.
~~~

The number-field Fourier--hyperbola proposal should therefore preserve the
analogues of both divisor colors, the Möbius sign, the complete local state
sum, the full Fourier phase, and the assembly across primitive color words.
Estimating each divisor orientation separately erases the exact Witt
mechanism.

Conversely, the present result warns against overclaiming from the
function-field laboratory: the rational polynomial zeta identity (0.7) is
much stronger than anything available for integer primes.

The next function-field target is to insert, one at a time, a fixed core,
a growing sieve, and a height endpoint, and measure exactly where the
normal-convergence radius degrades. The next number-field target remains a
signed mean-square or contour theorem which retains the two-color Euler
assembly. Neither target is proved here.

## 6. Claim ledger

| statement | grade |
|---|---|
| divisor-orientation product (0.2) | **PROVED EXACT** |
| complete two-color Euler product (0.3) | **PROVED EXACT** |
| necklace formula (0.4) | **PROVED BY MÖBIUS INVERSION / PRIMITIVE WORDS** |
| multivariate Witt factorization (0.5) | **PROVED AS A FORMAL IDENTITY** |
| polynomial-zeta substitution | **PROVED EXACT** |
| uniform continuation to \(|u|<1/2\) | **PROVED BY NORMAL CONVERGENCE** |
| coefficient bound (0.9) | **PROVED BY CAUCHY** |
| critical exponential decay for \(q\ge5\) | **PROVED** |
| critical decay for \(q=3\) | **NOT CLAIMED** |
| fixed degree-kernel bound (4.4) | **PROVED EXACTLY FROM FOURIER INVERSION** |
| growing sieve/core or maximal-height uniformity | **NOT INCLUDED** |
| integer `WAVEPRIMCAR` | **NOT PROVED** |
| RH or GRH | **NOT PROVED** |

No external novelty claim is made without a dedicated literature
comparison.

## 7. Bounded replay

The producer computes irreducible counts from the exact necklace formula;
it enumerates no irreducible or finite-field element. Through total degree
eight at \(q=3,5\), it expands both sides:

\[
 \prod_{d\le8}
 \left(1-u^dz^d-u^dz^{-d}\right)^{I_q(d)}
\]

and

\[
 \prod_{a+b\le8}
 \left(1-qu^{a+b}z^{a-b}\right)^{M(a,b)}.
\]

The complete Laurent coefficient dictionaries agree exactly. It also
checks every content-refined necklace multiplicity through length eight
and its sum (2.4). All arithmetic is integral; no polynomial, field
element, curve, point, floating-point fit, or zeta zero is enumerated.

~~~text
python -B research/l-families/atlas/function_field/function_field_divisor_wavelet_witt_factorization.py --check
python -B -O research/l-families/atlas/function_field/function_field_divisor_wavelet_witt_factorization.py --check
python -B -m unittest tests.test_function_field_divisor_wavelet_witt_factorization
python -B -O -m unittest tests.test_function_field_divisor_wavelet_witt_factorization
python -B -m ruff check research/l-families/atlas/function_field/function_field_divisor_wavelet_witt_factorization.py tests/test_function_field_divisor_wavelet_witt_factorization.py
python -B -m ruff format --check research/l-families/atlas/function_field/function_field_divisor_wavelet_witt_factorization.py tests/test_function_field_divisor_wavelet_witt_factorization.py
~~~
