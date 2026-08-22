# L-90201 — Liouville is the pointwise minimizer of every real squarefree generalized von Mangoldt coefficient

Claim ID: `L-90201`  
Status: **PROPOSED COMPLETE EXACT LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-10  
Depends on: only finite divisor algebra; consumes the class `H` and transported ramp notation of `T-90008`  
Scope: exact pointwise arithmetic and every nonnegative test weight; no lower estimate for the ordinary prime-power ramp and no RH conclusion

## 1. The real multiplicative cube

Let a real parameter

\[
 x_p\in[-1,1]
\]

be assigned to every prime. On squarefree integers put

\[
 f_x(d)=\prod_{p\mid d}x_p,
 \qquad f_x(1)=1,
\]

and define the squarefree source

\[
 b_x(d)=\mu^2(d)f_x(d).
\]

The associated generalized von Mangoldt coefficient is

\[
 \boxed{
 \Lambda_x(n)
 =(b_x*\log)(n)
 =\sum_{d\mid n}\mu^2(d)f_x(d)\log\frac nd .
 }
 \tag{L-90201.1}
\]

For the Liouville point `x_p=-1` on every prime, the squarefree restriction is
exactly `mu`, hence

\[
 \Lambda_{-1}(n)=(\mu*\log)(n)=\Lambda(n).
 \tag{L-90201.2}
\]

The class `H` of `T-90008` is the vertex set `x_p in {+-1}` of this real cube.

## 2. Exact Bernstein normal form

Let

\[
 \mathcal P(n)=\{p:p\mid n\},
 \qquad r=\omega(n),
 \qquad y_p=\frac{1+x_p}{2}\in[0,1],
\]

and write `rad(n)` for the radical. Then for every `n>=2`,

\[
 \boxed{
 \begin{aligned}
 \Lambda_x(n)
 ={}&2^{r-1}
 \sum_{q\mid\operatorname{rad}(n)\atop q\ {\rm prime}}
 (\log q)
 \prod_{p\mid n,\ p\ne q}y_p\\
 &\quad+2^r\log\frac{n}{\operatorname{rad}(n)}
 \prod_{p\mid n}y_p.
 \end{aligned}}
 \tag{L-90201.3}
\]

Every coefficient and every monomial on the right is nonnegative.

### Proof

Expanding the logarithm in (L-90201.1) over subsets of the distinct prime
divisors gives

\[
 \begin{aligned}
 \Lambda_x(n)
 &=\log n\prod_{p\mid n}(1+x_p)
 -\sum_{q\mid n\atop q\ {\rm prime}}
   (\log q)x_q
   \prod_{p\mid n,\ p\ne q}(1+x_p).
 \end{aligned}
 \tag{L-90201.4}
\]

Substitute `1+x_p=2y_p` and `x_q=2y_q-1`. The terms containing the full
product combine to

\[
 2^r\left(\log n-\sum_{q\mid n}\log q\right)
 \prod_{p\mid n}y_p
 =2^r\log\frac{n}{\operatorname{rad}(n)}
 \prod_{p\mid n}y_p,
\]

and the remaining terms are the first line of (L-90201.3). ∎

## 3. Pointwise Liouville extremality

The ordinary von Mangoldt coefficient is

\[
 \Lambda(n)=
 \begin{cases}
 \log p,&n=p^a,\\
 0,&\omega(n)\ge2.
 \end{cases}
\]

If `r=1`, the first term of (L-90201.3) is exactly `log p` and the second is
nonnegative. If `r>=2`, every term in (L-90201.3) is nonnegative and
`Lambda(n)=0`. Therefore

\[
 \boxed{
 \Lambda_x(n)\ge\Lambda(n)
 \qquad(n\ge2,
 \ x_p\in[-1,1]).
 }
 \tag{L-90201.5}
\]

Thus Liouville minimizes the generalized von Mangoldt sequence **at every
integer separately**, not merely after summation and not merely over the
vertices of `H`.

### Vertex classification

For `x_p in {+-1}`, let `nu_-(n)` be the number of distinct prime divisors of
`n` on which `x_p=-1`. Formula (L-90201.3) reduces to

\[
 \Lambda_x(n)=
 \begin{cases}
 2^{r-1}\bigl(2\log n-\log\operatorname{rad}(n)\bigr),
    &\nu_-(n)=0,\\[1mm]
 2^{r-1}\log q,
    &\nu_-(n)=1,
      \ q\text{ the unique negative prime},\\[1mm]
 0,&\nu_-(n)\ge2.
 \end{cases}
 \tag{L-90201.6}
\]

For a prime power `p^a`, equality with `Lambda(p^a)` holds when `x_p=-1`, and
also at the prime `a=1` regardless of `x_p`. For an integer with at least two
distinct prime divisors, equality holds exactly when at least two of those
prime signs are negative.

