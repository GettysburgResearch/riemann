# L-34414 — The Q4 all-pass is the cascade of two Q2 all-pass states

Claim ID: `L-34414`  
Title: The Q4 Euler–Blaschke colligation factors exactly into the `+` and `-` Q2 colligations; its one-dimensional reservoir telescope is the sum of a corrected low-pass state telescope and a Q2 compact state telescope  
Status: **PROPOSED COMPLETE EXACT TWO-STAGE INDEPENDENT-FREQUENCY THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring/review agent: `gpt56-sol`  
Created: 2026-08-10  
Dependencies: `L-34413`; PR #339 `L-33804`; elementary Blaschke factorization  
Scope: aligned physical blocks and any common parameter-independent source path; no dissipative sign theorem or RH conclusion

## 1. Factorization of the Euler–Blaschke multiplier

Put

\[
z=2^{-s}.
\]

Define the two radix-two factors

\[
E_+(z)=\frac{1-2z}{1-z},
\qquad
E_-(z)=\frac{1+2z}{1+z}.
\tag{L-34414.1}
\]

Then

\[
\boxed{
E_4(z)
:=\frac{1-4z^2}{1-z^2}
=E_+(z)E_-(z).
}
\tag{L-34414.2}

On the critical line each `E_±/sqrt(2)` is all-pass, and their product is `E_4/2`.

Let `g_tau` be any common Hilbert/Dirichlet source path to which the fixed filters may be applied.  Put

\[
\boxed{
h_4=(1-z^2)g_\tau,
}
\tag{L-34414.3}

\[
\boxed{
f_1=(1-2z)(1+z)g_\tau,
}
\tag{L-34414.4}

and

\[
\boxed{
c_4=(1-4z^2)g_\tau.
}
\tag{L-34414.5}

Thus

\[
f_1=E_+h_4,
\qquad
c_4=E_-f_1.
\]

## 2. The two reservoir states

The `+` Q2 reservoir is

\[
R_+(z)=\frac{1/\sqrt2}{1-z}.
\]

Applied to `h_4=(1-z)(1+z)g_tau`, it gives

\[
\boxed{
r_1:=R_+h_4
=\frac1{\sqrt2}(1+z)g_\tau.
}
\tag{L-34414.6}

The `-` Q2 reservoir is

\[
R_-(z)=\frac{1/\sqrt2}{1+z}.
\]

Applied to `f_1=(1-2z)(1+z)g_tau`, it gives

\[
\boxed{
r_2:=R_-f_1
=\frac1{\sqrt2}(1-2z)g_\tau.
}
\tag{L-34414.7}

Thus the cascade state consists exactly of

```text
r_1: one normalized corrected low-pass source;
r_2: one normalized Q2 compact source.
```

No infinite source tail or additional current species appears.

## 3. Two exact block telescopes

Let `B_I` be the independent-frequency physical block Gram and let `ell=log 2`.  Applying the Q2 identity at the first stage gives

\[
\boxed{
2B_I(h_4)-B_I(f_1)
=2\left[B_I(r_1)-B_{I-\ell}(r_1)\right].
}
\tag{L-34414.8}

The second stage gives

\[
\boxed{
2B_I(f_1)-B_I(c_4)
=2\left[B_I(r_2)-B_{I-\ell}(r_2)\right].
}
\tag{L-34414.9}

Multiply (L-34414.8) by two and add (L-34414.9):

\[
\boxed{
\begin{aligned}
4B_I(h_4)-B_I(c_4)
={}&4\Delta_\ell B_I(r_1)\\
&+2\Delta_\ell B_I(r_2),
\end{aligned}}
\tag{L-34414.10}

where

\[
\Delta_\ell B_I(f)=B_I(f)-B_{I-\ell}(f).
\]

## 4. Comparison with the direct Q4 reservoir

The direct Q4 all-pass reservoir is

\[
R_4(z)=\frac{\sqrt3/2}{1-z^2}.
\]

Therefore

\[
R_4h_4=\frac{\sqrt3}{2}g_\tau,
\]

and PR #339 gives

\[
\boxed{
4B_I(h_4)-B_I(c_4)
=3\Delta_{2\ell}B_I(g_\tau).
}
\tag{L-34414.11}

Combining (L-34414.10)--(L-34414.11), and substituting (L-34414.6)--(L-34414.7), yields the exact state-conservation identity

\[
\boxed{
3\Delta_{2\ell}B_I(g_\tau)
=2\Delta_\ell B_I((1+z)g_\tau)
 +\Delta_\ell B_I((1-2z)g_\tau).
}
\tag{L-34414.12}

This is a two-stage realization of the direct Q4 state telescope.

## 5. Curvature identity

Every filter is independent of the Jordan parameter.  Differentiate (L-34414.12) twice in the imaginary Jordan direction:

\[
\boxed{
3\Delta_{2\ell}\mathfrak C_I(g)
=2\Delta_\ell\mathfrak C_I((1+z)g)
 +\Delta_\ell\mathfrak C_I((1-2z)g).
}
\tag{L-34414.13}

Equivalently, the Q4 reservoir curvature is exactly the weighted sum of

```text
2 copies of the corrected low-pass curvature telescope;
1 copy of the Q2 compact curvature telescope.
```

The channel weights are forced by the unitary cascade and are independent of the arithmetic endpoint.

## 6. Significance for the final recurrence

`L-34413` proves at one scale that the same two outputs form the tight frame

\[
2\mathfrak C_I((1+z)g)
 +\mathfrak C_I((1-2z)g)
=3\mathfrak C_I(g)+3\mathfrak C_{I-\ell}(g).
\]

The present theorem proves that their **state differences** also reproduce the complete Q4 telescope.  Hence the direct Q4 route and the corrected low-pass/Q2 route are not parallel conjectures: they are two realizations of one finite unitary state system.

What remains is not source construction or reservoir identification.  It is the sign/orientation of the two output curvature telescopes after the complete generalized-prime and source boundary ledgers are inserted.

A scalar trace positivity theorem does not settle that orientation; the polarized matrix requirement of `L-34412` remains load bearing.

## 7. Proof boundary

Closed exactly:

1. factorization `E_4=E_+E_-`;
2. explicit intermediate source path;
3. exact two reservoir states;
4. both independent-frequency Q2 block telescopes;
5. equality with the direct Q4 reservoir telescope;
6. curvature-level state conservation.

Open:

1. polarized positivity/dissipation of the two output state telescopes;
2. coefficient-one global recurrence;
3. RH.
