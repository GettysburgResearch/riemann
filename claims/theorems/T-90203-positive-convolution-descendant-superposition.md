# T-90203 — Positive-convolution transports are exactly positive dilation superpositions of the true descendant problem

Claim ID: `T-90203`  
Status: **PROPOSED COMPLETE EXACT THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-10  
Depends on: `L-90203`; `L-90101/T-90201` scaling identities for the GFEP coefficient; `T-90008` ramp notation  
Scope: exact source/endpoint transport and first-failure rigidity; no sign theorem for the current Möbius coefficient and no RH conclusion

## 1. Abstract scaled kernel

Let `c_X(k)` be a finitely supported arithmetic kernel depending on an endpoint `X`, and suppose it obeys the critical scaling law

\[
 \boxed{
 c_X(ad)=a^{-1/2}c_{X/a}(d)
 }
 \tag{T-90203.1}
\]

whenever the displayed coefficients lie in range. Define the Möbius slice

\[
 F_\mu(X)=\sum_d\mu(d)c_X(d).
 \tag{T-90203.2}
\]

For a source `b=mu*h` with `h(1)=1`, define

\[
 F_b(X)=\sum_kb(k)c_X(k).
 \tag{T-90203.3}
\]

Finite convolution switching and (T-90203.1) give

\[
 \boxed{
 F_b(X)
 =\sum_{a\ge1}\frac{h(a)}{\sqrt a}\,F_\mu(X/a).
 }
 \tag{T-90203.4}
\]

### Proof

Since `b=mu*h`,

\[
\begin{aligned}
F_b(X)
&=\sum_{a,d}h(a)\mu(d)c_X(ad)\\
&=\sum_a\frac{h(a)}{\sqrt a}
  \sum_d\mu(d)c_{X/a}(d),
\end{aligned}
\]

which is (T-90203.4). All sums are finite. ∎

Thus the entire positive-convolution cone of `L-90203` does not produce new independent arithmetic coordinates: it produces positive dilation superpositions of the original Möbius coordinate.

## 2. Specialization to every GFEP exit

For a fixed threshold `n` and exit `p`, take

\[
 c_X(k)=c_p^{X,n}(k)
\]

from `L-90101/T-90201`. Its exact endpoint scaling is

\[
 c_p^{X,n}(ad)=a^{-1/2}c_p^{X/a,n}(d).
 \tag{T-90203.5}
\]

The Möbius slice is

\[
 F_\mu(X)=\Sigma_{X,n}(p).
\]

Therefore, for every `b=mu*h in C_mu`,

\[
 \boxed{
 \Sigma_{X,n}^{\,b}(p)
 =\sum_{a\le X/n}
   \frac{h(a)}{\sqrt a}
   \Sigma_{X/a,n}(p).
 }
 \tag{T-90203.6}
\]

The convention is `Sigma_{Y,n}(p)=0` when the exit is outside the endpoint.

This formula strictly contains the Boolean descendant hierarchy of `T-90201`: the real prime cube corresponds to the special multiplicative choices `h=h_x` of `L-90203.11`.

## 3. First-failure rigidity on the maximal cone

Suppose

\[
 \Sigma_{X/a,n}(p)\ge0
 \qquad(a\ge2).
 \tag{T-90203.7}
\]

Then for every normalized `h>=0`,

\[
 \boxed{
 \Sigma_{X,n}^{\,\mu*h}(p)
 \ge\Sigma_{X,n}(p).
 }
 \tag{T-90203.8}
\]

because the `a=1` term of (T-90203.6) is the current Möbius value and every other term is nonnegative.

Hence at a first GFEP failure in the full dilation endpoint DAG, the true Möbius source is automatically the global minimizer not merely over the completely multiplicative class, not merely over the real cube, but over the **maximal normalized positive-convolution cone** `C_mu`.

This is the natural endpoint of lambda-extremality:

```text
prime-sign extremality            finite shadow;
real-cube extremality             multiplicative face;
Boolean mixed derivatives         divisor-DAG shadow;
positive-convolution extremality  maximal source-cone theorem.
```

None of these assertions supplies the sign of the current Möbius term.

## 4. Every nonnegative exit trace and the sparse producer

Let `alpha(p)>=0` be any endpoint-independent trace and put

\[
 F_\mu^\alpha(X)=\sum_p\alpha(p)\Sigma_{X,n}(p).
 \tag{T-90203.9}
\]

Linearity gives

\[
 \boxed{
 F_{\mu*h}^\alpha(X)
 =\sum_a\frac{h(a)}{\sqrt a}
  F_\mu^\alpha(X/a).
 }
 \tag{T-90203.10}
\]

