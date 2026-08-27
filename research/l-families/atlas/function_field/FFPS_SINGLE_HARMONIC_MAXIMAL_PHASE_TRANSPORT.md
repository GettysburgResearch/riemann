# One signed guarded harmonic is RH-equivalent after maximal-prefix phase transport

Status: **exact maximal-prefix phase-transport theorem and exact
single-harmonic RH equivalence for the literal beta source; the required
single-harmonic estimate, an endpoint-only replacement, RH, and GRH remain
open**

Bounded exact replay:
[ffps_single_harmonic_maximal_phase_transport.py](ffps_single_harmonic_maximal_phase_transport.py).
Canonical summary:
[ffps_single_harmonic_maximal_phase_transport.json](ffps_single_harmonic_maximal_phase_transport.json).

Frozen source commit:
\(ece0694b29dfc6cd335a8f9da20fe141141d607b\).
The replay pins the complete critical spectral-witness and first-harmonic
theorem quartets at that commit.

One standard theorem is imported explicitly:
\[
\boxed{
\mathrm{RH}\Longleftrightarrow
\sup_{1\le Y\le X}\left|\sum_{n\le Y}\mu(n)\right|
=X^{1/2+o(1)}.}
\tag{0.1}
\]
This is the classical Mertens formulation of RH.  It is not reproved by the
bounded replay.

Throughout, a display of the form \(F(X)=X^{o(1)}\) denotes the subpower
upper bound \(F(X)\ll_\epsilon X^\epsilon\) for every \(\epsilon>0\); the
analogous convention is used in (0.1).  Prefix sums change only when their
endpoint crosses an integer, so every supremum below may be taken over
integer \(X,Y\).  Abel identities are written with those integer endpoints.

## 0. Outcome

Let
\[
 D_Y(t)=\sum_{n\le Y}{\beta(n)\over n^{1/2+it}},
 \qquad
 \beta(n)=\mu(n)-\mathbf1_{67\mid n}\mu(n/67).
\tag{0.2}
\]
For the fixed critical kernel and one guarded period, write
\[
 L_X=\log X+S_{r,\infty}+\delta,
 \qquad
 t_{h,X}={2\pi h\over L_X},
\tag{0.3}
\]
where \(h\ne0\) is any fixed integer and \(r\ge1\) is fixed.
For all sufficiently large \(X\), \(|h|\le K_*(X)\), so this is literally
one of the retained guarded Fourier coordinates.

The new mechanism is a general maximal phase-transport theorem.  For
arbitrary complex coefficients \(a_n\), put
\[
 F_Y(t)=\sum_{n\le Y}a_nn^{-it},
 \qquad
 \mathfrak F_t(X)=\sup_{1\le Y\le X}|F_Y(t)|.
\tag{0.4}
\]
Then, for every real \(t\),
\[
\boxed{
 {1\over1+|t|\log X}\mathfrak F_0(X)
 \le\mathfrak F_t(X)
 \le(1+|t|\log X)\mathfrak F_0(X).}
\tag{0.5}
\]

At one fixed guarded harmonic,
\[
 |t_{h,X}|\log X<2\pi|h|,
\tag{0.6}
\]
so (0.5) is a uniform constant isomorphism.  Applying it to
\(a_n=\beta(n)/\sqrt n\) gives
\[
\boxed{
 {1\over1+2\pi|h|}\mathfrak D_0(X)
 \le\mathfrak D_{t_{h,X}}(X)
 \le(1+2\pi|h|)\mathfrak D_0(X),}
\tag{0.7}
\]
where
\[
 \mathfrak D_t(X)=\sup_{1\le Y\le X}|D_Y(t)|.
\tag{0.8}
\]

The zero-frequency beta prefix is classically RH-equivalent:
\[
\boxed{
\mathrm{RH}\Longleftrightarrow
\mathfrak D_0(X)^2=X^{o(1)}.}
\tag{0.9}
\]
Consequently,
\[
\boxed{
\mathrm{RH}\Longleftrightarrow
\sup_{1\le Y\le X}|D_Y(t_{h,X})|^2=X^{o(1)}.}
\tag{0.10}
\]

This is already a one-frequency theorem.  It also retains the exact
critical-lattice weight
\[
 w_{h,X}={|\widehat B_{r,\infty}(t_{h,X})|^2\over L_X}.
\tag{0.11}
\]
The pinned low-frequency theorem gives
\[
\boxed{
 w_{h,X}\sim
 K_0^2(2\pi|h|)^{2r}L_X^{-(2r+1)},
 \qquad
 K_0=3(1-\sqrt2)^2(\log2)^2\ne0.}
\tag{0.12}
\]
Both \(w_{h,X}\) and \(w_{h,X}^{-1}\) are \(X^{o(1)}\).  Thus
\[
\boxed{
\mathrm{RH}\Longleftrightarrow
w_{h,X}\sup_{1\le Y\le X}|D_Y(t_{h,X})|^2=X^{o(1)}.}
\tag{0.13}
\]
The raw-versus-weighted caveat for the maximum over the whole growing
lattice therefore disappears at any one fixed nonzero harmonic: its weight
has an explicit polylogarithmic lower bound.

