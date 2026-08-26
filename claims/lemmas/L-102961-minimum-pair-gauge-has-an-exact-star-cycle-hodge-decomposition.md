# L-102961 — The minimum-pair gauge has an exact star/cycle Hodge decomposition

Claim ID: `L-102961`  
Status: **PROVED EXACT OWNER-GAUGE HODGE DECOMPOSITION**  
Created: 2026-08-25  
Depends on: `L-102746--L-102747`; PR #730 `T-105440`, `L-105432--L-105452`  
RH status: **not assumed**

Fix one squarefree labelled occurrence

\[
S=\{p_1<\cdots<p_k\},
\qquad k\ge4.
\]

Let \(e_{ij}=\binom{k}{2}^{-1}\) be its canonical equal-pair Duhamel allocation and let \(m_{ij}\) be the minimum-pair allocation

\[
m_{12}=1,
\qquad
m_{ij}=0\quad((i,j)\ne(1,2)).
\]

Put

\[
w_{ij}=m_{ij}-e_{ij}.
\]

Then

\[
\sum_{i<j}w_{ij}=0.
\tag{L-102961.1}
\]

## 1. Exact vertex/star component

Define the row sums

\[
r_i=\sum_{j\ne i}w_{ij}.
\]

A direct calculation gives

\[
\boxed{
r_1=r_2={k-2\over k},
\qquad
r_i=-{2\over k}\quad(i\ge3).
}
\tag{L-102961.2}
\]

Since \(\sum_i r_i=0\), put

\[
a_i={r_i\over k-2}
\]

and

\[
g_{ij}=a_i+a_j.
\]

Then the row sums of \(g\) equal those of \(w\). Hence

\[
\boxed{c_{ij}:=w_{ij}-g_{ij}}
\]

has zero row sums:

\[
\sum_{j\ne i}c_{ij}=0
\qquad(1\le i\le k).
\tag{L-102961.3}
\]

Thus

\[
\boxed{w=g+c}
\tag{L-102961.4}
\]

is the orthogonal decomposition into the complete-graph star space and the row-zero cycle space.

## 2. Exact energies

The three components satisfy

\[
\boxed{
\|w\|^2=1-{1\over\binom{k}{2}},
}
\tag{L-102961.5}
\]

\[
\boxed{
\|g\|^2={2\over k},
}
\tag{L-102961.6}
\]

and

\[
\boxed{
\|c\|^2={k-3\over k-1}.
}
\tag{L-102961.7}
\]

The star and cycle terms are orthogonal because every cycle row sum vanishes.

## 3. Source interpretation

Under the source-exact pair-gauge transfer:

```text
star component g:
  a linear combination of radial actual-owner currents;
  every difference factors by T-105440.3 into one native endpoint boundary
  minus one squared endpoint boundary;

cycle component c:
  the row-zero pair current;
  T-105440.8 localizes its norm exactly to four-label Pluecker rectangles;
  L-105451 identifies each clean rectangle with two nontrivial augmentation
  local systems.
```

Therefore the minimum-owner incidence current is not an arbitrary label-collapse error. It is the sum of one endpoint current and one balanced Pluecker cycle current on the same occurrence.

## Binding scope

The cycle energy tends to one:

\[
\|c\|^2\to1
\qquad(k\to\infty).
\]

Hence transferring from equal-pair to minimum-pair ownership is polylogarithmically bounded but not subcritical by owner combinatorics alone. A proof must orient the endpoint and Pluecker currents arithmetically; pair-gauge averaging cannot simply discard them.