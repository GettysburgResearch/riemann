# The primitive rho tilt is an exact Dirichlet-convolution isomorphism

Status: **exact arithmetic identities; bounded inverse convolution operators on
the stated weighted Hilbert space; exact two-sided Mertens-seminorm transfer;
exact finite pair-block superposition and primitive-support Boolean compression;
no weighted dilated-block estimate, PRIMCAR estimate, PRIMLS estimate, RH
proof, or GRH proof**

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
itself is an invertible `ell^1` coordinate change. On the actual primitive
support, where `F(u,v)` vanishes unless `u,v` are squarefree and coprime, the
outer variables are automatically squarefree and coprime. Forward and inverse
absolute pair mass then collapse to the same smaller Boolean product

\[
 \boxed{
 \mathcal K_{67}
 =\prod_{p\ne67}\left(1+{2\over(p+1)\sqrt p}\right)<\infty.}
\tag{0.16}
\]

Thus a uniform scalar primitive-pair bound costs `K_67`, and its squared
vector energy costs `K_67^2`, in either direction. Uniformity is not the
weakest sufficient input: the exact transfer only asks for the corresponding
outer-weighted sum of vector norms. In every formulation, however,
`F_(r,s)` has altered coprimality, height, ratio, and endpoint geometry. No
such weighted dilated-family estimate is proved here.

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

This is Minkowski's inequality applied to (0.14). More explicitly, set

\[
 E_0(r,s)=\sum_jw_j|\mathcal B_0(F_{j;r,s})|^2,
 \qquad
 E_\rho=\sum_jw_j|\mathcal B_\rho(F_j)|^2.
\]

Then

\[
 \boxed{
 E_\rho^{1/2}
 \leq\sum_{r,s}|\gamma(r)\gamma(s)|E_0(r,s)^{1/2}.}
\tag{5.3a}
\]

For a target `T`, the direct noncancellative sufficient input exposed by this
identity is

\[
 \sum_{r,s}|\gamma(r)\gamma(s)|E_0(r,s)^{1/2}
 \ll \mathcal T^{1/2}.
\tag{5.3b}
\]

This is weaker than a pointwise theorem uniform in `(r,s)`. The latter is a
convenient sufficient corollary and costs at most `L_g(1/2)^2` for a scalar
pair bound or `L_g(1/2)^4` for the corresponding squared Carleson energy:

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

### 5.1 Boolean compression on primitive support

The generic constants in (5.2)--(5.4) include prime powers and allow a prime
to divide both `r` and `s`. Neither can survive in the actual primitive test.
Indeed, a nonzero term of (5.7) has `rm` and `sn` squarefree and coprime.
Hence `r,s,m,n` are individually squarefree and their prime supports are
pairwise disjoint. In particular, `r` and `s` are squarefree and `(r,s)=1`.

Put

\[
 \kappa(r)={\mu(r)^2g(r)\over\sqrt r}.
\tag{5.8}
\]

For every test supported on squarefree coprime pairs, (0.14) can therefore be
restricted exactly to

\[
 \mathcal B_\rho(F)
 =\sum_{\substack{r,s\in\mathcal N_{67}\\
                   \mu(r)^2=\mu(s)^2=1\\(r,s)=1}}
 \kappa(r)\kappa(s)\mathcal B_0(F_{r,s}).
\tag{5.9}
\]

At each prime there are only three outer states: absent, in `r`, or in `s`.
Consequently the exact forward absolute mass is

\[
 \sum_{\substack{r,s\in\mathcal N_{67}\\
                  \mu(r)^2=\mu(s)^2=1\\(r,s)=1}}
 |\kappa(r)\kappa(s)|
 =\prod_{p\ne67}\left(1+{2\over(p+1)\sqrt p}\right)
 =\mathcal K_{67}.
\tag{5.10}
\]

The product converges because its nonconstant local term is at most
`2 p^(-3/2)`. For squarefree `r`, one also has `|h(r)|=g(r)`, since
`|h(p)|=g(p)=1/(p+1)`. Thus the inverse primitive-support superposition has
the **same** absolute mass `K_67`; the generic asymmetry between `L_g` and
`L_h` disappears on this Boolean quotient. Replacing the weights in (5.3a)
by the restricted weights in (5.9), a uniform primitive scalar estimate costs
`K_67` and a uniform squared vector estimate costs `K_67^2`, in both
directions. The weaker weighted vector gate remains the direct sufficient
condition.

### 5.2 The deformed tests are the same generalized primitive panel

The Boolean support permits a stronger reduction than the six raw conditions
in (5.7) suggest. For a squarefree `d` in `N_67`, define

\[
 \begin{aligned}
 \mathcal P^\rho_{\alpha,\gamma}(d;I)
 &=\mathcal B_\rho(F_{\alpha,\gamma,I,d}),\\
 \mathcal P^0_{A,B}(q;I)
 &=\sum_{\substack{m,n\ \mathrm{squarefree},\ 67\nmid mn\\
                    (m,n)=1,\ (mn,q)=1\\
                    \max(Am,Bn)\in I}}
 {\mu(m)\mu(n)\over\sqrt{mn}}
 \mathcal R\!\left(\log{Am\over Bn}\right).
 \end{aligned}
\tag{5.11}
\]

The first line introduces an auxiliary rho-weighted panel with a sieve
parameter. The predecessor's actual harmonic zero mode is exactly its `d=1`
specialization; the zero mode itself is not averaged over `d`.

For squarefree 67-free `m,n`, the support conditions satisfy the exact
equivalence