In particular, \(h=1\) alone suffices.  Within the positive
kernel-weighted retained Fourier lattice, and under maximal-prefix
assembly, the cardinality-minimal nonempty window consists of one nonzero
guarded coordinate.  The \(k=0\) lattice coordinate cannot replace it
because \(\widehat B(0)=0\).  This is not an information-theoretic claim
about raw coordinates: the unweighted central beta prefix is itself
RH-equivalent by (0.9).

The maximal prefix is load-bearing.  Equations (0.10)--(0.13) do **not**
claim that the isolated endpoint
\[
 w_{1,X}|D_X(t_{1,X})|^2
\tag{0.14}
\]
is RH-equivalent.  They also do not replace the prefix supremum by dyadic
endpoints.  Those are separate open compression problems.

## 1. Exact phase transport for arbitrary coefficients

Let
\[
 A_Y=\sum_{n\le Y}a_n.
\tag{1.1}
\]
Discrete Abel summation gives
\[
\boxed{
 F_Y(t)=
 A_YY^{-it}
 +\sum_{n<Y}A_n\left(n^{-it}-(n+1)^{-it}\right).}
\tag{1.2}
\]
Since
\[
\begin{aligned}
\left|n^{-it}-(n+1)^{-it}\right|
&=\left|1-e^{-it\log(1+1/n)}\right|\\
&\le |t|\log(1+1/n),
\end{aligned}
\tag{1.3}
\]
the total variation telescopes logarithmically:
\[
 \sum_{n<Y}
 \left|n^{-it}-(n+1)^{-it}\right|
 \le |t|\log Y.
\tag{1.4}
\]
Equations (1.2)--(1.4) prove
\[
 |F_Y(t)|\le(1+|t|\log Y)\mathfrak F_0(X)
\tag{1.5}
\]
uniformly for \(Y\le X\).

For the reverse direction, regard \(a_nn^{-it}\) as the coefficient
sequence and demodulate it by \(n^{it}\).  The same Abel argument gives
\[
 |F_Y(0)|\le(1+|t|\log Y)\mathfrak F_t(X).
\tag{1.6}
\]
Taking suprema proves (0.5).  No smoothness, multiplicativity, Möbius
cancellation, limiting integral, or hypothesis on \(t\) enters the proof.

The exact common period now matters.  All prefixes \(Y\le X\) are tested at
the one frequency \(t_{h,X}\) before the supremum is taken.  This is exactly
the architecture needed for (1.6); reperiodizing every prefix separately
would change the demodulating frequency inside the maximal family.

## 2. The zero-frequency beta prefix is RH-equivalent

Define
\[
 C(Y)=\sum_{n\le Y}\mu(n),
 \qquad
 M^\sharp_Y=\sum_{n\le Y}{\mu(n)\over\sqrt n}.
\tag{2.1}
\]
Partial summation in both directions gives
\[
\begin{aligned}
 M^\sharp_Y
 &=Y^{-1/2}C(Y)
 +{1\over2}\int_1^Y C(u)u^{-3/2}\,du,\\
 C(Y)
 &=Y^{1/2}M^\sharp_Y
 -{1\over2}\int_1^Y M^\sharp_u u^{-1/2}\,du.
\end{aligned}
\tag{2.2}
\]
Therefore the imported criterion (0.1) is equivalent to
\[
\boxed{
\mathrm{RH}\Longleftrightarrow
\sup_{1\le Y\le X}|M^\sharp_Y|=X^{o(1)}.}
\tag{2.3}
\]

At zero frequency the literal duplicate-\(67\) identity is
\[
 D_Y(0)=M^\sharp_Y-67^{-1/2}M^\sharp_{Y/67}.
\tag{2.4}
\]
Its inverse terminates:
\[
 M^\sharp_Y=\sum_{j\ge0}67^{-j/2}D_{Y/67^j}(0).
\tag{2.5}
\]
With \(a=67^{-1/2}\), taking maximal prefixes gives
\[
\boxed{
 (1-a)\sup_{Y\le X}|M^\sharp_Y|
 \le\mathfrak D_0(X)
 \le(1+a)\sup_{Y\le X}|M^\sharp_Y|.}
\tag{2.6}
\]
Combining (2.3) and (2.6) proves (0.9).

This step preserves the exact beta source.  No unsigned model or
source-blind Gram estimate is substituted.

## 3. One guarded harmonic is enough

