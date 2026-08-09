# L-90016 — The prime endpoint is a positive-source mean-age problem

Claim ID: `L-90016` (provisional branch range)  
Title: Every nonnegative arithmetic weighting of the parabolic residual has one positive occupancy source; the prime endpoint and all fractional endpoints are exact weighted-mean-age inequalities  
Status: **PROPOSED COMPLETE EXACT AGGREGATION / FRACTIONAL THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-09  
Dependencies: `L-90015`; PR #352 `T-90008/T-90010`  
Scope: exact positive-source normal form; no proof of the required mean-age inequality or RH

## 1. Nonnegative arithmetic weights

Let `lambda(q)>=0` be an arithmetic weight satisfying

\[
 \sum_{q\ge2}{\lambda(q)\over q^{1+\varepsilon}}<\infty
 \qquad(\varepsilon>0).
\tag{L-90016.1}
\]

Define

\[
 F_\lambda(X)=\sum_{q\le X}\lambda(q)r_X(q).
\tag{L-90016.2}
\]

The two principal examples are

\[
 \lambda_{\mathbb P}(q)
 =\begin{cases}\log q,&q\text{ prime},\\0,&\text{otherwise},\end{cases}
\]

for which

\[
 F_{\lambda_{\mathbb P}}(X)=A(X),
\tag{L-90016.3}
\]

and

\[
 \lambda_\Lambda(q)=\Lambda(q),
\]

the complete prime-power dual weight.

## 2. One positive aggregate source

Let `Delta_q` be the occupancy deficit of `L-90015`. For logarithmic endpoint `t`, define

\[
\boxed{
 \mathcal Q_\lambda(t)
 =e^{-t/2}\sum_{q\le e^t}
  \lambda(q)\Delta_q(e^t).
}
\tag{L-90016.4}
\]

Every term is nonnegative, and the source is strictly positive once a nonzero weight has activated.

Apply `L-90015.18` to each column with `t-log q` in place of `t`. The critical normalization cancels the apparent factor `sqrt(q)`:

\[
 {\lambda(q)\over\sqrt q}
 Q_q(t-\log q)
 =\lambda(q)e^{-t/2}\Delta_q(e^t).
\tag{L-90016.5}
\]

Tonelli's theorem, first for finite truncations and then by monotone convergence, gives the exact aggregate identity

\[
\boxed{
 -F_\lambda(e^t)
 =\int_0^t
  \left(1-{t-u\over2}\right)
  \mathcal Q_\lambda(u)\,du.
}
\tag{L-90016.6}
\]

Thus all arithmetic signs have disappeared from the source. The only sign change is the fixed Green kernel at backward age two.

Taking Laplace transforms,

\[
\boxed{
 -\widetilde F_\lambda(z)
 ={z-\frac12\over z^2}
  \widetilde{\mathcal Q_\lambda}(z).
}
\tag{L-90016.7}
\]

In particular,

\[
\boxed{
 \widetilde F_\lambda(z)<0
 \qquad(z>1/2\text{ real})
}
\tag{L-90016.8}
\]

for every nonzero nonnegative weight. For the prime weight this proves, unconditionally,

\[
\boxed{
 \widehat A(z)<0
 \qquad(z>1/2\text{ real}).
}
\tag{L-90016.9}
\]

This sign is columnwise and does not use the prime number theorem.

## 3. Exact mean-age criterion

Put

\[
 M_0(t)=\int_0^t\mathcal Q_\lambda(u)\,du,
 \qquad
 M_1(t)=\int_0^t(t-u)\mathcal Q_\lambda(u)\,du.
\tag{L-90016.10}
\]

Then (L-90016.6) is

\[
\boxed{
 F_\lambda(e^t)
 ={1\over2}[M_1(t)-2M_0(t)].
}
\tag{L-90016.11}
\]

When `M_0(t)>0`, define the backward mean age

\[
 \mathfrak a_\lambda(t)={M_1(t)\over M_0(t)}.
\]

Therefore

\[
\boxed{
 F_\lambda(e^t)<0
 \iff
 \mathfrak a_\lambda(t)<2.
}
\tag{L-90016.12}
\]

For the prime source, the minimal criterion `T-90008` becomes

\[
\boxed{
 \mathrm{RH}
 \iff
 \mathfrak a_{\mathbb P}(t)<2
 \quad\text{for all sufficiently large }t.
}
\tag{L-90016.13}
\]

This is an exact reformulation, not a new conditional implication.

Differentiating the two moments also gives

\[
 M_0'=\mathcal Q_\lambda,
 \qquad
 M_1'=M_0,
\]

