# L-91007 — Classical zero-free regions penetrate the unit-disc annulus beyond radius three quarters

Claim ID: `L-91007`  
Status: **PROPOSED COMPLETE TRANSFER LEMMA / UNCONDITIONAL COROLLARY — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: `T-91001`; any standard explicit zero-free region for zeta near `Re(s)=1`  
RH status: **unproved**

## 1. General transfer theorem

Let `eta(T)` be positive and nonincreasing for `T>=3`. Assume that every nontrivial zero `rho=beta+i gamma` satisfies

\[
 \beta\le1-\eta(|\gamma|+3).
\tag{L-91007.1}
\]

For a real centre `x`, put

\[
 T_x=|x|+3,
 \qquad
 \eta_x=\eta(2T_x).
\]

Assume `eta_x<=1/2` and `sqrt(eta_x/2)<=1`. Then the unit-disc generating function `A_x` of `T-91001` is holomorphic in

\[
 \boxed{
 |w|<\frac34+\frac12\eta_x.
 }
\tag{L-91007.2}
\]

### Proof

A right-side zero produces the pole

\[
 w_\rho(x)
 =1-\left[d+i(\gamma-x)\right]^2,
 \qquad d=\beta-\frac12.
\]

Its modulus is bounded below by its real part:

\[
 |w_\rho(x)|
 \ge1-d^2+(\gamma-x)^2.
\tag{L-91007.3}
\]

If

\[
 |\gamma-x|\ge\sqrt{\eta_x/2},
\]

then `d<1/2` gives immediately

\[
 |w_\rho(x)|
 >\frac34+\frac12\eta_x.
\]

Otherwise `|gamma-x|<1`, so

\[
 |\gamma|+3<2(|x|+3)=2T_x.
\]

Monotonicity of `eta` and (L-91007.1) give

\[
 d\le\frac12-\eta_x.
\]

Hence

\[
\begin{aligned}
 |w_\rho(x)|
 &\ge1-\left(\frac12-\eta_x\right)^2\\
 &=\frac34+\eta_x-\eta_x^2\\
 &\ge\frac34+\frac12\eta_x.
\end{aligned}
\]

Critical-line poles lie at `1+(gamma-x)^2>=1`. Therefore no pole of `A_x` lies in (L-91007.2). `square`

## 2. Vinogradov--Korobov corollary

Insert a standard Vinogradov--Korobov zero-free region

\[
 \eta(T)
 =\frac{c_0}
 {\{\log T\}^{2/3}\{\log\log T\}^{1/3}}
\]

for sufficiently large `T`, with a suitable absolute `c_0>0`. Then there is an absolute `c_1>0` such that, for every sufficiently large `|x|`,

\[
 \boxed{
 \mathcal A_x(w)\text{ is holomorphic whenever}
 \quad
 |w|<\frac34+
 \frac{c_1}
 {\{\log(|x|+3)\}^{2/3}
  \{\log\log(|x|+3)\}^{1/3}}.
 }
\tag{L-91007.4}
\]

Equivalently,

\[
 \boxed{
 \limsup_{k\to\infty}|a_k(x)|^{1/k}
 \le
 \left[
 \frac34+
 \frac{c_1}
 {\{\log(|x|+3)\}^{2/3}
  \{\log\log(|x|+3)\}^{1/3}}
 \right]^{-1}.
 }
\tag{L-91007.5}
\]

## 3. Meaning and limitation

The direct absolutely convergent Euler expression stops sharply at radius `3/4`. The classical zero-free region proves that the actual analytic object crosses that boundary by a quantitative amount. Thus the annulus is not inaccessible as an analytic-continuation problem.

What remains missing is the sign geometry:

```text
holomorphy a little past 3/4       unconditional;
Stieltjes/Pick or radial concavity  still open;
cofinal continuation to radius 1    RH-equivalent.
```

This lemma uses a conventional zero-free theorem as input. It does not provide a new zero-free region and does not prove RH.
