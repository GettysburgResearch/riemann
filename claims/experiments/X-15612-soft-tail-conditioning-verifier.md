# X-15612 — Exact soft-tail conditioning verifier

Claim ID: `X-15612`  
Title: Fraction-only replay of the regularized exact-frame and soft-tail absorption theorem  
Status: `EXACT FINITE RATIONAL REGRESSION`  
Authoring agent: `gpt56-08`  
Created: 2026-08-01  
Dependencies: `L-15630`

## Retained control

The exact diagonal Grams are

\[
G=I_4,
\]

\[
D=\operatorname{diag}\left(
\frac1{10000},\frac1{100},1,4
\right),
\]

and

\[
K=9I_4.
\]

Take

\[
M=3,
\qquad
\ell=4,
\qquad
\tau=\frac1{16},
\qquad
B=12.
\]

Coordinate \(0\) is the retained core. On the residual space, the soft sector is
coordinate \(1\), while coordinates \(2,3\) form the complete dangerous
complement.

The checker verifies exactly:

\[
K\preceq M^2G,
\]

\[
K\preceq B^2(D+\tau G),
\]

\[
D|_{\rm soft}\preceq\tau G,
\]

and

\[
D|_{\rm dang}\succeq\tau G,
\qquad
K|_{\rm dang}\preceq B^2D|_{\rm dang}.
\]

It also checks the exact source identity

\[
{\cal L}F=I_4.
\]

## Retained output

```text
core indices                   [0]
soft indices                   [1]
dangerous complement indices   [2,3]
tau                            1/16
declared B                     12
actual dangerous B^2           9
dangerous profile floor        1
soft profile trace             1/100
verdict                        PASS_EXACT_L15630_CONDITIONING_SPLIT
```

Certificate SHA-256:

```text
837e501cff446d233a9fea0651092e36b3a40217d2357abf76e2f4293f3f2be5
```

## Scope

The regression verifies only the exact finite conditioning algebra. It does not
verify the production Fourier--Mellin graph bound, a Suzuki radial primitive,
or an RH conclusion.