and hence

\[
\boxed{
 {d\over dt}F_\lambda(e^t)
 ={1\over2}M_0(t)-\mathcal Q_\lambda(t).
}
\tag{L-90016.14}
\]

Thus the endpoint-monotonicity gate of `T-90009` is the stronger instantaneous concentration inequality

\[
 M_0(t)\le2\mathcal Q_\lambda(t).
\]

## 4. Fractional endpoint family

For `1<sigma<=2`, let `mathscr F_(lambda,sigma)` be the fractional endpoint obtained from `F_lambda(e^t)` exactly as in `T-90010`. Its transform is

\[
 z^{2-\sigma}\widetilde F_\lambda(z).
\]

Equation (L-90016.7) gives

\[
 -\widetilde{\mathscr F_{\lambda,\sigma}}(z)
 ={z-\frac12\over z^\sigma}
  \widetilde{\mathcal Q_\lambda}(z).
\tag{L-90016.15}
\]

The inverse kernel is explicit:

\[
\boxed{
 h_\sigma(a)
 ={a^{\sigma-2}\over\Gamma(\sigma-1)}
 \left(1-{a\over2(\sigma-1)}\right).
}
\tag{L-90016.16}
\]

Therefore

\[
\boxed{
 -\mathscr F_{\lambda,\sigma}(t)
 =\int_0^t h_\sigma(t-u)
  \mathcal Q_\lambda(u)\,du.
}
\tag{L-90016.17}
\]

The whole fractional family has the same positive source. Only the one-sign-change age threshold moves from two to

\[
 2(\sigma-1).
\]

Indeed, with

\[
 M_a^{(\sigma)}(t)
 =\int_0^t(t-u)^a\mathcal Q_\lambda(u)\,du,
\]

one has

\[
\boxed{
 \mathscr F_{\lambda,\sigma}(t)<0
 \iff
 {M_{\sigma-1}^{(\sigma)}(t)
  \over M_{\sigma-2}^{(\sigma)}(t)}
 <2(\sigma-1).
}
\tag{L-90016.18}
\]

At `sigma=2` this is (L-90016.12). At the order-one boundary the positive lobe collapses to zero age, matching the absolute-convergence firewall in `T-90010`.

## 5. Exact integer source formulas

At an integer endpoint `N`, write

\[
 \ell(N)=\log\operatorname{rad}(N).
\]

The occupancy sawtooth satisfies

\[
\boxed{
 \Delta_q(N)=\left\{\frac Nq\right\}
 +\mathbf1_{q\mid N}.
}
\tag{L-90016.19}
\]

For the prime source this gives

\[
\boxed{
 \mathcal Q_{\mathbb P}(\log N)
 ={1\over\sqrt N}\left[
 N\sum_{p\le N}{\log p\over p}
 -\sum_{m\le N}\ell(m)
 +\ell(N)
 \right].
}
\tag{L-90016.20}
\]

For the complete von-Mangoldt source,

\[
\boxed{
 \mathcal Q_\Lambda(\log N)
 ={1\over\sqrt N}\left[
 N\sum_{q\le N}{\Lambda(q)\over q}
 -\log(N!)+\log N
 \right].
}
\tag{L-90016.21}
\]

The identities use only

\[
 \sum_{p\mid m}\log p=\log\operatorname{rad}(m),
 \qquad
 \sum_{q\mid m}\Lambda(q)=\log m.
\]

These are exact finite arithmetic coordinates for the positive source.

## 6. What this changes

The minimal endpoint problem is no longer merely

```text
prove one oscillatory prime scalar is negative.
```

It is equivalently

```text
construct/control one explicit positive occupancy source;
prove that its backward critical mean age stays below two.
```

The deterministic critical exponential source has mean age exactly two. The prime-square moat of PR #352 biases the true source to the favorable side, while an off-line zero would create a growing adverse mode. This explains simultaneously:

- why the endpoint has a stable negative finite drift;
- why every positive-real Mellin probe already has the desired sign;
- why pointwise fixed-column negativity is false;
- why differentiation reaches a stronger critical concentration boundary.

No inequality controlling the aggregate mean age is asserted here.

## 7. Proof boundary

Closed exactly:

1. positive-source aggregation for every nonnegative arithmetic weight;
2. strict negativity of every positive-real Mellin moment;
3. the endpoint mean-age identity;
4. the derivative/concentration identity;
5. the positive-source form of every fractional endpoint;
6. exact prime and prime-power source formulas at integer endpoints.

Open:

1. eventual prime-source mean age below two;
2. the prime endpoint sign;
3. RH.