# The complete beta source is a stable second difference of one 67-free channel

Status: **exact source factorization and sharp-prefix inverse; exact
RH-equivalent single-channel assembled criterion; conditional reduction of
the three-channel `COREAGG` route to its central channel; no new estimate for
that channel, `PRIMCAR`, RH, or GRH**

Architecture: **Architecture A only**.  No family or sheaf estimate is used.

Bounded exact replay:
[`ffps_beta_second_difference_single_channel_reduction.py`](ffps_beta_second_difference_single_channel_reduction.py).
Canonical fixture:
[`ffps_beta_second_difference_single_channel_reduction.json`](ffps_beta_second_difference_single_channel_reduction.json).

Frozen source: PR #760 head
`3a595dda92ef827a41e50d2395309692a93748ad`, specifically the exact beta
boundary criterion, the five-channel primitive decomposition, the full
core-wavelet transform, and the principal-frequency firewall pinned by the
replay.

## 0. Outcome

The current primitive route treats the three independent exceptional panels

\[
 \alpha=0,1,2
\]

separately and then takes positive square means.  That is a valid sufficient
route, but it discards one exact piece of source algebra before estimation.

Put \(q=67\), and let

\[
 \mu^{\langle q\rangle}(n)=\mu(n)\mathbf 1_{q\nmid n}.
\tag{0.1}
\]

The complete source is

\[
 \beta=(\delta_1-\delta_q)*\mu.
\tag{0.2}
\]

Since

\[
 \mu=(\delta_1-\delta_q)*\mu^{\langle q\rangle},
\]

one has the exact convolution identity

\[
 \boxed{
 \beta=(\delta_1-\delta_q)^{*2}*
        \mu^{\langle q\rangle}.}
\tag{0.3}
\]

Thus the local coefficients `(1,-2,1)` are not three unrelated sources.
They are one **second multiplicative difference** of the single 67-free
Möbius source.

Let `K_bd` be the frozen compact boundary kernel, and define the sharp-prefix
fields

\[
 \begin{aligned}
 U_X(t)&=\sum_{\substack{n\le X\\q\nmid n}}
 {\mu(n)\over\sqrt n}K_{\rm bd}(t-\log n),\\
 G_X(t)&=\sum_{n\le X}{\beta(n)\over\sqrt n}
 K_{\rm bd}(t-\log n).
 \end{aligned}
\tag{0.4}
\]

Writing \(L=\log q\) and \(a=q^{-1/2}\), (0.3) gives the exact finite-prefix
identity

\[
 \boxed{
 G_X(t)=U_X(t)-2aU_{X/q}(t-L)+a^2U_{X/q^2}(t-2L).}
\tag{0.5}
\]

It has an exact finite inverse:

\[
 \boxed{
 U_X(t)=
 \sum_{0\le j\le\lfloor\log_qX\rfloor}
 (j+1)a^jG_{X/q^j}(t-jL).}
\tag{0.6}
\]

No infinite tail and no softened prefix occurs.  The inverse terminates
because a prefix below one is empty.

For a prefix family `F`, put

\[
 \mathcal M_F(X)=\sup_{1\le Y\le X}\|F_Y\|_{L^2(\mathbb R)}.
\tag{0.7}
\]

Translation is an `L^2` isometry, so (0.5)--(0.6) imply

\[
 \boxed{
 (1-a)^2\mathcal M_U(X)
 \le \mathcal M_G(X)
 \le (1+a)^2\mathcal M_U(X).}
\tag{0.8}
\]

The constants are independent of `X`.  Consequently

\[
 \boxed{
 \|G_X\|_2^2=X^{o(1)}
 \quad\Longleftrightarrow\quad
 \|U_X\|_2^2=X^{o(1)}.}
\tag{0.9}
\]

The frozen theorem identifies the left assertion with RH.  Hence the right
assertion is also an exact RH-equivalent criterion.

This has a direct consequence for PR #760.  The 67-free field has only the
central primitive panel.  If `PRIMLS_0`, `PRIMCAR_0`, `COREAGG_0`, and
`COREWAVE_0` denote the existing gates restricted to `alpha=0`, then

\[
 \boxed{
 \mathrm{COREWAVE}_0
 \Longrightarrow\mathrm{COREAGG}_0
 \Longleftrightarrow\mathrm{PRIMCAR}_0
 \Longrightarrow\mathrm{PRIMLS}_0
 \Longrightarrow\mathrm{RH}.}
\tag{0.10}
\]

The first three arrows are the existing per-channel arguments.  The last
arrow is now justified by applying the central panel to `U` and then using
(0.9).  Therefore the `alpha=1,2` positive gates are **not necessary for this
sufficient route**.  They remain valid source-resolved diagnostics, but a
source-faithful proof attempt should first attack the assembled central
channel before paying for them separately.

No estimate in (0.10) is proved here.

## 1. Exact source factorization

At primes other than `q`, both \(\mu^{\langle q\rangle}\) and \(\mu\) have
local polynomial `1-z`.  At `q`, the former has local polynomial one and