For the true hitting trace of `L-32301`,

\[
 F_\mu^\alpha(X)=nA_X(n),
\]

so

\[
 \boxed{
 nA_X^{\,\mu*h}(n)
 =\sum_a\frac{h(a)}{\sqrt a}
   nA_{X/a}(n).
 }
 \tag{T-90203.11}
\]

At a first sparse-producer failure, the Möbius source is therefore the minimizer over the whole cone `C_mu` as well.

This is stronger than the hereditary Boolean theorem because the deformation `h` may be arbitrary and nonmultiplicative.

## 5. The unit source is exactly the empty-coefficient renewal

Choose `h=1`, the constant-one function. Then

\[
 \mu*1=\epsilon.
\]

The transported unit source sees only `k=1`, so

\[
 F_\epsilon(X)=c_X(1).
\]

Equation (T-90203.4) becomes

\[
 \boxed{
 c_X(1)
 =\sum_{a\ge1}\frac{F_\mu(X/a)}{\sqrt a}.
 }
 \tag{T-90203.12}
\]

For a GFEP exit this is exactly

\[
 c_p^{X,n}(1)
 =\sum_{a\le X/n}\frac{\Sigma_{X/a,n}(p)}{\sqrt a},
 \tag{T-90203.13}
\]

and for the sparse producer the identical relation holds with `nA_X(n)`.

Thus the empty-coefficient renewal is not an isolated inversion trick: it is the endpoint image of the **maximal positive source deformation** from `mu` to the unit source.

The inverse is necessarily Möbius signed:

\[
 \boxed{
 F_\mu(X)
 =\sum_{a\ge1}\frac{\mu(a)}{\sqrt a}
  c_{X/a}(1).
 }
 \tag{T-90203.14}
\]

This is precisely where positivity is lost. Any proof that inverts the positive descendant superposition without using extra structure has returned to the Möbius wall.

## 6. Ramp superposition on the entire cone

Let

\[
 P(X)=\sum_{m\le X}\Lambda(m)m^{-1/2}\log\frac Xm
\]

be the ordinary complete prime-power ramp. For `b=mu*h`, associativity gives

\[
 b*\log=h*(\mu*\log)=h*\Lambda.
\]

Therefore the transported ramp is

\[
 \boxed{
 \operatorname{Ramp}_{\mu*h}(X)
 =\sum_{a\le X/2}\frac{h(a)}{\sqrt a}P(X/a).
 }
 \tag{T-90203.15}
\]

Since `P(Y)>=0` for every `Y`,

\[
 \boxed{
 \operatorname{Ramp}_{\mu*h}(X)\ge P(X)
 =\operatorname{Ramp}_\mu(X)
 \qquad(h\ge0,h(1)=1).
 }
 \tag{T-90203.16}
\]

Thus `L-90201`'s real-cube ramp theorem extends to the entire maximal cone.

Consequently the following three uniform lower-bound criteria are equivalent:

```text
Form A at the Möbius/Liouville slice;
Form A uniformly over the real multiplicative cube;
Form A uniformly over all b in C_mu.
```

Combined with the resident prime-ramp/Landau consumer and the RH-side estimate of `T-90202`, each is equivalent to RH. This is an equivalence criterion, not an unconditional proof.

## 7. Exact location of the remaining obstruction

The cone theorem removes every source deformation generated by nonnegative Dirichlet convolution. What survives is the boundary inversion

\[
 \epsilon\longmapsto\mu,
\]

or equivalently the empty coefficient in (T-90203.12)--(T-90203.14).

The campaign map therefore sharpens to

```text
free signs                            refuted / too large;
complete multiplicativity            descendant arithmetic;
full real prime cube                  positive-convolution face;
all normalized positive convolutions maximal cone, classified exactly;
current Möbius boundary coefficient  OPEN / RH-bearing.
```

Any genuine continuation must use structure not preserved by arbitrary nonnegative convolution, because everything preserved by that cone has now been quotiented out exactly.

## 8. Proof boundary

Proved exactly:

- abstract positive descendant superposition (T-90203.4);
- its GFEP and sparse-producer specializations;
- first-failure Möbius minimality on the maximal cone;
- identification of the unit-source renewal as the extreme positive deformation;
- the Möbius-signed inverse;
- full-cone ramp extremality and the resulting RH criterion equivalence.

Still open:

- the sign of the current empty Möbius coefficient;
- a positive inversion of (T-90203.12), which cannot follow from cone information alone;
- GFEP, sparse producer positivity, and RH.
