# Coherent colors and rough deletion have an exact Witt phase surface

Status: **exact multicolor rough quotient, uniform finite-deletion
conditioning, exponential critical-normalized decay in the proven
\(q>c^2,\ \limsup y_n/\log_qn<2\) region, and a matching barrier for this
absolute conditioning method beyond \(2\log_q n\); no claim of a sharp
signed-coefficient boundary, native FFPS/sheaf realization, number-field
transfer, RH, or GRH result**

Bounded replay:
[function_field_multicolor_rough_witt_phase_surface.py](function_field_multicolor_rough_witt_phase_surface.py).
Canonical summary:
[function_field_multicolor_rough_witt_phase_surface.json](function_field_multicolor_rough_witt_phase_surface.json).

Frozen inputs are the multicolor Witt theorem at commit
**2d4e06ccc65b337f05410219f366323c40a4a8d5** and the binary rough-frontier
theorem at commit **11552aea89380809f45ff002eb0c6927c70ab1f2**. The replay
pins both complete quartets by Git blob ID and checks the imported
working-tree producer before executing it.

## 0. Outcome

Let \(q\) be a prime power, \(c\ge2\), \(y\) a nonnegative integer, and
\(|z_i|=1\). The complete colored squarefree series is

\[
 F_{q,c}(u;\mathbf z)
 =\prod_P\left(1-\sum_{i=1}^c(uz_i)^{\deg P}\right).
\tag{0.1}
\]

Delete every irreducible of degree at most \(y\):

\[
\begin{aligned}
 D_{q,c,y}(u;\mathbf z)
 &=\prod_{\deg P\le y}
   \left(1-\sum_{i=1}^c(uz_i)^{\deg P}\right),\\
 F_{q,c,>y}(u;\mathbf z)
 &=\prod_{\deg P>y}
   \left(1-\sum_{i=1}^c(uz_i)^{\deg P}\right).
\end{aligned}
\tag{0.2}
\]

Then, as formal series and throughout the guaranteed Witt disk,

\[
\boxed{
 F_{q,c,>y}(u;\mathbf z)
 ={F_{q,c}(u;\mathbf z)\over D_{q,c,y}(u;\mathbf z)}.}
\tag{0.3}
\]

Fix \(0<r<1/c\). On \(|u|\le r\),

\[
 \left|
  1-\sum_{i=1}^c(uz_i)^{\deg P}
 \right|
 \ge1-cr^{\deg P}>0.
\tag{0.4}
\]

Thus finite rough deletion creates no pole there. Its exact phase-uniform
condition number is bounded by

\[
\boxed{
 K_{q,c,y}(r)
 :=\prod_{\deg P\le y}(1-cr^{\deg P})^{-1},
 \qquad
 \log K_{q,c,y}(r)
 \ll_{q,c,r}{(qr)^y\over y}}
\tag{0.5}
\]

when \(qr>1\) and \(y\ge1\). At \(y=0\), \(K_{q,c,0}(r)=1\).
Combining (0.5) with the multicolor Witt bound gives, for every \(n\ge0\)
and \(y\ge1\),

\[
\boxed{
 \sup_{|z_1|=\cdots=|z_c|=1}
 |[u^n]F_{q,c,>y}(u;\mathbf z)|
 \le C_{q,c,r}r^{-n}
 \exp\left(
  O_{q,c,r}\left({(qr)^y\over y}\right)
 \right).}
\tag{0.6}
\]

There are now two independent axes.

For \(y=0\), the exponential conditioning term in (0.6) is replaced by
one. First, a critical radius satisfying

\[
 q^{-1/2}<r<1/c
\tag{0.7}
\]

exists exactly when \(q>c^2\). Second, as \(n\to\infty\), let \(y_n\) be
nonnegative integers. For fixed \(0<\eta<2\), if

\[
\boxed{y=y_n\le(2-\eta)\log_q n,}
\tag{0.8}
\]

then \(r\) can be chosen in (0.7), sufficiently close to \(q^{-1/2}\), so
that

\[
 (qr)^{y_n}=O(n^{1-\delta})
\tag{0.9}
\]

for some \(\delta=\delta(q,c,\eta)>0\). Consequently, for some
\(a_{q,c,\eta}>0\),

\[
\boxed{
 q^{-n/2}
 \sup_{|z_1|=\cdots=|z_c|=1}
 |[u^n]F_{q,c,>y_n}(u;\mathbf z)|
 \le
 \exp\left(-a_{q,c,\eta}n+O(n^{1-\delta})\right).}
\tag{0.10}
\]

