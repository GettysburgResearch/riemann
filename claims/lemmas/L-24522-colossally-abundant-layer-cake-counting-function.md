# L-24522 — The colossally abundant ledger is one threshold-counting function

Claim ID: `L-24522`  
Status: `PROPOSED — complete elementary finite/layer-cake algebra`  
Scope: Lagarias/Robin colossally abundant sequence  
Issue: #245

Use the increment items of `L-24521`:

\[
x_{p,a}=\log p,
\qquad
y_{p,a}=\log I_{p,a},
\qquad
\kappa_{p,a}=\frac{y_{p,a}}{x_{p,a}}.
\]

For a threshold `epsilon>0` not equal to an item slope, define

\[
\boxed{
X(\epsilon)=
\sum_{\kappa_{p,a}>\epsilon}\log p,
}
\tag{L-24522.1}
\]

and

\[
\boxed{
Y(\epsilon)=
\sum_{\kappa_{p,a}>\epsilon}\log I_{p,a}.
}
\tag{L-24522.2}
\]

The associated colossally abundant number is

\[
n(\epsilon)=\exp X(\epsilon),
\]

where the exponential notation abbreviates the exact prime product encoded by
the included increments.

## 1. Closed exponent threshold

Write `m=a+1` and `q=p^m`. The inequality

\[
\kappa_{p,a}>\epsilon
\]

is equivalent to

\[
\frac{1-p^{-m-1}}{1-p^{-m}}>p^\epsilon.
\]

After rearrangement,

\[
\boxed{
p^m<Q_p(\epsilon),
\qquad
Q_p(\epsilon)=
\frac{p^\epsilon-p^{-1}}{p^\epsilon-1}.
}
\tag{L-24522.3}
\]

Therefore the exponent of `p` in `n(epsilon)` is exactly

\[
\boxed{
A_p(\epsilon)
=\#\{m\ge1:p^m<Q_p(\epsilon)\},
}
\tag{L-24522.4}
\]

and

\[
\boxed{
X(\epsilon)=\sum_p A_p(\epsilon)\log p.
}
\tag{L-24522.5}
\]

Only finitely many primes occur because `Q_p(epsilon)<=p` for all sufficiently
large `p`.

At a tie `p^m=Q_p(epsilon)`, either choice gives a colossally abundant maximizer;
the two adjacent prefix values are retained separately.

## 2. Layer-cake identity

For every included item,

\[
y_{p,a}=\epsilon x_{p,a}
+\int_\epsilon^{\kappa_{p,a}}x_{p,a}\,dt.
\]

Summing the finite included family and interchanging the finite sum and
integral gives

\[
\boxed{
Y(\epsilon)
=\epsilon X(\epsilon)
+\int_\epsilon^\infty X(t)\,dt.
}
\tag{L-24522.6}
\]

Thus the complete normalized divisor ratio on the CA sequence is determined by
one decreasing step function `X(epsilon)`.

Equivalently, the logarithm of the maximal Rankin quotient is

\[
\boxed{
M(\epsilon)
:=\max_n\log\frac{\sigma(n)}{n^{1+\epsilon}}
=Y(\epsilon)-\epsilon X(\epsilon)
=\int_\epsilon^\infty X(t)\,dt.
}
\tag{L-24522.7}
\]

The maximum is achieved by `n(epsilon)` and the tie variants.

## 3. Exact Euler-product form

Independence of the prime exponents also gives

\[
\boxed{
\exp M(\epsilon)
=\prod_p
\max_{a\ge0}
\left[
\frac{1-p^{-a-1}}{1-p^{-1}}
 p^{-a\epsilon}
\right].
}
\tag{L-24522.8}
\]

The product is finite after replacing factors whose maximum is `1` by `1`.
Equation (L-24522.7) is the logarithmic layer-cake decomposition of this exact
finite Euler product.

## 4. Lagarias slack in one dimension

Put

\[
\mathcal H(n)=H_n+e^{H_n}\log H_n
\]

and

\[
\Phi(x)=\log\frac{\mathcal H(e^x)}{e^x},
\tag{L-24522.9}
\]

where at the CA points `e^x` denotes the exact integer encoded by the prefix.
Then the Lagarias slack at threshold `epsilon` is

\[
\boxed{
\mathfrak D(\epsilon)
=\Phi(X(\epsilon))
-\epsilon X(\epsilon)
-\int_\epsilon^\infty X(t)\,dt.
}
\tag{L-24522.10}
\]

Checking Lagarias on all colossally abundant numbers is exactly checking

\[
\mathfrak D(\epsilon)\ge0
\]

at every item threshold and both sides of every tie.

## 5. Connection to the prime-ramp coordinate

For small `epsilon`, equation (L-24522.3) gives

\[
Q_p(\epsilon)
=\frac{1-p^{-1}}{\epsilon\log p}+O_p(1).
\tag{L-24522.11}
\]

Hence `X(epsilon)` is a smoothed prime-power count in the hyperbolic region

\[
p^m\log p\lesssim\epsilon^{-1}.
\]

This is the same prime-power geometry appearing in the square-root prime ramp,
but integrated through the CA support function. `T-24504` supplies the exact
global equivalence; equation (L-24522.10) supplies the one-dimensional CA
coordinate.

## Status boundary

The exponent formula and layer-cake identities are complete elementary
mathematics. Proving `mathfrak D(epsilon)>=0` is still equivalent to the
Lagarias/RH scalar and is not asserted here.