\[
 (\delta_1-\delta_q)*\mu^{\langle q\rangle}
\]

has local polynomial `1-z`.  This proves

\[
 \mu=(\delta_1-\delta_q)*\mu^{\langle q\rangle}.
\]

Applying the extra source difference proves (0.3).  Coefficientwise, for
`q`-free squarefree `m`,

\[
 \beta(q^em)=
 \begin{cases}
 \mu(m),&e=0,\\
 -2\mu(m),&e=1,\\
 \mu(m),&e=2,\\
 0,&e\ge3.
 \end{cases}
\tag{1.1}
\]

This is exactly the `(c_0,c_1,c_2)=(1,-2,1)` source law used in the frozen
five-channel decomposition.

Insert (1.1) into (0.4).  A term at `q^j m` has normalization

\[
 {1\over\sqrt{q^jm}}=a^j{1\over\sqrt m}
\]

and translates the kernel by `jL`.  The three local states therefore give
(0.5) with the original prefix `q^jm<=X` intact.

## 2. Finite inverse and uniform conditioning

On prefix families define

\[
 (\mathsf SF)_X(t)=F_{X/q}(t-L).
\tag{2.1}
\]

Equation (0.5) is

\[
 G=(I-a\mathsf S)^2U.
\tag{2.2}
\]

The formal inverse is

\[
 (I-a\mathsf S)^{-2}
 =\sum_{j\ge0}(j+1)a^j\mathsf S^j.
\tag{2.3}
\]

For a fixed prefix `X`, every term with `q^j>X` is zero.  Thus (2.3) is a
finite algebraic identity and proves (0.6), without any convergence
interchange.

Taking norms in (0.5) gives the upper bound in (0.8).  Taking norms in
(0.6) gives

\[
 \mathcal M_U(X)
 \le\sum_{j\ge0}(j+1)a^j\mathcal M_G(X)
 ={1\over(1-a)^2}\mathcal M_G(X),
\tag{2.4}
\]

which proves the lower bound.

The maximal formulation does not strengthen the all-positive-exponent
criterion.  A bound `||F_Y||^2 <= C_epsilon Y^epsilon` for every `Y>=1`
immediately gives the same bound with `Y` replaced by the supremum range
`Y<=X`, and the converse is trivial.  Squaring (0.8) therefore proves (0.9).

## 3. The exact one-channel assembled primitive criterion

Let `R` be the frozen compact autocorrelation.  The diagonal of the 67-free
field is

\[
 \mathcal D_U(X)=\mathcal R(0)
 \sum_{\substack{n\le X\\q\nmid n}}{\mu(n)^2\over n}
 \ll_{\mathcal R}1+\log X.
\tag{3.1}
\]

Thus (0.9) is equivalent to a subpower estimate for the signed off-diagonal
of `U`.

For squarefree 67-free `d`, define the already frozen central panel

\[
 \begin{aligned}
 \mathcal P_0(d;H,V)
 =\sum_{\substack{a,b\ {m squarefree},\ q\nmid ab\\
 (a,b)=1,\ (ab,d)=1\\H<\max(a,b)\le V}}
 {\mu(a)\mu(b)\over\sqrt{ab}}
 \mathcal R\!\left(\log{a\over b}\right).
 \end{aligned}
\tag{3.2}
\]

An exact common-factor decomposition gives, for each dyadic primitive shell,

\[
 \boxed{
 \mathcal S_H^U(X)=
 \sum_{\substack{d\le X/H\\d\ {m squarefree},\ q\nmid d}}
 {1\over d}\,
 \mathcal P_0\!\left(
 d;H,\min\left(2H,{X\over d}\right)\right).}
\tag{3.3}
\]

If `J=ceil(log_2 X)`, the off-diagonal is exactly

\[
 \boxed{
 \mathcal O_U(X)=\sum_{j=0}^{J-1}\mathcal S_{2^j}^U(X).}
\tag{3.4}
\]

Combining (0.9), (3.1), and (3.3)--(3.4) yields the source-faithful
single-channel equivalence

\[
 \boxed{
 \mathrm{RH}
 \quad\Longleftrightarrow\quad
 |\mathcal O_U(X)|=X^{o(1)}.}
\tag{3.5}
\]

This is an assembled signed scalar, not a positive channelwise square mean.
Applying weighted Cauchy and the exact dyadic endpoint reduction to only
(3.2) proves `PRIMLS_0 -> RH`.  More explicitly, with `D=X/H`,

\[
 |\mathcal S_H^U(X)|
 \le
 \left(\sum_{d\le D}{1\over d}\right)^{1/2}
 \left(
 \sum_{d\le D}{1\over d}
 \sup_{H\le V\le2H}|\mathcal P_0(d;H,V)|^2
 \right)^{1/2}.
\tag{3.6}
\]

The first factor is logarithmic, `PRIMLS_0` makes the second subpower, and
there are only `O(log X)` shells in (3.4).  The frozen core transform is
per-channel, so its proofs give

