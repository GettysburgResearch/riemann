# L-92000 — The three-node Carathéodory determinant factors into two scalar curvatures

Claim ID: `L-92000`  
Status: **PROVED EXACT FINITE ALGEBRA**  
Created: 2026-08-13  
Depends on: `L-91904/L-91905` on PR #438  
RH status: **unproved**

## 1. The safe infinitesimal kernel

Let

\[
 F:(0,\infty)\longrightarrow(0,\infty)
\]

be a positive function and put

\[
 \boxed{
 p(t)=\frac{F(\sqrt t)}{\sqrt t},
 \qquad t>0.
 }
 \tag{L-92000.1}
\]

For positive nodes `x_i` define

\[
 \boxed{
 H_{ij}=\frac{F(x_i)+F(x_j)}{x_i+x_j}.
 }
 \tag{L-92000.2}
\]

For the actual Xi function,

\[
 F(x)=\frac{\Xi'(x)}{\Xi(x)},
 \qquad
 \Xi(x)=\xi\left(\frac12+x\right),
\]

this is the infinitesimal safe Pick matrix of `L-91904`.

Write

\[
 t_i=x_i^2,
 \qquad
 p_i=p(t_i).
\]

Then

\[
 H_{ij}=\frac{x_ip_i+x_jp_j}{x_i+x_j}.
 \tag{L-92000.3}
\]

## 2. One- and two-node minors

The diagonal is

\[
 H_{ii}=p_i.
\]

For two distinct nodes,

\[
 \boxed{
 \det H[\{i,j\}]
 =-\frac{(p_i-p_j)(t_ip_i-t_jp_j)}{(x_i+x_j)^2}.
 }
 \tag{L-92000.4}
\]

Consequently every two-node minor is positive whenever

```text
p is decreasing;
t p(t) is increasing.
```

This is exactly the pair of monotonicities established for the actual Xi
function in `L-91905`.

## 3. Second divided differences

For distinct real numbers `t_1,t_2,t_3` and a scalar function `f`, write

\[
 [t_1,t_2,t_3]f
 =\sum_{i=1}^3
 \frac{f(t_i)}{\prod_{j\ne i}(t_i-t_j)}.
 \tag{L-92000.5}
\]

Let

\[
 \Delta(t)
 =(t_2-t_1)(t_3-t_1)(t_3-t_2).
 \tag{L-92000.6}
\]

## 4. Exact three-node factorization

For `0<x_1<x_2<x_3`, direct determinant expansion gives

\[
\boxed{
\begin{aligned}
 \det H
 ={}&
 \frac{
  p_1p_2p_3\,\Delta(t)^2
 }{
  \prod_{1\le i<j\le3}(x_i+x_j)^2
 }\\
 &\times
 [t_1,t_2,t_3]\!\left(\frac1p\right)
 [t_1,t_2,t_3](tp).
\end{aligned}
}
\tag{L-92000.7}
\]

### Proof

Writing out the determinant and collecting its two irreducible factors gives

\[
\begin{aligned}
 \det H
={}&\frac{A\,B}
 {(x_1+x_2)^2(x_1+x_3)^2(x_2+x_3)^2},
\end{aligned}
\]

where

\[
\begin{aligned}
 A={}&p_1p_2(t_1-t_2)-p_1p_3(t_1-t_3)
      +p_2p_3(t_2-t_3),\\
 B={}&t_1p_1(t_2-t_3)+t_2p_2(t_3-t_1)
      +t_3p_3(t_1-t_2).
\end{aligned}
\]

The definitions imply

\[
 A=-p_1p_2p_3\,\Delta(t)
 [t_1,t_2,t_3](1/p),
\]

and

\[
 B=-\Delta(t)[t_1,t_2,t_3](tp).
\]

Multiplying proves (L-92000.7).

## 5. Curvature criterion

Assume

```text
p>0;
p decreases;
tp increases;
1/p is concave;
tp is concave.
```

Then every principal minor of every three-node matrix is nonnegative:

- order one: `p_i>0`;
- order two: (L-92000.4);
- order three: both second divided differences in (L-92000.7) are
  nonpositive.

Hence

\[
 \boxed{H[x_1,x_2,x_3]\succeq0.}
 \tag{L-92000.8}
\]

If `tp` is strictly concave, the converse at order three is also true:
positivity for every three-node packet forces `1/p` to be concave.
Indeed the prefactor in (L-92000.7) is positive and
`[t_1,t_2,t_3](tp)<0`.

## 6. Confluent form

Let the three nodes coalesce.  Since a second divided difference tends to
one half of the second derivative, the first genuinely order-three local
conditions are

\[
 \boxed{
 \left(\frac1p\right)''\le0,
 \qquad
 (tp)''\le0.
 }
 \tag{L-92000.9}
\]

The first inequality is

\[
 \boxed{
 p\,p''-2(p')^2\ge0.
 }
 \tag{L-92000.10}
\]

Thus the full three-node problem is not a mysterious matrix sign: it is the
simultaneous concavity of two explicit scalar functions.

## 7. Exact boundary

```text
one-node minor                                      EXACT
two-node factorization                              EXACT
three-node determinant factorization                EXACT
three-node PSD from two scalar concavities          EXACT
converse when tp is strictly concave                EXACT
actual-Xi tp concavity                              HANDLED IN L-92001
actual-Xi reciprocal concavity                      OPEN / ORDER-THREE GATE
Riemann Hypothesis                                  UNPROVED
```
