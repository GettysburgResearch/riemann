# Endpoint compression has a sharp square-root sampling frontier and one dyadic beta bridge

Status: **exact square-root-mesh endpoint theorem for the literal beta
source, sharp arbitrary-coefficient endpoint-query no-go, and exact dyadic
bridge decomposition; the beta bridge estimate, logarithmic endpoint-only
criterion, RH, and GRH remain open**

Bounded exact replay:
[ffps_endpoint_sampling_square_root_frontier.py](ffps_endpoint_sampling_square_root_frontier.py).
Canonical summary:
[ffps_endpoint_sampling_square_root_frontier.json](ffps_endpoint_sampling_square_root_frontier.json).

Frozen predecessor:
\(31c0e730ffe80683798d9cc830c26e9d451a8759\).
The replay pins the complete single-harmonic maximal phase-transport quartet
at that commit.

## 0. Outcome

Fix one nonzero guarded harmonic
\[
 t=t_{h,X}={2\pi h\over L_X}
\tag{0.1}
\]
and write
\[
 D_Y(t)=\sum_{n\le Y}{\beta(n)\over n^{1/2+it}},
 \qquad |\beta(n)|\le2.
\tag{0.2}
\]
The predecessor proves
\[
\mathrm{RH}\Longleftrightarrow
\sup_{Y\le X}|D_Y(t_{h,X})|^2=X^{o(1)}.
\tag{0.3}
\]

The first new theorem gives a deterministic endpoint compression.  Let
\[
 E_X=\{0=e_0<e_1<\cdots<e_m=X\}
\tag{0.4}
\]
and suppose its square-root mesh satisfies
\[
 \max_j(\sqrt{e_{j+1}}-\sqrt{e_j})\le R.
\tag{0.5}
\]
Here \(1\le R\le\sqrt X\); smaller meshes only increase the endpoint count
without changing the argument.
Then
\[
\boxed{
\sup_{Y\le X}|D_Y(t)|
\le\max_{e\in E_X}|D_e(t)|+4R.}
\tag{0.6}
\]
Consequently, for every prescribed \(R(X)=X^{o(1)}\), a predetermined
square-root grid with
\[
 |E_X|=O\!\left({\sqrt X\over R(X)}+1\right)=X^{1/2+o(1)}
\tag{0.7}
\]
gives the exact endpoint-only criterion
\[
\boxed{
\mathrm{RH}\Longleftrightarrow
\max_{e\in E_X}|D_e(t_{h,X})|^2=X^{o(1)}.}
\tag{0.8}
\]
The same statement holds with the fixed first-harmonic lattice weight
\(w_{h,X}\), because \(w_{h,X}^{\pm1}=X^{o(1)}\).

The exponent \(1/2\) is sharp for every source-blind argument using only
\[
 |a_n|\le n^{-1/2}.
\tag{0.9}
\]
For any sampler making at most \(m\) predetermined endpoint queries, and
for any prescribed unit-modulus phase sequence \(z_n\), there are
coefficients satisfying (0.9) such that
\[
 \sum_{n\le e}a_nz_n=0
\quad\text{at every sampled }e,
\tag{0.10}
\]
but
\[
\boxed{
\max_{Y\le X}\left|\sum_{n\le Y}a_nz_n\right|
\ge {\sqrt X\over2(m+1)}-{1\over2\sqrt X}.}
\tag{0.11}
\]
The same adversary defeats a deterministic adaptive value-query algorithm:
answer zero to every query and place a zero-total excursion in the largest
final unqueried gap.  Randomized performance guarantees are not analyzed.

Thus \(m=O(\log X)\), including ordinary dyadic endpoints, leaves a possible
\(X^{1/2-o(1)}\) excursion.  To make the worst source-blind interpolation
error subpower, (0.11) requires
\[
 m\ge X^{1/2-o(1)}.
\tag{0.12}
\]
Conversely the square-root mesh below uses \(X^{1/2+o(1)}\) samples and
suffices.  Thus exponent \(1/2\) is the sharp minimal sampling frontier;
larger polynomial-size samplers of course also work.

This no-go does **not** replace the literal beta signs by an adversary in
the RH theorem.  It says that coefficient size, sparsity-free endpoint
geometry, positivity, or an endpoint-query algorithm alone cannot compress
the beta maximal prefix to logarithmically many samples.

For the literal beta source, the exact missing arithmetic object is one
dyadic bridge.  Let
\[
 \mathfrak E_h(X)=
 \max_{e\in\{1,2,4,\ldots,X\}}|D_e(t_{h,X})|
\tag{0.13}
\]
where \(X\) is adjoined to the powers of two, and define
\[
 \mathfrak B_h(X)=
 \max_j\ \max_{2^j<Y\le\min(2^{j+1},X)}
 \left|
 \sum_{2^j<n\le Y}{\beta(n)\over n^{1/2+it_{h,X}}}
 \right|.
\tag{0.14}
\]
Then
\[
\boxed{
 {1\over2}\max(\mathfrak E_h,\mathfrak B_h)
 \le\sup_{Y\le X}|D_Y(t_{h,X})|
 \le2\max(\mathfrak E_h,\mathfrak B_h).}
\tag{0.15}
\]

