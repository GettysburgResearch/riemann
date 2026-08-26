# The primitive rho tilt is an exact Dirichlet-convolution isomorphism

Status: **exact arithmetic identities; bounded inverse convolution operators on
the stated weighted Hilbert space; exact two-sided Mertens-seminorm transfer;
exact finite pair-block superposition with dilated tests; no uniform dilated
block estimate, PRIMCAR estimate, PRIMLS estimate, RH proof, or GRH proof**

Bounded exact replay:
[`ffps_primitive_rho_tilt_convolution_isomorphism.py`](ffps_primitive_rho_tilt_convolution_isomorphism.py).
Canonical summary:
[`ffps_primitive_rho_tilt_convolution_isomorphism.json`](ffps_primitive_rho_tilt_convolution_isomorphism.json).

Frozen predecessor: the integrated primitive-pair harmonic-incidence packet at
`05da4d1705d994dd02d650f321196f8464034ba8`. The replay pins its complete
quartet:

| predecessor file | Git blob |
|---|---|
| `FFPS_PRIMITIVE_PAIR_HARMONIC_INCIDENCE_CARLESON.md` | `722ca5bd8acef2efdb5591f29935b4f97102f957` |
| `ffps_primitive_pair_harmonic_incidence_carleson.py` | `7e780f0109264dbfaac59cae36db6fd72c3f34ee` |
| `ffps_primitive_pair_harmonic_incidence_carleson.json` | `f0a556f8f3ab2db04f7e434646ac4c70987ae50f` |
| `tests/test_ffps_primitive_pair_harmonic_incidence_carleson.py` | `abaded5c04b4cec8464618f2dfff74a486ab025b` |

## 0. Outcome

Work on the multiplicative monoid

\[
 \mathcal N_{67}=\{n\geq 1:(n,67)=1\}.
\tag{0.1}
\]

Equivalently, extend every arithmetic function below by zero on integers
divisible by `67` and convolve on all positive integers. The zero-extended
functions form the same convolution algebra, with identity `delta_1`. The
replay works natively on `N_67` and therefore rejects a multiple of `67` as a
domain error rather than silently extending it.

For `p != 67`, put

\[
 \rho_p={p\over p+1},\qquad
 \rho(n)=\prod_{p\mid n}\rho_p,
 \qquad m(n)=\mu(n),\qquad a(n)=\mu(n)\rho(n).
\tag{0.2}
\]

Define multiplicative functions `g,h` on `N_67` by

\[
 \begin{aligned}
 G_p(x)&={1-\rho_p x\over1-x}
 =1+(1-\rho_p)\sum_{k\geq1}x^k,
 &g(p^k)&={1\over p+1},\\
 H_p(x)&={1-x\over1-\rho_p x}
 =1-(1-\rho_p)\sum_{k\geq1}\rho_p^{k-1}x^k,
 &h(p^k)&=-(1-\rho_p)\rho_p^{k-1}
 \end{aligned}
\tag{0.3}
\]

for every `k >= 1`. Then the coefficientwise Dirichlet-convolution identities
are

\[
 \boxed{m*g=a,\qquad a*h=m,\qquad g*h=\delta_1.}
\tag{0.4}
\]

They induce mutually inverse bounded operators

\[
 T_gf=f*g,qquad T_hf=f*h
\tag{0.5}
\]

on

\[
 \ell^2_{-1}(\mathcal N_{67})
 =\left\{f:\sum_{n\in\mathcal N_{67}}{|f(n)|^2\over n}<\infty\right\}.
\tag{0.6}
\]

Writing

\[
 L_g(\theta)=\sum_{n\in\mathcal N_{67}}{|g(n)|\over n^\theta},
 \qquad
 L_h(\theta)=\sum_{n\in\mathcal N_{67}}{|h(n)|\over n^\theta},
\tag{0.7}
\]

both constants are finite for every `theta > 0`. In particular,

\[
 \boxed{
 \|T_gf\|_{2,-1}\leq L_g(1/2)\|f\|_{2,-1},\qquad
 \|T_hf\|_{2,-1}\leq L_h(1/2)\|f\|_{2,-1}.}
\tag{0.8}
\]

The same kernels give an exact two-sided transfer for the summatory seminorm

\[
 S_\theta(f)=\sup_{x\geq1}x^{-\theta}
 \left|\sum_{n\leq x\atop n\in\mathcal N_{67}}f(n)\right|:
\tag{0.9}
\]

\[
 \boxed{
 L_h(\theta)^{-1}S_\theta(m)
 \leq S_\theta(a)
 \leq L_g(\theta)S_\theta(m),\qquad \theta>0.}
\tag{0.10}
\]