\[
 \begin{aligned}
 &\mu(rm)^2=\mu(sn)^2=1,\quad
 (rm,sn)=1,\quad(rsmn,d)=1\\
 &\quad\Longleftrightarrow\\
 &r,s\ \mathrm{squarefree},\quad(r,s)=1,\quad(rs,d)=1,\\
 &\hspace{35mm}(m,n)=1,\quad(mn,drs)=1.
 \end{aligned}
\tag{5.12}
\]

The forward primitive superposition therefore has the sharper exact form

\[
 \boxed{
 \mathcal P^\rho_{\alpha,\gamma}(d;I)
 =\sum_{\substack{r,s\in\mathcal N_{67}\ \mathrm{squarefree}\\
                   (r,s)=1,\ (rs,d)=1}}
 \kappa(r)\kappa(s)\,
 \mathcal P^0_{67^\alpha r,\,67^\gamma s}(drs;I).}
\tag{5.13}
\]

For bounded `I`, the height condition makes the outer sum finite. Thus
squarefreeness, cross-coprimality, the sieve predicate, and the ratio kernel
do **not** become unrelated obstructions. They retain exactly the ordinary
primitive-panel form after

\[
 (A,B,q)=(67^\alpha r,67^\gamma s,drs).
\]

The actual enlargement is a coupled family of two height scales and sieve
moduli. A ratio translation is simply `log(A/B)` in this notation, and an
annulus remains a difference of two upper max-height cutoffs.

### 5.3 Colored-cube norm and hereditary constraints

At one prime put

\[
 t_p={1\over(p+1)\sqrt p},\qquad
 T_p=
 \begin{pmatrix}1&0&0\\t_p&1&0\\t_p&0&1\end{pmatrix},\qquad
 T_p^{-1}=
 \begin{pmatrix}1&0&0\\-t_p&1&0\\-t_p&0&1\end{pmatrix}.
\tag{5.14}
\]

The three states are absence, membership in the left outer variable, and
membership in the right outer variable. Tensoring (5.14) over a finite prime
set gives the Boolean forward and inverse transforms. On the standard `ell^2`
space of colored configurations, their common exact finite-prime norm is the
corresponding partial product in

\[
 \boxed{
 \|T\|=\|T^{-1}\|
 =\prod_{p\ne67}
 {\sqrt{4+2t_p^2}+\sqrt2\,t_p\over2}<\infty.}
\tag{5.15}
\]

Indeed, the antisymmetric colored line has singular value one, while the
remaining two-dimensional block is a shear of size `sqrt(2)t_p`. Formula
(5.15) is its larger singular value. Since `t_p=O(p^(-3/2))`, the finite-prime
operators converge in operator norm and their norm products converge to the
displayed infinite product. This is a colored-configuration norm, not a
PRIMCAR estimate.

There is also an exact support criterion. Order colored configurations by
deleting colored primes. Since `T_(y,x)` and `T^(-1)_(y,x)` are nonzero
exactly when `x<=y`, a coordinate projection `P_A` satisfies

\[
 \boxed{
 P_{\mathcal A}T=P_{\mathcal A}TP_{\mathcal A}
 \quad\Longleftrightarrow\quad
 \mathcal A\text{ is downward closed},}
\tag{5.16}
\]

and the same is true for `T^(-1)`. Sieve avoidance and upper max-height
cutoffs are hereditary; an annulus is a difference of two hereditary cutoffs.
A fixed ratio band is generally not hereditary. Full commutation requires
both downward and upward closure and hence, on a connected colored cube, only
the two projections `P=0` and `P=I`. This explains exactly which sharp
restrictions survive the transform without leakage.

### 5.4 The harmonic sieve norm is critical but costs only logarithms

For squarefree `R` in `N_67`, define on squarefree 67-free sieve sequences

\[
 (D_RA)(d)=1_{(d,R)=1}A(Rd),\qquad
 \|A\|_w^2=\sum_d{|A(d)|^2\over d^w}.
\tag{5.17}
\]

The substitution `q=Rd` gives the sharp operator norm

\[
 \boxed{\|D_R\|=R^{w/2}.}
\tag{5.18}
\]

More explicitly, for `R=rs` with `r,s` squarefree and coprime, the exact
truncated vector identity is

\[
 \begin{aligned}
 &\sum_{\substack{d\leq D\ \mathrm{squarefree}\\(d,67rs)=1}}
 {\left|\mathcal P^0_{A,B}(drs;I)\right|^2\over d^w}\\
 &\qquad=(rs)^w
 \sum_{\substack{q\leq Drs\ \mathrm{squarefree}\\
                  67\nmid q,\ rs\mid q}}
 {\left|\mathcal P^0_{A,B}(q;I)\right|^2\over q^w}.
 \end{aligned}
\tag{5.18a}
\]

Consequently, after accounting for the sieve dilation `q=drs` in (5.13),
the absolute Boolean vector transfer has Euler product

\[
 \prod_{p\ne67}
 \left(1+{2p^{(w-1)/2}\over p+1}\right).
\tag{5.19}
\]

Its nonconstant local term is asymptotic to `2 p^((w-3)/2)`. The prime sum
converges for `w<1`; at `w=1` it is `2/(p+1)` and the prime harmonic series
diverges, while `w>1` only increases every sufficiently large local term.
Thus (5.19) converges exactly for `w<1`. At the PRIMCAR harmonic weight there
is no height-independent absolute constant. This is a genuine critical
boundary, not a failure of the half-weighted identity.

Native height support repairs the apparent divergence at subpower cost. For
`I` inside a height block of size `H`, every surviving outer variable is
`O(H)`. At `w=1`,

\[
 \kappa(r)\sqrt r=g(r)\leq{1\over r}
 \qquad(r\text{ squarefree}),
\]

and therefore

\[
 \sum_{r,s\ll H}\kappa(r)\kappa(s)\sqrt{rs}
 \ll(1+\log H)^2.
\tag{5.20}
\]