Local phase transport within a dyadic block gives
\[
\boxed{
 (1+|t_{h,X}|\log2)^{-1}\mathfrak B_0(X)
 \le\mathfrak B_h(X)
 \le(1+|t_{h,X}|\log2)\mathfrak B_0(X),}
\tag{0.16}
\]
where
\[
 \mathfrak B_0(X)=
 \max_j\ \max_{2^j<Y\le\min(2^{j+1},X)}
 \left|
 \sum_{2^j<n\le Y}{\beta(n)\over\sqrt n}
 \right|.
\tag{0.17}
\]
Therefore
\[
\boxed{
\mathrm{RH}\Longleftrightarrow
\mathfrak E_h(X)^2=X^{o(1)}
\quad\text{and}\quad
\mathfrak B_0(X)^2=X^{o(1)}.}
\tag{0.18}
\]

Equation (0.17) is the canonical exact residual after dyadic endpoint
control: a maximal signed beta sum inside one dyadic block.  No minimality
claim over every conceivable source-specific summary, and no estimate for
this residual, is proved.

## 1. Square-root mesh interpolation

Consider arbitrary coefficients with
\[
 |a_n|\le {C\over\sqrt n},
 \qquad
 F_Y(t)=\sum_{n\le Y}a_nn^{-it}.
\tag{1.1}
\]
If \(e_j\le Y\le e_{j+1}\), then
\[
\begin{aligned}
 |F_Y(t)-F_{e_j}(t)|
 &\le C\sum_{e_j<n\le Y}n^{-1/2}\\
 &\le2C(\sqrt Y-\sqrt{e_j})\\
 &\le2CR.
\end{aligned}
\tag{1.2}
\]
This proves
\[
 \sup_{Y\le X}|F_Y(t)|
 \le\max_{e\in E_X}|F_e(t)|+2CR.
\tag{1.3}
\]
For the literal beta coefficients \(a_n=\beta(n)/\sqrt n\), \(C=2\), so
(1.3) is (0.6).

A grid equally spaced in the \(\sqrt Y\) coordinate has the cardinality in
(0.7).  If \(R=X^{o(1)}\), the additive interpolation error is subpower.
The forward half of (0.8) follows from the maximal one-harmonic theorem;
the reverse half follows from (0.6) and (0.3).

This is an actual literal-beta endpoint theorem.  It uses no cancellation
between sampled endpoints, but its endpoint count is square-root size rather
than logarithmic.

## 2. Sharp source-blind lower bound

Let an endpoint sampler make at most \(m\) queries in
\(\{1,\ldots,X\}\).  Adjoin \(0\) and \(X\).  The resulting ordered set has
at most \(m+1\) gaps, so one gap \((A,B]\) has length
\[
 G=B-A\ge {X\over m+1}.
\tag{2.1}
\]
Put \(q=\lfloor G/2\rfloor\).  Inside this gap, define
\[
 a_{A+j}=
 \begin{cases}
 X^{-1/2}\overline{z_{A+j}},&1\le j\le q,\\
 -X^{-1/2}\overline{z_{A+j}},&q<j\le2q,\\
 0,&\text{otherwise}.
 \end{cases}
\tag{2.2}
\]
Because \(A+j\le X\),
\[
 |a_{A+j}|=X^{-1/2}\le(A+j)^{-1/2}.
\tag{2.3}
\]
Every queried prefix is zero: it lies before the gap or after the complete
zero-total excursion.  At its midpoint the twisted prefix equals
\[
 {q\over\sqrt X}
 \ge {\sqrt X\over2(m+1)}-{1\over2\sqrt X},
\tag{2.4}
\]
which proves (0.11).

For a deterministic adaptive sampler, answer zero as each endpoint is
requested.  Once the \(m\) requests have been made, construction (2.2) in
the largest final gap is consistent with every answer.  Thus deterministic
adaptivity without arithmetic information does not improve the exponent.
Randomized query guarantees lie outside this theorem.

The lower bound and the square-root grid upper bound match at exponent
\(1/2\).  The result is information-theoretic and source-blind.  It is not
a counterexample involving the fixed Möbius signs.

## 3. Exact endpoint plus bridge decomposition

For any ordered endpoint set \(E_X\), define
\[
\begin{aligned}
 \mathfrak E_E&=\max_{e\in E_X}|D_e(t)|,\\
 \mathfrak B_E&=
 \max_j\ \max_{e_j\le Y\le e_{j+1}}
 |D_Y(t)-D_{e_j}(t)|,\\
 \mathfrak M&=\sup_{Y\le X}|D_Y(t)|.
\end{aligned}
\tag{3.1}
\]
The triangle inequality gives
\[
 \mathfrak M\le\mathfrak E_E+\mathfrak B_E
 \le2\max(\mathfrak E_E,\mathfrak B_E).
\tag{3.2}
\]
Conversely,
\[
 \mathfrak E_E\le\mathfrak M,
 \qquad
 \mathfrak B_E\le2\mathfrak M.
\tag{3.3}
\]
Equations (3.2)--(3.3) prove (0.15) for dyadic endpoints.

