# R-32403 — Componentwise Bernstein and Stieltjes hinge positivity fail

Claim ID: `R-32403`  
Title: Square-root Hinge Average-Row Positivity cannot be proved by demanding positivity of every exponential or resolvent hinge before integration  
Status: **PROPOSED COMPLETE EXACT FINITE REFUTATION — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: PR #329 `L-32303` average-carry triangular inverse  
Scope: refutes two natural componentwise integral shortcuts; does not refute SHARP

## 1. Average-carry inverse

For an endpoint `T`, let

\[
 \beta_{nq}
 ={\lfloor n/q\rfloor[q-1-(n\bmod q)]\over n+1}
\]

and, for a target `h(q)`, let `c_h(n)` be its unique upper-triangular inverse:

\[
 h(q)=\sum_{n=q}^{T}c_h(n)\beta_{nq}.
\tag{R-32403.1}
\]

PR #329 proposes SHARP for

\[
 h_T(q)=q^{-1/2}-T^{-1/2}.
\]

Two tempting proofs use the classical positive integral representations

\[
 q^{-1/2}-T^{-1/2}
 ={1\over\sqrt\pi}\int_0^\infty
 u^{-1/2}(e^{-qu}-e^{-Tu})du
\tag{R-32403.2}
\]

or

\[
 q^{-1/2}-T^{-1/2}
 ={1\over\pi}\int_0^\infty
 t^{-1/2}
 \left({1\over q+t}-{1\over T+t}\right)dt.
\tag{R-32403.3}
\]

One might hope to prove the inverse coefficients of every integrand are nonnegative and then integrate. That stronger statement is false.

## 2. Exact linear-hinge counterexample

Take

\[
 T=61
\]

and the endpoint-vanishing linear target

\[
\boxed{
 \ell(q)=61-q,
 \qquad2\le q\le61.
}
\tag{R-32403.4}
\]

Backward substitution in the rational matrix `beta` is exact. At row

\[
 j=11
\]

one obtains

\[
\boxed{
 c_\ell(11)=-{2\over55}<0.
}
\tag{R-32403.5}
\]

No floating computation enters this witness.

## 3. Exponential hinges fail near one

For `0<z<1`, put

\[
 e_z(q)=z^q-z^{61}.
\]

As `z` tends to one from below,

\[
 {e_z(q)\over1-z}\longrightarrow61-q
\]

coefficientwise. Since the triangular inverse is finite and linear,

\[
\boxed{
 \lim_{z\uparrow1}{c_{e_z}(11)\over1-z}
 =-{2\over55}.
}
\tag{R-32403.6}
\]

Therefore there exists `z_0<1` such that

\[
\boxed{
 c_{e_z}(11)<0
 \qquad(z_0<z<1).
}
\tag{R-32403.7}
\]

Thus the Bernstein/Laplace representation (R-32403.2) cannot be lifted componentwise through the average-carry inverse.

## 4. Resolvent hinges fail at large parameter

For `t>=0`, put

\[
 r_t(q)={1\over q+t}-{1\over61+t}.
\]

Then

\[
 t^2r_t(q)\longrightarrow61-q
\qquad(t\to\infty)
\]

coefficientwise. Again finite linearity gives

\[
\boxed{
 \lim_{t\to\infty}t^2c_{r_t}(11)
 =-{2\over55}.
}
\tag{R-32403.8}
\]

Hence

\[
\boxed{
 c_{r_t}(11)<0
}
\tag{R-32403.9}
\]

for every sufficiently large `t`.

So the Stieltjes representation (R-32403.3) also cannot be lifted by proving positivity of each resolvent component separately.

## 5. Consequence for SHARP

The square-root hinge may still have a nonnegative inverse; directed exact certificates on PR #329 support that conjecture through large finite endpoints. But any proof must preserve cancellation **across the integral parameter** in (R-32403.2) or (R-32403.3), or exploit a different source-specific structure.

In particular the following ambient claims are false:

```text
all endpoint-vanishing completely monotone hinges have positive inverse;
all exponential hinges have positive inverse;
all Stieltjes resolvent hinges have positive inverse.
```

The exponent `1/2` is load bearing.

## 6. Proof boundary

Refuted exactly:

- componentwise exponential-hinge positivity;
- componentwise resolvent-hinge positivity.

Unaffected:

- SHARP itself;
- the positive square-root hinge decomposition of the critical target;
- RH, which remains unproved.