Minkowski then taxes a generalized ordinary vector theorem by only
`O(log^2 H)` at norm level and `O(log^4 H)` in squared energy, both absorbable
in a subpower allowance. For the actual `d=1` zero mode, `q=rs` is a single
atom; a harmonic ordinary-panel estimate controls that atom with the same
`sqrt(rs)` factor. Thus the following is a clean **sufficient**, not necessary,
zero-mode route: prove the ordinary-Möbius primitive Carleson estimate for the
generalized panels in (5.11), uniformly (or with outer-weight-summable losses)
over

\[
 A=67^\alpha r,\qquad B=67^\gamma s,\qquad q=drs.
\tag{5.21}
\]

One precise full-`q`, differently normalized gate is

\[
 \boxed{
 \mathrm{GENPRIMCAR}:\qquad
 \sum_{I\in\mathscr D_H}
 \sum_{\substack{q\leq Q\ \mathrm{squarefree}\\67\nmid q}}
 {\left|\mathcal P^0_{A,B}(q;I)\right|^2\over q}
 \ll_\varepsilon(2QH)^\varepsilon,}
\tag{5.22}
\]

uniformly for `Q,H>=1` and integers `1<=A,B<=2H`. For the ranges arising in
(5.13), one has `r,s<=2H` and hence `Q=Drs<=4DH^2`. Combining (5.18a),
(5.20), and (5.22) gives only a polylogarithmic outer loss, absorbable after
renaming `epsilon`. At `d=1`, the same gate controls the single atom `q=rs`
by positivity of the `q^-1` energy and incurs the same `sqrt(rs)` factor.
Since `B_I=P^rho_(alpha,gamma)(1;I)`, weighted Minkowski and (5.20) give the
conditional implication

\[
 \boxed{
 \mathrm{GENPRIMCAR}
 \quad\Longrightarrow\quad
 \sum_{I\in\mathscr D_H}|B_I|^2
 \ll_\varepsilon(2H)^\varepsilon.}
\tag{5.23}
\]

The logarithmic factors have been absorbed by renaming `epsilon`.

No such generalized-scale cancellation theorem is supplied. The generic
weighted condition (5.3b) remains valid, while (5.13)--(5.20) show that the
actual primitive incidence and harmonic-norm tax are much more structured
than an arbitrary dilated-test family. They do not turn the scalar zero mode
into a native `d`-average or prove that this full-`q` sufficient route is
necessary.

### 5.5 Compatible triples and the exact gate hierarchy

The full uniformity in `GENPRIMCAR` is not intrinsic. For one of the three
independent channels, fix `alpha in {0,1,2}` and `gamma=0`. The map

\[
 (r,s,d)\longmapsto
 (A,B,q)=(67^\alpha r,s,drs)
\tag{5.24}
\]

is a bijection from squarefree 67-free pairwise-coprime triples onto the
triples satisfying

\[
 \begin{gathered}
 v_{67}(A)=\alpha,\qquad v_{67}(B)=v_{67}(q)=0,\\
 r=A/67^\alpha,\qquad s=B\text{ are squarefree and coprime},\\
 q\text{ is squarefree},\qquad rs\mid q.
 \end{gathered}
\tag{5.25}
\]

The inverse is uniquely `d=q/(rs)`. For fixed squarefree `q`, every prime of
`q` is colored `r`, `s`, or `d`, so there are exactly `3^omega(q)` compatible
triples per channel. The actual zero mode has `d=1`: every prime is colored
only `r` or `s`, giving exactly `2^omega(q)` saturated rays and

\[
 q=rs={AB\over67^\alpha}.
\tag{5.26}
\]

This suggests a gate strictly tailored to the image. Put

\[
 \mathcal E^\alpha_{r,s}(D,H)
 =\sum_{I\in\mathscr D_H}
  \sum_{\substack{d\leq D\ \mathrm{squarefree}\\(d,67rs)=1}}
 {\left|\mathcal P^0_{67^\alpha r,s}(drs;I)\right|^2\over d}.
\tag{5.27}
\]

The exact vector form of (5.13) is

\[
 \left(
  \sum_{I\in\mathscr D_H}
  \sum_{\substack{d\leq D\ \mathrm{squarefree}\\67\nmid d}}
  {|\mathcal P^\rho_{\alpha,0}(d;I)|^2\over d}
 \right)^{1/2}
 \leq
 \sum_{\substack{r,s\in\mathcal N_{67}\ \mathrm{squarefree}\\(r,s)=1}}
 \kappa(r)\kappa(s)\,
 \mathcal E^\alpha_{r,s}(D,H)^{1/2}.
\tag{5.28}
\]

The minimal weighted-`l^1` sufficient condition furnished by
Minkowski and (5.28) is

\[
 \mathrm{COLLPRIMCAR}:\qquad
 \sum_{\substack{r,s\in\mathcal N_{67}\ \mathrm{squarefree}\\(r,s)=1}}
 \kappa(r)\kappa(s)\,
 \mathcal E^\alpha_{r,s}(D,H)^{1/2}
 \ll_\varepsilon(2DH)^{\varepsilon/2}.
\]

It need not bound any one ray. A stronger gate tailored to each compatible
ray is

\[
 \boxed{
 \mathrm{RAYPRIMCAR}:\qquad
 \mathcal E^\alpha_{r,s}(D,H)
 \ll_\varepsilon(2DHrs)^\varepsilon}
\tag{5.29}
\]

uniformly over admissible `r,s`. Indeed, for `0<epsilon<1`, its outer norm
cost is the convergent product

