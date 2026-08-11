# L-91029 — The positive generalized-Jordan channel is an infinitely divisible compound-Poisson prime semigroup

Claim ID: `L-91029`  
Status: **PROPOSED COMPLETE EXACT LEVY/CARRE-DU-CHAMP THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: `L-91014`, `L-91020`  
RH status: **unproved**

## 1. Positive Euler logarithm

For `a>0` and `Re(s)>1`,

\[
 Q_a(s)=\frac{\zeta(s)}{\zeta(s+2a)}.
\]

The Euler logarithm is

\[
 \boxed{
 \log Q_a(s)
 =\sum_p\sum_{k\ge1}
 {1-p^{-2ak}\over k}\,p^{-ks}.
 }
 \tag{L-91029.1}
\]

Every coefficient is nonnegative.

## 2. Compound-Poisson characteristic function

Fix `sigma>1` and normalize

\[
 M_{a,\sigma}(\theta)
 =\frac{Q_a(\sigma+i\theta)}{Q_a(\sigma)}.
 \tag{L-91029.2}
\]

Define the finite positive atomic measure

\[
 \boxed{
 \nu_{a,\sigma}
 =\sum_p\sum_{k\ge1}
 {1-p^{-2ak}\over k p^{k\sigma}}
 \delta_{k\log p}.
 }
 \tag{L-91029.3}
\]

Then

\[
 \boxed{
 \log M_{a,\sigma}(\theta)
 =\int_0^\infty(e^{-i\theta t}-1)d\nu_{a,\sigma}(t).
 }
 \tag{L-91029.4}
\]

Thus `M_(a,sigma)` is the characteristic function of a compound-Poisson
random variable with prime-power jumps.  In particular it is infinitely
divisible, and

\[
 M_{a,\sigma}(\theta)^r
\]

is positive definite for every real `r>=0`.

## 3. Random-unitary semigroup

For a finite carrier set `x_1,...,x_N`, define

\[
 \Phi_{a,\sigma}^{(r)}(X)
 =\mathbb E[D_{S_r}XD_{S_r}^*],
 \qquad
 D_t=\operatorname{diag}(e^{-ix_1t},...,e^{-ix_Nt}),
 \tag{L-91029.5}
\]

where `S_r` is the compound-Poisson process with Lévy measure
`r nu_(a,sigma)`.  Then

\[
 \boxed{
 \Phi^{(r+s)}=\Phi^{(r)}\Phi^{(s)},
 \qquad
 \Phi^{(0)}=I.
 }
 \tag{L-91029.6}
\]

Every `Phi^(r)` is completely positive, unital, trace preserving and
random-unitary.

## 4. Prime-jump Lindblad generator

The generator is

\[
 \boxed{
 \mathscr L_{a,\sigma}(X)
 =\int_0^\infty(D_tXD_t^*-X)d\nu_{a,\sigma}(t).
 }
 \tag{L-91029.7}
\]

Equivalently,

\[
 \mathscr L_{a,\sigma}(X)
 =\sum_{p,k}{1-p^{-2ak}\over kp^{k\sigma}}
  (D_{k\log p}XD_{k\log p}^*-X).
 \tag{L-91029.8}
\]

The corresponding scalar Dirichlet form is

\[
 \boxed{
 -\langle f,\mathscr L_{a,\sigma}f\rangle
 ={1\over2}\int_0^\infty
  \|f-D_tf\|^2d\nu_{a,\sigma}(t)\ge0.
 }
 \tag{L-91029.9}
\]

This is an exact positive Selberg/Lévy square over generalized prime-power
jumps.

## 5. Logarithmic currents are Lévy moments

Differentiating the positive Euler logarithm gives

\[
 \boxed{
 -\partial_\sigma\log Q_a(\sigma)
 =\int t\,d\nu_{a,\sigma}(t)
 =\sum_{n=p^k}\Lambda(n)(1-n^{-2a})n^{-\sigma}.
 }
 \tag{L-91029.10
}
\]

and

\[
 \boxed{
 \partial_\sigma^2\log Q_a(\sigma)
 =\int t^2d\nu_{a,\sigma}(t)
 =\sum_{n=p^k}\Lambda(n)\log n\,(1-n^{-2a})n^{-\sigma}.
 }
 \tag{L-91029.11}

\]

All higher alternating derivatives are positive Lévy moments.  Hence the
complete generalized-prime current tower is positive at every safe Euler line.

## 6. Carré du champ and independent frequencies

For the diagonal carrier algebra, the carré du champ is

\[
 \boxed{
 \Gamma_{a,\sigma}(f,g)
 ={1\over2}\int
  (D_tf-f)^*(D_tg-g)d\nu_{a,\sigma}(t).
 }
 \tag{L-91029.12}
\]

It is positive semidefinite for arbitrary independent carrier families before
aggregation.  Higher iterated carré-du-champ tensors remain positive because
the jump measure is positive and the process has independent increments.

This supplies the exact source-side reflected Selberg object requested by the
Cauchy--Jordan Hardy programme.

## 7. Boundary obstruction is now precisely an exponential tilt

The completed xi scattering ratio of `L-91023` requires the analytic
continuation of the source from safe `sigma>1` to the symmetric line

\[
 \sigma=\frac12-a.
\]

At the Lévy level this is the exponential tilt

\[
 d\nu_{a,\sigma}(t)
 =e^{-(\sigma-1)t}d\nu_{a,1}(t).
 \tag{L-91029.13}
\]

The positive jump measure ceases to be finite exactly when the tilt crosses its
abscissa of convergence.  Thus the final RH-bearing theorem is no longer a
mysterious Selberg sign: it is preservation of the compound-Poisson
carré-du-champ under the completed gamma/pole analytic continuation to the
critical boundary.

## 8. Boundary

Closed:

```text
positive Euler logarithm;
compound-Poisson prime-power representation;
infinitely divisible random-unitary channel;
exact jump Lindblad generator;
positive Selberg/Dirichlet form;
all logarithmic currents as positive Lévy moments;
independent-frequency carré-du-champ positivity.
```

Open:

```text
completed exponential-tilt continuation of the carré du champ;
identification with the one causal residual Hardy square at the critical boundary;
RH.
```