## 4. Universal nonnegative-weight theorem

Let `W(n)>=0` be any finitely supported arithmetic weight. Define

\[
 \mathcal R_x(W)=\sum_{n\ge2}W(n)\Lambda_x(n).
 \tag{L-90201.7}
\]

Then pointwise extremality gives

\[
 \boxed{
 \mathcal R_x(W)\ge\mathcal R_{-1}(W)
 =\sum_{n\ge2}W(n)\Lambda(n).
 }
 \tag{L-90201.8}
\]

This theorem is independent of the shape of `W`. It applies to every positive
endpoint, occupancy, or packing score whose arithmetic coefficient is
`(mu^2 f)*log`.

## 5. Exact resolution of the transported ramp problem

For the critical endpoint weight

\[
 w_X(q)=q^{-1/2}\log\frac Xq\,\mathbf1_{q\le X},
\]

`T-90008` defines

\[
 \operatorname{Ramp}_x(X)
 =\sum_{d\le X/2\atop d\ {\rm squarefree}}
 f_x(d)\sum_{2\le m\le X/d}(\log m)w_X(md).
 \tag{L-90201.9}
\]

Divisor switching gives exactly

\[
 \operatorname{Ramp}_x(X)
 =\sum_{q\le X}w_X(q)\Lambda_x(q).
 \tag{L-90201.10}
\]

Consequently

\[
 \boxed{
 \operatorname{Ramp}_x(X)
 \ge\operatorname{Ramp}_{\lambda}(X)
 =\sum_{q\le X}\Lambda(q)w_X(q)
 \qquad(x_p\in[-1,1]).
 }
 \tag{L-90201.11}
\]

This proves the one-scalar half of the `T-90008` lambda-extremality conjecture
for **every** endpoint. The WHT searches through classes described as large as
`2^669` are finite confirmations of an exact local identity, not the source of
the theorem.

It also upgrades the reduction theorem to the exact equivalence

\[
 \boxed{
 \text{Form A uniformly over }\mathcal H
 \quad\Longleftrightarrow\quad
 \text{Form A at the Liouville/Mobius slice}.
 }
 \tag{L-90201.12}
\]

The reverse implication is (L-90201.11); the forward implication is
specialization to `lambda` as in `T-90008`.

This equivalence does **not** prove Form A. It proves that class uniformity costs
exactly zero on the positive ramp functional.

## 6. Quantitative rigidity and equality at one endpoint

The point `lambda` is not only extremal. Every active prime flip pays an
explicit positive amount. From the term `n=2p` in (L-90201.3),

\[
 \Lambda_x(2p)-\Lambda(2p)
 \ge2(\log2)y_p
 \qquad(p\text{ prime}),
 \tag{L-90201.13}
\]

where for `p=2` the left side is read at `n=4`. Hence

\[
 \boxed{
 \operatorname{Ramp}_x(X)-\operatorname{Ramp}_{\lambda}(X)
 \ge2\log2
 \sum_{p<X/2}y_p\,w_X(2p).
 }
 \tag{L-90201.14}
\]

For vertex signs this says every prime changed from `-1` to `+1` below `X/2`
creates a visible positive penalty before any analytic estimate is used.

Because `w_X(n)>0` for `n<X`, equality in (L-90201.11) holds exactly when

\[
 x_p=-1\qquad\text{for every prime }p<X/2.
 \tag{L-90201.15}
\]

Prime signs at or above `X/2` are inactive: they occur only at a prime itself,
where the local coefficient already equals `log p`, or at the zero-weight
endpoint.

## 7. Relation to the Final Deficit Theorem

`T-90009` remains relevant as a fence on generic distance-based attempts to
bound the **Liouville slice** with power saving. But after (L-90201.11), Hall or
Halasz technology is not needed to compare the other members of `H` with that
slice. The correct separation is:

```text
class extremality of the positive ramp       exact local algebra, closed here;
sharp lower bound at the lambda slice         the surviving RH-bearing problem.
```

Thus the informational deficit is a statement about estimating the empty
Liouville/Mobius coordinate, not a deficit created by class uniformity.

## 8. Proof boundary

Proved exactly:

1. the Bernstein formula (L-90201.3);
2. pointwise `Lambda_x >= Lambda` on the full real cube;
3. minimization under every nonnegative arithmetic weight;
4. exact ramp lambda-extremality for every endpoint;
5. Form A over `H` iff Form A at `lambda`;
6. explicit coercivity and equality classification.

Still open:

1. the sharp `4 sqrt(X)-X^epsilon` lower bound at `lambda`;
2. GFEP and producer positivity;
3. RH.
