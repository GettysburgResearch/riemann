# L-32407 — Average-carry generating kernel and a positive reciprocal resolution

Claim ID: `L-32407`  
Title: The complete average-carry rows have an explicit generating function and resolve the reciprocal target `1/q` by one positive infinite row mixture  
Status: **PROPOSED COMPLETE EXACT ANALYTIC LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: PR #329 `L-32303`  
Scope: infinite positive average-row resolution of `1/q`; no finite square-root hinge theorem or RH conclusion

## 1. Average carry count

For `q>=2`, put

\[
 C_n(q)=(n+1)\beta_{nq}
 =\sum_{j=0}^{n}\chi_{n,j}(q).
\tag{L-32407.1}
\]

The floor generating function is

\[
 \sum_{n\ge0}\left\lfloor{n\over q}\right\rfloor z^n
 ={z^q\over(1-z)(1-z^q)}.
\tag{L-32407.2}
\]

Since

\[
 C_n(q)
 =(n+1)\left\lfloor{n\over q}\right\rfloor
 -2\sum_{j=0}^{n}\left\lfloor{j\over q}\right\rfloor,
\]

finite differentiation of (L-32407.2) gives, for `|z|<1`,

\[
\boxed{
 \sum_{n\ge0}C_n(q)z^n
 ={z^q\,[q(1-z)-(1-z^q)]
  \over(1-z)^2(1-z^q)^2}.
}
\tag{L-32407.3}
\]

## 2. One positive kernel

Define

\[
 \phi_q(z)
 ={z^{q-1}(1-z)\over1-z^q}
 ={z^{q-1}\over1+z+\cdots+z^{q-1}}.
\tag{L-32407.4}
\]

Direct differentiation gives

\[
\boxed{
 \phi_q'(z)
 =z^{q-2}
 {q(1-z)-(1-z^q)\over(1-z^q)^2}.
}
\tag{L-32407.5}
\]

For `0<z<1`, convexity of the geometric sum gives

\[
 q(1-z)\ge1-z^q,
\]

so

\[
\boxed{\phi_q'(z)\ge0.}
\tag{L-32407.6}
\]

Combining (L-32407.3) and (L-32407.5),

\[
\boxed{
 \phi_q'(z)
 =(1-z)^2z^{-2}
 \sum_{n\ge0}(n+1)\beta_{nq}z^n.
}
\tag{L-32407.7}
\]

Every coefficient on the right is nonnegative.

## 3. Positive reciprocal resolution

The endpoint values are

\[
 \phi_q(0)=0,
 \qquad
 \phi_q(1^-)=1/q.
\]

Integrating (L-32407.7) from zero to one and interchanging nonnegative terms gives

\[
 {1\over q}
 =\sum_{n\ge q}(n+1)\beta_{nq}
   \int_0^1(1-z)^2z^{n-2}dz.
\]

The beta integral is

\[
 \int_0^1(1-z)^2z^{n-2}dz
 ={2\over(n-1)n(n+1)}.
\]

Therefore

\[
\boxed{
 {1\over q}
 =\sum_{n=q}^{\infty}
 {2\over n(n-1)}\,\beta_{nq}.
}
\tag{L-32407.8}
\]

This is an exact positive average-row realization of the reciprocal target. The row coefficient

\[
\boxed{
 c_n^{(1)}={2\over n(n-1)}>0
}
\tag{L-32407.9}
\]

is independent of `q`.

## 4. Interpretation

Equation (L-32407.8) shows that the average-carry cone has a simple positive scale-invariant Green state at exponent one. The square-root hinge of PR #329 asks for the critical exponent one-half and a finite endpoint cancellation.

`R-32403` proves that this exponent-one positive resolution cannot be interpolated to the square-root target by demanding componentwise positivity of exponential or resolvent hinges. The missing `1/2` theorem is genuinely fractional and source-specific.

Thus the continuum intuition behind SHARP is correct but insufficient:

```text
reciprocal exponent 1:   explicit positive resolution;
critical exponent 1/2:   finite SHARP still open;
generic Bernstein pieces: positivity false.
```

## 5. Proof boundary

Closed exactly:

- the average-carry generating function;
- positivity of the kernel `phi_q'`;
- the positive infinite reciprocal resolution.

Open:

- a finite positive resolution of `q^-1/2-T^-1/2`;
- SHARP;
- RH.
