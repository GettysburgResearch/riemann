# R-32302 — The Möbius-projected divisor kernel is a critical shifted-zeta remainder, not an elementary shortcut

Claim ID: `R-32302`  
Title: The divisor-smoothed Möbius kernel has an elementary `O(x^(1-alpha))` error family, whose critical `alpha=1/2` member is exactly the square-root barrier  
Status: **EXACT SCOPE CORRECTION / PROPOSED COMPLETE ELEMENTARY LEMMA**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Scope: correction of the exploratory Möbius-projection idea from the previous pass; no RH conclusion

## 1. The projected kernel

For `0<alpha<=1`, define

\[
 a_\alpha(n)
 =\sum_{d\mid n}\frac{\mu(d)}{d^\alpha}.
\tag{R-32302.1}
\]

The function is multiplicative and, for every prime power `p^k`,

\[
 a_\alpha(p^k)=1-p^{-\alpha}>0.
\tag{R-32302.2}
\]

Thus `a_alpha(n)>0` for every integer `n`.

Its Dirichlet series is, initially for `Re(s)>1`,

\[
\boxed{
 \sum_{n\ge1}\frac{a_\alpha(n)}{n^s}
 =\frac{\zeta(s)}{\zeta(s+\alpha)}.
}
\tag{R-32302.3}
\]

The exploratory projection in the previous pass was the critical member `alpha=1/2`.

## 2. Elementary prefix asymptotic

Put

\[
 A_\alpha(x)=\sum_{n\le x}a_\alpha(n).
\]

Finite divisor switching gives

\[
\begin{aligned}
 A_\alpha(x)
 &=\sum_{d\le x}\frac{\mu(d)}{d^\alpha}
   \left\lfloor\frac xd\right\rfloor\\
 &=x\sum_{d\le x}\frac{\mu(d)}{d^{1+\alpha}}
   +O\left(\sum_{d\le x}d^{-\alpha}\right).
\end{aligned}
\tag{R-32302.4}

Because the series for `1/zeta(1+alpha)` is absolutely convergent,

\[
 x\sum_{d>x}d^{-1-\alpha}=O(x^{1-\alpha}).
\]

Also

\[
 \sum_{d\le x}d^{-\alpha}
 =\begin{cases}
   O_\alpha(x^{1-\alpha}),&0<\alpha<1,\\
   O(\log(2x)),&\alpha=1.
  \end{cases}
\]

Hence

\[
\boxed{
 A_\alpha(x)
 =\frac{x}{\zeta(1+\alpha)}
 +\begin{cases}
   O_\alpha(x^{1-\alpha}),&0<\alpha<1,\\
   O(\log(2x)),&\alpha=1.
  \end{cases}}
\tag{R-32302.5}

This estimate is completely elementary and uses no prime number theorem or cancellation in `mu`.

At the critical value,

\[
\boxed{
 A_{1/2}(x)
 =\frac{x}{\zeta(3/2)}+O(\sqrt x).
}
\tag{R-32302.6}

Thus the naïve projected kernel lands exactly on a square-root remainder, not below it.

## 3. Exact dyadic discrepancy

Define the centered error

\[
 E_\alpha(x)=A_\alpha(x)-\frac{x}{\zeta(1+\alpha)}
\]

and its dyadic discrepancy

\[
 \Delta_\alpha(x)=A_\alpha(2x)-2A_\alpha(x)
 =E_\alpha(2x)-2E_\alpha(x).
\tag{R-32302.7}

Equation (R-32302.5) gives unconditionally

\[
\boxed{
 \Delta_\alpha(x)=O_\alpha(x^{1-\alpha})
 \quad(0<\alpha<1),
}
\tag{R-32302.8}

and, in particular,

\[
\boxed{
 \Delta_{1/2}(x)=O(\sqrt x).
}
\tag{R-32302.9}

The previous exploratory suggestion that a generic dyadic contraction of this quantity might be elementary therefore has the wrong scale at the critical exponent.

## 4. A subpower dyadic estimate would imply a subpower prefix remainder

There is an exact reverse telescoping identity

\[
 E_\alpha(x)
 =2^{-k}E_\alpha(2^kx)
 -\sum_{j=0}^{k-1}2^{-j-1}\Delta_\alpha(2^jx).
\tag{R-32302.10}

For `alpha=1/2`, the unconditional bound `E_(1/2)(y)=O(sqrt(y))` makes the first term tend to zero as `k->infinity`.

Consequently, if for every `epsilon>0`

\[
 \Delta_{1/2}(x)=O_\epsilon(x^\epsilon),
\tag{R-32302.11}

then, taking `epsilon<1`, the geometric sum in (R-32302.10) gives

\[
\boxed{
 E_{1/2}(x)=O_\epsilon(x^\epsilon)
 \quad\text{for every }\epsilon>0.
}
\tag{R-32302.12}

So the proposed dyadic contraction is not merely a local smoothness estimate.  It would improve the complete summatory divisor kernel from the elementary square-root error to a subpower error.

## 5. Shifted-zeta analytic barrier

Partial summation applied to (R-32302.12) would continue

\[
 \frac{\zeta(s)}{\zeta(s+1/2)}
\]

from `Re(s)>1` to `Re(s)>0`, apart from its main pole at `s=1`, with no singularities not canceled by a simultaneous zero of the numerator.

Thus every off-line denominator zero `rho` would have to satisfy the highly rigid cancellation condition

\[
 \zeta(\rho-1/2)=0
\tag{R-32302.13}

with at least the required multiplicity.  By the functional equation, this forces the corresponding reflected shifted zero as well.

This file does **not** assert that such shifted common-zero configurations are already known to be impossible.  Therefore the divisor-smoothed kernel is not claimed to be an RH equivalence by itself.  The exact conclusion is narrower and sufficient for the scope correction:

> a subpower critical dyadic discrepancy is a deep shifted-zeta cancellation theorem, not an elementary adapter which removes the reciprocal-zeta difficulty.

## 6. Why the parameter family clarifies the criticality

For `alpha>1/2`, the elementary remainder in (R-32302.5) is already

\[
 O(x^{1-\alpha})=o(\sqrt x).
\]

At `alpha=1`, one recovers the familiar positive kernel

\[
 a_1(n)=\frac{\varphi(n)}n
\]

with only logarithmic summatory error.

Exactly at `alpha=1/2`, however, the divisor-switch error becomes `O(sqrt x)`, while the denominator in (R-32302.3) becomes `zeta(s+1/2)`, placing nontrivial zeta zeros at the critical shifted boundary.

The square-root scale and the half-shift therefore arise together.  This is the structural reason the critical projected kernel does not provide the hoped-for shortcut.

## 7. Corrected research lesson

The useful Möbius projection from the previous pass is `L-32302`, which projects positive fragmentation directly onto the **unsmoothed** Riesz mean with transform `1/zeta(z+1/2)`.  That projection cleanly exposes the RH source.

The divisor-smoothed positive kernel `a_(1/2)` instead inserts an extra `zeta(s)` numerator.  It is useful as a diagnostic family, but it should not replace the source-pinned Riesz consumer or be advertised as an easier route to RH.

## 8. Proof boundary

Proved elementarily:

1. positivity and multiplicativity of `a_alpha`;
2. its shifted-zeta Dirichlet series;
3. the uniform prefix estimate (R-32302.5);
4. the critical `O(sqrt x)` barrier;
5. the dyadic reverse telescope and implication (R-32302.11) => (R-32302.12).

Not asserted:

1. impossibility of all shifted common-zero cancellations in (R-32302.13);
2. RH from the smoothed kernel alone;
3. a subpower critical discrepancy.
