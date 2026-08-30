# L-104525 — Conrey's fixed-order Xi-derivative line proportions

Claim ID: `L-104525`  
Status: **IMPORTED UNCONDITIONAL THEOREM / HISTORICAL EXACTIFICATION**  
Created: 2026-08-23  
RH status: **not assumed**

## Convention

Let `N_m(T+U)-N_m(T)` count the zeros of `xi^(m)` on the critical line in the
short interval from height `T` to `T+U`, with

\[
U=T L^{-10},
\qquad
L=\log(T/(2\pi)).
\]

Conrey normalizes by the expected complete zero count

\[
{1\over2\pi}UL
\]

and defines

\[
\alpha_m
=
\liminf_{T\to\infty}
{N_m(T+U)-N_m(T)\over (2\pi)^{-1}UL}.
\]

## Fixed-order bounds

Conrey's 1983 theorem gives the explicit table

\[
\boxed{
\begin{aligned}
\alpha_0&>0.3658,\\
\alpha_1&>0.8137,\\
\alpha_2&>0.9584,\\
\alpha_3&>0.9873,\\
\alpha_4&>0.9948,\\
\alpha_5&>0.9970,
\end{aligned}}
\]

and in general

\[
\alpha_m=1+O(m^{-2}).
\]

The primary publication is:

```text
J. B. Conrey,
Zeros of derivatives of Riemann's xi-function on the critical line,
Journal of Number Theory 16 (1983), 49–74,
DOI 10.1016/0022-314X(83)90031-8.
```

## Direct answer for the second derivative

The theorem already proves

\[
\boxed{\alpha_2>0.9584.}
\]

Thus the unconditional numerical lower bound for the critical-line proportion
of `xi''` is **95.84%** in the stated convention.

The familiar claim “more than 99% for `xi'''`” should not be frozen literally:
the explicit table gives

\[
\boxed{\alpha_3>0.9873,}
\]

namely **98.73%**.  It is close to 99%, but below it.

## Scope firewall

The `alpha_2` and `alpha_3` rows are two independently proved outputs of
Conrey's mollified derivative method.  The table does not establish a logical
reverse-Rolle implication

\[
\alpha_3\ge p\Longrightarrow\alpha_2\ge C(p).
\]

`R-104514` proves that no such implication can depend on `p` alone in the
ambient real Cartwright class.