\[
 \mathcal K_{67}(\varepsilon)
 =\prod_{p\ne67}
 \left(1+{2p^{\varepsilon/2}\over(p+1)\sqrt p}\right)<\infty.
\tag{5.30}
\]

After renaming `epsilon`, `RAYPRIMCAR` implies the auxiliary rho-sieved
Carleson bound and, at `D=1`, the dyadic scalar-zero-mode bound. If the right
side of (5.29) is uniform in `r,s` without the harmless `(rs)^epsilon` loss,
the sharp outer costs are `K_67` in vector norm and `K_67^2` in energy.

The full-q gate and compatible-ray gate are not the same normalization. By
(5.18a),

\[
 \mathcal E^\alpha_{r,s}(D,H)
 =rs\sum_{I\in\mathscr D_H}
 \sum_{\substack{q\leq Drs\ \mathrm{squarefree}\\
                  67\nmid q,\ rs\mid q}}
 {\left|\mathcal P^0_{67^\alpha r,s}(q;I)\right|^2\over q}.
\tag{5.31}
\]

Therefore `GENPRIMCAR` bounds a ray only with a sharp linear `rs` factor;
collectively, the Boolean half weights turn its square root into the critical
polylogarithmic tax of (5.20). With
`H_N=\sum_{1\leq n\leq N}n^{-1}` and `H_0=0`, put

\[
 \begin{aligned}
 \Lambda_\alpha(H)
 &=
 \sum_{\substack{r,s\in\mathcal N_{67}\ \mathrm{squarefree}\\
                  (r,s)=1,\ 67^\alpha r\leq2H,\ s\leq2H}}
 g(r)g(s)\\
 &\leq
 H_{\lfloor2H/67^\alpha\rfloor}H_{\lfloor2H\rfloor}
 \leq(1+\log(2H))^2.
 \end{aligned}
\]

Then

\[
 \left(
  \sum_{I\in\mathscr D_H}
  \sum_{\substack{d\leq D\ \mathrm{squarefree}\\67\nmid d}}
  {|\mathcal P^\rho_{\alpha,0}(d;I)|^2\over d}
 \right)^{1/2}
 \leq
 \Lambda_\alpha(H)
 \sup_{1\leq A,B\leq2H}
 \mathfrak G_{A,B}(4DH^2,H)^{1/2},
\]

where `\mathfrak G` denotes the left side of (5.22). Thus the same
`O(\log^2 H)` vector / `O(\log^4 H)` energy loss controls the
whole auxiliary rho-sieved panel, not only `d=1`. Conversely,
`RAYPRIMCAR` sees no `q` outside
the compatible multiple ray `rs|q`. Hence neither gate implies the other at
the stated subpower normalization by positivity or norm algebra alone. Under
the native height support, the exact implication diagram is

\[
 \begin{gathered}
 \mathrm{RAYPRIMCAR}
 \xrightarrow{\ \mathcal K_{67}(\varepsilon)\ }
 \mathrm{COLLPRIMCAR}
 \longrightarrow \text{auxiliary rho-sieved energy}
 \xrightarrow{\ D=1\ }\text{zero-mode bound},\\
 \mathrm{GENPRIMCAR}
 \xrightarrow{\ O(\log^2 H)\text{ in vector norm}\ }
 \mathrm{COLLPRIMCAR}
 \longrightarrow \text{auxiliary rho-sieved energy}
 \xrightarrow{\ D=1\ }\text{zero-mode bound}.
 \end{gathered}
\tag{5.32}
\]

The collective gate is weaker than either uniform gate and formally implies
neither. Both uniform gates are scientifically useful sufficient routes, but
proving all of `GENPRIMCAR` would control many panels which the rho zero mode
never visits. The replay's non-implication witnesses are deliberately
abstract positive-norm arrays. They certify what restriction, positivity, and
norm algebra cannot prove; they are not asserted to be values of the
correlated arithmetic panels `\mathcal P^0_{A,B}`. Concretely, a
single prime-`p` ray of norm `p+1` has ray energy
`(p+1)^2`, while its squared contribution to the collective norm is
`\kappa(p)^2(p+1)^2=1/p`. The replay also exhibits equality in the
factor-`rs` conversion and a full-`q` atom invisible to its
compatible ray.

### 5.6 Core colors can interfere before taking a norm

The equal-weight compression extends to every fixed squarefree sieve value
`d`, provided one groups by the squarefree core `u=rs` rather
than by the total modulus `q=du`. For `(u,d)=1`, define

\[
 V^\alpha_{d;r,u/r}(I)
 =\mathcal P^0_{67^\alpha r,u/r}(du;I),
 \qquad
 \mathcal C^\alpha_{d,u}(I)
 =\sum_{r\mid u}V^\alpha_{d;r,u/r}(I).
\tag{5.33}
\]

The parameter colors remain ordered: swapping `r` and `u/r`
changes the oriented scales and ratio test. For `alpha=0`, evenness
of the ratio kernel gives equal values on the swapped pair, but both ordered
colors remain in the sum. Since `r` and `u/r` are coprime
and `g` is multiplicative, every one of the
`2^{\omega(u)}` colors has the same outer weight

\[
 \kappa(r)\kappa(u/r)
 ={g(r)g(u/r)\over\sqrt u}
 ={g(u)\over\sqrt u}
 =:w(u).
\tag{5.34}
\]

Consequently every auxiliary rho slice has the exact coherent-core form

\[
 \boxed{
 \mathcal P^\rho_{\alpha,0}(d;I)
 =\sum_{\substack{u\in\mathcal N_{67}\ \mathrm{squarefree}\\(u,d)=1}}
 w(u)\mathcal C^\alpha_{d,u}(I).}
\tag{5.35}
\]

