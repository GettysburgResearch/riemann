# First-Hermite zero-heat monotonicity: a two-parameter reality criterion and finite linear witnesses

**Status:** `PROPOSED COMPLETE ABSTRACT / EXPLICIT-FORMULA THEOREM — INDEPENDENT REVIEW REQUIRED`  
**RH status:** **unproved**  
**Continuation of:** PR #375 terminal Gaussian heat residues; PR #367 completed-Chebyshev scalar  
**External input:** the centered Guinand--Weil normalization used in Anthropic Zeta23  

## 1. Executive statement

Let `Z` be a conjugation-invariant locally finite multiset in a bounded horizontal strip, with subquadratic counting growth. Define

\[
 \mathcal M_Z(q,x)
 =\sum_{z\in Z}m_z(z-x)^2e^{-q(z-x)^2},
 \qquad q>0,\ x\in\mathbb R.
 \tag{ZH.1}
\]

The first theorem of this note is the abstract equivalence

\[
 \boxed{
 Z\subset\mathbb R
 \quad\Longleftrightarrow\quad
 \mathcal M_Z(q,x)\ge0
 \quad(q>0,\ x\in\mathbb R).
 }
 \tag{ZH.2}
\]

If `Z` is not real, a terminal conjugate pair `t_0 +/- i y_0` satisfies the sharper asymptotic

\[
 \boxed{
 {\mathcal M_Z(q,t_0)\over
  2y_0^2e^{qy_0^2}}
 \longrightarrow -m_0.
 }
 \tag{ZH.3}
\]

For the centered zeta-zero multiset

\[
 \gamma_\rho={\rho-1/2\over i},
 \tag{ZH.4}
\]

this gives a two-parameter RH criterion. It is the confluent, first-Hermite limit of PR #375's three-Gaussian terminal kernel. The corresponding Guinand--Weil test is explicit, Schwartz, and has a superconvergent all-prime formula. False RH would therefore yield a finite, directed, **linear** prime-power certificate in this family.

Nothing below proves the prime-side inequality in `(ZH.2)`. That inequality is RH-equivalent.

## 2. Abstract setting and convergence

Let `0<a<infinity`. Let `Z` be a multiset in

\[
 \{z\in\mathbb C:|\Im z|<a\}
\]

with multiplicities `m_z in N`, invariant under conjugation, and suppose

\[
 N_Z(R):=\sum_{|\Re z|\le R}m_z=o(R^2)
 \qquad(R\to\infty).
 \tag{ZH.5}
\]

In particular every bounded real-ordinate interval contains only finitely many points, including multiplicity.

For fixed `q>0` and `x in R`,

\[
 |(z-x)^2e^{-q(z-x)^2}|
 \le C_{q,a,x}(1+|\Re z|^2)e^{-q(\Re z-x)^2}.
 \tag{ZH.6}
\]

Partial summation against `(ZH.5)` proves absolute and locally uniform convergence of `(ZH.1)`. Conjugation invariance makes `M_Z(q,x)` real.

## 3. The parabolic threat graph

Let

\[
 Z_+=\{t+iy\in Z:y>0\},
\]

one coordinate from each conjugate pair. For distinct vertices

\[
 z=t+iy,
 \qquad
 w=u+id,
\]

define a directed threat edge

\[
 \boxed{
 z\longrightarrow w
 \quad\Longleftrightarrow\quad
 d^2-(u-t)^2\ge y^2.
 }
 \tag{ZH.7}
\]

Every edge strictly increases depth. Indeed `(ZH.7)` gives `d>=y`; equality would force `u=t`, hence the same point. Moreover

\[
 \boxed{
 (u-t)^2\le d^2-y^2.
 }
 \tag{ZH.8}
\]

### Theorem 3.1 — a terminal nonreal pair exists

If `Z_+` is nonempty, it has a vertex with no outgoing threat edge.

### Proof

Assume every vertex has an outgoing edge and recursively choose

\[
 z_n=t_n+iy_n\longrightarrow z_{n+1}=t_{n+1}+iy_{n+1}.
\]

The depths increase strictly and remain below `a`. By `(ZH.8)`,

\[
 \sum_{n=0}^{N-1}(t_{n+1}-t_n)^2
 \le y_N^2-y_0^2<a^2.
 \tag{ZH.9}
\]

Cauchy--Schwarz gives

\[
 |t_N-t_0|<a\sqrt N.
 \tag{ZH.10}
\]

Thus the first `N+1` distinct vertices lie in