Thus the rho-weighted, 67-free ordinary, and full ordinary Mertens exponents
coincide. In particular the family

\[
 S_{1/2+\varepsilon}(a)<\infty
 \quad\hbox{for every }\varepsilon>0
\tag{0.11}
\]

is equivalent to the standard Mertens formulation of RH. This is a transfer
of the classical equivalence, not a proof of any estimate in (0.11).

Finally, after half-weighting

\[
 c_\rho(n)={\mu(n)\rho(n)\over\sqrt n},\qquad
 c_0(n)={\mu(n)\over\sqrt n},\qquad
 \gamma(r)={g(r)\over\sqrt r},
\tag{0.12}
\]

equation (0.4) becomes

\[
 \boxed{c_\rho=c_0*\gamma.}
\tag{0.13}
\]

For every finitely supported pair test `F` on `N_67^2`, this gives the exact
superposition

\[
 \boxed{
 \mathcal B_\rho(F)
 =\sum_{r,s\in\mathcal N_{67}}\gamma(r)\gamma(s)
 \mathcal B_0(F_{r,s}),
 \qquad F_{r,s}(u,v)=F(ru,sv),}
\tag{0.14}
\]

where

\[
 \mathcal B_\rho(F)=\sum_{u,v}c_\rho(u)c_\rho(v)F(u,v),
 \qquad
 \mathcal B_0(F)=\sum_{u,v}c_0(u)c_0(v)F(u,v).
\tag{0.15}
\]

The outer absolute weight in (0.14) is `L_g(1/2)^2`. Therefore the rho tilt
itself is an invertible `ell^1` coordinate change. But `F_(r,s)` has altered
coprimality, height, ratio, and endpoint geometry. No estimate uniform over
those induced dilations is proved here.

## 1. Exact local and global convolution algebra

At one prime `p != 67`, the local series of `m` and `a` are

\[
 m_p(x)=1-x,\qquad a_p(x)=1-\rho_p x.
\tag{1.1}
\]

The definitions (0.3) give

\[
 m_p(x)G_p(x)=a_p(x),\qquad
 a_p(x)H_p(x)=m_p(x),\qquad
 G_p(x)H_p(x)=1.
\tag{1.2}
\]

Equating coefficients proves all three local identities. Multiplicativity
then proves (0.4). This use of Euler series is formal: for a fixed coefficient
`n`, only the finitely many primes and divisors of `n` occur, so no analytic
convergence premise is needed.

For clarity, the first two nontrivial inverse coefficients are

\[
 h(p)=-{1\over p+1},\qquad
 h(p^2)=-{p\over(p+1)^2}.
\tag{1.3}
\]

The replay checks exponents `0,...,5` at `p=2,3,5,7,11`, all 67-free
integers through `120`, and both orders of the exact rational truncated
operator matrices through `24`. The finite prefix matrix is only a bounded
coefficient replay on a divisor-closed set; it is not a claim that a sharp
primitive height annulus is invariant.

## 2. Absolute kernel sums

Multiplicativity and nonnegativity of `g` give, for every `theta > 0`,

\[
 \begin{aligned}
 L_g(\theta)
 &=\prod_{p\ne67}\left(1+u_g(p;\theta)\right),\\
 u_g(p;\theta)
 &=\sum_{k\geq1}{g(p^k)\over p^{k\theta}}
 ={1\over(p+1)(p^\theta-1)}.
 \end{aligned}
\tag{2.1}
\]

Similarly,

\[
 \begin{aligned}
 L_h(\theta)
 &=\prod_{p\ne67}\left(1+u_h(p;\theta)\right),\\
 u_h(p;\theta)
 &=\sum_{k\geq1}{|h(p^k)|\over p^{k\theta}}
 ={p^{-\theta}\over(p+1)(1-\rho_p p^{-\theta})}.
 \end{aligned}
\tag{2.2}
\]

For all sufficiently large `p`, one has `p^theta >= 2`, and hence

\[
 u_g(p;\theta)\leq 2p^{-1-\theta},\qquad
 u_h(p;\theta)\leq 2p^{-1-\theta}.
\tag{2.3}
\]

The sums of the right-hand sides over primes converge. Since
`log(1+u) <= u` for `u >= 0`, both products in (2.1)--(2.2) are finite.
The restriction `theta > 0` is essential: at `theta=0`, the `g` local sum
already contains infinitely many equal prime-power coefficients, while every
`h` local absolute tail equals `1`. Thus `L_g(0)=L_h(0)=infinity`.

