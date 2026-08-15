# L-92893 — Direct native slack of the one-shot row is below 61000

Claim ID: `L-92893`  
Status: **PROPOSED COMPLETE DIRECT \(Y_4\)-COST THEOREM ON FROZEN ANALYTIC ESTIMATES — REVIEW REQUIRED**  
Created: 2026-08-15  
Depends on: `L-91378`, `L-92891`, radix-four dual sparsity, the unconditional native benchmark bound, and the fixed terminal omission estimate  
Forbidden input: an upper estimate for \(J_\Lambda(X)-4\sqrt X\)  
RH status: **unproved at this claim**

Let

\[
r_X=\Omega_X-\Xi(d_X)\ge0
\]

be the numerical slack proved in `L-92891`, and put

\[
\delta_X=\langle Y_4,r_X\rangle.
\tag{L-92893.1}
\]

## 1. Exact dual identity

The positive radix-four dual is

\[
Y_4(q)=\sum_{k=0}^{v_4(q)}2^k\Lambda(q/4^k),
\]

and satisfies

\[
Y_4(q)-2\mathbf1_{4\mid q}Y_4(q/4)=\Lambda(q).
\]

Finite summation by parts gives

\[
\mathcal H(d_X)=\sum_qY_4(q)\Xi(d_X)(q),
\qquad
J_\Lambda(X)=\sum_qY_4(q)\Omega_X(q).
\]

Therefore

\[
\boxed{
\delta_X
=
J_\Lambda(X)-\mathcal H(d_X).
}
\tag{L-92893.2}
\]

## 2. Named slack classes

The external slack is bounded by four disjoint numerical classes:

```text
one global square-root thinning;
the nonterminal retained-cell and intrinsic-collar comparison;
the terminal comparison;
bottom/top omissions.
```

Hall, first-owner, causal-current and internal-child operations are exact in the
total row. By `L-92892` there is no port term, and there is no large-endpoint
base term.

## 3. Thinning cost

For

\[
\tau_K=\frac{\sqrt K}{\sqrt K+130},
\]

the unconditional positive benchmark estimate gives

\[
(1-\tau_K)J_\Lambda(X)<12012
\qquad(X\ge10^{12}).
\tag{L-92893.3}
\]

This estimate uses only a positive upper bound for \(J_\Lambda\), not an
RH-bearing comparison with \(4\sqrt X\).

## 4. Nonterminal cost

Radix-four dual sparsity gives

\[
\sum_{q\le X}\frac{Y_4(q)}q
\le
3+2L+2L^2,
\qquad L=\log(2X).
\]

Together with the all-column bound in `L-92891`,

\[
\delta_X^{\rm nonterm}
\le
\frac{971}{4\sqrt K}
\bigl(3+2L+2L^2\bigr)
<4
\quad(X\ge10^{12}).
\tag{L-92893.4}
\]

## 5. Terminal cost

The exact support formula for \(Y_4\) yields

\[
\sum_{q\ge2}\frac{Y_4(q)}{q^{3/2}}<11.
\]

The complete terminal comparison is at most \(4452X^{-3/2}\) in each possible
terminal coordinate, hence

\[
\delta_X^{\rm term}<4452\cdot11=48972.
\tag{L-92893.5}
\]

## 6. Omissions

The positive endpoint-score derivative and the bounded equality density imply
that the width-two bottom transition and fixed-width top omission have combined
literal score below one for \(X\ge10^{12}\):

\[
\delta_X^{\rm omit}<1.
\tag{L-92893.6}
\]

## 7. Total

Combining the named classes,

\[
\boxed{
0\le\delta_X
<
12012+4+48972+1
=
60989
<
61000.
}
\tag{L-92893.7}
\]

No term is charged both as current response and as unused slack.

```text
slack vector                                 DIRECTLY NONNEGATIVE
positive-source interpretation of slack      NOT REQUIRED
thinning                                     <12012
nonterminal comparison                       <4
terminal comparison                          <48972
omissions                                    <1
auxiliary port/base                          ZERO
complete native deficit                      <61000
RH-bearing benchmark bridge                  FORBIDDEN
Riemann Hypothesis                           UNPROVED AT THIS CLAIM
```
