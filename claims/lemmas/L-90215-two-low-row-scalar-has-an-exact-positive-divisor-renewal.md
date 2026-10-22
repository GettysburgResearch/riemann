# L-90215 — The extremal two-low-row scalar is the Möbius inverse of an explicit positive divisor forcing

Claim ID: `L-90215`  
Status: **PROPOSED COMPLETE EXACT POSITIVE-RENEWAL LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-10  
Corrected: 2026-08-10 — the forcing is now stated on the complete range `x>=1`; the earlier `x>=4` formula may not be Möbius-inverted without its finite boundary collar  
Depends on: two-low-row source identity `L-90209`; extremal reward `L-90214`; elementary Dirichlet convolution  
Scope: exact renewal and positive forcing for the square-root-hinge low-row scalar; no sign theorem and no RH conclusion

## 1. The zero-safe source and hinge scalar

Retain

\[
 \omega
 =(\varepsilon-\delta_2)
  *(2\varepsilon-\delta_2)*\mu .
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

Consequently

\[
 \boxed{
 \mathcal P\mathcal R_\omega(x)=
 \begin{cases}
 2-2x^{-1/2},&1\le x<2,\\[1mm]
 2-\dfrac3{\sqrt2}+x^{-1/2},&2\le x<4,\\[2mm]
 \dfrac52-\dfrac3{\sqrt2},&x\ge4.
 \end{cases}}
 \tag{L-90215.9}
\]

The third line is the previously recorded constant forcing.  The first two
lines are the finite boundary collar which must be retained before Möbius
inversion.

## 3. Exact all-scale positive forcing for the low-row scalar

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

substitution of (L-90215.5) into (L-90215.9) gives the exact identity

\[
 \boxed{
 \mathcal P\mathcal H(x)=\widetilde\Phi(x)
 \qquad(x\ge1),
 }
 \tag{L-90215.12}
\]

where

\[
 \boxed{
 \widetilde\Phi(x)=
 \begin{cases}
 0,&1\le x<2,\\[1mm]
 6J(x)-6+\dfrac9{\sqrt2}-\dfrac3{\sqrt x},
     &2\le x<4,\\[3mm]
 6J(x)-\dfrac{15}{2}+\dfrac9{\sqrt2},
     &x\ge4.
 \end{cases}}
 \tag{L-90215.13}
\]

Thus the complete two-low-row arithmetic scalar is the critical divisor
inverse of one explicit elementary forcing on the full causal domain.

## 4. The complete forcing is nonnegative

On `1<=x<2`, the forcing is zero.

For `2<=x<3`, one has

\[
 J(x)=1+\frac1{\sqrt2}-\frac2{\sqrt x},
\]

and hence

\[
 \boxed{
 \widetilde\Phi(x)
 =15\left(\frac1{\sqrt2}-\frac1{\sqrt x}\right)\ge0.
 }
 \tag{L-90215.14}
\]

For `3<=x<4`,

\[
 J(x)=1+\frac1{\sqrt2}+\frac1{\sqrt3}
      -\frac3{\sqrt x},
\]

so

\[
 \boxed{
 \widetilde\Phi(x)
 =\frac{15}{\sqrt2}+\frac6{\sqrt3}
  -\frac{21}{\sqrt x}>0.
 }
 \tag{L-90215.15}
\]

The expression increases with `x`, and at `x=3` it is

\[
 \frac{15}{\sqrt2}-\frac{15}{\sqrt3}>0.
\]

For `x>=4`, let `N=floor x`.  The elementary estimate

\[
 \sum_{d\le N}d^{-1/2}
 \ge\int_1^{N+1}t^{-1/2}dt
 =2(\sqrt{N+1}-1)
 \tag{L-90215.16}
\]

and `N/sqrt(x)<=sqrt(N)` give

\[
 J(x)\ge2\sqrt{N+1}-\sqrt N-2.
 \tag{L-90215.17}
\]

The right side increases for `N>=4`.  At `N=4` it is larger than `2/5`,
whereas

\[
 \frac54-\frac3{2\sqrt2}<\frac14.
\]

Therefore

\[
 \boxed{
 \widetilde\Phi(x)>0\qquad(x\ge2),
 }
 \tag{L-90215.18}
\]

with equality exactly on the initial interval `1<=x<=2`.

At integer endpoints `N>=4`, the forcing is the simpler expression

\[
 \boxed{
 \widetilde\Phi(N)
 =6\left(\sum_{d\le N}d^{-1/2}-\sqrt N\right)
 -\frac{15}{2}+\frac9{\sqrt2}>0.
 }
 \tag{L-90215.19}
\]

## 5. Exact Möbius inversion

The inverse of the positive operator `mathcal P` is the critically weighted
Möbius operator.  Because (L-90215.12) is now valid on the entire range sampled
by the inverse, finite divisor inversion gives

\[
 \boxed{
 \mathcal H(x)
 =\sum_{d\le x}\frac{\mu(d)}{\sqrt d}
  \widetilde\Phi(x/d).
 }
 \tag{L-90215.20}
\]

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
 =\frac{\widehat{\widetilde\Phi}(s)}
        {\zeta(s+1/2)}.
 }
 \tag{L-90215.22}
\]

### Boundary-collar warning

The high-range formula

\[
 \Phi_\infty(x)
 =6J(x)-\frac{15}{2}+\frac9{\sqrt2}
 \qquad(x\ge4)
\]

is correct on its declared range, but it may not be inserted by itself into
the divisor inverse.  The terms with `x/d<4` see the first two lines of
(L-90215.13).  Omitting that collar changes the recovered scalar.  Equation
(L-90215.20), with `widetilde Phi`, is the corrected all-scale inversion.

## 6. Exact frontier

The complete normal form is now

```text
positive divisor operator
applied to the desired scalar
=
nonnegative elementary forcing on every causal scale.
```

But the delay mass of `mathcal P` is not contractive.  Solving
(L-90215.12) is precisely Möbius inversion (L-90215.20), which restores the
reciprocal-zeta obstruction.  Thus:

1. the uniform-Pascal geometry and extremal `15:4` reward introduce no sign
   loss;
2. the forcing is explicit and nonnegative on its complete domain;
3. every remaining sign difficulty occurs in the final critical Möbius
   boundary inversion;
4. an eventual one-sign proof for `mathcal H` remains RH-bearing by
   `L-90209`.

This is a sharp positive normal form, not a positivity proof.

## 7. Proof boundary

Proved exactly:

- the critical divisor-renewal identity for the complete source;
- the full piecewise forcing, including the finite collar;
- nonnegativity of that forcing for every real `x>=1`;
- exact weighted Möbius inversion with no domain mismatch;
- the corresponding Mellin factorization.

Not proved:

- sign of `mathcal H` after Möbius inversion;
- SHARP or RH.
