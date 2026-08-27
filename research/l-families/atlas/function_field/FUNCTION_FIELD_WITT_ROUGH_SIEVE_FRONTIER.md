# The rough-sieved function-field divisor wavelet has an exponent-two conditioning frontier

Status: **exact finite rough-sieve quotient, exact fixed-core stability,
exponential critical decay below the degree-\(2\) logarithmic frontier, and
a matching barrier for absolute finite-deletion conditioning; no claim
that the actual rough coefficients fail beyond the frontier, no maximal
height wavelet, number-field transfer, RH, or GRH result**

Bounded replay:
[function_field_witt_rough_sieve_frontier.py](function_field_witt_rough_sieve_frontier.py).
Canonical summary:
[function_field_witt_rough_sieve_frontier.json](function_field_witt_rough_sieve_frontier.json).

Frozen source: the complete two-color Witt factorization at commit
`02555b216077a3cd3a1309eb530cd29b26c7f6a3`, with all four source blobs
pinned by the producer.

## 0. Outcome

Let \(q\) be a prime power. The predecessor proves that the complete
squarefree divisor-orientation series

\[
 F_q(u,z)
 =\prod_P\left(1-(uz)^{\deg P}-(u/z)^{\deg P}\right)
\tag{0.1}
\]

continues, uniformly for \(|z|=1\), to \(|u|<1/2\). For an integer
\(y\ge0\), remove every irreducible of degree at most \(y\):

\[
\boxed{
 F_{q,>y}(u,z)
 =\prod_{\deg P>y}
 \left(1-(uz)^{\deg P}-(u/z)^{\deg P}\right).}
\tag{0.2}
\]

Then the exact quotient identity is

\[
\boxed{
 F_{q,>y}(u,z)
 ={F_q(u,z)\over D_{q,y}(u,z)},\qquad
 D_{q,y}(u,z)
 =\prod_{\deg P\le y}
 \left(1-(uz)^{\deg P}-(u/z)^{\deg P}\right).}
\tag{0.3}
\]

For \(0<r<1/2\) and \(|z|=1\),

\[
 \left|
 1-(rz)^{\deg P}-(r/z)^{\deg P}
 \right|
 \ge1-2r^{\deg P}>0.
\tag{0.4}
\]

Thus finite rough deletion introduces no pole in the Witt disk. Its
uniform condition number satisfies

\[
\boxed{
 K_{q,y}(r)
 :=\prod_{\deg P\le y}(1-2r^{\deg P})^{-1},
 \qquad
 \log K_{q,y}(r)
 \ll_{q,r}{(qr)^y\over y}}
\tag{0.5}
\]

for \(qr>1\), with the harmless convention that the right side is replaced
by a constant at \(y=0\).

Cauchy's estimate therefore gives

\[
\boxed{
 \sup_{|z|=1}|[u^n]F_{q,>y}(u,z)|
 \le C_{q,r}r^{-n}
 \exp\left(O_{q,r}\left({(qr)^y\over y}\right)\right).}
\tag{0.6}
\]

This has the same exponent-\(2\) frontier as the independent integer
rough-preconditioner calculation. Fix \(q\ge5\) and \(\eta>0\). If

\[
\boxed{
 y=y_n\le(2-\eta)\log_q n,}
\tag{0.7}
\]

then one can choose

\[
 q^{-1/2}<r<1/2
\tag{0.8}
\]

so that

\[
 (qr)^{y_n}=O(n^{1-\delta})
\tag{0.9}
\]

for some \(\delta=\delta(q,\eta)>0\). Hence

\[
\boxed{
 q^{-n/2}
 \sup_{|z|=1}|[u^n]F_{q,>y_n}(u,z)|
 \le \exp(-c_{q,\eta}n+O(n^{1-\delta}))}
\tag{0.10}
\]

for a suitable \(c_{q,\eta}>0\). The complete rough degree shell still
decays exponentially after critical normalization.

The exponent \(2\) is also a sharp barrier for this **absolute
finite-deletion conditioning method**. For every fixed
\(q^{-1/2}<r<1/2\), the phase \(z=1\) gives

\[
\boxed{
 \log K_{q,y}(r)
 \gg_{q,r}{(qr)^y\over y}.}
\tag{0.11}
\]

If

\[
 y_n\ge(2+\eta)\log_q n,
\tag{0.12}
\]

