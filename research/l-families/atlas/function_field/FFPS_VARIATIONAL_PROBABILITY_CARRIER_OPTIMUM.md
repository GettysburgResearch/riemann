# The unique minimum-diagonal probability carrier is parabolic

Status: **exact variational optimum, exact autocorrelation sign geometry,
exact side-notch lattice, and an RH-equivalent minimum-diagonal beta
detector; no beta-energy estimate, proof of RH, or GRH result**

Bounded replay:
[ffps_variational_probability_carrier_optimum.py](ffps_variational_probability_carrier_optimum.py).
Canonical summary:
[ffps_variational_probability_carrier_optimum.json](ffps_variational_probability_carrier_optimum.json).

Frozen source: the uniform moving-probability-carrier theorem at commit
**52577ce7fb5840a93102b4808c87b1b2d6e8c304**. The producer pins all four
Git blobs and imports no live predecessor module.

## 0. Outcome

Fix a causal support length \(S>0\). Among all

\[
 Q\in H_0^1(0,S),\qquad Q\ge0,\qquad
 \int_0^S Q(x)\,dx=1,
\tag{0.1}
\]

there is a unique density which minimizes the detector diagonal

\[
 \|DQ\|_2^2.
\tag{0.2}
\]

It is the scaled Beta\((2,2)\) density

\[
\boxed{
 Q_*(x)={6x(S-x)\over S^3}\mathbf1_{[0,S]}(x).}
\tag{0.3}
\]

Its derivative detector is

\[
\boxed{
 J_*(x)={6(S-2x)\over S^3}\mathbf1_{(0,S)}(x),}
\tag{0.4}
\]

and the sharp minimum is

\[
\boxed{
 \|J_*\|_2^2={12\over S^3}.}
\tag{0.5}
\]

More strongly, every admissible \(Q\) satisfies the exact Pythagorean
identity

\[
\boxed{
 \|DQ\|_2^2
 ={12\over S^3}
 +\|D(Q-Q_*)\|_2^2.}
\tag{0.6}
\]

The autocorrelation is an explicit compact cubic:

\[
\boxed{
 \mathcal R_*(u)
 =
 {12\over S^3}
 -{36|u|\over S^4}
 +{24|u|^3\over S^6},
 \qquad |u|\le S,}
\tag{0.7}
\]

and vanishes outside that interval. Its primitive nonzero node is

\[
\boxed{
 {|u|\over S}={\sqrt3-1\over2}.}
\tag{0.8}
\]

Thus even the unique minimum-diagonal detector has a positive central
tube and a negative outer annulus.

The Fourier transform has infinitely many real side notches:

\[
\boxed{
 \tan\left({St\over2}\right)={St\over2}.}
\tag{0.9}
\]

Nevertheless, the frozen universal theorem proves

\[
\boxed{
 \mathrm{RH}
 \Longleftrightarrow
 \mathcal E_{J_*}(X)=X^{o(1)}.}
\tag{0.10}
\]

This is an exact design lesson. Removing every real side notch is not
necessary for a prefix-energy RH criterion. Positivity and normalization
of the primitive \(Q_*\), not pointwise nonvanishing of its Fourier
transform, supply the load-bearing real Laplace carrier.

No estimate in (0.10) is proved here.

## 1. The variational proof

The admissible set in (0.1) is convex. Ignore the positivity constraint
temporarily and minimize

\[
 \mathscr D(Q)=\int_0^S|Q'(x)|^2\,dx
\tag{1.1}
\]

under the affine mass constraint. The Euler--Lagrange equation is

\[
 -Q''=\lambda,
\qquad Q(0)=Q(S)=0.
\tag{1.2}
\]

Therefore

\[
 Q(x)={\lambda\over2}x(S-x).
\tag{1.3}
\]

The mass condition gives

\[
 1={\lambda\over2}\int_0^Sx(S-x)\,dx
 ={\lambda S^3\over12},
\tag{1.4}
\]

so \(\lambda=12/S^3\), proving (0.3). The solution is nonnegative, so
the ignored inequality is automatically satisfied.

For a proof which also yields sharp uniqueness, write

\[
 Q=Q_*+h,
\qquad h\in H_0^1(0,S),
\qquad \int_0^S h=0.
\tag{1.5}
\]

Since

\[
 Q_*''=-{12\over S^3},
\tag{1.6}
\]

integration by parts gives

\[
 \int_0^S Q_*'(x)h'(x)\,dx
 =-\int_0^S Q_*''(x)h(x)\,dx
 ={12\over S^3}\int_0^S h(x)\,dx
 =0.
\tag{1.7}
\]

