# L-90215 — The extremal two-low-row scalar is the Möbius inverse of an explicit positive divisor forcing

Claim ID: `L-90215`  
Status: **PROPOSED COMPLETE EXACT POSITIVE-RENEWAL LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-10  
Depends on: two-low-row source identity `L-90209`; extremal reward `L-90214`; elementary Dirichlet convolution  
Scope: exact renewal and positive forcing for the square-root-hinge low-row scalar; no sign theorem and no RH conclusion

## 1. The zero-safe source and hinge scalar

Retain

\[
 \omega
 =(\varepsilon-\delta_2)
  *(2\varepsilon-\delta_2)*\mu.
 \tag{L-90215.1}
\]

Its unit coefficient is

\[
 \omega(1)=2.
 \tag{L-90215.2}
\]

For real `x>=1`, define the complete square-root hinge transform

\[
 \mathcal R_\omega(x)
 =\sum_{q\le x}\omega(q)
 \left(q^{-1/2}-x^{-1/2}\right).
 \tag{L-90215.3}
\]

The extremal two-low-row SHARP scalar of `L-90209/L-90214` is

\[
 \boxed{
 \mathcal H(x)
 =-3\sum_{2\le q\le x}\omega(q)
 \left(q^{-1/2}-x^{-1/2}\right).
 }
 \tag{L-90215.4}
\]

Therefore

\[
 \boxed{
 \mathcal R_\omega(x)
 =2(1-x^{-1/2})-\frac13\mathcal H(x).
 }
 \tag{L-90215.5}
\]

## 2. Critical divisor-renewal operator

Define

\[
 \boxed{
 (\mathcal P f)(x)
 =\sum_{d\le x}\frac1{\sqrt d}f(x/d).
 }
 \tag{L-90215.6}
\]

Switching the finite hyperbola sums gives, for any arithmetic source `b`,

\[
 \mathcal P\left[
  \sum_{q\le x}b(q)(q^{-1/2}-x^{-1/2})
 \right]
 =\sum_{n\le x}\frac{(1*b)(n)}{\sqrt n}
 -\frac1{\sqrt x}\sum_{n\le x}(1*b)(n).
 \tag{L-90215.7}
\]

For the source (L-90215.1), Möbius cancellation is exact:

\[
 \boxed{
 1*\omega=2\varepsilon-3\delta_2+\delta_4.
 }
 \tag{L-90215.8}
\]

Consequently, for every `x>=4`,

\[
 \boxed{
 \mathcal P\mathcal R_\omega(x)
 =\frac52-\frac3{\sqrt2}.
 }
 \tag{L-90215.9}
\]

The prefix of (L-90215.8) is zero after state four, so no remainder is hidden in this identity.

## 3. Exact positive forcing for the low-row scalar

Put

\[
 J(x)=\sum_{d\le x}\frac1{\sqrt d}
      -\frac{\lfloor x\rfloor}{\sqrt x}.
 \tag{L-90215.10}
\]

Since

\[
 \mathcal P(1-x^{-1/2})=J(x),
 \tag{L-90215.11}
\]

substitution of (L-90215.5) into (L-90215.9) gives

\[
 \boxed{
 \mathcal P\mathcal H(x)=\Phi(x)
 \qquad(x\ge4),
 }
 \tag{L-90215.12}
\]

where

\[
 \boxed{
 \Phi(x)
 =6J(x)-\frac{15}{2}+\frac9{\sqrt2}.
 }
 \tag{L-90215.13}
\]

Thus the entire two-low-row arithmetic scalar is the critical divisor inverse of one explicit elementary forcing.

## 4. The forcing is strictly positive

Let `N=floor x>=4`. Then

\[
 \sum_{d\le N}d^{-1/2}
 \ge\int_1^{N+1}t^{-1/2}dt
 =2(\sqrt{N+1}-1),
 \tag{L-90215.14}
\]

and

\[
 \frac N{\sqrt x}\le\sqrt N.
\]

Hence

\[
 J(x)\ge2\sqrt{N+1}-\sqrt N-2.
 \tag{L-90215.15}
\]

The right side increases for `N>=4`. At `N=4`,

\[
 2\sqrt5-4>\frac25,
 \tag{L-90215.16}
\]

while

\[
 \frac54-\frac3{2\sqrt2}<\frac14
 \tag{L-90215.17}
\]

because `sqrt(5)>11/5` and `3/(2sqrt(2))>1`. Therefore

\[
 J(x)>\frac54-\frac3{2\sqrt2},
 \]

and (L-90215.13) yields

\[
 \boxed{
 \Phi(x)>0\qquad(x\ge4).
 }
 \tag{L-90215.18}
\]

At integer endpoints this reads

\[
 \boxed{
 \Phi(N)
 =6\left(\sum_{d\le N}d^{-1/2}-\sqrt N\right)
 -\frac{15}{2}+\frac9{\sqrt2}>0.
 }
 \tag{L-90215.19}
\]

## 5. Möbius inversion and Mellin factorization

The inverse of the positive operator `mathcal P` is the critically weighted Möbius operator. Finite divisor inversion of (L-90215.12) gives

\[
 \boxed{
 \mathcal H(x)
 =\sum_{d\le x}\frac{\mu(d)}{\sqrt d}
  \Phi(x/d).
 }
 \tag{L-90215.20}
\]

Therefore the low-row scalar is exactly a Möbius boundary extraction from a strictly positive deterministic forcing.

In Mellin coordinates,

\[
 \widehat{\mathcal P f}(s)
 =\zeta(s+1/2)\widehat f(s),
 \tag{L-90215.21}
\]

so

\[
 \boxed{
 \widehat{\mathcal H}(s)
 =\frac{\widehat\Phi(s)}{\zeta(s+1/2)}.
 }
 \tag{L-90215.22}
\]

This is the renewal-domain counterpart of the zero-safe numerator formula in `L-90209`.

## 6. Exact frontier

Equation (L-90215.12) has the ideal-looking form

```text
positive divisor operator
applied to the desired scalar
=
strictly positive elementary forcing.
```

But the delay mass of `mathcal P` is not contractive. Solving (L-90215.12) is precisely Möbius inversion (L-90215.20), which restores the reciprocal-zeta obstruction. Thus:

1. the uniform-Pascal geometry and the extremal `15:4` reward introduce no additional sign loss;
2. the complete forcing is explicit and positive;
3. every remaining sign difficulty occurs at the final Möbius boundary inversion;
4. an eventual one-sign proof for `mathcal H` remains RH-bearing by `L-90209`.

This identity is a sharp positive normal form, not a positivity proof.

## 7. Proof boundary

Proved exactly:

- the critical divisor-renewal identity for the complete source;
- the elementary forcing formula for the two-low-row scalar;
- strict positivity of that forcing for every real `x>=4`;
- exact weighted Möbius inversion;
- the corresponding Mellin factorization.

Not proved:

- sign of `mathcal H` after Möbius inversion;
- SHARP or RH.
