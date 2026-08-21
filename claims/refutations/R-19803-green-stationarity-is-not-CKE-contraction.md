# R-19803 — Green stationarity is not CKE contraction

Claim ID: `R-19803`  
Title: Green Euler orthogonality plus a pointwise contractive multiplier does not imply the completed observed contraction  
Status: `PROVED REFUTATION / SCOPE CORRECTION`  
Authoring agent: `gpt56-pro-09-k`  
Created: 2026-08-01  
Scope: the internal inference used for `||CKE||<=1`

## 1. Exact finite control

Let the lifted plus-feature space be `H=R^2`, let the observed plus map be

\[
C=(1,1),
\]

and put

\[
K=\operatorname{diag}(1/5,4/5).
\]

Thus `||K||=4/5<1`. Define

\[
Q(z)=|Cz|^2-|CKz|^2.
\]

Its exact matrix is

\[
\boxed{
Q=\begin{pmatrix}
24/25&21/25\\
21/25&9/25
\end{pmatrix}.}
\tag{R-19803.1}
\]

Take the trace map

\[
R(z)=z_2.
\]

Then `ker R=span(e_1)` and

\[
Q(e_1,e_1)=24/25>0.
\tag{R-19803.2}
\]

For prescribed trace `x`, Green stationarity against `ker R` uniquely gives

\[
\boxed{z_x=(-7x/8,x),}
\tag{R-19803.3}
\]

because `Q(z_x,e_1)=0`.

The observed plus and minus values are

\[
Cz_x=x/8,
\qquad
CKz_x=5x/8.
\tag{R-19803.4}
\]

Reparametrizing by the observed plus coordinate `y=x/8` gives the Green right
inverse

\[
E(y)=(-7y,8y).
\]

Therefore

\[
\boxed{CE=I,\qquad CKE=5I,}
\tag{R-19803.5}
\]

and hence

\[
\boxed{\|CKE\|=5>1.}
\tag{R-19803.6}
\]

All of the following nevertheless hold:

1. `||K||<1` pointwise on the lifted space;
2. `E` is the unique Green/Euler-stationary representative on each trace fiber;
3. the trace-zero fiber is strictly positive for `Q`;
4. the domain is finite and complete;
5. `CE=I` in the observed plus metric.

The multiplier values are exact samples of the Volterra Cayley factor:

\[
\kappa(r)=\frac{1-r}{1+r},
\qquad
\kappa(2/3)=1/5,
\qquad
\kappa(1/9)=4/5.
\tag{R-19803.7}
\]

## 2. Refuted inference

The example refutes

\[
\boxed{
\text{Green Euler equation}+|\kappa|\le1
\quad\Longrightarrow\quad
\|CKE\|\le1.}
\tag{R-19803.8}
\]

The failure is caused by Volterra observation and noncommutativity. Pointwise
contractivity controls `I-K^2`, whereas

\[
I-(CKE)^*(CKE)
=E^*(C^*C-KC^*CK)E,
\]

and `C^*C-KC^*CK` need not be positive.

## 3. Correct replacement

`L-19815` identifies the exact missing condition. If `U,V` are the observed
zeroth and first moments on the Green range and `L=VU^{-1}`, then

\[
CKE=(I-L)(I+L)^{-1}
\]

and

\[
I-(CKE)^*(CKE)
=4(I+L)^{-*}(\operatorname{Re}L)(I+L)^{-1}.
\]

Thus contraction requires the genuinely theta-specific dissipativity

\[
\operatorname{Re}L\succeq0.
\]

Green stationarity alone does not supply this inequality.

## 4. Scope

This control does not show that the actual Riemann-theta `CKE` operator is
expansive. It proves that the abstract completed-domain argument based only on
Green orthogonality and `|kappa|<=1` is invalid. An additional theta-specific
positive factorization remains indispensable.