then \(qr>\sqrt q\), together with monotonicity of \(a^t/t\) for
\(a=qr>1\) and large \(t\), forces the logarithm in (0.11) to exceed
\(n^{1+\eta/2-o(1)}\). No Cauchy estimate which pays the deleted factors
absolutely on a critical radius can retain an \(\exp(O(n))\) budget.

This is a method barrier, not a lower bound for the signed coefficient.
Cancellation between the numerator \(F_q\) and the deleted quotient, or a
different signed representation, could survive past (0.12). The exact
boundary \(y\sim2\log_qn\) is left open.

## 1. Exact quotient and fixed-core stability

Every irreducible local state is absent, left-colored, or right-colored.
Restricting the squarefree polynomial \(N\) to have no irreducible factor
of degree at most \(y\) simply deletes those local factors from the Euler
product. Multiplying the deleted and retained products reassembles (0.1)
coefficient by coefficient, proving (0.3).

More generally, let \(U\) be one fixed monic squarefree core. Sum
coherently over all placements of each factor of \(U\), and let the
remaining squarefree factor \(M\) satisfy \((M,U)=1\). The resulting core
series is

\[
\boxed{
 u^{\deg U}\Omega_z(U)
 {F_q(u,z)\over
  \displaystyle\prod_{P\mid U}
   \left(1-(uz)^{\deg P}-(u/z)^{\deg P}\right)},}
\tag{1.1}
\]

where

\[
 \Omega_z(U)
 =\mu(U)\sum_{A\mid U}z^{2\deg A-\deg U}.
\tag{1.2}
\]

The denominator in (1.1) is nonzero for \(|u|<1/2\) by (0.4), and the
numerator is a finite Laurent polynomial. Thus every fixed core preserves
the complete Witt continuation radius. The constant is allowed to depend
on \(U\). No uniform theorem for a growing core is inferred.

## 2. Uniform finite-deletion cost

Write

\[
 I_q(d)=\#\{P\ {\rm monic\ irreducible}:\deg P=d\}.
\tag{2.1}
\]

Since the roots of the degree-\(d\) irreducibles are distinct elements of
\(\mathbf F_{q^d}\),

\[
 dI_q(d)\le q^d.
\tag{2.2}
\]

For \(0<r<1/2\),

\[
 -\log(1-2r^d)\le C_r r^d.
\tag{2.3}
\]

Equations (2.2)--(2.3) give

\[
\begin{aligned}
 \log K_{q,y}(r)
 &=\sum_{d\le y}I_q(d)\bigl[-\log(1-2r^d)\bigr]\\
 &\ll_r\sum_{d\le y}{(qr)^d\over d}
 \ll_{q,r}{(qr)^y\over y},
\end{aligned}
\tag{2.4}
\]

proving (0.5). Combine this with the predecessor's uniform bound

\[
 \sup_{|z|=1}|F_q(u,z)|\le C_{q,r}
 \qquad(|u|=r)
\tag{2.5}
\]

and Cauchy's formula to obtain (0.6).

## 3. Why the subfrontier is exactly \(2-\eta\)

As \(r\downarrow q^{-1/2}\),

\[
 \log_q(qr)\longrightarrow\frac12.
\tag{3.1}
\]

Therefore for fixed \(\eta>0\), choose \(r\) sufficiently close to
\(q^{-1/2}\), while retaining \(r>q^{-1/2}\), that

\[
 (2-\eta)\log_q(qr)<1-\delta
\tag{3.2}
\]

for some \(\delta>0\). Equations (0.7) and (3.2) imply (0.9).

Meanwhile

\[
 q^{-n/2}r^{-n}=(r\sqrt q)^{-n}=e^{-c n}
\tag{3.3}
\]

with \(c=\log(r\sqrt q)>0\). The conditioning loss is
\(\exp(O(n^{1-\delta}))\), which is strictly smaller than the exponential
gain in (3.3). This proves (0.10).

The theorem is uniform in the Fourier phase because (0.4) is.

## 4. Matching barrier for the absolute conditioning method

The exact irreducible formula

\[
 I_q(d)={1\over d}\sum_{e\mid d}\mu(e)q^{d/e}
\tag{4.1}
\]

gives

\[
 I_q(d)={q^d\over d}+O_q(q^{d/2}).
\tag{4.2}
\]

