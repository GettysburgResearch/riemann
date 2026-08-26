# Primitive-pair PRIMLS has an exact incidence Gram and a dyadic Carleson lift

Status: **exact finite dual Gram identity; exact fixed-height harmonic limit;
exact identification and centering of the surviving zero mode; conditional
dyadic Carleson gate sufficient for PRIMLS and hence for RH; neither the gate,
PRIMLS, RH, nor GRH is proved**

Bounded exact replay:
[`ffps_primitive_pair_harmonic_incidence_carleson.py`](ffps_primitive_pair_harmonic_incidence_carleson.py).
Canonical summary:
[`ffps_primitive_pair_harmonic_incidence_carleson.json`](ffps_primitive_pair_harmonic_incidence_carleson.json).

Frozen source: the primitive-pair large-sieve packet, including its exact
Möbius--Gram and biased-Boolean normal forms, at `dd1bd8766`. Its Markdown,
producer, JSON, and test are pinned by the replay.

## 0. Outcome

The source packet reduces the RH-bearing high primitive beta sector to three
independent panels

\[
 \mathcal P_{\alpha,\gamma}(d;H,U),
 \qquad
 (\alpha,\gamma)=(0,0),(1,0),(2,0),
\tag{0.1}
\]

and proves that the maximal harmonic square estimate `PRIMLS` implies RH.
It also diagonalizes a finite artificial divisor cube and finds a surviving
harmonic zero mode. This successor connects that cube to the **actual
truncated common-factor average**, and removes the endpoint supremum by an
exact dyadic reduction.

For one channel and one set `I` of integer primitive heights, let

\[
 \mathcal P_I(d)
 =\sum_{e\mid Q_H\atop(d,e)=1}W_{I,e},
\tag{0.2}
\]

where `Q_H` is the product of the primes `p != 67` with `p <= 2H`, and
`W_(I,e)` is the exact signed contribution of primitive pairs in `I` with
`ab=e`. Then, for every finite `D`,

\[
\boxed{
 \sum_{\substack{d\le D\\d\ {\rm squarefree},\ 67\nmid d}}
 {\lvert\mathcal P_I(d)\rvert^2\over d}
 =
 \sum_{e,f\mid Q_H}W_{I,e}\overline{W_{I,f}}
 K_D([e,f]),}
\tag{0.3}
\]

where

\[
 K_D(n)=
 \sum_{\substack{d\le D\\d\ {\rm squarefree},\ 67\nmid d\\(d,n)=1}}
 {1\over d}.
\tag{0.4}
\]

Thus the common-factor large sieve is exactly a positive semidefinite
incidence Gram problem. No heuristic independence and no asymptotic
replacement is used in (0.3).

For fixed `H` and `I`, the genuine truncated average has the limit

\[
\boxed{
 {1\over\log D}
 \sum_{\substack{d\le D\\d\ {\rm squarefree},\ 67\nmid d}}
 {\lvert\mathcal P_I(d)\rvert^2\over d}
 \longrightarrow
 {67\over68\zeta(2)}
 \mathbb E_{\nu_{Q_H}}
 \lvert\mathcal P_I(\delta)\rvert^2,}
\tag{0.5}
\]

where

\[
 \nu_Q(\delta)={1\over Z_Q\delta},
 \qquad
 Z_Q=\prod_{p\mid Q}\left(1+{1\over p}\right).
\tag{0.6}
\]

This proves that the biased Boolean cube in the source packet is not merely
a convenient toy. It is the exact limiting incidence law seen by the real
`d^-1` average at every fixed primitive block.

Its zero mode is the explicit **rho-tilted Möbius pair panel**

\[
\boxed{
 B_I
 =\mathbb E_{\nu_Q}\mathcal P_I(\delta)
 =\sum_{(a,b)\in I}
 {\mu(a)\rho(a)\mu(b)\rho(b)\over\sqrt{ab}}
 \mathcal R\!\left(\log{67^\alpha a\over67^\gamma b}\right),}
\tag{0.7}
\]

with

\[
 \rho(n)=\prod_{p\mid n}{p\over p+1}.
\tag{0.8}
\]