The complete rough colored shell therefore still decays exponentially
after critical normalization in the proven open region

\[
\boxed{
 q>c^2,\qquad
 \limsup_{n\to\infty}{y_n\over\log_qn}<2.}
\tag{0.11}
\]

The depth exponent \(2\) is also a barrier for this **absolute
finite-deletion conditioning method**. For every fixed radius in (0.7),
the phase \(\mathbf z=(1,\ldots,1)\) gives

\[
\boxed{
 \log K_{q,c,y}(r)
 \gg_{q,c,r}{(qr)^y\over y}.}
\tag{0.12}
\]

If

\[
 y_n\ge(2+\eta)\log_q n,
\tag{0.13}
\]

then monotonicity of \((qr)^t/t\) for large \(t\) gives

\[
 \log K_{q,c,y_n}(r)
 \ge n^{1+\eta/2-o(1)}.
\tag{0.14}
\]

So every critical-radius Cauchy estimate which pays the deleted factors
absolutely has a superexponential condition budget. This proves a method
barrier, not a lower bound for the signed coefficient. Cancellation in the
quotient or another signed representation could survive beyond (0.13).

The resulting two-axis diagram is:

| region | this packet proves |
|---|---|
| \(q>c^2,\ y_n\le(2-\eta)\log_qn\) for fixed \(\eta>0\) | exponential critical-normalized decay |
| \(q>c^2,\ y_n\ge(2+\eta)\log_qn\) | absolute finite-deletion Cauchy method is superexponentially ill-conditioned |
| \(q\le c^2\) | no critical radius in the guaranteed Witt disk; behavior not claimed |
| \(y_n=2\log_qn+o(\log n)\) | boundary left open |

## 1. Exact quotient and colored-core stability

Each irreducible has one absent state and \(c\) mutually exclusive colored
states. Restricting all selected irreducibles to degree \(>y\) deletes
exactly the local factors of degrees at most \(y\). Multiplication of the
deleted and retained products reassembles (0.1), proving (0.3).

The statement is phase-coherent. No colorwise absolute value is inserted
in (0.1)--(0.3); the triangle inequality first appears only in the
condition-number estimate (0.4).

There is also a fixed-core corollary. Fix a squarefree colored polynomial
core \(U\), and let \(\Omega_{\mathbf z}(U)\) be its phase monomial,
including its squarefree sign. Requiring every additional irreducible to
avoid both \(U\) and the degree-\(\le y\) set gives

\[
 u^{\deg U}\Omega_{\mathbf z}(U)\,
 {F_{q,c}(u;\mathbf z)\over
  \displaystyle
  \prod_{\substack{\deg P\le y\\\text{or }P\mid U}}
  \left(1-\sum_i(uz_i)^{\deg P}\right)}.
\tag{1.1}
\]

For fixed \(U\) this is a finite monomial multiplier times a finite
deletion quotient, so it preserves the same open Witt disk. A core growing
with \(n\), overlapping colors, or a nonlocal mask is not covered.

## 2. Uniform condition number

Let \(I_q(d)\) denote the number of monic irreducibles of degree \(d\).
Equation (0.4) gives

\[
 \log K_{q,c,y}(r)
 =\sum_{d\le y}I_q(d)\bigl[-\log(1-cr^d)\bigr].
\tag{2.1}
\]

Since \(cr<1\),

\[
 -\log(1-cr^d)\ll_{c,r}r^d.
\tag{2.2}
\]

The elementary root count \(dI_q(d)\le q^d\) therefore yields

\[
 \log K_{q,c,y}(r)
 \ll_{c,r}\sum_{d\le y}{(qr)^d\over d}
 \ll_{q,c,r}{(qr)^y\over y},
\tag{2.3}
\]

for \(qr>1\). The complete multicolor Witt product is uniformly bounded
on \(|u|\le r<1/c\), so Cauchy's formula applied to (0.3) proves (0.6).

## 3. Why the frontier remains \(2\)

Assume \(q>c^2\). For \(r=q^{-1/2+\varepsilon}\),

\[
 \log_q(qr)=\frac12+\varepsilon.
\tag{3.1}
\]

Choose

\[
 0<\varepsilon<
 \min\left\{
  {1\over2}-\log_qc,\,
  {1\over2-\eta}-{1\over2}
 \right\}.
\tag{3.2}
\]

The first inequality puts \(r\) in (0.7); the second gives
\((2-\eta)(1/2+\varepsilon)<1\). Equations (0.8)--(0.9) follow. Meanwhile
\(r\sqrt q>1\), so