\[
 \mathrm{COREAGG}_0\Longleftrightarrow\mathrm{PRIMCAR}_0,
 \qquad
 \mathrm{COREWAVE}_0\Longrightarrow\mathrm{COREAGG}_0.
\tag{3.7}
\]

Equations (3.5)--(3.7) prove (0.10).

Crucially, (3.5) does **not** show that RH implies `PRIMCAR_0` or
`COREAGG_0`.  Those remain stronger positive sufficient gates.

## 4. Frequency firewall and the load-bearing half-weight

On a logarithmic Fourier mode `exp(i theta t)`, the source filter has symbol

\[
 h_q(\theta)=
 \left(1-q^{-1/2}e^{-i\theta\log q}\right)^2.
\tag{4.1}
\]

Hence

\[
 \boxed{
 (1-q^{-1/2})^2
 \le |h_q(\theta)|
 \le(1+q^{-1/2})^2.}
\tag{4.2}
\]

There is no real-frequency zero.  In particular, the principal logarithmic
frequency has multiplier `(1-q^(-1/2))^2`, not zero.  This complements the
frozen principal additive-frequency theorem: neither the compact boundary
mean nor the finite `67` source difference deletes the principal burden.

The half-weight is load-bearing.  With coefficients normalized by `n^-sigma`,
the same argument has contraction `q^-sigma`.  The inverse coefficients are

\[
 (j+1)q^{-j\sigma}.
\tag{4.3}
\]

They are summable exactly for `sigma>0`.  At `sigma=0`, the symbol
`(1-e^(-i theta log q))^2` vanishes at `theta=0` and the finite inverse cost
grows quadratically with the q-adic horizon.  Thus the stable reduction is a
genuine consequence of the native `n^-1/2` normalization, not a formal
license to remove arbitrary source differences.

## 5. Consequence for the next Architecture A pass

The exact route can now be ranked more sharply:

1. preserve the assembled central scalar (3.3)--(3.5) and seek cancellation
   there before applying a square mean;
2. if a Carleson route is still preferred, attack only `PRIMCAR_0` or its
   equivalent `COREAGG_0` first;
3. retain `alpha=1,2` as diagnostics or held-out checks, not mandatory
   positive gates;
4. use the Witt-zeta and gcd-mode packets only after the sharp hyperbola has
   been coupled to this assembled central source.

This does not make the remaining arithmetic theorem weaker than RH.  It
removes a finite, stably invertible source adapter that had been expanded
into three positive channel obligations.

## 6. Scope firewall

- The theorem retains the complete signed beta source before inversion.
- The exact inverse uses multiple smaller prefixes and physical
  translations; it is not a pointwise identity at one frozen horizon.
- The result removes the need to prove the exceptional positive gates; it
  does not prove they follow from the central gate.
- `PRIMLS_0`, `PRIMCAR_0`, `COREAGG_0`, and `COREWAVE_0` remain unproved.
- The single-channel assembled scalar (3.5) remains RH-equivalent and is not
  estimated here.
- The Witt-zeta poles and sharp-hyperbola endpoint problem remain.
- Architecture B is outside this packet.

**No COREWAVE, COREAGG, PRIMCAR, PRIMLS, RH, or GRH estimate is proved.**

## 7. Proof ledger

| statement | grade |
|---|---|
| beta as a second difference of 67-free Möbius (0.3) | **PROVED EXACT** |
| sharp-prefix forward identity (0.5) | **PROVED EXACT** |
| finite sharp-prefix inverse (0.6) | **PROVED EXACT** |
| maximal norm conditioning (0.8) | **PROVED** |
| beta / 67-free boundary-energy equivalence (0.9) | **PROVED AT ALL-POSITIVE-EXPONENT SCALE** |
| one-channel assembled primitive identity (3.3)--(3.4) | **PROVED EXACT** |
| one-channel assembled criterion equivalent to RH (3.5) | **PROVED USING THE FROZEN BETA CRITERION** |
| `COREAGG_0 <=> PRIMCAR_0 -> RH` | **PROVED AS A CONDITIONAL CHAIN** |
| frequency annulus and `sigma=0` firewall | **PROVED EXACT** |
| any central-channel estimate / RH / GRH | **NOT PROVED** |

No external novelty or priority claim is made.

## 8. Bounded replay

```text
python -B research/l-families/atlas/function_field/ffps_beta_second_difference_single_channel_reduction.py --check
python -B -O research/l-families/atlas/function_field/ffps_beta_second_difference_single_channel_reduction.py --check
python -B -m unittest tests.test_ffps_beta_second_difference_single_channel_reduction
python -B -O -m unittest tests.test_ffps_beta_second_difference_single_channel_reduction
```

The replay checks the exact local source law, the finite forward and inverse
prefix transforms for several q-adic horizons, the inverse coefficient sum,
the source-frequency annulus, and an exact small central-panel common-factor
reassembly.  It scans no zeta zero, prime family, finite field, curve,
conductor family, or `L`-function.