Consequently, putting

\[
 \mathcal P_I^\circ(d)=\mathcal P_I(d)-B_I
\tag{0.9}
\]

removes the harmonic zero mode exactly in the limiting product measure, and

\[
 \mathbb E_{\nu_Q}|\mathcal P_I|^2
 =|B_I|^2+
 \mathbb E_{\nu_Q}|\mathcal P_I^\circ|^2.
\tag{0.10}
\]

This is a decomposition, not a cancellation theorem. In particular, the
tilt in (0.7) retains the reciprocal-zeta factor. If `Re(s)>1`,

\[
 \sum_{(n,67)=1}{\mu(n)\rho(n)\over n^s}
 ={G_\rho(s)\over(1-67^{-s})\zeta(s)},
\tag{0.11}
\]

where

\[
 G_\rho(s)=
 \prod_{p\ne67}
 {1-\rho(p)p^{-s}\over1-p^{-s}}
\tag{0.12}
\]

converges absolutely and is nonzero for `Re(s)>0`. Harmonic centering has
therefore isolated a concrete weighted Chowla component; it has not made
the Möbius difficulty disappear.

Finally, let `D_H` be the aligned dyadic intervals in the integer-height
grid `(H,2H]`. Define

\[
 \mathcal E_D(I)=
 \sum_{\substack{d\le D\\d\ {\rm squarefree},\ 67\nmid d}}
 {\lvert\mathcal P_I(d)\rvert^2\over d}.
\tag{0.13}
\]

The exact dyadic chaining inequality is

\[
\boxed{
 \sum_{\substack{d\le D\\d\ {\rm squarefree},\ 67\nmid d}}{1\over d}
 \sup_{H\le U\le2H}
 |\mathcal P(d;H,U)|^2
 \le
 \lceil\log_2(N_H+1)\rceil
 \sum_{I\in\mathscr D_H}\mathcal E_D(I),}
\tag{0.14}
\]

where `N_H` is the number of integer heights in `(H,2H]`.

This supplies a nonmaximal named gate:

\[
\boxed{
 \mathrm{PRIMCAR}:\qquad
 \sum_{I\in\mathscr D_H}\mathcal E_D(I)
 \ll_\varepsilon(2DH)^\varepsilon}
\tag{0.15}
\]

uniformly for `D,H >= 1` and the three channels in (0.1). Then

\[
\boxed{
 \mathrm{PRIMCAR}\Longrightarrow
 \mathrm{PRIMLS}\Longrightarrow\mathrm{RH}.}
\tag{0.16}
\]

No estimate in (0.15) is proved. Its value is structural: it states one
precise averaged Chowla/Carleson input that removes the maximal endpoint,
and (0.3) rewrites every term of that input as an explicit finite incidence
quadratic form.

## 1. Exact height layers and incidence strata

Fix one of the five oriented source channels, although only the three in
(0.1) are independently needed. Put

\[
 h_{\alpha,\gamma}(a,b)=
 \max(67^\alpha a,67^\gamma b).
\tag{1.1}
\]

For an integer height `t`, define

\[
\begin{aligned}
 A_t(d)
 :=\sum_{\substack{
 a,b\ {\rm squarefree},\ 67\nmid ab,\ (a,b)=1\\
 h_{\alpha,\gamma}(a,b)=t,\ (ab,d)=1}}
 {\mu(a)\mu(b)\over\sqrt{ab}}
 \mathcal R\!\left(
 \log{67^\alpha a\over67^\gamma b}
 \right).
\end{aligned}
\tag{1.2}
\]

For a finite height block `I`, set

\[
 \mathcal P_I(d)=\sum_{t\in I}A_t(d).
\tag{1.3}
\]

The original moving-endpoint panel is exactly

\[
 \mathcal P_{\alpha,\gamma}(d;H,U)
 =\sum_{H<t\le U}A_t(d).
\tag{1.4}
\]

Every pair in `(H,2H]` has `a,b <= 2H`. Since `a,b` are squarefree,
67-free, and coprime, their product is a divisor of

