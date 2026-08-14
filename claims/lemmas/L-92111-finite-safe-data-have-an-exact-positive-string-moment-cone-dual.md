# L-92111 — Finite safe data have an exact positive-string moment-cone dual

Claim ID: `L-92111`  
Status: **PROVED FINITE PRIMAL/DUAL STRING THEOREM**  
Created: 2026-08-14  
Depends on: `L-92110`; finite-dimensional separation and Caratheodory's theorem  
RH status: **unproved**

## 1. Normalized string kernel

Fix a safe anchor `r>0` and distinct positive nodes

\[
 q_1=r,q_2,\ldots,q_N.
\]

Let

\[
 \overline{\mathbb R}_+=[0,\infty]
\]

be the one-point compactification and define

\[
 \boxed{
 K_j(s)=\frac{r+s}{q_j+s},
 \qquad
 K_j(\infty)=1.
 }
 \tag{L-92111.1}
\]

In particular

\[
 K_1(s)=1
\]

for every `s`.

## 2. Four equivalent finite certificates

Let `y=(y_1,...,y_N)` with `y_1>=0`. The following are equivalent.

### A. Generalized Stieltjes interpolation

There is a generalized Stieltjes function

\[
 f(z)=a/z+b+\int_{(0,\infty)}\frac{d\mu(s)}{z+s}
\]

such that

\[
 f(q_j)=y_j
 \qquad(1\le j\le N).
\]

### B. Compact positive moment representation

There is a positive finite measure `nu` on `[0,infinity]` such that

\[
 \boxed{
 y_j=\int K_j(s)d\nu(s)
 \qquad(1\le j\le N).
 }
 \tag{L-92111.2}
\]

Its total mass is forced:

\[
 \nu([0,\infty])=y_1.
 \tag{L-92111.3}
\]

### C. Finite dual-cone inequalities

For every real vector `c=(c_1,...,c_N)`,

\[
 \boxed{
 \sum_{j=1}^Nc_jK_j(s)\ge0
 \quad\text{for every }s\in[0,\infty]
 }
 \tag{L-92111.4}
\]

implies

\[
 \boxed{
 \sum_{j=1}^Nc_jy_j\ge0.
 }
 \tag{L-92111.5}
\]

### D. A finite positive string with at most `N` atoms

There are points

\[
 s_1,\ldots,s_m\in[0,\infty],
 \qquad m\le N,
\]

and weights `w_l>=0` such that

\[
 \boxed{
 y_j=\sum_{\ell=1}^m w_\ell K_j(s_\ell).
 }
 \tag{L-92111.6}
\]

## 3. Proof

A generalized Stieltjes representation gives (B) by the anchor renormalization

\[
 d\nu(s)=\frac{d\mu(s)}{r+s}
\]

on `(0,infinity)`, with masses `a/r` at zero and `b` at infinity. The reverse transformation is exactly the boundary-atom reconstruction in `L-92110`. Thus (A) and (B) are equivalent.

(B) implies (C) by integration.

For the converse, the map

\[
 s\longmapsto(K_1(s),\ldots,K_N(s))
\]

has compact image. Because `K_1=1`, all representing vectors of total mass `y_1` lie in the compact convex set

\[
 y_1\operatorname{conv}\{K(s):s\in[0,\infty]\}.
\]

If `y` were outside this set, finite-dimensional strict separation would give a vector `c` satisfying (L-92111.4) but violating (L-92111.5). Hence (C) implies (B).

Finally, Caratheodory's theorem in the affine hyperplane with first coordinate one represents every point of the convex hull by at most `N` generators. Thus (B) and (D) are equivalent.

## 4. Exact univariate-polynomial dual

If all nodes and `r` are rational, define

\[
 D(s)=\prod_{i=1}^N(q_i+s)>0
 \qquad(s\ge0).
\]

For a dual vector `c`, put

\[
 \boxed{
 P_c(s)
 =(r+s)\sum_{j=1}^Nc_j
       \prod_{i\ne j}(q_i+s).
 }
 \tag{L-92111.7}
\]

Then

\[
 \sum_jc_jK_j(s)=\frac{P_c(s)}{D(s)}.
 \tag{L-92111.8}
\]

Consequently the dual premise (L-92111.4) is exactly the univariate polynomial condition

\[
 \boxed{P_c(s)\ge0\quad(s\ge0).}
 \tag{L-92111.9}
\]

This can be certified by exact root isolation, a half-line sum-of-squares certificate, or a directed Sturm calculation. A vector `c` with `P_c>=0` and `c dot y<0` is an exact finite obstruction to a positive string.

## 5. Safe-Xi consequence

Enumerate a dense set

\[
 q_1=r,q_2,\ldots
 \subset\mathbb Q\cap(1/4,\infty)
\]

and put

\[
 y_j=
 \frac{\Xi'(\sqrt{q_j})}
      {\sqrt{q_j}\,\Xi(\sqrt{q_j})}.
\]

If every finite vector `(y_1,...,y_N)` satisfies the equivalent conditions above, choose the at-most-`N`-atom interpolant from (D). Its anchor value is exactly `y_1`, independently of `N`. The hypotheses of `L-92110` therefore hold with zero interpolation error, and RH follows.

Conversely RH supplies the critical-zero Stieltjes measure and hence every finite certificate. Subject to the analytic interface of `L-92100`,

\[
\boxed{
\mathrm{RH}
\iff
\text{every finite safe Xi data vector belongs to this string moment cone}.
}
\tag{L-92111.10}
\]

## 6. Strategic form of the final producer

At stage `N`, the arithmetic source has two fail-closed options:

```text
PRIMAL: return at most N positive string atoms and weights satisfying (L-92111.6);
DUAL:   return c with P_c(s)>=0 on the half-line and c dot y<0.
```

The primal certificates automatically glue by `L-92110`. No separate all-order compatibility proof or infinite string limit is required.

## 7. Exact boundary

```text
finite Stieltjes interpolation <-> compact moment cone   PROVED
finite moment cone <-> at most N positive atoms          PROVED
exact polynomial dual                                    PROVED
all finite Xi moment-cone memberships -> RH              PROVED CONDITIONAL
arithmetic proof of every finite membership               OPEN / RH-BEARING
Riemann Hypothesis                                        UNPROVEN
```