\[
 |\Re z-t_0|<a\sqrt N.
\]

But `(ZH.5)` permits only `o(N)` points there, contradicting the chain. `square`

The theorem needs no zero separation and no maximal-depth zero. Its load-bearing hypothesis is only subquadratic horizontal counting.

## 4. Terminal isolation by one first-Hermite Gaussian

Fix a terminal vertex

\[
 z_0=t_0+iy_0,
 \qquad y_0>0,
\]

of multiplicity `m_0`.

The target conjugate pair contributes exactly

\[
 \begin{aligned}
 &(iy_0)^2e^{-q(iy_0)^2}
 +(-iy_0)^2e^{-q(-iy_0)^2}\\
 &\hspace{28mm}=
 \boxed{-2y_0^2e^{qy_0^2}}.
 \end{aligned}
 \tag{ZH.11}
\]

A real point `r+t_0` contributes

\[
 r^2e^{-qr^2},
 \tag{ZH.12}
\]

whose ratio to `y_0^2e^{qy_0^2}` tends to zero.

For a nuisance conjugate pair

\[
 t_0+r\pm id,
\]

the absolute contribution is at most

\[
 \boxed{
 2(r^2+d^2)e^{q(d^2-r^2)}.
 }
 \tag{ZH.13}
\]

Terminality says, for every nuisance pair,

\[
 \Phi_{z_0}(r,d)
 :=d^2-r^2-y_0^2<0.
 \tag{ZH.14}
\]

On every bounded ordinate interval there are finitely many nuisances, so their largest exponent in `(ZH.14)` is strictly negative. For `|r|` large,

\[
 \Phi_{z_0}(r,d)
 \le a^2-y_0^2-r^2
 \le-{r^2\over2}
 \tag{ZH.15}
\]

once the cutoff is fixed sufficiently far out. The count `(ZH.5)` makes the resulting Gaussian majorant summable. Dominated convergence now gives

\[
 \sum_{\text{all nuisances}}
 {\text{absolute contribution}\over
  2y_0^2e^{qy_0^2}}
 \longrightarrow0.
 \tag{ZH.16}
\]

Combining `(ZH.11)` and `(ZH.16)` proves `(ZH.3)`.

### Theorem 4.1 — first-Hermite reality criterion

Under the hypotheses of Section 2,

\[
 \boxed{
 Z\subset\mathbb R
 \iff
 \mathcal M_Z(q,x)\ge0
 \quad\text{for every }q>0,\ x\in\mathbb R.
 }
 \tag{ZH.17}
\]

The forward implication is termwise. The reverse implication follows from `(ZH.3)`.

## 5. Zero-heat monotonicity and the odd-derivative hierarchy

Put

\[
 \mathcal H_Z(q,x)
 =\sum_{z\in Z}m_ze^{-q(z-x)^2}.
 \tag{ZH.18}
\]

Local-uniform convergence permits differentiation:

\[
 \boxed{
 -\partial_q\mathcal H_Z(q,x)=\mathcal M_Z(q,x).
 }
 \tag{ZH.19}
\]

Thus

\[
 \boxed{
 Z\subset\mathbb R
 \iff
 q\longmapsto\mathcal H_Z(q,x)
 \text{ is nonincreasing for every }x\in\mathbb R.
 }
 \tag{ZH.20}
\]

In heat time `tau=1/(4q)`, define

\[
 \mathcal Z_Z(\tau,x)
 =\sum_{z\in Z}m_z
 e^{-(z-x)^2/(4\tau)}.
 \tag{ZH.21}
\]

Then

\[
 \mathcal M_Z(q,x)=4\tau^2\partial_\tau\mathcal Z_Z(\tau,x),
 \tag{ZH.22}
\]

so reality is equivalent to monotone increase of the unnormalised zero heat trace in heat time.

More generally,

\[
 (-1)^k\partial_q^k\mathcal H_Z(q,x)
 =\sum_{z\in Z}m_z(z-x)^{2k}e^{-q(z-x)^2}.
 \tag{ZH.23}
\]

If `Z` is real, all these quantities are nonnegative. At a terminal target, the conjugate-pair contribution has sign `(-1)^k`; the same exponential isolation proves that **every odd `k` separately gives an equivalent reality criterion**. The case `k=1` is the minimal-degree member and already suffices.

## 6. Confluent limit of the PR #375 kernel

PR #375's normalized terminal residue contribution can be written