For fixed \(h\ne0\), equations (0.3) and
\(S_{r,\infty}+\delta>0\) give
\[
 |t_{h,X}|\log X
 ={2\pi|h|\log X\over\log X+S_{r,\infty}+\delta}
 <2\pi|h|.
\tag{3.1}
\]
Apply (0.5) with \(t=t_{h,X}\).  The resulting constants depend only on
\(h\), not on \(X\), and (0.7) follows.  Equations (0.7) and (0.9) prove
(0.10).

The pinned kernel expansion at zero is
\[
 \widehat B_{r,\infty}(t)
 =K_0(it)^r(1+O_r(|t|)).
\tag{3.2}
\]
Since \(t_{h,X}\to0\), this proves (0.12).  In particular, for sufficiently
large \(X\),
\[
 c_{h,r}(\log X)^{-(2r+1)}
 \le w_{h,X}
 \le C_{h,r}(\log X)^{-(2r+1)}
\tag{3.3}
\]
with positive fixed constants.  Multiplication or division by this weight
does not change an \(X^{o(1)}\) target, proving (0.13).

The result is stronger in coordinate count than the worst-witness theorem:
\[
\begin{array}{c}
\text{previous theorem: maximum over }X^{o(1)}\text{ retained frequencies},\\
\text{present theorem: one fixed nonzero frequency, but all prefixes}.
\end{array}
\tag{3.4}
\]
It does not make the arithmetic estimate easier automatically.  By (0.7),
the new single-harmonic target is a bounded coordinate change of the
classical weighted Mertens target.

## 4. Why endpoint-only phase retrieval is not claimed

The inverse half of (0.5) uses every prefix
\[
 \{D_Y(t_{h,X}):1\le Y\le X\}
\tag{4.1}
\]
at one common frequency.  An estimate only for \(D_X(t_{h,X})\) supplies
no bound for the Abel integral or discrete prefix sum in (1.6).

Likewise, the hypothesis
\[
 D_Y(t_{h,Y})=Y^{o(1)}
\tag{4.2}
\]
would evaluate different prefixes at different frequencies.  It does not
directly bound the common-frequency family in (4.1).

These observations are scope fences, not impossibility theorems for the
literal beta sequence.  A future Volterra inversion, dyadic assembly, or
source-specific recurrence might remove the full prefix supremum.  No such
result is proved here.

## 5. Interpretation

The first-harmonic unsigned firewall and the present signed theorem fit
together:

~~~text
unsigned first endpoint
  is power-size and obstructs source-blind operator bounds;

signed first harmonic plus every common-period prefix
  is exactly RH-equivalent by phase transport;

signed first endpoint alone
  remains unresolved.
~~~

The gain comes from assembly, not from a lucky cancellation at
\(t_{1,X}\).  Maximal-prefix phase transport shows that a bounded
logarithmic modulation cannot hide or create a positive Mertens exponent.

## 6. Claim ledger

| statement | grade |
|---|---|
| arbitrary-coefficient phase transport (0.5) | **PROVED EXACT BY DISCRETE ABEL SUMMATION** |
| fixed-harmonic constant bound (0.7) | **PROVED EXACT** |
| zero-frequency beta criterion (0.9) | **PROVED FROM THE CLASSICAL MERTENS CRITERION** |
| raw single-harmonic maximal criterion (0.10) | **PROVED RH-EQUIVALENT** |
| weighted single-harmonic maximal criterion (0.13) | **PROVED RH-EQUIVALENT FOR FIXED \(r,h\)** |
| one-coordinate minimality inside the weighted retained lattice | **PROVED; \(k=0\) IS IDENTICALLY NOTCHED** |
| endpoint-only first-harmonic criterion | **OPEN / NOT CLAIMED** |
| dyadic replacement of all prefixes | **OPEN / NOT CLAIMED** |
| the required signed estimate, RH, or GRH | **NOT PROVED** |

## 7. Bounded replay

~~~text
python -B research/l-families/atlas/function_field/ffps_single_harmonic_maximal_phase_transport.py --check
python -B -O research/l-families/atlas/function_field/ffps_single_harmonic_maximal_phase_transport.py --check
python -B -m unittest tests.test_ffps_single_harmonic_maximal_phase_transport
python -B -O -m unittest tests.test_ffps_single_harmonic_maximal_phase_transport
python -B -m ruff check research/l-families/atlas/function_field/ffps_single_harmonic_maximal_phase_transport.py tests/test_ffps_single_harmonic_maximal_phase_transport.py
python -B -m ruff format --check research/l-families/atlas/function_field/ffps_single_harmonic_maximal_phase_transport.py tests/test_ffps_single_harmonic_maximal_phase_transport.py
~~~

The replay checks forward and reverse finite Abel identities over twelve
prefixes using exact rational Gaussian phases, together with a ten-level
terminating duplicate-source scale inverse.  It performs no
floating-point computation, zeta-zero enumeration, prime search, or large
matrix calculation.
