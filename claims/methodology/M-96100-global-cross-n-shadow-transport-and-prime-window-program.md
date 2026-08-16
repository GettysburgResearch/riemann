# M-96100 — Global cross-n shadow transport and the exact prime-window producer

Claim ID: `M-96100`  
Status: **PROPOSED RESEARCH PROGRAM / FIRST OPEN THEOREM**  
Created: 2026-08-16  
Depends on: `R-96100`, `L-96100--L-96102`  
RH status: **unproved**

## 1. Why a global transport is unavoidable

The grouped coefficient sequence

\[
 \omega_{P,j}(n)=\sum_{d\mid(n,P)}\mu(d)q_j(n/d)
\]

has negative entries. For example,

\[
 \omega_{2,2}(4)=-2.
\]

The positive rough reservoir and the signed frontier in `L-96100.11` live at
different products `n`. Therefore a valid proof must transport capacity between
distinct logarithmic knots and record global ownership.

The one-prime theorem `L-96101` gives the first such transport. It spends
`2/j` units of the edge atom. Applying that packet independently to many primes
would reuse the same edge reservoir, so it cannot be superposed.

## 2. Exact call-order state

For fixed `P,j`, define

\[
 a_n=\frac{\omega_{P,j}(n)}{\sqrt n},
\]

\[
 M(N)=\sum_{n\le N}a_n,
 \qquad
 L(N)=\sum_{n\le N}a_n\log n,
\]

and

\[
 V(N)=\log N\,M(N)-L(N).
\tag{M-96100.1}
\]

Then

\[
 V(N)=e^{-\log N/2}\mathfrak S_{P,j}(N).
\]

Between consecutive integer knots, the potential is affine in `log Y`.
Consequently the universal sieve theorem is exactly

\[
 \boxed{V(N)\ge0\quad(N\ge1).}
\tag{M-96100.2}
\]

No componentwise sign of `a_n` is required.

## 3. Canonical one-use shadow compiler

For a finite activation range, split

\[
 \nu^+=\sum_{a_n>0}a_n\delta_{\log n},
 \qquad
 \nu^-=\sum_{a_n<0}(-a_n)\delta_{\log n}.
\]

A reviewable transport certificate consists of nonnegative packets of two
forms:

1. monotone packets
   \[
   \eta(\delta_a-\delta_b),\qquad a<b;
   \]
2. convex packets
   \[
   \eta\bigl[
    \lambda\delta_a+(1-\lambda)\delta_c-\delta_b
   \bigr],
   \quad a<b<c,
   \quad b\ge\lambda a+(1-\lambda)c.
   \]

The inequality on the barycentre is oriented for a decreasing convex test
kernel. Every positive atom receives one owner and every negative atom is paid
once.

There is a canonical greedy realization: process negative atoms in increasing
logarithmic position and take their left and right shadows from the nearest
unused positive reservoirs, splitting the terminal atoms when necessary. For a
fixed finite signed measure, this compiler succeeds if and only if its call
potential is nonnegative at every activation knot.

Thus the compiler is a deterministic ownership mechanism, not a proof of the
universal inequality. The missing theorem is that it succeeds for the exact
arithmetic measures `nu_(P_r,j)` for all `r,j`.

## 4. Prime-window form at full activation

At endpoint `Y>=j^2`, take the complete active product

\[
 P(Y/j)=\prod_{p\le Y/j}p.
\]

`L-96102` gives the exact decomposition

\[
\begin{aligned}
 \mathcal F_j(Y)
={}&C_j\log Y
 +C_j\sum_{Y/j<p\le Y}
   \frac{\log(Y/p)}{\sqrt p}\\
&+
 \sum_{m=1}^{j+1}
 \frac{h_j(m)}{\sqrt m}
 \sum_{\substack{d\mid P(Y/j)\\d\le Y/m}}
  \frac{\mu(d)}{\sqrt d}\log\frac{Y}{dm}.
\end{aligned}
\tag{M-96100.3}
\]

The first line is positive. The second line is the complete signed frontier.
The conclusion-producing producer can therefore be stated without transport
language:

> **Global prime-window frontier inequality.** Prove that the right-hand side
> of (M-96100.3) is nonnegative for every `j>=2` and every `Y>=j^2`, together
> with the finite range `j<=Y<j^2`.

This is exactly the discrete-tail row positivity consumed by PR #542.

## 5. Why local capacity estimates are insufficient

At full activation the positive rough atoms below `Y` are only

```text
1 and primes in (Y/j,Y].
```

They are not all integers in a block. Therefore a capacity estimate such as

\[
 \sum_{m=u}^{pu-1}m^{-1/2}
\]

cannot be charged as available rough capacity unless each integer in that sum
is given an actual unsieved owner. A correct proof must use the real top-prime
reservoir or an exactly equivalent signed cancellation.

## 6. Strongest honest route boundary

```text
one-prime global transport                   PROVED
multi-prime source decomposition             PROVED EXACTLY
canonical ownership compiler                 DEFINED
universal compiler success                   OPEN
full active prime-window formula             PROVED EXACTLY
prime-window frontier inequality             OPEN / RH-BEARING
PR #542 consumer after positivity             AVAILABLE
Riemann Hypothesis                            UNPROVED
```

A future complete successor should either prove (M-96100.2)/(M-96100.3), or
replace the row entirely. It must not reuse the fixed-product FRONTIER-CHAIN.