For bounded height blocks the core sum is finite. At `d=1`, put
`B^\rho_{\alpha,I}=\mathcal P^\rho_{\alpha,0}(1;I)`. Taking the
color sum before the norm gives the sharper chain

\[
 \left\|(B^\rho_{\alpha,I})_I\right\|_2
 \leq\sum_u w(u)\|\mathcal C^\alpha_{1,u}\|_2
 \leq\sum_u w(u)\sum_{r\mid u}\|V^\alpha_{1;r,u/r}\|_2.
\tag{5.36}
\]

The last member is the `d=1` raywise `COLLPRIMCAR` envelope.
The middle member retains coherent cancellation among the oriented
factorizations of one modulus and can be strictly smaller.

This exposes an image-faithful quadratic gate for the whole auxiliary panel.
Put

\[
 \begin{aligned}
 \mathfrak X^\alpha_{\rm color}(D,H)
 &=
 \sum_{\substack{d\leq D\ \mathrm{squarefree}\\67\nmid d}}
 {1\over d}
 \sum_{\substack{u\in\mathcal N_{67}\ \mathrm{squarefree}\\(u,d)=1}}
 w(u)\sum_{I\in\mathscr D_H}|\mathcal C^\alpha_{d,u}(I)|^2,\\
 \mathrm{AUXCOLORPRIMCAR}:\qquad
 \mathfrak X^\alpha_{\rm color}(D,H)
 &\ll_\varepsilon(2DH)^\varepsilon.
 \end{aligned}
\tag{5.37}
\]

Its `D=1` specialization is named `COLORPRIMCAR`. These are
weighted quadratic core energies, not uniform memberwise estimates. For
each fixed `d`, weighted Hilbert Cauchy and (5.35) give

\[
 \begin{aligned}
 \mathcal J_{67}(d)
 &=\sum_{\substack{u\in\mathcal N_{67}\ \mathrm{squarefree}\\(u,d)=1}}
 w(u)
 \leq
 \mathcal J_{67}
 :=\prod_{p\ne67}\left(1+{1\over(p+1)\sqrt p}\right)<\infty,\\
 \sum_{\substack{d\leq D\ \mathrm{squarefree}\\67\nmid d}}
 {1\over d}\sum_{I\in\mathscr D_H}
 |\mathcal P^\rho_{\alpha,0}(d;I)|^2
 &\leq
 \mathcal J_{67}\,
 \mathfrak X^\alpha_{\rm color}(D,H).
 \end{aligned}
\tag{5.38}
\]

Thus `AUXCOLORPRIMCAR` conditionally controls the auxiliary
rho-sieved energy and hence the `d=1` zero mode. The constant
`J_67(d)` is sharp on each positive-weight core space; the uniform
energy constant is `J_67` (operator norm `sqrt(J_67)`).

Moreover, `RAYPRIMCAR` implies `AUXCOLORPRIMCAR`. Cauchy--Schwarz
gives

\[
 \|\mathcal C^\alpha_{d,u}\|_2^2
 \leq 2^{\omega(u)}
 \sum_{r\mid u}\|V^\alpha_{d;r,u/r}\|_2^2,
\]

so after summing `d^{-1}`, applying the ray gate, and collecting the
`2^{\omega(u)}` ordered factorizations, the outer Euler product is

\[
 \prod_{p\ne67}
 \left(1+{4p^\eta\over(p+1)\sqrt p}\right)
\tag{5.39}
\]

and converges exactly for `0<eta<1/2`. Since
`RAYPRIMCAR` is asserted for every positive subpower exponent,
choosing `eta<min(epsilon,1/2)` proves the conditional implication.

For comparison, a uniform zero-mode bound
`\|\mathcal C^\alpha_{1,u}\|_2^2\ll_\eta(2Hu)^\eta` implies the
zero-mode estimate directly by Minkowski for `eta<1`, with vector
cost
`\prod_{p\ne67}(1+p^{\eta/2}/((p+1)\sqrt p))` and its square in
energy. It implies the named quadratic `COLORPRIMCAR` at the same
exponent only for `eta<1/2`; as an all-exponent subpower family it is
stronger after choosing and renaming a smaller exponent. It is not the gate
defined in (5.37).

At the positive-norm level, `AUXCOLORPRIMCAR` and
`COLLPRIMCAR` are formally incomparable. Fixed-core
cancellation can keep the color energy small while individual ray norms are
arbitrarily large. In the other direction, a single remote prime-`p`
ray of norm `p+1` contributes only `p^{-1/2}` to the
raywise weighted-`l^1` envelope, but contributes
`(p+1)/\sqrt p` to the weighted color energy. These are abstract
norm arrays, not arithmetic-panel counterexamples.

Nor does `GENPRIMCAR` imply `AUXCOLORPRIMCAR` by positivity.
Extracting one `q`-atom from the full-`q^{-1}` energy loses a
factor `q`. Formally, for every prime `p\ll H`, align the two
`q=p` color vectors with norm `sqrt(p)`. Each corresponding
`GENPRIMCAR` atom has normalized energy one, while its coherent
color contribution is `4\sqrt p/(p+1)`; summing over the primes grows
like `sqrt(H)/log H`. Conversely, `AUXCOLORPRIMCAR` is blind to
off-compatible moduli and to same-`q` color cancellation, so it
cannot recover `GENPRIMCAR` by positive-norm algebra. Again, these
are only synthetic non-implication witnesses.

This is a genuine extra cancellation opportunity, not a proved estimate.
The replay's cancellation witness is synthetic and is not asserted to arise
from the arithmetic panels. Equal weights persist at every fixed `d` and
core `u=rs`; what is special at `d=1` is that the core equals the
total generalized modulus. Thus `AUXCOLORPRIMCAR` addresses the whole
auxiliary rho-sieved energy, while its `COLORPRIMCAR` specialization
addresses only the zero mode. Neither controls any nonzero `PRIMCAR` mode.