\[
 Q_H=\prod_{p\le2H\atop p\ne67}p.
\tag{1.5}
\]

Define the exact product-incidence stratum

\[
 W_{I,e}=
 \sum_{(a,b)\in I\atop ab=e}
 {\mu(a)\mu(b)\over\sqrt{ab}}
 \mathcal R\!\left(
 \log{67^\alpha a\over67^\gamma b}
 \right).
\tag{1.6}
\]

Then `(ab,d)=1` is precisely `(e,d)=1`, proving (0.2). Notice that
`Q_H` is a symbolic bookkeeping modulus. Neither the theorem nor the replay
enumerates all of its divisors at growing `H`.

## 2. The finite dual incidence Gram

Expand the square in (0.13), use (0.2), and interchange finite sums:

\[
\begin{aligned}
 \mathcal E_D(I)
 &=\sum_d{1\over d}
   \sum_{e,f}W_{I,e}\overline{W_{I,f}}
   1_{(d,e)=1}1_{(d,f)=1}\\
 &=\sum_{e,f}W_{I,e}\overline{W_{I,f}}
   \sum_{d}{1_{(d,[e,f])=1}\over d}.
\end{aligned}
\tag{2.1}
\]

The inner sum is exactly `K_D([e,f])`, proving (0.3). Similarly,

\[
 \sum_d{\mathcal P_I(d)\over d}
 =\sum_eW_{I,e}K_D(e).
\tag{2.2}
\]

The matrix

\[
 \bigl(K_D([e,f])\bigr)_{e,f\mid Q_H}
\tag{2.3}
\]

is positive semidefinite because it is the Gram matrix of the functions
`d -> 1_(d,e)=1` in the finite weighted space with weights `1/d`.
Positivity does not prove a small upper bound: the signs and correlations
inside the `W_(I,e)` remain load-bearing.

Equation (0.3) is the requested dual large-sieve form. An averaged Chowla
input sufficient for the maximal theorem can now be stated entirely as a
bound for a sum of these explicit quadratic forms; Section 5 gives the
precise statement.

## 3. The actual harmonic limit is the biased Boolean cube

Fix `H`, `I`, and hence `Q=Q_H`. For each `delta | Q`, the squarefree
integers with

\[
 (d,Q)=\delta,
 \qquad 67\nmid d,
\tag{3.1}
\]

are uniquely `d=delta*m`, where `m` is squarefree and `(m,67Q)=1`.
The standard squarefree harmonic estimate from the frozen source gives

\[
 \sum_{\substack{d\le D\\(d,Q)=\delta\\
 d\ {\rm squarefree},\ 67\nmid d}}{1\over d}
 ={C(67Q)\over\delta}\log D+O_Q(1),
\tag{3.2}
\]

where

\[
 C(M)={1\over\zeta(2)}
 \prod_{p\mid M}\left(1+{1\over p}\right)^{-1}.
\tag{3.3}
\]

Now

\[
 C(67Q)
 ={67\over68\zeta(2)}{1\over Z_Q}.
\tag{3.4}
\]

Since `P_I(d)` depends only on `(d,Q)`, multiply (3.2) by
`|P_I(delta)|^2`, sum over `delta | Q`, and use (3.4). This proves (0.5),
with an error `O_(H,I,R)(1)` before division by `log D`. The same argument
without the square proves

\[
 {1\over\log D}
 \sum_{\substack{d\le D\\d\ {\rm squarefree},\ 67\nmid d}}
 {\mathcal P_I(d)\over d}
 \longrightarrow
 {67\over68\zeta(2)}B_I.
\tag{3.5}
\]

The limit is fixed-height. The `O_Q(1)` in (3.2) is not claimed uniform as
`H`, and therefore the primorial `Q_H`, grows. This is the decisive reason
that (0.5) does not prove PRIMLS.

## 4. Exact zero-mode extraction and its Euler factor

Under `nu_Q`, the prime indicators `1_(p|delta)` are independent with

\[
 \Pr(p\mid\delta)={1\over p+1},
 \qquad
 \Pr(p\nmid\delta)={p\over p+1}.
\tag{4.1}
\]

