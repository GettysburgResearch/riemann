# L-15154 — Prime/full-von-Mangoldt normal-energy bridge

Claim ID: `L-15154`  
Title: A compact safe window gives polynomially equivalent ordinary-prime and full-von-Mangoldt block energies, both in the adjoint/normal orientation  
Status: **PROPOSED EXACT LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-07  
Review input: the post-review bridge in the frozen PR #158 audit  
Dependencies: `L-15153`; PR #216 `T-21502/L-21504`  
Scope: exact orientation bridge and prime-power tail estimate; no Type-II bound

## 1. Two compact safe signals

Let `H` be the fixed compact ordinary-prime safe window of `T-21502`. Write

\[
 \operatorname{supp}H\subseteq[A,B],
 \qquad
 \|H\|_\infty\le C_H.
 \tag{L-15154.1}
\]

Define

\[
 Q_H^{\mathbb P}(x)
 =\sum_p {\log p\over\sqrt p}H(x-\log p)
 \tag{L-15154.2}
\]

and

\[
 Q_H^{\Lambda}(x)
 =\sum_{n\ge2}{\Lambda(n)\over\sqrt n}H(x-\log n).
 \tag{L-15154.3}
\]

Both sums are finite for every real `x`.

For an integer logarithmic block `J`, put

\[
 \mathcal B_J^{\mathbb P}
 =\int_J^{J+1}|Q_H^{\mathbb P}(x)|^2dx,
 \qquad
 \mathcal B_J^{\Lambda}
 =\int_J^{J+1}|Q_H^{\Lambda}(x)|^2dx.
 \tag{L-15154.4}
\]

## 2. Exact prime-power remainder

The difference is

\[
 \boxed{
 R_H(x)=Q_H^{\Lambda}(x)-Q_H^{\mathbb P}(x)
 =\sum_{k\ge2}\sum_p
 {\log p\over p^{k/2}}
 H(x-k\log p).}
 \tag{L-15154.5}
\]

For `x in [J,J+1]`, a nonzero summand satisfies

\[
 {x-B\over k}\le\log p\le {x-A\over k}.
 \tag{L-15154.6}
\]

### The square layer

For `k=2`, enlarge the prime sum to all integers. The interval in (L-15154.6)
has a fixed multiplicative ratio depending only on `H`, so integral comparison
gives

\[
\begin{aligned}
 \sum_{\exp((x-B)/2)\le p\le\exp((x-A)/2)}
 {\log p\over p}
 &\le
 \sum_{\exp((x-B)/2)\le m\le\exp((x-A)/2)}
 {\log m\over m}\\
 &\le C_H'(1+J).
\end{aligned}
 \tag{L-15154.7}
\]

No prime number theorem is used.

### Every higher layer

For `k>=3`, discard the support restriction and enlarge primes to integers:

\[
\begin{aligned}
 \sum_{k\ge3}\sum_p{\log p\over p^{k/2}}
 &\le
 \sum_{m\ge2}\log m
 \sum_{k\ge3}m^{-k/2}\\
 &=
 \sum_{m\ge2}{\log m\,m^{-3/2}\over1-m^{-1/2}}
 <\infty.
\end{aligned}
 \tag{L-15154.8}
\]

Consequently

\[
 \boxed{
 \sup_{J\le x\le J+1}|R_H(x)|
 \le C_H''(1+J).}
 \tag{L-15154.9}
\]

This is the exact bridge identified in the second-pass review: the prime-square
layer costs `O_H(J)` pointwise and all higher powers cost `O_H(1)`.

## 3. Polynomial equivalence of block energies

Using

\[
 |u+v|^2\le2|u|^2+2|v|^2,
\]

and (L-15154.9),

\[
 \boxed{
 \mathcal B_J^{\Lambda}
 \le2\mathcal B_J^{\mathbb P}+C_H(1+J)^2,}
 \tag{L-15154.10}
\]

and symmetrically

\[
 \boxed{
 \mathcal B_J^{\mathbb P}
 \le2\mathcal B_J^{\Lambda}+C_H(1+J)^2.}
 \tag{L-15154.11}
\]

Therefore the following properties are equivalent for the two block families:

1. polynomial growth in `J`;
2. `exp(o(J))` growth;
3. zero upper exponential block exponent.

In particular, either family may be used at the final Hardy interface.

## 4. Exact normal orientation

On logarithmic coordinates define the causal translation operators

\[
 (\mathsf T_yf)(x)=f(x-y)
 \tag{L-15154.12}
\]

and the source operators

\[
 \mathcal P_{\mathbb P}
 =\sum_p{\log p\over\sqrt p}\mathsf T_{\log p},
 \qquad
 \mathcal P_{\Lambda}
 =\sum_{n\ge2}{\Lambda(n)\over\sqrt n}\mathsf T_{\log n}.
 \tag{L-15154.13}
\]

At every finite block these sums act through finitely many translations. If
`chi_J` denotes multiplication by `1_[J,J+1]`, then

\[
 \boxed{
 \mathcal B_J^{\mathbb P}
 =\langle H,
 \mathcal P_{\mathbb P}^*\chi_J
 \mathcal P_{\mathbb P}H\rangle,}
 \tag{L-15154.14}
\]

and

\[
 \boxed{
 \mathcal B_J^{\Lambda}
 =\langle H,
 \mathcal P_{\Lambda}^*\chi_J
 \mathcal P_{\Lambda}H\rangle.}
 \tag{L-15154.15}
\]

Expanding either form gives the factor-ratio Gram

\[
 \sum_{m,n}{a_m a_n\over\sqrt{mn}}
 K_J(\log m,\log n),
 \tag{L-15154.16}
\]

not the product-dilation form `Re <f,U_(mn)f>` appearing in
`L-15152/R-15113`.

Thus the exact geometry compatible with the empirical PR #216 cancellation and
the prime/full-`Lambda` bridge is the localized normal operator

\[
 \boxed{
 \mathcal P^*\chi_J\mathcal P.}
 \tag{L-15154.17}
\]

## 5. Consequence for a repaired Selberg connection

Any use of the exact Selberg identities may now pass through the full
von-Mangoldt source without changing polynomial or subexponential block status.
However, it must return to the normal form (L-15154.15). The same-orientation
operator `mathcal P^2` and the normal operator `mathcal P^*chi_J mathcal P` are
not interchangeable.

A valid completion may therefore use:

1. full-`Lambda` coefficient identities to decompose the source;
2. rowwise centering in the null-mode quotient of `L-15155`;
3. adjoint/normal Type-I and Type-II energies;
4. a scale-contracting auxiliary-energy theorem.

## 6. Proof boundary

Closed here:

- the exact prime-power difference;
- the uniform `O_H(J)` block bound;
- polynomial/subexponential equivalence of prime and full-`Lambda` blocks;
- the exact normal-operator representation.

Not closed:

- a subexponential estimate for either block family;
- a Type-II or auxiliary-energy recurrence;
- RH.