This decomposition is exact but deliberately modest.  It identifies the
precise residual discarded by endpoint sampling; it does not estimate it.

## 4. A dyadic bridge has essentially no Fourier twist

Fix a block \((A,B]\) with \(B/A\le2\), and put
\[
 S_{A,Y}(t)=
 \sum_{A<n\le Y}{\beta(n)\over n^{1/2+it}}.
\tag{4.1}
\]
Apply discrete Abel summation to the local coefficient sequence.  Its phase
variation satisfies
\[
\sum_{A<n<Y}
 |n^{-it}-(n+1)^{-it}|
\le |t|\log{Y\over A+1}
\le |t|\log2.
\tag{4.2}
\]
The forward and reverse demodulations therefore give
\[
\begin{aligned}
\max_{A<Y\le B}|S_{A,Y}(t)|
&\le(1+|t|\log2)
\max_{A<Y\le B}|S_{A,Y}(0)|,\\
\max_{A<Y\le B}|S_{A,Y}(0)|
&\le(1+|t|\log2)
\max_{A<Y\le B}|S_{A,Y}(t)|.
\end{aligned}
\tag{4.3}
\]
Taking the maximum over dyadic blocks proves (0.16).  Since
\(|t_{h,X}|=O_h(1/\log X)\), the comparison factor is \(1+o(1)\).

Thus the missing bridge is not a high-frequency phenomenon.  It is the
ordinary signed beta/Möbius short-interval maximal problem inside a
multiplicative block of ratio two.

## 5. What is now closed and what remains

The endpoint-compression landscape is:

~~~text
all prefixes at one harmonic
  <-> RH exactly;

square-root-mesh endpoints
  <-> all prefixes by absolute interpolation;

logarithmic or dyadic endpoints
  fail for arbitrary coefficient envelopes;

dyadic beta endpoints + one signed bridge gate
  <-> all literal-beta prefixes exactly.
~~~

The open arithmetic question is whether the literal beta endpoint data can
control \(\mathfrak B_0(X)\), or whether a separate short-interval theorem
is unavoidable.  The arbitrary-coefficient lower bound cannot decide that
source-specific question.

Possible attacks on the bridge include a maximal short-interval
Möbius theorem, a dyadic Carleson estimate preserving beta signs, or a
Volterra relation special to the duplicate-\(67\) source.  None is supplied
here.

## 6. Claim ledger

| statement | grade |
|---|---|
| square-root mesh inequality (0.6) | **PROVED FOR THE LITERAL BETA SOURCE** |
| square-root endpoint RH criterion (0.8) | **PROVED FROM THE PINNED ONE-HARMONIC THEOREM** |
| arbitrary-coefficient lower bound (0.11) | **PROVED BY AN EXACT HIDDEN EXCURSION** |
| adaptive source-blind lower bound | **PROVED BY THE ZERO-ANSWER ADVERSARY** |
| exponent-\(1/2\) sampling frontier | **SHARP FOR THE COEFFICIENT ENVELOPE** |
| endpoint/bridge comparison (0.15) | **PROVED EXACT** |
| dyadic local phase transport (0.16) | **PROVED EXACT** |
| beta endpoint-plus-bridge RH criterion (0.18) | **PROVED EXACT** |
| dyadic endpoints alone for the literal beta source | **OPEN / NOT CLAIMED** |
| beta bridge estimate, RH, or GRH | **NOT PROVED** |

## 7. Bounded replay

~~~text
python -B research/l-families/atlas/function_field/ffps_endpoint_sampling_square_root_frontier.py --check
python -B -O research/l-families/atlas/function_field/ffps_endpoint_sampling_square_root_frontier.py --check
python -B -m unittest tests.test_ffps_endpoint_sampling_square_root_frontier
python -B -O -m unittest tests.test_ffps_endpoint_sampling_square_root_frontier
python -B -m ruff check research/l-families/atlas/function_field/ffps_endpoint_sampling_square_root_frontier.py tests/test_ffps_endpoint_sampling_square_root_frontier.py
python -B -m ruff format --check research/l-families/atlas/function_field/ffps_endpoint_sampling_square_root_frontier.py tests/test_ffps_endpoint_sampling_square_root_frontier.py
~~~

The replay uses a 256-term exact rational Gaussian hidden excursion,
dyadic endpoints, an exact square-root grid of mesh two, and a 16-term
endpoint/bridge norm identity.  It performs no floating-point computation,
zeta-zero enumeration, prime search, or large matrix calculation.