At the Hilbert-space weight `theta=1/2`, the local tails are explicitly

\[
 u_g(p;1/2)={1\over(p+1)(\sqrt p-1)},
 \qquad
 u_h(p;1/2)={1\over\sqrt p\,(p+1-\sqrt p)}.
\tag{2.4}
\]

The elementary bounds

\[
 \sqrt p-1\geq{\sqrt p\over4},
 \qquad p+1-\sqrt p\geq{p\over2}
\tag{2.5}
\]

give

\[
 u_g(p;1/2)\leq4p^{-3/2},\qquad
 u_h(p;1/2)\leq2p^{-3/2}.
\tag{2.6}
\]

For `p >= 2`, the two inequalities in (2.5) reduce respectively to the
positive rational margins `9p-16 >= 0` and `p^2/4+1 > 0` after squaring.
Those are the convergence panels stored by the replay; no floating-point
approximation is used.

## 3. The weighted Hilbert-space isomorphism

Put `F(n)=f(n)/sqrt(n)` and `gamma(r)=g(r)/sqrt(r)`. Then

\[
 {(f*g)(n)\over\sqrt n}
 =\sum_{r\mid n}\gamma(r)F(n/r).
\tag{3.1}
\]

For fixed `r`, the sequence `n -> 1_(r|n) F(n/r)` has the same unweighted
`ell^2` norm as `F`: multiplication by `r` is a bijection from `N_67` onto
its multiples by `r`. Minkowski's inequality and (2.1) therefore give

\[
 \|f*g\|_{2,-1}
 \leq\sum_r{|g(r)|\over\sqrt r}\|f\|_{2,-1}
 =L_g(1/2)\|f\|_{2,-1}.
\tag{3.2}
\]

The same proof with `h` gives the second bound in (0.8). Every coefficient of
a Dirichlet convolution is a finite divisor sum. Consequently associativity
and `g*h=delta_1` hold pointwise on the Hilbert space, and

\[
 T_hT_g=T_gT_h=I.
\tag{3.3}
\]

This proves the bounded inverse isomorphism.

In particular, applying the `T_h` bound to `T_gf` gives the explicit
condition-number estimate

\[
 L_h(1/2)^{-1}\|f\|_{2,-1}
 \leq \|T_gf\|_{2,-1}
 \leq L_g(1/2)\|f\|_{2,-1}.
\]

Neither `m` nor `a` is itself a vector of (0.6). Indeed,

\[
 \sum_n{|m(n)|^2\over n}
 =\prod_{p\ne67}(1+p^{-1})=\infty,
\tag{3.4}
\]

while the local nonconstant term for `a` is

\[
 {|a(p)|^2\over p}={p\over(p+1)^2}\asymp{1\over p},
\tag{3.5}
\]

so its squared norm also diverges. Thus (0.8) does not, by itself, estimate
either Mertens sum or any primitive-pair block.

## 4. Two-sided Mertens-seminorm transfer

Let

\[
 M_0(x)=\sum_{n\leq x\atop n\in\mathcal N_{67}}m(n),
 \qquad
 M_\rho(x)=\sum_{n\leq x\atop n\in\mathcal N_{67}}a(n).
\tag{4.1}
\]

Summing (0.4) over `n <= x` and regrouping the finite divisor pairs gives

\[
 M_\rho(x)=\sum_{r\leq x\atop r\in\mathcal N_{67}}g(r)M_0(x/r),
 \qquad
 M_0(x)=\sum_{r\leq x\atop r\in\mathcal N_{67}}h(r)M_\rho(x/r),
\tag{4.2}
\]

where a summatory function at a real argument means the sum through its
integer part. If `S_theta(m)` is finite, the first equality yields

\[
 |M_\rho(x)|
 \leq S_\theta(m)x^\theta
 \sum_{r\leq x}{|g(r)|\over r^\theta}
 \leq L_g(\theta)S_\theta(m)x^\theta.
\tag{4.3}
\]

The second equality gives the reverse bound, proving (0.10). Equivalently,

\[
 S_\theta(a)<\infty\quad\Longleftrightarrow\quad S_\theta(m)<\infty
 \qquad(\theta>0).
\tag{4.4}
\]

If

\[
 \beta(f)=\inf\{\theta>0:S_\theta(f)<\infty\},
\tag{4.5}
\]

then `beta(a)=beta(m)`.

To compare the 67-free and full ordinary sums, let

\[
 M(x)=\sum_{n\leq x}\mu(n).
\tag{4.6}
\]

Removing or restoring the one Euler factor gives the exact finite identities

