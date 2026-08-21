# L-91014 — The generalized-Jordan cocycle is a coefficient-one divisor-splitting isometry

Claim ID: `L-91014`  
Status: **PROPOSED COMPLETE EXACT POSITIVE-SOURCE THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: `L-91012` (the positive generalized-Jordan/sieve cocycle)  
RH status: **unproved**

## 1. The positive sieve coefficients

For `a>0`, put

\[
 Q_a(s)=\frac{\zeta(s)}{\zeta(s+2a)}
       =\sum_{n\ge1}\frac{q_a(n)}{n^s},
 \qquad
 q_a(n)=\prod_{p\mid n}(1-p^{-2a})>0.
\]

The cocycle

\[
 Q_{a+b}(s)=Q_a(s)Q_b(s+2a)
\]

implies the exact coefficient identity

\[
 \boxed{
 q_{a+b}(n)
 =\sum_{de=n}q_a(d)q_b(e)e^{-2a\log e}.
 }
 \tag{L-91014.1}
\]

Every term is nonnegative.

## 2. Divisor-splitting probabilities

For `de=n`, define

\[
 \pi_{a,b}(d,e\mid n)
 =\frac{q_a(d)q_b(e)e^{-2a\log e}}{q_{a+b}(n)}.
 \tag{L-91014.2}
\]

Then

\[
 \pi_{a,b}(d,e\mid n)\ge0,
 \qquad
 \sum_{de=n}\pi_{a,b}(d,e\mid n)=1.
 \tag{L-91014.3}
\]

Thus the analytic cocycle carries a canonical, lossless, state-dependent divisor fragmentation law.

## 3. The coefficient-one isometry

Let `H_c=ell^2(N)` with standard basis `e_n`. Define

\[
 \boxed{
 V_{a,b}e_n
 =\sum_{de=n}\sqrt{\pi_{a,b}(d,e\mid n)}\,e_d\otimes e_e.
 }
 \tag{L-91014.4}
\]

The factorisation supports for distinct `n` are disjoint. Hence

\[
 \boxed{V_{a,b}^*V_{a,b}=I.}
 \tag{L-91014.5}
\]

No coefficient loss, rowwise absolute value, or asymptotic normalisation occurs.

## 4. Coherent vectors factor exactly

For `Re(s)>1/2`, put

\[
 k_{c,s}=\sum_{n\ge1}\sqrt{q_c(n)}n^{-s}e_n\in H_c.
 \tag{L-91014.6}
\]

Its norm is

\[
 \|k_{c,s}\|^2=Q_c(2\Re s).
 \tag{L-91014.7}
\]

Using (L-91014.1) inside (L-91014.4) gives

\[
 \boxed{
 V_{a,b}k_{a+b,s}
 =k_{a,s}\otimes k_{b,s+a}.
 }
 \tag{L-91014.8}
\]

Taking inner products yields the positive-kernel cocycle

\[
 \boxed{
 Q_{a+b}(s+\bar t)
 =Q_a(s+\bar t)Q_b(s+\bar t+2a)
 }
 \tag{L-91014.9}
\]

on the full half-plane `Re(s),Re(t)>1/2`. In particular, each

\[
 K_a(s,t)=Q_a(s+\bar t)
\]

is a positive-definite kernel there.

## 5. Exact logarithmic coproduct

Let

\[
 Le_n=(\log n)e_n.
\]

Since `log(de)=log d+log e`,

\[
 \boxed{
 V_{a,b}L=(L\otimes I+I\otimes L)V_{a,b}.
 }
 \tag{L-91014.10}
\]

Consequently, for every polynomial `P`,

\[
 V_{a,b}P(L)
 =P(L\otimes I+I\otimes L)V_{a,b}.
 \tag{L-91014.11}
\]

The first two jets are therefore

\[
\begin{aligned}
 L&\mapsto L_1+L_2,\\
 L^2&\mapsto L_1^2+2L_1L_2+L_2^2.
\end{aligned}
 \tag{L-91014.12}
\]

This is the exact positive-source analogue of the three-state/symmetric-square algebra in the dyadic Cauchy all-pass completion.

## 6. Associativity

The maps `V_(a,b)` satisfy the natural pentagon identity after the canonical reassociation of tensor products. Both routes from `H_(a+b+c)` to `H_a tensor H_b tensor H_c` send `e_n` to the square-root weights

\[
 \frac{q_a(d)q_b(e)q_c(f)e^{-2a\log e-2(a+b)\log f}}
      {q_{a+b+c}(n)},
 \qquad def=n.
 \tag{L-91014.13}
\]

Thus the positive source forms a genuine coassociative dyadic/multiscale system.

## 7. Exact critical-pole coefficient

Put

\[
 \kappa_a=\frac1{\zeta(1+2a)}.
\]

Then

\[
 Q_a(s)=\frac{\kappa_a}{s-1}+O_a(1)
 \qquad(s\to1),
 \tag{L-91014.14}
\]

and

\[
 Q_b(1+2a)=\frac{\kappa_{a+b}}{\kappa_a}.
 \tag{L-91014.15}
\]

Hence the factorisation (L-91014.8) transports the divergent boundary state with exact coefficient one:

\[
 \frac{\kappa_a}{2\varepsilon}\,
 Q_b(1+2a)
 =\frac{\kappa_{a+b}}{2\varepsilon}.
 \tag{L-91014.16}
\]

Equivalently, the second tensor factor

\[
 \eta_{a,b,x}
 =\frac{k_{b,\,1/2+a+ix}}{\sqrt{Q_b(1+2a)}}
 \tag{L-91014.17}
\]

is a unit vector and the leading Hardy-pole state returns with coefficient exactly one. This is the source-side no-double-spend normalisation required by a delayed recurrence.

## 8. Boundary

Established here:

```text
positive divisor fragmentation at every scale;
coefficient-one Hilbert-space isometry;
exact coherent-vector tensor factorisation;
exact logarithmic jet coproduct;
coassociative all-generation source flow;
coefficient-one transport of the critical pole state.
```

Not established here:

```text
pole-subtracted critical-boundary positivity;
windowed/carry recombination after the isometry;
the dyadic Cauchy-square gate;
RH.
```
