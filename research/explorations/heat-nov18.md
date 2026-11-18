# First-Hermite positivity throughout a verified-height window

**Status.** Proposed lemma for independent review. Every heat parameter is covered throughout the stated finite interval of centers. The unbounded-center complement remains open.

## Statement

Write each nontrivial zero of zeta as $\rho=\beta+it$ and put $z=(\rho-1/2)/i=t+ia$, so $|a|\le1/2$. Count multiplicities once in each sum. For $q>0$ let
\[
 M(q,x)=\sum_\rho(z-x)^2 e^{-q(z-x)^2}.
\]
Then for **every** $|x|\le 10^{12}$ and **every** $q>0$,
\[
 M(q,x)>0.
\]
We use the imported Platt–Trudgian verified height $H=3\cdot10^{12}$ and one classical verified zero with ordinate $14<t_0<15$. Absolute convergence and reality follow from the classical zero count and the symmetry $\rho\mapsto1-\bar\rho$.

## The sign restriction for a single summand

Write $v=t-x$, $w=v+ia$. The real part of the summand is
\[
 e^{-q(v^2-a^2)}\big[(v^2-a^2)\cos(2qva)+2va\sin(2qva)\big].
\]
Whenever $|v|\ge1$ and $q|v|\le1$, both bracketed contributions are nonnegative. Indeed $|2qva|\le1$ and the sine has the sign of $va$. Thus a negative contribution with $|v|\ge1$ must have $q|v|>1$. This sign information makes the exterior tail estimate uniform down to arbitrarily small $q$.

## An absolute tail budget

The classical Hadamard identity for the completed $\xi$ function gives
\[
\sum_\rho \Re(1/\rho)=1+\gamma_E/2-\tfrac12\log(4\pi).
\]
The real-part sum converges absolutely by the zero count. The identity also follows by logarithmically differentiating the genus-one product at 0 and 1, using $\xi(s)=\xi(1-s)$ and the Laurent expansion at 1. Since $\beta/(1+t^2)\le \Re(1/\rho)$, reflection in the critical line gives
\[
\sum_\rho (1+t^2)^{-1}
=2\sum_\rho \beta/(1+t^2)
\le 2+\gamma_E-\log(4\pi)<1.
\]

Choose the real zero of ordinate $t_0$ or $-t_0$ opposite in sign to $x$ (either at $x=0$), and let $d=|x|+t_0$. This one summand contributes $d^2 e^{-qd^2}$. All other zeros with $|t|\le H$ have real $z$ and contribute nonnegatively.

For $|t|>H$ put $u=|v|$. Then $u>2\cdot10^{12}$, $|t|\le3u/2$, and $d\le10^{12}+15$. In particular $u^2-a^2-d^2\ge u^2/2$. For any negative real contribution from this range the sign restriction gives
\[
 |w^2e^{-qw^2}| e^{qd^2}
 \le (u^2+1/4)e^{-qu^2/2}
 \le (u^2+1/4)e^{-u/2}
 <(1+t^2)^{-1}.
\]
For the last inequality, $(1+t^2)(u^2+1/4)\le 8u^4$ for $u\ge1$ and $8u^4 e^{-u/2}<1$ for $u\ge100$ by monotonicity. Summing the exterior negative real contributions therefore costs less than $e^{-qd^2}$. Consequently $M(q,x)\ge (d^2-1)e^{-qd^2}>0$ throughout the claimed domain.

## Scope and dependencies

The result supplies a complement estimate for the local zero census. The exponential lower bound is deliberately weak at large heat parameter. The proof loses coverage when the available real anchor is too far from the center relative to the uncertified zeros. It gives no cofinal zero census.

The criterion and normalization are from PR #379, commit 589f1c05ccaf248cf08c87fefa7d5ab6d2380708, and [the integrated First-Hermite packet](../integrated/heat_hermite/FIRST_HERMITE_REGIONS.md). The height theorem is external. Its citation and exact imported bound appear in [the repository's source lock](../../formal/registry/deltas/C_EXTERNAL_SOURCE_STATEMENTS/EXT.XI.PLATT_TRUDGIAN.2021.txt). For the low zero bracket, see [DLMF §25.10](https://dlmf.nist.gov/25.10). No zero verification computation was rerun.

## Fixed-radius localization at unbounded centers

There are absolute constants $R,X$ such that for $|x|\ge X$, if every zero with $|t-x|\le R$ is on the critical line, then $M(q,x)>0$ for every $q>0$. In particular every negative witness with sufficiently large center is within the same fixed radius of an off-line zero. No hypothesis about the exterior zeros is imposed.

By evenness take $x>0$. The Riemann–von Mangoldt formula in its classical $O(\log T)$ remainder form gives two facts. First, each unit interval $[T,T+1]$ has $O(\log(2+|T|))$ ordinates counted with multiplicity. Second, for some fixed integer $D>2$ and all sufficiently large $x$, the interval $(x+1,x+D]$ contains a zero. For the latter statement take the difference of the main terms at the endpoints. Its leading coefficient of $\log x$ is $(D-1)/(2\pi)$, which can be made larger than twice an absolute remainder constant. Fix that $D$ and choose an integer $R>2D+4$.

Local reality now supplies one positive summand at distance $1<d\le D$ worth at least $e^{-qD^2}$. All other terms at distance at most $R$ are nonnegative. For $q\ge1$, divide the absolute exterior tail by $e^{-qD^2}$ and use the unit-interval counts in the shells $k\le|t-x|<k+1$. Its upper bound is
\[
 C\sum_{k\ge R}(k+2)^2\log(2+x+k)
 e^{-q(k^2-1/4-D^2)}
 \le C_R\log(2+x)e^{-q(R^2-1/4-D^2)}.
\]
Indeed $q(k^2-R^2)\ge k^2-R^2$ and $\log(2+x+k)\le\log(2+x)+\log(1+k)$. The residual series converges absolutely. When $q\ge3\log\log(2+x)$ the last display tends uniformly to zero, since $3(R^2-1/4-D^2)>1$. The tail is eventually smaller than the anchor. For $0<q\le3\log\log(2+x)$ use the integrated growing-wedge theorem with $\epsilon=1$. This proves the localization assertion.

The new implication requires a local census about the actual zeros. It does not show that the hypothesis holds around every large center. Its quantifier over $R$ is existential because the proof uses an unspecified absolute constant in the classical counting remainder.