\[
 M(x)=M_0(x)-M_0(x/67),
 \qquad
 M_0(x)=\sum_{j\geq0}M(x/67^j),
\tag{4.7}
\]

where the second sum is finite. Hence, for every `theta > 0`,

\[
 S_\theta(\mu)
 \leq(1+67^{-\theta})S_\theta(m),
 \qquad
 S_\theta(m)
 \leq{S_\theta(\mu)\over1-67^{-\theta}}.
\tag{4.8}
\]

Combining (0.10) and (4.8) proves equality of all three exponents. The
classical criterion

\[
 \mathrm{RH}\quad\Longleftrightarrow\quad
 M(x)=O_\varepsilon(x^{1/2+\varepsilon})
 \quad\hbox{for every }\varepsilon>0
\tag{4.9}
\]

therefore transfers exactly to (0.11). Equation (4.9) is an imported standard
theorem. The replay enumerates no zeta zero and establishes no bound in
(4.9).

## 5. Exact half-weighted pair-block superposition

Dividing `a=m*g` coefficientwise by `sqrt(n)` gives

\[
 c_\rho(n)
 =\sum_{rm=n}{\mu(m)\over\sqrt m}{g(r)\over\sqrt r}
 =(c_0*\gamma)(n),
\tag{5.1}
\]

which proves (0.13). Expanding both factors in (0.15) and regrouping finite
sums proves (0.14). Absolute outer weight is controlled by

\[
 \sum_{r,s}|\gamma(r)\gamma(s)|=L_g(1/2)^2<\infty.
\tag{5.2}
\]

For any finite family of tests `F_j` and nonnegative weights `w_j`, (0.14)
also gives the precise vector transfer

\[
 \left\|\bigl(\mathcal B_\rho(F_j)\bigr)_j\right\|_{\ell^2(w)}
 \leq
 \sum_{r,s}|\gamma(r)\gamma(s)|
 \left\|\bigl(\mathcal B_0(F_{j;r,s})\bigr)_j\right\|_{\ell^2(w)}.
\tag{5.3}
\]

This is Minkowski's inequality applied to (0.14). Therefore a scalar pair
bound uniform in `(r,s)` costs at most `L_g(1/2)^2`, while the corresponding
squared Carleson energy costs at most `L_g(1/2)^4`:

\[
 \begin{aligned}
 |\mathcal B_\rho(F)|
 &\leq L_g(1/2)^2\sup_{r,s}|\mathcal B_0(F_{r,s})|,\\
 \sum_jw_j|\mathcal B_\rho(F_j)|^2
 &\leq L_g(1/2)^4
 \sup_{r,s}\sum_jw_j|\mathcal B_0(F_{j;r,s})|^2.
 \end{aligned}
\tag{5.4}
\]

The inverse transfer has the corresponding `L_h(1/2)^2` scalar and
`L_h(1/2)^4` squared-energy costs. Indeed, the inverse identity is

\[
 c_0=c_\rho*\eta,
 \qquad \eta(r)={h(r)\over\sqrt r},
 \qquad \sum_r|\eta(r)|=L_h(1/2).
\tag{5.5}
\]

This applies directly to the predecessor's finite primitive block. For a
finite height set `I` and a 67-free sieve variable `d`, define

\[
 \begin{aligned}
 F_{\alpha,\gamma,I,d}(u,v)
 ={}&1_{\mu(u)^2=1}1_{\mu(v)^2=1}
 1_{(u,v)=1}1_{(uv,d)=1}
  1_{\max(67^\alpha u,67^\gamma v)\in I}\\
 &\times
 \mathcal R\!\left(\log{67^\alpha u\over67^\gamma v}\right).
 \end{aligned}
\tag{5.6}
\]

Taking `d=1` gives the rho-tilted zero mode, while general `d` retains the
finite primitive panel's sieve incidence. Equation (0.14) expresses either
case exactly as ordinary Möbius pair sums with

\[
 \begin{aligned}
 F_{\alpha,\gamma,I,d;r,s}(m,n)
 ={}&1_{\mu(rm)^2=1}1_{\mu(sn)^2=1}
 1_{(rm,sn)=1}1_{(rsmn,d)=1}
 1_{\max(67^\alpha rm,67^\gamma sn)\in I}\\
 &\times
 \mathcal R\!\left(
 \log{67^\alpha m\over67^\gamma n}+\log{r\over s}
 \right).
 \end{aligned}
\tag{5.7}
\]

Thus the identity does not discard the original structure; it moves that
structure into a family of dilated tests. In particular:

1. squarefreeness becomes a condition on `rm` and `sn`, not only on the
   ordinary Möbius variables `m,n`;
2. `(rm,sn)=1` contains cross-coprimality conditions involving all four
   variables, not merely `(m,n)=1`;
3. sieve incidence becomes `(rsmn,d)=1`;
4. the height boundary is anisotropically dilated by `(r,s)`;
5. the ratio kernel is translated by `log(r/s)`;
6. aligned dyadic endpoint blocks are not carried to one common aligned
   dyadic family.

An ordinary Möbius pair theorem uniform over all tests (5.7), with enough
summability to absorb (5.2), would transfer to the rho panel. No such theorem
is supplied. The obstruction after the exact algebra is uniform control of
the induced dilations, coprimality conditions, and annular boundaries—not an
uncontrolled rho coefficient.

## 6. Firewall against a PRIMCAR or RH misreading

The bounded isomorphism (0.5) acts on full one-variable sequences on
`N_67`. It does **not** preserve the sharp finite structures in the
primitive-pair packet:

- a sequence supported in one height range acquires contributions on
  arbitrarily large multiples under convolution by `g` or `h`;
- squarefreeness and pair coprimality change to the cross-conditions in (5.7);
- sieve incidence changes to `(rsmn,d)=1`;
- the ratio kernel is shifted separately for every `(r,s)`;
- the physical height shell and its dyadic endpoints depend on `(r,s)`;
- the fixed-height harmonic limit from the predecessor supplies no uniform
  estimate over this new dilation family.

In particular, the undilated PRIMCAR test class is not closed under the
dilations in (5.7). The exact forward `L_g(1/2)^4` energy cost, or inverse
`L_h(1/2)^4` cost in the other direction, becomes usable only after a uniform
theorem for that enlarged test class is supplied.
Moreover, this packet does not bound the predecessor's nonzero Boolean modes
or their collective incidence spectrum. Its fixed-height `D -> infinity`
limit still has no error uniform in the growing primorial `Q_H`, and so gives
no finite-`D`, height-uniform substitute for such a theorem.

Consequently, neither the Hilbert-space Young bound nor the exact
superposition proves the predecessor's open estimate

\[
 \mathrm{PRIMCAR}:\qquad
 \sum_{I\in\mathscr D_H}\mathcal E_D(I)
 \ll_\varepsilon(2DH)^\varepsilon.
\tag{6.1}
\]

No PRIMCAR, PRIMLS, RH, or GRH estimate is proved. The RH-equivalent statement
(0.11) is named only to calibrate the exact summatory transfer.

## 7. Proof and scope ledger

| statement | grade |
|---|---|
| local formulas (0.3) and convolution identities (0.4) | **PROVED EXACT** |
| convergence of `L_g(theta),L_h(theta)` for every `theta>0` | **PROVED** |
| bounded inverse operators on `ell^2(N_67,n^-1)` | **PROVED** |
| two-sided summatory-seminorm comparison (0.10) | **PROVED EXACT** |
| equality of rho-weighted, 67-free, and full Mertens exponents | **PROVED EXACT** |
| equivalence of the `1/2+epsilon` family with RH | **IMPORTED STANDARD EQUIVALENCE; NO ESTIMATE PROVED** |
| finite pair-test superposition (0.14), including primitive tests | **PROVED EXACT** |
| uniform control over induced tests (5.7) | **OPEN / NOT PROVED** |
| preservation of sharp height, coprimality, ratio, or dyadic geometry | **FALSE / EXPLICITLY NOT CLAIMED** |
| PRIMCAR, PRIMLS, RH, or GRH | **NOT PROVED** |

No external novelty claim is made.

## 8. Bounded replay

```text
python -B research/l-families/atlas/function_field/ffps_primitive_rho_tilt_convolution_isomorphism.py --check
python -B -O research/l-families/atlas/function_field/ffps_primitive_rho_tilt_convolution_isomorphism.py --check
python -B -m unittest tests.test_ffps_primitive_rho_tilt_convolution_isomorphism
python -B -O -m unittest tests.test_ffps_primitive_rho_tilt_convolution_isomorphism
```

The replay uses exact `Fraction` arithmetic. It pins the predecessor quartet;
checks the local and global convolution identities; checks exact rational
finite operator inverses; checks both summatory identities and the exceptional
Euler-factor identities through the stated caps; clears the common square-root
weight and checks representative pair coefficients; records exact rational
margins for the `theta=1/2` convergence proof; and enforces the scope firewall.
It enumerates no zeta zero, finite-field family, curve, conductor family, or
`L`-function.