Expanding \(\|Q_*'+h'\|_2^2\) proves (0.6). Equality forces \(h'=0\);
the zero boundary trace then forces \(h=0\). The minimizer is unique.

The bounded replay uses the explicit zero-mass perturbation

\[
 h_c(x)=c\,x(S-x)(x-S/2),
\qquad
 \|Dh_c\|_2^2={c^2S^5\over20},
\tag{1.7a}
\]

as a formula control for the strict excess term.

Finally,

\[
 \|Q_*'\|_2^2
 ={36\over S^6}\int_0^S(S-2x)^2\,dx
 ={12\over S^3},
\tag{1.8}
\]

which verifies the sharp value directly.

## 2. Ratio-band Pareto frontier

If \(J\) is supported on \([0,S]\), then its autocorrelation is supported
on \([-S,S]\). In the beta Gram form, only pairs satisfying

\[
 e^{-S}\le {m\over n}\le e^S
\tag{2.1}
\]

can interact. Put

\[
 R=e^S.
\tag{2.2}
\]

For a prescribed multiplicative ratio band \(R\), (0.5) becomes the
exact lower frontier

\[
\boxed{
 \inf_Q\|DQ\|_2^2
 ={12\over(\log R)^3}.}
\tag{2.3}
\]

This is a genuine detector-design tradeoff:

- increasing \(S\) lowers the unavoidable diagonal as \(S^{-3}\);
- the same change widens the primitive-pair interaction band
  exponentially to \(e^S\);
- no positive normalized \(H_0^1\) carrier can improve one side while
  holding the other fixed.

For the project's ratio-\(16\) band,

\[
 S=\log16=4\log2,
\qquad
 \|J_*\|_2^2={12\over(4\log2)^3}.
\tag{2.4}
\]

Choosing \(R<67\) excludes the literal same-core ratio-\(67\) collision
between the duplicate-\(67\) exceptional orientations. The replay
includes \(R=64\) as the widest integer benchmark below that threshold;
it does not claim to remove every exceptional-channel interaction.

This theorem minimizes the kernel's diagonal factor. It does not claim
that the full signed beta energy is minimized, because off-diagonal
arithmetic correlations also change with \(S\) and with the shape of
\(\mathcal R\).

For every fixed carrier, the arithmetic diagonal itself is only
logarithmic and is already \(X^{o(1)}\). Minimizing its coefficient
therefore does not weaken the asymptotic RH burden. The gain is an exact
conditioning and inverse-design optimum, not an unconditional
cancellation estimate.

## 3. Exact autocorrelation and sign geometry

For \(u\ge0\), the overlap of the two supports is \([0,S-u]\). Direct
integration gives

\[
\begin{aligned}
 \mathcal R_*(u)
 &=
 {36\over S^6}
 \int_0^{S-u}
 (S-2x)(S-2x-2u)\,dx\\
 &=
 {36\over S^6}
 \left({S^3\over3}-S^2u+{2u^3\over3}\right).
\end{aligned}
\tag{3.1}
\]

Evenness proves (0.7). With \(r=|u|/S\), the sign polynomial is

\[
 1-3r+2r^3
 =(r-1)(2r^2+2r-1).
\tag{3.2}
\]

Its roots in \([0,1]\) are

\[
 r={\sqrt3-1\over2},
 \qquad r=1.
\tag{3.3}
\]

Therefore

\[
\begin{array}{c|c}
0\le |u|<S(\sqrt3-1)/2&\mathcal R_*(u)>0\\
S(\sqrt3-1)/2<|u|<S&\mathcal R_*(u)<0.
\end{array}
\tag{3.4}
\]

Because \(\int J_*=0\),

\[
 \int_{-S}^S\mathcal R_*(u)\,du=0.
\tag{3.5}
\]

The negative annulus is therefore not a defect of a poor carrier. It is
the exact cancellation partner forced even at the minimum diagonal.

In the beta energy,

\[
 \mathcal E_{J_*}(X)
 =
 \sum_{m,n\le X}
 {\beta(m)\beta(n)\over\sqrt{mn}}
 \mathcal R_*\!\left(\log{m\over n}\right).
\tag{3.6}
\]

The diagonal part is explicit and positive. Closing (0.10) still
requires cancellation across the signed primitive-pair annulus.

## 4. Fourier transform and the notch lattice

Scale \(x=Sy\). The probability transform is

\[
\begin{aligned}
 \widehat Q_*(it)
 &=
 6\int_0^1y(1-y)e^{-iSty}\,dy\\
 &=
 12e^{-iSt/2}
 {2\sin(St/2)-St\cos(St/2)\over(St)^3}.
\end{aligned}
\tag{4.1}
\]

The value at \(t=0\) is filled continuously and equals one. Thus

\[
\boxed{
 |\widehat J_*(it)|^2
 =
 144t^2
 {[
 2\sin(St/2)-St\cos(St/2)
 ]^2\over(St)^6}.}
\tag{4.2}
\]

Besides the forced derivative zero at \(t=0\), the nonzero real notches
satisfy

\[
 2\sin(St/2)-St\cos(St/2)=0,
\tag{4.3}
\]

which is (0.9). If \(u_k\) is the positive root of

\[
 \tan u=u
\tag{4.4}
\]

in \((k\pi,(k+1/2)\pi)\), then the detector notch is

\[
 t_k={2u_k\over S}.
\tag{4.5}
\]

The first three \(u_k\) are replayed by bounded bisection. They are
formula checks, not evidence for the theorem.

The side notches would obstruct a naïve pointwise attempt to dominate
another positive spectral weight. They do not obstruct the prefix-energy
criterion. The frozen theorem instead evaluates the kernel at a fixed
positive real Laplace point:

\[
 \widehat J_*(\alpha)
 =\alpha\int_0^SQ_*(x)e^{-\alpha x}\,dx
 \ge\alpha e^{-\alpha S}.
\tag{4.6}
\]

This is another sharp distinction between a **spectral-comparison
firewall** and an **RH-equivalence firewall**.

## 5. RH equivalence

The density \(Q_*\) is nonnegative, normalized, compactly supported, and
belongs to \(H_0^1(0,S)\). Its zero-extended distributional derivative
is the ordinary compact \(L^2\cap BV\) function (0.4). All hypotheses of
the frozen universal theorem therefore hold.

The reverse implication follows from the exact finite-prefix chain

\[
 \mathcal E_{J_*}(X)=X^{o(1)}
 \Longrightarrow
 \sum_{n\le X}{\beta(n)\over n^{1/2+\alpha}}
 =X^{o(1)}
 \Longrightarrow
 {1-67^{-(s+1/2)}\over\zeta(s+1/2)}
 \text{ is holomorphic for }\Re s>0.
\tag{5.1}
\]

The last statement excludes every right-of-line zeta zero; the
functional equation excludes the reflected half.

Under RH, the fixed BV kernel \(J_*\) and the classical Mertens bound give

\[
 \mathcal E_{J_*}(X)=X^{o(1)}.
\tag{5.2}
\]

Together these prove (0.10).

The new contribution is not another equivalent criterion chosen at
random. It is the unique criterion selected by a natural inverse-design
problem: minimize the unavoidable diagonal under exact positivity,
normalization, support, and endpoint gates.

### Exact two-channel local form

The variational kernel is linear on its support. Define the local beta
mass and its first logarithmic lag moment by

\[
\begin{aligned}
 A_S(t;X)
 &=
 \sum_{\substack{n\le X\\t-S<\log n<t}}
 {\beta(n)\over\sqrt n},\\
 B_S(t;X)
 &=
 \sum_{\substack{n\le X\\t-S<\log n<t}}
 {\beta(n)\over\sqrt n}(t-\log n).
\end{aligned}
\tag{5.3}
\]

Endpoint conventions affect only a null set in the energy integral.
Substitution of (0.4) gives the exact field identity

\[
\boxed{
 H_{*;X}(t)
 ={6\over S^3}
 \left[
 S A_S(t;X)-2B_S(t;X)
 \right].}
\tag{5.4}
\]

Consequently,

\[
\boxed{
 \mathrm{RH}
 \Longleftrightarrow
 \int_{\mathbb R}
 |SA_S(t;X)-2B_S(t;X)|^2\,dt
 =X^{o(1)}.}
\tag{5.5}
\]

Thus the variational detector is a concrete two-channel multiplicative
short-window target: local beta mass interferes with one logarithmic
moment. No divisor orientation, Fourier integral, or auxiliary kernel
remains hidden in (5.5). This is still an equivalent target, not an
estimate of either channel.

## 6. Scope and interpretation

| statement | grade |
|---|---|
| unique minimizer (0.3) and Pythagorean identity (0.6) | **PROVED EXACT** |
| diagonal/ratio-band frontier (2.3) | **PROVED EXACT** |
| autocorrelation and annular sign law | **PROVED EXACT** |
| complete real side-notch lattice | **PROVED EXACT** |
| RH equivalence of the variational detector | **PROVED FROM THE FROZEN UNIVERSAL GATE** |
| beta-energy estimate for the detector | **NOT PROVED** |
| RH or GRH | **NOT PROVED** |

Three conclusions should be carried forward:

1. detector diagonal can be optimized exactly before any arithmetic
   estimate is attempted;
2. negative Gram annuli and Fourier side notches can coexist with a
   completely valid RH criterion;
3. proving the criterion still means controlling signed near-diagonal
   Möbius correlations, not merely reducing the diagonal.

No external novelty or priority is claimed without a dedicated
literature comparison.

## 7. Bounded replay

The producer:

- pins the complete frozen universal-carrier quartet;
- evaluates three support/ratio-band rows;
- evaluates the exact cubic autocorrelation at bounded points;
- isolates three roots of \(\tan u=u\) with 80 bisection steps each;
- performs no quadrature, beta sum, zeta evaluation, prime enumeration,
  finite-field enumeration, or random sampling.

~~~text
python -B research/l-families/atlas/function_field/ffps_variational_probability_carrier_optimum.py --check
python -O -B research/l-families/atlas/function_field/ffps_variational_probability_carrier_optimum.py --check
python -B -m unittest tests.test_ffps_variational_probability_carrier_optimum
python -O -B -m unittest tests.test_ffps_variational_probability_carrier_optimum
python -m ruff check research/l-families/atlas/function_field/ffps_variational_probability_carrier_optimum.py tests/test_ffps_variational_probability_carrier_optimum.py
python -m ruff format --check research/l-families/atlas/function_field/ffps_variational_probability_carrier_optimum.py tests/test_ffps_variational_probability_carrier_optimum.py
~~~