### 5.7 The color energy is an exact support-overlap Gram

The coherent core has a direct primitive-pair realization. Let
`X_d` be the squarefree, 67-free coprime pairs `(a,b)` with
`(ab,d)=1`, and include the height and ratio factor in

\[
 \Phi^{\alpha}_{d,I}(a,b)
 ={\mu(a)\mu(b)\over\sqrt{ab}}
 \mathcal R\!\left(\log{67^\alpha a\over b}\right)
 \mathbf 1_{\max(67^\alpha a,b)\in I}.
\]

For every squarefree `(u,d)=1`, the substitution
`a=rm`, `b=(u/r)n` is a bijection from the color-panel terms
onto the pairs in `X_d` for which `u|ab`. It preserves the full
height and ratio data and gives

\[
 \boxed{
 \mathcal C^{\alpha}_{d,u}(I)
 =\mu(u)\sqrt u
 \sum_{\substack{(a,b)\in\mathscr X_d\\u\mid ab}}
 \Phi^{\alpha}_{d,I}(a,b).}
\tag{5.40}
\]

Indeed, `mn u=ab` and
`mu(m)mu(n)=mu(u)mu(a)mu(b)`. Summing (5.40) against
`w(u)=g(u)/sqrt(u)` also recovers the original rho weight because

\[
 \sum_{u\mid ab}\mu(u)g(u)
 =\prod_{p\mid ab}\left(1-{1\over p+1}\right)
 =\rho(ab)=\rho(a)\rho(b).
\tag{5.41}
\]

More importantly, expanding the quadratic color energy gives the exact Gram
identity

\[
 \boxed{
 \sum_u w(u)\sum_I|\mathcal C^{\alpha}_{d,u}(I)|^2
 =\sum_I\sum_{\substack{x=(a,b),\ y=(a',b')\in\mathscr X_d}}
 \Phi^{\alpha}_{d,I}(x)\overline{\Phi^{\alpha}_{d,I}(y)}
 \mathscr K(ab,a'b'),}
\tag{5.42}
\]

where, for integers prime to `67d`,

\[
 \mathscr K(N,M)
 =\sum_{u\mid(N,M)}g(u)\sqrt u
 =\prod_{p\mid(N,M)}\left(1+{\sqrt p\over p+1}\right).
\tag{5.43}
\]

This kernel is positive definite on every finite Boolean support cube. On
ordered primitive pairs it is only positive semidefinite, because different
orientations can have the same product `ab`. Its feature map is
`N -> (sqrt(g(u)sqrt(u)) 1_(u|N))_u`; at one prime its
absence/presence block is

\[
 \begin{pmatrix}1&1\\1&1+c_p\end{pmatrix},
 \qquad c_p={\sqrt p\over p+1},
 \qquad \det=c_p>0.
\]

Thus `AUXCOLORPRIMCAR` is not merely another black-box norm: it is a
specific multiplicative shared-support Gram for the signed primitive-pair
data; its cross terms are not termwise positive. The increasingly small local
determinant also warns that inverting
this Gram uniformly is costly. The identity supplies a possible spectral or
large-sieve attack on the color gate; it does not prove that gate or any RH
estimate.

### 5.8 Product shells, exact inversion, and the high-prime penalty

The Gram kernel depends on a primitive pair only through its squarefree
product. Define the oriented product-shell amplitude

\[
 \mathcal A^{\alpha}_{d,I}(N)
 =\sum_{\substack{ab=N\\(a,b)\in\mathscr X_d}}
 \Phi^{\alpha}_{d,I}(a,b).
\]

Then (5.40) is precisely the upper-divisor zeta transform

\[
 \boxed{
 {\mathcal C^{\alpha}_{d,u}(I)\over\mu(u)\sqrt u}
 =\sum_{u\mid N}\mathcal A^{\alpha}_{d,I}(N).}
\tag{5.44}
\]

At fixed height only finitely many shells occur, so Boolean Möbius inversion
recovers every product shell exactly:

\[
 \boxed{
 \mathcal A^{\alpha}_{d,I}(N)
 =\sum_{\substack{N\mid k, k\ \mathrm{squarefree}\\
                    67\nmid k, (k,d)=1}}\mu(k/N)
 {\mathcal C^{\alpha}_{d,k}(I)\over\mu(k)\sqrt k}.}
\tag{5.45}
\]

Here color coordinates outside the finite height support are extended by
zero. Thus, for each fixed `(alpha,d,I)`, the complete color family
loses the orientation data inside a fixed product `N`, but it loses no
product-shell amplitude. This is a useful division of labor:
`AUXCOLORPRIMCAR` sees the coherently oriented shell sum, whereas nonzero
`PRIMCAR` modes may still see the internal orientation directions.

The algebraic Boolean Möbius inversion is exact and has no high-prime
parameter. However, recovering shell contrasts from the weighted color
energy is poorly conditioned at high primes. With `c_p=sqrt(p)/(p+1)`,
the local overlap Gram block has Cholesky factor and eigenvalues

\[
 \begin{pmatrix}1&1\\1&1+c_p\end{pmatrix}
 =
 \begin{pmatrix}1&0\\1&\sqrt{c_p}\end{pmatrix}
 \begin{pmatrix}1&1\\0&\sqrt{c_p}\end{pmatrix},
 \qquad
 \lambda_\pm(p)
 ={2+c_p\pm\sqrt{4+c_p^2}\over2}.
\tag{5.46}
\]