Therefore

\[
 \mathbb E_{\nu_Q}1_{(\delta,e)=1}
 =\prod_{p\mid e}{p\over p+1}=\rho(e).
\tag{4.2}
\]

Substitution into (0.2), followed by `e=ab` and the coprimality of `a,b`,
proves (0.7). The biased-Boolean Parseval formula in the source packet then
gives

\[
 \mathbb E_{\nu_Q}|\mathcal P_I|^2
 =|B_I|^2+
 \sum_{1\ne S\mid Q}{|b_{I,S}|^2\over N_S}.
\tag{4.3}
\]

Here the entire spectrum has a direct pair-sum form. Put

\[
 C_{I,S}=
 \sum_{e:\,S\mid e}W_{I,e}\rho(e/S),
 \qquad
 N_S=\prod_{p\mid S}{p\over(p+1)^2}.
\tag{4.4}
\]

The exact coefficient formula from the Boolean transform is

\[
 b_{I,S}=(-1)^{\omega(S)}N_SC_{I,S}.
\tag{4.5}
\]

Consequently,

\[
\boxed{
 \mathbb E_{\nu_Q}|\mathcal P_I|^2
 =\sum_{S\mid Q}N_S|C_{I,S}|^2,}
 \qquad C_{I,1}=B_I.
\tag{4.6}
\]

Thus every nonzero limiting mode is a divisibility-conditioned,
rho-tilted Möbius pair sum. This is more specific than asking vaguely for
"sieve cancellation": it identifies the complete fixed-block family of
Chowla-type quantities and their exact weights.

Thus the two exact analytic burdens at fixed block are:

1. the rho-tilted Möbius pair `B_I`;
2. the collective nonzero incidence spectrum in (4.3).

The first burden still has a reciprocal-zeta Euler factor. For `Re(s)>1`,
absolute convergence gives

\[
\begin{aligned}
 M_\rho^{(67)}(s)
 &:=\sum_{(n,67)=1}{\mu(n)\rho(n)\over n^s}\\
 &=\prod_{p\ne67}\left(1-{p\over p+1}p^{-s}\right).
\end{aligned}
\tag{4.7}
\]

Factor out the ordinary Möbius Euler product away from `67` to obtain
(0.11)--(0.12). For `sigma=Re(s)>0`,

\[
 {1-\rho(p)p^{-s}\over1-p^{-s}}-1
 ={p^{-s}\over(p+1)(1-p^{-s})}
 =O_\sigma(p^{-1-\sigma}).
\tag{4.8}
\]

The sum over primes converges. Each local numerator and denominator is
nonzero in that half-plane, so the product `G_rho` converges absolutely and
is nonzero there.

This proves a sharp firewall. Subtracting `B_I` is an exact zero-mode
projection for the limiting incidence measure, but it changes the
observable. Controlling the original panel still requires a theorem for
`B_I`, whose Euler product retains `1/zeta(s)`.

## 5. Dyadic endpoint removal and the PRIMCAR gate

List the integer heights in `(H,2H]` as

\[
 t_1<t_2<\cdots<t_{N_H}.
\tag{5.1}
\]

Let `D_H` contain all aligned dyadic subintervals of the index set
`{1,...,N_H}`. Every prefix `{1,...,m}` is a disjoint union of at most

\[
 L_H=\lceil\log_2(N_H+1)\rceil
\tag{5.2}
\]

members of `D_H`. Hence, for each admissible sieve `d`, Cauchy--Schwarz
gives

\[
 \sup_m\left|\sum_{j\le m}A_{t_j}(d)\right|^2
 \le L_H\sum_{I\in\mathscr D_H}|\mathcal P_I(d)|^2.
\tag{5.3}
\]

Multiplying by `1/d` and summing proves (0.14).

Assume PRIMCAR in the form (0.15), uniformly for all `D,H` and the three
independent channels. Since `N_H <= H+1`, the factor `L_H` is logarithmic
and is absorbed by an arbitrarily small change of epsilon. Equation (0.14)
then proves PRIMLS. The frozen source theorem proves