\[
 q^{-n/2}r^{-n}
 =\exp\bigl(-n\log(r\sqrt q)\bigr).
\tag{3.3}
\]

This negative linear exponent dominates the conditioning term in (0.6)
and proves (0.10).

For the reverse method barrier, set all phases equal to one. The lower
triangle inequality in (0.4) is then an equality on the positive real
radius, and

\[
 -\log(1-cr^d)\ge cr^d.
\tag{3.4}
\]

The prime-polynomial theorem in its elementary fixed-\(q\) form,

\[
 I_q(d)={q^d\over d}+O_q(q^{d/2}),
\tag{3.5}
\]

gives (0.12) from the single degree-\(y\) row. Put
\(Y=(2+\eta)\log_qn\) and \(a=qr>\sqrt q\). Since \(a^t/t\) is increasing
for large \(t\),

\[
 {(qr)^{y_n}\over y_n}
 \ge{(qr)^Y\over Y}
 \ge{n^{1+\eta/2}\over(2+\eta)\log_qn}
 =n^{1+\eta/2-o(1)}.
\tag{3.6}
\]

This proves (0.14), and nothing stronger about the signed coefficients.

## 4. Detector-design interpretation

The two taxes are orthogonal:

\[
\begin{array}{ccl}
\text{color entropy} &:& c<\sqrt q,\\
\text{rough deletion depth} &:&
\displaystyle\limsup_{n\to\infty}{y_n\over\log_qn}<2.
\end{array}
\tag{4.1}
\]

Adding coherent local states contracts the guaranteed analytic disk.
Deleting a growing band of low-degree places consumes the remaining
Cauchy budget through its condition number. Neither tax is visible if one
only checks a fixed color count and a fixed rough cutoff.

For the atlas, (4.1) is a concrete source-design constraint. A scalable
colored family adapter should either stay inside both axes or exploit
signed cancellation that is invisible to absolute conditioning. The
packet does not show that the native owner/Boolean/Artin--Schreier source
has the mutually exclusive local factor (0.1).

No number-field estimate is inferred. The exact Witt continuation uses
the polynomial zeta identity and has no literal integer Euler-product
counterpart.

## 5. Claim ledger

| statement | grade |
|---|---|
| multicolor rough quotient (0.3) | **PROVED EXACT** |
| phase-uniform condition number (0.5) | **PROVED** |
| two-axis subfrontier (0.10)--(0.11) | **PROVED** |
| absolute-conditioning barrier (0.12)--(0.14) | **PROVED** |
| fixed colored-core stability (1.1) | **PROVED** |
| sharp signed rough frontier | **NOT CLAIMED** |
| behavior at \(y\sim2\log_qn\) | **OPEN IN THIS PACKET** |
| behavior for \(q\le c^2\) | **NOT CLAIMED** |
| native FFPS or sheaf realization | **NOT INCLUDED** |
| number-field transfer | **NOT INFERRED** |
| RH or GRH | **NOT PROVED** |

No external novelty claim is made without a dedicated literature
comparison.

## 6. Bounded replay

The replay accepts formal integer \(q\ge2\); the field-theoretic theorem
requires \(q\) to be a prime power. It uses exact multivariate integer
dictionaries for the control
\((c,q,n,y)=(3,11,5,2)\). It checks that deleted and rough factors
reassemble the complete product, records the exact critical-radius
condition number at \(r=8/25\), and rechecks the binary specialization.
The unit tests also cover both \(c=2\) and \(c=3\) through degree five.

There is no finite-field element, finite-field polynomial, irreducible,
curve, point, zeta zero, floating-point fit, or random sample enumeration.

~~~text
python -B research/l-families/atlas/function_field/function_field_multicolor_rough_witt_phase_surface.py --check
python -B -O research/l-families/atlas/function_field/function_field_multicolor_rough_witt_phase_surface.py --check
python -B -m unittest tests.test_function_field_multicolor_rough_witt_phase_surface
python -B -O -m unittest tests.test_function_field_multicolor_rough_witt_phase_surface
python -B -m ruff check research/l-families/atlas/function_field/function_field_multicolor_rough_witt_phase_surface.py tests/test_function_field_multicolor_rough_witt_phase_surface.py
python -B -m ruff format --check research/l-families/atlas/function_field/function_field_multicolor_rough_witt_phase_surface.py tests/test_function_field_multicolor_rough_witt_phase_surface.py
~~~
