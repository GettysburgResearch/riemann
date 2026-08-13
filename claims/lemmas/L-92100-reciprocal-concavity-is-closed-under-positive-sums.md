# L-92100 — Reciprocal concavity is closed under positive sums

Claim ID: `L-92100`  
Status: **PROVED EXACT DIFFERENTIAL INEQUALITY**  
Created: 2026-08-13  
Depends on: none  
RH status: **unproved**

## 1. Curvature functional

For a positive `C^2` function `f` on an interval define

\[
 \boxed{
 \mathcal E[f]=ff''-2(f')^2.
 }
 \tag{L-92100.1}

Since

\[
 \left(\frac1f\right)''
 =-\frac{\mathcal E[f]}{f^3},
\]

one has

\[
 \boxed{
 \mathcal E[f]\ge0
 \quad\Longleftrightarrow\quad
 1/f\text{ is concave}.
 }
 \tag{L-92100.2}

Scaling preserves the sign:

\[
 \mathcal E[cf]=c^2\mathcal E[f]
 \qquad(c>0).
 \tag{L-92100.3}

## 2. Closure theorem

Let `f,g>0` be `C^2` and suppose

\[
 \mathcal E[f]\ge0,
 \qquad
 \mathcal E[g]\ge0.
\]

Then

\[
 \boxed{
 \mathcal E[f+g]\ge0.
 }
 \tag{L-92100.4}

Indeed,

\[
\begin{aligned}
 \mathcal E[f+g]
 ={}&\mathcal E[f]+\mathcal E[g]
 +fg''+gf''-4f'g'.
\end{aligned}
\]

The hypotheses give

\[
 f''\ge\frac{2(f')^2}{f},
 \qquad
 g''\ge\frac{2(g')^2}{g},
\]

so the cross term obeys

\[
\begin{aligned}
 fg''+gf''-4f'g'
 &\ge
 2\frac f g(g')^2
 +2\frac g f(f')^2
 -4f'g'\\
 &=2\left(
  \sqrt{\frac g f}f'
  -\sqrt{\frac f g}g'
 \right)^2\ge0.
\end{aligned}
\]

This proves the claim.

## 3. Infinite sums

Let `f_n>0` satisfy `E[f_n]>=0`, and suppose the series of `f_n` and its first
two derivatives converges locally uniformly.  Every finite partial sum has
concave reciprocal by the closure theorem.  Passing to the limit gives

\[
 \boxed{
 \mathcal E\left[\sum_n f_n\right]\ge0.
 }
 \tag{L-92100.5}

## 4. Parallel-sum interpretation

Writing

\[
 a=1/f,
 \qquad b=1/g,
\]

one has

\[
 \frac1{f+g}=\frac{ab}{a+b}.
\]

The scalar parallel-sum map `(a,b) -> ab/(a+b)` is jointly concave and
coordinatewise increasing on the positive quadrant.  Equation (L-92100.4) is
its differential proof.

## 5. Exact boundary

```text
reciprocal concavity functional               EXACT
closure under scaling                         EXACT
closure under finite positive sums            EXACT
closure under locally C2-convergent sums       EXACT
application to critical/off-line orbit blocks  L-92101--L-92103
Riemann Hypothesis                             UNPROVED
```