\[
 \mathrm{PRIMLS}\Longrightarrow\mathrm{RH},
\tag{5.4}
\]

so (0.16) follows.

PRIMCAR is stronger than the needed maximal estimate and is not claimed
equivalent to RH. It is useful because it has no endpoint supremum, and
every summand has the exact dual form (0.3). In expanded form, the requested
conditional input is precisely

\[
 \sum_{I\in\mathscr D_H}
 \sum_{e,f\mid Q_H}
 W_{I,e}\overline{W_{I,f}}K_D([e,f])
 \ll_\varepsilon(2DH)^\varepsilon.
\tag{5.5}
\]

This is a dyadic, product-incidence, harmonically averaged two-point Chowla
gate. Proving only its limiting zero-mode estimate, only the nonzero Boolean
modes at fixed `H`, or only a pointwise fixed-shift Chowla estimate would
not by itself prove (5.5).

## 6. What this changes and what remains open

The packet makes four exact advances over the primitive-pair source:

1. it gives the actual truncated `d` average a finite dual Gram matrix;
2. it proves that the source's biased Boolean cube is the fixed-height
   harmonic limit of that actual average;
3. it identifies the zero mode as a rho-tilted Möbius pair and factors its
   one-variable Euler series;
4. it replaces the moving endpoint by a precise nonmaximal Carleson gate.

It does **not** supply any of the estimates needed to close PRIMCAR. The
most promising analytic division is now explicit:

\[
 \text{rho-tilted zero mode}
 \quad+\quad
 \text{nonzero incidence spectrum}
 \quad+\quad
 \text{dyadic block summability}.
\tag{6.1}
\]

A future proof could attack these through bilinear Möbius estimates,
dispersion, a two-dimensional large sieve, or a source-faithful amplifier.
The fixed-height limit warns that abstract sieve orthogonality cannot remove
the first term.

## 7. Proof and scope ledger

| statement | grade |
|---|---|
| exact height-layer/product-incidence decomposition (0.2) | **PROVED EXACT** |
| finite linear and quadratic dual Gram identities (0.3), (2.2) | **PROVED EXACT** |
| fixed-height actual harmonic limit (0.5), (3.5) | **PROVED EXACT FROM STANDARD SQUAREFREE HARMONIC SUMMATION** |
| rho-tilted zero mode, centering, and derivative spectrum (0.7)--(0.10), (4.4)--(4.6) | **PROVED EXACT** |
| rho Euler factor and convergent correction (0.11)--(0.12) | **PROVED FOR THE STATED HALF-PLANES** |
| dyadic maximal reduction (0.14) | **PROVED EXACT** |
| PRIMCAR implies PRIMLS implies RH | **PROVED AS A CONDITIONAL IMPLICATION** |
| uniform PRIMCAR estimate (0.15) | **OPEN / NOT PROVED** |
| uniformity of the fixed-height `O_Q(1)` error as `H` grows | **NOT CLAIMED** |
| PRIMCAR equivalent to RH | **NOT CLAIMED** |
| PRIMLS, RH, or GRH | **NOT PROVED** |

No external novelty claim is made.

## 8. Bounded replay

```text
python -B research/l-families/atlas/function_field/ffps_primitive_pair_harmonic_incidence_carleson.py --check
python -B -O research/l-families/atlas/function_field/ffps_primitive_pair_harmonic_incidence_carleson.py --check
python -B -m unittest tests.test_ffps_primitive_pair_harmonic_incidence_carleson
python -B -O -m unittest tests.test_ffps_primitive_pair_harmonic_incidence_carleson
```

The replay pins the complete predecessor packet; partitions one exact
primitive shell into integer-height layers; verifies the finite linear and
quadratic incidence Gram identities in the source packet's exact radical
basis; checks every prefix decomposition on a four-layer grid; verifies the
rho-tilted harmonic mean and the limiting incidence-mass normalization on
the divisor cube of `210`; checks the local Euler correction; and enforces
the conditional scope and resource caps. It enumerates no zeta zero,
finite-field family, curve, conductor family, or `L`-function.
