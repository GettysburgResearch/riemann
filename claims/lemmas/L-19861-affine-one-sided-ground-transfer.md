# L-19861 — Affine one-sided quotient coercivity selects the ground line

Claim ID: `L-19861`  
Status: **PROVED ABSTRACT SPECTRAL THEOREM**  
Authoring agent: `gpt56-pro-09-r`  
Created: 2026-08-07  
Scope: exact spectral endpoint for the repaired positive RH route; no RH claim without the declared analytic inputs

## 1. Setup

Let `(H,\langle\cdot,\cdot\rangle)` be a real or complex Hilbert space. Let
`Q` be a densely defined, closed, lower-bounded Hermitian form with associated
selfadjoint operator `A`. Let `D` be a closed nonnegative form on the same form
domain.

Write

\[
 \theta_2(D)
 =\inf_{\substack{W\subset\operatorname{Dom}D\\\dim W=2}}
   \ \sup_{0\ne w\in W}{D(w)\over\|w\|^2}
 \tag{L-19861.1}
\]

for its second min--max value. Let `p` be a unit vector in the common form
domain.

Assume that for real `sigma`, positive `c_-`, positive `c_+`, and numbers
`g,m>0`,

\[
 \boxed{\theta_2(D)\ge g,}
 \tag{L-19861.2}
\]

\[
 \boxed{Q-\sigma I\succeq c_-D,}
 \tag{L-19861.3}
\]

and only on the target line,

\[
 \boxed{Q(p,p)-\sigma\le c_+m.}
 \tag{L-19861.4}
\]

No upper operator comparison between `Q` and `D` is assumed. The scalar shift
`sigma` may be negative.

## 2. Spectral separation theorem

If

\[
 c_+m<c_-g,
 \tag{L-19861.5}
\]

then the bottom of `A` is a simple isolated eigenvalue. More precisely,

\[
 \boxed{\lambda_1(A)\ge\sigma,}
 \tag{L-19861.6}
\]

\[
 \boxed{\lambda_2(A)\ge\sigma+c_-g,}
 \tag{L-19861.7}
\]

and

\[
 \boxed{\lambda_1(A)\le Q(p,p)\le\sigma+c_+m.}
 \tag{L-19861.8}
\]

Consequently,

\[
 \boxed{\lambda_2(A)-\lambda_1(A)
 \ge c_-g-c_+m>0.}
 \tag{L-19861.9}
\]

Here the min--max values may lie below the essential spectrum; inequality
(L-19861.9) itself forces the first value to be a discrete simple eigenvalue.

### Proof

Equation (L-19861.3) and `D>=0` give (L-19861.6). Applying the min--max
principle to (L-19861.3) gives (L-19861.7). The target Rayleigh value gives
(L-19861.8). Hence (L-19861.9), and the spectral subspace below
`lambda_2(A)` is one-dimensional. QED.

## 3. Quantitative target-to-ground estimate

Let `xi` be a unit ground eigenvector and write

\[
 p=\alpha\xi+w,
 \qquad w\perp\xi.
 \tag{L-19861.10}
\]

Then

\[
 \boxed{
 \|w\|^2
 \le {c_+m\over c_-g-c_+m}.}
 \tag{L-19861.11}
\]

Indeed, the spectral theorem and (L-19861.9) give

\[
 Q(p,p)-\lambda_1(A)
 \ge [\lambda_2(A)-\lambda_1(A)]\|w\|^2.
\]

Since `lambda_1(A)>=sigma`, the left side is at most
`Q(p,p)-sigma<=c_+m`. This proves (L-19861.11).

Thus, along a sequence,

\[
 {c_+m\over c_-g}\longrightarrow0
 \tag{L-19861.12}
\]

implies projective convergence of the exact ground line to the target line.

## 4. Parity

Suppose an involution `J` commutes with `A`, and suppose `Jp=p`. The simple
ground state has definite `J`-parity. If the ground state were odd, it would be
orthogonal to `p`, so `||w||=1`. Therefore (L-19861.11) forces the ground state
to be even whenever

\[
 {c_+m\over c_-g-c_+m}<1.
 \tag{L-19861.13}
\]

## 5. Moving-Hardy corollary

Let the support be `[-L,L]` and let

\[
 \|f\|_\tau^2
 =\int_{-L}^L|f(t)|^2\,2\cosh(2\tau t)\,dt,
 \qquad 0<\tau<1/2.
\]

Then

\[
 \|w\|_\tau^2
 \le2e^{2\tau L}\|w\|^2.
 \tag{L-19861.14}
\]

Hence the exact sufficient rate for Hardy convergence is

\[
 \boxed{
 e^{2\tau_LL}
 {c_{+,L}m_L\over c_{-,L}g_L-c_{+,L}m_L}
 \longrightarrow0.}
 \tag{L-19861.15}
\]

If explicit targets converge in this moving Hardy norm to a source whose
transform is `Xi`, and if the finite or continuous ground-state real-zero
theorem applies, local-uniform transform convergence and Hurwitz imply RH.

## 6. Why this is strictly weaker than complete relative local Weyl

The two-sided unshifted estimate

\[
 (1-\eta)cD\preceq Q\preceq(1+\eta)cD
\]

forces `Q>=0` and is already an RH-bearing cofinal Weil-positivity theorem on a
dense core. The present result asks only for:

```text
one shifted lower inequality on the whole complement;
one upper inequality on one target line.
```

It neither assumes nor proves positivity of `Q` when `sigma<0`.

## 7. Proof boundary

The theorem is exact abstract spectral theory. A Riemann application must still
produce the shift, the one-sided lower bound, the target upper bound, and the
moving-Hardy target limit in one immutable normalization.