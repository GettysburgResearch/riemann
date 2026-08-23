# L-104533 — Exponential theta tail and compact-height certification

Claim ID: `L-104533`  
Status: **PROVED EXACT ESTIMATE**  
Created: 2026-08-23  
Depends on: `L-104531`, `L-104532`  
RH status: **not assumed**

For `j>=0` put

\[
M_{n,j}=\int_{\mathbb R}|u|^j g_n(u)\,du.
\]

Using `r=ne^u` on `u>=0`, the explicit orbit formula of `L-104531` gives, for every fixed `J`,

\[
\boxed{
M_{n,j}\le C_J n^{J+4}e^{-\pi n^2}
\qquad(0\le j\le J).
}
\tag{L-104533.1}
\]

The exponent of `n` is deliberately nonoptimal; the Gaussian theta tail is the controlling fact.

Since

\[
|F_n^{(j)}(t)|\le M_{n,j},
\]

one obtains the uniform mixed-tail estimate

\[
\boxed{
\sup_{t\in\mathbb R}
\sum_{\max(m,n)>N}|\mathcal T_{mn}(t)|
\le C N^{C}e^{-\pi N^2}.
}
\tag{L-104533.2}
\]

Here `C` is an absolute effective constant after fixing the derivative orders `0,1,2` appearing in `T_mn`.

## Fail-closed compact-height certification

Define

\[
\Lambda_N(t)=\mathbf1_N^T\mathbf T_N(t)\mathbf1_N.
\]

If a directed finite proof establishes

\[
\mu_{N,T}=\min_{|t|\le T}\Lambda_N(t)>0
\]

and the explicit tail in (L-104533.2) is smaller than `mu_(N,T)`, then

\[
\boxed{
\Xi'''(t)^2-\Xi''(t)\Xi''''(t)>0
\qquad(|t|\le T).
}
\tag{L-104533.3}
\]

This provides an exact finite route for any prescribed height.  It does not prove the asymptotic fixed-order transfer: the finite-block margin may shrink with `T`, and the full modular cancellation cannot be replaced by one fixed orbit cutoff.

Accordingly, a global proof must supply either

```text
uniform mixed-orbit Schur domination;
cofinal directed margins beating the explicit theta tail;
or a direct modular identity for the complete infinite matrix.
```

No finite scan is promoted to an asymptotic theorem.