Consequently the weighted Gram block's spectral condition number is
`lambda_+(p)/lambda_-(p) ~ 4 sqrt(p)`. Tensoring naïve inverse
bounds in this weighted Gram norm over many high primes is therefore
prohibitive. A viable proof should
exploit the forward signed shell transform or additional arithmetic
orthogonality, rather than whiten the full Boolean Gram prime by prime. This
is an exact conditioning diagnosis, not a no-go theorem for
`AUXCOLORPRIMCAR`.

### 5.9 Collapse to a one-variable Möbius divisor wavelet

The product-shell amplitude is more explicit than a generic orientation
sum. For squarefree 67-free `N=ab`, coprimality of `a,b` is automatic and

\[
 \mu(a)\mu(b)=\mu(N),
\]

independently of the orientation. Define the finite divisor wavelet

\[
 \mathcal W^\alpha_I(N)
 =\sum_{a\mid N}
 \mathcal R\!\left(\log{67^\alpha a^2\over N}\right)
 \mathbf 1_{\max(67^\alpha a,N/a)\in I}.
\tag{5.47}
\]

Then the auxiliary sieve coordinate enters a shell only by coprimality:

\[
 \boxed{
 \mathcal A^\alpha_{d,I}(N)
 =\mathbf 1_{(N,d)=1}{\mu(N)\over\sqrt N}
 \mathcal W^\alpha_I(N).}
\tag{5.48}
\]

Combining (5.40) and (5.48) gives the exact one-variable normal form

\[
 \boxed{
 \mathcal C^\alpha_{d,u}(I)
 =\mu(u)\sqrt u
 \sum_{\substack{N\in\mathcal N_{67}\ \mathrm{squarefree}\\
                   u\mid N,\ (N,d)=1}}
 {\mu(N)\over\sqrt N}\mathcal W^\alpha_I(N).}
\tag{5.49}
\]

Writing `N=uM` cancels both the core sign and square root:

\[
 \boxed{
 \mathcal C^\alpha_{d,u}(I)
 =\sum_{\substack{M\in\mathcal N_{67}\ \mathrm{squarefree}\\
                    (M,u)=1,\ (uM,d)=1}}
 {\mu(M)\over\sqrt M}\mathcal W^\alpha_I(uM).}
\tag{5.50}
\]

Put

\[
 \mathcal Y^\alpha_u(D,H)
 =\sum_{\substack{d\le D\ \mathrm{squarefree}\\(d,67u)=1}}{1\over d}
  \sum_{I\in\mathscr D_H}
  \left|
   \sum_{\substack{M\in\mathcal N_{67}\ \mathrm{squarefree}\\
                     (M,u)=1,\ (M,d)=1}}
   {\mu(M)\over\sqrt M}\mathcal W^\alpha_I(uM)
  \right|^2.
\]

Then the quadratic color gate is exactly the absolutely weighted
one-variable square-function assembly

\[
 \boxed{
 \mathfrak X^\alpha_{\rm color}(D,H)
 =\sum_{\substack{u\in\mathcal N_{67}\ \mathrm{squarefree}}}
 {g(u)\over\sqrt u}\mathcal Y^\alpha_u(D,H).}
\tag{5.51}
\]

This exposes a concrete sufficient theorem:

\[
 \boxed{
 \mathrm{WAVEPRIMCAR}:\qquad
 \mathcal Y^\alpha_u(D,H)
 \ll_\eta(2DHu)^\eta}
\tag{5.52}
\]

uniformly in squarefree 67-free `u` and the three actual `alpha`
channels. For `0<eta<1/2`, its outer
cost is
`prod_(p!=67)(1+p^eta/((p+1)sqrt(p)))<infinity`.
Since the assertion is an all-positive-exponent family, exponent renaming
proves `WAVEPRIMCAR -> AUXCOLORPRIMCAR`. This new gate is unproved;
it is scientifically useful because its inner object is one-variable rather
than an individual oriented primitive-pair ray. It is a stronger per-core
statement than the weighted aggregate `AUXCOLORPRIMCAR`, which does not
reverse-imply it by positive-norm algebra. One fixed-`eta` theorem would
not supply the asserted all-exponent family.

This is an exact reduction from a correlated primitive-pair panel to a
one-variable Möbius divisibility square function with an explicit divisor
wavelet. There is no Möbius cancellation *within* one product shell: any
orientation cancellation there comes from the signed ratio kernel and the
height block. Möbius cancellation occurs across distinct `N` in (5.49).
The wavelet is neither multiplicative nor positive; at `alpha>0` swapped
orientations differ, while at `alpha=0` both ordered terms are still counted.
Classical multiplicative large-sieve, Selberg-form, or summatory methods are
now plausible tools, but the varying wavelets, divisor multiplicity,
off-diagonal correlations, and harmonic `d` average still have to be
controlled. No such estimate is proved here.

### 5.10 The wavelet is a near-square, factor-64 shell

The imported autocorrelation is supported on ratio window `[1/16,16]`.
If one divisor term in (5.47) survives, then

\[
 {1\over16}\le {67^\alpha a^2\over N}\le16,
 \qquad
 {1\over4}\sqrt{N\over67^\alpha}
 \le a\le
 4\sqrt{N\over67^\alpha}.
\tag{5.53}
\]

Moreover, every `I` in `D_H` lies in the height grid `(H,2H]`.
Writing `X=67^alpha a` and `Y=N/a`, the same ratio window gives
`min(X,Y)>=max(X,Y)/16`. Hence

\[
 \boxed{
 {H^2\over16\,67^\alpha}<N\le {4H^2\over67^\alpha}.}
\tag{5.54}
\]

Thus, for fixed core `u`, the cofactor in (5.50) is confined to the
factor-64 multiplicative shell

\[
 {H^2\over16\,67^\alpha u}<M\le {4H^2\over67^\alpha u}.
\tag{5.55}
\]