At \(z=1\), every deleted local factor on a real radius \(r<1/2\) is
positive. Since

\[
 -\log(1-2r^d)\ge2r^d,
\tag{4.3}
\]

the single degree-\(y\) row and (4.2) imply

\[
 \log K_{q,y}(r)
 \ge2I_q(y)r^y
 \gg_{q,r}{(qr)^y\over y}
\tag{4.4}
\]

for all sufficiently large \(y\). This proves (0.11).

If \(q^{-1/2}<r<1/2\), set

\[
 a=qr>\sqrt q,
 \qquad
 Y=(2+\eta)\log_q n.
\]

The function \(a^t/t\) is increasing once \(t>1/\log a\). Hence, under
(0.12),

\[
 {(qr)^{y_n}\over y_n}
 \ge{(qr)^Y\over Y}
 \ge{n^{1+\eta/2}\over(2+\eta)\log_qn}
 =n^{1+\eta/2-o(1)}.
\tag{4.5}
\]

Thus the absolute condition number itself already costs at least
\(\exp(n^{1+\eta/2-o(1)})\), before the coefficient is estimated. This
proves the declared barrier and nothing stronger.

## 5. Relation to the integer rough frontier

The integer prefix-truncated preconditioner independently finds

\[
 \log y_X\le(2+o(1))\log\log X
\tag{5.1}
\]

as the exact subpower frontier for its positive squarefree/smooth
conditioning masses. Put \(X=q^n\). Then

\[
 \log\log X=\log n+O_q(1),
\]

while a function-field prime of degree \(y\) has norm \(q^y\). The
condition \(q^y\lesssim n^2\) is exactly

\[
 y\lesssim2\log_qn.
\tag{5.2}
\]

The matching exponents arise from the same critical half-weight:
small-prime deletion pays approximately the square root of the local norm.
The function-field theorem is stronger below the frontier because the
complete two-color Witt algebra supplies exponential signed cancellation.

No number-field estimate follows. The polynomial zeta identity turns every
primitive color word into the finite factor \(1-qv\); the integer Euler
product has no corresponding rational collapse.

## 6. Claim ledger

| statement | grade |
|---|---|
| rough quotient identity (0.3) | **PROVED EXACT** |
| no finite-deletion pole in \(|u|<1/2\) | **PROVED EXACT** |
| condition-number upper bound (0.5) | **PROVED** |
| coefficient estimate (0.6) | **PROVED** |
| exponential critical decay below \((2-\eta)\log_qn\) | **PROVED** |
| condition-number lower bound (0.11) | **PROVED** |
| exponent-\(2\) absolute-method barrier | **PROVED; NOT AN ACTUAL COEFFICIENT LOWER BOUND** |
| fixed squarefree core stability (1.1) | **PROVED EXACT** |
| growing core, arbitrary sieve, or maximal endpoint | **NOT INCLUDED** |
| sharp signed frontier at \(2\log_qn\) | **OPEN / NOT CLAIMED** |
| integer WAVEPRIMCAR | **NOT PROVED** |
| RH or GRH | **NOT PROVED** |

No external novelty claim is made without a dedicated literature
comparison.

## 7. Bounded replay

At \(q=5\), total degree at most eight, and rough cutoff \(y=2\), the
producer expands the retained and deleted Laurent Euler factors separately
and verifies that their truncated product equals the complete source. It
uses the exact rational critical radius \(r=9/20\), for which

\[
 5r^2={405\over400}>1,\qquad r<1/2,
\]

and computes the finite-deletion condition number exactly. No field
element, polynomial, irreducible, curve, point, floating-point value, or
zeta zero is enumerated.

~~~text
python -B research/l-families/atlas/function_field/function_field_witt_rough_sieve_frontier.py --check
python -B -O research/l-families/atlas/function_field/function_field_witt_rough_sieve_frontier.py --check
python -B -m unittest tests.test_function_field_witt_rough_sieve_frontier
python -B -O -m unittest tests.test_function_field_witt_rough_sieve_frontier
python -B -m ruff check research/l-families/atlas/function_field/function_field_witt_rough_sieve_frontier.py tests/test_function_field_witt_rough_sieve_frontier.py
python -B -m ruff format --check research/l-families/atlas/function_field/function_field_witt_rough_sieve_frontier.py tests/test_function_field_witt_rough_sieve_frontier.py
~~~