\[
 \mathcal W_{q,y}(z)
 =-2e^{q(z^2-y^2)}
 \left({\sinh(qyz)\over\sinh(qy^2)}\right)^2.
 \tag{ZH.24}
\]

For fixed `q,z`,

\[
 \boxed{
 \lim_{y\downarrow0}y^2\mathcal W_{q,y}(z)
 =-2z^2e^{qz^2}.
 }
 \tag{ZH.25}
\]

Thus the first-Hermite kernel is not an unrelated test family. It is the exact confluent limit of the pair-depth-adapted three-Gaussian kernel. The former target-dependent depth parameter disappears, while the terminal exponent becomes

\[
 d^2-r^2-y_0^2,
 \tag{ZH.26}
\]

which is precisely the threat relation `(ZH.7)`.

This section is a local continuation of PR #375, not part of the upstream Anthropic formalisation.

## 7. Zeta specialization

For a nontrivial zeta zero

\[
 \rho=\beta+i\gamma,
\]

put

\[
 \gamma_\rho={\rho-1/2\over i}
 =\gamma-i(\beta-1/2).
 \tag{ZH.27}
\]

The multiset is invariant under conjugation, lies in `|Im z|<1/2`, and the Riemann--von Mangoldt formula gives

\[
 N_Z(R)=O(R\log(2+R))=o(R^2).
 \tag{ZH.28}
\]

The abstract theorem therefore gives:

### Theorem 7.1 — zero-heat criterion for RH

\[
 \boxed{
 \mathrm{RH}
 \iff
 \sum_\rho m_\rho
 (\gamma_\rho-x)^2
 e^{-q(\gamma_\rho-x)^2}
 \ge0
 \quad(q>0,\ x\in\mathbb R).
 }
 \tag{ZH.29}
\]

Equivalently, the centered zeta-zero heat trace is nonincreasing in `q`, or increasing in heat time, at every real centre.

False RH forces a terminal pair `t_0 +/- i y_0` with

\[
 \boxed{
 {1\over2y_0^2e^{qy_0^2}}
 \sum_\rho m_\rho(\gamma_\rho-t_0)^2
 e^{-q(\gamma_\rho-t_0)^2}
 \longrightarrow-m_0.
 }
 \tag{ZH.30}
\]

## 8. Countable criterion

The false-RH asymptotic `(ZH.30)` is strictly negative for every sufficiently large `q`. Hence one may choose an integer `q=n`. For that fixed integer, continuity in `x` preserves strict negativity at a nearby rational centre.

Therefore

\[
 \boxed{
 \mathrm{RH}
 \iff
 \mathcal M_\zeta(n,r)\ge0
 \quad\text{for every }n\in\mathbb N_{>0},\ r\in\mathbb Q.
 }
 \tag{ZH.31}
\]

Powers of two in place of all positive integers also suffice. This produces a countable proof/disproof search space.

## 9. The first-Hermite Weil square

Define

\[
 F_{q,x}(z)=(z-x)e^{-q(z-x)^2/2}.
 \tag{ZH.32}
\]

Because `q,x` are real,

\[
 F_{q,x}(z)\overline{F_{q,x}(\bar z)}
 =(z-x)^2e^{-q(z-x)^2}.
 \tag{ZH.33}
\]

Thus `(ZH.29)` is a genuine Weil quadratic square, not merely a linear zero statistic.

With Fourier convention

\[
 \widehat f(\tau)=\int_\mathbb R f(u)e^{i\tau u}\,du,
\]

one inverse source is

\[
 f_{q,x}(u)
 =-{iu\over q\sqrt{2\pi q}}
 e^{-u^2/(2q)}e^{-ixu},
 \tag{ZH.34}
\]

and the autocorrelation transform in `(ZH.33)` has inverse

\[
 \boxed{
 k_{q,x}(u)
 ={e^{-ixu}\over4\sqrt\pi q^{3/2}}
 \left(1-{u^2\over2q}\right)e^{-u^2/(4q)}.
 }
 \tag{ZH.35}
\]

These are Schwartz tests. No compact-support approximation or Gram inversion is needed.

## 10. Exact prime-side formula

Use the standard Guinand--Weil formula in the normalization of the imported Zeta23 paper. Put

\[
 h_{q,x}(z)=(z-x)^2e^{-q(z-x)^2}.
 \tag{ZH.36}
\]

Then

