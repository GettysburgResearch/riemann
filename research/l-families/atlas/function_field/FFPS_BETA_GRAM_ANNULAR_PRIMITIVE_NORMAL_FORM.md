# The first beta Gram has an exact annular primitive-pair normal form

Status: **exact full-gcd primitive-ray reindexing, positive radial
amplitudes, four signed physical annuli, continuous shell/moment
constraints, and an exact positivity no-go; the required annular
cancellation estimate, RH, and GRH remain open**

Bounded replay:
[ffps_beta_gram_annular_primitive_normal_form.py](ffps_beta_gram_annular_primitive_normal_form.py).
Canonical summary:
[ffps_beta_gram_annular_primitive_normal_form.json](ffps_beta_gram_annular_primitive_normal_form.json).

## 0. Provenance and outcome

The normalization and first-rung RH-equivalent energy are frozen at commit
3658d4c31cc866e15d48ab1fc9d8d119136da424. The four source blobs are

| frozen path | Git blob |
|---|---|
| FFPS_ZERO_FREE_BETA_ENERGY_LADDER.md | bd4cbb842e78c1dad5d380c8d20ff14c39bba15e |
| ffps_zero_free_beta_energy_ladder.py | df80000192292cc5fc1cd08013f152fb257054f9 |
| ffps_zero_free_beta_energy_ladder.json | 7e8889aa0dd1b01674e20158a52502cff0d8dffa |
| tests/test_ffps_zero_free_beta_energy_ladder.py | 983a1320f89087028f6724fe36aaca5ca1309b15 |

The immediate sign-geometry predecessor is frozen at commit
731398930c02cdc871259656dac2e2a4e6569e37. This replay binds its complete
quartet:

| exact predecessor path | Git blob |
|---|---|
| FFPS_BETA_GRAM_SIGN_GEOMETRY.md | bbdcb30dadb529cafad27abe6d6c9510d1c9b7d4 |
| ffps_beta_gram_sign_geometry.py | 750b77d8864c8f1a69c3e7144dc926b9b0477dd9 |
| ffps_beta_gram_sign_geometry.json | 00961f89cf3d74e364b89999a74b85e1f49018b8 |
| tests/test_ffps_beta_gram_sign_geometry.py | e486cca99bb4aaa4b61878e754c6b989d0f18d73 |

Let

\[
 \beta(n)=\mu(n)-\mathbf 1_{67\mid n}\mu(n/67)
\tag{0.1}
\]

Put

\[
 \Phi(x)=e^{x-1}(1-|x-1|)_+,
 \qquad
 M=\int_{\mathbb R}\Phi(x)\,dx=4\sinh^2(1/2),
\tag{0.2}
\]

and define

