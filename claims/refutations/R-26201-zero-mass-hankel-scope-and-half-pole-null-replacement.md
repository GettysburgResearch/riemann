# R-26201 — Zero-mass conditional Hankel positivity is false; the surviving source-specific cone is half-pole-null

Claim ID: `R-26201`  
Title: The exact review counterexample kills the old conditional-Hankel middle line, while an exact weighted-moment factorization identifies the narrower cone that the dyadic source really occupies  
Status: **REFUTATION OF THE FROZEN `L-23603` MECHANISM; REPLACEMENT INTERFACE PROVED EXACTLY**  
Authoring agent: `gpt56-02-r`  
Created: 2026-08-08  
Dependencies: frozen PR #243; review PRs #251/#255/#257  
Scope: kernel algebra only; no positivity conclusion for the global carry profile

## 1. Frozen claim disposed

The frozen carry proposal used the Green generator

\[
\phi(t)=8e^t-7e^{t/2}-\frac32 t e^{t/2}
\tag{R-26201.1}
\]

and attempted to place the derivative kernel `phi''(x+y)` in a positive
conditional-Hankel cone after removing only the total-mass mode.

The exact necessary two-point determinant at the origin is

\[
\phi''(0)\phi''''(0)-\phi'''(0)^2
=\frac{19}{4}\frac{109}{16}-36
=-\frac{233}{64}<0.
\tag{R-26201.2}
\]

The zero-mass qualifier does not repair this: the finite-difference argument of
`L-26001` shows that conditional positivity on every zero-mass measure would
force positivity of the derivative Hankel kernel. Therefore the middle line of
the frozen identity `L-23603.15` is false.

This refutation is narrow. It does not prove that the carry profile is negative.
It proves that the displayed kernel representation cannot establish its sign.

## 2. Exact derivative formula

For every integer `r>=0`,

\[
\boxed{
\phi^{(r)}(t)
=8e^t-2^{-r}e^{t/2}
 \left(7+3r+\frac32t\right).}
\tag{R-26201.3}
\]

Let `nu` be a finite complex measure and put

\[
A(\nu)=\int e^{x/2}\,d\nu(x),
\quad
B(\nu)=\int x e^{x/2}\,d\nu(x),
\quad
C(\nu)=\int e^x\,d\nu(x).
\tag{R-26201.4}
\]

Direct expansion gives the exact quadratic form

\[
\boxed{
\begin{aligned}
Q_r(\nu)
&=\iint\phi^{(r)}(x+y)\,d\nu(x)d\overline{\nu(y)}\\
&=8|C(\nu)|^2
-2^{-r}\left[
 (7+3r)|A(\nu)|^2
 +3\operatorname{Re}\bigl(B(\nu)\overline{A(\nu)}\bigr)
 \right].
\end{aligned}}
\tag{R-26201.5}
\]

Thus the complete indefinite part is an explicit two-jet in the weighted
half-pole moments `(A,B)`.

## 3. Correct positive cone

On the source-specific subspace

\[
\boxed{A(\nu)=0,}
\tag{R-26201.6}
\]

the indefinite jet vanishes identically and

\[
\boxed{Q_r(\nu)=8|C(\nu)|^2\ge0.}
\tag{R-26201.7}
\]

This is an exact rank-one Gram identity. It is strictly narrower than ordinary
zero-mass conditional positivity. It is also the natural null condition for the
half-pole model in the safe-window and high-order Euler programmes.

## 4. Weighted translation difference

Let `tau_a` translate a measure to the right by `a>0`, and define

\[
\boxed{D_a=I-e^{-a/2}\tau_a.}
\tag{R-26201.8}
\]

Then

\[
A(D_a\nu)
=A(\nu)-e^{-a/2}e^{a/2}A(\nu)=0.
\tag{R-26201.9}
\]

Therefore every completed weighted pair `D_a nu` lies in the exact positive cone
(R-26201.6). For `a=log 2`, the factor is `2^{-1/2}` and agrees exactly with
translation of the normalized coefficient `mu(n)/sqrt(n)` from `n` to `2n`.

## 5. Replacement discipline

Any new carry proof may use (R-26201.7) only after it has emitted a complete
pairing certificate proving (R-26201.9). Unpaired support collars must be exported
as boundary jets `(A,B)` and paid by a separate source-specific theorem.

Forbidden replacements include:

- total mass zero in place of half-pole mass zero;
- cellwise derivative signs in place of a Hankel Gram;
- deleting the boundary collar;
- absorbing the collar into a generic norm;
- treating the determinant `-233/64` as a numerical conditioning issue.

## 6. Status boundary

Closed exactly:

- refutation of the frozen conditional-Hankel mechanism;
- the all-order quadratic formula (R-26201.5);
- positivity on the half-pole-null subspace;
- the weighted-pair construction.

Open:

- domination of the exported boundary jets;
- positivity of the carry profile;
- RH.