\[
 \boxed{
 \begin{aligned}
 \mathcal M_\zeta(q,x)
 ={}&h_{q,x}(i/2)+h_{q,x}(-i/2)\\
 &+{1\over2\pi}\int_\mathbb R
 h_{q,x}(\tau)
 \left[
 \Re{\Gamma'\over\Gamma}
 \left({1\over4}+{i\tau\over2}\right)
 -\log\pi
 \right]d\tau\\
 &-{1\over2\sqrt\pi q^{3/2}}
 \sum_{n\ge2}{\Lambda(n)\over\sqrt n}
 \left(1-{(\log n)^2\over2q}\right)
 e^{-(\log n)^2/(4q)}
 \cos(x\log n).
 \end{aligned}
 }
 \tag{ZH.37}
\]

Every term is absolutely convergent. The prime weight is one first-Hermite Gaussian in logarithmic scale.

Consequently RH is equivalent to the explicit family of inequalities

\[
 \boxed{
 \begin{aligned}
 {1\over2\sqrt\pi q^{3/2}}
 \sum_{n\ge2}{\Lambda(n)\over\sqrt n}
 &\left(1-{(\log n)^2\over2q}\right)
 e^{-(\log n)^2/(4q)}
 \cos(x\log n)\\
 &\le h_{q,x}(i/2)+h_{q,x}(-i/2)+\Gamma_{q,x},
 \end{aligned}
 }
 \tag{ZH.38}
\]

for all `q>0,x in R`, where `Gamma_(q,x)` denotes the displayed integral in `(ZH.37)`.

This is the prime-side version of the corrected arithmetic floor on one universal two-parameter family. The inequality itself is not proved here.

## 11. Finite linear witnesses under false RH

The absolute prime coefficient is bounded by

\[
 {\log n\over2\sqrt\pi q^{3/2}\sqrt n}
 \left(1+{(\log n)^2\over2q}\right)
 e^{-(\log n)^2/(4q)}.
 \tag{ZH.39}
\]

For `t=log u`, the logarithmic derivative of the envelope before `du` is at most

\[
 {3\over t}-{1\over2}-{t\over2q},
 \tag{ZH.40}
\]

so it is decreasing for `t>=6`. Hence, whenever `log P>=6`, the omitted prime-power tail is bounded explicitly by

\[
 \boxed{
 \begin{aligned}
 R(P;q)
 ={1\over2\sqrt\pi q^{3/2}}
 \Bigg[&f_q(P)\\
 &+\int_{\log P}^\infty
 t\left(1+{t^2\over2q}\right)
 e^{t/2-t^2/(4q)}dt\Bigg],
 \end{aligned}
 }
 \tag{ZH.41}
\]

with `f_q(P)` the first all-integer envelope term. This uses only `Lambda(n)<=log n`.

If RH is false, `(ZH.30)` supplies a strict negative value at finite `q`. Choose nearby rational parameters as in Section 8, then a finite prime cutoff whose directed tail bound is smaller than the negative margin. The pole terms and gamma integral are explicit and may be evaluated outward.

Therefore, subject only to the standard explicit-formula normalization,

\[
 \boxed{
 \neg\mathrm{RH}
 \Longrightarrow
 \text{a finite rational-parameter, finite-prime, strict negative certificate.}
 }
 \tag{ZH.42}
\]

Conversely any rigorously negative interval for `(ZH.37)` is a finite negative Weil witness and disproves RH. No such Riemann-data witness is claimed here.

## 12. Relation to Claude's theorem

The upstream Zeta23 theorem uses a finite critical-density Gabor compression and its first two traces. It deliberately yields a positive proportion and cannot see one isolated off-line pair. The present criterion changes the consumer: it uses one pair-adapted asymptotic direction, obtained as the confluent limit of PR #375's terminal Gaussian family.

What is imported from upstream is only the centered Weil / Guinand--Weil normalization and the hyperbolic-pair viewpoint. The terminal graph, first-Hermite criterion, countable reduction, and finite-witness theorem are local proposed results and inherit no Lean status.

## 13. Proof boundary

Proposed complete, pending independent review:

```text
abstract parabolic terminal-pair theorem
first-Hermite reality criterion
zero-heat monotonicity equivalence
odd-derivative Hermite hierarchy
confluent limit of the PR #375 kernel
zeta zero-heat RH criterion
integer/rational countable criterion
first-Hermite Weil-square realization
exact all-prime explicit formula
finite linear witness completeness under false RH
```

Open:

```text
unconditional first-Hermite prime inequality (ZH.38)
corrected-kernel arithmetic floor
Riemann Hypothesis
```