\[
 J_1(x)={\Phi'(x)\over M},
 \qquad
 \mathcal R(u)=\int_{\mathbb R}J_1(v)J_1(v+u)\,dv.
\tag{0.3}
\]

Writing \(q=|u|\) and \(C(q)=M^2\mathcal R(u)\), the exact physical
formula used throughout is

\[
 C(q)=
 \begin{cases}
 {1\over4}\left[
   \bigl(e^2+4-(e^2+2)q\bigr)e^{-q}
   -\bigl(2q+e^{-2}(q+1)\bigr)e^q
 \right],&0\le q\le1,\\[2mm]
 -{1\over2}\bigl(\sinh(2-q)+(2-q)\cosh(2-q)\bigr),&1\le q\le2,\\
 0,&q\ge2.
 \end{cases}
\tag{0.3a}
\]

For integer \(X\ge1\), the frozen energy is

\[
 \mathcal E_1(X)=
 \sum_{m,n\le X}{\beta(m)\beta(n)\over\sqrt{mn}}
 \mathcal R\!\left(\log{m\over n}\right).
\tag{0.4}
\]

The predecessor proves that there is a unique \(\xi\in(0,1)\) such that

\[
\begin{array}{c|c}
q=|u|&\mathcal R(u)\\ \hline
0\le q<\xi&>0\\
q=\xi&=0\\
\xi<q<2&<0\\
q\ge2&=0.
\end{array}
\tag{0.5}
\]

The result of this packet is the exact primitive-pair identity

\[
\boxed{
 \mathcal E_1(X)
 =D(X)+2\bigl(C_+(X)-C_-(X)-O_+(X)+O_-(X)\bigr),}
\tag{0.6}
\]

where every quantity on the right is nonnegative. The letters \(C,O\)
mean central and outer physical ratio annuli, while the subscripts record
the sign of the primitive beta phase. Thus physical kernel sign and
arithmetic source sign form four, not two, channels.

Put

\[
 P=C_++O_-,
 \qquad
 N=C_-+O_+.
\tag{0.7}
\]

Then

\[
 \boxed{\mathcal E_1(X)=D(X)+2(P(X)-N(X)).}
\tag{0.8}
\]

The frozen Fourier weight is positive almost everywhere, so the Gram form
on distinct translates is strictly positive definite. Since
\(\beta(1)=1\), the prefix vector is nonzero for every \(X\ge1\). Thus the
direct scalar consequence of assembled Gram positivity is the strict bound

\[
 \boxed{N(X)<P(X)+{D(X)\over2}.}
\tag{0.9}
\]

The open cancellation statement is exact and RH-equivalent:

\[
 \boxed{
 \mathrm{RH}
 \Longleftrightarrow
 |P(X)-N(X)|=X^{o(1)}.}
\tag{0.10}
\]

Equation (0.10) is a coordinate theorem, not an estimate proved here.

## 1. Primitive rays and the exceptional radial factor

Every ordered source pair has the unique full-gcd representation

\[
 m=gr,
 \qquad n=gs,
 \qquad (r,s)=1.
\tag{1.1}
\]

Both the physical ratio and its autocorrelation are constant on this ray:

\[
 \log{m\over n}=\log{r\over s}.
\tag{1.2}
\]

Define the finite radial coefficient

\[
 A_{r,s}(Y)
 =\sum_{g\le Y}{\beta(gr)\beta(gs)\over g}.
\tag{1.3}
\]

Substitution of (1.1) into (0.4) gives the first normal form

\[
\boxed{
 \mathcal E_1(X)=
 \sum_{(r,s)=1}
 {\mathcal R(\log(r/s))\over\sqrt{rs}}
 A_{r,s}\!\left(\left\lfloor{X\over\max(r,s)}\right\rfloor\right).}
\tag{1.4}
\]

This is a finite identity. No density approximation or asymptotic common
factor is used.

The beta source is multiplicative because, initially for \(\Re w>1\),

\[
 \sum_{n\ge1}{\beta(n)\over n^w}
 ={1-67^{-w}\over\zeta(w)}
 =(1-67^{-w})^2\prod_{p\ne67}(1-p^{-w}).
\tag{1.5a}
\]

Away from \(67\), its local coefficients are \((1,-1,0,\ldots)\), while
at \(67\) they are

\[
 (b_0,b_1,b_2,b_3,\ldots)=(1,-2,1,0,\ldots).
\tag{1.5}
\]

Suppose \((r,s)\) is active, meaning \(\beta(r)\beta(s)\ne0\), and put

\[
 \alpha=v_{67}(rs)\in\{0,1,2\}.
\tag{1.6}
\]

Because \(r,s\) are coprime, at most one contains \(67\). Write
\(g=67^e h\), with \(67\nmid h\). A nonzero product
\(\beta(gr)\beta(gs)\) requires

\[
 \mu(h)^2=1,
 \qquad
 (h,67rs)=1.
\tag{1.7}
\]

The exceptional local product divided by its primitive value is

\[
 q_{\alpha,e}
 ={b_{e+\alpha}b_e\over b_\alpha}.
\tag{1.8}
\]

Its three possible nonzero rows are

\[
\boxed{
 (q_{0,e})=(1,4,1),
 \qquad
 (q_{1,e})=(1,1),
 \qquad
 (q_{2,e})=(1).}
\tag{1.9}
\]

Every omitted later entry is zero.

For real \(Y\ge0\), set

\[
 S_{r,s}(Y)
 =\sum_{\substack{h\le Y,\ \mu(h)^2=1\\ (h,67rs)=1}}{1\over h}.
\tag{1.10}
\]

Then (1.3) has the exact closed form

\[
\boxed{
A_{r,s}(Y)=\beta(r)\beta(s)Q_\alpha(Y),}
\tag{1.11}
\]

where

\[
\begin{aligned}
 Q_0(Y)&=S_{r,s}(Y)+{4\over67}S_{r,s}(Y/67)
                 +{1\over67^2}S_{r,s}(Y/67^2),\\
 Q_1(Y)&=S_{r,s}(Y)+{1\over67}S_{r,s}(Y/67),\\
 Q_2(Y)&=S_{r,s}(Y).
\end{aligned}
\tag{1.12}
\]

If \(Y\ge1\), the \(h=1\) term shows \(Q_\alpha(Y)>0\). Therefore

\[
 \boxed{
 \operatorname{sgn}A_{r,s}(Y)
 =\operatorname{sgn}(\beta(r)\beta(s))}
 \qquad(Y\ge1).
\tag{1.13}
\]

This fixed-ray sign is the key simplification: the common-factor average
changes magnitude, including all exceptional \(67\)-adic states, but
never changes the primitive beta phase.

The only primitive diagonal ray is \((r,s)=(1,1)\). Hence

\[
\begin{aligned}
 D(X)
 &=\mathcal R(0)A_{1,1}(X)\\
 &=\mathcal R(0)\sum_{g\le X}{\beta(g)^2\over g}>0.
\end{aligned}
\tag{1.14}
\]

In particular, \(|\beta(g)|\le2\) gives

\[
 D(X)\le4\mathcal R(0)(1+\log X)=X^{o(1)}.
\tag{1.15}
\]

## 2. The four physical-arithmetic channels

Orient every active off-diagonal primitive pair by \(r<s\), and put

\[
 \rho={s\over r}>1,
 \qquad
 \varepsilon_{r,s}=\operatorname{sgn}(\beta(r)\beta(s)).
\tag{2.1}
\]

For an active ray with \(s\le X\), define its positive magnitude

\[
 W_X(r,s)
 ={|\beta(r)\beta(s)|Q_\alpha(X/s)\over\sqrt{rs}}
 \left|\mathcal R\!\left(\log{s\over r}\right)\right|.
\tag{2.2}
\]

The floor convention in (1.4) is understood inside \(Q_\alpha\). Nodal
and support-boundary rays have \(W_X=0\).

The finite central and outer ray sets are

\[
\begin{aligned}
 \mathcal C_X&=\{(r,s):r<s\le X,\ (r,s)=1,\quad
   \beta(r)\beta(s)\ne0,\ 1<s/r<e^\xi\},\\
 \mathcal O_X&=\{(r,s):r<s\le X,\ (r,s)=1,\quad
   \beta(r)\beta(s)\ne0,\ e^\xi<s/r<e^2\}.
\end{aligned}
\tag{2.3}
\]

Split each by \(\varepsilon_{r,s}\):

\[
\begin{aligned}
 C_\pm(X)&=\sum_{(r,s)\in\mathcal C_X,\ \varepsilon_{r,s}=\pm1}W_X(r,s),\\
 O_\pm(X)&=\sum_{(r,s)\in\mathcal O_X,\ \varepsilon_{r,s}=\pm1}W_X(r,s).
\end{aligned}
\tag{2.4}
\]

Evenness of \(\mathcal R\), the ray sign (1.13), and the physical sign
(0.5) now prove (0.6):

\[
 \mathcal E_1
 =D+2C_+-2C_--2O_++2O_-.
\tag{2.5}
\]

The physically negative outer annulus therefore contains both negative
and positive beta contributions. Likewise, the physically positive
central tube contains both signs.

There is an equivalent signed-measure form. Define the finite atomic
measure

\[
 d\Lambda_X(u)
 =\sum_{\substack{r<s,\ (r,s)=1,\ \beta(r)\beta(s)\ne0\\s\le X}}
 {\beta(r)\beta(s)Q_\alpha(X/s)\over\sqrt{rs}}
 \delta_{\log(s/r)}(du).
\tag{2.6}
\]

Then

\[
 \boxed{
 {\mathcal E_1(X)-D(X)\over2}
 =\int_0^2\mathcal R(u)\,d\Lambda_X(u).}
\tag{2.7}
\]

The measure is atomic, arithmetically weighted, and signed. This is the
precise obstruction to importing a continuous shell cancellation.

## 3. What unconditional positivity actually gives

The full energy is the squared \(L^2\) norm of a nonzero finite translate
combination, so strict Gram positivity gives \(\mathcal E_1(X)>0\).
Combining this with (0.8) proves (0.9). This is a comparison of the two
assembled positive masses \(P,N\); it does not say that either physical
annulus has one sign.

There is also a linear-size absolute bound. Cauchy--Schwarz for two
translates gives

\[
 |\mathcal R(u)|\le\mathcal R(0).
\tag{3.1}
\]

The positive entries in (1.9) also show that every nonzero term along one
active ray has its primitive beta sign. Using this fact,
\(|\beta|\le2\), ratio support, and
\(\sum_{n\le Y}n^{-1/2}\le2\sqrt Y\),

\[
\begin{aligned}
 D(X)+2(P(X)+N(X))
 &=\sum_{m,n\le X}{|\beta(m)\beta(n)|\over\sqrt{mn}}
   \left|\mathcal R\!\left(\log{m\over n}\right)\right|\\
 &\le8e\,\mathcal R(0)X.
\end{aligned}
\tag{3.2}
\]

Consequently

\[
 \boxed{P(X)+N(X)\le4e\,\mathcal R(0)X.}
\tag{3.3}
\]

This is only the trivial \(O(X)\) scale. It supplies no subpower
cancellation.

The frozen first-rung theorem says

\[
 \mathrm{RH}\Longleftrightarrow\mathcal E_1(X)=X^{o(1)}.
\tag{3.4}
\]

Since \(D=X^{o(1)}\), equations (0.8) and (3.4) prove the equivalence
(0.10). In particular, it is enough for the *difference* \(P-N\) to be
subpower. Neither \(P\) nor \(N\), and neither the central nor outer
annulus, is asserted to be subpower separately.

## 4. Continuous shell balance and moment constraints

The physical kernel has exact continuous constraints. In the positive
ratio coordinate \(\rho=e^u\), Lebesgue measure \(du\) becomes logarithmic
Haar measure \(d\rho/\rho\). The unit-shell balance is

\[
\boxed{
\begin{aligned}
 \int_1^e\mathcal R(\log\rho){d\rho\over\rho}
  &={\sinh1\over2M^2},\\
 \int_e^{e^2}\mathcal R(\log\rho){d\rho\over\rho}
  &=-{\sinh1\over2M^2}.
\end{aligned}}
\tag{4.1}
\]

The first unit shell is not the positive tube: it contains the negative
shoulder \(e^\xi<\rho<e\). The actual positive/negative mass balance is

\[
\boxed{
 \int_1^{e^\xi}\mathcal R(\log\rho){d\rho\over\rho}
 =-\int_{e^\xi}^{e^2}\mathcal R(\log\rho){d\rho\over\rho}>0.}
\tag{4.2}
\]

The two low log moments are

\[
\boxed{
\begin{aligned}
 \int_1^{e^2}\log\rho\,\mathcal R(\log\rho){d\rho\over\rho}
 &={2-\sinh2\over32\sinh^4(1/2)},\\
 \int_1^{e^2}(\log\rho)^2\mathcal R(\log\rho){d\rho\over\rho}
 &=-1.
\end{aligned}}
\tag{4.3}
\]

These follow by evenness from the predecessor's full absolute-first and
second moments.

Equations (4.1)--(4.3) constrain \(\mathcal R(u)du\). The primitive energy
(2.7) instead integrates against \(d\Lambda_X\). No change of variables
turns the signed atomic arithmetic measure into \(du\). Therefore the
continuous moments imply no discrete identity such as \(C_+=O_-\),
\(C_-=O_+\), or \(P=N\).

## 5. Exact positivity no-go

There are two independent obstructions to an annular positivity shortcut.

First, isolate any nonzero off-diagonal physical edge with value \(k\).
Its off-diagonal two-point matrix is

\[
 \begin{pmatrix}0&k\\k&0\end{pmatrix},
\tag{5.1}
\]

whose eigenvalues are \(-|k|,|k|\). Thus every nonempty isolated central
or outer off-diagonal form is indefinite. The full matrix regains
positive semidefiniteness only after its diagonal and all assembled edges
are restored.

Second, the literal beta source realizes both signs inside both physical
annuli. This can be proved without the decimal value of \(\xi\). For
\(C(q)=M^2\mathcal R(q)\), direct substitution gives

\[
 8e^{3/2}C(1/2)=e^3-2e^2+6e-3>0.
\tag{5.2}
\]

Since the inner branch is strictly decreasing, (5.2) gives

\[
 \xi>{1\over2}.
\tag{5.3}
\]

The elementary inequalities

\[
 e^{1/2}>1+{1\over2}={3\over2},
 \qquad
 2<e<3,
 \qquad
 e^2>4
\tag{5.4}
\]

then classify the following four coprime active rays exactly:

| primitive ray \((r,s)\) | ratio | beta phase \(\beta(r)\beta(s)\) | physical annulus | ray contribution |
|---|---:|---:|---|---:|
| \((2,3)\) | \(3/2\) | \(+1\) | central | positive |
| \((5,6)\) | \(6/5\) | \(-1\) | central | negative |
| \((1,3)\) | \(3\) | \(-1\) | outer | positive |
| \((2,7)\) | \(7/2\) | \(+1\) | outer | negative |

For example, \(6/5<3/2<e^{1/2}<e^\xi\), whereas
\(e<3<7/2<4<e^2\) and \(\xi<1\). The fixed radial sign theorem (1.13)
shows that common-factor summation cannot reverse any row of the table.

This exactly refutes:

- termwise positivity in the central tube;
- termwise negativity in the outer annulus;
- positive semidefiniteness of either isolated off-diagonal annular block;
- any cancellation claim based only on the sign or moments of
  \(\mathcal R\).

It does **not** prove that the complete central or outer beta-prefix block
has either sign, nor does it refute the possibility of a deeper arithmetic
cancellation theorem. Those statements remain undetermined.

## 6. Analytic programme implications

The primitive normal form isolates the remaining burden without changing
it:

~~~text
positive physical tube + positive beta phase      C_+
positive physical tube + negative beta phase      C_-
negative physical annulus + positive beta phase   O_+
negative physical annulus + negative beta phase   O_-

RH-equivalent cancellation:
    (C_+ + O_-) - (C_- + O_+) = X^{o(1)}.
~~~

The common factor is not the source of sign oscillation: its exact
harmonic amplitude is positive. All ray signs already reside in the
primitive beta phase. Conversely, grouping by physical annulus alone
mixes those phases and loses the exact Gram assembly.

A viable estimate may exploit joint information about prime parity,
primitive ratio, and common-factor occupancy. The present theorem gives
no such estimate. In particular:

- (0.9) is a consequence of strict assembled Gram positivity, not a
  cancellation theorem;
- the \(O(X)\) cap (3.3) is far above the RH-equivalent subpower scale;
- continuous log-Haar moment cancellation is not an arithmetic sampling
  theorem;
- applying absolute values separately to the four channels replaces the
  open difference \(P-N\) by the much stronger quantity \(P+N\).

## 7. Scope ledger

| statement | grade |
|---|---|
| full-gcd primitive-ray reindexing (1.4) | **PROVED EXACT** |
| exceptional profiles and closed radial factor (1.9)--(1.12) | **PROVED EXACT** |
| fixed sign on every active primitive ray (1.13) | **PROVED EXACT** |
| four-channel annular identity (0.6) | **PROVED EXACT** |
| positive-mass identity and Gram inequality (0.8)--(0.9) | **PROVED EXACT** |
| continuous shell and log-moment constraints | **PROVED EXACT** |
| termwise or geometry-only annular positivity | **REFUTED EXACTLY** |
| RH equivalence of the cancellation gate (0.10) | **PROVED FROM THE PINNED FIRST-RUNG ENERGY CRITERION** |
| sign of either complete physical annulus | **NOT DETERMINED** |
| subpower cancellation in \(P-N\) | **OPEN; EQUIVALENT TO RH** |
| RH or GRH | **NOT PROVED** |

Equivalent RH criteria are common. No external novelty claim is made
without a dedicated literature comparison.

## 8. Bounded replay

The replay checks the four frozen base blobs and four frozen sign-geometry
blobs;
the local beta coefficients; 2,430 direct-versus-closed radial identities,
including \(67\) and \(67^2\) primitive layers; and an independent exact
source-pair reconstruction at cap 72 in 485 square-root coordinates. It
also checks the physical four-channel assembly at \(X=30\), the four
physical sign witnesses, the two-point indefinite spectrum, and bounded
Simpson regressions for the three half-moments.

The signed toy kernel used for the exact square-root-vector reconstruction
is explicitly not the physical autocorrelation. It authenticates the
scale-invariant gcd reindexing; the physical formula and sign theorem are
proved in the pinned predecessor. Floating-point witness and quadrature
values are regression checks only.

No zeta zero, prime interval, curve, random sample, or L-function is
evaluated.

~~~text
python -B research/l-families/atlas/function_field/ffps_beta_gram_annular_primitive_normal_form.py --check
python -B -O research/l-families/atlas/function_field/ffps_beta_gram_annular_primitive_normal_form.py --check
python -B -m unittest tests.test_ffps_beta_gram_annular_primitive_normal_form
python -B -O -m unittest tests.test_ffps_beta_gram_annular_primitive_normal_form
python -B -m ruff check research/l-families/atlas/function_field/ffps_beta_gram_annular_primitive_normal_form.py tests/test_ffps_beta_gram_annular_primitive_normal_form.py
python -B -m ruff format --check research/l-families/atlas/function_field/ffps_beta_gram_annular_primitive_normal_form.py tests/test_ffps_beta_gram_annular_primitive_normal_form.py
~~~
