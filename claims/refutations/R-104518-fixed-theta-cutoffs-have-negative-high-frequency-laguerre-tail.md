# R-104518 — Every fixed theta-orbit cutoff has a negative high-frequency Laguerre tail

Claim ID: `R-104518`  
Status: **EXACT REFUTATION OF FIXED-CUTOFF COFINAL CERTIFICATION**  
Created: 2026-08-23  
Depends on: `L-104531--L-104533`  
RH status: **unproved**

Let

\[
G_N(u)=\sum_{n\le N}g_n(u),
\qquad
F_N(t)=\widehat G_N(t),
\]

where the individual positive theta orbits `g_n` are defined using `|u|` in
`L-104531`.

The complete sum `g=u^2 Phi` is smooth and even.  A finite orbit sum is only
`C^2` at the modular fixed point: the missing theta tail is exactly what
cancels its third-order cusp.

## 1. The uncancelled cusp coefficient is strictly positive

For `u>=0`,

\[
g_n(u)=u^2n^{-1/2}\phi(u+\log n).
\]

Hence

\[
G_N'''(0+)
=6\sum_{n\le N}n^{-1/2}\phi'(\log n)
=:J_N.
\tag{R-104518.1}
\]

Since the complete function is smooth and even,

\[
\sum_{n\ge1}n^{-1/2}\phi'(\log n)=0.
\tag{R-104518.2}
\]

For `v=log n` put `x=pi n^2`.  The explicit theta profile gives

\[
\frac{\phi'(v)}{\phi(v)}
=\frac52+\frac{4x}{2x-3}-2x.
\tag{R-104518.3}
\]

For every `n>=2`, `x>=4 pi`, and the right side is strictly negative. Thus the
omitted tail in (R-104518.2) is negative and

\[
\boxed{J_N>0\qquad(N>=1).}
\tag{R-104518.4}
\]

## 2. Exact Fourier asymptotics

On the positive half-line, `G_N` is smooth with rapidly decreasing
derivatives. Repeated integration by parts, retaining the right third
boundary jet, gives

\[
\boxed{
F_N(t)=\frac{2J_N}{t^4}+O_N(t^{-6}),
}
\tag{R-104518.5}
\]

\[
\boxed{
F_N'(t)=-\frac{8J_N}{t^5}+O_N(t^{-7}),
\qquad
F_N''(t)=\frac{40J_N}{t^6}+O_N(t^{-8}).
}
\tag{R-104518.6}
\]

Consequently the finite-cutoff Laguerre profile satisfies

\[
\boxed{
(F_N')^2-F_NF_N''
=-\frac{16J_N^2}{t^{10}}+O_N(t^{-12}).
}
\tag{R-104518.7}
\]

It is therefore strictly negative for all sufficiently large `|t|`.

## 3. Verdict

For every fixed `N`,

```text
min_(|t|<=T) [(F_N')^2-F_N F_N''] > 0
```

fails once `T` is large enough.  Hence no cofinal proof may freeze one finite
theta-orbit cutoff and send the physical height to infinity.

This does **not** refute positivity of the complete profile. It proves that the
finite orbit decomposition destroys a modular cancellation which is essential
at high frequency.

Every valid cofinal certification must therefore use at least one of:

```text
an orbit cutoff N=N(T) tending to infinity;
a jet-renormalized cutoff that restores the missing modular jets;
direct evaluation of the complete carrier-subtracted Jacobi mother.
```

The fixed-`N` version of the cofinal-margin lane is permanently closed.