The WAVE target is therefore not a full unstructured prefix sum: it is a
Möbius sum over one moving short multiplicative shell, with a near-square
divisor wavelet. At `alpha=0`, evenness of `R` and symmetry of the max
height make paired orientations `a` and `N/a` equal. For squarefree
`N>1` there is no fixed divisor, so the wavelet is exactly twice either
half-divisor sum. At positive `alpha` this pairing symmetry is absent.
These support facts sharpen the prospective bilinear/large-sieve attack but
do not provide cancellation.

## 6. Firewall against a PRIMCAR or RH misreading

The bounded isomorphism (0.5) acts on full one-variable sequences on
`N_67`. The primitive-support reduction preserves more structure than a
generic convolution, but it does **not** preserve the predecessor's original
two-ray parameter class:

- a sequence supported in one height range acquires contributions on
  arbitrarily large multiples under convolution by `g` or `h`;
- squarefreeness, pair coprimality, and sieve avoidance do reassemble exactly
  into the generalized primitive predicate (5.11);
- the two scale parameters become `(67^alpha r,67^gamma s)` and the sieve
  modulus becomes `drs`;
- upper height cutoffs are hereditary, but a ratio band generally is not;
- the physical height shell and its dyadic decomposition now range over these
  coupled scales;
- reindexing the harmonic `d^-1` norm through the full-`q`
  `GENPRIMCAR` gate introduces the `O(log^2 H)` vector tax in
  (5.20), while the direct `d^-1` `RAYPRIMCAR` gate has a
  convergent `\mathcal K_{67}(\varepsilon)` cost;
- the fixed-height harmonic limit from the predecessor supplies no uniform
  generalized-scale estimate.

In particular, the undilated PRIMCAR parameter class is not closed under
(5.13). The exact weighted vector inequality (5.3a) becomes usable only after
a bound of type (5.3b) for the enlarged class. At fixed test-index geometry, a
uniform theorem is a stronger special case with the `K_67^2` Boolean energy
cost. After reindexing the harmonic sieve variable from `d` to `drs`, the
relevant cost is instead the critical but subpower `O(log^4 H)` bound of
(5.20).
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
| primitive-support Boolean compression and symmetric cost (5.9)--(5.10) | **PROVED EXACT** |
| generalized primitive-panel identity and support equivalence (5.11)--(5.13) | **PROVED EXACT** |
| colored-cube norm and hereditary-projection law (5.14)--(5.16) | **PROVED EXACT** |
| critical harmonic threshold and polylog height tax (5.17)--(5.20) | **PROVED** |
| `GENPRIMCAR` implies the auxiliary rho-sieved and zero-mode bounds | **PROVED CONDITIONALLY** |
| compatible-triple bijection and `3^omega/2^omega` counts (5.24)--(5.26) | **PROVED EXACT** |
| `RAYPRIMCAR` implies the auxiliary rho-sieved and zero-mode bounds via (5.28)--(5.30) | **PROVED CONDITIONALLY** |
| exact `RAYPRIMCAR` / `GENPRIMCAR` / `COLLPRIMCAR` hierarchy (5.31)--(5.32) | **PROVED AT THE POSITIVE-NORM LEVEL** |
| fixed-`d`, fixed-core coherent coloring compression (5.33)--(5.36) | **PROVED EXACT** |
| `RAYPRIMCAR` implies `AUXCOLORPRIMCAR`, which controls the auxiliary rho-sieved energy and the zero mode (5.37)--(5.39) | **PROVED CONDITIONALLY** |
| direct primitive-pair color formula and support-overlap Gram (5.40)--(5.43) | **PROVED EXACT** |
| product-shell zeta transform, finite-height inverse, and local spectrum (5.44)--(5.46) | **PROVED EXACT** |
| one-variable Möbius divisor-wavelet normal form (5.47)--(5.51) | **PROVED EXACT** |
| `WAVEPRIMCAR` implies `AUXCOLORPRIMCAR` (5.52) | **PROVED CONDITIONALLY; ESTIMATE OPEN** |
| near-square divisor support and factor-64 product/cofactor shell (5.53)--(5.55) | **PROVED EXACT FROM IMPORTED KERNEL SUPPORT** |
| weighted vector gate (5.3b) over induced tests (5.7) | **OPEN / NOT PROVED** |
| uniform control over induced tests (5.7) | **STRONGER SUFFICIENT SPECIAL CASE; NOT PROVED** |
| `GENPRIMCAR`, `RAYPRIMCAR`, `COLLPRIMCAR`, `WAVEPRIMCAR`, `AUXCOLORPRIMCAR`, or `COLORPRIMCAR` estimate | **OPEN / NOT PROVED** |
| preservation of the original two-ray/dyadic parameter class | **FALSE / EXPLICITLY NOT CLAIMED** |
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
weight and checks representative pair coefficients; checks the squarefree-
coprime Boolean restriction, generalized support equivalence, colored-cube
heredity, local shear certificates, harmonic dilation identities, and equality
of forward/inverse local masses; exhausts the compatible image independently
on the three-prime bit cube, verifies the `3^{\omega(q)}` and
`2^{\omega(q)}` color counts, and checks exact synthetic witnesses for
the sharp `rs` conversion, off-ray blindness, remote-ray hiding, and
coherent fixed-`q` color cancellation after verifying the common
weight on `q=1,2,6,30`;
checks one end-to-end generalized panel with coefficient, height, ratio, and
sieve data after clearing one common square-root weight; records exact
rational margins for the `theta=1/2` convergence proof; and enforces
the scope firewall. It enumerates no zeta zero, finite-field family, curve,
conductor family, or `L`-function.
